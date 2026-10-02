#!/usr/bin/env python3
"""Genera i caroselli Instagram di DenkiCode: 1080x1350, un HTML per slide.

Ogni carosello ha la sua cartella, caroselli/<nome>/. Senza argomenti rifa'
l'ultimo; con il nome rifa' quello: `genera-carosello.py 2026-10-08-ore-whatsapp`.

Il rendering in PNG/JPEG lo fa rendi-carosello.sh con Brave headless.
Stesso sistema grafico delle storie (genera-storie.py): il CSS e' copiato e
non importato, perche' quel file cambia per conto suo. Se cambia il marchio
delle storie, si ricopia qui a mano.

I testi vengono dalle note del vault, parola per parola: le bozze del 3/10
(02-Sales/processo/bozze-social-2026-10-03.md) e le didascalie del 30/09
(02-Sales/processo/didascalie-instagram.md). Restano source: claude finche'
Patrick non li rilegge prima di pubblicare.
"""
import pathlib
import re
import sys

QUI = pathlib.Path(__file__).parent
FUORI = QUI / "caroselli"

# ---------------------------------------------------------------- i segni

# I pallini delle bozze (rosso, verde, saetta) diventano disegni: le emoji di
# sistema nel render escono come le fa il Mac, non come le vogliamo noi.
SEGNI = {
    "rosso": '<svg viewBox="0 0 24 24" class="segno"><circle cx="12" cy="12" r="9" fill="#f0475a"/></svg>',
    "verde": '<svg viewBox="0 0 24 24" class="segno"><circle cx="12" cy="12" r="9" fill="#34c77b"/></svg>',
    "lampo": '<svg viewBox="0 0 24 24" class="segno"><path d="M14 1 L4 14 H11 L9 23 L20 9 H13 Z" fill="url(#g)"/></svg>',
}

# ---------------------------------------------------------------- la grafica
# carosello 2026-10-08-ore-whatsapp

def vocale(x, y, w, forte=False, durata="0:42"):
    """Una nuvoletta vocale: tasto play, onda, durata."""
    fondo = 'fill="url(#g)"' if forte else 'class="debole"'
    onda_cls = 'fill="#0a0a0d" opacity=".55"' if forte else 'class="riga"'
    play = 'fill="#0a0a0d"' if forte else 'class="riga"'
    onda = "".join(
        f'<rect x="{x + 72 + i*11}" y="{y + 34 - h/2}" width="5" height="{h}" rx="2.5" {onda_cls}/>'
        for i, h in enumerate([10, 22, 34, 18, 28, 12, 30, 20, 8, 24, 16, 30, 14, 22, 10, 18])
        if x + 72 + i*11 < x + w - 80)
    return (f'<rect x="{x}" y="{y}" width="{w}" height="68" rx="34" {fondo}/>'
            f'<path d="M{x+30} {y+22} L{x+52} {y+34} L{x+30} {y+46} Z" {play}/>'
            f'{onda}<text x="{x+w-24}" y="{y+43}" class="durata{" scura" if forte else ""}" '
            f'text-anchor="end">{durata}</text>')

def telefono_vocali():
    """Copertina: il telefono del gruppo, una fila di vocali che non finisce."""
    fila = "".join(vocale(118, 150 + i*82, 250, durata=d)
                   for i, d in enumerate(["0:42", "1:15", "0:38", "2:04"]))
    return f"""
<svg viewBox="0 0 880 470" class="art">
  <g transform="rotate(-5 240 260)">
    <rect x="90" y="20" width="306" height="500" rx="40" class="tratto"/>
    <rect x="210" y="40" width="66" height="8" rx="4" class="riga-tenue"/>
    <circle cx="136" cy="96" r="20" fill="url(#g)" opacity=".5"/>
    <rect x="168" y="84" width="150" height="11" rx="5.5" class="riga"/>
    <rect x="168" y="104" width="90" height="8" rx="4" class="riga-tenue"/>
    {fila}
  </g>
  <text x="500" y="70" class="micro">gruppo squadre</text>
  {vocale(500, 100, 360, forte=True, durata="1:48")}
  {vocale(500, 190, 300, durata="0:56")}
  {vocale(500, 280, 330, durata="3:12")}
  <text x="500" y="420" class="micro">venerdì, da ricopiare</text>
</svg>"""

