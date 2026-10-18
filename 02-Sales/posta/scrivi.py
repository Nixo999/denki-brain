#!/usr/bin/env python3
"""Il passaggio di Claude: una riga personale per azienda, poi la mail si compone da sola.

    python3 02-Sales/posta/scrivi.py prepara [--n 60]     scrive dati/da-scrivere.json
    python3 02-Sales/posta/scrivi.py importa dati/scritte.json
    python3 02-Sales/posta/scrivi.py mostra [--n 3]       stampa le ultime mail composte

Claude legge `da-scrivere.json` (nome, settore, attività, comune, estratto del
sito) e scrive `scritte.json`, una lista di {"piva": ..., "riga": ...}. La riga
è UNA frase, al «voi», che dice una cosa vera del loro lavoro letta
nell'estratto: cosa fanno, per chi, con cosa. Esempio buono: «Ho visto sul
vostro sito che fate taglio laser e piegatura della lamiera per conto terzi.»

Le regole che `importa` controlla, e per cui scarta la riga:
- una frase sola, fra 8 e 30 parole, che finisce col punto;
- niente complimenti e niente aggettivi vuoti (eccellenza, leader, qualità,
  professionale, innovativo, su misura...);
- niente fatturato, dipendenti, milioni, bilancio: si sa, ma dirlo fa sembrare
  uno che li ha schedati (script di Patrick);
- niente em dash e niente di quello che ferma voce-check.py.
Se l'estratto non ha un fatto concreto, la riga si lascia vuota ("riga": ""):
la mail funziona anche senza, e una frase inventata è peggio di nessuna.
"""
import argparse
import importlib.util
import json
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
import config  # noqa: E402
import db      # noqa: E402
import testi   # noqa: E402

DA_SCRIVERE = os.path.join(db.DATI, 'da-scrivere.json')

_spec = importlib.util.spec_from_file_location('voce_check', os.path.join(QUI, '..', 'strumenti', 'voce-check.py'))
voce = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(voce)

VIETATE = re.compile(r'(complimenti|eccellen|leader|qualit[àa]|professional|innovativ|su misura|soluzion|'
                     r'all\'avanguardia|punto di riferimento|fatturat|dipendent|milioni|bilancio|addetti|—|–)', re.I)


def prepara(n):
    with db.connessione() as c:
        righe = c.execute("SELECT a.* FROM aziende a WHERE a.fase='pronta' AND a.email IS NOT NULL "
                          "AND NOT EXISTS (SELECT 1 FROM messaggi m WHERE m.piva=a.piva) "
                          "ORDER BY a.fatturato DESC").fetchall()
        righe = [r for r in righe if not db.disiscritto(c, r['email'])]
    # un settore alla volta, a giro: così un giorno non va tutto alle officine
    per_settore = {}
    for r in righe:
        per_settore.setdefault(r['settore'] or '', []).append(r)
    scelte = []
    while len(scelte) < n and any(per_settore.values()):
        for s in list(per_settore):
            if per_settore[s] and len(scelte) < n:
                scelte.append(per_settore[s].pop(0))
    out = [dict(piva=r['piva'], nome=r['nome'], settore=r['settore'], attivita=r['attivita'],
                comune=r['comune'], sito=r['sito'], estratto=(r['estratto'] or '')[:1500]) for r in scelte]
    os.makedirs(db.DATI, exist_ok=True)
    json.dump(out, open(DA_SCRIVERE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{len(out)} aziende in {DA_SCRIVERE}')
    print('Per ognuna una riga in dati/scritte.json: [{"piva": "...", "riga": "..."}]. Regole in testa a scrivi.py.')


def controlla_riga(riga):
    if not riga:
        return None
    if VIETATE.search(riga):
        return 'parola vietata: ' + VIETATE.search(riga).group(0)
    parole = len(riga.split())
    if not 8 <= parole <= 30:
        return f'{parole} parole, servono fra 8 e 30'
    if not riga.endswith('.') or re.search(r'[.!?]\s+\S', riga[:-1]):
        return 'deve essere una frase sola, chiusa dal punto'
    if riga.endswith('?') or riga.lower().startswith(('sai ', 'avete mai', 'hai mai')):
        return 'niente domande'
    return None


def problemi_voce(testo):
    """Le segnalazioni di voce-check.py sulla mail intera, se ce ne sono."""
    return voce.controlla(testo)


def importa(file):
    scritte = json.load(open(file, encoding='utf-8'))
    tel = config.leggi().get('TELEFONO', '')
    ok, scarti = 0, []
    with db.connessione() as c:
        for s in scritte:
            a = c.execute('SELECT * FROM aziende WHERE piva=?', (s['piva'],)).fetchone()
            if not a or a['fase'] != 'pronta':
                scarti.append((s['piva'], 'azienda non in fase pronta'))
                continue
            riga = (s.get('riga') or '').strip()
            errore = controlla_riga(riga)
            if errore:
                scarti.append((s['piva'], f'{errore} → «{riga}»'))
                continue
            oggetto, corpo = testi.primo(a['settore'], riga, tel)
            p = problemi_voce(corpo)
            if p:
                scarti.append((s['piva'], 'voce-check: ' + '; '.join(p)[:200]))
                continue
            c.execute("INSERT INTO messaggi(piva, tipo, a, oggetto, corpo, scritto) VALUES (?,?,?,?,?,?)",
                      (a['piva'], 'primo', a['email'], oggetto, corpo, db.adesso()))
            db.metti_fase(c, a['piva'], 'scritta')
            ok += 1
    print(f'importate {ok}, scartate {len(scarti)}')
    for piva, motivo in scarti:
        print(' -', piva, motivo)


def mostra(n):
    with db.connessione() as c:
        for m in c.execute("SELECT m.*, a.nome FROM messaggi m JOIN aziende a ON a.piva=m.piva "
                           "WHERE m.tipo='primo' ORDER BY m.id DESC LIMIT ?", (n,)):
            print('=' * 70)
            print(f"{m['nome']}  →  {m['a']}\nOggetto: {m['oggetto']}\n\n{m['corpo']}")


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('azione', choices=['prepara', 'importa', 'mostra'])
    ap.add_argument('file', nargs='?')
    ap.add_argument('--n', type=int, default=60)
    x = ap.parse_args()
    if x.azione == 'prepara':
        prepara(x.n)
    elif x.azione == 'importa':
        importa(x.file or os.path.join(db.DATI, 'scritte.json'))
    else:
        mostra(x.n if x.n != 60 else 3)
