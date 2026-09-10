#!/usr/bin/env python3
"""Rigenera indice.md dai file veri del vault e segnala i buchi.

    python3 01-Coding/strumenti/genera-indice.py            # riscrive indice.md
    python3 01-Coding/strumenti/genera-indice.py --check     # non scrive, esce 1 se serve

Esiste perche' l'indice a mano resta indietro: nessun comando lo scriveva, e un
indice vecchio fa concludere che una nota non esiste. La descrizione e' la prima
frase di prosa dopo il titolo, come dice indice.md da sempre.
"""
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]

SEZIONI = [
    ("00-Inbox", "Catture al volo, non ancora sistemate"),
    ("01-Coding", "Il lato tecnico: progetti, stack, strumenti, skill"),
    ("02-Sales", "Il lato commerciale: clienti, script, liste, processo"),
    ("03-Storage", "Azienda, team, sistemi"),
    ("05-Decisioni", "Una decisione per file, datata. Non si riscrivono"),
    ("06-Daily", "Note di giornata e handoff"),
    ("04-Archive", "Progetti chiusi e lead persi"),
    ("99-Templates", "Da copiare quando si crea una nota nuova"),
]

SALTA_PROSA = ("#", ">", "-", "|", "`", "!", "[!", "⬜", "✅")

# progetti fuori DenkiCode: stanno nel registro ma non devono avere una scheda
FUORI_VAULT = {"sito V-BAG"}


def note(cartella):
    return sorted(
        (VAULT / cartella).rglob("*.md"), key=lambda p: (str(p.parent), p.name)
    )


def testo(p):
    return p.read_text(encoding="utf-8")


def frontmatter(t):
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    if not m:
        return {}, t
    campi = {}
    for riga in m.group(1).splitlines():
        if ":" in riga and not riga.startswith(" "):
            k, _, v = riga.partition(":")
            campi[k.strip()] = v.strip()
    return campi, t[m.end():]


def descrizione(p):
    """La `riga:` del frontmatter. Indovinare dalla prosa e' il ripiego."""
    campi, corpo = frontmatter(testo(p))
    if campi.get("riga"):
        # scritta da una persona: si mostra intera, non si taglia alla prima frase
        return pulisci(campi["riga"])
    righe = corpo.splitlines()
    for i, r in enumerate(righe):
        if r.startswith("# "):
            righe = righe[i + 1:]
            break
    for i, r in enumerate(righe):
        s = r.strip()
        if not s or s.startswith(SALTA_PROSA) or (s.startswith("*") and not s.startswith("**")):
            continue
        # il paragrafo intero, non la singola riga: una frase spezzata su due
        # righe si legge male tanto quanto una tagliata a meta'
        par = [s]
        for succ in righe[i + 1:]:
            if not succ.strip():
                break
            par.append(succ.strip())
        return frase(" ".join(par))
    return "TODO — nessuna prosa dopo il titolo."


def pulisci(r):
    r = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", r)
    return re.sub(r"\[\[([^\]]+)\]\]", r"\1", r).replace("**", "").replace("`", "").strip()


def frase(r):
    r = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", r)
    r = re.sub(r"\[\[([^\]]+)\]\]", r"\1", r).replace("**", "").replace("`", "")
    # si accumula finche' la frase non dice qualcosa: «D.S.I.» non e' una frase
    pezzi, testa = re.split(r"(?<=[.!?])\s", r), ""
    for pezzo in pezzi:
        testa = (testa + " " + pezzo).strip()
        if len(testa) >= 40:
            break
    return testa if len(testa) <= 140 else testa[:140].rstrip() + "..."


def blocco(cartella):
    fuori, dentro = [], {}
    for p in note(cartella):
        campi, _ = frontmatter(testo(p))
        segno = "⚠️ " if campi.get("source") == "claude" and not campi.get("verificato") else ""
        voce = f"- [[{p.stem}]] — {segno}{descrizione(p)}"
        rel = p.parent.relative_to(VAULT / cartella)
        (fuori if rel == Path(".") else dentro.setdefault(str(rel), [])).append(voce)
    out = list(fuori)
    for sub in sorted(dentro):
        out += ["", f"**{sub}/**", ""] + dentro[sub]
    return out


