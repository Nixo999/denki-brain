---
type: progetto
riga: Bozza sito Per un Pelo (toelettatura di Ambra Longoni, Nembro BG), lettere arruffate che si pettinano. perunpelo.netlify.app dal 25/9, 8/8.
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
- **La passata**: un pin con Bagno, Tosatura, Taglio e Prima volta. Una fascia
  (`clip-path` su due copie della parola) pettina la parola mentre scendi.
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

## Misurato

| Cosa | Valore |
|---|---|
| Livello | 8/8, slop 0 blocchi (3 avvisi), testo 0 blocchi (1 avviso: una frase di 41 parole) |
| Overflow | 0 a 320, 375, 600, 1023, 1024, 1280 e 1440 |
| Sbarramenti | `x-robots-tag`, `robots.txt` e `meta robots` verificati con `curl` sul deploy pubblicato, file di lavoro a 404, badge spento |
| Token | Sonnet 141k + 122k · Opus 395k fra direzione e costruzione · direttore Opus 5.5 |

## Da sapere prima del DM

- **Sul telefono i servizi non si aprono sul posto**: il menu porta alla
  parola dentro la passata. È uno scarto dalla direttiva del 25/09 su Lei
  Beauty Room (sezioni chiuse che si aprono dal menu), scelto perché qui i
  quattro servizi stanno già in un pin solo e non fanno muro. Se Nicola li vuole
  a scomparsa, va rifatto.
- Il marchio è scontornato da `03`, a circa 450 px. Il file originale va
  chiesto ad Ambra.
- **Non verificato**: Safari e un iPhone vero; la pagina senza JS e con
  `prefers-reduced-motion` aperta davvero; lo scorrimento dopo il salto dal
  menu; il font di ripiego a CDN fredda. Il movimento a 375 l'ha guardato
  l'operatore nel pannello (apertura campionata, passata in cinque posizioni).
- `TODO` il verdetto di Nicola. Il DM col link è di Patrick. Le domande per
  Ambra stanno in [[perunpelo]].

## Collegamenti

[[perunpelo]] · [[competitor-siti-toelettatura]] · [[processo-siti]] · [[direttive-siti]] · [[registro-interventi]]
