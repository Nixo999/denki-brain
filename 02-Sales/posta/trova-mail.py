#!/usr/bin/env python3
"""Per ogni azienda in fase `nuova` cerca il sito e la casella di posta generica.

    python3 02-Sales/posta/trova-mail.py [--max N] [--paralleli 6] [--senza-pg] [--riprova]

1. Il sito. La base sono i domini indovinati dal nome (rossimeccanica.it,
   rossi-meccanica.com, rossimeccanicasrl.it ...), come in
   02-Sales/strumenti/verifica-sito.py, senza motori di ricerca: DuckDuckGo e
   Brave senza chiave si bloccano dopo poche decine di richieste. La prova
   forte è la partita IVA nella pagina: se c'è, il sito è dell'azienda. Senza
   partita IVA il sito vale solo se porta tutte le parole del nome e il comune.
   Se i domini indovinati non danno niente, seconda strada lenta: Pagine
   Gialle (una richiesta ogni 8 secondi, si ferma da sola al primo 429).
2. La casella. Home più le pagine contatti / chi siamo / dove siamo (link
   interni con quelle parole, più /contatti e /contact). Si leggono anche i
   `mailto:`, gli indirizzi protetti da Cloudflare e le forme «info [at]».
   Restano solo le caselle generiche sul dominio dell'azienda, con record MX.
   Fuori le PEC e le caselle con il nome di una persona.
3. La prova: `sito_prova` dice come è stato trovato il sito (o perché no),
   `email_prova` è l'URL esatto della pagina dove sta l'indirizzo. Un sito
   che non risponde è scritto come tale: non è un «senza sito» certo.
4. `estratto`: il testo della home e della pagina chi siamo, max 1500 caratteri.
5. Fase finale `pronta`, `senza_sito` o `senza_mail`. Due aziende con lo
   stesso sito o la stessa casella: resta quella col fatturato più alto,
   l'altra va `scartata` con il motivo (e la casella finisce in `note`,
   perché in base dati una casella può stare su una riga sola).

Idempotente: lavora solo le righe `nuova`, e ogni riga si salva appena finita.
`--riprova` rimette in coda le `senza_sito` e `senza_mail` la cui prova dice
che un sito non rispondeva o che Pagine Gialle era bloccata.
"""
import argparse, hashlib, html, json, os, re, socket, ssl, subprocess, sys, threading, time, unicodedata
import urllib.error, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
import db  # noqa: E402

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'
SSL = ssl.create_default_context()
SSL.check_hostname = False
SSL.verify_mode = ssl.CERT_NONE

# Portali e directory: un dominio che finisce qui non è il sito dell'azienda.
# Presi da verifica-sito.py, con le directory di imprese che contano per il B2B.
DIRECTORY = re.compile(
    r'(instagram|facebook|linkedin|youtube|twitter|tiktok|google|paginegialle|pagine-gialle|paginebianche|'
    r'companyreports|reportaziende|registroaziende|ufficiocamerale|informazione-aziende|icribis|atoka|kompass|'
    r'europages|misterimprese|cylex|infobel|aziende\.it|bluaziende|visurissima|empresite|dnb\.com|'
    r'firmania|reteimprese|elencoimpreseitaliane|aziendit|trovaprezzi|amazon|ebay|subito\.it|wikipedia|'
    r'virgilio|tuttocitta|pagineaziende|telefono\.click|italiaonline|sedo\.com|dan\.com|afternic|'
    r'godaddy|hugedomains|aruba\.it|register\.it|siteground|wix\.com|wordpress\.com|dropcatch|'
    r'abovedomains|bodis|parkingcrew|sedoparking|domainmarket|undeveloped)', re.I)
PARCHEGGIO_HTML = re.compile(r'abovedomains|parkingcrew|bodis\.com|sedoparking|forsale\.min\.js|'
                             r'domain-for-sale|parked-content', re.I)
PARCHEGGIO = re.compile(
    r'(apache2? (ubuntu |debian )?default page|it works!|index of /|coming soon|domain (is )?for sale|'
    r'questo dominio|dominio (è stato )?registrato|sito in costruzione|under construction|presto online|'
    r'parked|default web site page|plesk|cpanel|web server.{0,20}default|this domain|buy this domain|'
    r'account suspended|sito sospeso|work in progress|lavori in corso|in vendita|premium domain|'
    r'is available for purchase|make an offer)', re.I)
ANTIBOT = re.compile(r'(just a moment|attention required|cf-browser-verification|captcha|access denied)', re.I)

# Le caselle generiche, nell'ordine in cui si preferiscono.
GENERICHE = ['info', 'commerciale', 'ufficio', 'segreteria', 'contatti', 'vendite', 'amministrazione',
             'sales', 'office', 'ordini', 'preventivi', 'mail', 'posta']
RX_GENERICA = re.compile(r'^(' + '|'.join(GENERICHE) + r')([._-]?[a-z0-9]{0,20})$')
RX_PEC_DOMINIO = re.compile(r'(^|\.)(pec|cert|legalmail|postacert|arubapec|pecimprese|registerpec|'
                            r'sicurezzapostale|casellapec|pec-mail|mypec)(\.|$)|legalmail|arubapec|postacert|'
                            r'pecimprese|sicurezzapostale', re.I)
