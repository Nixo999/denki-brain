# Unisce i due giri (ATECO -> Pagine Gialle, Pagine Gialle -> bilancio), tiene solo il settore giusto,
# misura la distanza sull'indirizzo e ordina da Seveso verso fuori.
import json, os, re
import costruisci, geo

HERE = os.path.dirname(os.path.abspath(__file__))
LO, HI = 250000, 10000000

# Giro 1: il codice ATECO dice il settore, la categoria di Pagine Gialle conferma che e' la stessa societa' e che fa quello.
CAT_OK = {
    '52.24.4': ('facchinaggio', 'cooperative produzione, lavoro e servizi', 'consorzi', 'imprese di pulizia',
                'magazzinaggio', 'ricerca e selezione del personale'),
    '77.39.94': ('eventi e manifestazioni', 'audiovisivi apparecchi ed impianti', 'illuminazione', 'amplificazione'),
    '82.3': ('eventi e manifestazioni - impianti ed attrezzature', 'amplificazione'),
    '90.02.09': ('eventi e manifestazioni - impianti ed attrezzature', 'amplificazione'),
    '52.24': ('facchinaggio', 'cooperative produzione, lavoro e servizi', 'consorzi', 'imprese di pulizia',
              'magazzinaggio', 'ricerca e selezione del personale'),
    '90.02.01': ('eventi e manifestazioni', 'audiovisivi apparecchi ed impianti', 'illuminazione', 'amplificazione'),
    '16.23.21': ('eventi e manifestazioni - impianti ed attrezzature',),
}
# attivita' prevalenti che smentiscono la categoria di Pagine Gialle: immobiliare, stampa, elettronica, ingrosso, edilizia
FUORI = {'68', '18', '26', '46', '41', '47', '56', '58', '62', '64', '66', '69', '70', '86'}
SETT = {'52.24.4': 'Facchinaggio', '77.39.94': 'Allestimento', '82.3': 'Allestimento', '90.02.09': 'Allestimento',
        '52.24': 'Facchinaggio', '90.02.01': 'Allestimento', '16.23.21': 'Allestimento'}


def riga(cr, pgr, settore, fonte, livello):
    return dict(piva=cr['piva'], slug=cr['slug'], nome=cr['nome'], fatturato=cr['fatturato'], anno=cr.get('anno'),
                personale=cr.get('personale'), dipendenti=cr.get('dipendenti'), stato=cr.get('stato'), forma=cr.get('forma'),
                ateco=cr.get('ateco'), attivita=cr.get('attivita'), indirizzo_legale=cr.get('indirizzo'),
                settore=settore, pg=pgr, fonte=fonte, livello=livello)


# Lista solo facchinaggio: chi arriva dalla categoria di Pagine Gialle deve avere un'attivita' prevalente compatibile
# (movimentazione e logistica, servizi integrati e pulizia, imballaggio conto terzi, servizi alle imprese, lavoro)
FACCH_OK = ('52', '81', '82.92', '82.99', '78')


