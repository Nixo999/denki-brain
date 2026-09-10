---
riga: Pizzeria Lobidù, pizzeria siciliana, Via IV Novembre 13, 21049 Tradate (VA).
type: progetto
status: bozza-locale
cliente: "[[pizzeria-lobidu]]"
created: 2026-09-10
updated: 2026-09-10
source: claude
repo: da creare (`lobidu-site`, privata)
tags: [sito-vetrina, bozza, ristorazione, varese]
---

# Sito Pizzeria Lobidù — bozza non commissionata

**Pizzeria Lobidù**, pizzeria siciliana, Via IV Novembre 13, 21049 Tradate (VA).
Instagram `@pizzeria_lobidu` (258 follower, 12 post, quasi tutti reel di
preparazione). Nessun sito: linktree con TheFork, WhatsApp, Maps, Facebook.
Il lead ha risposto al DM il 10 settembre 2026: «Buon giorno, se senza impegno
me la mandi pure. Grazie». La bozza è la risposta.

Nicola, 10 settembre: «simile a quello per la pizzeria [Tarilli], pizze volanti
prese dalle sue foto, professionale, pieno di animazioni, animazione
all'apertura; Fable dirige, Opus esegue» (stessa modalità di [[sito-da-caterina]]).

## Dati verificati (fonte fra parentesi)

| Cosa | Dato | Fonte |
|---|---|---|
| Telefono | 0331 386967 | Google Maps, reel 4 set 2026 |
| WhatsApp ordini | 333 864 1860 | linktree |
| Tavolo | TheFork `pizzeria-lobidu-r828650` | linktree, Google |
| Email | mircolobianco@outlook.it (personale) | linktree |
| Google | 4,2 su 168 recensioni, 10–20 € | Google Maps |
| Servizi | sul posto, ritiro, consegna | Google Maps |
| Orari | mer→lun 18–22, martedì chiuso | Google Maps, **non il titolare** |
| Claim | «La Sicilia a casa Tua» | linktree |
| Cannolo | «non solo si mangia, ma anche si beve» | post del proprietario, 28 apr 2026 |

⚠️ Listini «Servizio al Tavolo» e «Asporto e Consegna 2026» sul linktree hanno
link vuoti: **nessun prezzo di pizza è pubblico**, il sito non ne scrive.
⚠️ Le pagine dei post con `curl` sono vuote (login): foto a 640 px dal pannello,
più le 11 di Google Maps a 1600.

## Direzione (brief del direttore, giro 1)

Mondo «la sera in pizzeria»: crema caldo, bruno, rosso del logo contato,
Fraunces + DM Sans. Hero con 5–6 pizze tonde in orbita e parallasse (meccanica
di Tarilli), apertura con sipario e pizze che volano dentro, stato
aperto/chiuso calcolato dagli orari (meccanica di Caterina). Sezioni: pizze ·
Sicilia a casa tua (tavolo, asporto, consegna, cannolo, birre) · recensioni ·
dove e orari · footer con firma. Pagina di decisione di impeccable **saltata**:
la direzione è imposta dal brief (riferimento esplicito di Nicola).

## Com'è andata, in tre giri

**Giro 1 bocciato** da Nicola: «le foto che fluttuano nella hero sono fatte
malissimo, ritagliate giuste, usa il loro sfondo, non le voglio più che si
muovano». Ritagli con Vision da anteprime a 640 px sopra la meccanica di
Tarilli: la falla di Caterina v1 ripagata (in [[trappole]]). Operatore
fermato prima del rapporto.

**Giro 2**: niente ritagli, `assets/tondi/` cancellata, GSAP tolto. Hero a
griglia: testo a sinistra, tre foto intere in cornice a destra (una grande,
due piccole), entrata una volta sola e poi `transform: none`. Sotto i 760 le
foto in flusso sotto i CTA. Commit `9f686ca`.

**Giro 3**, finish review `fix` con otto punti, tutti applicati: pizza intera
(salsiccia e cipolla) al posto del macro nell'hero, galleria densa con celle
alte su due righe, via la cella «zucca e porcini» (ingredienti inventati),
filetti gialli e rosso contato, alone unico sull'hero, «Lobidù» testo anche a
375, hero 5/7. Commit `9c30e33`. Misure: overflow 0 su sei larghezze, fondo
foto hero 786 a 1440×900, galleria 0 slot vuoti, contrasti da 5,5 a 15,1,
console vuota. `DESIGN.md` dal documenter.

## Stato

✅ Sito costruito e misurato, commit locale `9c30e33`. ⬜ Repo remota e
Netlify: in attesa del via di Nicola. ⬜ Safari su iPhone. ⬜ Orari da
confermare col titolare. ⬜ Due sorgenti a 360 px (forno, melanzane): da
chiedere le foto originali. ⬜ DM di risposta: Patrick.

## Collegamenti

[[sito-osteria-tarilli]] · [[sito-da-caterina]] · [[processo-siti]] · [[trappole]]
