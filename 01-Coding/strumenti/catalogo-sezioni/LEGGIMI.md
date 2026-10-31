---
type: risorsa
riga: Catalogo delle sezioni approvate per i siti vetrina, 14 pezzi parametrici su token.css da copiare nel sito nato dallo starter.
updated: 2026-10-31
source: claude
verificato: 2026-10-31
tags: [siti, catalogo, starter, strumenti, sezioni]
---

# Catalogo delle sezioni approvate

Un sito vetrina nuovo parte da queste sezioni invece che da zero. Nicola l'ha
deciso il 31/10/2026 («Sì, cambialo», in [[direttive-siti]]). Ogni sezione
viene da un sito che Nicola ha approvato e porta in testa da dove viene e cosa
ne ha detto lui. I colori, i caratteri e le foto restano del cliente: le
sezioni li leggono tutti da `token.css`, e nessuna contiene un colore o un font
scritto a mano.

Lo usa la testa che costruisce il sito con `/nuovo-sito`, dopo che Nicola ha
scelto una delle tre tavole di direzione. Il catalogo dà la struttura e
l'idraulica delle sezioni; la metafora, la spina dello scroll e l'apertura del
sito si decidono ogni volta sul cliente.

## Le sezioni

I commit sono quelli in cui il pezzo è stato preso, e ognuno era l'ultimo
commit del suo repository il 31/10/2026.

| Sezione | Da dove viene | Cosa dice Nicola | Foto che servono | JS |
|---|---|---|---|---|
| `barra-fissa` | Groavel, `a6a1751` | «da telefono la navbar non va bene perche è appiccicata al titolo» (20/10): menu a parte sotto 1024 px, 16 px minimo sopra il titolo | il logo, quadrato, ≥96 px | sì, facoltativo |
| `hero-foto-laterale` | Groavel, `a6a1751` | «con quello siamo sulla strada giusta» (30/10); il nome come titolo e una frase sotto (14/09) | 1 verticale 4:5 ≥1080 px; logo PNG 512 px facoltativo | no |
| `prossima-uscita` | Groavel, `a6a1751` | la locandina resta intera, senza parallasse (27/10); «meno testo» (29/10) | 1 locandina 1:1 o 4:5 ≥1080 px; badge 320 px facoltativo | no |
| `scena-tappe` | Groavel, `a6a1751` (la spina) | sul telefono ogni tappa ha uno schema suo (26/10); foto cambiate con opacità, niente will-change (26/10, 27/10) | 1 per tappa ≥1080 px, da 3 a 5 | sì |
| `righe-foto-piccole` | Groavel, `a6a1751` | foto piccole accanto al testo, «non riesco a leggere il testo e vedere la foto insieme» (06/10) | 1 per riga ≥1080 px, 4:5 o 1:1 | no |
| `galleria-irregolare` | Groavel, `a6a1751` | «da telefono togline giusto un paio in modo che non sembri un muro di foto» (26/10) | 6 ≥1080 px: 3 orizzontali 3:2, 3 verticali 4:5 | no |
| `contatto-finale` | Groavel, `a6a1751` | niente di suo su questa sezione; il sito intero «sulla strada giusta» (30/10) | nessuna | no |
| `piede-firma` | Groavel, `a6a1751` | la firma DenkiCode resta su ogni sito ([[convenzioni]]) | il logo ≥192 px | no |
| `passaggio-curva` | Groavel, `a6a1751` (le cuciture) | «metti gli sfondi in modo che si mischino tra loro con delle righe disegnate colorate» (26/10), poi «meglio» | nessuna | no |
| `sedi-elenco` | NG Barber, `648187b` | «NG Barber e Fiftynine passano, gli altri no» (il metro) | 1 per sede ≥1080 px, 4:5 | sì |
| `orari-adesso` | Fiftynine, `16b3492` | il metro; un sito con orari dice prima di tutto se è aperto adesso | nessuna | sì |
| `recensioni-voto` | Fiftynine, `16b3492` | «mancano delle belle recensioni scritte affianco alle loro recensioni su google» (18/09) | nessuna | no |
| `contrari-scorrevoli` | Mikuma giro 7, `38bb1bb` | «per il resto mi piace molto» (11/09) | nessuna | sì, GSAP |
| `servizio-tre-foto` | Davide Milan, `b39dde4` | «va bene» sul giro 1 (06/10) | 3 dello stesso lavoro ≥1080 px, una verticale 3:4 | no |

Ogni sezione sta in `sezioni/<nome>.html` e `sezioni/<nome>.css`, più
`sezioni/<nome>.js` dove la tabella dice sì. Il commento in testa all'HTML dice
anche quali testi vanno scritti e cosa è stato tolto rispetto al sito
d'origine.

Il JS è sempre un'aggiunta: senza script, in `?cattura` e con
`prefers-reduced-motion` ogni sezione è già completa. Solo
`contrari-scorrevoli` usa GSAP e ScrollTrigger, gli stessi che lo starter carica
da CDN; gli altri usano IntersectionObserver o niente.

## I file comuni