def tutte(solo=None, pg_files=('pg_abbinate.json',)):
    out, scarti = {}, []
    for x in json.load(open(os.path.join(HERE, 'trovate.json'))).values():
        if x.get('scartata') or not x.get('esito'):
            continue
        if solo and SETT[x['ateco_lista']] != solo:
            continue
        cat = x['pg']['cat'].lower()
        if not any(k in cat for k in CAT_OK[x['ateco_lista']]):
            scarti.append((x['nome'], x['ateco_lista'], x['pg']['cat'], 'categoria PG incoerente col codice ATECO'))
            continue
        if x['esito'] == 'altra-sede':
            m = re.search(r'\d{5}\s+(.*?)\s*\((\w\w)\)', x['pg']['adr'])
            a, b = geo.coord(x['comune_nome'], x['prov']), (geo.coord(m.group(1), m.group(2)) if m else None)
            if not a or not b or geo.km(a, b) > 25:
                scarti.append((x['nome'], x['ateco_lista'], x['pg']['adr'], 'omonimo probabile: sede legale lontana dalla scheda PG'))
                continue
        out[x['piva']] = riga(x, x['pg'], SETT[x['ateco_lista']], 'ateco', x['esito'])
    pgs = [v for f in pg_files if os.path.exists(os.path.join(HERE, f)) for v in json.load(open(os.path.join(HERE, f)))]
    for v in pgs:
        cr = v.get('cr')
        if not cr or cr['piva'] in out or (solo and v['settore'] != solo):
            continue
        pgr = {k: v[k] for k in ('nome', 'cat', 'adr', 'tel', 'link')}
        out[cr['piva']] = riga(cr, pgr, v['settore'], 'categoria', v['cr_esito'])
    tenute = []
    for r in out.values():
        if r['stato'] != 'Attiva':
            scarti.append((r['nome'], r['settore'], r['stato'], 'non attiva')); continue
        if 'LIQUIDAZ' in r['nome'].upper():
            scarti.append((r['nome'], r['settore'], '', 'in liquidazione')); continue
        if not r['fatturato'] or not LO <= r['fatturato'] <= HI:
            scarti.append((r['nome'], r['settore'], r['fatturato'], 'fatturato fuori fascia')); continue
        if r['personale'] is not None and r['personale'] < 60000:
            scarti.append((r['nome'], r['settore'], r['personale'], 'costo del personale sotto 60.000 euro: niente squadra')); continue
        if r['fonte'] == 'categoria' and (r['ateco'] or '').split('.')[0] in FUORI:
            scarti.append((r['nome'], r['settore'], r['ateco'], 'attivita prevalente fuori settore')); continue
        if solo == 'Facchinaggio' and r['fonte'] == 'categoria' and not (r['ateco'] or '').startswith(FACCH_OK):
            scarti.append((r['nome'], r['settore'], r['ateco'], 'attivita prevalente non di facchinaggio')); continue
        if r['piva'] in ('09191930156',):
            scarti.append((r['nome'], r['settore'], '', 'BluNotte, gia\' nel giro di Seba')); continue
        tenute.append(r)
    # un centralino, una riga
    tenute.sort(key=lambda r: -r['fatturato'])
    visti, uniche = set(), []
    for r in tenute:
        t = r['pg']['tel'][0]
        if t in visti:
            scarti.append((r['nome'], r['settore'], t, 'stesso centralino di un\'altra riga')); continue
        visti.add(t)
        uniche.append(r)
    for r in uniche:
        r['comune'], r['prov'] = costruisci.comune_pg(r['pg']['adr'])
        c = geo.coord(r['comune'], r['prov']) if r['comune'] else None
        r['km'], r['km_da'] = costruisci.km_indirizzo(r['pg']['adr'], round(geo.km(c), 1) if c else None)
        p = costruisci.GCACHE.get(r['pg']['adr'])
        if p and c and geo.km(p, c) > 7:
            r['km'], r['km_da'] = round(geo.km(c), 1), 'comune (indirizzo non trovato)'
    uniche = [r for r in uniche if r['km'] is not None] + [r for r in uniche if r['km'] is None]
    uniche.sort(key=lambda r: (r['km'] is None, r['km'] or 0, -r['fatturato']))
    return uniche, scarti


if __name__ == '__main__':
    import sys
    SOLO = sys.argv[1] if len(sys.argv) > 1 else None
    OUTF = sys.argv[2] if len(sys.argv) > 2 else 'finale.json'
    u, s = tutte(SOLO, ('pg_abbinate.json', 'pg_abbinate_f.json') if SOLO else ('pg_abbinate.json',))
    import collections
    print('tenute', len(u), collections.Counter(r['settore'] for r in u), 'senza km', sum(1 for r in u if r['km'] is None))
    print(collections.Counter(x[3] for x in s))
    for r in u[:110]:
        print(r['km'], r['km_da'], r['comune'], '|', r['nome'][:42], '|', r['settore'], '|', r['pg']['cat'][:40], '|', r['fatturato'], r['fonte'], r['livello'])
    json.dump(dict(tenute=u, scarti=s), open(os.path.join(HERE, OUTF), 'w'), ensure_ascii=False)
