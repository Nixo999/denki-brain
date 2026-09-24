# Scarica le liste companyreports per codice ATECO: nome, slug, fatturato, comune, provincia.
# Uso: python3 cr_ateco.py <codice> [soglia_minima]
import re, html, json, sys, time, os, hashlib, urllib.request

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'cache')
os.makedirs(CACHE, exist_ok=True)


def get(url, delay=0.4):
    f = os.path.join(CACHE, hashlib.md5(url.encode()).hexdigest() + '.html')
    if os.path.exists(f):
        return open(f, encoding='utf-8', errors='ignore').read()
    for _ in range(3):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'it-IT,it'}), timeout=30)
            t = r.read().decode('utf-8', 'ignore')
            open(f, 'w').write(t)
            time.sleep(delay)
            return t
        except Exception as e:
            print('ERR', url, e, file=sys.stderr)
            time.sleep(3)
    return ''


def page(code, n):
    url = f'https://www.companyreports.it/ateco/{code}' + ('' if n == 1 else f'/{n}')
    t = get(url)
    out = []
    for blk in t.split('class="row aziende-row"')[1:]:
        m = re.search(r'href="https://www\.companyreports\.it/([a-z0-9-]+-(\d{11}))" title="Bilancio ([^"]+)"', blk)
        if not m:
            continue
        slug, piva, full = m.groups()
        f = re.search(r'Fatturato: </div>.*?<a [^>]*>([^<]+)</a>', blk, re.S)
        c = re.search(r'comune/([a-z0-9-]+)"[^>]*>([^<]+)</a>\s*<a [^>]*>\(([A-Z]{2})\)', blk)
        fv = f.group(1).strip() if f else 'N.D.'
        fat = int(re.sub(r'[^0-9]', '', fv)) if re.search(r'\d', fv) else None
        out.append(dict(slug=slug, piva=piva, nome=html.unescape(full).strip(), fatturato=fat,
                        comune=c.group(1) if c else None,
                        comune_nome=html.unescape(c.group(2)).strip() if c else None,
                        prov=c.group(3) if c else None, ateco_lista=code))
    return out


def scarica(code, lo=250000):
    allr, n = [], 1
    while n < 300:
        rows = page(code, n)
        if not rows:
            break
        allr += rows
        fats = [r['fatturato'] for r in rows if r['fatturato']]
        if not fats or max(fats) < lo:
            break
        n += 1
    json.dump(allr, open(os.path.join(HERE, f'ateco_{code}.json'), 'w'), ensure_ascii=False)
    return n, allr


if __name__ == '__main__':
    code = sys.argv[1]
    lo = int(sys.argv[2]) if len(sys.argv) > 2 else 250000
    n, allr = scarica(code, lo)
    print(code, 'pagine', n, 'righe', len(allr))