RX_PEC_LOCALE = re.compile(r'(^|[._-])pec([._-]|$)|^pec|pec$|^cert[._-]|[._-]cert$', re.I)

# Parole che nel nome di una società non fanno il dominio, e parole troppo generiche per un dominio da sole.
FORME = set('''srl srls spa sapa sas snc ss scarl scrl sc arl rl soc societa cooperativa coop consortile
unipersonale socio unico in liquidazione semplificata responsabilita limitata per azioni con impresa
sociale onlus siglabile sigla breve abbreviabile abbreviata forma o ed di del della dei delle e the and
a la il lo le gli i'''.split())
TAGLIO = set('srl srls spa sapa sas snc scarl scrl sc soc societa cooperativa coop consortile unipersonale'.split())
GENERICHE_NOME = set('''officina officine meccanica meccaniche costruzioni costruzione industria industrie
industriale italia italiana italiano group gruppo impianti service servizi commerciale tecnica tecnologie
nuova nuovo general generale international internazionale europa euro sistemi system systems tecno metal
metalli lavorazioni lavorazione trading forniture fornitura distribuzione ingrosso'''.split())

# Sigle di paese che, in coda a una casella (info.de@, sales.il@) o come sottodominio (de.helu.com),
# dicono che la casella è di un'altra filiale. Fuori le sigle che sono anche province italiane
# (BG, CO, CR, LC, MN, SO, VA, BS ...), perché info.bg@ può essere l'ufficio di Bergamo.
PAESI = set('''de fr es uk gb us cn ch at nl be pl cz ro hu pt se dk fi no jp kr in br mx tr ru ae sg au ca il
za ar cl gr ie lu sk si hr rs ua ma eg sa qa hk tw th my id ph vn nz'''.split())

TLD = ('.it', '.com', '.eu', '.net')
PAGINE_UTILI = re.compile(r'contatt|contact|chi[-_ ]?siamo|chisiamo|about|azienda|company|dove[-_ ]?siamo|'
                          r'dovesiamo|where|storia|profilo|who-we-are|impressum|sede', re.I)
PAGINE_LEGALI = re.compile(r'privacy|note[-_ ]?legali|legal|imprint|impressum|cookie|dati[-_ ]?societari|'
                           r'informazioni[-_ ]?societarie|termini|condizioni', re.I)
PERCORSI_CONTATTI = ['/contatti', '/contatti/', '/contact', '/contact/', '/contacts', '/it/contatti']
MAX_PAGINE = 6

CACHE_PG = os.path.join(db.DATI, 'cache', 'pg')


# ---------------------------------------------------------------- rete

def scarica(url, timeout=12):
    """(url finale, testo html) oppure (None, motivo dell'errore). Un errore di DNS si riprova:
    il 18/10/2026, con sei ricerche in parallelo, il resolver del Mac ha dato «nodename nor
    servname» a domini vivi (hamamatsu.com, romanicomponents.it) che un minuto dopo rispondevano."""
    for tentativo in range(3):
        fin, t = _scarica(url, timeout)
        if fin or 'nodename' not in t:
            return fin, t
        time.sleep(2 + 3 * tentativo)
    return fin, t


def _scarica(url, timeout):
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers={
            'User-Agent': UA, 'Accept-Language': 'it-IT,it;q=0.9,en;q=0.5',
            'Accept': 'text/html,application/xhtml+xml'}), timeout=timeout, context=SSL)
        grezzo = r.read(2_000_000)
        tipo = r.headers.get('Content-Type', '')
        if tipo and 'html' not in tipo and 'text' not in tipo:
            return None, f'non html ({tipo.split(";")[0]})'
        cs = re.search(r'charset=([\w-]+)', tipo) or re.search(rb'<meta[^>]+charset=["\']?([\w-]+)', grezzo[:4000], re.I)
        cs = cs.group(1) if cs else 'utf-8'
        cs = cs.decode() if isinstance(cs, bytes) else cs
        try:
            testo = grezzo.decode(cs, 'replace')
        except LookupError:
            testo = grezzo.decode('utf-8', 'replace')
        return r.geturl(), testo
    except urllib.error.HTTPError as e:
        if e.code in (403, 503):
            try:
                corpo = e.read(20000).decode('utf-8', 'ignore')
                if ANTIBOT.search(corpo):
                    return None, f'http {e.code} pagina anti-bot'
            except Exception:
                pass
        return None, f'http {e.code}'
    except Exception as e:
        m = str(getattr(e, 'reason', e))
        if 'timed out' in m or isinstance(e, socket.timeout):
            return None, 'non risponde (timeout)'
        return None, 'non risponde (' + m[:60] + ')'


_dns, _dns_lock = {}, threading.Lock()


