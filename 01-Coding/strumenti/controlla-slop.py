#!/usr/bin/env python3
"""Dice se un sito ha i segni che lo fanno sembrare fatto con l'AI, fra quelli che si
misurano nei file.

    python3 01-Coding/strumenti/controlla-slop.py ~/lavoro/pinkploy-site
    python3 01-Coding/strumenti/controlla-slop.py --tutti

Esiste perche' Nicola, il 17/09/2026: «usa poi quei risultati come base per controllare
i siti futuri». Le regole, e le fonti di ognuna, stanno in 01-Coding/stack/anti-slop-siti.md:
la ricerca del 17/09 sui segni visivi e sui testi in italiano, il pavimento di qualita' di
impeccable, direttive-siti.md e voce-denkicode.

BLOCCA: le fonti concordano e le nostre regole lo vietano gia'. Esce 1, il sito non si
consegna. AVVISA: si guarda e si decide. In fondo, se c'e', il rilevatore di impeccable
(`impeccable detect`, 61 regole fisse): e' severo anche con NG Barber, quindi avvisa e basta.

Vale per i siti nuovi. NG Barber e Fiftynine sono piu' vecchi della voce DenkiCode: i loro
trattini lunghi oggi bloccano, e il metro resta la loro grafica, non il loro copy.
Non sostituisce lo sguardo: un sito pulito qui puo' ancora sembrare finto.
"""
import colorsys
import datetime
import json
import re
import statistics
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

LAVORO = Path.home() / "lavoro"
IMPECCABLE = Path.home() / ".claude" / "skills" / "impeccable" / "scripts" / "impeccable"
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⭕]")

# Frasi fatte che non passano mai: ricerca del 17/09, lista A, voci senza ambiguita'
FRASI_BLOCCA = [
    "benvenuti nel nostro sito", "a 360 gradi", "soluzioni su misura", "soluzioni innovative",
    "leader del settore", "leader di mercato", "all'avanguardia", "nel cuore di", "esperienza unica",
    "un'esperienza unica", "offerta imperdibile", "prezzi imbattibili", "il tuo partner ideale",
    "per chi non si accontenta", "qualità che dura nel tempo", "tradizione che incontra l'innovazione",
    "innovazione e tradizione", "tradizione e innovazione", "una vasta gamma di", "da sempre al servizio",
    "grazie per averci scelto", "non perdere questa opportunità", "giovane e dinamica",
    "miglior rapporto qualità-prezzo", "miglior rapporto qualità prezzo", "lusso a un prezzo accessibile",
    "atmosfera unica", "panorama mozzafiato", "unico nel suo genere", "soddisfazione del cliente",
    "esperienze immersive", "gentili clienti", "vale la pena notare", "si potrebbe sostenere",
]
# Parole che contano per densita', non alla prima comparsa
PAROLE_AVVISA = [
    "davvero", "veramente", "approfondire", "valorizzare", "vanta", "rinomat", "vibrante", "eccellenza",
    "passione", "appassionat", "qualità", "su misura", "innovativ", "professionalità", "cura dei dettagli",
    "ruolo fondamentale", "ruolo cruciale", "testimonianza di", "ricco di storia", "incastonat", "immers",
]
FONT_ABUSATI = [
    "Inter", "Roboto", "Open Sans", "Lato", "Montserrat", "Arial", "Helvetica", "Geist", "Mona Sans",
    "Plus Jakarta Sans", "DM Sans", "Manrope", "Space Grotesk", "Instrument Serif", "Instrument Sans",
    "Fraunces", "Recoleta", "Bricolage Grotesque", "Syne", "Sora",
]


