#!/usr/bin/env python3
"""Da un profilo Instagram letto nel browser dell'app, la scheda cliente fissa da cui parte un sito.

    python3 01-Coding/strumenti/raccogli-instagram.py <utente>
    python3 01-Coding/strumenti/raccogli-instagram.py <utente> --cartella ~/lavoro/raccolte/<utente>

Lavora sulla cartella ~/lavoro/raccolte/<utente>/ (fuori dal vault: le foto non vanno su GitHub). Dentro
`grezzo/` ci sono i JSON restituiti da raccogli-instagram.js, uno per pagina: `profilo.json` e un
`<codice>.json` per ogni post aperto. Lo script:

1. scarica le foto a taglia piena con urllib (gli URL firmati scadono: si lancia nella stessa sessione);
2. le misura con sips e scarta tutto sotto i 1080 px di lato lungo, i file finti da 22 byte e i fotogrammi dei
   Reel (lo dice il tag `efg` dell'URL, non il nome);
3. converte le WebP in JPEG, sempre con sips;
4. campiona i colori della foto profilo, che di solito e' il logo (Pillow; senza Pillow lo dichiara);
5. cerca prezzi, orari, recensioni e contatti in bio, didascalie e titoli delle storie in evidenza, e
   scrive cosa manca invece di lasciarlo indovinare a chi costruisce;
6. scrive `scheda.md` (da leggere) e `scheda.json` (da usare), sempre con le stesse sezioni.

Esce 1 se le foto buone sono meno di MIN_FOTO_BUONE: il sito non puo' dipendere da Instagram, e chi lo
costruisce deve saperlo prima della direzione, non dopo. Nato il 31/10/2026 dalla pipeline dei siti.
"""
import base64
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

MIN_LATO = 1080
MIN_FOTO_BUONE = 6
RACCOLTE = Path.home() / "lavoro" / "raccolte"

# cosa si cerca nei testi. Ogni voce: le espressioni che la trovano. Se nessuna trova, la voce «manca».
CERCA = {
    "prezzi": [r"\d+[.,]?\d*\s?(?:€|euro)\b", r"€\s?\d+", r"\bprezz", r"\blistino\b", r"\btariff"],
    "orari": [r"\b\d{1,2}[:.]\d{2}\s?[-–]\s?\d{1,2}[:.]\d{2}", r"\borari", r"\baperti\b", r"\bchiuso il\b",
              r"\b(?:lun|mar|mer|gio|ven|sab|dom)[a-z]*\s?[-–]\s?(?:lun|mar|mer|gio|ven|sab|dom)"],
    "recensioni": [r"recension", r"\bstelle\b", r"⭐", r"\bgoogle\b", r"\btripadvisor\b", r"\bfeedback\b"],
    "telefono": [r"(?:\+39\s?)?3\d{2}[\s.]?\d{3}[\s.]?\d{3,4}", r"(?:\+39\s?)?0\d{1,3}[\s.]?\d{5,8}", r"wa\.me/"],
    "email": [r"[\w.+-]+@[\w-]+\.[a-z]{2,}"],
    "indirizzo": [r"\b(?:via|viale|piazza|corso|largo|vicolo|p\.za|v\.le)\s+[A-ZÀ-Ü]", r"📍"],
    "prenotazione": [r"prenot", r"\bbooking\b", r"\bappuntament", r"\btreatwell\b", r"\bfresha\b"],
}


def tag_efg(url):
    """Il tag di encoding di Instagram, base64 nel parametro efg: dice se e' una foto o un fotogramma di Reel."""
    v = urllib.parse.parse_qs(urllib.parse.urlparse(url).query).get("efg", [""])[0]
    try:
        return base64.b64decode(v + "=" * (-len(v) % 4)).decode("utf-8", "replace")
    except Exception:
        return ""


def sips(percorso, *chiavi):
    args = [a for k in chiavi for a in ("-g", k)]     # sips vuole un -g per ogni chiave
    out = subprocess.run(["sips", *args, str(percorso)], capture_output=True, text=True).stdout
    return {k: v for k, v in re.findall(r"^\s+(\w+): (.+)$", out, re.M)}


