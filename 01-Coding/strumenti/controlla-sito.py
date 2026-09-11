#!/usr/bin/env python3
"""Dice se un sito sta sopra il livello di NG Barber e Fiftynine, o sotto.

    python3 01-Coding/strumenti/controlla-sito.py ~/lavoro/mikuma-site
    python3 01-Coding/strumenti/controlla-sito.py --tutti

Esiste perche' «i siti devono sempre migliorare, mai peggiorare» e' una frase,
e una frase cede sotto il volume. Questo e' il passo che la fa rispettare: si
lancia **prima di pubblicare**, e se il sito e' sotto il livello esce 1.

Il livello non e' inventato, e' misurato sui due siti che Nicola ha approvato.
Non misura la bellezza: misura le cose che quando mancano il sito e' sempre
brutto. Un sito che passa puo' essere ancora brutto; uno che non passa lo e'
di sicuro.
"""
import re
import subprocess
import sys
from pathlib import Path

MIN_SVG = 3        # NG Barber 8, Fiftynine 10, Mikuma 4, Lobidu 0
MIN_FOTO = 1080    # lato lungo. Le copertine dei Reel sono 360 e si vedono

# loghi, avatar e icone possono essere piccoli: non sono fotografia di contenuto
NON_FOTO = ("logo", "profile", "profilo", "avatar", "icon", "icona", "favicon")
# gestionali e cartelle che non sono vetrine: qui comanda il CLAUDE.md del repo
NON_VETRINE = {"opero-sito", "smooth-duty", "denki-brain", "sebapp-bolanos",
               "pixel-perfect-rebuild", "vibrant-web-foundation", "WeBolt-v1"}


def testo(d):
    t = ""
    for p in list(d.glob("*.html")) + sorted(d.glob("assets/*.css")):
        t += p.read_text(encoding="utf-8", errors="ignore")
    return t


def foto_piccole(d):
    piccole = []
    for p in sorted((d / "assets" / "img").glob("*")):
        if p.suffix.lower() not in (".jpg", ".jpeg", ".png", ".webp") or p.name.startswith("."):
            continue
        if any(x in p.name.lower() for x in NON_FOTO):
            continue
        try:
            out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(p)],
                                 capture_output=True, text=True).stdout
            n = [int(x) for x in re.findall(r":\s*(\d+)", out)]
            if n and max(n) < MIN_FOTO:
                piccole.append((p.name, max(n)))
        except Exception:
            pass
    return piccole


def controlla(d):
    d = Path(d).expanduser()
    if not (d / "index.html").exists():
        return None
    t = testo(d)
    robots = (d / "robots.txt").read_text(encoding="utf-8", errors="ignore") if (d / "robots.txt").exists() else ""
    toml = (d / "netlify.toml").read_text(encoding="utf-8", errors="ignore") if (d / "netlify.toml").exists() else ""
    piccole = foto_piccole(d)

    return {
        "nome": d.name,
        "esiti": [
            ("grafica inventata", t.count("<svg") >= MIN_SVG,
             f"{t.count('<svg')} <svg> inline, ne servono {MIN_SVG}. Senza, la pagina dipende tutta dalle foto"),
            ("racconto allo scroll", ("ScrollTrigger" in t) or ("animation-timeline" in t),
             "niente GSAP/ScrollTrigger ne' animation-timeline: e' un impaginato, non un racconto"),
            ("animazione d'apertura", (".js:not(.cattura)" in t) or ("gsap.timeline" in t),
             "nessuna apertura: manca il primo secondo"),
            # o le foto reggono, o il sito non dipende da loro. Fiftynine ha foto
            # da 640 e piace lo stesso: regge su dieci SVG inventati. Mikuma no.
            ("foto, oppure grafica che le sostituisca",
             (not piccole) or t.count("<svg") >= 6,
             f"{len(piccole)} foto sotto {MIN_FOTO}px e solo {t.count('<svg')} <svg> inventati: "
             "il sito dipende da foto che non reggono. O le chiedi al cliente, o disegni "
             "una pagina che non ne abbia bisogno (" +
             ", ".join(f"{n} {w}px" for n, w in piccole[:3]) + ")"),
            ("firma DenkiCode", "firma-denkicode" in t or "Powered by" in t,
             "manca la firma nel footer"),
            ("sbarramento meta", "noindex" in t, "manca <meta name=robots noindex>"),
            ("sbarramento header", "X-Robots-Tag" in toml, "manca X-Robots-Tag in netlify.toml"),
            ("sbarramento robots", "Disallow: /" in robots, "manca robots.txt"),
        ],
        "avvisi": ([] if (d / "assets" / "base.css").exists() else
                   ["nato prima dello starter: niente base.css, le trappole del reset "
                    "vanno verificate a mano"]),
    }


def stampa(r):
    rotti = [(n, p) for n, ok, p in r["esiti"] if not ok]
    segno = "OK " if not rotti else "NO "
    print(f"\n{segno}{r['nome']}  ({len(r['esiti']) - len(rotti)}/{len(r['esiti'])})")
    for n, perche in rotti:
        print(f"   ⛔ {n}: {perche}")
    for a in r["avvisi"]:
        print(f"   ·  {a}")
    return not rotti


if __name__ == "__main__":
    arg = sys.argv[1:] or ["."]
    if "--tutti" in arg:
        cartelle = sorted(p for p in (Path.home() / "lavoro").iterdir()
                          if (p / "index.html").exists() and p.name not in NON_VETRINE)
    else:
        cartelle = [Path(a).expanduser() for a in arg]
    tutti_ok = True
    for c in cartelle:
        r = controlla(c)
        if r is None:
            print(f"\n?? {c}: nessun index.html")
            continue
        tutti_ok &= stampa(r)
    print()
    sys.exit(0 if tutti_ok else 1)
