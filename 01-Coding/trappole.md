---
type: risorsa
riga: Errori tecnici già pagati e strade scartate, per dominio. Descrittivo, non è un rulebook - le regole stanno in convenzioni.
updated: 2026-10-26
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

- `[TRAPPOLA]` **Con il pannello del browser dell'app nascosto non arrivano `requestAnimationFrame` né eventi di scroll, e le transizioni CSS restano ferme**: un banco di prova di motion sembra rotto quando è solo in secondo piano. → si porta il pannello davanti, oppure il banco gira con un `requestAnimationFrame` a timer e `ScrollTrigger.update()` chiamato a mano. ([[sito-monamour]], 24/10)
- `[TRAPPOLA]` **`cattura-fette.mjs` taglia a metà le schede dentro un contenitore che scorre di lato** (un carosello orizzontale sul telefono): la fetta non sa dello scorrimento interno. → per quelle sezioni uno scatto diretto via CDP con il contenitore scrollato, o si giudicano dal browser. ([[sito-mybalance]], 20/10)
- `[TRAPPOLA]` **Brave in headless con `--screenshot` si blocca e non scrive niente.** Per fotografare un file HTML locale funziona `node ~/.claude/skills/anatomy/scripts/capture.mjs <file.html> --out <png>` con `CHROME_PATH="/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"`; per i siti restano `cattura-fette.mjs` e `cattura-apertura.mjs` via CDP. ([[sito-mybalance]], 20/10)
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

- **Il primo fotogramma catturato via CDP subito dopo `navigate` è falso**
  (pagina a metà, elementi doppi): si scatta due volte e si tiene il secondo.
  E sulla macchina possono girare Brave headless di altre sessioni sulle porte
  9334 e 9341: si parte da 9377 in su (Soul Ink, 26/09).

- `[TRAPPOLA]` **Il pannello browser dell'app, quando la sua scheda non è in primo
  piano, non esegue `requestAnimationFrame`, non manda eventi di scroll e non
  fa scattare `IntersectionObserver`.** Un'animazione GSAP o uno shader letti da
  lì sembrano fermi o a metà anche dopo tre secondi, e un reveal allo scroll non
  parte mai. → per misurare la motion si sostituisce `requestAnimationFrame` con
  un `setTimeout` nella pagina di prova, si chiama `ScrollTrigger.update()` a
  mano e si scatta uno screenshot per far passare un fotogramma; per giudicare
  l'apertura si usa `cattura-apertura.mjs` (Chrome headless), e con `--disable-gpu`
  lì il WebGL non disegna: si vede il campo CSS di riserva, non lo shader.
  (23/10/2026, [[sito-laperegina]])

- `[TRAPPOLA]` **Con `html{scroll-behavior:smooth}` lo scroll programmato per fotogramma non avanza**: `window.scrollTo(0, y)` a ogni rAF riavvia uno scroll animato e in 9 s la pagina arriva a 1.100 px su 11.000, così `misura-fotogrammi.mjs` dal 20/10 ha misurato solo il primo schermo dei siti con smooth scroll (su Marta Cesena la fascia 0-999 aveva 488 fotogrammi, la 1000-1999 ne aveva 53, oltre niente). → `scrollTo({top, behavior:'instant'})` e `scrollBehavior='auto'` prima di partire, corretto il 26/10. (26/10/2026, [[sito-martacesena]])
- `[TRAPPOLA]` **Il pannello del browser dell'app non disegna fotogrammi se la sessione non è aperta in una finestra**: un campionatore `requestAnimationFrame` restituisce 0 fotogrammi e ogni misura di motion esce vuota, mentre gli screenshot escono normali. → `misura-fotogrammi.mjs --vivo` apre un Brave con GPU via CDP e misura lì. (26/10/2026, [[sito-martacesena]])
- `[TRAPPOLA]` **La finestra di Claude in Chrome su questo Mac nasce a 400×781 sotto il bordo dello schermo** (screenY 982 su uno schermo alto 982) e `resize_window` risponde «fatto» senza cambiare niente: da lì si misura solo a larghezza telefono. → per la larghezza computer si usa `--vivo`. (26/10/2026)
- `[TRAPPOLA]` **Un `let` al livello globale dentro `Runtime.evaluate` rompe la evaluate successiva** che lo ridichiara (SyntaxError «already been declared»), e il secondo campionamento restituisce i dati del primo. → proprietà di `window` o una IIFE. Nello stesso script, prima di ogni `Tracing.end` si svuota la lista degli eventi su cui si aspetta `Tracing.tracingComplete`, altrimenti la seconda traccia esce vuota. (26/10/2026)

- `[TRAPPOLA]` **`misura-fotogrammi.mjs --vivo` resta fermo senza stampare niente se Brave si è aggiornato su disco mentre il Brave di Nicola è aperto**: lo script lancia il binario nuovo (`156.1.98.60`) con un profilo suo, ma il processo resta a mezzo secondo di CPU e la porta di debug non si apre mai, finché gira la versione vecchia (`155.1.97.59`). Nessun errore: solo silenzio, due volte di fila per dieci minuti. → prima della misura si confronta la versione del binario (`/Applications/Brave Browser.app/Contents/Frameworks/Brave Browser Framework.framework/Versions/`) con quella del processo in corsa (`ps`); se differiscono si misura con Chrome e GPU (`BROWSER_CATTURE="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"`) e lo si dichiara, oppure si aspetta che Nicola riavvii Brave. ([[sito-emozionidicasa]], 28/10/2026)

## Immagini e `sips`

- `[TRAPPOLA]` **`sips --cropOffset` con uno zero su un asse centra il ritaglio su quell'asse invece di partire dal bordo.** Chi vuole tagliare dal bordo mette 1 al posto di 0, e poi misura dove è caduto il taglio. ([[sito-monamour]], 24/10)
- `[TRAPPOLA]` **`python3 -I` non trova PIL.** `-I` esclude i pacchetti installati per l'utente, e Pillow sta lì: per gli script che leggono immagini scaricate si usa `-I` solo se Pillow è nel sistema, altrimenti `python3 -s`-less normale con il file passato come argomento. ([[sito-mybalance]], 20/10)
- `[TRAPPOLA]` **`cwebp` e `magick` non ci sono sul Mac di Nicola, ma Pillow scrive WebP e AVIF** (`features.check('webp')` è vero). Su Materia il primo giro è uscito con JPEG da 376 KB serviti anche al telefono perché «non c'è il convertitore», e Nicola ha notato subito che le foto ci mettevano tanto. Con Pillow, WebP a 480/800/1080 px qualità 72 e `srcset`, il peso delle foto sul telefono è sceso da 6,8 a 1,7 MB. ([[sito-materia]], 20/10)

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

- `[TRAPPOLA]` **Generare immagini senza chiave: Pollinations risponde 402
  anche a 256 px, gli Space ZeroGPU di Hugging Face danno tre giri anonimi** e
  poi l'API `/call/` restituisce `data: null` senza motivo (il motivo si legge
  con `/queue/join` + `/queue/data`: «ZeroGPU quota exceeded»). La sandbox non
  risolve `*.hf.space`: `nslookup` e poi `curl --resolve host:443:IP`. (10/10/2026, [[sito-barbershop-snia]])