class Pagina(HTMLParser):
    """Il testo visibile, il testo dei titoli, le classi. Senza script, stili e svg."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.testo, self.titoli, self.classi, self.title = [], [], [], ""
        self._salta, self._titolo, self._in_title = 0, None, False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("class"):
            self.classi.extend(a["class"].split())
        if tag in ("script", "style", "svg", "noscript", "template"):
            self._salta += 1
        elif tag in ("h1", "h2", "h3"):
            self._titolo = [tag, []]
        elif tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag in ("script", "style", "svg", "noscript", "template") and self._salta:
            self._salta -= 1
        elif self._titolo and tag == self._titolo[0]:
            self.titoli.append((tag, " ".join(" ".join(self._titolo[1]).split())))
            self._titolo = None
        elif tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
            return
        if self._salta:
            return
        self.testo.append(data)
        if self._titolo:
            self._titolo[1].append(data)


def testo_di(html):
    p = Pagina()
    p.feed(html)
    return " ".join(" ".join(p.testo).split()), p


def colori(css):
    """I colori esadecimali del CSS, come (esadecimale, tonalita' in gradi, saturazione, luminosita')."""
    visti = []
    for h in re.findall(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", css):
        h = "".join(c * 2 for c in h) if len(h) == 3 else h
        r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
        tono, luce, sat = colorsys.rgb_to_hls(r, g, b)
        visti.append((h.lower(), tono * 360, sat, luce))
    return visti


def vicino(hexa, bersaglio, soglia):
    a = [int(hexa[i:i + 2], 16) for i in (0, 2, 4)]
    b = [int(bersaglio[i:i + 2], 16) for i in (0, 2, 4)]
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5 < soglia


def impeccable(indice):
    """I risultati di impeccable detect, per regola. None se impeccable non c'e'."""
    if not IMPECCABLE.exists():
        return None
    try:
        out = subprocess.run([str(IMPECCABLE), "detect", "--json", "--no-advisory", str(indice)],
                             capture_output=True, text=True, timeout=180).stdout
        voci = json.loads(out or "[]")
    except (subprocess.TimeoutExpired, json.JSONDecodeError):
        return None
    conta = {}
    for v in voci:
        conta[v.get("antipattern", "?")] = conta.get(v.get("antipattern", "?"), 0) + 1
    return conta


def controlla(d, con_impeccable=True):
    d = Path(d).expanduser()
    indice = d / "index.html"
    if not indice.exists():
        return None
    html = indice.read_text(encoding="utf-8", errors="ignore")
    css = re.sub(r"<script\b.*?</script>", "", html, flags=re.S | re.I) + "".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for p in d.rglob("*.css") if "node_modules" not in p.parts and ".cantiere" not in p.parts
    )
    testo, p = testo_di(html)
    basso = testo.lower()
    blocca, avvisa = [], []

    # --- BLOCCA: testi ---------------------------------------------------------
    segnaposti = re.findall(
        r"lorem ipsum|your company|company name|john doe|jane doe|\bacme\b|example\.com|\(555\)"
        r"|\[(?:nome|numero|via|indirizzo|telefono|profilo)[^\]]*\]|\bTODO\b|\bXXX\b|da definire|inserisci qui",
        testo, re.I)
    if segnaposti:
        blocca.append(f"segnaposto nel testo: {', '.join(sorted(set(segnaposti))[:4])}")
    if re.search(r"<img[^>]+src=[\"'](?:https?://)?(?:[\w.-]*\.)?(?:picsum\.photos|placehold|unsplash)", html, re.I):
        blocca.append("immagini di riempitivo o di stock (picsum, placehold, unsplash): servono le foto vere")
    processo = re.findall(r"\b(?:in questa sezione|qui trovi|qui sotto trovi|abbiamo inserito|ho inserito|da confermare"
                          r"|non confermat\w*|orari (?:presi )?da google|foto (?:prese )?da instagram|fonte:)", basso)
    if processo:
        blocca.append(f"tracce del nostro lavoro in pagina: {', '.join(sorted(set(processo)))} (voce-denkicode, il muro)")
    trattini = testo.count("—")
    if trattini:
        blocca.append(f"{trattini} trattini lunghi nel testo: zero, con virgola, punto o « – » (voce-denkicode)")
    # le citazioni del cliente fra « » sono parole sue: non contano
    senza_citazioni = re.sub(r"«[^»]*»", " ", testo)
    non_x = re.findall(r"\bnon\s+solo\b[^.!?\n]{1,80}?\bma\s+anche\b", senza_citazioni, re.I) + re.findall(
        r"\bnon\s+(?:è|sono|era|erano|si\s+tratta\s+di|vendiamo|offriamo|facciamo|siamo)\b[^.!?\n]{1,60}?[,;:]\s*(?:ma\s+)?"
        r"(?:è|sono|era|erano|si\s+tratta\s+di|vendiamo|offriamo|facciamo|siamo)\b", senza_citazioni, re.I)
    if non_x:
        blocca.append(f"«non è X, è Y»: {len(non_x)} volte, la firma piu' riconoscibile del copy generato. Si dice Y")
    connettivi = re.findall(r"(?:^|(?<=[.!?]\s))(?:Inoltre|Perciò|Dunque|Quindi|Di conseguenza|Insomma)\b", testo)
    if connettivi:
        blocca.append(f"frasi che aprono con un connettivo da tema: {', '.join(sorted(set(connettivi)))} (voce-denkicode)")
    frasi = [f for f in FRASI_BLOCCA if f in basso]
    if frasi:
        blocca.append(f"frasi fatte: {', '.join(frasi[:5])}")
    emoji = EMOJI.findall(testo)
    if emoji:
        blocca.append(f"emoji o glifi al posto delle icone: {''.join(sorted(set(emoji)))[:10]} (craft-floor)")

    # --- BLOCCA: grafica e codice ----------------------------------------------
    if re.search(r"background-clip\s*:\s*text", css) and re.search(r"gradient\(", css):
        blocca.append("testo con sfumatura: l'enfasi viene da peso e misura (craft-floor)")
    if re.search(r"cdn\.tailwindcss\.com|@tailwindcss/browser", html):
        blocca.append("Tailwind dal CDN di prova: e' fatto per lo sviluppo, non per un sito vero")

    # --- AVVISA: testi -----------------------------------------------------------
    parole = [w for w in PAROLE_AVVISA if w in basso]
    if parole:
        avvisa.append(f"parole da densita': {', '.join(parole[:6])}. Ognuna va sostituita con un fatto")
    superlativi = re.findall(r"\b(?:il|la|i|le) miglior[ei]?\b|\b(?:il|la|i|le) più \w+|\bstraordinari[oae]?\b", basso)
    if superlativi:
        avvisa.append(f"superlativi: {', '.join(sorted(set(superlativi))[:5])} (direttiva 14/09)")
    tre = re.findall(r"\b[\w'’]+(?:\s+[\w'’]+){0,2},\s+[\w'’]+(?:\s+[\w'’]+){0,2}\s+(?:e|ed|o)\s+[\w'’]+(?:\s+[\w'’]+){0,2}", testo)
    if len(tre) >= 4:
        avvisa.append(f"{len(tre)} gruppi di tre, per esempio «{tre[0]}»: due voci, o quattro diverse (voce-denkicode)")
    periodi = [len(s.split()) for s in re.split(r"(?<=[.!?])\s+", testo) if len(s.split()) >= 2]
    if len(periodi) >= 15:
        cv = statistics.pstdev(periodi) / statistics.mean(periodi)
        if cv < 0.4:
            avvisa.append(f"ritmo piatto: le frasi sono tutte lunghe uguali (variazione {cv:.2f}, sotto 0,40)")
    if re.search(r"content\s*:\s*[\"'](?:\\2014|\u2014)", css):
        avvisa.append("trattino lungo come decorazione nel CSS (content): il testo lo nasconde, la pagina lo mostra")
    h1 = [t for tag, t in p.titoli if tag == "h1"]
    if h1 and len(h1[0].split()) > 7:
        avvisa.append(f"titolo principale lungo {len(h1[0].split())} parole: il nome del cliente e una frase sotto (direttiva 14/09)")
    # niente parole di una lettera: la I di «via Umberto I» e' un numero, non un articolo
    minuscole = {"Il", "Lo", "La", "Gli", "Le", "Un", "Una", "Di", "Del", "Della", "Dei", "Delle", "Da", "In", "Con", "Su",
                 "Per", "Tra", "Fra", "Ed", "Nostro", "Nostra", "Nostri", "Nostre", "Tuo", "Tua", "Tuoi", "Tue", "Chi", "Come", "Dove", "Cosa"}
    maiuscole = [t for _, t in p.titoli if any(w in minuscole for w in re.findall(r"(?<=\s)[A-ZÀ-Ý][\w'’]*", re.sub(r"^\s*\d+[.)]?\s+", "", t)))]
    if maiuscole:
        avvisa.append(f"titoli con le maiuscole all'inglese: «{maiuscole[0][:60]}». In italiano solo la prima parola")
    mesi = re.findall(r"(?<=[a-zà-ù,;]\s)(?:Gennaio|Febbraio|Marzo|Aprile|Maggio|Giugno|Luglio|Agosto|Settembre|Ottobre|Novembre|Dicembre"
                      r"|Lunedì|Martedì|Mercoledì|Giovedì|Venerdì|Sabato|Domenica)\b(?!\s*[\d:–-])", testo)
    if mesi:
        avvisa.append(f"mesi o giorni maiuscoli a meta' frase: {', '.join(sorted(set(mesi))[:3])} (Treccani: minuscoli)")
    if re.search(r"<li[^>]*>\s*<(?:strong|b)>[^<]{1,40}:\s*</(?:strong|b)>|<li[^>]*>\s*<(?:strong|b)>[^<]{1,40}</(?:strong|b)>\s*:", html, re.I):
        avvisa.append("elenchi con «**Titolo:** testo»: e' la formattazione di una chat, non di un sito")
    if re.search(r"[“”]", testo) and '"' in testo:
        avvisa.append("virgolette dritte e curve mischiate: uno stile solo, in italiano « »")
    sezioni = re.findall(r"<section\b.*?</section>", html, re.S | re.I)
    vuote = 0
    for s in sezioni:
        t, _ = testo_di(s)
        if len(t.split()) >= 25 and not re.search(r"\d|€|\b(?:via|viale|piazza|corso|largo|vicolo)\s+[A-ZÀ-Ý]", t):
            vuote += 1
    if vuote:
        avvisa.append(f"{vuote} sezioni senza un fatto verificabile (numero, prezzo, orario, indirizzo): testo che starebbe su qualunque sito")
    numeri = re.findall(r"(?<![\w.,])0[1-9](?![\w.,:/])", testo)
    if len(numeri) >= 3:
        avvisa.append("numeri di sezione 01, 02, 03: solo se la sequenza dice qualcosa (craft-floor)")
    statistiche = re.findall(r"(?<![\w.,])\d[\d.,]*\s?(?:k|K|\+|%)(?![\w])", testo)
    if len(statistiche) >= 3:
        avvisa.append(f"file di numeri da vetrina ({', '.join(statistiche[:3])}): numeri veri o niente (craft-floor)")
    frecce = len(re.findall(r"→\s*</(?:a|button)>", html))
    if frecce >= 3:
        avvisa.append(f"freccia → in fondo a {frecce} link o bottoni: decorazione di serie")

    # --- AVVISA: grafica -----------------------------------------------------------
    occhielli = sorted({c for c in p.classi if re.search(r"eyebrow|kicker|overline|pre-?title|supertitle", c, re.I)})
    if occhielli:
        avvisa.append(f"occhiello sopra il titolo: classi {', '.join(occhielli[:4])} (craft-floor lo vieta; NG Barber ne ha uno)")
    if re.search(r"<h1\b[^>]*>(?:(?!</h1>).)*<(?:em|i)\b", html, re.S | re.I):
        avvisa.append("una parola del titolo in corsivo o di un altro colore: il segno piu' comune di pagina generata")
    # conta il primo font di ogni lista, non quelli di riserva, e le famiglie chieste a Google Fonts
    primi = {m.strip().strip("'\"") for m in re.findall(r"font-family\s*:\s*([^,;{}]+)", css)}
    primi |= {m.replace("+", " ") for m in re.findall(r"family=([A-Za-z+]+)", html)}
    font = [f for f in FONT_ABUSATI if f in primi]
    if font:
        avvisa.append(f"font abusati dai modelli: {', '.join(font[:4])}. Se non vengono dal cliente, si cambiano")
    cs = colori(css)
    viola = [h for h, tono, sat, luce in cs if 250 <= tono <= 310 and sat > 0.25 and 0.15 < luce < 0.85]
    if len(viola) >= 2:
        avvisa.append(f"viola e indaco ({', '.join(sorted(set(viola))[:3])}): il colore di serie dei generatori. Solo se e' del cliente")
    if any(vicino(h, "f4f1ea", 18) for h, *_ in cs) and any(vicino(h, "d97757", 30) for h, *_ in cs):
        avvisa.append("crema con accento terracotta: la palette di gusto che esce da sola ai modelli")
    bagliori = [m for m in re.finditer(r"box-shadow\s*:\s*0(?:px)?\s+0(?:px)?\s+(\d+)px[^;]*", css) if int(m.group(1)) >= 15 and re.search(r"#[0-9a-f]{6}|rgba?\(\s*\d+\s*,\s*\d+", m.group(0), re.I)]
    if bagliori:
        avvisa.append(f"{len(bagliori)} aloni colorati senza sfalsamento (box-shadow 0 0 grande): decorazione, non profondita'")
    if re.search(r"filter\s*:\s*blur\(\s*(?:[4-9]\d|\d{3,})px", css):
        avvisa.append("macchie sfocate come sfondo (blur di 40px o piu'): si mostra il posto, non un bagliore")
    if len(re.findall(r"backdrop-filter\s*:", css)) > 2:
        avvisa.append("vetro sfocato usato piu' volte: fuori dalla navigazione e' decorazione (craft-floor)")
    strisce = [c for c in re.findall(r"border-(?:left|right)\s*:\s*(?:[2-9]|\d{2,})px\s+solid\s+([^;}]+)", css)
               if c.strip().startswith("var(") or any(sat > 0.2 and 0.1 < luce < 0.9 for _, _, sat, luce in colori(c))]
    if strisce:
        avvisa.append("striscia colorata sul lato di un blocco (craft-floor, il segno piu' riconoscibile per impeccable)")
    if re.search(r"box-shadow\s*:\s*-?\d+(?:\.\d+)?px\s+-?\d+(?:\.\d+)?px\s+0(?:px)?\s", css):
        avvisa.append("ombra dura sfalsata: solo in un mondo davvero neobrutalista (craft-floor)")
    if re.search(r"font-family\s*:\s*['\"]?(?:Impact|Arial Black)", css, re.I):
        avvisa.append("font di sistema come voce dei titoli (craft-floor)")
    if re.search(r"cubic-bezier\(\s*[\d.]+\s*,\s*(?:-0?\.[2-9]|-\d|1\.[2-9]|[2-9])", css):
        avvisa.append("easing che rimbalza: curve che vanno oltre il bersaglio leggono come effetto di serie")
    if re.search(r"img:hover[^{]*\{[^}]*scale", css) or "data-aos" in html:
        avvisa.append("zoom sulle foto al passaggio o animazioni AOS: effetti di serie")
    mancano = [n for n, rx in (("::selection", r"::selection"), (":focus-visible", r":focus-visible"), ("caret-color", r"caret-color"), ("text-underline-offset", r"text-underline-offset")) if not re.search(rx, css)]
    if len(mancano) >= 3:
        avvisa.append(f"superfici del browser non disegnate: mancano {', '.join(mancano)} (craft-floor)")

    # --- AVVISA: pagina -------------------------------------------------------------
    anni = [int(a) for a in re.findall(r"©\s*(20\d\d)", testo)]
    if anni and max(anni) != datetime.date.today().year:
        avvisa.append(f"© {max(anni)} nel footer: l'anno e' vecchio")
    if not re.search(r"rel=[\"'](?:shortcut )?icon", html):
        avvisa.append("nessuna favicon: resta quella di default del browser")
    if not re.search(r"property=[\"']og:image", html):
        avvisa.append("nessuna og:image: condiviso su WhatsApp il link esce senza anteprima")
    if re.search(r"href=[\"']#[\"']", html):
        avvisa.append("link che non portano da nessuna parte (href=\"#\")")

    risultato = {"sito": d.name, "blocca": blocca, "avvisa": avvisa, "impeccable": None}
    if con_impeccable:
        risultato["impeccable"] = impeccable(indice)
    return risultato


def stampa(r):
    esito = "NO" if r["blocca"] else "OK"
    print(f"{esito} {r['sito']}  ({len(r['blocca'])} blocca, {len(r['avvisa'])} avvisa)")
    for b in r["blocca"]:
        print(f"   ⛔ {b}")
    for a in r["avvisa"]:
        print(f"   ·  {a}")
    if r["impeccable"]:
        voci = ", ".join(f"{k} {v}" for k, v in sorted(r["impeccable"].items(), key=lambda kv: -kv[1]))
        print(f"   ·  impeccable detect, {sum(r['impeccable'].values())} segnalazioni: {voci}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--senza-impeccable"]
    if not args:
        sys.exit(__doc__)
    con_impeccable = "--senza-impeccable" not in sys.argv
    cartelle = sorted(c for c in LAVORO.iterdir() if (c / "index.html").exists()) if args == ["--tutti"] else [Path(a) for a in args]
    risultati = [r for r in (controlla(c, con_impeccable) for c in cartelle) if r]
    for r in risultati:
        stampa(r)
    sys.exit(1 if any(r["blocca"] for r in risultati) else 0)
