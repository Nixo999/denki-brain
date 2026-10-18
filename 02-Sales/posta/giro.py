#!/usr/bin/env python3
"""Il giro che gira da solo sul Mac che manda: invio e lettura delle risposte.

- ogni volta: un giro di `manda.py`, che fuori orario non fa niente;
- se l'ultima lettura ha più di 25 minuti, dalle 8 alle 20: `leggi-risposte.py`;
- una volta al giorno, dopo le 19: se le aziende pronte e non ancora scritte sono
  meno di SCORTA, `aziende.py` e `trova-mail.py` su un settore, a giro. Gira
  in un processo a parte (log in `dati/ricerca.log`), così l'invio non aspetta.

Non tocca git: tutto quello che scrive sta in `dati/`, fuori dal vault, che è
pubblico. Il log dell'invio sta in `dati/manda.log`.
"""
import importlib.util
import os
import subprocess
import sys
from datetime import datetime, timedelta

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
import db     # noqa: E402
import manda  # noqa: E402

SEGNO_LETTURA = os.path.join(db.DATI, 'ultima-lettura.txt')
SEGNO_RICERCA = os.path.join(db.DATI, 'ultima-ricerca.txt')
PID_RICERCA = os.path.join(db.DATI, 'ricerca.pid')
SCORTA = 200        # aziende pronte da tenere in magazzino: circa una settimana di invii a regime
LOTTO = 300         # aziende nuove da cercare in una sera: circa un'ora fra le due ricerche


def ultima_lettura():
    try:
        return datetime.fromisoformat(open(SEGNO_LETTURA).read().strip())
    except Exception:
        return datetime.min


def leggi_risposte():
    spec = importlib.util.spec_from_file_location('leggi', os.path.join(QUI, 'leggi-risposte.py'))
    leggi = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(leggi)
    leggi.main()


def ricerca_in_corso():
    try:
        os.kill(int(open(PID_RICERCA).read().strip()), 0)
        return True
    except Exception:
        return False


def prossimo_settore():
    """Un settore a sera, a giro. Non «il più scarso»: un settore esaurito in Lombardia
    resterebbe il più scarso per sempre e bloccherebbe la ricerca."""
    spec = importlib.util.spec_from_file_location('aziende', os.path.join(QUI, 'aziende.py'))
    az = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(az)
    settori = list(az.SETTORI)
    f = os.path.join(db.DATI, 'ricerca-settore.txt')
    try:
        i = (int(open(f).read().strip()) + 1) % len(settori)
    except Exception:
        i = 0
    with open(f, 'w') as h:
        h.write(str(i))
    return settori[i], az.SETTORI[settori[i]].split()


def ricerca_serale(ora):
    if ora.hour < 19 or open_or(SEGNO_RICERCA) == ora.date().isoformat() or ricerca_in_corso():
        return
    with db.connessione() as c:
        scorta = c.execute("SELECT COUNT(*) FROM aziende a WHERE fase='pronta' "
                           "AND NOT EXISTS (SELECT 1 FROM messaggi m WHERE m.piva=a.piva)").fetchone()[0]
    with open(SEGNO_RICERCA, 'w') as f:
        f.write(ora.date().isoformat())
    if scorta >= SCORTA:
        return
    settore, classi = prossimo_settore()
    comando = (f'cd {QUI!r} && /usr/bin/python3 aziende.py --ateco {",".join(classi)} --max {LOTTO} '
               f'&& /usr/bin/python3 trova-mail.py --max {LOTTO + 100} --paralleli 6')
    log = open(os.path.join(db.DATI, 'ricerca.log'), 'a')
    log.write(f'\n=== {ora:%Y-%m-%d %H:%M} scorta {scorta}, cerco {settore}\n')
    log.flush()
    p = subprocess.Popen(['/bin/sh', '-c', comando], stdout=log, stderr=log, start_new_session=True)
    with open(PID_RICERCA, 'w') as f:
        f.write(str(p.pid))
    manda.log('ricerca serale partita:', settore, f'(scorta {scorta} su {SCORTA})')


def open_or(f):
    try:
        return open(f).read().strip()
    except Exception:
        return ''


def main():
    ora = datetime.now()
    try:
        manda.giro()
    except Exception as e:
        manda.log('giro di invio fallito:', repr(e))
    if 8 <= ora.hour < 20 and ora - ultima_lettura() > timedelta(minutes=25):
        try:
            leggi_risposte()
        except SystemExit:
            pass
        except Exception as e:
            manda.log('lettura fallita:', repr(e))
        with open(SEGNO_LETTURA, 'w') as f:
            f.write(ora.isoformat(timespec='seconds'))
    try:
        ricerca_serale(ora)
    except Exception as e:
        manda.log('ricerca serale non partita:', repr(e))


if __name__ == '__main__':
    os.makedirs(db.DATI, exist_ok=True)
    main()