def scrivi():
    tutte = sum(len(note(c)) for c, _ in SEZIONI)
    testa = (VAULT / "indice.md").read_text(encoding="utf-8").split("## 00-Inbox")[0]
    testa = re.sub(r"^updated: .*$", "updated: " + oggi(), testa, flags=re.M)
    testa = re.sub(r"Tutte le \*\*\d+ note\*\*", f"Tutte le **{tutte} note**", testa)
    righe = [testa.rstrip(), ""]
    for cartella, desc in SEZIONI:
        righe += [f"## {cartella}", "", f"*{desc}*", ""] + blocco(cartella) + [""]
    return "\n".join(righe).rstrip() + "\n"


def oggi():
    import datetime
    return datetime.date.today().isoformat()


def controlli():
    problemi = []

    esistenti = {p.stem for p in VAULT.rglob("*.md") if ".git" not in p.parts}
    rotti = {}
    for p in VAULT.rglob("*.md"):
        # i template e il README contengono segnaposto finti apposta
        if ".git" in p.parts or p.name in ("indice.md", "README.md") or "99-Templates" in p.parts:
            continue
        for link in re.findall(r"\[\[([^\]|#]+)", testo(p)):
            link = link.strip().rstrip("\\").split("\\|")[0].strip()
            if link and link not in esistenti:
                rotti.setdefault(link, []).append(p.stem)
    for link, dove in sorted(rotti.items(), key=lambda x: -len(x[1])):
        problemi.append(f"link rotto: [[{link}]] × {len(dove)} (es. {dove[0]})")

    claude = testo(VAULT / "CLAUDE.md")
    for p in note("01-Coding/progetti"):
        campi, _ = frontmatter(testo(p))
        if campi.get("type") != "progetto":
            continue
        if campi.get("status") != "completato" and f"[[{p.stem}]]" not in claude:
            problemi.append(f"progetto attivo fuori dalla tabella di CLAUDE.md: {p.stem}")

    senza_link = {}
    for riga in testo(VAULT / "01-Coding/registro-interventi.md").splitlines():
        celle = riga.split("|")
        cella = celle[3].strip() if len(celle) > 4 else ""
        # «— sistemi», «— commerciale»: interventi senza progetto, non sono buchi
        if len(celle) > 4 and "[[" not in celle[3] and not cella.startswith("—") and cella not in (
            "Progetto", "", "tutti"
        ) and not set(cella) <= set("-: "):
            nome = re.split(r"[(,]", celle[3].strip())[0].strip()[:40]
            if nome in FUORI_VAULT:
                continue
            senza_link[nome] = senza_link.get(nome, 0) + 1
    for nome, n in sorted(senza_link.items(), key=lambda x: -x[1]):
        problemi.append(f"registro: progetto senza wikilink × {n} → {nome}")

    import datetime
    limite = (datetime.date.today() - datetime.timedelta(days=30)).isoformat()
    senza_riga, ipotesi, scadute = [], [], []
    for cartella, _ in SEZIONI:
        for p in note(cartella):
            campi, _ = frontmatter(testo(p))
            rel = p.relative_to(VAULT)
            if "type" not in campi:
                problemi.append(f"frontmatter senza type: {rel}")
            if not campi.get("riga") and "99-Templates" not in p.parts:
                senza_riga.append(str(rel))
            if campi.get("source") == "claude":
                v = campi.get("verificato", "")
                if not v:
                    ipotesi.append(str(rel))
                elif v < limite and campi.get("type") in ("progetto", "cliente", "daily"):
                    scadute.append(f"{rel} ({v})")
    if senza_riga:
        problemi.append(f"`riga:` mancante × {len(senza_riga)} (es. {senza_riga[0]})")
    if ipotesi:
        problemi.append(
            f"source: claude senza `verificato:` × {len(ipotesi)} — sono ipotesi, "
            f"non fatti (es. {ipotesi[0]})"
        )
    for s in scadute:
        problemi.append(f"`verificato:` piu' vecchio di 30 giorni su una nota che cambia: {s}")
    return problemi


if __name__ == "__main__":
    nuovo = scrivi()
    vecchio = (VAULT / "indice.md").read_text(encoding="utf-8")
    check = "--check" in sys.argv
    if not check:
        (VAULT / "indice.md").write_text(nuovo, encoding="utf-8")
    for riga in controlli():
        print("⚠️ " + riga, file=sys.stderr)
    if nuovo != vecchio:
        print(("indice.md è indietro" if check else "indice.md riscritto"), file=sys.stderr)
        sys.exit(1 if check else 0)
    print("indice.md già allineato", file=sys.stderr)
