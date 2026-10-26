---
type: progetto
riga: Sito nuovo di Pilates District (studio Reformer, Buccinasco): giro 1 «La prima lezione» online dal 26/10/2026 su pilates-district.netlify.app, Astro con GSAP.
status: attivo
client: pilates-district
stack: Astro 5, GSAP ScrollTrigger e SplitText; Netlify
started: 2026-10-26
deadline: TODO
updated: 2026-10-26
source: claude
verificato: 2026-10-26
tags: [sito, pilates, buccinasco, astro, gsap]
---

# Sito Pilates District — giro 1 «La prima lezione»

Bozza di sito vetrina per Pilates District, lo studio di Pilates Reformer di Alessandro Manzo a Buccinasco (MI), chiesta da Nicola il 26/10/2026 dopo la risposta al DM («Ciao Patrick, si mandami pure il pros…»), «seguendo le stesse istruzioni degli ultimi siti». Cliente: [[pilates-district]].

**Cartella**: `~/lavoro/pilates-district-site`, ramo `main`, nessun remoto per ora.
**Online**: <https://pilates-district.netlify.app> dal 26/10/2026 sera, con i tre sbarramenti; progetto Netlify `pilates-district` (id `115aac03-a88a-4fd7-a6f0-68bdc060088f`, team denkicode), cartella non collegata: si ripubblica con `npm run build && netlify deploy --prod --dir dist --site 115aac03-a88a-4fd7-a6f0-68bdc060088f`.
**Memoria tecnica**: `CLAUDE.md` del repo, `PRODUCT.md`, `direzione/DIREZIONE.md`, `direzione/contratto.md`.

## Chi è, in breve

Studio aperto nel giugno 2026 al secondo piano del Centro Commerciale Emilia (via Romagna 1), con accesso dall'ascensore col citofono. Sei Reformer con torre (marca Cuore), Chair e Cadillac, una lounge nera e oro. Lezioni private e mini classi da sei («Sei persone, non una di più»), prima lezione a 10 euro. Google: 5,0 su 59 recensioni. Orari di apertura lunedì-venerdì 8-21, sabato 9-12. Instagram `@pilates_district` con una grafica già decisa: verde bosco `#083F24`, oro `#DDB54C`, carta crema con nastro adesivo, serif alto in maiuscolo, scrittura a mano in oro per gli occhielli. Il resto in `PRODUCT.md` e in `raccolta/` del repo.

## Il giro 1 (26/10/2026)

- **Metafora**: la prima lezione nell'ordine vero: si sale al 2° piano, la lounge, la sala con i sei posti, sul Reformer (Chair, Cadillac: «cambiando molle, ampiezza e ritmo»), la prova a 10 euro. Luoghi e numeri veri, fotografati davvero.
- **Apertura «Si accendono le luci»**: la foto larga della sala sotto un velo nero che si schiarisce, il nome sale per lettere, poi il sipario sale.
- **Interazione firma**: l'indicatore dell'ascensore, una colonna di cinque tappe che si accendono in oro mentre si scorre; sul telefono una striscia fissa «2 di 5 · La lounge».
- **Spina**: scena sticky da 1024 con cross-fade delle foto su livelli a opacità; sul telefono cinque schemi diversi, senza scrub.
- **Cuciture**: fra chiaro e verde il bordo a pannelli (gli specchi sulla parete), che si ritira allo scroll; fra verde e chiaro una riga oro che si disegna sopra una dissolvenza. Dietro al testo una grana di carta e i pannelli degli specchi in parallasse.
- **Font**: Instrument Serif (candidati Cormorant Garamond, Fraunces), Mrs Saint Delafield per gli occhielli, Figtree per corpo ed etichette; specimen a 375 in `prove/`.
- **Niente disegni**: My Balance aveva il Reformer di `anatomy`; qui ci sono le foto vere (cinque da Google Maps a 2400 px, una da Instagram) e si usano quelle.
- **Come è stato costruito**: raccolta su Opus (Instagram senza login, Maps), concorrenti su Sonnet (letti al volo), scheletro su Sonnet; direzione di Fable; tre operatori in parallelo con un contratto di DOM: «pagina» e «motion» su Opus, «foto» su Sonnet.

## Stato

**Giro 1 online dalle 20:30 del 26/10/2026**, commit `5940674`. Misurato: `controlla-sito` 8/8, `controlla-slop` 0 blocchi (4 avvisi: gruppi di tre nelle loro frasi, i numeri «Segnale 01-03» che sono il loro formato, Instrument Serif segnalato come font abusato ma scelto su specimen perché è il più vicino al serif delle loro grafiche), `controlla-testo` 0; overflow zero a 375 e 1440; apertura 1,7 s campionata in sei fotogrammi; 60 fps in 5 s di scroll a 1440; i tre sbarramenti e i file di lavoro a 404 verificati con `curl` sul permalink del deploy. Guardato dal direttore nel pannello a 375 (dal vivo) e nelle catture a 1440; iPhone vero e Safari mai. Durante la costruzione: il raccoglitore e i concorrenti si sono fermati dalle 17:50 alle 19:20 per il limite d'uso di Opus e Sonnet; i nastri ritagliati come JPEG lasciavano un quadrato chiaro sulle schede e sono stati rifatti in PNG con trasparenza; tre frasi «non è X, è Y» (loro) bloccavano l'anti-slop e sono state tagliate; `scroll-behavior: smooth` tolto perché blocca le misure. Verdetto di Nicola: `TODO`.

## Da chiedere al cliente

Elenco preso da `PRODUCT.md`, da portare a Patrick.

- Listino della lezione privata e della mini classe, pacchetti e scadenze.
- Durata e orario delle classi (gli orari in pagina sono di apertura).
- Cosa portare alla prima lezione (abbigliamento, calze antiscivolo).
- Titoli e anni di esperienza di Alessandro; ruolo di Riccardo Camicia.
- WhatsApp e mail; se il 346 767 6321 è anche WhatsApp.
- Foto originali (sala, lezioni, ritratti), il permesso per le foto con allievi, il logo vettoriale.

## Aperto

- [x] Controlli (8/8, slop 0, testo 0) e pubblicazione (26/10 sera)
- [ ] Verdetto di Nicola dal telefono e dal Mac
- [ ] Il link nel DM lo manda Patrick

## Collegamenti

[[pilates-district]] · [[sito-mybalance]] · [[processo-siti]] · [[direttive-siti]] · [[stack]] · [[convenzioni]]
