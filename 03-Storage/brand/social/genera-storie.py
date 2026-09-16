#!/usr/bin/env python3
"""Genera le storie Instagram di DenkiCode: 1080x1920, un HTML per storia.

Il rendering in PNG/JPEG lo fa rendi-storie.sh con Chrome headless.
I testi sono passati dalla skill voce-denkicode. Restano source: claude
finche' Patrick non li rilegge prima di pubblicare.
"""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
FUORI = QUI / "storie"

# ---------------------------------------------------------------- la grafica

def ricerca():
    return """
<svg viewBox="0 0 880 340" class="art">
  <rect x="0" y="18" width="620" height="92" rx="46" class="tratto"/>
  <circle cx="62" cy="64" r="17" class="tratto"/>
  <line x1="74" y1="76" x2="90" y2="92" class="tratto"/>
  <text x="112" y="76" class="mono">parrucchiere seveso</text>
  <rect x="0" y="152" width="620" height="60" rx="10" fill="url(#g)"/>
  <rect x="24" y="172" width="240" height="9" rx="4.5" fill="#0a0a0d" opacity=".78"/>
  <rect x="24" y="190" width="150" height="7" rx="3.5" fill="#0a0a0d" opacity=".45"/>
  <rect x="0" y="232" width="620" height="60" rx="10" class="debole"/>
  <rect x="24" y="252" width="205" height="9" rx="4.5" class="riga"/>
  <rect x="24" y="270" width="128" height="7" rx="3.5" class="riga-tenue"/>
  <rect x="700" y="18" width="164" height="274" rx="24" class="tratto-tenue"/>
  <circle cx="782" cy="104" r="30" class="tratto-tenue"/>
  <rect x="736" y="160" width="92" height="9" rx="4.5" class="riga-tenue"/>
  <rect x="746" y="184" width="72" height="7" rx="3.5" class="riga-tenue"/>
  <line x1="712" y1="258" x2="852" y2="258" class="tratto-tenue"/>
  <text x="700" y="330" class="micro">profilo</text>
  <text x="0" y="330" class="micro">ricerca</text>
</svg>"""

def dieci_secondi():
    return """
<svg viewBox="0 0 880 340" class="art">
  <circle cx="150" cy="160" r="112" class="binario"/>
  <circle cx="150" cy="160" r="112" class="arco" stroke="url(#g)"
    stroke-dasharray="703" stroke-dashoffset="211" transform="rotate(-90 150 160)"/>
  <text x="150" y="182" class="numero" text-anchor="middle">10</text>
  <text x="150" y="316" class="micro" text-anchor="middle">secondi</text>
  <rect x="340" y="62" width="500" height="80" rx="12" fill="url(#g)" opacity=".16"/>
  <rect x="340" y="62" width="6" height="80" fill="url(#g)"/>
  <text x="376" y="110" class="voce">L'indirizzo</text>
  <rect x="340" y="178" width="500" height="80" rx="12" fill="url(#g)" opacity=".16"/>
  <rect x="340" y="178" width="6" height="80" fill="url(#g)"/>
  <text x="376" y="226" class="voce">Il tasto per prenotare</text>
</svg>"""

