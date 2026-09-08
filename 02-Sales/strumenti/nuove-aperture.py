#!/usr/bin/env python3
"""Nuove aperture da Subito lavoro: chi assume per aprire.

Uso: python3 nuove-aperture.py [regione] [giorni]
     python3 nuove-aperture.py lombardia 30 > ../liste/AAAA-MM-GG-nuove-aperture.csv

Legge il JSON __NEXT_DATA__ delle pagine di ricerca (stdlib, niente login),
tiene solo gli annunci degli ultimi N giorni e scrive un CSV col telefono
se sta nel testo. La riga dice cosa e' stato cercato: la verifica la fa
verifica-sito.py, come per le altre liste.
"""
import csv, json, re, sys, time, urllib.request, urllib.parse
from datetime import datetime, timedelta

REGIONE = sys.argv[1] if len(sys.argv) > 1 else "lombardia"
GIORNI = int(sys.argv[2]) if len(sys.argv) > 2 else 30
PAROLE = ["nuova apertura", "nuovo locale", "prossima apertura", "apertura nuovo", "in apertura"]
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128 Safari/537.36"
APRE = re.compile(r"nuov[ao] apertura|nuovo locale|prossima apertura|in apertura|apertura (di|del|della) (un |nostr|nuov)|apriremo|apre a", re.I)
# ponytail: lista fissa di rumore visto il 8/9/2026 (immobiliari a provvigione, fotovoltaico, promoter, interinali); si allunga quando si vede altro
RUMORE = re.compile(r"immobiliar|tempocasa|tecnorete|real estate|fotovoltaic|promoter|telefonia|windtre|kena|call center|agenzia per il lavoro|tempoagency|apertura (nuovo |del nuovo )?ufficio|umana|adecco|manpower|randstad|humangest|during spa|valori s\.p\.a|gi group|synergie|openjob|porta a porta|network marketing|vigilanza|cantier", re.I)
TEL = re.compile(r"(?:\+39\s?)?(?:3\d{2}|0\d{1,3})[\s.\-]?\d{3}[\s.\-]?\d{3,4}")

def pagina(parola, n):
    q = urllib.parse.urlencode({"q": parola, "o": n})
    url = f"https://www.subito.it/annunci-{REGIONE}/vendita/offerte-lavoro/?{q}"
    html = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=20).read().decode()
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    if not m:
        return []
    out = []
    def walk(o):
        if isinstance(o, dict):
            if "subject" in o and "urn" in o:
                out.append(o)
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(json.loads(m.group(1)))
    return out

visti, righe = set(), []
limite = datetime.now() - timedelta(days=GIORNI)
for parola in PAROLE:
    for n in range(1, 4):  # ponytail: 3 pagine per parola, alza se la coda e' piena
        ann = pagina(parola, n)
        if not ann:
            break
        for a in ann:
            if a["urn"] in visti:
                continue
            visti.add(a["urn"])
            data = datetime.fromisoformat(a["date"][:19]) if a.get("date") else None
            if data and data < limite:
                continue
            testo = f'{a.get("subject","")} {a.get("body","")}'
            if not APRE.search(testo) or RUMORE.search(testo):
                continue
            tel = TEL.search(a.get("body", ""))
            righe.append({
                "data": data.date().isoformat() if data else "",
                "comune": a.get("geo", {}).get("town", {}).get("value", ""),
                "provincia": a.get("geo", {}).get("city", {}).get("shortName", ""),
                "titolo": a.get("subject", ""),
                "inserzionista": a.get("advertiser", {}).get("name", "") or "",
                "telefono": tel.group(0) if tel else "",
                "url": a.get("urls", {}).get("default", ""),
                "cercato": f"subito:{parola}",
                "estratto": re.sub(r"\s+", " ", a.get("body", ""))[:160],
            })
        time.sleep(1.5)

righe.sort(key=lambda r: r["data"], reverse=True)
w = csv.DictWriter(sys.stdout, fieldnames=list(righe[0].keys()) if righe else ["data"])
w.writeheader(); w.writerows(righe)
print(f"{len(righe)} annunci ({REGIONE}, {GIORNI} giorni, {len(visti)} letti)", file=sys.stderr)
