---
type: risorsa
riga: Errori tecnici già pagati e strade scartate, per dominio. Descrittivo, non è un rulebook - le regole stanno in convenzioni.
updated: 2026-09-25
verificato: 2026-09-10
source: denkicode
tags: [trappole, memoria, frontend, gsap, git]
---

# Trappole — quello che non voglio riscoprire due volte

**Questo file non è un manuale.** È il registro degli errori già pagati e delle
strade che non funzionano. Serve prima di ripetere un gesto, non prima di
progettare.

## Le tre classi — la regola che tiene in piedi il file

Dal 10 settembre 2026 ogni voce nuova si apre con la sua classe
([[come-si-scrive-una-nota]]):

| Classe | Cos'è | Cosa ci si fa |
|---|---|---|
| `[TRAPPOLA]` | È successo, è costato tempo, ecco la contromisura | Si evita di ripeterlo |
| `[SCARTATO]` | Provato, non funziona | Non si ripropone |
| **REGOLA** | Il modo giusto, da qui in avanti | **Non sta qui**: sta in [[convenzioni]], nel `CLAUDE.md` del repo, o in una decisione |

Le tre cose che ne discendono:

1. **Una trappola non diventa una regola da sola.** Se il modo giusto va reso
   dottrina lo scrive una persona in [[convenzioni]], di proposito. Leggere
   questo file non promuove niente.
2. **Una trappola è descrittiva, mai prescrittiva fuori dal suo caso.** «Brave
   headless sotto 500 px mente sul layout» non è «non si misura a 375».
3. **Uno scarto che ricompare in una risposta è un errore della risposta.**
   Riaprirlo si può, ma si dichiara che lo si sta riaprendo e perché.

**Tutte le voci scritte prima del 10 settembre 2026 sono `[TRAPPOLA]`**, ed è
per questo che non portano il marcatore: il file nasce come raccolta di errori.
Nessuna di loro è mai stata una regola di casa.

## Come si legge — a sezioni, mai intero

Sono oltre 3.000 parole. Si guarda l'indice delle sezioni e si apre solo quella
del lavoro di oggi:

```bash
grep -n '^## ' 01-Coding/trappole.md
```

## Come si aggiorna

A fine sessione, con `/chiudi-sessione`, e solo se è uscito qualcosa che vale su
un progetto che ancora non esiste. **Max 4 righe a voce**: trappola,
contromisura, dove è stata pagata. Il racconto resta nella daily e nel registro,
e da qui ci si linka.

## Scartato — non si ripropone

Vuota al 10 settembre 2026. Ci finisce una strada provata davvero e bocciata,
non un'idea scartata a tavolino: quella sta in `05-Decisioni/`, sezione «Cosa si
è scartato».

## Catture e verifica in headless

- `[TRAPPOLA]` **Uno zero di `grep -c` su un `curl` non distingue «non c'è»
  da «non è arrivato niente».** Sei giri su `vbag.it/styles.css` davano `0`
  occorrenze della regola nuova e l'ho riferito come «forse il deploy non è
  mai andato online»: le risposte erano **vuote**, `shasum` a `da39a3ee5e6b`,
  che è l'hash della stringa vuota. Il giro dopo la regola c'era, 11 volte —
  Nicola stava giudicando il sito vero, e gli ho detto il contrario. → un
  conteggio a zero si legge **insieme alla lunghezza della risposta**: si
  scarica il file (`curl -o`) e si fa `diff` con quello locale, oppure si
  stampa anche `wc -c`. Un `grep -c` da solo su una risposta di rete non è una
  misura. (21/09/2026, sito V-BAG)

- `[TRAPPOLA]` **Un'apertura che vive sotto `.js` compare mezzo secondo dopo la
  pagina, e le cade sopra.** `.js` lo metteva il boot in fondo al body, che sta
  **dietro ai due `<script src>` di GSAP**: con la CDN fredda i fotogrammi erano
  pieni di pagina fino a 800 ms e il sipario arrivava a 900. → le classi di stato
  si accendono da uno `<script>` **in testa**, e l'uscita del sipario si scrive in
  CSS invece che in una timeline GSAP, cosi' non dipende da una richiesta di rete.
  Lo starter e' stato corretto lo stesso giorno: porta `.apertura` dalla testa.
  (21/09/2026, [[sito-designcapelli]])


- `[TRAPPOLA]` **Se il server di anteprima muore, il browser continua a servire
  dalla cache il sito di un'altra sessione che stava sulla stessa porta.** Il
  21/09 la 8765 rispondeva con il titolo `Pizzeria Lobidù, Tradate` mentre
  `lsof -iTCP:8765` non trovava nessuno in ascolto: la pagina veniva dalla cache
  del pannello. Si stava per giudicare il sito sbagliato. → **prima di guardare
  una cattura si controlla il titolo con `curl -s <url> | grep -o "<title>[^<]*"`**,
  e la porta si sceglie diversa per ogni sito. (21/09/2026, [[sito-designcapelli]])

- `[TRAPPOLA]` **`cattura-fette.mjs | head -3` uccide la cattura a metà e non lo
  dice.** `head` chiude la pipe, node prende SIGPIPE e si ferma dopo tre fette:
  restano 4 PNG su 6 e sembra che la pagina sia alta un solo schermo. → l'output
  si porta su un file (`> cattura.log 2>&1`) e si guarda dopo, oppure si usa
  `tail`. Il numero di fette atteso è `ceil(altezza / viewport)`, e si conta.
  (21/09/2026, [[sito-designcapelli]])

- `[TRAPPOLA]` **L'apertura si giudica contando le tinte di ogni fotogramma, non
  a occhio.** Su Design Capelli fra l'ultimo salto di tono e la discesa del
  marchio restavano **300 ms di schermo a una tinta sola** — vuoto — e nel
  pannello non si notava. Campionando da CDP un PNG ogni 100 ms e contando le
  tinte distinte, i fotogrammi vuoti escono da soli: `1 tinta` = niente in
  pagina. Lo strumento è `01-Coding/strumenti/cattura-apertura.mjs`:
  `node cattura-apertura.mjs <url> <cartella> 100,200,300,…`
  (21/09/2026, [[sito-designcapelli]])

- `[TRAPPOLA]` **Il pannello del browser non consegna i tasti alla pagina
  mentre c'è un `<dialog>` modale aperto.** Su Barbershop SNIA né `Escape` né
  le frecce arrivavano — un listener di prova su `document` in fase di cattura
  registrava **zero** eventi — e il visore sembrava rotto. Con la tastiera vera
  via CDP (`Input.dispatchKeyEvent`, keyDown + keyUp con
  `windowsVirtualKeyCode`) funzionava tutto al primo colpo. → **una scorciatoia
  da tastiera si prova con CDP**, non dal pannello, e prima di dire che è rotta
  si controlla che l'evento arrivi. (20/09/2026, [[sito-barbershop-snia]])
- **L'evento `close` di un `<dialog>` non è arrivato**, quindi la pulizia
  appesa a quell'evento non è mai partita: `overflow:hidden` restava sul body e
  la pagina non scorreva più. E un `preventDefault()` su `cancel` (o sul
  keydown di Esc) **annulla la chiusura nativa**: il visore restava aperto. →
  la pulizia sta in una funzione idempotente chiamata da tutte le vie d'uscita,
  Esc compreso con `setTimeout(…, 0)` dopo la chiusura nativa; nessun
  `preventDefault`. (20/09/2026, [[sito-barbershop-snia]])

- **Nel pannello del browser a scheda nascosta `innerHeight` è 0 e le
  transizioni CSS non avanzano**: una rivelazione con `.dentro` messo e
  `clip-path` ancora chiuso sembra rotta e non lo è. → lo stato di una motion
  si legge in headless o a scheda visibile. (19/09/2026, [[sito-barbershop-snia]])

- **Il pannello del browser dipinge solo il primo frame dopo il load.** Uno
  screenshot dopo lo scroll fotografa il nulla, o peggio fotografa una cosa
  falsa. → **Si misura, non si guarda**: `getBoundingClientRect` e computed
  style su viewport emulati con `resize_window`. È la regola nata su
  [[sito-castiglione]] e diventata vera su [[sito-fiftynine]], dove uno
  screenshot mostrava l'hero salito sotto la nav e la misura diceva `scrollY 0`.
- **A pane nascosto il viewport è 0×0.** I trigger si calcolano su una finestra
  inesistente e `gsap.matchMedia` non fa partire i blocchi `min-width`. →
  `ScrollTrigger.refresh()` su `visibilitychange`. Non è un bug del sito: su
  browser vero il viewport è giusto dal primo istante.
- **Gli IntersectionObserver non vengono consegnati a pane nascosto**, quindi
  reveal-on-scroll significa pagina bianca sotto la piega. → fallback a tempo:
  1 s senza callback e si mostra tutto.
- **`scrollTo(0, y)` con `html{scroll-behavior:smooth}` si ferma a metà** nelle
  catture. → `behavior:'instant'` nei wrapper di cattura. ([[sito-nails-mania]])
- **`sips --cropOffset` non ritaglia: viene ignorato in silenzio.** Exit 0 e
  file identico all'originale, su JPEG come su PNG — due ritagli a offset
  diversi hanno lo stesso `md5`. Era registrato come «restituisce un PNG nero»
  ([[sito-salone-di-andrea]]): non annerisce, non fa niente, ed e' peggio,
  perche' un pezzo sbagliato sembra un pezzo giusto. → venti righe di Swift con
  `CGImage.cropping(to:)`, argomenti `in out x y w h`. Serve ogni volta che una
  cattura di pagina intera va spezzata per guardarla. ([[sito-mikuma-dogs]])
- **Una cattura oltre il viewport non fa scattare il lazy-load.** Con
  `captureBeyondViewport` le foto sotto la piega escono nere e sembra un bug
  del sito. → `loading="eager"` forzato prima della cattura e attesa di
  `decode()` su ogni immagine. ([[sito-mikuma-dogs]])
- **Brave headless rilanciato a ogni cattura con il profilo cancellato riparte
  dal first-run e si impianta.** → una sola istanza viva via CDP e
  `Page.captureScreenshot` a ripetizione su quella. ([[sito-mikuma-dogs]])
- **In `?cattura` anche un `clamp(4.5rem, 11vh, 8rem)` va passato da `--vh`.**
  La finestra headless e' alta quanto il documento, quindi `11vh` sfonda il
  tetto del clamp e i vuoti fra le sezioni si presentano al doppio di quello
  che sono: si corregge un difetto che sul browser vero non esiste. `--vh`
  copriva `min-height`, non i padding dentro `clamp`. ([[sito-mikuma-dogs]])