def chat_gruppo():
    """Slide 2: le tre risposte del gruppo, una col vocale."""
    return f"""
<svg viewBox="0 0 880 340" class="art">
  <text x="0" y="24" class="micro">capocantiere · 18:42</text>
  {vocale(0, 44, 420, forte=True, durata="1:48")}
  <text x="0" y="158" class="micro">squadra 2 · 19:05</text>
  <rect x="0" y="176" width="390" height="68" rx="34" class="debole"/>
  <text x="34" y="221" class="voce">io 8, Marco 7 e mezza</text>
  <text x="0" y="290" class="micro">squadra 3 · lunedì 8:10</text>
  <rect x="0" y="306" width="150" height="34" rx="17" class="debole" opacity=".7"/>
  <circle cx="44" cy="323" r="5" class="riga-tenue"/>
  <circle cx="74" cy="323" r="5" class="riga-tenue"/>
  <circle cx="104" cy="323" r="5" class="riga-tenue"/>
  <rect x="520" y="44" width="360" height="296" rx="18" class="tratto-tenue"/>
  <text x="548" y="88" class="micro">excel</text>
  <g class="griglia">{"".join(
      f'<rect x="{548 + c*80}" y="{110 + r*54}" width="70" height="42" rx="6"/>'
      for r in range(4) for c in range(4))}</g>
  <path d="M432 78 C 476 78, 470 150, 512 150" fill="none" stroke="url(#g)"
    stroke-width="3" stroke-dasharray="8 8"/>
</svg>"""

def foglio_ore():
    """Slide 3: il foglio a quadretti, un orario cancellato e riscritto."""
    giorni = ["lun", "mar", "mer", "gio", "ven"]
    ore = [["8", "8", "", "8", "6"], ["8", "8", "8", "8", "8"],
           ["7", "8", "8", "", "8"]]
    celle = ""
    for r, riga in enumerate(ore):
        for c, v in enumerate(riga):
            x, y = 200 + c * 136, 74 + r * 84
            celle += f'<rect x="{x}" y="{y}" width="124" height="72" rx="8"/>'
            if v:
                celle += f'<text x="{x+62}" y="{y+47}" class="mono" text-anchor="middle">{v}</text>'
    intestazione = "".join(
        f'<text x="{262 + c*136}" y="52" class="micro" text-anchor="middle">{g}</text>'
        for c, g in enumerate(giorni))
    nomi = "".join(
        f'<rect x="0" y="{102 + r*84}" width="{w}" height="14" rx="7" class="riga-tenue"/>'
        for r, w in enumerate([150, 120, 170]))
    return f"""
<svg viewBox="0 0 880 360" class="art">
  {intestazione}{nomi}
  <g class="griglia-ore">{celle}</g>
  <text x="508" y="121" class="mono" text-anchor="middle" opacity=".6">8</text>
  <line x1="492" y1="118" x2="526" y2="100" stroke="url(#g)" stroke-width="4" stroke-linecap="round"/>
  <text x="560" y="124" class="scritto" text-anchor="middle">7,5</text>
  <rect x="472" y="74" width="124" height="72" rx="8" fill="none" stroke="url(#g)" stroke-width="3"/>
  <rect x="608" y="242" width="124" height="72" rx="8" fill="none" stroke="url(#g)"
    stroke-width="3" stroke-dasharray="8 7"/>
  <text x="200" y="352" class="micro">ricopiato a memoria</text>
</svg>"""

