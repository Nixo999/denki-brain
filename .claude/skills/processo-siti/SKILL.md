---
name: processo-siti
description: Come si costruisce un sito vetrina DenkiCode. Da usare prima di scrivere una riga di HTML per un sito cliente o una bozza. La direzione la propone un operatore su Opus che ha letto le skill di design, il direttore sceglie e non scrive codice. Impeccable guida la costruzione, lo scroll-telling e la grafica inventata sono obbligatori. Non vale per OperO e DenkiShift, dove comanda il CLAUDE.md del repo.
---

# Il processo, in ordine

Il metro sono **NG Barber** e **Fiftynine**. Non si copiano: si eguaglia il
livello. Cos'hanno che i siti di settembre non hanno, misurato:

| | NG Barber | Fiftynine | Mikuma | Lobidù | Da Caterina |
|---|---|---|---|---|---|
| `<svg>` inline | 8 | 10 | 4 | 0 | 0 |
| scroll-telling (GSAP/ScrollTrigger) | sì | sì | no | no | no |

**Grafica inventata e racconto allo scroll.** Le pagine che piacciono hanno un
globo che gira, una mappa con le città che pulsano, una tenda che scorre, una
goccia che si stacca — roba disegnata, non foto messe in griglia — e una storia
che si srotola mentre scendi. Quelle che non piacciono sono impaginati con
rivelazioni in entrata.

## 0. Il direttore raccoglie, non decide

Regola dal 11 settembre 2026, e **ribalta quella di ieri**. Prima il direttore
sceglieva la metafora prima che qualcuno avesse letto una skill di design: la
decisione creativa stava nel modello che di design non aveva letto niente, e
l'operatore diventava un esecutore. Non si fa più.

Il direttore raccoglie e verifica: profilo Instagram, logo, vecchio sito, le
parole loro, gli orari, il ritmo del mestiere, gli oggetti fisici del posto, e
**cosa non c'è** (prezzi, recensioni, indirizzo: si dichiara, non si inventa).
Scrive tutto nella nota di progetto. **Le foto si scaricano subito** e si
controllano (passo 1). Poi scrive `PRODUCT.md` con `impeccable init`: è la
verità di prodotto, non la direzione.

Il direttore **non** sceglie metafora, palette, font o sezioni.

## 1. Le foto — si controllano prima, non dopo

```bash
sips -g pixelWidth -g pixelHeight assets/img/*.jpg | paste - - -
```

**Minimo 1080 px sul lato lungo.** Da Instagram si prendono i post del feed, non
le copertine dei Reel: quelle sono 360 px e su Retina rendono a metà. Su Mikuma
tutte le foto erano 360 px, e si vede.

Se dopo il controllo il materiale non regge — sotto 1080, rapporti scombinati,
fotogrammi di video, dominanti diverse — ci sono due strade, e si **dichiara
quale**:

1. **Si chiedono le foto buone al cliente.** È anche un motivo per scrivergli.
2. **Si disegna un sito che non dipende dalle foto**: grafica inventata,
   tipografia, colore. NG Barber ha otto foto e regge sul globo e sulla mappa.

Quello che non si fa mai è impaginare foto brutte e sperare. Un trattamento
solo per tutte (taglio, grana, duotone, cornice) o nessuno.

## 2. La direzione la propone chi ha letto le skill

Il direttore lancia **un operatore di direzione** (agente `operatore`, Opus).
Quell'operatore carica la catena — `impeccable context`, poi
`reference/new-work.md`, `design-taste-frontend`, la skill di stile — e **torna
con due o tre mondi visivi**, non con un sito.

Ogni mondo, in dieci righe:

- **La metafora**, presa dal mestiere vero. Se si potrebbe spostare su un altro
  cliente non è quella giusta.
- **La spina dello scroll**: cosa racconta la pagina mentre scendi, in tre
  battute. È la cosa che rende NG Barber NG Barber.
- **I tre o quattro pezzi di grafica inventata** che nascono da quella metafora.
- Palette e famiglia tipografica, con i valori.

