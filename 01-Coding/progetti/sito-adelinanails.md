---
type: progetto
riga: Bozza sito per Adelina Nails (Alessandria) in ~/lavoro/adelinanails-site - contenuto solo da profilo + inventario competitor, giro 3 «lacca, oro e rilievo», Melodrama + Grape Nuts, apertura in 4 tempi, 8/8 - online su adelinanails-site.netlify.app dal 19/9 (deploy da GitHub).
status: attivo
client: adelina-nails
stack: html-css-js
started: 2026-09-18
deadline:
updated: 2026-09-19
source: claude
verificato: 2026-09-19
tags: [sito, bozza, nail, alessandria, instagram]
---

# Sito Adelina Nails — bozza, Alessandria

Cliente: [[adelina-nails]]. Cartella `~/lavoro/adelinanails-site`, repo **privata**
`Nixo999/adelinanails-site` (`main`, pushata il 18/09). Database: nessuno. Processo: [[processo-siti]].

## Cosa cambia rispetto alle altre bozze — deciso da Nicola il 18/09

1. **Prima la ricerca competitor**, poi il sito: [[competitor-siti-nail]], 15
   siti aperti. I competitor decidono **quali blocchi esistono**, il suo profilo
   decide **cosa li riempie**. Blocco senza dato = blocco omesso, mai inventato.
2. Apertura animata sempre, zero muri di testo, motion «affascinante ma non
   esagerata, soprattutto utile». Verbatim in [[direttive-siti]].
3. **Token**: raccolta e ricerca a operatori Sonnet che tornano su file ≤90
   righe (`RACCOLTA.md`, `COMPETITOR.md`); Opus solo per direzione e
   costruzione, **lo stesso operatore** per entrambe, così la catena di skill si
   carica una volta sola. La ricerca nail è nel vault e non si rifà.

## Materiale, verificato il 18/09

7 foto di lavori (6 ≥1080 px, una a 912), 1 foto con l'attestato (Era Aesthetic Academy, marzo
2023), avatar 150 px inutilizzabile, nessun logo. **Non ci sono**: prezzi,
durate, orari, indirizzo, telefono, recensioni, marchi. Dettaglio in
`RACCOLTA.md` e `PRODUCT.md` nella cartella.

## Pagina

Hero → Lavori per stile → Servizi a categorie (righe pronte per `durata ·
prezzo`) → Chi è (attestato) → Prenota in DM → footer.

## Mondo scelto

**A «Il sigillo»**, seed impeccable `bfd21097`, con un innesto da B. Scelto dal
direttore il 18/09 fra tre (B «Il ventaglio», C «I sessanta secondi»).

- Metafora: il sigillo dell'attestato che tiene in mano nella foto 03, l'unico
  fatto verificabile che possiede. La pagina è un documento che rilascia.
- Spina: il nome si incide e il sigillo si imprime · ogni stile è una tavola nel
  suo fregio, che cambia disegno da stile a stile · ultima tavola l'attestato,
  e al posto della firma in calce il DM.
- Apertura 1,4 s: filetto d'oro dai quattro angoli, poi il sigillo. Testo pieno
  dal primo fotogramma: si anima solo la cornice.
- Palette: lacca `#1A1014`, inchiostro `#F7F1ED`, oro `#C39A55` / `#E3C079`,
  rosso `#8E1B27`, incarnato `#E6BFB4`. Font: Bodoni Moda + Archivo.
- Da B: pettine dei pois e numeri tabulari nel blocco Servizi, colonna pronta
  per `durata · prezzo`. Il filtro-ventaglio scartato: con 7 foto è finto.
- Perché A: fondo lacca uniforma i tre fondi freddi (auto, granito) delle foto;
  nessuno dei cinque siti nail già fatti è «incisione», quattro sono disegno
  tecnico. Rischio dichiarato: scivolare su crema/pergamena o sul lusso cupo.

Foto di lavori usabili: **7**, non 8 (01, 02, 04, 05, 06, 10, 11; 04 a 912 px).

## Stato al 18/09 — costruita, non pubblicata

- `controlla-sito.py` **8/8**, `controlla-slop.py` **0 blocca, 0 avvisa**, overflow
  0 su 20 larghezze (320-1920), 39 nodi di testo tutti AA (minimo 6,89:1),
  console 0. Apertura chiusa a 1.180 ms, testo a opacità piena dal fotogramma
  120 ms. Commit locale `1392774`. Catture in `.cantiere/`.
