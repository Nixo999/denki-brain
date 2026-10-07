---
type: progetto
riga: Bozza sito Luiza Lash Artist, extension ciglia, Torino. Mondo «Il ventaglio», online su cigliadiluiza.netlify.app dal 07/10, metodo a pezzi in parallelo su Fable.
status: attivo
client: ciglia-di-luiza
stack: html-css-js
started: 2026-10-07
deadline: TODO
updated: 2026-10-07
source: claude
verificato: 2026-10-07
tags: [sito, bozza, ciglia, torino, instagram, metodo]
---

# Sito Luiza Lash Artist — bozza, Torino

Cartella `~/lavoro/ciglia-di-luiza-site`, **repo solo locale**, nessun remote.
Online su <https://cigliadiluiza.netlify.app> (team `nicola-la-rezza`, id
`6e289b6a-b3d9-4761-b801-b0b65e4a2538`), tre sbarramenti attivi. Cliente: `@ciglia.di.luiza_`
(611 follower, 437 post, nessun sito, si prenota solo in DM). Ha risposto al DM di Patrick il
07/10: «ciao sì!». Il DM col link è di Patrick.

## Il materiale
5 foto uniche da Instagram sloggato, 4 usabili (macro d'occhio di clienti, 1440-3072 px) + una di fiori;
5 caption su 12 hanno testo, tutte di 1-6 parole. Prezzi, indirizzo, orari, WhatsApp, recensioni: non
pubblicati. Il sito non dipende dalle foto: le ciglia sono SVG disegnati. Concorrenti: tutti sans geometrici
e frasi fatte; il buco è la parte seria del mestiere in prima persona.

## Il metodo (nuovo, 07/10) — `monta.py` + `parti/`
Raccolta e concorrenti su Sonnet (due in parallelo) → **direzione su Fable** (`DIREZIONE.md`: due mondi, token,
font provati a 375 px, mappa dei file, regole mobile, apertura a battute) → sei costruttori Fable in
parallelo, **un file per operatore** in `parti/NN-nome.{html,css,js}` con contratto in `BRIEF-OPERATORI.md`
→ `python3 monta.py` assembla `index.html`, `stile.css`, `sito.js`; `monta.py /tmp/x` fa un'anteprima isolata.
Tempi reali: raccolta 10 min, direzione 18, costruzione 10-14, **circa 70 minuti** in tutto, non 30: la
direzione è il pezzo lungo. Due operatori su sei si sono bloccati dopo aver scritto i file (watchdog).

## Mondo e scelte
«Il ventaglio»: mascara `#15100e`, osso, rosa `#ff5c8a` solo sull'azione; Imbue (display) + Ysabeau (testo).
Sezioni: occhio (apertura 1,7 s), effetti (8 trattamenti, pin con scrub sul PC), ventaglio, seduta, lavori, DM.

## Misurato (07/10)
`controlla-sito` 8/8, `controlla-slop` 0 bloccanti, `controlla-testo` 0. 375: nessun overflow, tap ≥44, apertura
1700 ms, selettore effetti ok. 1440 guardato a fette (pin dei passi ok). Console pulita.

## Da fare
iPhone e Safari veri · reduced-motion vero · 768 e 1024 mai guardati · hero desktop piccolo · differenza fra
3D/4D/5D poco leggibile nel disegno · parole «qualità» e superlativi (avvisi slop) · polish impeccable ·
verdetto di Nicola.

## Da chiedere a Luiza
Prezzi, durata, indirizzo e cos'è «To Dream», orari, WhatsApp, nome del corso/certificato, foto migliori
(servono originali), se lavora da sola o con lo studio di @iamgiuliaandrealashbar.
