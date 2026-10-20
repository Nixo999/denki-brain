# Pagine prodotto nello stile di apple.com

Questo file serve per una landing o una pagina prodotto, non per un'app. I
valori sono misurati il 20 ottobre 2026 sui fogli di stile veri della home,
di `/macbook-air/` e di `/iphone/`. Dove le fonti della community (il DESIGN.md
di VoltAgent e la skill di bkhoi0311) dicono altro, hanno torto. Gli errori
principali sono il bottone di colore `#0066cc`, la barra nera, le sezioni alte
80 px e i titoli a peso 700.

Su un sito vetrina DenkiCode valgono anche `processo-siti` e le direttive dei
siti: le foto vere del cliente, la sua personalità e un racconto allo scroll.
Lo stile Apple decide spazio, tipografia e misura, non il contenuto.

## Token misurati

| Ruolo | Valore | Nota |
|---|---|---|
| Testo | `#1d1d1f` | pieno, mai trasparente |
| Testo secondario | `#6e6e73` | |
| Testo terziario, introduzioni grigie | `#86868b` | 3,6:1: solo testo da 21 px in su |
| Fondo | `#ffffff` | |
| Fascia alternata | `#f5f5f7` | |
| Fondo scuro | `#000000`, poi `#161617` e `#1d1d1f` | testo `#f5f5f7` |
| Bottone primario | `#0071e3`, hover `#0076df`, premuto `#006edb` | testo bianco 4,7:1 |
| Link e bottone secondario | `#0066cc` | il secondario ha bordo e testo di questo colore |
| Link su scuro | `#2997ff` | |
| Linee | `rgba(0,0,0,.16)`, `#d2d2d7` | |
| Barra in alto | trasparente in cima, poi `rgba(250,250,252,.8)` con `saturate(180%) blur(20px)` | alta 44 px da 834 px in su, 48 px sotto |
| Focus | contorno 2 px `#0071e3`, distanza 3 px | |
| Capsula | `border-radius: 980px` | |
| Raggi | tile 18 px; card e bento 28 px; immagini nelle card 8 px | |
| Ombre | nessuna su bottoni, barre e card | |

## Spazio e misure

| Cosa | Computer (da 1069 px) | Tablet (735-1068 px) | Telefono (fino a 734 px) |
|---|---|---|---|
| Spazio sopra e sotto una sezione | 160 px | 128 px | 96 px |
| Spazio fra testata e contenuto | 80 px | 64 px | 48 px |
| Colonna del testo | 980 px | 692 px | 87,5 % |
| Contenitore largo | 1260 px | | 420 px |
| Gap del bento | 20 px | 20 px | 18 px |
| Padding delle card del bento | 40 px | 40 px | 30 px |
| Gap fra i tile della home | 12 px | 12 px | 12 px |

I breakpoint veri sono 734 e 1068 px (con 735 e 1069 come minimi), più un
`min-width: 1441px`. Il valore 1440 citato in giro non esiste.

## Tipografia

Apple carica SF Pro dai suoi server; noi usiamo lo stack di sistema di
`apple.css`. Il corpo resta a 17 px su tutte le larghezze. I titoli hanno peso
600, i sottotitoli 400.

Formato: dimensione / interlinea in px / tracking in em.

| Ruolo | Computer | Tablet | Telefono |
|---|---|---|---|
| Titolo di pagina | 80 / 84 / -0,015 | 64 / 68 / -0,009 | 48 / 52 / -0,003 |
| Titolo di un tile o di una sezione | 56 / 60 / -0,005 | 48 / 52 / -0,003 | 32 / 36 / +0,004 |
| Titolo di sottosezione | 48 / 52 / -0,003 | 40 / 44 / 0 | 32 / 36 / +0,004 |
| Titolo di card | 32 / 36 / +0,004 | 28 / 32 / +0,007 | 24 / 28 / +0,009 |
| Etichetta sopra il titolo | 28 / 32 / +0,007 | 24 / 28 / +0,009 | 21 / 25 / +0,011 |
| Sottotitolo | 28 / 32 / +0,007 | 24 / 28 / +0,009 | 19 / 23 / +0,012 |
| Introduzione di sezione | 21 / 29 / +0,011 | 21 / 29 / +0,011 | 19 / 27 / +0,012 |
| Corpo | 17 / 25 / -0,022 | uguale | uguale |
| Corpo ridotto | 14 / 20 / -0,016 | uguale | uguale |
| Didascalia, note legali | 12 / 16 / -0,01 | uguale | uguale |

**Il tracking cambia segno.** È negativo sopra i 48 px, zero a 40 px e positivo
fra 19 e 32 px. Mettere -0,02em su tutti i titoli è l'errore più visibile delle
imitazioni. Questi valori valgono per il SF Pro caricato da Apple; con il font di
sistema conviene applicare solo i valori negativi dei titoli da 48 px in su e
guardare il risultato su un Mac.

Apple controlla gli a capo dei titoli con uno spazio non divisibile prima
dell'ultima parola (`&nbsp;`) e con una larghezza massima in `em`.

## Composizione