def scarica(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        dest.write_bytes(r.read())


def colori(percorso, quanti=6):
    """I colori principali dell'immagine, con la quota. Esclude la cornice bianca del cerchio profilo."""
    try:
        from PIL import Image
    except ImportError:
        return None
    img = Image.open(percorso).convert("RGB").resize((120, 120))
    px = [p for p in img.getdata()]
    q = Image.new("RGB", (len(px), 1))
    q.putdata(px)
    pal = q.quantize(colors=quanti, method=Image.Quantize.MEDIANCUT)
    conta = Counter(pal.getdata())
    rgb = pal.getpalette()
    tot = sum(conta.values())
    # fonde i colori quasi uguali (due bianchi, due neri): distanza RGB sotto 40
    fusi = []
    for i, n in conta.most_common():
        c = tuple(rgb[i * 3:i * 3 + 3])
        vicino = next((f for f in fusi if sum((a - b) ** 2 for a, b in zip(f["rgb"], c)) < 1600), None)
        if vicino:
            vicino["n"] += n
        else:
            fusi.append({"rgb": c, "n": n})
    return [{"hex": "#%02x%02x%02x" % f["rgb"], "quota": round(f["n"] / tot, 2)}
            for f in sorted(fusi, key=lambda f: -f["n"])]


def leggi_grezzo(cartella):
    g = cartella / "grezzo"
    if not g.is_dir():
        sys.exit(f"manca {g}: dentro vanno i JSON di raccogli-instagram.js (profilo.json e uno per post)")
    profilo, post = None, []
    for f in sorted(g.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        if isinstance(d, str):          # javascript_tool restituisce la stringa JSON, a volte salvata con le virgolette
            d = json.loads(d)
        if d.get("pagina") == "profilo":
            profilo = d
        elif d.get("pagina") == "post":
            post.append(d)
    if not profilo:
        sys.exit(f"manca il profilo in {g}: apri instagram.com/<utente>/ e salva l'esito come profilo.json")
    return profilo, post


def raccogli_foto(cartella, post, griglia):
    dir_foto = cartella / "foto"
    dir_foto.mkdir(exist_ok=True)
    buone, scartate = [], []
    ordine = {p["codice"]: i for i, p in enumerate(griglia)}
    for p in sorted(post, key=lambda p: ordine.get(p["codice"], 99)):
        for n, url in enumerate(p.get("immagini", []), 1):
            tag = tag_efg(url)
            nome = f"{p['codice']}-{n}"
            if "regular_photo" not in tag:
                scartate.append((nome, "non e' una foto (fotogramma di Reel o anteprima)"))
                continue
            grezza = dir_foto / f"{nome}.scaricata"
            try:
                scarica(url, grezza)
            except Exception as e:
                scartate.append((nome, f"scaricamento fallito ({e}): URL scaduto o copiato male"))
                continue
            if grezza.stat().st_size < 2000:
                scartate.append((nome, f"file finto da {grezza.stat().st_size} byte: firma dell'URL rotta"))
                grezza.unlink()
                continue
            jpg = dir_foto / f"{nome}.jpg"
            subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "90", str(grezza),
                            "--out", str(jpg)], capture_output=True)
            grezza.unlink()
            m = sips(jpg, "pixelWidth", "pixelHeight")
            w, h = int(m.get("pixelWidth", 0)), int(m.get("pixelHeight", 0))
            if max(w, h) < MIN_LATO:
                scartate.append((nome, f"{w}x{h}, sotto i {MIN_LATO} px"))
                jpg.unlink()
                continue
            buone.append({"file": f"foto/{jpg.name}", "w": w, "h": h, "post": p["codice"],
                          "orientamento": "verticale" if h > w * 1.05 else "orizzontale" if w > h * 1.05 else "quadrata",
                          "didascalia": p.get("didascalia", "")[:160]})
    return buone, scartate


def cerca_mancanti(testi):
    trovati = {}
    for voce, regex in CERCA.items():
        trovati[voce] = []
        for fonte, t in testi:
            for r in regex:
                for m in re.finditer(r, t, re.I):
                    a, b = max(0, m.start() - 40), min(len(t), m.end() + 40)
                    trovati[voce].append({"fonte": fonte, "estratto": t[a:b].replace("\n", " ").strip()})
                    break
        # tieni al massimo tre estratti per voce, da fonti diverse se ci sono
        visti, tenuti = set(), []
        for x in trovati[voce]:
            if x["fonte"] not in visti:
                visti.add(x["fonte"])
                tenuti.append(x)
        trovati[voce] = tenuti[:3]
    return trovati