- `[SCARTATO]` **Un prima di trapianto ricavato a mano dal dopo non regge.**
  A strati (pelle estrapolata, capelli radi disegnati) fa pettine e cuciture;
  per deformazione (fronte allungata, capelli compressi) l'attaccatura resta
  folta e netta, e Nicola: «questa immagine è irrealistica». Il diradamento
  disegnato fa zebra. → un modello che modifica l'immagine: Nicola su ChatGPT,
  allegando il dopo, un minuto; poi si riallinea su occhi, naso e bocca e si
  pareggiano i toni del fondo. (10/10/2026, [[sito-barbershop-snia]])

- `[TRAPPOLA]` **Un tatuaggio vettorializzato con potrace diventa una sagoma nera piena se in pagina si copia solo il `d`.** potrace scrive i buchi come sottotracciati con `fill-rule="evenodd"` sul `<path>`; il costruttore aveva estratto il `d` con una regex per riusarlo in `<use>` e nei sigilli, e la falena usciva come una macchia nera con il teschio bianco. → quando si estrae il `d` si riporta anche `fill-rule="evenodd"`. Lo strumento è `scripts/traccia.mjs` di jadetattoo-site (soglia adattiva sull'inchiostro più potrace): linee nette e nero pieno escono puliti, il puntinato fine e i petti pelosi no. ([[sito-jadetattoo]], 24/10/2026)

## GSAP e motion

- `[TRAPPOLA]` **`pathLength="1"` più `vector-effect: non-scaling-stroke` rompe il tratto che si disegna allo scroll.** Chromium legge `stroke-dasharray` e `stroke-dashoffset` in pixel di schermo e ignora `pathLength`: i valori fra 0 e 1 diventano trattini sotto il pixel e il percorso appare già tutto disegnato, a pezzi. Si calcola in pixel: `L = getTotalLength() * getScreenCTM().a`, tratteggio «3 4» ripetuto fino a L più un gap «0 2L» in coda, offset da L a 0, ricalcolato a ogni `refresh`. E una lista di dash con un numero dispari di valori viene raddoppiata dal browser: l'ultimo valore da solo diventa un tratto pieno. ([[sito-martacesena]], 26/10/2026)
- `[TRAPPOLA]` **`astro dev` risponde `504 Outdated Optimize Dep` dopo un `npm install` di font o librerie nuove fatto mentre il server gira**: la pagina si vede ma i moduli della motion non caricano, e le misure fatte lì valgono senza motion. Si riavvia il server, o si misura su `astro preview` della build. ([[sito-martacesena]], 26/10/2026)
- `[TRAPPOLA]` **`gsap.matchMedia().add({ grande: '(min-width: 1024px)', ridotto: '(prefers-reduced-motion: reduce)' }, fn)` non chiama `fn` se nessuna condizione vale**: sotto 1024 px con motion normale non partiva niente, nemmeno le rivelazioni e gli split, che dovevano valere sempre. → si aggiunge una condizione che copra il resto (`piccolo: '(max-width: 1023px)'`) e dentro `fn` si legge `conditions.grande`. `monamour-site/src/scripts/spina.js` ha lo stesso difetto: sul telefono non fa rivelazioni, da correggere. ([[sito-whitelilium]], 26/10)

- `[TRAPPOLA]` **Con ScrollSmoother le ancore non portano più alla sezione.** Un link `#sezione` o un indirizzo con `#sezione` restano fermi, perché il contenuto scorre dentro `#smooth-content`: li deve gestire il JS con `ScrollSmoother.get().scrollTo('#sezione')`. Dopo un salto le foto in `loading="lazy"` restano grigie per un attimo, e in una cattura fatta subito sembrano mancanti. ([[sito-materia]], 20/10)

- `[TRAPPOLA]` **`html{scroll-behavior:smooth}` sposta tutti gli ScrollTrigger di quanto
  si è già scrollato.** Su Cake Royal i tre piani della torta partivano a −517 px con la
  sezione a 792: a 375 la torta era già montata prima di arrivarci, e `refresh()` peggiorava
  (−1517 a scroll 2000). I controlli passavano 8/8 e le catture in `?cattura` erano belle,
  perché la motion lì è spenta. → niente scroll morbido sull'`html` nei siti con GSAP; si
  verifica sulla pagina vera con `ScrollTrigger.getAll().map(t=>t.start)` contro
  `getBoundingClientRect().top+scrollY` del trigger. (10/10/2026, [[sito-cakeroyal]])

- `[TRAPPOLA]` **Un `@keyframes` su `visibility` da `visible` a `hidden` in Chrome lascia `visible` a fine corsa**: `visibility` interpola «visibile finché uno dei due lo è», quindi serve `50%,to{visibility:hidden}` o si spegne con `opacity`+`pointer-events`. Cugina: **GSAP 3.13 legge la `scale` CSS dell'`img` al boot e se la tiene inline**, sovrascrivendo l'animazione CSS: la posa 1.06→1 va sulla `figure`, non sull'`img` bersaglio di ScrollTrigger. (07/10/2026, [[sito-ciglia-di-luiza]])

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

- `[TRAPPOLA]` **Il pannello del browser dell'app può essere visibile e girare a 2
  fotogrammi al secondo** (misurato con un ciclo di `requestAnimationFrame` di un secondo,
  con `document.hidden` falso). Dopo uno scroll veloce le apparizioni restano vuote
  per più di un secondo e l'apertura sembra ferma a metà, ma su un telefono vero girano
  a 60. → prima di correggere un'animazione «lenta» si misurano i fotogrammi del
  pannello; se sono pochi, il giudizio sulla motion va su un browser vero o sul
  telefono. (16/10/2026, [[sito-ohana-special-dog]])

- `[TRAPPOLA]` **Il sito «lagga» sul telefono anche se Chrome senza interfaccia misura
  fotogrammi da 17 ms**: i costi veri sono quelli di iPhone. Su Ohana c'erano una barra
  fissa con `backdrop-filter: blur`, ricalcolata a ogni fotogramma dello scroll; il
  `resize` che iPhone manda quando la barra degli indirizzi entra ed esce, che faceva
  `ScrollTrigger.refresh()` a metà scroll; un filo in `scrub` anche sul telefono; un
  controllo con `getBoundingClientRect` su tutte le schede ogni 80 ms; maschere `clip-path`
  e `filter` sulle foto. → barre fisse a fondo pieno, `ScrollTrigger.config({
  ignoreMobileResize: true })` e resize ignorato se cambia solo l'altezza, scrub solo da
  PC, misure solo a scroll fermo. Patrick l'ha visto prima di noi. (16/10/2026,
  [[sito-ohana-special-dog]])