def risolve(host):
    """True se il nome ha un indirizzo, False se non esiste, None se il DNS non ha risposto.
    Prima Cloudflare DoH (1.1.1.1, NXDOMAIN distinto dal silenzio), poi il resolver del Mac:
    sotto carico quello del Mac risponde «non esiste» anche a domini vivi."""
    with _dns_lock:
        if host in _dns:
            return _dns[host]
    esito = None
    try:
        r = urllib.request.urlopen(urllib.request.Request(
            'https://1.1.1.1/dns-query?type=A&name=' + urllib.parse.quote(host),
            headers={'accept': 'application/dns-json'}), timeout=8, context=SSL)
        j = json.loads(r.read().decode())
        if j.get('Status') == 3:
            esito = False
        elif j.get('Status') == 0:
            esito = any(a.get('type') == 1 for a in j.get('Answer', []))
    except Exception:
        pass
    if esito is None:
        try:
            socket.getaddrinfo(host, 443, proto=socket.IPPROTO_TCP)
            esito = True
        except Exception:
            esito = None
    with _dns_lock:
        _dns[host] = esito
    return esito


_mx, _mx_lock = {}, threading.Lock()


def ha_mx(dominio):
    """True / False / None (DNS non ha risposto). Con `host -t mx`, come chiesto; «no» solo
    davanti a una risposta netta (nessun MX, NXDOMAIN). Il 18/10/2026, con sei ricerche in
    parallelo, `host` ha risposto SERVFAIL o timeout per elsap.it e montorfano.com, che l'MX
    ce l'hanno: contati come «senza MX» toglievano caselle buone. Ora si riprova tre volte."""
    with _mx_lock:
        if dominio in _mx:
            return _mx[dominio]
    esito = None
    for tentativo in range(3):
        try:
            out = subprocess.run(['host', '-W', '5', '-t', 'mx', dominio], capture_output=True, text=True,
                                 timeout=15).stdout
        except Exception:
            out = ''
        if 'mail is handled by' in out:
            esito = True
            break
        if 'has no MX record' in out or 'NXDOMAIN' in out:
            esito = False
            break
        time.sleep(2 + 3 * tentativo)
    if esito is None:
        # ultima strada: Cloudflare DoH, che non passa dal DNS della rete locale
        try:
            r = urllib.request.urlopen(urllib.request.Request(
                'https://1.1.1.1/dns-query?type=MX&name=' + urllib.parse.quote(dominio),
                headers={'accept': 'application/dns-json'}), timeout=8, context=SSL)
            j = json.loads(r.read().decode())
            if j.get('Status') == 3:
                esito = False
            elif j.get('Status') == 0:
                esito = any(x.get('type') == 15 for x in j.get('Answer', []))
        except Exception:
            pass
    with _mx_lock:
        _mx[dominio] = esito
    return esito


def dominio_di(url):
    h = urllib.parse.urlparse(url if '//' in url else '//' + url).netloc.lower().split(':')[0]
    return h[4:] if h.startswith('www.') else h


def stesso_sito(a, b):
    """rossi.it, www.rossi.it e shop.rossi.it sono lo stesso sito."""
    return a == b or a.endswith('.' + b) or b.endswith('.' + a)


# ---------------------------------------------------------------- testo

def ascii_basso(s):
    return unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode().lower()


def parole_nome(nome):
    """(parole distintive, sigla «in sigla X» se c'è). Il nome si taglia alla prima forma
    giuridica: «Rossi Meccanica S.r.l. a socio unico» → rossi meccanica."""
    s = re.sub(r'&\s*c\b\.?', ' ', ascii_basso(nome)).replace('&', ' e ')   # «Rossi Mario & C.» → rossi mario
    sigla = None
    m = re.search(r'\b(?:in sigla|in breve|siglabile|abbreviat\w*|o anche)\b[:\s]+([a-z0-9. ]+?)(?:\s+s\.?r\.?l|\s+s\.?p\.?a|$)', s)
    if m:
        sigla = re.sub(r'[^a-z0-9]', '', m.group(1)) or None
    s = re.sub(r'(?<=[a-z0-9])\.(?=[a-z0-9])', '', s)           # s.r.l. → srl, f.lli → flli, fa.ro → faro
    t, lettere = [], ''
    for w in re.sub(r'[^a-z0-9]+', ' ', s).split():              # «O M G spa» → omg
        if len(w) == 1:
            lettere += w
            continue
        if lettere:
            t.append(lettere)
            lettere = ''
        t.append(w)
    if lettere:
        t.append(lettere)
    for i, w in enumerate(t):
        if i > 0 and w in TAGLIO:
            t = t[:i]
            break
    t = [w for w in t if w not in FORME]
    return t, sigla


def testo_visibile(pagina):
    p = re.sub(r'(?is)<(script|style|noscript|svg|template)[^>]*>.*?</\1>', ' ', pagina)
    p = re.sub(r'(?s)<!--.*?-->', ' ', p)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', p))).strip()


def contiene_piva(pagina, piva):
    """La partita IVA nel testo, anche scritta «IT 012 345 678 90» o con i punti."""
    t = re.sub(r'(?<=\d)[\s.\-/](?=\d)', '', testo_visibile(pagina))
    return re.search(r'(?<!\d)' + piva + r'(?!\d)', t) is not None


