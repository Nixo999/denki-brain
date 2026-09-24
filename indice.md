---
type: risorsa
updated: 2026-09-25
source: claude
tags: [indice]
---

# Indice delle note — si legge prima di cercare

Tutte le **234 note** del vault, per cartella, con una riga a testa. Serve a un
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

- [[come-si-usa-inbox]] — ⚠️ Questa cartella è il posto dove buttare le cose senza pensarci.

## 01-Coding

*Il lato tecnico: progetti, stack, strumenti, skill*

- [[registro-interventi]] — Una riga per intervento - chi, quando, progetto, repository e QUALE DATABASE. La colonna database e' il motivo del file.
- [[trappole]] — Errori tecnici già pagati e strade scartate, per dominio. Descrittivo, non è un rulebook - le regole stanno in convenzioni.

**progetti/**

- [[denki-agents]] — Piattaforma interna multi-agente - ogni task sul suo modello via LiteLLM, costo di ogni chiamata in Postgres. Fase 1: solo il gateway.
- [[denkishift-interfaccia]] — ⚠️ Obiettivo dichiarato - un'interfaccia che si venda da sola durante la demo di Patrick, calibrata su due utenti che non sono due gradini dello...
- [[denkishift]] — Prodotto di punta, turni per squadre a orario variabile. Dimostrabile, NON installabile in produzione.
- [[opero-intermediar-receive-testo]] — Testo integrale della specifica Intermediar + Receive mandata da Seba il 24/09/2026. La fonte: la sintesi sta in opero-intermediar-receive.
- [[opero-intermediar-receive]] — ⚠️ Intermediar + Receive, il prossimo pezzo di OperO chiesto da Seba il 24/09 - da conoscere, non da fare. Principi, demo minima, buchi della specifica.
- [[opero]] — Il prodotto che Sebastian rivende, non un gestionale nostro. Chi tocca il Super Admin tocca il suo conto economico.
- [[sito-adelinanails]] — Bozza sito per Adelina Nails (Alessandria) in ~/lavoro/adelinanails-site - contenuto solo da profilo + inventario competitor, giro 3 «lacca, oro e rilievo», Melodrama + Grape Nuts, apertura in 4 tempi, 8/8 - online su adelinanails-site.netlify.app dal 19/9 (deploy da GitHub).
- [[sito-albybike]] — Sito vetrina per Albybike, negozio di biciclette - vendita, assistenza, riparazione, abbigliamento e integratori.
- [[sito-atelier-selva]] — ⚠️ Sito per Shari Piras, tatuatrice fineline a Merate (LC), e per il suo studio privato Atelier Selva (Via Statale 147).
- [[sito-barbershop-snia]] — Sito vetrina di Andrea, barbiere al Villaggio SNIA di Cesano Maderno, che fa anche da tramite per i trapianti in Albania. Primo presidio volantini, gratis.
- [[sito-castiglione]] — ⚠️ Sito vetrina non commissionato per castiglione-furniture, costruito il 30 agosto 2026 dai contenuti veri del loro profilo Instagram.
- [[sito-custombeautynails]] — Custom Beauty Nails, onicotecnica a Treviglio (BG): bozza online su custombeautynails.netlify.app dal 16/9, mondo «Un centimetro di spazio», 21 SVG, 8/8, copy rifatto professionale dopo la bocciatura.
- [[sito-da-caterina]] — ⚠️ Da Caterina Toelettatura Professionale, Via Introzzi 8, 21057 Olgiate Olona (VA).
- [[sito-denkicode]] — Sito di DenkiCode. È qui che sta la galleria dei lavori - il posto dove si mostra a un cliente cosa abbiamo già fatto.
- [[sito-designcapelli]] — Bozza sito per Design Capelli (Nichelino, TO) - mondo «la luce della via», la pagina schiarisce di un tono a sezione, marchio composto in Pinyon Script, Cabinet Grotesk + Gambetta, apertura a 0,80 s. Online su designcapelli.netlify.app dal 21/9, giro 6, 8/8, slop 0 e testo 0.
- [[sito-dianails]] — Diana @dianails_brescia, onicotecnica e PMU a Brescia: bozza creata in C:\Users\User\Desktop\dianails-site, mondo A «la regola del 90°», 8/8 sbarramenti verificati.
- [[sito-dragonfly]] — ⚠️ Raccolta materiale per sito vetrina di Dragonfly Beauty&Relax, centro estetico a Casale Monferrato, lead da Instagram.
- [[sito-dsi-advertising]] — ⚠️ Sito vetrina in una pagina per D.S.I. Advertising di Piras Sebastiano, Merate (LC) - dal 1992 progetta e produce articoli promozionali per il...
- [[sito-fiftynine]] — ⚠️ Sito vetrina in una pagina per Bar Tabacchi Fiftynine, bar tabaccheria e pizzeria in via Nazionale dei Giovi 59, Cesano Maderno (MB).
- [[sito-hairstylebrescia]] — Hair Style Parrucchieri @hairstyle_brescia, salone a Brescia, gancio sposa - bozza online su hairstylebrescia.netlify.app dal 16/9, mondo A «La prova», 8/8, DM non partito.
- [[sito-laurafranzoni]] — Laura Franzoni @laurafranzoni_lashmaker, ciglia a Brescia: bozza online su laurafranzoni.netlify.app dal 14/9, mondo «Dall'alto». Online c'è il giro 2, il giro 3 è fermo in locale.
- [[sito-leibeautyroom]] — Bozza sito per Lei Beauty Room (Torino Cavoretto) - mondo «La stanza», l'arco del logo è la porta. Online su leibeautyroom.netlify.app, giro 5: sul telefono cinque porte diverse con tre foto vere da Google e Instagram, 8/8.
- [[sito-mikuma-dogs]] — Online su mikumadogs.netlify.app per Martina Carneli (mikuma.dogs), Como - giro 7 'il bianco e il nero', logo vero, Nicola: 'mi piace molto'.
- [[sito-nails-mania]] — ⚠️ Sito vetrina in una pagina per Nails Mania, centro di ricostruzione unghie mani e piedi di Lory Frosio a Seriate (BG).
- [[sito-nails-robyy]] — Roberta @nails.robyy, nail artist e educator a Brescia: bozza online su nailsrobyy.netlify.app dal 14/9, mondo A «la sezione quotata», 8/8, sbarramenti verificati.
- [[sito-newfantasy]] — New Fantasy Parrucchieri @newfantasy_parrucchieri, Lurate Caccivio (CO): bozza online su newfantasy-parrucchieri.netlify.app dal 16/9, mondo B «l'agenda a tre colonne», prenotazioni e gestionale su localStorage.
- [[sito-ngbarber]] — ⚠️ Bozza vetrina per ng-barber, riga 2 dell'anello 1-b delle liste Instagram, gancio 5.
- [[sito-osteria-tarilli]] — ⚠️ Osteria Tarilli, Via Ronco Nuovo 2, 6949 Comano (TI), a 300 m dalla RSI.
- [[sito-p0t-tattoo]] — Bozza sito per p0t_tattoo (Ruben, tatuatore anime e cartoon, Collegno TO) - mondo «Rodovetro × Retino», linea → puntinato → colore, Unbounded + Hanken Grotesk. Online su p0t-tattoo.netlify.app dal 24/9, giro 6 (meno macchinoso, mobile per primo), 8/8, slop 0, testo 0.
- [[sito-pinkploy]] — Online su pinkploy.netlify.app per @nails_art_by_pinkploy, onicotecnica a Brescia centro - mondo B «lo spessore», l'unghia in quota.
- [[sito-pizzeria-lobidu]] — ⚠️ Pizzeria Lobidù, pizzeria siciliana, Via IV Novembre 13, 21049 Tradate (VA).
- [[sito-salone-di-andrea]] — ⚠️ Sito vetrina in una pagina per Il Salone di Andrea, parrucchiere donna e uomo di Andrea Bielli a Dalmine (BG), Viale Natale Betelli 58.
- [[sito-shaddai]] — Bozza di sito vetrina non commissionata per Shaddai Extension Lash, lash artist a Bergamo, costruita il 16 settembre 2026 dai contenuti veri del profilo Instagram.

**skills/**

- [[design-frontend]] — ⚠️ Quattro skill di design sono installate a livello di account (~/.claude/skills/), quindi valgono in ogni cartella - OperO, DenkiShift, cococa...
- [[processo-siti]] — ⚠️ Nota di catalogo, non la skill. È il wikilink più citato del vault (quindici richiami e nessun file, fino al 7 settembre 2026) perché ogni s...
- [[skills]] — ⚠️ Quale strumento di Claude si usa per quale lavoro.

**stack/**

- [[anti-slop-siti]] — ⚠️ Cosa fa sembrare un sito fatto con l'AI, dalla ricerca del 17/09/2026 - segni visivi e di testo, cosa blocca controlla-slop, cosa va guardato.
- [[competitor-siti-barber]] — ⚠️ Inventario di 15 siti (6 barber Brianza, 5 barbershop italiani noti, 4 trapianto Albania) per il sito di Barbershop SNIA (Cesano Maderno).
- [[competitor-siti-estetica]] — ⚠️ 18 siti di centri estetici (5 locali AL/VC/AT, 5 boutique italiane, 3 specialistici, 5 Torino collina) - sezioni, info reali, stile, per Dragonfly e Lei Beauty Room.
- [[competitor-siti-nail]] — ⚠️ Inventario di cosa pubblicano 15 siti di nail studio (5 Piemonte, 6 Italia, 4 estero) - sezioni, formati, FAQ ricorrenti, errori. Si riusa per ogni sito nail.
- [[competitor-siti-tattoo]] — ⚠️ Inventario di cosa pubblicano 14 siti di studi/tatuatori tattoo (5 Piemonte, 5 Italia, 4 estero) - sezioni, FAQ, parole anime, errori.
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


**clienti/**

- [[adelina-nails]] — Nail artist ad Alessandria, @nails_by_.adelina, 1.246 follower, nessun sito. Ha risposto «Ciaooo, ok» al primo DM del 17/9, bozza in costruzione dal 18/9.
- [[albybike]] — Negozio di biciclette - vendita, assistenza e riparazione, abbigliamento e integratori per ciclismo.
- [[bar-tabacchi-fiftynine]] — ⚠️ Bar tabaccheria e pizzeria in via Nazionale dei Giovi 59, Cesano Maderno (MB), telefono 0362 528451.
- [[castiglione-furniture]] — ⚠️ Falegnameria su misura, @castiglione_furniture su Instagram.
- [[custom-beauty-nails]] — Onicotecnica a Treviglio (BG), @custombeautynailstreviglio, 1.033 follower. Bozza online dal 16/9, il DM non e' ancora partito.
- [[design-capelli]] — Parrucchiere a Nichelino (TO), @designcapelli, 203 follower, dal 2015 in via XXV Aprile, nessun sito. Ha risposto «Buonasera qui grazie» al DM del 20/9. Bozza online su designcapelli.netlify.app dal 21/9, il DM col link e' di Patrick.
- [[dsi-advertising]] — ⚠️ D.S.I. Advertising di Piras Sebastiano, Merate (LC).
- [[edilida]] — Edilida SRL, impresa edile di Travagliato (BS). Ha compilato il modulo della ricerca il 18/09. Si punta a una videochiamata sulle scadenze di cantiere, mail di lunedì 21.
- [[il-salone-di-andrea]] — ⚠️ Parrucchiere donna e uomo di Andrea Bielli, Viale Natale Betelli 58, Dalmine.
- [[laurafranzoni]] — Extension ciglia a Brescia, @laurafranzoni_lashmaker, 452 follower. Bozza online dal 14/9, il DM non è mai partito.
- [[lei-beauty-room]] — Centro estetico a Torino Cavoretto (via alla Parrocchia 4/c), @lei_beauty_room_, 671 follower, aperto dal 23/10/2025. Ha risposto «Grazie manda pure qui» al DM di Patrick del 24/9. Bozza in lavorazione, non ancora inviata.
- [[ms-service]] — ⚠️ Lead caldo - ha chiesto lui il materiale.
- [[nails-mania]] — ⚠️ Centro di ricostruzione unghie mani e piedi di Lory Frosio, onicotecnica dal 2005.
- [[newfantasy]] — New Fantasy Parrucchieri, Lurate Caccivio (CO), @newfantasy_parrucchieri, 2.606 follower. Bozza online dal 16/9 su newfantasy-parrucchieri.netlify.app; il link va su WhatsApp, da Patrick.
- [[ng-barber]] — ⚠️ Barbershop, @ngbarberstudio123. Riga 2 dell'anello 1-b, gancio 5 - l'unico link in bio è ngbarber.my-booking-app.com, cioè un'app di prenotaz...
- [[p0t-tattoo]] — Ruben, tatuatore anime e cartoon (@p0t_tattoo, 307 follower) da K-Ink Studio Tattoo, via Adua 9b Collegno (TO). Ha risposto al DM del 24/09 - la bozza la vuole su Instagram.
- [[parrucchiere-morgan]] — Portato da Morgan il 15/9: espone volantini e biglietti e parla coi clienti in cambio del sito gratis, zero percentuali. Nome TODO.
- [[pinkploy]] — Onicotecnica a Brescia centro, @nails_art_by_pinkploy, 832 follower. Bozza online dal 14/9, il secondo DM col link tocca a Patrick.
- [[sebastian-torres]] — Privato, non un'azienda. Sta aprendo la sua attività, e l'attività è opero - l'app che stiamo costruendo noi è la sua idea imprenditoriale.
- [[shaddai-extension-lash]] — Lash artist a domicilio a Bergamo, 736 follower, nessun sito - bozza costruita il 16 settembre 2026, DM non ancora inviato.
- [[shari-piras]] — ⚠️ Shari Piras, tatuatrice, Merate (LC). Due account - @shari_tattooer (4.504 follower, 493 post) è la persona, @atelierselva_ (593 follower, 41...

**contratti/**

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
- [[contattati]] — ⚠️ Due CSV, scritti dal banco e non a mano.
- [[metodo-instagram]] — ⚠️ Serve a produrre, ogni giorno, fino a 65 account Instagram verificati a cui Patrick può scrivere il messaggio di dm-instagram-vetrina senza...
- [[metodo-liste]] — ⚠️ Come si costruisce una lista - il sito si verifica aprendolo, mai dedotto da Pagine Gialle.
- [[metodo-nuove-aperture]] — ⚠️ Tre differenze rispetto a una lista normale di metodo-instagram, e la terza è quella che conta -

**processo/**

- [[canali-indiretti]] — Chi vende al posto vostro - caller, agenzie a performance, rivenditori. Prezzi al 13/9/2026. Primo segnalatore in casa: Morgan, 15/9.
- [[ciclo-settimanale]] — Dettato da Patrick il 28 agosto 2026. È il processo fisso.
- [[core-commerciale]] — Consultazione, non obbligo. I framework con cui si costruisce un testo commerciale.
- [[flusso-vendita]] — I quattro flussi di vendita e lo Straight Line - come un lead arriva alla chiusura.
- [[generazione-lead]] — Il collo di bottiglia dell'azienda - da dove arrivano i lead e quanti ne servono.
- [[materiale-offline]] — Quello che abbiamo di fisico, e a cosa è agganciato.
- [[materiale-social]] — I post pubblicati sul profilo Instagram di DenkiCode - cosa e' uscito, con che didascalia, e dove stanno i file.
- [[presidi-volantini]] — ⚠️ Terzo canale, deciso il 28/8/2026. Primo presidio vero il 15/9/2026: un parrucchiere via Morgan, pagato col sito gratis, non a risultato.
- [[prodotti-e-listino]] — I quattro prodotti e i prezzi. I prezzi sono indicativi - l'aggancio, non la cifra finale.
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
- [[script-siti-vetrina]] — ⚠️ Lo usano tutti e tre - Giulia, Gabriele, Edoardo.

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
- [[2026-09-03-tetto-dm-65]] — ⚠️ Deciso da Nicola il 3 settembre 2026, la sera stessa del primo giro vero.
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

## 06-Daily

*Note di giornata e handoff*

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
