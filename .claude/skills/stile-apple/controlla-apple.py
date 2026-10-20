#!/usr/bin/env python3
"""controlla-apple: cerca nel codice web gli errori tipici delle imitazioni Apple.

Uso:
  python3 controlla-apple.py <cartella>   esce con 1 se trova un errore che blocca
  python3 controlla-apple.py --prova      prova lo script su un esempio sbagliato e sulla skill

Legge .css .scss .html .jsx .tsx .js .ts .vue .svelte .astro e salta node_modules, dist,
build e .git. Un risultato è un indizio, non un verdetto: si apre il file e si guarda.
Le regole e il loro perché stanno in SKILL.md, sezione «Il controllo».
"""
import re
import sys
import tempfile
from pathlib import Path

EST = {".css", ".scss", ".html", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte", ".astro"}
SALTA = {"node_modules", "dist", "build", ".git", ".next", ".astro", "vendor"}
TOKEN = {"apple.css"}  # il file dei token può contenere colori scritti a mano

# (codice, livello, espressione, messaggio): controlli riga per riga
RIGHE = [
    ("SF-FONT", "BLOCCA", r"@font-face[^}]*SF[ -]?Pro|url\([^)]*SF-?Pro",
     "SF Pro servito come font web: la licenza Apple lo vieta. Si usa lo stack di sistema."),
    ("SF-SIMBOLI", "BLOCCA", "[\U000F0000-\U0010FFFF]",
     "glifo di SF Symbols scritto come carattere: fuori da Apple non si vede, e la licenza non copre il web."),
    ("CONTRASTO", "BLOCCA", r"prefers-contrast:\s*high",
     "prefers-contrast: high non esiste e non scatta mai. Il valore giusto è more."),
    ("ZOOM", "BLOCCA", r"user-scalable\s*=\s*no|maximum-scale\s*=\s*1(\.0)?\b",
     "zoom bloccato: chi ingrandisce il testo non può più farlo."),
    ("TRANS-ALL", "AVVISA", r"transition(-property)?:\s*all\b",
     "transition: all. Si animano solo le proprietà che servono, con la loro durata."),
    ("ANIM-LAYOUT", "AVVISA", r"transition[^;{}]*\b(width|height|top|left|margin|padding)\b",
     "transizione su una misura di layout: si anima transform o opacity."),
    ("MAIUSCOLO", "AVVISA", r"text-transform:\s*uppercase",
     "testo tutto maiuscolo: da iOS 26 i titoli dei gruppi sono in maiuscolo/minuscolo."),
    ("PESO", "AVVISA", r"font-weight:\s*(800|900)\b",
     "peso 800 o 900: Apple usa 400 e 600, il 700 solo per i titoli grandi."),
    ("FONT-WEB", "AVVISA", r"fonts\.googleapis|font-family:[^;]*\bInter\b",
     "font caricato: su Mac e iPhone il font di sistema è già SF. Inter fa scattare anche controlla-slop."),
    ("PRESSIONE", "AVVISA", r":active[^{]*\{[^}]*scale\(",
     "il bottone si rimpicciolisce alla pressione: Apple cambia il colore, non la scala."),
    ("EMOJI", "AVVISA", "[\U0001F300-\U0001FAFF☀-➿]",
     "emoji nel codice: se fa da icona va sostituita con un'icona del set."),
]


def file_web(cartella):
    for p in sorted(Path(cartella).rglob("*")):
        if p.is_file() and p.suffix in EST and not SALTA & set(p.parts):
            yield p


def controlla(cartella):
    rilievi = []  # (livello, codice, posizione, messaggio)
    testi = {p: p.read_text(errors="ignore") for p in file_web(cartella)}
    tutto = "\n".join(testi.values())

    for p, t in testi.items():
        righe = t.splitlines()
        for n, riga in enumerate(righe, 1):
            for codice, livello, rx, msg in RIGHE:
                if re.search(rx, riga, re.I if codice != "SF-SIMBOLI" else 0):
                    rilievi.append((livello, codice, f"{p}:{n}", msg))
            for m in re.finditer(r"cubic-bezier\(([^)]*)\)", riga):
                v = [float(x) for x in re.findall(r"-?\d*\.?\d+", m.group(1))]
                if len(v) == 4 and not (0 <= v[1] <= 1 and 0 <= v[3] <= 1):
                    rilievi.append(("AVVISA", "RIMBALZO", f"{p}:{n}",
                                    "curva che rimbalza: la molla predefinita di Apple non rimbalza."))

        if re.search(r"outline:\s*(none|0)\b", t) and ":focus-visible" not in t:
            rilievi.append(("BLOCCA", "FOCUS", str(p),
                            "outline tolto senza un :focus-visible: chi usa la tastiera non vede dove si trova."))
        if re.search(r"(?<!-webkit-)backdrop-filter:\s*(?!none)", t) and "-webkit-backdrop-filter" not in t:
            rilievi.append(("AVVISA", "VETRO-PREFISSO", str(p),
                            "backdrop-filter senza -webkit-backdrop-filter: Safari prima della 18 non lo vede."))
        selettori = [s.strip() for s in re.findall(r"([^{}]+)\{[^{}]*(?<!-webkit-)backdrop-filter:\s*(?!none)", t)]
        for s in selettori:
            if re.search(r"card|tile|row|item|section|\bli\b|\btd\b|cell", s, re.I):
                rilievi.append(("AVVISA", "VETRO-CONTENUTO", f"{p} «{s[-60:]}»",
                                "vetro su un elemento del contenuto: va solo su barre, menu, popover e sheet."))
        if len(set(selettori)) > 4:
            rilievi.append(("AVVISA", "VETRO-TROPPO", str(p),
                            f"{len(set(selettori))} selettori con il vetro: per vista ne bastano due o tre."))
        if p.name not in TOKEN:
            fuori = [h for riga in t.splitlines() if not riga.strip().startswith("--")
                     for h in re.findall(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b", riga)]
            if len(fuori) >= 5:
                rilievi.append(("AVVISA", "COLORI", str(p),
                                f"{len(fuori)} colori scritti a mano: si usano i token."))
        raggi = {r.strip() for r in re.findall(r"border-radius:\s*([^;}]+)", t)
                 if not re.search(r"var\(|^0$|50%|9999px|980px|inherit", r.strip())}
        if len(raggi) > 8:
            rilievi.append(("AVVISA", "RAGGI", str(p),
                            f"{len(raggi)} raggi diversi: si usa la scala dei token e la regola concentrica."))

    if re.search(r"@keyframes|transition:|animation:", tutto) and "prefers-reduced-motion" not in tutto:
        rilievi.append(("BLOCCA", "MOVIMENTO", str(cartella),
                        "animazioni senza prefers-reduced-motion: con Riduci movimento devono diventare dissolvenze."))
    if re.search(r"(?<!-webkit-)backdrop-filter:\s*(?!none)", tutto) and not re.search(
            r"@supports[^{]*backdrop-filter|prefers-reduced-transparency", tutto):
        rilievi.append(("AVVISA", "VETRO-RIPIEGO", str(cartella),
                        "vetro senza ripiego: servono @supports e prefers-reduced-transparency con uno sfondo pieno."))
    return rilievi


def stampa(rilievi):
    for livello, codice, dove, msg in sorted(rilievi):
        print(f"{livello:6}  {codice:15}  {dove}\n        {msg}")
    blocchi = sum(r[0] == "BLOCCA" for r in rilievi)
    print(f"\n{blocchi} da correggere, {len(rilievi) - blocchi} da guardare.")
    return blocchi


def prova():
    sbagliato = """
<meta name="viewport" content="width=device-width, user-scalable=no">
<style>
@font-face { font-family: "SF Pro Display"; src: url(fonts/SF-Pro-Display.woff2); }
.card { backdrop-filter: blur(30px); transition: all .3s cubic-bezier(.68,-.55,.265,1.55); }
.btn:focus { outline: none; }
.btn:active { transform: scale(.95); }
h3 { text-transform: uppercase; font-weight: 800; }
@media (prefers-contrast: high) { .card { background: #fff; } }
</style>
<button>\U00100184 Salva</button> <p>Fatto 🎉</p>
"""
    attesi = {"SF-FONT", "SF-SIMBOLI", "CONTRASTO", "ZOOM", "TRANS-ALL", "MAIUSCOLO", "PESO",
              "PRESSIONE", "EMOJI", "RIMBALZO", "FOCUS", "VETRO-PREFISSO", "VETRO-CONTENUTO",
              "MOVIMENTO", "VETRO-RIPIEGO"}
    with tempfile.TemporaryDirectory() as d:
        Path(d, "brutto.html").write_text(sbagliato)
        trovati = {r[1] for r in controlla(d)}
    assert attesi <= trovati, f"non trovati: {attesi - trovati}"
    skill = controlla(Path(__file__).parent)
    assert not [r for r in skill if r[0] == "BLOCCA"], f"la skill non passa il suo controllo: {skill}"
    print(f"prova superata: {len(attesi)} errori trovati nell'esempio sbagliato, la skill passa "
          f"({len(skill)} avvisi da guardare).")


if __name__ == "__main__":
    if sys.argv[1:] == ["--prova"]:
        prova()
    elif len(sys.argv) == 2 and Path(sys.argv[1]).is_dir():
        sys.exit(1 if stampa(controlla(sys.argv[1])) else 0)
    else:
        print(__doc__)
        sys.exit(2)