RX_PIVA_DICHIARATA = re.compile(r'(?:p\.?\s?iva|partita\s+iva|p\.\s?i\.|vat(?:\s+(?:no|number|n|code))?\.?|'
                                r'c\.?\s?f\.?\s*(?:e|/|-)\s*p\.?\s?iva)\s*[:.]?\s*(?:it)?\s?(\d{11})(?!\d)', re.I)


def piva_dichiarate(pagina):
    """Le partite IVA scritte sulla pagina dopo un'etichetta (P.IVA, Partita IVA, P.I., VAT)."""
    t = re.sub(r'(?<=\d)[\s.\-/](?=\d)', '', testo_visibile(pagina))
    return list(dict.fromkeys(RX_PIVA_DICHIARATA.findall(t)))


def estratto(pagine):
    """Frasi vere dalla home e dalla pagina chi siamo, senza menu, cookie e piè di pagina."""
    righe, viste = [], set()
    for pg in pagine:
        m = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']{30,300})', pg, re.I)
        if m:
            righe.append(html.unescape(m.group(1)).strip())
        p = re.sub(r'(?s)<!--.*?-->', ' ', pg)
        p = re.sub(r'(?is)<head\b.*?</head>', ' ', p)
        p = re.sub(r'(?is)<(script|style|noscript|svg|nav|header|footer|form|template|button|select)[^>]*>.*?</\1>', ' ', p)
        for blocco in re.split(r'(?i)</?(?:p|h[1-6]|li|div|section|article|br|td|blockquote)[^>]*>', p):
            r = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', blocco))).strip()
            if len(r) < 50 or len(r.split()) < 8:
                continue
            if re.search(r'cookie|privacy|consenso|javascript|browser|copyright|diritti riservati|p\.?\s?iva|'
                         r'partita iva|newsletter|©', r, re.I):
                continue
            chiave = r.lower()[:80]
            if chiave in viste:
                continue
            viste.add(chiave)
            righe.append(r)
    out = ''
    for r in righe:
        if len(out) + len(r) + 1 > 1500:
            resto = 1500 - len(out) - 1
            if resto > 120:
                out += ' ' + r[:resto].rsplit(' ', 1)[0] + '…'
            break
        out += (' ' if out else '') + r
    return out.strip()


def decodifica_cf(hexa):
    try:
        k = int(hexa[:2], 16)
        return ''.join(chr(int(hexa[i:i + 2], 16) ^ k) for i in range(2, len(hexa), 2))
    except ValueError:
        return ''


RX_MAIL = re.compile(r'[a-z0-9][a-z0-9._%+-]{0,63}@[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,10}', re.I)


def indirizzi(pagina):
    """Tutti gli indirizzi della pagina, comprese le forme protette o scritte per esteso."""
    p = html.unescape(urllib.parse.unquote(pagina))
    trovati = [decodifica_cf(h) for h in re.findall(r'data-cfemail="([0-9a-f]+)"', p)]
    trovati += [decodifica_cf(h) for h in re.findall(r'email-protection#([0-9a-f]+)', p)]
    p = re.sub(r'\s*[\[\(\{]\s*(?:at|chiocciola)\s*[\]\)\}]\s*', '@', p, flags=re.I)
    p = re.sub(r'\s*[\[\(\{]\s*(?:dot|punto)\s*[\]\)\}]\s*', '.', p, flags=re.I)
    trovati += RX_MAIL.findall(p)
    out = []
    for e in trovati:
        e = e.lower().strip('.')
        if re.search(r'\.(png|jpe?g|gif|webp|svg|css|js|ico|avif)$', e) or '@' not in e:
            continue
        if e not in out:
            out.append(e)
    return out


def classifica(email, sito, parole):
    """(rango, None) se la casella va bene; (None, motivo) se no. Rango più basso = preferita."""
    locale, dom = email.split('@', 1)
    if RX_PEC_DOMINIO.search(dom) or RX_PEC_LOCALE.search(locale):
        return None, 'PEC'
    proprio = stesso_sito(dom, sito)
    if not proprio:
        # info@rmli.it per il sito rmliconstructionengineeringsrl.it sì; info@flir.cn per flir.com no
        etichetta = dom.split('.')[-2] if dom.count('.') >= 1 else dom
        if dom.rsplit('.', 1)[-1] not in ('it', 'com', 'eu', 'net') or \
                not any(len(w) >= 4 and w in etichetta for w in parole):
            return None, 'altro dominio'
    # le caselle di un'altra filiale del gruppo: info.de@baumerhhs.com, info-hcsb@de.helu.com
    paese = re.search(r'[._-]([a-z]{2})$', locale)
    if (paese and paese.group(1) in PAESI) or (dom.count('.') >= 2 and dom.split('.')[0] in PAESI):
        return None, 'casella di un altro paese'
    m = RX_GENERICA.match(locale)
    if not m:
        # sarg@sarg.it, agom@agom.it: la casella col nome della società è dell'azienda, non di una persona.
        # Vale solo se il nome sta tutto nel dominio, così rossi@ di «Rossi Mario Srl» su mariorossi.it resta fuori.
        etichetta = dom.split('.')[-2] if dom.count('.') >= 1 else dom
        if proprio and re.sub(r'[._-]', '', locale) == etichetta.replace('-', ''):
            return 1000, None
        return None, 'non generica'
    rango = GENERICHE.index(m.group(1)) * 10 + (0 if not m.group(2) else 1) + (0 if proprio else 5)
    return rango, None


