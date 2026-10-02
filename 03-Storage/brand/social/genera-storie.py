#!/usr/bin/env python3
"""Genera le storie Instagram di DenkiCode: 1080x1920, un HTML per storia.

Ogni serie ha la sua cartella, storie/<chiave>/. La chiave comincia con la
data (`2026-09-16`, `2026-10-07-sarto-1`). Senza argomenti rifa' l'ultima
serie; con la chiave rifa' quella: `genera-storie.py 2026-09-16`.

Il rendering in PNG/JPEG lo fa rendi-storie.sh con Chrome headless.
I testi sono passati dalla skill voce-denkicode. Restano source: claude
finche' Patrick non li rilegge prima di pubblicare.
"""
import pathlib
import re
import sys

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
  <text x="96" y="24" class="micro">dal telefono</text>
  <text x="470" y="24" class="micro">dal computer</text>
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

# i disegni della serie del 25 settembre

def messaggi():
    return """
<svg viewBox="0 0 880 400" class="art">
  <text x="0" y="24" class="micro">messaggi</text>
  <rect x="0" y="52" width="300" height="68" rx="34" class="debole"/>
  <text x="34" y="97" class="voce">quanto costa?</text>
  <text x="322" y="96" class="micro">10:14</text>
  <rect x="0" y="136" width="254" height="68" rx="34" class="debole"/>
  <text x="34" y="181" class="voce">info prezzo</text>
  <text x="276" y="180" class="micro">13:52</text>
  <rect x="0" y="220" width="186" height="68" rx="34" class="debole"/>
  <text x="34" y="265" class="voce">prezzi?</text>
  <text x="208" y="264" class="micro">17:30</text>
  <rect x="452" y="304" width="428" height="92" rx="24" fill="url(#g)"/>
  <rect x="476" y="322" width="56" height="56" rx="12" fill="#0a0a0d" opacity=".22"/>
  <text x="556" y="346" class="link">Listino prezzi</text>
  <rect x="556" y="360" width="170" height="8" rx="4" fill="#0a0a0d" opacity=".4"/>
</svg>"""

def profilo():
    """In alto le foto tutte uguali, sotto i lavori diversi che nessuno vede."""
    quadri = []
    for r in range(3):
        for c in range(3):
            x, y = c * 108, 48 + r * 108
            if r < 2:
                quadri.append(
                    f'<rect x="{x}" y="{y}" width="100" height="100" rx="8" '
                    f'fill="url(#g)" opacity=".26"/>'
                    f'<circle cx="{x+50}" cy="{y+50}" r="18" fill="#fff" opacity=".55"/>')
            else:
                quadri.append(
                    f'<rect x="{x}" y="{y}" width="100" height="100" rx="8" '
                    f'class="tratto-tenue" opacity=".6"/>')
    diversi = ('<rect x="34" y="298" width="32" height="32" rx="4" class="riga-tenue"/>'
               '<path d="M142 330 L158 298 L174 330 Z" class="riga-tenue"/>'
               '<rect x="244" y="306" width="44" height="16" rx="8" class="riga-tenue"/>')
    righe = ""
    for i, (w, forte) in enumerate([(250, 0), (190, 0), (290, 0), (220, 1), (170, 0)]):
        y = 72 + i * 60
        colore = 'fill="url(#g)"' if forte else 'class="riga"'
        righe += (f'<circle cx="452" cy="{y}" r="7" {colore}/>'
                  f'<rect x="480" y="{y-7}" width="{w}" height="14" rx="7" {colore}/>'
                  f'<line x1="440" y1="{y+30}" x2="880" y2="{y+30}" class="tratto-tenue"/>')
    return f"""
<svg viewBox="0 0 880 380" class="art">
  <text x="0" y="24" class="micro">profilo</text>
  <text x="440" y="24" class="micro">sito</text>
  {''.join(quadri)}{diversi}
  {righe}
</svg>"""

def whatsapp():
    griglia = "".join(
        f'<rect x="{617 + c*60}" y="{140 + r*60}" width="54" height="54" rx="6" class="riga-tenue-p"/>'
        for r in range(4) for c in range(3))
    return f"""
<svg viewBox="0 0 880 452" class="art">
  <text x="0" y="24" class="micro">su whatsapp</text>
  <text x="600" y="24" class="micro">senza instagram</text>
  <rect x="0" y="64" width="470" height="208" rx="28" class="debole"/>
  <text x="32" y="116" class="voce">prova qui, ti trovi bene</text>
  <rect x="32" y="144" width="406" height="96" rx="14" class="tratto-tenue"/>
  <rect x="48" y="160" width="64" height="64" rx="10" fill="url(#g)" opacity=".35"/>
  <rect x="128" y="172" width="200" height="12" rx="6" class="riga"/>
  <rect x="128" y="198" width="150" height="9" rx="4.5" class="riga-tenue"/>
  <path d="M482 168 C 530 168, 546 232, 590 232" fill="none" stroke="url(#g)"
    stroke-width="3" stroke-dasharray="8 8"/>
  <rect x="600" y="52" width="208" height="372" rx="34" class="tratto"/>
  <circle cx="640" cy="100" r="18" class="riga-tenue"/>
  <rect x="670" y="94" width="90" height="10" rx="5" class="riga-tenue"/>
  <g opacity=".55">{griglia}</g>
  <rect x="612" y="236" width="184" height="176" rx="20" fill="#15151b" stroke="#2c2c34" stroke-width="2"/>
  <rect x="636" y="262" width="136" height="10" rx="5" class="riga"/>
  <rect x="646" y="284" width="116" height="8" rx="4" class="riga-tenue"/>
  <rect x="636" y="320" width="136" height="48" rx="24" fill="url(#g)"/>
  <text x="704" y="352" class="ora" text-anchor="middle">Accedi</text>
</svg>"""

def mappa():
    return """
<svg viewBox="0 0 880 360" class="art">
  <rect x="0" y="40" width="880" height="34" class="strada"/>
  <rect x="0" y="236" width="880" height="34" class="strada"/>
  <rect x="300" y="0" width="34" height="360" class="strada"/>
  <rect x="640" y="0" width="34" height="360" class="strada"/>
  <text x="60" y="110" class="micro">parcheggio</text>
  <rect x="60" y="126" width="120" height="84" rx="12" fill="none" stroke="url(#g)" stroke-width="3"/>
  <text x="120" y="186" class="lettera" text-anchor="middle">P</text>
  <path d="M180 168 H317 V253 H780 V218" class="percorso"/>
  <g transform="translate(780 150)">
    <path d="M0 64 C -14 42 -34 26 -34 0 A34 34 0 0 1 34 0 C 34 26 14 42 0 64 Z" fill="url(#g)"/>
    <circle cx="0" cy="0" r="12" fill="#0a0a0d"/>
  </g>
  <text x="780" y="104" class="micro" text-anchor="middle">ingresso</text>
  <text x="420" y="316" class="micro">a piedi</text>
</svg>"""

