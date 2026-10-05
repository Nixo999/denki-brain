---
type: progetto
riga: Bozza sito Studio fotografico JPP, Merate. Tre mondi in dodici tavole guardabili in locale (05/10), niente online; Nicola deve scegliere.
status: attivo
client: jpp-merate
stack: html-css-js
started: 2026-10-05
deadline: 2026-10-06
updated: 2026-10-05
source: claude
verificato: 2026-10-05
tags: [sito, bozza, fotografia, merate, instagram]
---

# Sito Studio fotografico JPP — bozza, Merate

Cartella `~/lavoro/jpp-merate-site`, dallo starter. **Repo solo locale**, nessun
remote, niente online. Cliente: [[jpp-merate]]. La chiamata di Patrick con
Stefania è attesa il 06/10 fra le 17 e le 19: la bozza serve per allora.

## Cosa c'è nella cartella

- `PRODUCT.md`: la verità di prodotto, scritta dal direttore.
- `COPY.md`: il copy frase per frase, impersonale, coi segnaposto `[TRA QUADRE]`
  dove il dato manca. Si inserisce com'è.
- `raccolta/` (fuori da git): `RACCOLTA.md` con le parole loro, i quattro
  pacchetti testuali, 17 recensioni Google, i conflitti tra fonti;
  `foto/MANIFESTO.md` con 30 foto sopra i 1080 px, guardate una per una.
- `MONDI.md`: i tre mondi dell'operatore di direzione (Opus).

## Il materiale, in una riga

Due registri di foto: colore pieno su fondali ocra e terracotta per famiglie e
bimbi, bianco e nero su fondo scuro per maternità e neonati. Colore loro: malva
`#823c78` con crema-oro e pesca. Logo al tratto a 500 px, vettoriale assente.
Concorrenti: [[competitor-siti-fotografi]] (48 siti; in Italia nessuno dà
acconto e disdetta, 3 su 31 i tempi di consegna).

## I tre mondi (`MONDI.md`, seed impeccable `039ca394`)

- **A «Uno, due, tre, stella»**: in studio si scatta giocando a 1-2-3 stella.
  Apertura: la conta su malva, lampo, la silhouette `gm-1` si ferma nitida.
  Malva a tutto campo, Shrikhand + Figtree. Rischio: festa di compleanno.
- **B «Il fondale»**: ogni sezione ha il colore del fondale della sua foto.
  Apertura: scende il rotolo ocra, si accende la luce, due tagli a terracotta
  e nero. Lexend Giga + Lexend. Rischio: dipende dai volti dei bambini.
- **C «Il libro fustellato»**: cartoncini con un foro che si apre come un
  diaframma, linguette come indice. Gabarito + Onest. Rischio: spostabile su
  un altro fotografo per bambini.

L'operatore raccomanda A coi campi di B. **La scelta è di Nicola, `TODO`.**

## Le tavole (05/10) — in locale, niente online

Dodici comp in `sorgenti/tela/project`, quattro per mondo: apertura in quattro
battute, apertura animata, telefono, computer. Si guardano col visore:

```bash
cd ~/lavoro/jpp-merate-site/sorgenti/tela && python3 -m http.server 8793 --bind 127.0.0.1
```

Nicola ha fermato la pubblicazione sulla tela Claude Design («non pubblicare 3
siti diversi online», regola in [[direttive-siti]]): le opzioni si mostrano in
locale. Sulla tela privata <https://claude.ai/artifact/CQywDvzNzfnZSJyqEKMj7s>
restano 16 foto e i due loghi caricati prima dello stop, nessuna tavola.
Le foto del visore stanno in `sorgenti/tela/_blob`, fuori da git.

Bocciata il 05/10 la foto della famiglia con la giacca arancio
(`canva-famiglia-colore-2400`): non si usa. In C apre la bambina con la
macchinetta giocattolo.

## I giri

- **Giro 0** (05/10): raccolta e concorrenti su Sonnet, direzione su Opus.
  Nessun codice del sito ancora.

## Da chiedere a Stefania

Liberatoria per i minori nelle foto · prezzi veri (12 mesi 390 o 490 €,
famiglia 280 o 350 €, buono 120 o 315 €) · tempi di consegna · acconto e
disdetta · giorni per il newborn · come si riconosce l'ingresso · ruolo di
Massimo e cognomi · file del logo · foto di stampe, tele e album.

## Non verificato

Storie in evidenza e post oltre i dodici (serve il login) · il video YouTube
«Dentro il perché del nostro lavoro», non trascritto · che la donna con le due
macchine fotografiche sia Stefania.