# ---------------------------------------------------------------- il sito

def domini_indovinati(nome, forma):
    t, sigla = parole_nome(nome)
    if not t:
        return []
    basi = []

    def b(x, minimo=4):
        if x and len(x) >= minimo and x not in basi:
            basi.append(x)
    b(''.join(t))
    if len(t) > 1:
        b('-'.join(t))
    distintive = [w for w in t if w not in GENERICHE_NOME]
    if distintive and distintive != t:
        b(''.join(distintive))
    if len(t) >= 3 and not set(t[:2]) <= GENERICHE_NOME:
        b(''.join(t[:2]))
    if t[0] not in GENERICHE_NOME and len(t[0]) >= 5:
        b(t[0])
    if 'flli' in t:
        b(''.join('fratelli' if w == 'flli' else w for w in t))
        b(''.join(w for w in t if w != 'flli'))
    b(sigla, 3)
    suff = 'spa' if forma and 'AZIONI' in forma.upper() else 'srl'
    b(''.join(t) + suff)
    out = []
    for i, base in enumerate(basi):
        for tld in (TLD if i == 0 else TLD[:2]):
            out.append(base + tld)
    return out[:22]


RX_RINVIO = re.compile(r'(?:window\.|document\.)?location(?:\.href)?\s*=\s*["\']([^"\']+)["\']|'
                       r'location\.replace\(\s*["\']([^"\']+)["\']|'
                       r'http-equiv=["\']?refresh["\']?[^>]*content=["\'][^"\']*url=([^"\'>\s]+)|'
                       r'<frame[^>]+src=["\']([^"\']+)["\']', re.I)


def apri_sito(dominio):
    """(url finale, html) del primo indirizzo che risponde, oppure (None, motivo).
    Segue anche i rinvii scritti nella pagina (JavaScript, meta refresh, frame): il
    18/10/2026 omgspa.it era solo `window.location='http://www.bernexgroup.com/it/home'`."""
    motivi = []
    www = risolve('www.' + dominio) is not False
    prove = ([f'https://www.{dominio}/'] if www else []) + [f'https://{dominio}/'] + \
            ([f'http://www.{dominio}/'] if www else [f'http://{dominio}/'])
    for u in prove:
        fin, t = scarica(u)
        if fin:
            m = RX_RINVIO.search(t) if len(testo_visibile(t)) < 200 else None
            if m:
                dest = urllib.parse.urljoin(fin, next(g for g in m.groups() if g))
                f2, t2 = scarica(dest)
                if f2:
                    return f2, t2
            return fin, t
        motivi.append(t)
        if 'anti-bot' in t:
            break
    return None, motivi[0] if len(set(motivi)) == 1 else '; '.join(dict.fromkeys(motivi))


def pagine_interne(base_url, pagina, sito, quali=PAGINE_UTILI):
    """I link interni che portano a contatti / chi siamo / dove siamo, contatti prima."""
    link = []
    for m in re.finditer(r'<a\b[^>]*href=["\']([^"\'#]+)["\'][^>]*>(.*?)</a>', pagina, re.I | re.S):
        href, testo = m.group(1).strip(), re.sub(r'<[^>]+>', ' ', m.group(2))
        if href.startswith(('mailto:', 'tel:', 'javascript:')):
            continue
        u = urllib.parse.urljoin(base_url, href)
        if not stesso_sito(dominio_di(u), sito) or re.search(r'\.(pdf|jpe?g|png|zip|docx?)$', u, re.I):
            continue
        if quali.search(href) or quali.search(testo):
            if u.split('#')[0] not in link:
                link.append(u.split('#')[0])
    link.sort(key=lambda u: 0 if re.search(r'contatt|contact', u, re.I) else 1)
    return link


