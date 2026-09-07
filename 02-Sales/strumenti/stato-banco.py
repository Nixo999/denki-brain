#!/usr/bin/env python3
"""Stato del banco DM, per account. Lo lancia /patrick come prima cosa.

Legge quello che sanno i CSV pubblicati: quante righe restano, quante sono
partite oggi, quali recuperi sono maturi. ATTENZIONE: il conto vero degli
invii vive nel browser di Patrick (localStorage), non qui. Questo dice cosa
c'e` pubblicato e cosa il banco trovera` aprendosi, non quanti DM ha mandato
davvero oggi.
"""
import csv, datetime, pathlib, re, sys

QUI = pathlib.Path(__file__).resolve().parent
ATTESA = 4          # giorni lavorativi prima del recupero, come nel banco
OGGI = datetime.date.today()

# i tetti stanno nel banco: leggerli di la` evita che i due numeri divergano
sorgente = (QUI / "banco-dm.html").read_text(encoding="utf-8")
TETTI = dict(re.findall(r'(\w+):\s*\{[^}]*?tetto:\s*(\d+)', sorgente))

ACCOUNT = [("Patrick Sappa", "lista-corrente.csv"), ("DenkiCode", "lista-denkicode.csv")]


def lavorativi_da(iso):
    try:
        d = datetime.date.fromisoformat(iso)
    except ValueError:
        return 0
    # stesso conteggio del banco: dal giorno dell'invio a ieri, weekend esclusi
    return sum(1 for n in range((OGGI - d).days)
               if (d + datetime.timedelta(days=n)).weekday() < 5)


def stato(nome, file, chiave):
    p = QUI / file
    if not p.exists():
        return f"{nome}: nessuna lista pubblicata ({file} non c'e')"
    righe = list(csv.DictReader(p.open(encoding="utf-8")))
    inv = "DM inviato (data)"
    da_mandare = sum(1 for r in righe if not (r.get(inv) or "").strip()
                     and not re.match(r"scartat", (r.get("Esito DM") or "").strip(), re.I))
    oggi = sum(1 for r in righe if (r.get(inv) or "").strip() == OGGI.isoformat())
    recuperi = sum(1 for r in righe if (r.get(inv) or "").strip()
                   and not (r.get("Esito DM") or "").strip()
                   and lavorativi_da(r[inv].strip()) >= ATTESA)
    tetto = TETTI.get(chiave, "?")
    return (f"{nome}: {da_mandare} da mandare, {oggi} partiti oggi (tetto {tetto}), "
            f"{recuperi} recuperi maturi — {len(righe)} righe in {file}")


print(f"Banco DM, {OGGI.isoformat()}")
for (nome, file), chiave in zip(ACCOUNT, ("patrick", "denkicode")):
    print(" ", stato(nome, file, chiave))