**Il direttore sceglie uno** e può chiedere di incrociarne due. Da lì, e solo da
lì, parte la costruzione. Il mondo scelto si scrive nella nota di progetto col
seed di impeccable, o non è ripetibile.

## 3. La costruzione — impeccable al centro

L'operatore che costruisce carica, in quest'ordine:

0. `01-Coding/stack/direttive-siti.md` — quello che è già stato bocciato.
1. `impeccable context` → `reference/new-work.md` per il mondo scelto.
2. `reference/craft-floor.md` **immediatamente prima di toccare la UI**. È il
   pavimento di qualità e la lista dei divieti assoluti.
3. La skill di stile, **una sola**: `high-end-visual-design`, `minimalist-ui` o
   `industrial-brutalist-ui`. Due si contraddicono.
4. `ui-ux-pro-max` per pescare un valore preciso, non una direzione.
5. `voce-denkicode` sul copy, prima della review.

Modo di impeccable: **Persuade**. È una vetrina, il visitatore deve decidere e
agire.

Poi il **passo di carattere**, che è quello che mancava: `bolder` se la pagina
è timida, `delight` per i momenti memorabili, `animate` sulla spina dello
scroll, `overdrive` quando il mondo lo chiede. Su un impaginato educato si
passa da `bolder`, non si consegna.

**Nessun giro parte senza catena.** Su Mikuma tre operatori su sette non hanno
caricato niente, e il giro finito online è uno di quelli. Un giro che tocca la
UI carica almeno `impeccable context` e `craft-floor`.

## 4. Lo scroll-telling non è un extra

Una vetrina ha una spina che si srotola: pin, parallasse sui layer immagine,
elementi che entrano in sequenza, un momento che sorprende. GSAP con
ScrollTrigger, oppure `animation-timeline: view()` dove basta.

⚠️ **Togliere GSAP non è pulizia.** Su Mikuma è stato rimosso al giro 4 con la
motivazione «restavano per un pin che non esiste più»: il pin *era* il racconto.
Se una direzione cancella la spina, quella direzione è finita e si torna al
passo 2.

Le trappole di motion in [[trappole]] dicono **come** farlo senza rompere le
catture. Non dicono di non farlo.

## 5. Verifica misurata, e poi guardata

1440×900 e 375×812, più i bordi di ogni media query. Overflow zero, contrasti
AA, console pulita, pagina completa senza JS.

Poi **si guarda**, e si guarda la pagina vera, non solo `?cattura`: in cattura
la motion è spenta per costruzione, quindi da lì non si giudica mai né
l'apertura né la spina. Catture a pagina intera a 1440 e a 375, e si guardano.

## 5-bis. Il livello, misurato — e le direttive già date

```bash
python3 01-Coding/strumenti/controlla-sito.py ~/lavoro/<cartella>
```

Misura grafica inventata, racconto allo scroll, apertura, foto, firma e
sbarramenti. **NG Barber e Fiftynine passano 8 su 8**: è tarato su quelli. Se
esce 1 il sito non si pubblica.

E si legge `01-Coding/stack/direttive-siti.md`, che raccoglie ogni bocciatura di
Nicola con la regola che ne è uscita. **Quel file cresce e non si accorcia**: è
il meccanismo per cui i siti migliorano invece di oscillare. Un sito nuovo non
può ripetere niente di quello che c'è scritto lì.

## 6. Finish review e consegna

`impeccable polish` prima di chiudere, poi la finish review: è il passo che ha
trovato diciotto didascalie false e un prezzo mancante. **Le didascalie si
scrivono guardando la foto, non il nome del file.**

Netlify, i **tre sbarramenti restano** finché il sito non è suo, e li toglie il
direttore tutti e tre insieme. Poi la riga in `01-Coding/registro-interventi.md`
— chi, quando, progetto, repository, database — e push.

## Dove questo processo NON vale

OperO e DenkiShift: nei loro repo comanda il `CLAUDE.md` del repo.