def esamina(dominio, az, parole, fonte):
    """Apre il sito e decide se è dell'azienda. Ritorna un dict con l'esito."""
    fin, home = apri_sito(dominio)
    if not fin:
        return dict(stato='non risponde', nota=f'{dominio} {home}')
    sito = dominio_di(fin)
    if DIRECTORY.search(sito):
        return dict(stato='directory', nota=f'{dominio} porta a {sito}')
    tv = testo_visibile(home)
    titolo = re.search(r'<title[^>]*>(.*?)</title>', home, re.I | re.S)
    titolo = re.sub(r'\s+', ' ', html.unescape(titolo.group(1))).strip()[:80] if titolo else ''
    if PARCHEGGIO.search(titolo) or PARCHEGGIO.search(tv[:1500]) or PARCHEGGIO_HTML.search(home[:30000]) or len(tv) < 80:
        if len(tv) < 80 and '<script' in home.lower() and not PARCHEGGIO.search(titolo + tv[:1500]) \
                and not PARCHEGGIO_HTML.search(home[:30000]):
            return dict(stato='vuoto', nota=f'{dominio} pagina senza testo (sito tutto in JavaScript?)')
        return dict(stato='parcheggiato', nota=f'{dominio} parcheggiato o in costruzione' + (f' «{titolo}»' if titolo else ''))
    basso = ascii_basso(tv + ' ' + titolo)
    con_nome = sum(1 for w in parole if re.search(r'\b' + re.escape(w), basso))
    piva_home = contiene_piva(home, az['piva'])
    if not piva_home and con_nome == 0:
        return dict(stato='altro', nota=f'{dominio} vivo ma di altri ({titolo or "senza titolo"})')
    # è un candidato: si leggono le pagine utili
    pagine = [(fin, home)]
    for u in pagine_interne(fin, home, sito)[:MAX_PAGINE - 1]:
        f2, t2 = scarica(u)
        if f2 and f2 not in dict(pagine):
            pagine.append((f2, t2))
        time.sleep(0.2)
    if not any(re.search(r'contatt|contact', u, re.I) for u, _ in pagine[1:]):
        for perc in PERCORSI_CONTATTI:
            if len(pagine) >= MAX_PAGINE:
                break
            f2, t2 = scarica(urllib.parse.urljoin(fin, perc))
            if f2 and stesso_sito(dominio_di(f2), sito) and f2.rstrip('/') != fin.rstrip('/'):
                pagine.append((f2, t2))
                break
    piva_url = next((u for u, t in pagine if contiene_piva(t, az['piva'])), None)
    altrui = [(u, x) for u, t in pagine for x in piva_dichiarate(t) if x != az['piva']]
    if not piva_url:
        # la partita IVA spesso sta solo nella privacy o nelle note legali: si guardano, non entrano nell'estratto
        for u in [x for x in pagine_interne(fin, home, sito, PAGINE_LEGALI) if x not in dict(pagine)][:3]:
            f2, t2 = scarica(u)
            if f2 and contiene_piva(t2, az['piva']):
                piva_url = f2
                break
            if f2:
                altrui += [(f2, x) for x in piva_dichiarate(t2) if x != az['piva']]
    if not piva_url and altrui:
        # 18/10/2026: comapsrl.com porta «Comap» e la parola Milano, ma la P.IVA è di una Comap di Fidenza
        return dict(stato='altro', nota=f'{dominio} vivo, ma la P.IVA del sito è {altrui[0][1]} ({altrui[0][0]}), '
                                         f'non {az["piva"]}')
    comune = ascii_basso(az['comune'] or '')
    tutto = ascii_basso(' '.join(testo_visibile(t) for _, t in pagine))
    tutte_parole = parole and all(re.search(r'\b' + re.escape(w), tutto) for w in parole)
    col_comune = bool(comune) and comune in tutto
    if piva_url:
        prova = f'{fonte} {dominio} → {fin} · P.IVA {az["piva"]} trovata in {piva_url}'
    elif tutte_parole and (col_comune or fonte.startswith('Pagine Gialle')):
        prova = (f'{fonte} {dominio} → {fin} · P.IVA non trovata in {len(pagine)} pagine; '
                 f'nome «{" ".join(parole)}»' + (f' e comune {az["comune"]}' if col_comune else '') + ' presenti')
    else:
        return dict(stato='altro', nota=f'{dominio} vivo, P.IVA assente e nome o comune mancanti ({titolo or "senza titolo"})')
    return dict(stato='suo', sito=sito, url=fin, prova=prova, pagine=pagine, piva=bool(piva_url))


# ---------------------------------------------------------------- Pagine Gialle

_pg_lock = threading.Lock()
_pg = {'ultima': 0.0, 'bloccata_fino': 0.0, 'errori': 0}
PG_PAUSA = 8


def pg_get(url):
    """Pagina di Pagine Gialle, una alla volta, con la pausa. (html, None) o (None, motivo)."""
    os.makedirs(CACHE_PG, exist_ok=True)
    f = os.path.join(CACHE_PG, hashlib.md5(url.encode()).hexdigest() + '.html')
    if os.path.exists(f):
        return open(f, encoding='utf-8', errors='ignore').read(), None
    with _pg_lock:
        if time.time() < _pg['bloccata_fino']:
            return None, 'Pagine Gialle bloccata (429), non interrogata'
        attesa = _pg['ultima'] + PG_PAUSA - time.time()
        if attesa > 0:
            time.sleep(attesa)
        _pg['ultima'] = time.time()
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers={
                'User-Agent': UA, 'Accept-Language': 'it-IT,it'}), timeout=25, context=SSL)
            t = r.read().decode('utf-8', 'ignore')
        except urllib.error.HTTPError as e:
            if e.code == 429:
                _pg['bloccata_fino'] = time.time() + 1800
                return None, 'Pagine Gialle 429, ferma per 30 minuti'
            return None, f'Pagine Gialle http {e.code}'
        except Exception as e:
            return None, f'Pagine Gialle non risponde ({str(e)[:40]})'
    if 'search-itm' not in t and 'data-pag=' not in t and not re.search(r'<title>[^<]*Pagine Gialle', t):
        return None, 'Pagine Gialle pagina inattesa (anti-bot?)'
    with open(f, 'w', encoding='utf-8') as out:
        out.write(t)
    return t, None


