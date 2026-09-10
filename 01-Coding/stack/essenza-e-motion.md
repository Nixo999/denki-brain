---
type: risorsa
riga: Come si cava l'essenza di un cliente da Instagram e come diventa metafora e motion. Il metro sono NG Barber e Fiftynine.
updated: 2026-09-10
verificato: 2026-09-10
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
