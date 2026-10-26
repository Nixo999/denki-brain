---
type: progetto
riga: Sito nuovo di Groavel (uscite guidate in bici, Cesano Maderno): giro 1 «Da 0 a 40 km» in Astro con GSAP, costruito il 26/10/2026.
status: attivo
client: groavel
stack: Astro 5, GSAP ScrollTrigger, Flip, SplitText; Netlify
started: 2026-10-26
deadline: TODO
updated: 2026-10-26
source: claude
tags: [sito, bici, cesano-maderno, astro, gsap]
---

# Sito Groavel — giro 1 «Da 0 a 40 km»

Sito nuovo per Groavel, uscite guidate in bici con base a Cesano Maderno (MB). Il cliente sta in [[groavel]]. Nicola ha chiesto «personalità e animazioni fatte bene e pulite», su telefono e computer.

**Cartella**: `~/lavoro/groavel-site`, ramo `main`, nessun remoto per ora.
**Online**: ancora no.

## Cosa c'è oggi

Il sito attuale `groavel.com` è su Squarespace, quindi non ha repo. Era in galleria su denkicode.com e Nicola l'ha tolto il 12/09/2026 ([[sito-denkicode]]). Dalle note del vault non risulta chi l'abbia costruito: il vault dice soltanto che la firma DenkiCode andava messa dal pannello Squarespace ([[2026-09-08-firma-powered-by-denkicode]]). Il meccanico di Groavel è Alberto Sappa di Alby Bike, già cliente nostro ([[albybike]]).

## Il giro 1 di oggi (26/10/2026)

- **Metafora**: le distanze vere delle loro uscite. 0 km è la gimkana dei bambini, 10 km la Family, 25 km la Night, 40 km la Race, poi i viaggi, che si contano in giorni.
- **Apertura «la ruota»**: il badge del logo rotola in scena e vola nella barra di navigazione con Flip.
- **Ciclocomputer**: un ciclocomputer sul manubrio conta i chilometri mentre si scorre la pagina.
- **Scena sticky delle tappe**: su computer le tappe stanno in una scena fissata; sul telefono ognuna ha uno schema diverso, cinque in tutto.
- **Stack**: Astro con GSAP (ScrollTrigger, Flip, SplitText).
- **Come è stato costruito**: tre operatori Opus con un contratto di DOM scritto prima, raccolta e digest su quattro Sonnet, direzione di Fable. La direzione sta in `direzione/DIREZIONE.md` nel repo, la verità di prodotto in `PRODUCT.md`.

## Stato

**Giro 1 online dal 26/10/2026 (pomeriggio)** su <https://groavel.netlify.app>, con i tre sbarramenti; commit `ad5ce91`. Misurato: `controlla-sito` 8/8, `controlla-slop` 0 blocchi (4 avvisi: «vanta» è nel cognome Vantadori, «passione» è la loro frase), `controlla-testo` 0; overflow zero da 375 a 1440; apertura 1,8 s sulla build statica senza fotogrammi vuoti, badge sulla sede con scarto 0,5 px; 57-60 fps a 1440 in 5 s di scroll; foto ridotte sotto i 250 KB. Guardato dal direttore nel pannello a 375 e a 1440: iPhone vero e Safari mai. Verdetto di Nicola: `TODO`.

## Da chiedere al cliente

Elenco preso da `PRODUCT.md`, da portare a Patrick.

- Prezzi di corsi, uscite e viaggi.
- Sede e telefono o WhatsApp.
- Calendario 2026.
- Un file GPX di un giro.
- Forma giuridica, tessere e assicurazione.
- Foto originali e ritratti delle guide, più una foto di Alberto.
- Logo in formato vettoriale: oggi c'è solo un PNG da 1024 px.
- Chi è l'altro fondatore oltre a Gabriele Amadigi.

## Aperto

- [x] Stato di fine giro (26/10: online, verdetto di Nicola `TODO`)
- [ ] Contatto di Groavel e primo messaggio (decide Patrick)
- [ ] Repo remoto e pubblicazione: decisione del direttore

## Collegamenti

[[groavel]] · [[albybike]] · [[stack]] · [[convenzioni]]
