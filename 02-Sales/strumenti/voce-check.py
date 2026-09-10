#!/usr/bin/env python3
"""Passa un testo cliente dalla blacklist di voce-denkicode, meccanicamente.

    python3 02-Sales/strumenti/voce-check.py --csv 02-Sales/liste/<lista>.csv
    echo "testo" | python3 02-Sales/strumenti/voce-check.py

Non sostituisce la rilettura ad alta voce: prende i tell che una macchina vede
(em dash, connettivi da tema, asterischi, apertura a domanda, frasi tutte
lunghe uguali, catene di «e», le frasi-cuscinetto) e stampa dove stanno.
Nato il 10 settembre 2026 per rileggere 80 messaggi scritti a mano.
"""
import csv, re, statistics, sys

CONNETTIVI = re.compile(r"\b(quindi|perciò|percio|dunque|inoltre|di conseguenza|pertanto|in sintesi|in conclusione)\b", re.I)
CUSCINETTO = re.compile(r"(capisco perfettamente|fantastica domanda|sono qui per|spero che questo messaggio|mi permetto di|non esiti a)", re.I)
OMBRELLO = re.compile(r"\b(soluzion[ei]|innovativ[oa]|su misura|professional[ei]|strategic[oa]|all'avanguardia)\b", re.I)
VIETATE = re.compile(r"\b(fattura|abbonamento|contratto|canone)\b", re.I)


def controlla(testo):
    p = []
    if "—" in testo or "–" in testo:
        p.append("em/en dash")
    if "*" in testo or "#" in testo:
        p.append("markdown/asterischi")
    if CONNETTIVI.search(testo):
        p.append("connettivo da tema: " + CONNETTIVI.search(testo).group(0))
    if CUSCINETTO.search(testo):
        p.append("frase-cuscinetto: " + CUSCINETTO.search(testo).group(0))
    if OMBRELLO.search(testo):
        p.append("aggettivo ombrello: " + OMBRELLO.search(testo).group(0))
    if VIETATE.search(testo):
        p.append("parola fiscale vietata: " + VIETATE.search(testo).group(0))
    prima = re.split(r"[.!?\n]", testo.strip(), maxsplit=1)[0]
    if prima.strip().endswith("?") or re.match(r"\s*(hai mai|sai che|ha mai|sa che)", testo, re.I):
        p.append("apertura a domanda")
    frasi = [f.strip() for f in re.split(r"[.!?]\s+|\n+", testo) if len(f.strip().split()) >= 2]
    lun = [len(f.split()) for f in frasi]
    if len(lun) >= 4 and min(lun) > 7:
        p.append(f"nessuna frase corta (min {min(lun)} parole)")
    if len(lun) >= 4 and statistics.pstdev(lun) < 3:
        p.append(f"frasi tutte lunghe uguali (dev {statistics.pstdev(lun):.1f})")
    for f in frasi:
        if len(re.findall(r"\be\b", f)) >= 3:
            p.append("frase tenuta insieme da tre «e»: " + f[:60])
            break
    tre = re.search(r"non deve [^,.]+, non deve [^,.]+ e non deve", testo, re.I)
    if tre:
        p.append("elenco di tre «non deve»")
    if re.search(r"http|www\.", testo):
        p.append("link nel messaggio")
    return p


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--csv":
        righe = list(csv.DictReader(open(sys.argv[2], encoding="utf-8")))
        col = next(c for c in righe[0] if c.lower().startswith("messaggio"))
        n = 0
        for r in righe:
            p = controlla(r[col] or "")
            if p:
                n += 1
                print(f"{r.get('Account IG','?'):34} " + " · ".join(p))
        print(f"{n} messaggi su {len(righe)} con almeno un tell")
        sys.exit(1 if n else 0)
    t = sys.stdin.read()
    p = controlla(t)
    print("\n".join(p) if p else "pulito")
