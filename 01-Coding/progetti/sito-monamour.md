---
type: progetto
riga: Bozza di sito per Mon Amour (Dalmine, BG). Giro 1 del 24/10, «Il giorno della festa, in ordine»; Astro con GSAP; online su monamour-dalmine.netlify.app.
updated: 2026-10-24
source: claude
status: attivo
client: monamour
stack: Astro 5, GSAP ScrollTrigger, Lenis
started: 2026-10-24
deadline: TODO
---

# Sito Mon Amour

Bozza di sito vetrina a una pagina per il negozio Mon Amour di Dalmine, costruita il 24/10/2026 dopo la risposta al DM di Patrick. Cliente: [[monamour]]. Il processo è quello di [[processo-siti]]; le bocciature già date stanno in [[direttive-siti]], e il lavoro gemello del giorno prima è [[sito-laperegina]].

**Cartella**: `~/lavoro/monamour-site`, repo privato `Nixo999/monamour-site`, ramo `main`.
**Online**: <https://monamour-dalmine.netlify.app> dal 24/10/2026, sito Netlify `monamour-dalmine` (id `66a827b7-4e2d-4358-ac4b-2ea27f048d56`), deploy a mano; i tre sbarramenti sono attivi.

## Cosa c'è da sapere sul cliente

Negozio di bomboniere che segue l'evento intero: partecipazioni, palloncini e fiori, confettate, bomboniere, regali. Le recensioni nominano Antonella e la figlia Noemi. Google 4,9 su 5 con 172 recensioni. I fatti, gli orari discordanti e i rischi stanno in [[monamour]]. Le fonti sono in `riferimenti/LEGGIMI.md` e in `PRODUCT.md` del repo. Il confronto con altri siti del settore sta in [[competitor-siti-bomboniere]].

## Il giro 1 (24/10/2026): «Il giorno della festa, in ordine»

- **Il mondo**: il modo di lavorare del negozio. Seguono una festa dall'inizio alla fine e ogni servizio arriva in un momento preciso della giornata. La pagina racconta quella giornata in cinque tappe: prima (partecipazioni e coordinato grafico), la mattina (allestimento), a tavola (confettata), al saluto (bomboniera), il giorno dopo (smontaggio e ritiro). Il secondo tratto è che ogni festa ha il suo colore, e le schede delle feste lo mostrano.
- **L'apertura** (1,6 secondi a ogni caricamento): schermo pieno del malva-talpa del logo, «Mon Amour» in corsivo si scrive da sinistra a destra, poi il campo si divide in due metà che scorrono via come un nastro che si scioglie. Sotto c'è già l'hero con un fondo di palloncini di luce sfocati (shader WebGL, con una riserva in CSS).
- **La spina dello scroll**: il binario del giorno, una linea orizzontale con cinque fermate. Da computer la sezione resta fissa per al massimo due schermate e il cursore avanza con lo scroll; da telefono sono cinque blocchi impilati, ciascuno col suo colore. Dentro «A tavola» compaiono uno per volta i cinque confetti della tradizione, uno per ogni augurio. Nessun disegno a mano.
- **Palette**: avorio `#F6F1EA`, malva-talpa `#8F796E` misurato sul logo, pastelli cipria `#E8C4C4`, polvere `#BFD0E6`, acqua `#A9DCD3` e lino `#E2D6C2`, oro `#B8963E` come accento unico, inchiostro `#2B2422`.
- **Font**: Bodoni Moda per i titoli, Figtree per il testo, Monsieur La Doulaise per il corsivo del nome e una sola parola per sezione.
- **Come è organizzata la costruzione**: Trevis (su Fable) ha scritto la direzione dopo aver guardato i riferimenti a 375 pixel, cioè su un telefono. Un operatore Sonnet ha fatto la raccolta, un secondo la ricerca sui concorrenti, uno lo scheletro del progetto e un altro le foto con le note. Poi due operatori Opus hanno lavorato in parallelo, uno sulla pagina e uno sul movimento, legati da un contratto sulla struttura della pagina scritto in `direzione/contratto.md`.

## Com'è andata la verifica

`controlla-sito` 8/8, `controlla-slop` OK con quattro avvisi (parole da densità e il superlativo «straordinarie» dentro una recensione citata alla lettera), `controlla-testo` OK con una frase di 34 parole. Trevis ha guardato l'apertura campionata a cinque istanti con `cattura-apertura.mjs`, le catture a fette a 1440 e a 375 e la pagina viva nel pannello dell'app a 1440 (pin delle tappe, bokeh, console) e a 375 (hero, carosello delle feste, negozio). Dopo il primo sguardo: il cambio di tappa nel pin faceva vedere i due testi sovrapposti a metà dissolvenza (ora quella che esce sparisce in 0,12 s e quella che entra appare con 0,1 s di ritardo) e la foto dell'hero da computer era grande (colonna a 340 px). Online dal 24/10 su <https://monamour-dalmine.netlify.app> (Netlify `monamour-dalmine`, id `66a827b7-4e2d-4358-ac4b-2ea27f048d56`, deploy a mano: `npm run build` e `netlify deploy --dir dist --prod --no-build --site 66a827b7-4e2d-4358-ac4b-2ea27f048d56`); i tre sbarramenti verificati con `curl`. Non provati: iPhone vero, Safari, tablet fra 768 e 1023 px, la pagina senza JavaScript.

Da sapere se Nicola lo chiede: l'avorio sul malva del logo fa 3,6:1, quindi sul malva c'è solo testo grande e il piede è in malva scuro; l'oro non porta mai testo; la recensione di Sara Rigamonti è tagliata con «[…]» per togliere un «Inoltre»; 11 ritagli hanno un nome di cliente leggibile, elencati in `assets/img/LEGGIMI.md`; la copertina Facebook con la ragazza non è usata.

## Da chiedere nel DM

Prezzi e fasce; nome, cognome e ruolo di Antonella e Noemi; anno di apertura; orari validi e chiusura estiva; chi gestisce `monamourbomboniere.it`; foto di vetrina, ingresso e banco senza persone; permessi per le foto con nomi di clienti e per la copertina Facebook; logo in vettoriale e nome del corsivo; come e con quanto anticipo si prenota; dove e a quanto spediscono; raggio degli allestimenti; quanto va in beneficenza con la linea solidale. Elenco completo in `riferimenti/LEGGIMI.md`, sezione 12.

## Collegamenti

[[monamour]] · [[processo-siti]] · [[competitor-siti-bomboniere]] · [[direttive-siti]] · [[sito-laperegina]]
