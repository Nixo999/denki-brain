#!/usr/bin/env python3
"""Resa dei DM Instagram per settore/provincia/follower/gancio/canale. Sola lettura sul vault.
Uso: python3 02-Sales/strumenti/resa-dm.py [tabella]   tabelle: prodotto settore prov follower gancio contatto mapping rotazione banco coorte
Coorte = DM con data <= 2026-09-14 + archivio pre-8/9 + chi ha risposto senza data: la posta e' stata letta fino al 17-21/9.
"""
import csv, re, sys, collections, datetime, pathlib
csv.field_size_limit(10**9)
V = pathlib.Path(__file__).resolve().parent.parent
CUT = '2026-09-14'

def rd(p): return list(csv.DictReader(open(V / p, encoding='utf-8-sig')))
L = rd('strumenti/lista-corrente.csv')
A = rd('liste/archivio-2026-09-11-contattati-senza-data.csv')
RISP = {x['Account IG']: x for x in rd('liste/risposte-dm.csv')}

# ---------- macro-settori: vince la parola che compare per prima nel Segmento ----------
MACRO = [
 ('ciglia/PMU', r'trucco permanente|ciglia|\bpmu\b|microblading|laminazione|lash|dermopigment|nanoblading|sopracciglia|hydralips|lip blush'),
 ('unghie', r'\bnails?\b|onicotecnica|unghie'),
 ('estetica', r'estetic|solarium|massagg|skincare'),
 ('parrucchieri', r'parrucc|\bhair|acconciat|tricolog|hairstyl'),
 ('barbieri', r'barb'),
 ('trucco/make-up', r'make-up|trucco'),
 ('tatuatori', r'tatu|tattoo|piercing'),
 ('toelettature/pet', r'toelett|\bdog|\bcani\b|cinofil|\bpet\b|ippico'),
 ('fotografi', r'fotograf|videomaker'),
 ('personal trainer/palestre', r'personal trainer|pilates|yoga|palestra|ginnastica|boxe'),
 ('pasticcerie/gelaterie', r'pasticcer|gelater|cake'),
 ('ospitalita (hotel/agriturismo)', r'albergo|hotel|agriturismo|campeggio'),
 ('ristorazione', r'pizzeria|ristorante|\bbar\b|osteria|\bpub\b|street food|hamburgeria|birreria|enoteca|vineria|grotto|ristorazione'),
 ('fioristi/wedding/vivai', r'fiorist|wedding|floral|vivai|florovivais|ingrosso fiori|garden|giardinagg|atelier sposa'),
 ('sartorie/tessile', r'sartor|atelier|tappezz|tessitur|tessuti|maglific|tendagg|calzaturific|ricamo|stampa digitale tessile'),
 ('officine/auto', r'officin|carrozzer|autofficin|gommist|concessionar|\bmoto\b|autodemoliz|ricambi auto|autolavagg|detailing|autoriparaz|\bauto\b|nautic|camper|revisioni|autoscuola|centro auto'),
 ('impiantisti', r'impiant|termoidraul|idraulic|elettric|fotovoltaic|climatizzaz|caldaie|antincendio|domotica|automazione|efficientamento|spurghi|piscine'),
 ('edilizia/serramenti/falegnamerie', r'edil|costruzion|ristruttur|serrament|infissi|falegnam|pavimenti|pavimenti|parquet|marm|ponteggi|tetti|coperture|scavi|asfalt|resina|vetreria|arredament|arredo|arredi|imbianchino|cartongess|rivestiment|decorazione|insegne|vetrofanie'),
 ('metalmeccanica/industria', r'carpenteria|fabbro|lamiere|meccanic|torneria|tornitura|stampi|verniciatura|packaging|lavanderia|corderia|sollevamento|riciclaggio|depurazione|siderurgic|lavorazioni'),
 ('agricole/produttori alimentari', r'agricol|allevament|caseific|salumific|alimentar|cantina|ortofrutta|panific|pastific|riseria|risicola|caseari|frantoio|torrefaz|birrificio|formaggi|ortaggi|frutta|suini|salumi|gastronomia|patate|orticoltura|street|ingrosso ittico|prodotti ittici|vivaio'),
 ('ingrossi/trasporti/logistica', r'ingross|distribuzion|trasport|trasloch|logistic|noleggio|grossisti|cash and carry|commercio|forniture|colorificio|ferramenta|autotrasporti|autoservizi'),
 ('sanitario/sociale', r'poliambulatorio|cooperativa|\brsa\b|comunita|centro medico|dentist|soccorso|asilo nido'),
 ('studi/servizi alle imprese', r'studio tecnico|architett|ingegner|immobiliar|agenzia|tipografia|serigraf|stampa|cartotecnica|vigilanza|disinfestazione|pulizie|gestione rifiuti|onoranze|ottica'),
]
MACRO = [(n, re.compile(p, re.I)) for n, p in MACRO]
def macro(seg):
    best = None
    for i, (n, rx) in enumerate(MACRO):
        m = rx.search(seg or '')
        if m and (best is None or (m.start(), i) < best[0]): best = ((m.start(), i), n)
    return best[1] if best else 'altro'

