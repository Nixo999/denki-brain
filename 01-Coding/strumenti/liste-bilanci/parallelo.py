# Stesso lavoro di schede.py + raccogli.py, in parallelo: prima tutte le schede, poi Pagine Gialle.
import json, os, sys
from concurrent.futures import ThreadPoolExecutor
import scheda, pg
ESCLUSE = {'09191930156': "Blu Notte S.r.l.: e' il BluNotte di Paolo, gia' nel giro di Seba"}
SETTORE = {'52.24.4': 'facchinaggio', '77.39.94': 'allestimento', '82.3': 'allestimento', '90.02.09': 'allestimento',
           '52.24': 'facchinaggio', '90.02.01': 'allestimento', '16.23.21': 'allestimento'}
IN = sys.argv[1] if len(sys.argv) > 1 else 'candidati.json'
cands = json.load(open(IN))
uniq = {}
for x in sorted(cands, key=lambda x: (x['km'] is None, x['km'] or 0)):
    uniq.setdefault(x['piva'], x)
cands = list(uniq.values())
with ThreadPoolExecutor(8) as ex:
    list(ex.map(scheda.leggi, cands))
print('schede', len(cands), flush=True)
def motivo(x):
    if x.get('stato') != 'Attiva': return f"stato {x.get('stato')}"
    if 'LIQUIDAZ' in x['nome'].upper(): return 'in liquidazione'
    if x['piva'] in ESCLUSE: return ESCLUSE[x['piva']]
    if x['km'] is None: return 'comune non trovato'
def cerca(x):
    m = motivo(x)
    if m: return dict(x, esito=None, pg=None, prova=m, scartata=True)
    try:
        e, r, p = pg.trova(x, SETTORE[x['ateco_lista']])
    except Exception as err:
        return dict(x, esito=None, pg=None, prova=f'errore {err}', scartata=False)
    return dict(x, esito=e, pg=r, prova=p, scartata=False)
with ThreadPoolExecutor(4) as ex:
    res = list(ex.map(cerca, cands))
old = json.load(open('trovate.json')) if os.path.exists('trovate.json') and IN != 'candidati.json' else {}
old.update({r['piva']: r for r in res})
json.dump(old, open('trovate.json', 'w'), ensure_ascii=False)
print('fatto', sum(1 for r in res if r['esito']), 'con telefono su', sum(1 for r in res if not r['scartata']), 'attive')
