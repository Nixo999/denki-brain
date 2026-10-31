---
type: risorsa
riga: La pipeline dei siti vetrina da un profilo Instagram - raccolta, catalogo, cancelli, skill. Cosa gira, cosa no, cosa aspetta Nicola.
updated: 2026-10-31
source: claude
verificato: 2026-10-31
tags: [siti, pipeline, instagram, cancelli, strumenti]
---

# Pipeline dei siti vetrina

Nicola, 31/10/2026: i siti vetrina «a volte vengono bene a volte male». Su 54
note di siti, 4 sono riusciti, 17 bocciati, 18 «bello ma…». La pipeline serve
a ridurre la casualità prendendo il metodo «compito ripetuto → skill →
automazione con cancelli». Parte dall'Instagram del cliente. Il gusto resta di
Nicola: la pipeline non sceglie la direzione al posto suo.

## I quattro pezzi e a che punto sono

| Pezzo | Stato al 31/10 | File |
|---|---|---|
| 1. Raccolta da Instagram | gira, provata su `@mikuma.dogs` | `raccogli-instagram.js`, `raccogli-instagram.py` |
| 2. Catalogo di sezioni approvate | fermo: cambia lo starter, aspetta Nicola | — |
| 3. Cancelli | gira, provata su Mikuma e Davide Milan | `cancelli-sito.py`, `cancelli-telefono.mjs` |
| 4. Skill `/nuovo-sito @profilo` | fermo: cambia il processo, aspetta Nicola | — |

## 1. Raccolta

Instagram senza login non risponde più a `curl`: l'API pubblica dà `401
require_login` ([[trappole]], sezione Scraping). Nel browser dell'app sloggato
invece profilo, griglia, didascalie e foto a 1440 px si leggono ancora.

Il giro è questo:

1. Si apre `instagram.com/<utente>/` nel browser dell'app, scheda in primo
   piano, e si incolla `raccogli-instagram.js` in `javascript_tool`. L'esito
   si salva in `~/lavoro/raccolte/<utente>/grezzo/profilo.json`.
2. Per ogni post di tipo `p` della griglia si apre la sua pagina, si rilancia
   lo stesso snippet e si salva `grezzo/<codice>.json`. I Reel si saltano:
   danno solo fotogrammi a 640 px.
3. `python3 01-Coding/strumenti/raccogli-instagram.py <utente>` scarica le foto,
   le misura con `sips`, scarta i Reel e tutto sotto i 1080 px, campiona i
   colori della foto profilo e scrive `scheda.md` e `scheda.json`.

Gli URL delle foto sono firmati e scadono in pochi giorni, quindi il passo 3 si
fa nella stessa sessione. Lo script esce 1 se le foto buone sono meno di sei.

Limiti verificati: il contenuto delle storie in evidenza da sloggati non si
apre, quindi la scheda ha solo i titoli. La pagina di Instagram non può
mandare dati a un server locale, quindi chi guida il browser copia il JSON su
file; un URL copiato male si riconosce perché lo script lo scarta come «file
finto» o «scaricamento fallito».

## 3. Cancelli

`python3 01-Coding/strumenti/cancelli-sito.py ~/lavoro/<nome>-site` lancia i
tre controlli sui file e poi `cancelli-telefono.mjs`, che apre la pagina a
375x812 con CPU rallentata 4 volte e misura lag e nove bocciature ricorrenti
di [[direttive-siti]]: pagina più larga del telefono, apertura di sola
scritta, numerazione delle sezioni, muro di foto, disegni inline, sottolineature,
cambi di sfondo netti, barra appiccicata al titolo, peso della pagina.

**Il lag non si misura in headless.** Su quattro siti approvati e cinque
bocciati per il lag, lo scroll dà a tutti un p95 di 17-18 ms. L'unico segnale
che separava i due gruppi è il numero di elementi della pagina:

| Sito | Verdetto | Elementi |
|---|---|---|
| Mikuma | approvato | 181 |
| NG Barber | approvato | 242 |
| Davide Milan | approvato | 273 |
| Fiftynine | approvato | 450 |
| Pilates District | bocciato per il lag | 500 |
| Emozioni di casa | bocciato per il lag | 526 |
| Marta Cesena | bocciato per il lag | 685 |
| Groavel | bocciato per il lag | 693 |
| My Balance | bocciato per il lag | 1625 |

Sono nove siti, quindi sopra i 480 elementi il cancello avvisa e non blocca.

## Contraddizioni aperte con processo-siti

- `processo-siti` rende obbligatori «la grafica inventata e lo scroll-telling»,
  e `controlla-sito.py` chiede almeno 3 `<svg>` inline o un racconto
  tipografico. Nicola ha scritto più volte di non disegnare niente noi
  ([[direttive-siti]], 12/10 e 23/10). In `cancelli-sito.py` quei due
  controlli escono come CONTRADDIZIONE e non bloccano, finché Nicola non
  decide.
- Lo starter dice «nessun componente, nessuna sezione». Il catalogo di sezioni
  approvate lo contraddice per costruzione.
- `processo-siti` divide la direzione e la costruzione fra più operatori; i siti
  riusciti li ha fatti una sola testa, con Nicola che sceglieva guardando le
  tavole.

## Collegamenti

[[processo-siti]] · [[direttive-siti]] · [[strumenti]] · [[trappole]] ·
[[sito-ngbarber]] · [[sito-fiftynine]] · [[sito-mikuma-dogs]] · [[sito-davidemilan]]