def sito_da_pg(az, parole):
    """(dominio | None, nota). Vale solo un risultato con le stesse parole del nome e nel comune giusto."""
    if not parole:
        return None, 'Pagine Gialle: nome vuoto'
    q = ' '.join(parole)
    comune = ascii_basso(az['comune'] or '')
    url = 'https://www.paginegialle.it/ricerca/' + urllib.parse.quote(q) + '/' + urllib.parse.quote(comune)
    t, err = pg_get(url)
    if err:
        return None, err
    t = t.split('section-similar__title')[0]
    for blk in t.split('class="search-itm card-listing')[1:]:
        n = re.search(r'search-itm__rag[^>]*>(.*?)</h2>', blk, re.S)
        a = re.search(r'search-itm__adr[^>]*>(.*?)</div>\s*</div>', blk, re.S)
        lk = re.search(r'href="(https://www\.paginegialle\.it/[^"]+)"', blk)
        if not (n and a and lk):
            continue
        nome = testo_visibile(n.group(1))
        adr = ascii_basso(testo_visibile(a.group(1)))
        if set(parole) <= set(parole_nome(nome)[0]) and comune and comune in adr:
            sch, err = pg_get(lk.group(1))
            if err:
                return None, err
            w = re.search(r'data-pag="WWW"[^>]*href="([^"]+)"', sch) or re.search(r'href="([^"]+)"[^>]*data-pag="WWW"', sch)
            if not w:
                return None, f'Pagine Gialle «{q}» in {comune}: trovata «{nome}», senza sito'
            return dominio_di(w.group(1)), f'Pagine Gialle «{q}» in {comune} → «{nome}»'
    return None, f'Pagine Gialle «{q}» in {comune}: nessun risultato con nome e comune'


# ---------------------------------------------------------------- un'azienda

def lavora(az, usa_pg=True):
    parole, _ = parole_nome(az['nome'])
    # per riconoscere il nome sulla pagina contano le parole distintive: «Kistler Italia» → kistler
    parole = [w for w in parole if w not in GENERICHE_NOME and len(w) >= 2] or parole
    domini = domini_indovinati(az['nome'], az['forma'])
    note, trovato, provati, dns_muto = [], None, 0, 0
    for d in domini:
        r = risolve(d)
        if r is None:
            r = risolve('www.' + d)
        if r is False:
            r = risolve('www.' + d)
        if r is None:
            dns_muto += 1
            note.append(f'{d} DNS non risponde')
            continue
        if not r:
            continue
        provati += 1
        e = esamina(d, az, parole, 'dominio indovinato')
        if e['stato'] == 'suo':
            trovato = e
            if e['piva']:
                break
            # senza P.IVA si continua a cercare un dominio migliore, ma si tiene questo
            note.append(f'{d} probabile (senza P.IVA)')
            altro = next((dd for dd in domini[domini.index(d) + 1:] if risolve(dd)), None)
            if altro:
                e2 = esamina(altro, az, parole, 'dominio indovinato')
                if e2['stato'] == 'suo' and e2['piva']:
                    trovato = e2
            break
        note.append(e['nota'])
    testa = f'provati {len(domini)} domini dal nome, {provati} esistenti'
    if not trovato and usa_pg:
        dom, nota_pg = sito_da_pg(az, parole)
        note.append(nota_pg)
        if dom and not DIRECTORY.search(dom):
            e = esamina(dom, az, parole, 'Pagine Gialle →')
            if e['stato'] == 'suo':
                trovato = e
                e['prova'] = nota_pg + ' · ' + e['prova']
            else:
                note.append(e['nota'])
    elif not trovato:
        note.append('Pagine Gialle non usata (--senza-pg)')
    if not trovato:
        return dict(fase='senza_sito', sito_prova=(testa + ' · ' + ' · '.join(note))[:1500])

    sito = trovato['sito']
    pagine = trovato['pagine']
    candidate, scartate = [], {}
    for url, t in pagine:
        for em in indirizzi(t):
            rango, perche = classifica(em, sito, parole)
            if rango is None:
                scartate.setdefault(em, perche)
            elif em not in [c[1] for c in candidate]:
                candidate.append((rango, em, url))
    candidate.sort()
    scelta, mx_note = None, []
    for rango, em, url in candidate:
        mx = ha_mx(em.split('@', 1)[1])
        if mx:
            scelta = (em, url)
            break
        mx_note.append(f'{em} {"senza MX" if mx is False else "MX non verificabile"}')
    chi_siamo = [t for u, t in pagine[1:] if re.search(r'chi[-_ ]?siamo|chisiamo|about|azienda|company|storia|profilo', u, re.I)]
    out = dict(sito=trovato['url'], sito_prova=trovato['prova'][:1500],
               estratto=estratto([pagine[0][1]] + chi_siamo[:1]), dominio=sito)
    if scelta:
        out.update(fase='pronta', email=scelta[0], email_prova=scelta[1])
        if mx_note:
            out['email_prova'] += ' · scartate prima: ' + '; '.join(mx_note)
    else:
        lette = ', '.join(u for u, _ in pagine)
        motivi = '; '.join(f'{e} ({p})' for e, p in list(scartate.items())[:8]) or 'nessun indirizzo nelle pagine'
        out.update(fase='senza_mail', email_prova=(f'lette {len(pagine)} pagine: {lette} · scartati: {motivi}'
                                                    + (' · ' + '; '.join(mx_note) if mx_note else ''))[:1500])
    return out


