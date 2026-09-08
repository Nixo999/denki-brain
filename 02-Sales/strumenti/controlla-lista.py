#!/usr/bin/env python3
"""Controllo di una lista PRIMA di pubblicarla sul banco. Lo lancia chi la
genera (di solito Claude), sul CSV finito.

    python3 02-Sales/strumenti/controlla-lista.py 02-Sales/liste/2026-09-08-....csv

Ferma due errori gia` pagati:
- la verifica del sito copiata uguale su decine di righe (l'8 settembre 2026:
  62 righe su 68 con la stessa frase, e almeno 20 il sito ce l'avevano);
- un handle che sta gia` in contattati.csv o su un banco (metodo, passo 4);
- una riga verificata a occhio invece che da verifica-sito.py (passo 3).
Esce con 1 se trova qualcosa: la lista non si pubblica finche` non esce con 0.
"""
import csv, collections, re, sys
from pathlib import Path

QUI = Path(__file__).resolve().parent
SALES = QUI.parent
SOGLIA = 3        # oltre queste ripetizioni la frase e` un modello, non una verifica


def handle(s):
    return (s or "").strip().lstrip("@").lower()


def gia_scritti():
    visti = {}
    for p in [SALES / "liste" / "contattati.csv", SALES / "liste" / "gia-col-sito.csv",
              *QUI.glob("lista-*.csv")]:
        if not p.exists():
            continue
        for r in csv.DictReader(p.open(encoding="utf-8")):
            h = handle(r.get("Account IG"))
            if h and (p.name.startswith("lista-") and not (r.get("DM inviato (data)") or "").strip()):
                visti.setdefault(h, f"gia` sul banco ({p.name})")
            elif h:
                visti.setdefault(h, f"gia` in {p.name}")
    return visti


def controlla(p):
    righe = list(csv.DictReader(p.open(encoding="utf-8")))
    errori = []
    col = next((c for c in righe[0] if c.lower().startswith("esito verifica")), None) if righe else None
    if not col:
        return [f"{p.name}: manca la colonna «Esito verifica sito»"]
    # dall'8/9 la colonna la scrive verifica-sito.py: una riga senza la sua prova
    # e` una riga verificata a occhio, e quelle non si pubblicano piu`
    senza = [r.get("Account IG", "?") for r in righe if not r[col].strip().startswith("cercato «")]
    if senza:
        errori.append(f"{len(senza)} righe senza la prova di verifica-sito.py (es. {senza[0]}): «cercato «…» → …» manca")
    senza_script = [r.get("Account IG", "?") for r in righe if "[verifica-sito]" not in r[col]]
    if senza_script:
        errori.append(f"{len(senza_script)} righe mai passate da verifica-sito.py (es. {senza_script[0]})")
    prob = [r.get("Account IG", "?") for r in righe if "PROBABILE SITO" in r[col]]
    if prob:
        errori.append(f"{len(prob)} righe con un PROBABILE SITO da aprire e decidere: {', '.join(prob[:6])}")
    rifare = [r.get("Account IG", "?") for r in righe if "DA RIFARE" in r[col]]
    if rifare:
        errori.append(f"{len(rifare)} righe con la ricerca fallita, da rilanciare: {', '.join(rifare[:5])}")
    conta = collections.Counter(re.sub(r"\s+", " ", r[col].strip().lower()) for r in righe)
    for frase, n in conta.items():
        if not frase:
            errori.append(f"{n} righe senza verifica del sito")
        elif n > SOGLIA:
            errori.append(f"{n} righe con la stessa verifica: «{frase[:70]}…» — e` una frase, non un controllo")
    visti = gia_scritti()
    for r in righe:
        h = handle(r.get("Account IG"))
        if h in visti:
            errori.append(f"@{h}: {visti[h]}")
    return errori


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    tot = 0
    for f in sys.argv[1:]:
        e = controlla(Path(f))
        tot += len(e)
        print(f"{f}: {'ok' if not e else str(len(e)) + ' problemi'}")
        for riga in e:
            print("  -", riga)
    sys.exit(1 if tot else 0)