def telefono():
    """Le etichette stanno in alto: il telefono ruotato scende oltre il viewBox
    e in basso gli finiva sopra."""
    return """
<svg viewBox="0 0 880 452" class="art">
  <text x="96" y="24" class="micro">telefono, una mano</text>
  <text x="470" y="24" class="micro">monitor, quasi mai</text>
  <g transform="rotate(-6 200 250)">
    <rect x="96" y="64" width="208" height="356" rx="34" class="tratto"/>
    <rect x="176" y="84" width="48" height="7" rx="3.5" class="riga-tenue"/>
    <rect x="118" y="112" width="164" height="94" rx="10" fill="url(#g)" opacity=".3"/>
    <rect x="118" y="226" width="126" height="11" rx="5.5" class="riga"/>
    <rect x="118" y="254" width="164" height="8" rx="4" class="riga-tenue"/>
    <rect x="118" y="272" width="140" height="8" rx="4" class="riga-tenue"/>
    <rect x="118" y="310" width="112" height="38" rx="19" fill="url(#g)"/>
    <rect x="118" y="370" width="164" height="8" rx="4" class="riga-tenue"/>
    <rect x="118" y="388" width="96" height="8" rx="4" class="riga-tenue"/>
  </g>
  <g opacity=".4">
    <rect x="470" y="86" width="390" height="242" rx="14" class="tratto-tenue"/>
    <rect x="618" y="328" width="94" height="40" class="tratto-tenue"/>
    <rect x="556" y="368" width="218" height="10" rx="5" class="tratto-tenue"/>
    <rect x="504" y="126" width="230" height="14" rx="7" class="riga-tenue"/>
    <rect x="504" y="158" width="322" height="9" rx="4.5" class="riga-tenue"/>
    <rect x="504" y="180" width="286" height="9" rx="4.5" class="riga-tenue"/>
    <rect x="504" y="236" width="140" height="36" rx="18" class="riga-tenue"/>
  </g>
</svg>"""

def scheda():
    return """
<svg viewBox="0 0 880 340" class="art">
  <rect x="0" y="10" width="560" height="310" rx="18" class="tratto"/>
  <rect x="0" y="10" width="560" height="10" rx="5" fill="url(#g)"/>
  <rect x="40" y="56" width="248" height="16" rx="8" class="riga"/>
  <g class="stelle">
    <text x="40" y="118" class="voce">★ ★ ★ ★ ★</text>
  </g>
  <line x1="40" y1="150" x2="520" y2="150" class="tratto-tenue"/>
  <text x="40" y="192" class="voce-tenue">Orari</text>
  <text x="300" y="192" class="voce">08:30 - 19:00</text>
  <text x="40" y="240" class="voce-tenue">Indirizzo</text>
  <text x="300" y="240" class="voce">Seveso, MB</text>
  <text x="40" y="288" class="voce-tenue">Foto</text>
  <text x="300" y="288" class="voce">12</text>
  <text x="640" y="150" class="numero-grande">0 €</text>
  <text x="640" y="196" class="micro">un pomeriggio</text>
</svg>"""

def modello():
    return """
<svg viewBox="0 0 880 386" class="art">
  <g class="griglia">
    <rect x="0" y="20" width="196" height="132" rx="10"/>
    <rect x="216" y="20" width="196" height="132" rx="10"/>
    <rect x="432" y="20" width="196" height="132" rx="10"/>
    <rect x="0" y="176" width="196" height="132" rx="10"/>
    <rect x="216" y="176" width="196" height="132" rx="10"/>
  </g>
  <rect x="446" y="186" width="238" height="164" rx="12" fill="url(#g)" opacity=".2"/>
  <rect x="446" y="186" width="238" height="164" rx="12" stroke="url(#g)" fill="none" stroke-width="3"/>
  <text x="466" y="244" class="voce">il tuo</text>
  <text x="466" y="288" class="voce">mestiere</text>
  <text x="744" y="76" class="micro">blog</text>
  <line x1="744" y1="96" x2="836" y2="96" class="tratto-tenue"/>
  <text x="744" y="140" class="micro">team</text>
  <line x1="744" y1="160" x2="836" y2="160" class="tratto-tenue"/>
  <text x="744" y="204" class="micro">eventi</text>
  <line x1="744" y1="224" x2="836" y2="224" class="tratto-tenue"/>
</svg>"""

def notte():
    return """
<svg viewBox="0 0 880 380" class="art">
  <g class="griglia-ore">"""+ "".join(
    f'<rect x="{c*108}" y="{r*62+54}" width="92" height="46" rx="8"/>'
    for r in range(4) for c in range(8)
  ) + """</g>
  <rect x="540" y="240" width="92" height="46" rx="8" fill="url(#g)"/>
  <text x="586" y="270" class="ora" text-anchor="middle">23:40</text>
  <line x1="586" y1="292" x2="586" y2="330" stroke="url(#g)" stroke-width="2"/>
  <text x="586" y="362" class="micro" text-anchor="middle">prenotazione ricevuta</text>
  <text x="0" y="30" class="micro">negozio chiuso</text>
</svg>"""