# ---------- classificazione risposte ----------
# Tipo scritto a mano nelle sessioni precedenti (risposte-dm.csv) -> classe
TIPO = {'auto': 'auto', 'ha-il-sito': 'hasito', 'no': 'rifiuto', 'CRITICA': 'rifiuto',
        'caldo': 'positivo', 'CHIEDE': 'positivo', 'tiepido': 'positivo', 'rimanda': 'positivo',
        'ricerca': 'positivo', 'siti': 'positivo', 'cortesia': 'neutro', 'altro': 'neutro'}
# parole chiave usate per le righe che hanno solo Chat (stesso set di stato-banco.py)
AUTO = re.compile(r"grazie per aver|ti ringraziamo per|risponderemo|ti risponder|ti ricontatter|messaggio automatico|"
                  r"per prenotazion|per informazion|il prima possibile|al piu' presto|abbiamo ricevuto il tuo messaggio|"
                  r"scrivici su whatsapp|chiamaci|benvenut|autorisposta", re.I)
HASITO = re.compile(r"gia' un sito|già un sito|ce l'abbiamo|abbiamo un sito|ho gia' un sito|sito internet", re.I)
RIF = re.compile(r"non siamo interessat|non sono interessat|non mi interessa|non ci interessa|no grazie|non ne ho bisogno|"
                 r"non ne abbiamo bisogno|non abbiamo intenzione|non ci serve|per ora no", re.I)
def classe_chat(chat):
    pezzi = [p.strip() for p in chat.split('|') if p.strip()]
    if pezzi and all(AUTO.search(p) for p in pezzi): return 'auto'
    if HASITO.search(chat): return 'hasito'
    if RIF.search(chat): return 'rifiuto'
    return 'neutro'

PHONE = re.compile(r'(?<!\d)(\+39[\s.-]?)?(3\d{2}[\s.-]?\d{6,7}|0\d{1,3}[\s./-]?\d{5,8})(?!\d)')
MAIL = re.compile(r'[\w.+-]+@[\w-]+\.[a-z]{2,}', re.I)
WAPP = re.compile(r'whatsapp|\bwa\b', re.I)

def prov(c):
    m = re.search(r'\(([A-Za-z]{2})\)\s*$', c or '')
    return m.group(1).upper() if m else 'n.d.'
def fol(f):
    f = (f or '').strip()
    if not f.isdigit(): return 'n.d.'
    n = int(f)
    return '<500' if n < 500 else '500-1500' if n < 1500 else '1500-5000' if n < 5000 else '>5000'
def prodotto(r, fallback):
    p = r.get('Prodotto', '')
    if p: return p
    m = (r.get('Messaggio') or '').lower()
    if 'turni' in m or 'denkishift' in m: return 'denkishift'
    if 'bozza' in m and 'sito' in m: return 'siti'
    return fallback

# ---------- universo: tutti i DM ----------
U = {}
for r in L:
    if not r['DM inviato (data)'] and r['Account IG'] not in RISP and not r['Chat']: continue
    ch = r['Chat']
    U[r['Account IG']] = dict(acc=r['Account IG'], seg=r['Segmento'], prov=prov(r['Comune (prov)']), fol=fol(r['Follower']),
        gan=r['Gancio (1-6)'] or 'n.d.', prod=prodotto(r, 'n.d.'), data=r['DM inviato (data)'] or 'senza data',
        src='lista', scheda=r['Scheda'] + ' ' + r['Esito verifica sito'], msg=r['Messaggio'], chat=ch,
        lista=r['Lista'], letto=r['Letto (data)'])
for r in A:
    if r['Account IG'] in U: continue
    U[r['Account IG']] = dict(acc=r['Account IG'], seg=r['Segmento'], prov=prov(r['Comune (prov)']), fol=fol(r['Follower']),
        gan=r['Gancio (1-6)'] or 'n.d.', prod='siti', data='pre-8/9', src='archivio', scheda=r['Scheda'] + ' ' + r['Esito verifica sito'],
        msg=r['Messaggio'], chat='', lista='', letto='')
for u in U.values():
    u['macro'] = macro(u['seg'])
    c = None
    if u['acc'] in RISP: c = TIPO[RISP[u['acc']]['Tipo']]
    elif u['chat']: c = classe_chat(u['chat'])
    u['cl'] = c
    u['coorte'] = u['data'] in ('pre-8/9', 'senza data') or u['data'] <= CUT
    s = u['scheda']
    u['tel'] = bool(PHONE.search(s)); u['mail'] = bool(MAIL.search(s)); u['wa'] = bool(WAPP.search(s))
    u['num'] = u['tel'] or u['wa']
