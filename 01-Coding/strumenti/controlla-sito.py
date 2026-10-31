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
import shutil
import subprocess
import sys
from pathlib import Path

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


def lato_lungo(p):
    """Il lato lungo in pixel: sips sul Mac, Pillow su Linux. Senza nessuno dei due si
    ferma e lo dice: prima un errore finiva nell'except qui sotto e la foto passava."""
    if shutil.which("sips"):
        out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(p)],
                             capture_output=True, text=True).stdout
        n = [int(x) for x in re.findall(r":\s*(\d+)", out)]
        return max(n) if n else None
    try:
        from PIL import Image
    except ImportError:
        sys.exit("controlla-sito: per misurare le foto serve sips (macOS) o Pillow (pip install pillow)")
    with Image.open(p) as im:
        return max(im.size)


def foto_piccole(d):
    piccole = []
    for p in sorted((d / "assets" / "img").glob("*")):
        if p.suffix.lower() not in (".jpg", ".jpeg", ".png", ".webp") or p.name.startswith("."):
            continue
        if any(x in p.name.lower() for x in NON_FOTO):
            continue
        # foto-800.jpg accanto a foto.jpg e' la taglia piccola del srcset, non la foto
        m = re.match(r"(.+)-\d{3,4}$", p.stem)
        if m and any(q != p and (q.stem == m.group(1) or q.stem.startswith(m.group(1) + "-"))
                     for q in p.parent.iterdir()):
            continue
        try:
            lato = lato_lungo(p)
            if lato is not None and lato < MIN_FOTO:
                piccole.append((p.name, lato))
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
    # il JS sta in assets/*.js e testo() non lo legge: qui serve
    js = "".join(p.read_text(encoding="utf-8", errors="ignore") for p in sorted(d.glob("assets/*.js")))
    # racconto tipografico: scrub e un asse variabile. Regge una pagina con foto piccole
    tipografica = ("scrub" in (t + js)) and ("font-variation-settings" in (t + js))

    return {
        "nome": d.name,
        "esiti": [
            # «grafica inventata» (almeno MIN_SVG <svg> inline o un racconto tipografico)
            # e' stata tolta il 31/10/2026. Nicola, alla domanda se toglierla: «Sì, toglila»
            # (direttive-siti). Un sito non deve piu' contenere disegni nostri per passare.
            ("racconto allo scroll", ("ScrollTrigger" in t + js) or ("animation-timeline" in t),
             "niente GSAP/ScrollTrigger ne' animation-timeline: e' un impaginato, non un racconto"),
            ("animazione d'apertura", (".js:not(.cattura)" in t) or ("gsap.timeline" in t),
             "nessuna apertura: manca il primo secondo"),
            # Fiftynine ha foto da 640 e piace lo stesso: regge su dieci SVG. Dal 31/10/2026
            # i disegni non sono piu' una strada da consigliare, ma un sito che ce li ha gia'
            # non si boccia per questo: passa con un avviso (vedi sotto).
            ("foto da almeno 1080 px", (not piccole) or tipografica or t.count("<svg") >= 6,
             f"{len(piccole)} foto sotto {MIN_FOTO}px: si chiedono al cliente, o la pagina si regge "
             "su un racconto tipografico (scrub + font-variation-settings) (" +
             ", ".join(f"{n} {w}px" for n, w in piccole[:3]) + ")"),
            ("firma DenkiCode", "firma-denkicode" in t or "Powered by" in t,
             "manca la firma nel footer"),
            ("sbarramento meta", "noindex" in t, "manca <meta name=robots noindex>"),
            ("sbarramento header", "X-Robots-Tag" in toml, "manca X-Robots-Tag in netlify.toml"),
            ("sbarramento robots", "Disallow: /" in robots, "manca robots.txt"),
        ],
        "avvisi": ([] if (d / "assets" / "base.css").exists() else
                   ["nato prima dello starter: niente base.css, le trappole del reset "
                    "vanno verificate a mano"]) +
                  ([f"{len(piccole)} foto sotto {MIN_FOTO}px coperte da {t.count('<svg')} disegni inline: "
                    "dal 31/10/2026 la grafica inventata non e' piu' obbligatoria e non va usata per "
                    "coprire foto deboli"] if piccole and not tipografica and t.count("<svg") >= 6 else []),
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
