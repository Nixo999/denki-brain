---
type: risorsa
riga: Lo stato di DenkiCode adesso - chi, soldi, cosa e' aperto, cosa e' bloccato. Si legge a ogni sessione, si riscrive a ogni chiusura.
updated: 2026-09-19
verificato: 2026-09-16
source: denkicode
tags: [stato, fatti]
---

# I fatti — stato al 15 settembre 2026

**Questo file si riscrive, non si accumula.** È lo stato di adesso: quando un
fatto cambia si sostituisce la riga, non se ne aggiunge una sotto. La storia
sta in `05-Decisioni/` e nelle daily.

Ogni riga è marcata: **senza data** = non scade; **(data)** = vero a quel
giorno e da ricontrollare; **→** = non vive qui, vive là.

## Chi

- Patrick Sappa, 21, unica voce commerciale. **Non scrive codice e non usa il
  terminale**: quando lavora lui, il brain fa tutto da solo.
- Nicola Larezza, 22, lead dev. Scrive tutto il codice.
- Giulia Venneri, 21, cold call a provvigione. **Non ha accesso al vault.**
  **Unica persona al telefono** da oggi: ha chiuso le sue 131 righe in due
  settimane (13/09/2026), il reso conto lo deve ancora girare Patrick.
- Gabriele ed Edoardo **fuori in via definitiva** (15/09/2026): zero numeri
  chiamati in quattordici giorni, non si riprovano → [[gabriele-edoardo]]
- **Morgan, fratello di Patrick, dentro dal 15/09/2026.** Non chiama: porta
  conoscenze. Primo frutto un parrucchiere-presidio. Compenso e ore `TODO`
  → [[morgan]]
- Patrick, Nicola e Giulia lavorano e studiano: DenkiCode è il terzo impegno
  → [[team-e-vincoli]]

## Soldi

- OperO: **2.000 € da incassare** (11/09/2026) → [[sebastian-torres]]
- Albybike: sito online e **mai pagato** (11/09/2026) → [[albybike]]
- Nessuna P.IVA, prestazione occasionale. Nei testi «ricevuta» → [[vincoli-fiscali]]

## Cosa è aperto adesso (15/09/2026)

- **Edilida** (impresa edile, Travagliato BS) ha **compilato il modulo della
  ricerca il 18/09**: strumenti che non si parlano, sito vecchio, il
  beneficio più grosso sulle **scadenze di attrezzature e sicurezza**. Enrico
  ha lasciato la mail e il sì a essere avvisato. **Patrick punta a una
  videochiamata**: mail lunedì 21 mattina presto, recupero giovedì 24; **il riepilogo di zona promesso a due (Penta, Edilida) non esiste**
  e il form ha 2 risposte in tutto → [[edilida]]
- **V-BAG, gestionale con login** pushato il 16/09 (`28f51ad`): Giulia
  pubblica dal telefono via Netlify Function + commit su GitHub. **Spento
  finché Nicola non mette `ADMIN_PASSWORD` e `GITHUB_TOKEN` su Netlify.**
  Palette (11 colori) e manici (9) disegnati in SVG, WhatsApp `3924944950`
  → [[2026-09-16-vbag-gestionale-login]]
- **Barbershop SNIA, il parrucchiere-presidio via Morgan** (Andrea, Cesano
  Maderno): sito gratis in cambio di volantini e passaparola, nessuna
  percentuale. Online su `barber-shop-snia.netlify.app`, che **si pubblica da solo dal
  repo**: giro 16 del 19/09 con la targa **ricostruita in SVG** come logo, doghe e
  palladiana come pattern SVG, listino letto dalla vetrina. Il giro 15 (foto
  come logo e sfondo) è stato bocciato: «un collage». Nicola non ha ancora
  rivisto il 16.
  Prima del go-live: consenso dei genitori per il viso del bambino nella foto
  del lavoro, o la foto si toglie → [[sito-barbershop-snia]],
  [[parrucchiere-morgan]]
- **Le 87 righe di Gabriele ed Edoardo passano a Giulia** — 27 siti/e-commerce,
  30 DenkiShift, 30 indagine, zone Groane e Vimercatese, siti riverificati a
  macchina il 13/09 → [[2026-09-13-liste-giulia-groane-vimercatese]]
- **Il reso conto di Giulia non è ancora arrivato**: senza quello le sue
  chiamate, risposte e appuntamenti restano `TODO` in [[metriche]], e oggi è
  l'unico canale che ha girato davvero
- **Mikuma Dogs** rifatto dal passo 2 col metodo nuovo e online su
  `mikumadogs.netlify.app` (11/09 sera, giro 7 «il bianco e il nero»). Nicola:
  «per il resto mi piace molto». Logo vero a 480 px, il file buono lo chiede
  Patrick. Safari su iPhone non provato → [[sito-mikuma-dogs]]
- **Lobidù** e **Da Caterina** online come bozze: zero grafica inventata,
  nessun racconto allo scroll. Sotto il livello.
- Bozze mai proposte: DSI, Atelier Selva, Salone di Andrea, Nails Mania,
  Tarilli, Fiftynine.
- **Castiglione** e **NG Barber** fermi. Il sorgente di NG Barber sta su una
  repo **pubblica**.
- **Pinkploy** (onicotecnica, Brescia) online su `pinkploy.netlify.app` (14/09),
  mondo «lo spessore», 8/8. Nicola ha bocciato solo l'hero, la correzione è
  online. Il DM col link è di Patrick, lei ha già risposto «si prova mandami»
  → [[sito-pinkploy]]