def menu_lungo():
    """Slide 4: un menu che non finisce e scende fuori dallo schermo."""
    voci = ""
    for i, w in enumerate([200, 150, 220, 180, 130, 210, 165, 195, 140, 220, 175, 155, 190]):
        y = 90 + i * 46
        voci += (f'<rect x="270" y="{y}" width="18" height="18" rx="4" class="riga-tenue"/>'
                 f'<rect x="306" y="{y+4}" width="{w}" height="10" rx="5" class="riga"/>'
                 f'<path d="M{556} {y+3} l7 6 l-7 6" fill="none" stroke="#3d3d46" stroke-width="2.5"/>')
    return f"""
<svg viewBox="0 0 880 470" class="art">
  <defs>
    <linearGradient id="sfuma" x1="0" y1="0" x2="0" y2="1">
      <stop offset=".62" stop-color="#fff"/><stop offset="1" stop-color="#000"/>
    </linearGradient>
    <mask id="giu"><rect x="0" y="0" width="880" height="470" fill="url(#sfuma)"/></mask>
  </defs>
  <rect x="240" y="10" width="360" height="300" rx="26" class="tratto"/>
  <rect x="270" y="38" width="120" height="12" rx="6" class="riga"/>
  <line x1="240" y1="68" x2="600" y2="68" class="tratto-tenue"/>
  <g mask="url(#giu)">{voci}</g>
  <rect x="650" y="150" width="230" height="64" rx="12" fill="none" stroke="url(#g)"
    stroke-width="3" stroke-dasharray="8 7"/>
  <text x="765" y="190" class="micro" text-anchor="middle">non c’è</text>
  <text x="650" y="252" class="micro">chiudi dal</text>
  <text x="650" y="284" class="micro">telefono</text>
</svg>"""

def schermata_nostra():
    """Slide 5: la schermata disegnata da zero, niente di OperO."""
    righe = ""
    for i, (w, ore) in enumerate([(120, "8"), (100, "7,5"), (140, "8")]):
        y = 150 + i * 56
        righe += (f'<rect x="560" y="{y}" width="{w}" height="11" rx="5.5" class="riga"/>'
                  f'<text x="852" y="{y+12}" class="mono-p" text-anchor="end">{ore}</text>'
                  f'<line x1="560" y1="{y+30}" x2="852" y2="{y+30}" class="tratto-tenue"/>')
    return f"""
<svg viewBox="0 0 880 450" class="art">
  <rect x="40" y="0" width="290" height="450" rx="38" class="tratto"/>
  <rect x="152" y="18" width="66" height="8" rx="4" class="riga-tenue"/>
  <text x="70" y="78" class="micro">cantiere</text>
  <rect x="70" y="92" width="230" height="64" rx="12" class="debole"/>
  <text x="92" y="134" class="voce">Cantiere 1</text>
  <text x="70" y="200" class="micro">ora di fine</text>
  <rect x="70" y="214" width="230" height="64" rx="12" class="debole"/>
  <text x="92" y="256" class="voce">17:30</text>
  <rect x="70" y="320" width="230" height="64" rx="32" fill="url(#g)"/>
  <text x="185" y="360" class="bottone" text-anchor="middle">Chiudi il lavoro</text>
  <path d="M350 250 C 420 250, 440 190, 520 190" fill="none" stroke="url(#g)"
    stroke-width="3" stroke-dasharray="8 8"/>
  <text x="540" y="40" class="micro">in ufficio</text>
  <rect x="540" y="62" width="330" height="270" rx="14" class="tratto-tenue"/>
  <text x="560" y="114" class="micro-p">Cantiere 1</text>
  {righe}
</svg>"""

# carosello 2026-10-06-telefono-in-una-mano

def telefono_in_mano():
    """Il telefono tenuto con una mano: l'arco dove arriva il pollice."""
    return """
<svg viewBox="0 0 880 470" class="art">
  <g transform="rotate(-6 440 240)">
    <rect x="320" y="10" width="250" height="450" rx="38" class="tratto"/>
    <rect x="412" y="28" width="66" height="8" rx="4" class="riga-tenue"/>
    <rect x="346" y="60" width="198" height="120" rx="12" fill="url(#g)" opacity=".3"/>
    <rect x="346" y="204" width="150" height="12" rx="6" class="riga"/>
    <rect x="346" y="232" width="198" height="9" rx="4.5" class="riga-tenue"/>
    <rect x="346" y="252" width="170" height="9" rx="4.5" class="riga-tenue"/>
    <rect x="346" y="296" width="130" height="44" rx="22" fill="url(#g)"/>
    <path d="M590 470 A 230 230 0 0 0 360 260" fill="none" stroke="url(#g)"
      stroke-width="3" stroke-dasharray="8 8"/>
  </g>
  <text x="640" y="300" class="micro">dove arriva</text>
  <text x="640" y="332" class="micro">il pollice</text>
</svg>"""

