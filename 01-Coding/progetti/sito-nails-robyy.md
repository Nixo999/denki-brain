---
type: progetto
riga: Roberta @nails.robyy, nail artist e educator a Brescia: bozza online su nailsrobyy.netlify.app dal 14/9, mondo A «la sezione quotata», 8/8, sbarramenti verificati.
status: attivo
client: nails-robyy
stack: html-css-js
started: 2026-09-13
deadline:
updated: 2026-09-14
source: claude
verificato: 2026-09-14
tags: [sito, bozza, unghie, brescia, corsi]
---

# Sito nails.robyy — online, mondo «la sezione quotata»

Bozza **attesa**: Patrick le ha scritto in DM il 13 settembre 2026 e lei ha
risposto «Ciao ok vediamo». Repo `~/lavoro/nailsrobyy-site`, dallo starter
(`nuovo-sito.py`), commit `9ec160c`, poi `Nixo999/nailsrobyy-site` (privata).

**Il [[processo-siti]] è stato percorso intero**, passi 0-6, nella notte fra il
13 e il 14 settembre: direttore su Fable, sette operatori su Opus in sequenza.

## Chi è, verificato sul profilo il 13 settembre 2026 (senza login)

`@nails.robyy`, nome del profilo «ROBERTA || Nail Artist & Educator Brescia».
**1.430 follower, 394 seguiti, 112 post** — la griglia pubblica ne mostra 12.

Bio, parola per parola:

```
🎓 In continua evoluzione
✨ Perfezione tecnica & crescita costante
💅 Struttura • Refill correttivo • Corsi
📍 Brescia e provincia
💌 Scrivimi in DM
```

**Nessun link in bio. Nessun sito**: verifica del banco del 12/9, «Roberta Nail
Artist» Brescia dà 0 risultati sui motori e nessun dominio risponde. Storie in
evidenza: «Chi sono», «Correzioni», «📚Formazione», «💅Lavori» — dietro login,
non lette.

## Il marchio, e i colori campionati

Monogramma **«RD»** in oro, due lettere serif alte e intrecciate (la gamba della
R fa da asta della D), su campo rosa cipria pieno, con **«— NAILS —»** sotto in
maiuscoletto spaziato fra due filetti sottili. **Il tondo è il ritaglio di
Instagram: l'originale è quadrato.**

Campionato pixel per pixel sul file (`sips -s format bmp` + parsing BMP in
`python3` puro, 22.500 px letti — niente PIL, niente Swift):

| | esadecimale | come |
|---|---|---|
| rosa cipria del fondo | **`#FCE2E3`** | 17.479 px su 22.500, il 78% dell'immagine |
| oro, nucleo pieno del tratto | **`#A4804E`** | il più scuro dei 433 px «oro» (r>g>b) |
| oro, tratto medio | `#D7B590` | media dei 433, include i bordi sfumati |

⚠️ A 150 px **il lettering è tutto antialiasato sul rosa**: nessun pixel d'oro è
puro. `#A4804E` è il valore su cui costruire, `#D7B590` no.

**Il logo esiste solo a 150×150**: le varianti più grandi rispondono 403. Non si
ridisegna e non si ingrandisce. → `TODO`.

## Cosa fotografa

Sempre e solo **mani, in primo piano stretto**. Fondo bianco o grigio chiaro del
tavolo da lavoro, luce piatta da finestra, la lampada UV bianca a cupola che
entra nell'inquadratura in dodici scatti su trentacinque, i guanti neri in
nitrile della sua mano, il tappetino da lavoro stampato, un po' di polvere di
limatura sulle dita.

Molti scatti sono **laterali sul profilo dell'unghia**: è il modo in cui si
guarda una bombatura, non il modo in cui si mostra una manicure. Registro
clinico, non da centro estetico. Il suo viso non compare mai.

**Nessun colore acceso, nessuna nail art.** Nude, latte, french bianco, rosa
perlato, un lilla chiaro, e in un solo post tre puntini neri per unghia. Il
soggetto è la forma.

## Le sue parole

Struttura · apex · parallelismi · refill correttivo · copertura in Acrygel ·
one step · unghie grifotiche · unghia discendente · ripristino dell'asse ·
bombatura · controllo della direzione · «non si asseconda, si corregge
strutturalmente» · «Non seguire l'unghia, CORREGGILA» · «Scrivimi in DM».

Le due caption lunghe, per esteso:

- **p01, 3 aprile**: «Copertura su unghia naturale con correzione di unghie
  grifotiche: struttura bilanciata, apex correttamente posizionato e
  parallelismi ricostruiti per ristabilire armonia, direzione e resistenza. Hai
  anche tu unghie difficili da gestire? Scrivimi in DM per una consulenza
  personalizzata». 58 like, 10 commenti, quasi tutti di **colleghe** («ti ho
  scritto in privato»).
- **p05, 24 marzo**: «Copertura in Acrygel: il perfetto equilibrio tra
  flessibilità e stabilità. Una lavorazione mirata che consente di rinforzare
  l'unghia naturale senza appesantire, mantenendo una struttura sottile ma
  performante. Il controllo totale del prodotto permette una stesura uniforme,
  una perfetta gestione dei volumi e una durata impeccabile nel tempo».
- **p09, 25 gennaio**: «Refill correttivo eseguito per ripristinare struttura,
  bilanciamento e corretta architettura dell'unghia. Se vuoi imparare questa
  tecnica e portare i tuoi lavori a un livello superiore, scrivimi in privato».
- **p03, 30 marzo**: «Base latte naturale. French bianco pulito. Refill con
  correzione della struttura per un risultato armonioso e preciso».

Quattro post su dodici sono **solo hashtag**: `#corsiunghiebrescia`,
`#refillcorrettivo`, `#ricostruzionegel`, `#coperturagel`, `#corsiunghie`,
`#ricostruzioneunghie`.

## Cosa NON c'è, e non si inventa

Cognome · nome dello studio · indirizzo (solo «Brescia e provincia») · telefono ·
mail · orari · giorni di chiusura · prezzi · recensioni · foto di Roberta ·
programma, durata, sede, date e prezzo dei corsi · numero di allieve.

**Unico canale verificato: il DM di Instagram.**

## Le foto scaricate — 35 a 1440 px

Scaricate il 13 settembre 2026 in `assets/img/_orig/` (gli URL del CDN scadono in
giorni). Tutte `1440×1920` salvo dove indicato.