def complimento():
    return """
<svg viewBox="0 0 880 380" class="art">
  <text x="0" y="24" class="micro">messaggio</text>
  <text x="520" y="24" class="micro">sul sito</text>
  <rect x="0" y="48" width="440" height="250" rx="28" class="debole"/>
  <rect x="32" y="84" width="340" height="11" rx="5.5" class="riga"/>
  <rect x="32" y="114" width="370" height="9" rx="4.5" class="riga-tenue"/>
  <rect x="32" y="138" width="320" height="9" rx="4.5" class="riga-tenue"/>
  <rect x="32" y="162" width="360" height="9" rx="4.5" class="riga-tenue"/>
  <rect x="32" y="186" width="250" height="9" rx="4.5" class="riga-tenue"/>
  <rect x="32" y="222" width="300" height="9" rx="4.5" class="riga-tenue"/>
  <rect x="32" y="246" width="180" height="9" rx="4.5" class="riga-tenue"/>
  <circle cx="416" cy="298" r="30" fill="#1d1d24" stroke="#07070a" stroke-width="6"/>
  <path transform="translate(416 300) scale(1.3)" fill="url(#g)"
    d="M0 8 C -2 6 -12 0 -12 -6 C -12 -10 -9 -13 -5.5 -13 C -3 -13 -1 -11.5 0 -9.5
       C 1 -11.5 3 -13 5.5 -13 C 9 -13 12 -10 12 -6 C 12 0 2 6 0 8 Z"/>
  <text x="512" y="192" class="virgolette">“</text>
  <rect x="524" y="154" width="330" height="13" rx="6.5" class="riga"/>
  <rect x="524" y="184" width="290" height="13" rx="6.5" class="riga"/>
  <rect x="524" y="214" width="200" height="13" rx="6.5" class="riga"/>
  <rect x="524" y="257" width="40" height="4" rx="2" fill="url(#g)"/>
  <rect x="578" y="254" width="110" height="10" rx="5" class="riga-tenue"/>
</svg>"""

# i disegni delle serie di ottobre: linea siti (A, B) e linea gestionali.
# I telefoni sono disegnati da zero, niente schermate vere e niente loghi.

def mano(schermo, x, y, giro=0, scala=1):
    """Un telefono 200x360 tenuto in mano: le dita dietro, il pollice sopra.
    Il palmo esce dal fondo del disegno."""
    dita = "".join(f'<rect x="168" y="{d}" width="62" height="42" rx="21" class="dito"/>'
                   for d in (128, 178, 228, 278))
    return f"""
  <g transform="translate({x} {y}) rotate({giro} 100 180) scale({scala})">
    {dita}
    <rect x="0" y="0" width="200" height="360" rx="32" class="telefono"/>
    <rect x="76" y="16" width="48" height="7" rx="3.5" class="riga-tenue"/>
    {schermo}
    <path class="dito" d="M-40 560 C -44 420, -46 330, -22 268 C -8 234, 14 212, 40 204
      C 60 198, 74 214, 64 232 C 50 258, 32 280, 28 310 C 24 336, 50 356, 96 372
      C 136 386, 168 410, 184 560"/>
  </g>"""

def monitor():
    quadri = "".join(
        f'<rect x="{112 + c*100}" y="{140 + r*100}" width="92" height="92" rx="8" '
        f'fill="url(#g)" opacity="{(.16, .34, .5)[(r + c) % 3]}"/>'
        for r in range(2) for c in range(3))
    return f"""
<svg viewBox="0 0 880 430" class="art">
  <text x="92" y="24" class="micro">profilo</text>
  <text x="452" y="24" class="micro">bozza</text>
  <rect x="64" y="44" width="752" height="330" rx="18" class="tratto"/>
  <rect x="92" y="70" width="340" height="280" rx="10" class="debole"/>
  <circle cx="132" cy="106" r="18" class="riga-tenue"/>
  <rect x="164" y="100" width="120" height="10" rx="5" class="riga-tenue"/>
  {quadri}
  <rect x="452" y="70" width="336" height="280" rx="10" class="debole"/>
  <rect x="472" y="90" width="296" height="96" rx="8" fill="url(#g)" opacity=".34"/>
  <rect x="472" y="208" width="210" height="13" rx="6.5" class="riga"/>
  <rect x="472" y="236" width="270" height="9" rx="4.5" class="riga-tenue"/>
  <rect x="472" y="256" width="230" height="9" rx="4.5" class="riga-tenue"/>
  <rect x="472" y="294" width="120" height="36" rx="18" fill="url(#g)"/>
  <rect x="398" y="374" width="84" height="40" class="tratto-tenue"/>
  <rect x="330" y="414" width="220" height="10" rx="5" class="tratto-tenue"/>
</svg>"""

def bozza_in_mano():
    schermo = """
    <rect x="18" y="40" width="164" height="96" rx="10" fill="url(#g)" opacity=".3"/>
    <rect x="18" y="154" width="126" height="11" rx="5.5" class="riga"/>
    <rect x="18" y="180" width="164" height="8" rx="4" class="riga-tenue"/>
    <rect x="18" y="198" width="140" height="8" rx="4" class="riga-tenue"/>
    <rect x="70" y="232" width="112" height="36" rx="18" fill="url(#g)"/>
    <rect x="70" y="290" width="112" height="8" rx="4" class="riga-tenue"/>"""
    return f"""
<svg viewBox="0 0 880 452" class="art">
  <text x="470" y="80" class="micro">in chat</text>
  <rect x="470" y="110" width="390" height="140" rx="36" class="debole"/>
  <path d="M496 236 L472 282 L540 246 Z" class="debole"/>
  <rect x="510" y="152" width="300" height="12" rx="6" class="riga"/>
  <rect x="510" y="190" width="220" height="12" rx="6" class="riga-tenue"/>
  {mano(schermo, 150, 40, -6)}
</svg>"""

def insegna():
    return """
<svg viewBox="0 0 880 380" class="art">
  <line x1="170" y1="0" x2="170" y2="40" class="tratto-tenue"/>
  <line x1="710" y1="0" x2="710" y2="40" class="tratto-tenue"/>
  <rect x="40" y="40" width="800" height="150" rx="10" class="tratto"/>
  <rect x="58" y="58" width="764" height="114" rx="4" class="tratto-tenue"/>
  <text x="440" y="135" class="insegna" text-anchor="middle">IL TUO NEGOZIO</text>
  <path d="M440 200 V 252" class="percorso"/>
  <rect x="40" y="268" width="800" height="96" rx="48" class="tratto"/>
  <rect x="84" y="310" width="28" height="22" rx="4" class="riga"/>
  <path d="M90 310 v-8 a8 8 0 0 1 16 0 v8" fill="none" stroke="#84848f" stroke-width="3"/>
  <text x="140" y="331" class="mono-grande">iltuonegozio<tspan fill="url(#g)">.it</tspan></text>
</svg>"""

