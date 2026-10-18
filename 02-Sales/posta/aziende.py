#!/usr/bin/env python3
"""Riempie la tabella `aziende` con le società B2B lombarde fra 1 e 15 milioni.

    python3 02-Sales/posta/aziende.py [--prov MI,MB] [--ateco 25.62,46.69] [--max N]

Legge le liste di companyreports.it per codice ATECO (ordinate per fatturato
decrescente), tiene le righe lombarde fra 1.000.000 e 15.000.000 €, apre la
scheda di ognuna e applica i filtri: stato «Attiva», nome senza liquidazione o
fallimento, solo persone giuridiche, almeno 6 dipendenti dichiarati. Chi passa
entra in fase `nuova`; chi cade sulla scheda entra in fase `scartata` con il
motivo in `note`, così una seconda passata non la rilegge. Chi cade già sulla
lista (provincia, fatturato) non entra in base dati: si conta e basta.

Idempotente: una P.IVA già in base dati non si riscrive. Riprende da dove si è
fermato perché pagine e schede stanno in cache (`dati/cache/`).

## Come companyreports divide i codici (verificato il 18/10/2026)

Ogni stringa di codice è una lista a sé, e le stringhe sono di quattro tipi:

- `25.62`     classe a 4 cifre, ATECO 2007: lista piccola, residui vecchi;
- `46.69.2`   categoria a 5 cifre, ATECO 2007;
- `46.69.99`  sottocategoria a 6 cifre, ATECO 2007;
- `25.53.00`  sottocategoria a 6 cifre, ATECO 2025: qui sta il grosso.

Le stringhe a 6 cifre si scontrano: `25.62.00` oggi contiene le serrature
(ATECO 2025), mentre le officine di meccanica generale stanno in `25.53.00`.
Per questo lo script non usa una lista fissa di stringhe: per ogni CLASSE
della tabella sotto prova

- la classe nuda, `.00` e le dieci categorie `.0`-`.9`;
- le sottocategorie ATECO 2007 dell'albero di companyreports (/settori-economici/);
- le sottocategorie ATECO 2025 della classe su codiceateco.it, più la loro forma
  `.X0` (companyreports ha liste come `46.64.10` e `46.64.90`);

e tiene quelle che hanno righe. Il 18/10/2026, sulle classi 25.53, 25.62, 46.64
e 46.69, questa scoperta ha trovato tutte le liste trovate provando le 111
combinazioni possibili, con circa 20 richieste per classe invece di 111.
Il risultato resta in `dati/cache/liste-ateco.json`.

## Tabella classe → settore

Il settore dipende dalle prime cifre del codice, che per i gruppi scelti
coincidono fra ATECO 2007 e 2025: per questo una classe vale per tutte e due
le classificazioni. Le classi che esistono solo nel 2025 sono segnate «2025».
"""
import argparse, hashlib, html, json, os, re, sys, time, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
import db  # noqa: E402

OFFICINE = 'Officine e carpenterie'
MANIFATTURA = 'Manifattura'
IMPIANTI = 'Impiantistica'
COSTRUZIONI = 'Costruzioni'
INGROSSO = 'Ingrosso'
TRASPORTI = 'Trasporti'
LOGISTICA = 'Magazzinaggio e logistica'
PULIZIE = 'Pulizie e servizi'

