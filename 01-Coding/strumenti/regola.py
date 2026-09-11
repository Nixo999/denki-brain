#!/usr/bin/env python3
"""Scrive **subito** una regola nuova nel file dove verra' riletta.

    python3 01-Coding/strumenti/regola.py siti "Sui siti voglio sempre X" --chi nicola
    python3 01-Coding/strumenti/regola.py --dove            # elenca le destinazioni

Esiste perche' il meccanismo delle direttive era agganciato alla **bocciatura**
e alla fine della sessione: «quando una bozza viene bocciata, /chiudi-sessione
chiede la frase esatta». Una preferenza detta a meta' sessione, senza niente da
bocciare, non scattava. Detto l'11 settembre 2026 da Nicola: «da adesso deve
diventare sempre piu' intelligente e completo, mai stupido».

Tre proprieta', e sono il punto:
- **subito**, non a fine sessione: una regola detta e non scritta e' persa;
- **nel file giusto**, non in un raccoglitore: una regola sui siti fra le
  convenzioni dei commit non la legge nessuno;
- **verbatim**: la frase di chi l'ha detta non si riassume e non si ammorbidisce.

I file crescono e non si accorciano. Una regola superata si marca superata,
non si cancella: serve sapere che c'e' stata.
"""
import subprocess
import sys
from datetime import date
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]

DOVE = {
    "siti":        ("01-Coding/stack/direttive-siti.md", "Design, motion, copy e direzione di un sito vetrina"),
    "voce":        ("02-Sales/processo/stile-comunicazione.md", "Come si scrive a un cliente o a un lead"),
    "codice":      ("01-Coding/stack/convenzioni.md", "Convenzioni tecniche: naming, commit, struttura"),
    "liste":       ("02-Sales/liste/metodo-liste.md", "Come si costruisce e si verifica una lista"),
    "registro":    ("03-Storage/azienda/registro-trevis.md", "Come Trevis parla a Nicola, Patrick e Giulia"),
    "prezzi":      ("02-Sales/processo/prodotti-e-listino.md", "Prezzi, pacchetti, cosa si vende"),
    "vault":       ("03-Storage/sistemi/come-si-scrive-una-nota.md", "Come si scrive e si marca una nota"),
    "azienda":     ("03-Storage/azienda/protocollo-trevis.md", "Vincoli e postura che valgono ovunque"),
}


def scrivi(chiave, testo, chi, perche):
    via, _ = DOVE[chiave]
    p = VAULT / via
    if not p.exists():
        sys.exit(f"manca {via}: la regola non si scrive in un file che non c'e'")

    oggi = date.today().strftime("%d/%m/%Y")
    blocco = f"\n### {oggi} — {chi}: «{testo.strip()}»\n\n"
    blocco += (perche.strip() + "\n") if perche else (
        "Regola detta e non ancora spiegata: vale comunque. Il perche' si aggiunge "
        "quando si sa, non si aspetta per scriverla.\n")

    t = p.read_text(encoding="utf-8")
    # va in cima all'elenco delle regole, se il file ne ha uno: la piu' recente per prima
    ancora = next((a for a in ("## Le direttive, dalla più recente", "## Le direttive",
                               "## Regole", "## Collegamenti") if a in t), None)
    if ancora == "## Collegamenti" or ancora is None:
        # nessun elenco: si accoda una sezione propria prima dei collegamenti
        testa = "\n## Regole date a voce\n\nScritte da `regola.py` nel momento in cui sono state dette.\n"
        i = t.index("## Collegamenti") if "## Collegamenti" in t else len(t)
        t = t[:i] + testa + blocco + "\n" + t[i:]
    else:
        i = t.index(ancora) + len(ancora)
        t = t[:i] + "\n" + blocco + t[i:]

    import re
    t = re.sub(r"^updated: .*$", "updated: " + date.today().isoformat(), t, count=1, flags=__import__("re").M)
    p.write_text(t, encoding="utf-8")
    return p


def committa(p, testo, chi):
    r = subprocess.run(["git", "-C", str(VAULT), "add", str(p)], capture_output=True)
    if r.returncode:
        return False
    msg = f"Regola nuova di {chi}: {testo.strip()[:60]}"
    corpo = ("Scritta da regola.py nel momento in cui e' stata detta, non a fine "
             "sessione: una regola detta e non scritta e' persa.")
    subprocess.run(["git", "-C", str(VAULT), "commit", "-q", "-m", msg, "-m", corpo],
                   capture_output=True)
    return True


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or "--dove" in a or a[0] in ("-h", "--help"):
        print(__doc__)
        print("Destinazioni:\n")
        for k, (via, cosa) in DOVE.items():
            print(f"  {k:<10} {cosa}\n             → {via}")
        sys.exit(0)
    if len(a) < 2 or a[0] not in DOVE:
        sys.exit(f"uso: regola.py <{'|'.join(DOVE)}> \"la frase\" [--chi nome] [--perche \"...\"]")

    chiave, testo = a[0], a[1]
    chi = a[a.index("--chi") + 1] if "--chi" in a else "Nicola"
    perche = a[a.index("--perche") + 1] if "--perche" in a else ""
    p = scrivi(chiave, testo, chi.capitalize(), perche)
    ok = committa(p, testo, chi.capitalize())
    print(f"scritta in {p.relative_to(VAULT)}" + ("" if ok else "  ⚠️ non committata"))
