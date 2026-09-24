# Dalle trovate al file per Seba: classifica, distanza sull'indirizzo, 100 da chiamare + riserva.
import json, re, csv, os, sys, time, urllib.request, urllib.parse
import geo

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
BASE = '2026-09-24-opero-facchinaggio-allestimento'

# Per 82.3 e 90.02.09 (organizzazione fiere ed eventi, supporto allo spettacolo) il codice ATECO non basta:
# dentro ci sono anche agenzie, promoter e congressi. Resta solo chi su Pagine Gialle si dichiara allestitore.
ALLESTIMENTO_PG = ('allestiment', 'stand', 'fiere e mostre', 'palchi', 'tensostruttur', 'strutture', 'impianti ed attrezzature',
                   'audiovisivi', 'amplificazione', 'illuminazion', 'luci', 'gazebo', 'tende', 'scenograf', 'noleggio', 'service')

GANCIO = {
    'Facchinaggio': "Squadre su piu' commesse ogni giorno. Chi va dove e quante ore ha fatto, senza il giro di telefonate la sera prima.",
    'Allestimento': "Montaggi e smontaggi su piu' cantieri nella stessa settimana. Squadra, orari e ore da fatturare al cliente in un posto solo.",
}


def settore(x):
    cat = ((x.get('pg') or {}).get('cat') or '').lower()
    if x['ateco_lista'] == '52.24.4':
        return 'Facchinaggio'
    if x['ateco_lista'] == '77.39.94':
        return 'Allestimento'
    if any(k in cat for k in ALLESTIMENTO_PG):
        return 'Allestimento'
    return None


GC = os.path.join(HERE, 'coord_indirizzi.json')
GCACHE = json.load(open(GC)) if os.path.exists(GC) else {}


def km_indirizzo(adr, fallback):
    """Distanza in linea d'aria da Seveso all'indirizzo di Pagine Gialle; se non si trova, il centro del comune."""
    if adr not in GCACHE:
        m = re.match(r'(.*?),?\s*(\d+[A-Za-z/]*)?\s*-\s*(\d{5})\s+(.*?)\s*\(([A-Z]{2})\)', adr)
        r = []
        if m:
            q = urllib.parse.urlencode({'street': f"{m.group(2) or ''} {m.group(1)}".strip(), 'postalcode': m.group(3),
                                        'city': m.group(4), 'country': 'Italy', 'format': 'json', 'limit': 1})
            try:
                r = json.load(urllib.request.urlopen(urllib.request.Request('https://nominatim.openstreetmap.org/search?' + q,
                                                                            headers={'User-Agent': 'DenkiCode-liste/1.0'}), timeout=30))
            except Exception as e:
                print('geo', adr, e)
            time.sleep(1.1)
        GCACHE[adr] = [float(r[0]['lat']), float(r[0]['lon'])] if r else None
        json.dump(GCACHE, open(GC, 'w'), ensure_ascii=False)
    c = GCACHE[adr]
    return (round(geo.km(c), 1), 'indirizzo') if c else (fallback, 'comune')


def comune_pg(adr):
    m = re.search(r'\d{5}\s+(.*?)\s*\(([A-Z]{2})\)', adr or '')
    return (m.group(1), m.group(2)) if m else (None, None)


def righe():
    d = json.load(open(os.path.join(HERE, 'trovate.json')))
    tenute, scartate_settore = [], []
    for x in d.values():
        if x.get('scartata') or not x.get('esito'):
            continue
        s = settore(x)
        if not s:
            scartate_settore.append(x)
            continue
        x['settore'] = s
        tenute.append(x)
    # un centralino, una riga: le societa' dello stesso gruppo sullo stesso numero restano una
    tenute.sort(key=lambda x: -(x['fatturato'] or 0))
    visti, uniche = set(), []
    for x in tenute:
        t = x['pg']['tel'][0]
        if t in visti:
            continue
        visti.add(t)
        uniche.append(x)
    for x in uniche:
        x['km_adr'], x['km_da'] = km_indirizzo(x['pg']['adr'], x['km'])
        x['comune_op'], x['prov_op'] = comune_pg(x['pg']['adr'])
    uniche.sort(key=lambda x: (x['km_adr'], -(x['fatturato'] or 0)))
    return uniche, scartate_settore


if __name__ == '__main__':
    u, s = righe()
    print('tenute', len(u), 'fuori settore', len(s))
    for x in u[:120]:
        print(x['km_adr'], x['km_da'], x['comune_op'], '|', x['nome'][:45], '|', x['settore'], '|', x['pg']['cat'][:50], '|', x['fatturato'], x['esito'])