SETTORI = {
    # Officine e carpenterie: divisione 25 (prodotti in metallo), 28 (macchinari), 33.1 (riparazioni)
    OFFICINE: '''25.11 25.12 25.21 25.22 25.29 25.30 25.40 25.50 25.51 25.52 25.53 25.61 25.62 25.63
                 25.71 25.72 25.73 25.91 25.92 25.93 25.94 25.99
                 28.11 28.12 28.13 28.14 28.15 28.21 28.22 28.23 28.24 28.25 28.29 28.30 28.41 28.42
                 28.49 28.91 28.92 28.93 28.94 28.95 28.96 28.99
                 33.11 33.12 33.13 33.14 33.15 33.16 33.17 33.18 33.19''',
    # Manifattura: alimentare industriale (fuori 10.71, panetterie e pasticcerie fresche),
    # tessile, abbigliamento, legno, chimica, gomma e plastica, mobili
    MANIFATTURA: '''10.11 10.12 10.13 10.20 10.31 10.32 10.39 10.41 10.42 10.51 10.52 10.61 10.62
                    10.72 10.73 10.81 10.82 10.83 10.84 10.85 10.86 10.89 10.91 10.92
                    13.10 13.20 13.30 13.91 13.92 13.93 13.94 13.95 13.96 13.99
                    14.10 14.11 14.12 14.13 14.14 14.19 14.20 14.21 14.22 14.23 14.24 14.29 14.31 14.39
                    16.10 16.11 16.12 16.21 16.22 16.23 16.24 16.25 16.26 16.27 16.28 16.29
                    20.11 20.12 20.13 20.14 20.15 20.16 20.17 20.20 20.30 20.41 20.42 20.51 20.52
                    20.53 20.59 20.60
                    22.11 22.19 22.21 22.22 22.23 22.24 22.25 22.26 22.29
                    31.00 31.01 31.02 31.03 31.09''',
    # Impiantistica: 43.21 elettrici, 43.22 idraulici e termici, 43.29 altri (2007),
    # 43.23 isolamento e 43.24 altri impianti (2025)
    IMPIANTI: '43.21 43.22 43.29 43.23 43.24',
    # Costruzioni: 41.20 edifici (2007), 41.00 edifici (2025), ingegneria civile 42
    COSTRUZIONI: '41.20 41.00 42.11 42.12 42.13 42.21 42.22 42.91 42.99',
    # Ingrosso: tutta la divisione 46 tranne 46.1 (intermediari, agenti di commercio).
    # Nel 2025 il 46.7 diventa veicoli e ricambi, e il vecchio 46.7 passa a 46.8.
    INGROSSO: '''46.21 46.22 46.23 46.24 46.31 46.32 46.33 46.34 46.35 46.36 46.37 46.38 46.39
                 46.41 46.42 46.43 46.44 46.45 46.46 46.47 46.48 46.49 46.50 46.51 46.52
                 46.61 46.62 46.63 46.64 46.65 46.66 46.69 46.71 46.72 46.73 46.74 46.75 46.76
                 46.77 46.81 46.82 46.83 46.84 46.85 46.86 46.87 46.89 46.90''',
    TRASPORTI: '49.41',
    # Magazzinaggio e logistica: 52.10 magazzini, 52.24 movimentazione merci, 52.29 spedizionieri
    # e logistica (2007), 52.25 logistica e 52.26 altre attività di supporto (2025)
    LOGISTICA: '52.10 52.24 52.29 52.25 52.26',
    # Pulizie e servizi: 81.21-81.29 pulizie (2007), 81.23 (2025), 81.30 verde
    PULIZIE: '81.21 81.22 81.23 81.29 81.30',
}
CLASSE_SETTORE = {c: s for s, cc in SETTORI.items() for c in cc.split()}

LOMBARDIA = 'BG BS CO CR LC LO MB MI MN PV SO VA'.split()
FATT_MIN, FATT_MAX = 1_000_000, 15_000_000

# Forma giuridica: etichette vere lette sulle schede di companyreports, normalizzate
# (maiuscole, senza apostrofi). Prima regola che combacia vince: l'ordine conta,
# «a responsabilita limitata semplificata» va controllata prima di «a responsabilita limitata».
# Fuori le società di persone e le ditte: per l'art. 130 del Codice privacy sono
# persone fisiche, e una mail commerciale non richiesta vuole il consenso.
FORME = [
    (r'NOME COLLETTIVO', None, 'S.n.c.'),
    (r'ACCOMANDITA SEMPLICE', None, 'S.a.s.'),
    (r'SOCIETA SEMPLICE', None, 'società semplice'),
    (r'IMPRESA INDIVIDUALE|DITTA INDIVIDUALE|IMPRENDITORE', None, 'ditta individuale'),
    (r'ACCOMANDITA PER AZIONI', 'S.a.p.a.', None),
    (r'RESPONSABILITA LIMITATA SEMPLIFICATA', 'S.r.l.s.', None),
    (r'COOPERATIV', 'cooperativa', None),
    (r'CONSORZI|CONSORTILE', 'consorzio', None),
    (r'RESPONSABILITA LIMITATA', 'S.r.l.', None),
    (r'PER AZIONI|SOCIETA EUROPEA', 'S.p.A.', None),
]

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'
CACHE = os.path.join(db.DATI, 'cache', 'companyreports')
LISTE = os.path.join(db.DATI, 'cache', 'liste-ateco.json')
PAUSA = 0.5


