# Giro inverso, passo 2: per ogni scheda Pagine Gialle cerca la societa' nella lista companyreports del suo comune.
# Vale solo se il nome coincide parola per parola (o coincide togliendo il «di <titolare>») nello stesso comune.
import json, os, re, sys, time, unicodedata, urllib.request
from concurrent.futures import ThreadPoolExecutor
import pg, scheda, geo

HERE = os.path.dirname(os.path.abspath(__file__))
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'
LC = os.path.join(HERE, 'liste_comuni')
os.makedirs(LC, exist_ok=True)
SOGLIA = 250000


def slug(comune):
    s = unicodedata.normalize('NFKD', comune).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def pagina_comune(sl, n):
    f = os.path.join(LC, f'{sl}__{n}.json')
    if os.path.exists(f):
        return json.load(open(f))
    url = f'https://www.companyreports.it/comune/{sl}' + ('' if n == 1 else f'/{n}')
    t = ''
    for _ in range(3):
        try:
            t = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=30).read().decode('utf-8', 'ignore')
            break
        except Exception as e:
            if '404' in str(e):
                break
            time.sleep(3)
    out = []
    for blk in t.split('class="row aziende-row"')[1:]:
        m = re.search(r'href="https://www\.companyreports\.it/([a-z0-9-]+-(\d{11}))" title="Bilancio ([^"]+)"', blk)
        fm = re.search(r'Fatturato: </div>.*?<a [^>]*>([^<]+)</a>', blk, re.S)
        if not m:
            continue
        fv = fm.group(1) if fm else ''
        out.append(dict(slug=m.group(1), piva=m.group(2), nome=m.group(3),
                        fatturato=int(re.sub(r'[^0-9]', '', fv)) if re.search(r'\d', fv) else None))
    json.dump(out, open(f, 'w'), ensure_ascii=False)
    time.sleep(0.25)
    return out


def lista_comune(sl, lo=SOGLIA):
    """Tutte le societa' del comune con fatturato >= lo. Le pagine sono ordinate per fatturato decrescente."""
    tutte, n = [], 1
    # le prime pagine in sequenza per capire quanto e' profonda la lista, poi a blocchi in parallelo
    while True:
        blocco = list(range(n, n + 8))
        with ThreadPoolExecutor(4) as ex:
            pagine = list(ex.map(lambda k: pagina_comune(sl, k), blocco))
        fine = False
        for p in pagine:
            if not p:
                fine = True
                break
            tutte += p
            fats = [x['fatturato'] for x in p if x['fatturato']]
            if not fats or max(fats) < lo:
                fine = True
                break
        if fine:
            return tutte
        n += 8


def senza_titolare(nome):
    return re.split(r'\bdi\b', pg.norm(nome))[0]


def abbina(v, lista):
    tk = set(pg.tokens(v['nome']))
    base = set(pg.tokens(senza_titolare(v['nome'])))
    for c in lista:
        ct = set(pg.tokens(c['nome']))
        if ct and ct == tk:
            return 'esatto', c
    for c in lista:
        ct = set(pg.tokens(senza_titolare(c['nome'])))
        if ct and base and ct == base and len(''.join(ct)) >= 5:
            return 'senza-titolare', c
    return None, None


if __name__ == '__main__':
    IN = sys.argv[2] if len(sys.argv) > 2 else 'pg_categorie.json'
    OUTF = sys.argv[3] if len(sys.argv) > 3 else 'pg_abbinate.json'
    pgs = json.load(open(os.path.join(HERE, IN)))
    for v in pgs:
        m = re.search(r'\d{5}\s+(.*?)\s*\((\w\w)\)$', v['adr'])
        v['comune_op'], v['prov_op'] = (m.group(1), m.group(2)) if m else (None, None)
        c = geo.coord(v['comune_op'], v['prov_op']) if v['comune_op'] else None
        v['km_comune'] = round(geo.km(c), 1) if c else None
    comuni = sorted({(v['comune_op'], v['km_comune']) for v in pgs if v['comune_op'] and v['km_comune'] is not None}, key=lambda x: x[1])
    maxkm = float(sys.argv[1]) if len(sys.argv) > 1 else 60
    liste = {}
    for com, k in comuni:
        if k > maxkm:
            break
        liste[com] = lista_comune(slug(com))
        print(f'{k:5} {com}: {len(liste[com])} societa sopra soglia', flush=True)
    for v in pgs:
        v['cr_esito'], v['cr'] = abbina(v, liste.get(v['comune_op'], [])) if v['comune_op'] in liste else (None, None)
        if v['cr']:
            scheda.leggi(v['cr'])
    json.dump(pgs, open(os.path.join(HERE, OUTF), 'w'), ensure_ascii=False)
    print('abbinate', sum(1 for v in pgs if v['cr']), 'su', len(pgs))
