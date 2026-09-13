---
type: progetto
riga: Laura Franzoni @laurafranzoni_lashmaker, extension ciglia a Brescia: bozza costruita sul mondo «dall'alto», 8/8 al controllo. Manca il DM e il file del logo.
status: attivo
client: laurafranzoni
stack: html-css-js
started: 2026-09-13
deadline:
updated: 2026-09-14
source: claude
verificato: 2026-09-14
tags: [sito, bozza, ciglia, brescia, instagram]
---

# Sito Laura Franzoni — raccolta e costruzione

Bozza-esca: **il DM non è ancora partito** e non c'è scheda cliente. Repo
`~/lavoro/laurafranzoni-site`, dallo starter (`nuovo-sito.py`). Nessun repo su
GitHub, nessun push: lo decide il direttore.

Passi 0, 1 e 2 fatti. La pagina è costruita: `index.html` + `assets/stile.css`,
tre commit, **nessun remote e nessun deploy**.

## Chi è, verificato sul profilo il 13 settembre 2026 (senza login)

`@laurafranzoni_lashmaker`, nome del profilo **«Laura Franzoni | Lash Maker
Brescia»**. **452 follower, 1.613 seguiti, 35 post** — la griglia pubblica ne
mostra 12, le altre 23 stanno dietro il muro del login.

⚠️ I due numeri dei seguiti non coincidono: il `og:description` servito ai bot
dice **1.633**, il DOM vivo dice **1.613**. Vale il DOM.

Bio intera, parola per parola (aperta cliccando «altro»: da sloggati arriva
troncata a «👇…»):

```
Laura Franzoni | Lash Maker Brescia
✨ Trasformo il tuo sguardo
👁️ Extension Ciglia | Laminazione
🕒 Risparmia 15 min ogni mattina (addio mascara!)
👇 Prenota il tuo trattamento in DM!
```

**Nessun link in bio**, e non è una deduzione: nell'intera pagina gli unici link
fuori da `instagram.com` sono i piedini di Meta. **Nessun pulsante contatto,
nessuna categoria professionale, zero storie in evidenza** (zero link
`/stories/highlights/` nel DOM). C'è **una storia attiva** il 13/9 — dietro login,
non letta. Il 👇 della bio punta a una riga di testo, non a un link: è la frase
del DM, non un bottone.

## Il marchio, e i colori campionati

L'immagine di profilo **non è una foto: è un logo**. Quadrato nero pieno,
monogramma **L · E · L** in maiuscole con grazie, bianche, separate da un filetto
verticale sottile, attraversate da un **ramo fiorito inciso** (due fiori aperti e
foglie, tratto da incisione ottocentesca). Sotto, **«LUXURY EYE LASH»** in
maiuscolo spaziato, e più in basso **una riga di didascalia illeggibile** a questa
risoluzione.

**Il nome commerciale «Luxury Eye Lash» sta solo nel logo**: nella bio non compare
mai, e sui motori non esiste.

Campionato pixel per pixel su `logo-profilo.jpg` (`sips -s format bmp` + parsing
BMP in `python3` puro, 22.500 px letti — niente PIL):

| | esadecimale | come |
|---|---|---|
| nero del fondo | **`#000000`** | 19.017 px su 22.500, l'84,5 % dell'immagine |
| lettering bianco, picco | `#FFFFFF` | solo **272 px** sopra 170 di luminanza |
| lettering bianco, medio | `#D7D7D7` | media di quei 272, bordi sfumati inclusi |

⚠️ Stessa trappola di [[sito-nails-robyy]]: **a 150 px il lettering è quasi tutto
antialiasato**. `#000000` è un valore su cui costruire, `#D7D7D7` no.

**Il logo esiste solo a 150×150.** Le varianti più grandi rispondono 403 (la firma
`oh=` dell'URL copre anche il parametro di taglia: modificare `s150x150` a mano
non funziona). Non si ridisegna e non si ingrandisce. → `TODO`.

## Cosa fotografa

Sempre e solo **occhi**. Mai le mani, mai il posto, mai lei, mai un attrezzo in
posa. Due tagli soli, e si alternano:

1. **La macro sull'occhio**, ravvicinatissima, quattro scatti su tredici: si legge
   ciglio per ciglio, si vede il riflesso della lampada ad anello nella pupilla, si
   vedono i pori e i nei della pelle. È fotografia clinica, non da centro estetico.
2. **Il volto intero della cliente sdraiata sul lettino**, ripreso dall'alto da
   dietro la testa. È il punto di vista del suo mestiere, e si vede: **dieci foto su
   tredici non hanno il viso dritto** — sette ruotate di circa 90°, due quasi
   capovolte, due inclinate; le tre dritte sono tutte macro sull'occhio.
   Non è un difetto di orientamento (`sips` e `naturalWidth` del browser danno le
   stesse misure), è dove sta seduta mentre lavora.

Elementi che ricorrono: il **poggiatesta di velluto rosa cipria** del lettino (in
nove foto su tredici), i capelli sciolti sul cuscino, il **buio pieno** attorno al
viso quando lavora con la lampada puntata, un **pettinino nero da ciglia** appoggiato
sul cuscino in uno scatto solo. In una foto la cliente ha ancora addosso la
**mascherina** del lettino. Le clienti sono donne di età molto diverse, dalla
ventenne truccata alla signora con la pelle matura: non c'è un target unico.

**Nessun testo impresso su nessuna foto. Nessun prima/dopo dichiarato.** In due
scatti però la cliente ha gli occhi **aperti** subito dopo il lavoro, e in due ha
gli occhi **chiusi** durante: chi guarda la sequenza capisce il momento.

Dominante misurata su tutte e tredici (170.760 px letti, bucket da 16): incarnato
caldo (`#A87868`, `#B87858`, `#986858`) e nero profondo di ciglia e capelli
(**`#130D0E`** medio, fino al 20 % del fotogramma). Il rosa del poggiatesta è
**`#DFBCD1`** medio, e in una foto arriva all'**11,5 %** dell'inquadratura.

## Le sue parole

Extension Ciglia · Laminazione · volume · volume 2D · dolly eyelashes · «Trasformo
il tuo sguardo» · «Risparmia 15 min ogni mattina (addio mascara!)» · «Prenota il
tuo trattamento in DM!» · «Per fissare appuntamenti, scrivetemi in DM 🫶🏽» · «Per
qualsiasi informazione scrivimi in DM ✨».

Le dodici caption lette, per intero:

- **p01, 28 nov 2025** (fissato in alto): solo hashtag —
  `#lashextensionsbrescia#lashextencion#lashmaker#volume#beautylash#beautyfromitaly`
- **p02, 15 mag 2025** (fissato in alto): «**Svegliati già pronta: con le mie lash
  extension, risparmi tempo e guadagni sguardi! 💕✨**». È la caption più lunga che
  abbia mai scritto. Due commenti, entrambi di `s.n_v.v`: «Bellissime😮😮😮😮😮» e
  «🔥🔥🔥🔥🔥🔥🔥🔥🔥».
- **p03, 9 set 2026** (reel): «#lashmakerbrescia #extencionciglia 🌸✨»
- **p04, 28 ago 2026**: «**Laminazione 🌸**»
- **p05, 4 ago 2026**: «#lashmakerbrescia #volume»
- **p06, 25 lug 2026** (reel): «#lashmakerbrescia #extencionciglia #beauty #volume»
- **p07, 14 lug 2026**: «#lashmakerbrescia #volume #dolleyelashes 🌷 / **Per
  qualsiasi informazione scrivimi in DM ✨**». Un commento di `be_naily`: «Belleeee».
- **p08, 3 lug 2026**: «🌷» — e basta.
- **p09, 1 lug 2026**: «#lashmakerbrescia#brescia#volume2d #eyelashextensions /
  **Per fissare appuntamenti, scrivetemi in DM 🫶🏽**»
- **p10, 16 giu 2026**: «✨✨✨👈🏽👈🏽👈🏽 #lashmaker #brescia». Commento di
  `be_naily`: «😮😮😮».
- **p11, 15 giu 2026** (reel): «**Prenota il tuo appuntamento🔥** #lashmakerbrescia
  #brescia #extensionciglia»
- **p12, 9 giu 2026**: «👉🏽✨🩷». Due commenti: `azzurrapinzii` «🔥🔥❤️»,
  `be_naily` «🔥 bellissime».