- **Un'idea per sezione.** Ogni capitolo ha un'etichetta di una parola
  («Design», «Prestazioni»), un titolo che dice una cosa sola, un'immagine larga
  e un'introduzione breve.
- **Prima il testo, poi il prodotto.** Nei tile il titolo, il sottotitolo e due
  azioni stanno in alto, e il prodotto è ancorato al fondo. Il testo non copre
  il prodotto.
- **Ritmo chiaro.** La pagina è bianca con una fascia `#f5f5f7` ogni due o tre
  capitoli. Il nero è riservato a un prodotto o a un blocco, e non si alterna a
  ogni sezione. Il piè di pagina è chiaro.
- **Bento.** Due colonne con gap di 20 px, raggio 28, card bianche sulla fascia
  `#f5f5f7` e nessun colore d'accento. La griglia alterna una card alta e due
  basse.
- **Eroe.** Contiene il nome del prodotto, una frase, due azioni (il bottone
  pieno «Acquista» e il link «Scopri di più ›») e un'immagine. Non contiene
  liste di funzioni né tre bottoni.
- **Colore di campagna.** L'unica nota di colore è un gradiente leggero dietro
  l'eroe, legato al prodotto. Non si ripete nelle altre sezioni.

## Movimento

- Il testo entra con una dissolvenza e uno scorrimento di 4-10 px in 0,4-0,5 s,
  quando la sezione arriva all'85 % dell'altezza della finestra. Non c'è una
  cascata lenta.
- I video sono muti, partono una volta sola quando entrano nella vista e hanno
  un'immagine di partenza e una di arrivo. Non seguono lo scroll.
- Sulle tre pagine misurate non ci sono canvas, `animation-timeline` o scene
  bloccate lunghe.
- Le card al passaggio del mouse si ingrandiscono dell'1,6 % (`scale(1.0161)`)
  in 0,3 s, e solo sui dispositivi senza tocco.
- La curva più usata è `cubic-bezier(.4, 0, .6, 1)` fra 240 e 320 ms. Con Riduci
  movimento restano le immagini ferme.

Su un sito DenkiCode l'equivalente leggero è un `IntersectionObserver` con
`opacity` e `translateY(10px)` in 0,45 s. Il racconto allo scroll di
`processo-siti` resta obbligatorio, ma con questa misura.

## Testi

- I titoli sono corti: due-cinque parole nella home, una frase con il punto.
- I paragrafi hanno due-tre frasi, e i numeri sono concreti e vicini all'unità
  di misura («fino a 18 ore»).
- In italiano Apple dà del tu, e i bottoni sono «Acquista», «Confronta»,
  «Scopri di più».
- Apple usa spesso tre frasi brevi di fila; la voce DenkiCode vieta gli elenchi
  da tre, quindi qui si usa con parsimonia.

## Gli errori delle imitazioni

- Tracking negativo su tutti i titoli, e titoli a peso 700-800.
- Corpo a 16 px, nero puro sul testo, testo semitrasparente.
- Barra nera o piena, invece che trasparente e poi di vetro.
- Bottoni con ombra, gradiente o raggio piccolo.
- Un solo azzurro per bottoni e link.
- Card con ombra, bordo e raggio da 12 px.
- Sezioni separate da 60-80 px invece di 128-160.
- Nero e bianco alternati a ogni sezione.
- Scroll bloccato e sequenze di fotogrammi.
- Carosello con frecce enormi e puntini colorati (quelli veri stanno in una
  capsula traslucida).
- Tema scuro legato al sistema che inverte la pagina: Apple sceglie il tema
  sezione per sezione. In `apple.css` si fa con `class="theme-dark"` su una
  sezione.

## Il blocco CSS di partenza

Si aggiunge a `apple.css`, che dà già colori, font e vetro.

```css
:root { --section-pad: 160px; --content: 980px; --content-wide: 1260px; }
@media (max-width: 1068px) { :root { --section-pad: 128px; --content: 692px; } }
@media (max-width: 734px) { :root { --section-pad: 96px; --content: 87.5%; } }

body { font: 400 17px/25px var(--font); background: var(--bg-surface); }
.section { padding-block: var(--section-pad); }
.section.alt { background: var(--bg-page); }
.content { width: var(--content); margin-inline: auto; }
.headline { font: 600 56px/60px var(--font); letter-spacing: -.005em; margin: 0; }
.intro { font: 400 21px/29px var(--font); color: var(--label-2); }

.pill { display: inline-block; padding: 11px 21px; border: 1px solid transparent;
        border-radius: 980px; font: 400 17px/1.18 var(--font);
        background: var(--accent); color: var(--on-accent); text-decoration: none; }
.pill:hover { background: var(--accent-hover); text-decoration: none; }
.pill.secondary { background: transparent; color: var(--link); border-color: var(--link); }
.more::after { content: " ›"; } /* «Scopri di più ›» */

.bento { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 20px; }
.bento > * { background: var(--bg-surface); border-radius: var(--radius-xl); padding: 40px; }
@media (max-width: 734px) { .bento { grid-template-columns: 1fr; gap: 18px; } .bento > * { padding: 30px; } }
```