def get(url):
    """Pagina di companyreports, dalla cache se c'è (stessa logica di
    01-Coding/strumenti/liste-bilanci/cr_ateco.py, con la cache qui)."""
    os.makedirs(CACHE, exist_ok=True)
    f = os.path.join(CACHE, hashlib.md5(url.encode()).hexdigest() + '.html')
    if os.path.exists(f):
        return open(f, encoding='utf-8', errors='ignore').read()
    for tentativo in range(3):
        try:
            r = urllib.request.urlopen(urllib.request.Request(
                url, headers={'User-Agent': UA, 'Accept-Language': 'it-IT,it'}), timeout=30)
            t = r.read().decode('utf-8', 'ignore')
            with open(f, 'w', encoding='utf-8') as out:
                out.write(t)
            time.sleep(PAUSA)
            return t
        except urllib.error.HTTPError as e:
            if e.code not in (429, 502, 503, 504):
                return ''       # risposta netta: codiceateco.it dà 500 per le classi che nel 2025 non esistono
            print('  errore', url, e, file=sys.stderr)
            time.sleep(10 * (tentativo + 1))
        except Exception as e:
            print('  errore', url, e, file=sys.stderr)
            time.sleep(3 * (tentativo + 1))
    return None     # nessuna risposta (rete, DNS): non vuol dire «lista vuota»


def pagina(codice, n):
    """Le righe di una pagina di lista: copiato da cr_ateco.page()."""
    t = get(f'https://www.companyreports.it/ateco/{codice}' + ('' if n == 1 else f'/{n}'))
    if t is None:
        return None     # chi chiama distingue: None = non scaricata, [] = vuota
    out = []
    for blk in t.split('class="row aziende-row"')[1:]:
        m = re.search(r'href="https://www\.companyreports\.it/([a-z0-9-]+-(\d{11}))" title="Bilancio ([^"]+)"', blk)
        if not m:
            continue
        slug, piva, nome = m.groups()
        f = re.search(r'Fatturato: </div>.*?<a [^>]*>([^<]+)</a>', blk, re.S)
        c = re.search(r'comune/([a-z0-9-]+)"[^>]*>([^<]+)</a>\s*<a [^>]*>\(([A-Z]{2})\)', blk)
        fv = f.group(1).strip() if f else 'N.D.'
        out.append(dict(slug=slug, piva=piva, nome=html.unescape(nome).strip(),
                        fatturato=int(re.sub(r'[^0-9]', '', fv)) if re.search(r'\d', fv) else None,
                        comune=html.unescape(c.group(2)).strip() if c else None,
                        prov=c.group(3) if c else None, lista=codice))
    return out


def campo(s, etichetta, fino):
    m = re.search(re.escape(etichetta) + r'\s*\n(.*?)\n' + re.escape(fino), s, re.S)
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else None


def scheda(x):
    """Copiato da liste-bilanci/scheda.leggi(), più il fatturato della scheda."""
    t = get('https://www.companyreports.it/' + x['slug'])
    if t is None:
        x['errore'] = 'scheda non scaricata'
        return x
    t = re.sub(r'<script.*?</script>|<style.*?</style>', '', t, flags=re.S)
    s = html.unescape(re.sub(r'<[^>]+>', '\n', t))
    s = re.sub(r'[ \t]*\n\s*', '\n', s)
    x['indirizzo'] = (campo(s, 'Indirizzo', 'Fatturato') or '').split(' - ')[0].strip()
    m = re.search(r'Fatturato\n€ ([\d.]+)\n\((\d{4})\)', s)
    x['anno'] = int(m.group(2)) if m else None
    x['dipendenti'] = campo(s, 'N. Dipendenti', 'Stato Attività')
    x['stato'] = campo(s, 'Stato Attività', 'Condividi')
    x['forma'] = campo(s, 'Forma giuridica', 'Codice Ateco')
    x['ateco'] = campo(s, 'Codice Ateco', 'Attività prevalente')
    x['attivita'] = campo(s, 'Attività prevalente', 'Fondazione')
    return x


_albero = None


