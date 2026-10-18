#!/usr/bin/env python3
"""Il giro che gira da solo sul Mac che manda: invio e lettura delle risposte.

- ogni volta: un giro di `manda.py`, che fuori orario non fa niente;
- se l'ultima lettura ha più di 25 minuti, dalle 8 alle 20: `leggi-risposte.py`.

Non tocca git: il registro nel vault lo esporta e lo committa il giro del
mattino di Claude (`giro-posta.md`). Il log sta in `dati/manda.log`.
"""
import importlib.util
import os
import sys
from datetime import datetime, timedelta

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
import db     # noqa: E402
import manda  # noqa: E402

SEGNO_LETTURA = os.path.join(db.DATI, 'ultima-lettura.txt')


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


if __name__ == '__main__':
    os.makedirs(db.DATI, exist_ok=True)
    main()
