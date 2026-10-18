#!/usr/bin/env python3
"""Riporta quello che è successo in CSV leggibili, in `dati/registro/`. Riscrive i file da capo ogni volta.

I CSV restano sul Mac che manda, fuori da git: il vault è un repository
PUBBLICO su GitHub (controllato il 18/10/2026), e qui dentro ci sono indirizzi,
nomi e testi di chi risponde.

    python3 02-Sales/posta/registro.py

- `registro/inviate.csv`: una riga per mail partita, con la pagina da cui
  viene l'indirizzo. È l'origine documentata che chiede la decisione del 2/09.
- `registro/risposte.csv`: risposte, rimbalzi e disiscrizioni.
- `registro/disiscritti.csv`: i domini a cui non si scrive più. È un obbligo,
  e vale anche se la base dati si rovina: `--ricarica` li rimette dentro.
"""
import csv
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
import db  # noqa: E402

DIR = os.environ.get('POSTA_REGISTRO', os.path.join(db.DATI, 'registro'))


def scrivi(nome, intestazione, righe):
    os.makedirs(DIR, exist_ok=True)
    with open(os.path.join(DIR, nome), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(intestazione)
        w.writerows(righe)


def esporta():
    with db.connessione() as c:
        inviate = c.execute(
            "SELECT m.inviato, m.casella, m.tipo, a.nome, a.piva, m.a, a.settore, a.comune, a.prov, "
            "a.email_prova, m.oggetto FROM messaggi m JOIN aziende a ON a.piva=m.piva "
            "WHERE m.inviato IS NOT NULL ORDER BY m.inviato").fetchall()
        eventi = c.execute(
            "SELECT e.quando, e.tipo, a.nome, e.piva, e.da, e.oggetto, substr(replace(e.testo, char(10), ' '), 1, 300) "
            "FROM eventi e LEFT JOIN aziende a ON a.piva=e.piva "
            "WHERE e.tipo IN ('risposta','rimbalzo','disiscrizione','automatica','freno') ORDER BY e.quando").fetchall()
        disiscritti = c.execute('SELECT dominio, quando, substr(replace(motivo, char(10), \' \'), 1, 200) '
                                'FROM disiscritti ORDER BY quando').fetchall()
    scrivi('inviate.csv', ['quando', 'casella', 'tipo', 'azienda', 'piva', 'email', 'settore', 'comune', 'prov',
                           'origine indirizzo', 'oggetto'], inviate)
    scrivi('risposte.csv', ['quando', 'tipo', 'azienda', 'piva', 'da', 'oggetto', 'testo'], eventi)
    scrivi('disiscritti.csv', ['dominio', 'quando', 'motivo'], disiscritti)
    print(f'inviate {len(inviate)}, eventi {len(eventi)}, disiscritti {len(disiscritti)} → {DIR}')


def ricarica():
    f = os.path.join(DIR, 'disiscritti.csv')
    if not os.path.exists(f):
        return
    with db.connessione() as c:
        for r in csv.DictReader(open(f, encoding='utf-8')):
            c.execute('INSERT OR IGNORE INTO disiscritti(dominio, quando, motivo) VALUES (?,?,?)',
                      (r['dominio'], r['quando'], r['motivo']))
    print('disiscritti ricaricati dal vault')


if __name__ == '__main__':
    if '--ricarica' in sys.argv:
        ricarica()
    else:
        esporta()