def albero_2007():
    """I codici ATECO 2007 dell'albero di companyreports, es. 46.69.99 e 25.73.1."""
    global _albero
    if _albero is None:
        _albero = set()
        for n in [''] + [str(i) for i in range(1, 60)]:
            t = get('https://www.companyreports.it/settori-economici/' + n) or ''
            _albero |= {k.replace('-', '.') for k in re.findall(r'companyreports\.it/ateco/([0-9-]+)"', t)}
    return _albero


def sottocategorie_2025(classe):
    """Le sottocategorie ATECO 2025 della classe, dalla pagina di codiceateco.it (in cache)."""
    t = get('https://codiceateco.it/classe?q=' + classe)
    if t is None:
        return None
    return sorted(set(re.findall(re.escape(classe) + r'\.\d\d', t)))


def liste_della_classe(classe, scoperte):
    """Le stringhe di codice con righe per una classe, scoperte una volta e poi in cache."""
    if classe in scoperte:
        return scoperte[classe]
    prove = [classe, classe + '.00'] + [f'{classe}.{d}' for d in range(10)]
    for k in sorted(albero_2007()):
        if k.startswith(classe + '.'):
            prove += [k, k + '0'] if len(k) == len(classe) + 2 else [k]
    nuove = sottocategorie_2025(classe)
    for k in nuove or []:
        prove += [k, k[:-1] + '0']
    prove = list(dict.fromkeys(prove))
    with ThreadPoolExecutor(2) as ex:
        esiti = list(ex.map(lambda c: pagina(c, 1), prove))
    piene = [c for c, righe in zip(prove, esiti) if righe]
    if nuove is None or any(r is None for r in esiti):
        # 18/10/2026: il DNS del Mac è caduto per qualche minuto e la scoperta di 28.41-28.96 è
        # uscita vuota. Una scoperta con buchi non si salva: si rifà alla passata dopo.
        print(f'  {classe}: scoperta incompleta (rete), non salvata', file=sys.stderr)
        return piene
    scoperte[classe] = piene
    os.makedirs(os.path.dirname(LISTE), exist_ok=True)
    json.dump(scoperte, open(LISTE, 'w'), indent=1, sort_keys=True)
    return piene


def righe_in_fascia(codice):
    """Scorre la lista finché il fatturato più alto della pagina scende sotto il milione."""
    n = 1
    while True:
        righe = pagina(codice, n)
        if righe is None:
            raise RuntimeError(f'pagina {n} della lista {codice} non scaricata')
        if not righe:
            return
        yield from righe
        fats = [r['fatturato'] for r in righe if r['fatturato']]
        if not fats or max(fats) < FATT_MIN:
            return
        n += 1


def norm(s):
    return re.sub(r'\s+', ' ', (s or '').upper().replace("'", '').replace('’', '')).strip()


def forma_giuridica(etichetta):
    """(sigla ammessa | None, motivo dello scarto | None)"""
    e = norm(etichetta)
    if not e:
        return None, 'forma giuridica non indicata'
    for rx, ok, fuori in FORME:
        if re.search(rx, e):
            return (ok, None) if ok else (None, f'forma {fuori}')
    return None, f'forma non mappata: {etichetta}'


def pochi_dipendenti(banda):
    """True se la banda dichiarata sta tutta sotto i 6. Etichette viste sulle schede il 18/10/2026:
    «nessuno», «1», «da 2 a 5», «da 6 a 9», «da 10 a 19», «da 20 a 49», «da 50 a 99», «da 100 a 249»;
    sulle schede senza la riga «N. Dipendenti» la banda manca: non dichiarata, si tiene."""
    if not banda:
        return False
    if re.fullmatch(r'\s*(nessuno|0)\s*', banda, re.I):
        return True     # «nessuno» è un'etichetta vera della scheda: zero dipendenti
    numeri = [int(n) for n in re.findall(r'\d+', banda)]
    return bool(numeri) and max(numeri) < 6


