---
type: progetto
riga: Bozza sito Jade Tattoo (blackwork, Bergamo): giro 1 «Bestiario + stencil» su jadetattoo.netlify.app, 8/8, disegni = suoi tatuaggi.
status: attivo
client: jadetattoo
stack: astro
started: 2026-10-24
deadline:
updated: 2026-10-24
source: claude
tags: [sito, bozza, tattoo, bergamo, instagram]
---

# Sito Jade Tattoo — bozza, Bergamo

Cartella `~/lavoro/jadetattoo-site`, ramo `main`, nessun remoto GitHub
(24/10). Online su <https://jadetattoo.netlify.app>. Scheletro Astro estratto da laperegina-site al commit
`7040661`. Lei viene dalla lista del 23/10
(`02-Sales/liste/2026-10-23-instagram-siti-bg-tatuatori.csv`): il 24/10 ha
risposto a Patrick che la bozza la vuole vedere su Instagram.

## Cosa sappiamo

Profilo letto da sloggati il 24/10/2026 nel browser dell'app; il dettaglio sta
in `RACCOLTA.md` e `PRODUCT.md` del repo.

- Bio: «✧Tattoo Artist Bergamo✧ / ✦ JADE TATTOO ✦ / • Blackwork & dark fantasy
  / 📍 Bergamo @k_woky_ink / ✦ Custom tattoos & Flash / ↓ BOOKING / INFO».
  376 follower, 27 post, nessun link in bio. Prenotazioni in DM.
- Storie in evidenza: feedback, studio, healed, available, booking, aftercare,
  altri, process. Da sloggati non si aprono.
- Immaginario: teschi, falene, lame, spine, corna, donne dagli occhi bianchi e
  lacrime nere, clessidre, ornamentale e neo-tribale. Solo nero.
- **Dove tatua non è sicuro.** La bio tagga K-woky Ink (viale Ernesto
  Pirovano 2/E, Bergamo, tel. dello studio 351 031 6403), ma i post da
  ottobre 2025 a luglio 2026 sono geotaggati «The Factory Tattoo Studio» di
  Romano di Lombardia. Il sito dice «Bergamo» e nessun indirizzo.

## Cosa non c'è, e si chiede a lei

Prezzi, caparra, età minima, giorni in studio, cognome, contatti suoi, il
contenuto delle storie booking, aftercare e available, i flash disponibili,
dove tatua oggi, l'ok sulle foto in studio (sono di @monicahurtado.ph e
kinko.photography) e sulle foto dei clienti riconoscibili (nuca, petto).

## Foto e disegni

16 foto del feed a 1440 px (`assets/img/`, copie da 800 in `assets/img/800/`).
I disegni del sito **sono i suoi tatuaggi vettorializzati**, non disegni
nostri: `scripts/traccia.mjs` fa soglia adattiva sull'inchiostro più potrace e
scrive SVG a un colore. Sette puliti (clessidra, sterno, spine, pipistrello,
nuca, falena, due volti), il montone no (petto peloso, puntinato fine).
Parametri di ogni disegno in `assets/img/LEGGIMI.md`.

## Skill

Cercate il 24/10 con `npx skills find` su sette parole chiave. Installata
`anthropics/skills@algorithmic-art` (89K installazioni). Scartate
`image-to-svg` (123 installazioni, sotto la soglia di mille della regola del
23/10), `eachlabs/tattoo-design-generation` e i generatori di immagini (chiavi
API a pagamento). Già installate e usate: `shader-glsl`, `gsap-plugins`,
`svg-animation`.

## Il mondo scelto — «Bestiario + stencil»

Tre mondi proposti da un operatore su Fable (`direzione/MONDI.md`): «Lo
stencil», «Il foglio di flash», «Il bestiario». Nicola ha scelto il 24/10 il
bestiario con dentro la scena dello stencil: sipario sul nome, campo
d'inchiostro in shader, la falena che si disegna nel viola dello stencil
(`#9185D1`, misurato sull'anteprima del reel del 21/10) e diventa nero pieno,
poi le sue creature I-VI, poi il DM. Font Metamorphous e Cormorant. La
direzione per esteso sta in `direzione/DIREZIONE.md` del repo.

## Giro 1 (24/10, sera) — com'è fatto

Commit `1a5b9f5`. Online su <https://jadetattoo.netlify.app> dal 24/10 (progetto Netlify `jadetattoo`, id `0175938f-a64f-421f-aa37-0231654c4485`, team denkicode; si ripubblica con `npm run build` e `netlify deploy --dir dist --prod --no-build --site 0175938f-…`), con i tre sbarramenti verificati con `curl`. Costruito da due operatori Opus in parallelo
(«pagina» e «motion», contratto di DOM in `direzione/contratto.md`).

- **Apertura** (1,7 s, CSS): sipario color osso con la falena stampata a
  contorno viola e «Jade Tattoo» in nero; le lettere salgono, poi le due metà
  si aprono e sotto il nome è già in osso sull'hero nero.
- **Hero**: nome a tutta larghezza (91 px a 375), foto di Jade 200×250 che
  entra sotto «Tattoo», striscia dei sei sigilli che porta alle voci.
- **Spina**: «Dal viola al nero» (la falena prima contorno viola, poi nero
  pieno; da computer pin di una schermata in scrub, sul telefono una volta
  sola), il bestiario I-VI a campi alternati nero e osso, «Prenota il tuo
  pezzo» con il campo d'inchiostro. Poi lo studio, nero pieno e filigrana, le
  storie in evidenza, il piede.
- **Testi** in prima persona, come lei su Instagram; «Booking aperte» è di una
  didascalia di luglio e non si usa.
- **Misure**: overflow zero a 375 e 1440, controlli 8/8, testo 0, slop 0
  blocchi; apertura e scena guardate dal video a 390×844.
- **Per il DM**: `consegna/jade-tattoo-telefono.mp4` (28 s, 1080 di
  larghezza) e quattro fermi, fatti con `scripts/video-telefono.mjs`.

Correzioni del direttore dopo il primo giro dei costruttori: la falena usciva
come sagoma nera piena (mancava `fill-rule="evenodd"`), il sipario era nero su
nero e invisibile, l'hero era una scatola vuota, il bestiario da computer era
troppo piccolo. Safari e iPhone veri mai provati.

## Collegamenti

[[processo-siti]] · [[direttive-siti]] · [[competitor-siti-tattoo]] ·
[[sito-p0t-tattoo]] · [[sito-soul-ink]] · [[registro-interventi]]