- **A pane nascosto è stale anche `getComputedStyle`, non solo il pixel.** Un
  campo in stato `.invalid` leggeva ancora il colore di bordo vecchio, `opacity`
  restava a 0 e `img.complete` era `false`; dopo uno `screenshot`, che forza un
  frame, i valori erano quelli giusti. La misura non è automaticamente più
  affidabile dello screenshot: se il pane non ha disegnato, mente anche lei.
  (sito V-BAG di Giulia, 7 settembre)
- **Il pane ha un viewport fantasma**, e `scrollWidth - clientWidth` misurato lì
  dà overflow che a 1440 e 375 emulati è zero. Si misura solo su viewport
  emulati espliciti, mai su quello che capita.
- **`timeout` non esiste su macOS.** `perl -e 'alarm N; exec @ARGV' cmd`
  fa lo stesso lavoro. ([[sito-osteria-tarilli]])
- **Brave è un Chromium headless già installato**: `"/Applications/Brave
  Browser.app/Contents/MacOS/Brave Browser" --headless=new --screenshot=…
  --window-size=1440,900 --virtual-time-budget=6000 URL` scrive un PNG vero
  su disco, cosa che il pannello non sa fare. Per la pagina intera la
  finestra va alta quanto il documento, **e tutto ciò che è in `vh` si
  allunga con lei**: un hero `100dvh` diventa alto 6.800 px. → le misure in
  `vh` passano da `--vh:1vh` e un wrapper `?cattura` le fissa a 9 px.
  Senza `--user-data-dir` usa il profilo vero, cache compresa: la cattura può
  mostrare il CSS di prima. Con un profilo nuovo però `--headless=new` si
  impianta (finestra di benvenuto): profilo nuovo solo con `--no-first-run
  --disable-features=…`, o si verifica dal pannello con le misure.
  ([[sito-osteria-tarilli]])
- **Brave headless non scende sotto ~500 px di finestra.** Con
  `--window-size=375,812` il PNG e' largo 375 ma il layout dentro e' piu'
  largo: la nav perde il bottone di destra e il testo esce dal bordo, e sembra
  un bug del CSS che il pannello a 375 non conferma. → il sito va in un
  `<iframe style="width:375px">` dentro una pagina wrapper, finestra da 800,
  e si ritaglia il PNG (Swift `CGImage.cropping`, perche' `sips --cropOffset`
  non ritaglia affatto). ([[sito-da-caterina]])
- **La cattura headless fotografa l'animazione d'ingresso a meta'**: figurine
  mezze trasparenti e sovrapposte, che a occhio sembrano un difetto. → in
  `?cattura` si spegne l'animazione (`.cattura .x{animation:none}`), come si
  fissa `--vh`. ([[sito-da-caterina]])
- **Brave headless con `--virtual-time-budget` non consegna gli IntersectionObserver**,
  come il pannello a pane nascosto: una pagina con rivelazioni allo scroll esce col
  sotto-piega vuoto e sembra un bug del sito. → in `?cattura` le rivelazioni sono
  spente; la prova vera delle rivelazioni si fa con Brave `--remote-debugging-port`
  pilotato in CDP da node 22 (`WebSocket` nativo, zero dipendenze), scorrendo a passi
  e leggendo `opacity`. Trovata dall'operatore su Opus. ([[sito-da-caterina]])
- **L'altezza della pagina intera si misura prima di catturare**
  (`document.scrollHeight` sul viewport emulato) e si aggiunge margine: una
  finestra a 4900 su una pagina da 5135 taglia mappa e footer, e il finish
  reviewer la rifiuta (`disposition: recapture`). ([[sito-da-caterina]])
- **`netlify sites:create --account-slug denkicode` risponde 404**: lo slug
  del team non e' il nome che `netlify status` mostra. Si legge con
  `netlify api listAccountsForUser` (qui: `nicola-la-rezza`). Il CLI non e'
  installato: `npx -y netlify@latest`. ([[sito-da-caterina]])
- **`launch.json` va nella cartella della sessione, non nel repo**, e
  `python3 -m http.server` non parte da una cartella Google Drive
  (`os.getcwd()` è vietato): `sh -c "cd <repo> && exec python3 -m
  http.server"`. ([[sito-osteria-tarilli]])
- **Nel pannello non arrivano `scroll` e `resize`, e lo scroll fluido non
  parte.** `scrollLeft` cambia ma nessun listener viene chiamato, e
  `scrollBy({behavior:"smooth"})` lascia la posizione a zero mentre `"auto"`
  funziona. → l'aritmetica si prova forzando `scroll-behavior:auto`,
  l'animazione morbida resta da guardare su browser vero; e per lo stato di un
  carosello conviene **`ResizeObserver`**, che scatta anche dove `resize` non
  arriva. ([[sito-fiftynine]])
- **La console del pannello tiene i messaggi delle pagine precedenti.** Warning
  di una versione gia' corretta continuano a comparire dopo il ricaricamento e
  sembrano vivi. → si verifica caricando una pagina che *non puo'* produrli (su
  [[sito-fiftynine]] `?fermo=1`, che non fa girare GSAP): se ci sono ancora,
  sono vecchi.
- **`file://` non è il sito**: aperto come istantanea statica (URL `data:`) non
  gira JS e non carica le immagini relative. Si riapre dal server prima di
  concludere che qualcosa è rotto. ([[sito-fiftynine]])
- **A pane nascosto `getBoundingClientRect` restituisce il box già scalato
  dall'intro** (0,96 di un'entrata `scale`) e sembra un disallineamento di
  griglia. La geometria di un hero con entrata si misura a intro finita, o in
  Brave via CDP. Trovata dall'operatore su Opus. ([[sito-pizzeria-lobidu]])
- **Brave via CDP serve le immagini dalla cache di `python3 -m http.server`**:
  una foto ricampionata compare vecchia nella cattura. →
  `Network.setCacheDisabled` prima di `Page.navigate`. ([[sito-pizzeria-lobidu]])
- **`elementFromPoint` dichiara vuoto ogni slot fuori dal viewport**: un
  mosaico a una colonna si verifica scorrendo slot per slot, non da fermo.
  ([[sito-pizzeria-lobidu]])

- **Brave headless con lo stesso `--user-data-dir` e la stessa porta lascia
  un'istanza viva, e la corsa dopo ci si attacca in silenzio.** Nessun errore:
  CDP risponde, le misure arrivano, e sono quelle della **pagina di prima** —
  9.264 px di documento letti come 5.008. È il caso peggiore, perché il numero
  sbagliato sembra un numero giusto. → `pkill` sul processo **e profilo
  cancellato a ogni corsa**, prima di lanciare. ([[sito-laurafranzoni]],
  14 settembre)
- **Per catturare la pagina vera a piena altezza vanno prima congelati `--vh`
  e uccisi gli ScrollTrigger.** La finestra headless diventa alta quanto il
  documento, lo scrub ricalcola su quella e la cattura fotografa una pagina a
  metà animazione che non esiste su nessun browser. → si fissa `--vh` al valore
  del viewport vero e si fa `ScrollTrigger.getAll().forEach(t => t.kill())`
  prima dello scatto. ([[sito-laurafranzoni]], 14 settembre)

- `[TRAPPOLA]` **`captureBeyondViewport` non rasterizza le foto fuori dal
  viewport.** Il PNG esce completo (`complete:true`) ma le fasce basse sono
  bianche con la sola didascalia sopra: sembra un'immagine rotta in pagina. →
  si cattura a **fette di viewport 1440×900** e si cuciono in Python.
  ([[sito-nails-robyy]], 13-14 settembre)
- `[TRAPPOLA]` **Allargare la finestra all'altezza del documento gonfia i
  `clamp()` legati a `vh`.** Un `clamp(...,9vh,...)` misurato su una finestra
  alta 9.000 px dà spaziature che nessuno vedrà mai, e la cattura mostra una
  pagina diversa da quella vera. → fette al viewport vero, mai finestra alta
  quanto la pagina. ([[sito-nails-robyy]], 13-14 settembre)
- `[TRAPPOLA]` **Un `pkill` su Brave ammazza anche l'istanza CDP di un'altra
  sessione.** A metà catture l'impianto è sparito senza errore di CDP: le
  catture mancavano e basta. → si rilancia e **si riparte dalle catture che
  mancano**, non da capo, e si dichiara che l'istanza era condivisa.
  ([[sito-nails-robyy]], 13-14 settembre)
- `[TRAPPOLA]` **`scrollTo` con `scroll-behavior:smooth` falsa la verifica di
  ScrollTrigger.** La lettura arriva mentre la pagina sta ancora scorrendo e i
  trigger risultano non entrati. → `window.scrollTo({top:y, behavior:'instant'})`
  in ogni script di verifica. ([[sito-nails-robyy]], 13-14 settembre)

- `[TRAPPOLA]` **Nel pannello, a viewport emulato 1440×900 e scalato, uno
  screenshot dentro un pin fotografa uno schermo vuoto**, barra compresa, e
  sembra che il pin abbia mollato l'elemento. La geometria
  (`getBoundingClientRect` con `scrollTo({behavior:'instant'})`) diceva
  `fixed`, `top 0` per tutta la corsa, e `scrollY` risultava spostato di una
  costante rispetto a quanto chiesto: viewport fantasma. → la prova del pin si
  fa con Brave via CDP a posizioni precise della corsa:
  `01-Coding/strumenti/cattura-fette.mjs` (fette di viewport più cinque punti
  dentro ogni pin, zero dipendenze). ([[sito-hairstylebrescia]], 16 settembre)
- `[TRAPPOLA]` **`Page.captureScreenshot` via CDP può consegnare il frame
  precedente** dopo uno `scrollTo` con scrub: due catture consecutive a fine
  corsa sono uscite scambiate (169° dove doveva esserci 96°, e viceversa). →
  si legge il valore dal DOM nello stesso giro e lo si scrive nel nome del
  file, o si scatta due volte e si tiene la seconda.
  ([[sito-hairstylebrescia]], 16 settembre)