- `[TRAPPOLA]` **Un elemento chiuso da `clip-path` ha area zero e
  l'IntersectionObserver non lo vede mai entrare**: la porta chiusa non si
  apriva perché l'osservatore aspettava un'intersezione che non poteva
  esserci. → si osserva la stanza (la sezione), non la porta.
  (25/09/2026, [[sito-leibeautyroom]])

- `[TRAPPOLA]` **Con `invalidateOnRefresh` un tween `.to` su una variabile CSS
  rilegge come partenza il valore che ha in quel momento**, cioè quello finale
  se il refresh arriva a scroll già fatto: la passata restava ferma a 100 e la
  fascia non si muoveva più. → `fromTo` col valore di partenza scritto e
  `immediateRender: false`. (25/09/2026, [[sito-perunpelo]])

- **Con `scrub` la timeline deve durare esattamente 1** (12/10/2026, Giulia Pregnolato):
  se l'ultimo tween finisce a .86, tutto arriva in ritardo del 14% rispetto allo scroll.
  Si chiude con un tween vuoto che finisce a 1.
- **`transform:translateY(110%)` scritto in CSS, GSAP lo legge come `y` in pixel e non
  come `yPercent`** (12/10/2026): nel `fromTo` va messo `y:0` esplicito, oltre a `yPercent`.
- **`clip-path` si interpola solo se la stringa ha la stessa forma del valore calcolato**
  (`inset(0% 0px 0px round …)`), e la proprietà CSS `scale` non è quella che GSAP tocca
  con `scale`: serve `transform:scale()` (12/10/2026).

- **`overwrite:true` su un tween uccide anche i tween con `scrub` sullo stesso elemento**, e con
  loro i loro ScrollTrigger: la sezione resta ferma su un solo stato (12/10/2026, Giulia
  Pregnolato). Con `overwrite:'auto'` sopravvivono. E con lo scrub sul colore chi si ferma a
  metà vede il colore misto: i cambi di stato scattano a tempo, lo scrub resta sui valori continui.

- `[TRAPPOLA]` **`clearProps: 'all'` di GSAP cancella anche gli stili in linea messi dalla pagina**, non solo quelli dell'animazione: si elencano le proprietà toccate (`clearProps: 'opacity,transform'`). E su un `<path>` SVG GSAP riscrive l'attributo `transform`: con `clearProps` lo cancella e tutte le lettere di un logo tracciato finiscono nell'angolo in alto a sinistra. → la traslazione di ogni glifo sta su un `<g>` attorno al path, non sul path. ([[sito-satatttvision]], 24/10/2026)
- `[TRAPPOLA]` **Dopo una ricarica a metà pagina gli elementi `[data-entra]` rimasti sopra lo schermo non entrano mai** (il trigger è già passato) e restano invisibili. → a scroll fermo, un controllo porta allo stato finale tutto ciò che sta sopra la finestra. ([[sito-satatttvision]], 24/10/2026)
- **Le sonde `getComputedStyle` lanciate dal pannello del browser dell'app durante un'apertura GSAP possono dire «transform: none» mentre in un Chrome vero l'animazione gira**: il pannello non disegna fotogrammi mentre è nascosto o rallenta a 3 al secondo. L'apertura si giudica con `cattura-apertura.mjs` (Brave headless via CDP), non con le sonde dal pannello. ([[sito-satatttvision]], 24/10/2026)

- `[TRAPPOLA]` **Animare con GSAP una variabile CSS (`--campo`) su una sezione fa ricalcolare lo stile di tutta la sezione a ogni fotogramma**, perché la variabile si eredita: su Groavel il ricalcolo costava 131-135 ms in 5 s di scroll e scendeva a 16 ms spegnendo lo script. → si anima `background-color` sull'elemento e la variabile si scrive una volta sola a fine passaggio (26/10/2026, sito-groavel).

- `[TRAPPOLA]` **Un fotogramma lungo con `blockingDuration` 0 e senza script è raster e GPU, non JavaScript**: su Marta Cesena l'apertura a freddo aveva fotogrammi da 400-500 ms mentre il main thread era pulito (scroll a 120 fps), perché al caricamento nascevano tre livelli compositi grandi quanto la sezione (`will-change: opacity` su campi da 1440×5928 px) e sei luci da 1000 px con `will-change: transform`, e il badge di Netlify registrava un rAF a ogni fotogramma. → i campi di colore stanno in uno schermo sticky alto una finestra; `will-change` si mette da JavaScript quando la sezione è vicina e si toglie dopo; si misura con `--vivo --traccia` guardando `GPUTask` e `RasterTask`. (26/10/2026, [[sito-martacesena]])

- `[TRAPPOLA]` **Un velo d'apertura col fondo sul contenitore non può svanire lasciando in vista le stampe che volano via con `Flip`**: svanisce tutto insieme. Il fondo va su un figlio con `z-index: -1` (creato da JS) e la luce del `::before` si spegne con una regola iniettata; così il campo sparisce e le stampe restano. E le stampe del velo vanno spente in CSS sotto `.js.apertura:not(.cattura)` finché il modulo non le riaccende, altrimenti nei primi 30 ms si vedono ferme al centro. ([[sito-emozionidicasa]], 27/10/2026)
- `[TRAPPOLA]` **Il tetto duro dell'apertura in `Base.astro` (2 s) taglia la sequenza quando il modulo arriva tardi** (font, rete): `apertura.js` legge `performance.now()` all'avvio e comprime la timeline per finire prima del tetto, invece di partire da zero. ([[sito-emozionidicasa]], 27/10/2026)
- `[TRAPPOLA]` **Una `transition` CSS su `stroke-dashoffset` scritta per il telefono ritarda lo scrub da computer**: con lo scrub GSAP scrive il valore a ogni fotogramma e la transizione lo insegue con 0,9 s di ritardo. Da 1024 px si spegne in linea (`transition: none`) e resta solo sotto. ([[sito-emozionidicasa]], 27/10/2026)
- `[TRAPPOLA]` **Nel cambio di campo a livelli di opacità, se il livello che esce e quello che entra svaniscono insieme, a metà passaggio traspare il fondo della sezione**: il livello che esce aspetta che quello nuovo sia a 1 (0,4 s) e poi svanisce. ([[sito-emozionidicasa]], 27/10/2026)

## CSS e layout

- `[TRAPPOLA]` **`main>section>*{margin-inline:auto}` restringe e centra i figli di una griglia**: la regola pensata per i blocchi di testo arriva anche alle celle di `grid`, che si stringono alla larghezza del contenuto. → la si limita ai blocchi di testo o la si spegne sulle griglie. ([[sito-mybalance]], 20/10)
- `[TRAPPOLA]` **Con `line-height: .92` l'accento di «È» tocca la riga sopra** nei titoli in maiuscolo stretto. → sopra le righe con lettere accentate l'interlinea sta almeno a 1. ([[sito-mybalance]], 20/10)
- `[TRAPPOLA]` **Il petrolio #1E6E87 sulla sabbia #C3AD98 fa 2,7:1**, sotto AA: per i titoli su quella fascia serve #165A6F. Si misura ogni coppia fondo-testo, non solo quella sul bianco. ([[sito-mybalance]], 20/10)
- `[TRAPPOLA]` **Una regola sugli `span` di un contenitore azzera i numeri di CountUp** (React Bits): il componente annida i suoi `span` dentro, e `.numeri-lista span{font-size:17px}` li porta a 17 px. Si mira la regola a una classe. ([[sito-dogschoolpiacenza]], 20/10)

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

