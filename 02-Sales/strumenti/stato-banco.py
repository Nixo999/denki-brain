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


# Lo stesso criterio del banco, dal 12/09/2026. Patrick: «i recuperi non devono
# essere a caso, ma pochi e mirati, per situazioni calde o almeno chi ha letto
# e sensati in base alla chat», e «devi leggere tutta la chat». Prima qui e nel
# banco bastavano quattro giorni lavorativi: erano 74 righe, cinque delle quali
# avevano gia` detto no.
RIFIUTO = re.compile(r"non siamo interessat|non sono interessat|non mi interessa|non ci interessa|no grazie|"
                     r"non ne ho bisogno|non ne abbiamo bisogno|non abbiamo intenzione|non ci serve|"
                     r"gia' un sito|già un sito|ce l'abbiamo|l'ho chiuso|in bocca al lupo|per ora no|"
                     r"verra' chiuso|verrà chiuso|non esiste piu|non esiste più|abbiamo chiuso", re.I)
AUTORISPOSTA = re.compile(r"grazie per aver|grazie di aver|ti ringraziamo per|risponderemo|ti risponder|"
                          r"ti ricontatter|messaggio automatico|per prenotazion|per informazion|"
                          r"il prima possibile|al piu' presto|al più presto|abbiamo ricevuto il tuo messaggio|"
                          r"scrivici su whatsapp|chiamaci|puoi contattarci|benvenut", re.I)
APPUNTAMENTO = re.compile(r"\b(lunedi|lunedì|martedi|martedì|mercoledi|mercoledì|giovedi|giovedì|venerdi|venerdì|"
                          r"sabato|domenica)\b|risentiamoci|mi richiami|la chiamo|ti chiamo|chiamami|dopo le \d|"
                          r"la prossima settimana|settimana prossima", re.I)
ESITO_CHIUSO = re.compile(r"^scartat|^no\b|ha gia' il sito|ha già il sito|nessun interesse|chiude il negozio|"
                          r"non interessa", re.I)
ESITO_CALDO = re.compile(r"in valutazione|caldo|chiede|ha chiesto", re.I)


def e_un_recupero(r, inv, rec):
    inviato = (r.get(inv) or "").strip()
    if not inviato or (rec and (r.get(rec) or "").strip()):
        return False
    esito = (r.get("Esito DM") or "").strip()
    if esito and ESITO_CHIUSO.search(esito):
        return False
    chat = (r.get("Chat") or "").strip()
    letto = (r.get("Letto (data)") or "").strip()
    if chat and RIFIUTO.search(chat):
        return False
    if chat and APPUNTAMENTO.search(chat):
        return True                      # un appuntamento non aspetta i quattro giorni
    if lavorativi_da(inviato) < ATTESA:
        return False
    if ESITO_CALDO.search(esito):
        return True
    if chat:
        pezzi = [x.strip() for x in chat.split("|") if x.strip()]
        return not all(AUTORISPOSTA.search(x) for x in pezzi)
    return bool(letto)


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
    recuperi = sum(1 for r in righe if e_un_recupero(r, inv, rec))
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