# ---------------------------------------------------------------- base dati

FASI_VIVE = ('pronta', 'senza_mail')


def salva(c, az, r):
    ora = db.adesso()
    piva = az['piva']
    fase, nota = r['fase'], None
    email = r.get('email')
    # doppioni: stesso sito o stessa casella → resta il fatturato più alto
    if r.get('dominio'):
        for o in c.execute('SELECT piva, nome, fatturato, fase, sito, email FROM aziende WHERE piva != ? AND sito IS NOT NULL '
                           "AND fase NOT IN ('nuova', 'scartata', 'senza_sito')", (piva,)).fetchall():
            stesso_dom = stesso_sito(dominio_di(o['sito']), r['dominio'])
            stessa_mail = email and o['email'] == email
            if not (stesso_dom or stessa_mail):
                continue
            perche = 'stesso sito' if stesso_dom else 'stessa casella'
            if o['fase'] in FASI_VIVE and (o['fatturato'] or 0) < (az['fatturato'] or 0):
                db.metti_fase(c, o['piva'], 'scartata',
                              f'trova-mail.py: {perche} di {az["nome"]} ({piva}), che fattura di più'
                              + (f' · casella {o["email"]}' if o['email'] else ''))
                c.execute('UPDATE aziende SET email=NULL WHERE piva=?', (o['piva'],))
            else:
                fase = 'scartata'
                nota = (f'trova-mail.py: {perche} di {o["nome"]} ({o["piva"]}), che fattura di più o è già avanti'
                        + (f' · casella {email}' if email else ''))
                email = None
                break
    c.execute('''UPDATE aziende SET sito=?, sito_prova=?, email=?, email_prova=?, estratto=?, fase=?,
                 note=COALESCE(?, note), aggiornata=? WHERE piva=?''',
              (r.get('sito'), r.get('sito_prova'), email, r.get('email_prova'), r.get('estratto'),
               fase, nota, ora, piva))
    c.commit()
    return fase


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--max', type=int, default=0)
    ap.add_argument('--paralleli', type=int, default=6)
    ap.add_argument('--senza-pg', action='store_true', help='non usare Pagine Gialle')
    ap.add_argument('--riprova', action='store_true', help='rimette in coda le ricerche fallite per siti muti o PG bloccata')
    a = ap.parse_args()
    with db.connessione() as c:
        if a.riprova:
            n = c.execute("""UPDATE aziende SET fase='nuova' WHERE fase IN ('senza_sito','senza_mail') AND
                             (sito_prova LIKE '%non risponde%' OR sito_prova LIKE '%bloccata%' OR sito_prova LIKE '%429%'
                              OR email_prova LIKE '%MX non verificabile%')""").rowcount
            print(f'rimesse in coda: {n}')
        righe = [dict(r) for r in c.execute(
            "SELECT piva, nome, forma, comune, prov, fatturato FROM aziende WHERE fase='nuova' ORDER BY fatturato DESC")]
    if a.max:
        righe = righe[:a.max]
    print(f'da cercare: {len(righe)}', flush=True)
    inizio, conti = time.time(), {}
    with db.connessione() as c, ThreadPoolExecutor(a.paralleli) as ex:
        futuri = {ex.submit(lavora, az, not a.senza_pg): az for az in righe}
        for i, f in enumerate(as_completed(futuri), 1):
            az = futuri[f]
            try:
                r = f.result()
            except Exception as e:
                r = dict(fase='nuova', sito_prova=f'errore dello script: {e!r}'[:500])
                print(f'  ERRORE {az["nome"]}: {e!r}', file=sys.stderr)
            fase = salva(c, az, r) if r['fase'] != 'nuova' else 'errore'
            conti[fase] = conti.get(fase, 0) + 1
            print(f'{i:4}/{len(righe)} {fase:10} {az["nome"][:40]:40} {r.get("email") or r.get("sito") or ""}', flush=True)
    durata = time.time() - inizio
    print(f'\n{len(righe)} aziende in {durata / 60:.1f} minuti '
          f'({durata / max(len(righe), 1) * 100 / 60:.1f} minuti ogni 100) con {a.paralleli} in parallelo')
    print('Esiti:', ', '.join(f'{k} {v}' for k, v in sorted(conti.items(), key=lambda kv: -kv[1])))


if __name__ == '__main__':
    main()