| file | px | cosa mostra |
|---|---|---|
| `p01a-2026-04-03` | 1440×1920 | mano di tre quarti aperta sul tavolo grigio, unghie a mandorla nude opache, la cupola della lampada UV in alto a destra, polsino di maglia lilla a coste |
| `p01b` | 1440×1920 | primissimo piano di due dita, unghia a mandorla latte con la punta più chiara, si legge la curva dell'apex di profilo |
| `p01c` | 1440×1920 | stesse dita da un altro angolo, unghia a punta ovale, sfondo nero e fascia bianca in alto |
| `p03a-2026-03-30` | 1440×1920 | mano appoggiata su un guanto nero, unghie a mandorla lunghe nude **glitterate**, anello con pietra rossa, asciugamano fucsia nell'angolo in basso |
| `p03b` | 1440×1920 | tre dita in verticale su fondo bianco lattiginoso, unghie bianco latte lucide, lembo nero sfocato dietro |
| `p03c` | 1440×1920 | mano di taglio, unghie a stiletto appuntite color latte, alone di luce bianca della lampada dietro |
| `p03d` | 1440×1920 | mano rilassata sul tavolo grigio, unghie a mandorla lunghe bianco perla, cerchio bianco della lampada in alto a destra |
| `p05a-2026-03-24` | 1440×1920 | **due mani sovrapposte**, unghie corte quadrate nude opache, due anelli d'oro, tavolo grigio e bordo bianco della lampada |
| `p08a-2026-03-13` | 1440×1920 | quattro dita di taglio, unghie corte quadrate rosa chiaro con french bianco sottile, la cupola bianca della lampada riempie lo sfondo |
| `p08b` | 1440×1920 | **una goccia di prodotto rosa in cima a un'unghia**, non ancora stesa: è la lavorazione in corso |
| `p08c` | 1440×1920 | mano tenuta da un guanto nero, unghie corte quadrate rosa cipria con lunetta bianca, due nei sul dito |
| `p08d` | 1440×1910 | primo piano lateralissimo di tre unghie a mandorla latte, si legge il parallelismo dei profili |
| `p08e` | 1440×1920 | mano poggiata su fondo bianco, unghie quadrate rosa con french bianco, un neo sul dito |
| `p09a-2026-01-25` | **1440×1440** | dita di profilo su fondo bianco, unghie lunghe a mandorla nude opache, luce bassa e grigia |
| `p09b` | **1440×1440** | stesse dita, taglio più stretto, la curva delle punte in fila |
| `p09c` | **1440×1440** | mano **coperta di polvere di limatura bianca**, unghie a stiletto lunghe nude, manica grigia, anello d'argento |
| `p09d` | **1440×1440** | dito tenuto fra due guanti neri, unghia lunga nuda vista di profilo: la bombatura è il soggetto |
| `p10a-2026-01-24` | 1440×1920 | mano distesa sul tavolo grigio, unghie lunghe a mandorla bianco perla, anello con pietra rossa, bordo bianco della lampada |
| `p10b` | 1440×1920 | **il prima**: quattro unghie quadrate cresciute, ricrescita evidente, una punta trasparente scheggiata, guanto nero dietro |
| `p10c` | 1440×1920 | mano su guanto nero coperto di polvere bianca, unghie a ballerina lunghe nude glitterate |
| `p10d` | 1440×1910 | tre dita, unghie **lilla perlato** lucide appena finite, guanto nero |
| `p10e` | 1440×1916 | un'unghia sola di profilo, lilla perlato, il dito tenuto da un guanto nero: taglio didattico sulla curva |
| `p10f` | 1440×1910 | **goccia di gel rosa in cima a un'unghia**, dita in guanto nero, tappetino chiaro stampato sotto |
| `p10g` | 1440×1920 | due dita in verticale, unghie lunghe a mandorla **lilla opaco**, pelle coperta di polvere di limatura |
| `p10h` | 1440×1920 | quattro dita di taglio su fondo bianco e grigio, unghie lunghe a mandorla rosa cipria opaco |
| `p11a-2025-09-10` | 1440×1920 | mano di taglio, unghie a ballerina **rosa antico** con **tre puntini neri** per unghia: l'unico decoro di tutto il feed |
| `p11b` | 1440×1920 | stesse unghie, taglio più stretto, i puntini neri in fila alla base |
| `p11c` | 1440×1910 | mano raccolta su fondo chiaro, unghie rosa chiaro coi puntini, bordo bianco della lampada |
| `p11d` | 1440×1911 | **due mani** sul tavolo grigio, unghie rosa coi puntini, anello d'oro sottile |
| `p12a-2025-09-01` | 1440×1920 | **il prima**: un'unghia naturale dall'alto con la ricrescita e la lamina rovinata, tappetino a righe rosa sotto |
| `p12b` | 1440×1920 | mano in lavorazione coperta di polvere bianca, unghie a mandorla nude, tappetino a righe rosa |
| `p12c` | 1440×1910 | dito tenuto da un **guanto bianco**, unghia lunga a mandorla rosa chiaro vista di profilo |
| `p12d` | 1440×1910 | stesso dito, angolo diverso, la punta nel vuoto: profilo pulito |
| `p12e` | 1440×1920 | mano su guanto bianco, unghie a mandorla **rosa glitterato**, tappetino con disegni tecnici |
| `p12f` | 1440×1920 | **due mani** una sull'altra tenute da un guanto bianco, unghie a mandorla rosa naturale, cupola della lampada in alto |

**Non utilizzabili, restano nella cartella ma fuori dal sito:**

- le 12 anteprime di griglia a 480×640 (`p01…p12-*-foto.jpg`) e la 640×640 di p09:
  superate dalle 1440;
