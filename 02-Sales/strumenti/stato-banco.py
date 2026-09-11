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

# il tetto giornaliero non esiste piu': tolto l'11/09/2026 su richiesta di
# Patrick, «togli il limite giornaliero». Qui restava solo per stamparlo.

ACCOUNT = [("Patrick Sappa", "lista-corrente.csv"), ("DenkiCode", "lista-denkicode.csv")]


def lavorativi_da(iso):
    try:
        d = datetime.date.fromisoformat(iso)
    except ValueError:
        return 0
    # stesso conteggio del banco: dal giorno dell'invio a ieri, weekend esclusi
    return sum(1 for n in range((OGGI - d).days)
               if (d + datetime.timedelta(days=n)).weekday() < 5)


def stato(nome, file):
    p = QUI / file
    if not p.exists():
        return f"{nome}: nessuna lista pubblicata ({file} non c'e')"
    righe = list(csv.DictReader(p.open(encoding="utf-8")))
    inv = "DM inviato (data)"
    da_mandare = sum(1 for r in righe if not (r.get(inv) or "").strip()
                     and not re.match(r"scartat", (r.get("Esito DM") or "").strip(), re.I))
    oggi = sum(1 for r in righe if (r.get(inv) or "").strip() == OGGI.isoformat())
    # dall'11/09/2026 il banco scrive la data del secondo messaggio in
    # «Recupero (data)»: una riga recuperata non e` piu` un recupero maturo, o
    # i due conti dicono numeri diversi sullo stesso file
    rec = next((c for c in righe[0] if c.lower().startswith("recupero")), None) if righe else None
    recuperi = sum(1 for r in righe if (r.get(inv) or "").strip()
                   and not (r.get("Esito DM") or "").strip()
                   and not (rec and (r.get(rec) or "").strip())
                   and lavorativi_da(r[inv].strip()) >= ATTESA)
    return (f"{nome}: {da_mandare} da mandare, {oggi} partiti oggi, "
            f"{recuperi} recuperi maturi — {len(righe)} righe in {file}")


print(f"Banco DM, {OGGI.isoformat()}")
for nome, file in ACCOUNT:
    print(" ", stato(nome, file))

# quello che il banco ha scritto nel brain (liste/contattati.csv, dall'8 settembre)
for nome, file in (("contattati", "contattati.csv"), ("scartati perche' il sito ce l'avevano", "gia-col-sito.csv")):
    p = QUI.parent / "liste" / file
    righe = list(csv.DictReader(p.open(encoding="utf-8"))) if p.exists() else []
    oggi = sum(1 for r in righe if r.get("Data") == OGGI.isoformat())
    print(f"  {nome}: {len(righe)} in tutto, {oggi} oggi ({file})")
