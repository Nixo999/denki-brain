#!/usr/bin/env python3
"""Controlla il TESTO di un sito: didascalie, etichette, frasi, leggibilita'.

    python3 01-Coding/strumenti/controlla-testo.py ~/lavoro/<cartella>
    python3 01-Coding/strumenti/controlla-testo.py --tutti

Nasce il 21/09/2026 da una bocciatura di Nicola: «sotto le foto hai scritto
delle cose completamente inutili a uno spettatore del sito, tipo descrizioni
della foto o titoletti completamente inutili». Misurato lo stesso giorno: sui
16 siti in ~/lavoro, 35 didascalie su 97 ripetevano il testo alternativo
dell'immagine.

`alt` e `figcaption` servono a due persone diverse. L'`alt` lo legge chi la
foto non la vede; la `figcaption` la legge chi la sta guardando. Se dicono la
stessa cosa, una delle due e' di troppo, ed e' sempre la seconda.

Esce 1 se qualcosa blocca. Accanto a controlla-sito.py e controlla-slop.py.
"""
import re
import sys
import unicodedata
from pathlib import Path

LAVORO = Path.home() / "lavoro"

# parole che non contano nel confronto fra alt e didascalia
VUOTE = {
    "il", "lo", "la", "i", "gli", "le", "un", "uno", "una", "di", "a", "da", "in",
    "con", "su", "per", "tra", "fra", "e", "ed", "o", "che", "del", "della", "dei",
    "delle", "dello", "degli", "al", "alla", "ai", "alle", "allo", "dal", "dalla",
    "nel", "nella", "nei", "sul", "sulla", "si", "non", "piu", "come", "dove",
}

# un micro-titolo che ripete la categoria di quello che sta etichettando
ETICHETTE = {
    "dove", "quando", "telefono", "orari", "orario", "indirizzo", "contatti",
    "contatto", "email", "mail", "whatsapp", "recapito", "info", "informazioni",
    "servizi", "chi siamo",
}

# un fatto che la foto non puo' dire da sola
FATTO = re.compile(
    r"\d|€|\beuro\b|\bmin\b|\bminuti\b|\bore\b|\bann[oi]\b|\bda\s+\d|\bprezz|\bdurat",
    re.I,
)


def senza_accenti(t):
    return "".join(c for c in unicodedata.normalize("NFD", t) if not unicodedata.combining(c))


def parole(t):
    t = senza_accenti(re.sub(r"<[^>]+>", " ", t)).lower()
    return [p for p in re.findall(r"[a-z]+", t) if p not in VUOTE and len(p) > 2]


def testo(t):
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"&[a-z]+;|&#\d+;", " ", t)
    return re.sub(r"\s+", " ", t).strip()


BLOCCHI = ("p", "li", "h1", "h2", "h3", "h4", "h5", "figcaption", "dd", "dt",
           "blockquote", "td", "th", "div", "section", "footer", "header", "title")


def visibile(html):
    """Il testo come lo legge una persona. Fra un blocco e l'altro ci va un
    confine di frase: senza, il titolo e la voce di elenco sotto si fondono in
    un periodo di trenta parole che nessuno ha mai scritto."""
    h = re.sub(r"<script.*?</script>|<style.*?</style>|<svg.*?</svg>|<!--.*?-->", " ", html, flags=re.S)
    h = re.sub(r"</(?:%s)\s*>" % "|".join(BLOCCHI), " ¶ ", h, flags=re.I)
    h = re.sub(r"<br\s*/?>", " ¶ ", h, flags=re.I)
    return testo(h)


def nome_proprio(t):
    """Un nome che la foto non dice: una maiuscola che non apre la frase."""
    p = t.split()
    return any(w[:1].isupper() for w in p[1:] if len(w) > 2)


