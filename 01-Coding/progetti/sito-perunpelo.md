---
type: progetto
riga: Bozza sito Per un Pelo (toelettatura di Ambra Longoni, Nembro BG), lettere che si pettinano. Giro 2 online su perunpelo.netlify.app.
status: attivo
client: perunpelo
stack: html-css-js
started: 2026-09-25
deadline:
updated: 2026-09-25
source: claude
verificato: 2026-09-25
tags: [sito, bozza, toelettatura, pet, nembro, bergamo, instagram]
---

# Sito Per un Pelo — bozza, Nembro (BG)

Cartella `~/lavoro/perunpelo-site`, dallo starter. Repo `Nixo999/perunpelo-site`
privata, online su <https://perunpelo.netlify.app> con i tre sbarramenti. Il
cliente sta in [[perunpelo]]: ha risposto al DM di Patrick il 25/09 e aspetta
la bozza.

## Il metodo, con più modelli

Regola di Nicola del 25/09, in [[direttive-siti]]: «usa sempre il nuovo metodo
per iusare pochi token». Raccolta del profilo e inventario di 15 competitor su
**Sonnet**, in parallelo ([[competitor-siti-toelettatura]]). Tre mondi e
costruzione sullo **stesso operatore Opus**, così la catena di skill si carica
una volta sola. Il direttore ha letto solo `RACCOLTA.md`, la sintesi dei
competitor e `MONDI.md`.

## Il mondo scelto — «Per un Pelo»

Seed di impeccable `9c3ba0e1`. Tre mondi proposti in `MONDI.md`: «La scheda»,
«Per un Pelo» e «La tenda». Il terzo è scartato perché lo zoom sull'unica
illustrazione a 1440 px la sgrana.

**La metafora.** Il pelo entra arruffato ed esce pettinato. Lo fa il carattere:
Shantell Sans ha gli assi Bounce e Informality, le lettere saltellano storte e a
zero si mettono in riga. È l'unica lingua di movimento della pagina.

- **Apertura** (1,65 s, a ogni caricamento, si salta al tocco): «Per un» e
  «Pelo» arrivano arruffati dai due lati, si fermano per un pelo e si pettinano.
- **Testa a tre livelli**: «PELO» enorme dietro, Spillo in mezzo, il nome
  davanti, con parallasse.
- **La passata**: Bagno, Tosatura, Taglio e Prima volta. Una fascia
  (`clip-path` su due copie della parola) pettina la parola una volta, a tempo,
  quando entra. Dal giro 2 niente pin: sul telefono quattro blocchi, a 1440 una
  fila con le foto grandi sfalsate.
- Poi Ambra, con l'illustrazione del 2023 e le sue parole. Le recensioni: 5,0
  su 102 e sei citazioni vere. Dove e orari, con la riga di oggi segnata. In
  fondo «Prenota», che compone il messaggio WhatsApp con nome, razza e servizio.
- Palette `#EAA2C6` rosa del marchio come fondo, `#3A1128` bacca come
  inchiostro, `#FBEAF2`, `#D65C9B`. Font Shantell Sans variabile e Hanken
  Grotesk.

Innesti del direttore: il messaggio WhatsApp composto e la riga di oggi, presi
dal mondo «La scheda». Contenuto solo verificato: stripping e forbice sono
fuori perché non risultano da nessuna fonte.

## Giri

| Giro | Chi | Cosa |
|---|---|---|
| 1 | operatore Opus | costruzione, `2f3dd7c` |
| 1-bis | direttore | virgola di «5,0» sopra «102 recensioni», blocco di Ambra vuoto a 1440 riempito con le sue parole del 2023, `ad922e5` |
| 2 | operatore Opus nuovo | verdetto di Nicola sul giro 1 (PC vuoto, scroll che trattiene sul telefono, foto lente): pin tolto ovunque, servizi in fila a 1440, foto in WebP, `847e857` |

## Misurato

| Cosa | Valore |
|---|---|
| Livello | 8/8, slop 0, testo 0 (giro 1 e giro 2) |
| Scroll a 375 | 15 passi da 400 px, nessuno trattenuto; `.pin-spacer` 0 a ogni larghezza (giro 2) |
| Immagini a 375, primo caricamento | 98 KB invece di 547; la foto più grande servita al telefono pesa 27 KB invece di 179 (giro 2) |
| Overflow | 0 a 320, 375, 600, 1023, 1024, 1280 e 1440 |
| Sbarramenti | `x-robots-tag`, `robots.txt` e `meta robots` verificati con `curl` sul deploy pubblicato, file di lavoro a 404, badge spento |
| Token | Sonnet 141k + 122k · Opus 395k fra direzione e costruzione del giro 1 · Opus 191k il giro 2 · direttore Opus 5.5 |

## Da sapere prima del DM

- **Niente pin dal giro 2**: GSAP resta solo per la parallasse della testa.
  Il menu porta a sezioni vere.
- Il marchio è scontornato da `03`, a circa 450 px. Il file originale va
  chiesto ad Ambra.
- **Non verificato**: Safari e un iPhone vero; la pagina senza JS e con
  `prefers-reduced-motion` aperta davvero; il font di ripiego a CDN fredda; il
  peso delle immagini a DPR 2. Il giro 2 è misurato in Brave headless: scroll
  a passi, atterraggi del menu, opacità a 400 ms dal salto.
- `TODO` il verdetto di Nicola sul giro 2. Il DM col link è di Patrick. Le
  domande per Ambra stanno in [[perunpelo]].

## Collegamenti

[[perunpelo]] · [[competitor-siti-toelettatura]] · [[processo-siti]] · [[direttive-siti]] · [[registro-interventi]]
