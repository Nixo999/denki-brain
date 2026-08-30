---
type: risorsa
updated: 2026-08-30
source: denkicode
tags: [registro, interventi, repo, database]
---

# Registro degli interventi — chi ha toccato cosa, quando, e dove

Una riga per **intervento**, non per commit. Il più recente in cima.

Serve a rispondere in dieci secondi a tre domande che altrimenti costano
mezz'ora di `git log` su due macchine: *chi ha cambiato questa cosa*, *quando*,
e soprattutto **se il database è andato dietro al codice** — perché il push
porta il codice e non lo schema, ed è il modo in cui questo progetto si è già
rotto due volte.

## La regola

**Ogni modifica a un progetto va in due posti**, sempre, dal 28 agosto 2026:

1. **Nel repository del progetto** — commit con il *perché*, e voce nel diario
   del repo se ce l'ha (`docs/07-diario.md` su [[denkishift]],
   `docs/handoff.md` su [[opero]]).
2. **Qui**, una riga. Si scrive **quando il lavoro è finito**, non quando si
   comincia, e prima di chiudere la sessione.

Le regole di push restano quelle di ciascun repo — su [[denkishift]] si pusha
dopo ogni pezzo, su [[opero]] si chiede prima — e il vault si pusha sempre.

⚠️ **La colonna che conta è `Database`.** Se un intervento cambia lo schema e la
migrazione non è stata eseguita, la riga si scrive lo stesso, con ⬜ e il nome
del file: è l'unico posto in cui quel debito resta visibile. Un codice
pubblicato senza la sua migrazione apre un tabellone vuoto.

Colonne: **Quando** (data e ora) · **Chi** (persona, e `+claude` se il lavoro è
stato fatto in sessione) · **Progetto** · **Repository** · **Database**
(`—` se non toccato, `sviluppo`/`produzione` + stato) · **Cosa** · **Commit**.

## 2026-08-31

| Quando | Chi | Progetto | Repository | Database | Cosa | Commit |
|---|---|---|---|---|---|---|
| 01:3x | Nicola +claude | sito V-BAG | `vbag-site` | — | **Pouch menta nel lookbook** (foto arrivate in Downloads: `foto3` usata, `foto 4` scartata per le dita nel ritaglio) scontornato con rembg, catena pulita. **Animazione ad apparizione**: la borsa atterra sul palco con rimbalzo leggero dopo la card (fill `backwards`, non `both`: il fill finale bloccherebbe l'hover). ✅ Misurato: 384×430 nel palco, `land` running con stagger 290ms. L'IO non consegna a pane nascosto (nota già a registro): reveal provato nelle sessioni a pane visibile | `2821417` |
| 01:0x | Nicola +claude | sito V-BAG | `vbag-site` | — | **Piu' animazioni, tutte CSS**: entrata hero in stagger al load, respiro continuo della borsa (7s), reveal dei titoli e parallax della trama via `animation-timeline: view()`, underline che si ritirano. Nota tecnica: un'`animation` vince sul transform di `:hover`, quindi il lift della borsa in hover e' stato tolto a favore del float. ✅ Misurato: DocumentTimeline + ViewTimeline + ScrollTimeline attive insieme, float campionato (-8.3→-3.8px in 1.2s). ⚠️ Il pouch menta resta senza foto: i file non sono mai arrivati su disco, servono da Nicola | `a3f56ea` |
| 00:4x | Nicola +claude | sito V-BAG | `vbag-site` | — | **Foto scontornate e pannelli calmati** (feedback: sfondo delle foto inguardabile, pannelli un pugno in un occhio). Borsa rosa scontornata con **rembg locale** (modello bria ~1GB in `~/.rembg`, ritaglio pulito coi buchi della maglia passanti), webp con alpha su pannelli-scena tenui: arco sfumato nell'hero, palco radiale nel lookbook, drop-shadow viola. Handmade da lilla pieno a `--lilla-soft`, slot menta senza bordo su mint al 55%, sezioni fino a 8.5rem. Foto col divano rimosse; og.jpg composta (l'alpha negli og diventa nero). ✅ Palco 4:5, zero overflow a 375, light e dark visti al primo frame | `b4eb759` |
| 00:1x | Nicola +claude | sito V-BAG | `vbag-site` | — | **Palette del logo + fondo animato allo scroll**: il lilla `#DC92FF` da accento a protagonista (CTA lilla, sezione handmade in lilla pieno identica nei due temi, testo ink fisso: il viola su lilla dava 2.7:1). Dietro la pagina tre forme dal logo (V in didone al 9%, arco, cerchio) mosse da `animation-timeline: scroll(root)`, zero JS: dove manca il supporto (Firefox) restano ferme, decorative. Sintassi presa da `modern-web-guidance` (parallax-scroll-effects). ✅ Misurato: ScrollTimeline attiva, a scrollY 1506 la V trasla 150px e ruota 2.3°, zero overflow a 375 | `94b2cb6` |