FUORI = [RISP[a] for a in RISP if a not in U]   # risposte di account non presenti in nessuna lista

def agg(rows, key):
    d = collections.defaultdict(lambda: collections.Counter())
    for u in rows:
        k = key(u); c = d[k]; c['n'] += 1
        if u['cl']:
            c['risp'] += 1; c[u['cl']] += 1
    return d
def pct(a, b): return f"{100*a/b:.1f}%" if b else '-'
def tab(d, minn=0, order=None):
    print(f"{'chiave':36} {'inv':>4} {'risp':>4} {'%risp':>6} {'umane':>5} {'pos':>3} {'%pos':>5} {'rif':>3} {'hasito':>6} {'auto':>4} {'neu':>3}  nota")
    ks = sorted(d, key=order or (lambda k: -d[k]['n']))
    for k in ks:
        c = d[k]
        if c['n'] < minn: continue
        um = c['risp'] - c['auto']
        print(f"{str(k):36} {c['n']:>4} {c['risp']:>4} {pct(c['risp'],c['n']):>6} {um:>5} {c['positivo']:>3} {pct(c['positivo'],c['n']):>5} {c['rifiuto']:>3} {c['hasito']:>6} {c['auto']:>4} {c['neutro']:>3}  {'n<30: non signif.' if c['n']<30 else ''}")

co = [u for u in U.values() if u['coorte']]
cmd = sys.argv[1] if len(sys.argv) > 1 else 'prodotto'
if cmd == 'coorte':
    print('universo', len(U), 'coorte', len(co), 'fuori lista (risposte senza riga):', len(FUORI), [(f['Account IG'], f['Tipo']) for f in FUORI])
    print('per data', sorted(collections.Counter(u['data'] for u in U.values()).items()))
    print('risposte totali in universo', sum(1 for u in U.values() if u['cl']), 'in coorte', sum(1 for u in co if u['cl']))
    print('risposte fuori coorte', [(u['acc'], u['data'], u['cl']) for u in U.values() if u['cl'] and not u['coorte']])
    print('prodotto nd', sum(1 for u in U.values() if u['prod'] == 'n.d.'))
    print('Chat vuota con letto', sum(1 for u in U.values() if u['letto']))
elif cmd == 'prodotto': print('COORTE'); tab(agg(co, lambda u: u['prod'])); print('TUTTI i DM (incl. non letti)'); tab(agg(U.values(), lambda u: u['prod']))
elif cmd == 'settore': tab(agg(co, lambda u: u['macro']))
elif cmd == 'settore_prod':
    d = agg(co, lambda u: (u['prod'], u['macro'])); tab(d, order=lambda k: (k[0], -d[k]['n']))
elif cmd == 'prov': tab(agg(co, lambda u: u['prov']))
elif cmd == 'follower': tab(agg(co, lambda u: u['fol']), order=lambda k: ['<500','500-1500','1500-5000','>5000','n.d.'].index(k))
elif cmd == 'gancio': tab(agg(co, lambda u: u['gan']))
elif cmd == 'contatto':
    for nome, f in (('numero/WA nella scheda', 'num'), ('email nella scheda', 'mail'), ('numero|WA|email', None)):
        print(nome); tab(agg(co, lambda u: (u['num'] or u['mail']) if f is None else u[f]))
    print('Messaggio con tel/WA/mail:', sum(1 for u in U.values() if PHONE.search(u['msg']) or MAIL.search(u['msg']) or WAPP.search(u['msg'])), 'su', len(U))
elif cmd == 'mapping':
    m = collections.defaultdict(collections.Counter)
    for u in U.values(): m[u['macro']][u['seg']] += 1
    for k, v in sorted(m.items()): print(k, sum(v.values()), '|', '; '.join(f"{s}({n})" for s, n in v.most_common(6)))
elif cmd == 'banco':
    inv = 'DM inviato (data)'
    dm = [r for r in L if not r[inv] and not re.match(r'scartat', r['Esito DM'], re.I)]
    print('da mandare', len(dm))
    print(collections.Counter(r['Prodotto'] or 'n.d.' for r in dm))
    def datalista(r):
        m = re.match(r'(\d{4}-\d{2}-\d{2})', r['Lista']); return m.group(1) if m else 'senza lista'
    c = collections.Counter((r['Prodotto'] or 'n.d.', datalista(r), re.sub(r'^\d{4}-\d{2}-\d{2}-(instagram-)?|\.csv$', '', r['Lista'])) for r in dm)
    for k, v in sorted(c.items()): print(v, k)
    print('segmenti da mandare (macro):', collections.Counter(macro(r['Segmento']) for r in dm).most_common(40))
    pa = [r for r in dm if macro(r['Segmento']) in ('unghie','estetica','ciglia/PMU','parrucchieri','barbieri','trucco/make-up')]
    print('di cui settori in pausa:', len(pa))

