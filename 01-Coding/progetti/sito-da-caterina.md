---
type: progetto
status: bozza-online
cliente: "Da Caterina Toelettatura Professionale (nessuna scheda cliente: non è ancora un lead lavorato)"
created: 2026-09-09
updated: 2026-09-10
source: claude
repo: Nixo999/caterina-site
tags: [sito-vetrina, bozza, varese, toelettatura, animali]
---

# Sito Da Caterina Toelettatura — bozza non commissionata

**Da Caterina Toelettatura Professionale**, Via Introzzi 8, 21057 Olgiate Olona (VA).
Titolare Caterina Nucibella. Instagram `@dacaterinatoelettatura`: 1.420 follower,
3.354 post. Nessun sito: Instagram, Facebook e i portali di categoria.
Richiesta di Nicola del 9 settembre 2026: «nuovo sito vetrina per questo account
Instagram, col solito modello, immagini di cani carine, alcuni ritagliati senza
sfondo in giro tra un punto e l'altro del sito».

## Dati verificati

| Cosa | Dato | Fonte |
|---|---|---|
| Telefono | 351 856 6948 | bio Instagram |
| Email | dacaterinatoelettatura@gmail.com | distrettomedioolona.com, oraridiapertura24.it |
| Indirizzo | Via Introzzi 8, 21057 Olgiate Olona | specialoneitalia.it (store locator), portali |
| Bio | «Centro estetico per cani» | Instagram |
| Storie in evidenza | Trattamenti, Pulizia dentale, Magnetoterapia, Trattamenti 2025, Mondiali 2024 | Instagram |
| Affiliazione | centro Special One Grooming Center | specialoneitalia.it |
| Orari | mar–ven 9–18, sab 9–17 (un portale dice 18), lun e dom chiuso (un portale: «lun solo il 1° del mese») | **portali, non la titolare: `TODO` confermare** |
| Squadra | 4 persone, foto del 15 dic 2025 con caption «Complici e allegre, una squadra unita dalla passione per il nostro lavoro» | Instagram |

Le foto Instagram sono **i cani toelettati montati in scene** (spiaggia, caramelle,
orsetti, nave, lago, spa): 11 cani e la squadra, scaricate a 640×640 nella stessa
sessione. Le caption dei post sono vuote (tranne la squadra). Nessuna recensione letta,
nessun prezzo pubblicato: il sito non ne parla.

## Identità

Logo rosso vermiglio pieno (`#e03020` campionato con uno script Swift sui pixel) con
«DA CATERINA» in lettering morbido crema e «TOELETTATURA PROFESSIONALE» in sans. **Il
sito usa il loro rosso solo come accento** (bottone «Prenota», voce di nav attiva, riga
«oggi» degli orari) su fondo bianco caldo `#f7f6f3`; Manrope a tutti i pesi. È
l'impegno di marca scritto in `PRODUCT.md` dopo la bocciatura della versione 1.

## La bozza (versione 2)

Repo `~/lavoro/caterina-site` → `Nixo999/caterina-site` (privata, `main`).
**Online su <https://dacaterina.netlify.app>** dal 9 settembre 2026 (versione 2 dalle
00:2x del 10), sito `dacaterina` sul team `denkicode` (slug API `nicola-la-rezza`),
deploy diretto dal CLI (`npx netlify deploy --prod --no-build`), non collegato al repo:
un push non ripubblica. Statico puro: `index.html`, `assets/stile.css`, `assets/moto.js`,
nessuna libreria. Tre sbarramenti agli indici attivi e verificati con `curl`.

Lo standard della categoria fatto bene, registro `safer` di impeccable scelto da Nicola
in parole: nav bianca con marchio, quattro voci e bottone rosso · hero «Toelettatura /
a Olgiate Olona» con un rigo e tre foto in cornice su griglia 2×2 · trattamenti in
lista a filetti su due colonne (bagno e taglio, cura del mantello, pulizia dentale,
magnetoterapia) più il pannello Special One · squadra con foto, citazione loro e
credito al fotografo · galleria 4×2 delle loro foto · Dove siamo con orari («oggi» dal
JS, nota «orari indicativi»), mappa e indicazioni · footer scuro. Motion: entrata
dell'hero a scalare, rivelazione sfalsata degli otto riquadri della galleria, foto che
respirano al passaggio; fermo con `reduced-motion`, completo senza JS.

**Costruito in modalità direttore/operatore**, chiesta da Nicola: Fable scrive il brief
(copy, token, layout, verifiche da riportare), l'agente `operatore` su Opus scrive i
file e misura nel pannello, Fable rilegge e decide. Tre giri: struttura, «vita», fix
della finish review.

## Giro «vita» (10 settembre, mattina)

Nicola: «ancora completamente senza vita». Ogni sezione ha ora un dettaglio e un'entrata
sua, stesso linguaggio: maschera ed evidenziatore sul titolo, **stato aperto/chiuso
calcolato dagli orari** (l'unico pallino), parallasse e zoomata dell'hero, indicatore
della nav, filetti sotto gli h2, voci da sinistra, virgoletta rossa, didascalie di scena
al passaggio, file della galleria in deriva opposta. Regole in `DESIGN.md`: rosso
contato, unico pallino, entrata per sezione, riposo finale. Finish review `fix` (8) →
applicati (`ffda8a3`).

## Versione 1, bocciata

L'«album delle figurine» (rosso pieno, ritagli Vision ruotati fra le sezioni, seed
impeccable `7d230b00`, direzione assegnata 6 su 7, pagina di decisione chiusa senza
risposta) è nei commit `86a972a`…`8c639e1` ed è stata online un'ora. Nicola: «da
telefono è orribile, i ritagli fanno pena, sembra tutto buttato a caso». Non si riapre.
I ritagli restano in `assets/cani/`, inutilizzati.

## Misurato (versione 2)

1440×900, 375×812, più 641, 760, 901, 1101: overflow 0, nav su una riga, h1 su due
righe, bottone dell'hero su una riga e sopra la piega, font caricati, console vuota.
Contrasti: corpo su carta 6,9, su tinta 6,2, su fondo 6,4, footer 12, testo del
bottone su rosso 4,9. Rivelazioni: 20 su 20 su Chromium vero via CDP (nel pannello e
in Brave headless gli observer non arrivano, [[trappole]]). Detector impeccable: solo
i falsi positivi su `clamp()` nel padding.

## Finish review

Primo giro `fix` con otto punti (span rosso spezzato nel titolo, la stessa entrata su
venti nodi, pannello largo con il 40% vuoto, citazione rientrata senza motivo, «quattro
persone» non documentato, un alt sbagliato, watermark del fotografo senza credito, voci
di nav sparite sotto 760): tutti applicati. Verdetto nella daily
[[2026-09-09-sito-da-caterina]].

⬜ Safari su iPhone. ⬜ Orari da confermare con la titolare. ⬜ Il DM a Caterina è di Patrick.

## Collegamenti

[[processo-siti]] · [[netlify]] · [[trappole]] · [[registro-interventi]] · [[sito-osteria-tarilli]]