## 2026-08-30

| Quando | Chi | Progetto | Repository | Database | Cosa | Commit |
|---|---|---|---|---|---|---|
| 23:5x | Nicola +claude | sito V-BAG | `vbag-site` | — | **Redesign boutique** su feedback di Nicola («più elegante e professionale»): Bodoni Moda + Jost al posto di Fredoka + Nunito, bottoni netti uppercase, foto hero ad arco, logo script nel footer e solo simbolo in topbar (`assets/simbolo.svg`, 10 path senza defs → ripetibile inline). H1 misurato: 3 righe a 1280 con la scala vecchia, 2 dopo il clamp. Trappola nuova del pannello: gli screenshot congelano al primo frame dopo il load anche a pane visibile — hero e mobile visti, sezioni interne verificate solo a misure | `6f899ef` |
| 23:2x | Nicola +claude | sito V-BAG (personale di Giulia, **fuori DenkiCode**: niente listino, niente scheda progetto nel vault) | `vbag-site` (nuovo, `Desktop/vbag-site`, solo locale: nessun remote) | — (statico, nessun database) | **Sito vetrina V-BAG**: le borse chunky fatte a mano da Giulia, ordini via form → messaggio wa.me precompilato. Logo vettoriale estratto dal PDF (tratti a `currentColor`: un SVG per tema chiaro e scuro, V lilla `#DC92FF` fissa), Fredoka+Nunito self-hostate, light/dark automatico. Bug vero trovato: l'attributo `height` delle `<img>` vince su `aspect-ratio` CSS (card a 1405px) → reset `img{height:auto}`, lo stesso già visto su castiglione. ✅ Misurato a 1280 e 375 emulati: zero sfondamento, form validato (errori inline + focus), contrasti 5.8-16:1, tap target ≥44px. ⚠️ Aperti: numero WhatsApp vuoto in `script.js` (il form avvisa invece di aprire), foto del pouch menta solo in chat (slot dichiarato in pagina), nessun deploy. Il pannello a pane nascosto renderizza a viewport 0×0: verifica fatta a misure + emulazione, la resa vera va vista su un browser | `308bae6` |
| 03:4x | Nicola +claude | [[castiglione-furniture]] | `vetrina_castigliano_furniture` | — | Il sito va online: repo GitHub creato da Nicola e push di `master` locale su `origin/main` (stesso schema di OperO), destinazione Netlify. Statico puro: niente build command, publish directory = root | — |
| 03:2x | Nicola +claude | [[castiglione-furniture]] | `castiglione-site` | — | **Galleria pinnata corretta** (feedback: titolo sparito e foto tagliate durante lo scroll laterale). Il pin passava dal nastro all'intera sezione alta un viewport; foto dimensionate dall'altezza (56dvh) con larghezza dall'aspect ratio. Trappola trovata: un `.wrap` (margin auto) dentro flex column si shrink-wrappa e centra — `width:100%`. Misurato al caso peggiore 1280×700: tutto dentro, pin 1647px, zero errori | `b2d4cb5` |
| 02:5x | Nicola +claude | [[castiglione-furniture]] | `castiglione-site` | — | **Spazi e foto ribilanciati** su feedback di Nicola (capitoli semivuoti, crop stretto). Tre bug veri: reset `img` senza `height:auto` (l'attributo height teneva un'immagine a 340×1440), `.stat span` che colpiva anche il contatore dentro `b` (0 alto 10px), capitoli con colonna morta. Ora ogni capitolo ha principale + immagine di spalla con didascalia (entrano bagno marmo, libreria noce, bottigliera), parallax dimezzato, tolto il 1990 inventato (→ «100% prodotto nei nostri laboratori»). Verificato con viewport emulati e hook `?peek` temporaneo (rimosso prima del commit) | `a91ecb6` |
| 02:0x | Nicola +claude | [[castiglione-furniture]] | `castiglione-site` | — | **Riscrittura immersiva**: la v1 era «il sito più piatto della storia» (parole di Nicola). Ora scroll-telling scuro con GSAP da CDN (pattern e dosi dalla base dati `ui-ux-pro-max`: max 1 pin, scrub 0.5-1.5, parallax solo sulle immagini): sipario, hero didone Playfair 900 a tutta larghezza, capitoli con parallax, galleria orizzontale pinnata (desktop; su touch scroll-snap), count-up, marquee. Motion additiva: senza CDN o con reduced-motion il sito resta completo. ✅ Misurato a 1280/375: zero overflow, 2 righe di titolo, 1 pin, 23 trigger, 0 errori. ⚠️ Il pannello dipinge solo il primo frame dopo il load: le sezioni interne sono verificate a misure, la resa vera va vista su un browser | `8cb10ea` |
| 01:2x | Nicola +claude | [[castiglione-furniture]] | `castiglione-site` (nuovo, `Desktop/castiglione-site`, solo locale: nessun remote) | — (statico, nessun database) | **Sito vetrina per Castiglione Falegnameria** (Bronte, CT) costruito dai contenuti veri di `@castiglione_furniture`: profilo e 20 post scrapati con lo strumento **Apify** collegato a Claude Code, 31 foto scaricate in locale (gli URL CDN scadono), palette oliva+carta presa dai loro lavori. Un solo `index.html`. ⚠️ L'account si chiama `castiglione_furniture` (inglese), non «forniture»: la ricerca col nome italiano non lo trovava. ✅ Misurato a 1280 e 375 emulati: zero sfondamento, H1 su 2 righe, CTA nel viewport, contrasto nav 9:1 (era invisibile per specificità CSS, corretto). Reveal con fallback: il pannello browser a pane nascosto non consegna gli IntersectionObserver e la pagina restava bianca sotto la piega. Non verificato: resa su browser vero e telefono fisico; contatti solo IG/FB perché il profilo non pubblica email o telefono | `e0260f8` |