# ---------- gruppi: settori messi in pausa il 29/09 vs gli altri ----------
PAUSA = {'unghie', 'estetica', 'ciglia/PMU', 'parrucchieri', 'barbieri', 'trucco/make-up'}
def wilson(k, n, z=1.96):
    if not n: return (0, 0)
    p = k / n; d = 1 + z*z/n; c = p + z*z/(2*n); a = z*((p*(1-p)/n + z*z/(4*n*n))**.5)
    return ((c-a)/d, (c+a)/d)
if cmd == 'pausa':
    for nome, pool in (('siti, coorte', [u for u in co if u['prod'] == 'siti']), ('tutti i prodotti, coorte', co)):
        print(nome)
        for g, f in (('in pausa', lambda u: u['macro'] in PAUSA), ('aperti dopo, senza ristorazione', lambda u: u['macro'] not in PAUSA and u['macro'] != 'ristorazione'),
                     ('ristorazione', lambda u: u['macro'] == 'ristorazione'), ('tutti i non-pausa', lambda u: u['macro'] not in PAUSA)):
            rows = [u for u in pool if f(u)]; n = len(rows)
            r = sum(1 for u in rows if u['cl']); um = sum(1 for u in rows if u['cl'] and u['cl'] != 'auto'); p = sum(1 for u in rows if u['cl'] == 'positivo')
            rf = sum(1 for u in rows if u['cl'] == 'rifiuto'); hs = sum(1 for u in rows if u['cl'] == 'hasito')
            lo, hi = wilson(um, n); lp, hp = wilson(p, n)
            print(f"  {g:34} n={n:4} risp={r:3} ({pct(r,n)}) umane={um:3} ({pct(um,n)}, IC95 {100*lo:.1f}-{100*hi:.1f}) pos={p:2} ({pct(p,n)}, IC95 {100*lp:.1f}-{100*hp:.1f}) rif={rf} hasito={hs}")
    # settori aperti con n>=30 nella coorte, siti
if cmd == 'rotazione':
    R = rd('liste/rotazione.csv'); agg2 = collections.defaultdict(lambda: [0, 0, 0])
    for x in R:
        n = x['Nota']; mp = re.search(r'(\d+) profil', n)
        if not mp: continue
        mr = re.search(r'(\d+) righ', n) or re.search(r'(\d+) riga', n)
        if not mr: continue
        s = x['Settore']; k = (x['Lista'], s)
        agg2[k][0] += int(mp.group(1)); agg2[k][1] += int(mr.group(1)); agg2[k][2] += 1
    print(f"{'lista':8} {'settore':36} {'luoghi':>6} {'profili':>7} {'righe':>5} {'resa':>6}")
    for k, (p, r, nl) in sorted(agg2.items(), key=lambda t: (t[0][0], -t[1][1]/max(t[1][0], 1))):
        print(f"{k[0]:8} {k[1]:36} {nl:>6} {p:>7} {r:>5} {pct(r,p):>6}")
    for lst in ('siti', 'ricerca'):
        P = sum(v[0] for k, v in agg2.items() if k[0] == lst); Rr = sum(v[1] for k, v in agg2.items() if k[0] == lst); print(lst, 'totale', P, Rr, pct(Rr, P))
if cmd == 'bio':
    pat = re.compile(r'in bio[^.]{0,60}(numero|telefon|whatsapp|\b3\d{2})|bio[^.]{0,40}\b3\d{2}[\s.]?\d{6,7}', re.I)
    for nome, f in (('bio con numero/WA', lambda u: bool(pat.search(u['scheda']))), ('bio con mail', lambda u: bool(re.search(r'in bio[^.]{0,60}(mail|email)', u['scheda'], re.I)))):
        print(nome); tab(agg(co, f))
if cmd == 'senza_ristorazione':
    nr = [u for u in co if u['macro'] not in ('ristorazione', 'ospitalita (hotel/agriturismo)') and u['prod'] != 'n.d.']
    print('prov, escluse ristorazione/hotel'); tab(agg(nr, lambda u: u['prov']), minn=1)
    print('follower'); tab(agg(nr, lambda u: u['fol']))
    print('gancio'); tab(agg(nr, lambda u: u['gan']))
    print('contatto numero'); tab(agg(nr, lambda u: u['num']))
    print('contatto mail'); tab(agg(nr, lambda u: u['mail']))
