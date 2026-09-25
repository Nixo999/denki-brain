# Giro inverso: le schede di Pagine Gialle delle due categorie, raccolte da piu' comuni attorno a Seveso.
import json, re, html, sys
from concurrent.futures import ThreadPoolExecutor
import cr_ateco, pg

CATEGORIE = {
    'Facchinaggio, carico e scarico merci, portabagagli': 'Facchinaggio',
    'Eventi e manifestazioni - impianti ed attrezzature': 'Allestimento',
}
QUERY = ['facchinaggio', 'allestimenti fieristici', 'allestimento stand', 'allestimenti eventi', 'movimentazione merci',
         'facchinaggio industriale', 'stand fieristici', 'allestimenti fiere']
ANCORE = ['seveso', 'seregno', 'desio', 'monza', 'lissone', 'cantu', 'como', 'saronno', 'vimercate', 'cinisello balsamo',
          'sesto san giovanni', 'rho', 'legnano', 'busto arsizio', 'varese', 'lecco', 'bergamo', 'milano', 'arcore',
          'mariano comense', 'erba', 'merate', 'gallarate', 'bollate', 'paderno dugnano', 'brugherio', 'agrate brianza']


def pagina(q, a, n):
    url = f'https://www.paginegialle.it/ricerca/{q.replace(" ", "%20")}/{a.replace(" ", "%20")}' + ('' if n == 1 else f'/p-{n}')
    t = cr_ateco.get(url, delay=0.8)
    t = t.split('section-similar__title')[0]
    out = []
    for blk in t.split('class="search-itm card-listing')[1:]:
        g = lambda rx: (lambda m: html.unescape(re.sub(r'\s+', ' ', re.sub(r'<!--.*?-->|<[^>]+>', ' ', m.group(1)))).strip() if m else '')(re.search(rx, blk, re.S))
        m = re.search(r'href="(https://www\.paginegialle\.it/[^"]+)"', blk)
        adr = re.sub(r'\s+', ' ', g(r'search-itm__adr[^>]*>.*?</svg>(.*?)</div>\s*</div>')).strip()
        out.append(dict(nome=g(r'search-itm__rag[^>]*>(.*?)</h2>'), cat=g(r'search-itm__category[^>]*>(.*?)</div>'), adr=adr,
                        tel=[html.unescape(x).strip() for x in re.findall(r'search-itm__phone-item">([^<]+)<', blk)],
                        link=m.group(1) if m else '', dist=g(r'search-itm__dist[^>]*>\s*<span>([^<]+)</span>'),
                        query=q, ancora=a))
    return out


def raccogli(qa):
    q, a = qa
    res = []
    for n in range(1, 11):
        r = pagina(q, a, n)
        if not r:
            break
        res += r
        if not any(x['cat'] in CATEGORIE for x in r):
            break
    return res


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'facchinaggio':
        # solo facchinaggio, ancore oltre la cintura di Seveso
        CATEGORIE.pop('Eventi e manifestazioni - impianti ed attrezzature')
        QUERY = ['facchinaggio', 'facchinaggio industriale', 'movimentazione merci', 'cooperativa facchinaggio']
        ANCORE = ANCORE + ['novara', 'pavia', 'lodi', 'cremona', 'crema', 'treviglio', 'brescia', 'piacenza', 'vercelli', 'biella',
                           'torino', 'alessandria', 'genova', 'verona', 'mantova', 'parma', 'reggio emilia', 'modena', 'bologna',
                           'vigevano', 'voghera', 'sondrio', 'chivasso', 'asti', 'savona', 'vicenza', 'padova']
    OUT = 'pg_categorie_f.json' if len(sys.argv) > 1 else 'pg_categorie.json'
    jobs = [(q, a) for a in ANCORE for q in QUERY]
    with ThreadPoolExecutor(3) as ex:
        tutte = [x for r in ex.map(raccogli, jobs) for x in r]
    schede = {}
    for x in tutte:
        if x['cat'] in CATEGORIE and x['tel'] and x['link']:
            schede.setdefault(x['link'], dict(x, settore=CATEGORIE[x['cat']]))
    json.dump(list(schede.values()), open(OUT, 'w'), ensure_ascii=False)
    import collections
    print('righe', len(tutte), 'schede uniche nelle due categorie', len(schede))
    print(collections.Counter(v['settore'] for v in schede.values()))
    print(collections.Counter(re.sub(r'.*\((\w\w)\)$', r'\1', v['adr']) for v in schede.values()).most_common())