- `[TRAPPOLA]` **Il pannello browser può restare `visibilityState: hidden` per
  tutta la sessione**: dipinge il primo frame e poi gli screenshot dopo lo
  scroll tornano vuoti. Il JS però gira, quindi le misure (overflow, contrasti,
  prestazioni) restano valide da lì. Le immagini si prendono da Chrome headless
  via CDP. ⚠️ **`cattura-fette.mjs` cerca Brave**, che sul Mac di Patrick non
  c'è: lì serve uno script su `/Applications/Google Chrome.app`, e
  `Emulation.setDeviceMetricsOverride` scende a 375 dove `--window-size` no.
  (16/09/2026, [[sito-barbershop-snia]])

- `[TRAPPOLA]` **Chrome headless con `--disable-gpu` non ha WebGL**:
  `canvas.getContext('webgl')` torna `null`, un sito con three.js esce dal suo
  ramo di avvio e sembra che il 3D non sia mai stato scritto. → per verificarlo
  servono `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader`
  al posto di `--disable-gpu`. (17/09/2026, [[sito-barbershop-snia]])
- `[TRAPPOLA]` **Con un canvas fisso alto un viewport la cattura a pagina
  intera esplode**: headless allunga la finestra quanto il documento e tutto
  ciò che è in `vh` si allunga con lei, e una pagina da 9.400 px ne ha
  misurati **41.201**. → il 3D si fotografa a fette di viewport, la pagina
  intera si fotografa con `?cattura`, dove il 3D è spento per costruzione.
  (17/09/2026, [[sito-barbershop-snia]])

- `[TRAPPOLA]` **`cattura-fette.mjs` lanciato due volte di fila si aggancia
  all'istanza di Chrome della corsa precedente** e misura la pagina alla
  larghezza sbagliata: la corsa a 1440 ha riportato `documento 812 x 375`,
  cioè la finestra della corsa a 375 ancora viva. → una corsa alla volta, e
  prima di leggere i numeri si controlla la riga `documento` nel log: se la
  larghezza non è quella chiesta, si rilancia da solo. Al giro 3 due corse di
  fila sulla stessa porta CDP fallivano del tutto: serve `pkill` del Chrome
  headless e un'attesa fra una corsa e l'altra.
  (24/09/2026, [[sito-leibeautyroom]])

- `[TRAPPOLA]` **Su macOS `timeout` non esiste**: una cattura headless che si
  blocca tiene fermo l'operatore per sempre (600 s di stallo il 24/09). → si
  incapsula in `perl -e 'alarm 120; exec @ARGV' -- node …`, o si usa `gtimeout`
  di coreutils. (24/09/2026, [[sito-p0t-tattoo]])
- `[TRAPPOLA]` **`pkill -f headless` spegne anche il server di anteprima** del
  pannello, che non si chiama così ma sta nella stessa riga di comando del
  browser. → si uccide per PID, non per pattern. (24/09/2026, [[sito-p0t-tattoo]])

- `[TRAPPOLA]` **Nel pannello, il primo screenshot dopo uno scroll restituisce il
  fotogramma precedente**: due catture di fila hanno mostrato carta nuda e poi la
  pagina giusta, stessa posizione. → dopo uno scroll si cattura due volte e si
  giudica la seconda; e con il pannello nascosto si legge il DOM (`className`,
  `opacity`, `clip-path`, `elementFromPoint`), non l'immagine. (24/09/2026,
  [[sito-p0t-tattoo]])

- `[TRAPPOLA]` **Un `<iframe>` di prova ha 2 px di bordo di default**: le misure
  «a 1440» erano a 1436 e «a 375» a 371, e le altezze del documento non tornavano
  fra un giro e l'altro. → `style="border:0"` sull'iframe, o si misura con
  `resize_window` del pannello. (25/09/2026, [[sito-p0t-tattoo]])

- `[TRAPPOLA]` **Nel pannello browser nascosto `scrollTo` non genera eventi di
  `scroll` e rAF non gira**: un listener di scroll misurato così sembra rotto
  (il bottone fisso non si ritirava mai) mentre il codice era giusto. → nel test
  si fa `dispatchEvent(new Event('scroll'))` dopo ogni `scrollTo`, e si evita
  di mettere un rAF fra evento e stato: un rAF che non arriva lascia un latch
  chiuso per sempre. (25/09/2026, [[sito-leibeautyroom]])

## Immagini e `sips`

- **Una texture specchiata sui due assi da una foto in prospettiva fa chevron
  e occhi simmetrici**, e le correzioni automatiche della pendenza erano rumore
  (tre tentativi). → tessera tagliata fra due giunti trovati sui profili
  detrendizzati, bordi laterali fusi in dissolvenza. (19/09/2026, [[sito-barbershop-snia]])

- **`sips` da HEIC lascia l'orientamento nell'EXIF: tre foto verticali sono
  uscite coricate a 1600×1200 e `sips -r 90` a mano le ha girate una seconda
  volta.** → da HEIC si passa con PIL, `ImageOps.exif_transpose` poi
  `thumbnail`, e si guarda il risultato. (19/09/2026, [[sito-barbershop-snia]])

- `[TRAPPOLA]` **`sips` scrive in place, e `git restore` non ripristina un file
  untracked.** Su Custom Beauty Nails il primo ritaglio sopra il watermark era
  giusto; per allargare il margine su due foto e' partito un
  `git restore assets/img` che **e' fallito in silenzio** — le foto erano
  ancora `?? assets/img/` nel git status — e il secondo ritaglio ha lavorato
  sui file gia' tagliati: fuori le unghie, restano le nocche. Dodici foto da
  riscaricare. → **gli originali si committano prima di toccarli** (qui
  `assets/originali/`, tracciata), i ritagli si scrivono **su nomi nuovi, mai
  in place**, e l'esito di un `restore` si legge: un `||` sopra un ripristino
  fallito e' un ripristino che non c'e' stato. (16/09/2026,
  [[sito-custombeautynails]])

- **`sips` legge le dimensioni trasposte quando il browser ruota la foto.** Su
  una locandina `sips -g pixelWidth` dava 733×1100 e il browser la mostrava
  1100×733, cioe' coricata: l'orientamento c'era, ma `sips -g orientation`
  rispondeva `<nil>`. → **l'orientamento si verifica nel browser**, con
  `naturalWidth`/`naturalHeight`, non con `sips`; si raddrizza con `sips -r 90`
  e si ricontrolla. Sbagliarlo mette una locandina di traverso in pagina, e gli
  attributi `width`/`height` dell'`<img>` restano bugiardi. ([[sito-fiftynine]])
- **`sips` non scrive webp.** `-s format webp` fallisce in silenzio e non
  produce il file. Senza `rembg`/ImageMagick a portata, per un sito statico si
  resta a jpeg, che e' anche quello che il canvas codifica ovunque — su Safari
  `canvas.toBlob('image/webp')` non e' affidabile.
- **Una locandina non e' una foto**: si legge, quindi non entra in un
  contenitore che ritaglia con `object-fit:cover` e non prende parallasse.
  Serve una classe sua che la mostri intera — e il prezzo va **scritto anche in
  testo**, o chi usa uno screen reader non lo legge.
- **Un mosaico con la prima cella a tutta larghezza lascia un buco quando le
  celle scendono a due.** → `.mosaico:has(> :nth-child(3)) .foto:first-child`,
  cosi' la regola vale solo quando c'e' abbastanza da riempire la riga.
- **I ritagli con Vision da anteprime Instagram a 640 px non reggono**, e
  sopra una meccanica di orbita e parallasse il bordo sfrangiato si vede
  ancora di più. Pagata su [[sito-da-caterina]] v1, **ripagata identica** su
  [[sito-pizzeria-lobidu]] giro 1 («fatte malissimo»). → foto intere col loro
  sfondo, in cornice, `object-fit: cover`, ferme. Un ritaglio si fa solo da
  una sorgente ≥ 1200 px con soggetto netto.
- **Un gradiente d'ambiente dipinto su una scatola con `max-width` si taglia
  di netto al suo bordo** (salto di 10 sul blu a x=1412 su 1440). → il fondo
  sull'elemento a tutta finestra, il contenuto tenuto a misura con
  `padding-inline: max(var(--pad), (100% - 1240px) / 2)`. ([[sito-pizzeria-lobidu]])

## GSAP e motion

- `[TRAPPOLA]` **Dentro una sezione pinnata a `100vh` con `overflow:hidden`, il
  testo che sfora non si vede e non avvisa.** Su Custom Beauty Nails il copy
  rifatto ha portato il blocco della spina da ~660 a ~790 px: a 375x667 gli
  ultimi due righi finivano sotto il taglio, a 760x900 ne restavano fuori 95, e
  non compare nessuna barra di scorrimento. → chi allunga un testo dentro un pin
  **misura l'altezza del blocco**, non la guarda, e le media query si scrivono
  su larghezza **e altezza**. ⚠️ `--vh` costruito su `1vh` e' il viewport grande
  di iOS: con la barra dell'URL visibile lo spazio vero e' meno di quello
  misurato in headless. (16/09/2026, [[sito-custombeautynails]])

- **La natura simulata in CSS non regge accanto a una foto vera nella stessa
  pagina.** Tre giri su Mikuma Dogs: l'acqua a righe ripetute nel giro 1, le
  caustiche «come nebbia» nel giro 3, e Nicola: «sembra finta, eliminala, non
  stare a provare a generare acqua finta che non viene bene». → la metafora si
  prende da un artefatto del mestiere (nastri, cuciture, fibbie, tende,
  ottone): quello in CSS sembra vero perché è grafico. L'acqua, il cielo, il
  fuoco stanno solo dentro le foto. ([[sito-mikuma-dogs]])

- **GSAP e framer sovrascrivono il `transform` CSS al primo frame.** Un elemento
  centrato con `translate(-50%,-50%)` salta appena parte l'animazione. →
  centrare con `inset:0; margin:auto`, sfalsare con `margin-top`. Trovata su
  [[sito-castiglione]], [[sito-ngbarber]], [[sito-denkicode]] e
  [[sito-salone-di-andrea]]: quattro volte, quattro progetti.
- **rAF è fermo nei tab in background**: un sipario d'apertura resta eterno. →
  timer di sicurezza che porta l'intro a fine comunque.
- **La motion è additiva o non è.** `gsap.from` più CDN esterno: se il CDN manca
  o c'è `reduced-motion`, la pagina deve restare completa.
- **Il clamp CSS su `prefers-reduced-motion` non ferma le animazioni JS.** Con
  framer serve `MotionConfig reducedMotion="user"`.
- **Dosi che hanno funzionato**: massimo un pin per pagina, scrub 0.5-1.5,
  parallax solo sui layer immagine. Vengono dalla base dati di `ui-ux-pro-max`.