def controlla(cartella):
    d = Path(cartella).expanduser()
    indice = d / "index.html"
    if not indice.exists():
        return None
    html = indice.read_text(encoding="utf-8", errors="ignore")
    blocca, avvisa = [], []

    # ── 1. didascalie ─────────────────────────────────────────────────────────
    for fig in re.findall(r"<figure\b.*?</figure>", html, re.S):
        cap = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", fig, re.S)
        if not cap:
            continue
        c = testo(cap.group(1))
        if not c:
            continue
        corta = (c[:52] + "…") if len(c) > 52 else c
        alt = re.search(r'\balt="([^"]*)"', fig)
        if alt and alt.group(1).strip():
            pa, pc = set(parole(alt.group(1))), set(parole(c))
            if pc and pa and len(pa & pc) >= max(2, round(0.5 * len(pc))):
                blocca.append(f"la didascalia ripete il testo alternativo: «{corta}»")
                continue
        # una citazione attribuita e' gia' un fatto
        citazione = re.search(r"<(blockquote|q)\b", fig) is not None
        if not citazione and not FATTO.search(c) and not nome_proprio(c):
            blocca.append(f"la didascalia non dice niente che la foto non dica: «{corta}»")

    # ── 2. micro-titoli che ripetono la categoria ─────────────────────────────
    # un'etichetta portata via dalla pagina e lasciata a chi legge con la voce
    # non e' un titoletto inutile: e' il contrario, ed e' la correzione giusta
    NASCOSTO = re.compile(r'class="[^"]*(?:solo-lettori|sr-only|visually-hidden|a11y)[^"]*"')
    micro = [m for m in re.findall(r"<dt[^>]*>(.*?)</dt>", html, re.S) if not NASCOSTO.search(m)]
    micro += [m[1] for m in re.findall(
        r'<(h3|h4|span|p|b)[^>]*class="[^"]*(?:etichett|occhiell|label|kicker|micro)[^"]*"[^>]*>(.*?)</\1>',
        html, re.S) if not NASCOSTO.search(m[0] + m[1])]
    trovate = sorted({testo(m) for m in micro if senza_accenti(testo(m)).lower().strip(" :") in ETICHETTE})
    if trovate:
        avvisa.append("micro-titoli che ripetono la categoria del contenuto sotto: "
                      + ", ".join(f"«{t}»" for t in trovate))

    # ── 3. frasi, leggibilita', punteggiatura ─────────────────────────────────
    t = visibile(html)
    frasi = [f.strip() for f in re.split(r"(?<=[.!?])\s+|\s*¶\s*", t) if len(f.split()) > 1]
    t = t.replace("¶", " ")
    if frasi:
        lunghe = [f for f in frasi if len(f.split()) > 30]
        if lunghe:
            avvisa.append(f"{len(lunghe)} frasi sopra le 30 parole, la piu' lunga di {max(len(f.split()) for f in lunghe)}")
        lettere = len(re.findall(r"[A-Za-zÀ-ſ]", t))
        n = len(t.split())
        gulpease = 89 + (300 * len(frasi) - 10 * lettere) / n if n else 0
        if gulpease < 55:
            avvisa.append(f"Gulpease {gulpease:.0f}: sotto 55 il testo e' faticoso per chi ha la licenza media")

    # i punti esclamativi delle recensioni citate non contano
    citato = " ".join(testo(q) for q in re.findall(r"<(?:blockquote|q)\b.*?</(?:blockquote|q)>", html, re.S))
    urla = t.count("!") - citato.count("!")
    if urla > 0:
        avvisa.append(f"{urla} punti esclamativi fuori dalle citazioni")

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
    cartelle = (sorted(c for c in LAVORO.iterdir() if (c / "index.html").exists())
                if args == ["--tutti"] else [Path(a) for a in args])
    risultati = [r for r in (controlla(c) for c in cartelle) if r]
    for r in risultati:
        stampa(r)
    sys.exit(1 if any(r["blocca"] for r in risultati) else 0)
