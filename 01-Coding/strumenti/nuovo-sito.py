#!/usr/bin/env python3
"""Crea un sito nuovo dallo starter, con git gia' inizializzato.

    python3 01-Coding/strumenti/nuovo-sito.py da-caterina

Fa una cosa sola: copiare. Il sito lo progetta chi lo progetta — lo starter
porta solo le trappole gia' pagate, mai il gusto. Vedi starter-sito/LEGGIMI.md.
"""
import shutil, subprocess, sys
from pathlib import Path

STARTER = Path(__file__).resolve().parent / "starter-sito"
LAVORO = Path.home() / "lavoro"


def main(nome):
    dest = LAVORO / (nome if nome.endswith("-site") else f"{nome}-site")
    if dest.exists():
        sys.exit(f"esiste gia': {dest}")
    shutil.copytree(STARTER, dest, ignore=shutil.ignore_patterns("LEGGIMI.md"))
    (dest / "assets" / "img").mkdir(exist_ok=True)
    (dest / "assets" / "stile.css").write_text(
        "/* Il sito vive qui. base.css porta solo l'idraulica: colori, font,\n"
        "   griglia e sezioni nascono dall'essenza del cliente. */\n", encoding="utf-8")
    subprocess.run(["git", "init", "-q"], cwd=dest, check=True)
    subprocess.run(["git", "add", "-A"], cwd=dest, check=True)
    subprocess.run(["git", "commit", "-q", "-m",
                    f"Starter DenkiCode per {nome}: reset, sbarramenti, firma, boot motion"],
                   cwd=dest, check=True)
    print(f"{dest}\n  → tre sbarramenti attivi, firma nel footer, stile.css vuoto")
    print("  → adesso: essenza del cliente, poi il brief, poi l'operatore")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1].strip("/"))
