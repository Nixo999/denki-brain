#!/usr/bin/env python3
"""Cerca nel vault per rilevanza, non per parola esatta.

    python3 01-Coding/strumenti/cerca.py cache telefono cliente
    python3 01-Coding/strumenti/cerca.py --tutto "prezzo sconto garanzia"

`grep` trova la parola che hai scritto. Questo prende piu' parole insieme, le
pesa e ordina le note per quanto ci somigliano: «cosa avevamo deciso sulla
cache» trova la nota che parla di Cache-Control anche se la parola «cache» ci
compare una volta sola in mezzo ad altro.

Usa FTS5, che sta dentro sqlite3 della libreria standard: nessuna installazione,
nessuna chiave, funziona identico sul Mac di Patrick. Non e' ricerca semantica
vera — per quella servirebbe un modello di embedding da scaricare — ma copre il
caso che rompeva grep, cioe' la domanda fatta con parole diverse da quelle
scritte nella nota.

L'indice sta in `.cache/`, e' fuori da git e si ricostruisce da solo quando i
file cambiano.
"""
import re
import sqlite3
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
DB = VAULT / ".cache" / "cerca.sqlite"
SALTA = {".git", ".cache", "node_modules"}


def note():
    for p in VAULT.rglob("*.md"):
        if SALTA & set(p.parts):
            continue
        yield p


def campi(testo):
    m = re.match(r"^---\n(.*?)\n---\n", testo, re.S)
    if not m:
        return {}, testo
    d = {}
    for r in m.group(1).splitlines():
        if ":" in r and not r.startswith(" "):
            k, _, v = r.partition(":")
            d[k.strip()] = v.strip()
    return d, testo[m.end():]


def apri():
    DB.parent.mkdir(exist_ok=True)
    c = sqlite3.connect(DB)
    c.execute("CREATE TABLE IF NOT EXISTS stato (via TEXT PRIMARY KEY, quando REAL)")
    c.execute("CREATE VIRTUAL TABLE IF NOT EXISTS note USING fts5("
              "via UNINDEXED, nome, riga, corpo, tokenize='unicode61 remove_diacritics 2')")
    return c


def aggiorna(c):
    vecchie = dict(c.execute("SELECT via, quando FROM stato"))
    viste, cambiate = set(), 0
    for p in note():
        via = str(p.relative_to(VAULT))
        viste.add(via)
        quando = p.stat().st_mtime
        if vecchie.get(via) == quando:
            continue
        testo = p.read_text(encoding="utf-8", errors="ignore")
        fm, corpo = campi(testo)
        c.execute("DELETE FROM note WHERE via = ?", (via,))
        c.execute("INSERT INTO note (via, nome, riga, corpo) VALUES (?,?,?,?)",
                  (via, p.stem.replace("-", " "), fm.get("riga", ""), corpo))
        c.execute("INSERT OR REPLACE INTO stato VALUES (?,?)", (via, quando))
        cambiate += 1
    for via in set(vecchie) - viste:
        c.execute("DELETE FROM note WHERE via = ?", (via,))
        c.execute("DELETE FROM stato WHERE via = ?", (via,))
    c.commit()
    return cambiate


def cerca(c, parole, quante):
    # OR fra le parole: chi ne contiene di piu', e nei campi che pesano, sale
    q = " OR ".join(f'"{p}"*' for p in parole if len(p) > 2)
    if not q:
        sys.exit("servono parole di almeno tre lettere")
    return c.execute(
        "SELECT via, riga, snippet(note, 3, '»', '«', ' … ', 18), "
        "bm25(note, 0, 6.0, 4.0, 1.0) AS punti "
        "FROM note WHERE note MATCH ? ORDER BY punti LIMIT ?", (q, quante)).fetchall()


def main(argv):
    quante = 30 if "--tutto" in argv else 8
    parole = [a.lower() for a in argv if not a.startswith("--")]
    if not parole:
        sys.exit(__doc__)
    c = apri()
    n = aggiorna(c)
    if n:
        print(f"({n} note reindicizzate)\n", file=sys.stderr)
    righe = cerca(c, parole, quante)
    if not righe:
        print("niente. Prova con meno parole, o guarda indice.md")
        return
    for via, riga, pezzo, _ in righe:
        print(f"\n{via}")
        if riga:
            print(f"   {riga}")
        print(f"   … {' '.join(pezzo.split())}")


if __name__ == "__main__":
    main(sys.argv[1:])
