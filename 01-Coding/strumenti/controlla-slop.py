#!/usr/bin/env python3
"""Dice se un sito ha i segni che lo fanno sembrare fatto con l'AI, fra quelli che si
misurano nei file.

    python3 01-Coding/strumenti/controlla-slop.py ~/lavoro/pinkploy-site
    python3 01-Coding/strumenti/controlla-slop.py --tutti

Esiste perche' Nicola, il 17/09/2026: «usa poi quei risultati come base per controllare
i siti futuri». Le regole vengono dal pavimento di qualita' di impeccable
(reference/craft-floor.md), da direttive-siti.md, da voce-denkicode e dalla ricerca sull'AI
slop del 17/09/2026.

Due livelli: BLOCCA fa uscire 1 e il sito non si consegna; AVVISA si guarda e si decide.
Non sostituisce lo sguardo: un sito pulito qui puo' ancora sembrare finto.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

LAVORO = Path.home() / "lavoro"
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⭕]")


class Pagina(HTMLParser):
    """Il testo visibile, e il testo di ogni titolo, senza script, stili e svg."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.testo, self.titoli, self.classi = [], [], []
        self._salta, self._titolo = 0, None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("class"):
            self.classi.extend(a["class"].split())
        if tag in ("script", "style", "svg", "noscript", "template"):
            self._salta += 1
        elif tag in ("h1", "h2", "h3"):
            self._titolo = [tag, []]

    def handle_endtag(self, tag):
        if tag in ("script", "style", "svg", "noscript", "template") and self._salta:
            self._salta -= 1
        elif self._titolo and tag == self._titolo[0]:
            self.titoli.append((tag, " ".join(" ".join(self._titolo[1]).split())))
            self._titolo = None

    def handle_data(self, data):
        if self._salta:
            return
        self.testo.append(data)
        if self._titolo:
            self._titolo[1].append(data)


def leggi(d):
    html = (d / "index.html").read_text(encoding="utf-8", errors="ignore")
    css = html + "".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for p in d.rglob("*.css") if "node_modules" not in p.parts and ".cantiere" not in p.parts
    )
    p = Pagina()
    p.feed(html)
    testo = " ".join(" ".join(p.testo).split())
    return html, css, testo, p


def controlla(d):
    d = Path(d).expanduser()
    if not (d / "index.html").exists():
        return None
    html, css, testo, p = leggi(d)
    basso = testo.lower()
    blocca, avvisa = [], []

    # --- BLOCCA ---------------------------------------------------------------
    segnaposti = re.findall(r"lorem ipsum|\[(?:nome|numero|via|indirizzo|telefono|profilo)[^\]]*\]|\bTODO\b|\bXXX\b|da definire|inserisci qui", testo, re.I)
    if segnaposti:
        blocca.append(f"segnaposto nel testo: {', '.join(sorted(set(segnaposti))[:4])}")
    note = re.findall(r"\b(?:in questa sezione|qui trovi|qui sotto trovi|abbiamo inserito|ho inserito|questa sezione (?:mostra|racconta|presenta))\b", basso)
    if note:
        blocca.append(f"note di chi ha costruito il sito, non del cliente: {', '.join(sorted(set(note)))} (direttiva 14/09)")
    emoji = EMOJI.findall(testo)
    if emoji:
        blocca.append(f"emoji al posto delle icone: {''.join(sorted(set(emoji)))[:10]} (craft-floor)")
    if re.search(r"background-clip\s*:\s*text", css) and re.search(r"gradient\(", css):
        blocca.append("testo con sfumatura: l'enfasi viene da peso e misura (craft-floor)")

    # --- AVVISA ---------------------------------------------------------------
    # craft-floor lo vieta sempre, ma NG Barber, che e' il metro approvato da Nicola, ne ha uno
    occhielli = sorted({c for c in p.classi if re.search(r"eyebrow|kicker|overline|pre-?title|supertitle", c, re.I)})
    if occhielli:
        avvisa.append(f"occhiello sopra il titolo: classi {', '.join(occhielli[:4])} (craft-floor lo vieta; NG Barber ne ha uno)")
    superlativi = re.findall(r"\b(?:il|la|i|le) miglior[ei]?\b|\b(?:il|la|i|le) più \w+|\bunic[oa] nel suo genere\b|\bstraordinari[oae]?\b", basso)
    if superlativi:
        avvisa.append(f"superlativi: {', '.join(sorted(set(superlativi))[:5])} (direttiva 14/09: niente «la migliore del mondo»)")
    trattini = testo.count("—")
    if trattini:
        avvisa.append(f"{trattini} trattini lunghi nel testo: in italiano leggono come testo generato (voce-denkicode)")
    h1 = [t for tag, t in p.titoli if tag == "h1"]
    if h1 and len(h1[0].split()) > 7:
        avvisa.append(f"titolo principale lungo {len(h1[0].split())} parole: il nome del cliente e una frase sotto (direttiva 14/09)")
    numeri = re.findall(r"(?<![\w.,])0[1-9](?![\w.,:/])", testo)
    if len(numeri) >= 3:
        avvisa.append("numeri di sezione 01, 02, 03: solo se la sequenza dice qualcosa (craft-floor)")
    if re.search(r"box-shadow\s*:\s*-?\d+(?:\.\d+)?px\s+-?\d+(?:\.\d+)?px\s+0(?:px)?\s", css):
        avvisa.append("ombra dura sfalsata: solo in un mondo davvero neobrutalista (craft-floor)")
    if re.search(r"border-(?:left|right)\s*:\s*(?:[2-9]|\d{2,})px", css):
        avvisa.append("bordo colorato a sinistra o a destra oltre 1px su blocchi (craft-floor)")
    if re.search(r"font-family\s*:\s*['\"]?(?:Impact|Arial Black)", css, re.I):
        avvisa.append("font di sistema come voce dei titoli (craft-floor)")
    superfici = [nome for nome, rx in (("::selection", r"::selection"), (":focus-visible", r":focus-visible"), ("caret-color", r"caret-color")) if not re.search(rx, css)]
    if len(superfici) == 3:
        avvisa.append("superfici del browser non disegnate: niente ::selection, :focus-visible, caret-color (craft-floor)")

    return {"sito": d.name, "blocca": blocca, "avvisa": avvisa}


def stampa(r):
    esito = "NO" if r["blocca"] else "OK"
    print(f"{esito} {r['sito']}  ({len(r['blocca'])} blocca, {len(r['avvisa'])} avvisa)")
    for b in r["blocca"]:
        print(f"   ⛔ {b}")
    for a in r["avvisa"]:
        print(f"   ·  {a}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    cartelle = sorted(c for c in LAVORO.iterdir() if (c / "index.html").exists()) if args == ["--tutti"] else [Path(a) for a in args]
    risultati = [r for r in (controlla(c) for c in cartelle) if r]
    for r in risultati:
        stampa(r)
    sys.exit(1 if any(r["blocca"] for r in risultati) else 0)
