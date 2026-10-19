#!/usr/bin/env python3
"""A che punto è la posta a freddo, in una schermata.

    python3 02-Sales/posta/stato.py
"""
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config  # noqa: E402
import db      # noqa: E402
import manda   # noqa: E402


def main():
    cfg = config.leggi()
    oggi = date.today().isoformat()
    with db.connessione() as c:
        fasi = dict(c.execute('SELECT fase, COUNT(*) FROM aziende GROUP BY fase').fetchall())
        coda = c.execute("SELECT COUNT(*) FROM messaggi WHERE tipo='primo' AND inviato IS NULL AND esito IS NULL").fetchone()[0]
        seguiti = c.execute("SELECT COUNT(*) FROM messaggi WHERE tipo='seguito' AND inviato IS NULL").fetchone()[0]
        tot = c.execute("SELECT COUNT(*) FROM messaggi WHERE inviato IS NOT NULL").fetchone()[0]
        ev = dict(c.execute("SELECT tipo, COUNT(*) FROM eventi WHERE tipo!='altro' GROUP BY tipo").fetchall())
        ev_oggi = dict(c.execute("SELECT tipo, COUNT(*) FROM eventi WHERE tipo!='altro' AND substr(quando,1,10)=? "
                                 "GROUP BY tipo", (oggi,)).fetchall())
        caselle = manda.stato_caselle(c, cfg['caselle'])
    print('Invio vero:', 'ACCESO' if cfg['attivo'] else 'spento (ATTIVO=0, il giro dice solo cosa manderebbe)')
    if os.path.exists(manda.FRENO):
        print('FRENO TIRATO:', open(manda.FRENO).read().strip())
    print('\nAziende per fase:')
    for f in ('nuova', 'senza_sito', 'senza_mail', 'pronta', 'scritta', 'inviata', 'seguita', 'risposta',
              'rimbalzata', 'disiscritta', 'scartata'):
        if fasi.get(f):
            print(f'  {f:12} {fasi[f]}')
    print(f'\nIn coda: {coda} prime mail scritte, {seguiti} seguiti programmati. Mandate finora: {tot}.')
    print('\nOggi per casella:')
    for a, st in caselle.items():
        print(f"  {a:32} {st['oggi']:>3} su {st['quota']}")
    with db.connessione() as c:
        per_oggetto = c.execute(
            "SELECT m.variante, COUNT(*) AS mandate, SUM(a.fase IN ('risposta','disiscritta')) AS risposte "
            "FROM messaggi m JOIN aziende a ON a.piva=m.piva WHERE m.tipo='primo' AND m.inviato IS NOT NULL "
            "GROUP BY m.variante ORDER BY m.variante").fetchall()
    if per_oggetto:
        print('\nRisposte per oggetto (prime mail mandate; servono qualche centinaio per forma prima di scegliere):')
        for r in per_oggetto:
            print(f"  {r['variante'] or '-'}  {r['risposte'] or 0} su {r['mandate']}  ({(r['risposte'] or 0) / r['mandate']:.1%})")
    print('\nRitorni (oggi / in tutto):')
    for t in ('risposta', 'disiscrizione', 'automatica', 'rimbalzo', 'freno', 'errore'):
        if ev.get(t):
            print(f'  {t:14} {ev_oggi.get(t, 0)} / {ev[t]}')


if __name__ == '__main__':
    main()
