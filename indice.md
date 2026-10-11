---
type: risorsa
updated: 2026-10-11
source: claude
tags: [indice]
---

# Indice delle note — si legge prima di cercare

Tutte le **2464 note** del vault, per cartella, con una riga a testa. Serve a un
motivo solo: **leggere questo file costa meno che cercare in tutto il vault**, e
nove volte su dieci dice già dove sta la cosa.

**Non si scrive a mano**: `python3 01-Coding/strumenti/genera-indice.py` lo
riscrive dai file veri. La descrizione è la `riga:` che ogni nota dichiara nel
frontmatter — chi scrive la nota scrive anche come si presenta qui.

⚠️ **Il marcatore `⚠️` davanti a una descrizione vuol dire ipotesi**: la nota è
`source: claude` e nessuno l'ha ancora verificata. Si legge per orientarsi, non
si cita come fatto e non ne esce niente verso un cliente, finché una persona non
controlla e scrive `verificato:`. Vedi [[come-si-scrive-una-nota]].

Come è fatto il vault sta in `CLAUDE.md`; qui c'è solo il catalogo.

## 00-Inbox

*Catture al volo, non ancora sistemate*

- [[2026-09-27-ricerca-brain-siti-claude-code]] — ⚠️ Ricerca del 27/09/2026 su cosa adottare per brain, siti e Claude Code - classifica per resa/sforzo, con fonti. Ipotesi da verificare prima di muoversi.
- [[come-si-usa-inbox]] — ⚠️ Questa cartella è il posto dove buttare le cose senza pensarci.

## 01-Coding

*Il lato tecnico: progetti, stack, strumenti, skill*

- [[registro-interventi]] — Una riga per intervento - chi, quando, progetto, repository e QUALE DATABASE. La colonna database e' il motivo del file.
- [[trappole]] — Errori tecnici già pagati e strade scartate, per dominio. Descrittivo, non è un rulebook - le regole stanno in convenzioni.

**progetti/**

- [[co-opero-clienti]] — ⚠️ CO-OPERO lato clienti, deciso con Patrick il 30/09 - accesso, pagina Richieste in OperO, stati delle richieste, il mockup letto.
- [[co-opero-prototipo]] — ⚠️ Prototipo di CO-OPERO (1/10) sul ramo coopero di opero-sito - cosa c'è, cosa manca per mostrarlo, dove va oltre le decisioni del 30/09.
- [[denki-agents]] — Piattaforma interna multi-agente - ogni task sul suo modello via LiteLLM, costo di ogni chiamata in Postgres. Fase 1: solo il gateway.
- [[denkishift-interfaccia]] — ⚠️ Obiettivo dichiarato - un'interfaccia che si venda da sola durante la demo di Patrick, calibrata su due utenti che non sono due gradini dello...
- [[denkishift]] — Prodotto di punta, turni per squadre a orario variabile. Dimostrabile, NON installabile in produzione.
- [[opero-intermediar-receive-testo]] — Testi integrali: specifica Intermediar + Receive di Seba (24/09) e riassetto CO-OPERO portato da Patrick (30/09). La sintesi sta altrove.
- [[opero-intermediar-receive]] — ⚠️ Ecosistema OperO + CO-OPERO (30/09) sopra Intermediar + Receive (24/09) - da conoscere, non da fare. Modello, cosa dice il repo oggi, buchi.
- [[opero]] — Il prodotto che Sebastian rivende, non un gestionale nostro. Chi tocca il Super Admin tocca il suo conto economico.
- [[sito-adelinanails]] — Bozza sito per Adelina Nails (Alessandria) in ~/lavoro/adelinanails-site - contenuto solo da profilo + inventario competitor, giro 3 «lacca, oro e rilievo», Melodrama + Grape Nuts, apertura in 4 tempi, 8/8 - online su adelinanails-site.netlify.app dal 19/9 (deploy da GitHub).
- [[sito-albybike]] — Sito vetrina per Albybike, negozio di biciclette - vendita, assistenza, riparazione, abbigliamento e integratori.
- [[sito-atelier-selva]] — ⚠️ Sito per Shari Piras, tatuatrice fineline a Merate (LC), e per il suo studio privato Atelier Selva (Via Statale 147).
- [[sito-barbershop-snia]] — Sito vetrina di Andrea, barbiere al Villaggio SNIA di Cesano Maderno, che fa anche da tramite per i trapianti in Albania. Primo presidio volantini, gratis.
- [[sito-beba-evolution]] — ⚠️ Restyling del sito di Beba Evolution, parrucchiere di Barbara Tarantino a Villasanta (MB). Giro 1 «Il muro con la macchia» del 09/10.
- [[sito-cakeroyal]] — ⚠️ Bozza vetrina per Cake Royal, pasticceria cake design a Borgosatollo (BS). Torta a tre piani che si monta allo scroll, nome che va su WhatsApp.
- [[sito-castiglione]] — ⚠️ Sito vetrina non commissionato per castiglione-furniture, costruito il 30 agosto 2026 dai contenuti veri del loro profilo Instagram.
- [[sito-ciglia-di-luiza]] — Bozza sito Luiza Lash Artist, extension ciglia, Torino. Giro 3 «Da 1 a mega» (la pagina è la scala del volume della sua bio) online su cigliadiluiza.netlify.app dal 07/10, una testa sola su Fable; giri 1 e 2 bocciati.
- [[sito-claudia-dogsitter]] — ⚠️ Bozza sito Claudia, educatrice cinofila e dog sitter ad Azzano San Paolo (BG). Giro 1 «Una giornata da Claudia» dell'08/10, una testa sola su Fable.
- [[sito-custombeautynails]] — Custom Beauty Nails, onicotecnica a Treviglio (BG): bozza online su custombeautynails.netlify.app dal 16/9, mondo «Un centimetro di spazio», 21 SVG, 8/8, copy rifatto professionale dopo la bocciatura.
- [[sito-da-caterina]] — ⚠️ Da Caterina Toelettatura Professionale, Via Introzzi 8, 21057 Olgiate Olona (VA).
- [[sito-davidemilan]] — Bozza sito Davide Milan, fotografo di diciottesimi e matrimoni, Milano. Mondo A «Il provino», giro 1 del 06/10 su davidemilan.netlify.app, pubblicato da Nicola.
- [[sito-denkicode]] — Sito di DenkiCode. È qui che sta la galleria dei lavori - il posto dove si mostra a un cliente cosa abbiamo già fatto.
- [[sito-designcapelli]] — Bozza sito per Design Capelli (Nichelino, TO) - mondo «la luce della via», la pagina schiarisce di un tono a sezione, marchio composto in Pinyon Script, Cabinet Grotesk + Gambetta, apertura a 0,80 s. Online su designcapelli.netlify.app dal 21/9, giro 6, 8/8, slop 0 e testo 0.
- [[sito-dianails]] — Diana @dianails_brescia, onicotecnica e PMU a Brescia: bozza creata in C:\Users\User\Desktop\dianails-site, mondo A «la regola del 90°», 8/8 sbarramenti verificati.
- [[sito-dragonfly]] — ⚠️ Raccolta materiale per sito vetrina di Dragonfly Beauty&Relax, centro estetico a Casale Monferrato, lead da Instagram.
- [[sito-dsi-advertising]] — ⚠️ Sito vetrina in una pagina per D.S.I. Advertising di Piras Sebastiano, Merate (LC) - dal 1992 progetta e produce articoli promozionali per il...
- [[sito-fiftynine]] — ⚠️ Sito vetrina in una pagina per Bar Tabacchi Fiftynine, bar tabaccheria e pizzeria in via Nazionale dei Giovi 59, Cesano Maderno (MB).
- [[sito-hairstylebrescia]] — Hair Style Parrucchieri @hairstyle_brescia, salone a Brescia, gancio sposa - bozza online su hairstylebrescia.netlify.app dal 16/9, mondo A «La prova», 8/8, DM non partito.
- [[sito-icaarus]] — ⚠️ Bozza sito ICAARUS ASD, centro cinofilo a Brembate-Grignano (BG). Giro 1 «Il percorso» del 09/10, direzione Trevis, costruzione Opus.
- [[sito-jpp-merate]] — Bozza sito Studio fotografico JPP, Merate. Mondo C «Il libro fustellato», giro 1 online su jppmerate.netlify.app dal 06/10; chiusura su Fable, verdetto di Nicola da avere.
- [[sito-laurafranzoni]] — Laura Franzoni @laurafranzoni_lashmaker, ciglia a Brescia: bozza online su laurafranzoni.netlify.app dal 14/9, mondo «Dall'alto». Online c'è il giro 2, il giro 3 è fermo in locale.
- [[sito-leibeautyroom]] — Bozza sito per Lei Beauty Room (Torino Cavoretto) - mondo «La stanza». Online su leibeautyroom.netlify.app, giro 7: da PC il pin, sul telefono menu con i nomi e cinque stanze a scomparsa con porte diverse e tre foto vere, 8/8.
- [[sito-mikuma-dogs]] — Online su mikumadogs.netlify.app per Martina Carneli (mikuma.dogs), Como - giro 7 'il bianco e il nero', logo vero, Nicola: 'mi piace molto'.
- [[sito-minniminerva]] — Bozza sito Minerva Esposito, MUA ad Alessandria. Online dal 05/10 il giro 3 «Il velo» (bianco su bianco), verdetto di Nicola da avere.
- [[sito-mitril-tattoo]] — ⚠️ Bozza sito Mitril Tattoo & Piercing (Rovato BS, Giovi Salvi e Jennifer Galli). Giro 1 «Due mani, una pelle» del 09/10, direzione Fable, costruzione Opus.
- [[sito-nails-mania]] — ⚠️ Sito vetrina in una pagina per Nails Mania, centro di ricostruzione unghie mani e piedi di Lory Frosio a Seriate (BG).
- [[sito-nails-robyy]] — Roberta @nails.robyy, nail artist e educator a Brescia: bozza online su nailsrobyy.netlify.app dal 14/9, mondo A «la sezione quotata», 8/8, sbarramenti verificati.
- [[sito-newfantasy]] — New Fantasy Parrucchieri @newfantasy_parrucchieri, Lurate Caccivio (CO): bozza online su newfantasy-parrucchieri.netlify.app dal 16/9, mondo B «l'agenda a tre colonne», prenotazioni e gestionale su localStorage.
- [[sito-ngbarber]] — ⚠️ Bozza vetrina per ng-barber, riga 2 dell'anello 1-b delle liste Instagram, gancio 5.
- [[sito-osteria-tarilli]] — ⚠️ Osteria Tarilli, Via Ronco Nuovo 2, 6949 Comano (TI), a 300 m dalla RSI.
- [[sito-p0t-tattoo]] — Bozza sito per p0t_tattoo (Ruben, tatuatore anime e cartoon, Collegno TO) - mondo «Rodovetro × Retino», linea → puntinato → colore, Unbounded + Hanken Grotesk. Online su p0t-tattoo.netlify.app dal 24/9, giro 9 (mobile per primo, desktop pieno, testa con spessore), 8/8, slop 0, testo 0.
- [[sito-perunpelo]] — Bozza sito Per un Pelo (toelettatura di Ambra Longoni, Nembro BG), lettere che si pettinano. Giro 3 online su perunpelo.netlify.app.
- [[sito-petliving]] — Bozza sito Pet Living Toelettatura (Giussano MB, seconda sede Bovisio), lo stripping come mestiere. Chiesta da Nicola il 30/09, metodo a più modelli.
- [[sito-pinkploy]] — Online su pinkploy.netlify.app per @nails_art_by_pinkploy, onicotecnica a Brescia centro - mondo B «lo spessore», l'unghia in quota.
- [[sito-pizzeria-lobidu]] — ⚠️ Pizzeria Lobidù, pizzeria siciliana, Via IV Novembre 13, 21049 Tradate (VA).
- [[sito-salone-di-andrea]] — ⚠️ Sito vetrina in una pagina per Il Salone di Andrea, parrucchiere donna e uomo di Andrea Bielli a Dalmine (BG), Viale Natale Betelli 58.
- [[sito-shaddai]] — Bozza di sito vetrina non commissionata per Shaddai Extension Lash, lash artist a Bergamo, costruita il 16 settembre 2026 dai contenuti veri del profilo Instagram.
- [[sito-soul-ink]] — Bozza sito per Soul Ink Torino City (studio tattoo, via Cremona 27/b Torino, Franco Roggia giapponese + Alessandro Audino tradizionale) - mondo «Munewari × cartigli», giro 3 online su soul-ink-torino.netlify.app dal 26/09, 8/8, slop 0, testo 0.
- [[sito-whitelilium]] — ⚠️ Bozza sito White Lilium Photography, fotografa maternity/newborn/famiglia, Trezzano sul Naviglio. Giro 1 «Il controluce» del 07/10, una testa sola su Fable.

**skills/**

- [[design-frontend]] — ⚠️ Quattro skill di design sono installate a livello di account (~/.claude/skills/), quindi valgono in ogni cartella - OperO, DenkiShift, cococa...
- [[processo-siti]] — ⚠️ Nota di catalogo, non la skill. È il wikilink più citato del vault (quindici richiami e nessun file, fino al 7 settembre 2026) perché ogni s...
- [[proposta-commerciale]] — Nota di catalogo della skill proposta-commerciale, non la skill - preventivi WhatsApp per i siti, PDF «Piano di Sviluppo» per i gestionali.
- [[skills]] — ⚠️ Quale strumento di Claude si usa per quale lavoro.
- [[voce-denkicode]] — Nota di catalogo della skill voce-denkicode, non la skill. Esisteva solo come wikilink rotto, il piu' citato del vault (27 richiami al 27/09/2026).

**stack/**

- [[anti-slop-siti]] — ⚠️ Cosa fa sembrare un sito fatto con l'AI, dalla ricerca del 17/09/2026 - segni visivi e di testo, cosa blocca controlla-slop, cosa va guardato.
- [[competitor-siti-barber]] — ⚠️ Inventario di 15 siti (6 barber Brianza, 5 barbershop italiani noti, 4 trapianto Albania) per il sito di Barbershop SNIA (Cesano Maderno).
- [[competitor-siti-estetica]] — ⚠️ 18 siti di centri estetici (5 locali AL/VC/AT, 5 boutique italiane, 3 specialistici, 5 Torino collina) - sezioni, info reali, stile, per Dragonfly e Lei Beauty Room.
- [[competitor-siti-fotografi-eventi]] — 50 siti: diciottesimi (16), matrimoni documentari (6), eventi corporate/concerti (24), 4 premiati. Prezzi, extra, FAQ, cliché, motion.
- [[competitor-siti-fotografi]] — ⚠️ 48 siti di fotografi famiglia/newborn/maternità (16 zona Merate, 15 Italia, 12 estero, 5 premiati): sezioni, prezzi, FAQ, cliché.
- [[competitor-siti-nail]] — ⚠️ Inventario di cosa pubblicano 15 siti di nail studio (5 Piemonte, 6 Italia, 4 estero) - sezioni, formati, FAQ ricorrenti, errori. Si riusa per ogni sito nail.
- [[competitor-siti-tattoo]] — ⚠️ Inventario di cosa pubblicano 24 siti di studi/tatuatori tattoo (5 Piemonte, 5 Italia, 4 estero, + 10 Torino/giapponese) - sezioni, FAQ, parole anime/giapponese, errori.
- [[competitor-siti-toelettatura]] — ⚠️ Inventario di 15 siti di toelettatura (5 Bergamo/Val Seriana, 6 Italia curati, 4 estero) - sezioni, FAQ, vocabolario, errori. Per il sito di Ambra Longoni, Nembro.
- [[convenzioni]] — Le REGOLE tecniche di casa - naming, commit, firma Powered by DenkiCode. Qui sta il modo giusto, non gli errori.
- [[copy-siti-competitor]] — ⚠️ Ricerca su 11 siti di parrucchieri, quartiere e fascia alta: didascalie, titoli, bottoni, punteggiatura; confronto con Design Capelli.
- [[direttive-siti]] — Ogni correzione che Nicola ha dato su un sito, diventata regola permanente. Si legge prima di costruire e prima di pubblicare.
- [[essenza-e-motion]] — Essenza da Instagram, metafora, spina dello scroll, grafica inventata e foto minime 1080px. Il metro misurato sono NG Barber e Fiftynine.
- [[livello-siti]] — Le costanti visive dei siti premiati del settore, lette nei loro sorgenti il 17/09/2026 - rapporti, misure, palette. Il metro con cui si giudica un sito nuovo.
- [[scrittura-web]] — ⚠️ Regole verificabili per il testo dei siti: didascalie, leggibilità Gulpease, punteggiatura, SEO locale, microcopy, tutte con fonte.
- [[stack]] — Le tecnologie dei due gestionali. OperO Vite 8 + Tailwind 3, DenkiShift Next 16 + Tailwind 4. Restano diversi.

**strumenti/**

- [[netlify]] — Detto da Patrick il 31 agosto 2026 - *«il sito di Castiglione, come tutti i siti bozza, viene messo su Netlify per farlo vedere»*.
- [[plugin-da-valutare]] — ⚠️ Elenco ragionato, non un catalogo. Il marketplace ufficiale (claude-plugins-official, già registrato su questa macchina) ne ha 289 - qui stan...
- [[strumenti]] — ⚠️ Gli attrezzi con cui si costruisce, e come sono configurati da noi.

**strumenti/starter-sito/**

- [[LEGGIMI]] — Come si usa lo starter dei siti - cosa porta dentro (le trappole gia' pagate) e cosa non porta mai (il gusto).

## 02-Sales

*Il lato commerciale: clienti, script, liste, processo*


**banco/.netlify/plugins/node_modules/@alloc/quick-lru/**

- [[readme]] — This is a CommonJS-only fork of [quick-lru](https://github.com/sindresorhus/quick-lru).

**banco/.netlify/plugins/node_modules/@babel/code-frame/**

- [[README]] — See our website [@babel/code-frame](https://babeljs.io/docs/babel-code-frame) for more information.

**banco/.netlify/plugins/node_modules/@babel/compat-data/**

- [[README]] — See our website [@babel/compat-data](https://babeljs.io/docs/babel-compat-data) for more information.

**banco/.netlify/plugins/node_modules/@babel/core/**

- [[README]] — See our website [@babel/core](https://babeljs.io/docs/babel-core) for more information or the [issues](https://github.com/babel/babel/issues...

**banco/.netlify/plugins/node_modules/@babel/core/node_modules/semver/**

- [[README]] — semver(1) -- The semantic versioner for npm ===========================================

**banco/.netlify/plugins/node_modules/@babel/generator/**

- [[README]] — See our website [@babel/generator](https://babeljs.io/docs/babel-generator) for more information or the [issues](https://github.com/babel/ba...

**banco/.netlify/plugins/node_modules/@babel/helper-compilation-targets/**

- [[README]] — See our website [@babel/helper-compilation-targets](https://babeljs.io/docs/babel-helper-compilation-targets) for more information.

**banco/.netlify/plugins/node_modules/@babel/helper-compilation-targets/node_modules/lru-cache/**

- [[README]] — A cache object that deletes the least-recently-used items.

**banco/.netlify/plugins/node_modules/@babel/helper-compilation-targets/node_modules/semver/**

- [[README]] — semver(1) -- The semantic versioner for npm ===========================================

**banco/.netlify/plugins/node_modules/@babel/helper-compilation-targets/node_modules/yallist/**

- [[README]] — Yet Another Linked List

**banco/.netlify/plugins/node_modules/@babel/helper-globals/**

- [[README]] — See our website [@babel/helper-globals](https://babeljs.io/docs/babel-helper-globals) for more information.

**banco/.netlify/plugins/node_modules/@babel/helper-module-imports/**

- [[README]] — See our website [@babel/helper-module-imports](https://babeljs.io/docs/babel-helper-module-imports) for more information.

**banco/.netlify/plugins/node_modules/@babel/helper-module-transforms/**

- [[README]] — See our website [@babel/helper-module-transforms](https://babeljs.io/docs/babel-helper-module-transforms) for more information.

**banco/.netlify/plugins/node_modules/@babel/helper-string-parser/**

- [[README]] — See our website [@babel/helper-string-parser](https://babeljs.io/docs/babel-helper-string-parser) for more information.

**banco/.netlify/plugins/node_modules/@babel/helper-validator-identifier/**

- [[README]] — See our website [@babel/helper-validator-identifier](https://babeljs.io/docs/babel-helper-validator-identifier) for more information.

**banco/.netlify/plugins/node_modules/@babel/helper-validator-option/**

- [[README]] — See our website [@babel/helper-validator-option](https://babeljs.io/docs/babel-helper-validator-option) for more information.

**banco/.netlify/plugins/node_modules/@babel/helpers/**

- [[README]] — See our website [@babel/helpers](https://babeljs.io/docs/babel-helpers) for more information.

**banco/.netlify/plugins/node_modules/@babel/parser/**

- [[CHANGELOG]] — _Note: Gaps between patch versions are faulty, broken or test releases._
- [[README]] — See our website [@babel/parser](https://babeljs.io/docs/babel-parser) for more information or the [issues](https://github.com/babel/babel/is...

**banco/.netlify/plugins/node_modules/@babel/runtime/**

- [[README]] — See our website [@babel/runtime](https://babeljs.io/docs/babel-runtime) for more information.

**banco/.netlify/plugins/node_modules/@babel/template/**

- [[README]] — See our website [@babel/template](https://babeljs.io/docs/babel-template) for more information or the [issues](https://github.com/babel/babe...

**banco/.netlify/plugins/node_modules/@babel/traverse/**

- [[README]] — See our website [@babel/traverse](https://babeljs.io/docs/babel-traverse) for more information or the [issues](https://github.com/babel/babe...

**banco/.netlify/plugins/node_modules/@babel/types/**

- [[README]] — See our website [@babel/types](https://babeljs.io/docs/babel-types) for more information or the [issues](https://github.com/babel/babel/issu...

**banco/.netlify/plugins/node_modules/@colors/colors/**

- [[DISTRIBUTION]] — Distributed and maintained by DABH LLC.
- [[README]] — DABH — Distributed and maintained by [DABH LLC](https://dabh.llc/).

**banco/.netlify/plugins/node_modules/@commander-js/extra-typings/**

- [[README]] — This package offers TypeScript typings for commander which infer strong types for:

**banco/.netlify/plugins/node_modules/@contentful/rich-text-types/**

- [[README]] — Type definitions and constants for the Contentful rich text field type.

**banco/.netlify/plugins/node_modules/@dabh/diagnostics/**

- [[CHANGELOG]] — never used. So smaller install size, less dependencies for all.
- [[DISTRIBUTION]] — Distributed and maintained by DABH LLC.
- [[README]] — DABH — Distributed and maintained by [DABH LLC](https://dabh.llc/).

**banco/.netlify/plugins/node_modules/@dependents/detective-less/**

- [[README]] — npm install @dependents/detective-less

**banco/.netlify/plugins/node_modules/@emotion/babel-plugin/**

- [[README]] — above of Emotion.

**banco/.netlify/plugins/node_modules/@emotion/babel-plugin/node_modules/convert-source-map/**

- [[README]] — Converts a source-map from/to  different formats and allows adding/changing properties.

**banco/.netlify/plugins/node_modules/@emotion/babel-plugin/node_modules/escape-string-regexp/**

- [[readme]] — $ npm install escape-string-regexp

**banco/.netlify/plugins/node_modules/@emotion/babel-plugin/node_modules/source-map/**

- [[CHANGELOG]] — happens to have come to depend on. See #235.
- [[README]] — This is a library to generate and consume the source map format [described here][format].

**banco/.netlify/plugins/node_modules/@emotion/cache/**

- [[README]] — import createCache from '@emotion/cache'

**banco/.netlify/plugins/node_modules/@emotion/hash/**

- [[README]] — import hash from '@emotion/hash'

**banco/.netlify/plugins/node_modules/@emotion/react/**

- [[README]] — yarn add @emotion/react

**banco/.netlify/plugins/node_modules/@emotion/sheet/**

- [[README]] — yarn add @emotion/sheet

**banco/.netlify/plugins/node_modules/@emotion/unitless/**

- [[README]] — import unitless from '@emotion/unitless'

**banco/.netlify/plugins/node_modules/@emotion/use-insertion-effect-with-fallbacks/**

- [[README]] — TODO — nessuna prosa dopo il titolo.

**banco/.netlify/plugins/node_modules/@emotion/weak-memoize/**

- [[README]] — yarn add @emotion/weak-memoize

**banco/.netlify/plugins/node_modules/@esbuild/darwin-arm64/**

- [[README]] — This is the macOS ARM 64-bit binary for esbuild, a JavaScript bundler and minifier.

**banco/.netlify/plugins/node_modules/@fastify/busboy/**

- [[README]] — Description ===========

**banco/.netlify/plugins/node_modules/@floating-ui/core/**

- [[README]] — This is the platform-agnostic core of Floating UI, exposing the main computePosition function but no platform interface logic.

**banco/.netlify/plugins/node_modules/@floating-ui/dom/**

- [[README]] — This is the library to use Floating UI on the web, wrapping @floating-ui/core with DOM interface logic.

**banco/.netlify/plugins/node_modules/@floating-ui/utils/**

- [[README]] — Utility functions shared across Floating UI packages.

**banco/.netlify/plugins/node_modules/@fullstory/browser/**

- [[README]] — Fullstory's browser SDK lets you manage Fullstory data capture on your site as well as retrieve deep links to session replays and send your...

**banco/.netlify/plugins/node_modules/@fullstory/snippet/**

- [[README]] — FullStory's snippet package provides a number of ways to integrate the FullStory snippet with your build tooling of choice.

**banco/.netlify/plugins/node_modules/@google-cloud/paginator/**

- [[CHANGELOG]] — [npm history][1]
- [[README]] — A result paging utility used by Google node.js modules

**banco/.netlify/plugins/node_modules/@google-cloud/projectify/**

- [[CHANGELOG]] — [npm history][1]
- [[README]] — A simple utility for replacing the projectid token in objects.

**banco/.netlify/plugins/node_modules/@google-cloud/promisify/**

- [[CHANGELOG]] — [npm history][1]
- [[README]] — A simple utility for promisifying functions and classes.

**banco/.netlify/plugins/node_modules/@google-cloud/storage/**

- [[CHANGELOG]] — [npm history][1]
- [[README]] — [Cloud Storage](https://cloud.google.com/storage/docs) allows world-wide storage and retrieval of any amount of data at any time.

**banco/.netlify/plugins/node_modules/@google-cloud/storage/node_modules/configstore/**

- [[readme]] — The config is stored in a JSON file located in $XDG_CONFIG_HOME or ~/.config.<br> Example: ~/.config/configstore/some-id.json

**banco/.netlify/plugins/node_modules/@google-cloud/storage/node_modules/crypto-random-string/**

- [[readme]] — Can be useful for creating an identifier, slug, salt, fixture, etc.

**banco/.netlify/plugins/node_modules/@google-cloud/storage/node_modules/dot-prop/**

- [[readme]] — $ npm install dot-prop

**banco/.netlify/plugins/node_modules/@google-cloud/storage/node_modules/unique-string/**

- [[readme]] — $ npm install unique-string

**banco/.netlify/plugins/node_modules/@google-cloud/storage/node_modules/write-file-atomic/**

- [[CHANGELOG]] — error.
- [[README]] — write-file-atomic -----------------

**banco/.netlify/plugins/node_modules/@graphql-tools/batch-delegate/**

- [[CHANGELOG]] — In case of batched delegation (for example multiple book entitites fetched from different places from a field), remove the index from the er...
- [[README]] — Check API Reference for more information about this package; https://www.graphql-tools.com/docs/api/modules/batch_delegate_src

**banco/.netlify/plugins/node_modules/@graphql-tools/batch-execute/**

- [[CHANGELOG]] — See the use case below;
- [[README]] — Check API Reference for more information about this package; https://www.graphql-tools.com/docs/api/modules/batch_execute_src

**banco/.netlify/plugins/node_modules/@graphql-tools/delegate/**

- [[CHANGELOG]] — Because abstract types can be nested.
- [[README]] — Check API Reference for more information about this package; https://www.graphql-tools.com/docs/api/modules/delegate_src

**banco/.netlify/plugins/node_modules/@graphql-tools/executor/**

- [[README]] — Fork of GraphQL.js' execute function

**banco/.netlify/plugins/node_modules/@graphql-tools/merge/**

- [[README]] — Check API Reference for more information about this package; https://www.graphql-tools.com/docs/api/modules/merge_src

**banco/.netlify/plugins/node_modules/@graphql-tools/schema/**

- [[README]] — Check API Reference for more information about this package; https://www.graphql-tools.com/docs/api/modules/schema_src

**banco/.netlify/plugins/node_modules/@graphql-tools/stitch/**

- [[CHANGELOG]] — When a field in an interface needs to be isolated, it should not remove the field from the base subschema if it is used by other members of...
- [[README]] — For more information about this package: https://the-guild.dev/graphql/stitching

**banco/.netlify/plugins/node_modules/@graphql-tools/wrap/**

- [[CHANGELOG]] — When a subschema's a root field argument is renamed, the passed arguments should be also transformed;
- [[README]] — Check API Reference for more information about this package; https://www.graphql-tools.com/docs/api/modules/wrap_src

**banco/.netlify/plugins/node_modules/@hapi/hoek/**

- [[LICENSE]] — Copyright (c) 2011-2020, Sideway Inc, and project contributors Copyright (c) 2011-2014, Walmart Copyright (c) 2011, Yahoo Inc.
- [[README]] — hoek is part of the hapi ecosystem and was designed to work seamlessly with the [hapi web framework](https://hapi.dev) and its other compone...

**banco/.netlify/plugins/node_modules/@hapi/topo/**

- [[LICENSE]] — Copyright (c) 2012-2020, Sideway Inc, and project contributors Copyright (c) 2012-2014, Walmart.
- [[README]] — topo is part of the hapi ecosystem and was designed to work seamlessly with the [hapi web framework](https://hapi.dev) and its other compone...

**banco/.netlify/plugins/node_modules/@hookform/resolvers/**

- [[README]] — <div align="center"> <p align="center"> <a href="https://react-hook-form.com" title="React Hook Form - Simple React forms validation"> <img...

**banco/.netlify/plugins/node_modules/@iarna/toml/**

- [[CHANGELOG]] — This release just updates the spec compliance tests and benchmark data to better represent @ltd/j-toml.
- [[README]] — Better TOML parsing and stringifying all in that familiar JSON interface.

**banco/.netlify/plugins/node_modules/@isaacs/cliui/**

- [[README]] — Temporary fork of [cliui](http://npm.im/cliui).

**banco/.netlify/plugins/node_modules/@isaacs/cliui/node_modules/ansi-regex/**

- [[readme]] — npm install ansi-regex

**banco/.netlify/plugins/node_modules/@isaacs/cliui/node_modules/strip-ansi/**

- [[readme]] — npm install strip-ansi

**banco/.netlify/plugins/node_modules/@isaacs/fs-minipass/**

- [[README]] — Filesystem streams based on [minipass](http://npm.im/minipass).

**banco/.netlify/plugins/node_modules/@jridgewell/gen-mapping/**

- [[README]] — With a source map, you're able to trace the original location in the source file, either in Chrome's DevTools or using a library like [@jrid...

**banco/.netlify/plugins/node_modules/@jridgewell/remapping/**

- [[README]] — Remapping allows you to take the sourcemaps generated through transforming your code and "remap" them to the original source locations.

**banco/.netlify/plugins/node_modules/@jridgewell/resolve-uri/**

- [[README]] — Resolve any combination of absolute URIs, protocol-realtive URIs, absolute paths, or relative paths.

**banco/.netlify/plugins/node_modules/@jridgewell/sourcemap-codec/**

- [[README]] — Encode/decode the mappings property of a [sourcemap](https://docs.google.com/document/d/1U1RGAehQwRypUTovF1KRlpiOFze0b-_2gc6fAH0KY0k/edit).

**banco/.netlify/plugins/node_modules/@jridgewell/trace-mapping/**

- [[README]] — original location in the source file through a source map.

**banco/.netlify/plugins/node_modules/@lmdb/lmdb-darwin-arm64/**

- [[README]] — Platform specific binary for lmdb on darwin OS with arm64 architecture

**banco/.netlify/plugins/node_modules/@mapbox/node-pre-gyp/**

- [[CHANGELOG]] — and users need to know why builds are falling back to source compiles that might then error out.
- [[README]] — On Feb 9th, 2021 @mapbox/node-pre-gyp@1.0.0 was [released](./CHANGELOG.md).
- [[RELEASE]] — 1. Change the version number in package.json.
- [[contributing]] — TODO — nessuna prosa dopo il titolo.

**banco/.netlify/plugins/node_modules/@msgpackr-extract/msgpackr-extract-darwin-arm64/**

- [[README]] — Platform specific binary for msgpackr-extract on darwin OS with arm64 architecture

**banco/.netlify/plugins/node_modules/@netlify/binary-info/**

- [[README]] — @netlify/binary-info is a WebAssembly(WASM) module to extract very specific information from binary files.

**banco/.netlify/plugins/node_modules/@netlify/blobs/**

- [[README]] — A TypeScript client for Netlify Blobs.

**banco/.netlify/plugins/node_modules/@netlify/content-engine/**

- [[README]] — TODO — nessuna prosa dopo il titolo.

**banco/.netlify/plugins/node_modules/@netlify/content-engine/node_modules/ansi-styles/**

- [[readme]] — You probably want the higher-level [chalk](https://github.com/chalk/chalk) module for styling your strings.

**banco/.netlify/plugins/node_modules/@netlify/content-engine/node_modules/chalk/**

- [[readme]] — <h1 align="center"> <br> <br> <img width="320" src="media/logo.svg" alt="Chalk"> <br> <br> <br> </h1>

**banco/.netlify/plugins/node_modules/@netlify/content-engine/node_modules/execa/**

- [[readme]] — <img src="media/logo.svg" width="400"> <br>

**banco/.netlify/plugins/node_modules/@netlify/content-engine/node_modules/get-stream/**

- [[readme]] — $ npm install get-stream

**banco/.netlify/plugins/node_modules/@netlify/content-engine/node_modules/graphql/**

- [[README]] — The JavaScript reference implementation for GraphQL, a query language for APIs created by Facebook.

**banco/.netlify/plugins/node_modules/@netlify/content-engine/node_modules/human-signals/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — const { signalsByName, signalsByNumber } = require('human-signals')

**banco/.netlify/plugins/node_modules/@netlify/content-engine/node_modules/is-stream/**

- [[readme]] — $ npm install is-stream

**banco/.netlify/plugins/node_modules/@netlify/content-engine/node_modules/npm-run-path/**

- [[readme]] — In [npm run scripts](https://docs.npmjs.com/cli/run-script) you can execute locally installed binaries by name.

**banco/.netlify/plugins/node_modules/@netlify/content-engine/node_modules/strip-final-newline/**

- [[readme]] — Can be useful when parsing the output of, for example, ChildProcess#execFile, as [binaries usually output a newline at the end](https://stac...

**banco/.netlify/plugins/node_modules/@netlify/dev-utils/node_modules/uuid/**

- [[LICENSE]] — The MIT License (MIT)
- [[README]] — For the creation of [RFC9562](https://www.rfc-editor.org/rfc/rfc9562.html) (formerly [RFC4122](https://www.rfc-editor.org/rfc/rfc4122.html))...

**banco/.netlify/plugins/node_modules/@netlify/functions/**

- [[README]] — JavaScript and TypeScript utilities for [Netlify Functions](https://docs.netlify.com/functions/overview/).

**banco/.netlify/plugins/node_modules/@netlify/functions/node_modules/@netlify/blobs/**

- [[README]] — A TypeScript client for Netlify Blobs.

**banco/.netlify/plugins/node_modules/@netlify/integrations/**

- [[README]] — Update me!

**banco/.netlify/plugins/node_modules/@netlify/integrations/node_modules/@netlify/functions/**

- [[README]] — JavaScript and TypeScript utilities for [Netlify Functions](https://docs.netlify.com/functions/overview/).

**banco/.netlify/plugins/node_modules/@netlify/integrations/node_modules/is-promise/**

- [[readme]] — Test whether an object looks like a promises-a+ promise

**banco/.netlify/plugins/node_modules/@netlify/netlify-design-tokens/**

- [[README]] — Install the package in the project of your choice:

**banco/.netlify/plugins/node_modules/@netlify/node-cookies/**

- [[README]] — A Node.js port of https://deno.land/std@0.184.0/http/cookie.ts.

**banco/.netlify/plugins/node_modules/@netlify/open-api/**

- [[README]] — $ yarn add @netlify/open-api

**banco/.netlify/plugins/node_modules/@netlify/sdk/**

- [[README]] — SDK for developing extensions on Netlify.

**banco/.netlify/plugins/node_modules/@netlify/sdk--extension-api-client/**

- [[README]] — An API client for interacting with the Netlify extensions API.

**banco/.netlify/plugins/node_modules/@netlify/sdk--ui-core/**

- [[README]] — A framework-agnostic toolkit for building UI extensions on top of the Netlify platform.

**banco/.netlify/plugins/node_modules/@netlify/sdk--ui-functions/**

- [[README]] — A toolkit for building Netlify Functions for use by UI extensions.

**banco/.netlify/plugins/node_modules/@netlify/sdk--ui-react/**

- [[README]] — A React-based toolkit for building UI extensions on top of the Netlify platform.

**banco/.netlify/plugins/node_modules/@netlify/serverless-functions-api/**

- [[README]] — A Node.js module that implements the runtime API for serverless functions.

**banco/.netlify/plugins/node_modules/@netlify/tailwind-config/**

- [[README]] — This package provides a shared Tailwind CSS configuration for Netlify products.

**banco/.netlify/plugins/node_modules/@netlify/types/**

- [[README]] — TypeScript types for Netlify platform primitives.

**banco/.netlify/plugins/node_modules/@netlify/ui/node_modules/@netlify/netlify-design-tokens/**

- [[README]] — Install the package in the project of your choice:

**banco/.netlify/plugins/node_modules/@netlify/ui/node_modules/history/**

- [[README]] — [npm-badge]: https://img.shields.io/npm/v/history.svg?style=flat-square [npm]: https://www.npmjs.org/package/history [build-badge]: https://...

**banco/.netlify/plugins/node_modules/@netlify/zip-it-and-ship-it/**

- [[README]] — Creates Zip archives from Node.js, Go, and Rust programs.

**banco/.netlify/plugins/node_modules/@netlify/zip-it-and-ship-it/node_modules/@babel/types/**

- [[README]] — See our website [@babel/types](https://babeljs.io/docs/babel-types) for more information or the [issues](https://github.com/babel/babel/issu...

**banco/.netlify/plugins/node_modules/@netlify/zip-it-and-ship-it/node_modules/@esbuild/darwin-arm64/**

- [[README]] — This is the macOS ARM 64-bit binary for esbuild, a JavaScript bundler and minifier.

**banco/.netlify/plugins/node_modules/@netlify/zip-it-and-ship-it/node_modules/@netlify/serverless-functions-api/**

- [[README]] — A Node.js module that implements the runtime API for serverless functions.

**banco/.netlify/plugins/node_modules/@netlify/zip-it-and-ship-it/node_modules/esbuild/**

- [[LICENSE]] — MIT License
- [[README]] — This is a JavaScript bundler and minifier.

**banco/.netlify/plugins/node_modules/@netlify/zip-it-and-ship-it/node_modules/execa/**

- [[readme]] — <picture> <source media="(prefers-color-scheme: dark)" srcset="media/logo_dark.svg"> <img alt="execa logo" src="media/logo.svg" width="400">...

**banco/.netlify/plugins/node_modules/@netlify/zip-it-and-ship-it/node_modules/get-stream/**

- [[readme]] — npm install get-stream

**banco/.netlify/plugins/node_modules/@netlify/zip-it-and-ship-it/node_modules/human-signals/**

- [[README]] — import { signalsByName, signalsByNumber } from 'human-signals'

**banco/.netlify/plugins/node_modules/@netlify/zip-it-and-ship-it/node_modules/is-stream/**

- [[readme]] — $ npm install is-stream

**banco/.netlify/plugins/node_modules/@netlify/zip-it-and-ship-it/node_modules/mimic-fn/**

- [[readme]] — <img src="media/logo.svg" alt="mimic-fn" width="400"> <br>

**banco/.netlify/plugins/node_modules/@netlify/zip-it-and-ship-it/node_modules/npm-run-path/**

- [[readme]] — In [npm run scripts](https://docs.npmjs.com/cli/run-script) you can execute locally installed binaries by name.

**banco/.netlify/plugins/node_modules/@netlify/zip-it-and-ship-it/node_modules/onetime/**

- [[readme]] — When called multiple times it will return the return value from the first call.

**banco/.netlify/plugins/node_modules/@netlify/zip-it-and-ship-it/node_modules/path-key/**

- [[readme]] — It's usually PATH but on Windows it can be any casing like Path...

**banco/.netlify/plugins/node_modules/@netlify/zip-it-and-ship-it/node_modules/signal-exit/**

- [[README]] — When you want to fire an event no matter how a process exits:

**banco/.netlify/plugins/node_modules/@netlify/zip-it-and-ship-it/node_modules/strip-final-newline/**

- [[readme]] — Can be useful when parsing the output of, for example, ChildProcess#execFile, as [binaries usually output a newline at the end](https://stac...

**banco/.netlify/plugins/node_modules/@nodelib/fs.scandir/**

- [[README]] — The package is aimed at obtaining information about entries in the directory.

**banco/.netlify/plugins/node_modules/@nodelib/fs.stat/**

- [[README]] — Wrapper around standard method fs.lstat and fs.stat with some features.

**banco/.netlify/plugins/node_modules/@nodelib/fs.walk/**

- [[README]] — npm install @nodelib/fs.walk

**banco/.netlify/plugins/node_modules/@octokit/auth-token/**

- [[README]] — It is useful if you want to support multiple authentication strategies, as it’s API is compatible with its sibling packages for [basic](http...

**banco/.netlify/plugins/node_modules/@octokit/core/**

- [[README]] — <!-- toc -->

**banco/.netlify/plugins/node_modules/@octokit/endpoint/**

- [[README]] — <!-- update table of contents by running npx markdown-toc README.md -i -->

**banco/.netlify/plugins/node_modules/@octokit/graphql/**

- [[README]] — <!-- toc -->

**banco/.netlify/plugins/node_modules/@octokit/openapi-types/**

- [[README]] — This package is continously updated based on [GitHub's OpenAPI specification](https://github.com/github/rest-api-description/)

**banco/.netlify/plugins/node_modules/@octokit/plugin-paginate-rest/**

- [[README]] — <table> <tbody valign=top align=left> <tr><th> Browsers </th><td width=100%>

**banco/.netlify/plugins/node_modules/@octokit/plugin-request-log/**

- [[README]] — <table> <tbody valign=top align=left> <tr><th> Browsers </th><td width=100%>

**banco/.netlify/plugins/node_modules/@octokit/plugin-rest-endpoint-methods/**

- [[README]] — <table> <tbody valign=top align=left> <tr><th> Browsers </th><td width=100%>

**banco/.netlify/plugins/node_modules/@octokit/request/**

- [[README]] — to interact with [GitHub’s REST API](https://developer.github.com/v3/) and [GitHub’s GraphQL API](https://developer.github.com/v4/guides/for...

**banco/.netlify/plugins/node_modules/@octokit/request-error/**

- [[README]] — <table> <tbody valign=top align=left> <tr><th> Browsers </th><td width=100%> Load <code>@octokit/request-error</code> directly from <a href=...

**banco/.netlify/plugins/node_modules/@octokit/rest/**

- [[README]] — <table> <tbody valign=top align=left> <tr><th> Browsers </th><td width=100%> Load <code>@octokit/rest</code> directly from <a href="https://...

**banco/.netlify/plugins/node_modules/@octokit/types/**

- [[README]] — <!-- toc -->

**banco/.netlify/plugins/node_modules/@pkgjs/parseargs/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — Polyfill of util.parseArgs()

**banco/.netlify/plugins/node_modules/@pnpm/exec/**

- [[README]] — <!--@shields('npm', 'travis')--> [![npm version](https://img.shields.io/npm/v/@pnpm/exec.svg)](https://www.npmjs.com/package/@pnpm/exec) [![...

**banco/.netlify/plugins/node_modules/@pnpm/self-installer/**

- [[README]] — <!--@shields('npm', 'travis')--> [![npm version](https://img.shields.io/npm/v/@pnpm/self-installer.svg)](https://www.npmjs.com/package/@pnpm...

**banco/.netlify/plugins/node_modules/@popperjs/core/**

- [[LICENSE]] — The MIT License (MIT)
- [[README]] — npm i @popperjs/core

**banco/.netlify/plugins/node_modules/@react-hook/latest/**

- [[README]] — <hr> <div align="center"> <h1 align="center"> useLatest() </h1> </div>

**banco/.netlify/plugins/node_modules/@react-hook/passive-layout-effect/**

- [[README]] — <hr> <div align="center"> <h1 align="center"> usePassiveLayoutEffect() </h1> </div>

**banco/.netlify/plugins/node_modules/@react-hook/resize-observer/**

- [[README]] — <hr> <div align="center"> <h1 align="center"> useResizeObserver() </h1>

**banco/.netlify/plugins/node_modules/@repeaterjs/repeater/**

- [[CHANGELOG]] — This release flattens the monorepo into a single package, adds explicit resource management, and migrates the build to [@b9g/libuild](https:...
- [[README]] — The missing constructor for creating safe async iterators.

**banco/.netlify/plugins/node_modules/@rollup/pluginutils/**

- [[README]] — A set of utility functions commonly used by 🍣 Rollup plugins.

**banco/.netlify/plugins/node_modules/@sanity/block-tools/**

- [[README]] — Various tools for processing Sanity block content.
- [[changelog]] — 2018-12-13:  BREAKING: Changed params for htmlToBlocks from (html, options={blockContentType}) to (html, blockContentType, options={} as blo...

**banco/.netlify/plugins/node_modules/@sanity/client/**

- [[README]] — Javascript client for Sanity. Works in node.js and modern browsers (older browsers need a [Promise polyfill](https://www.sanity.io/help/js-c...

**banco/.netlify/plugins/node_modules/@sanity/color/**

- [[README]] — The Sanity color palette.

**banco/.netlify/plugins/node_modules/@sanity/eventsource/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Meta-package to make browsers and Node use different EventSource polyfills

**banco/.netlify/plugins/node_modules/@sanity/generate-help-url/**

- [[README]] — Generates URLs to specific sections of the Sanity documentation.

**banco/.netlify/plugins/node_modules/@sanity/schema/**

- [[README]] — You are almost always better off using composition, rather than inheritance hierarchies
- [[member-types]] — A member type is a type that is not a part of the schema, but rather exists as a member of another type.

**banco/.netlify/plugins/node_modules/@sanity/schema/node_modules/@sanity/types/parts/part.@sanity/components/build-snapshot/__legacy/@sanity/components/lists/**

- [[README]] — import type React from 'react' import {List, Item} from 'part:@sanity/components/lists/default'

**banco/.netlify/plugins/node_modules/@sanity/schema/node_modules/@types/react/**

- [[README]] — This package contains type definitions for react (https://react.dev/).

**banco/.netlify/plugins/node_modules/@sanity/schema/node_modules/arrify/**

- [[readme]] — $ npm install --save arrify

**banco/.netlify/plugins/node_modules/@sanity/timed-out/**

- [[readme]] — Emit Error object with code property equal ETIMEDOUT or ESOCKETTIMEDOUT when ClientRequest is hanged.

**banco/.netlify/plugins/node_modules/@sanity/types/node_modules/@sanity/client/**

- [[README]] — JavaScript client for Sanity. Works in modern browsers, as well as runtimes like [Node.js], [Bun], [Deno], and [Edge Runtime]

**banco/.netlify/plugins/node_modules/@sanity/types/node_modules/@sanity/eventsource/**

- [[README]] — Meta-package to make browsers and Node use different EventSource polyfills

**banco/.netlify/plugins/node_modules/@sanity/types/node_modules/@sanity/types/node_modules/@sanity/client/**

- [[README]] — JavaScript client for Sanity. Works in modern browsers, as well as runtimes like [Node.js], [Bun], [Deno], and [Edge Runtime]

**banco/.netlify/plugins/node_modules/@sanity/types/node_modules/@sanity/types/node_modules/eventsource/**

- [[README]] — WhatWG/W3C-compatible [server-sent events/eventsource](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) client.

**banco/.netlify/plugins/node_modules/@sanity/types/node_modules/@sanity/types/node_modules/get-it/**

- [[README]] — Generic HTTP request library for Node.js (>= 22.12), browsers, Deno, Bun, and edge runtimes.

**banco/.netlify/plugins/node_modules/@sanity/types/node_modules/decompress-response/**

- [[readme]] — Decompresses the [response](https://nodejs.org/api/http.html#http_class_http_incomingmessage) from [http.request](https://nodejs.org/api/htt...

**banco/.netlify/plugins/node_modules/@sanity/types/node_modules/get-it/**

- [[README]] — Generic HTTP request library for node.js (>= 14) and [modern browsers].

**banco/.netlify/plugins/node_modules/@sanity/types/node_modules/is-retry-allowed/**

- [[readme]] — $ npm install --save is-retry-allowed

**banco/.netlify/plugins/node_modules/@sanity/types/node_modules/readable-stream/**

- [[CONTRIBUTING]] — By making a contribution to this project, I certify that:
- [[GOVERNANCE]] — The Node.js Streams is jointly governed by a Working Group (WG) that is responsible for high-level guidance of the project.
- [[README]] — *Node.js core streams for userland* [![Build Status](https://travis-ci.com/nodejs/readable-stream.svg?branch=master)](https://travis-ci.com/...

**banco/.netlify/plugins/node_modules/@sanity/types/node_modules/rxjs/**

- [[CHANGELOG]] — 5bc8e3361 Fix/6052 ajax responseType should default to "json" (#6056)
- [[CODE_OF_CONDUCT]] — In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our pro...
- [[README]] — Curious what's next for RxJS? Follow along with [Issue 6367](https://github.com/ReactiveX/rxjs/issues/6367).

**banco/.netlify/plugins/node_modules/@sanity/types/node_modules/through2/**

- [[LICENSE]] — Copyright (c) Rod Vagg (the "Original Author") and additional contributors
- [[README]] — A tiny wrapper around Node.js streams.Transform (Streams2/3) to avoid explicit subclassing noise

**banco/.netlify/plugins/node_modules/@sec-ant/readable-stream/**

- [[README]] — A tiny, zero-dependency yet spec-compliant asynchronous iterator polyfill/ponyfill for [ReadableStream](https://developer.mozilla.org/docs/W...

**banco/.netlify/plugins/node_modules/@shikijs/core/**

- [[README]] — The core functionality of [Shiki](https://github.com/shikijs/shiki), without any grammar of themes bundled.

**banco/.netlify/plugins/node_modules/@shikijs/engine-javascript/**

- [[README]] — Engine for Shiki using JavaScript's native RegExp.

**banco/.netlify/plugins/node_modules/@shikijs/engine-oniguruma/**

- [[README]] — Engine for Shiki using Oniguruma RegExp engine in WebAssembly.

**banco/.netlify/plugins/node_modules/@shikijs/langs/**

- [[README]] — TextMate grammars for Shiki.

**banco/.netlify/plugins/node_modules/@shikijs/themes/**

- [[README]] — TextMate themes for Shiki.

**banco/.netlify/plugins/node_modules/@shikijs/types/**

- [[README]] — Types for Shiki.

**banco/.netlify/plugins/node_modules/@shikijs/vscode-textmate/**

- [[LICENSE]] — The MIT License (MIT)
- [[README]] — Changes make in this fork:

**banco/.netlify/plugins/node_modules/@sideway/address/**

- [[LICENSE]] — Copyright (c) 2019-2020, Sideway, Inc. and Project contributors All rights reserved.
- [[README]] — address is part of the joi ecosystem.

**banco/.netlify/plugins/node_modules/@sideway/formula/**

- [[LICENSE]] — Copyright (c) 2019-2020, Sideway. Inc, and project contributors All rights reserved.
- [[README]] — formula is part of the joi ecosystem.

**banco/.netlify/plugins/node_modules/@sideway/pinpoint/**

- [[LICENSE]] — Copyright (c) 2019-2020, Sideway. Inc, and project contributors
- [[README]] — pinpoint is part of the joi ecosystem.

**banco/.netlify/plugins/node_modules/@sindresorhus/is/**

- [[readme]] — For example, is.string('🦄') //=> true

**banco/.netlify/plugins/node_modules/@sindresorhus/merge-streams/**

- [[readme]] — npm install @sindresorhus/merge-streams

**banco/.netlify/plugins/node_modules/@sindresorhus/slugify/**

- [[readme]] — Useful for URLs, filenames, and IDs.

**banco/.netlify/plugins/node_modules/@sindresorhus/transliterate/**

- [[readme]] — Can be useful for [slugification](https://github.com/sindresorhus/slugify) purposes and other times you cannot use Unicode.

**banco/.netlify/plugins/node_modules/@so-ric/colorspace/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[LICENSE]] — The MIT License (MIT)
- [[README]] — Colorspace is a simple module which generates HEX color codes for namespaces.

**banco/.netlify/plugins/node_modules/@so-ric/colorspace/node_modules/color/**

- [[README]] — const color = Color('#7743CE').alpha(0.5).lighten(0.5); console.log(color.hsl().string());  // 'hsla(262, 59%, 81%, 0.5)'

**banco/.netlify/plugins/node_modules/@so-ric/colorspace/node_modules/color-convert/**

- [[README]] — Color-convert is a color conversion library for JavaScript and node.

**banco/.netlify/plugins/node_modules/@so-ric/colorspace/node_modules/color-name/**

- [[README]] — A JSON with color names and its values. Based on http://dev.w3.org/csswg/css-color/#named-colors.

**banco/.netlify/plugins/node_modules/@so-ric/colorspace/node_modules/color-string/**

- [[README]] — npm install color-string

**banco/.netlify/plugins/node_modules/@socket.io/component-emitter/**

- [[Readme]] — Event emitter component.

**banco/.netlify/plugins/node_modules/@stackbit/artisanal-names/**

- [[README]] — A name generator using hand-picked nouns and adjectives.

**banco/.netlify/plugins/node_modules/@stackbit/cms-contentful/**

- [[README]] — TODO — nessuna prosa dopo il titolo.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/**

- [[README]] — TODO — nessuna prosa dopo il titolo.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@esbuild/darwin-arm64/**

- [[README]] — This is the macOS ARM 64-bit binary for esbuild, a JavaScript bundler and minifier.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/content-engine/**

- [[README]] — TODO — nessuna prosa dopo il titolo.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/content-engine/node_modules/execa/**

- [[readme]] — <img src="media/logo.svg" width="400"> <br>

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/content-engine/node_modules/fs-extra/**

- [[README]] — Node.js: fs-extra =================

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/content-engine/node_modules/get-stream/**

- [[readme]] — $ npm install get-stream

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/content-engine/node_modules/human-signals/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — const { signalsByName, signalsByNumber } = require('human-signals')

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/content-engine/node_modules/is-stream/**

- [[readme]] — $ npm install is-stream

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/content-engine/node_modules/npm-run-path/**

- [[readme]] — In [npm run scripts](https://docs.npmjs.com/cli/run-script) you can execute locally installed binaries by name.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/content-engine/node_modules/path-key/**

- [[readme]] — It's usually PATH, but on Windows it can be any casing like Path...

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/content-engine/node_modules/strip-final-newline/**

- [[readme]] — Can be useful when parsing the output of, for example, ChildProcess#execFile, as [binaries usually output a newline at the end](https://stac...

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/content-engine/node_modules/uuid/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[CONTRIBUTING]] — Please feel free to file GitHub Issues or propose Pull Requests.
- [[LICENSE]] — The MIT License (MIT)
- [[README]] — For the creation of [RFC4122](http://www.ietf.org/rfc/rfc4122.txt) UUIDs

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/functions/**

- [[README]] — JavaScript and TypeScript utilities for [Netlify Functions](https://docs.netlify.com/functions/overview/).

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/sdk/**

- [[README]] — SDK for developing integrations on Netlify.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/sdk--extension-api-client/**

- [[README]] — An API client for interacting with the Netlify extensions API.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/sdk/node_modules/chalk/**

- [[readme]] — <h1 align="center"> <br> <br> <img width="320" src="media/logo.svg" alt="Chalk"> <br> <br> <br> </h1>

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/sdk/node_modules/fs-extra/**

- [[README]] — Node.js: fs-extra =================

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/sdk/node_modules/js-yaml/**

- [[README]] — JS-YAML - YAML 1.2 parser / writer for JavaScript =================================================

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/@netlify/serverless-functions-api/**

- [[README]] — A Node.js module that implements the runtime API for serverless functions.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/ansi-styles/**

- [[readme]] — You probably want the higher-level [chalk](https://github.com/chalk/chalk) module for styling your strings.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/axios/**

- [[CHANGELOG]] — Fixes and Functionality: - Fixing JSON transform when data is stringified.
- [[README]] — Promise based HTTP client for the browser and node.js
- [[SECURITY]] — Please report security issues to jasonsaayman@gmail.com
- [[UPGRADE_GUIDE]] — The Promise type declarations have been removed from the axios typings in favor of the built-in type declarations.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/axios/lib/adapters/**

- [[README]] — The modules under adapters/ are modules that handle dispatching a request and settling a returned Promise once a response is received.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/axios/lib/core/**

- [[README]] — The modules found in core/ should be modules that are specific to the domain logic of axios.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/axios/lib/helpers/**

- [[README]] — The modules found in helpers/ should be generic modules that are _not_ specific to the domain logic of axios.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/brace-expansion/**

- [[README]] — [Brace expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html), as known from sh/bash, in JavaScript.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/chalk/**

- [[readme]] — <h1 align="center"> <br> <br> <img width="320" src="media/logo.svg" alt="Chalk"> <br> <br> <br> </h1>

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/esbuild/**

- [[LICENSE]] — MIT License
- [[README]] — This is a JavaScript bundler and minifier.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/execa/**

- [[readme]] — <picture> <source media="(prefers-color-scheme: dark)" srcset="media/logo_dark.svg"> <img alt="execa logo" src="media/logo.svg" width="400">...

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/execa/node_modules/onetime/**

- [[readme]] — When called multiple times it will return the return value from the first call.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/execa/node_modules/signal-exit/**

- [[README]] — When you want to fire an event no matter how a process exits:

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/fs-extra/**

- [[CHANGELOG]] — 8.1.0 / 2019-06-28 ------------------
- [[README]] — Node.js: fs-extra =================

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/fs-extra/node_modules/jsonfile/**

- [[CHANGELOG]] — 4.0.0 / 2017-07-12 ------------------
- [[README]] — Node.js - jsonfile ================

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/fs-extra/node_modules/universalify/**

- [[README]] — Make a callback- or promise-based function support both promises and callbacks.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/get-stream/**

- [[readme]] — npm install get-stream

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/glob/**

- [[README]] — Match files using the patterns the shell uses, like stars and stuff.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/graphql/**

- [[README]] — The JavaScript reference implementation for GraphQL, a query language for APIs created by Facebook.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/human-signals/**

- [[README]] — import { signalsByName, signalsByNumber } from 'human-signals'

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/is-stream/**

- [[readme]] — $ npm install is-stream

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/js-yaml/**

- [[README]] — JS-YAML - YAML 1.2 parser / writer for JavaScript =================================================

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/js-yaml/node_modules/argparse/**

- [[CHANGELOG]] — 1.0.10 / 2018-02-15 ------------------
- [[README]] — argparse ========

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/mimic-fn/**

- [[readme]] — <img src="media/logo.svg" alt="mimic-fn" width="400"> <br>

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/minimatch/**

- [[README]] — A minimal matching utility.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/npm-run-path/**

- [[readme]] — In [npm run scripts](https://docs.npmjs.com/cli/run-script) you can execute locally installed binaries by name.

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/path-key/**

- [[readme]] — It's usually PATH but on Windows it can be any casing like Path...

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/strip-final-newline/**

- [[readme]] — Can be useful when parsing the output of, for example, ChildProcess#execFile, as [binaries usually output a newline at the end](https://stac...

**banco/.netlify/plugins/node_modules/@stackbit/cms-core/node_modules/uuid/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[CONTRIBUTING]] — Please feel free to file GitHub Issues or propose Pull Requests.
- [[LICENSE]] — The MIT License (MIT)
- [[README]] — For the creation of [RFC4122](https://www.ietf.org/rfc/rfc4122.txt) UUIDs

**banco/.netlify/plugins/node_modules/@stackbit/cms-git/**

- [[README]] — TODO — nessuna prosa dopo il titolo.

**banco/.netlify/plugins/node_modules/@stackbit/cms-git/node_modules/axios/**

- [[CHANGELOG]] — Breaking changes: - Revert: change type of AxiosResponse to any, please read lengthy discussion here: ([4141](https://github.com/axios/axios...
- [[README]] — Promise based HTTP client for the browser and node.js
- [[SECURITY]] — Please report security issues to jasonsaayman@gmail.com
- [[UPGRADE_GUIDE]] — The Promise type declarations have been removed from the axios typings in favor of the built-in type declarations.

**banco/.netlify/plugins/node_modules/@stackbit/cms-git/node_modules/axios/lib/adapters/**

- [[README]] — The modules under adapters/ are modules that handle dispatching a request and settling a returned Promise once a response is received.

**banco/.netlify/plugins/node_modules/@stackbit/cms-git/node_modules/axios/lib/core/**

- [[README]] — The modules found in core/ should be modules that are specific to the domain logic of axios.

**banco/.netlify/plugins/node_modules/@stackbit/cms-git/node_modules/axios/lib/env/**

- [[README]] — The data.js file is updated automatically when the package version is upgrading.

**banco/.netlify/plugins/node_modules/@stackbit/cms-git/node_modules/axios/lib/helpers/**

- [[README]] — The modules found in helpers/ should be generic modules that are _not_ specific to the domain logic of axios.

**banco/.netlify/plugins/node_modules/@stackbit/cms-sanity/node_modules/fs-extra/**

- [[CHANGELOG]] — 9.1.0 / 2021-01-19 ------------------
- [[README]] — Node.js: fs-extra =================

**banco/.netlify/plugins/node_modules/@stackbit/cms-sanity/node_modules/glob/**

- [[README]] — Match files using the patterns the shell uses.

**banco/.netlify/plugins/node_modules/@stackbit/cms-sanity/node_modules/jackspeak/**

- [[LICENSE]] — Version 1.0.0
- [[README]] — A very strict and proper argument parser.

**banco/.netlify/plugins/node_modules/@stackbit/cms-sanity/node_modules/minipass/**

- [[README]] — A _very_ minimal implementation of a [PassThrough stream](https://nodejs.org/api/stream.html#stream_class_stream_passthrough)

**banco/.netlify/plugins/node_modules/@stackbit/dev-common/**

- [[README]] — TODO — nessuna prosa dopo il titolo.

**banco/.netlify/plugins/node_modules/@stackbit/dev-common/node_modules/ansi-styles/**

- [[readme]] — You probably want the higher-level [chalk](https://github.com/chalk/chalk) module for styling your strings.

**banco/.netlify/plugins/node_modules/@stackbit/dev-common/node_modules/argparse/**

- [[CHANGELOG]] — 1.0.10 / 2018-02-15 ------------------
- [[README]] — argparse ========

**banco/.netlify/plugins/node_modules/@stackbit/dev-common/node_modules/axios/**

- [[CHANGELOG]] — Breaking changes: - Fixing maxBodyLength enforcement ([#3786](https://github.com/axios/axios/pull/3786)) - Don't rely on strict mode behavio...
- [[README]] — Promise based HTTP client for the browser and node.js
- [[SECURITY]] — Please report security issues to jasonsaayman@gmail.com
- [[UPGRADE_GUIDE]] — Routing through an https proxy now requires setting the protocol attribute of the proxy configuration to https

**banco/.netlify/plugins/node_modules/@stackbit/dev-common/node_modules/axios/lib/adapters/**

- [[README]] — The modules under adapters/ are modules that handle dispatching a request and settling a returned Promise once a response is received.

**banco/.netlify/plugins/node_modules/@stackbit/dev-common/node_modules/axios/lib/core/**

- [[README]] — The modules found in core/ should be modules that are specific to the domain logic of axios.

**banco/.netlify/plugins/node_modules/@stackbit/dev-common/node_modules/axios/lib/env/**

- [[README]] — The data.js file is updated automatically when the package version is upgrading.

**banco/.netlify/plugins/node_modules/@stackbit/dev-common/node_modules/axios/lib/helpers/**

- [[README]] — The modules found in helpers/ should be generic modules that are _not_ specific to the domain logic of axios.

**banco/.netlify/plugins/node_modules/@stackbit/dev-common/node_modules/chalk/**

- [[readme]] — <h1 align="center"> <br> <br> <img width="320" src="media/logo.svg" alt="Chalk"> <br> <br> <br> </h1>

**banco/.netlify/plugins/node_modules/@stackbit/dev-common/node_modules/configstore/**

- [[readme]] — The config is stored in a JSON file located in $XDG_CONFIG_HOME or ~/.config.<br> Example: ~/.config/configstore/some-id.json

**banco/.netlify/plugins/node_modules/@stackbit/dev-common/node_modules/crypto-random-string/**

- [[readme]] — Can be useful for creating an identifier, slug, salt, fixture, etc.

**banco/.netlify/plugins/node_modules/@stackbit/dev-common/node_modules/dot-prop/**

- [[readme]] — $ npm install dot-prop

**banco/.netlify/plugins/node_modules/@stackbit/dev-common/node_modules/fs-extra/**

- [[README]] — Node.js: fs-extra =================

**banco/.netlify/plugins/node_modules/@stackbit/dev-common/node_modules/js-yaml/**

- [[README]] — JS-YAML - YAML 1.2 parser / writer for JavaScript =================================================

**banco/.netlify/plugins/node_modules/@stackbit/dev-common/node_modules/unique-string/**

- [[readme]] — $ npm install unique-string

**banco/.netlify/plugins/node_modules/@stackbit/dev-common/node_modules/write-file-atomic/**

- [[CHANGELOG]] — error.
- [[README]] — write-file-atomic -----------------

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/ansi-styles/**

- [[readme]] — You probably want the higher-level [chalk](https://github.com/chalk/chalk) module for styling your strings.

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/axios/**

- [[CHANGELOG]] — Breaking changes: - Fixing maxBodyLength enforcement ([#3786](https://github.com/axios/axios/pull/3786)) - Don't rely on strict mode behavio...
- [[README]] — Promise based HTTP client for the browser and node.js
- [[SECURITY]] — Please report security issues to jasonsaayman@gmail.com
- [[UPGRADE_GUIDE]] — Routing through an https proxy now requires setting the protocol attribute of the proxy configuration to https

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/axios/lib/adapters/**

- [[README]] — The modules under adapters/ are modules that handle dispatching a request and settling a returned Promise once a response is received.

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/axios/lib/core/**

- [[README]] — The modules found in core/ should be modules that are specific to the domain logic of axios.

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/axios/lib/env/**

- [[README]] — The data.js file is updated automatically when the package version is upgrading.

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/axios/lib/helpers/**

- [[README]] — The modules found in helpers/ should be generic modules that are _not_ specific to the domain logic of axios.

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/chalk/**

- [[readme]] — <h1 align="center"> <br> <br> <img width="320" src="media/logo.svg" alt="Chalk"> <br> <br> <br> </h1>

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/chokidar/**

- [[README]] — Node.js fs.watch:

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/configstore/**

- [[readme]] — The config is stored in a JSON file located in $XDG_CONFIG_HOME or ~/.config.<br> Example: ~/.config/configstore/some-id.json

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/crypto-random-string/**

- [[readme]] — Can be useful for creating an identifier, slug, salt, fixture, etc.

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/define-lazy-prop/**

- [[readme]] — Useful when the value of a property is expensive to generate, so you want to delay the computation until the property is needed.

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/dot-prop/**

- [[readme]] — $ npm install dot-prop

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/fs-extra/**

- [[README]] — Node.js: fs-extra =================

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/is-docker/**

- [[readme]] — $ npm install is-docker

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/open/**

- [[readme]] — This is meant to be used in command-line tools and scripts, not in the browser.

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/picomatch/**

- [[README]] — picomatch x 1,993,050 ops/sec ±0.51% (91 runs sampled) minimatch x 627,206 ops/sec ±1.96% (87 runs sampled))

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/readdirp/**

- [[README]] — Recursive version of [fs.readdir](https://nodejs.org/api/fs.html#fs_fs_readdir_path_options_callback).

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/unique-string/**

- [[readme]] — $ npm install unique-string

**banco/.netlify/plugins/node_modules/@stackbit/dev/node_modules/write-file-atomic/**

- [[CHANGELOG]] — error.
- [[README]] — write-file-atomic -----------------

**banco/.netlify/plugins/node_modules/@stackbit/sdk/**

- [[README]] — Stackbit SDK contains set of utilities to work with stackbit.yaml file.

**banco/.netlify/plugins/node_modules/@stackbit/sdk/node_modules/@esbuild/darwin-arm64/**

- [[README]] — This is the macOS ARM 64-bit binary for esbuild, a JavaScript bundler and minifier.

**banco/.netlify/plugins/node_modules/@stackbit/sdk/node_modules/chokidar/**

- [[README]] — Node.js fs.watch:

**banco/.netlify/plugins/node_modules/@stackbit/sdk/node_modules/esbuild/**

- [[LICENSE]] — MIT License
- [[README]] — This is a JavaScript bundler and minifier.

**banco/.netlify/plugins/node_modules/@stackbit/sdk/node_modules/fs-extra/**

- [[CHANGELOG]] — 9.1.0 / 2021-01-19 ------------------
- [[README]] — Node.js: fs-extra =================

**banco/.netlify/plugins/node_modules/@stackbit/sdk/node_modules/picomatch/**

- [[README]] — picomatch x 1,993,050 ops/sec ±0.51% (91 runs sampled) minimatch x 627,206 ops/sec ±1.96% (87 runs sampled))

**banco/.netlify/plugins/node_modules/@stackbit/sdk/node_modules/readdirp/**

- [[README]] — Recursive version of [fs.readdir](https://nodejs.org/api/fs.html#fs_fs_readdir_path_options_callback).

**banco/.netlify/plugins/node_modules/@stackbit/types/**

- [[README]] — import StackbitTypes from '@stackbit/types';

**banco/.netlify/plugins/node_modules/@stackbit/utils/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Stackbit utilities

**banco/.netlify/plugins/node_modules/@stackbit/utils/node_modules/fs-extra/**

- [[CHANGELOG]] — 9.1.0 / 2021-01-19 ------------------
- [[README]] — Node.js: fs-extra =================

**banco/.netlify/plugins/node_modules/@szmarczak/http-timer/**

- [[README]] — Inspired by the [request package](https://github.com/request/request).

**banco/.netlify/plugins/node_modules/@tailwindcss/container-queries/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — A plugin for Tailwind CSS v3.2+ that provides utilities for container queries.

**banco/.netlify/plugins/node_modules/@tippyjs/react/**

- [[README]] — npm i @tippyjs/react

**banco/.netlify/plugins/node_modules/@tokenizer/token/**

- [[README]] — TypeScript definition of an [strtok3](https://github.com/Borewit/strtok3) token.

**banco/.netlify/plugins/node_modules/@tootallnate/once/**

- [[README]] — Install with npm:

**banco/.netlify/plugins/node_modules/@trpc/server/**

- [[README]] — Full documentation for @trpc/server can be found [here](https://trpc.io/docs/router)

**banco/.netlify/plugins/node_modules/@trpc/server/skills/adapter-aws-lambda/**

- [[SKILL]] — // server.ts import { initTRPC } from '@trpc/server'; import type { CreateAWSLambdaContextOptions } from '@trpc/server/adapters/aws-lambda';...

**banco/.netlify/plugins/node_modules/@trpc/server/skills/adapter-express/**

- [[SKILL]] — // server.ts import { initTRPC } from '@trpc/server'; import * as trpcExpress from '@trpc/server/adapters/express'; import express from 'exp...

**banco/.netlify/plugins/node_modules/@trpc/server/skills/adapter-fastify/**

- [[SKILL]] — // server.ts import { initTRPC } from '@trpc/server'; import { fastifyTRPCPlugin, FastifyTRPCPluginOptions, } from '@trpc/server/adapters/fa...

**banco/.netlify/plugins/node_modules/@trpc/server/skills/adapter-fetch/**

- [[SKILL]] — // Cloudflare Worker example import { initTRPC } from '@trpc/server'; import { fetchRequestHandler } from '@trpc/server/adapters/fetch'; imp...

**banco/.netlify/plugins/node_modules/@trpc/server/skills/adapter-standalone/**

- [[SKILL]] — // server.ts import { initTRPC } from '@trpc/server'; import { createHTTPServer } from '@trpc/server/adapters/standalone'; import { z } from...

**banco/.netlify/plugins/node_modules/@trpc/server/skills/auth/**

- [[SKILL]] — // server/trpc.ts import { initTRPC, TRPCError } from '@trpc/server'; import type { CreateHTTPContextOptions } from '@trpc/server/adapters/s...

**banco/.netlify/plugins/node_modules/@trpc/server/skills/caching/**

- [[SKILL]] — // server/trpc.ts import { initTRPC } from '@trpc/server'; import type { CreateHTTPContextOptions } from '@trpc/server/adapters/standalone';

**banco/.netlify/plugins/node_modules/@trpc/server/skills/error-handling/**

- [[SKILL]] — // server/trpc.ts import { initTRPC } from '@trpc/server'; import { ZodError } from 'zod';

**banco/.netlify/plugins/node_modules/@trpc/server/skills/middlewares/**

- [[SKILL]] — // server/trpc.ts import { initTRPC, TRPCError } from '@trpc/server';

**banco/.netlify/plugins/node_modules/@trpc/server/skills/non-json-content-types/**

- [[SKILL]] — Server:

**banco/.netlify/plugins/node_modules/@trpc/server/skills/server-setup/**

- [[SKILL]] — // server/trpc.ts import { initTRPC } from '@trpc/server';

**banco/.netlify/plugins/node_modules/@trpc/server/skills/server-side-calls/**

- [[SKILL]] — // server/trpc.ts import { initTRPC } from '@trpc/server';

**banco/.netlify/plugins/node_modules/@trpc/server/skills/service-oriented-architecture/**

- [[SKILL]] — // packages/server-lib/index.ts import { initTRPC } from '@trpc/server';

**banco/.netlify/plugins/node_modules/@trpc/server/skills/subscriptions/**

- [[SKILL]] — SSE is recommended for most subscription use cases.

**banco/.netlify/plugins/node_modules/@trpc/server/skills/trpc-router/**

- [[SKILL]] — // server/trpc.ts import { initTRPC } from '@trpc/server';

**banco/.netlify/plugins/node_modules/@trpc/server/skills/validators/**

- [[SKILL]] — // server/trpc.ts import { initTRPC } from '@trpc/server';

**banco/.netlify/plugins/node_modules/@types/cacheable-request/**

- [[README]] — This package contains type definitions for cacheable-request (https://github.com/lukechilds/cacheable-request#readme).

**banco/.netlify/plugins/node_modules/@types/chance/**

- [[README]] — This package contains type definitions for chance (http://chancejs.com).

**banco/.netlify/plugins/node_modules/@types/configstore/**

- [[README]] — This package contains type definitions for configstore (https://github.com/yeoman/configstore).

**banco/.netlify/plugins/node_modules/@types/cors/**

- [[README]] — This package contains type definitions for cors (https://github.com/expressjs/cors/).

**banco/.netlify/plugins/node_modules/@types/debug/**

- [[README]] — This package contains type definitions for debug (https://github.com/visionmedia/debug).

**banco/.netlify/plugins/node_modules/@types/estree/**

- [[README]] — This package contains type definitions for estree (https://github.com/estree/estree).

**banco/.netlify/plugins/node_modules/@types/estree-jsx/**

- [[README]] — This package contains type definitions for estree-jsx (https://github.com/facebook/jsx).

**banco/.netlify/plugins/node_modules/@types/event-source-polyfill/**

- [[README]] — This package contains type definitions for event-source-polyfill (https://github.com/Yaffle/EventSource).

**banco/.netlify/plugins/node_modules/@types/eventsource/**

- [[README]] — This package contains type definitions for eventsource (https://github.com/EventSource/eventsource).

**banco/.netlify/plugins/node_modules/@types/get-port/**

- [[README]] — This package contains type definitions for get-port (https://github.com/sindresorhus/get-port).

**banco/.netlify/plugins/node_modules/@types/glob/**

- [[README]] — This package contains type definitions for Glob (https://github.com/isaacs/node-glob).

**banco/.netlify/plugins/node_modules/@types/hast/**

- [[README]] — This package contains type definitions for hast (https://github.com/syntax-tree/hast).

**banco/.netlify/plugins/node_modules/@types/http-cache-semantics/**

- [[README]] — This package contains type definitions for http-cache-semantics (https://github.com/kornelski/http-cache-semantics#readme).

**banco/.netlify/plugins/node_modules/@types/json-patch/**

- [[README]] — This package contains type definitions for json-patch (https://github.com/bruth/jsonpatch-js).

**banco/.netlify/plugins/node_modules/@types/keyv/**

- [[README]] — This package contains type definitions for keyv (https://github.com/lukechilds/keyv).

**banco/.netlify/plugins/node_modules/@types/lodash/**

- [[README]] — This package contains type definitions for lodash (https://lodash.com).

**banco/.netlify/plugins/node_modules/@types/mdast/**

- [[README]] — This package contains type definitions for mdast (https://github.com/syntax-tree/mdast).

**banco/.netlify/plugins/node_modules/@types/minimatch/**

- [[README]] — This package contains type definitions for minimatch (https://github.com/isaacs/minimatch).

**banco/.netlify/plugins/node_modules/@types/mkdirp/**

- [[README]] — This package contains type definitions for mkdirp (https://github.com/substack/node-mkdirp).

**banco/.netlify/plugins/node_modules/@types/ms/**

- [[README]] — This package contains type definitions for ms (https://github.com/vercel/ms).

**banco/.netlify/plugins/node_modules/@types/node/**

- [[README]] — This package contains type definitions for Node.js (http://nodejs.org/).

**banco/.netlify/plugins/node_modules/@types/normalize-package-data/**

- [[README]] — This package contains type definitions for normalize-package-data (https://github.com/npm/normalize-package-data#readme).

**banco/.netlify/plugins/node_modules/@types/parse-json/**

- [[README]] — This package contains type definitions for parse-json (https://github.com/sindresorhus/parse-json).

**banco/.netlify/plugins/node_modules/@types/prop-types/**

- [[README]] — This package contains type definitions for prop-types (https://github.com/facebook/prop-types).

**banco/.netlify/plugins/node_modules/@types/react/**

- [[README]] — This package contains type definitions for react (https://react.dev/).

**banco/.netlify/plugins/node_modules/@types/react-transition-group/**

- [[README]] — This package contains type definitions for react-transition-group (https://github.com/reactjs/react-transition-group).

**banco/.netlify/plugins/node_modules/@types/responselike/**

- [[README]] — This package contains type definitions for responselike (https://github.com/lukechilds/responselike#readme).

**banco/.netlify/plugins/node_modules/@types/rimraf/**

- [[README]] — This package contains type definitions for rimraf (https://github.com/isaacs/rimraf).

**banco/.netlify/plugins/node_modules/@types/scheduler/**

- [[README]] — This package contains type definitions for scheduler (https://reactjs.org/).

**banco/.netlify/plugins/node_modules/@types/tmp/**

- [[README]] — This package contains type definitions for tmp (https://www.npmjs.com/package/tmp).

**banco/.netlify/plugins/node_modules/@types/triple-beam/**

- [[README]] — This package contains type definitions for triple-beam (https://github.com/winstonjs/triple-beam).

**banco/.netlify/plugins/node_modules/@types/unist/**

- [[README]] — This package contains type definitions for unist (https://github.com/syntax-tree/unist).

**banco/.netlify/plugins/node_modules/@types/ws/**

- [[README]] — This package contains type definitions for ws (https://github.com/websockets/ws).

**banco/.netlify/plugins/node_modules/@types/yauzl/**

- [[README]] — This package contains type definitions for yauzl (https://github.com/thejoshwolfe/yauzl).

**banco/.netlify/plugins/node_modules/@typescript-eslint/project-service/**

- [[README]] — A standalone export of the "Project Service" that powers typed linting for typescript-eslint.

**banco/.netlify/plugins/node_modules/@typescript-eslint/tsconfig-utils/**

- [[README]] — The utilities in this package are separated from @typescript-eslint/utils so that they do not have a dependency on eslint or @typescript-esl...

**banco/.netlify/plugins/node_modules/@typescript-eslint/types/**

- [[README]] — This package exists to help us reduce cycles and provide lighter-weight packages at runtime.

**banco/.netlify/plugins/node_modules/@typescript-eslint/typescript-estree/**

- [[README]] — 👉 See https://typescript-eslint.io/packages/typescript-estree for documentation on this package.

**banco/.netlify/plugins/node_modules/@typescript-eslint/typescript-estree/node_modules/balanced-match/**

- [[LICENSE]] — (MIT)
- [[README]] — Match balanced string pairs, like { and } or <b> and </b>.

**banco/.netlify/plugins/node_modules/@typescript-eslint/typescript-estree/node_modules/brace-expansion/**

- [[README]] — [Brace expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html), as known from sh/bash, in JavaScript.

**banco/.netlify/plugins/node_modules/@typescript-eslint/typescript-estree/node_modules/minimatch/**

- [[LICENSE]] — Version 1.0.0
- [[README]] — A minimal matching utility.

**banco/.netlify/plugins/node_modules/@typescript-eslint/visitor-keys/**

- [[README]] — This is an _internal package_ to the [typescript-eslint monorepo](https://github.com/typescript-eslint/typescript-eslint).

**banco/.netlify/plugins/node_modules/@ungap/structured-clone/**

- [[README]] — An env agnostic serializer and deserializer with recursion ability and types beyond *JSON* from the *HTML* standard itself.

**banco/.netlify/plugins/node_modules/@vercel/nft/**

- [[readme]] — Used to determine exactly which files (including node_modules) are necessary for the application runtime.

**banco/.netlify/plugins/node_modules/@vue/compiler-core/**

- [[README]] — TODO — nessuna prosa dopo il titolo.

**banco/.netlify/plugins/node_modules/@vue/compiler-core/node_modules/entities/**

- [[readme]] — Encode & decode HTML & XML entities with ease & speed.

**banco/.netlify/plugins/node_modules/@vue/compiler-dom/**

- [[README]] — TODO — nessuna prosa dopo il titolo.

**banco/.netlify/plugins/node_modules/@vue/compiler-sfc/**

- [[README]] — Note: as of 3.2.13+, this package is included as a dependency of the main vue package and can be accessed as vue/compiler-sfc.

**banco/.netlify/plugins/node_modules/@vue/compiler-ssr/**

- [[README]] — TODO — nessuna prosa dopo il titolo.

**banco/.netlify/plugins/node_modules/@vue/shared/**

- [[README]] — Internal utility functions and constants shared across @vue packages.

**banco/.netlify/plugins/node_modules/@whatwg-node/fetch/**

- [[CHANGELOG]] — [0079afd](https://github.com/ardatan/whatwg-node/commit/0079afdc785c012fad22dd35963800a8199bfe89) Thanks [@ardatan](https://github.com/ardat...
- [[README]] — A ponyfill package for the [Fetch Standard](https://fetch.spec.whatwg.org/).

**banco/.netlify/plugins/node_modules/@whatwg-node/fetch/node_modules/urlpattern-polyfill/**

- [[README]] — URLPattern polyfills ===

**banco/.netlify/plugins/node_modules/@whatwg-node/server/**

- [[README]] — for Node.js, AWS Lambda, Cloudflare Workers, Deno, Express, Fastify, Koa, Next.js and Sveltekit.

**banco/.netlify/plugins/node_modules/abab/**

- [[LICENSE]] — Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are me...
- [[README]] — A JavaScript module that implements window.atob and window.btoa according the forgiving-base64 algorithm in the [Infra Standard](https://inf...

**banco/.netlify/plugins/node_modules/abbrev/**

- [[README]] — Just like [ruby's Abbrev](http://apidock.com/ruby/Abbrev).

**banco/.netlify/plugins/node_modules/abort-controller/**

- [[README]] — An implementation of [WHATWG AbortController interface](https://dom.spec.whatwg.org/#interface-abortcontroller).

**banco/.netlify/plugins/node_modules/accepts/**

- [[HISTORY]] — 1.3.8 / 2022-02-02 ==================
- [[README]] — Higher level content negotiation based on [negotiator](https://www.npmjs.com/package/negotiator).

**banco/.netlify/plugins/node_modules/accepts/node_modules/negotiator/**

- [[HISTORY]] — 0.6.3 / 2022-01-22 ==================
- [[README]] — An HTTP content negotiator for Node.js

**banco/.netlify/plugins/node_modules/acorn/**

- [[CHANGELOG]] — Add support for Unicode 18.
- [[README]] — A tiny, fast JavaScript parser written in JavaScript.

**banco/.netlify/plugins/node_modules/acorn-globals/**

- [[README]] — Detect global variables in JavaScript using acorn

**banco/.netlify/plugins/node_modules/acorn-import-attributes/**

- [[README]] — yarn add acorn-import-attributes

**banco/.netlify/plugins/node_modules/acorn-walk/**

- [[CHANGELOG]] — Emit a more informative error message when trying to walk a node type that has no walker function.
- [[README]] — An abstract syntax tree walker for the [ESTree](https://github.com/estree/estree) format.

**banco/.netlify/plugins/node_modules/address/**

- [[README]] — address =======

**banco/.netlify/plugins/node_modules/agent-base/**

- [[README]] — agent-base ========== ### Turn a function into an [http.Agent][http.Agent] instance

**banco/.netlify/plugins/node_modules/ansi-escapes/**

- [[readme]] — $ npm install ansi-escapes

**banco/.netlify/plugins/node_modules/ansi-escapes/node_modules/type-fest/**

- [[readme]] — <div align="center"> <br> <br> <img src="media/logo.svg" alt="type-fest" height="300"> <br> <br> <b>A collection of essential TypeScript typ...

**banco/.netlify/plugins/node_modules/ansi-regex/**

- [[readme]] — $ npm install ansi-regex

**banco/.netlify/plugins/node_modules/ansi-styles/**

- [[readme]] — You probably want the higher-level [chalk](https://github.com/chalk/chalk) module for styling your strings.

**banco/.netlify/plugins/node_modules/any-promise/**

- [[README]] — $ npm install mz

**banco/.netlify/plugins/node_modules/anymatch/**

- [[README]] — anymatch [![Build Status](https://travis-ci.org/micromatch/anymatch.svg?branch=master)](https://travis-ci.org/micromatch/anymatch) [![Covera...

**banco/.netlify/plugins/node_modules/anymatch/node_modules/picomatch/**

- [[README]] — picomatch x 1,993,050 ops/sec ±0.51% (91 runs sampled) minimatch x 627,206 ops/sec ±1.96% (87 runs sampled))

**banco/.netlify/plugins/node_modules/application-config-path/**

- [[README]] — Store your application config in the right location.

**banco/.netlify/plugins/node_modules/archiver/**

- [[README]] — A streaming interface for archive generation

**banco/.netlify/plugins/node_modules/archiver-utils/**

- [[README]] — TODO — nessuna prosa dopo il titolo.

**banco/.netlify/plugins/node_modules/archiver-utils/node_modules/is-stream/**

- [[readme]] — $ npm install is-stream

**banco/.netlify/plugins/node_modules/arg/**

- [[LICENSE]] — The MIT License (MIT)
- [[README]] — npm install arg

**banco/.netlify/plugins/node_modules/argparse/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — argparse ========

**banco/.netlify/plugins/node_modules/array-buffer-byte-length/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Get the byte length of an ArrayBuffer, even in engines without a .byteLength method.

**banco/.netlify/plugins/node_modules/array-flatten/**

- [[README]] — npm install array-flatten --save

**banco/.netlify/plugins/node_modules/array-union/**

- [[readme]] — $ npm install array-union

**banco/.netlify/plugins/node_modules/array.prototype.flatmap/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — An ES2019 spec-compliant Array.prototype.flatMap shim/polyfill/replacement that works as far down as ES3.

**banco/.netlify/plugins/node_modules/arraybuffer.prototype.slice/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — An ES spec-compliant ArrayBuffer.prototype.slice shim.

**banco/.netlify/plugins/node_modules/arrify/**

- [[readme]] — $ npm install arrify

**banco/.netlify/plugins/node_modules/ast-module-types/**

- [[README]] — Collection of useful helper functions when trying to determine module type (CommonJS or AMD) properties of an AST node.

**banco/.netlify/plugins/node_modules/async/**

- [[CHANGELOG]] — The async/await release!
- [[README]] — <!-- |Linux|Windows|MacOS| |-|-|-| |[![Linux Build Status](https://dev.azure.com/caolanmcmahon/async/_apis/build/status/caolan.async?branchN...

**banco/.netlify/plugins/node_modules/async-function/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — A function that returns the normally hidden AsyncFunction constructor, when available.

**banco/.netlify/plugins/node_modules/async-mutex/**

- [[README]] — This package implements primitives for synchronizing asynchronous operations in Javascript.

**banco/.netlify/plugins/node_modules/async-retry/**

- [[LICENSE]] — The MIT License (MIT)
- [[README]] — Retrying made simple, easy, and async.

**banco/.netlify/plugins/node_modules/async-sema/**

- [[license]] — The MIT License (MIT)
- [[readme]] — This is a semaphore implementation for use with async and await.

**banco/.netlify/plugins/node_modules/asynckit/**

- [[README]] — Minimal async jobs utility library, with streams support.

**banco/.netlify/plugins/node_modules/at-least-node/**

- [[README]] — Sometimes you need to check if you're on _at least_ a given Node.js version, but you don't want to pull in the whole [semver](https://www.np...

**banco/.netlify/plugins/node_modules/autoprefixer/**

- [[README]] — <img align="right" width="94" height="71" src="https://postcss.github.io/autoprefixer/logo.svg" title="Autoprefixer logo by Anton Lovchikov"...

**banco/.netlify/plugins/node_modules/available-typed-arrays/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Returns an array of Typed Array names that are available in the current environment.

**banco/.netlify/plugins/node_modules/axios/**

- [[CHANGELOG]] — This release raises the form-data security floor, adds configuration and type-system capabilities, and fixes NO_PROXY matching, interceptor...
- [[MIGRATION_GUIDE]] — Axios 1.x introduced several breaking changes to improve consistency, security, and developer experience.
- [[README]] — <h3 align="center">💎 Platinum sponsors <br /></h3> <table align="center"> <tr> <td align="center" width="50%"> <a href="https://thanks.dev/?...

**banco/.netlify/plugins/node_modules/axios/lib/adapters/**

- [[README]] — The modules under adapters/ are modules that handle dispatching a request and settling a returned Promise once a response is received.

**banco/.netlify/plugins/node_modules/axios/lib/core/**

- [[README]] — The modules found in core/ should be modules that are specific to the domain logic of axios.

**banco/.netlify/plugins/node_modules/axios/lib/env/**

- [[README]] — The data.js file is updated automatically when the package version is upgrading.

**banco/.netlify/plugins/node_modules/axios/lib/helpers/**

- [[README]] — The modules found in helpers/ should be generic modules that are _not_ specific to the domain logic of axios.

**banco/.netlify/plugins/node_modules/axios/node_modules/agent-base/**

- [[README]] — agent-base ========== ### Turn a function into an [http.Agent][http.Agent] instance [![Build Status](https://github.com/TooTallNate/node-age...

**banco/.netlify/plugins/node_modules/axios/node_modules/https-proxy-agent/**

- [[README]] — https-proxy-agent ================ ### An HTTP(s) proxy http.Agent implementation for HTTPS [![Build Status](https://github.com/TooTallNate/...

**banco/.netlify/plugins/node_modules/babel-plugin-macros/**

- [[CHANGELOG]] — The changelog is automatically updated using [semantic-release](https://github.com/semantic-release/semantic-release).
- [[README]] — <div align="center"> <h1>babel-plugin-macros 🎣</h1>

**banco/.netlify/plugins/node_modules/babel-plugin-macros/node_modules/resolve/**

- [[SECURITY]] — Please [file a private vulnerability report](https://github.com/browserify/resolve/security/advisories/new), or email [@ljharb](https://gith...

**banco/.netlify/plugins/node_modules/babel-plugin-macros/node_modules/resolve/.github/**

- [[INCIDENT_RESPONSE_PROCESS]] — We take the security of resolve very seriously.
- [[THREAT_MODEL]] — This threat model focuses on the core path resolution algorithm, including filesystem interaction, option handling, and cache management.

**banco/.netlify/plugins/node_modules/balanced-match/**

- [[LICENSE]] — (MIT)
- [[README]] — Match balanced string pairs, like { and } or <b> and </b>.

**banco/.netlify/plugins/node_modules/bare-events/**

- [[README]] — Event emitters for JavaScript.

**banco/.netlify/plugins/node_modules/bare-fs/**

- [[README]] — Native file system operations for Bare. The API closely follows that of the Node.js fs module.

**banco/.netlify/plugins/node_modules/bare-path/**

- [[README]] — Path manipulation library for JavaScript.

**banco/.netlify/plugins/node_modules/bare-stream/**

- [[README]] — Streaming data for JavaScript. The classic Node.js-style stream classes are backed by streamx (<https://github.com/mafintosh/streamx>) while...

**banco/.netlify/plugins/node_modules/bare-stream/node_modules/b4a/**

- [[README]] — Buffer for Array (B4A) provides a set of functions for bridging the gap between the Node.js Buffer class and the Uint8Array class.

**banco/.netlify/plugins/node_modules/bare-url/**

- [[README]] — WHATWG URL implementation for JavaScript, built on <https://github.com/holepunchto/liburl>.

**banco/.netlify/plugins/node_modules/base64-js/**

- [[README]] — base64-js =========

**banco/.netlify/plugins/node_modules/baseline-browser-mapping/**

- [[README]] — By the [W3C WebDX Community Group](https://www.w3.org/community/webdx/) and contributors.

**banco/.netlify/plugins/node_modules/before-after-hook/**

- [[README]] — // instantiate singular hook API const hook = new Hook.Singular();

**banco/.netlify/plugins/node_modules/better-opn/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — If you wish to overwrite the default browser, override BROWSER environment variable to your desire browser name (name is platform dependent)...

**banco/.netlify/plugins/node_modules/better-opn/node_modules/is-docker/**

- [[readme]] — $ npm install is-docker

**banco/.netlify/plugins/node_modules/better-opn/node_modules/open/**

- [[readme]] — This is meant to be used in command-line tools and scripts, not in the browser.

**banco/.netlify/plugins/node_modules/big-integer/**

- [[README]] — [travis-url]: https://travis-ci.org/peterolson/BigInteger.js [travis-img]: https://travis-ci.org/peterolson/BigInteger.js.svg?branch=master...

**banco/.netlify/plugins/node_modules/bignumber.js/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[LICENCE]] — The MIT License (MIT) =====================
- [[README]] — A JavaScript library for arbitrary-precision decimal and non-decimal arithmetic.

**banco/.netlify/plugins/node_modules/binary-extensions/**

- [[readme]] — The list is just a [JSON file](binary-extensions.json) and can be used anywhere.

**banco/.netlify/plugins/node_modules/bindings/**

- [[LICENSE]] — (The MIT License)
- [[README]] — node-bindings ============= ### Helper module for loading your native module's .node file

**banco/.netlify/plugins/node_modules/bl/**

- [[LICENSE]] — The MIT License (MIT) =====================
- [[README]] — A Node.js Buffer list collector, reader and streamer thingy.

**banco/.netlify/plugins/node_modules/bl/node_modules/buffer/**

- [[AUTHORS]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — [travis-image]: https://img.shields.io/travis/feross/buffer/master.svg [travis-url]: https://travis-ci.org/feross/buffer [npm-image]: https:...

**banco/.netlify/plugins/node_modules/bl/node_modules/readable-stream/**

- [[CONTRIBUTING]] — By making a contribution to this project, I certify that:
- [[GOVERNANCE]] — The Node.js Streams is jointly governed by a Working Group (WG) that is responsible for high-level guidance of the project.
- [[README]] — *Node.js core streams for userland* [![Build Status](https://travis-ci.com/nodejs/readable-stream.svg?branch=master)](https://travis-ci.com/...

**banco/.netlify/plugins/node_modules/bluebird/**

- [[README]] — Bluebird is a fully featured promise library with focus on innovative features and performance
- [[changelog]] — [http://bluebirdjs.com/docs/changelog.html](http://bluebirdjs.com/docs/changelog.html)

**banco/.netlify/plugins/node_modules/body-parser/**

- [[HISTORY]] — 1.20.8 ===================
- [[README]] — Node.js body parsing middleware.

**banco/.netlify/plugins/node_modules/body-parser/node_modules/debug/**

- [[CHANGELOG]] — 2.6.9 / 2017-09-22 ==================
- [[README]] — A tiny node.js debugging utility modelled after node core's debugging technique.

**banco/.netlify/plugins/node_modules/body-parser/node_modules/ms/**

- [[license]] — The MIT License (MIT)
- [[readme]] — Use this package to easily convert various time formats to milliseconds.

**banco/.netlify/plugins/node_modules/boolbase/**

- [[README]] — This very simple module provides two basic functions, one that always returns true (trueFunc) and one that always returns false (falseFunc).

**banco/.netlify/plugins/node_modules/bplist-parser/**

- [[README]] — Binary Mac OS X Plist (property list) parser.

**banco/.netlify/plugins/node_modules/brace-expansion/**

- [[README]] — [Brace expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html), as known from sh/bash, in JavaScript.

**banco/.netlify/plugins/node_modules/braces/**

- [[README]] — Please consider following this project's author, [Jon Schlinkert](https://github.com/jonschlinkert), and consider starring the project to sh...

**banco/.netlify/plugins/node_modules/browserslist/**

- [[README]] — <img width="120" height="120" alt="Browserslist logo by Anton Popov" src="https://browsersl.ist/logo.svg" align="right">

**banco/.netlify/plugins/node_modules/buffer/**

- [[AUTHORS]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — [travis-image]: https://img.shields.io/travis/feross/buffer/master.svg [travis-url]: https://travis-ci.org/feross/buffer [npm-image]: https:...

**banco/.netlify/plugins/node_modules/buffer-crc32/**

- [[README]] — crc32 that works with binary data and fancy character sets, outputs buffer, signed or unsigned data and has tests.

**banco/.netlify/plugins/node_modules/buffer-equal-constant-time/**

- [[README]] — Constant-time Buffer comparison for node.js.

**banco/.netlify/plugins/node_modules/buffer-from/**

- [[readme]] — A [ponyfill](https://ponyfill.com) for Buffer.from, uses native implementation if available.

**banco/.netlify/plugins/node_modules/builtin-modules/**

- [[readme]] — The list is just a [JSON file](builtin-modules.json) and can be used anywhere.

**banco/.netlify/plugins/node_modules/bundle-name/**

- [[readme]] — $ npm install bundle-name

**banco/.netlify/plugins/node_modules/bytes/**

- [[History]] — 3.1.2 / 2022-01-27 ==================
- [[Readme]] — Utility to parse a string bytes (ex: 1TB) to bytes (1099511627776) and vice-versa.

**banco/.netlify/plugins/node_modules/cache-manager/**

- [[History]] — in an options object which will be passed to the cache store's set method.
- [[README]] — A cache module for nodejs that allows easy wrapping of functions in cache, tiered caches, and a consistent interface.

**banco/.netlify/plugins/node_modules/cache-manager/node_modules/async/**

- [[CHANGELOG]] — New Features: - Added constant - Added asyncify/wrapSync for making sync functions work with callbacks.
- [[README]] — Async is a utility module which provides straight-forward, powerful functions for working with asynchronous JavaScript.

**banco/.netlify/plugins/node_modules/cacheable-lookup/**

- [[README]] — Making lots of HTTP requests? You can save some time by caching DNS lookups :zap:

**banco/.netlify/plugins/node_modules/cacheable-request/**

- [[README]] — [RFC 7234](http://httpwg.org/specs/rfc7234.html) compliant HTTP caching for native Node.js HTTP/HTTPS requests.

**banco/.netlify/plugins/node_modules/cacheable-request/node_modules/get-stream/**

- [[readme]] — $ npm install get-stream

**banco/.netlify/plugins/node_modules/call-bind/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Robustly .call.bind() a function.

**banco/.netlify/plugins/node_modules/call-bind-apply-helpers/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Helper functions around Function call/apply/bind, for use in call-bind.

**banco/.netlify/plugins/node_modules/call-bound/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Robust call-bound JavaScript intrinsics, using call-bind and get-intrinsic.

**banco/.netlify/plugins/node_modules/callsite/**

- [[History]] — 1.0.0 / 2013-01-24 ==================
- [[Readme]] — Access to v8's "raw" CallSites.

**banco/.netlify/plugins/node_modules/callsites/**

- [[readme]] — $ npm install callsites

**banco/.netlify/plugins/node_modules/camelcase/**

- [[readme]] — Correctly handles Unicode strings.

**banco/.netlify/plugins/node_modules/camelcase-css/**

- [[README]] — [Node.js](http://nodejs.org/) >= 6 is required.

**banco/.netlify/plugins/node_modules/camelize-ts/**

- [[README]] — camelize-ts === [![CI](https://github.com/kbrabrand/camelize-ts/actions/workflows/main.yml/badge.svg)](https://github.com/kbrabrand/camelize...

**banco/.netlify/plugins/node_modules/caniuse-lite/**

- [[README]] — A smaller version of caniuse-db, with only the essentials!

**banco/.netlify/plugins/node_modules/capture-stack-trace/**

- [[readme]] — $ npm install --save capture-stack-trace

**banco/.netlify/plugins/node_modules/ccount/**

- [[readme]] — Count how often a character (or substring) is used in a string.

**banco/.netlify/plugins/node_modules/chalk/**

- [[readme]] — <h1 align="center"> <br> <br> <img width="320" src="media/logo.svg" alt="Chalk"> <br> <br> <br> </h1>

**banco/.netlify/plugins/node_modules/chance/**

- [[README]] — Chance - Random generator helper for JavaScript

**banco/.netlify/plugins/node_modules/chance/.github/**

- [[pull_request_template]] — TODO — nessuna prosa dopo il titolo.

**banco/.netlify/plugins/node_modules/chance/docs/**

- [[README]] — <script type="text/javascript" src="chance.js"></script>
- [[intro]] — Chance is a minimalist generator of random <a href="#true-random">[1]</a> strings, numbers, etc.

**banco/.netlify/plugins/node_modules/chance/docs/basics/**

- [[bool]] — // usages chance.bool() chance.bool({ likelihood: 30 })  Return a random boolean value (true or false).
- [[character]] — // usages chance.character() chance.character({ pool: 'abcde' }) chance.character({ alpha: true }) chance.character({ numeric: true }) chanc...
- [[falsy]] — // usages chance.falsy() chance.falsy({ pool: [ NaN, undefined ] })  Return a random falsy value (false, null, undefined, 0, NaN, '').
- [[floating]] — // usages chance.floating() chance.floating({ fixed: 7 }) chance.floating({ min: 0, max: 100 })  <p class="pullquote">I wanted to use float...
- [[integer]] — // usage chance.integer() chance.integer({ min: -20, max: 20 })
- [[letter]] — // usage chance.letter() chance.letter({ casing: 'lower' })
- [[natural]] — // usage chance.natural() chance.natural({ min: 1, max: 20 })
- [[prime]] — // usage chance.prime() chance.prime({ min: 1, max: 20 })
- [[string]] — // usage chance.string() chance.string({ length: 5 }) chance.string({ min: 5 }) chance.string({ max: 50 }) chance.string({ min: 5, max: 20 }...
- [[template]] — Return a random string matching the given template.

**banco/.netlify/plugins/node_modules/chance/docs/finance/**

- [[cc]] — // usage chance.cc() chance.cc({type: 'Mastercard'})
- [[cc_type]] — // usage chance.cc_type() chance.cc_type({raw: true})
- [[currency]] — // usage chance.currency()
- [[currency_pair]] — // usage chance.currency_pair()
- [[dollar]] — // usage chance.dollar() chance.dollar({max: 250})
- [[euro]] — // usage chance.euro() chance.euro({max: 250})
- [[exp]] — // usage chance.exp() chance.exp({raw: true})
- [[exp_month]] — // usage chance.exp_month() chance.exp_month({future: true})
- [[exp_year]] — // usage chance.exp_year()

**banco/.netlify/plugins/node_modules/chance/docs/helpers/**

- [[capitalize]] — // usage chance.capitalize(string)
- [[mixin]] — // usage chance.mixin(<Object>)
- [[pad]] — // usage chance.pad(number, width) chance.pad(number, width, padder)
- [[pick]] — // usage chance.pick(array) chance.pick(array, count)
- [[pickone]] — // usage chance.pickone(array)
- [[pickset]] — // usage chance.pickset(array, quantity)
- [[set]] — // usage chance.set(key, value)
- [[shuffle]] — // usage chance.shuffle(array)

**banco/.netlify/plugins/node_modules/chance/docs/location/**

- [[address]] — // usage chance.address() chance.address({short_suffix: true})
- [[altitude]] — // usage chance.altitude() chance.altitude({ fixed: 7 }) chance.altitude({ max: 1000 })
- [[areacode]] — // usage chance.areacode()
- [[city]] — // usage chance.city()
- [[coordinates]] — // usage chance.coordinates() chance.coordinates({fixed: 2}) chance.coordinates({format: 'dms'})
- [[country]] — // usage chance.country() chance.country({ full: true })
- [[depth]] — // usage chance.depth() chance.depth({ fixed: 2 }) chance.depth({ min: -1000 })
- [[geohash]] — // usage chance.geohash() chance.geohash({ length: 5 })
- [[latitude]] — // usage chance.latitude() chance.latitude({fixed: 7}) chance.latitude({format: 'dms'})
- [[locale]] — // usage chance.locale() chance.locale({region: true})
- [[longitude]] — // usage chance.longitude() chance.longitude({fixed: 7}) chance.longitude({format: 'dms'})
- [[phone]] — // usage chance.phone() chance.phone({ formatted: false }) chance.phone({ country: "fr" }) chance.phone({ country: "fr", mobile: true })
- [[postal]] — // usage chance.postal()
- [[postcode]] — // usage chance.postcode()
- [[province]] — // usage chance.province() chance.province({full: true}) chance.province({full: true})
- [[state]] — // usage chance.state() chance.state({ full: true }) chance.state({ territories: true }) chance.state({ armed_forces: true }) chance.state({...
- [[street]] — // usage chance.street() chance.street({country:it})
- [[zip]] — // usage chance.zip() chance.zip({plusfour: true})

**banco/.netlify/plugins/node_modules/chance/docs/miscellaneous/**

- [[coin]] — // usage chance.coin()
- [[dice]] — // usage chance.d4() chance.d6() chance.d8() chance.d10() chance.d12() chance.d20() chance.d30() chance.d100()
- [[fileWithContent]] — Generates a file with random name, extention and data js // Usage chance.fileWithContent({ fileName: "AwesomeFile", fileExtension: "gif", fi...
- [[guid]] — // usage chance.guid() chance.guid({version: 5})
- [[hash]] — // usage chance.hash() chance.hash({length: 25}) chance.hash({casing: 'upper'})
- [[hidden]] — // usage chance.cc_types() chance.mersenne_twister() chance.mersenne_twister(12345) chance.months() chance.name_prefixes() chance.provinces(...
- [[n]] — // usage chance.n(chance.email, 5) chance.n(chance.email, 5, { domain: "socialradar.com" })
- [[normal]] — // usage chance.normal() chance.normal({mean: 100}) chance.normal({mean: 100, dev: 15})
- [[radio]] — // usage chance.radio()
- [[rpg]] — // usage chance.rpg('#d#') chance.rpg('#d#', {sum: true})
- [[tv]] — // usage chance.tv() chance.tv({side: 'west'})
- [[unique]] — // usage chance.unique(chance.state, 5) chance.unique(chance.state, 5, { comparator: func })
- [[weighted]] — // usage chance.weighted(['a', 'b'], [100, 1]) chance.weighted(['a', 'b', 'c', 'd'], [1, 2, 3, 4])

**banco/.netlify/plugins/node_modules/chance/docs/mobile/**

- [[android_id]] — // usage chance.android_id()
- [[apple_token]] — // usage chance.apple_token()
- [[bb_pin]] — // usage chance.bb_pin()
- [[wp7_anid]] — // usage chance.wp7_anid()
- [[wp8_anid2]] — // usage chance.wp8_anid2()

**banco/.netlify/plugins/node_modules/chance/docs/music/**

- [[music_genre]] — // usage chance.music_genre();
- [[note]] — // usage chance.note(); chance.note({ notes: 'flatkey' });
- [[tempo]] — // usage chance.tempo(); //default between 40 to 320 chance.tempo({ min: 60, max: 120 });

**banco/.netlify/plugins/node_modules/chance/docs/person/**

- [[aadhar]] — _Aadhar_ (English: Foundation) is a 12-digit unique identity number that can be obtained by residents of India, based on their biometric and...
- [[age]] — // usage chance.age() chance.age({ type: 'child' })
- [[birthday]] — // usage chance.birthday() chance.birthday({ string: true }) chance.birthday({ type: 'child' })
- [[cf]] — // usage chance.cf()  Generate a random Italian social security number (Codice Fiscale).
- [[cpf]] — // usage chance.cpf()
- [[first]] — // usage chance.first() chance.first({ nationality: 'en' })
- [[gender]] — // usage chance.gender()
- [[last]] — // usage chance.last() chance.last({ nationality: 'en' })
- [[name]] — // usage chance.name() chance.name({ middle: true }) chance.name({ middle_initial: true }) chance.name({ prefix: true }) chance.name({ natio...
- [[prefix]] — // usage chance.prefix() chance.prefix({ full: true })
- [[ssn]] — // usage chance.ssn() chance.ssn({ ssnFour: true }) chance.ssn({ dashes: false })
- [[suffix]] — // usage chance.suffix() chance.suffix({ full: true })
- [[zodiac]] — // usage chance.zodiac()  Generate a random zodiac signs.

**banco/.netlify/plugins/node_modules/chance/docs/text/**

- [[emoji]] — // usage chance.emoji(); chance.emoji({ category: "smileys_and_emotions" }); chance.emoji({ length: 5 });
- [[paragraph]] — // usage chance.paragraph() chance.paragraph({ sentences: 1 }) chance.paragraph({ linebreak: true })
- [[sentence]] — // usage chance.sentence() chance.sentence({ words: 5 })
- [[syllable]] — // usage chance.syllable()
- [[word]] — // usage chance.word() chance.word({ syllables: 3 }) chance.word({ length: 5 })

**banco/.netlify/plugins/node_modules/chance/docs/thing/**

- [[animal]] — // usage chance.animal() chance.animal({type: 'zoo'})

**banco/.netlify/plugins/node_modules/chance/docs/time/**

- [[ampm]] — // usage chance.ampm()
- [[date]] — // usage chance.date() chance.date({string: true}) chance.date({string: true, american: false}) chance.date({year: 1983})
- [[hammertime]] — // usage chance.hammertime()
- [[hour]] — // usage chance.hour() chance.hour({twentyfour: true})
- [[millisecond]] — // usage chance.millisecond()
- [[minute]] — // usage chance.minute()
- [[month]] — // usage chance.month()
- [[second]] — // usage chance.second()
- [[timestamp]] — // usage chance.timestamp()
- [[timezone]] — // usage chance.timezone()
- [[weekday]] — // usage chance.weekday() chance.weekday({weekday_only: true})
- [[year]] — // usage chance.year() chance.year({min: 1900, max: 2100})

**banco/.netlify/plugins/node_modules/chance/docs/usage/**

- [[bower]] — Chance can be easily installed with [Bower](https://bower.io)
- [[browser]] — Chance instantiates itself onto the window.
- [[cli]] — To use Chance from the command line, install chance-cli globally with:
- [[function]] — Instead of providing a seed, which will be used to seed our [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_twister), you can also...
- [[node]] — It can also be used in [Node.js](http://nodejs.org)
- [[requirejs]] — Load Chance with <a href="http://requirejs.org">RequireJS</a>
- [[seed]] — You can also instantiate your own instance of Chance with a known seed.

**banco/.netlify/plugins/node_modules/chance/docs/web/**

- [[avatar]] — // usage chance.avatar() chance.avatar({protocol: 'https'}) chance.avatar({fileExtension: 'jpg'}) chance.avatar({email: 'mail@victorquinn.co...
- [[color]] — // usage chance.color() chance.color({format: 'hex'}) chance.color({grayscale: true}) chance.color({casing: 'upper'})
- [[company]] — // usage chance.company()
- [[domain]] — // usage chance.domain() chance.domain({tld: 'com'})
- [[email]] — // usage chance.email() chance.email({domain: "example.com"})
- [[fbid]] — // usage chance.fbid()
- [[google_analytics]] — // usage chance.google_analytics()
- [[hashtag]] — // usage chance.hashtag()
- [[ip]] — // usage chance.ip()
- [[ipv6]] — // usage chance.ipv6()
- [[klout]] — // usage chance.klout()
- [[mac]] — // usage chance.mac() chance.mac({delimiter: '-'})
- [[profession]] — // usage chance.profession() chance.profession({rank: true})
- [[tld]] — // usage chance.tld()
- [[twitter]] — // usage chance.twitter()
- [[url]] — // usage chance.url() chance.url({protocol: 'ftp'}) chance.url({domain: 'www.socialradar.com'}) chance.url({domain_prefix: 'docs'}) chance.u...

**banco/.netlify/plugins/node_modules/character-entities/**

- [[readme]] — Map of named character references.

**banco/.netlify/plugins/node_modules/character-entities-html4/**

- [[readme]] — Map of named character references from HTML 4.

**banco/.netlify/plugins/node_modules/character-entities-legacy/**

- [[readme]] — List of legacy HTML named character references that don’t need a trailing semicolon.

**banco/.netlify/plugins/node_modules/character-reference-invalid/**

- [[readme]] — Map of invalid numeric character references to their replacements, according to HTML.

**banco/.netlify/plugins/node_modules/chardet/**

- [[README]] — chardet [![Build Status](https://travis-ci.org/runk/node-chardet.png)](https://travis-ci.org/runk/node-chardet) =====

**banco/.netlify/plugins/node_modules/chokidar/**

- [[README]] — There are many reasons to prefer Chokidar to raw fs.watch / fs.watchFile in 2024:

**banco/.netlify/plugins/node_modules/chownr/**

- [[LICENSE]] — Version 1.0.0
- [[README]] — Like chown -R.

**banco/.netlify/plugins/node_modules/ci-info/**

- [[CHANGELOG]] — Breaking changes:
- [[README]] — Get details about the current Continuous Integration environment.

**banco/.netlify/plugins/node_modules/cli-cursor/**

- [[readme]] — The cursor is [gracefully restored](https://github.com/sindresorhus/restore-cursor) if the process exits.

**banco/.netlify/plugins/node_modules/cli-width/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Get stdout window width, with four fallbacks, tty, output.columns, a custom environment variable and then a default.

**banco/.netlify/plugins/node_modules/cliui/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — easily create complex multi-column command-line-interfaces.

**banco/.netlify/plugins/node_modules/cliui/node_modules/ansi-styles/**

- [[readme]] — You probably want the higher-level [chalk](https://github.com/chalk/chalk) module for styling your strings.

**banco/.netlify/plugins/node_modules/cliui/node_modules/emoji-regex/**

- [[README]] — _emoji-regex_ offers a regular expression to match all emoji symbols (including textual representations of emoji) as per the Unicode Standar...

**banco/.netlify/plugins/node_modules/cliui/node_modules/string-width/**

- [[readme]] — Some Unicode characters are [fullwidth](https://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms) and use double the normal width.

**banco/.netlify/plugins/node_modules/cliui/node_modules/wrap-ansi/**

- [[readme]] — $ npm install wrap-ansi

**banco/.netlify/plugins/node_modules/clone-response/**

- [[README]] — Returns a new stream and copies over all properties and methods from the original response giving you a complete duplicate.

**banco/.netlify/plugins/node_modules/clone-response/node_modules/mimic-response/**

- [[readme]] — $ npm install mimic-response

**banco/.netlify/plugins/node_modules/clsx/**

- [[readme]] — This module is available in three formats:

**banco/.netlify/plugins/node_modules/color/**

- [[README]] — const color = Color('#7743CE').alpha(0.5).lighten(0.5); console.log(color.hsl().string());  // 'hsla(262, 59%, 81%, 0.5)'

**banco/.netlify/plugins/node_modules/color-convert/**

- [[CHANGELOG]] — ([#27](https://github.com/Qix-/color-convert/pull/27)) - Removed: xxx2xxx() and xxx2xxxRaw() functions ([#27](https://github.com/Qix-/color-...
- [[README]] — Color-convert is a color conversion library for JavaScript and node.

**banco/.netlify/plugins/node_modules/color-name/**

- [[README]] — A JSON with color names and its values. Based on http://dev.w3.org/csswg/css-color/#named-colors.

**banco/.netlify/plugins/node_modules/color-string/**

- [[README]] — With [npm](http://npmjs.org/):

**banco/.netlify/plugins/node_modules/combined-stream/**

- [[Readme]] — A stream that emits multiple other streams one after another.

**banco/.netlify/plugins/node_modules/comma-separated-tokens/**

- [[readme]] — Parse and stringify comma-separated tokens.

**banco/.netlify/plugins/node_modules/command-exists/**

- [[README]] — command-exists ==============

**banco/.netlify/plugins/node_modules/commander/**

- [[Readme]] — The complete solution for [node.js](http://nodejs.org) command-line interfaces.

**banco/.netlify/plugins/node_modules/common-path-prefix/**

- [[README]] — Computes the longest prefix string that is common to each path, excluding the base component.

**banco/.netlify/plugins/node_modules/common-tags/**

- [[license]] — License (MIT) -------------
- [[readme]] — 🔖 A set of well-tested, commonly used template literal tag functions for use in ES2015+.

**banco/.netlify/plugins/node_modules/compress-commons/**

- [[README]] — Compress Commons is a library that defines a common interface for working with archive formats within node.

**banco/.netlify/plugins/node_modules/compress-commons/node_modules/is-stream/**

- [[readme]] — $ npm install is-stream

**banco/.netlify/plugins/node_modules/compressible/**

- [[HISTORY]] — 2.0.18 / 2020-01-05 ===================
- [[README]] — Compressible Content-Type / mime checking.

**banco/.netlify/plugins/node_modules/compression/**

- [[README]] — Node.js compression middleware.

**banco/.netlify/plugins/node_modules/compression/node_modules/debug/**

- [[CHANGELOG]] — 2.6.9 / 2017-09-22 ==================
- [[README]] — A tiny node.js debugging utility modelled after node core's debugging technique.

**banco/.netlify/plugins/node_modules/compression/node_modules/ms/**

- [[license]] — The MIT License (MIT)
- [[readme]] — Use this package to easily convert various time formats to milliseconds.

**banco/.netlify/plugins/node_modules/compute-scroll-into-view/**

- [[README]] — npm i compute-scroll-into-view

**banco/.netlify/plugins/node_modules/configstore/**

- [[readme]] — The config is stored in a JSON file located in $XDG_CONFIG_HOME or ~/.config.\ Example: ~/.config/configstore/some-id.json

**banco/.netlify/plugins/node_modules/configstore/node_modules/dot-prop/**

- [[readme]] — $ npm install dot-prop

**banco/.netlify/plugins/node_modules/configstore/node_modules/write-file-atomic/**

- [[CHANGELOG]] — error.
- [[README]] — write-file-atomic -----------------

**banco/.netlify/plugins/node_modules/configstore/node_modules/xdg-basedir/**

- [[readme]] — This package is meant for Linux. You should not use XDG on macOS or Windows.

**banco/.netlify/plugins/node_modules/consola/**

- [[README]] — <!-- [![Codecov][codecov-src]][codecov-href] -->

**banco/.netlify/plugins/node_modules/content-disposition/**

- [[HISTORY]] — 0.5.4 / 2021-12-10 ==================
- [[README]] — Create and parse HTTP Content-Disposition header

**banco/.netlify/plugins/node_modules/content-engine/**

- [[README]] — TODO — nessuna prosa dopo il titolo.

**banco/.netlify/plugins/node_modules/content-engine/node_modules/ansi-styles/**

- [[readme]] — You probably want the higher-level [chalk](https://github.com/chalk/chalk) module for styling your strings.

**banco/.netlify/plugins/node_modules/content-engine/node_modules/axios/**

- [[CHANGELOG]] — Fixes and Functionality: - Fixing JSON transform when data is stringified.
- [[README]] — Promise based HTTP client for the browser and node.js
- [[SECURITY]] — Please report security issues to jasonsaayman@gmail.com
- [[UPGRADE_GUIDE]] — The Promise type declarations have been removed from the axios typings in favor of the built-in type declarations.

**banco/.netlify/plugins/node_modules/content-engine/node_modules/axios/lib/adapters/**

- [[README]] — The modules under adapters/ are modules that handle dispatching a request and settling a returned Promise once a response is received.

**banco/.netlify/plugins/node_modules/content-engine/node_modules/axios/lib/core/**

- [[README]] — The modules found in core/ should be modules that are specific to the domain logic of axios.

**banco/.netlify/plugins/node_modules/content-engine/node_modules/axios/lib/helpers/**

- [[README]] — The modules found in helpers/ should be generic modules that are _not_ specific to the domain logic of axios.

**banco/.netlify/plugins/node_modules/content-engine/node_modules/brace-expansion/**

- [[README]] — [Brace expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html), as known from sh/bash, in JavaScript.

**banco/.netlify/plugins/node_modules/content-engine/node_modules/chalk/**

- [[readme]] — <h1 align="center"> <br> <br> <img width="320" src="media/logo.svg" alt="Chalk"> <br> <br> <br> </h1>

**banco/.netlify/plugins/node_modules/content-engine/node_modules/execa/**

- [[readme]] — <img src="media/logo.svg" width="400"> <br>

**banco/.netlify/plugins/node_modules/content-engine/node_modules/get-stream/**

- [[readme]] — $ npm install get-stream

**banco/.netlify/plugins/node_modules/content-engine/node_modules/glob/**

- [[README]] — Match files using the patterns the shell uses, like stars and stuff.

**banco/.netlify/plugins/node_modules/content-engine/node_modules/graphql/**

- [[README]] — The JavaScript reference implementation for GraphQL, a query language for APIs created by Facebook.

**banco/.netlify/plugins/node_modules/content-engine/node_modules/human-signals/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — const { signalsByName, signalsByNumber } = require('human-signals')

**banco/.netlify/plugins/node_modules/content-engine/node_modules/is-stream/**

- [[readme]] — $ npm install is-stream

**banco/.netlify/plugins/node_modules/content-engine/node_modules/minimatch/**

- [[README]] — A minimal matching utility.

**banco/.netlify/plugins/node_modules/content-engine/node_modules/npm-run-path/**

- [[readme]] — In [npm run scripts](https://docs.npmjs.com/cli/run-script) you can execute locally installed binaries by name.

**banco/.netlify/plugins/node_modules/content-engine/node_modules/strip-final-newline/**

- [[readme]] — Can be useful when parsing the output of, for example, ChildProcess#execFile, as [binaries usually output a newline at the end](https://stac...

**banco/.netlify/plugins/node_modules/content-type/**

- [[HISTORY]] — 1.0.5 / 2023-01-29 ==================
- [[README]] — Create and parse HTTP Content-Type header according to RFC 7231

**banco/.netlify/plugins/node_modules/contentful/**

- [[README]] — _JavaScript library for the Contentful [Content Delivery API](https://www.contentful.com/developers/docs/references/content-delivery-api/) a...

**banco/.netlify/plugins/node_modules/contentful-management/**

- [[README]] — To get started with the Contentful Management JS library you'll need to install it, and then get credentials which will allow you to access...

**banco/.netlify/plugins/node_modules/contentful-management/node_modules/axios/**

- [[CHANGELOG]] — Fixes and Functionality: - Fixing JSON transform when data is stringified.
- [[README]] — Promise based HTTP client for the browser and node.js
- [[SECURITY]] — Please report security issues to jasonsaayman@gmail.com
- [[UPGRADE_GUIDE]] — The Promise type declarations have been removed from the axios typings in favor of the built-in type declarations.

**banco/.netlify/plugins/node_modules/contentful-management/node_modules/axios/lib/adapters/**

- [[README]] — The modules under adapters/ are modules that handle dispatching a request and settling a returned Promise once a response is received.

**banco/.netlify/plugins/node_modules/contentful-management/node_modules/axios/lib/core/**

- [[README]] — The modules found in core/ should be modules that are specific to the domain logic of axios.

**banco/.netlify/plugins/node_modules/contentful-management/node_modules/axios/lib/helpers/**

- [[README]] — The modules found in helpers/ should be generic modules that are _not_ specific to the domain logic of axios.

**banco/.netlify/plugins/node_modules/contentful-management/node_modules/contentful-sdk-core/**

- [[README]] — [Contentful](https://www.contentful.com) provides a content infrastructure for digital teams to power content in websites, apps, and devices...

**banco/.netlify/plugins/node_modules/contentful-management/node_modules/type-fest/**

- [[readme]] — <div align="center"> <br> <br> <img src="media/logo.svg" alt="type-fest" height="300"> <br> <br> <b>A collection of essential TypeScript typ...

**banco/.netlify/plugins/node_modules/contentful-resolve-response/**

- [[README]] — Suppose you have a Contentful query's response JSON.

**banco/.netlify/plugins/node_modules/contentful-resolve-response/node_modules/fast-copy/**

- [[CHANGELOG]] — (defaults to 1000, pass Infinity to traverse without a limit) - Throw the new MaxDepthExceededError when a value is nested more deeply than...
- [[README]] — <img src="https://img.shields.io/badge/build-passing-brightgreen.svg"/> <img src="https://img.shields.io/badge/coverage-100%25-brightgreen.s...

**banco/.netlify/plugins/node_modules/contentful-sdk-core/**

- [[README]] — [Contentful](https://www.contentful.com) provides a content infrastructure for digital teams to power content in websites, apps, and devices...

**banco/.netlify/plugins/node_modules/contentful/node_modules/@contentful/rich-text-types/**

- [[README]] — Type definitions and constants for the Contentful rich text field type.

**banco/.netlify/plugins/node_modules/convert-hrtime/**

- [[readme]] — $ npm install convert-hrtime

**banco/.netlify/plugins/node_modules/convert-source-map/**

- [[README]] — Converts a source-map from/to  different formats and allows adding/changing properties.

**banco/.netlify/plugins/node_modules/cookie/**

- [[README]] — Basic HTTP cookie parser and serializer for HTTP servers.
- [[SECURITY]] — The cookie team and community take all security bugs seriously.

**banco/.netlify/plugins/node_modules/cookie-signature/**

- [[History]] — 1.0.7 / 2023-04-12 ==================
- [[Readme]] — Sign and unsign cookies.

**banco/.netlify/plugins/node_modules/copy-file/**

- [[readme]] — npm install copy-file

**banco/.netlify/plugins/node_modules/core-util-is/**

- [[README]] — The util.is* functions introduced in Node v0.12.

**banco/.netlify/plugins/node_modules/cors/**

- [[README]] — CORS is a [Node.js](https://nodejs.org/en/) middleware for [Express](https://expressjs.com/)/[Connect](https://github.com/senchalabs/connect...

**banco/.netlify/plugins/node_modules/cosmiconfig/**

- [[README]] — Cosmiconfig searches for and loads configuration for your program.

**banco/.netlify/plugins/node_modules/crc-32/**

- [[README]] — Standard CRC-32 algorithm implementation in JS (for the browser and nodejs).

**banco/.netlify/plugins/node_modules/crc32-stream/**

- [[README]] — crc32-stream is a streaming CRC32 checksumer.

**banco/.netlify/plugins/node_modules/create-error-class/**

- [[readme]] — $ npm install --save create-error-class

**banco/.netlify/plugins/node_modules/cron-parser/**

- [[README]] — cron-parser ================

**banco/.netlify/plugins/node_modules/cross-spawn/**

- [[README]] — [npm-url]:https://npmjs.org/package/cross-spawn [downloads-image]:https://img.shields.io/npm/dm/cross-spawn.svg [npm-image]:https://img.shie...

**banco/.netlify/plugins/node_modules/crypto-js/**

- [[CONTRIBUTING]] — The crypto-js project uses [git flow](https://github.com/nvie/gitflow) to manage branches.
- [[README]] — JavaScript library of crypto standards.

**banco/.netlify/plugins/node_modules/crypto-random-string/**

- [[readme]] — Can be useful for creating an identifier, slug, salt, PIN code, fixture, etc.

**banco/.netlify/plugins/node_modules/crypto-random-string/node_modules/type-fest/**

- [[readme]] — <div align="center"> <br> <br> <img src="media/logo.svg" alt="type-fest" height="300"> <br> <br> <b>A collection of essential TypeScript typ...

**banco/.netlify/plugins/node_modules/css-select/**

- [[README]] — A CSS selector compiler and engine

**banco/.netlify/plugins/node_modules/css-what/**

- [[readme]] — A CSS selector parser.

**banco/.netlify/plugins/node_modules/cssesc/**

- [[README]] — A JavaScript library for escaping CSS strings and identifiers while generating the shortest possible ASCII-only output.

**banco/.netlify/plugins/node_modules/cssstyle/**

- [[README]] — A Node JS implementation of the CSS Object Model [CSSStyleDeclaration interface](https://www.w3.org/TR/cssom-1/#the-cssstyledeclaration-inte...

**banco/.netlify/plugins/node_modules/csstype/**

- [[README]] — TypeScript and Flow definitions for CSS, generated by [data from MDN](https://github.com/mdn/data).

**banco/.netlify/plugins/node_modules/d/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — _Originally derived from [d](https://github.com/medikoo/d) package._

**banco/.netlify/plugins/node_modules/data-uri-to-buffer/**

- [[README]] — data-uri-to-buffer ================== ### Generate a Buffer instance from a [Data URI][rfc] string [![Build Status](https://travis-ci.org/To...

**banco/.netlify/plugins/node_modules/data-urls/**

- [[README]] — This package helps you parse data: URLs [according to the WHATWG Fetch Standard](https://fetch.spec.whatwg.org/#data-urls):

**banco/.netlify/plugins/node_modules/data-view-buffer/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Get the ArrayBuffer out of a DataView, robustly.

**banco/.netlify/plugins/node_modules/data-view-byte-length/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Get the byteLength out of a DataView, robustly.

**banco/.netlify/plugins/node_modules/data-view-byte-offset/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Get the byteOffset out of a DataView, robustly.

**banco/.netlify/plugins/node_modules/dataloader/**

- [[README]] — DataLoader is a generic utility to be used as part of your application's data fetching layer to provide a simplified and consistent API over...

**banco/.netlify/plugins/node_modules/debug/**

- [[README]] — <img width="647" src="https://user-images.githubusercontent.com/71256/29091486-fa38524c-7c37-11e7-895f-e7ec8e1039b6.png">

**banco/.netlify/plugins/node_modules/decache/**

- [[README]] — Delete a module from node.js' require.cache so you can freshly require it again.

**banco/.netlify/plugins/node_modules/decimal.js/**

- [[LICENCE]] — The MIT Licence.
- [[README]] — An arbitrary-precision Decimal type for JavaScript.

**banco/.netlify/plugins/node_modules/decode-named-character-reference/**

- [[readme]] — Decode named character references.

**banco/.netlify/plugins/node_modules/decompress-response/**

- [[readme]] — Decompresses the [response](https://nodejs.org/api/http.html#http_class_http_incomingmessage) from [http.request](https://nodejs.org/api/htt...

**banco/.netlify/plugins/node_modules/deep-extend/**

- [[CHANGELOG]] — Changelog =========
- [[README]] — Deep Extend ===========

**banco/.netlify/plugins/node_modules/default-browser/**

- [[readme]] — Works on macOS, Linux, and Windows.

**banco/.netlify/plugins/node_modules/default-browser-id/**

- [[readme]] — $ npm install default-browser-id

**banco/.netlify/plugins/node_modules/default-browser/node_modules/execa/**

- [[readme]] — <picture> <source media="(prefers-color-scheme: dark)" srcset="media/logo_dark.svg"> <img alt="execa logo" src="media/logo.svg" width="400">...

**banco/.netlify/plugins/node_modules/default-browser/node_modules/get-stream/**

- [[readme]] — $ npm install get-stream

**banco/.netlify/plugins/node_modules/default-browser/node_modules/human-signals/**

- [[README]] — Please [reach out](https://www.linkedin.com/feed/update/urn:li:activity:7018596298127781890/) if you're looking for a Node.js API or CLI eng...

**banco/.netlify/plugins/node_modules/default-browser/node_modules/is-stream/**

- [[readme]] — $ npm install is-stream

**banco/.netlify/plugins/node_modules/default-browser/node_modules/mimic-fn/**

- [[readme]] — <img src="media/logo.svg" alt="mimic-fn" width="400"> <br>

**banco/.netlify/plugins/node_modules/default-browser/node_modules/npm-run-path/**

- [[readme]] — In [npm run scripts](https://docs.npmjs.com/cli/run-script) you can execute locally installed binaries by name.

**banco/.netlify/plugins/node_modules/default-browser/node_modules/onetime/**

- [[readme]] — When called multiple times it will return the return value from the first call.

**banco/.netlify/plugins/node_modules/default-browser/node_modules/path-key/**

- [[readme]] — It's usually PATH but on Windows it can be any casing like Path...

**banco/.netlify/plugins/node_modules/default-browser/node_modules/strip-final-newline/**

- [[readme]] — Can be useful when parsing the output of, for example, ChildProcess#execFile, as [binaries usually output a newline at the end](https://stac...

**banco/.netlify/plugins/node_modules/defer-to-connect/**

- [[README]] — Once you receive the socket, it may be already connected (or disconnected).<br> To avoid checking that, use defer-to-connect.

**banco/.netlify/plugins/node_modules/define-data-property/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Define a data property on an object. Will fall back to assignment in an engine without descriptors.

**banco/.netlify/plugins/node_modules/define-lazy-prop/**

- [[readme]] — Useful when the value of a property is expensive to generate, so you want to delay the computation until the property is needed.

**banco/.netlify/plugins/node_modules/define-properties/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Define multiple non-enumerable properties at once.

**banco/.netlify/plugins/node_modules/delayed-stream/**

- [[Readme]] — Buffers events from a stream until you are ready to handle them.

**banco/.netlify/plugins/node_modules/depd/**

- [[History]] — 2.0.0 / 2018-10-26 ==================
- [[Readme]] — Deprecate all the things

**banco/.netlify/plugins/node_modules/deprecation/**

- [[README]] — <table> <tbody valign=top align=left> <tr><th> Browsers </th><td width=100%>

**banco/.netlify/plugins/node_modules/dequal/**

- [[readme]] — This module supports comparison of all types, including Function, RegExp, Date, Set, Map, TypedArrays, DataView, null, undefined, and NaN va...

**banco/.netlify/plugins/node_modules/destroy/**

- [[README]] — Destroy a stream.

**banco/.netlify/plugins/node_modules/detect-libc/**

- [[README]] — Node.js module to detect details of the C standard library (libc) implementation provided by a given Linux system.

**banco/.netlify/plugins/node_modules/detect-port/**

- [[README]] — $ detect

**banco/.netlify/plugins/node_modules/detective-amd/**

- [[README]] — Returns a list of dependencies for a given JavaScript file or AST using any of the AMD module syntaxes.

**banco/.netlify/plugins/node_modules/detective-cjs/**

- [[README]] — npm install detective-cjs

**banco/.netlify/plugins/node_modules/detective-es6/**

- [[README]] — npm install detective-es6

**banco/.netlify/plugins/node_modules/detective-postcss/**

- [[README]] — Supports @import and [@value ... from](https://github.com/css-modules/postcss-icss-values).

**banco/.netlify/plugins/node_modules/detective-sass/**

- [[README]] — npm install detective-sass

**banco/.netlify/plugins/node_modules/detective-scss/**

- [[README]] — npm install detective-scss

**banco/.netlify/plugins/node_modules/detective-stylus/**

- [[README]] — npm install detective-stylus

**banco/.netlify/plugins/node_modules/detective-typescript/**

- [[README]] — npm install detective-typescript typescript

**banco/.netlify/plugins/node_modules/detective-vue2/**

- [[README]] — npm install detective-vue2 typescript

**banco/.netlify/plugins/node_modules/devcert/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — So, running a local HTTPS server usually sucks.

**banco/.netlify/plugins/node_modules/devcert/node_modules/@types/configstore/**

- [[README]] — This package contains type definitions for configstore (https://github.com/yeoman/configstore).

**banco/.netlify/plugins/node_modules/devcert/node_modules/brace-expansion/**

- [[README]] — [Brace expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html), as known from sh/bash, in JavaScript.

**banco/.netlify/plugins/node_modules/devcert/node_modules/debug/**

- [[CHANGELOG]] — 3.1.0 / 2017-09-26 ==================
- [[README]] — <img width="647" src="https://user-images.githubusercontent.com/71256/29091486-fa38524c-7c37-11e7-895f-e7ec8e1039b6.png">

**banco/.netlify/plugins/node_modules/devcert/node_modules/glob/**

- [[README]] — Match files using the patterns the shell uses, like stars and stuff.

**banco/.netlify/plugins/node_modules/devcert/node_modules/minimatch/**

- [[README]] — A minimal matching utility.

**banco/.netlify/plugins/node_modules/devcert/node_modules/rimraf/**

- [[README]] — The [UNIX command](http://en.wikipedia.org/wiki/Rm_(Unix)) rm -rf for node.

**banco/.netlify/plugins/node_modules/devcert/node_modules/tslib/**

- [[README]] — This is a runtime library for [TypeScript](http://www.typescriptlang.org/) that contains all of the TypeScript helper functions.

**banco/.netlify/plugins/node_modules/devlop/**

- [[readme]] — Some tools to make developing easier while not including code in production.

**banco/.netlify/plugins/node_modules/didyoumean/**

- [[README]] — didYouMean.js - A simple JavaScript matching engine ===================================================

**banco/.netlify/plugins/node_modules/dir-glob/**

- [[readme]] — $ npm install dir-glob

**banco/.netlify/plugins/node_modules/dlv/**

- [[README]] — Smallest possible implementation: only 130 bytes.

**banco/.netlify/plugins/node_modules/dom-converter/**

- [[README]] — Converts bare objects to DOM objects, compatible with htmlparser2's DOM objects.

**banco/.netlify/plugins/node_modules/dom-helpers/**

- [[README]] — tiny modular DOM lib for ie9+

**banco/.netlify/plugins/node_modules/dom-serializer/**

- [[README]] — Renders a [domhandler](https://github.com/fb55/domhandler) DOM node or an array of domhandler DOM nodes to a string.

**banco/.netlify/plugins/node_modules/dom-walk/**

- [[README]] — iteratively walk a DOM node

**banco/.netlify/plugins/node_modules/domelementtype/**

- [[readme]] — All the types of nodes in htmlparser2's DOM.

**banco/.netlify/plugins/node_modules/domexception/**

- [[README]] — This package implements the [DOMException](https://heycam.github.io/webidl/#idl-DOMException) class, from web browsers.

**banco/.netlify/plugins/node_modules/domhandler/**

- [[readme]] — The DOM handler creates a tree containing all nodes of a page.

**banco/.netlify/plugins/node_modules/domutils/**

- [[readme]] — Utilities for working with [htmlparser2](https://github.com/fb55/htmlparser2)'s DOM.

**banco/.netlify/plugins/node_modules/dot-prop/**

- [[readme]] — npm install dot-prop

**banco/.netlify/plugins/node_modules/dotenv/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README-es]] — <img src="https://raw.githubusercontent.com/motdotla/dotenv/master/dotenv.svg" alt="dotenv" align="right" width="200" />
- [[README]] — <img src="https://raw.githubusercontent.com/motdotla/dotenv/master/dotenv.svg" alt="dotenv" align="right" width="200" />
- [[SECURITY]] — Please report any security vulnerabilities to security@dotenvx.com.

**banco/.netlify/plugins/node_modules/downshift/**

- [[README]] — <h1 align="center"> downshift 🏎 <br> <img src="https://raw.githubusercontent.com/downshift-js/downshift/master/other/public/logo/downshift.s...

**banco/.netlify/plugins/node_modules/dset/**

- [[readme]] — For _accessing_ deep object properties, please see [dlv](https://github.com/developit/dlv).

**banco/.netlify/plugins/node_modules/dunder-proto/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — If available, the Object.prototype.__proto__ accessor and mutator, call-bound.

**banco/.netlify/plugins/node_modules/duplexify/**

- [[README]] — Turn a writeable and readable stream into a single streams2 duplex stream.

**banco/.netlify/plugins/node_modules/duplexify/node_modules/readable-stream/**

- [[CONTRIBUTING]] — By making a contribution to this project, I certify that:
- [[GOVERNANCE]] — The Node.js Streams is jointly governed by a Working Group (WG) that is responsible for high-level guidance of the project.
- [[README]] — *Node.js core streams for userland* [![Build Status](https://travis-ci.com/nodejs/readable-stream.svg?branch=master)](https://travis-ci.com/...

**banco/.netlify/plugins/node_modules/eastasianwidth/**

- [[README]] — Get [East Asian Width](http://www.unicode.org/reports/tr11/) from a character.

**banco/.netlify/plugins/node_modules/ecdsa-sig-formatter/**

- [[README]] — Translate between JOSE and ASN.1/DER encodings for ECDSA signatures

**banco/.netlify/plugins/node_modules/ee-first/**

- [[README]] — Get the first event in a set of event emitters and event pairs, then clean up after itself.

**banco/.netlify/plugins/node_modules/electron-to-chromium/**

- [[README]] — This repository provides a mapping of Electron versions to the Chromium version that it uses.

**banco/.netlify/plugins/node_modules/emoji-regex/**

- [[README]] — _emoji-regex_ offers a regular expression to match all emoji symbols and sequences (including textual representations of emoji) as per the U...

**banco/.netlify/plugins/node_modules/emoji-regex-xs/**

- [[README]] — This is a drop-in replacement for the [emoji-regex](https://github.com/mathiasbynens/emoji-regex) package that shares its API and passes all...

**banco/.netlify/plugins/node_modules/enabled/**

- [[README]] — [version]: http://img.shields.io/npm/v/enabled.svg?style=flat-square [build]: http://img.shields.io/travis/3rd-Eden/enabled/master.svg?style...

**banco/.netlify/plugins/node_modules/encodeurl/**

- [[README]] — Encode a URL to a percent-encoded form, excluding already-encoded sequences.

**banco/.netlify/plugins/node_modules/end-of-stream/**

- [[README]] — A node module that calls a callback when a readable/writable/duplex stream has completed or failed.

**banco/.netlify/plugins/node_modules/engine.io/**

- [[README]] — <h1>Engine.IO</h1>

**banco/.netlify/plugins/node_modules/engine.io-parser/**

- [[Readme]] — This is the JavaScript parser for the engine.io protocol encoding, shared by both [engine.io-client](https://github.com/socketio/engine.io-c...

**banco/.netlify/plugins/node_modules/engine.io/node_modules/@types/node/**

- [[README]] — This package contains type definitions for node (https://nodejs.org/).

**banco/.netlify/plugins/node_modules/engine.io/node_modules/ws/**

- [[README]] — ws is a simple to use, blazing fast, and thoroughly tested WebSocket client and server implementation.

**banco/.netlify/plugins/node_modules/enhanced-resolve/**

- [[README]] — Offers an async require.resolve function.

**banco/.netlify/plugins/node_modules/ent/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Encode and decode HTML entities

**banco/.netlify/plugins/node_modules/entities/**

- [[readme]] — Encode & decode HTML & XML entities with ease & speed.

**banco/.netlify/plugins/node_modules/env-paths/**

- [[readme]] — Uses the correct OS-specific paths. Most developers get this wrong.

**banco/.netlify/plugins/node_modules/eol/**

- [[README]] — [Newline](http://en.wikipedia.org/wiki/Newline) character converter for JavaScript.

**banco/.netlify/plugins/node_modules/error-ex/**

- [[README]] — To include in your project: javascript var errorEx = require('error-ex');

**banco/.netlify/plugins/node_modules/es-abstract/**

- [[CHANGELOG]] — 1.24.2 / 2026-04-07 ================= - [Fix] IfAbruptCloseIterator: handle all abrupt completions, not just throw - [Robustness] use +x ins...
- [[README]] — ECMAScript spec abstract operations.

**banco/.netlify/plugins/node_modules/es-abstract-get/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — The ECMAScript “getting properties” abstract operations — [Get][Get], [GetV][GetV], and [GetMethod][GetMethod] — plus the [isPropertyKey][is...

**banco/.netlify/plugins/node_modules/es-define-property/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — const assert = require('assert');

**banco/.netlify/plugins/node_modules/es-errors/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — A simple cache for a few of the JS Error constructors.

**banco/.netlify/plugins/node_modules/es-module-lexer/**

- [[README]] — A JS module syntax lexer used in [es-module-shims](https://github.com/guybedford/es-module-shims).

**banco/.netlify/plugins/node_modules/es-object-atoms/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — ES Object-related atoms: Object, ToObject, RequireObjectCoercible.

**banco/.netlify/plugins/node_modules/es-set-tostringtag/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — A helper to optimistically set Symbol.toStringTag, when possible.

**banco/.netlify/plugins/node_modules/es-shim-unscopables/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Helper package to shim a method into Array.prototype[Symbol.unscopables]

**banco/.netlify/plugins/node_modules/es-to-primitive/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — ECMAScript “ToPrimitive” algorithm. Provides ES5 and ES2015 versions.

**banco/.netlify/plugins/node_modules/es5-ext/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Shims for upcoming ES6 standard and other goodies implemented strictly with ECMAScript conventions in mind.

**banco/.netlify/plugins/node_modules/es6-iterator/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — $ npm install es6-iterator

**banco/.netlify/plugins/node_modules/es6-symbol/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — For more information about symbols see following links

**banco/.netlify/plugins/node_modules/es6-weak-map/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — _Roughly inspired by Mark Miller's and Kris Kowal's [WeakMap implementation](https://github.com/drses/weak-map)_.

**banco/.netlify/plugins/node_modules/esbuild/**

- [[LICENSE]] — MIT License
- [[README]] — This is a JavaScript bundler and minifier.

**banco/.netlify/plugins/node_modules/esbuild-plugin-copy/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — ESBuild plugin for assets copy.

**banco/.netlify/plugins/node_modules/esbuild-plugin-copy/node_modules/ansi-styles/**

- [[readme]] — You probably want the higher-level [chalk](https://github.com/chalk/chalk) module for styling your strings.

**banco/.netlify/plugins/node_modules/esbuild-plugin-copy/node_modules/chalk/**

- [[readme]] — <h1 align="center"> <br> <br> <img width="320" src="media/logo.svg" alt="Chalk"> <br> <br> <br> </h1>

**banco/.netlify/plugins/node_modules/esbuild-plugin-copy/node_modules/chokidar/**

- [[README]] — Node.js fs.watch:

**banco/.netlify/plugins/node_modules/esbuild-plugin-copy/node_modules/fs-extra/**

- [[README]] — Node.js: fs-extra =================

**banco/.netlify/plugins/node_modules/esbuild-plugin-copy/node_modules/picomatch/**

- [[README]] — picomatch x 1,993,050 ops/sec ±0.51% (91 runs sampled) minimatch x 627,206 ops/sec ±1.96% (87 runs sampled))

**banco/.netlify/plugins/node_modules/esbuild-plugin-copy/node_modules/readdirp/**

- [[README]] — Recursive version of [fs.readdir](https://nodejs.org/api/fs.html#fs_fs_readdir_path_options_callback).

**banco/.netlify/plugins/node_modules/escalade/**

- [[readme]] — With [escalade](https://en.wikipedia.org/wiki/Escalade), you can scale parent directories until you've found what you're looking for.<br>Giv...

**banco/.netlify/plugins/node_modules/escape-html/**

- [[Readme]] — Escape string for use in HTML

**banco/.netlify/plugins/node_modules/escape-string-regexp/**

- [[readme]] — $ npm install escape-string-regexp

**banco/.netlify/plugins/node_modules/escodegen/**

- [[README]] — Escodegen ([escodegen](http://github.com/estools/escodegen)) is an [ECMAScript](http://www.ecma-international.org/publications/standards/Ecm...

**banco/.netlify/plugins/node_modules/eslint-visitor-keys/**

- [[README]] — Constants and utilities about visitor keys to traverse AST.

**banco/.netlify/plugins/node_modules/esm/**

- [[README]] — The brilliantly simple, babel-less, bundle-less ECMAScript module loader.

**banco/.netlify/plugins/node_modules/esniff/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Low footprint, fast source code parser, which allows you to find all code fragment occurrences with respect to all syntax rules that cannot...

**banco/.netlify/plugins/node_modules/esprima/**

- [[README]] — Esprima ([esprima.org](http://esprima.org), BSD license) is a high performance, standard-compliant [ECMAScript](http://www.ecma-internationa...

**banco/.netlify/plugins/node_modules/estraverse/**

- [[README]] — Estraverse ([estraverse](http://github.com/estools/estraverse)) is [ECMAScript](http://www.ecma-international.org/publications/standards/Ecm...

**banco/.netlify/plugins/node_modules/estree-util-is-identifier-name/**

- [[readme]] — [estree][] utility to check if something can be an identifier.

**banco/.netlify/plugins/node_modules/estree-walker/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — Simple utility for walking an [ESTree](https://github.com/estree/estree)-compliant AST, such as one generated by [acorn](https://github.com/...

**banco/.netlify/plugins/node_modules/esutils/**

- [[README]] — esutils ([esutils](http://github.com/estools/esutils)) is utility box for ECMAScript language tools.

**banco/.netlify/plugins/node_modules/etag/**

- [[HISTORY]] — 1.8.1 / 2017-09-12 ==================
- [[README]] — Create simple HTTP ETags

**banco/.netlify/plugins/node_modules/event-emitter/**

- [[README]] — $ npm install event-emitter

**banco/.netlify/plugins/node_modules/event-iterator/**

- [[CHANGELOG]] — The second RemoveHandler argument has been removed.
- [[README]] — emitters, event targets, and similar objects into EcmaScript async iterators.

**banco/.netlify/plugins/node_modules/event-source-polyfill/**

- [[LICENSE]] — MIT License
- [[README]] — EventSource polyfill - https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events ===================================...

**banco/.netlify/plugins/node_modules/event-target-shim/**

- [[README]] — An implementation of [WHATWG EventTarget interface](https://dom.spec.whatwg.org/#interface-eventtarget), plus few extensions.

**banco/.netlify/plugins/node_modules/eventemitter3/**

- [[README]] — EventEmitter3 is a high performance EventEmitter.

**banco/.netlify/plugins/node_modules/events/**

- [[History]] — Now you can use the events.once function with objects that implement the EventTarget interface.
- [[Readme]] — This implements the Node.js [events][node.js docs] module for environments that do not have it, like browsers.
- [[security]] — Only the latest major version is supported at any given time.

**banco/.netlify/plugins/node_modules/events-universal/**

- [[README]] — Universal wrapper for the Node.js events module.

**banco/.netlify/plugins/node_modules/eventsource/**

- [[CONTRIBUTING]] — If you add or fix something, add tests.
- [[HISTORY]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — This library is a pure JavaScript implementation of the [EventSource](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-...

**banco/.netlify/plugins/node_modules/eventsource-parser/**

- [[README]] — A streaming parser for [server-sent events/eventsource](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events), without any as...

**banco/.netlify/plugins/node_modules/execa/**

- [[readme]] — <picture> <source media="(prefers-color-scheme: dark)" srcset="media/logo_dark.svg"> <img alt="execa logo" src="media/logo.svg" width="400">...

**banco/.netlify/plugins/node_modules/execa/node_modules/signal-exit/**

- [[README]] — When you want to fire an event no matter how a process exits:

**banco/.netlify/plugins/node_modules/expand-template/**

- [[README]] — $ npm i expand-template -S

**banco/.netlify/plugins/node_modules/express/**

- [[History]] — 4.22.3 ======
- [[Readme]] — Fast, unopinionated, minimalist web framework for [Node.js](http://nodejs.org).

**banco/.netlify/plugins/node_modules/express/node_modules/debug/**

- [[CHANGELOG]] — 2.6.9 / 2017-09-22 ==================
- [[README]] — A tiny node.js debugging utility modelled after node core's debugging technique.

**banco/.netlify/plugins/node_modules/express/node_modules/ms/**

- [[license]] — The MIT License (MIT)
- [[readme]] — Use this package to easily convert various time formats to milliseconds.

**banco/.netlify/plugins/node_modules/ext/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — _(Previously known as es5-ext)_

**banco/.netlify/plugins/node_modules/ext/docs/**

- [[global-this]] — Returns global object. Resolve native [globalThis](https://github.com/tc39/proposal-global) if implemented, otherwise fallback to internal r...

**banco/.netlify/plugins/node_modules/ext/docs/function/**

- [[identity]] — Returns input argument.

**banco/.netlify/plugins/node_modules/ext/docs/math/**

- [[ceil-10]] — Decimal ceil
- [[floor-10]] — Decimal floor
- [[round-10]] — Decimal round

**banco/.netlify/plugins/node_modules/ext/docs/object/**

- [[clear]] — Deletes all own, enumerable, non-symbol properties in the object
- [[entries]] — [Object.entries](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries) implementation.

**banco/.netlify/plugins/node_modules/ext/docs/promise/**

- [[limit]] — Helps to limit concurrency of asynchronous operations.

**banco/.netlify/plugins/node_modules/ext/docs/string/**

- [[random]] — Returns generated random string, contained only of ascii cars a-z and 0-1.

**banco/.netlify/plugins/node_modules/ext/docs/string_/**

- [[camel-to-hyphen]] — Convert camelCase string to hyphen separated, e.g.
- [[capitalize]] — Capitalize input string, e.g. convert this is a test into This is a test.
- [[includes]] — const includes = require("ext/string_/includes");

**banco/.netlify/plugins/node_modules/ext/docs/thenable_/**

- [[finally]] — const finally = require("ext/thenable_/finally");

**banco/.netlify/plugins/node_modules/extend/**

- [[CHANGELOG]] — 3.0.2 / 2018-07-19 ================== * [Fix] Prevent merging __proto__ property (#48) * [Dev Deps] update eslint, @ljharb/eslint-config, ta...
- [[README]] — Notes:

**banco/.netlify/plugins/node_modules/external-editor/**

- [[README]] — A node module to edit a string with a users preferred text editor using $VISUAL or $ENVIRONMENT.

**banco/.netlify/plugins/node_modules/extract-zip/**

- [[readme]] — Unzip written in pure JavaScript. Extracts a zip into a directory.

**banco/.netlify/plugins/node_modules/extract-zip/node_modules/get-stream/**

- [[readme]] — $ npm install get-stream

**banco/.netlify/plugins/node_modules/fast-copy/**

- [[CHANGELOG]] — Backport of the fix released in [4.1.0](https://github.com/planttheidea/fast-copy/releases/tag/v4.1.0) for consumers remaining on 2.x.
- [[README]] — <img src="https://img.shields.io/badge/build-passing-brightgreen.svg"/> <img src="https://img.shields.io/badge/coverage-100%25-brightgreen.s...

**banco/.netlify/plugins/node_modules/fast-fifo/**

- [[README]] — A fast fifo implementation similar to the one powering nextTick in Node.js core

**banco/.netlify/plugins/node_modules/fast-glob/**

- [[README]] — This package provides methods for traversing the file system and returning pathnames that matched a defined set of a specified pattern accor...

**banco/.netlify/plugins/node_modules/fast-text-encoding/**

- [[README]] — Install as "fast-text-encoding" via your favourite package manager.

**banco/.netlify/plugins/node_modules/fastest-levenshtein/**

- [[LICENSE]] — MIT License
- [[README]] — $ npm i fastest-levenshtein

**banco/.netlify/plugins/node_modules/fastq/**

- [[README]] — Fast, in memory work queue.
- [[SECURITY]] — Use this section to tell people about which versions of your project are currently being supported with security updates.

**banco/.netlify/plugins/node_modules/fd-slicer/**

- [[CHANGELOG]] — if a maximum size is exceeded * improve documentation
- [[README]] — Safe fs.ReadStream and fs.WriteStream using the same fd.

**banco/.netlify/plugins/node_modules/fdir/**

- [[README]] — <p align="center"> <img src="https://github.com/thecodrr/fdir/raw/master/assets/fdir.gif" width="75%"/>

**banco/.netlify/plugins/node_modules/fecha/**

- [[README]] — Lightweight date formatting and parsing (~2KB).

**banco/.netlify/plugins/node_modules/fetch-blob/**

- [[README]] — A Blob implementation in Node.js, originally from [node-fetch](https://github.com/node-fetch/node-fetch).

**banco/.netlify/plugins/node_modules/figures/**

- [[readme]] — [*and more...*](index.js)

**banco/.netlify/plugins/node_modules/file-type/**

- [[readme]] — The file type is detected by checking the [magic number](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files) of...

**banco/.netlify/plugins/node_modules/file-uri-to-path/**

- [[History]] — 1.0.0 / 2017-07-06 ==================
- [[README]] — file-uri-to-path ================ ### Convert a file: URI to a file path [![Build Status](https://travis-ci.org/TooTallNate/file-uri-to-path...

**banco/.netlify/plugins/node_modules/fill-range/**

- [[README]] — Please consider following this project's author, [Jon Schlinkert](https://github.com/jonschlinkert), and consider starring the project to sh...

**banco/.netlify/plugins/node_modules/filter-obj/**

- [[readme]] — npm install filter-obj

**banco/.netlify/plugins/node_modules/finalhandler/**

- [[HISTORY]] — v1.3.2 / 2025-12-01 ==================
- [[README]] — Node.js function to invoke as the final step to respond to HTTP request.
- [[SECURITY]] — The finalhandler team and community take all security bugs seriously.

**banco/.netlify/plugins/node_modules/finalhandler/node_modules/debug/**

- [[CHANGELOG]] — 2.6.9 / 2017-09-22 ==================
- [[README]] — A tiny node.js debugging utility modelled after node core's debugging technique.

**banco/.netlify/plugins/node_modules/finalhandler/node_modules/ms/**

- [[license]] — The MIT License (MIT)
- [[readme]] — Use this package to easily convert various time formats to milliseconds.

**banco/.netlify/plugins/node_modules/find-root/**

- [[LICENSE]] — Copyright © 2017 jsdnxx
- [[README]] — recursively find the closest package.json

**banco/.netlify/plugins/node_modules/find-up/**

- [[readme]] — npm install find-up

**banco/.netlify/plugins/node_modules/find-up-simple/**

- [[readme]] — This is a simpler version of my [find-up](https://github.com/sindresorhus/find-up) package, now with zero dependencies.

**banco/.netlify/plugins/node_modules/flatted/**

- [[README]] — <sup>Social Media Photo by [Matt Seymour](https://unsplash.com/@mattseymour) on [Unsplash](https://unsplash.com/)</sup>

**banco/.netlify/plugins/node_modules/flatted/golang/**

- [[README]] — A super light and fast circular JSON parser.

**banco/.netlify/plugins/node_modules/fn.name/**

- [[README]] — [version]: http://img.shields.io/npm/v/fn.name.svg?style=flat-square [build]: http://img.shields.io/travis/3rd-Eden/fn.name/master.svg?style...

**banco/.netlify/plugins/node_modules/follow-redirects/**

- [[README]] — Drop-in replacement for Node's http and https modules that automatically follows redirects.

**banco/.netlify/plugins/node_modules/for-each/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — A better forEach.

**banco/.netlify/plugins/node_modules/for-each/.github/**

- [[SECURITY]] — Please email [@ljharb](https://github.com/ljharb) or see https://tidelift.com/security if you have a potential security vulnerability to rep...

**banco/.netlify/plugins/node_modules/foreground-child/**

- [[README]] — Run a child as if it's the foreground process.

**banco/.netlify/plugins/node_modules/foreground-child/node_modules/signal-exit/**

- [[README]] — When you want to fire an event no matter how a process exits:

**banco/.netlify/plugins/node_modules/form-data/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — A library to create readable "multipart/form-data" streams.

**banco/.netlify/plugins/node_modules/form-urlencoded/**

- [[README]] — form-urlencoded =============== (c)[Bumblehead][0],[JBlashill][6] 2012-2017

**banco/.netlify/plugins/node_modules/formdata-polyfill/**

- [[README]] — npm install formdata-polyfill

**banco/.netlify/plugins/node_modules/forwarded/**

- [[HISTORY]] — 0.2.0 / 2021-05-31 ==================
- [[README]] — Parse HTTP X-Forwarded-For header

**banco/.netlify/plugins/node_modules/fraction.js/**

- [[CHANGELOG]] — v5.2.2 - Improved documentation and removed unecessary check
- [[README]] — Do you find the limitations of floating-point arithmetic frustrating, especially when rational and irrational numbers like π or √2 are store...

**banco/.netlify/plugins/node_modules/fresh/**

- [[HISTORY]] — 0.5.2 / 2017-09-13 ==================
- [[README]] — HTTP response freshness testing

**banco/.netlify/plugins/node_modules/from2/**

- [[LICENSE]] — Copyright (c) 2014 Hugh Kennedy
- [[README]] — Convience wrapper for [readable-stream](http://github.com/isaacs/readable-stream)'s ReadableStream base class, with an API lifted from [from...

**banco/.netlify/plugins/node_modules/from2/node_modules/isarray/**

- [[README]] — ](https://ci.testling.com/juliangruber/isarray)

**banco/.netlify/plugins/node_modules/from2/node_modules/readable-stream/**

- [[CONTRIBUTING]] — By making a contribution to this project, I certify that:
- [[GOVERNANCE]] — The Node.js Streams is jointly governed by a Working Group (WG) that is responsible for high-level guidance of the project.
- [[README]] — *Node-core v8.17.0 streams for userland* [![Build Status](https://travis-ci.org/nodejs/readable-stream.svg?branch=master)](https://travis-ci...

**banco/.netlify/plugins/node_modules/from2/node_modules/readable-stream/doc/wg-meetings/**

- [[2015-01-30]] — Extracted from https://github.com/iojs/readable-stream/labels/wg-agenda prior to meeting.

**banco/.netlify/plugins/node_modules/from2/node_modules/safe-buffer/**

- [[README]] — [travis-image]: https://img.shields.io/travis/feross/safe-buffer/master.svg [travis-url]: https://travis-ci.org/feross/safe-buffer [npm-imag...

**banco/.netlify/plugins/node_modules/from2/node_modules/string_decoder/**

- [[README]] — *Node-core v8.9.4 string_decoder for userland*

**banco/.netlify/plugins/node_modules/fs-constants/**

- [[README]] — Small module that allows you to get the fs constants across Node and the browser.

**banco/.netlify/plugins/node_modules/fs-exists-cached/**

- [[README]] — Just like fs.exists and fs.existsSync, but cached

**banco/.netlify/plugins/node_modules/fs-extra/**

- [[README]] — Node.js: fs-extra =================

**banco/.netlify/plugins/node_modules/fs.realpath/**

- [[README]] — A backwards-compatible fs.realpath for Node v6 and above

**banco/.netlify/plugins/node_modules/fsevents/**

- [[README]] — Native access to MacOS FSEvents in [Node.js](https://nodejs.org/)

**banco/.netlify/plugins/node_modules/function-bind/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — <!--[![coverage][codecov-image]][codecov-url]--> [![dependency status][deps-svg]][deps-url] [![dev dependency status][dev-deps-svg]][dev-dep...

**banco/.netlify/plugins/node_modules/function-bind/.github/**

- [[SECURITY]] — Please email [@ljharb](https://github.com/ljharb) or see https://tidelift.com/security if you have a potential security vulnerability to rep...

**banco/.netlify/plugins/node_modules/function.prototype.name/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — An ES2015 spec-compliant Function.prototype.name shim.

**banco/.netlify/plugins/node_modules/functions-have-names/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Does this JS environment support the name property on functions?

**banco/.netlify/plugins/node_modules/gatsby-sharp/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.

**banco/.netlify/plugins/node_modules/gaxios/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — $ npm install gaxios

**banco/.netlify/plugins/node_modules/gaxios/node_modules/agent-base/**

- [[README]] — agent-base ========== ### Turn a function into an [http.Agent][http.Agent] instance [![Build Status](https://github.com/TooTallNate/node-age...

**banco/.netlify/plugins/node_modules/gaxios/node_modules/https-proxy-agent/**

- [[README]] — https-proxy-agent ================ ### An HTTP(s) proxy http.Agent implementation for HTTPS [![Build Status](https://github.com/TooTallNate/...

**banco/.netlify/plugins/node_modules/gaxios/node_modules/is-stream/**

- [[readme]] — $ npm install is-stream

**banco/.netlify/plugins/node_modules/gcp-metadata/**

- [[CHANGELOG]] — [npm history][1]
- [[README]] — Get the metadata from a Google Cloud Platform environment

**banco/.netlify/plugins/node_modules/generator-function/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[LICENSE]] — Copyright (c) 2015 Tiancheng “Timothy” Gu
- [[README]] — A function that returns the normally hidden GeneratorFunction constructor, when available.

**banco/.netlify/plugins/node_modules/gensync/**

- [[README]] — This module allows for developers to write common code that can share implementation details, hiding whether an underlying request happens s...

**banco/.netlify/plugins/node_modules/get-amd-module-type/**

- [[README]] — npm install get-amd-module-type

**banco/.netlify/plugins/node_modules/get-caller-file/**

- [[LICENSE]] — ISC License (ISC) Copyright 2018 Stefan Penner
- [[README]] — This is a utility, which allows a function to figure out from which file it was invoked.

**banco/.netlify/plugins/node_modules/get-intrinsic/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Get and robustly cache all JS language-level intrinsics at first require time.

**banco/.netlify/plugins/node_modules/get-it/**

- [[README]] — Generic HTTP request library for node.js (>= 12) and browsers (IE9 and newer)

**banco/.netlify/plugins/node_modules/get-it/lib-node/middleware/cancel/**

- [[README]] — The cancel token API is based on the [cancelable promises proposal](https://github.com/tc39/proposal-cancelable-promises), which is currentl...

**banco/.netlify/plugins/node_modules/get-it/lib/middleware/cancel/**

- [[README]] — The cancel token API is based on the [cancelable promises proposal](https://github.com/tc39/proposal-cancelable-promises), which is currentl...

**banco/.netlify/plugins/node_modules/get-it/node_modules/debug/**

- [[CHANGELOG]] — 2.6.9 / 2017-09-22 ==================
- [[README]] — A tiny node.js debugging utility modelled after node core's debugging technique.

**banco/.netlify/plugins/node_modules/get-it/node_modules/is-plain-object/**

- [[README]] — Install with [npm](https://www.npmjs.com/):

**banco/.netlify/plugins/node_modules/get-it/node_modules/is-stream/**

- [[readme]] — $ npm install --save is-stream

**banco/.netlify/plugins/node_modules/get-it/node_modules/ms/**

- [[license]] — The MIT License (MIT)
- [[readme]] — Use this package to easily convert various time formats to milliseconds.

**banco/.netlify/plugins/node_modules/get-port/**

- [[readme]] — $ npm install get-port

**banco/.netlify/plugins/node_modules/get-proto/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Robustly get the Prototype of an object.

**banco/.netlify/plugins/node_modules/get-random-values/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — var getRandomValues = require('get-random-values');

**banco/.netlify/plugins/node_modules/get-stream/**

- [[readme]] — npm install get-stream

**banco/.netlify/plugins/node_modules/get-symbol-description/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Gets the description of a Symbol. Handles Symbol() vs Symbol('') properly when possible.

**banco/.netlify/plugins/node_modules/git-up/**

- [[README]] — <a href="https://www.buymeacoffee.com/H96WwChMy" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/yellow_img....

**banco/.netlify/plugins/node_modules/git-url-parse/**

- [[README]] — <a href="https://www.buymeacoffee.com/H96WwChMy" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/yellow_img....

**banco/.netlify/plugins/node_modules/glob/**

- [[README]] — Match files using the patterns the shell uses.

**banco/.netlify/plugins/node_modules/glob-parent/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — Extract the non-magic parent path from a glob string.

**banco/.netlify/plugins/node_modules/global/**

- [[README]] — <!-- [![build status][1]][2]

**banco/.netlify/plugins/node_modules/globalthis/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — An ECMAScript spec-compliant polyfill/shim for globalThis.

**banco/.netlify/plugins/node_modules/globby/**

- [[readme]] — Based on [fast-glob](https://github.com/mrmlnc/fast-glob) but adds a bunch of useful features.

**banco/.netlify/plugins/node_modules/gonzales-pe/**

- [[CHANGELOG]] — :japanese_ogre: — be afraid of this change because it breaks the way things worked before.
- [[README]] — [npm-img]:      https://img.shields.io/npm/v/gonzales-pe.svg [npm]:          https://www.npmjs.com/package/gonzales-pe [travis-img]:   https...

**banco/.netlify/plugins/node_modules/google-auth-library/**

- [[CHANGELOG]] — [npm history][1]
- [[README]] — This is Google's officially supported [node.js](http://nodejs.org/) client library for using OAuth 2.0 authorization and authentication with...

**banco/.netlify/plugins/node_modules/google-auth-library/node_modules/lru-cache/**

- [[README]] — A cache object that deletes the least-recently-used items.

**banco/.netlify/plugins/node_modules/google-auth-library/node_modules/yallist/**

- [[README]] — Yet Another Linked List

**banco/.netlify/plugins/node_modules/google-p12-pem/**

- [[CHANGELOG]] — [npm history][1]
- [[README]] — Convert Google .p12 keys to .pem keys.

**banco/.netlify/plugins/node_modules/gopd/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — var gOPD = require('gopd'); var assert = require('assert');

**banco/.netlify/plugins/node_modules/got/**

- [[readme]] — <div align="center"> <br> <br> <img width="360" src="media/logo.svg" alt="Got"> <br> <br> <br> <p align="center">Huge thanks to <a href="htt...

**banco/.netlify/plugins/node_modules/graceful-fs/**

- [[README]] — graceful-fs functions as a drop-in replacement for the fs module, making various improvements.

**banco/.netlify/plugins/node_modules/graphql/**

- [[README]] — The JavaScript reference implementation for GraphQL, a query language for APIs created by Facebook.

**banco/.netlify/plugins/node_modules/graphql-compose/**

- [[LICENSE]] — The MIT License (MIT)
- [[README]] — graphql-compose – provides a type registry with a bunch of methods for programmatic schema construction.

**banco/.netlify/plugins/node_modules/graphql-http/**

- [[LICENSE]] — MIT License
- [[README]] — <div align="center"> <br />

**banco/.netlify/plugins/node_modules/graphql-scalars/**

- [[README]] — Please refer to [our website](https://www.graphql-scalars.dev) for all the documentation related to GraphQL Scalars

**banco/.netlify/plugins/node_modules/graphql-type-json/**

- [[README]] — JSON scalar types for [GraphQL.js](https://github.com/graphql/graphql-js).

**banco/.netlify/plugins/node_modules/gtoken/**

- [[CHANGELOG]] — [npm history][1]
- [[README]] — This is a low level utility library used to interact with Google Authentication services.

**banco/.netlify/plugins/node_modules/has-bigints/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Determine if the JS environment has BigInt support.

**banco/.netlify/plugins/node_modules/has-flag/**

- [[readme]] — Correctly stops looking after an -- argument terminator.

**banco/.netlify/plugins/node_modules/has-property-descriptors/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Does the environment have full property descriptor support?

**banco/.netlify/plugins/node_modules/has-proto/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Does this environment have the ability to set the Prototype of an object on creation with __proto__?

**banco/.netlify/plugins/node_modules/has-symbols/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Determine if the JS environment has Symbol support.

**banco/.netlify/plugins/node_modules/has-tostringtag/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Determine if the JS environment has Symbol.toStringTag support.

**banco/.netlify/plugins/node_modules/hash-stream-validation/**

- [[readme]] — $ npm install --save hash-stream-validation  js var hashStreamValidation = require('hash-stream-validation');

**banco/.netlify/plugins/node_modules/hash-wasm/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — Hash-WASM is a ⚡lightning fast⚡ hash function library for browsers and Node.js.

**banco/.netlify/plugins/node_modules/hasha/**

- [[readme]] — <h1 align="center"> <br> <br> <br> <img width="380" src="media/logo.svg" alt="hasha"> <br> <br> <br> <br> <br> </h1>

**banco/.netlify/plugins/node_modules/hasha/node_modules/is-stream/**

- [[readme]] — $ npm install is-stream

**banco/.netlify/plugins/node_modules/hasha/node_modules/type-fest/**

- [[readme]] — <div align="center"> <br> <br> <img src="media/logo.svg" alt="type-fest" height="300"> <br> <br> <b>A collection of essential TypeScript typ...

**banco/.netlify/plugins/node_modules/hasown/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — A robust, ES3 compatible, "has own property" predicate.

**banco/.netlify/plugins/node_modules/hast-util-to-html/**

- [[readme]] — [hast][github-hast] utility to serialize hast as HTML.

**banco/.netlify/plugins/node_modules/hast-util-to-jsx-runtime/**

- [[readme]] — hast utility to transform a tree to preact, react, solid, svelte, vue, etcetera, with an automatic JSX runtime.

**banco/.netlify/plugins/node_modules/hast-util-whitespace/**

- [[readme]] — [hast][] utility to check if a node is [*inter-element whitespace*][spec].

**banco/.netlify/plugins/node_modules/he/**

- [[README]] — _he_ (for “HTML entities”) is a robust HTML entity encoder/decoder written in JavaScript.

**banco/.netlify/plugins/node_modules/history/**

- [[README]] — [npm-badge]: https://img.shields.io/npm/v/history.svg?style=flat-square [npm]: https://www.npmjs.org/package/history

**banco/.netlify/plugins/node_modules/hoist-non-react-statics/**

- [[CHANGELOG]] — [#55]: https://github.com/mridgway/hoist-non-react-statics/pull/55 [#61]: https://github.com/mridgway/hoist-non-react-statics/pull/61 [#62]:...
- [[LICENSE]] — Software License Agreement (BSD License) ========================================
- [[README]] — Copies non-react specific statics from a child component to a parent component.

**banco/.netlify/plugins/node_modules/hoist-non-react-statics/node_modules/react-is/**

- [[README]] — This package allows you to test arbitrary values and see if they're a particular React element type.

**banco/.netlify/plugins/node_modules/hosted-git-info/**

- [[README]] — This will let you identify and transform various git hosts URLs between protocols.

**banco/.netlify/plugins/node_modules/hosted-git-info/node_modules/lru-cache/**

- [[README]] — A cache object that deletes the least-recently-used items.

**banco/.netlify/plugins/node_modules/html-encoding-sniffer/**

- [[README]] — This package implements the HTML Standard's [encoding sniffing algorithm](https://html.spec.whatwg.org/multipage/syntax.html#encoding-sniffi...

**banco/.netlify/plugins/node_modules/html-void-elements/**

- [[readme]] — List of HTML void tag names.

**banco/.netlify/plugins/node_modules/htmlparser/**

- [[README]] — A forgiving HTML/XML/RSS parser written in JS for both the browser and NodeJS (yes, despite the name it works just fine in any modern browse...

**banco/.netlify/plugins/node_modules/htmlparser2/**

- [[README]] — The fast & forgiving HTML/XML parser.

**banco/.netlify/plugins/node_modules/http-cache-semantics/**

- [[README]] — This library tells when responses can be reused from a cache, taking into account [HTTP RFC 7234/9111](http://httpwg.org/specs/rfc9111.html)...

**banco/.netlify/plugins/node_modules/http-errors/**

- [[HISTORY]] — 2.0.1 / 2025-11-20 ==================
- [[README]] — Create HTTP errors for Express, Koa, Connect, etc.

**banco/.netlify/plugins/node_modules/http-proxy/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[CODE_OF_CONDUCT]] — In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our pro...
- [[README]] — websockets. It is suitable for implementing components such as reverse proxies and load balancers.

**banco/.netlify/plugins/node_modules/http-proxy-agent/**

- [[README]] — http-proxy-agent ================ ### An HTTP(s) proxy http.Agent implementation for HTTP [![Build Status](https://github.com/TooTallNate/no...

**banco/.netlify/plugins/node_modules/http-proxy-agent/node_modules/agent-base/**

- [[README]] — agent-base ========== ### Turn a function into an [http.Agent][http.Agent] instance [![Build Status](https://github.com/TooTallNate/node-age...

**banco/.netlify/plugins/node_modules/http-proxy-middleware/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — Node.js proxying made simple. Configure proxy middleware with ease for [connect](https://github.com/senchalabs/connect), [express](https://g...

**banco/.netlify/plugins/node_modules/http2-wrapper/**

- [[README]] — This package was created to support HTTP/2 without the need to rewrite your code.<br> I recommend adapting to the [http2](https://nodejs.org...

**banco/.netlify/plugins/node_modules/https-proxy-agent/**

- [[README]] — https-proxy-agent ================ ### An HTTP(s) proxy http.Agent implementation for HTTPS

**banco/.netlify/plugins/node_modules/human-signals/**

- [[README]] — import { signalsByName, signalsByNumber } from 'human-signals'

**banco/.netlify/plugins/node_modules/humanize-list/**

- [[readme]] — Comma delimit an array for human readability, the Oxford comma is optional.

**banco/.netlify/plugins/node_modules/iconv-lite/**

- [[Changelog]] — just spaces. This should minimize the importance of "default" endianness.
- [[README]] — [Grunt](http://gruntjs.com/), [Nodemailer](http://www.nodemailer.com/), [Yeoman](http://yeoman.io/) and others.

**banco/.netlify/plugins/node_modules/ieee754/**

- [[README]] — [travis-image]: https://img.shields.io/travis/feross/ieee754/master.svg [travis-url]: https://travis-ci.org/feross/ieee754 [npm-image]: http...

**banco/.netlify/plugins/node_modules/ignore/**

- [[README]] — Pay ATTENTION that [minimatch](https://www.npmjs.org/package/minimatch) (which used by fstream-ignore) does not follow the gitignore spec.

**banco/.netlify/plugins/node_modules/import-fresh/**

- [[readme]] — Useful for testing purposes when you need to freshly import a module.

**banco/.netlify/plugins/node_modules/import-fresh/node_modules/resolve-from/**

- [[readme]] — $ npm install resolve-from

**banco/.netlify/plugins/node_modules/import-from/**

- [[readme]] — $ npm install import-from

**banco/.netlify/plugins/node_modules/imurmurhash/**

- [[README]] — iMurmurHash.js ==============

**banco/.netlify/plugins/node_modules/index-to-position/**

- [[readme]] — npm install index-to-position

**banco/.netlify/plugins/node_modules/inflight/**

- [[README]] — Add callbacks to requests in flight to avoid async duplication

**banco/.netlify/plugins/node_modules/inherits/**

- [[README]] — Browser-friendly inheritance fully compatible with standard node.js [inherits](http://nodejs.org/api/util.html#util_util_inherits_constructo...

**banco/.netlify/plugins/node_modules/ini/**

- [[README]] — An ini format parser and serializer for node.

**banco/.netlify/plugins/node_modules/inline-style-parser/**

- [[README]] — Inline style parser copied from [css/lib/parse/index.js](https://github.com/reworkcss/css/blob/v2.2.4/lib/parse/index.js):

**banco/.netlify/plugins/node_modules/inquirer/**

- [[README]] — A collection of common interactive command line user interfaces.

**banco/.netlify/plugins/node_modules/inquirer/node_modules/ansi-styles/**

- [[readme]] — You probably want the higher-level [chalk](https://github.com/chalk/chalk) module for styling your strings.

**banco/.netlify/plugins/node_modules/inquirer/node_modules/chalk/**

- [[readme]] — <h1 align="center"> <br> <br> <img width="320" src="media/logo.svg" alt="Chalk"> <br> <br> <br> </h1>

**banco/.netlify/plugins/node_modules/inquirer/node_modules/emoji-regex/**

- [[README]] — _emoji-regex_ offers a regular expression to match all emoji symbols (including textual representations of emoji) as per the Unicode Standar...

**banco/.netlify/plugins/node_modules/inquirer/node_modules/escape-string-regexp/**

- [[readme]] — $ npm install --save escape-string-regexp

**banco/.netlify/plugins/node_modules/inquirer/node_modules/figures/**

- [[readme]] — [*and more...*](index.js)

**banco/.netlify/plugins/node_modules/inquirer/node_modules/string-width/**

- [[readme]] — Some Unicode characters are [fullwidth](https://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms) and use double the normal width.

**banco/.netlify/plugins/node_modules/internal-slot/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Truly private storage, akin to the JS spec’s concept of internal slots.

**banco/.netlify/plugins/node_modules/into-stream/**

- [[readme]] — Correctly chunks up the input and handles backpressure.

**banco/.netlify/plugins/node_modules/invariant/**

- [[CHANGELOG]] — 2.2.4 / 2018-03-13 ==================
- [[README]] — A mirror of Facebook's invariant (e.g. [React](https://github.com/facebook/react/blob/v0.13.3/src/vendor/core/invariant.js), [flux](https://...

**banco/.netlify/plugins/node_modules/ipaddr.js/**

- [[README]] — ipaddr.js is a small (1.9K minified and gzipped) library for manipulating IP addresses in JavaScript environments.

**banco/.netlify/plugins/node_modules/is-absolute-url/**

- [[readme]] — $ npm install is-absolute-url

**banco/.netlify/plugins/node_modules/is-alphabetical/**

- [[readme]] — Check if a character is alphabetical.

**banco/.netlify/plugins/node_modules/is-alphanumerical/**

- [[readme]] — Check if a character is alphanumerical.

**banco/.netlify/plugins/node_modules/is-array-buffer/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value a JS ArrayBuffer? This module works cross-realm/iframe, does not depend on instanceof or mutable properties, and despite ES6 S...

**banco/.netlify/plugins/node_modules/is-arrayish/**

- [[README]] — var isArrayish = require('is-arrayish');

**banco/.netlify/plugins/node_modules/is-async-function/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this a native async function?

**banco/.netlify/plugins/node_modules/is-bigint/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this an ES BigInt value?

**banco/.netlify/plugins/node_modules/is-binary-path/**

- [[readme]] — $ npm install is-binary-path

**banco/.netlify/plugins/node_modules/is-boolean-object/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value a JS Boolean? This module works cross-realm/iframe, and despite ES6 @@toStringTag.

**banco/.netlify/plugins/node_modules/is-builtin-module/**

- [[readme]] — $ npm install is-builtin-module

**banco/.netlify/plugins/node_modules/is-callable/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this JS value callable? Works with Functions and GeneratorFunctions, despite ES6 @@toStringTag.

**banco/.netlify/plugins/node_modules/is-ci/**

- [[CHANGELOG]] — Breaking changes:
- [[README]] — Returns true if the current environment is a Continuous Integration server.

**banco/.netlify/plugins/node_modules/is-core-module/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this specifier a node.js core module?

**banco/.netlify/plugins/node_modules/is-data-view/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value a JS DataView? This module works cross-realm/iframe, does not depend on instanceof or mutable properties, and despite ES6 Symb...

**banco/.netlify/plugins/node_modules/is-date-object/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value a JS Date object? This module works cross-realm/iframe, and despite ES6 @@toStringTag.

**banco/.netlify/plugins/node_modules/is-decimal/**

- [[readme]] — Check if a character is a decimal.

**banco/.netlify/plugins/node_modules/is-docker/**

- [[readme]] — $ npm install is-docker

**banco/.netlify/plugins/node_modules/is-document.all/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value document.all, i.e. an object with the IsHTMLDDA internal slot?

**banco/.netlify/plugins/node_modules/is-extglob/**

- [[README]] — Install with [npm](https://www.npmjs.com/):

**banco/.netlify/plugins/node_modules/is-finalizationregistry/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value a JS FinalizationRegistry?

**banco/.netlify/plugins/node_modules/is-fullwidth-code-point/**

- [[readme]] — $ npm install is-fullwidth-code-point

**banco/.netlify/plugins/node_modules/is-generator-function/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this a native generator function?

**banco/.netlify/plugins/node_modules/is-glob/**

- [[README]] — Please consider following this project's author, [Jon Schlinkert](https://github.com/jonschlinkert), and consider starring the project to sh...

**banco/.netlify/plugins/node_modules/is-hexadecimal/**

- [[readme]] — Check if a character is hexadecimal.

**banco/.netlify/plugins/node_modules/is-inside-container/**

- [[readme]] — npm install is-inside-container

**banco/.netlify/plugins/node_modules/is-map/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value a JS Map? This module works cross-realm/iframe, and despite ES6 @@toStringTag.

**banco/.netlify/plugins/node_modules/is-negative-zero/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value negative zero? === will lie to you.

**banco/.netlify/plugins/node_modules/is-number/**

- [[README]] — Please consider following this project's author, [Jon Schlinkert](https://github.com/jonschlinkert), and consider starring the project to sh...

**banco/.netlify/plugins/node_modules/is-number-object/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value a JS Number object? This module works cross-realm/iframe, and despite ES6 @@toStringTag.

**banco/.netlify/plugins/node_modules/is-obj/**

- [[readme]] — Keep in mind that array, function, regexp, etc, are objects in JavaScript.<br> See [is-plain-obj](https://github.com/sindresorhus/is-plain-o...

**banco/.netlify/plugins/node_modules/is-path-inside/**

- [[readme]] — $ npm install is-path-inside

**banco/.netlify/plugins/node_modules/is-plain-obj/**

- [[readme]] — An object is plain if it's created by either {}, new Object(), or Object.create(null).

**banco/.netlify/plugins/node_modules/is-plain-object/**

- [[README]] — Please consider following this project's author, [Jon Schlinkert](https://github.com/jonschlinkert), and starring the project to show your ❤...

**banco/.netlify/plugins/node_modules/is-potential-custom-element-name/**

- [[README]] — _is-potential-custom-element-name_ checks whether a given string matches [the PotentialCustomElementName production](https://html.spec.whatw...

**banco/.netlify/plugins/node_modules/is-promise/**

- [[readme]] — Test whether an object looks like a promises-a+ promise

**banco/.netlify/plugins/node_modules/is-regex/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value a JS regex? This module works cross-realm/iframe, and despite ES6 @@toStringTag.

**banco/.netlify/plugins/node_modules/is-relative/**

- [[README]] — Install with [npm](https://www.npmjs.com/):

**banco/.netlify/plugins/node_modules/is-relative-url/**

- [[readme]] — $ npm install is-relative-url

**banco/.netlify/plugins/node_modules/is-retry-allowed/**

- [[readme]] — Is retry allowed for Error?

**banco/.netlify/plugins/node_modules/is-set/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value a JS Set? This module works cross-realm/iframe, and despite ES6 @@toStringTag.

**banco/.netlify/plugins/node_modules/is-shared-array-buffer/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value a JS SharedArrayBuffer? This module works cross-realm/iframe, does not depend on instanceof or mutable properties, and despite...

**banco/.netlify/plugins/node_modules/is-ssh/**

- [[README]] — <a href="https://www.buymeacoffee.com/H96WwChMy" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/yellow_img....

**banco/.netlify/plugins/node_modules/is-stream/**

- [[readme]] — npm install is-stream

**banco/.netlify/plugins/node_modules/is-string/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value a JS String object or primitive?

**banco/.netlify/plugins/node_modules/is-symbol/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this an ES6 Symbol value?

**banco/.netlify/plugins/node_modules/is-typed-array/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value a JS Typed Array? This module works cross-realm/iframe, does not depend on instanceof or mutable properties, and despite ES6 S...

**banco/.netlify/plugins/node_modules/is-typedarray/**

- [[LICENSE]] — This software is released under the MIT license:
- [[README]] — Detect whether or not an object is a [Typed Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays).

**banco/.netlify/plugins/node_modules/is-unc-path/**

- [[README]] — Install with [npm](https://www.npmjs.com/):

**banco/.netlify/plugins/node_modules/is-unicode-supported/**

- [[readme]] — This can be useful to decide whether to use Unicode characters or fallback ASCII characters in command-line output.

**banco/.netlify/plugins/node_modules/is-url-superb/**

- [[readme]] — $ npm install is-url-superb

**banco/.netlify/plugins/node_modules/is-valid-domain/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — [https://lab.miguelmota.com/is-valid-domain](https://lab.miguelmota.com/is-valid-domain)

**banco/.netlify/plugins/node_modules/is-valid-domain/node_modules/punycode/**

- [[README]] — Punycode.js is a robust Punycode converter that fully complies to [RFC 3492](https://tools.ietf.org/html/rfc3492) and [RFC 5891](https://too...

**banco/.netlify/plugins/node_modules/is-weakmap/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value a JS WeakMap? This module works cross-realm/iframe, and despite ES6 @@toStringTag.

**banco/.netlify/plugins/node_modules/is-weakref/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value a JS WeakRef? This module works cross-realm/iframe, and despite ES6 @@toStringTag.

**banco/.netlify/plugins/node_modules/is-weakset/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Is this value a JS WeakSet? This module works cross-realm/iframe, and despite ES6 @@toStringTag.

**banco/.netlify/plugins/node_modules/is-wsl/**

- [[readme]] — Can be useful if you need to work around unimplemented or buggy features in WSL.

**banco/.netlify/plugins/node_modules/is-wsl/node_modules/is-docker/**

- [[readme]] — $ npm install is-docker

**banco/.netlify/plugins/node_modules/isarray/**

- [[README]] — ](https://ci.testling.com/juliangruber/isarray)

**banco/.netlify/plugins/node_modules/isexe/**

- [[README]] — Minimal module to check if a file is executable, and a normal file.

**banco/.netlify/plugins/node_modules/isobject/**

- [[README]] — Install with [npm](https://www.npmjs.com/):

**banco/.netlify/plugins/node_modules/iter-tools-es/**

- [[README]] — import { filter } from 'iter-tools-es'; const { filter } = require('iter-tools-es');

**banco/.netlify/plugins/node_modules/jackspeak/**

- [[LICENSE]] — Version 1.0.0
- [[README]] — A very strict and proper argument parser.

**banco/.netlify/plugins/node_modules/jiti/**

- [[README]] — Runtime Typescript and ESM support for Node.js.

**banco/.netlify/plugins/node_modules/joi/**

- [[LICENSE]] — Copyright (c) 2012-2022, Project contributors.
- [[README]] — TODO — nessuna prosa dopo il titolo.

**banco/.netlify/plugins/node_modules/js-tokens/**

- [[CHANGELOG]] — regex flag. - Changed: _All_ tokens returned by the matchToToken function now have a closed property.
- [[README]] — Overview [![Build Status](https://travis-ci.org/lydell/js-tokens.svg?branch=master)](https://travis-ci.org/lydell/js-tokens) ========

**banco/.netlify/plugins/node_modules/js-xxhash/**

- [[README]] — Pure Javascript / Typescript Implementation of [xxHash](http://cyan4973.github.io/xxHash/)

**banco/.netlify/plugins/node_modules/js-yaml/**

- [[README]] — JS-YAML - YAML 1.2 parser / writer for JavaScript =================================================

**banco/.netlify/plugins/node_modules/jsdom/**

- [[README]] — <h1 align="center"> <img width="100" height="100" src="logo.svg" alt=""><br> jsdom </h1>

**banco/.netlify/plugins/node_modules/jsdom/node_modules/agent-base/**

- [[README]] — agent-base ========== ### Turn a function into an [http.Agent][http.Agent] instance [![Build Status](https://github.com/TooTallNate/node-age...

**banco/.netlify/plugins/node_modules/jsdom/node_modules/entities/**

- [[readme]] — Encode & decode HTML & XML entities with ease & speed.

**banco/.netlify/plugins/node_modules/jsdom/node_modules/https-proxy-agent/**

- [[README]] — https-proxy-agent ================ ### An HTTP(s) proxy http.Agent implementation for HTTPS [![Build Status](https://github.com/TooTallNate/...

**banco/.netlify/plugins/node_modules/jsdom/node_modules/parse5/**

- [[README]] — <p align="center"> <a href="https://github.com/inikulin/parse5"> <img src="https://raw.github.com/inikulin/parse5/master/media/logo.png" alt...

**banco/.netlify/plugins/node_modules/jsesc/**

- [[README]] — Given some data, _jsesc_ returns a stringified representation of that data.

**banco/.netlify/plugins/node_modules/json-bigint/**

- [[README]] — JSON.parse/stringify with bigints support.

**banco/.netlify/plugins/node_modules/json-buffer/**

- [[README]] — JSON functions that can convert buffers!

**banco/.netlify/plugins/node_modules/json-parse-even-better-errors/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[LICENSE]] — Copyright 2017 Kat Marchán Copyright npm, Inc.
- [[README]] — [json-parse-even-better-errors](https://github.com/npm/json-parse-even-better-errors) is a Node.js library for getting nicer errors out of J...

**banco/.netlify/plugins/node_modules/json-stringify-safe/**

- [[CHANGELOG]] — circularity. It previously assumed every visited object was circular which led to [false positives][issue9].
- [[README]] — Like JSON.stringify, but doesn't throw on circular references.

**banco/.netlify/plugins/node_modules/json5/**

- [[LICENSE]] — MIT License
- [[README]] — Status] [![Coverage Status](https://coveralls.io/repos/github/json5/json5/badge.svg)][Coverage Status]

**banco/.netlify/plugins/node_modules/jsonfile/**

- [[README]] — Node.js - jsonfile ================

**banco/.netlify/plugins/node_modules/jsonwebtoken/**

- [[README]] — An implementation of [JSON Web Tokens](https://tools.ietf.org/html/rfc7519).

**banco/.netlify/plugins/node_modules/junk/**

- [[readme]] — $ npm install junk

**banco/.netlify/plugins/node_modules/jwa/**

- [[README]] — A [JSON Web Algorithms](http://tools.ietf.org/id/draft-ietf-jose-json-web-algorithms-08.html) implementation focusing (exclusively, at this...

**banco/.netlify/plugins/node_modules/jws/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[readme]] — An implementation of [JSON Web Signatures](http://self-issued.info/docs/draft-ietf-jose-json-web-signature.html).

**banco/.netlify/plugins/node_modules/jwt-decode/**

- [[README]] — IMPORTANT: This library doesn't validate the token, any well-formed JWT can be decoded.

**banco/.netlify/plugins/node_modules/keyv/**

- [[README]] — In this section of the documentation we will cover:

**banco/.netlify/plugins/node_modules/kleur/**

- [[readme]] — ansi-colors  x 199,381 ops/sec ±1.04% (96 runs sampled) chalk        x  12,107 ops/sec ±2.07% (87 runs sampled) kleur        x 715,334 ops/s...

**banco/.netlify/plugins/node_modules/kuler/**

- [[README]] — Kuler is small and nifty node module that allows you to create terminal based colors using hex color codes, just like you're used to doing i...

**banco/.netlify/plugins/node_modules/lambda-local/**

- [[README]] — Lambda-local lets you test NodeJS Amazon Lambda functions on your local machine, by providing a simplistic API and command-line tool.

**banco/.netlify/plugins/node_modules/lambda-local/node_modules/commander/**

- [[Readme]] — The complete solution for [node.js](http://nodejs.org) command-line interfaces.

**banco/.netlify/plugins/node_modules/lazystream/**

- [[README]] — Sometimes you feel the itch to open *all the files* at once.

**banco/.netlify/plugins/node_modules/lazystream/node_modules/isarray/**

- [[README]] — ](https://ci.testling.com/juliangruber/isarray)

**banco/.netlify/plugins/node_modules/lazystream/node_modules/readable-stream/**

- [[CONTRIBUTING]] — By making a contribution to this project, I certify that:
- [[GOVERNANCE]] — The Node.js Streams is jointly governed by a Working Group (WG) that is responsible for high-level guidance of the project.
- [[README]] — *Node-core v8.17.0 streams for userland* [![Build Status](https://travis-ci.org/nodejs/readable-stream.svg?branch=master)](https://travis-ci...

**banco/.netlify/plugins/node_modules/lazystream/node_modules/readable-stream/doc/wg-meetings/**

- [[2015-01-30]] — Extracted from https://github.com/iojs/readable-stream/labels/wg-agenda prior to meeting.

**banco/.netlify/plugins/node_modules/lazystream/node_modules/safe-buffer/**

- [[README]] — [travis-image]: https://img.shields.io/travis/feross/safe-buffer/master.svg [travis-url]: https://travis-ci.org/feross/safe-buffer [npm-imag...

**banco/.netlify/plugins/node_modules/lazystream/node_modules/string_decoder/**

- [[README]] — *Node-core v8.9.4 string_decoder for userland*

**banco/.netlify/plugins/node_modules/lazystream/test/**

- [[data]] — And the rest, after a sudden wet thud, was silence.

**banco/.netlify/plugins/node_modules/leven/**

- [[readme]] — $ npm install leven

**banco/.netlify/plugins/node_modules/lilconfig/**

- [[readme]] — A zero-dependency alternative to [cosmiconfig](https://www.npmjs.com/package/cosmiconfig) with the same API.

**banco/.netlify/plugins/node_modules/lines-and-columns/**

- [[README]] — Maps lines and columns to character offsets and back.

**banco/.netlify/plugins/node_modules/lmdb/**

- [[README]] — This is an ultra-fast NodeJS and Deno interface to LMDB; probably the fastest and most efficient key-value/database interface that exists fo...
- [[SECURITY]] — Please report security vulnerabilities to kriszyp@gmail.com.

**banco/.netlify/plugins/node_modules/lmdb/dependencies/lz4/lib/**

- [[README]] — LZ4 - Library Files ================================

**banco/.netlify/plugins/node_modules/lmdb/dependencies/lz4/lib/dll/example/**

- [[README]] — LZ4 Windows binary package ====================================

**banco/.netlify/plugins/node_modules/locate-path/**

- [[readme]] — $ npm install locate-path

**banco/.netlify/plugins/node_modules/lodash/**

- [[README]] — The [Lodash](https://lodash.com/) library exported as [Node.js](https://nodejs.org/) modules.

**banco/.netlify/plugins/node_modules/lodash-es/**

- [[README]] — The [Lodash](https://lodash.com/) library exported as [ES](http://www.ecma-international.org/ecma-262/6.0/) modules.

**banco/.netlify/plugins/node_modules/lodash.camelcase/**

- [[README]] — The [lodash](https://lodash.com/) method _.camelCase exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.clonedeep/**

- [[README]] — The [lodash](https://lodash.com/) method _.cloneDeep exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.debounce/**

- [[README]] — The [lodash](https://lodash.com/) method _.debounce exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.difference/**

- [[README]] — The [lodash](https://lodash.com/) method _.difference exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.differencewith/**

- [[README]] — The [lodash](https://lodash.com/) method _.differenceWith exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.every/**

- [[README]] — The [lodash](https://lodash.com/) method _.every exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.flattendeep/**

- [[README]] — The [lodash](https://lodash.com/) method _.flattenDeep exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.foreach/**

- [[README]] — The [lodash](https://lodash.com/) method _.forEach exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.get/**

- [[README]] — The [lodash](https://lodash.com/) method _.get exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.groupby/**

- [[README]] — The [lodash](https://lodash.com/) method _.groupBy exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.includes/**

- [[README]] — The [lodash](https://lodash.com/) method _.includes exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.intersection/**

- [[README]] — The [lodash](https://lodash.com/) method _.intersection exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.intersectionwith/**

- [[README]] — The [lodash](https://lodash.com/) method _.intersectionWith exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.isboolean/**

- [[README]] — The [lodash](https://lodash.com/) method _.isBoolean exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.isempty/**

- [[README]] — The [lodash](https://lodash.com/) method _.isEmpty exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.isequal/**

- [[README]] — The [Lodash](https://lodash.com/) method _.isEqual exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.isinteger/**

- [[README]] — The [lodash](https://lodash.com/) method _.isInteger exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.isnumber/**

- [[README]] — The [lodash](https://lodash.com/) method _.isNumber exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.isplainobject/**

- [[README]] — The [lodash](https://lodash.com/) method _.isPlainObject exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.isstring/**

- [[README]] — The [lodash](https://lodash.com/) method _.isString exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.kebabcase/**

- [[README]] — The [lodash](https://lodash.com/) method _.kebabCase exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.map/**

- [[README]] — The [lodash](https://lodash.com/) method _.map exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.mapvalues/**

- [[README]] — The [lodash](https://lodash.com/) method _.mapValues exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.maxby/**

- [[README]] — The [lodash](https://lodash.com/) method _.maxBy exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.memoize/**

- [[README]] — The [lodash](https://lodash.com/) method _.memoize exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.merge/**

- [[README]] — The [Lodash](https://lodash.com/) method _.merge exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.omit/**

- [[README]] — The [Lodash](https://lodash.com/) method _.omit exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.once/**

- [[README]] — The [lodash](https://lodash.com/) method _.once exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.orderby/**

- [[README]] — The [Lodash](https://lodash.com/) method _.orderBy exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.pick/**

- [[README]] — The [lodash](https://lodash.com/) method _.pick exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.pickby/**

- [[README]] — The [lodash](https://lodash.com/) method _.pickBy exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.set/**

- [[README]] — The [lodash](https://lodash.com/) method _.set exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.snakecase/**

- [[README]] — The [lodash](https://lodash.com/) method _.snakeCase exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.sortby/**

- [[README]] — The [lodash](https://lodash.com/) method _.sortBy exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.topairs/**

- [[README]] — The [lodash](https://lodash.com/) method _.toPairs exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.uniq/**

- [[README]] — The [lodash](https://lodash.com/) method _.uniq exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/lodash.uniqwith/**

- [[README]] — The [lodash](https://lodash.com/) method _.uniqWith exported as a [Node.js](https://nodejs.org/) module.

**banco/.netlify/plugins/node_modules/logform/**

- [[CHANGELOG]] — 2023/02/07 ## Bugfix The triple-beam types package has been promoted to a full dependency, by first-time contributor @carboneater (Thanks!)...
- [[README]] — A mutable object-based log format designed for chaining & objectMode streams.

**banco/.netlify/plugins/node_modules/logform/node_modules/@colors/colors/**

- [[README]] — Please check out the [roadmap](ROADMAP.md) for upcoming features and releases.

**banco/.netlify/plugins/node_modules/longest-streak/**

- [[readme]] — Get the count of the longest repeating streak of substring in value.

**banco/.netlify/plugins/node_modules/loose-envify/**

- [[README]] — Fast (and loose) selective process.env replacer using [js-tokens](https://github.com/lydell/js-tokens) instead of an AST.

**banco/.netlify/plugins/node_modules/lowercase-keys/**

- [[readme]] — $ npm install lowercase-keys

**banco/.netlify/plugins/node_modules/lru-cache/**

- [[README]] — A cache object that deletes the least-recently-used items.

**banco/.netlify/plugins/node_modules/lru-queue/**

- [[README]] — _Originally derived from [memoizee](https://github.com/medikoo/memoize) package._

**banco/.netlify/plugins/node_modules/luxon/**

- [[LICENSE]] — Copyright 2019 JS Foundation and other contributors
- [[README]] — Luxon is a library for working with dates and times in JavaScript.

**banco/.netlify/plugins/node_modules/magic-string/**

- [[README]] — <a href="https://github.com/Rich-Harris/magic-string/actions/workflows/test.yml"> <img src="https://img.shields.io/github/actions/workflow/s...

**banco/.netlify/plugins/node_modules/make-dir/**

- [[readme]] — $ npm install make-dir

**banco/.netlify/plugins/node_modules/make-dir/node_modules/semver/**

- [[README]] — semver(1) -- The semantic versioner for npm ===========================================

**banco/.netlify/plugins/node_modules/make-error/**

- [[README]] — Installation of the [npm package](https://npmjs.org/package/make-error):

**banco/.netlify/plugins/node_modules/math-intrinsics/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — ES Math-related intrinsics and helpers, robustly cached.

**banco/.netlify/plugins/node_modules/mdast-util-from-markdown/**

- [[readme]] — [mdast][github-mdast] utility that turns markdown into a syntax tree.

**banco/.netlify/plugins/node_modules/mdast-util-mdx-expression/**

- [[readme]] — [mdast][] extensions to parse and serialize [MDX][] expressions ({Math.PI}).

**banco/.netlify/plugins/node_modules/mdast-util-mdx-jsx/**

- [[readme]] — [mdast][] extensions to parse and serialize [MDX][] JSX (<a />).

**banco/.netlify/plugins/node_modules/mdast-util-mdxjs-esm/**

- [[readme]] — [mdast][] extensions to parse and serialize [MDX][] ESM (import/exports).

**banco/.netlify/plugins/node_modules/mdast-util-phrasing/**

- [[readme]] — [mdast][] utility to check if a node is phrasing content.

**banco/.netlify/plugins/node_modules/mdast-util-to-hast/**

- [[readme]] — [mdast][] utility to transform to [hast][].

**banco/.netlify/plugins/node_modules/mdast-util-to-markdown/**

- [[readme]] — [mdast][github-mdast] utility that turns a syntax tree into markdown.

**banco/.netlify/plugins/node_modules/mdast-util-to-string/**

- [[readme]] — [mdast][] utility to get the text content of a node.

**banco/.netlify/plugins/node_modules/meant/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Like the Did you mean? in git for npm

**banco/.netlify/plugins/node_modules/media-typer/**

- [[HISTORY]] — 0.3.0 / 2014-09-07 ==================
- [[README]] — Simple RFC 6838 media type parser

**banco/.netlify/plugins/node_modules/memoize-one/**

- [[README]] — A memoization library that only caches the result of the most recent arguments.

**banco/.netlify/plugins/node_modules/memoizee/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — _Originally derived from [es5-ext](https://github.com/medikoo/es5-ext) package._

**banco/.netlify/plugins/node_modules/merge-descriptors/**

- [[HISTORY]] — 1.0.1 / 2016-01-17 ==================
- [[README]] — Merge objects using descriptors.

**banco/.netlify/plugins/node_modules/merge-options/**

- [[readme]] — $ npm install --save merge-options

**banco/.netlify/plugins/node_modules/merge-options/node_modules/is-plain-obj/**

- [[readme]] — An object is plain if it's created by either {}, new Object(), or Object.create(null).

**banco/.netlify/plugins/node_modules/merge-stream/**

- [[README]] — Merge (interleave) a bunch of streams.

**banco/.netlify/plugins/node_modules/merge2/**

- [[README]] — Merge multiple streams into one stream in sequence or parallel.

**banco/.netlify/plugins/node_modules/methods/**

- [[HISTORY]] — 1.1.2 / 2016-01-17 ==================
- [[README]] — HTTP verbs that Node.js core's HTTP parser supports.

**banco/.netlify/plugins/node_modules/micro-api-client/**

- [[README]] — Small library for talking to micro REST APIs (not related to Netlify's main API).

**banco/.netlify/plugins/node_modules/micromark/**

- [[readme]] — Markdown parser.

**banco/.netlify/plugins/node_modules/micromark-core-commonmark/**

- [[readme]] — [micromark][] constructs that make up the core of CommonMark.

**banco/.netlify/plugins/node_modules/micromark-factory-destination/**

- [[readme]] — [micromark][] factory to parse destinations (found in resources, definitions).

**banco/.netlify/plugins/node_modules/micromark-factory-label/**

- [[readme]] — [micromark][] factory to parse labels (found in media, definitions).

**banco/.netlify/plugins/node_modules/micromark-factory-space/**

- [[readme]] — [micromark][] factory to parse [markdown space][markdown-space] (found in lots of places).

**banco/.netlify/plugins/node_modules/micromark-factory-title/**

- [[readme]] — [micromark][] factory to parse markdown titles (found in resources, definitions).

**banco/.netlify/plugins/node_modules/micromark-factory-whitespace/**

- [[readme]] — [micromark][] factory to parse [markdown line endings or spaces][ws] (found in lots of places).

**banco/.netlify/plugins/node_modules/micromark-util-character/**

- [[readme]] — [micromark][] utility to handle [character codes][code].

**banco/.netlify/plugins/node_modules/micromark-util-chunked/**

- [[readme]] — [micromark][] utility to splice and push with giant arrays.

**banco/.netlify/plugins/node_modules/micromark-util-classify-character/**

- [[readme]] — [micromark][] utility to classify whether a character is whitespace or punctuation.

**banco/.netlify/plugins/node_modules/micromark-util-combine-extensions/**

- [[readme]] — [micromark][] utility to combine [syntax][] or [html][] extensions.

**banco/.netlify/plugins/node_modules/micromark-util-decode-numeric-character-reference/**

- [[readme]] — [micromark][] utility to decode numeric character references.

**banco/.netlify/plugins/node_modules/micromark-util-decode-string/**

- [[readme]] — [micromark][] utility to decode markdown strings.

**banco/.netlify/plugins/node_modules/micromark-util-edit-map/**

- [[readme]] — [micromark][] utility to batch changes to lists of events.

**banco/.netlify/plugins/node_modules/micromark-util-encode/**

- [[readme]] — [micromark][] utility to encode dangerous html characters.

**banco/.netlify/plugins/node_modules/micromark-util-html-tag-name/**

- [[readme]] — [micromark][] utility with list of html tag names.

**banco/.netlify/plugins/node_modules/micromark-util-normalize-identifier/**

- [[readme]] — [micromark][] utility normalize identifiers.

**banco/.netlify/plugins/node_modules/micromark-util-resolve-all/**

- [[readme]] — [micromark][] utility to resolve subtokens.

**banco/.netlify/plugins/node_modules/micromark-util-sanitize-uri/**

- [[readme]] — [micromark][] utility to sanitize urls.

**banco/.netlify/plugins/node_modules/micromark-util-subtokenize/**

- [[readme]] — [micromark][] utility to tokenize subtokens.

**banco/.netlify/plugins/node_modules/micromark-util-symbol/**

- [[readme]] — [micromark][] utility with symbols.

**banco/.netlify/plugins/node_modules/micromark-util-types/**

- [[readme]] — [micromark][] utility package with TypeScript types.

**banco/.netlify/plugins/node_modules/micromark/node_modules/@types/debug/**

- [[README]] — This package contains type definitions for debug (https://github.com/debug-js/debug).

**banco/.netlify/plugins/node_modules/micromatch/**

- [[README]] — Please consider following this project's author, [Jon Schlinkert](https://github.com/jonschlinkert), and consider starring the project to sh...

**banco/.netlify/plugins/node_modules/micromatch/node_modules/picomatch/**

- [[README]] — picomatch x 1,993,050 ops/sec ±0.51% (91 runs sampled) minimatch x 627,206 ops/sec ±1.96% (87 runs sampled))

**banco/.netlify/plugins/node_modules/mime/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — A comprehensive, compact MIME type module.

**banco/.netlify/plugins/node_modules/mime-db/**

- [[HISTORY]] — 1.54.0 / 2025-03-17 ===================
- [[README]] — This is a large database of mime types and information about them.

**banco/.netlify/plugins/node_modules/mime-types/**

- [[HISTORY]] — 2.1.35 / 2022-03-12 ===================
- [[README]] — The ultimate javascript content-type utility.

**banco/.netlify/plugins/node_modules/mime-types/node_modules/mime-db/**

- [[HISTORY]] — 1.52.0 / 2022-02-21 ===================
- [[README]] — This is a large database of mime types and information about them.

**banco/.netlify/plugins/node_modules/mimic-fn/**

- [[readme]] — Useful when you wrap a function in another function and like to preserve the original name and other properties.

**banco/.netlify/plugins/node_modules/mimic-response/**

- [[readme]] — $ npm install mimic-response

**banco/.netlify/plugins/node_modules/min-document/**

- [[CONTRIBUTION]] — Individuals making significant and valuable contributions are given commit-access to the project to contribute as they see fit.
- [[README]] — <!-- [![browser support][5]][6] -->

**banco/.netlify/plugins/node_modules/minimatch/**

- [[README]] — A minimal matching utility.

**banco/.netlify/plugins/node_modules/minimist/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — parse argument options

**banco/.netlify/plugins/node_modules/minipass/**

- [[LICENSE]] — Version 1.0.0
- [[README]] — A _very_ minimal implementation of a [PassThrough stream](https://nodejs.org/api/stream.html#stream_class_stream_passthrough)

**banco/.netlify/plugins/node_modules/minizlib/**

- [[README]] — A fast zlib stream built on [minipass](http://npm.im/minipass) and Node.js's zlib binding.

**banco/.netlify/plugins/node_modules/mkdirp-classic/**

- [[README]] — Just a non-deprecated mirror of [mkdirp 0.5.2](https://github.com/substack/node-mkdirp/tree/0.5.1) for use in modules where we depend on the...

**banco/.netlify/plugins/node_modules/module-definition/**

- [[README]] — Determines the module definition type (CommonJS, AMD, ES6, or none) for a given JavaScript file by walking through the AST.

**banco/.netlify/plugins/node_modules/moment/**

- [[CHANGELOG]] — Changelog =========
- [[README]] — A JavaScript date library for parsing, validating, manipulating, and formatting dates.

**banco/.netlify/plugins/node_modules/ms/**

- [[license]] — The MIT License (MIT)
- [[readme]] — Use this package to easily convert various time formats to milliseconds.

**banco/.netlify/plugins/node_modules/msgpackr/**

- [[README]] — The msgpackr package is an extremely fast MessagePack NodeJS/JavaScript implementation.
- [[SECURITY]] — Please report security vulnerabilities to kriszyp@gmail.com.
- [[benchmark]] — Here are more comprehensive benchmarks. This is comparison with the next fastest JS projects using the benchmark tool from msgpack-lite (and...

**banco/.netlify/plugins/node_modules/msgpackr-extract/**

- [[README]] — This module is designed to do fast and efficient native/C-level extraction of strings from MessagePack binary data.

**banco/.netlify/plugins/node_modules/msgpackr-extract/node_modules/node-gyp-build-optional-packages/**

- [[README]] — npm install node-gyp-build

**banco/.netlify/plugins/node_modules/mute-stream/**

- [[README]] — Bytes go in, but they don't come out (when muted).

**banco/.netlify/plugins/node_modules/mz/**

- [[HISTORY]] — 2.7.0 / 2017-09-13 ==================
- [[README]] — Modernize node.js to current ECMAScript specifications!

**banco/.netlify/plugins/node_modules/nano-pubsub/**

- [[README]] — Tiny (<0.5 kb) publish/subscribe

**banco/.netlify/plugins/node_modules/nanoid/**

- [[README]] — <img src="https://ai.github.io/nanoid/logo.svg" align="right" alt="Nano ID logo by Anton Lovchikov" width="180" height="94">

**banco/.netlify/plugins/node_modules/napi-build-utils/**

- [[README]] — A set of utilities to assist developers of tools that build [Node-API](https://nodejs.org/api/n-api.html#n_api_n_api) native add-ons.
- [[index]] — TODO — nessuna prosa dopo il titolo.

**banco/.netlify/plugins/node_modules/negotiator/**

- [[HISTORY]] — unreleased ==================
- [[README]] — An HTTP content negotiator for Node.js

**banco/.netlify/plugins/node_modules/netlify/**

- [[README]] — A Netlify [OpenAPI](https://github.com/netlify/open-api) client that works in the browser and Node.js.

**banco/.netlify/plugins/node_modules/netlify/node_modules/node-fetch/**

- [[LICENSE]] — The MIT License (MIT)
- [[README]] — <div align="center"> <img src="docs/media/Banner.svg" alt="Node Fetch"/> <br> <p>A light-weight module that brings <a href="https://develope...

**banco/.netlify/plugins/node_modules/next-tick/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — To be used in environment agnostic modules that need nextTick functionality.

**banco/.netlify/plugins/node_modules/node-abi/**

- [[README]] — Get the Node ABI (application binary interface) for a given target and runtime, and vice versa.

**banco/.netlify/plugins/node_modules/node-addon-api/**

- [[LICENSE]] — The MIT License (MIT) =====================
- [[README]] — This module contains header-only C++ wrapper classes which simplify the use of the C based [Node-API](https://nodejs.org/dist/latest/docs/ap...

**banco/.netlify/plugins/node_modules/node-addon-api/tools/**

- [[README]] — The clang-format checking tools is designed to check changed lines of code compared to given git-refs.

**banco/.netlify/plugins/node_modules/node-domexception/**

- [[README]] — An implementation of the DOMException class from NodeJS

**banco/.netlify/plugins/node_modules/node-domexception/.history/**

- [[README_20210527203617]] — An implementation of the DOMException class from NodeJS
- [[README_20210527212714]] — An implementation of the DOMException class from NodeJS
- [[README_20210527213345]] — An implementation of the DOMException class from NodeJS
- [[README_20210527213411]] — An implementation of the DOMException class from NodeJS
- [[README_20210527213803]] — An implementation of the DOMException class from NodeJS
- [[README_20210527214323]] — An implementation of the DOMException class from NodeJS
- [[README_20210527214408]] — An implementation of the DOMException class from NodeJS

**banco/.netlify/plugins/node_modules/node-exports-info/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Info about node exports field support: version ranges, categories, etc.

**banco/.netlify/plugins/node_modules/node-exports-info/node_modules/semver/**

- [[README]] — semver(1) -- The semantic versioner for npm ===========================================

**banco/.netlify/plugins/node_modules/node-fetch/**

- [[LICENSE]] — The MIT License (MIT)
- [[README]] — node-fetch ==========

**banco/.netlify/plugins/node_modules/node-fetch/node_modules/webidl-conversions/**

- [[LICENSE]] — Copyright (c) 2014, Domenic Denicola All rights reserved.
- [[README]] — This package implements, in JavaScript, the algorithms to convert a given JavaScript value according to a given [WebIDL](http://heycam.githu...

**banco/.netlify/plugins/node_modules/node-fetch/node_modules/whatwg-url/**

- [[README]] — ﻿# whatwg-url

**banco/.netlify/plugins/node_modules/node-forge/**

- [[README]] — A native implementation of [TLS][] (and various other cryptographic tools) in [JavaScript][].

**banco/.netlify/plugins/node_modules/node-gyp-build/**

- [[README]] — npm install node-gyp-build
- [[SECURITY]] — To report a security vulnerability, please use the [Tidelift security contact](https://tidelift.com/security).

**banco/.netlify/plugins/node_modules/node-gyp-build-optional-packages/**

- [[README]] — npm install node-gyp-build

**banco/.netlify/plugins/node_modules/node-html-parser/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Fast HTML Parser is a _very fast_ HTML parser.

**banco/.netlify/plugins/node_modules/node-object-hash/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — <div style="margin: 24px 0 16px;"> <img src="https://gitlab.com/m03geek/node-object-hash/raw/master/logo.svg" align="left" width="256" heigh...

**banco/.netlify/plugins/node_modules/node-releases/**

- [[README]] — All data is located in data directory.

**banco/.netlify/plugins/node_modules/node-source-walk/**

- [[README]] — npm install node-source-walk

**banco/.netlify/plugins/node_modules/nopt/**

- [[README]] — $ node my-program.js --many1 5 --many1 null --many1 foo { many1: ["5", "null", "foo"] }

**banco/.netlify/plugins/node_modules/normalize-package-data/**

- [[README]] — normalize-package-data exports a function that normalizes package metadata.

**banco/.netlify/plugins/node_modules/normalize-path/**

- [[README]] — Please consider following this project's author, [Jon Schlinkert](https://github.com/jonschlinkert), and consider starring the project to sh...

**banco/.netlify/plugins/node_modules/normalize-url/**

- [[readme]] — Useful when you need to display, store, deduplicate, sort, compare, etc, URLs.

**banco/.netlify/plugins/node_modules/npm-run-path/**

- [[readme]] — In [npm run scripts](https://docs.npmjs.com/cli/run-script) you can execute locally installed binaries by name.

**banco/.netlify/plugins/node_modules/npm-run-path/node_modules/path-key/**

- [[readme]] — It's usually PATH but on Windows it can be any casing like Path...

**banco/.netlify/plugins/node_modules/npm-run-path/node_modules/unicorn-magic/**

- [[readme]] — npm install unicorn-magic

**banco/.netlify/plugins/node_modules/nth-check/**

- [[README]] — Parses and compiles CSS nth-checks to highly optimized functions.

**banco/.netlify/plugins/node_modules/nwsapi/**

- [[README]] — Fast CSS Selectors API Engine

**banco/.netlify/plugins/node_modules/object-assign/**

- [[readme]] — Node.js 4 and up, as well as every evergreen browser (Chrome, Edge, Firefox, Opera, Safari), support Object.assign() :tada:.

**banco/.netlify/plugins/node_modules/object-inspect/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.

**banco/.netlify/plugins/node_modules/object-keys/**

- [[CHANGELOG]] — 1.1.1 / 2019-04-06 ================= * [Fix] exclude deprecated Firefox keys (#53)
- [[README]] — An Object.keys shim. Invoke its "shim" method to shim Object.keys if it is unavailable.

**banco/.netlify/plugins/node_modules/object.assign/**

- [[CHANGELOG]] — 4.1.7 / 2024-12-18 ================== * [Deps] add missing es-object-atoms (#86)
- [[README]] — An Object.assign shim. Invoke its "shim" method to shim Object.assign if it is unavailable.

**banco/.netlify/plugins/node_modules/object.entries/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — An ES2017 spec-compliant Object.entries shim.

**banco/.netlify/plugins/node_modules/obug/**

- [[README]] — A lightweight JavaScript debugging utility, forked from [debug](https://www.npmjs.com/package/debug), featuring TypeScript and ESM support.

**banco/.netlify/plugins/node_modules/on-finished/**

- [[HISTORY]] — 2.4.1 / 2022-02-22 ==================
- [[README]] — Execute a callback when a HTTP request closes, finishes, or errors.

**banco/.netlify/plugins/node_modules/on-headers/**

- [[HISTORY]] — 1.1.0 / 2025-07-17 ================== * - Fix [CVE-2025-7339](https://www.cve.org/CVERecord?id=CVE-2025-7339) ([GHSA-76c9-3jph-rj3q](https:/...
- [[README]] — Execute a listener when a response is about to write headers.

**banco/.netlify/plugins/node_modules/once/**

- [[README]] — Only call a function once.

**banco/.netlify/plugins/node_modules/one-time/**

- [[README]] — Call the supplied function exactly one time.

**banco/.netlify/plugins/node_modules/onetime/**

- [[readme]] — When called multiple times it will return the return value from the first call.

**banco/.netlify/plugins/node_modules/oniguruma-to-es/**

- [[README]] — “I think \[Oniguruma-To-ES] is very wonderful”<br> — K.

**banco/.netlify/plugins/node_modules/open/**

- [[readme]] — This is meant to be used in command-line tools and scripts, not in the browser.

**banco/.netlify/plugins/node_modules/openapi-fetch/**

- [[CHANGELOG]] — Refresh of 0.13.2; corrupted package
- [[CONTRIBUTING]] — Thanks for being willing to contribute! 🙏
- [[README]] — <img src="../../docs/public/assets/openapi-fetch.svg" alt="openapi-fetch" width="216" height="40" />

**banco/.netlify/plugins/node_modules/openapi-typescript-helpers/**

- [[README]] — Helper utilities that power openapi-fetch but are generically-available for any project.

**banco/.netlify/plugins/node_modules/opentracing/**

- [[README]] — This library is a JavaScript implementation of Open Tracing API.

**banco/.netlify/plugins/node_modules/ordered-binary/**

- [[README]] — The ordered-binary package provides a representation of JavaScript primitives, serialized into binary format (NodeJS Buffers or Uint8Arrays)...

**banco/.netlify/plugins/node_modules/ordered-binary/.claude/worktrees/bun-finishutf8/**

- [[README]] — The ordered-binary package provides a representation of JavaScript primitives, serialized into binary format (NodeJS Buffers or Uint8Arrays)...

**banco/.netlify/plugins/node_modules/os-tmpdir/**

- [[readme]] — Use this instead of require('os').tmpdir() to get a consistent behavior on different Node.js versions (even 0.8).

**banco/.netlify/plugins/node_modules/outdent/**

- [[CHANGELOG]] — I didn't maintain a changelog before this point, sorry!
- [[README]] — ES6 template strings are great, but they preserve everything between the backticks, including leading spaces.

**banco/.netlify/plugins/node_modules/own-keys/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Robustly get an object's own property keys (strings and symbols), including non-enumerables when possible.

**banco/.netlify/plugins/node_modules/p-cancelable/**

- [[readme]] — Useful for animation, loading resources, long-running async computations, async iteration, etc.

**banco/.netlify/plugins/node_modules/p-defer/**

- [[readme]] — [Don't use this unless you know what you're doing.](https://github.com/petkaantonov/bluebird/wiki/Promise-anti-patterns#the-deferred-anti-pa...

**banco/.netlify/plugins/node_modules/p-event/**

- [[readme]] — Useful when you need only one event emission and want to use it with promises or await it in an async function.

**banco/.netlify/plugins/node_modules/p-is-promise/**

- [[readme]] — Why not [is-promise](https://github.com/then/is-promise)?

**banco/.netlify/plugins/node_modules/p-limit/**

- [[readme]] — $ npm install p-limit

**banco/.netlify/plugins/node_modules/p-locate/**

- [[readme]] — Think of it like an async version of [Array#find](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Array/find).

**banco/.netlify/plugins/node_modules/p-locate/node_modules/p-limit/**

- [[readme]] — $ npm install p-limit

**banco/.netlify/plugins/node_modules/p-locate/node_modules/yocto-queue/**

- [[readme]] — You should use this package instead of an array if you do a lot of Array#push() and Array#shift() on large arrays, since Array#shift() has [...

**banco/.netlify/plugins/node_modules/p-map/**

- [[readme]] — Useful when you need to run promise-returning & async functions multiple times with different inputs concurrently.

**banco/.netlify/plugins/node_modules/p-throttle/**

- [[readme]] — It also works with normal functions.

**banco/.netlify/plugins/node_modules/p-timeout/**

- [[readme]] — npm install p-timeout

**banco/.netlify/plugins/node_modules/p-wait-for/**

- [[readme]] — Can be useful for polling.

**banco/.netlify/plugins/node_modules/package-json-from-dist/**

- [[LICENSE]] — Version 1.0.0
- [[README]] — Sometimes you want to load the package.json into your TypeScript program, and it's tempting to just import '../package.json', since that see...

**banco/.netlify/plugins/node_modules/parent-module/**

- [[readme]] — Node.js exposes module.parent, but it only gives you the first cached parent, which is not necessarily the actual parent.

**banco/.netlify/plugins/node_modules/parse-entities/**

- [[readme]] — Parse HTML character references.

**banco/.netlify/plugins/node_modules/parse-entities/node_modules/@types/unist/**

- [[README]] — This package contains type definitions for unist (https://github.com/syntax-tree/unist).

**banco/.netlify/plugins/node_modules/parse-gitignore/**

- [[README]] — Please consider following this project's author, [Jon Schlinkert](https://github.com/jonschlinkert), and consider starring the project to sh...

**banco/.netlify/plugins/node_modules/parse-headers/**

- [[readme]] — Parse http headers, works with browserify/xhr

**banco/.netlify/plugins/node_modules/parse-json/**

- [[readme]] — $ npm install parse-json

**banco/.netlify/plugins/node_modules/parse-ms/**

- [[readme]] — npm install parse-ms

**banco/.netlify/plugins/node_modules/parse-path/**

- [[README]] — <a href="https://www.buymeacoffee.com/H96WwChMy" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/yellow_img....

**banco/.netlify/plugins/node_modules/parse-url/**

- [[README]] — <a href="https://www.buymeacoffee.com/H96WwChMy" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/yellow_img....

**banco/.netlify/plugins/node_modules/parse5/**

- [[README]] — <p align="center"> <a href="https://github.com/inikulin/parse5"> <img src="https://raw.github.com/inikulin/parse5/master/media/logo.png" alt...

**banco/.netlify/plugins/node_modules/parseurl/**

- [[HISTORY]] — 1.3.3 / 2019-04-15 ==================
- [[README]] — Parse a URL with memoization.

**banco/.netlify/plugins/node_modules/password-prompt/**

- [[README]] — Node cross-platform password prompt.

**banco/.netlify/plugins/node_modules/path-exists/**

- [[readme]] — NOTE: fs.existsSync has been un-deprecated in Node.js since 6.8.0.

**banco/.netlify/plugins/node_modules/path-is-absolute/**

- [[readme]] — $ npm install --save path-is-absolute

**banco/.netlify/plugins/node_modules/path-key/**

- [[readme]] — It's usually PATH, but on Windows it can be any casing like Path...

**banco/.netlify/plugins/node_modules/path-parse/**

- [[README]] — $ npm install --save path-parse

**banco/.netlify/plugins/node_modules/path-scurry/**

- [[LICENSE]] — Version 1.0.0
- [[README]] — Extremely high performant utility for building tools that read the file system, minimizing filesystem and path string munging operations to...

**banco/.netlify/plugins/node_modules/path-scurry/node_modules/lru-cache/**

- [[README]] — A cache object that deletes the least-recently-used items.

**banco/.netlify/plugins/node_modules/path-to-regexp/**

- [[Readme]] — Turn an Express-style path string such as /user/:name into a regular expression.

**banco/.netlify/plugins/node_modules/path-type/**

- [[readme]] — $ npm install path-type

**banco/.netlify/plugins/node_modules/peek-readable/**

- [[README]] — A promise based asynchronous stream reader, which makes reading from a stream easy.

**banco/.netlify/plugins/node_modules/pend/**

- [[README]] — Dead-simple optimistic async helper.

**banco/.netlify/plugins/node_modules/picocolors/**

- [[README]] — The tiniest and the fastest library for terminal output formatting with ANSI colors.

**banco/.netlify/plugins/node_modules/picomatch/**

- [[README]] — picomatch x 3,251,247 ops/sec ±0.25% (95 runs sampled) minimatch x 497,224 ops/sec ±0.11% (100 runs sampled)

**banco/.netlify/plugins/node_modules/pirates/**

- [[README]] — This library allows to add custom require hooks, which do not interfere with other require hooks.

**banco/.netlify/plugins/node_modules/pkg-dir/**

- [[readme]] — $ npm install pkg-dir

**banco/.netlify/plugins/node_modules/pkg-dir/node_modules/find-up/**

- [[readme]] — $ npm install find-up

**banco/.netlify/plugins/node_modules/pkg-dir/node_modules/locate-path/**

- [[readme]] — $ npm install locate-path

**banco/.netlify/plugins/node_modules/pkg-dir/node_modules/p-locate/**

- [[readme]] — Think of it like an async version of [Array#find](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Array/find).

**banco/.netlify/plugins/node_modules/pkg-dir/node_modules/path-exists/**

- [[readme]] — NOTE: fs.existsSync has been un-deprecated in Node.js since 6.8.0.

**banco/.netlify/plugins/node_modules/possible-typed-array-names/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — A simple list of possible Typed Array names.

**banco/.netlify/plugins/node_modules/postcss/**

- [[README]] — <img align="right" width="95" height="95" alt="Philosopher’s stone, logo of PostCSS" src="https://postcss.org/logo.svg">

**banco/.netlify/plugins/node_modules/postcss-import/**

- [[README]] — rules by inlining content.

**banco/.netlify/plugins/node_modules/postcss-import/node_modules/resolve/**

- [[SECURITY]] — Please [file a private vulnerability report](https://github.com/browserify/resolve/security/advisories/new), or email [@ljharb](https://gith...

**banco/.netlify/plugins/node_modules/postcss-import/node_modules/resolve/.github/**

- [[INCIDENT_RESPONSE_PROCESS]] — We take the security of resolve very seriously.
- [[THREAT_MODEL]] — This threat model focuses on the core path resolution algorithm, including filesystem interaction, option handling, and cache management.

**banco/.netlify/plugins/node_modules/postcss-js/**

- [[README]] — <img align="right" width="135" height="95" title="Philosopher’s stone, logo of PostCSS" src="https://postcss.org/logo-leftp.svg">

**banco/.netlify/plugins/node_modules/postcss-nested/**

- [[README]] — <img align="right" width="135" height="95" title="Philosopher’s stone, logo of PostCSS" src="https://postcss.org/logo-leftp.svg">

**banco/.netlify/plugins/node_modules/postcss-selector-parser/**

- [[API]] — not documented here are subject to change at any point.*
- [[CHANGELOG]] — were not parsed correctly. - Updated cssesc to 2.0.0 (major).
- [[README]] — With [npm](https://npmjs.com/package/postcss-selector-parser) do:

**banco/.netlify/plugins/node_modules/postcss-value-parser/**

- [[README]] — Transforms CSS declaration values and at-rule parameters into a tree of nodes, and provides a simple traversal API.

**banco/.netlify/plugins/node_modules/postcss-values-parser/**

- [[README]] — A CSS property value parser built upon [PostCSS](https://github.com/postcss/postcss), following the same node and traversal patterns as Post...

**banco/.netlify/plugins/node_modules/prebuild-install/**

- [[CHANGELOG]] — [7.1.3]: https://github.com/prebuild/prebuild-install/releases/tag/v7.1.3
- [[CONTRIBUTING]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — Instead of [prebuild](https://github.com/prebuild/prebuild) paired with [prebuild-install](https://github.com/prebuild/prebuild-install), we...

**banco/.netlify/plugins/node_modules/prebuild-install/node_modules/chownr/**

- [[README]] — Like chown -R.

**banco/.netlify/plugins/node_modules/prebuild-install/node_modules/readable-stream/**

- [[CONTRIBUTING]] — By making a contribution to this project, I certify that:
- [[GOVERNANCE]] — The Node.js Streams is jointly governed by a Working Group (WG) that is responsible for high-level guidance of the project.
- [[README]] — *Node.js core streams for userland* [![Build Status](https://travis-ci.com/nodejs/readable-stream.svg?branch=master)](https://travis-ci.com/...

**banco/.netlify/plugins/node_modules/prebuild-install/node_modules/tar-fs/**

- [[README]] — filesystem bindings for [tar-stream](https://github.com/mafintosh/tar-stream).

**banco/.netlify/plugins/node_modules/prebuild-install/node_modules/tar-stream/**

- [[README]] — tar-stream is a streaming tar parser and generator and nothing else.

**banco/.netlify/plugins/node_modules/precinct/**

- [[README]] — npm install precinct

**banco/.netlify/plugins/node_modules/pretty-error/**

- [[README]] — A small tool to see node.js errors with less clutter:

**banco/.netlify/plugins/node_modules/pretty-ms/**

- [[readme]] — npm install pretty-ms

**banco/.netlify/plugins/node_modules/process/**

- [[README]] — Works in node.js and browsers via the browser.js shim provided with the module.

**banco/.netlify/plugins/node_modules/process-nextick-args/**

- [[license]] — Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Softw...
- [[readme]] — process-nextick-args =====

**banco/.netlify/plugins/node_modules/progress/**

- [[CHANGELOG]] — 2.0.0 / 2017-04-04 ==================
- [[Readme]] — Flexible ascii progress bar.

**banco/.netlify/plugins/node_modules/progress-stream/**

- [[README]] — Read the progress of a stream. Supports speed and eta.

**banco/.netlify/plugins/node_modules/prompts/**

- [[readme]] — <p align="center"> <img src="https://github.com/terkelg/prompts/raw/master/prompts.png" alt="Prompts" width="500" /> </p>

**banco/.netlify/plugins/node_modules/prop-types/**

- [[README]] — Runtime type checking for React props and similar objects.

**banco/.netlify/plugins/node_modules/prop-types/node_modules/react-is/**

- [[README]] — This package allows you to test arbitrary values and see if they're a particular React element type.

**banco/.netlify/plugins/node_modules/property-information/**

- [[readme]] — Info on the properties and attributes of the web platform (HTML, SVG, ARIA, XML, XMLNS, XLink).

**banco/.netlify/plugins/node_modules/protocols/**

- [[README]] — <a href="https://www.buymeacoffee.com/H96WwChMy" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/yellow_img....

**banco/.netlify/plugins/node_modules/proxy-addr/**

- [[HISTORY]] — 2.0.8 =====
- [[README]] — Determine address of proxied request

**banco/.netlify/plugins/node_modules/proxy-from-env/**

- [[README]] — that takes an input URL (a string, an instance of [URL](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api), or [url.parse](http...

**banco/.netlify/plugins/node_modules/pseudomap/**

- [[README]] — A thing that is a lot like ES6 Map, but without iterators, for use in environments where for..of syntax and Map are not available.

**banco/.netlify/plugins/node_modules/psl/**

- [[README]] — [Public Suffix List](https://publicsuffix.org/).
- [[SECURITY]] — To report a security vulnerability, please use the [Tidelift security contact](https://tidelift.com/security).

**banco/.netlify/plugins/node_modules/psl/node_modules/punycode/**

- [[README]] — Punycode.js is a robust Punycode converter that fully complies to [RFC 3492](https://tools.ietf.org/html/rfc3492) and [RFC 5891](https://too...

**banco/.netlify/plugins/node_modules/pump/**

- [[README]] — pump is a small node module that pipes streams together and destroys all of them if one of them closes.
- [[SECURITY]] — To report a security vulnerability, please use the [Tidelift security contact](https://tidelift.com/security).

**banco/.netlify/plugins/node_modules/pumpify/**

- [[README]] — Combine an array of streams into a single duplex stream using [pump](https://github.com/mafintosh/pump) and [duplexify](https://github.com/m...

**banco/.netlify/plugins/node_modules/punycode/**

- [[README]] — A robust Punycode converter that fully complies to [RFC 3492](https://tools.ietf.org/html/rfc3492) and [RFC 5891](https://tools.ietf.org/htm...

**banco/.netlify/plugins/node_modules/qs/**

- [[CHANGELOG]] — [Fix] fix regressions from robustness refactor [actions] update reusable workflows
- [[LICENSE]] — BSD 3-Clause License
- [[README]] — A querystring parsing and stringifying library with some added security.

**banco/.netlify/plugins/node_modules/qs/.github/**

- [[SECURITY]] — Please file a private vulnerability report via GitHub, email [@ljharb](https://github.com/ljharb), or see https://tidelift.com/security if y...
- [[THREAT_MODEL]] — This threat model focuses on the core parsing and stringifying functionality, specifically the handling of nested objects and arrays, option...

**banco/.netlify/plugins/node_modules/querystringify/**

- [[README]] — A somewhat JSON compatible interface for query string parsing.

**banco/.netlify/plugins/node_modules/queue-microtask/**

- [[README]] — [ci-image]: https://img.shields.io/github/workflow/status/feross/queue-microtask/ci/master [ci-url]: https://github.com/feross/queue-microta...

**banco/.netlify/plugins/node_modules/quick-lru/**

- [[readme]] — Useful when you need to cache something and limit memory usage.

**banco/.netlify/plugins/node_modules/quote-unquote/**

- [[README]] — quote and unquote strings. escapes internal quotes and slashes.

**banco/.netlify/plugins/node_modules/range-parser/**

- [[HISTORY]] — 1.2.1 / 2019-05-10 ==================
- [[README]] — Range header field parser.

**banco/.netlify/plugins/node_modules/raw-body/**

- [[README]] — Gets the entire buffer of a stream either as a Buffer or a string.

**banco/.netlify/plugins/node_modules/rc/**

- [[README]] — The non-configurable configuration loader for lazy people.

**banco/.netlify/plugins/node_modules/react/**

- [[README]] — React is a JavaScript library for creating user interfaces.

**banco/.netlify/plugins/node_modules/react-dom/**

- [[README]] — This package serves as the entry point to the DOM and server renderers for React.

**banco/.netlify/plugins/node_modules/react-hook-form/**

- [[README]] — <div align="center"> <a href="https://react-hook-form.com" title="React Hook Form - Simple React forms validation"> <img src="https://raw.gi...

**banco/.netlify/plugins/node_modules/react-is/**

- [[README]] — This package allows you to test arbitrary values and see if they're a particular React element type.

**banco/.netlify/plugins/node_modules/react-select/**

- [[README]] — The Select control for [React](https://reactjs.com).

**banco/.netlify/plugins/node_modules/react-to-text/**

- [[README]] — Convert react components to plain text without any HTML markup.

**banco/.netlify/plugins/node_modules/react-transition-group/**

- [[README]] — A set of components for managing component states (including mounting and unmounting) over time, specifically designed with animation in min...

**banco/.netlify/plugins/node_modules/read/**

- [[README]] — For reading user input from stdin.

**banco/.netlify/plugins/node_modules/read-cache/**

- [[README]] — Reads and caches the entire contents of a file until it is modified.

**banco/.netlify/plugins/node_modules/read-package-up/**

- [[readme]] — npm install read-package-up

**banco/.netlify/plugins/node_modules/read-pkg/**

- [[readme]] — npm install read-pkg

**banco/.netlify/plugins/node_modules/read-pkg/node_modules/parse-json/**

- [[readme]] — npm install parse-json

**banco/.netlify/plugins/node_modules/readable-stream/**

- [[README]] — _Node.js core streams for userland_

**banco/.netlify/plugins/node_modules/readable-web-to-node-stream/**

- [[README]] — Converts a [Web-API readable stream](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStreamDefaultReader) into a [Node.js readable...

**banco/.netlify/plugins/node_modules/readdir-glob/**

- [[README]] — Recursive version of fs.readdir wih stream API and glob filtering.

**banco/.netlify/plugins/node_modules/readdir-glob/node_modules/minimatch/**

- [[README]] — A minimal matching utility.
- [[changelog]] — rather than escaped literals

**banco/.netlify/plugins/node_modules/readdirp/**

- [[README]] — Recursive version of fs.readdir. Exposes a stream API (with small RAM & CPU footprint) and a promise API.

**banco/.netlify/plugins/node_modules/redux/**

- [[LICENSE]] — The MIT License (MIT)
- [[README]] — Redux is a predictable state container for JavaScript apps.

**banco/.netlify/plugins/node_modules/redux-thunk/**

- [[LICENSE]] — The MIT License (MIT)
- [[README]] — Thunk [middleware](https://redux.js.org/tutorials/fundamentals/part-4-store#middleware) for Redux.

**banco/.netlify/plugins/node_modules/reflect.getprototypeof/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — An ES2015 mostly-spec-compliant Reflect.getPrototypeOf sham/polyfill/replacement that works in as many engines as possible - specifically, a...

**banco/.netlify/plugins/node_modules/regex/**

- [[README]] — <div align="center"> <a href="https://github.com/slevithan/regex#readme"> <picture> <source media="(prefers-color-scheme: dark)" srcset="htt...

**banco/.netlify/plugins/node_modules/regex-recursion/**

- [[README]] — This is an official plugin for [Regex+](https://github.com/slevithan/regex) that adds support for recursive matching up to a specified max d...

**banco/.netlify/plugins/node_modules/regex-utilities/**

- [[README]] — Tiny utilities that the [regex](https://github.com/slevithan/regex) library makes available for reuse in its plugins.

**banco/.netlify/plugins/node_modules/regexp.prototype.flags/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — RegExp.prototype.flags <sup>[![Version Badge][npm-version-svg]][package-url]</sup>

**banco/.netlify/plugins/node_modules/remove-trailing-separator/**

- [[history]] — Initial release.
- [[readme]] — Removes all separators from the end of a string.

**banco/.netlify/plugins/node_modules/renderkid/**

- [[README]] — RenderKid allows you to use HTML and CSS to style your CLI output, making it easy to create a beautiful, readable, and consistent look for y...

**banco/.netlify/plugins/node_modules/renderkid/node_modules/ansi-regex/**

- [[readme]] — $ npm install --save ansi-regex

**banco/.netlify/plugins/node_modules/renderkid/node_modules/strip-ansi/**

- [[readme]] — $ npm install --save strip-ansi

**banco/.netlify/plugins/node_modules/require-package-name/**

- [[LICENSE]] — The MIT License (MIT) Copyright (c) 2015 Matt DesLauriers
- [[README]] — Gets the base package name for a module path in a require statement.

**banco/.netlify/plugins/node_modules/requires-port/**

- [[README]] — The module name says it all, check if a protocol requires a given port.

**banco/.netlify/plugins/node_modules/resolve/**

- [[SECURITY]] — Please [file a private vulnerability report](https://github.com/browserify/resolve/security/advisories/new), or email [@ljharb](https://gith...

**banco/.netlify/plugins/node_modules/resolve-alpn/**

- [[README]] — Returns an object with an alpnProtocol property.

**banco/.netlify/plugins/node_modules/resolve-from/**

- [[readme]] — $ npm install resolve-from

**banco/.netlify/plugins/node_modules/resolve-pathname/**

- [[README]] — [build-badge]: https://img.shields.io/travis/mjackson/resolve-pathname/master.svg?style=flat-square [build]: https://travis-ci.org/mjackson/...

**banco/.netlify/plugins/node_modules/resolve/.github/**

- [[INCIDENT_RESPONSE_PROCESS]] — We take the security of resolve very seriously.
- [[THREAT_MODEL]] — This threat model focuses on the core path resolution algorithm, including filesystem interaction, option handling, and cache management.

**banco/.netlify/plugins/node_modules/responselike/**

- [[README]] — Returns a streamable response object similar to a [Node.js HTTP response stream](https://nodejs.org/api/http.html#http_class_http_incomingme...

**banco/.netlify/plugins/node_modules/restore-cursor/**

- [[readme]] — Prevent the cursor you've hidden interactively from remaining hidden if the process crashes.

**banco/.netlify/plugins/node_modules/retry/**

- [[README]] — Abstraction for exponential and custom retry strategies for failed operations.

**banco/.netlify/plugins/node_modules/retry-request/**

- [[readme]] — $ npm install --save request $ npm install --save retry-request  js var request = require('retry-request', { request: require('request') });

**banco/.netlify/plugins/node_modules/reusify/**

- [[README]] — Reuse your objects and functions for maximum speed.
- [[SECURITY]] — Use this section to tell people about which versions of your project are currently being supported with security updates.

**banco/.netlify/plugins/node_modules/rimraf/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — The [UNIX command](http://en.wikipedia.org/wiki/Rm_(Unix)) rm -rf for node.

**banco/.netlify/plugins/node_modules/rimraf/node_modules/brace-expansion/**

- [[README]] — [Brace expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html), as known from sh/bash, in JavaScript.

**banco/.netlify/plugins/node_modules/rimraf/node_modules/glob/**

- [[README]] — Match files using the patterns the shell uses, like stars and stuff.

**banco/.netlify/plugins/node_modules/rimraf/node_modules/minimatch/**

- [[README]] — A minimal matching utility.

**banco/.netlify/plugins/node_modules/run-applescript/**

- [[readme]] — $ npm install run-applescript

**banco/.netlify/plugins/node_modules/run-applescript/node_modules/execa/**

- [[readme]] — <img src="media/logo.svg" width="400"> <br>

**banco/.netlify/plugins/node_modules/run-applescript/node_modules/get-stream/**

- [[readme]] — $ npm install get-stream

**banco/.netlify/plugins/node_modules/run-applescript/node_modules/human-signals/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — const { signalsByName, signalsByNumber } = require('human-signals')

**banco/.netlify/plugins/node_modules/run-applescript/node_modules/is-stream/**

- [[readme]] — $ npm install is-stream

**banco/.netlify/plugins/node_modules/run-applescript/node_modules/npm-run-path/**

- [[readme]] — In [npm run scripts](https://docs.npmjs.com/cli/run-script) you can execute locally installed binaries by name.

**banco/.netlify/plugins/node_modules/run-applescript/node_modules/strip-final-newline/**

- [[readme]] — Can be useful when parsing the output of, for example, ChildProcess#execFile, as [binaries usually output a newline at the end](https://stac...

**banco/.netlify/plugins/node_modules/run-async/**

- [[README]] — Run Async =========

**banco/.netlify/plugins/node_modules/run-parallel/**

- [[README]] — [travis-image]: https://img.shields.io/travis/feross/run-parallel/master.svg [travis-url]: https://travis-ci.org/feross/run-parallel [npm-im...

**banco/.netlify/plugins/node_modules/rxjs/**

- [[README]] — Find out how to update to v6, automatically update your TypeScript code, and more!

**banco/.netlify/plugins/node_modules/rxjs/_esm2015/**

- [[README]] — Find out how to update to v6, automatically update your TypeScript code, and more!

**banco/.netlify/plugins/node_modules/rxjs/_esm5/**

- [[README]] — Find out how to update to v6, automatically update your TypeScript code, and more!

**banco/.netlify/plugins/node_modules/rxjs/node_modules/tslib/**

- [[README]] — This is a runtime library for [TypeScript](http://www.typescriptlang.org/) that contains all of the TypeScript helper functions.

**banco/.netlify/plugins/node_modules/rxjs/src/**

- [[README]] — Find out how to update to v6, automatically update your TypeScript code, and more!

**banco/.netlify/plugins/node_modules/safe-array-concat/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — npm install --save safe-array-concat

**banco/.netlify/plugins/node_modules/safe-buffer/**

- [[README]] — [travis-image]: https://img.shields.io/travis/feross/safe-buffer/master.svg [travis-url]: https://travis-ci.org/feross/safe-buffer [npm-imag...

**banco/.netlify/plugins/node_modules/safe-push-apply/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Push an array of items into an array, while being robust against prototype modification.

**banco/.netlify/plugins/node_modules/safe-regex-test/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Give a regex, get a robust predicate function that tests it against a string.

**banco/.netlify/plugins/node_modules/safe-stable-stringify/**

- [[readme]] — Safe, deterministic and fast serialization alternative to [JSON.stringify][].

**banco/.netlify/plugins/node_modules/safer-buffer/**

- [[Porting-Buffer]] — <a id="overview"></a> ## Overview
- [[Readme]] — [travis-image]: https://travis-ci.org/ChALkeR/safer-buffer.svg?branch=master [travis-url]: https://travis-ci.org/ChALkeR/safer-buffer [npm-i...

**banco/.netlify/plugins/node_modules/same-origin/**

- [[README]] — same-origin ===========

**banco/.netlify/plugins/node_modules/sanitize-filename/**

- [[Changelog]] — Check for reserved Windows filenames (CON, PRN, AUX, NUL, COM1, LPT1, etc).
- [[LICENSE]] — This project is licensed under the [WTFPL][] and [ISC][] licenses.
- [[README]] — Sanitize a string to be safe for use as a filename by removing directory paths and invalid characters.

**banco/.netlify/plugins/node_modules/saxes/**

- [[README]] — A sax-style non-validating parser for XML.

**banco/.netlify/plugins/node_modules/scheduler/**

- [[README]] — This is a package for cooperative scheduling in a browser environment.

**banco/.netlify/plugins/node_modules/semver/**

- [[README]] — semver(1) -- The semantic versioner for npm ===========================================

**banco/.netlify/plugins/node_modules/send/**

- [[HISTORY]] — 0.19.2 / 2025-12-15 ===================
- [[README]] — Send is a library for streaming files from the file system as a http response supporting partial responses (Ranges), conditional-GET negotia...
- [[SECURITY]] — The send team and community take all security bugs seriously.

**banco/.netlify/plugins/node_modules/send/node_modules/debug/**

- [[CHANGELOG]] — 2.6.9 / 2017-09-22 ==================
- [[README]] — A tiny node.js debugging utility modelled after node core's debugging technique.

**banco/.netlify/plugins/node_modules/send/node_modules/debug/node_modules/ms/**

- [[license]] — The MIT License (MIT)
- [[readme]] — Use this package to easily convert various time formats to milliseconds.

**banco/.netlify/plugins/node_modules/send/node_modules/mime/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — Comprehensive MIME type mapping API based on mime-db module.

**banco/.netlify/plugins/node_modules/serve-static/**

- [[HISTORY]] — 1.16.3 / 2024-12-15 ===================
- [[README]] — This is a [Node.js](https://nodejs.org/en/) module available through the [npm registry](https://www.npmjs.com/).

**banco/.netlify/plugins/node_modules/set-function-length/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Set a function’s length.

**banco/.netlify/plugins/node_modules/set-function-name/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Set a function’s name.

**banco/.netlify/plugins/node_modules/set-proto/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Robustly set the Prototype of an object.

**banco/.netlify/plugins/node_modules/setprototypeof/**

- [[README]] — A simple cross platform implementation to set the prototype of an instianted object.

**banco/.netlify/plugins/node_modules/sharp/**

- [[README]] — <img src="https://cdn.jsdelivr.net/gh/lovell/sharp@main/docs/image/sharp-logo.svg" width="160" height="160" alt="sharp logo" align="right">

**banco/.netlify/plugins/node_modules/sharp/node_modules/node-addon-api/**

- [[LICENSE]] — The MIT License (MIT) =====================
- [[README]] — This module contains  header-only C++ wrapper classes which simplify the use of the C based [Node-API](https://nodejs.org/dist/latest/docs/a...

**banco/.netlify/plugins/node_modules/sharp/node_modules/node-addon-api/tools/**

- [[README]] — The clang-format checking tools is designed to check changed lines of code compared to given git-refs.

**banco/.netlify/plugins/node_modules/sharp/vendor/8.14.5/darwin-arm64v8/**

- [[THIRD-PARTY-NOTICES]] — This software contains third-party libraries used under the terms of the following licences:

**banco/.netlify/plugins/node_modules/shebang-command/**

- [[readme]] — $ npm install shebang-command

**banco/.netlify/plugins/node_modules/shebang-regex/**

- [[readme]] — $ npm install shebang-regex

**banco/.netlify/plugins/node_modules/shiki/**

- [[README]] — A beautiful syntax highlighter based on TextMate grammars, accurate and powerful.

**banco/.netlify/plugins/node_modules/side-channel/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Store information about any JS value in a side channel.

**banco/.netlify/plugins/node_modules/side-channel-list/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Store information about any JS value in a side channel, using a linked list.

**banco/.netlify/plugins/node_modules/side-channel-map/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Store information about any JS value in a side channel, using a Map.

**banco/.netlify/plugins/node_modules/side-channel-weakmap/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Store information about any JS value in a side channel.

**banco/.netlify/plugins/node_modules/signal-exit/**

- [[README]] — When you want to fire an event no matter how a process exits:

**banco/.netlify/plugins/node_modules/simple-concat/**

- [[README]] — [travis-image]: https://img.shields.io/travis/feross/simple-concat/master.svg [travis-url]: https://travis-ci.org/feross/simple-concat [npm-...

**banco/.netlify/plugins/node_modules/simple-get/**

- [[README]] — [ci-image]: https://img.shields.io/github/workflow/status/feross/simple-get/ci/master [ci-url]: https://github.com/feross/simple-get/actions...

**banco/.netlify/plugins/node_modules/simple-swizzle/**

- [[README]] — var swizzle = require('simple-swizzle');

**banco/.netlify/plugins/node_modules/simple-swizzle/node_modules/is-arrayish/**

- [[README]] — var isArrayish = require('is-arrayish');

**banco/.netlify/plugins/node_modules/sisteransi/**

- [[readme]] — npm install sisteransi

**banco/.netlify/plugins/node_modules/slash/**

- [[readme]] — [Forward-slash paths can be used in Windows](http://superuser.com/a/176395/6877) as long as they're not extended-length paths and don't cont...

**banco/.netlify/plugins/node_modules/slugify/**

- [[README]] — var slugify = require('slugify')

**banco/.netlify/plugins/node_modules/snakify-ts/**

- [[README]] — A typescript typed snake_case function that recursively snake cases a camel cased object structure.

**banco/.netlify/plugins/node_modules/socket.io/**

- [[Readme]] — Socket.IO enables real-time bidirectional event-based communication.

**banco/.netlify/plugins/node_modules/socket.io-adapter/**

- [[Readme]] — Default socket.io in-memory adapter class.

**banco/.netlify/plugins/node_modules/socket.io-adapter/node_modules/ws/**

- [[README]] — ws is a simple to use, blazing fast, and thoroughly tested WebSocket client and server implementation.

**banco/.netlify/plugins/node_modules/socket.io-parser/**

- [[Readme]] — A socket.io encoder and decoder written in JavaScript complying with version 5 of [socket.io-protocol](https://github.com/socketio/socket.io...

**banco/.netlify/plugins/node_modules/source-map/**

- [[CHANGELOG]] — happens to have come to depend on. See #235.
- [[README]] — This is a library to generate and consume the source map format [described here][format].

**banco/.netlify/plugins/node_modules/source-map-js/**

- [[README]] — Difference between original [source-map](https://github.com/mozilla/source-map):

**banco/.netlify/plugins/node_modules/source-map-support/**

- [[LICENSE]] — The MIT License (MIT)
- [[README]] — This module provides source map support for stack traces in node via the [V8 stack trace API](https://github.com/v8/v8/wiki/Stack-Trace-API)...

**banco/.netlify/plugins/node_modules/space-separated-tokens/**

- [[readme]] — Parse and stringify space-separated tokens.

**banco/.netlify/plugins/node_modules/spdx-correct/**

- [[README]] — var correct = require('spdx-correct') var assert = require('assert')

**banco/.netlify/plugins/node_modules/spdx-exceptions/**

- [[README]] — The package exports an array of strings.

**banco/.netlify/plugins/node_modules/spdx-expression-parse/**

- [[README]] — This package parses [SPDX license expression](https://spdx.org/spdx-specification-21-web-version#h.jxpfx0ykyb60) strings describing license...

**banco/.netlify/plugins/node_modules/spdx-license-ids/**

- [[README]] — A list of [SPDX license](https://spdx.org/licenses/) identifiers

**banco/.netlify/plugins/node_modules/speedometer/**

- [[README]] — Speed measurement in Javascript

**banco/.netlify/plugins/node_modules/sprintf-js/**

- [[README]] — sprintf.js is a complete open source JavaScript sprintf implementation for the *browser* and *node.js*.

**banco/.netlify/plugins/node_modules/stack-trace/**

- [[Readme]] — Get v8 stack traces as an array of CallSite objects.

**banco/.netlify/plugins/node_modules/statuses/**

- [[HISTORY]] — 2.0.2 / 2025-06-06 ==================
- [[README]] — HTTP status utility for node.

**banco/.netlify/plugins/node_modules/stop-iteration-iterator/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Firefox 17-26 iterators throw a StopIteration object to indicate "done".

**banco/.netlify/plugins/node_modules/stream-chain/**

- [[README]] — [npm-img]:      https://img.shields.io/npm/v/stream-chain.svg [npm-url]:      https://npmjs.org/package/stream-chain

**banco/.netlify/plugins/node_modules/stream-events/**

- [[readme]] — This is just a simple thing that tells you when _read and _write have been called, saving you the trouble of writing this yourself.

**banco/.netlify/plugins/node_modules/stream-json/**

- [[README]] — [npm-image]:      https://img.shields.io/npm/v/stream-json.svg [npm-url]:        https://npmjs.org/package/stream-json

**banco/.netlify/plugins/node_modules/stream-shift/**

- [[README]] — Returns the next buffer/object in a stream's readable queue

**banco/.netlify/plugins/node_modules/streamx/**

- [[README]] — An iteration of the Node.js core streams with a series of improvements.

**banco/.netlify/plugins/node_modules/string-argv/**

- [[CHANGELOG]] — Dev Experience Changes - Project now compiled with TypeScript and provides typings
- [[README]] — This is useful when testing Command Line Utilities that you want to pass arguments to and is the opposite of what the other argv utilities d...

**banco/.netlify/plugins/node_modules/string-similarity/**

- [[README]] — string-similarity =================

**banco/.netlify/plugins/node_modules/string-width/**

- [[readme]] — Some Unicode characters are [fullwidth](https://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms) and use double the normal width.

**banco/.netlify/plugins/node_modules/string-width-cjs/**

- [[readme]] — Some Unicode characters are [fullwidth](https://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms) and use double the normal width.

**banco/.netlify/plugins/node_modules/string-width-cjs/node_modules/emoji-regex/**

- [[README]] — _emoji-regex_ offers a regular expression to match all emoji symbols (including textual representations of emoji) as per the Unicode Standar...

**banco/.netlify/plugins/node_modules/string-width/node_modules/ansi-regex/**

- [[readme]] — npm install ansi-regex

**banco/.netlify/plugins/node_modules/string-width/node_modules/strip-ansi/**

- [[readme]] — npm install strip-ansi

**banco/.netlify/plugins/node_modules/string.prototype.trim/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — An ES5 spec-compliant String.prototype.trim shim.

**banco/.netlify/plugins/node_modules/string.prototype.trimend/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — An ES2019-spec-compliant String.prototype.trimEnd shim.

**banco/.netlify/plugins/node_modules/string.prototype.trimstart/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — An ES2019-spec-compliant String.prototype.trimStart shim.

**banco/.netlify/plugins/node_modules/string_decoder/**

- [[README]] — *Node-core v8.9.4 string_decoder for userland*

**banco/.netlify/plugins/node_modules/stringify-entities/**

- [[readme]] — Serialize (encode) HTML character references.

**banco/.netlify/plugins/node_modules/strip-ansi/**

- [[readme]] — $ npm install strip-ansi

**banco/.netlify/plugins/node_modules/strip-ansi-cjs/**

- [[readme]] — $ npm install strip-ansi

**banco/.netlify/plugins/node_modules/strip-final-newline/**

- [[readme]] — This can be useful when parsing the output of, for example, ChildProcess#execFile(), as [binaries usually output a newline at the end](https...

**banco/.netlify/plugins/node_modules/strip-json-comments/**

- [[readme]] — This is now possible:

**banco/.netlify/plugins/node_modules/strtok3/**

- [[README]] — A promise based streaming [*tokenizer*](#tokenizer) for [Node.js](http://nodejs.org) and browsers.

**banco/.netlify/plugins/node_modules/stubs/**

- [[readme]] — For when you don't want to write the same thing over and over to cache a method and call an override, then revert it, and blah blah.

**banco/.netlify/plugins/node_modules/style-to-js/**

- [[README]] — Parses CSS inline style to JavaScript object (camelCased):

**banco/.netlify/plugins/node_modules/style-to-object/**

- [[README]] — Parse CSS inline style to JavaScript object:

**banco/.netlify/plugins/node_modules/stylis/**

- [[README]] — A Light–weight CSS Preprocessor.

**banco/.netlify/plugins/node_modules/sucrase/**

- [[README]] — yarn add --dev sucrase  # Or npm install --save-dev sucrase node -r sucrase/register main.ts

**banco/.netlify/plugins/node_modules/sucrase/node_modules/commander/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[Readme]] — The complete solution for [node.js](http://nodejs.org) command-line interfaces, inspired by Ruby's [commander](https://github.com/commander-...

**banco/.netlify/plugins/node_modules/sudo-prompt/**

- [[CHANGELOG]] — [#78](https://github.com/jorangreef/sudo-prompt/issues/78).
- [[README]] — Run a non-graphical terminal command using sudo, prompting the user with a graphical OS dialog if necessary.

**banco/.netlify/plugins/node_modules/supports-color/**

- [[readme]] — $ npm install supports-color

**banco/.netlify/plugins/node_modules/supports-preserve-symlinks-flag/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Determine if the current node version supports the --preserve-symlinks flag.

**banco/.netlify/plugins/node_modules/symbol-tree/**

- [[README]] — symbol-tree =========== [![Travis CI Build Status](https://api.travis-ci.org/jsdom/js-symbol-tree.svg?branch=master)](https://travis-ci.org/...

**banco/.netlify/plugins/node_modules/tailwindcss/**

- [[README]] — <p align="center"> <a href="https://tailwindcss.com" target="_blank"> <picture> <source media="(prefers-color-scheme: dark)" srcset="https:/...

**banco/.netlify/plugins/node_modules/tailwindcss/lib/postcss-plugins/nesting/**

- [[README]] — This is a PostCSS plugin that wraps [postcss-nested](https://github.com/postcss/postcss-nested) or [postcss-nesting](https://github.com/csst...

**banco/.netlify/plugins/node_modules/tailwindcss/lib/value-parser/**

- [[README]] — This is a customized version of of [PostCSS Value Parser](https://github.com/TrySound/postcss-value-parser) to fix some bugs around parsing...

**banco/.netlify/plugins/node_modules/tailwindcss/node_modules/chokidar/**

- [[README]] — Node.js fs.watch:

**banco/.netlify/plugins/node_modules/tailwindcss/node_modules/chokidar/node_modules/glob-parent/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — Extract the non-magic parent path from a glob string.

**banco/.netlify/plugins/node_modules/tailwindcss/node_modules/glob-parent/**

- [[README]] — Extract the non-magic parent path from a glob string.

**banco/.netlify/plugins/node_modules/tailwindcss/node_modules/picomatch/**

- [[README]] — picomatch x 1,993,050 ops/sec ±0.51% (91 runs sampled) minimatch x 627,206 ops/sec ±1.96% (87 runs sampled))

**banco/.netlify/plugins/node_modules/tailwindcss/node_modules/postcss-load-config/**

- [[README]] — <div align="center"> <img width="100" height="100" title="Load Options" src="http://michael-ciniawsky.github.io/postcss-load-options/logo.sv...

**banco/.netlify/plugins/node_modules/tailwindcss/node_modules/readdirp/**

- [[README]] — Recursive version of [fs.readdir](https://nodejs.org/api/fs.html#fs_fs_readdir_path_options_callback).

**banco/.netlify/plugins/node_modules/tailwindcss/node_modules/resolve/**

- [[SECURITY]] — Please [file a private vulnerability report](https://github.com/browserify/resolve/security/advisories/new), or email [@ljharb](https://gith...

**banco/.netlify/plugins/node_modules/tailwindcss/node_modules/resolve/.github/**

- [[INCIDENT_RESPONSE_PROCESS]] — We take the security of resolve very seriously.
- [[THREAT_MODEL]] — This threat model focuses on the core path resolution algorithm, including filesystem interaction, option handling, and cache management.

**banco/.netlify/plugins/node_modules/tailwindcss/node_modules/yaml/**

- [[README]] — This library:

**banco/.netlify/plugins/node_modules/tailwindcss/src/postcss-plugins/nesting/**

- [[README]] — This is a PostCSS plugin that wraps [postcss-nested](https://github.com/postcss/postcss-nested) or [postcss-nesting](https://github.com/csst...

**banco/.netlify/plugins/node_modules/tailwindcss/src/value-parser/**

- [[README]] — This is a customized version of of [PostCSS Value Parser](https://github.com/TrySound/postcss-value-parser) to fix some bugs around parsing...

**banco/.netlify/plugins/node_modules/tapable/**

- [[README]] — The tapable package exposes many Hook classes, which can be used to create hooks for plugins.

**banco/.netlify/plugins/node_modules/tar/**

- [[LICENSE]] — Version 1.0.0
- [[README]] — Fast and full-featured Tar for Node.js

**banco/.netlify/plugins/node_modules/tar-fs/**

- [[README]] — Filesystem bindings for [tar-stream](https://github.com/mafintosh/tar-stream).

**banco/.netlify/plugins/node_modules/tar-stream/**

- [[README]] — tar-stream is a streaming tar parser and generator and nothing else.

**banco/.netlify/plugins/node_modules/tar-stream/node_modules/b4a/**

- [[README]] — Buffer for Array (B4A) provides a set of functions for bridging the gap between the Node.js Buffer class and the Uint8Array class.

**banco/.netlify/plugins/node_modules/tar/node_modules/yallist/**

- [[LICENSE]] — Version 1.0.0
- [[README]] — Yet Another Linked List

**banco/.netlify/plugins/node_modules/teeny-request/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — Like request, but much smaller - and with less options.

**banco/.netlify/plugins/node_modules/teeny-request/node_modules/agent-base/**

- [[README]] — agent-base ========== ### Turn a function into an [http.Agent][http.Agent] instance [![Build Status](https://github.com/TooTallNate/node-age...

**banco/.netlify/plugins/node_modules/teeny-request/node_modules/https-proxy-agent/**

- [[README]] — https-proxy-agent ================ ### An HTTP(s) proxy http.Agent implementation for HTTPS [![Build Status](https://github.com/TooTallNate/...

**banco/.netlify/plugins/node_modules/teex/**

- [[README]] — Turn a readable stream into multiple readable [streamx streams](https://github.com/mafintosh/streamx).

**banco/.netlify/plugins/node_modules/text-decoder/**

- [[README]] — Streaming text decoder that preserves multibyte Unicode characters.

**banco/.netlify/plugins/node_modules/text-decoder/node_modules/b4a/**

- [[README]] — Buffer for Array (B4A) provides a set of functions for bridging the gap between the Node.js Buffer class and the Uint8Array class.

**banco/.netlify/plugins/node_modules/text-hex/**

- [[README]] — Transforms a given piece of text to a hex color.

**banco/.netlify/plugins/node_modules/thenify/**

- [[History]] — 3.3.1 / 2020-06-18 ==================
- [[README]] — Promisify a callback-based function using [any-promise](https://github.com/kevinbeaty/any-promise).

**banco/.netlify/plugins/node_modules/thenify-all/**

- [[History]] — 1.6.0 / 2015-01-11 ==================
- [[README]] — Promisifies all the selected functions in an object.

**banco/.netlify/plugins/node_modules/through2/**

- [[LICENSE]] — Copyright (c) Rod Vagg (the "Original Author") and additional contributors
- [[README]] — A tiny wrapper around Node streams.Transform (Streams2/3) to avoid explicit subclassing noise

**banco/.netlify/plugins/node_modules/through2/node_modules/isarray/**

- [[README]] — ](https://ci.testling.com/juliangruber/isarray)

**banco/.netlify/plugins/node_modules/through2/node_modules/readable-stream/**

- [[CONTRIBUTING]] — By making a contribution to this project, I certify that:
- [[GOVERNANCE]] — The Node.js Streams is jointly governed by a Working Group (WG) that is responsible for high-level guidance of the project.
- [[README]] — *Node-core v8.17.0 streams for userland* [![Build Status](https://travis-ci.org/nodejs/readable-stream.svg?branch=master)](https://travis-ci...

**banco/.netlify/plugins/node_modules/through2/node_modules/readable-stream/doc/wg-meetings/**

- [[2015-01-30]] — Extracted from https://github.com/iojs/readable-stream/labels/wg-agenda prior to meeting.

**banco/.netlify/plugins/node_modules/through2/node_modules/safe-buffer/**

- [[README]] — [travis-image]: https://img.shields.io/travis/feross/safe-buffer/master.svg [travis-url]: https://travis-ci.org/feross/safe-buffer [npm-imag...

**banco/.netlify/plugins/node_modules/through2/node_modules/string_decoder/**

- [[README]] — *Node-core v8.9.4 string_decoder for userland*

**banco/.netlify/plugins/node_modules/timers-ext/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — $ npm install timers-ext

**banco/.netlify/plugins/node_modules/tiny-invariant/**

- [[README]] — A tiny [invariant](https://www.npmjs.com/package/invariant) alternative.

**banco/.netlify/plugins/node_modules/tiny-warning/**

- [[README]] — A tiny [warning](https://www.npmjs.com/package/warning) alternative.

**banco/.netlify/plugins/node_modules/tinycolor2/**

- [[README]] — TinyColor is a small, fast library for color manipulation and conversion in JavaScript.

**banco/.netlify/plugins/node_modules/tinyglobby/**

- [[README]] — A fast and minimal alternative to globby and fast-glob, meant to behave the same way.

**banco/.netlify/plugins/node_modules/tippy.js/**

- [[README]] — npm i tippy.js

**banco/.netlify/plugins/node_modules/titleize/**

- [[readme]] — $ npm install titleize

**banco/.netlify/plugins/node_modules/tmp/**

- [[README]] — A simple temporary file and directory creator for [node.js.][1]

**banco/.netlify/plugins/node_modules/tmp-promise/**

- [[README]] — A simple utility for creating temporary files or directories.

**banco/.netlify/plugins/node_modules/tmp-promise/node_modules/tmp/**

- [[README]] — A simple temporary file and directory creator for [node.js.][1]

**banco/.netlify/plugins/node_modules/to-regex-range/**

- [[README]] — Please consider following this project's author, [Jon Schlinkert](https://github.com/jonschlinkert), and consider starring the project to sh...

**banco/.netlify/plugins/node_modules/toidentifier/**

- [[HISTORY]] — 1.0.1 / 2021-11-14 ==================
- [[README]] — This is a [Node.js](https://nodejs.org/en/) module available through the [npm registry](https://www.npmjs.com/).

**banco/.netlify/plugins/node_modules/token-types/**

- [[README]] — A primitive token library used to read and write from a node Buffer.

**banco/.netlify/plugins/node_modules/toml/**

- [[CHANGELOG]] — 2.3.0 - July 13 2015 ====================
- [[README]] — TOML Parser for Node.js =======================

**banco/.netlify/plugins/node_modules/tough-cookie/**

- [[README]] — [RFC 6265](https://tools.ietf.org/html/rfc6265) Cookies and CookieJar for Node.js

**banco/.netlify/plugins/node_modules/tough-cookie/node_modules/punycode/**

- [[README]] — Punycode.js is a robust Punycode converter that fully complies to [RFC 3492](https://tools.ietf.org/html/rfc3492) and [RFC 5891](https://too...

**banco/.netlify/plugins/node_modules/tough-cookie/node_modules/universalify/**

- [[README]] — Make a callback- or promise-based function support both promises and callbacks.

**banco/.netlify/plugins/node_modules/tr46/**

- [[LICENSE]] — The MIT License (MIT)
- [[README]] — An JavaScript implementation of [Unicode Technical Standard #46: Unicode IDNA Compatibility Processing](https://unicode.org/reports/tr46/).

**banco/.netlify/plugins/node_modules/tr46/node_modules/punycode/**

- [[README]] — Punycode.js is a robust Punycode converter that fully complies to [RFC 3492](https://tools.ietf.org/html/rfc3492) and [RFC 5891](https://too...

**banco/.netlify/plugins/node_modules/trim-lines/**

- [[readme]] — Remove spaces and tabs around line breaks.

**banco/.netlify/plugins/node_modules/triple-beam/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — Definitions of levels for logging purposes & shareable Symbol constants.

**banco/.netlify/plugins/node_modules/truncate-utf8-bytes/**

- [[README]] — Truncate a string to the given length in bytes.

**banco/.netlify/plugins/node_modules/ts-api-utils/**

- [[LICENSE]] — Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Softw...
- [[README]] — <h1 align="center">TypeScript API Utils</h1>

**banco/.netlify/plugins/node_modules/ts-interface-checker/**

- [[README]] — This package is the runtime support for validators created by [ts-interface-builder](https://github.com/gristlabs/ts-interface-builder).

**banco/.netlify/plugins/node_modules/tslib/**

- [[README]] — This is a runtime library for [TypeScript](https://www.typescriptlang.org/) that contains all of the TypeScript helper functions.
- [[SECURITY]] — <!-- BEGIN MICROSOFT SECURITY.MD V0.0.7 BLOCK -->

**banco/.netlify/plugins/node_modules/tunnel-agent/**

- [[README]] — tunnel-agent ============

**banco/.netlify/plugins/node_modules/type/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Validate arguments input in public API endpoints.

**banco/.netlify/plugins/node_modules/type-fest/**

- [[readme]] — <div align="center"> <br> <br> <img src="media/logo.svg" alt="type-fest" height="300"> <br> <br> <b>A collection of essential TypeScript typ...

**banco/.netlify/plugins/node_modules/type-is/**

- [[HISTORY]] — 1.6.18 / 2019-04-26 ===================
- [[README]] — Infer the content-type of a request.

**banco/.netlify/plugins/node_modules/type-of/**

- [[Readme]] — Type assertions aka less-broken typeof.

**banco/.netlify/plugins/node_modules/type/docs/**

- [[array-length]] — _number_ primitive that conforms as valid _array length_
- [[array-like]] — _Array-like_ value (any value with length property)
- [[array]] — _Array_ instance
- [[big-int]] — _bigint_ primitive
- [[constructor]] — A _Function_ instance that's a _constructor_ (either regular function or _class_)
- [[date]] — _Date_ instance
- [[ensure]] — Provides a complete cumulated input validation for an API endpoint.
- [[error]] — _Error_ instance
- [[finite]] — Finite _number_ primitive
- [[function]] — _Function_ instance
- [[integer]] — Integer _number_ primitive
- [[iterable]] — Value which implements _iterable_ protocol
- [[map]] — _Map_ instance
- [[natural-number]] — Natural _number_ primitive
- [[number]] — _number_ primitive
- [[object]] — _Object_, any non-primitive value
- [[plain-function]] — A _Function_ instance that is not a _Class_
- [[plain-object]] — A _plain object_
- [[promise]] — _Promise_ instance
- [[prototype]] — Some constructor's prototype property
- [[reg-exp]] — _RegExp_ instance
- [[safe-integer]] — Safe integer _number_ primitive
- [[set]] — _Set_ instance
- [[string]] — _string_ primitive
- [[thenable]] — _Thenable_ object (an object with then method)
- [[time-value]] — _number_ primitive which is a valid _time value_ (as used internally in _Date_ instances)
- [[value]] — _Value_, any value that's neither null nor undefined .

**banco/.netlify/plugins/node_modules/typed-array-buffer/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Get the ArrayBuffer out of a TypedArray, robustly.

**banco/.netlify/plugins/node_modules/typed-array-byte-length/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Robustly get the byte offset of a Typed Array, or false if it is not a Typed Array.

**banco/.netlify/plugins/node_modules/typed-array-byte-offset/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Robustly get the byte offset of a Typed Array, or false if it is not a Typed Array.

**banco/.netlify/plugins/node_modules/typed-array-length/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Robustly get the length of a Typed Array, or false if it is not a Typed Array.

**banco/.netlify/plugins/node_modules/typedarray-to-buffer/**

- [[README]] — [travis-image]: https://img.shields.io/travis/feross/typedarray-to-buffer/master.svg [travis-url]: https://travis-ci.org/feross/typedarray-t...

**banco/.netlify/plugins/node_modules/typescript/**

- [[README]] — [TypeScript](https://www.typescriptlang.org/) is a language for application-scale JavaScript.
- [[SECURITY]] — <!-- BEGIN MICROSOFT SECURITY.MD V0.0.9 BLOCK -->

**banco/.netlify/plugins/node_modules/unbox-primitive/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Unbox a boxed JS primitive value. This module works cross-realm/iframe, does not depend on instanceof or mutable properties, and works despi...

**banco/.netlify/plugins/node_modules/unc-path-regex/**

- [[README]] — Visit the MSDN reference for [Common Data Types 2.2.57 UNC](https://msdn.microsoft.com/en-us/library/gg465305.aspx) for more information abo...

**banco/.netlify/plugins/node_modules/undici/**

- [[README]] — An HTTP/1.1 client, written from scratch for Node.js.

**banco/.netlify/plugins/node_modules/undici-types/**

- [[README]] — This package is a dual-publish of the [undici](https://www.npmjs.com/package/undici) library types.

**banco/.netlify/plugins/node_modules/undici/docs/docs/api/**

- [[Agent]] — Extends: undici.Dispatcher
- [[BalancedPool]] — Extends: undici.Dispatcher
- [[CacheStorage]] — Undici exposes a W3C spec-compliant implementation of [CacheStorage](https://developer.mozilla.org/en-US/docs/Web/API/CacheStorage) and [Cac...
- [[CacheStore]] — A Cache Store is responsible for storing and retrieving cached responses.
- [[Client]] — Extends: undici.Dispatcher
- [[ClientStats]] — Stats for a [Client](/docs/docs/api/Client.md).
- [[Connector]] — Undici creates the underlying socket via the connector builder.
- [[ContentType]] — Implements [parse a MIME type](https://mimesniff.spec.whatwg.org/#parse-a-mime-type).
- [[Cookies]] — Sets the expiry time of the cookie to the unix epoch, causing browsers to delete it when received.
- [[Debug]] — Undici (and subsenquently fetch and websocket) exposes a debug statement that can be enabled by setting NODE_DEBUG within the environment.
- [[DiagnosticsChannel]] — Stability: Experimental.
- [[Dispatcher]] — Extends: events.EventEmitter
- [[EnvHttpProxyAgent]] — Extends: undici.Dispatcher
- [[Errors]] — Undici exposes a variety of error objects that you can use to enhance your error handling.
- [[EventSource]] — Undici exposes a WHATWG spec-compliant implementation of [EventSource](https://developer.mozilla.org/en-US/docs/Web/API/EventSource) for [Se...
- [[Fetch]] — Undici exposes a fetch() method starts the process of fetching a resource from the network.
- [[GlobalInstallation]] — Undici provides an install() function to add all WHATWG fetch classes to globalThis, making them available globally without requiring import...
- [[H2CClient]] — Extends: undici.Dispatcher
- [[MockAgent]] — Extends: undici.Dispatcher
- [[MockCallHistory]] — Access to an instance with :
- [[MockCallHistoryLog]] — Access to an instance with :
- [[MockClient]] — Extends: undici.Client
- [[MockErrors]] — Undici exposes a variety of mock error objects that you can use to enhance your mock error handling.
- [[MockPool]] — Extends: undici.Pool
- [[Pool]] — Extends: undici.Dispatcher
- [[PoolStats]] — Aggregate stats for a [Pool](/docs/docs/api/Pool.md) or [BalancedPool](/docs/docs/api/BalancedPool.md).
- [[ProxyAgent]] — Extends: undici.Dispatcher
- [[RedirectHandler]] — A class that handles redirection logic for HTTP requests.
- [[RetryAgent]] — Extends: undici.Dispatcher
- [[RetryHandler]] — Extends: undici.DispatcherHandlers
- [[RoundRobinPool]] — Extends: undici.Dispatcher
- [[SnapshotAgent]] — The SnapshotAgent provides a powerful way to record and replay HTTP requests for testing purposes.
- [[Socks5ProxyAgent]] — Extends: undici.Dispatcher
- [[Util]] — Utility API for third-party implementations of the dispatcher API.
- [[WebSocket]] — Extends: [EventTarget](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget)
- [[api-lifecycle]] — An Undici [Client](/docs/docs/api/Client.md) can be best described as a state machine.

**banco/.netlify/plugins/node_modules/undici/docs/docs/best-practices/**

- [[client-certificate]] — Client certificate authentication can be configured with the Client, the required options are passed along through the connect option.
- [[crawling]] — [RFC 9309](https://datatracker.ietf.org/doc/html/rfc9309) defines crawlers as automated clients.
- [[mocking-request]] — Undici has its own mocking [utility](/docs/docs/api/MockAgent.md).
- [[proxy]] — Connecting through a proxy is possible by:
- [[undici-vs-builtin-fetch]] — Node.js has shipped a built-in fetch() implementation powered by undici since Node.js v18.
- [[writing-tests]] — Undici is tuned for a production use case and its default will keep a socket open for a few seconds after an HTTP request is completed to re...

**banco/.netlify/plugins/node_modules/undici/lib/web/subresource-integrity/**

- [[Readme]] — based on Editor’s Draft, 12 June 2025

**banco/.netlify/plugins/node_modules/undici/types/**

- [[README]] — This package is a dual-publish of the [undici](https://www.npmjs.com/package/undici) library types.

**banco/.netlify/plugins/node_modules/unicorn-magic/**

- [[readme]] — npm install unicorn-magic

**banco/.netlify/plugins/node_modules/unique-string/**

- [[readme]] — $ npm install unique-string

**banco/.netlify/plugins/node_modules/unist-util-is/**

- [[readme]] — [unist][] utility to check if nodes pass a test.

**banco/.netlify/plugins/node_modules/unist-util-position/**

- [[readme]] — [unist][] utility to get positional info of nodes.

**banco/.netlify/plugins/node_modules/unist-util-stringify-position/**

- [[readme]] — [unist][] utility to pretty print the positional info of a node.

**banco/.netlify/plugins/node_modules/unist-util-visit/**

- [[readme]] — [unist][github-unist] utility to walk the tree.

**banco/.netlify/plugins/node_modules/unist-util-visit-parents/**

- [[readme]] — [unist][] utility to walk the tree with a stack of parents.

**banco/.netlify/plugins/node_modules/universal-user-agent/**

- [[LICENSE]] — Copyright (c) 2018, Gregor Martynus (https://github.com/gr2m)
- [[README]] — const { getUserAgent } = require("universal-user-agent"); // or import { getUserAgent } from "universal-user-agent";

**banco/.netlify/plugins/node_modules/universalify/**

- [[README]] — Make a callback- or promise-based function support both promises and callbacks.

**banco/.netlify/plugins/node_modules/unixify/**

- [[README]] — Install with [npm](https://www.npmjs.com/):

**banco/.netlify/plugins/node_modules/unixify/node_modules/normalize-path/**

- [[README]] — Install with [npm](https://www.npmjs.com/):

**banco/.netlify/plugins/node_modules/unpipe/**

- [[HISTORY]] — 1.0.0 / 2015-06-14 ==================
- [[README]] — Unpipe a stream from all destinations.

**banco/.netlify/plugins/node_modules/untildify/**

- [[readme]] — $ npm install untildify

**banco/.netlify/plugins/node_modules/update-browserslist-db/**

- [[README]] — <img width="120" height="120" alt="Browserslist logo by Anton Popov" src="https://browsersl.ist/logo.svg" align="right">

**banco/.netlify/plugins/node_modules/url-parse/**

- [[README]] — url-parse was created in 2014 when the WHATWG URL API was not available in Node.js and the URL interface was supported only in some browsers...

**banco/.netlify/plugins/node_modules/urlpattern-polyfill/**

- [[README]] — URLPattern polyfills ===

**banco/.netlify/plugins/node_modules/use-isomorphic-layout-effect/**

- [[README]] — A React helper hook for scheduling a layout effect with a fallback to a regular effect for environments where layout effects should not be u...

**banco/.netlify/plugins/node_modules/utf8-byte-length/**

- [[README]] — Get the utf8 byte length of a string, taking into account multi-byte characters and surrogate pairs.

**banco/.netlify/plugins/node_modules/util-deprecate/**

- [[History]] — 1.0.2 / 2015-10-07 ==================
- [[README]] — util-deprecate ============== ### The Node.js util.deprecate() function with browser support

**banco/.netlify/plugins/node_modules/utila/**

- [[README]] — npm: npm install utila

**banco/.netlify/plugins/node_modules/utils-merge/**

- [[README]] — Merges the properties from a source object into a destination object.

**banco/.netlify/plugins/node_modules/uuid/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[CONTRIBUTING]] — Please feel free to file GitHub Issues or propose Pull Requests.
- [[LICENSE]] — The MIT License (MIT)
- [[README]] — For the creation of [RFC4122](http://www.ietf.org/rfc/rfc4122.txt) UUIDs

**banco/.netlify/plugins/node_modules/validate-npm-package-license/**

- [[README]] — validate-npm-package-license ============================

**banco/.netlify/plugins/node_modules/value-equal/**

- [[README]] — [build-badge]: https://img.shields.io/travis/mjackson/value-equal/master.svg?style=flat-square [build]: https://travis-ci.org/mjackson/value...

**banco/.netlify/plugins/node_modules/vary/**

- [[HISTORY]] — 1.1.2 / 2017-09-23 ==================
- [[README]] — Manipulate the HTTP Vary header

**banco/.netlify/plugins/node_modules/vfile/**

- [[readme]] — <h1> <img src="https://raw.githubusercontent.com/vfile/vfile/fc8164b/logo.svg?sanitize=true" alt="vfile" /> </h1>

**banco/.netlify/plugins/node_modules/vfile-message/**

- [[readme]] — Create [vfile][github-vfile] messages.

**banco/.netlify/plugins/node_modules/w3c-xmlserializer/**

- [[LICENSE]] — The MIT License (MIT) =====================
- [[README]] — An XML serializer that follows the [W3C specification](https://w3c.github.io/DOM-Parsing/).

**banco/.netlify/plugins/node_modules/weak-lru-cache/**

- [[README]] — The weak-lru-cache package provides a powerful cache that works in harmony with the JS garbage collection (GC) and least-recently used (LRU)...

**banco/.netlify/plugins/node_modules/web-streams-polyfill/**

- [[README]] — Web Streams, based on the WHATWG spec reference implementation.

**banco/.netlify/plugins/node_modules/webidl-conversions/**

- [[LICENSE]] — Copyright (c) 2014, Domenic Denicola All rights reserved.
- [[README]] — This package implements, in JavaScript, the algorithms to convert a given JavaScript value according to a given [Web IDL](http://heycam.gith...

**banco/.netlify/plugins/node_modules/whatwg-encoding/**

- [[README]] — This package provides a thin layer on top of [iconv-lite](https://github.com/ashtuchkin/iconv-lite) which makes it expose some of the same p...

**banco/.netlify/plugins/node_modules/whatwg-encoding/node_modules/iconv-lite/**

- [[Changelog]] — in recent Node versions. * Reworked Streaming API behavior in browser environments to fix #204.
- [[README]] — [Grunt](http://gruntjs.com/), [Nodemailer](http://www.nodemailer.com/), [Yeoman](http://yeoman.io/) and others.

**banco/.netlify/plugins/node_modules/whatwg-mimetype/**

- [[README]] — This package will parse [MIME types](https://mimesniff.spec.whatwg.org/#understanding-mime-types) into a structured format, which can then b...

**banco/.netlify/plugins/node_modules/whatwg-url/**

- [[README]] — ﻿# whatwg-url

**banco/.netlify/plugins/node_modules/which/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — Like the unix which utility.

**banco/.netlify/plugins/node_modules/which-boxed-primitive/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Which kind of boxed JS primitive is this?

**banco/.netlify/plugins/node_modules/which-builtin-type/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — What is the type of this builtin JavaScript value?

**banco/.netlify/plugins/node_modules/which-collection/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Which kind of Collection (Map, Set, WeakMap, WeakSet) is this JavaScript value?

**banco/.netlify/plugins/node_modules/which-typed-array/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — Which kind of Typed Array is this JavaScript value?

**banco/.netlify/plugins/node_modules/winston/**

- [[README]] — A logger for just about everything.

**banco/.netlify/plugins/node_modules/winston-transport/**

- [[CHANGELOG]] — No longer works  js const Transport = require('winston-transport'); const transport = Transport({ log: (info, callback) => { /* log somethin...
- [[README]] — The base TransportStream implementation for winston >= 3.

**banco/.netlify/plugins/node_modules/winston-transport/node_modules/readable-stream/**

- [[CONTRIBUTING]] — By making a contribution to this project, I certify that:
- [[GOVERNANCE]] — The Node.js Streams is jointly governed by a Working Group (WG) that is responsible for high-level guidance of the project.
- [[README]] — *Node.js core streams for userland* [![Build Status](https://travis-ci.com/nodejs/readable-stream.svg?branch=master)](https://travis-ci.com/...

**banco/.netlify/plugins/node_modules/winston/node_modules/is-stream/**

- [[readme]] — $ npm install is-stream

**banco/.netlify/plugins/node_modules/winston/node_modules/readable-stream/**

- [[CONTRIBUTING]] — By making a contribution to this project, I certify that:
- [[GOVERNANCE]] — The Node.js Streams is jointly governed by a Working Group (WG) that is responsible for high-level guidance of the project.
- [[README]] — *Node.js core streams for userland* [![Build Status](https://travis-ci.com/nodejs/readable-stream.svg?branch=master)](https://travis-ci.com/...

**banco/.netlify/plugins/node_modules/wrap-ansi/**

- [[readme]] — $ npm install wrap-ansi

**banco/.netlify/plugins/node_modules/wrap-ansi-cjs/**

- [[readme]] — $ npm install wrap-ansi

**banco/.netlify/plugins/node_modules/wrap-ansi-cjs/node_modules/ansi-styles/**

- [[readme]] — You probably want the higher-level [chalk](https://github.com/chalk/chalk) module for styling your strings.

**banco/.netlify/plugins/node_modules/wrap-ansi-cjs/node_modules/emoji-regex/**

- [[README]] — _emoji-regex_ offers a regular expression to match all emoji symbols (including textual representations of emoji) as per the Unicode Standar...

**banco/.netlify/plugins/node_modules/wrap-ansi-cjs/node_modules/string-width/**

- [[readme]] — Some Unicode characters are [fullwidth](https://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms) and use double the normal width.

**banco/.netlify/plugins/node_modules/wrap-ansi/node_modules/ansi-regex/**

- [[readme]] — npm install ansi-regex

**banco/.netlify/plugins/node_modules/wrap-ansi/node_modules/strip-ansi/**

- [[readme]] — npm install strip-ansi

**banco/.netlify/plugins/node_modules/wrappy/**

- [[README]] — Callback wrapping utility

**banco/.netlify/plugins/node_modules/wretch/**

- [[README]] — Fetch needs a second callback to process the response body.

**banco/.netlify/plugins/node_modules/write-file-atomic/**

- [[LICENSE]] — Copyright (c) 2015, Rebecca Turner
- [[README]] — write-file-atomic -----------------

**banco/.netlify/plugins/node_modules/write-file-atomic/node_modules/signal-exit/**

- [[README]] — When you want to fire an event no matter how a process exits:

**banco/.netlify/plugins/node_modules/ws/**

- [[README]] — ws is a simple to use, blazing fast, and thoroughly tested WebSocket client and server implementation.

**banco/.netlify/plugins/node_modules/xdg-basedir/**

- [[readme]] — $ npm install xdg-basedir

**banco/.netlify/plugins/node_modules/xml-name-validator/**

- [[README]] — This package simply tells you whether or not a string matches the [Name](http://www.w3.org/TR/xml/#NT-Name) or [QName](http://www.w3.org/TR/...

**banco/.netlify/plugins/node_modules/xmlchars/**

- [[README]] — Utilities for determining whether characters belong to character classes defined by the XML specs.

**banco/.netlify/plugins/node_modules/xtend/**

- [[README]] — Extend like a boss

**banco/.netlify/plugins/node_modules/y18n/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — The bare-bones internationalization library used by yargs.

**banco/.netlify/plugins/node_modules/yallist/**

- [[README]] — Yet Another Linked List

**banco/.netlify/plugins/node_modules/yaml/**

- [[README]] — The library is released under the ISC open source license, and the code is [available on GitHub](https://github.com/eemeli/yaml/).

**banco/.netlify/plugins/node_modules/yargs/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — <p align="center"> <img width="250" src="https://raw.githubusercontent.com/yargs/yargs/main/yargs-logo.png"> </p> <h1 align="center"> Yargs...

**banco/.netlify/plugins/node_modules/yargs-parser/**

- [[CHANGELOG]] — All notable changes to this project will be documented in this file.
- [[README]] — The mighty option parser used by [yargs](https://github.com/yargs/yargs).

**banco/.netlify/plugins/node_modules/yargs/node_modules/emoji-regex/**

- [[README]] — _emoji-regex_ offers a regular expression to match all emoji symbols (including textual representations of emoji) as per the Unicode Standar...

**banco/.netlify/plugins/node_modules/yargs/node_modules/string-width/**

- [[readme]] — Some Unicode characters are [fullwidth](https://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms) and use double the normal width.

**banco/.netlify/plugins/node_modules/yauzl/**

- [[README]] — yet another unzip library for node. For zipping, see [yazl](https://github.com/thejoshwolfe/yazl).

**banco/.netlify/plugins/node_modules/yauzl/node_modules/buffer-crc32/**

- [[README]] — crc32 that works with binary data and fancy character sets, outputs buffer, signed or unsigned data and has tests.

**banco/.netlify/plugins/node_modules/yocto-queue/**

- [[readme]] — You should use this package instead of an array if you do a lot of Array#push() and Array#shift() on large arrays, since Array#shift() has [...

**banco/.netlify/plugins/node_modules/yoctocolors/**

- [[readme]] — <sup>yoctocolors 🌈</sup>

**banco/.netlify/plugins/node_modules/yurnalist/**

- [[CHANGELOG]] — TODO — nessuna prosa dopo il titolo.
- [[README]] — An elegant console reporter, borrowed from [Yarn](https://yarnpkg.com).

**banco/.netlify/plugins/node_modules/yurnalist/node_modules/ansi-regex/**

- [[readme]] — <div align="center"> <b> <a href="https://tidelift.com/subscription/pkg/npm-ansi-regex?utm_source=npm-ansi-regex&utm_medium=referral&utm_cam...

**banco/.netlify/plugins/node_modules/yurnalist/node_modules/ansi-styles/**

- [[readme]] — You probably want the higher-level [chalk](https://github.com/chalk/chalk) module for styling your strings.

**banco/.netlify/plugins/node_modules/yurnalist/node_modules/chalk/**

- [[readme]] — <h1 align="center"> <br> <br> <img width="320" src="media/logo.svg" alt="Chalk"> <br> <br> <br> </h1>

**banco/.netlify/plugins/node_modules/yurnalist/node_modules/color-convert/**

- [[CHANGELOG]] — ([#27](https://github.com/Qix-/color-convert/pull/27)) - Removed: xxx2xxx() and xxx2xxxRaw() functions ([#27](https://github.com/Qix-/color-...
- [[README]] — Color-convert is a color conversion library for JavaScript and node.

**banco/.netlify/plugins/node_modules/yurnalist/node_modules/color-name/**

- [[README]] — A JSON with color names and its values. Based on http://dev.w3.org/csswg/css-color/#named-colors.

**banco/.netlify/plugins/node_modules/yurnalist/node_modules/escape-string-regexp/**

- [[readme]] — $ npm install --save escape-string-regexp

**banco/.netlify/plugins/node_modules/yurnalist/node_modules/has-flag/**

- [[readme]] — Correctly stops looking after an -- argument terminator.

**banco/.netlify/plugins/node_modules/yurnalist/node_modules/strip-ansi/**

- [[readme]] — <div align="center"> <b> <a href="https://tidelift.com/subscription/pkg/npm-strip-ansi?utm_source=npm-strip-ansi&utm_medium=referral&utm_cam...

**banco/.netlify/plugins/node_modules/yurnalist/node_modules/supports-color/**

- [[readme]] — $ npm install supports-color

**banco/.netlify/plugins/node_modules/zip-stream/**

- [[README]] — zip-stream is a streaming zip archive generator based on the ZipArchiveOutputStream prototype found in the [compress-commons](https://www.np...

**banco/.netlify/plugins/node_modules/zod/**

- [[README]] — <p align="center"> <img src="logo.svg" width="200px" align="center" alt="Zod logo" /> <h1 align="center">Zod</h1> <p align="center"> TypeScr...

**banco/.netlify/plugins/node_modules/zod-metadata/**

- [[README]] — Metadata support for [Zod](https://www.npmjs.com/package/zod) schemas.

**banco/.netlify/plugins/node_modules/zod-to-json-schema/**

- [[README]] — As of November 2025, this project will no longer be actively maintained.
- [[changelog]] — TODO — nessuna prosa dopo il titolo.
- [[contributing]] — Hey, thanks for wanting to contribute.

**banco/.netlify/plugins/node_modules/zod-validation-error/**

- [[README]] — Wrap zod validation errors in user-friendly readable messages.

**banco/.netlify/plugins/node_modules/zwitch/**

- [[readme]] — Handle values based on a field.

**clienti/**

- [[adelina-nails]] — Nail artist ad Alessandria, @nails_by_.adelina, 1.246 follower, nessun sito. Ha risposto «Ciaooo, ok» al primo DM del 17/9, bozza in costruzione dal 18/9.
- [[albybike]] — Negozio di biciclette - vendita, assistenza e riparazione, abbigliamento e integratori per ciclismo.
- [[bar-tabacchi-fiftynine]] — ⚠️ Bar tabaccheria e pizzeria in via Nazionale dei Giovi 59, Cesano Maderno (MB), telefono 0362 528451.
- [[cake-royal]] — Pasticceria cake design a Borgosatollo (BS), @cakeroyal.bs. Lead dal DM Instagram del 10/10/2026, bozza del sito in costruzione.
- [[castiglione-furniture]] — ⚠️ Falegnameria su misura, @castiglione_furniture su Instagram.
- [[claudia-dogsitter]] — ⚠️ Claudia, educatrice cinofila e dog sitter ad Azzano San Paolo (BG), @claudia_dogsitterbergamo. Ha risposto al DM l'08/10: «se vuoi mandarmela qui».
- [[custom-beauty-nails]] — Onicotecnica a Treviglio (BG), @custombeautynailstreviglio, 1.033 follower. Bozza online dal 16/9, il DM non e' ancora partito.
- [[davidemilan]] — Davide Milan, fotografo di diciottesimi e matrimoni, Milano, @davidemilan.ph. Il 05/10 ha risposto al DM: «Manda pure qui, sono curioso».
- [[design-capelli]] — Parrucchiere a Nichelino (TO), @designcapelli, 203 follower, dal 2015 in via XXV Aprile, nessun sito. Ha risposto «Buonasera qui grazie» al DM del 20/9. Bozza online su designcapelli.netlify.app dal 21/9, il DM col link e' di Patrick.
- [[dsi-advertising]] — ⚠️ D.S.I. Advertising di Piras Sebastiano, Merate (LC).
- [[edilida]] — Edilida SRL, impresa edile di Travagliato (BS). Ha compilato il modulo della ricerca il 18/09. Si punta a una videochiamata sulle scadenze di cantiere, mail di lunedì 21.
- [[il-salone-di-andrea]] — ⚠️ Parrucchiere donna e uomo di Andrea Bielli, Viale Natale Betelli 58, Dalmine.
- [[jpp-merate]] — Studio fotografico JPP (Just Pure Portraits), Merate, @jppmerate. Stefania ha risposto al DM il 05/10 e vuole una chiamata. Ha già una pagina Canva.
- [[laurafranzoni]] — Extension ciglia a Brescia, @laurafranzoni_lashmaker, 452 follower. Bozza online dal 14/9, il DM non è mai partito.
- [[lei-beauty-room]] — Centro estetico a Torino Cavoretto (via alla Parrocchia 4/c), @lei_beauty_room_, 671 follower, aperto dal 23/10/2025. Ha risposto «Grazie manda pure qui» al DM di Patrick del 24/9. Bozza in lavorazione, non ancora inviata.
- [[minniminerva]] — Minerva Esposito, MUA ad Alessandria, @minniminerva_make.up. Ha risposto al DM il 04/10 - curiosa, titubante sull'utilità. Bozza online: minervaesposito.netlify.app.
- [[mitril-tattoo]] — ⚠️ Mitril Tattoo & Piercing, piazza Don G. Racheli 6, Rovato (BS), @mitril_tattoo_studio, 11,4K follower. Ha chiesto la bozza nel DM il 09/10.
- [[ms-service]] — ⚠️ Lead caldo - ha chiesto lui il materiale.
- [[nails-mania]] — ⚠️ Centro di ricostruzione unghie mani e piedi di Lory Frosio, onicotecnica dal 2005.
- [[newfantasy]] — New Fantasy Parrucchieri, Lurate Caccivio (CO), @newfantasy_parrucchieri, 2.606 follower. Bozza online dal 16/9 su newfantasy-parrucchieri.netlify.app; il link va su WhatsApp, da Patrick.
- [[ng-barber]] — ⚠️ Barbershop, @ngbarberstudio123. Riga 2 dell'anello 1-b, gancio 5 - l'unico link in bio è ngbarber.my-booking-app.com, cioè un'app di prenotaz...
- [[p0t-tattoo]] — Ruben, tatuatore anime e cartoon (@p0t_tattoo, 307 follower) da K-Ink Studio Tattoo, via Adua 9b Collegno (TO). Ha risposto al DM del 24/09 - la bozza la vuole su Instagram.
- [[parrucchiere-morgan]] — Portato da Morgan il 15/9: espone volantini e biglietti e parla coi clienti in cambio del sito gratis, zero percentuali. Nome TODO.
- [[perunpelo]] — Ambra Longoni, groomer di Per un Pelo Toelettatura, Nembro (BG), @toelettatura.perunpelo. 5,0 su 102 su Google. Ha risposto al DM il 25/09 - vuole la bozza.
- [[petliving]] — Pet Living Toelettatura, Giussano (MB) + Bovisio Masciago, @petlivingtoelettatura. Ha risposto al DM il 30/09, vuole vedere qualcosa. Bozza in sito-petliving.
- [[pinkploy]] — Onicotecnica a Brescia centro, @nails_art_by_pinkploy, 832 follower. Bozza online dal 14/9, il secondo DM col link tocca a Patrick.
- [[sebastian-torres]] — Privato, non un'azienda. Sta aprendo la sua attività, e l'attività è opero - l'app che stiamo costruendo noi è la sua idea imprenditoriale.
- [[shaddai-extension-lash]] — Lash artist a domicilio a Bergamo, 736 follower, nessun sito - bozza costruita il 16 settembre 2026, DM non ancora inviato.
- [[shari-piras]] — ⚠️ Shari Piras, tatuatrice, Merate (LC). Due account - @shari_tattooer (4.504 follower, 493 post) è la persona, @atelierselva_ (593 follower, 41...
- [[soul-ink-torino-city]] — Soul Ink Torino City, studio di tatuaggi in via Cremona 27/b Torino (@soul_ink_torino_city, 738 post) - Franco Roggia (giapponese, dal 1999) e Alessandro Audino (tradizionale). Bozza in costruzione dal 26/09, DM non confermato.
- [[whitelilium]] — ⚠️ White Lilium Photography, fotografa maternity/newborn/famiglia a Trezzano sul Naviglio (MI). Lead Instagram del 05/10, ha risposto sì alla bozza il 07/10.

**contratti/**

- [[accordo-riservatezza-opero]] — Riservatezza + non concorrenza a 5 anni che Seba vuole far firmare (25/09/2026). Non firmato - cosa morde e la controproposta.
- [[contratti]] — ⚠️ Qui vanno gli accordi chiusi - cosa è stato promesso, a che prezzo, con quali tempi.

**liste/**

- [[2026-08-28-brianza-turni]] — ⚠️ Prima lista operativa. File - 2026-08-28-brianza-turni.csv, 51 contatti, pronto da importare in Google Sheets.
- [[2026-08-28-liste-31-agosto]] — ⚠️ Primo giro completo del ciclo-settimanale, generato con un giorno di anticipo.
- [[2026-08-28-presidi-volantini]] — ⚠️ Prima applicazione di presidi-volantini.
- [[2026-08-30-liste-gabriele-edoardo]] — ⚠️ Le 87 righe consegnate il 30 agosto 2026 a Gabriele ed Edoardo. Tornate vuote il 13 settembre: riassegnate a Giulia.
- [[2026-08-30-verifica-siti-giulia]] — ⚠️ Patrick il 30 agosto 2026 - *«ho preso in mano la lista di Giulia e già il primo era sbagliato, La Rustica ha un sito»*.
- [[2026-08-31-instagram-anello-1]] — ⚠️ 50 account, tutti verificati uno per uno il 31 agosto 2026.
- [[2026-09-01-instagram-anello-1-b]] — ⚠️ 50 account nuovi, tutti verificati uno per uno il 1 settembre 2026.
- [[2026-09-02-instagram-tattoo-wedding]] — ⚠️ 47 account nuovi, verificati uno per uno il 1 settembre 2026.
- [[2026-09-03-instagram-anello-1-2]] — ⚠️ 33 righe nuove, verificate una per una il 3 settembre 2026.
- [[2026-09-05-instagram-bg-va]] — ⚠️ 65 righe nuove, verificate una per una il 5 settembre 2026.
- [[2026-09-07-instagram-ticino]] — ⚠️ Due liste, una per account, perché dal 7 settembre il [banco DM](../strumenti/banco-dm.html) ha due postazioni - il profilo personale di Patr...
- [[2026-09-08-anello1-ristorazione]] — ⚠️ 68 righe, tutte per l'account personale di Patrick, appese a lista-corrente.csv che passa da 247 a 315 righe e da 170 a 238 da mandare.
- [[2026-09-09-anello1-pet]] — ⚠️ Settore nuovo, mai toccato in Lombardia - toelettature, asili e pensioni per cani, un centro cinofilo.
- [[2026-09-09-ristorazione-va-co-lc-bg]] — ⚠️ 64 righe sul banco (65 nel file - Da Bassano è rimasta dentro come SCARTATO), tutte per l'account personale di Patrick, appese a lista-corren...
- [[2026-09-10-animali-va-co-lc-bg-ti]] — ⚠️ 17 righe, tutte per l'account personale di Patrick, appese a lista-corrente.csv con la colonna Lista valorizzata.
- [[2026-09-10-siti-e-denkishift-va-co-lc-bg]] — ⚠️ Liste DM del 10 settembre - 50 profili senza sito piu' 30 per DenkiShift, VA CO LC BG, un messaggio per riga.
- [[2026-09-11-ricerca-mb-va-co]] — Prima lista della ricerca di mercato - 9 righe da 26 profili aperti, e la scoperta che Instagram non trova gli artigiani per comune.
- [[2026-09-11-tre-liste-brianza]] — Le tre liste dell'11 settembre - 43 siti e 43 DenkiShift sulla Brianza mai battuta, piu' 9 di ricerca di mercato.
- [[2026-09-12-cinquanta-per-tipologia]] — Le liste portate a 50 per tipologia - ricerca su tutta la Lombardia, siti su Milano, e i tatuatori che il sito ce l'hanno.
- [[2026-09-12-rilanci-lead-aperti]] — I sette lead aperti al 12 settembre, coi rilanci riscritti dopo aver letto le conversazioni intere e non l'ultimo messaggio.
- [[2026-09-13-liste-giulia-groane-vimercatese]] — Le 87 righe di Gabriele ed Edoardo riordinate per Giulia nello schema del ciclo: 27 siti, 30 DenkiShift, 30 indagine. Siti riverificati a macchina il 13/09.
- [[2026-09-13-tre-liste-settori-nuovi]] — Le tre liste del 13 settembre - 50 DenkiShift, 50 siti su Brescia, 41 ricerca - e i testi riscritti la sera coi due mesi gratis, i siti accorciati e il sito in tutti e tre.
- [[2026-09-14-denkishift-e-ricerca]] — Le due liste che stamattina mancavano - 50 DenkiShift e 50 ricerca di mercato, tutte in Lombardia - costruite dopo la bocciatura di Patrick sul 50-50-50.
- [[2026-09-14-lista-siti-bs-bg]] — La lista siti del 14 settembre - 43 righe su parrucchieri e barber fra Brescia e Bergamo da 99 profili aperti - e le due liste che non sono state fatte, col motivo.
- [[2026-09-14-rilanci-lead-aperti]] — I lead aperti al 14 settembre letti dalla posta intera - quattro bozze promesse e mai consegnate, una chiamata da fare oggi, e la seconda critica sull'AI in otto giorni.
- [[2026-09-15-rilanci-lead-aperti]] — I lead aperti al 15 settembre sera letti dalla posta intera - una bozza chiesta alle 21:14 che non esiste, un'email da mandare a Koinè, quattro bozze consegnate e zero chiamate fatte.
- [[2026-09-16-tre-liste-bergamo-lago-aziende]] — Le tre liste del 16 settembre - 51 siti sulla bellezza di Bergamo, 50 DenkiShift fra alberghi di lago e di montagna, 50 ricerca su concessionarie, arredo, ottici e immobiliari - e il modo nuovo di leggere i profili.
- [[2026-09-17-brianza-gestionali-1m]] — 100 aziende +1M di fatturato entro 10 km da Seveso per la campagna gestionali. File - 2026-09-17-brianza-gestionali-1m.csv, piu' 237 di riserva.
- [[2026-09-17-denkishift-e-ricerca]] — Le due liste che mancavano al 17 settembre - 50 DenkiShift e 50 ricerca di mercato in Lombardia - costruite col chaining di Instagram dopo che l'endpoint di ricerca si e' bloccato, e il difetto del banco che le faceva sembrare vuote.
- [[2026-09-17-rilanci-lead-aperti]] — I lead aperti al 17 settembre letti dalla posta - la bozza chiesta da Hair Style ferma da due giorni, l'email a Koine' mai partita, sette bozze consegnate e zero chiamate fatte, e 262 righe sul banco mai mandate.
- [[2026-09-17-siti-piemonte]] — La lista siti del 17 settembre - 50 righe di bellezza fra Torino e il resto del Piemonte, zona nuova aperta perche' la Lombardia della bellezza e' finita, e le toelettature abbandonate dopo 110 ricerche.
- [[2026-09-19-denkishift-e-ricerca]] — Le due liste che erano state saltate il 19 settembre - 50 DenkiShift e 50 ricerca in Lombardia - costruite col chaining dopo il terzo errore uguale in quattro giorni, e la scusa che non vale.
- [[2026-09-19-siti-piemonte-capelli]] — La lista siti del 19 settembre - 50 parrucchieri e barber del Piemonte, secondo settore della zona dopo la bellezza del 17 - e la posta che dice che i DM non escono dall'account di Patrick.
- [[2026-09-21-tre-liste]] — Le tre liste del 21 settembre - 50 studi di tatuaggi del Piemonte, 50 DenkiShift e 50 ricerca in Lombardia - e la ricerca di Instagram che si e' bloccata due volte in mezza giornata.
- [[2026-09-23-tre-liste]] — Le tre liste del 23 settembre - 50 fotografi e truccatrici sposa del Piemonte, 50 birrifici, lidi e hotel di citta' per DenkiShift, 50 aziende artigiane per la ricerca - e i fotografi che il sito ce l'hanno nel 65% dei casi.
- [[2026-09-25-barbieri-piemonte-e-ricerca]] — Le due liste del 25 settembre - 101 barbieri del Piemonte e 62 aziende lombarde per la ricerca - costruite con Google e Pagine Gialle dopo il blocco di Instagram.
- [[2026-09-25-opero-facchinaggio-allestimento]] — 100 aziende di facchinaggio e allestimento per le chiamate di Seba su OperO, da Seveso verso fuori (0,8-55 km), fatturato 250k-10M. Piu' 213 senza numero.
- [[2026-09-25-opero-facchinaggio]] — 100 aziende di solo facchinaggio per Seba su OperO, da Seveso a Firenze (9,8-265 km), fatturato 250k-10M. 29 gia' nella lista mista. Piu' 149 senza numero.
- [[2026-09-29-ciglia-piemonte-e-ricerca]] — Liste del 29/9 - 100 tecniche di ciglia e sopracciglia del Piemonte, 60 aziende lombarde per la ricerca. Google su ogni riga siti.
- [[2026-09-30-siti-e-ricerca-mb-co-lc-mi]] — Liste del 29-30/9, prime con la regola dei luoghi: 100 siti da MB, CO, LC e MI senza bellezza, 61 ricerca da MB e CO. Resa e trappole.
- [[2026-10-02-siti-e-ricerca-mi-bs-lc-co]] — Per Patrick - il /banco lasciato a meta' l'1/10 finito da Nicola il 2/10: 144 righe sul banco (siti 86, ricerca 58), cosa guardare prima di mandare
- [[2026-10-05-siti-e-ricerca-mi-bg-bs-lc]] — Per Patrick - il /banco del 5/10 finito il 6/10, 160 righe sul banco (siti 100, ricerca 60) da 11 celle, cosa guardare prima di mandare
- [[2026-10-07-siti-e-ricerca-bs-mi-lc-lo]] — Per Patrick - il /banco del 7/10 finito l'8/10, 117 righe sul banco (siti 68, ricerca 49) da 11 celle, cosa guardare prima di mandare
- [[2026-10-09-siti-e-ricerca-co-lc-bs-mi]] — Per Patrick - il /banco del 9/10 finito il 10/10, siti 100 e ricerca 60 da 20 celle, cosa guardare prima di mandare
- [[2026-10-10-siti-e-ricerca-no-mi-pc-co]] — Per Patrick - il /banco del 10/10, siti 94 e ricerca 60 da 16 celle, cosa guardare prima di mandare
- [[contattati]] — ⚠️ Due CSV, scritti dal banco e non a mano.
- [[metodo-instagram]] — ⚠️ Serve a produrre, ogni giorno, fino a 65 account Instagram verificati a cui Patrick può scrivere il messaggio di dm-instagram-vetrina senza...
- [[metodo-liste]] — ⚠️ Come si costruisce una lista - il sito si verifica aprendolo, mai dedotto da Pagine Gialle.
- [[metodo-nuove-aperture]] — ⚠️ Tre differenze rispetto a una lista normale di metodo-instagram, e la terza è quella che conta -

**processo/**

- [[bozze-social-2026-10-03]] — ⚠️ Bozze del 03/10/2026 - sei storie linea siti (Come funziona, Cose che succedono) e la linea gestionali del brief Sarto - analisi, calendario, due post, quattro sequenze. Da rileggere Nicola, poi Patrick.
- [[brief-social-sarto]] — Brief di Nicola del 03/10/2026 per post e storie «Sarto del Software» - contrasto con i gestionali standard, tre tipi di post, storie in sequenze da 3, storie Relatable. Verbatim, con i punti che urtano le regole esistenti.
- [[canali-indiretti]] — Chi vende al posto vostro - caller, agenzie a performance, rivenditori. Prezzi al 13/9/2026. Primo segnalatore in casa: Morgan, 15/9.
- [[ciclo-settimanale]] — Dettato da Patrick il 28 agosto 2026. È il processo fisso.
- [[core-commerciale]] — Consultazione, non obbligo. I framework con cui si costruisce un testo commerciale.
- [[didascalie-instagram]] — ⚠️ Testi pronti da copiare per le prime due settimane del piano Instagram - slide dei caroselli, righe dei Reel, didascalie e hashtag.
- [[flusso-vendita]] — I quattro flussi di vendita e lo Straight Line - come un lead arriva alla chiusura.
- [[generazione-lead]] — Il collo di bottiglia dell'azienda - da dove arrivano i lead e quanti ne servono.
- [[materiale-offline]] — Quello che abbiamo di fisico, e a cosa è agganciato.
- [[materiale-social]] — I post e le storie Instagram di DenkiCode - cosa e' uscito, con che testo, e dove stanno i file e il sorgente per rifarli.
- [[piano-instagram]] — ⚠️ Cosa pubblica @denkicode, quanto, quando, con che didascalie e hashtag. Deciso da Trevis il 30/09/2026 su delega di Patrick, si rivede a 4 settimane.
- [[presidi-volantini]] — ⚠️ Terzo canale, deciso il 28/8/2026. Primo presidio vero il 15/9/2026: un parrucchiere via Morgan, pagato col sito gratis, non a risultato.
- [[prodotti-e-listino]] — I quattro prodotti e i prezzi. I prezzi sono indicativi - l'aggancio, non la cifra finale.
- [[ricerca-instagram]] — ⚠️ Come funziona Instagram al 30/09/2026 per un profilo piccolo - algoritmo, orari, hashtag, didascalie, API - e chi vende siti su Instagram. Con le fonti.
- [[ricerca-storie]] — ⚠️ Ricerca del 03/10/2026 sulle storie Instagram di chi vende siti a piccole attivita, Italia ed estero - schemi che rendono, cosa evitare, fonti 2025-26. Storie non viste: solo highlights e feed da fuori.
- [[stile-comunicazione]] — Il registro dei testi che legge un cliente - Lei o Tu, voce di Patrick. Non e' il registro di Trevis.

**report/**

- [[2026-09-12-posta-dm-primo-resoconto]] — Primo resoconto della posta Instagram - 490 DM in sei giorni, 5,8% di risposte vere, sette trattative aperte e ferme.
- [[metriche]] — I numeri del funnel con la data accanto. Un numero senza data non e' una metrica.

**script/**

- [[briefing-prodotti-gabriele-edoardo]] — ⚠️ Serve a dare ai due nuovi cold caller la certezza sul prodotto - il primo dei tre Dieci di Belfort (flusso-vendita).
- [[dm-instagram-denkishift]] — ⚠️ Il DM Instagram per DenkiShift - come si scrive, e perche' si scrive uno per profilo invece di un modello.
- [[dm-instagram-ricerca]] — Il DM Instagram della ricerca di mercato - qui non si vende niente, si chiede il modulo, e chi risponde si qualifica da solo.
- [[dm-instagram-vetrina]] — ⚠️ Lo manda Patrick, dal suo account personale.
- [[email-centralino-rsa]] — ⚠️ Il caso. Su molte RSA la chiamata di Giulia non arriva al decisore - risponde un centralino che non passa nessuno e lascia un indirizzo mail.
- [[email-presentazione-denkishift]] — ⚠️ Il testo che accompagna la presentazione (presentazione-denkishift-ms-service.pptx, 8 slide) quando un contatto chiede materiale via mail in...
- [[obiezione-non-sapranno-usarlo]] — ⚠️ Framework - Belfort — looping sul primo dei 3 Dieci (la certezza nel prodotto), con l'isolamento di Blount in chiusura.
- [[pattern-interrupt]] — ⚠️ Le aperture - come si rompe lo schema nei primi sette secondi di una chiamata a freddo.
- [[script-denkishift]] — ⚠️ Lo script telefonico di Giulia su DenkiShift, con le obiezioni e i looping.
- [[script-ecommerce]] — ⚠️ Lo usano tutti e tre. Dove c'è [nome] ci va il proprio.
- [[script-gestionali-brianza]] — ⚠️ Lo script di Patrick sulle 100 aziende +1M della Brianza. Qui si vende - l'obiettivo e' l'appuntamento conoscitivo, non il modulo.
- [[script-indagine]] — ⚠️ Lo usano tutti e tre. Dove c'è [nome] ci va il proprio.
- [[script-siti-vetrina]] — ⚠️ Lo usa Giulia, unica al telefono dal 15/09/2026.

## 03-Storage

*Azienda, team, sistemi*


**azienda/**

- [[core-crescita-finanze]] — Consultazione, non obbligo. Equazione del valore, garanzia invece dello sconto, Incassi meno Utile uguale Spese.
- [[core-produttivita-leadership]] — Consultazione, non obbligo. Blocchi di tempo, gesto giornaliero minimo, l'errore di guida prima dell'esterno.
- [[core-strutturale]] — Consultazione, non obbligo. SOP delegabili, versione minima, servizi a pacchetto.
- [[obiettivi-6-mesi]] — Tre traguardi. Sono di Nicola, testuali, non miei.
- [[protocollo-trevis]] — Il livello base di Trevis - postura commerciale, priorità, i quattro vincoli duri e l'indirizzario del vault.
- [[registro-trevis]] — Come Trevis parla a Nicola, Patrick e Giulia - postura, formule vietate, continuita', otto righe.
- [[stato-azienda]] — Fotografia al 28 agosto 2026. Da rileggere e aggiornare ogni mese - i numeri qui dentro invecchiano in fretta.
- [[vincoli-fiscali]] — Prestazione occasionale, nessuna P.IVA. Nei testi 'ricevuta', mai 'fattura elettronica'.

**brand/**

- [[identita-visiva]] — ⚠️ I file vettoriali e i sorgenti di stampa di DenkiCode, portati nel vault il 28 agosto 2026 da ~/Desktop/denki-pubblicità sul Mac di Patrick,...

**sistemi/**

- [[agente-operatore]] — Copia canonica di ~/.claude/agents/operatore.md - il subagente Opus che scrive il codice deciso dal direttore.
- [[claude-md-globale]] — Copia canonica di ~/.claude/CLAUDE.md - il protocollo Trevis che va ricreato a mano su ogni macchina nuova.
- [[come-si-scrive-una-nota]] — Le regole di scrittura del vault - riga, verificato, marcatura per affermazione, tre classi di memoria, tetti di lunghezza.
- [[credenziali]] — ⚠️ Dove stanno le chiavi e come si passano. Nessun valore e' scritto qui, e non lo sara' mai.
- [[modifiche-al-database]] — ⚠️ Come Patrick applica una modifica allo schema di DenkiShift in sviluppo. La produzione resta fuori.
- [[patrick-modifica-denkishift]] — ⚠️ Guida passo passo, scritta per chi non scrive codice.
- [[plugin-claude-code]] — ⚠️ Due meccanismi diversi, che si confondono facilmente -

**team/**

- [[gabriele-edoardo]] — Fuori in via definitiva dal 15/9/2026. Il 13 avevano detto che non se la sentono: zero chiamate in 14 giorni. Liste passate a Giulia.
- [[morgan]] — Fratello di Patrick, dentro dal 15/9/2026. Non chiama, porta conoscenze: primo frutto un parrucchiere-presidio. Compenso e ore TODO.
- [[ruoli-e-responsabilita]] — Quattro persone dal 15/9/2026. Sotto, chi fa cosa davvero — non i titoli.
- [[setup-macchina-nuova]] — Scritto per il MacBook Air di Patrick, ma vale per qualunque macchina nuova.
- [[team-e-vincoli]] — Quante ore ci sono davvero - Patrick, Nicola e Giulia lavorano e studiano, DenkiCode e' il terzo impegno. Morgan (15/9): TODO.

## 05-Decisioni

*Una decisione per file, datata. Non si riscrivono*

- [[2026-08-11-opero-scope-allargato]] — opero nasce come ricostruzione pulita di sebapp-bolanos, l'app che il cliente usa già in produzione.
- [[2026-08-22-xml-sdi-da-quotare]] — opero, insieme all'area Direzione. Decisione sua.
- [[2026-08-28-ciclo-settimanale]] — Fino a oggi le liste si producevano quando Patrick trovava il tempo, e quello che tornava indietro dalle chiamate non tornava indietro affat...
- [[2026-08-28-core-commerciale]] — Decisione di Patrick. Da oggi ogni script, ogni obiezione smontata e ogni analisi dei report settimanali si costruisce applicando i testi ra...
- [[2026-08-28-domini-a-scadenza]] — I domini si comprano a ~1 € con l'offerta promozionale del primo anno.
- [[2026-08-28-protocollo-jarvis]] — Decisione di Nicola. Da oggi l'assistente si chiama Trevis e opera su un protocollo base — protocollo-trevis — attivo a ogni avvio, in ogni...
- [[2026-08-28-push-automatico]] — Deciso da Patrick il 28 agosto 2026. Parole sue - ogni volta che si cambia qualcosa nel vault, anche minima, si pusha su git — da qualunque d...
- [[2026-08-28-registro-interventi]] — Decisione di Nicola. Dal 28 agosto 2026 ogni modifica a un progetto va in due posti - nel repository del progetto, e in registro-interventi —...
- [[2026-08-28-registro-jarvis]] — Decisione - la postura con cui l'assistente parla a Nicola, Patrick e Giulia sta in un file solo — registro-trevis — e ogni comando del vault...
- [[2026-08-28-stack-non-uniforme]] — ⚠️ Al 28 agosto 2026, DenkiCode ha cinque basi di codice e cinque stack -
- [[2026-08-28-supabase-denkishift-sul-mac]] — Chiesto da Patrick il 28 agosto 2026, poche ore dopo la decisione di far pushare git da quella macchina (2026-08-28-push-automatico).
- [[2026-08-29-architettura-interfaccia-denkishift]] — ⚠️ Il ragionamento completo sta in denkishift-interfaccia.
- [[2026-08-30-core-crescita-finanze]] — Decisione di Patrick, lo stesso giorno del 2026-08-30-core-strutturale.
- [[2026-08-30-core-produttivita-leadership]] — Decisione di Patrick, terza della stessa giornata dopo 2026-08-30-core-strutturale e 2026-08-30-core-crescita-finanze.
- [[2026-08-30-core-strutturale]] — Decisione di Patrick. Da oggi ogni operazione, ogni funzione nuova e ogni servizio si guardano attraverso i tre testi raccolti in core-strut...
- [[2026-08-30-nome-trevis]] — Deciso da Patrick il 30 agosto 2026, con queste parole - *«da adesso in poi ovunque e sempre ti chiamerai trevis»*.
- [[2026-08-30-verifica-sito-reale]] — Deciso da Patrick il 30 agosto 2026, dopo aver preso in mano la lista di Giulia e trovato l'errore alla prima riga - *«se dici che il sito no...
- [[2026-08-31-canale-dm-instagram]] — Deciso da Patrick il 31 agosto 2026, insieme alla chiusura del porta-a-porta (2026-08-31-stop-porta-a-porta-a-freddo).
- [[2026-08-31-stop-porta-a-porta-a-freddo]] — Deciso da Patrick il 31 agosto 2026 - *«io o Patrick che vado dal vivo senza prima una chiamata - mi occupa troppo tempo e mi risulta inutile»...
- [[2026-09-01-skill-design-processo-siti]] — ⚠️ Decisione. Da oggi ogni sito vetrina/landing/portfolio parte dalla skill processo-siti (~/.claude/skills/, sul PC di Nicola), che mette in f...
- [[2026-09-02-automazione-dm-instagram]] — ⚠️ Chiesto da Nicola per Patrick, il 2 settembre 2026 - rendere automatico e più veloce il contatto dei possibili clienti dai messaggi diretti d...
- [[2026-09-02-cold-email-gestionali]] — Chiesto da Nicola il 2 settembre e da Patrick il 13 - l'invio si automatizza tutto, ma su 566 righe di banco solo 2 sono scrivibili per legge.
- [[2026-09-02-impostazioni-due-colonne]] — ⚠️ Chiesta da Nicola il 2 settembre 2026 con un brief esplicito - «i testi sono infantilizzati, poco professionali e strutturati male, e da desk...
- [[2026-09-03-bozza-gia-fatta]] — ⚠️ Chiesta da Nicola il 3 settembre 2026, insieme all'installazione del banco DM sul MacBook di Patrick.
- [[2026-09-03-gh-crea-repository]] — ⚠️ Decisione di Nicola, 3 settembre 2026 - «voglio impostare che da adesso tu possa creare le mie repository».
- [[2026-09-03-tetto-dm-65]] — ⚠️ Superata l'11/09/2026 (Patrick, «togli il limite giornaliero» → metodo-liste). Il 3/09 Nicola aveva fissato 65 DM al giorno, misurati.
- [[2026-09-06-mac-nicola-in-lavoro]] — ⚠️ Decisione di Nicola, 6 settembre 2026 - messa in piedi da zero una seconda macchina sua, un MacBook Pro, e tutto sta in ~/lavoro — vault e re...
- [[2026-09-06-sito-salone-andrea-direzione]] — ⚠️ Decisione. Sul sito di sito-salone-di-andrea il concept-seed di impeccable (seed e5bd3d89) aveva assegnato «Il rullo» - un fotogramma a scher...
- [[2026-09-06-skill-voce-denkicode]] — ⚠️ Il fatto. Un lead, angolorelax_nembro, ha risposto a un DM Instagram scritto da Claude per conto di Patrick dicendo, testuale - *'è un banale...
- [[2026-09-07-due-account-dm]] — ⚠️ Chiesto da Patrick il 7 settembre 2026. I DM non partono più solo dal suo profilo personale - il banco ha un selettore con Patrick Sappa e De...
- [[2026-09-07-indice-generato]] — ⚠️ Decisione. indice.md smette di essere una nota scritta a mano.
- [[2026-09-07-trappole-memoria-tecnica]] — ⚠️ Decisione di Nicola, 7 settembre 2026 - le note di giornata funzionano, quindi le uso anche per parlare con me stesso da una sessione all'alt...
- [[2026-09-08-firma-powered-by-denkicode]] — ⚠️ Decisione. Nicola, 8 settembre 2026. Ogni cosa che esce da qui — siti vetrina, e-commerce, gestionali — porta nel piè di pagina la scritta P...
- [[2026-09-08-test-dm-chiuso]] — I numeri veri li ha dati Patrick l'8 settembre 2026, a voce.
- [[2026-09-10-direttore-operatore]] — Da adesso i siti si fanno con starter, essenza del cliente e metafora sola, e il direttore non scrive codice - lo scrive l'operatore su Opus.
- [[2026-09-10-liste-50-30-messaggi-personalizzati]] — Ogni lista DM e' 50 siti piu' 30 DenkiShift, e ogni riga porta il suo messaggio scritto a mano.
- [[2026-09-10-memoria-verificata]] — Il brain smette di leggersi addosso - riga obbligatoria, verificato, tre classi di memoria, core non piu' obbligatori.
- [[2026-09-11-brain-autonomo]] — Il brain si chiude, promuove, pusha e controlla i siti da solo, perche' Patrick non sa fare niente di tutto questo.
- [[2026-09-11-comando-banco]] — /banco apre il banco DM e costruisce le tre liste del giorno; cinque pagine, annulla l'ultimo, e per i siti la bozza si annuncia gia' fatta.
- [[2026-09-11-direzione-da-chi-ha-letto]] — La direzione di un sito la propone un operatore che ha letto le skill, non il direttore. Scroll-telling e grafica inventata obbligatori.
- [[2026-09-11-niente-note-di-fonte-in-pagina]] — ⚠️ Sul sito non si scrivono note di fonte: le fonti restano nei documenti interni, la pagina dice il fatto.
- [[2026-09-13-caller-fuori]] — Gabriele ed Edoardo si ritirano senza aver chiamato nessuno: il telefono resta su Giulia sola e le 87 righe passano a lei.
- [[2026-09-14-denki-agents-parte-dal-gateway]] — denki-agents parte dal gateway verso i modelli - modello, prezzo e tetto di ogni task nel database, mai nel codice.
- [[2026-09-15-morgan-entra-parrucchiere-presidio]] — Edo e Gabriele fuori per sempre. Entra Morgan (fratello di Patrick): non chiama, segnala. Primo frutto un parrucchiere pagato col sito.
- [[2026-09-16-cervello-denki-agents]] — Il cervello di denki-agents - memoria, regista e fermate umane in un Postgres solo con pgvector, e il prompt si compone a budget.
- [[2026-09-16-denki-agents-prima-i-siti]] — ⚠️ In denki-agents prima la parte che fa i siti - Nicola ci sposta la produzione e ne descrive il flusso, dal login alla chat per progetto.
- [[2026-09-16-vbag-gestionale-login]] — ⚠️ V-BAG - il gestionale di Giulia ha un login vero e pubblica dal telefono via Netlify Function + commit su GitHub. Store a file confermato.
- [[2026-09-17-cantiere-un-dollaro-in-locale]] — ⚠️ Il cantiere di denki-agents costa al massimo un dollaro a sito, gira in locale, raccoglie le foto da Instagram in automatico.
- [[2026-09-23-fiftynine-archivio-netlify]] — ⚠️ Fiftynine - le modifiche della pagina di modifica vanno in Netlify Blobs, senza chiavi, e una edge function le rimette nelle pagine; parola iniziale admin, si cambia dalla pagina.
- [[2026-09-23-fiftynine-pubblica-da-solo]] — ⚠️ Fiftynine - la pagina di modifica pubblica da sola come V-BAG (Netlify Function + commit su GitHub), ma in un commit solo e con la parola d'ordine in sessionStorage.
- [[2026-09-27-daily-abolita]] — Le daily non si scrivono più - la giornata sta nel registro interventi, lo stato in FATTI sotto le 80 righe. Approvata da Nicola il 27/09/2026.
- [[2026-09-27-verificato-in-chiusura]] — verificato lo scrive /chiudi-sessione sulle note toccate in sessione che Nicola o Patrick approvano. 109 note su 246 erano ipotesi. 27/09/2026.
- [[2026-09-30-instagram-pubblicazione-api]] — Post e storie di DenkiCode li pubblica uno script con l'API ufficiale di Instagram. Deciso da Patrick il 30/09/2026, tocca a Nicola.
- [[2026-10-01-banco-ricircolo]] — /banco riscritto l'1 ottobre - perche' la lista non usciva al primo colpo, il piano del giorno lo stampa uno script, Patrick non lancia piu' niente, e la resa misurata dei DM.
- [[2026-10-01-coopero-prototipo]] — ⚠️ Prototipo di CO-OPERO chiesto da Nicola il 1/10 - quattro scelte tecniche proposte da Claude, in attesa del suo verdetto. Niente pubblicato.
- [[2026-10-11-banco-online]] — ⚠️ Il banco DM esce dal Mac di Patrick e va online su Netlify - stato in Blobs, login, giro ogni 30 minuti che riporta contattati.csv nel vault.

## 06-Daily

*Note di giornata, chiuse il 27/09/2026: storia, la giornata sta nel registro*

- [[2026-08-28-avvio-vault]] — ⚠️ Prima nota del vault. Scritta da Claude a fine costruzione, per lasciare un punto di partenza invece di una cartella muta.
- [[2026-08-29-interfaccia-denkishift]] — ⚠️ Richiesta arrivata in sessione - rifare l'interfaccia perché si venda da sola in demo, su due utenti che non sono due gradini dello stesso ru...
- [[2026-08-30-sito-castiglione]] — ⚠️ Primo uso vero dello scraper Instagram di Apify agganciato a Claude Code - profilo e 20 post di @castiglione_furniture (Castiglione Falegname...
- [[2026-09-03-sito-dsi]] — ⚠️ Sera del 2 e notte del 3 - sito vetrina per D.S.I.
- [[2026-09-05-lista-instagram-65]] — ⚠️ Un blocco solo, chiesto da Patrick - «crea i 65 dm di oggi in banco dm».
- [[2026-09-06-sito-salone-di-andrea]] — ⚠️ Un blocco solo, chiesto da Nicola in /nicola - «nuovo progetto - sito per l'account Instagram ilsalonediandrea, come al solito, seguendo il pr...
- [[2026-09-07-sito-nails-mania]] — ⚠️ Sessione a cavallo della mezzanotte, in /nicola.
- [[2026-09-08-sito-fiftynine-foto-e-admin]] — ⚠️ Nicola ha portato una chiavetta («NO NAME») con il materiale del proprietario del sito-fiftynine e ha chiesto due cose - usare quelle foto al...
- [[2026-09-08-sito-tarilli]] — ⚠️ Nicola ha chiesto un sito per «pizzeria Tarilli, cercali su Instagram», con «un sacco di animazioni» e «pizze che si muovono e fluttuano».
- [[2026-09-09-sito-albybike-motion]] — ⚠️ Nicola, dal suo Mac - «riprendi questa conversazione su questo pc», e il compito di ieri sera dal Mac di Patrick - «rendi ancora più bello, co...
- [[2026-09-09-sito-da-caterina]] — ⚠️ Nicola, dal Mac, in /nicola - «nuovo sito vetrina per questo account Instagram - dacaterinatoelettatura.
- [[2026-09-13-sito-nails-robyy]] — ⚠️ Bozza nails.robyy costruita col processo intero e messa online - mondo «la sezione quotata», 8/8, due regressioni chiuse all'ultimo.

## 04-Archive

*Progetti chiusi e lead persi*

- [[cococat]] — Sito vetrina in una pagina per cococat caffè, bar in via Piero Caldirola 5, Milano (Bicocca) - caffetteria, bubble tea, street food cinese, a...
- [[sito-dropout]] — Non è un cliente e non è un lavoro DenkiCode.
- [[webolt-v1]] — Repo - github.com/Nixo999/WeBolt-v1 — creato il 23 marzo 2026.

## 99-Templates

*Da copiare quando si crea una nota nuova*

- [[template-cliente]] — Modello per una scheda cliente - rapporto, conto economico, consegnato, come si comporta.
- [[template-daily]] — Max 40 righe, questo file compreso. Il contenuto sono le risposte di chi ha lavorato, raccolte da /chiudi-sessione con cinque domande.
- [[template-decisione]] — Modello per una decisione datata - contesto, scelta, cosa si e' scartato, conseguenze.
- [[template-progetto]] — Modello per una nota progetto - stato, soldi, decisioni prese, cosa resta aperto.
- [[template-report-settimanale]] — ⚠️ Cosa si consegna la domenica: tre CSV di Giulia piu' il modulo blitz di Patrick.
