#!/usr/bin/env python3
"""Dice COM'E` fatto un sito vivo, con i fatti che si possono scrivere in un DM.

    python3 02-Sales/strumenti/esamina-sito.py dominio1.it dominio2.com ...
    python3 02-Sales/strumenti/esamina-sito.py --csv 02-Sales/liste/<lista>.csv

Il passo 3 di metodo-instagram dice se un sito c'e`. Questo dice se e` VECCHIO
o FATTO MALE, e perche`, con cose verificabili: niente https, non si adatta al
telefono (manca il viewport), l'anno in fondo alla pagina e` fermo, il costruttore
e` di un'altra era (Flash, tabelle, Joomla 1.x), la pagina pesa niente, ecc.
Chiesto da Patrick il 10 settembre 2026: si scrive solo a chi il sito non ce
l'ha, o ce l'ha davvero vecchio o fatto male. Il gancio 6 di dm-instagram-vetrina
si usa SOLO con un fatto uscito da qui.

Il DNS locale del Mac di Patrick a volte non risolve: i domini si risolvono
con Cloudflare DoH e si aprono con curl --resolve.

Con --csv legge la colonna «Esito verifica sito» di ogni riga, prende i domini
segnati (vivo ...) e (piattaforma ...) e appende il verdetto, marcato
`[esamina-sito]`.
"""
import csv, json, re, subprocess, sys, time, urllib.parse
from pathlib import Path

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
ANNO = time.localtime().tm_year


def doh(dom):
    """(ip | None, stato) via Cloudflare DoH. stato: ok | nxdomain | errore"""
    try:
        out = subprocess.run(["curl", "-s", "--max-time", "8",
                              f"https://cloudflare-dns.com/dns-query?name={dom}&type=A",
                              "-H", "accept: application/dns-json"], capture_output=True, text=True, timeout=12).stdout
        j = json.loads(out)
        if j.get("Status") == 3:
            return None, "nxdomain"
        a = [x["data"] for x in j.get("Answer", []) if x.get("type") == 1]
        return (a[0], "ok") if a else (None, "senza A")
    except Exception as e:
        return None, f"errore {e}"


def scarica(dom, schema="https"):
    """(codice http, corpo, header, url finale) aprendo con curl --resolve"""
    ip, stato = doh(dom)
    if not ip:
        return 0, "", "", stato
    res = []
    for h in (dom, "www." + dom if not dom.startswith("www.") else dom.removeprefix("www.")):
        res += ["--resolve", f"{h}:443:{ip}", "--resolve", f"{h}:80:{ip}"]
    try:
        r = subprocess.run(["curl", "-sL", "-k", "--max-time", "20", "-A", UA, "-D", "-", "-o", "-",
                            "-w", "\n@@URL@@%{url_effective}@@CODE@@%{http_code}", *res, f"{schema}://{dom}"],
                           capture_output=True, text=True, errors="replace", timeout=30).stdout
    except Exception as e:
        return 0, "", "", f"curl {e}"
    m = re.search(r"@@URL@@(.*?)@@CODE@@(\d+)$", r, re.S)
    url, code = (m.group(1), int(m.group(2))) if m else ("", 0)
    r = r[:m.start()] if m else r
    parti = re.split(r"\r?\n\r?\n", r, maxsplit=1)
    header, corpo = (parti[0], parti[1]) if len(parti) == 2 else ("", r)
    # con -L ci sono piu` blocchi di header: tengo l'ultimo per il corpo
    while corpo.lstrip().startswith("HTTP/"):
        parti = re.split(r"\r?\n\r?\n", corpo, maxsplit=1)
        header, corpo = (parti[0], parti[1]) if len(parti) == 2 else (corpo, "")
    return code, corpo, header, url


