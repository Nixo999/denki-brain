#!/usr/bin/env python3
"""Passa un testo cliente dalla blacklist di voce-denkicode, meccanicamente.

    python3 02-Sales/strumenti/voce-check.py --csv 02-Sales/liste/<lista>.csv
    echo "testo" | python3 02-Sales/strumenti/voce-check.py

Non sostituisce la rilettura ad alta voce: prende i tell che una macchina vede
(em dash, connettivi da tema, asterischi, apertura a domanda, frasi tutte
lunghe uguali, catene di «e», le frasi-cuscinetto) e stampa dove stanno.
Nato il 10 settembre 2026 per rileggere 80 messaggi scritti a mano.

Dall'11/09/2026 prende anche le tre cose che Nicola ha segnalato: le tracce del
nostro processo finite in un testo cliente («orari da Google», «da confermare»),
il registro misto Lei/Voi dentro lo stesso messaggio, e le minuscole dopo il
punto. Quest'ultima e' un refuso, non «fretta umana»: la riga della skill che
diceva «punteggiatura imperfetta» e' stata tolta.
"""
import csv, re, statistics, sys

CONNETTIVI = re.compile(r"\b(quindi|perciò|percio|dunque|inoltre|di conseguenza|pertanto|in sintesi|in conclusione)\b", re.I)
CUSCINETTO = re.compile(r"(capisco perfettamente|fantastica domanda|sono qui per|spero che questo messaggio|mi permetto di|non esiti a)", re.I)
OMBRELLO = re.compile(r"\b(soluzion[ei]|innovativ[oa]|su misura|professional[ei]|strategic[oa]|all'avanguardia)\b", re.I)
VIETATE = re.compile(r"\b(fattura|abbonamento|contratto|canone)\b", re.I)

# Aggiunti l'11/09/2026, dopo «sembra un bambino che non sa la punteggiatura»
# e «mette note che dovrebbe tenersi per se» (note di fonte finite in pagina).
# Il nostro processo non esce mai verso il cliente.
PROCESSO = re.compile(
    r"(da confermare|non confermat|\bTODO\b|le foto (sono |le )?(prese|prelevate)|"
    r"(orari|foto|immagini|recensioni|dati) (presi |prese |da |dal )?(google|instagram|facebook|pagine ?gialle)|"
    r"secondo (google|instagram)|fonte:|dal profilo instagram|bozza non commissionata|"
    r"non verificat)", re.I)
# «Lei» e «Voi» nello stesso messaggio: il difetto piu' visibile
LEI = re.compile(r"\b(le preparo|le mando|le faccio|gliela|glielo|le piace|suo sito|sue foto|lei\b|la ringrazio)", re.I)
VOI = re.compile(r"\b(vi preparo|vi mando|vi faccio|ve la|ve lo|vi piace|vostro sito|vostre foto|voi\b|vi ringrazio)", re.I)
# minuscola dopo il punto: refuso, non «fretta umana»
MINUSCOLA = re.compile(r"[.!?]\s+([a-zàèéìòù])")


def controlla(testo, sito=False):
    """sito=True: copy di una pagina, non un messaggio.

    Le due cose non si controllano uguale. L'em dash e' un tell perche' un lead
    lo cerca in un DM per capire se gli ha scritto una macchina; dentro il
    titolo di un sito e' tipografia, e infatti NG Barber e Fiftynine — i due che
    Nicola ha approvato — ne sono pieni. Gli aggettivi ombrello idem: «Da
    Caterina Toelettatura Professionale» e' il nome dell'attivita'.
    Quello che invece su un sito e' PIU' grave e' la traccia del nostro
    processo: la legge il cliente del cliente.
    """
    p = []
    if not sito and ("—" in testo or "–" in testo):
        p.append("em/en dash")
    if "*" in testo or "#" in testo:
        p.append("markdown/asterischi")
    if CONNETTIVI.search(testo):
        p.append("connettivo da tema: " + CONNETTIVI.search(testo).group(0))
    if CUSCINETTO.search(testo):
        p.append("frase-cuscinetto: " + CUSCINETTO.search(testo).group(0))
    if not sito and OMBRELLO.search(testo):
        p.append("aggettivo ombrello: " + OMBRELLO.search(testo).group(0))
    if VIETATE.search(testo):
        p.append("parola fiscale vietata: " + VIETATE.search(testo).group(0))
    if PROCESSO.search(testo):
        p.append("traccia del nostro processo, non esce mai: " + PROCESSO.search(testo).group(0))
    if LEI.search(testo) and VOI.search(testo):
        p.append(f"registro misto Lei/Voi: «{LEI.search(testo).group(0)}» e «{VOI.search(testo).group(0)}»")
    if MINUSCOLA.search(testo):
        p.append("minuscola dopo il punto: «" + MINUSCOLA.search(testo).group(0).strip() + "»")
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
