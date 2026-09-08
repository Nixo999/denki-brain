#!/usr/bin/env python3
"""Verifica meccanica del sito, riga per riga. Il passo 3 di metodo-instagram
non lo fa piu` il modello a occhio: lo fa questo, e scrive la prova.

    python3 02-Sales/strumenti/verifica-sito.py 02-Sales/liste/<lista>.csv

Due controlli, e il primo non dipende da nessuno:

1. **Domini indovinati dal nome** (gelaterialariana.it, al-posto-giusto.it,
   ristorantekaralis.com ...): DNS, poi si apre, e conta come sito SOLO se la
   pagina porta il nome E il comune. Cinque dei sei siti trovati l'8 settembre
   sono usciti da qui. Nessun motore di ricerca in mezzo: funziona sempre.
2. **Motori di ricerca** (DuckDuckGo html e Brave, senza chiave): «"Nome"
   comune», domini fuori dalle directory, aperti uno per uno. Si bloccano dopo
   poche decine di richieste (403/429) e allora la riga lo dice: e` un extra,
   non la base. `--senza-motori` li salta.

Alla colonna «Esito verifica sito» lo script APPENDE la sua prova, marcata
`[verifica-sito]`, dopo quello che chi fa la lista ha scritto a mano (che
deve gia` essere «cercato «...» → ...», controlla-lista.py lo pretende).
Se trova un sito vivo col nome e il comune mette «Esito DM = SCARTATO».

Nato l'8 settembre 2026, dopo una lista con 62 verifiche uguali su 68 e
almeno 20 profili col sito. gelaterialariana.it era il PRIMO risultato.
"""
import csv, html, re, socket, ssl, sys, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 DenkiCode-verifica"
DIRECTORY = re.compile(r"(instagram|facebook|tripadvisor|thefork|yelp|paginegialle|pagine-gialle|google|"
                       r"wanderlog|justeat|deliveroo|glovo|uber|foursquare|tiktok|linkedin|youtube|"
                       r"virgilio|cylex|misterimprese|infobel|ristoranti\.it|local\.ch|search\.ch|"
                       r"trustpilot|booking|airbnb|apple\.com|mapquest|waze|sluurpy|ristorantiitaliani|"
                       r"gastroranking|restaurantguru|quandoo|wikipedia|amazon|linktr\.ee|"
                       r"treatwell|fresha|bookizon|simplybook|sumup|planity|thefork)", re.I)
PIATTAFORMA = re.compile(r"(wixsite\.com|jimdofree\.com|business\.site|myshopify\.com|res-menu|eatbu|"
                         r"\.menu$|menu\.|godaddysites|webnode|altervista|blogspot|wordpress\.com|"
                         r"weebly|site123|carrd\.co|strikingly)", re.I)
PARCHEGGIO = re.compile(r"(apache2 (ubuntu )?default|it works|index of /|coming soon|domain is for sale|"
                        r"questo dominio|sito in costruzione|under construction|parked|register\.it|aruba)", re.I)
PAUSA = 12  # secondi fra due ricerche: DuckDuckGo senza chiave si blocca se si corre


def slug(s, sep=""):
    s = s.lower().replace("&", " e ").replace("'", "")
    s = s.translate(str.maketrans("àèéìòóù", "aeeioou"))
    return re.sub(r"[^a-z0-9]+", sep, s).strip(sep)


def indovina(nome):
    """i domini che un'attivita` si compra davvero: nome intero, senza le
    parole di categoria, con e senza trattini"""
    p = parole(nome)
    if len(p) <= 1 and len(slug(nome)) < 8:
        return []        # «Tortuga», «Zenit», «Nautilus»: quel dominio e` di chiunque
    pieno = slug(nome); pieno_tr = slug(nome, "-")
    # «Pizzeria Maya» → maya.it e` di chiunque: la forma corta vale solo se
    # restano due parole, o una sola ma lunga (gelatilandia, grignapom)
    corto, corto_tr = ("".join(p), "-".join(p)) if (len(p) >= 2 or (p and len(p[0]) >= 8)) else ("", "")
    basi = [b for b in dict.fromkeys([pieno, pieno_tr, corto, corto_tr]) if len(b) >= 4]
    return [b + suff for b in basi for suff in (".it", ".com", ".ch", ".eu", ".net")]


