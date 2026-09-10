#!/usr/bin/env python3
"""Riporta nei CSV del banco le date degli invii che stanno in liste/contattati.csv.

    python3 02-Sales/strumenti/allinea-contattati.py [--prova]

Il banco scrive ogni «Segna inviato» in `liste/contattati.csv` (lo fa il
server, subito) ma la data nella riga della lista resta nel localStorage del
browser di Patrick finche` lui non scarica il CSV aggiornato. Risultato: lo
stato del banco conta come «da mandare» gente gia` contattata, ed e` cosi` che
il 9 settembre 2026 Patrick ha riaperto dieci profili che aveva gia` scritto.

Questo script chiude il buco dal lato file: per ogni handle che risulta
contattato, se la riga in `lista-corrente.csv` (o `lista-denkicode.csv`) non ha
data, ci scrive quella dell'invio. Non tocca le righe che una data ce l'hanno
gia` e non cancella niente.
"""
import csv, sys
from pathlib import Path

QUI = Path(__file__).resolve().parent
SALES = QUI.parent
PROVA = "--prova" in sys.argv


def handle(s):
    return (s or "").strip().lstrip("@").lower()


def date_per_handle():
    p = SALES / "liste" / "contattati.csv"
    date = {}
    for r in csv.DictReader(p.open(encoding="utf-8")):
        h, d = handle(r.get("Account IG")), (r.get("Data") or "").strip()
        if h and len(d) == 10 and d[4] == "-":
            date[h] = min(date.get(h, d), d)     # la prima volta che gli si e` scritto
    return date


def allinea(p, date):
    if not p.exists():
        return 0
    righe = list(csv.DictReader(p.open(encoding="utf-8")))
    if not righe:
        return 0
    campi = list(righe[0].keys())
    col = next((c for c in campi if c.lower().startswith("dm inviato")), None)
    if not col:
        return 0
    n = 0
    for r in righe:
        d = date.get(handle(r.get("Account IG")))
        if d and not (r[col] or "").strip():
            r[col] = d
            n += 1
    if n and not PROVA:
        with p.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=campi, lineterminator="\n")
            w.writeheader()
            w.writerows(righe)
    return n


if __name__ == "__main__":
    date = date_per_handle()
    print(f"contattati.csv: {len(date)} handle con una data")
    for nome in ("lista-corrente.csv", "lista-denkicode.csv"):
        n = allinea(QUI / nome, date)
        print(f"  {nome}: {n} righe {'da allineare' if PROVA else 'allineate'}")