def vetrina():
    """In fila o davanti alla vetrina: il negozio e il telefono che dice se e' aperto."""
    righe = "".join(
        f'<rect x="{x}" y="0" width="56" height="64" {"fill=&quot;url(#g)&quot; opacity=&quot;.35&quot;" if i % 2 == 0 else "class=&quot;debole&quot;"}/>'
        for i, x in enumerate(range(0, 560, 56))).replace("&quot;", '"')
    return f"""
<svg viewBox="0 0 880 440" class="art">
  {righe}
  <rect x="0" y="64" width="560" height="376" class="tratto-tenue"/>
  <rect x="34" y="110" width="300" height="250" rx="6" class="tratto-tenue"/>
  <rect x="380" y="110" width="146" height="330" rx="6" class="tratto-tenue"/>
  <rect x="404" y="160" width="98" height="46" rx="8" class="debole"/>
  <text x="453" y="190" class="micro-p" text-anchor="middle">chiuso?</text>
  <circle cx="500" cy="290" r="7" class="riga-tenue"/>
  <rect x="640" y="70" width="210" height="370" rx="34" class="tratto"/>
  <rect x="712" y="88" width="66" height="8" rx="4" class="riga-tenue"/>
  <text x="664" y="150" class="micro">orari</text>
  <circle cx="676" cy="190" r="9" fill="#34c77b"/>
  <text x="696" y="199" class="voce-p">aperto</text>
  <rect x="664" y="230" width="160" height="9" rx="4.5" class="riga-tenue"/>
  <rect x="664" y="252" width="130" height="9" rx="4.5" class="riga-tenue"/>
  <rect x="664" y="274" width="150" height="9" rx="4.5" class="riga-tenue"/>
  <rect x="664" y="340" width="160" height="44" rx="22" fill="url(#g)"/>
</svg>"""

def computer_spento():
    """Dal computer quasi nessuno: lo schermo grande resta al buio."""
    return """
<svg viewBox="0 0 880 420" class="art">
  <g opacity=".45">
    <rect x="60" y="20" width="560" height="340" rx="16" class="tratto-tenue"/>
    <rect x="290" y="360" width="100" height="40" class="tratto-tenue"/>
    <rect x="220" y="400" width="240" height="10" rx="5" class="tratto-tenue"/>
    <rect x="100" y="64" width="260" height="16" rx="8" class="riga-tenue"/>
    <rect x="100" y="104" width="460" height="10" rx="5" class="riga-tenue"/>
    <rect x="100" y="128" width="400" height="10" rx="5" class="riga-tenue"/>
  </g>
  <g transform="rotate(-6 760 280)">
    <rect x="690" y="150" width="150" height="260" rx="26" class="tratto"/>
    <rect x="708" y="190" width="114" height="66" rx="8" fill="url(#g)" opacity=".35"/>
    <rect x="708" y="276" width="90" height="9" rx="4.5" class="riga"/>
    <rect x="708" y="296" width="114" height="7" rx="3.5" class="riga-tenue"/>
    <rect x="708" y="340" width="80" height="30" rx="15" fill="url(#g)"/>
  </g>
</svg>"""