| File | Cosa contiene |
|---|---|
| `token.css` | Le variabili che ogni sezione legge: campi di sfondo, inchiostri, accento, caratteri, scala tipografica, raggio, spazi. Ogni valore è marcato `TODO` e porta come esempio quello di Groavel giro 4. |
| `comuni.css` | La grammatica che le sezioni condividono, presa da Groavel: titoli, bottoni, link con freccia, foto, striscia di dati, campi, superfici del browser (selezione, barra di scorrimento, focus). Contiene anche `.manca`, il segno per un dato che il cliente non ha ancora dato. |
| `monta-prova.py` | Rimonta `prova.html` con tutte le sezioni. Si rilancia dopo ogni modifica. |
| `prova.html` | Tutte le sezioni con i valori di Groavel e riquadri grigi al posto delle foto, con le proporzioni giuste. Serve solo a verificare il catalogo. |

## Come si usa

1. Si crea il sito dallo starter: `python3 01-Coding/strumenti/nuovo-sito.py <nome>`.
2. Si copiano nel sito `token.css`, `comuni.css` e i file delle sezioni scelte,
   per esempio in `assets/`. Nella testa si caricano in quest'ordine:
   `base.css` dello starter, `token.css`, `comuni.css`, poi i CSS delle sezioni.
   Gli script delle sezioni vanno in fondo al body, dopo GSAP e dopo il boot
   dello starter, che accende `.rivela`.
3. Si compila `token.css` con i valori della tavola scelta da Nicola: colori,
   caratteri, scala. I contrasti si rimisurano su ogni campo.
4. Si incolla l'HTML delle sezioni nell'ordine del contratto
   (`direzione/contratto.md`). La barra va subito dentro `<body>`, il piede dopo
   `</main>`. Dove il campo di sfondo cambia ci va un `passaggio-curva`, con le
   classi del campo che esce e di quello che entra.
5. Si sostituiscono tutti i `TODO`: testi, link, percorsi delle foto, larghezze
   e altezze vere delle foto. Un dato che il cliente non ha dato resta in
   `<b class="manca">`, che si vede in pagina: il sito non esce finché ce n'è uno.
6. Si passa ai cancelli: `python3 01-Coding/strumenti/cancelli-sito.py ~/lavoro/<nome>-site`.

Un sito non usa tutte le sezioni. Due siti che escono con le stesse sezioni
nello stesso ordine e lo stesso campo hanno saltato la direzione.

## Cosa non sta nel catalogo, e perché

- **L'apertura e la spina dello scroll del sito.** Nascono dalla metafora del
  cliente (la ruota di Groavel, il globo di NG Barber, la pellicola di Davide
  Milan) e lo starter ha già il posto dove scriverle. `scena-tappe` è una spina
  possibile, non quella di ogni sito.
- **I disegni nati da un sito solo.** Il globo di NG Barber è il loro logo
  ridisegnato in SVG («il logo non si ridisegna», 16/09 e 19/09); la forma del
  percorso di Groavel è ricalcata dalla traccia Strava di quell'evento; il
  marchio di Mikuma che si apre e la linea di taglio sono il suo logo. Nessuno
  dei tre si parametrizza.
- **Gli sfondi di Groavel**: le isoipse, la ghiaia, la grana e i numeri giganti
  al chilometro. Sono la carta topografica di un'attività in bici, e su un altro
  cliente sarebbero decorazione.
- **Il foglio di provino di Davide Milan**, la seconda schermata fissata che
  sceglie tre foto: è il mestiere del fotografo, e da computer mette sei foto in
  fila.
- **La griglia 4x2 di Mikuma** in bianco e nero, perché sono quattro foto di
  fila (26/10), e **i lavori di NG Barber con la didascalia** sotto ogni foto
  (17/09 e 21/09).
- **I nastri di parole che scorrono** (il marquee dei servizi e il «Book now» di
  NG Barber): bocciati il 16/09, «togli il carosello di frasi».
- **La numerazione dei capitoli** («01 — Portfolio», «02 — Dove siamo») e le
  etichette sopra i titoli: bocciate il 07/10.
- **L'hero a due colonne di Mikuma con il marchio che entra ruotando**, che a
  Nicola piace: nel primo schermo mette il logo e non una foto, e dal 29/10
  l'apertura di sola scritta o di solo logo non passa.

## Come si verifica

Si serve la cartella `01-Coding/strumenti/` su 127.0.0.1, perché `prova.html`
legge `base.css` e la firma da `../starter-sito/`:

```bash
python3 01-Coding/strumenti/catalogo-sezioni/monta-prova.py
python3 -m http.server 8793 --bind 127.0.0.1 --directory 01-Coding/strumenti
node 01-Coding/strumenti/cancelli-telefono.mjs http://127.0.0.1:8793/catalogo-sezioni/prova.html
```

Misure del 31/10/2026: nessun controllo bloccante fallito a 375×812 con la CPU
rallentata 4 volte, scroll con p95 di 17 ms, zero elementi con `will-change`,
nessuno scorrimento laterale a 1440 e a 375, console pulita. Gli avvisi attesi
sono tre: i passaggi contano come disegni inline, la pagina ha più elementi di
un sito vero perché monta tutte le sezioni, e il punto di «aperto adesso» è
un'animazione infinita. `controlla-slop.py` blocca sui `TODO`, come deve: un sito
con un segnaposto rimasto non si consegna.

## Collegamenti

[[direttive-siti]] · [[pipeline-siti]] · [[processo-siti]] · [[sito-groavel]] ·
[[sito-ngbarber]] · [[sito-fiftynine]] · [[sito-mikuma-dogs]] ·
[[sito-davidemilan]] · [[convenzioni]]
