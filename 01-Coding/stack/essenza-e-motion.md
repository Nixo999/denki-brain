---
type: risorsa
riga: Essenza da Instagram, metafora, spina dello scroll, grafica inventata e foto minime 1080px. Il metro misurato sono NG Barber e Fiftynine.
updated: 2026-09-11
verificato: 2026-09-11
source: denkicode
tags: [siti, design, motion, instagram, essenza]
---

# L'essenza del cliente, e la motion che la serve

Chiesto da Nicola il 10 settembre 2026: «voglio siti originali, sempre
un'animazione all'avvio, tante animazioni particolari per far sembrare il sito
vero, e voglio essere sorpreso come su NG Barber e Fiftynine».

Non è una lista di effetti. È una regola sola: **ogni sito ha una metafora
sola, presa dal mestiere vero del cliente, e la motion serve quella.** Un sito
con dieci animazioni scelte da un catalogo sembra generato. Un sito con quattro
animazioni che parlano tutte della stessa cosa sembra vero.

## Il metro, misurato

Aggiornato l'11 settembre 2026 confrontando i sei siti fatti finora.

| | NG Barber | Fiftynine | Mikuma | Lobidù | Da Caterina |
|---|---|---|---|---|---|
| `<svg>` inline | 8 | 10 | 4 | 0 | 0 |
| scroll-telling | sì | sì | no | no | no |
| foto, lato lungo | 1350 px | 1100 px | **380 px** | — | 640 px |

Le due che piacciono a Nicola hanno **grafica inventata** e **una storia che si
srotola allo scroll**. Le altre sono impaginati con rivelazioni in entrata, su
foto piccole. Non è una questione di gusto: è la differenza fra una pagina
disegnata e una pagina compilata.

## 1. Cosa si porta via da Instagram, prima di disegnare

Si scrive in `01-Coding/progetti/<slug>.md` **prima** di aprire una skill di
design. Se non è scritto, non è stato guardato.

| Cosa | Perché serve |
|---|---|
| I colori veri, campionati dal logo o da una foto | `#e03020` di Da Caterina è uscito da uno script Swift sul pixel, non da un'ipotesi |
| Cosa fotografano, e come | Da Caterina montava i cani in scene: spiaggia, caramelle, nave. È diventato l'album delle figurine |
| Le parole loro | Caption, bio, come chiamano le cose. Il copy del sito parla la loro lingua, non la nostra |
| Il ritmo del mestiere | Orari, giorni di chiusura, il momento pieno della giornata |
| Gli oggetti fisici del posto | La tenda del bar, l'insegna, la poltrona, il bancone |
| Cosa NON c'è | Niente recensioni, niente prezzi: si dichiara, non si inventa |

Le foto si scaricano nella stessa sessione: gli URL Instagram scadono in giorni.

## 2. La metafora — una, scritta, prima del codice

Una riga nella nota di progetto, e tutto il resto discende da lì.

- **Fiftynine**: il bar come tenda a righe e come giornata. La riga della tenda
  scorre all'infinito, il pallino «adesso aperto» pulsa sugli orari veri, la
  giornata è un binario con un cursore che dice a che punto siamo.
- **NG Barber**: il barbiere come grana, ottone e goccia. La grana si muove a
  `steps(10)`, il globo gira in 140 secondi, il suggerimento di scroll è una
  goccia che si riempie e si stacca, le città servite pulsano su una mappa.
- **Da Caterina**: l'album delle figurine. I cani ritagliati si attaccano uno
  alla volta e derivano con lo scroll.

Nessuna delle tre si potrebbe spostare su un altro cliente. È quello il test.

## 2-bis. La spina dello scroll e la grafica inventata

Due cose obbligatorie su ogni vetrina, e sono quelle che mancavano a settembre.

**La spina.** Cosa racconta la pagina mentre si scende, in tre battute. NG
Barber è scroll-telling sul globo del logo: il commit si chiama così. Fiftynine
è la giornata che avanza su un binario. Si costruisce con GSAP e ScrollTrigger,
o con `animation-timeline: view()` dove basta.