- **Un tween in attesa è layout.** `gsap.from` con `x:90` e uno
  ScrollTrigger che non è ancora partito tiene gli elementi 90 px a destra:
  se stanno al bordo, la pagina scrolla di lato. → `overflow-x:clip` sulla
  sezione, o la rivelazione in CSS con il fallback a tempo.
  ([[sito-osteria-tarilli]])
- **Un conteggio animato su un prezzo mostra un prezzo falso** per tutta la
  durata del tween, e una cattura lo fotografa: «CHF 34» per un brunch a 39.
  I numeri che impegnano non si animano. ([[sito-osteria-tarilli]])
- **Su mobile i trigger in sequenza si sovrappongono** e l'evidenziazione balla.
  → niente sequenza sotto i 640px, tutto acceso. ([[sito-ngbarber]])
- **Un motion value e un `animate` sullo stesso nodo si contendono la
  proprietà.** `style={{ scale: daScroll }}` più `animate={{ scale: 1 }}`:
  per tutta l'apertura la parallasse riscrive quello che l'animazione sta
  portando a 1. → due nodi annidati: fuori lo scroll, dentro l'apertura.
  ([[sito-albybike]])
- **Il fallback a tempo della rivelazione uccide la rivelazione.** Un timer
  che mostra tutto dopo 1,2 s su ogni elemento fa sì che sotto la piega sia
  già tutto acceso prima dello scroll. → il timer scatta solo con
  `document.visibilityState === "hidden"`: in una scheda che dipinge
  l'observer arriva. ([[sito-albybike]])
- **Una `transition` più specifica spegne quella della rivelazione.** `.rivela`
  (0,1,0) dichiarava `opacity, translate`; `.galleria .riquadro` (0,2,0) dichiarava
  `transform, box-shadow` per l'hover e vinceva: `transition-delay` 0 su tutti gli
  otto riquadri, lo sfalsamento a 70 ms non è mai esistito e nessuno l'ha visto
  finché le rivelazioni erano venti. Cugina del `transition-all` di Albybike. → le
  transizioni di un elemento si dichiarano tutte insieme nel selettore che vince
  (`.galleria .riquadro.rivela{transition: opacity, translate, transform,
  box-shadow}`), e si misura `transition-property` e `transition-delay` calcolati,
  non si guarda. Trovata dall'operatore su Opus. ([[sito-da-caterina]])
- **`transition-all` in coda a una classe che ha già la sua `transition` la
  spegne**: la utility vince e la curva condivisa sparisce. Trovata su due
  card che sembravano avere `hover-lift` e non lo avevano. → `grep
  transition-all` prima di dichiarare un linguaggio di motion unico.
  ([[sito-albybike]])

- `[TRAPPOLA]` **Pinnare solo la scena delle foto lascia fuori dal pin il
  pannello con testo e quadrante**, che scorre via mentre le foto restano
  ferme. → si pinna il contenitore intero (`.giro-dentro`), non il figlio.
  (operatore su Sonnet, [[sito-hairstylebrescia]], 16 settembre)

- `[TRAPPOLA]` **Il perno di rotazione di un `<g>` SVG non si imposta né con
  `svgOrigin` di GSAP né con `transform-origin` CSS + `transform-box:view-box`:
  sbagliano tutti e due, e a 375 px le lame delle forbici sparivano fuori dal
  viewBox. → si ruota con l'**attributo** `transform="rotate(a cx cy)"` scritto
  a mano. (16/09/2026, [[sito-barbershop-snia]])
- `[TRAPPOLA]` **Un path costruito in JS sugli ancoraggi della pagina va
  misurato con la catena `offsetTop`/`offsetParent`, mai con
  `getBoundingClientRect`.** Le rivelazioni (`translate 0 18px`) e i
  `position:sticky` spostano gli elementi mentre il path si misura, e il tratto
  nasce storto. (16/09/2026, [[sito-barbershop-snia]])
- **`getPointAtLength` in ricerca binaria a ogni frame non è un problema**:
  misurato su un path da 8.292 px, 18 iterazioni costano **0,56 ms** contro i
  16,7 di budget. Vale finché la `y` del path è monotòna — e va verificato che
  lo sia, o la ricerca binaria dà il punto sbagliato senza errore.
  (16/09/2026, [[sito-barbershop-snia]])

- `[TRAPPOLA]` **Uno ScrollTrigger che finisce a `bottom <n>%` sull'ultima
  sezione della pagina non si completa mai.** Il punto di fine sta oltre lo
  scroll massimo, la timeline resta a meta', e tutto quello che l'ultima parte
  doveva accendere non si accende: su [[sito-barbershop-snia]] il logo
  DenkiCode, messo a `opacity: 0` da `gsap.set`, non e' mai tornato visibile.
  → sull'ultima sezione si chiude a `bottom bottom`, **e quello che deve
  restare visibile non si affida a una timeline con scrub**: si rivela con
  l'observer, che un fallback ce l'ha. (16/09/2026)

- `[TRAPPOLA]` **Un `<svg>` alto quanto il documento che anima
  `stroke-dashoffset` ridipinge tutto il documento a ogni frame.** Su
  [[sito-barbershop-snia]] il filo stava in un SVG da 8.000 px: il calcolo
  della lunghezza costava 0,56 ms (misurato, non e' quello), ma l'area di
  raster era la pagina intera e sul Mac di Nicola si vedeva. → **l'SVG va
  `position:fixed` alto un viewport, con dentro un `<g>` traslato di
  `-scrollY`**: il path resta in coordinate di documento e l'area ridipinta
  passa da 8.000 px a uno schermo. ⚠️ **`viewBox` e altezza CSS devono
  coincidere** (`doc.clientHeight`, non `innerHeight`): se differiscono il
  disegno si scala in verticale e il filo si stacca dalla pagina di qualche
  punto percentuale. E il fisso vale solo con la motion viva: in `?cattura` e
  senza JS torna `absolute` e alto quanto la pagina, o nelle catture a pagina
  intera si vede solo nel primo schermo. (17/09/2026)
- **`scrub` di ScrollTrigger non e' morbidezza, e' ritardo.** A `.8` l'elemento
  arriva otto decimi di secondo dopo il dito e si legge come lag, non come
  eleganza. Su quello che deve sembrare attaccato allo scroll si usa
  `scrub: true`. (17/09/2026, [[sito-barbershop-snia]])
- **Un alone si fa con un cerchio, non con `drop-shadow`.** Un filtro si
  rasterizza a ogni frame in cui l'elemento si muove; un secondo cerchio piu'
  grande e trasparente no. (17/09/2026, [[sito-barbershop-snia]])

- `[TRAPPOLA]` **Un `transform` CSS, anche solo dentro dei keyframes, sostituisce
  l'attributo `transform` di un `<path>` SVG**: a fine animazione il pezzo torna
  all'origine del viewBox. → la posizione va nelle coordinate del path, non in
  un attributo. ([[sito-adelinanails]], 18/09/2026)
- `[TRAPPOLA]` **Un'animazione su `animation-timeline: view()` non ha durata**,
  quindi l'azzeramento di `animation-duration` in `base.css` non la ferma: sotto
  `prefers-reduced-motion` resta a metà. → si spegne per nome.
  ([[sito-adelinanails]], 18/09/2026)
- `[TRAPPOLA]` **`opacity:initial` nel blocco reduced-motion resetta anche le
  opacità dichiarate a mano** (un filetto a .7 diventa pieno). → si dichiara il
  valore finale vero, non `initial`. ([[sito-adelinanails]], 18/09/2026)

- `[TRAPPOLA]` **Un'animazione GSAP legata allo scroll resta ferma se allo script
  non arrivano eventi di scroll.** A pagina già scrollata (link con ancora,
  ricarica a metà, `scrollTo` programmatico) il rodovetro restava fuori schermo
  e al suo posto si vedeva carta vuota per due terzi del viewport. → la spina
  che deve stare «già a posto» va in CSS con `animation-timeline: view()`, che
  legge la posizione e non gli eventi; in GSAP restano i contatori e le scale.
  (24/09/2026, [[sito-p0t-tattoo]])
- `[TRAPPOLA]` **Con GSAP 3.13 la proprietà CSS `translate` viene azzerata appena
  si anima `x`/`y`**, e lo sfalsamento di un'ombra o di un livello sparisce.
  → gli sfalsamenti fissi si mettono in `inset`, non in `translate`.
  (24/09/2026, [[sito-p0t-tattoo]])
- `[TRAPPOLA]` **Il contorno di un font pesante fatto con `-webkit-text-stroke`
  mostra le sovrapposizioni interne dei glifi** (Unbounded 900). → `paint-order:
  stroke fill` e il pieno del colore della carta. (24/09/2026, [[sito-p0t-tattoo]])

- `[TRAPPOLA]` **GSAP che interpola una variabile CSS di colore letta da un
  altro elemento parte da trasparente**: il tween su `--luce` leggeva il valore
  iniziale come `rgba(0,0,0,0)` e il campo dentro l'arco si accendeva dal nero
  invece che dalla lacca precedente. → un campo per stanza con i suoi colori
  scritti fissi, e GSAP muove opacità e posizione, non il colore della
  variabile. (24/09/2026, [[sito-leibeautyroom]])

- `[TRAPPOLA]` **Lo script delle apparizioni dietro GSAP dalla CDN parte quando parte
  GSAP**: a freddo fino a 2,7 s, e chi scorre subito dopo il sipario trova carta
  nuda. Cugina della trappola del sipario di [[sito-designcapelli]]. → `motion.js`
  primo e sincrono, GSAP e ScrollTrigger `defer`, e quello che GSAP anima parte a
  `DOMContentLoaded`. (24/09/2026, [[sito-p0t-tattoo]])
- `[TRAPPOLA]` **In una scheda che non disegna fotogrammi le animazioni CSS non
  avanzano e `animationend` non arriva mai** (pannello nascosto, scheda aperta in
  secondo piano, `document.timeline.currentTime` fermo a 0). Se la fine
  dell'apertura o le apparizioni aspettano quell'evento, la pagina resta al primo
  istante: sipario su, tutto a opacità 0. → l'apertura ha un tetto duro (1,1 s o
  il primo scroll), niente sotto l'hero dipende dalla classe dell'apertura, e se
  entro 800 ms non arriva un `requestAnimationFrame` la pagina passa a uno stato
  senza motion, tutto rivelato. (24/09/2026, [[sito-p0t-tattoo]])

