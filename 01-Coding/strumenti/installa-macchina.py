#!/usr/bin/env python3
"""Installa in ~/.claude/ i file che git non porta, dalle copie canoniche del vault.

    python3 01-Coding/strumenti/installa-macchina.py           # scrive
    python3 01-Coding/strumenti/installa-macchina.py --check   # dice e basta, esce 1 se serve

`~/.claude/` e' locale alla macchina e fuori da git: protocollo, agenti, comandi
e skill nostre vivono li'. Le copie canoniche stanno nel vault e ci arrivano col
push, ma qualcuno deve portarle dentro. Finche' era un passaggio a mano restava
indietro, come la firma nel footer. Adesso e' un comando.

Non tocca niente di terze parti: plugin, skill di design e settings restano
come sono.
"""
import filecmp, shutil, sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
CLAUDE = Path.home() / ".claude"
MARK = "<!-- INIZIO FILE LOCALE"

# copia canonica nel vault -> dove va sulla macchina
CANONICHE = {
    "03-Storage/sistemi/claude-md-globale.md": "CLAUDE.md",
    "03-Storage/sistemi/agente-operatore.md": "agents/operatore.md",
}
# cartelle del vault ricopiate pari pari
CARTELLE = ["commands", "skills"]


def corpo(p):
    """Il file vero: quello che sta sotto il marcatore, senza l'involucro del vault."""
    t = p.read_text(encoding="utf-8")
    i = t.find(MARK)
    if i < 0:
        sys.exit(f"{p}: manca il marcatore «{MARK}...»")
    return t[t.index("\n", i) + 1:].lstrip("\n")


def scrivi(dest, testo, check, fatti):
    vecchio = dest.read_text(encoding="utf-8") if dest.exists() else None
    if vecchio == testo:
        return
    fatti.append(("aggiorna" if vecchio else "crea", dest))
    if not check:
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(testo, encoding="utf-8")


def main(check):
    fatti = []
    for sorgente, destinazione in CANONICHE.items():
        scrivi(CLAUDE / destinazione, corpo(VAULT / sorgente), check, fatti)

    for cartella in CARTELLE:
        radice = VAULT / ".claude" / cartella
        if not radice.is_dir():
            continue
        for p in radice.rglob("*.md"):
            scrivi(CLAUDE / cartella / p.relative_to(radice),
                   p.read_text(encoding="utf-8"), check, fatti)

    for azione, dest in fatti:
        print(f"{azione}: ~/{dest.relative_to(Path.home())}")
    if not fatti:
        print("~/.claude/ e' gia' allineato al vault")
        return 0
    print(f"\n{len(fatti)} file {'da aggiornare' if check else 'scritti'}")
    return 1 if check else 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