⚠️ **Togliere GSAP non è pulizia.** Su Mikuma è stato rimosso al giro 4 perché
«restava per un pin che non esiste più»: il pin *era* il racconto, ed è uscito
un impaginato. Se una direzione cancella la spina, quella direzione è finita.

**La grafica inventata.** Tre o quattro pezzi disegnati che nascono dalla
metafora, non foto messe in griglia: il globo che gira in 140 secondi, la mappa
con le città che pulsano, la tenda a righe che scorre, la goccia che si stacca.
Sono `<svg>` inline e CSS. Una pagina con zero SVG inventati è una pagina che
dipende interamente dalle foto — e le foto spesso non reggono.

## 2-ter. Le foto — si controllano prima di progettare

```bash
sips -g pixelWidth -g pixelHeight assets/img/*.jpg | paste - - -
```

**Minimo 1080 px sul lato lungo.** Da Instagram si prendono i post del feed, non
le copertine dei Reel: quelle sono 360 px, e mostrate a ~386 px CSS rendono a
metà risoluzione su uno schermo Retina. Su Mikuma erano tutte così.

Se il materiale non regge — sotto 1080, rapporti scombinati, fotogrammi di
video, dominanti diverse — due strade, e si **dichiara quale**:

1. **Chiedere le foto buone al cliente.** È anche un motivo per scrivergli.
2. **Disegnare un sito che non dipenda dalle foto.** NG Barber ne ha otto e
   regge sul globo, sulla mappa e sulla grana.

Non si impaginano foto brutte sperando che passino. Un trattamento solo per
tutte — taglio, grana, duotone, cornice — oppure nessuno: quattro foto a
quattro rapporti e quattro dominanti leggono come disordine, non come ritmo.

## 3. L'apertura — sempre, e sempre diversa

**Ogni sito ha un'animazione d'avvio.** È il primo secondo ed è quello che
decide se il sito sembra vero. Non è un fade generico: è la metafora che entra
in scena.

Vive in CSS (`.js:not(.cattura) …{animation:… both}`), così lo stato a riposo è
già quello finale: senza JS, in cattura o con `reduced-motion` la pagina è
completa. Se serve una timeline GSAP, il sipario ha il timer di sicurezza:
`rAF` è fermo nei tab in background e un sipario resterebbe eterno.

## 4. «Tante animazioni particolari» — cosa vuol dire davvero

Quattro tipi, e servono tutti e quattro perché il sito respiri:

1. **Una che risponde a un dato vero.** Aperto/chiuso calcolato dagli orari, il
   punto della giornata, il conto alla rovescia al servizio. È quella che fa più
   effetto e costa meno: il sito sa qualcosa.
2. **Un ambiente che non si ferma mai.** Grana, tenda che scorre, globo che
   gira. Lento, in loop, di sottofondo. Dice che la pagina è viva anche ferma.
3. **Un momento autoriale, uno solo.** Le figurine che si attaccano, la goccia
   che si stacca. Se ce ne sono tre, non ce n'è nessuno.
4. **Le rivelazioni allo scroll**, sfalsate, che sono la base e non il piatto.

⛔ Quello che fa sembrare il sito generato: fade-up identico su tutto, marquee
messo perché fa moderno, hover-lift su ogni card, numeri grandi animati che
contano, eyebrow sopra ogni titolo.

⛔ **I numeri che impegnano non si animano.** Un prezzo in conteggio mostra una
cifra falsa per tutta la durata, e una cattura la fotografa: «CHF 34» per un
brunch a 39. Pagata su [[sito-osteria-tarilli]].

## 5. Le regole tecniche stanno già altrove

`assets/base.css` dello starter porta dentro il reset, `--vh`, `.cattura`, le
rivelazioni col fallback solo a scheda nascosta e `reduced-motion`. Non si
riscrivono: si eredita. Il resto delle trappole di motion è in [[trappole]],
sezione «GSAP e motion».

## Collegamenti

[[processo-siti]] · [[trappole]] · [[convenzioni]] · [[design-frontend]]