- `[TRAPPOLA]` **Un elemento chiuso da `clip-path` ha area zero e
  l'IntersectionObserver non lo vede mai entrare**: la porta chiusa non si
  apriva perché l'osservatore aspettava un'intersezione che non poteva
  esserci. → si osserva la stanza (la sezione), non la porta.
  (25/09/2026, [[sito-leibeautyroom]])

## CSS e layout

**`sticky` non entra nel padding del contenitore.** Su [[sito-barbershop-snia]]
(23/09) la foto del prima e dopo doveva restare ferma per 70vh sotto di sé: con
`padding-bottom:70vh` sul contenitore scorreva via lo stesso, perché lo sticky
è vincolato al content box. Funziona con contenuto vero, un `::after` con
`display:block;height:70vh`.

- `[TRAPPOLA]` **L'endpoint multi-famiglia di Fontshare serve la famiglia
  sbagliata, e il testo cade sul serif di sistema senza dire niente.** Chiedendo
  `?f[]=cabinet-grotesk&f[]=gambetta` in un solo `<link>` torna **Satoshi** al
  posto della seconda famiglia: `font-family: Gambetta` non trova niente e il
  browser ripiega in silenzio, quindi la pagina *sembra* solo un po' diversa. →
  **un `<link>` separato per ogni famiglia di Fontshare**, e dopo si controlla
  con `document.fonts.check()` che la famiglia chiesta sia davvero caricata.
  (21/09/2026, [[sito-designcapelli]])

- **Fra il punto in cui finisce lo scorrimento del telefono e quello in cui
  parte la griglia larga si apre una fascia senza nessuna delle due.** Su
  Barbershop SNIA, fra 761 e 900 px, ogni foto prendeva uno schermo intero e la
  pagina misurava **15.787 px contro 8.433 a 1024**: si scorreva a vuoto. →
  l'altezza del documento si misura su **tutte** le larghezze di prova, non
  solo a 375 e 1440; un salto del doppio è un buco fra due media query.
  (20/09/2026, [[sito-barbershop-snia]])

- **Una sezione chiamata `.dentro` prende il padding su ogni elemento
  rivelato: `dentro` è la classe di stato di `.rivela`.** Pagina alta 21.000 px
  a 1440, e il pannello del browser non lo mostrava: l'ha detto `scrollHeight`.
  → i nomi di sezione non riusano `dentro`, `js`, `cattura`, `rivela`, `aperto`.
  (19/09/2026, [[sito-barbershop-snia]])

- **Un bottone più lungo in barra non dà overflow di pagina: si sovrappone
  al marchio.** «Scrivimi su Instagram» in nav copriva «Mikuma.Dogs» di 50 px
  a 320 e `scrollWidth` restava uguale a `clientWidth`, perché il marchio ha
  `overflow: visible`. → il controllo della barra è la distanza fra il bordo
  destro del nome e il bordo sinistro del bottone, non l'overflow; sotto i
  480 l'etichetta si accorcia. ([[sito-mikuma-dogs]])
- **Il font di ripiego cambia la larghezza del titolo, e l'apertura parte dal
  posto sbagliato.** Archivo ripiega su Helvetica Neue, dove «MIKUMA DOGS»
  misura il 19% in piu': l'h1 nasceva su due righe, cinghia e fibbia si
  animavano 193 px sotto il posto loro e poi saltavano su all'arrivo del font.
  → `@font-face` di ripiego con `local()` e `size-adjust`, solo sul display,
  e la verifica si fa anche con `fonts.gstatic.com` bloccato: le posizioni
  devono coincidere. `size-adjust` manca prima di Safari 17. ([[sito-mikuma-dogs]])

- **`ease-[var(--x)]` in Tailwind 3 è ambiguo** («matches multiple utilities»)
  e la classe non viene generata. → `transitionTimingFunction` nominata nel
  config (`ease-fluid`). Idem per le durate: `transitionDuration` con i nomi
  della scala. ([[sito-albybike]])
- **React 18 non conosce `fetchPriority`**: warning in console e attributo
  camelCase nel DOM. → `{...{ fetchpriority: "high" }}` minuscolo.
  ([[sito-albybike]])

- **L'attributo `height` di `<img>` vince su `aspect-ratio` CSS.** Card alte
  1405px. → nel reset, `img { height: auto }`. Pagata su [[sito-castiglione]],
  ripagata identica su V-BAG.
- **`<use>` di un `<symbol>` non eredita gli stili del documento**: sette
  boccette nere al primo giro. → la grafica che prende colore da CSS va inline.
  ([[sito-nails-mania]])
- **Un `.wrap` con `margin: auto` dentro una flex column si shrink-wrappa.** →
  `width: 100%`. ([[sito-castiglione]])
- **Una griglia con `align-items:center` che diventa flex column su mobile
  centra anche in orizzontale**: un contenitore di soli figli assoluti si
  restringe a larghezza zero e i figli partono tutti dal centro. →
  `align-items:stretch` nella media query, o `width:100%` sul contenitore.
  ([[sito-osteria-tarilli]])
- **Un elemento ancorato al fondo dell'hero incontra il testo che cresce
  dall'alto** su un viewport basso (telefono con la barra del browser). Su
  mobile le decorazioni vanno in flusso dopo il CTA, non in assoluto.
  ([[sito-osteria-tarilli]])
- **La specificità produce bug invisibili a occhio**: `.nav-links a` batteva
  `.btn` e il CTA in nav era verde su verde. Si trova misurando il contrasto,
  non guardando lo screenshot.
- **Un CTA che wrappa su due righe a 375px si toglie, non si comprime.**
- **Un `<a>` con `flex-basis:100%` è cliccabile su tutta la riga**: 1.296 px a
  1440 per una scritta da 178. Il link va dentro un blocco (`<p>`) che prende
  la riga, e resta `inline-flex` a misura del suo contenuto. Trovata misurando
  `getBoundingClientRect().width` della firma DenkiCode, non guardando.
- **Una classe corta è già presa da qualcun altro**: `.firma` su Atelier Selva
  era la scritta a mano della titolare, e il CSS nuovo l'avrebbe rimpicciolita.
  `grep -n 'class="[^"]*nome'` prima di aggiungere una regola globale.
- **Una voce in piu' in nav non si misura a 1440 e 375**: li' e' sempre a
  posto. Rompe nella banda stretta in mezzo — su [[sito-fiftynine]] la quinta
  voce sforava di 36px fra 761 e 899, dove il resto ci stava per un pelo. → si
  misura `nav.scrollWidth - nav.clientWidth` sui bordi di ogni media query, e
  la voce nuova prende il suo punto di rottura.
- **Una regola di componente che imposta `display` batte `[hidden]`.** Il
  browser dà `display:none` agli elementi con l'attributo, ma `button.link-line
  { display: inline-flex }` ha più specificità: il nodo resta a schermo con
  `hidden` messo, e il JS che lo nasconde sembra rotto. Sul sito di Giulia il
  pulsante «Esci» si vedeva prima del login. → `[hidden] { display: none
  !important }` nel reset, una volta per tutte. (sito V-BAG di Giulia, 7 settembre)

- **`17ch` su un display serif fa 1.713 px.** Su Bodoni Moda lo `0` di
  riferimento è larghissimo, quindi una misura pensata per «diciassette
  caratteri» esce larga quanto lo schermo e il titolo non va mai a capo dove
  deve. → **i tetti di un display si scrivono in `em`, mai in `ch`**: `ch`
  dipende dal font e cambia sotto ai piedi al primo cambio di famiglia o al
  ripiego. ([[sito-laurafranzoni]], 14 settembre)
- **Una regola più specifica vince anche su `max-width`, non solo sui colori.**
  `.atto--occhi .colonna > p` batteva `.richiamo` e il richiamo prendeva la
  misura del paragrafo normale: la classe c'era, l'HTML era giusto, e la riga
  era lunga il doppio. → si misura `getBoundingClientRect().width` calcolata,
  non si guarda la classe nell'HTML. Cugina della `transition` più specifica di
  [[sito-da-caterina]]. ([[sito-laurafranzoni]], 14 settembre)

- `[TRAPPOLA]` **`clamp(4rem,10vw,11rem)` non garantisce una riga sola.** Su un
  h1 lungo 14,45 em il termine centrale si scollega dalla larghezza del
  contenitore e il titolo va a capo dove non deve. → il tetto si lega al
  contenitore: `min(11rem, 6.85cqw)`, misurato sul numero di em del titolo.
  ([[sito-nails-robyy]], 13-14 settembre)
- `[TRAPPOLA]` **Il font di ripiego può stringere, non solo allargare.** Su
  Helvetica Neue il titolo usciva più stretto del definitivo e serviva
  `size-adjust:109.4%`, mentre su [[sito-mikuma-dogs]] serviva 84%. → il
  valore si misura ogni volta, non si copia da un altro sito.
  ([[sito-nails-robyy]], 13-14 settembre)
- `[TRAPPOLA]` **Il testo dentro un `<svg>` scala col `viewBox`.** Le etichette
  di una quota diventano illeggibili o enormi a seconda della larghezza, e la
  dimensione in CSS non le tiene. → nel disegno restano i tratti, **le etichette
  si scrivono in HTML** sopra l'SVG, posizionate in percentuale.
  ([[sito-nails-robyy]], 13-14 settembre)
- `[TRAPPOLA]` **`img,svg,video{max-width:100%}` di `base.css` annulla una
  larghezza sopra il 100%.** Un SVG che deve sbordare resta incastrato nel
  contenitore e la regola nuova sembra ignorata. → `max-width:none` sul singolo
  disegno; `base.css` non si tocca. ([[sito-nails-robyy]], 13-14 settembre)
- `[TRAPPOLA]` **La barra su una riga sfondava di 5 px a 901.** Stesso caso
  della quinta voce di [[sito-fiftynine]] fra 761 e 899: a 1440 e 375 era a
  posto. → si misura sui bordi di ogni media query, e «CORSI» tagliato in barra
  si vede solo lì. ([[sito-nails-robyy]], 13-14 settembre)
- `[TRAPPOLA]` **`grid-row: 1 / -1` su una griglia senza `grid-template-rows`
  non arriva all'ultima riga.** `-1` si risolve sulla **griglia esplicita**, che
  lì è una riga sola: l'elemento resta in riga 1, la fa alta quanto lui e stira
  il contenuto accanto dentro quel vuoto. → con righe implicite serve
  `grid-row: 1 / span N`, o le righe si dichiarano.
  ([[sito-nails-robyy]], 14 settembre)

- **Un padding che alza la barra sticky sposta le ancore sotto la barra.** Su nails.robyy l'area di tocco del link in barra (padding 15px) ha portato la barra da 97 a 109px e `#corsi` finiva coperto: `scroll-padding-top` va rialzato insieme, e misurato con `getBoundingClientRect` dopo il salto. ([[sito-nails-robyy]], 14/09/2026)