def comodino():
    return """
<svg viewBox="0 0 880 452" class="art">
  <ellipse cx="636" cy="210" rx="190" ry="150" fill="url(#g)" opacity=".07"/>
  <rect x="470" y="14" width="330" height="72" rx="36" class="debole"/>
  <path d="M640 80 L660 112 L680 80 Z" class="debole"/>
  <rect x="504" y="36" width="230" height="10" rx="5" class="riga"/>
  <rect x="504" y="56" width="150" height="8" rx="4" class="riga-tenue"/>
  <rect x="560" y="116" width="150" height="206" rx="22" class="telefono"/>
  <rect x="574" y="134" width="122" height="170" rx="12" fill="url(#g)" opacity=".16"/>
  <rect x="582" y="152" width="106" height="38" rx="10" fill="url(#g)" opacity=".7"/>
  <path d="M536 190 q-14 34 0 68 M518 176 q-22 48 0 96" class="vibra"/>
  <path d="M734 190 q14 34 0 68 M752 176 q22 48 0 96" class="vibra"/>
  <rect x="110" y="168" width="300" height="152" rx="28" class="telefono"/>
  <rect x="134" y="192" width="252" height="104" rx="12" class="debole"/>
  <text x="260" y="274" class="cifre" text-anchor="middle">23:50</text>
  <rect x="40" y="320" width="800" height="18" rx="6" class="tratto"/>
  <rect x="70" y="338" width="740" height="130" class="tratto-tenue"/>
  <line x1="70" y1="398" x2="810" y2="398" class="tratto-tenue"/>
  <circle cx="440" cy="368" r="7" class="riga-tenue"/>
</svg>"""

def bancone():
    return """
<svg viewBox="0 0 880 452" class="art">
  <rect x="110" y="10" width="660" height="200" rx="46" class="debole"/>
  <path d="M290 204 L262 262 L360 204 Z" class="debole"/>
  <text x="440" y="100" class="trattini" text-anchor="middle">_ _ . _ _ _ <tspan fill="url(#g)">_</tspan> .</text>
  <text x="440" y="174" class="trattini" text-anchor="middle">. _ _ <tspan fill="url(#g)">.</tspan> _ _ _ . _</text>
  <path d="M100 300 L780 300 L860 360 L20 360 Z" class="tratto"/>
  <rect x="20" y="360" width="840" height="110" class="tratto-tenue"/>
  <line x1="300" y1="360" x2="300" y2="452" class="tratto-tenue"/>
  <line x1="580" y1="360" x2="580" y2="452" class="tratto-tenue"/>
  <path d="M372 312 L524 312 L540 346 L356 346 Z" class="telefono"/>
  <path d="M384 318 L514 318 L526 340 L372 340 Z" fill="url(#g)" opacity=".3"/>
</svg>"""