def foto():
    return """
<svg viewBox="0 0 880 340" class="art">
  <rect x="0" y="20" width="400" height="290" rx="14" fill="#141418"/>
  <rect x="0" y="20" width="400" height="290" rx="14" class="tratto-tenue"/>
  <circle cx="200" cy="150" r="52" fill="#1e1e24"/>
  <rect x="120" y="236" width="160" height="10" rx="5" fill="#1e1e24"/>
  <text x="0" y="336" class="micro">la sera, al chiuso</text>
  <rect x="470" y="20" width="400" height="290" rx="14" fill="url(#g)" opacity=".2"/>
  <rect x="470" y="20" width="400" height="290" rx="14" stroke="url(#g)" fill="none" stroke-width="3"/>
  <path d="M470 310 L700 20 L800 20 L570 310 Z" fill="#fff" opacity=".10"/>
  <circle cx="670" cy="150" r="52" fill="#fff" opacity=".82"/>
  <rect x="590" y="236" width="160" height="10" rx="5" fill="#fff" opacity=".5"/>
  <text x="470" y="336" class="micro">di giorno, luce naturale</text>
</svg>"""

def bozza():
    return """
<svg viewBox="0 0 880 340" class="art">
  <rect x="0" y="14" width="880" height="306" rx="18" class="tratto"/>
  <line x1="0" y1="82" x2="880" y2="82" class="tratto"/>
  <circle cx="36" cy="48" r="8" class="riga-tenue-p"/>
  <circle cx="64" cy="48" r="8" class="riga-tenue-p"/>
  <circle cx="92" cy="48" r="8" class="riga-tenue-p"/>
  <rect x="128" y="34" width="420" height="28" rx="14" class="debole"/>
  <rect x="148" y="44" width="180" height="8" rx="4" class="riga-tenue"/>
  <rect x="44" y="124" width="360" height="26" rx="6" class="riga"/>
  <rect x="44" y="166" width="280" height="12" rx="6" class="riga-tenue"/>
  <rect x="44" y="192" width="320" height="12" rx="6" class="riga-tenue"/>
  <rect x="44" y="236" width="180" height="44" rx="22" fill="url(#g)"/>
  <rect x="470" y="124" width="366" height="156" rx="12" fill="url(#g)" opacity=".22"/>
  <line x1="470" y1="124" x2="836" y2="280" class="tratto-tenue"/>
</svg>"""

# ---------------------------------------------------------------- i contenuti

STORIE = [
    dict(tag="Farsi trovare", grafica=ricerca,
         titolo="Il link in bio non ti fa trovare su Google",
         corpo="Su Instagram ti trova chi sa gia' come ti chiami. Su Google ti "
               "trova chi cerca il tuo mestiere e il tuo comune, e ancora non "
               "ti conosce. Il secondo pubblico e' quello che ti manca."),
    dict(tag="I primi secondi", grafica=dieci_secondi,
         titolo="Dove sei, e come si prenota",
         corpo="Sono le prime due cose che un cliente cerca quando apre il tuo "
               "sito. Se deve cercarle, chiude. Vanno in alto e grandi, non in "
               "fondo alla pagina contatti."),
    dict(tag="Telefono", grafica=telefono,
         titolo="Il tuo sito lo guardano in piedi",
         corpo="Quasi nessuno apre il sito di un negozio dal computer. Lo apre "
               "dal telefono, con una mano, mentre fa altro. Un sito disegnato "
               "sul monitor e provato solo li', in quella situazione, non tiene."),
    dict(tag="Costo zero", grafica=scheda,
         titolo="La scheda Google non si paga",
         corpo="Orari, indirizzo, foto e recensioni in un posto solo. Si "
               "compila in un pomeriggio. Chi cerca il tuo mestiere nella tua "
               "zona ti trova li' prima che sul sito."),
    dict(tag="Modelli pronti", grafica=modello,
         titolo="Un modello ti da' le sezioni di un altro",
         corpo="I temi pronti nascono per un'attivita' generica. Ti ritrovi con "
               "lo spazio per un blog che non scriverai e senza quello per la "
               "cosa che vendi davvero. Il sito segue il mestiere, non il "
               "contrario."),
    dict(tag="Agenda", grafica=notte,
         titolo="Le prenotazioni arrivano quando sei chiuso",
         corpo="Chi decide alle undici di sera non telefona, e la mattina dopo "
               "se ne dimentica. Un'agenda dentro il sito raccoglie quella "
               "richiesta mentre il negozio e' chiuso."),
    dict(tag="Fotografie", grafica=foto,
         titolo="Un sito sembra vecchio per le foto",
         corpo="Il codice non si vede, le fotografie si'. Cinque scatti fatti "
               "di giorno, con la luce che entra dalla finestra, cambiano una "
               "pagina piu' di qualunque animazione."),
    dict(tag="Come lavoriamo", grafica=bozza,
         titolo="Il sito lo vedi prima di pagarlo",
         corpo="Guardiamo il tuo profilo e costruiamo una bozza vera del sito, "
               "poi te la mandiamo. Si apre dal telefono e si scorre come "
               "quello finito. Nessun costo e nessun impegno: se non ti "
               "convince, l'hai vista e basta."),
]