- `[TRAPPOLA]` **`figcaption` dentro un `<figure>` con `aspect-ratio` e
  `overflow:hidden` resta tagliata e invisibile.** → `aspect-ratio` e
  `overflow` vanno sull'`<img>`, non sul `figure` che contiene anche la
  didascalia. (operatore su Sonnet, [[sito-hairstylebrescia]], 16 settembre)

- `[TRAPPOLA]` **Non si ripulisce un CSS con una regex `\.classe\{.*?\n\}` in
  DOTALL.** Il `.*?` non si ferma alla graffa della regola: si ferma al primo
  `\n}` che trova, e se la regola da togliere e' multiriga si porta via tutto
  quello che sta in mezzo. Il 17/09/2026 su [[sito-barbershop-snia]] ha
  cancellato 134 righe, fra cui l'intero blocco dei bottoni, e la pagina e'
  andata in cattura con i bottoni ridotti a testo. → si ripristina con
  `git checkout HEAD -- <file>` e si rifa' a **sostituzioni di stringhe
  esatte**, una per blocco, che falliscono rumorosamente se il blocco e'
  cambiato.

- `[TRAPPOLA]` **`scrollbar-color` con un colore pieno dipinge una barra sul
  bordo destro che in cattura sembra un elemento fuori griglia.** →
  `scrollbar-width:thin` e colore a metà opacità. ([[sito-adelinanails]],
  18/09/2026)

- `[TRAPPOLA]` **L'overflow di pagina a 0 non vede un titolo che esce dalla
  propria scheda.** Una parola sola in un display largo («Scaramanzia»,
  «Prenotazioni») non va a capo e sfora il contenitore senza allargare il
  documento. → si misurano i `getBoundingClientRect` dei titoli contro il
  contenitore; cura: `container-type` e corpo in `cqi`. ([[sito-adelinanails]], 18/09/2026)

- `[TRAPPOLA]` **`container-type:inline-size` dentro una griglia con colonna
  `auto` e `justify-content:center` misura 0 px**: la larghezza intrinseca del
  contenitore è 0 e il testo va a una parola per riga. La sonda «titolo contro
  contenitore» non lo vede, perché anche il contenitore è a 0. → colonna
  esplicita `minmax(0,1fr)` e `width:100%`. ([[sito-adelinanails]], 19/09/2026)

- `[TRAPPOLA]` **`text-indent` si eredita dentro gli `inline-block`**: la
  citazione scritta parola per parola (una `span` per parola) mangiava lo
  spazio prima di ogni parola. → `text-indent: 0` sulle `span`, o l'indent
  solo sul contenitore con `display: block`. (25/09/2026, [[sito-leibeautyroom]])

## Git, account e pubblicazione

- `[TRAPPOLA]` **Un `[[redirects]]` di Netlify senza `force = true` non scatta
  se il file esiste davvero.** Su Custom Beauty Nails la regola che doveva
  nascondere `BRIEF.md` era scritta e il file rispondeva `200` online: il
  nostro processo, le didascalie e le misure erano leggibili da chiunque avesse
  l'indirizzo. → nei siti bozza si sbarrano **con `force = true`** tutti i file
  di lavoro (`BRIEF.md`, `PRODUCT.md`, `DESIGN.md`, `strumenti/`,
  `originali/`), e si verifica con `curl` che rispondano 404, non che la regola
  sia scritta. ⚠️ **`/.netlify/*` e' riservato e il redirect non lo ferma**: il
  badge «Powered by Netlify» si spegne solo dal pannello del progetto.
  (16/09/2026, [[sito-custombeautynails]])

- **`gh` tiene un solo account nel keyring.** Con due account, il push sulla repo
  dell'altro dà `403` o `Repository not found`, e sembra un problema del repo. →
  `gh auth login` con l'account giusto. La paternità dei commit è un'altra cosa
  ancora: la decide il `git config` locale del repo.
- **`gh repo create --push` passa e il push successivo no**: il primo usa il
  proprio helper. → si svuota l'helper e si rimette quello di `gh`.
- **`Cache-Control` lungo su `assets/*` tiene il CSS vecchio sul telefono del
  cliente per una settimana.** Su Tarilli la regola di Fiftynine, che era su
  `assets/img/*`, e' stata allargata a `assets/*`: la correzione era online e
  l'iPhone di Nicola vedeva ancora il difetto. → CSS e JS con
  `max-age=0, must-revalidate` (Netlify rivalida con ETag) e un `?v=` nel
  link; la cache lunga resta solo alle foto. ([[sito-osteria-tarilli]])
- **`netlify deploy --prod` senza `--no-build` prova a installare plugin in
  `.netlify/plugins/` e puo' fallire li'** anche su un sito statico senza
  build: `--no-build`, e `.netlify/` nel `.gitignore`.
  ([[sito-osteria-tarilli]])
- **Il sito Netlify creato dal CLI non e' collegato al repo**: un push non
  ripubblica, il deploy si rilancia a mano con `--site <id>`.
- **Una bozza non commissionata non si fa indicizzare.** Tre sbarramenti (`meta
  robots`, `X-Robots-Tag`, `robots.txt`) che si tolgono quando il sito diventa
  loro: indicizzarla mette un secondo sito col nome del lead su Google, cioè un
  danno fatto prima della vendita. Sta in [[netlify]].
- **Le credenziali non le digito io.** `netlify login` apre il browser e chiede
  l'accesso di Nicola: si prepara tutto e ci si ferma lì. [[credenziali]]

- `[TRAPPOLA]` **`netlify sites:create --name X` con un nome già preso crea
  `X-NNN` e non dà errore.** `newfantasy` era di qualcun altro: è uscito
  `newfantasy-306`, e il deploy ci è finito sopra. → si legge l'URL stampato
  prima di pubblicare, e se ha il suffisso si cancella (`sites:delete <id>
  --force`) e si ricrea con un nome libero. Il CLI non è in `npx --no-install`
  ma nella cache: `~/.npm/_npx/da5c1b6ea715e8b4/node_modules/.bin/netlify`.
  ([[sito-newfantasy]], 16 settembre)

- `[TRAPPOLA]` **Il deploy dal CLI di Netlify pubblica tutta la cartella**:
  `/catture/` (le schermate di lavoro) e `/assets/img/vere/` (gli originali
  delle foto, compreso il ritratto coi diritti da verificare) rispondevano 200
  online fino al giro 4, anche se fuori da git. → in `netlify.toml` una regola
  `404` per `/catture/*` e `/assets/img/vere/*`, verificata con `curl`; e
  `MONDO.md`, `PRODUCT.md`, `LEGGIMI.md` si controllano allo stesso modo.
  (25/09/2026, [[sito-leibeautyroom]])

## Far modificare il sito al cliente