def rullino():
    quadri = []
    tinte = [.42, 0, .22, .3, .5, "pasta", 0, .18, .36, .26, 0, "bolletta"]
    for k, t in enumerate(tinte):
        x, y = 60 + (k % 3) * 90, 74 + (k // 3) * 90
        if t == 0:
            quadri.append(f'<rect x="{x}" y="{y}" width="84" height="84" rx="6" class="debole"/>')
        elif t == "pasta":
            quadri.append(
                f'<rect x="{x}" y="{y}" width="84" height="84" rx="6" class="debole"/>'
                f'<circle cx="{x+42}" cy="{y+42}" r="30" class="tratto"/>'
                f'<circle cx="{x+42}" cy="{y+42}" r="18" class="tratto-tenue"/>'
                f'<path d="M{x+28} {y+38} q7 -9 14 0 t14 0 M{x+28} {y+48} q7 -9 14 0 t14 0" '
                f'fill="none" stroke="#84848f" stroke-width="2.5"/>')
        elif t == "bolletta":
            quadri.append(
                f'<rect x="{x}" y="{y}" width="84" height="84" rx="6" class="debole"/>'
                f'<rect x="{x+20}" y="{y+12}" width="44" height="60" rx="3" class="tratto"/>'
                + "".join(f'<rect x="{x+28}" y="{y+22+i*11}" width="{28 - i*4}" height="4" '
                          f'rx="2" class="riga-tenue"/>' for i in range(4)))
        else:
            quadri.append(f'<rect x="{x}" y="{y}" width="84" height="84" rx="6" '
                          f'fill="url(#g)" opacity="{t}"/>')
    return f"""
<svg viewBox="0 0 880 452" class="art">
  <rect x="40" y="6" width="300" height="440" rx="40" class="tratto"/>
  <rect x="166" y="24" width="48" height="7" rx="3.5" class="riga-tenue"/>
  <rect x="60" y="46" width="110" height="10" rx="5" class="riga-tenue"/>
  {''.join(quadri)}
  <path d="M330 206 H 420" class="filo"/><text x="436" y="214" class="micro">pranzo di domenica</text>
  <path d="M330 296 H 420" class="filo"/><text x="436" y="304" class="micro">i lavori</text>
  <path d="M330 386 H 420" class="filo"/><text x="436" y="394" class="micro">bolletta</text>
</svg>"""

def furgone():
    schermo = """
    <rect x="18" y="40" width="120" height="10" rx="5" class="riga-tenue"/>
    <rect x="18" y="80" width="130" height="44" rx="22" class="debole"/>
    <rect x="34" y="208" width="148" height="56" rx="28" fill="url(#g)"/>
    <path d="M58 226 L74 236 L58 246 Z" fill="#0a0a0d"/>""" + "".join(
        f'<rect x="{86 + i*8}" y="{236 - h/2}" width="4" height="{h}" rx="2" fill="#0a0a0d" opacity=".6"/>'
        for i, h in enumerate((10, 22, 14, 28, 18, 24, 10, 16, 8, 12)))
    return f"""
<svg viewBox="0 0 880 452" class="art">
  <defs><clipPath id="cielo"><rect x="0" y="0" width="880" height="410"/></clipPath></defs>
  <circle cx="470" cy="410" r="170" fill="url(#g)" opacity=".22" clip-path="url(#cielo)"/>
  <circle cx="470" cy="410" r="110" fill="url(#g)" opacity=".28" clip-path="url(#cielo)"/>
  <line x1="0" y1="410" x2="880" y2="410" class="tratto-tenue"/>
  <path d="M60 86 L8 60 L8 392 L60 370 Z" class="telefono"/>
  <path d="M420 86 L472 60 L472 392 L420 370 Z" class="telefono"/>
  <rect x="24" y="300" width="18" height="40" rx="4" fill="url(#g)"/>
  <rect x="438" y="300" width="18" height="40" rx="4" fill="url(#g)"/>
  <rect x="60" y="70" width="360" height="310" rx="22" class="tratto"/>
  <rect x="88" y="100" width="304" height="240" rx="6" class="debole"/>
  <line x1="88" y1="186" x2="392" y2="186" class="tratto-tenue"/>
  <line x1="88" y1="264" x2="392" y2="264" class="tratto-tenue"/>
  <rect x="110" y="140" width="70" height="46" rx="4" class="tratto-tenue"/>
  <rect x="196" y="154" width="48" height="32" rx="4" class="tratto-tenue"/>
  <rect x="300" y="218" width="72" height="46" rx="4" class="tratto-tenue"/>
  <rect x="50" y="380" width="380" height="18" rx="6" class="tratto"/>
  <rect x="84" y="398" width="72" height="24" rx="6" class="debole"/>
  <rect x="324" y="398" width="72" height="24" rx="6" class="debole"/>
  {mano(schermo, 620, 96, 8, .9)}
</svg>"""

def chiudi_lavoro():
    righe = ""
    for i, (w, forte) in enumerate([(150, 0), (120, 1), (170, 0)]):
        y = 130 + i * 92
        colore = 'fill="url(#g)"' if forte else 'class="riga"'
        righe += (f'<circle cx="514" cy="{y}" r="18" {colore} opacity=".8"/>'
                  f'<rect x="548" y="{y-14}" width="{w}" height="11" rx="5.5" {colore}/>'
                  f'<rect x="548" y="{y+6}" width="90" height="8" rx="4" class="riga-tenue"/>'
                  f'<text x="860" y="{y+10}" class="voce-tenue" text-anchor="end">{(8, 7, 8)[i]} h</text>'
                  f'<line x1="490" y1="{y+46}" x2="880" y2="{y+46}" class="tratto-tenue"/>')
    return f"""
<svg viewBox="0 0 880 452" class="art">
  <rect x="40" y="6" width="320" height="440" rx="40" class="telefono"/>
  <rect x="176" y="24" width="48" height="7" rx="3.5" class="riga-tenue"/>
  <text x="70" y="82" class="micro">cantiere</text>
  <text x="70" y="128" class="schermo-titolo">Cantiere 1</text>
  <line x1="70" y1="160" x2="330" y2="160" class="tratto-tenue"/>
  <text x="70" y="208" class="voce-tenue">Inizio</text>
  <text x="330" y="208" class="voce" text-anchor="end">7:30</text>
  <line x1="70" y1="236" x2="330" y2="236" class="tratto-tenue"/>
  <text x="70" y="284" class="voce-tenue">Fine</text>
  <text x="330" y="284" class="voce" text-anchor="end">16:45</text>
  <line x1="70" y1="312" x2="330" y2="312" class="tratto-tenue"/>
  <rect x="64" y="350" width="272" height="64" rx="32" fill="url(#g)"/>
  <text x="200" y="392" class="link" text-anchor="middle">Chiudi il lavoro</text>
  <path d="M344 382 C 420 382, 420 222, 484 222" fill="none" stroke="url(#g)"
    stroke-width="3" stroke-dasharray="8 8"/>
  <text x="490" y="60" class="micro">in ufficio</text>
  {righe}
</svg>"""

def logo():
    return '<img class="marchione" src="../../simbolo.svg" alt="">'

def niente():
    return ""

def lavagna():
    return """
<svg viewBox="0 0 880 430" class="art">
  <rect x="10" y="10" width="860" height="380" rx="12" class="tratto"/>
  <rect x="26" y="26" width="828" height="348" rx="6" class="tratto-tenue"/>
  <ellipse cx="660" cy="150" rx="170" ry="40" fill="#fff" opacity=".045"/>
  <ellipse cx="290" cy="306" rx="110" ry="34" fill="#fff" opacity=".045"/>
  <text x="70" y="92" class="penna">domani</text>
  <path d="M70 108 q60 10 140 -2" fill="none" stroke="url(#g)" stroke-width="3"/>
  <text x="70" y="168" class="penna">Luca - Cantiere 4</text>
  <text x="70" y="244" class="penna">Andrea - <tspan class="cancellato"
    text-decoration="line-through">Cantiere 2</tspan> <tspan fill="url(#g)">Cantiere 4</tspan></text>
  <text x="70" y="320" class="penna">Marco - <tspan opacity=".2">Cant</tspan>   Cantiere 3 ?</text>
  <rect x="240" y="390" width="400" height="14" rx="7" class="tratto-tenue"/>
  <rect x="300" y="376" width="96" height="14" rx="7" fill="url(#g)"/>
  <rect x="420" y="376" width="96" height="14" rx="7" class="riga-tenue"/>
</svg>"""

def domani():
    def faccia(x, nome):
        return f"""
  <g opacity=".45">
    <rect x="{x}" y="70" width="180" height="320" rx="30" class="tratto-tenue"/>
    <rect x="{x+20}" y="112" width="70" height="8" rx="4" class="riga-tenue"/>
    <rect x="{x+20}" y="136" width="120" height="14" rx="7" class="riga"/>
    <rect x="{x+20}" y="166" width="90" height="9" rx="4.5" class="riga-tenue"/>
    <rect x="{x+20}" y="210" width="140" height="150" rx="10" class="debole"/>
  </g>
  <text x="{x}" y="430" class="micro">{nome}</text>"""
    return f"""
<svg viewBox="0 0 880 452" class="art">
  <defs><clipPath id="mappa"><rect x="62" y="270" width="276" height="150" rx="14"/></clipPath></defs>
  <rect x="40" y="6" width="320" height="440" rx="40" class="telefono"/>
  <rect x="176" y="24" width="48" height="7" rx="3.5" class="riga-tenue"/>
  <text x="70" y="82" class="micro">domani</text>
  <text x="70" y="130" class="schermo-titolo">Cantiere 4</text>
  <text x="70" y="182" class="voce">ore 7:30</text>
  <text x="70" y="230" class="voce-tenue">con Luca e Andrea</text>
  <g clip-path="url(#mappa)">
    <rect x="62" y="270" width="276" height="150" class="debole"/>
    <rect x="62" y="304" width="276" height="20" class="strada"/>
    <rect x="62" y="376" width="276" height="20" class="strada"/>
    <rect x="150" y="270" width="20" height="150" class="strada"/>
    <rect x="262" y="270" width="20" height="150" class="strada"/>
    <path d="M90 314 H160 V386 H272 V352" class="percorso"/>
  </g>
  <rect x="62" y="270" width="276" height="150" rx="14" class="tratto-tenue"/>
  <g transform="translate(272 318) scale(.6)">
    <path d="M0 64 C -14 42 -34 26 -34 0 A34 34 0 0 1 34 0 C 34 26 14 42 0 64 Z" fill="url(#g)"/>
    <circle cx="0" cy="0" r="12" fill="#0a0a0d"/>
  </g>
  {faccia(450, "luca")}
  {faccia(670, "andrea")}
</svg>"""

def non_risponde():
    celle = "".join(
        f'<rect x="{c*112}" y="{20 + r*48}" width="112" height="48" class="cella"/>'
        + (f'<rect x="{c*112 + 16}" y="{38 + r*48}" width="{(56, 40, 64, 48)[(r*3 + c) % 4]}" '
           f'height="9" rx="4.5" class="riga-tenue"/>' if c and r else "")
        for r in range(6) for c in range(6))
    return f"""
<svg viewBox="0 0 880 320" class="art">
  <g opacity=".7">{celle}</g>
  <rect x="380" y="96" width="496" height="212" rx="16" class="telefono"/>
  <line x1="380" y1="144" x2="876" y2="144" class="tratto-tenue"/>
  <circle cx="412" cy="120" r="7" class="riga-tenue"/>
  <circle cx="436" cy="120" r="7" class="riga-tenue"/>
  <circle cx="460" cy="120" r="7" class="riga-tenue"/>
  <text x="412" y="204" class="voce">Il programma non risponde</text>
  <rect x="580" y="236" width="130" height="46" rx="23" class="tratto-tenue"/>
  <rect x="724" y="236" width="130" height="46" rx="23" class="tratto"/>
</svg>"""

def cartella():
    nomi = ["ore_ottobre.xlsx", "ore_ottobre_DEFINITIVO.xlsx",
            "ore_ottobre_DEFINITIVO_v2_Marco.xlsx", "ore_ottobre_QUESTO.xlsx"]
    righe = ""
    for i, nome in enumerate(nomi):
        y = 128 + i * 80
        if i == 3:
            righe += (f'<rect x="16" y="{y}" width="848" height="68" rx="10" fill="url(#g)" opacity=".16"/>'
                      f'<rect x="16" y="{y}" width="6" height="68" fill="url(#g)"/>')
        righe += (f'<path d="M44 {y+12} h26 l12 12 v34 h-38 Z" class="tratto"/>'
                  f'<line x1="52" y1="{y+40}" x2="74" y2="{y+40}" class="tratto-tenue"/>'
                  f'<line x1="52" y1="{y+50}" x2="74" y2="{y+50}" class="tratto-tenue"/>'
                  f'<text x="104" y="{y+45}" class="mono">{nome}</text>')
    return f"""
<svg viewBox="0 0 880 452" class="art">
  <rect x="0" y="8" width="880" height="440" rx="16" class="tratto-tenue"/>
  <path d="M30 42 h26 l8 8 h36 v32 h-70 Z" class="tratto"/>
  <text x="120" y="74" class="micro">cartella condivisa</text>
  <line x1="0" y1="106" x2="880" y2="106" class="tratto-tenue"/>
  {righe}
</svg>"""

def distanza():
    def spillo(x):
        return f"""
  <g transform="translate({x} 86)">
    <path d="M0 64 C -14 42 -34 26 -34 0 A34 34 0 0 1 34 0 C 34 26 14 42 0 64 Z" fill="url(#g)"/>
    <circle cx="0" cy="0" r="12" fill="#0a0a0d"/>
  </g>"""
    return f"""
<svg viewBox="0 0 880 250" class="art">
  <line x1="0" y1="150" x2="880" y2="150" class="tratto-tenue"/>
  <path d="M190 140 C 330 84, 550 84, 690 140" class="percorso"/>
  <text x="440" y="70" class="voce" text-anchor="middle">40 km</text>
  {spillo(150)}{spillo(730)}
  <text x="150" y="200" class="micro" text-anchor="middle">cantiere 1</text>
  <text x="730" y="200" class="micro" text-anchor="middle">cantiere 2</text>
  <text x="150" y="238" class="mono" text-anchor="middle">10:00</text>
  <text x="730" y="238" class="mono" text-anchor="middle">10:00</text>
</svg>"""

def quadretti():
    linee = "".join(f'<line x1="40" y1="{y}" x2="840" y2="{y}" class="quadretto"/>'
                    for y in range(40, 440, 30))
    linee += "".join(f'<line x1="{x}" y1="10" x2="{x}" y2="440" class="quadretto"/>'
                     for x in range(70, 840, 30))
    return f"""
<svg viewBox="0 0 880 452" class="art">
  <rect x="40" y="10" width="800" height="430" rx="6" fill="#0e0e12"/>
  {linee}
  <line x1="118" y1="10" x2="118" y2="440" stroke="url(#g)" stroke-width="2" opacity=".5"/>
  <rect x="40" y="10" width="800" height="430" rx="6" class="tratto-tenue"/>
  <text x="140" y="124" class="penna" opacity=".45">lun. 6 - Cantiere 2 - 8</text>
  <text x="140" y="234" class="penna">mar. 7 - <tspan fill="url(#g)">??</tspan> Monza (o Lissone)</text>
  <text x="140" y="344" class="penna" opacity=".45">mer. 8 -</text>
</svg>"""

# ---------------------------------------------------------------- i contenuti

# La prima di ogni serie e' la copertina: porta il titolo e l'indice delle
# cinque che seguono. Le storie dicono una situazione che al titolare capita
# davvero e si fermano li'. Niente antitesi e niente frase che tira la morale
# di quella prima: Patrick, 16 settembre, «cerca di parlare normalmente».
SERIE = {}

SERIE["2026-09-16"] = dict(copertina=dict(
    tag="DenkiCode",
    titolo="Cinque cose sul sito del tuo negozio",
    corpo="Quelle che si vedono quando un cliente lo apre davvero.",
    indice=["Chi ti cerca su Google", "I primi dieci secondi",
            "Il telefono in una mano", "Le prenotazioni di sera",
            "Le foto"],
), storie=[
    dict(tag="Farsi trovare", grafica=ricerca,
         titolo="Chi ha bisogno adesso cerca su Google",
         corpo="Scrive il mestiere e il nome del paese, apre i primi risultati "
               "e chiama il primo che risponde. Su Instagram invece ti trova "
               "chi sa gia' come ti chiami. Questo qui no, e senza un sito non "
               "ti vede nemmeno."),
    dict(tag="I primi secondi", grafica=dieci_secondi,
         titolo="Guarda l'indirizzo e il telefono, poi decide",
         corpo="Apre il sito e cerca dove sei e come si prenota. Ci mette dieci "
               "secondi. Se le deve andare a cercare in fondo alla pagina dei "
               "contatti, chiude e prova un altro nome."),
    dict(tag="Telefono", grafica=telefono,
         titolo="Il tuo sito lo aprono col telefono in una mano",
         corpo="In fila alla cassa, sul divano, davanti alla vetrina per vedere "
               "se sei aperto. Dal computer quasi nessuno. Un sito provato solo "
               "sul monitor grande, sul telefono diventa una cosa da "
               "ingrandire con le dita."),
    dict(tag="Agenda", grafica=notte,
         titolo="Chi decide alle undici di sera non ti telefona",
         corpo="Aspetta domani, e domani ha da fare. Oppure intanto ha chiamato "
               "un altro. Con l'agenda dentro il sito ti lascia la prenotazione "
               "la sera stessa, e la trovi quando apri."),
    dict(tag="Fotografie", grafica=foto,
         titolo="Se il sito ti sembra vecchio, guarda le foto",
         corpo="Le foto scure fatte col telefono la sera fanno sembrare vecchio "
               "qualsiasi sito. Cinque scatti di giorno, con la luce che entra "
               "dalla finestra, e la stessa pagina cambia faccia."),
])

# Il seguito della prima, sugli argomenti che restavano fuori. Non tornano i
# tre che Patrick ha tolto il 16 settembre (la scheda Google, i modelli
# pronti, il come lavoriamo): il gancio della bozza resta il mestiere del DM.
# Niente che metta in guardia dai link nei messaggi, perche' e' il canale con
# cui scrive lui.
SERIE["2026-09-25"] = dict(copertina=dict(
    tag="DenkiCode",
    titolo="Altre cinque cose sul sito del tuo negozio",
    corpo="Queste ti capitano gia', anche se il sito non ce l'hai.",
    indice=["Chi ti chiede il prezzo", "Le ultime foto del profilo",
            "Il passaparola su WhatsApp", "Il primo appuntamento",
            "I complimenti in DM"],
), storie=[
    dict(tag="Prezzi", grafica=messaggi,
         titolo="Il prezzo te lo chiedono mentre lavori",
         corpo="Hai qualcuno sulla poltrona e il telefono vibra. La sera "
               "riscrivi il listino da capo, e chi te l'aveva chiesto intanto "
               "ha gia' scritto a un altro negozio. Con i prezzi sul sito gli "
               "mandi un link. Ci vuole un attimo."),
    dict(tag="Servizi", grafica=profilo,
         titolo="Chi apre il profilo guarda le ultime foto",
         corpo="Se da un mese posti sempre lo stesso tipo di lavoro, per lui "
               "fai solo quello. Il resto sta trenta post piu' sotto. Fin li' "
               "scendono in pochi. Sul sito i servizi stanno tutti in una "
               "pagina, anche quelli che non fotografi mai."),
    dict(tag="Passaparola", grafica=whatsapp,
         titolo="Un cliente contento ti consiglia su WhatsApp",
         corpo="Manda a un amico il link del tuo profilo. Se l'amico Instagram "
               "non ce l'ha, lo apre e dopo due foto la pagina gli chiede di "
               "accedere. Il sito si apre e basta, da qualunque telefono."),
    dict(tag="La prima volta", grafica=mappa,
         titolo="La prima volta nessuno sa dove parcheggiare",
         corpo="Il cliente nuovo fa due volte il giro dell'isolato, poi ti "
               "chiama dalla strada perche' non trova l'ingresso. Sul sito "
               "basta una riga sotto la mappa: dove si lascia la macchina e da "
               "che parte si entra."),
    dict(tag="Recensioni", grafica=complimento,
         titolo="I complimenti piu' belli arrivano in DM",
         corpo="Una cliente si riguarda allo specchio di casa e ti manda un "
               "messaggio per ringraziarti. Lo leggi solo tu. Con il suo "
               "permesso lo metti sul sito, e lo legge anche chi non ti "
               "conosce ancora."),
])

# Ottobre: niente copertina, si numerano «1 / 3». Testi dalle bozze del 3/10
# (02-Sales/processo/bozze-social-2026-10-03.md). Le emoji delle bozze
# diventano un segno nell'etichetta: pallino verde per 🟢, fulmine per ⚡.
# Il frame col sondaggio esce due volte: senza sticker (quello dell'API) e
# -sondaggio, con la domanda in alto e la fascia vuota dove Patrick
# appoggia lo sticker a mano.
PALLINO = '<span class="pallino"></span>'
FULMINE = ('<svg class="fulmine" viewBox="0 0 12 16"><path d="M7.5 0 L0 9.2 H5 '
           'L4 16 L12 6.6 H6.8 Z" fill="url(#g)"/></svg>')

SERIE["2026-10-05-come-funziona"] = dict(storie=[
    dict(tag="Prima di scriverti", grafica=monitor,
         titolo="Il tuo sito parte dal tuo profilo",
         corpo="Sul monitor teniamo aperto il tuo profilo, e nella finestra di "
               "fianco c'e' la bozza del sito che stiamo facendo per te. "
               "Guardiamo che lavori fai piu' spesso e dove si trova il negozio. "
               "Quando ti scriviamo, e' gia' pronta."),
    dict(tag="La bozza", grafica=bozza_in_mano,
         titolo="La guardi dal telefono, tra due clienti",
         corpo="Ti mandiamo il link qui in DM. La apri appena il negozio si "
               "svuota e la scorri col pollice, come fara' chi ti cerca. Se una "
               "foto non ti convince o manca un servizio, ce lo scrivi nella "
               "stessa chat e lo sistemiamo."),
    dict(tag="Il primo giorno", grafica=insegna,
         titolo="Il sito va online col tuo nome",
         corpo="Nell'indirizzo c'e' il nome del negozio, lo stesso "
               "dell'insegna. Il primo giorno lo apri dal telefono, e il link "
               "finisce dritto nella chat di famiglia. Il sito e l'indirizzo "
               "restano tuoi."),
])

SERIE["2026-10-05-cose-che-succedono"] = dict(storie=[
    dict(tag="Gli orari", grafica=comodino,
         titolo="Mezzanotte meno dieci, il telefono vibra",
         corpo="E' una cliente: «Scusa l'ora, domani siete aperti?» "
               "Le rispondi lo stesso, e ormai il sonno e' passato. Su un sito "
               "gli orari stanno sotto il nome del negozio, e lei li trova da "
               "sola."),
    dict(tag="A voce", grafica=bancone,
         titolo="Il nome del profilo, dettato al banco",
         corpo="«Silvia, underscore, hair, punto, studio, tutto "
               "attaccato.» Lei scrive e cancella. Alla fine ti passa il "
               "telefono, e il profilo lo cerchi tu mentre in negozio c'e' gente "
               "che aspetta. Un indirizzo col nome del negozio si detta in un "
               "fiato."),
    dict(tag="Il rullino", grafica=rullino,
         titolo="Ti chiedono qualche foto dei lavori",
         corpo="Apri il rullino e scorri, in mezzo al pranzo di domenica e agli "
               "screenshot della bolletta. Dieci minuti dopo gliene hai mandate "
               "sei, una per volta. Sul sito i lavori stanno gia' in fila, e "
               "basta un link."),
])

SERIE["2026-10-07-sarto-1"] = dict(storie=[
    dict(tag="Le ore delle squadre", grafica=furgone,
         titolo="Le 18:30.",
         corpo="La squadra chiude il furgone e le ore partono in un vocale sul "
               "gruppo.",
         sondaggio=dict(titolo="Le ore delle squadre, da voi, come arrivano "
                               "in ufficio?", corpo="")),
    dict(tag=PALLINO + "Le ore delle squadre", grafica=chiudi_lavoro,
         titolo="Una schermata sola, sul telefono di chi lavora.",
         corpo="Sceglie il cantiere, segna l'ora di fine e chiude. In ufficio "
               "arriva gia' divisa per persona e per cantiere."),
    dict(tag=FULMINE + "Le ore delle squadre", grafica=logo,
         titolo="La schermata la disegniamo su come lavorate voi.",
         corpo="Scrivici SARTO in DM e veniamo a vedere da dove partono le "
               "vostre ore."),
])

SERIE["2026-10-09-relatable-1"] = dict(storie=[
    dict(tag="Il foglio che non si salva", grafica=non_risponde,
         titolo="Venerdi', 18:52. Hai appena finito di riportare le ore di "
                "tutto il mese. Il foglio si chiude da solo. L'ultimo "
                "salvataggio e' di martedi'.",
         corpo=""),
    dict(tag="Il foglio che non si salva", grafica=cartella,
         titolo="Intanto, nella cartella condivisa, la famiglia si e' "
                "allargata.",
         corpo=""),
    dict(tag=FULMINE + "Il foglio che non si salva", grafica=logo,
         titolo="Nei programmi che scriviamo le ore si salvano mentre le "
                "segni, e la versione e' una sola.",
         corpo="Scrivici SARTO in DM.",
         sondaggio=dict(titolo="Quante versioni di «definitivo» "
                               "avete in cartella?",
                        corpo="Nei programmi che scriviamo le ore si salvano "
                              "mentre le segni. Scrivici SARTO in DM.",
                        grafica=niente)),
])

SERIE["2026-10-14-sarto-2"] = dict(storie=[
    dict(tag="Chi va dove domani", grafica=lavagna,
         titolo="Le 17.",
         corpo="Il programma di domani e' sulla lavagna dell'ufficio, e lo "
               "vede solo chi passa di li'.",
         sondaggio=dict(titolo="Chi va dove domani, da voi, dove sta "
                               "scritto?", corpo="")),
    dict(tag=PALLINO + "Chi va dove domani", grafica=domani,
         titolo="La sera ognuno apre il telefono e trova il suo domani.",
         corpo="Se l'ufficio sposta qualcuno, lo trova gia' scritto li'."),
    dict(tag=FULMINE + "Chi va dove domani", grafica=logo,
         titolo="Lo scriviamo partendo dalla vostra lavagna, con le parole "
                "che usate gia'.",
         corpo="Scrivici SARTO in DM."),
])

SERIE["2026-10-16-relatable-2"] = dict(storie=[
    dict(tag="Le ore segnate a memoria", grafica=distanza,
         titolo="Secondo il foglio ore, martedi' alle 10 Luca era su due "
                "cantieri. A quaranta chilometri di distanza.",
         corpo=""),
    dict(tag="Le ore segnate a memoria", grafica=quadretti,
         titolo="Il venerdi' glielo chiedi.",
         corpo="«Martedi'… era il giorno che pioveva?» Da li' si "
               "va a memoria, la sua e la tua."),
    dict(tag=FULMINE + "Le ore segnate a memoria", grafica=logo,
         titolo="Quando la squadra segna l'ora dal telefono prima di lasciare "
                "il cantiere, il venerdi' non serve ricordarsi niente.",
         corpo="Scrivici SARTO in DM.",
         sondaggio=dict(titolo="Le ore, da voi, quando si segnano?",
                        corpo="Con l'ora segnata dal telefono prima di "
                              "lasciare il cantiere, il venerdi' non serve "
                              "ricordarsi niente. Scrivici SARTO in DM.",
                        grafica=niente)),
])

# gli accenti veri: il sorgente non porta le lettere accentate, e nemmeno
# l'apostrofo tipografico. Si sostituiscono qui, in quest'ordine.
ACCENTI = [
    (r"\bgia'", "gi\u00e0"), (r"\bpiu'", "pi\u00f9"), (r"\bli'", "l\u00ec"),
    (r"\bsi'", "s\u00ec"), (r"\bda'", "d\u00e0"), (r"\be'(?=[\s,.:;]|$)", "\u00e8"),
    (r"\battivita'", "attivit\u00e0"), (r"\bqualita'", "qualit\u00e0"),
    (r"\bperche'", "perch\u00e9"), (r"\bpero'", "per\u00f2"),
    # a inizio frase: «E' gente» restava con l'apostrofo
    (r"\bE'(?=[\s,.:;]|$)", "\u00c8"), (r"\bGia'", "Gi\u00e0"),
    (r"\bPiu'", "Pi\u00f9"), (r"\bLi'", "L\u00ec"), (r"\bSi'", "S\u00ec"),
    (r"\bDa'", "D\u00e0"), (r"\bPerche'", "Perch\u00e9"),
    (r"\bPero'", "Per\u00f2"), (r"\bLa'", "L\u00e0"), (r"\bla'", "l\u00e0"),
    (r"\bfara'", "far\u00e0"),
    (r"\b([Ll]une|[Mm]arte|[Mm]ercole|[Gg]iove|[Vv]ener)di'", "\\1d\u00ec"),
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
    text-wrap:pretty;
  }}
  footer {{ margin-top:64px; display:flex; align-items:center; gap:30px; }}
  .barra {{
    height:5px; width:132px; border-radius:3px;
    background:linear-gradient(90deg,#923adf,#da2f9b);
  }}
  .sito {{ font-size:28px; font-weight:500; letter-spacing:.1em; color:#dededf; }}

  /* tratti comuni ai disegni */
  .telaio.fronte {{ justify-content:center; }}
  .marchione {{ width:150px; height:150px; display:block; }}
  .fronte h1 {{
    margin-top:56px; font-size:112px; line-height:.99; letter-spacing:-.042em;
  }}
  .fronte p {{ margin-top:34px; font-size:40px; color:#b6b6c0; max-width:760px; }}
  .indice {{ margin-top:78px; border-top:1px solid #23232b; }}
  .indice div {{
    display:flex; align-items:baseline; gap:30px;
    padding:25px 0; border-bottom:1px solid #23232b;
    font-size:35px; color:#c9c9d2; letter-spacing:-.01em;
  }}
  .indice span {{
    font-size:24px; font-weight:600; letter-spacing:.14em; color:#7a4bd0;
    font-variant-numeric:tabular-nums;
  }}
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
  .link {{ font-size:30px; font-weight:600; fill:#0a0a0d; }}
  .strada {{ fill:#131318; }}
  .lettera {{ font-size:54px; font-weight:700; fill:#e6e6ea; }}
  .percorso {{ fill:none; stroke:url(#g); stroke-width:4; stroke-dasharray:12 10;
              stroke-linecap:round; }}
  .virgolette {{ font-size:150px; font-weight:700; fill:url(#g); }}
</style>{extra}
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
    <span class="conta">{conta}</span>
  </header>
  <div class="scena">{grafica}</div>
  <div class="tag">{tag}</div>
  <h1>{titolo}</h1>{sticker}
  <p>{corpo}</p>
  <footer>
    <span class="barra"></span>
    <span class="sito">denkicode.com</span>
  </footer>
</div>
"""


FRONTE = """<!doctype html>
<meta charset="utf-8">
<title>{titolo}</title>
<style>{stile}</style>
<div class="fondo"></div>
<div class="trama"></div>
<div class="telaio fronte">
  <img class="marchione" src="../../simbolo.svg" alt="">
  <div class="tag" style="margin-top:44px">{tag}</div>
  <h1>{titolo}</h1>
  <p>{corpo}</p>
  <div class="indice">{indice}</div>
  <footer style="margin-top:58px">
    <span class="barra"></span>
    <span class="sito">denkicode.com</span>
  </footer>
</div>
"""

# Solo per le serie senza copertina: le serie di settembre restano byte per
# byte quelle di prima.
EXTRA = """
<style>
  p:empty { display:none; }
  .pallino { display:inline-block; width:22px; height:22px; border-radius:50%;
             margin-right:18px; vertical-align:-1px; background:#34c77b; }
  .fulmine { width:22px; height:29px; margin-right:16px; vertical-align:-4px; }
  .scena .marchione { width:260px; height:260px; }
  .telefono, .dito { fill:#0c0c10; stroke:#4a4a55; stroke-width:2.5; }
  .vibra { fill:none; stroke:url(#g); stroke-width:3; stroke-linecap:round; }
  .filo { fill:none; stroke:#3d3d46; stroke-width:2; stroke-dasharray:6 6; }
  .cella { fill:none; stroke:#22222a; stroke-width:2; }
  .quadretto { stroke:#1a1a21; stroke-width:1.5; }
  .insegna { font-size:58px; font-weight:700; letter-spacing:.16em; fill:url(#g); }
  .mono-grande { font-size:40px; fill:#c9c9d2; font-family:"SF Mono",Menlo,monospace; }
  .trattini { font-size:64px; fill:#84848f; letter-spacing:.06em;
              font-family:"SF Mono",Menlo,monospace; }
  .cifre { font-size:82px; font-weight:700; letter-spacing:-.02em; fill:url(#g); }
  .schermo-titolo { font-size:40px; font-weight:700; fill:#fff; letter-spacing:-.02em; }
  .art .penna { font-size:44px; fill:#c9c9d2;
           font-family:Noteworthy,"Bradley Hand","Marker Felt",cursive; }
  .cancellato { opacity:.45; }
  .sondaggio h1 { margin-top:84px; }
  .sondaggio .scena { order:1; flex:none; padding:40px 0 0; }
  .sondaggio .art { max-height:300px; }
  .sondaggio footer { order:2; }
  .sticker { flex:1; min-height:440px; display:flex; align-items:flex-end; }
  .sticker span { font-size:23px; font-weight:500; letter-spacing:.14em;
                  text-transform:uppercase; color:#5e5e6a; }
</style>"""

def main():
    serie = sys.argv[1] if len(sys.argv) > 1 else max(SERIE)
    if serie not in SERIE:
        sys.exit(f"serie {serie} sconosciuta, ci sono: {', '.join(sorted(SERIE))}")
    copertina, storie = SERIE[serie].get("copertina"), SERIE[serie]["storie"]
    fuori = FUORI / serie
    fuori.mkdir(parents=True, exist_ok=True)
    for f in fuori.glob("storia-*.html"):
        f.unlink()
    tot = len(storie)
    print(f"serie {serie}")

    if copertina:
        stile = PAGINA[PAGINA.index("<style>") + 7:PAGINA.index("</style>")]
        stile = stile.replace("{{", "{").replace("}}", "}")
        indice = "".join(
            f'<div><span>{i:02d}</span>{accenta(v)}</div>'
            for i, v in enumerate(copertina["indice"], 1)
        )
        (fuori / "storia-00.html").write_text(
            FRONTE.format(stile=stile, tag=copertina["tag"],
                          titolo=accenta(copertina["titolo"]),
                          corpo=accenta(copertina["corpo"]), indice=indice),
            encoding="utf-8")
        print("storia-00.html  " + copertina["titolo"] + "  (copertina)")

    for i, s in enumerate(storie, 1):
        conta = f"{i:02d} / {tot:02d}" if copertina else f"{i} / {tot}"
        versioni = [("", s)]
        if "sondaggio" in s:
            versioni.append(("-sondaggio", dict(s, tag="", **s["sondaggio"])))
        for coda, v in versioni:
            titolo = accenta(v["titolo"])
            h1 = 96 if len(titolo) <= 30 else (86 if len(titolo) <= 48 else 78)
            html = PAGINA.format(
                conta=conta, tag=v["tag"], titolo=titolo,
                corpo=accenta(v["corpo"]), grafica=accenta(v["grafica"]()),
                corpo_h1=h1, extra="" if copertina else EXTRA,
                classe=" sondaggio" if coda else "",
                sticker='<div class="sticker"><span>rispondi qui sopra</span></div>'
                        if coda else "",
            )
            (fuori / f"storia-{i:02d}{coda}.html").write_text(html, encoding="utf-8")
            print(f"storia-{i:02d}{coda}.html  {titolo}")

if __name__ == "__main__":
    main()