- **nails.robyy** (Roberta, nail artist e educator, Brescia) online su
  `nailsrobyy.netlify.app` (14/09), mondo A «la sezione quotata», verdetto 8/8,
  **tre sbarramenti verificati con `curl`**, due regressioni di finitura chiuse
  (`673d6c6`). Bozza **attesa**: ha risposto «Ciao ok vediamo» al DM di Patrick.
  Il DM col link è di Patrick → [[sito-nails-robyy]]
- **Laura Franzoni** (ciglia, Brescia) online su `laurafranzoni.netlify.app`
  (14/09), mondo «Dall'alto», 8/8 e overflow 0 su 27 larghezze. ⚠️ **Online c'è
  il giro 2**: il giro 3 del copy è fermo in locale (`93081ec` non pushato alle
  09:12). Il DM non è mai partito ed è di Patrick → [[sito-laurafranzoni]]
- **Hair Style Parrucchieri** (salone, Brescia, gancio sposa) online su
  `hairstylebrescia.netlify.app` (16/09), mondo A «La prova», 8/8, pin
  verificato con catture headless. ⚠️ Sbarramenti verificati nei file, non
  con `curl` (classificatore): lo fa Nicola. **Il DM non è ancora partito**
  ed è di Patrick → [[sito-hairstylebrescia]]
- **New Fantasy Parrucchieri** (Lurate Caccivio, `@newfantasy_parrucchieri`) online
  su `newfantasy-parrucchieri.netlify.app` (16/09), mondo B «l'agenda a tre
  colonne», 8/8, sbarramenti con `curl`. **Prenotazioni e gestionale interni
  al sito** su `localStorage`: la demo vale su un dispositivo solo, per venderlo
  serve uno store ospitato (una giornata). PIN area salone `1234`. Il DM è finito
  in un autorisponditore: il link va su WhatsApp, da Patrick → [[sito-newfantasy]]
- **Adelina Nails** (nail artist, Alessandria, `@nails_by_.adelina`) ha risposto
  «Ciaooo, ok» al DM del 17/09. Bozza **online su `adelinanails-site.netlify.app`** (19/09), repo privata
  `Nixo999/adelinanails-site`, giro 3 dopo una bocciatura di Nicola sul giro 1 (piatto, font anonimi), 8/8 e slop 0. Primo sito col
  metodo «prima i competitor»: contenuto solo da profilo + [[competitor-siti-nail]],
  niente inventato. Manca il DM col link (Patrick, con
  le domande su prezzi, orari, indirizzo) → [[sito-adelinanails]], [[adelina-nails]]
- **denki-agents**: piattaforma multi-agente interna. **La fase 1, il gateway,
  è chiusa** (16/09): le cinque prove della definizione di fatto passano con
  chiamate vere sul Mac, Postgres e LiteLLM in Docker, commit solo locali.
  **Prima la parte che fa i siti**: Nicola la vuole online con un login serio,
  una pagina progetti con siti e gestionali, una chat per progetto e la
  creazione dei siti autonoma con Fable e Astra. Ordine approvato: gateway,
  cantiere autonomo da riga di comando, piattaforma. **Il cantiere gira come
  meccanismo** (17/09): un giro di prova su Haiku, 0,22 USD. **Un dollaro a
  sito**, tutto in locale, foto da Instagram in automatico, i siti esistenti non
  si rifanno: deciso da Nicola il 17/09. **`pnpm run sito` sta nel dollaro**:
  tre bozze di prova su un'attivita' inventata, 0,57-0,82 USD, 8/8, critica
  4-5/10, senza foto. Manca il token di Apify per un giro con foto vere. I
  controlli anti-slop valgono per tutti i siti → [[denki-agents]],
  [[anti-slop-siti]], [[2026-09-17-cantiere-un-dollaro-in-locale]]

## Cosa è bloccato, e perché

- **Il campo «Chat» del banco DM non registra le risposte.** La riga
  `@nails.robyy` del 13/09 dice ancora che il DM è partito, non che lei ha
  risposto «Ciao ok vediamo»: la risposta è arrivata da uno screenshot di
  Nicola. Finché il banco non la scrive, un lead che ha risposto è
  indistinguibile da uno freddo (14/09/2026)

- **La migrazione dello storico di OperO non si fa piu'** (13/09/2026). Seba:
  «non e' richiesta alcuna procedura automatizzata di migrazione per i dati
  storici», settembre lo inserisce a mano lui, e di giugno-agosto vuole solo un
  **report da consultare**. OperO 2 parte vuoto: trasformazione e caricamento
  del piano non servono, **e il blocco al go-live non c'e' piu'**. Il report lo
  scrive `strumenti/report-mesi.mjs` dai JSON dell'estrazione. ⚠️ **Manca solo
  la chiave**: `OPERO1_SERVICE` da Settings → API del pannello di OperO 1,
  oppure un login di segreteria. **La digita una persona**, non Claude
  → [[opero]]
- **DenkiShift non è installabile in produzione.** Dimostrabile, non vendibile
  con una data → [[denkishift]]
- **La produzione resta fuori** su tutti e due i prodotti. Patrick applica lo
  schema solo in sviluppo → [[modifiche-al-database]]
- **Le credenziali non entrano nel vault** e non le digita Claude → [[credenziali]]
- Il collo di bottiglia è la **generazione lead**, non il closing → [[generazione-lead]]

## Il livello dei siti

**NG Barber e Fiftynine passano, gli altri no.** Dal metodo nuovo passano anche
le bozze costruite col [[processo-siti]] intero: **nailsrobyy 8/8**, pinkploy
8/8, laurafranzoni 8/8 (14/09/2026), hairstylebrescia 8/8 (16/09/2026). Prima di pubblicare:

```bash
python3 01-Coding/strumenti/controlla-sito.py ~/lavoro/<cartella>
```

Quello che è già stato bocciato sta in [[direttive-siti]], e non si ripete.