# gli accenti veri: il sorgente non porta le lettere accentate, e nemmeno
# l'apostrofo tipografico. Si sostituiscono qui, in quest'ordine.
ACCENTI = [
    (r"\bgia'", "gi\u00e0"), (r"\bpiu'", "pi\u00f9"), (r"\bli'", "l\u00ec"),
    (r"\bsi'", "s\u00ec"), (r"\bda'", "d\u00e0"), (r"\be'(?=[\s,.:;]|$)", "\u00e8"),
    (r"\battivita'", "attivit\u00e0"), (r"\bqualita'", "qualit\u00e0"),
    (r"\bperche'", "perch\u00e9"), (r"\bpero'", "per\u00f2"),
]

def accenta(t):
    """Prima gli accenti, poi l'apostrofo tipografico.

    L'ordine conta: girando prima l'apostrofo in pagina restano «li\u2019» e
    «piu\u2019», perche' i motivi qui sopra cercano l'apostrofo dritto.
    """
    for motivo, giusto in ACCENTI:
        t = re.sub(motivo, giusto, t)
    return t.replace("'", "\u2019")

# ---------------------------------------------------------------- il modello

PAGINA = """<!doctype html>
<meta charset="utf-8">
<title>{titolo}</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:1080px; height:1920px; overflow:hidden; }}
  body {{
    background:#07070a;
    font-family:-apple-system,"SF Pro Display","Helvetica Neue",Helvetica,sans-serif;
    -webkit-font-smoothing:antialiased;
  }}
  .fondo {{
    position:absolute; inset:0;
    background:
      radial-gradient(900px 620px at 92% -6%, rgba(218,47,155,.20), transparent 68%),
      radial-gradient(820px 640px at -12% 104%, rgba(146,58,223,.18), transparent 70%);
  }}
  .trama {{
    position:absolute; inset:0; opacity:.30;
    background-image:
      linear-gradient(to right, rgba(255,255,255,.045) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255,255,255,.045) 1px, transparent 1px);
    background-size:90px 90px;
    mask-image:radial-gradient(760px 900px at 50% 42%, #000 20%, transparent 78%);
  }}
  .telaio {{
    position:absolute; left:0; right:0; top:236px; bottom:236px;
    padding:0 96px; display:flex; flex-direction:column;
  }}
  header {{ display:flex; align-items:center; gap:22px; }}
  header img {{ width:62px; height:62px; }}
  .marchio {{
    font-size:25px; font-weight:600; letter-spacing:.34em;
    color:#f3f3f5; text-transform:uppercase;
  }}
  .conta {{
    margin-left:auto; font-size:24px; font-weight:500; letter-spacing:.16em;
    color:#5c5c66; font-variant-numeric:tabular-nums;
  }}
  .scena {{ flex:1; display:flex; align-items:center; padding:56px 0 24px; }}
  .art {{ width:100%; height:auto; max-height:470px; display:block; }}
  .tag {{
    font-size:26px; font-weight:600; letter-spacing:.22em;
    text-transform:uppercase;
    background:linear-gradient(96deg,#b34ae6,#f0389f);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
  }}
  h1 {{
    margin-top:30px; font-size:{corpo_h1}px; line-height:1.015;
    letter-spacing:-.035em; font-weight:700; color:#fff;
    text-wrap:balance;
  }}
  p {{
    margin-top:38px; max-width:800px;
    font-size:38px; line-height:1.46; letter-spacing:-.008em;
    font-weight:400; color:#a6a6b2;
  }}
  footer {{ margin-top:64px; display:flex; align-items:center; gap:30px; }}
  .barra {{
    height:5px; width:132px; border-radius:3px;
    background:linear-gradient(90deg,#923adf,#da2f9b);
  }}
  .sito {{ font-size:28px; font-weight:500; letter-spacing:.1em; color:#dededf; }}

  /* tratti comuni ai disegni */
  .art text {{ font-family:-apple-system,"Helvetica Neue",sans-serif; }}
  .tratto {{ fill:none; stroke:#4a4a55; stroke-width:2.5; }}
  .tratto-tenue {{ fill:none; stroke:#2c2c34; stroke-width:2.5; }}
  .binario {{ fill:none; stroke:#22222a; stroke-width:14; }}
  .arco {{ fill:none; stroke-width:14; stroke-linecap:round; }}
  .debole {{ fill:#15151b; }}
  .riga {{ fill:#84848f; }}
  .riga-tenue {{ fill:#3d3d46; }}
  .riga-tenue-p {{ fill:#2c2c34; }}
  .griglia rect, .griglia-ore rect {{
    fill:none; stroke:#26262e; stroke-width:2.5; stroke-dasharray:9 8;
  }}
  .griglia-ore rect {{ fill:#111116; stroke-dasharray:none; }}
  .mono {{
    font-size:30px; fill:#7c7c88;
    font-family:"SF Mono",Menlo,monospace;
  }}
  .voce {{ font-size:32px; font-weight:500; fill:#e6e6ea; }}
  .voce-tenue {{ font-size:32px; font-weight:400; fill:#6c6c78; }}
  .micro {{ font-size:23px; font-weight:500; letter-spacing:.14em; fill:#5e5e6a;
           text-transform:uppercase; }}
  .numero {{ font-size:86px; font-weight:700; fill:#fff; letter-spacing:-.04em; }}
  .numero-grande {{ font-size:96px; font-weight:700; fill:#fff; letter-spacing:-.045em; }}
  .ora {{ font-size:26px; font-weight:700; fill:#0a0a0d; }}
  .stelle text {{ fill:#f0389f; letter-spacing:.12em; }}
</style>
<div class="fondo"></div>
<div class="trama"></div>
<svg width="0" height="0" style="position:absolute">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#923adf"/>
      <stop offset="1" stop-color="#da2f9b"/>
    </linearGradient>
  </defs>
</svg>
<div class="telaio">
  <header>
    <img src="../simbolo.svg" alt="">
    <span class="marchio">DenkiCode</span>
    <span class="conta">{n:02d} / {tot:02d}</span>
  </header>
  <div class="scena">{grafica}</div>
  <div class="tag">{tag}</div>
  <h1>{titolo}</h1>
  <p>{corpo}</p>
  <footer>
    <span class="barra"></span>
    <span class="sito">denkicode.com</span>
  </footer>
</div>
"""

def main():
    FUORI.mkdir(exist_ok=True)
    tot = len(STORIE)
    for i, s in enumerate(STORIE, 1):
        titolo = accenta(s["titolo"])
        # i titoli lunghi scendono di corpo per restare su tre righe
        h1 = 86 if len(titolo) > 38 else 96
        html = PAGINA.format(
            n=i, tot=tot, tag=s["tag"], titolo=titolo,
            corpo=accenta(s["corpo"]), grafica=accenta(s["grafica"]()), corpo_h1=h1,
        )
        (FUORI / f"storia-{i:02d}.html").write_text(html, encoding="utf-8")
        print(f"storia-{i:02d}.html  {titolo}")

if __name__ == "__main__":
    main()
