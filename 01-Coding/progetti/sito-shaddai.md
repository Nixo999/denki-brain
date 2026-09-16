---
type: progetto
riga: Bozza di sito vetrina non commissionata per Shaddai Extension Lash, lash artist a Bergamo, costruita il 16 settembre 2026 dai contenuti veri del profilo Instagram.
updated: 2026-09-16
source: claude
verificato: 2026-09-16
status: attivo
client: shaddai-extension-lash
stack: [html, css, gsap]
started: 2026-09-16
deadline: 
---

# Sito Shaddai Extension Lash

Bozza **non commissionata**, cartella `~/lavoro/shaddai-site`, nessun remote e
nessuna pubblicazione: serve come gancio per il DM. Il profilo era gia' nella
lista `02-Sales/liste/2026-09-16-instagram-siti-bergamo.csv`, gancio 1, DM non
ancora inviato.

## Come e' stato estratto il materiale

Lo **scraper Apify non e' agganciato su questa macchina** (lo era su quella di
[[2026-08-30-sito-castiglione]]). Estrazione fatta dal **browser in-app gia'
loggato su Instagram**, con JS sul DOM: bio, contatori, storie in evidenza,
caption dal campo `alt` delle immagini, URL foto in piena risoluzione.

Due cose che si riusano:
- Il grid di Instagram **non carica altri post a pane nascosto** (nessun
  IntersectionObserver, la stessa trappola di Castiglione): con sette scroll il
  bottino resta quello del primo schermo, 12 immagini. Va bene per un profilo
  da 100 post, non per uno da 1000.
- La dimensione vera di una foto sta nel parametro `efg` dell'URL, che e'
  **base64**: `atob()` e dentro c'e' `regular_photo` con la larghezza. Filtrare
  cosi' separa le foto dai fotogrammi dei Reel senza scaricarle.

I fatti verificati stanno nel repo, in `BRIEF.md`.

## I fatti, in breve

- 103 post, 736 follower (16/09/2026). **Nessun sito**, l'unico contatto e'
  WhatsApp `350 926 2986`.
- Lavora **a domicilio**, zona Bergamo, suo hashtag
  `#extensioncigliasanpaolodargon` → San Paolo d'Argon.
- Bilingue italiano/spagnolo, latina, diploma «Diseño Avanzado de Pestañas»
  maggio 2024, in bio «futura lashtrainer».
- Gli effetti li nomina lei: **Natural, Arabo, V.tech, Anime, Cat Eye, Fox Eye**.
- La frase che tiene in piedi il sito e' sua: «**Il problema non sono le tue
  ciglia. E' il mapping.**»

## Foto: tre, e si vede

`ritratto-occhi-chiusi.jpg` 1440×1800, `quattro-effetti.jpg` 1350×1688 (da cui
quattro ritagli 880×422 dell'occhio senza etichetta), `shaddai-ritratto.jpg`
1080×1350 ma con testo grafico sopra. **Tutto il resto del feed sono copertine
di Reel a 640 px.** Dichiarata la strada 2 del passo 1 di [[processo-siti]]: il
sito regge su grafica inventata, non sulle foto.

## TODO — chiesti a lei, non inventati

prezzi · indirizzo o raggio del domicilio · orari · nome proprio · recensioni
testuali (stanno in una storia in evidenza)
