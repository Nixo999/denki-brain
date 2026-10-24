---
type: progetto
riga: Bozza sito per Jade Tattoo (@jadetattoo.ink_, blackwork e dark fantasy, Bergamo) - mondo «Bestiario + stencil», disegni = suoi tatuaggi vettorializzati.
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

Cartella `~/lavoro/jadetattoo-site`, ramo `main`, solo locale (nessun remoto
GitHub al 24/10). Scheletro Astro estratto da laperegina-site al commit
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
bestiario con dentro la scena dello stencil: sipario nero sul nome, campo
d'inchiostro in shader, la falena che si disegna nel viola dello stencil
(`#9185D1`, misurato sull'anteprima del reel del 21/10) e diventa nero pieno,
poi le sue creature I-VI, poi il DM. Font Metamorphous e Cormorant. La
direzione per esteso sta in `direzione/DIREZIONE.md` del repo.

## Collegamenti

[[processo-siti]] · [[direttive-siti]] · [[competitor-siti-tattoo]] ·
[[sito-p0t-tattoo]] · [[sito-soul-ink]] · [[registro-interventi]]