def pizzico():
    """Il sito da ingrandire con le dita: testo minuscolo e due polpastrelli."""
    minuscolo = "".join(
        f'<rect x="316" y="{70 + i*16}" width="{w * 4 // 5}" height="5" rx="2.5" class="riga-tenue"/>'
        for i, w in enumerate([300, 280, 310, 260, 300, 240, 290, 270, 305, 250, 280, 230,
                               300, 270, 290, 260]))
    return f"""
<svg viewBox="0 0 880 440" class="art">
  <rect x="290" y="10" width="290" height="420" rx="40" class="tratto"/>
  <rect x="402" y="26" width="66" height="8" rx="4" class="riga-tenue"/>
  <rect x="316" y="44" width="110" height="8" rx="4" class="riga"/>
  {minuscolo}
  <rect x="316" y="340" width="70" height="16" rx="8" class="riga-tenue"/>
  <circle cx="390" cy="240" r="44" fill="url(#g)" opacity=".18"/>
  <circle cx="390" cy="240" r="24" fill="url(#g)"/>
  <circle cx="490" cy="170" r="44" fill="url(#g)" opacity=".18"/>
  <circle cx="490" cy="170" r="24" fill="url(#g)"/>
  <path d="M352 314 l-22 0 l0 -22 M374 292 l-22 0 l0 -22" fill="none" stroke="#e6e6ea"
    stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M528 96 l22 0 l0 22 M506 118 l22 0 l0 22" fill="none" stroke="#e6e6ea"
    stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

# ---------------------------------------------------------------- i contenuti

# Una voce per carosello. Ogni slide: segno (rosso, verde, lampo o niente),
# tag, titolo, corpo (le righe a capo restano a capo), grafica (None: solo
# testo, centrato). La prima slide e' la copertina: titolo piu' grande,
# perche' nel feed la si vede in miniatura. La seconda deve reggere da sola:
# Instagram ripropone il carosello partendo da li'.
CAROSELLI = {}

# Post A della linea gestionali, giovedi' 8/10 alle 13:30. Testi della bozza
# del 3/10, sezione «Post · Tipologia A»: la prima frase di ogni slide fa da
# titolo, il resto da corpo. In S6 «denkicode.com» non si ripete nel corpo:
# sta gia' in fondo a ogni slide.
CAROSELLI["2026-10-08-ore-whatsapp"] = [
    dict(grafica=telefono_vocali,
         titolo="Le ore delle squadre arrivano su WhatsApp.",
         corpo="Il venerdì qualcuno le ricopia a mano."),
    dict(segno="rosso", tag="Come va adesso", grafica=chat_gruppo,
         titolo="Il capocantiere manda un vocale a fine giornata.",
         corpo="Un altro scrive «io 8, Marco 7 e mezza».\n"
               "Un terzo se ne ricorda lunedì.\n"
               "In ufficio qualcuno apre il gruppo, scorre e riporta tutto su Excel."),
    dict(tag="Dove se ne va il margine", grafica=foglio_ore,
         titolo="Non nei grandi errori.",
         corpo="Nella mezz'ora segnata a memoria. Nel cantiere scritto col nome "
               "sbagliato. Nel conto al cliente con le ore di un'altra settimana.\n"
               "E nel pomeriggio di chi ricopia."),
    dict(segno="rosso", tag="Il gestionale a pacchetto", grafica=menu_lungo,
         titolo="Cento voci di menu, e quella che ti serve non c'è:",
         corpo="la squadra che chiude il lavoro dal telefono, prima di risalire "
               "sul furgone.\nCosì si torna al gruppo WhatsApp. E il pacchetto "
               "lo paghi lo stesso, ogni mese."),
    dict(segno="verde", tag="Come lo facciamo noi", grafica=schermata_nostra,
         titolo="Una schermata sola, sul telefono di chi lavora: cantiere, ora di fine, chiudi.",
         corpo="In ufficio le ore arrivano già divise per persona e per cantiere.\n"
               "Il resto lo scriviamo guardando come lavorate voi, non come lavora "
               "un'azienda media."),
    dict(segno="lampo", grafica=None,
         titolo="Scrivici *SARTO* in DM",
         corpo="Veniamo a vedere da dove partono le vostre ore e ti diciamo cosa "
               "scriveremmo.\nSiamo a Seveso."),
]

# Il carosello di martedi' 6/10 del piano, estetista: le cinque righe di
# didascalie-instagram.md, una per slide, senza corpo. L'etichetta della
# copertina e' quella della storia del 16/09 da cui il carosello nasce.
CAROSELLI["2026-10-06-telefono-in-una-mano"] = [
    dict(tag="Telefono", grafica=telefono_in_mano,
         titolo="Il tuo sito lo aprono col telefono in una mano."),
    dict(grafica=vetrina,
         titolo="In fila alla cassa, o davanti alla vetrina per vedere se sei aperta."),
    dict(grafica=computer_spento, titolo="Dal computer quasi nessuno."),
    dict(grafica=pizzico,
         titolo="Un sito provato solo sul monitor grande, sul telefono diventa "
                "una cosa da ingrandire con le dita."),
    dict(segno="lampo", grafica=None,
         titolo="Scrivici *BOZZA* in DM.",
         corpo="La bozza del tuo sito te la facciamo vedere prima, gratis."),
]

# ---------------------------------------------------------------- il modello

# Il CSS e' quello di PAGINA in genera-storie.py, portato da 1920 a 1350 di
# altezza: margini 88 px di lato, il testo si ferma a 1200, negli ultimi
# 120 px c'e' solo denkicode.com.
PAGINA = """<!doctype html>
<meta charset="utf-8">
<title>{titolo_pagina}</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:1080px; height:1350px; overflow:hidden; }}
  body {{
    background:#07070a;
    font-family:-apple-system,"SF Pro Display","Helvetica Neue",Helvetica,sans-serif;
    -webkit-font-smoothing:antialiased;
  }}
  .fondo {{
    position:absolute; inset:0;
    background:
      radial-gradient(820px 560px at 92% -6%, rgba(218,47,155,.20), transparent 68%),
      radial-gradient(760px 560px at -12% 104%, rgba(146,58,223,.18), transparent 70%);
  }}
  .trama {{
    position:absolute; inset:0; opacity:.30;
    background-image:
      linear-gradient(to right, rgba(255,255,255,.045) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255,255,255,.045) 1px, transparent 1px);
    background-size:90px 90px;
    mask-image:radial-gradient(700px 680px at 50% 40%, #000 20%, transparent 78%);
  }}
  .telaio {{
    position:absolute; left:0; right:0; top:76px; bottom:150px;
    padding:0 88px; display:flex; flex-direction:column;
  }}
  header {{ display:flex; align-items:center; gap:20px; }}
  header img {{ width:56px; height:56px; }}
  .marchio {{
    font-size:23px; font-weight:600; letter-spacing:.34em;
    color:#f3f3f5; text-transform:uppercase;
  }}
  .conta {{
    margin-left:auto; font-size:22px; font-weight:500; letter-spacing:.16em;
    color:#5c5c66; font-variant-numeric:tabular-nums;
  }}
  .scena {{ flex:1; min-height:0; display:flex; align-items:center; padding:34px 0 30px; }}
  .art {{ width:100%; height:100%; max-height:470px; display:block; }}
  .etichetta {{ display:flex; align-items:center; gap:16px; }}
  .segno {{ width:26px; height:26px; flex:none; }}
  .tag {{
    font-size:25px; font-weight:600; letter-spacing:.22em;
    text-transform:uppercase;
    background:linear-gradient(96deg,#b34ae6,#f0389f);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
  }}
  h1 {{
    margin-top:24px; font-size:{h1}px; line-height:1.03;
    letter-spacing:-.035em; font-weight:700; color:#fff;
    text-wrap:balance;
  }}
  .etichetta + h1 {{ margin-top:24px; }}
  p {{
    margin-top:28px; max-width:880px;
    font-size:{p}px; line-height:1.42; letter-spacing:-.008em;
    font-weight:400; color:#a6a6b2;
    text-wrap:pretty;
  }}
  footer {{
    position:absolute; left:88px; bottom:48px;
    display:flex; align-items:center; gap:30px;
  }}
  .barra {{
    height:5px; width:132px; border-radius:3px;
    background:linear-gradient(90deg,#923adf,#da2f9b);
  }}
  .sito {{ font-size:27px; font-weight:500; letter-spacing:.1em; color:#dededf; }}

  /* la slide di solo testo: centrata, il segno grande sopra */
  .solo .testo {{ flex:1; display:flex; flex-direction:column; justify-content:center; }}
  .solo .segno {{ width:64px; height:64px; }}
  .grad {{
    background:linear-gradient(96deg,#b34ae6,#f0389f);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
  }}

  /* tratti comuni ai disegni */
  .art text {{ font-family:-apple-system,"Helvetica Neue",sans-serif; }}
  .tratto {{ fill:none; stroke:#4a4a55; stroke-width:2.5; }}
  .tratto-tenue {{ fill:none; stroke:#2c2c34; stroke-width:2.5; }}
  .debole {{ fill:#15151b; }}
  .riga {{ fill:#84848f; }}
  .riga-tenue {{ fill:#3d3d46; }}
  .griglia rect, .griglia-ore rect {{
    fill:none; stroke:#26262e; stroke-width:2.5; stroke-dasharray:9 8;
  }}
  .griglia-ore rect {{ fill:#111116; stroke-dasharray:none; }}
  .mono {{
    font-size:30px; fill:#7c7c88;
    font-family:"SF Mono",Menlo,monospace;
  }}
  .mono-p {{ font-size:24px; fill:#7c7c88; font-family:"SF Mono",Menlo,monospace; }}
  .voce {{ font-size:32px; font-weight:500; fill:#e6e6ea; }}
  .voce-p {{ font-size:27px; font-weight:500; fill:#e6e6ea; }}
  .micro {{ font-size:23px; font-weight:500; letter-spacing:.14em; fill:#5e5e6a;
           text-transform:uppercase; }}
  .micro-p {{ font-size:20px; font-weight:600; letter-spacing:.12em; fill:#84848f;
             text-transform:uppercase; }}
  .durata {{ font-size:22px; font-weight:500; fill:#84848f; font-variant-numeric:tabular-nums; }}
  .durata.scura {{ fill:#0a0a0d; }}
  .bottone {{ font-size:26px; font-weight:700; fill:#0a0a0d; }}
  .scritto {{ font-size:34px; font-weight:600; font-style:italic; fill:url(#g); }}
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
<div class="telaio{classe}">
  <header>
    <img src="../../simbolo.svg" alt="">
    <span class="marchio">DenkiCode</span>
    <span class="conta">{n:02d} / {tot:02d}</span>
  </header>
  {scena}
  <div class="testo">{etichetta}<h1>{titolo}</h1>{corpo}</div>
</div>
<footer>
  <span class="barra"></span>
  <span class="sito">denkicode.com</span>
</footer>
"""

def tipografico(t):
    """L'apostrofo tipografico. I testi portano gia' gli accenti veri."""
    return t.replace("'", "’")

def misure(i, s):
    """Corpo dei caratteri: la copertina ha il titolo piu' grande, perche'
    nel feed si vede in miniatura. Il disegno prende lo spazio che resta.
    """
    titolo, corpo = s["titolo"], s.get("corpo", "")
    if s.get("grafica") is None:
        return dict(h1=118, p=40)
    if i == 1:
        return dict(h1=92 if len(titolo) <= 50 else 80, p=40)
    if not corpo:
        return dict(h1=74 if len(titolo) <= 72 else 66, p=34)
    return dict(h1=80 if len(titolo) <= 30 else (66 if len(titolo) <= 56 else 58), p=34)

def slide(i, tot, s):
    m = misure(i, s)
    etichetta = ""
    if s.get("tag") or s.get("segno"):
        tag = f'<span class="tag">{s["tag"]}</span>' if s.get("tag") else ""
        etichetta = f'<div class="etichetta">{SEGNI.get(s.get("segno"), "")}{tag}</div>'
    # *parola*: la parola da scrivere in DM, in gradiente
    titolo = re.sub(r"\*(.+?)\*", r'<span class="grad">\1</span>', tipografico(s["titolo"]))
    corpo = ""
    if s.get("corpo"):
        corpo = "<p>" + tipografico(s["corpo"]).replace("\n", "<br>") + "</p>"
    grafica = s.get("grafica")
    return PAGINA.format(
        titolo_pagina=tipografico(s["titolo"]).replace("*", ""), n=i, tot=tot,
        classe="" if grafica else " solo",
        scena=f'<div class="scena">{grafica()}</div>' if grafica else "",
        etichetta=etichetta, titolo=titolo, corpo=corpo, **m)

def main():
    nome = sys.argv[1] if len(sys.argv) > 1 else max(CAROSELLI)
    if nome not in CAROSELLI:
        sys.exit(f"carosello {nome} sconosciuto, ci sono: {', '.join(sorted(CAROSELLI))}")
    slides = CAROSELLI[nome]
    assert 2 <= len(slides) <= 10, "Instagram vuole da 2 a 10 slide"
    fuori = FUORI / nome
    fuori.mkdir(parents=True, exist_ok=True)
    for f in fuori.glob("slide-*.html"):
        f.unlink()
    print(f"carosello {nome}")
    for i, s in enumerate(slides, 1):
        (fuori / f"slide-{i:02d}.html").write_text(slide(i, len(slides), s), encoding="utf-8")
        print(f"slide-{i:02d}.html  {s['titolo'].replace('*', '')}")

if __name__ == "__main__":
    main()