def motivo_scheda(x):
    if x.get('errore'):
        return x['errore']
    if x.get('stato') != 'Attiva':
        return f"stato {x.get('stato') or 'non indicato'}"
    sigla, fuori = forma_giuridica(x.get('forma'))
    if fuori:
        return fuori
    x['sigla'] = sigla
    if pochi_dipendenti(x.get('dipendenti')):
        return f"dipendenti {x['dipendenti']}"
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--prov', default=','.join(LOMBARDIA))
    ap.add_argument('--ateco', default='', help='classi o prefissi, separati da virgola (es. 25.62,46)')
    ap.add_argument('--max', type=int, default=0, help='si ferma dopo N aziende nuove in filtro')
    a = ap.parse_args()
    prov = {p.strip().upper() for p in a.prov.split(',') if p.strip()}
    fuori = prov - set(LOMBARDIA)
    if fuori:
        sys.exit(f'province fuori dalla Lombardia: {", ".join(sorted(fuori))}')
    filtri = [p.strip() for p in a.ateco.split(',') if p.strip()]
    classi = [c for c in CLASSE_SETTORE if not filtri or any(c.startswith(f) or f.startswith(c) for f in filtri)]
    if not classi:
        sys.exit('nessuna classe della tabella corrisponde a --ateco')

    scoperte = json.load(open(LISTE)) if os.path.exists(LISTE) else {}
    conti = {}
    nuove = 0

    def conta(motivo):
        conti[motivo] = conti.get(motivo, 0) + 1

    with db.connessione() as c:
        gia = {r[0] for r in c.execute('SELECT piva FROM aziende')}
        for classe in classi:
            liste = liste_della_classe(classe, scoperte)
            if filtri and not any(classe.startswith(f) for f in filtri):
                # --ateco 25.53.00: della classe si tiene solo la lista chiesta
                liste = [l for l in liste if any(l.startswith(f) for f in filtri)]
            settore = CLASSE_SETTORE[classe]
            print(f'{classe} {settore}: liste {", ".join(liste) or "nessuna"}', flush=True)
            for codice in liste:
                candidati = []
                try:
                    righe_lista = list(righe_in_fascia(codice))
                except RuntimeError as e:
                    print(f'  {codice}: {e}, la lista si riprende alla prossima passata', file=sys.stderr)
                    conta('lista interrotta dalla rete')
                    continue
                for r in righe_lista:
                    if r['piva'] in gia:
                        conta('già in base dati')
                        continue
                    if r['prov'] not in prov:
                        conta('fuori provincia')
                        continue
                    if not r['fatturato'] or not FATT_MIN <= r['fatturato'] <= FATT_MAX:
                        conta('fatturato fuori fascia')
                        continue
                    if re.search(r'liquidaz|fallim|concordato', r['nome'], re.I):
                        conta('in liquidazione o fallimento')
                        gia.add(r['piva'])
                        continue
                    gia.add(r['piva'])
                    candidati.append(r)
                with ThreadPoolExecutor(3) as ex:
                    schede = list(ex.map(scheda, candidati))
                for x in schede:
                    if a.max and nuove >= a.max:
                        break
                    m = motivo_scheda(x)
                    ora = db.adesso()
                    c.execute('''INSERT OR IGNORE INTO aziende (piva, nome, slug, fatturato, anno, ateco, attivita, forma,
                                 stato, dipendenti, indirizzo, comune, prov, settore, fase, note, creata, aggiornata)
                                 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                              (x['piva'], x['nome'], x['slug'], x['fatturato'], x.get('anno'), x.get('ateco'),
                               x.get('attivita'), x.get('forma'), x.get('stato'), x.get('dipendenti'),
                               x.get('indirizzo'), x['comune'], x['prov'], settore,
                               'scartata' if m else 'nuova',
                               f'aziende.py: {m} (lista {codice})' if m else f'lista {codice}', ora, ora))
                    if m:
                        conta(re.sub(r':.*', '', m) if m.startswith('forma non mappata') else m)
                        if m.startswith('forma non mappata'):
                            print('  ', m, '·', x['nome'], file=sys.stderr)
                    else:
                        conta('IN FILTRO')
                        nuove += 1
                c.commit()
                print(f'  {codice}: {len(candidati)} schede lette, {nuove} in filtro finora', flush=True)
                if a.max and nuove >= a.max:
                    break
            if a.max and nuove >= a.max:
                break

    print('\nConti di questa passata:')
    for k, v in sorted(conti.items(), key=lambda kv: -kv[1]):
        print(f'  {v:6}  {k}')
    with db.connessione() as c:
        print('Base dati per fase:', ', '.join(f'{f} {n}' for f, n in c.execute(
            'SELECT fase, COUNT(*) FROM aziende GROUP BY fase ORDER BY 2 DESC')))


if __name__ == '__main__':
    main()
