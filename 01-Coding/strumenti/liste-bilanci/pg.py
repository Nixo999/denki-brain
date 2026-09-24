# Telefono da Pagine Gialle, con la regola della lista del 17/09:
# vale solo se il nome coincide parola per parola E l'indirizzo e' nel comune giusto.
# Secondo livello, dichiarato nella prova: nome in parte uguale E stessa via della sede legale.
import re, html, urllib.parse, unicodedata
import cr_ateco

FORME = set('''s r l srl srls sas snc spa p a sapa ss societa cooperativa coop soc sc scarl scrl arl rl responsabilita limitata
semplificata in liquidazione unipersonale per azioni consortile con socio unico impresa sociale onlus abbreviabile
abbreviata forma breve siglabile sigla o ed di del della e & and the'''.split())


def norm(s):
    s = unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode().lower()
    s = s.replace('&', ' e ').replace("'", ' ')
    return re.sub(r'[^a-z0-9 ]', ' ', re.sub(r'(?<=\b[a-z])\.(?=[a-z]\b)', '', s))


def tokens(nome):
    t = norm(nome).split()
    # sigle puntate: "S.R.L." diventa "s r l", "G.M." diventa "g m" -> ricompone le lettere singole consecutive
    out, buf = [], ''
    for w in t:
        if len(w) == 1:
            buf += w
        else:
            if buf: out.append(buf); buf = ''
            out.append(w)
    if buf: out.append(buf)
    return [w for w in out if w not in FORME]


def via(ind):
    t = [w for w in norm(ind).split() if not w.isdigit() and w not in ('via', 'viale', 'piazza', 'piazzale', 'corso', 'largo', 'strada', 'str', 'v', 'le', 'p', 'za', 'snc', 'sn', 'ss', 'statale', 'provinciale', 'sp', 'loc', 'localita', 'frazione', 'fraz', 'dei', 'del', 'della', 'delle', 'di', 'da', 'san', 's')]
    return set(t)


def cerca(query, comune):
    url = 'https://www.paginegialle.it/ricerca/' + urllib.parse.quote(query) + '/' + urllib.parse.quote(comune)
    t = cr_ateco.get(url, delay=1.2)
    t = t.split('section-similar__title')[0]  # le «attivita' simili» sotto non sono risultati
    out = []
    for blk in t.split('class="search-itm card-listing')[1:]:
        g = lambda rx: (lambda m: html.unescape(re.sub(r'\s+', ' ', re.sub(r'<!--.*?-->|<[^>]+>', ' ', m.group(1)))).strip() if m else '')(re.search(rx, blk, re.S))
        nome = g(r'search-itm__rag[^>]*>(.*?)</h2>')
        cat = g(r'search-itm__category[^>]*>(.*?)</div>')
        adr = re.sub(r'<[^>]+>', ' ', g(r'search-itm__adr[^>]*>.*?</svg>(.*?)</div>\s*</div>'))
        adr = re.sub(r'\s+', ' ', adr).strip()
        tel = [html.unescape(x).strip() for x in re.findall(r'search-itm__phone-item">([^<]+)<', blk)]
        m = re.search(r'href="(https://www\.paginegialle\.it/[^"]+)"', blk)
        link = m.group(1) if m else ''
        out.append(dict(nome=nome, cat=cat, adr=adr, tel=tel, link=link))
    return url, out


SETTORE_PG = {
    'facchinaggio': ('facchin', 'trasloc', 'magazzin', 'logistic', 'movimentazione', 'trasporti', 'spedizion'),
    'allestimento': ('allestiment', 'stand', 'fiere', 'mostre', 'palchi', 'strutture', 'eventi e manifestazioni', 'audiovisivi',
                     'service', 'noleggio', 'scenograf', 'tende', 'gazebo', 'luci', 'illuminazion', 'amplificazione', 'spettacol'),
}


def trova(az, settore=None):
    """az: dict con nome, comune_nome, prov, indirizzo. Ritorna (esito, risultato, prova)."""
    tk = tokens(az['nome'])
    if not tk:
        return None, None, 'nome vuoto dopo le forme giuridiche'
    q = ' '.join(tk)
    url, res = cerca(q, az['comune_nome'].lower())
    com = norm(az['comune_nome']).split()
    v = via(az.get('indirizzo') or '')
    for r in res:
        if not r['tel']:
            continue
        a = norm(r['adr'])
        nel_comune = (' '.join(com) in a) and (f"({az['prov'].lower()})" in r['adr'].lower() or az['prov'].lower() in a.split())
        if not nel_comune:
            continue
        tr = tokens(r['nome'])
        if set(tr) == set(tk):
            return 'esatto', r, f"PG «{q}» in {az['comune_nome'].lower()} → {r['nome']} | {r['adr']}"
        vr = via(r['adr'].split(' - ')[0])
        if set(tr) & set(tk) and v and vr and (v <= vr or vr <= v):
            return 'via', r, f"PG «{q}» in {az['comune_nome'].lower()} → {r['nome']} | {r['adr']} (nome in parte diverso, stessa via della sede legale)"
    # terzo livello: nome identico e distintivo (almeno due parole), sede operativa in un altro comune,
    # categoria di Pagine Gialle coerente col settore
    if settore and len(tk) >= 2:
        for r in res:
            if r['tel'] and set(tokens(r['nome'])) == set(tk) and any(k in r['cat'].lower() for k in SETTORE_PG[settore]):
                return 'altra-sede', r, f"PG «{q}» → {r['nome']} | {r['adr']} | {r['cat']} (nome identico, sede operativa diversa dalla sede legale di {az['comune_nome']})"
    return None, None, f"PG «{q}» in {az['comune_nome'].lower()}: {len(res)} risultati, nessuno con nome e comune coincidenti"