- `[TRAPPOLA]` **`window.open(url, '_blank', 'noopener')` restituisce sempre
  `null`**, anche quando la scheda si apre: un ripiego `if (!w) location.href =
  url` apre il link due volte (WhatsApp in una scheda nuova e anche in quella
  del sito). → si apre senza `noopener`, si stacca a mano con `w.opener = null`,
  e `location.href` resta solo per il popup bloccato. (25/09/2026,
  [[sito-perunpelo]])

- `[TRAPPOLA]` **Un `<source>` dentro un `<picture>` messo a `display:contents`
  occupa una cella della griglia**: fra 600 e 1023 px i quattro servizi erano
  alti 4.858 px, con le celle vuote dove stavano i `<source>`. →
  `picture > source{display:none}`. (25/09/2026, [[sito-perunpelo]])

- **Ridefinire una variabile di colore su una sezione non cambia il colore già
  ereditato dal `body`.** Su Soul Ink (26/09) i titoli restavano avorio sulla
  carta rosa: `--carne` era ridefinita sulla sezione ma `color` lo prendeva il
  `body`. Il colore va rimesso sulla sezione (`color: var(--carne)`), e i
  blocchi a fondo scuro fisso (cartigli, targhe, sigillo) riportano le loro
  variabili all'avorio da soli.
- **Una `<figure>` in griglia con `width: auto` e `justify-self: start` va a
  larghezza 0**: su Soul Ink da PC la bambola era sparita. Serve una larghezza
  o `justify-self: stretch`.
- **Con `vector-effect: non-scaling-stroke` il `stroke-dasharray` legato a
  `pathLength` non traccia più**: la curva usciva a trattini. O si toglie il
  `vector-effect`, o la curva si svela con `clip-path` (Soul Ink, 26/09).

- `[TRAPPOLA]` **Hover su un elemento che ruota: la zona sensibile ruota con
  lui.** La targa larga 1.100 px a 90° copriva la riga sopra e sotto, il
  puntatore vicino la riprendeva e la rotazione invertiva. → `pointer-events:none`
  sull'elemento che gira, hover sulla scatola ferma che lo contiene, un ritardo
  d'ingresso, e niente rotazione sotto `(hover:none),(pointer:coarse)`.
  (10/10/2026, [[sito-barbershop-snia]])

- `[TRAPPOLA]` **Un `position: absolute` dentro una scheda di un carosello senza un antenato posizionato allarga il documento** (a 375 px `html` arrivava a 2.558 px): la scheda vuole `position: relative`. ([[sito-satatttvision]], 24/10/2026)
- **Lo `<style>` dentro un SVG messo inline vale per tutta la pagina**: le regole di una figura di `anatomy` colpiscono tutto ciò che ha le sue classi (`.iso-*`). Le classi della figura restano con un prefisso suo. ([[sito-satatttvision]], 24/10/2026)

## Git, account e pubblicazione

- `[TRAPPOLA]` **Chi ha OperO aperto prima di un deploy continua a vedere la
  versione vecchia finché non preme «Aggiorna».** La PWA aggiorna solo a
  comando (`registerType: 'prompt'`, scelto apposta per non ricaricare la
  pagina sotto una bozza di fattura), e il portale coOperO, senza service
  worker, resta sulla scheda caricata. Il 26/10 Seba è entrato nel sito di
  prova alle 20:05, il deploy è arrivato alle 20:23 e lui ha segnato mancanti
  due punti che erano online. → prima di chiedere a Seba di controllare si fa
  il deploy e gli si dice di premere «Aggiorna» o di ricaricare; per sapere
  cosa ha visto davvero si rilegge il bundle dal permalink del deploy
  (`https://<id>--opero-prova.netlify.app`, id da `netlify api
  listSiteDeploys`) e si cercano le stringhe nuove. ([[opero-intermediar-receive]], 26/10)