## 2026-08-29

| Quando | Chi | Progetto | Repository | Database | Cosa | Commit |
|---|---|---|---|---|---|---|
| 23:5x | Nicola +claude | [[sito-denkicode]] | `pixel-perfect-rebuild` | — (il sito non ha migrazioni; Supabase serve solo al form contatti) | **denkicode.com diviso in due metà**: siti web e gestionali, separate da una fascia e raggiungibili dai due bottoni dell'hero. Nella parte nuova: DenkiShift, i gestionali su misura, e una galleria sua con DenkiShift e OperO (dichiarato come **collaborazione**, è il prodotto di Sebastian). Blog tolto dal listino; vetrina da «600 sbarrato 300 −50%» a **«circa 300»**; degli abbonamenti resta il prezzo del solo **Base, 15-40 €**. DenkiShift a schermo non ha una cifra ma una **quota annuale sui dipendenti**, e nessuna data. ✅ Misurato a 1440 e 375: zero sfondamento orizzontale, bottoni pari, barra su una riga | `443f3ae` |
| 01:1x | Nicola +claude | [[opero]] | `opero-sito` | ✅ **sviluppo: `20260829120000_opero_choice.sql` eseguita** (`db push`), e con lei `20260829100000_super_admin_torres_ritenta.sql` che era rimasta indietro. Edge function `send-push` ridistribuita | **OperO Choice**: il Super Admin sceglie una o piu` persone fra tutti gli account di tutte le aziende, scrive, e alla loro prossima apertura esce un messaggio a schermo pieno col pulsante bloccato 5 secondi. Funzione **nuova**, senza originale in OperO 1 → da quotare. ✅ **Verificato nel browser** con Nicola dentro: blocco di 5 s misurato, esce una volta sola, `seen_at` scritto, `send-push` risponde 200 al Super Admin. Resta scoperta la consegna su un telefono vero | `01495b9` `760dda3` |

## 2026-08-30

| Quando | Chi | Progetto | Repository | Database | Cosa | Commit |
|---|---|---|---|---|---|---|
| 14:0x | Patrick +claude | [[denkishift]] | `smooth-duty` + `denki-brain` | — (solo grafica) | **Il marchio vero al posto del segnaposto.** Patrick passa il logo di DenkiShift in PDF; al suo posto c'era un quadretto sfumato con dentro l'icona `CalendarDays` di lucide. Il PDF non conteneva immagini — solo tracciati — quindi il marchio è **estratto come vettore** (34 percorsi, quelli veri di Affinity) in `components/ui/marchio.tsx`, non ridisegnato e non rasterizzato. Metà neutra e calendario usano `currentColor`: sul tema scuro è identico all'originale, sul chiaro è il negativo — senza, su bianco sparirebbe metà marchio. `--marchio-1`/`--marchio-2` diventano la sorgente unica da cui scende `--brand-gradient`. Rifatte le tre icone PWA. ⚠️ **Il PDF è sparito dal Desktop a metà lavoro**; l'SVG estratto è ora anche in `03-Storage/brand/logo/logo-denkishift.svg`, ma **il sorgente Affinity non è nel vault**. ✅ Verificato a 28-110px sui due temi; ⚠️ dentro l'app no, è dietro login | `f224a31` |
| 13:4x | Patrick +claude | [[denkishift]] | `smooth-duty` | — (solo colore, nessuna migrazione) | **Il turno nel tabellone torna azzurro, e lo sfondo diventa quello del sito.** Nel tabellone (`roster.tsx`, il `Chip`) ogni turno assegnato era `bg-accent-soft text-accent`: seguiva l'accento, quindi era diventato viola. Nascono `--turno` / `--turno-soft` fissi sull'azzurro (`#0057AD` chiaro, `#3D9EFF` scuro; il chiaro è mezzo passo più scuro perché sui grigi viola `#005BB7` sulla pastiglia stava a 4,49). **La ragione è più forte della richiesta**: il foglio di stile dice già che l'accento è azione e selezione, mai uno stato — un turno non è nessuna delle due. Dallo sfondo di `denkicode.com` entrano sfumatura verticale, due aloni viola radiali e i fili inclinati; dosi del sito sullo scuro, dimezzate sul chiaro. Il fondo passa da `<body>` a `<html>` perché il livello sta a `z-index: -1`. ✅ Verificato **a schermo** (1280 e 375, due temi) su riproduzione fedele fuori dall'app; ⚠️ dentro l'app no, è dietro login | `a704db2` |
| 13:1x | Patrick +claude | [[denkishift]] | `smooth-duty` | — (solo colore, nessuna migrazione) | **La tavolozza passa dall'azzurro di sistema al viola del marchio**: `--accent` da `#005BB7` a `#802ACB` (chiaro) e da `#3D9EFF` a `#BC79F6` (scuro), alla tinta 272 — il punto di mezzo esatto fra i due colori del logo. Anche i grigi portano quella tinta: è il pezzo che fa leggere l'app come una cosa sola. Fondo scuro `#09090B` e oro `#EBC247` presi da denkicode.com; il magenta è `--brand-2` e resta fuori dalle pagine operative (troppo vicino al rosso degli errori). ⚠️ **Costruito sopra la revisione contrasti di Nicola delle 12:0x, non al posto suo**: il rebase ha dato conflitto su `globals.css` e i valori sono stati ricalcolati col suo metodo (fondo peggiore + pastiglia tenue). Tutti e otto i colori passano 4,5 su entrambe le misure, in tutti e due i temi. Le tinte dei reparti perdono la fascia 260-285 (26 → 24 valori): un reparto viola sembrava il reparto selezionato. ✅ `tsc` pulito, build completa. **Non verificato a schermo** (l'app è dietro login) | `f05b47e` |
| 13:3x | Nicola +claude | [[denkishift]] | `smooth-duty` | ✅ sviluppo e ✅ **produzione**: `20-pagina-disponibilita.sql` eseguita (produzione da Nicola, SQL Editor) | Pagina Disponibilità spegnibile dalle Impostazioni; Supervisione senza assenti. Pushato dopo la migrazione | `1c5066b` |
| 13:0x | Nicola +claude | [[denkishift]] | `smooth-duty` | — | **Tolta la pagina «Oggi»** (vissuta un giorno): via rotta, motore, prova, distintivo e le 3 query del guscio. In rebase sono arrivati 3 commit di branding da un'altra macchina (viola, logo vero): tenuti tutti e due i lavori | `bcc6544` |
| 12:0x | Nicola +claude | [[denkishift]] | `smooth-duty` | — | Applicata la revisione UI: impostazioni a una riga per leva con salvataggio automatico, filtri del tabellone dietro un bottone, Svuota nella sessione, badge numerico e caret nel guscio. Pushato, non verificato a schermo (dietro login) | `998cadf` |
| 10:3x | Nicola +claude | [[denkishift]] | `smooth-duty` | — (letto, non toccato: diagnosi RLS 3,7ms, piano ottimale) | Indagine lentezza: colpa di Ohio e del freddo, non del DB. Ping programmato + `staleTimes: 30`. **Pushato alle 10:5x insieme al lotto design** su decisione di Nicola: da qui torna la regola del repo, pezzo finito → push | `032091c` `05e34fb` |

## 2026-08-28

| Quando | Chi | Progetto | Repository | Database | Cosa | Commit |
|---|---|---|---|---|---|---|
| 16:3x | Nicola +claude | — | `denki-brain` | — | Creato [[indice]] (70 note) e installato `ponytail` a livello utente | — |
| 16:0x | Nicola +claude | — | — | — | Installati `superdesign`, `playground`, `modern-web-guidance` (~1.030 tok/sessione). **Solo sul PC di Nicola**: i plugin non stanno in git | — |
| 15:2x | Nicola +claude | [[denkishift]] | — | ✅ **sviluppo: `19-lavoratori-a-chiamata.sql` eseguita** dal SQL Editor. `verifica-schema`: 19 su 19 | — |
| 14:5x | Nicola +claude | tutti | `denki-brain` + `smooth-duty` + `opero-sito` | — | **Regola nuova**: ogni modifica va nel repo *e* qui. Registro creato e agganciato ai tre `CLAUDE.md` | `1763144` + questo |
| 14:26 | Nicola +claude | — | `denki-brain` | — | Controllo incrociato dei due repo, guida e nota database allineate alla decisione «non più in locale» | `665e9f0` |
| 14:16 | Nicola +claude | [[denkishift]] | `smooth-duty` | — | **Decisione**: non si avvia più niente in locale, si guarda su `denkishift.it`; migrazione in produzione *prima* del push | `ee6ae92` |
| 14:10 | Nicola +claude | [[denkishift]] | `smooth-duty` | — | `pg` dichiarato in `devDependencies`: su macchina nuova gli script del database non si fermano più | `201f939` `6e31ab9` `d7018da` |
| 14:14 | Nicola +claude | — | `denki-brain` | — | [[patrick-modifica-denkishift]]: guida passo passo per chi non scrive codice | `72eb66e` |
| 13:36 | Patrick +claude | — | `denki-brain` | — | Modulo Word del report settimanale, `.gitattributes` per i binari | `dc13ec5` |
| 13:18 | Nicola +claude | [[denkishift]] | `smooth-duty` | ⬜ **sviluppo: `19-lavoratori-a-chiamata.sql` non eseguita** | Disponibilità del responsabile nel tabellone | `d6a4335` |
| 13:10 | Patrick +claude | — | `denki-brain` | — | Ciclo settimanale: 4 liste la domenica, 5 report indietro | `bdbb8a3` |
| 12:13 | Nicola +claude | — | `denki-brain` | — | Protocollo Trevis come livello base a ogni avvio | `f563e75` `f84f378` |
| 12:09 | Nicola +claude | [[denkishift]] | `smooth-duty` | ⬜ **sviluppo: `19-lavoratori-a-chiamata.sql` non eseguita** | Lavoratori a chiamata: chi tace non ha accettato | `1b160ea` |
| ~12:00 | Patrick +claude | [[denkishift]] | `denki-brain` | 🟡 sviluppo: catena provata fino alla password, `.env` predisposti e vuoti | Corretta la fotografia del Mac in [[setup-macchina-nuova]]; su DenkiShift `db push` non esiste | `9358c87` |

## Il debito aperto, in chiaro

- ✅ **`19-lavoratori-a-chiamata.sql` eseguita sullo sviluppo** il 28/08 alle
  15:2x, incollata nel SQL Editor da Nicola. `verifica-schema.mjs` risponde
  **19 su 19**: sviluppo e produzione sono allineati fra loro e a `main`
- ✅ **Password del database rimessa.** Era stata **davvero cambiata**: il
  valore vecchio veniva letto e rifiutato, quello nuovo passa. Chi ha ancora
  il vecchio in `.env.db` — qualunque altra macchina — deve rifare il giro
- ✅ **La produzione ha la 19** — verificato nel browser il 28/08 alle 15:0x, da
  una sessione già autenticata: la vista **Disponibilità** si apre e spiega il
  regime, il filtro **«A chiamata»** c'è, il tabellone della settimana 24-30
  agosto è pieno. Quindi `availability_days` e `company_settings.regime_chiamata`
  esistono là. **Il disallineamento è al contrario di come sembrava**: è lo
  *sviluppo* a essere indietro rispetto alla produzione, non il viceversa
- 🟡 Restano due errori in console (`404` e `UnrecognizedActionError: Server
  Action non trovata`), ma sono **del caricamento precedente**: dopo un reload
  pulito nessuna richiesta fallisce. È il caso classico della scheda rimasta
  aperta su una build vecchia mentre ne è stata pubblicata una nuova

## Collegamenti

[[denkishift]] · [[opero]] · [[modifiche-al-database]] ·
[[patrick-modifica-denkishift]] · [[2026-08-28-registro-interventi]]