Due cose che si vedono da questo elenco. **Scrive pochissimo**: otto post su dodici
sono emoji e hashtag, e da lì non esce copy — il testo del sito lo scrive DenkiCode.
E i commenti pubblici sono **di colleghe** (`be_naily`, `azzurrapinzii`), non di
clienti: le clienti non commentano.

Ricorre `#extencionciglia` con la c: è come lo scrive lei.

## Cosa NON c'è, e non si inventa

Indirizzo (dice solo «Brescia», mai una via) · nome del salone confermato · telefono ·
WhatsApp · mail · orari · giorni di chiusura · prezzi · durata dei trattamenti ·
recensioni · anni di attività · certificazioni · corsi · una foto di Laura · una foto
dello studio · se lavora in salone o a casa.

**Sui motori non esiste**, riverificato oggi: `"Laura Franzoni" lash maker Brescia`,
`laurafranzoni_lashmaker` e `"Luxury Eye Lash" Brescia` non restituiscono né lei né
un posto fisico col suo nome — escono Heylash, Queen Lashes e i portali di
categoria. **Nessuna scheda Google Maps.** Cinque domini plausibili
(`laurafranzoni.it`, `laurafranzonilashmaker.it`, `luxuryeyelash.it`,
`luxuryeyelash.com`, `laurafranzonilash.it`): **nessun record DNS**. Regge la
verifica di lista del 12/9.

**Unico canale verificato: il DM di Instagram**, e lo dice lei tre volte.

## Le foto scaricate — 13 file, 12 usabili

Scaricate il 13 settembre 2026 in `~/lavoro/laurafranzoni-site/assets/img/_orig/`
(gli URL del CDN scadono in giorni). Numerate secondo l'ordine della griglia; la
lettera è la posizione nel carosello.