- **Netlify Blobs si prova in locale col protocollo vero, non con un finto.**
  `BlobsServer` da `@netlify/blobs/server` più `NETLIFY_BLOBS_CONTEXT` (JSON in
  base64 con `edgeURL`, `uncachedEdgeURL`, `siteID`, `token`): funzione ed edge
  function girano in Node come su Netlify. Online, per sapere se l'archivio
  risponde senza entrare con la parola vera: una parola volutamente sbagliata
  deve dare 401 (l'archivio è stato letto), non 500. ([[sito-fiftynine]])
- **Il classificatore di Claude Code, in modalità automatica, ferma le azioni
  che indeboliscono la sicurezza anche quando le chiede Nicola**: togliere una
  regola sulle credenziali dal `CLAUDE.md`, scrivere una parola d'ordine nel
  codice di un repo pubblico, far pubblicare una pagina con una parola debole.
  → non si aggira e non si provano varianti: si mette il lavoro da parte, si
  dice cosa è stato fermato, e Nicola cambia la modalità dei permessi se vuole
  procedere. ([[sito-fiftynine]], 23 settembre 2026)

- **Netlify non serve l'HTML come sta nel repo.** Con le rielaborazioni accese
  riscrive i link (`menu.html` → `/menu`, e con loro le virgolette del tag), e
  inietta un commento e uno script suo prima di `</body>`. Una pagina di modifica
  che legge l'HTML dal sito e lo riscrive nel repo lo sporca a ogni salvataggio,
  e gli script iniettati si moltiplicano. → **si legge dal repo** (Contents API
  con `accept: application/vnd.github.raw+json`), mai dal sito; e per sapere se
  un deploy è arrivato non si confronta il file intero, si cerca un segno
  scritto apposta (una `meta` con la versione). ([[sito-fiftynine]])

- **Con uno store a file, pubblicare vuol dire fare un commit.** Un sito statico
  non scrive su sé stesso: `dati/*.json` più le foto è la soluzione più leggera e
  regge finché le voci sono poche, ma l'ultimo passo lo fa chi ha il repo. Dal
  telefono il cliente non ci arriva proprio, e va detto prima di prometterlo.
  Se deve pubblicare da solo davvero, serve qualcosa di ospitato.
- **`showDirectoryPicker` va chiamato per primo dentro il gestore del click, prima
  di qualunque `await`.** Dopo un `await` l'attivazione utente è scaduta e il
  picker fallisce senza spiegare perché. Vale per tutta la File System Access API.
  Esiste solo su Chrome ed Edge da computer: su iOS non c'è.
- **Un file di dati servito da un server statico arriva dalla cache.** Con
  `Last-Modified` e nessun `Cache-Control` il browser tiene la copia vecchia, e
  la cosa appena pubblicata non si vede. → `fetch(url, { cache: 'no-cache' })`,
  che non salta la cache ma la fa rivalidare: se non è cambiato torna un 304.
- **Due download di fila: il secondo il browser lo lascia cadere.** Vanno
  distanziati di qualche centinaio di millisecondi.
- **Lo store puo' essere l'HTML stesso, non un JSON di fianco.** Ogni pezzo
  modificabile fra due commenti (`<!-- @menu pizze -->` … `<!-- /@menu -->`),
  si legge con `DOMParser` e si riscrive **solo quello che sta fra i due**: il
  resto del file non lo tocca nessuno. Costa piu' codice nella pagina di
  modifica, ma la pagina pubblica **resta statica** — con lo store a JSON un
  menu' senza JS e' un menu' vuoto, e su un listino di bar e' il contenuto
  principale. ([[sito-fiftynine]])
- **Scappare l'apice dritto nel testo rende ogni salvataggio illeggibile.**
  `'` → `&#39;` riscrive quarantaquattro righe di pizze per un prezzo cambiato,
  e il diff non dice piu' niente. → due funzioni: nel testo si chiudono solo
  `& < >`, nell'attributo anche `"` e `'`. Il giro completo deve lasciare il
  file **identico al byte**, ed e' la prima cosa da provare.
- **Se una regione marcata non si trova, si alza un errore.** Non si scrive
  alla cieca: vuol dire che il file e' cambiato sotto, e sovrascriverlo perde
  il lavoro di qualcun altro.

## Supabase e chiavi nel browser

- **La chiave anon è pubblica per definizione**: sta in chiaro nel JS che scarica
  chiunque. Non è un problema di per sé, lo diventa se le RLS si fidano del solo
  `authenticated`: basta che le registrazioni restino aperte e uno sconosciuto si
  iscrive, diventa `authenticated` e scrive. → le policy controllano **chi**
  (`auth.jwt() ->> 'email'`), non solo *se* è collegato. La `service_role` non
  entra mai in un file servito al browser.
- **Meglio fallire chiusi.** Il segnaposto della mail in `supabase.sql` fa sì che
  finché non è stato configurato non pubblichi nessuno, nemmeno chi di dovere. Un
  interruttore nel pannello che ci si dimentica fallisce aperto, ed è peggio.
- **401 e 403 non sono la stessa cosa**: il primo è la sessione scaduta, il
  secondo è il database che dice di no. Mandano l'utente a fare due cose diverse
  e vanno scritti come due messaggi diversi.

## Scraping

- `[TRAPPOLA]` **In zsh una variabile di ciclo che si chiama `path` cancella il
  `PATH`.** `while IFS='|' read -r q host path name` e dalla riga dopo `curl`,
  `ls` e `sed` rispondono `command not found`: in zsh `path` è l'array legato a
  `PATH`, e assegnarlo lo sostituisce. → nei cicli non si usano `path`, `cdpath`,
  `fpath`, `manpath`. (21/09/2026, [[sito-designcapelli]])

- `[TRAPPOLA]` **Da Instagram senza login si scende a 640 px e non più in giù,
  e l'URL è firmato.** Cambiare `s640x640` in `s1080x1080` dentro `stp=` fa
  rispondere al CDN **`URL signature mismatch`** e scrive un file di 22 byte con
  quel testo dentro — non un JPEG rotto, proprio un file finto. La pagina del
  singolo post rimanda al login e anche il suo `og:image` è a 640. → o si accetta
  che le foto sono sotto il minimo di 1080 e **il sito non dipende da loro**, o
  si chiedono gli originali al cliente. E dopo ogni scaricamento si controlla con
  `sips -g pixelWidth`: un file da 22 byte non è una foto.
  (21/09/2026, [[sito-designcapelli]])

- **Gli URL delle foto Instagram scadono** (firme CDN a giorni). → si scaricano
  in locale subito, nella stessa sessione.
- **La bio troncata e le caption si leggono senza login.** La bio intera sta
  nel `meta name="description"` della pagina profilo; la caption di ogni
  post nell'`og:title` di `instagram.com/<utente>/p/<id>/`, con `curl`.
  Il pannello mostra le prime dodici anteprime a 640 px e poi chiede il
  login. ([[sito-osteria-tarilli]])
- **L'handle esatto va chiesto, non indovinato.** `castiglione_furniture` è
  inglese: quattro username italiani tentati, zero risultati, risolto da uno
  screenshot di Nicola.
- **Il dump grezzo dello scraping non si committa.** Su [[sito-ngbarber]] è
  finito nel commit iniziale di una repo pubblica e adesso resta nella storia.
- `[TRAPPOLA]` **Il modale di login blocca il caricamento della foto grande.**
  Nel pannello browser il DOM del post si legge prima che l'immagine esista:
  `naturalWidth` non trova niente e si conclude che il post non ha foto — 3 post
  su 9 riusciti. → `navigate` → `wait 5` → `Escape` → `wait 2` → lettura.
  (13/09/2026, [[sito-laurafranzoni]])
- `[TRAPPOLA]` **L'alta risoluzione sta nella pagina del singolo post, non nella
  griglia.** Da sloggati `instagram.com/<utente>/p/<id>/` serve l'immagine alla
  taglia nativa (fino a 3024×4032), mentre la griglia si ferma a 640 px. Nei
  caroselli le slide oltre la prima si caricano solo cliccando «Avanti».
  (13/09/2026, [[sito-laurafranzoni]])
- `[SCARTATO]` **Alzare `s640x640` nell'URL di `og:image`.** Non funziona più: la
  firma `oh=` copre anche il parametro di taglia e la CDN risponde 403. Vale
  anche per la foto profilo, che resta a 150×150 e dall'URL non si ingrandisce.
  (13/09/2026, [[sito-laurafranzoni]])
- `[TRAPPOLA]` **Il bottone «altro» della bio non ha nome accessibile.** La bio
  arriva troncata e il click a coordinate lo manca. → si prende il `ref` da
  `read_page` con filtro `interactive` e si clicca quel riferimento.
  (13/09/2026, [[sito-laurafranzoni]])
- `[SCARTATO]` **`api/v1/users/web_profile_info`** da sloggati risponde 401
  `require_login`: il profilo non si legge da lì. (13/09/2026,
  [[sito-laurafranzoni]])

- `[TRAPPOLA]` **Finché il modale di login è aperto, la foto grande non esiste
  nel DOM**: `document.images` contiene solo le anteprime della griglia a 640.
  Cugina della trappola di [[sito-laurafranzoni]], con la chiusura a
  coordinate: la X sta a **`dialog.right − 16`, `dialog.top + 14`**, e dopo il
  click arrivano le 1440. ([[sito-nails-robyy]], 13-14 settembre)
- `[TRAPPOLA]` **`window.__fn` non sopravvive alla `navigate` del pannello.**
  Una funzione definita per raccogliere gli URL sparisce al post dopo e lo
  script risponde `undefined`, come se il selettore fosse sbagliato. → si
  ridefinisce dopo ogni navigazione, o si legge tutto in una sola valutazione.
  ([[sito-nails-robyy]], 13-14 settembre)

- `[TRAPPOLA]` **Le pagine dei post da `curl` tornano il guscio di login senza
  `og:`.** Il 15/09/2026 dodici post su dodici rispondono 623 KB senza
  `og:title` né `og:image`: la didascalia si legge solo dal pannello, con
  `get_page_text` a modale aperto (il testo di `<main>` arriva lo stesso), e
  l'`h1` non esiste. Il `meta description` del profilo idem. La voce sopra su
  `curl` vale fino a quella data. ([[sito-newfantasy]])
- `[TRAPPOLA]` **Su Facebook la stessa foto Instagram si ingrandisce dall'URL,
  fino a `cstp=mx…`.** La pagina `/photos` da sloggati mostra le anteprime a
  414 px con `ctp=s552x414&cstp=mx1152x1152`: si alza `ctp` fino al valore di
  `cstp` e arriva a quella taglia. Togliere il prefisso di ritaglio
  (`c0.95.1152.1152a`) risponde 403. Serve per i post più vecchi dei dodici
  visibili su Instagram, e per la copertina, che è a 946×2048.
  ([[sito-newfantasy]])

- `[TRAPPOLA]` **La taglia vera della foto sta nel parametro `efg` dell'URL, ed e'
  base64.** `atob(efg)` restituisce il tag di encoding: dentro c'e'
  `regular_photo` con la larghezza (1080, 1350, 1440) oppure
  `video_first_frame_thumbnail` a 640. Filtrando li' si separano le foto dai
  fotogrammi dei Reel **senza scaricarle**, e si evita di impaginare copertine a
  640 px. Cercare `regular_photo` nell'URL non decodificato non trova niente.
  (16/09/2026, [[sito-shaddai]])
- `[TRAPPOLA]` **Da loggati il grid non carica altri post se il pannello e'
  nascosto.** Sette scroll programmati, bottino fermo a dodici immagini: senza
  pannello visibile non scattano gli IntersectionObserver, la stessa causa della
  pagina bianca di [[sito-castiglione]]. Per un profilo da cento post il primo
  schermo basta; sopra, o si mostra il pannello o si va per URL dei singoli post.
  (16/09/2026, [[sito-shaddai]])

- `[TRAPPOLA]` **Il DNS di questa sandbox non risolve i sottodomini `netlify.app`
  appena creati**, e `curl` esce con codice 6 e `%{http_code}` 000 — che si legge
  come «il sito è giù», mentre il sito sta benissimo. `host` invece li risolve,
  quindi non è il DNS di sistema: è il risolutore del processo. Il 17/09/2026
  `pinkploy.netlify.app` rispondeva 200 e `barbershop-snia.netlify.app` e
  `custombeautynails.netlify.app` no. → **la verifica dei tre sbarramenti si fa
  sul permalink del deploy pubblicato**, che risolve:
  `https://<deploy-id>--<sito>.netlify.app`. L'id del deploy vivo si legge con
  `netlify api getSite`, campo `published_deploy.id`, ed è esattamente quello che
  la produzione serve. ([[sito-barbershop-snia]])

- `[TRAPPOLA]` **La galleria «Foto» di una scheda Google Maps, aperta nel
  pannello browser con un account Google dentro, mescola alle foto del locale
  un carosello di foto personali dell'account** (un supermercato, una
  biblioteca, un rifugio), sotto lo stesso prefisso `lh3.googleusercontent.com`.
  Raccolte per prefisso URL sarebbero finite nella cartella del cliente. → si
  isolano per posizione nel DOM della galleria del locale, non per prefisso, e
  si guardano una per una prima di tenerle. (25/09/2026, [[sito-leibeautyroom]])
- `[TRAPPOLA]` **Anche `instagram.com/p/<shortcode>/embed/captioned/` da `curl`
  torna il guscio di login** (25/09/2026): la strada dell'embed, che il 15/09
  passava, è chiusa. Le foto vere del locale sono arrivate dalla galleria di
  Google Maps nel pannello browser (4 su 6, «dal proprietario»), non da
  Instagram. → per un centro senza foto nel feed si parte da Google Maps.
  (25/09/2026, [[sito-leibeautyroom]])