def scarica(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "it-IT,it;q=0.9"})
    return urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "replace")


def dominio(u):
    if not u.startswith("http"):
        u = "https:" + u
    return urllib.parse.urlparse(u).netloc.lower().removeprefix("www.")


ddg_bloccato_fino = 0.0

def cerca(q):
    """Due motori: DuckDuckGo (html) e Brave. Bing ignora le virgolette e
    risponde con un'altra citta`, quindi non si usa. Nessuno dei due ha una
    chiave: DDG dopo ~50 ricerche di fila risponde 403 per qualche minuto, e
    allora si va avanti con Brave e si riprova DDG piu` tardi."""
    global ddg_bloccato_fino
    dom, motori, errori = [], [], []
    if time.time() > ddg_bloccato_fino:
        try:
            pagina = scarica("https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(q))
            for m in re.finditer(r'result__a" href="([^"]+)', pagina):
                h = html.unescape(m.group(1))
                u = urllib.parse.parse_qs(urllib.parse.urlparse(h).query).get("uddg", [h])[0]
                d = dominio(u)
                if d and d not in dom:
                    dom.append(d)
            motori.append("ddg")
        except urllib.error.HTTPError as e:
            if e.code in (403, 429):
                ddg_bloccato_fino = time.time() + 180
            errori.append(f"ddg {e.code}")
        except Exception as e:
            errori.append(f"ddg {e}")
    try:
        pagina = scarica("https://search.brave.com/search?q=" + urllib.parse.quote(q))
        for m in re.finditer(r'href="(https?://[^"]+)"', pagina):
            d = dominio(html.unescape(m.group(1)))
            if d and "brave.com" not in d and d not in dom:
                dom.append(d)
        motori.append("brave")
    except Exception as e:
        errori.append(f"brave {e}")
    if not motori:
        return None, "ricerca fallita (" + ", ".join(errori) + ")"
    return dom, None


def apri(dominio):
    """(stato, titolo, corpo). stato: vivo | parcheggiato | morto | non risponde"""
    try:
        socket.gethostbyname(dominio)
    except socket.gaierror:
        return "morto", "", ""
    for schema in ("https://", "http://"):
        try:
            req = urllib.request.Request(schema + dominio, headers={"User-Agent": UA})
            ctx = ssl.create_default_context(); ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
            r = urllib.request.urlopen(req, timeout=12, context=ctx)
            corpo = r.read(60000).decode("utf-8", "replace")
            t = re.search(r"<title[^>]*>(.*?)</title>", corpo, re.I | re.S)
            titolo = re.sub(r"\s+", " ", html.unescape(t.group(1))).strip()[:80] if t else ""
            if PARCHEGGIO.search(titolo) or PARCHEGGIO.search(corpo[:3000]) or len(corpo.strip()) < 300:
                return "parcheggiato", titolo, corpo
            return "vivo", titolo, corpo
        except Exception:
            continue
    return "non risponde", "", ""


def parole(nome):
    stop = {"il", "la", "lo", "le", "gli", "i", "di", "da", "del", "della", "dei", "al", "alla", "e", "the",
            "bar", "ristorante", "pizzeria", "trattoria", "osteria", "gelateria", "caffe", "cafe", "caffè",
            "pub", "bistrot", "bistro", "sas", "srl", "snc"}
    return [p for p in re.findall(r"[a-zà-ú0-9]{3,}", nome.lower()) if p not in stop]


def verifica(nome, comune, motori=True):
    comune_base = re.sub(r"\s*\(.*\)", "", comune).split("-")[0].strip()
    q = f'"{nome}" {comune_base}'
    dom, err = ([], None)
    if motori:
        dom, err = cerca(q)
        dom = dom or []
    candidati = [d for d in dom if not DIRECTORY.search(d)]
    for g in indovina(nome):
        if g not in candidati:
            candidati.append(g)
    esiti, sito_vivo, probabile = [], None, None
    for d in candidati[:24]:
        stato, titolo, corpo = apri(d)
        indovinato = d not in dom
        if stato == "morto":
            if indovinato:
                continue        # dominio indovinato che non esiste: non si scrive
            esiti.append(f"{d} (DNS morto)"); continue
        tag = "piattaforma" if PIATTAFORMA.search(d) else stato
        esiti.append(f"{d} ({tag}{', indovinato' if indovinato else ''}{': ' + titolo if titolo else ''})")
        if stato == "vivo" and tag == "vivo" and not sito_vivo:
            testo = (titolo + " " + corpo).lower()
            col_nome = any(p in titolo.lower() for p in parole(nome))
            col_comune = comune_base.lower() in testo
            # dalla ricerca basta il nome nel titolo; un dominio indovinato e` sicuro
            # solo se la pagina nomina anche il comune, altrimenti e` «probabile»
            # e lo apre una persona (o il modello): alpostogiusto.it non scrive
            # «Varese» nel primo schermo, anteomnia.it e` un'altra cosa
            if col_nome and (col_comune or not indovinato):
                sito_vivo = d
            elif col_nome and not probabile:
                probabile = d
    scartati = [d for d in dom if DIRECTORY.search(d)][:4]
    if motori:
        testa = f"[verifica-sito] motori «{q}»: " + (err if err else f"{len(dom)} risultati")
    else:
        testa = "[verifica-sito] senza motori"
    testo = testa + " · domini: " + ("; ".join(esiti) if esiti else "nessuno risponde")
    if scartati:
        testo += f" · directory: {', '.join(scartati)}"
    if probabile and not sito_vivo:
        testo += f" ⚠ PROBABILE SITO {probabile}: da aprire prima di pubblicare"
    return testo, sito_vivo, probabile, bool(err)


def main(percorso, motori=True):
    p = Path(percorso)
    with p.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f); righe = list(r); campi = r.fieldnames
    col_v = next((c for c in campi if c.lower().startswith("esito verifica")), None)
    col_n = next((c for c in campi if c.lower().startswith("nome")), None)
    col_c = next((c for c in campi if c.lower().startswith("comune")), None)
    col_e = next((c for c in campi if c.lower().startswith("esito dm")), None)
    if not all((col_v, col_n, col_c, col_e)):
        sys.exit("mancano le colonne: Nome, Comune, Esito verifica sito, Esito DM")
    vivi = probabili = 0
    for i, x in enumerate(righe, 1):
        testo, sito, prob, err = verifica(x[col_n], x[col_c], motori)
        prima = re.sub(r"\s*\[verifica-sito\].*$", "", x[col_v] or "", flags=re.S).strip()
        x[col_v] = (prima + " " if prima else "") + testo
        if sito:
            vivi += 1
            if not (x[col_e] or "").strip():
                x[col_e] = f"SCARTATO: sito vivo {sito} (verifica-sito.py, {time.strftime('%Y-%m-%d')})"
        if prob and not sito:
            probabili += 1
        print(f"{i:3}/{len(righe)} {'SITO ' if sito else 'SITO?' if prob else ' ??? ' if err else '     '} {x[col_n][:30]:30} {testo[:120]}", flush=True)
        if motori:
            time.sleep(PAUSA)
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campi, lineterminator="\n"); w.writeheader(); w.writerows(righe)
    print(f"\n{vivi} su {len(righe)} hanno un sito vivo col loro nome: segnati SCARTATO in «Esito DM».")
    print(f"{probabili} con un PROBABILE SITO: si aprono uno per uno e si decide, controlla-lista.py non passa finche` restano.")
    print("Il resto e` da rileggere a mano: «non risponde» e «piattaforma» non sono «nessun sito».")
    print("Righe con ???: i motori erano bloccati, vale solo il controllo sui domini.")


if __name__ == "__main__":
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(argv) != 1:
        sys.exit(__doc__)
    main(argv[0], motori="--senza-motori" not in sys.argv)