| file | px | cosa mostra |
|---|---|---|
| `p01a-2025-11-28` | **834×945** | macro di un occhio chiuso di tre quarti: ciglia lunghissime e fitte a ventaglio, sopracciglio pettinato verso l'alto, ciocca bionda e un lembo di tessuto rosa in alto a sinistra. **Sotto soglia** |
| `p02a-2025-05-15` | 1440×1440 | ragazza sdraiata sul poggiatesta rosa, testa inclinata, occhi aperti verso l'obiettivo: ciglia nere spesse, anellino al naso, labbra rosse lucide, felpa nera |
| `p02b-2025-05-15` | 1440×1440 | stessa ragazza, **occhi chiusi**: le ciglia si leggono in silhouette contro la palpebra. È il controcampo di `p02a` |
| `p04a-2026-08-28` | 2166×2166 | macro ravvicinatissima su un occhio **aperto** di una cliente matura, ruotato di 90°: ciglia sottili e naturali (è la **laminazione**, non l'extension), pelle segnata, rughe, riflesso della lampada nella pupilla, tessuto bianco a boccoli sullo sfondo |
| `p05a-2026-08-04` | 1756×2335 | volto di una signora sdraiata, ruotato di 90°, **occhi chiusi**: due file di ciglia lunghe e nere, luce calda che taglia la fronte, bordo del cuscino lilla in basso a destra |
| `p07a-2026-07-14` | 2268×2318 | ragazza sdraiata su poggiatesta **rosa e viola**, camicia bianca a coste, occhi chiusi, capelli sparsi sul cuscino: la posa completa del lettino |
| `p07b-2026-07-14` | 2268×2309 | macro su un occhio **aperto** della stessa ragazza, dritta: ciglia a ventaglio nette, sopracciglio folto, iride castana, pelle abbronzata |
| `p07c-2026-07-14` | 2268×2310 | stessa ragazza dall'alto, ruotata di 90°, **occhi aperti** verso l'obiettivo — e in basso a destra, sul cuscino rosa, il **pettinino nero da ciglia**: l'unico attrezzo di tutto il feed |
| `p08a-2026-07-03` | 1411×1411 | macro su un occhio **aperto**, ciglia lunghissime a curva, iride nocciola con il riflesso ad anello della lampada, un neo sulla palpebra, ciocca scura in alto a sinistra |
| `p09a-2026-07-01` | 1938×1938 | volto ruotato di 90°, occhi aperti, **piercing al naso a fiore dorato**, cuscino rosa dietro: ciglia molto folte, chiusura a virgola verso l'esterno |
| `p10a-2026-06-16` | 1934×2509 | volto ruotato di 90° su fondo **nero pieno**, occhi chiusi, spallina nera: solo il profilo illuminato e le due file di ciglia. La più cinematografica delle tredici |
| `p10b-2026-06-16` | 2072×2681 | stessa sessione, ruotata di 90°: **occhi azzurri aperti**, la **mascherina grigia** ancora appoggiata sul cuscino rosa in alto a sinistra, catenina d'oro |
| `p12a-2026-06-09` | **3024×4032** | ragazza sdraiata sul cuscino rosa, capelli castano-rossi, ruotata di 90°, occhi aperti: **due anellini dorati al naso e uno al setto**, tre collane d'oro, un tatuaggio sulla spalla. La più grande del gruppo |

**Non utilizzabili, e non sono nella cartella:**

- le **3 copertine di reel** (`p03` 9 set, `p06` 25 lug, `p11` 15 giu): nella griglia
  sono **360×640**, sotto soglia, e sono fotogrammi di video. Fuori per regola.
- le 12 anteprime di griglia a 360–640 px: superate dalle grandi.
- `logo-profilo.jpg`, 150×150: c'è, ma è il logo, non una foto.

## Passo 1 — strada dichiarata: **1, le foto reggono**

**12 file su 13 stanno sopra i 1080 px** sul lato lungo, contro il minimo del
processo: il più piccolo utilizzabile è 1411, il più grande **3024×4032**. L'unico
scartato è `p01a` a 834×945, che è anche uno dei fissati in alto.

I rapporti non sono omogenei come su [[sito-nails-robyy]] — **5 quadrati 1:1, 3
quasi quadrati 1:1,02, 4 verticali 3:4** — ma la dominante è **una sola** su
tutte: incarnato caldo, nero delle ciglia, rosa del poggiatesta. Un trattamento solo
per tutte, e basta. **Non serve costruire un sito che prescinda dalle foto.**

Restano tre paletti che valgono lo stesso:

1. Grafica inventata e spina dello scroll sono obbligatorie comunque: dodici occhi
   in griglia non sono un sito.
2. **Le foto ruotate non si raddrizzano.** L'inclinazione è il punto di vista del
   mestiere, e togliendola si ottengono ritratti anonimi. Chi costruisce lo tenga in
   conto quando sceglie i ritagli: un `object-fit: cover` stretto su un volto a 90°
   taglia l'occhio, che è il soggetto.
3. Strada 1 **non chiude il `TODO` del logo**: quello resta a 150×150.

## Passo 2 — mondo scelto: «Dall'alto», con l'innesto «Quindici minuti»

Scelto dal direttore il 14 settembre 2026. Seed `d07a0ceb`, modo **Persuade**,
**indice assegnato 3** nella lista dei mondi. Il contratto di direzione sta nel
repo, in `.impeccable/surfaces/index-html.md`, e non compare in pagina.

**La metafora è lo sgabello di Laura.** Il sito è girato dal suo posto, dietro
una testa sdraiata: chi guarda non sta davanti a un occhio, sta **sopra** un
occhio. È il punto di vista che esiste solo perché il mestiere si fa sopra una
faccia, ed è già dentro le sue dodici foto: per questo dieci su tredici non sono
dritte.

**La spina dello scroll, in tre battute.** *Ti sdrai*: si parte da una fascia di
ciglia a tutta pagina e scendendo l'inquadratura si allarga e si raddrizza,
finché si capisce che era una testa sdraiata vista dall'alto. *Si spegne la
luce*: la pagina si ferma, il fondo cala a `#130D0E`, il ventaglio si infittisce
pelo per pelo e il contatore sale ai quindici minuti della bio. *Apri gli occhi*:
tre ritratti a occhi aperti entrano capovolti, e solo l'ultimo si raddrizza,
sul messaggio.

### Le sezioni, in ordine

| # | Sezione | Cosa fa | Foto |
|---|---|---|---|
| 0 | barra | nome, mestiere, bottone DM (sotto i 560 px resta la sola icona, bersaglio 44×44) | — |
| 1 | **Laura Franzoni** | h1 col nome che entra ruotato di 90° e si raddrizza in 900 ms, la sua frase «Trasformo il tuo sguardo» sotto, piccola; poi la fascia con «Ti sdrai.» sul bordo alto | `p07a` (90°) |
| 2 | **Dallo sgabello** | perché le foto sono storte, e che nessuna è stata raddrizzata | `p01a` (20°), `p07c` (170°) |
| 3 | **Si spegne la luce** | l'unico fermo della pagina: buio, ventaglio, contatore | nessuna, è tutta disegnata |
| 4 | **Quello che Laura mette sulle tue ciglia** | Extension ciglia con le tre tecniche, Laminazione | `p10a` (110°), `p08a` (40°), `p07b` (0°), `p04a` (90°) |
| 5 | **Sul lettino non devi fare niente** | campo rosa pieno, quattro passi senza nessuna durata | nessuna |
| 6 | **Apri gli occhi** | tre visi interi capovolti, l'ultimo si raddrizza sul DM | `p12a`, `p09a` (180°), `p10b` (0° dopo la rotazione) |
| 7 | piede | logo a 96 px, Instagram, firma DenkiCode | logo |

⚠️ **L'h1 è il nome della cliente** perché il 14/9 è entrata la direttiva di
Nicola sulla bozza Pinkploy. Il mondo era stato scelto con «Ti sdrai.» come
titolo: quella frase è stata spostata sul bordo alto della prima fascia, dove
apre il racconto senza fare da titolo.

### La grafica inventata — quattro segni, tutti SVG disegnati

- **Il contaciglia**: arco graduato in una pastiglia scura a sinistra, 19 tacche,
  scatta fino a 90 mentre si scende (novanta è quante ne servono per un occhio).
  Sotto i 1320 px diventa una pastiglia in basso a sinistra con la sola lettura:
  nel canale stretto l'arco finirebbe sul testo.
- **Il ventaglio**: 90 peli piantati uno per uno su una linea palpebrale
  quadratica, generati a mano e accesi con
  `opacity: calc(var(--peli) * 96 - var(--i))`. Nessun JS per pelo.
- **L'anello di luce**: cerchio aperto dietro il ventaglio, è la lampada che si
  vede riflessa nelle sue macro.
- **La bussola del capovolto**: pastiglia in basso a destra, ago e gradi della
  foto che stai guardando. Vince quella più vicina al centro dello schermo.
  È il pezzo che rende il capovolto una scelta.

### Il trattamento delle foto

**Un taglio solo per tutte**: fascia **21:9** centrata sulla linea delle ciglia
(sotto i 560 px diventa 16:9), bordo vivo, **nessuna cornice**. Duotone leggero
verso l'incarnato (`grayscale .42 / sepia .22 / saturate 1.16 / contrast 1.07`),
grana al 3 % su strato fisso. Ogni ritaglio ha il suo `object-position`,
guardato uno per uno a 375: la fascia non taglia mai l'occhio. **I tre visi
interi restano interi**, senza ritaglio, ognuno col suo rapporto, allineati in
basso.

Ricampionate a **1440 px** di lato lungo, i tre ritratti a 900 (in pagina stanno
a 419). `p01a` resta alla sua misura nativa 834×945 e non supera i 380 px CSS.
Le `_orig` restano nel repo ma Netlify risponde **404** su `/assets/img/_orig/*`.

**Nove foto in pagina su dodici usabili.** Fuori: `p02a`, `p02b`, `p05a` —
non hanno trovato un posto che non fosse una griglia.

### Palette e tipi

Nero `#130D0E`, incarnato `#C99A86`, rosa poggiatesta `#DFBCD1` come **campo
pieno su una sezione intera**, lettering `#F2EDEA`. Due derivati per il testo
secondario, entrambi mescolati dai quattro: `#6E544A` sul chiaro (5,97:1),
`#C99A86` sul nero (7,74:1). **Bodoni Moda** 600/900 display, **Schibsted
Grotesk** 400/600 testo, con ripiego dichiarato (`local()` + `size-adjust`).

### Il copy, e cosa resta da confermare

Niente prezzi, orari, indirizzo, telefono, durate: non esistono e non si
inventano. Unico canale il DM. **Da confermare con Laura** le descrizioni dei
servizi (Extension, Volume, Volume 2D, Dolly, Laminazione) e i quattro passi
della sezione rosa: sono scritti da noi da quello che si vede nelle foto, non
da lei. I nomi invece sono suoi, letti nella bio e negli hashtag.

### Cosa è stato misurato, il 14 settembre 2026

Overflow orizzontale **0 su 25 larghezze** da 320 a 1920, bordi delle media
query compresi; barra e bottone su una riga a ogni larghezza. Console **vuota**,
nessuna richiesta fallita. Pagina **1,73 MB** su 18 risorse. Senza JS la pagina
è completa: ogni valore a riposo è già quello finale (`--buio` 1, `--peli` 1,
`--dritto` 1, contatore 15, contaciglia 90). Contrasti AA calcolati su tutto il
testo: nessun fallimento. «Ti sdrai.» sulla foto sta a 10,78:1 nel pixel
peggiore. La bussola legge i gradi giusti su tutte e nove le foto, verificata
in Brave via CDP.

`controlla-sito.py`: **8/8**. `impeccable detect`: 8 avvisi, tutti dichiarati
(grana al 3 %, fasce a tutta pagina che toccano i bordi per scelta, interlinea
1,10 su un display da 51 px, fondo chiaro della palette del cliente).

## Contesto commerciale

Riga 233 di [[2026-09-13-instagram-siti-brescia]] — `@laurafranzoni_lashmaker`,
Laura Franzoni Lash Maker, Brescia (BS), segmento **Ciglia**, 452 follower, **gancio
1**, prodotto **siti**. Trovata cercando «lash maker brescia» nella ricerca di
Instagram, profilo letto il 12/9.

**Il DM non è ancora partito**: le colonne «DM inviato» ed «Esito DM» sono vuote. Il
messaggio è già scritto in lista e attacca sulla frase della bio:

> «quindici minuti risparmiati ogni mattina» è l'argomento migliore che potevi
> trovare. Ho notato però una cosa: quella frase sta in una riga di bio, dove la
> legge solo chi è già sul tuo profilo.

⚠️ **Quindi l'argomento del sito è già promesso, e non è la bellezza: è il tempo.**
Quella frase deve stare dove la vede chi arriva, non in una riga di bio. Non è una
nostra idea di sezione, è la promessa del DM.

## TODO — da chiedere a Laura

- [ ] **Il file del logo vero**, vettoriale o almeno 1000 px. Oggi si ha 150×150, e
      la riga di didascalia sotto «LUXURY EYE LASH» è illeggibile: cosa c'è scritto?
- [ ] «Luxury Eye Lash» è il nome che vuole sul sito, o preferisce il suo?
- [ ] Indirizzo, o conferma che resta «Brescia» e basta. Salone o studio in casa?
- [ ] Telefono / WhatsApp / mail: esiste un canale oltre al DM?
- [ ] Orari e giorni di lavoro.
- [ ] Prezzi e durate, o almeno se vuole che compaiano.
- [ ] **I trattamenti**: che differenza fa fra Extension, volume, volume 2D e dolly?
      Fa il refill? Ogni quanto? La laminazione dura quanto?
- [ ] Una foto di lei al lavoro e una del posto: nel feed pubblico non esiste nessuna
      delle due.
- [ ] Recensioni o messaggi di clienti che possiamo citare: pubblicamente ce ne sono
      **zero**, e i soli commenti sono di colleghe.
- [ ] Se le 23 foto non pubbliche contengono materiale migliore (prima/dopo veri).

## Cosa manca al processo

✅ Passo 2 — mondo scelto e scritto qui sopra. ✅ Passo 3 — costruzione.
⬜ Scheda cliente in `02-Sales/clienti/laurafranzoni.md`. ⬜ DM da mandare.
⬜ Riga in [[registro-interventi]]. ⬜ Repo su GitHub, deploy: li decide il
direttore, il repo locale non ha remote.

## Collegamenti

[[processo-siti]] · [[sito-nails-robyy]] · [[sito-pinkploy]] · [[trappole]] ·
[[direttive-siti]] · [[registro-interventi]]
