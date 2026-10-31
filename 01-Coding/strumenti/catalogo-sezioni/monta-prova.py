#!/usr/bin/env python3
"""Rimonta prova.html con tutte le sezioni del catalogo, nell'ordine di ORDINE.

    python3 01-Coding/strumenti/catalogo-sezioni/monta-prova.py

prova.html serve solo a verificare il catalogo: usa token.css cosi' com'e' (i valori di Groavel), base.css dello
starter, e al posto di ogni foto un riquadro grigio con le proporzioni giuste (un SVG in data URI, cosi' la pagina
non chiede file che non esistono e la console resta pulita). Si serve la cartella 01-Coding/strumenti/ e si apre
/catalogo-sezioni/prova.html: i percorsi verso ../starter-sito/ funzionano solo cosi'.

Si rilancia ogni volta che cambia una sezione: prova.html non si modifica a mano.
"""
import re
from math import gcd
from pathlib import Path
from urllib.parse import quote

QUI = Path(__file__).resolve().parent
SEZ = QUI / "sezioni"

# (file della sezione, classi del passaggio da mettere PRIMA di lei, se il campo cambia)
ORDINE = [
    ("hero-foto-laterale", None),
    ("prossima-uscita", "passaggio--da-fondo passaggio--a-superficie"),
    ("scena-tappe", "passaggio--da-superficie passaggio--a-fondo"),
    ("contrari-scorrevoli", None),
    ("servizio-tre-foto", None),
    ("righe-foto-piccole", "passaggio--da-fondo passaggio--a-superficie"),
    ("sedi-elenco", "passaggio--da-superficie passaggio--a-fondo"),
    ("galleria-irregolare", None),
    ("recensioni-voto", None),
    ("orari-adesso", "passaggio--da-fondo passaggio--a-superficie"),
    ("contatto-finale", None),
]
PIEDE_PASSAGGIO = "passaggio--da-superficie passaggio--a-piede"
JS = ["barra-fissa", "scena-tappe", "sedi-elenco", "orari-adesso", "contrari-scorrevoli"]


def leggi(nome):
    return (SEZ / f"{nome}.html").read_text(encoding="utf-8")


def riquadro(tag):
    """Sostituisce src e srcset di un <img> con un riquadro grigio delle sue proporzioni."""
    w = int(re.search(r'\bwidth="(\d+)"', tag).group(1))
    h = int(re.search(r'\bheight="(\d+)"', tag).group(1))
    src = re.search(r'\bsrc="([^"]+)"', tag).group(1)
    if src.endswith(".svg") and "logo-simbolo" in src:          # la firma DenkiCode: il file vero dello starter
        return tag.replace(f'src="{src}"', f'src="../starter-sito/{src}"')
    nome = Path(src).stem.replace("TODO-", "").rsplit("-", 1)[0] if "TODO-" in src else Path(src).stem
    g = gcd(w, h)
    rapporto = f"{w // g}:{h // g}"
    corpo = max(10, min(w, h) // 12)
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}'>"
           f"<rect width='{w}' height='{h}' fill='#3a3d42'/>"
           f"<text x='50%' y='50%' fill='#aeb3b8' font-family='monospace' font-size='{corpo}' text-anchor='middle'"
           f" dominant-baseline='middle'>{nome} {rapporto}</text></svg>")
    tag = re.sub(r'\s+srcset="[^"]*"', "", tag)
    return tag.replace(f'src="{src}"', f'src="data:image/svg+xml,{quote(svg)}"')


def sostituisci_foto(html):
    return re.sub(r"<img\b[^>]*>", lambda m: riquadro(m.group(0)), html, flags=re.S)


def passaggio(classi):
    p = leggi("passaggio-curva")
    p = re.sub(r"<!--.*?-->\s*", "", p, count=1, flags=re.S)       # il commento lungo sta una volta sola, nel file
    return p.replace("passaggio--da-fondo passaggio--a-superficie", classi)


def main():
    css = ["token.css", "comuni.css"] + [f"sezioni/{p.stem}.css" for p in sorted(SEZ.glob("*.css"))]
    righe = [
        "<!doctype html>",
        '<html lang="it">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>Catalogo delle sezioni DenkiCode: pagina di prova</title>",
        '<meta name="robots" content="noindex, nofollow">',
        '<link rel="icon" href="data:,">',
        "<!-- Generata da monta-prova.py: non si modifica a mano. -->",
        '<link rel="preconnect" href="https://fonts.googleapis.com">',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&amp;family=JetBrains+Mono:wght@400..700&amp;display=swap">',
        '<link rel="stylesheet" href="../starter-sito/assets/base.css">',
    ] + [f'<link rel="stylesheet" href="{c}">' for c in css] + [
        "<script>",
        "(function(d){",
        "  var cattura = new URLSearchParams(location.search).has('cattura');",
        "  d.classList.add('js');",
        "  if (cattura) d.classList.add('cattura');",
        "})(document.documentElement);",
        "</script>",
        "</head>",
        "<body>",
        sostituisci_foto(leggi("barra-fissa")),
        "<main>",
    ]
    for nome, classi in ORDINE:
        if classi:
            righe.append(passaggio(classi))
        righe.append(sostituisci_foto(leggi(nome)))
    righe += ["</main>", passaggio(PIEDE_PASSAGGIO), sostituisci_foto(leggi("piede-firma"))]
    righe += [
        '<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>',
        '<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js"></script>',
        "<script>",
        "/* Le rivelazioni dello starter (index.html dello starter, identiche): .rivela -> .dentro all'ingresso. */",
        "(function(){",
        "  var cattura = document.documentElement.classList.contains('cattura');",
        "  var fermo = matchMedia('(prefers-reduced-motion: reduce)').matches;",
        "  var rivela = document.querySelectorAll('.rivela');",
        "  if (cattura || fermo || !('IntersectionObserver' in window)) { rivela.forEach(function(el){ el.classList.add('dentro'); }); return; }",
        "  var oss = new IntersectionObserver(function(voci){",
        "    voci.forEach(function(v){ if (v.isIntersecting) { v.target.classList.add('dentro'); oss.unobserve(v.target); } });",
        "  }, { rootMargin: '0px 0px -12% 0px' });",
        "  rivela.forEach(function(el){ oss.observe(el); });",
        "  setTimeout(function(){ if (document.visibilityState === 'hidden') rivela.forEach(function(el){ el.classList.add('dentro'); }); }, 1200);",
        "})();",
        "</script>",
    ] + [f'<script src="sezioni/{j}.js"></script>' for j in JS] + ["</body>", "</html>", ""]
    (QUI / "prova.html").write_text("\n".join(righe), encoding="utf-8")
    passaggi = sum(1 for _, c in ORDINE if c) + 1
    print(f"prova.html: {len(ORDINE) + 2} sezioni con barra e piede, {passaggi} passaggi, {len(css)} fogli di stile, {len(JS)} script")


if __name__ == "__main__":
    main()
