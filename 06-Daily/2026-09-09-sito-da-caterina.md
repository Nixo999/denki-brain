---
type: daily
data: 2026-09-09
source: claude
tags: [daily, sito-da-caterina, frontend, impeccable, netlify]
---

# 9 settembre 2026, sera — Da Caterina: l'album delle figurine

Nicola, dal Mac, in `/nicola`: «nuovo sito vetrina per questo account Instagram:
dacaterinatoelettatura. Fallo seguendo il solito modello, con delle immagini di cani
carine e mettine alcuni ritagliati senza sfondo in giro tra un punto e l'altro del
sito». Nessun lead in lista, nessuna scheda cliente: la bozza è l'esca.

## Cosa c'era

Una toelettatura per cani in Via Introzzi 8 a Olgiate Olona (VA), Caterina Nucibella,
centro Special One. Instagram con 3.354 post: i cani appena toelettati montati in
scene (spiaggia, caramelle, orsetti, nave, lago, spa), caption vuote. Logo rosso
vermiglio con lettering crema. Orari solo sui portali. Il profilo si legge senza login
dal pannello; le pagine dei post con `curl` no, questa volta: tutte vuote, e nel
pannello arrivano senza caption. Dettaglio in [[sito-da-caterina]].

## Il processo

[[processo-siti]] completo. `design-taste` letta (dial 8/6/3), `high-end-visual-design`
unica skill di stile, `brandkit` e `imagegen` saltate, `ui-ux-pro-max` saltata
(script assente). Impeccable: `PRODUCT.md`, seed **`7d230b00`**, indice assegnato
**6 su 7**: «l'album delle figurine». Sei sfidanti, tutti `declined`, ognuno con una
disciplina donata. Pagina di decisione servita nel pannello, `--wait` due giri, poi
`PAGE CLOSED`: si è costruita l'assegnata. Code-led. `voce-denkicode` sul copy,
`emilkowalski-motion` per ultima. Finish review con un subagente sul riferimento
degradato: primo giro `recapture` (le catture intere erano tagliate prima della mappa
e del footer), secondo giro `fix` con otto punti, tutti applicati. Verdetto e
DESIGN.md nella riga del registro.

## Il pezzo nuovo: i ritagli

`rembg` e PIL non ci sono. Vision di macOS sì: `VNGenerateForegroundInstanceMaskRequest`
in venti righe di Swift ritaglia il soggetto e scrive un PNG con alfa rifilato. Undici
cani in un colpo. Il bordo bianco fustellato è CSS, sei `drop-shadow` a offset zero
sull'alfa vera più uno sfalsato per l'ombra: segue il contorno, non un cerchio. Sei
figurine nell'hero si attaccano una alla volta all'apertura (un rimbalzo solo),
quattro vaganti sbucano fra le sezioni e derivano con lo scroll via
`animation-timeline: view()`, senza JS. Il logo l'ho campionato pixel per pixel con un
altro script Swift: `#e03020`.

## Le trappole pagate oggi

Brave headless non scende sotto ~500 px di finestra: il PNG a 375 mostrava la nav senza
bottone e il testo fuori bordo, e sembrava un bug del CSS che il pannello non
confermava. Sito in un `iframe` da 375 e ritaglio con Swift. La cattura fotografava
l'animazione d'ingresso a metà: in `?cattura` si spegne. L'altezza della pagina intera
va misurata prima: a 4900 mancavano mappa e footer. `sites:create --account-slug
denkicode` dà 404: lo slug vero è `nicola-la-rezza`. Tutto in [[trappole]].

## Misurato

1440×900, 375×812, più 641, 760, 901, 1101: overflow 0, nav su una riga, CTA su una
riga, sei figurine sopra la piega (fondo a 827 px), contrasti 5,1 / 5,4 / 14 e 4,1
solo sui titoli grandi, console vuota. Detector: restano gli avvisi dichiarati.

✅ Online su <https://dacaterina.netlify.app>, tre sbarramenti verificati con `curl`.
✅ Repo `Nixo999/caterina-site`, privata. ⬜ Safari su iPhone. ⬜ Orari da confermare.
⬜ Il DM a Caterina è di Patrick: la bozza è pronta da mandare al secondo messaggio.

## La bocciatura, e la versione 2

Nicola, alle 23:4x, con la bozza online: «così mi fa cagare il sito, da telefono è
orribile, i ritagli degli animali fanno pena, e sembra tutto buttato a caso: rifallo
da capo con un altro stile, meno rosso e un po' più professionale». Tre falle, tutte
mie: il mondo «album» era una direzione da catalogo per un target che vuole la
toelettatura seria del paese; i ritagli a 640 px non reggono a grandezza di figurina;
e ho costruito l'assegnata con la pagina di decisione chiusa senza risposta invece di
fermarmi. Contromisura: registro `safer` dichiarato in `PRODUCT.md` come impegno di
marca (fondo chiaro, rosso solo accento, niente ruotato, niente ritagli, foto in
cornice, griglie allineate), e da qui in poi **Fable dirige, Opus esegue**: brief
completo all'agente `operatore` su Opus (copy, token, layout sezione per sezione,
verifiche misurate da riportare), io rileggo e decido. Richiesto da Nicola alle
23:5x: «usa la modalità in cui Fable fa da agente capo e Opus fa da lavoratore».

## Versione 2, in tre giri

Operatore su Opus, brief del direttore. Giro 1: struttura (nav bianca, hero 6/12 con
tre foto in cornice, trattamenti a filetti, squadra, galleria 4×2, Dove, footer);
misure pulite, un buco: l'h1 su tre righe, accorciato a «Toelettatura / a Olgiate
Olona» con «professionale» nel rigo sotto. Nicola alle 00:0x: «sta venendo meglio ma
dagli un po' di vita in più». Giro 2: entrata hero a scalare, rivelazioni allo
scroll, foto che respirano, fondi alternati con la tinta del rosso, footer scuro, nav
di vetro. Finish review: `fix` con otto punti (span rosso spezzato, la stessa entrata
su venti nodi, pannello largo col 40% vuoto, citazione rientrata, «quattro persone»
non documentato, un alt, il watermark del fotografo, voci di nav sparite sul
telefono). Giro 3: tutti applicati, e l'operatore ha trovato che la `transition`
dell'hover spegneva quella della rivelazione: lo sfalsamento non era mai esistito.
Verdetto **`ship`**. Online alle 00:4x del 10, sopra la versione bocciata.

## Collegamenti

[[sito-da-caterina]] · [[processo-siti]] · [[trappole]] · [[netlify]] · [[registro-interventi]]
