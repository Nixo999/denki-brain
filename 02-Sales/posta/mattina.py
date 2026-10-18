#!/usr/bin/env python3
"""Il giro del mattino della posta, in due comandi fissi. Lo segue Claude da `giro-posta.md`.

    python3 02-Sales/posta/mattina.py prima
    python3 02-Sales/posta/mattina.py dopo

I comandi sono sempre questi due, con questo testo esatto: il task pianificato
parte coi permessi normali e l'app ricorda un comando approvato solo se il
testo è identico (trappole.md, «Liste e banco DM»).

`prima` legge le risposte, stampa lo stato, prepara `dati/da-scrivere.json`
con le aziende da scrivere per i prossimi due giorni lavorativi, e stampa le
risposte arrivate dall'ultimo giro, da rileggere.
In mezzo Claude scrive `dati/scritte.json` e aggiorna `dati/risposte.md`.
`dopo` importa le righe, stampa gli scarti ed esporta il registro in `dati/`.
Non committa niente: il vault è pubblico, e il registro ha nomi e testi di chi
risponde.
"""
import importlib.util
import os
import sys
from datetime import date, timedelta

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
import config    # noqa: E402
import db        # noqa: E402
import registro  # noqa: E402
import scrivi    # noqa: E402
import stato     # noqa: E402

SCRITTE = os.path.join(db.DATI, 'scritte.json')
RIVISTO = os.path.join(db.DATI, 'ultimo-evento-rivisto.txt')


def modulo(nome, file):
    spec = importlib.util.spec_from_file_location(nome, os.path.join(QUI, file))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def quanti_da_scrivere(cfg):
    """La quota dei prossimi due giorni lavorativi, meno le prime mail già in coda."""
    with db.connessione() as c:
        caselle = stato.manda.stato_caselle(c, cfg['caselle'])
        coda = c.execute("SELECT COUNT(*) FROM messaggi WHERE tipo='primo' AND inviato IS NULL AND esito IS NULL").fetchone()[0]
    g, giorni = date.today(), []
    while len(giorni) < 2:
        if config.lavorativo(g):
            giorni.append(g)
        g += timedelta(days=1)
    with db.connessione() as c:
        totale = 0
        for a, _ in cfg['caselle']:
            primo = c.execute('SELECT MIN(inviato) FROM messaggi WHERE casella=? AND inviato IS NOT NULL', (a,)).fetchone()[0]
            inizio = date.fromisoformat(primo[:10]) if primo else None
            totale += sum(config.quota(inizio, x) for x in giorni)
    return max(0, totale - coda)


def ultimo_rivisto():
    try:
        return int(open(RIVISTO).read().strip())
    except Exception:
        return 0


def prima():
    cfg = config.leggi()
    if not cfg['caselle']:
        print('Questo Mac non manda: non c\'è', config.FILE, '. Il giro della posta si ferma qui.')
        return
    registro.ricarica()
    try:
        modulo('leggi', 'leggi-risposte.py').main()
    except Exception as e:
        print('lettura delle risposte non riuscita:', e)
    print()
    stato.main()
    print()
    n = quanti_da_scrivere(cfg)
    if os.path.exists(stato.manda.FRENO):
        print('Il freno è tirato: oggi non si scrive niente di nuovo.')
        n = 0
    if n:
        scrivi.prepara(n)
    else:
        print('Niente da scrivere oggi: la coda copre i prossimi due giorni.')
    with db.connessione() as c:
        ev = c.execute("SELECT e.id, e.quando, e.tipo, e.da, e.oggetto, e.testo, a.nome, a.piva FROM eventi e "
                       "LEFT JOIN aziende a ON a.piva=e.piva WHERE e.id>? AND e.tipo IN "
                       "('risposta','disiscrizione','automatica','rimbalzo','freno','errore') ORDER BY e.id",
                       (ultimo_rivisto(),)).fetchall()
    print(f'\nRisposte e ritorni da rileggere: {len(ev)}')
    for e in ev:
        print('-' * 60)
        print(f"#{e['id']} {e['quando']} {e['tipo'].upper()} | {e['nome'] or '?'} ({e['piva'] or '-'}) | da {e['da']}")
        print('Oggetto:', e['oggetto'])
        print((e['testo'] or '')[:1200])


def dopo():
    if not config.leggi()['caselle']:
        print('Questo Mac non manda: niente da fare.')
        return
    if os.path.exists(SCRITTE):
        scrivi.importa(SCRITTE)
        os.replace(SCRITTE, SCRITTE + '.importato')
    else:
        print('Nessun dati/scritte.json da importare.')
    registro.esporta()
    with db.connessione() as c:
        ultimo = c.execute('SELECT MAX(id) FROM eventi').fetchone()[0] or 0
    with open(RIVISTO, 'w') as f:
        f.write(str(ultimo))
    with db.connessione() as c:
        fasi = dict(c.execute('SELECT fase, COUNT(*) FROM aziende GROUP BY fase').fetchall())
    print('Fasi adesso:', ', '.join(f'{k} {v}' for k, v in sorted(fasi.items())))
    print('Registro e risposte stanno in', db.DATI, '(fuori da git: il vault è pubblico).')