## Liste e banco DM

- **Una frase di verifica ripetuta su sessanta righe è un modello, non un
  controllo.** Lista dell'8 settembre: 62 righe su 68 con la stessa frase,
  almeno 20 su 72 col sito. → ogni riga dice cosa è stato cercato e cosa è
  uscito; `02-Sales/strumenti/controlla-lista.py` ferma la lista prima della
  pubblicazione. [[contattati]]
- **I motori di ricerca senza chiave non reggono una lista.** DuckDuckGo html
  risponde 403 dopo ~50 richieste, Brave 429 dopo ~10, Bing ignora le
  virgolette e risponde con un'altra città. → la base è quello che non dipende
  da nessuno: indovinare i domini dal nome e aprirli (`verifica-sito.py`); i
  motori sono un extra con 12 s di pausa. Il 25/9, partiti a 2,5 s, DuckDuckGo
  ha dato la pagina anti-bot alla quarta ricerca, **con status 200**: lo script
  la contava come «zero risultati». Adesso la riconosce e la scrive nella riga.
  [[2026-09-25-barbieri-piemonte-e-ricerca]]
- **Su companyreports i codici ATECO 2025 sono liste a parte.** `52.24`
  (movimentazione merci) non sta dentro `52.24.4`, `90.02.01` non sta dentro
  `90.02.09`: il 25/9 il primo giro li ha persi, 99 facchinaggi solo in Lombardia.
  → per ogni settore si scaricano sia il codice 2007 sia il 2025. [[2026-09-25-opero-facchinaggio]]
- **Una regola scritta cede sotto il volume.** «Verificato, mai dedotto» stava
  nel metodo dal 30 agosto ed è stata violata su 62 righe. → il passo si
  trasforma in uno script che scrive la prova nella riga, e un secondo script
  rifiuta la lista senza prova. La regola resta, ma non è più lei a reggere.
- **`python3 -m http.server` non scrive niente.** Se il browser deve lasciare
  traccia nel vault serve un handler `POST` (stdlib, `banco-server.py`): il
  file si aggiorna sul disco di chi clicca, e nel brain arriva solo col push —
  che il server fa da solo, con un timer, e alla chiusura via segnale. Con
  `SIGKILL` il timer non parte e il commit si perde.

- **Un recupero calcolato sul calendario e non sulla chat riscrive a chi ha
  detto no.** Il banco marcava «da ricontattare» ogni riga con quattro giorni
  lavorativi e nessun esito: il 12 settembre erano 74 profili, e dentro c'erano
  cinque che avevano gia' risposto «non siamo interessati» o «ho gia' un sito».
  → il criterio guarda quello che e' successo nella chat: ha letto il
  messaggio, oppure ha risposto a mano. Chi non ha mai aperto la chat non e' un
  recupero, e un no non torna mai. [[metodo-liste]]
- **L'ultimo messaggio di una conversazione mente: sono i saluti.** Corretti i
  74 recuperi guardando «la risposta», il banco ne proponeva ancora due, e
  tutti e due erano dei no: @tattooextreme aveva aperto con «guarda non mi
  interessa grazie» e chiuso con «ok grazie», @biumotattooclub con «ti
  ringrazio ma non siamo interessati» e tre emoji. Patrick: «devi leggere tutta
  la chat». → la colonna si chiama `Chat` e contiene **tutti** i messaggi loro
  separati da « | »; un rifiuto trovato in qualunque punto chiude la riga per
  sempre. E nella direzione opposta si guadagna quello che l'ultimo messaggio
  nascondeva: il «lunedi` meglio» di Mikuma Dogs era il quinto messaggio su
  sette, ed era **una chiamata da fissare**, la cosa piu' calda di tutta la
  posta. Chi ha fissato un momento salta l'attesa dei quattro giorni e sta in
  cima: un appuntamento ha una data sua, e aspettare lo fa scadere.
- **Un esito scritto in colonna faceva sparire il lead piu' caldo.** La stessa
  pagina escludeva ogni riga con un `Esito DM` qualsiasi, e «Risposta — in
  valutazione» e' un esito: le quattro trattative aperte finivano fra i «gia'
  contattati» con centosessanta righe morte, dove nessuno le guardava piu'.
  Shari Tattooer e' stata ferma otto giorni per questo. → gli esiti si dividono
  in due: quelli che chiudono (scartata, un no, ce l'aveva il sito) e quelli
  che tengono aperto. I secondi stanno in cima ai recuperi, non in fondo ai
  fatti.
- **`regola.py` cercava «## Regole» come sottostringa.** In un file il cui
  titolo era `## Regole date a voce` ha inserito la regola dentro il titolo,
  lasciando « date a voce» orfano sotto il testo. → il titolo si cerca come
  riga intera con una regex, e la regola si infila davanti alla prima `###`,
  cioe' dopo l'eventuale riga che spiega la sezione.

## Skill e strumenti di processo

- **`voce-denkicode` sulle didascalie e sul copy di un sito produce frasi da
  bambino.** Taglia connettivi e verbi e lascia frasi nominali che descrivono
  la foto («Ghiaia da una parte, erba dall'altra», «Sostenuto finché non si
  fida del fondo che non c'è»). Nicola su Mikuma Dogs: «sembra che non sai
  l'italiano, scrivi solo cose utili». → il copy di un sito vetrina lo scrive
  il direttore nel brief, frase per frase, e l'operatore lo inserisce senza
  riscriverlo. Ogni frase ha un verbo e dice una cosa utile a chi legge; una
  didascalia descrive il servizio, non la foto, o non c'è. Le frasi prese dai
  post del cliente entrano solo se sono utili. Il metro è NN/g: conciso,
  scandibile, oggettivo, mai promozionale. ([[sito-mikuma-dogs]])

- **Lo script di `ui-ux-pro-max` non sta dove la skill dice.** Il percorso
  `.claude/skills/ui-ux-pro-max/scripts/search.py` sotto la cartella del
  plugin non esiste, e `find` non trova nessun `search.py`. Il passo 4 del
  processo si salta e si dichiara, finché non si trova la copia giusta.
- **Il `build-phase` di impeccable è solo comp-led**: senza generatore di
  immagini si ferma a «comps». Il percorso code-led è previsto dal
  playbook e non passa da lì; il brief di superficie si scrive con
  `impeccable surface-brief write <target> <file>` e finisce in
  `.impeccable/surfaces/`.
- **La pagina di decisione senza nessuno davanti resta aperta per sempre.**
  Si aspetta un tempo dichiarato (due giri da 60 s), poi si costruisce
  l'assegnata e lo si scrive. Se il `--wait` risponde `PAGE CLOSED` (la
  scheda del pannello e' stata riusata), vale lo stesso: assegnata, senza
  aprire un secondo server. ([[sito-da-caterina]])
- **I ritagli senza sfondo si fanno con Vision di macOS, senza installare
  niente**: `VNGenerateForegroundInstanceMaskRequest` in uno script Swift di
  venti righe (`ritaglia.swift`, compilato con `swiftc`), PNG con alfa
  rifilato al soggetto. `rembg` e PIL non ci sono e non servono. Il bordo
  bianco fustellato poi e' CSS: sei `drop-shadow` a offset 0 blur piu' uno
  sfalsato per l'ombra. ([[sito-da-caterina]])

- `[TRAPPOLA]` **`netlify` non è nel PATH di questa shell.** `command not found`
  non vuol dire che manchi: → `npx --no-install netlify` (27.5.2) lo trova e
  pubblica. ([[sito-nails-robyy]], 13-14 settembre)
- `[TRAPPOLA]` **`impeccable-finish-reviewer` e `impeccable-documenter` hanno
  `model: inherit`**, cioè girano sul modello del direttore (Fable) e bruciano
  la percentuale che serve a dirigere. → si passa `model: opus` esplicito a ogni
  invocazione. ([[sito-nails-robyy]], 13-14 settembre)
- `[TRAPPOLA]` **Il classificatore dell'auto mode blocca i comandi combinati in
  una riga.** Lo stesso lavoro spezzato in due comandi passa senza chiedere
  niente. → non si accorpano con `&&` i comandi di una catena lunga.
  ([[sito-nails-robyy]], 13-14 settembre)

- `[TRAPPOLA]` **Un operatore di costruzione su Opus muore due volte in un
  modo diverso.** La sera del 15/09 per limite di sessione (reset alle 3:10),
  la mattina dopo per stallo a 600 s mentre scriveva l'`index.html` intero in
  un colpo. → il file grande si scrive a pezzi, e se il giro muore due volte
  il direttore costruisce da sé con la catena caricata invece di rilanciare
  una terza volta. ([[sito-newfantasy]], 16 settembre)

- `[TRAPPOLA]` **`npx --no-install netlify` non trova più il CLI**: vuole
  `netlify@27.7.0` e si ferma. La copia buona sta nella cache di npx,
  `~/.npm/_npx/b3ca12a867cd0704/node_modules/.bin/netlify` (27.5.2), loggata
  come Nicola, team `denkicode`. → si chiama quel binario col percorso intero.
  ([[sito-hairstylebrescia]], 16 settembre)
- `[TRAPPOLA]` **Il classificatore dell'auto mode marca «Production Deploy»
  anche `curl` e la navigazione del pannello verso il sito Netlify appena
  pubblicato**, non solo il deploy. `sites:create` e `deploy --prod` passano
  se lanciati **uno per comando**; la verifica dei tre sbarramenti sul sito
  vivo resta bloccata. → si dichiara il buco e il `curl` lo lancia Nicola.
  ([[sito-hairstylebrescia]], 16 settembre)

- `[TRAPPOLA]` **`translate(42%)` dentro `transform` misura l'elemento, non il
  contenitore.** Undici attrezzi che dovevano stare su un anello intorno alla
  foto stavano tutti al centro, a 23 px. → `container-type:inline-size` sul
  contenitore e il raggio in `cqw`. ([[sito-newfantasy]], 16 settembre)

- `[TRAPPOLA]` **`preview_start` legge `launch.json` dalla cartella della
  sessione, non dal repo del sito.** Da una sessione aperta nel vault il server
  del sito non parte per nome. → server da Bash e pannello con `preview_start
  --url`. ([[sito-adelinanails]], 18/09/2026)

## Collegamenti

[[registro-interventi]] · [[processo-siti]] · [[convenzioni]] · [[netlify]] ·
[[design-frontend]]