- **Un giro bocciato dal direttore**: sotto i quattro stili c'erano righe di
  tecnica («il charm va posato sul gel ancora morbido…») senza fonte. Ora ci sono
  le sue caption verbatim, rilette dal post: `Dc-RNc4M_tB`, `Dc0sO66DL4H`,
  `DcwTX_ljFUg`, `Dc_QMOdMslB`. Titoli dei capitoli presi dalle sue parole
  (French, Pois e fiori, Scaramanzia, Rosso). Dai servizi è uscita
  «ricostruzione»: non è in bio, caption né attestato. Restano Manicure, Gel,
  French, Nail art, Pedicure.
- **Non verificato**: Safari e Firefox veri (il ramo senza `animation-timeline:
  view()` non è stato visto girare), iPhone con barra URL. `og:image` va resa
  assoluta il giorno della pubblicazione (annotato nel `LEGGIMI.md` del repo).
- **Manca**: pubblicazione su Netlify coi tre sbarramenti, e il DM col link.
  `netlify.toml` sbarra anche `RACCOLTA.md`, `COMPETITOR.md`, `LEGGIMI.md` e
  `sorgenti/*`: da verificare con `curl` al primo deploy.

## Giri 2 e 3 — dopo la bocciatura di Nicola del 18/09

Parole sue sul giro 1: «studio del design terribile, troppo piatto, animazione
all'avvio troppo semplice, studio dei font terribile, per niente particolare e
non dà personalità al sito». Falla del direttore: «non esagerate» letto come
«minime», `overdrive` vietato, `bolder` saltato, Bodoni + Archivo lasciata
passare. Verbatim in [[direttive-siti]]. Il contenuto non è cambiato.

- **Font**, tre studi su specimen (`.cantiere/specimen.png`): scelto **Melodrama
  700 + Grape Nuts + Satoshi**. Grape Nuts solo sui suoi virgolettati. Tutti
  **self-hosted** in `assets/fonts/` (132 KB), licenze lette alla fonte in
  `LICENZE.md`, richieste esterne 0.
- **Il mondo si è piegato, dichiarato**: da «documento che rilascia» a «lacca,
  oro e rilievo». Gradienti per capitolo, grana, riflesso di lacca, banda rossa
  piena su «Rosso», lettere a 44vw fuori margine, tavole con ombra vera
  sovrapposte, parallasse con `animation-timeline: view()`.
- **Apertura in 4 tempi, 3,0 s**: luce sulla lacca → nome lettera per lettera →
  sipario → tre tavole dei suoi lavori a ventaglio nell'hero (due sotto i 600
  px). CTA viva a 2,4 s, si salta a scroll/tap, non ripete nella sessione,
  scostamento di impaginato 0.
- **Overflow interno**: 5 casi veri che l'overflow di pagina non vedeva
  («Prenotazioni» e «Scaramanzia» fuori dal proprio blocco). Chiusi con
  `container-type` e titoli in `cqi`. Pagina 0 e interno 0 su 20 larghezze.
- Controlli: 8/8, slop 0/0, 33 nodi AA, console 0. Commit locale `8e8d1f4`.
- **Non verificato in più**: `container-type` senza fallback sui browser vecchi,
  LCP con le tre foto dell'hero non lazy, apertura su telefono fisico.

## 19/09 — online, e la prima correzione da telefono vero

Pubblicato da Nicola su `adelinanails-site.netlify.app`, deploy automatico dal
push su GitHub. Da iPhone la sezione «Adelina» aveva il testo a una parola per
riga: `container-type` a 0 px nella griglia centrata, corretto in `3b9569a`.
Verificato online con `curl`: correzione servita, `RACCOLTA.md`,
`COMPETITOR.md`, `LEGGIMI.md`, `PRODUCT.md` e `sorgenti/` a 404, `X-Robots-Tag:
noindex`. **Falla del processo**: la sonda dell'overflow interno del giro 3 non
poteva vederlo, e il direttore non ha guardato il fondo della cattura mobile.

## Collegamenti

[[adelina-nails]] · [[competitor-siti-nail]] · [[processo-siti]] ·
[[direttive-siti]] · [[trappole]] · [[registro-interventi]]