- `[TRAPPOLA]` **Netlify CLI 27 su questo Mac salva il collegamento del progetto in `~/.netlify/state.json`, non nella cartella del sito**: `netlify link` da qualunque cartella sovrascrive un solo stato globale, e `netlify status` o `netlify deploy` in `mybalance-site` risultavano collegati a `materia-rezzato` (l'ultimo link fatto). Il 20/10 il `siteId` globale è stato tolto, quindi un deploy senza sito dichiarato si ferma. → **si pubblica sempre con `netlify deploy --dir dist --prod --site <nome-o-id del sito>`**, e si legge l'URL che la CLI stampa prima di dirlo fatto. ([[sito-mybalance]], 20/10)
- **`netlify deploy --prod` resta fermo un minuto e mezzo su «Installing extensions · baseline»** (09/10/2026,
  [[sito-mitril-tattoo]]): non è piantato, ma sembra, e chi apre il link nel frattempo non trova niente. Il sito è
  statico → `netlify deploy --prod --no-build --dir <copia>` esce in pochi secondi. La copia si fa con `rsync` senza
  `raccolta/`, `prove/`, `DIREZIONE.md` e `.git`: `--dir .` pubblica anche le note sul cliente (successo qui per
  cinque secondi, poi coperto dal deploy pulito).

- `[TRAPPOLA]` **Un `_redirects` di Netlify senza `force = true` non scatta
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
- `[TRAPPOLA]` **La cache lunga sulle foto tiene la foto vecchia se la si
  sostituisce con lo stesso nome**: `assets/img/*` a `max-age=604800`, il prima
  rifatto era online e Chrome di Nicola mostrava ancora quello di stamattina.
  → una foto cambiata prende **un nome nuovo**. (10/10/2026, [[sito-barbershop-snia]])
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
- `[TRAPPOLA]` **L'hook «Chiusura automatica» committa e pusha il lavoro degli
  agenti a metà.** L'11/10 ha pushato due volte il banco online mentre gli
  operatori lavoravano, compreso un workflow che da quel momento girava ogni 30
  minuti senza i suoi secret. Il vault è pubblico: un file di prova con un
  valore vero, anche per un minuto, finisce su GitHub. → i segreti degli agenti
  stanno fuori dal vault (`~/.config/denkicode/`), e quello che un agente scrive
  nel vault si considera pubblicato. ([[2026-10-11-banco-online]])
- `[TRAPPOLA]` **L'`ignore` di Netlify che guarda solo l'ultimo commit salta le
  liste.** Se una lista nuova e un commit automatico arrivano insieme, conta
  l'ultimo e la lista non va online. → si guarda tutto l'intervallo
  `$CACHED_COMMIT_REF..$COMMIT_REF` e si costruisce se un commit qualunque, che
  non sia quello automatico, ha toccato i file. ([[2026-10-11-banco-online]])

- `[TRAPPOLA]` **Il badge «Powered by Netlify» dei siti gratuiti inietta `hud?variant=public`**: 44 ms di script all'avvio e un callback a ogni fotogramma. → `netlify api updateSite` con `built_with_badge_enabled: false` lo spegne anche sul piano gratuito (fatto su `martacesena` il 26/10). (26/10/2026, [[sito-martacesena]])

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

- **Una funzione Netlify accetta al massimo 6 MB di corpo** (funzioni sincrone),
  e il base64 ne aggiunge un terzo. Le foto vanno **una per richiesta**, ridotte
  nel browser prima di partire. Il Fiftynine ne manda fino a 12 da 1,5 MB nella
  stessa richiesta: con più di tre foto grandi insieme rischia il rifiuto, mai
  provato online. ([[sito-barbershop-snia]], 10 ottobre 2026)
- `[TRAPPOLA]` **La scrittura condizionata di Netlify Blobs (`onlyIfMatch`)
  perde scritture sotto carico, con risposta 200.** Online, con 3-5 scrittori
  insieme, 2-7 righe su 40 sparivano: più scrittori passavano con lo stesso
  ETag. → dopo la scrittura si aspettano ~400 ms, si rilegge e, se il gesto non
  c'è, si riscrive: 40/40, 48/48, 25/25. E il `BlobsServer` locale non manda
  l'ETag in lettura: in locale la concorrenza non si prova, serve un archivio
  finto che perde scritture apposta. (`@netlify/blobs` 11.1.4, 11/10/2026,
  [[2026-10-11-banco-online]])

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

- `[TRAPPOLA]` **Claude in Chrome non restituisce indirizzi con parametri.** Un `javascript_tool` che rende l'URL di un'immagine di Instagram (firmato con `?stp=…&oh=…`) risponde «BLOCKED: Cookie/query string data», e l'API interna di Instagram risponde con la pagina HTML. Le didascalie si leggono dall'`alt` delle immagini della griglia scrivendole nel DOM e leggendole con `get_page_text`; i file si scaricano dal browser dell'app sloggato più `curl`. ([[sito-dogschoolpiacenza]], 20/10)

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

- `[TRAPPOLA]` **Le foto di `cdn0.matrimonio.com` rispondono 403 a `curl`**,
  perché le protegge Akamai. Funziona il `fetch` fatto dentro la pagina aperta
  nel browser dell'app: l'operatore ha passato i byte al disco con un piccolo
  server su localhost, poi spento. Le foto della galleria arrivano a 1230x820.
  (16/10/2026, [[sito-nocloudsproduction]])

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

- `[TRAPPOLA]` **Su alcuni profili la caption sta nel primo commento, o non c'è.**
  Il testo letto da `<main>` di un post può essere il commento di un cliente,
  non le parole del profilo: si controlla chi lo firma prima di citarlo.
  (30/09/2026, [[sito-petliving]])

- `[TRAPPOLA]` **«Non ha un sito» può essere falso anche con tutti i domini
  morti: il riquadro «Sito web» della scheda Google può puntare a una pagina
  Canva** (`*.canva.link`). Si legge con `get_page_text` e dentro ci sono i
  testi e il logo in PNG trasparente. (05/10/2026, [[sito-jpp-merate]])
- `[TRAPPOLA]` **I testi dei pacchetti di un catalogo WhatsApp Business si
  leggono con `curl`**: stanno nell'`og:description` di
  `whatsapp.com/product/<id>/<telefono>`. Il catalogo intero `wa.me/c/…` no.
  (05/10/2026, [[sito-jpp-merate]])
- `[TRAPPOLA]` **Su Google Maps la miniatura arriva alla taglia massima
  cambiando il suffisso `=w…-h…-k-no` in `=s2400`.** Da sloggati non si sa se
  la foto è «dal proprietario». (05/10/2026, [[sito-jpp-merate]])
- `[TRAPPOLA]` **Dopo aver chiuso il modale di login di Instagram, le foto di
  un carosello arrivano con 2-3 secondi di ritardo**: letto subito, il post
  risulta senza immagini. → attesa di 2,5 s. E l'URL firmato va passato intero:
  tolto anche solo `_nc_ohc`, torna il file da 22 byte. (05/10/2026,
  [[sito-jpp-merate]])
- `[TRAPPOLA]` **Instagram sloggato: la pagina di un post non ha l'`<img>` a
  1440 nel DOM.** Gli URL grandi si leggono da
  `performance.getEntriesByType('resource')` (host `*.fna.fbcdn.net`, firmati
  con scadenza `oe=`: si scaricano subito con `curl -L`). E il primo `<img>`
  con alt «Photo by» è la griglia dietro il modale, non il post: si filtra per
  `naturalWidth >= 700` e si controlla l'ID. Le foto arrivano in WebP, non JPEG.
  (08/10/2026, [[sito-claudia-dogsitter]])

- `[TRAPPOLA]` **Nel browser dell'app le immagini di Instagram a 1440 px non
  arrivano se la scheda sta in secondo piano.** Durante la raccolta su
  `@dogschoolpiacenza` l'elenco delle immagini grandi restava vuoto finché la
  scheda non era in primo piano (`tabs_select`) e il post aperto direttamente.
  Gli indirizzi si scaricano poi con `curl` senza login, ma interi: a un
  indirizzo a cui si toglie un parametro Instagram risponde 403, e scadono dopo
  poco. (13/10/2026, [[sito-dogschoolpiacenza]])

- `[TRAPPOLA]` **Sotto carico il DNS del Mac risponde «il dominio non esiste»
  anche per domini vivi, e `host -t mx` dà SERVFAIL.** Con sei ricerche in
  parallelo `trova-mail.py` perdeva siti veri e segnava «senza MX» caselle
  buone, per esempio `elsap.it`. → i siti si risolvono col DNS di Cloudflare
  via HTTPS (1.1.1.1), gli errori di rete si ritentano, e una ricerca con buchi
  di rete non si salva come negativa. (19/10/2026, [[posta-fredda]])
- `[TRAPPOLA]` **Pagine Gialle mostra il sito solo nelle schede a pagamento.**
  Su 87 aziende cercate, 34 volte ha trovato l'azienda ma non il sito: «nessun
  sito su Pagine Gialle» non vuol dire che il sito non c'è.
  (19/10/2026, [[posta-fredda]])
- `[TRAPPOLA]` **Su companyreports le stringhe ATECO 2007 e 2025 si scontrano.**
  `25.62.00` (2025) oggi contiene le serrature, mentre le officine di meccanica
  generale stanno in `25.53.00`. → il settore lo decide la classe a quattro
  cifre, e lo script scopre da solo tutte le liste di ogni classe.
  (19/10/2026, [[posta-fredda]])
- `[TRAPPOLA]` **«Sito su un dominio non .it e testo in inglese» non vuol dire
  filiale di un gruppo estero.** La regola aveva scartato Cospal, Berta,
  Contech, Ramallumin e Sprinx, che sono italiane ed esportano. Le separa la
  partita IVA: un'azienda italiana la scrive sul suo sito anche se è in
  inglese, il sito del gruppo estero no. (19/10/2026, [[posta-fredda]])

- `[TRAPPOLA]` **Dal browser dell'app le pagine di Instagram e Facebook bloccano `fetch` e le immagini verso `127.0.0.1`**: non si può passare un file a un server locale per salvarlo. Si leggono gli URL dalla pagina e si scarica con `curl`. ([[sito-satatttvision]], 24/10/2026)
- **Le foto della scheda Foto di Facebook arrivano a 1440 px alzando il parametro `cstp` a `mx1440x1440`**, ma possono essere due fotogrammi di video impilati in un quadrato con una barra nera in mezzo: si guardano prima di tenerle, e se ne ritaglia uno. Le didascalie dei post Instagram con `curl` dall'`og:title` funzionano ancora il 24/10/2026, anche sul post dello studio. ([[sito-satatttvision]])
- `[TRAPPOLA]` **Vettorializzare un tatuaggio da una miniatura a 640 px non regge**: con `vtracer` (installabile con `pip` in un venv, senza toccare il Mac) dopo una soglia le linee fini escono spezzate e la pelle diventa macchia. Il tracciato funziona bene solo su un'immagine piatta e pulita, come il lettering di un logo (16 tracciati puliti dalla copertina Facebook di Satatttvision). Per i disegni dai lavori servono gli originali a 1080+. ([[sito-satatttvision]], 24/10/2026)

- `[TRAPPOLA]` **`cattura-fette.mjs` può mostrare una sezione tagliata che nel DOM è intera.** Sul sito di Pilates District le tre schede dei segnali a 1440 px uscivano mozzate a metà riga nella fetta, mentre `getBoundingClientRect` dava 340 px per tutte e tre con il testo dentro; una cattura ferma della stessa sezione (`cattura-apertura.mjs` sull'indirizzo con `?cattura#segnali`) le mostrava intere. → prima di correggere un «taglio» visto in una fetta si misura il DOM, e si fotografa la sezione da ferma. ([[sito-pilates-district]], 26/10/2026)
- `[TRAPPOLA]` **Dal 26/10/2026 anche l'`og:title` dei post Instagram letto con `curl` torna vuoto** (guscio di login su 12 post su 12): la voce del 24/10 non vale più. Le didascalie si leggono dal browser dell'app senza login, aprendo il singolo post; le foto a 4096 px arrivano ancora da lì con `curl` e l'indirizzo intero. ([[sito-pilates-district]], 26/10/2026)
- `[TRAPPOLA]` **Il fotogramma di copertina di un reel non è l'anteprima della griglia.** Per misurare il viola dello stencil la `video_additional_cover_frame` del reel (640 px) mostrava un selfie allo specchio, mentre la griglia del profilo mostrava lo stencil. L'anteprima giusta è il `currentSrc` dell'`<img>` dentro `a[href*="/reel/<id>/"]` della pagina profilo (361 px, `CLIPS.best_image_urlgen`): basta per un colore, non per una foto. ([[sito-jadetattoo]], 24/10/2026)
- `[TRAPPOLA]` **In 7 post su 11 il testo di `<main>` non contiene «Segui»**, quindi la didascalia letta dopo «Segui» resta vuota. La didascalia di chi pubblica sta subito dopo la data relativa («3 g», «12 sett»), prima dei commenti. ([[sito-jadetattoo]], 24/10/2026)

- `[TRAPPOLA]` **Un sito su Pixieset (`*.mypixieset.com`) risponde 403 «Just a moment...» di Cloudflare a `curl` e a WebFetch**, e archive.org non ne ha copia; passano solo `sitemap.xml`, `robots.txt` e le immagini del CDN (`images-pw.pixieset.com`, al massimo 1000 px di larghezza: ogni altro suffisso di taglia dà 403). Le pagine si leggono dal browser dell'app con `get_page_text`, senza login. ([[sito-emozionidicasa]], 27/10/2026)
- `[TRAPPOLA]` **Su Instagram senza login la griglia carica altri post solo col bottone «Mostra altri post»** (si prende con `find` e si clicca per `ref`; lo scroll non basta): da 12 a 24 a 36 elementi, poi al suo posto torna il modale di login. Per un carosello, un solo `javascript_exec` fa tutto: clicca «Avanti» fino a 15 volte, raccoglie le immagini con `naturalWidth >= 700` e legge la didascalia dal testo di `<main>` dopo la data relativa; con `browser_batch` (massimo 25 azioni) escono 6 post per chiamata se l'attesa di 2,5 s sta dentro il JS. La data di pubblicazione sta nell'`alt` («Photo by … on October 11, 2026»). ([[sito-emozionidicasa]], 27/10/2026)
- **Il profilo di una collina viene dai dati di quota, non da un disegno**: Open Topo Data (`api.opentopodata.org/v1/srtm30m`, 100 punti a richiesta, una al secondo) ha risposto al primo colpo per tre linee da 200 punti sul Monferrato; `scripts/genera-colline.mjs` e `Colline.astro` del repo lo rendono come polilinea con `preserveAspectRatio="none"`. Cugina della carta OSM di Marta Cesena. ([[sito-emozionidicasa]], 27/10/2026)

## Liste e banco DM

- **Il giro del mattino lavora sul ramo in cui il vault si trova.** Dal 20 al
  23/10/2026 il vault del Mac di Nicola era su `skill/stile-apple`: i giri
  hanno pushato lì, mentre Netlify e `banco-sync.yml` lavorano su `main`. Il
  banco online è rimasto con la lista del 20, i DM del 22 non sono tornati nel
  vault e `prossimo-giro.py` ha contato 164 righe invece di 31. → prima del
  giro va controllato `git branch --show-current`; se non è `main`, lo stato del
  banco va letto da `origin/main`. [[2026-10-23-posta-giro-mattina]]
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

- **Xcode installato senza accettare la licenza spegne `python3` e `git` di
  sistema, e con loro il banco.** Il 28/09/2026 sul Mac di Patrick `xcode-select`
  puntava a Xcode 27 appena comparso: `/usr/bin/python3` e `/usr/bin/git` sono
  shim che rifiutano di partire finché la licenza non è accettata, quindi
  `Banco DM.command` (usa entrambi) non apriva niente e il `git pull` di inizio
  sessione falliva in silenzio con lo stesso messaggio. I Command Line Tools in
  `/Library/Developer/CommandLineTools` funzionano lo stesso, chiamati per
  percorso. Fix: `sudo xcode-select -s /Library/Developer/CommandLineTools`
  (o `sudo xcodebuild -license accept` se Xcode serve davvero). Serve la
  password: lo lancia la persona, non Trevis. (Mac di Patrick, 28/09/2026)
- `[TRAPPOLA]` **«Già contattati» con 2.265 righe bloccava la scheda per più
  di 45 secondi**, anche sul banco vecchio: `disegna()` creava ogni cartella e
  `misura()` forzava un reflow per ogni `textarea`. → 100 righe per volta e un
  bottone «Mostra altri»: 0,1 s. Una pagina che cresce ogni giorno si misura
  col numero di righe di fra un mese, non di oggi. (11/10/2026)
- `[TRAPPOLA]` **Il recupero cancellava il primo messaggio.** In `annota()` il
  recupero usava la data del primo invio come chiave `(Data, Da, handle)`, cioè
  la stessa della riga `primo`, e il server la sostituiva: in `contattati.csv`
  ci sono 43 recuperi su 25 handle senza più la riga del primo messaggio. La
  data del primo si ricava dalla prima riga di qualunque tipo, come fa
  `allinea-contattati.py`. Corretto nel banco online. (11/10/2026)

- `[TRAPPOLA]` **Il task pianificato dell'app parte in modalità permessi
  «default», non «auto», e nessun campo del task la cambia.** Le sessioni
  normali di Nicola partono in `auto`, dove il classificatore approva da solo;
  la sessione di `banco-mattina` parte in `default` (log dell'app:
  `requested=default effective=default`) e si ferma al primo comando che nessuna
  regola di `permissions.allow` copre. Il 12/10 ha aspettato dalle 8:04 alle
  17:43 su `python3 02-Sales/strumenti/giro-mattina.py --ruolo primo; echo
  "EXIT $?"`, il 13/10 dalle 8:10 sullo stesso comando scritto con `EXIT=$?`.
  L'app memorizza sul task le regole approvate durante un giro («Added 1
  approved permission rule on task»), ma la regola è il testo del comando: una
  coda diversa non combacia, e un comando con `$VAR` o `$(...)` non produce
  nessuna regola («no suggestions on request»), quindi non si memorizza mai.
  L'11/10 e il 12/10 il giro è andato avanti solo perché Nicola ha messo la
  sessione in `auto` a mano; in `auto` il classificatore ha poi negato
  `pubblica-lista.py` («Real-World Transactions») e il push («External System
  Writes»). → Le regole di `settings.json` da sole non bastano, perché il
  modello cambia la coda dei comandi a ogni giro: serve un hook `PreToolUse`
  che riconosca la sessione del task (`permessi-giro.py`). E l'hook lo installa
  una persona: il classificatore ferma il modello che prova a scriverlo
  («Self-Modification»). (13/10/2026, [[giro-mattina]])
  ⚠️ **Cambiato il 19/10/2026**: creato dall'app da una sessione in modalità
  automatica, il task `posta-mattina` è stato salvato in modalità automatica
  («This task was saved in Auto mode because this session is in it»). La
  modalità del task si cambia modificandolo nell'app. Se il primo giro gira
  senza fermarsi, l'hook non serve più per i task nuovi. ([[posta-fredda]])

- **Sette operatori che leggono Instagram in parallelo chiudono l'indirizzo
  in venti minuti.** Giro del 16/10, dalle 18:55 alle 19:16: Cremona ha
  sondato 848 handle indovinati dai nomi di Pagine Gialle con 8 richieste in
  parallelo, Milano 350 letture con 10, Brescia ~100 con 6, Novara 280 con 3,
  Genova 135 con 6; più di 1.700 richieste, e alle 19:16 ogni `curl` Googlebot
  e ogni pagina del browser sloggato rimandava al login con `is_from_rle`. Il
  blocco è durato oltre 40 minuti e il giro ha chiuso con 26 righe su 160.
  Nei giri precedenti le stesse ~1.200 letture, fatte una alla volta in
  un'ora e mezza, erano passate. Due operatori hanno anche lanciato `pkill -f`
  per nome di file (`yahoo.sh`, `xargs -P 6`) e possono aver fermato lo script
  di un altro. → Il brief degli operatori fissa il ritmo prima di partire: una
  lettura alla volta, mai in parallelo, almeno 3 secondi fra una e l'altra,
  nessun handle indovinato a centinaia (si sondano solo quelli che una fonte dà
  già come esistenti: siti aziendali, menzioni, elenchi), e durante un blocco
  una sola sonda ogni 2 minuti. I processi si fermano solo per PID, mai per
  nome. (16/10/2026, [[2026-10-16-siti-e-ricerca-giro-mattina]])
- **Sette operatori nella stessa scratchpad si sovrascrivono gli script.**
  Giro del 17/10: un operatore ha scritto `ig.py`, `sito.sh` e `pgparse.py`
  nella radice della scratchpad condivisa e per qualche minuto ha riempito le
  cartelle `ig/` di un altro. → il brief assegna a ogni operatore una cartella
  propria (`scratchpad/op-<cella>/`) e nessuno scrive nella radice. Nello
  stesso giro Pagine Gialle ha risposto 429 in cinque celle su sette dopo
  5-50 richieste: sette operatori sullo stesso indirizzo la saturano, mentre
  Instagram a una lettura ogni 5 secondi per operatore ha retto 196 letture.
  (17/10/2026, [[2026-10-17-siti-e-ricerca-giro-mattina]])
- **Il link del modulo nel primo DM della ricerca non si apre.** Posta del
  17/10: tre aziende su tre che hanno risposto dicono «non riesco a cliccare
  il link», «da Instagram non si riesce ad aprire», «Instagram sconsiglia
  l'apertura del link perché possibile truffa», e hanno chiesto il modulo per
  email. Instagram blocca i link nelle richieste di messaggio da sconosciuti,
  come dice già la regola 5 di [[metodo-instagram]] per i siti. → il primo DM
  della ricerca chiede se va bene mandare il modulo; il link parte nel secondo
  messaggio o per email. Nello stesso giro: 92 DM dal 25/09 risultano «non
  consegnati» (l'account non accetta richieste da tutti), e l'API
  `direct_v2/inbox` che leggeva la posta risponde 404: la posta si legge
  scorrendo il DOM dell'inbox, dall'account denkicode collegato in Brave sul
  Mac di Nicola. (17/10/2026, [[2026-10-17-siti-e-ricerca-giro-mattina]])
- **La pagina che Instagram dà a Googlebot non porta più il link in bio né le
  date dei post.** Dal 17/10 `external_url`, `bio_links` e `taken_at_timestamp`
  mancano: le righe scritte con «nessun link in bio» non l'hanno verificato, e
  la data di un post si ricava dal suo ID (spostato di 23 bit più l'epoca di
  Instagram, 1314220021721 ms). → il link in bio si apre nell'app prima di
  scrivere; da Brave, con l'account collegato, `/api/v1/fbsearch/account_serp/`
  trasforma un nome in handle (`topsearch` risponde 404) e
  `/api/v1/discover/chaining/?target_id=` dà fino a 80 account simili, mentre
  `users/{pk}/info/` e `web_profile_info` rispondono 429. Il chaining rende
  bene sul mestiere e male sulla provincia: su 230 candidati letti il 17/10, 90
  erano di un'altra provincia. (17/10/2026, [[2026-10-17-siti-e-ricerca-giro-mattina]])

## Skill e strumenti di processo

- `[TRAPPOLA]` **`controlla-slop.py` e `controlla-testo.py` lanciati sulla radice di un repo Astro escono 0 senza controllare niente**, perché lì non c'è `index.html`: un operatore ha riportato «testo 0» tre volte mentre su `dist` c'erano 16 blocchi. Si lanciano sempre su `dist`, dove `controlla-sito.py` almeno avvisa («nessun index.html»). ([[sito-martacesena]], 26/10/2026)
- `[TRAPPOLA]` **anatomy: un attributo senza valore (`data-car`) passa nell'SVG inline ma rompe il file `.svg` aperto da solo**, che mostrava 30 parti su 137: come XML l'attributo nudo non è valido. → si scrive sempre `data-car=""`, e il file `.svg` statico si apre da solo almeno una volta prima di consegnarlo. Il Reformer di My Balance (135 parti) è nato così il 20/10 in circa 40 minuti, con `CHROME_PATH` su Brave per i controlli. ([[sito-mybalance]], 20/10)
- `[TRAPPOLA]` **La skill `uiux-pro-max` sul Mac ha solo `SKILL.md`**, senza gli script e i dati (palette, 74 coppie di font, 17 preset GSAP), sia nel plugin `anthropic-skills` sia in `~/.claude/skills/synced/`: le ricerche promesse dalla descrizione non rispondono. Gli effetti si prendono da React Bits e dai plugin GSAP ufficiali; gli abbinamenti di font si provano con specimen renderizzati. ([[sito-mybalance]], 20/10)
- `[TRAPPOLA]` **In Astro uno `slot={`c${i}`}` dentro un `.map` viene compilato fuori dal ciclo** e la build si ferma con `j is not defined`. Le schede di una pila si passano come dati a un componente React. ([[sito-dogschoolpiacenza]], 20/10)
- `[TRAPPOLA]` **Con `build.format: 'file'` in Astro, `Astro.url.pathname` durante la build arriva come `/maternity.html`** (e `/index` per la home), quindi il canonical e l'`aria-current` della barra escono sbagliati se si confronta il percorso nudo. → si toglie `.html` e `/index` prima di confrontare, oppure si usa `Astro.url.pathname.replace(/(\/index)?\.html$/, '')`. In sviluppo il percorso è pulito, per questo non si vede finché non si legge `dist/`. ([[sito-whitelilium]], 24/10)
- **Mod di Claude Code: nel terminale `'Svg' in $.ui.resolve(e)` è sempre vero.** La tabella degli elementi viene completata, e un elemento che la superficie non ha disegna un frammento vuoto: il ripiego «se non c'è Svg uso il testo» non scatta mai e il pannello resta muto. Si decide da `e.surface`. Il `claude` nel PATH (2.1.261) non ha `plugin test`: si usa il binario dell'app, `~/Library/Application Support/Claude/claude-code/<versione>/…/MacOS/claude`. ([[registro-interventi]], 10/10)
- **`voce-denkicode` sulle didascalie e sul copy di un sito produce frasi da
  bambino.** Taglia connettivi e verbi e lascia frasi nominali che descrivono
  la foto («Ghiaia da una parte, erba dall'altra», «Sostenuto finché non si
  fida del fondo che non c'è»). Nicola su Mikuma Dogs: «sembra che non sai
  l'italiano, scrivi solo cose utili». → il copy di un sito vetrina lo scrive
  il direttore nel brief, frase per frase, e l'operatore lo inserisce senza
  riscriverlo. Ogni frase ha un verbo e dice una cosa utile a chi legge; una
  didascalia descrive il servizio, non la foto, o non c'è. Le frasi prese dai
  post del cliente entrano solo se sono utili. Il metro è NN/g: conciso,
  scandibile, oggettivo, mai promozionale. ([[sito-mikuma-dogs]]; dal 12/10/2026
  la regola sta in [[italiano-chiaro]])

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

- `[TRAPPOLA]` **`controlla-sito.py` conta le versioni `-800.jpg` dentro `assets/img/` come
  «foto sotto 1080» e boccia il sito** (sito-whitelilium, 07/10/2026). → le versioni per
  il telefono vanno in una sottocartella (`assets/img/800/`), che il glob non attraversa.


- `[TRAPPOLA]` **Un mod di Claude Code che scrive `$.state` dentro `tool.call` o
  `turn.step` ferma gli agenti in background.** Il pannello `agenti-live` registrava
  l'ultima mossa e i token di ogni agente: tutti e quattro gli operatori di CO-OPERO
  si sono fermati insieme, ciascuno sul punto di lanciare uno strumento, e il
  watchdog li ha chiusi dopo 600 s. → un mod che guarda gli agenti legge e basta
  (`$.agent.list`, `$.session.messages({ agentId })`, `$.session.usage`) da un
  `ui.render` con un timer; niente hook sul loro percorso. (10/10/2026)

- `[TRAPPOLA]` **Due agenti nello stesso browser integrato si rubano la scheda.**
  `read_page` tornava vuoto e uno dei due si è fermato due volte all'apertura. →
  un agente alla volta nel browser, o ciascuno con `tabs_create` e il suo `tabId`.
  (10/10/2026)

- `[TRAPPOLA]` **Le porte 4321 e 4322 possono essere già prese dal server di un altro sito**, e `astro dev` scivola da solo sulla porta successiva, che può essere quella di un altro operatore. → `--strictPort` e una porta diversa per ogni operatore. ([[sito-jadetattoo]], 24/10/2026)
- `[TRAPPOLA]` **Con il pannello del browser nascosto `requestAnimationFrame` non gira**, quindi apertura, shader e scrub sembrano fermi. Le animazioni si guardano con Chrome headless pilotato via CDP (come `cattura-fette.mjs`), oppure con `scripts/video-telefono.mjs` di jadetattoo-site, che registra la pagina a 390×844 con lo screencast di CDP e la monta in MP4 con `ffmpeg-static` installato nello scratchpad. Il video serve anche da consegna quando il cliente vuole vedere la bozza su Instagram. ([[sito-jadetattoo]], 24/10/2026)
- `[TRAPPOLA]` **`controlla-slop.py` legge un h1 diviso in uno `<span>` per lettera come un «titolo di 10 parole»**, ed è un falso positivo; blocca invece la ✦ usata come segno al posto di un'icona, quindi va sostituita con un'icona Phosphor (`star-four`). ([[sito-jadetattoo]], 24/10/2026)

- `[TRAPPOLA]` **Gli operatori lanciati in parallelo condividono la stessa cartella temporanea della sessione**: su Groavel uno ha sovrascritto il `fette.mjs` di un altro. → ogni operatore lavora in una sottocartella sua (`/tmp/<sito>-<ruolo>`), scritta nel contratto fra operatori (26/10/2026, sito-groavel).

## Collegamenti

[[registro-interventi]] · [[processo-siti]] · [[convenzioni]] · [[netlify]] ·
[[design-frontend]]