def esamina(dom):
    """Torna (verdetto, fatti[], dettagli{}). verdetto: VECCHIO | DUBBIO | OK | NON APRE"""
    dom = dom.lower().removeprefix("https://").removeprefix("http://").split("/")[0]
    code, corpo, header, url = scarica(dom, "https")
    https = code and url.startswith("https://") and code < 400
    if not https:
        code2, corpo2, header2, url2 = scarica(dom, "http")
        if code2 and code2 < 400:
            code, corpo, header, url = code2, corpo2, header2, url2
    if not code or code >= 400:
        return "NON APRE", [f"{dom} non apre (http {code or 'niente'}, {url or 'nessuna risposta'})"], {}
    testo = re.sub(r"<script.*?</script>|<style.*?</style>", " ", corpo, flags=re.S | re.I)
    visibile = re.sub(r"<[^>]+>", " ", testo)
    visibile = re.sub(r"\s+", " ", visibile).strip()
    t = re.search(r"<title[^>]*>(.*?)</title>", corpo, re.I | re.S)
    titolo = re.sub(r"\s+", " ", t.group(1)).strip()[:90] if t else ""
    gen = re.search(r'<meta[^>]+name=["\']generator["\'][^>]+content=["\']([^"\']+)', corpo, re.I)
    generator = gen.group(1)[:60] if gen else ""
    viewport = bool(re.search(r'<meta[^>]+name=["\']viewport["\']', corpo, re.I))
    anni = [int(a) for a in re.findall(r"(?:©|&copy;|copyright)\s*(?:\d{4}\s*[-–]\s*)?((?:19|20)\d{2})", corpo, re.I)]
    anni += [int(a) for a in re.findall(r"((?:19|20)\d{2})\s*[-–]\s*(?:oggi|today)", corpo, re.I)]
    anno_footer = max(anni) if anni else None
    lm = re.search(r"^last-modified:\s*(.+)$", header, re.I | re.M)
    parole = len(visibile.split())
    fatti, punti = [], 0
    if not https:
        fatti.append(f"apre solo in http, senza lucchetto (https non risponde)"); punti += 2
    if not viewport:
        fatti.append("non si adatta al telefono: manca il meta viewport"); punti += 2
    if anno_footer and anno_footer <= ANNO - 3:
        fatti.append(f"in fondo alla pagina è fermo al {anno_footer}"); punti += 2
    elif anno_footer and anno_footer <= ANNO - 2:
        fatti.append(f"in fondo alla pagina riporta il {anno_footer}"); punti += 1
    if re.search(r"\.swf|shockwave|application/x-shockwave-flash", corpo, re.I):
        fatti.append("usa ancora Flash, che nessun browser apre più"); punti += 3
    if re.search(r"<frameset|<frame ", corpo, re.I):
        fatti.append("è fatto a frame, come nel 2005"); punti += 3
    if re.search(r"<table[^>]*(width|border)=", corpo, re.I) and not viewport:
        fatti.append("impaginato a tabelle"); punti += 1
    vecchi = re.search(r"(joomla! 1\.|joomla! 2\.|wordpress 3\.|wordpress 4\.|frontpage|dreamweaver|"
                       r"incomedia website x5 evolution 1|nvu|kompozer|iweb)", (generator + " " + corpo[:20000]), re.I)
    if vecchi:
        fatti.append(f"costruito con {vecchi.group(1).strip()}"); punti += 2
    if parole < 60:
        fatti.append(f"la pagina ha {parole} parole in tutto: è una vetrina vuota"); punti += 1
    if re.search(r"just another wordpress site|^home page$|^untitled|^new site$|^benvenuto$|^welcome$|^home$", titolo, re.I):
        fatti.append(f"il titolo della pagina è ancora quello di default: «{titolo}»"); punti += 2
    wp = re.search(r"wordpress ([3-5])\.(\d+)", generator, re.I)
    if wp:
        fatti.append(f"gira su WordPress {wp.group(1)}.{wp.group(2)}, una versione ferma a qualche anno fa"); punti += 1
    if re.search(r"lorem ipsum", corpo, re.I):
        fatti.append("ha ancora il testo finto «lorem ipsum»"); punti += 2
    if re.search(r"sito in costruzione|under construction|coming soon|work in progress", visibile, re.I):
        fatti.append("dice «sito in costruzione»"); punti += 2
    plat = re.search(r"(wix\.com|wixstatic|jimdo|weebly|site123|webnode|godaddysites|squarespace|"
                     r"business\.site|altervista|blogspot|wordpress\.com|canva\.site|carrd\.co|strikingly)", (url + corpo[:30000]), re.I)
    if plat:
        fatti.append(f"sta su una piattaforma ({plat.group(1)})")
    if lm:
        fatti.append(f"il server lo dà modificato l'ultima volta il {lm.group(1).strip()[5:16]}")
    verdetto = "VECCHIO" if punti >= 3 else "DUBBIO" if punti >= 1 else "OK"
    dett = {"titolo": titolo, "generator": generator, "viewport": viewport, "https": bool(https),
            "anno": anno_footer, "parole": parole, "url": url}
    return verdetto, fatti, dett


def riga(dom):
    v, fatti, d = esamina(dom)
    extra = f" · titolo «{d['titolo']}»" if d.get("titolo") else ""
    extra += f" · {d['generator']}" if d.get("generator") else ""
    return f"[esamina-sito] {dom}: {v}" + (" (" + "; ".join(fatti) + ")" if fatti else "") + extra


def main_csv(percorso):
    p = Path(percorso)
    with p.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f); righe = list(r); campi = r.fieldnames
    col = next((c for c in campi if c.lower().startswith("esito verifica")), None)
    if not col:
        sys.exit("manca la colonna «Esito verifica sito»")
    n = 0
    for x in righe:
        v = x[col] or ""
        if "[esamina-sito]" in v:
            continue
        doms = re.findall(r"([a-z0-9.-]+\.[a-z]{2,6}) \((?:vivo|piattaforma)", v)
        for dm in dict.fromkeys(doms):
            x[col] = x[col].rstrip() + " · " + riga(dm); n += 1
            print(f"  {x.get('Account IG','?'):32} {x[col].split('[esamina-sito]')[-1][:140]}", flush=True)
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campi, lineterminator="\n"); w.writeheader(); w.writerows(righe)
    print(f"{n} siti esaminati in {p.name}")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == "--csv":
        main_csv(a[1])
    else:
        for d in a:
            print(riga(d))