- le **4 copertine di reel** a 361×640 — `p02` (mano in guanto nero al lavoro con
  la fresa), `p04` («Non seguire l'unghia CORREGGILA» impresso in serif bianco),
  `p06` («Copertura one step in Acrygel» impresso, due mani sul tappetino),
  `p07` («Refill correttivo in Acrygel» impresso, unghie rosa su guanto nero).
  Sono fotogrammi di video, sotto soglia, e tre su quattro hanno **una citazione
  in serif bianco impressa**. Fuori.
- `logo-profilo.jpg`, 150×150.

## Passo 1 — strada dichiarata: **1, le foto reggono**

35 file ≥1440 px sul lato lungo, contro il minimo di 1080. Rapporti omogenei:
31 verticali 3:4, 4 quadrati 1:1. Dominante unica su tutte (bianco, grigio
chiaro, nero del guanto, incarnato). **Non serve costruire un sito che prescinda
dalle foto.**

Restano due paletti che valgono comunque: la grafica inventata e la spina dello
scroll sono obbligatorie lo stesso (non è una scusa per impaginare foto in
griglia), e **un trattamento solo per tutte**.

Strada 1 non chiude il `TODO` del logo: quello resta a 150 px.

## Contesto commerciale

Riga `@nails.robyy` in `02-Sales/liste/2026-09-13-instagram-siti-brescia.csv`,
gancio 1, prodotto siti. Il DM di Patrick è **già partito** e lei ha risposto oggi
«Ciao ok vediamo». Il DM promette, testualmente: «Fai anche i corsi… un corso
senza una pagina dove iscriversi lo compra solo chi ti scrive già in chat… una
bozza del tuo sito, già fatta».

⚠️ **Quindi la bozza deve avere un posto dove iscriversi ai corsi.** È una
promessa già fatta a voce, non una nostra idea di sezione. Il posto porta al DM:
un sistema di prenotazione non esiste e non si finge.

## TODO — da chiedere a Roberta

- [ ] **Il file del logo vero**, vettoriale o almeno 1000 px. Oggi si ha 150×150.
- [ ] Cognome, e come vuole essere chiamata sul sito.
- [ ] Nome dello studio, se esiste. Indirizzo, o conferma che resta «Brescia e provincia».
- [ ] Telefono / WhatsApp / mail: c'è un canale oltre al DM?
- [ ] Orari e giorni di lavoro.
- [ ] Prezzi, o almeno se vuole che compaiano.
- [ ] **I corsi**: come si chiamano, a chi sono rivolti, durata, sede, date, prezzo,
      quante allieve ha già formato. Oggi non si sa nulla oltre l'hashtag.
- [ ] Una foto di lei al lavoro: nel feed pubblico non c'è.
- [ ] Recensioni o messaggi di clienti che possiamo citare.
- [ ] Se le storie in evidenza contengono materiale usabile (sono dietro login).

## Passo 2 — tre mondi da un operatore di direzione, 13 settembre 2026

Operatore su Opus con la catena caricata (`impeccable context`, `new-work.md`,
`design-taste-frontend`, skill di stile **`industrial-brutalist-ui`** in
modalità Swiss print: il registro suo è clinico, e la griglia svizzera con
quote e mono è l'antidoto al rosa-e-oro da template). Ha guardato dodici foto
a 1440, NG Barber e Fiftynine come metro, Nails Mania come mondo da non
ripetere. `concept-seed` degradato (nessuna rete), seed **`f39d5612`**,
indice assegnato 4 = mondo B.

- **A «La sezione quotata»** — lei guarda l'unghia di taglio: una curva sola,
  quotata (apex, asse, parallelismi, bombatura). Pin centrale: la curva ruota
  da discendente a corretta, la foto di profilo accanto fa lo stesso. Poi
  cinque profili che convergono, l'ultimo vuoto: il posto dell'allieva.
- **B «La camera di luce»** (assegnato dal dado) — la cupola della lampada,
  la pagina è il tempo sotto la luce. Dichiarato dall'operatore come il più
  spostabile su un'altra onicotecnica.
- **C «Il manuale di correzione»** — tavole didattiche numerate, richiami che
  citano le sue caption.

**Scelto A dal direttore**, sopra l'assegnato: il momento centrale è il
ripristino dell'asse, cioè il gesto che vende lei; su una che fa decoro non c'è
niente da ruotare. Palette: carta `#F4F2EE`, inchiostro `#14120F`, quota
`#8B867E`, costruzione in oro `#A4804E`, il rosa `#FCE2E3` solo come campo
pieno della fascia corsi. Archivo 900 maiuscolo per i titoli, Martian Mono
per le quote. Foto in strisce orizzontali con un trattamento unico, sotto la
quota che le descrive. Corsi subito dopo il pin, iscrizione via DM.


## Passo 3 — costruzione, 13 settembre notte

Operatore su Opus, mondo A, **copy del direttore verbatim**. `index.html`,
`assets/stile.css`, `assets/motion.js` (GSAP 3.13 + ScrollTrigger). Commit
`e106664`, `2c2df11`.

| | |
|---|---|
| grafica inventata | **11 `<svg>` inline**: la curva dell'unghia quotata, apex, asse, parallelismi, bombatura |
| foto | **14 su 35**, un trattamento unico |
| h1 | «Struttura, non decoro.» |
| quote | APEX · ASSE · PARALLELISMI · BOMBATURA |
| pin | «Unghia discendente? Non si asseconda, si corregge strutturalmente.» — parole sue |
| fascia corsi | campo rosa `#FCE2E3` pieno, iscrizione via DM |

Misurato: overflow **0 su 13 larghezze** da 320 a 1440, h1 su una riga da
**761**, **18 coppie AA** (minimo **5,14**), console vuota, **7 ScrollTrigger**
e **un pin**, `controlla-sito.py` **8/8**, `impeccable detect` **0 errori**.

## Passo 4 — catture su disco, e tre bug visti lì

Brave headless in CDP da node 22, **fette di viewport 1440×900 cucite in
Python**. Corretti sulle catture (`269140d`): l'etichetta ASSE attraversata
dalla linea, il gruppo BOMBATURA addosso al profilo, `scroll-padding-top`
mancante sotto la barra sticky.

## Passo 5 — finish review su Opus: `fix`, otto punti

`impeccable-finish-reviewer` forzato a `model: opus`. Terza battuta ridotta a
una riga sola · pin assente sotto 761 · «Posto 01/02/03» = capienza **mai
verificata** · chiusura da template centrata · riga mono sopra l'h1 = **kicker
vietato** · a 375 una linea sulla «O.» di «DECORO.» · Lavori con tre scatti
senza profilo e didascalie ripetute · «CORSI» tagliato in barra. Più il tetto:
foto mai annotate, niente cartiglio, retino usato una volta sola.

## Passo 6 — fix, tutti applicati (`26982f4`, `f9c03d9`)

- **cinque profili distinti** col retino, il quinto tratteggiato «IL TUO»:
  «Il quinto profilo è vuoto: è il posto di chi impara.»
- la correzione dell'asse gira **anche sotto 761**, come scrub senza pin
- **un solo profilo vuoto** nei corsi: la capienza inventata è uscita
- chiusura sull'asse a sinistra, quotata
- kicker via, l'informazione passa nel **cartiglio del footer**
  (NOME / LUOGO / CANALE / FOGLIO 1/1)
- la sovrapposizione a 375 era **la virgola di «STRUTTURA,»** con
  `line-height:.88`, non la «O.»
- **otto foto riscelte**, **tre annotate** con richiami SVG, callout sulla
  bombatura

Misurato dopo i fix: overflow **0 su 15 larghezze**, ScrollTrigger **7 a 1440**
e **3 a 375**, `reduced-motion` **18/18 rivelazioni e 0 trigger**,
`controlla-sito.py` **8/8**, `detect` **0 errori e 22 warning dichiarati**.

`DESIGN.md` dal documenter su Opus (`17cc5ab`). Verdetto **pass**: otto su otto
risolti, **due regressioni di finitura** — quote senza valore nella chiusura,
fascia corsi vuota per due terzi a 1440 — **chiuse con `673d6c6`**: il valore
della quota si legge a runtime, la fascia corsi va su due colonne (era
`grid-row: 1 / -1` su righe implicite, → [[trappole]]).

## Dove sta

✅ Repo **`Nixo999/nailsrobyy-site`**, privata, `main`, creata con `gh`.
✅ Sito **`nailsrobyy`** sul team `denkicode` (slug `nicola-la-rezza`),
<https://nailsrobyy.netlify.app>, HTTP 200: **tre sbarramenti verificati con
`curl` il 14/09** — `x-robots-tag: noindex, nofollow`, `robots.txt` con
`Disallow: /`, `<meta name="robots" content="noindex, nofollow">` in pagina.
Online c'è il **giro di finitura `673d6c6`**: quote con il valore vero letto a
runtime, fascia corsi a due colonne. Dopo quel commit solo `.gitignore`
(`.impeccable/`, `.netlify`).

Nessuna sovrapposizione con [[sito-pinkploy]], l'altra onicotecnica di Brescia
messa online oggi: mondo, caratteri e palette sono altri (Anybody/Hanken,
rosa-viola-rosso).

## Cosa resta aperto

⬜ Safari su iPhone, mai provato. ⬜ La motion viva è stata vista **solo a 4,5 s
dal load**. ⬜ Le coordinate dei richiami sulle foto sono lette **a occhio**.
⬜ Il DM col link è di Patrick. ⬜ Scheda cliente
`02-Sales/clienti/nails-robyy.md`. ⬜ I dieci `TODO` da chiedere a Roberta,
qui sopra.

## Collegamenti

[[processo-siti]] · [[essenza-e-motion]] · [[trappole]] · [[direttive-siti]] ·
[[netlify]] · [[registro-interventi]] · [[sito-pinkploy]]