def scrivi_scheda(cartella, profilo, post, buone, scartate, palette, trovati):
    griglia = profilo.get("post", [])
    reel = sum(1 for p in griglia if p["tipo"] == "reel")
    altrui = [p for p in griglia if p.get("di") and p["di"] != profilo["utente"]]
    mancano = [v for v, x in trovati.items() if not x]
    scheda = {"utente": profilo["utente"], "titolo": profilo.get("titolo", ""), "bio": profilo.get("bio", ""),
              "follower": profilo.get("follower", ""), "post_totali": profilo.get("post_totali", ""),
              "link": profilo.get("link", []), "evidenza": profilo.get("evidenza", []),
              "griglia": {"post": len(griglia), "reel": reel, "di_altri": len(altrui)},
              "foto": buone, "scartate": [{"nome": n, "motivo": m} for n, m in scartate],
              "palette_logo": palette, "trovati": trovati, "mancano": mancano,
              "didascalie": [{"post": p["codice"], "data": p.get("data", ""), "testo": p.get("didascalia", "")} for p in post]}
    (cartella / "scheda.json").write_text(json.dumps(scheda, ensure_ascii=False, indent=2), encoding="utf-8")

    r = [f"# Scheda Instagram di @{profilo['utente']}", "",
         f"{profilo.get('titolo', '')}. {profilo.get('follower', '?')} follower, {profilo.get('post_totali', '?')} post.",
         "Raccolta senza login dal browser dell'app: vale per la data della cartella, gli URL delle foto scadono.", "",
         "## Bio", "", profilo.get("bio", "") or "(vuota)", ""]
    if profilo.get("link"):
        r += ["Link in bio: " + ", ".join(profilo["link"]), ""]
    r += ["## Storie in evidenza", "",
          ", ".join(profilo["evidenza"]) if profilo.get("evidenza") else "Nessuna, o non leggibile.",
          "Si leggono solo i titoli: il contenuto delle storie da sloggati non si apre.", ""]
    r += ["## Foto utilizzabili", "",
          f"{len(buone)} foto sopra i {MIN_LATO} px, da {len(post)} post aperti su {len(griglia)} in griglia "
          f"({reel} sono Reel, quindi niente foto; {len(altrui)} sono di altri profili).", ""]
    if buone:
        r += ["| File | Taglia | Forma | Didascalia |", "|---|---|---|---|"]
        for f in buone:
            r.append(f"| `{f['file']}` | {f['w']}x{f['h']} | {f['orientamento']} | {f['didascalia'][:70].replace('|', '/').replace(chr(10), ' ')} |")
        r.append("")
    if scartate:
        r += ["Scartate:", ""] + [f"- `{n}`: {m}" for n, m in scartate] + [""]
    if len(buone) < MIN_FOTO_BUONE:
        r += [f"**Le foto buone sono {len(buone)}, meno di {MIN_FOTO_BUONE}.** Il sito non puo' reggersi su Instagram: "
              "o si chiedono gli originali al cliente, o la direzione parte dalla tipografia e dal logo.", ""]
    r += ["## Colori della foto profilo", ""]
    if palette is None:
        r += ["Pillow non e' installato: colori non campionati (`pip3 install pillow`).", ""]
    else:
        r += ["Campionati dalla foto profilo, che di solito e' il logo. Se e' una foto di persona, non valgono come palette.", ""]
        r += [f"- `{c['hex']}` — {int(c['quota'] * 100)}%" for c in palette] + [""]
    r += ["## Cosa c'e' e cosa manca", ""]
    for voce, x in trovati.items():
        if x:
            r.append(f"- **{voce}**: " + " · ".join(f"«{e['estratto']}» ({e['fonte']})" for e in x))
        else:
            r.append(f"- **{voce}**: MANCA. Non si inventa: si chiede al cliente o la sezione non c'e'.")
    r += ["", "## Didascalie", ""]
    for p in post:
        r += [f"**{p['codice']}** ({p.get('data', '')})", "", (p.get("didascalia") or "(nessuna)").strip(), ""]
    (cartella / "scheda.md").write_text("\n".join(r), encoding="utf-8")
    return scheda


def main(argv):
    if not argv or argv[0].startswith("-"):
        sys.exit(__doc__)
    utente = argv[0].lstrip("@").strip("/")
    cartella = Path(argv[argv.index("--cartella") + 1]).expanduser() if "--cartella" in argv else RACCOLTE / utente
    profilo, post = leggi_grezzo(cartella)
    buone, scartate = raccogli_foto(cartella, post, profilo.get("post", []))

    palette = None
    if profilo.get("foto_profilo"):
        logo = cartella / "foto-profilo.jpg"
        try:
            scarica(profilo["foto_profilo"], cartella / "foto-profilo.scaricata")
            subprocess.run(["sips", "-s", "format", "jpeg", str(cartella / "foto-profilo.scaricata"), "--out", str(logo)],
                           capture_output=True)
            (cartella / "foto-profilo.scaricata").unlink()
            palette = colori(logo)
        except Exception as e:
            print(f"foto profilo non scaricata ({e})")

    testi = [("bio", profilo.get("bio", ""))] + [("evidenza", " ".join(profilo.get("evidenza", [])))]
    testi += [("link", " ".join(profilo.get("link", [])))]
    testi += [(f"post {p['codice']}", p.get("didascalia", "")) for p in post]
    trovati = cerca_mancanti(testi)
    s = scrivi_scheda(cartella, profilo, post, buone, scartate, palette, trovati)

    print(f"{cartella}/scheda.md")
    print(f"  foto buone {len(buone)} · scartate {len(scartate)} · post aperti {len(post)} su {len(profilo.get('post', []))}")
    print(f"  mancano: {', '.join(s['mancano']) or 'niente'}")
    if len(buone) < MIN_FOTO_BUONE:
        print(f"  BLOCCA: meno di {MIN_FOTO_BUONE} foto sopra i {MIN_LATO} px")
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
