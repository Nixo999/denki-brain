---
type: risorsa
updated: 2026-09-08
source: claude
tags: [trappole, memoria, frontend, gsap, git]
---

# Trappole — quello che non voglio riscoprire due volte

**Questo file lo scrivo per me stesso.** Il [[registro-interventi]] dice *cosa*
è stato fatto e in che ordine, le daily dicono *com'è andata quel giorno*. Qui
sta solo il residuo riutilizzabile: la trappola e la contromisura, senza il
racconto intorno.

Serve perché a inizio sessione leggo **solo l'ultima daily**. Tutto quello che
è stato imparato più di un giorno fa, se sta solo lì dentro, per me non esiste
più. Ed è già successo: il reset `img{height:auto}` è stato pagato su
[[sito-castiglione]] e ripagato su V-BAG, e il `transform` sovrascritto da GSAP
è stato ritrovato quattro volte su quattro progetti diversi.

**Come si aggiorna**: a fine sessione, con `/chiudi-sessione`. Ci finisce solo
quello che vale su un progetto che ancora non esiste. Il dettaglio del caso
resta nella daily e nel registro, e da qui ci si linka.

## Catture e verifica in headless

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
- **`sips --cropOffset` restituisce un PNG nero.** ([[sito-salone-di-andrea]])
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
  ([[sito-osteria-tarilli]])
- **`launch.json` va nella cartella della sessione, non nel repo**, e
  `python3 -m http.server` non parte da una cartella Google Drive
  (`os.getcwd()` è vietato): `sh -c "cd <repo> && exec python3 -m
  http.server"`. ([[sito-osteria-tarilli]])
- **`file://` non è il sito**: aperto come istantanea statica (URL `data:`) non
  gira JS e non carica le immagini relative. Si riapre dal server prima di
  concludere che qualcosa è rotto. ([[sito-fiftynine]])

## Immagini e `sips`

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

## GSAP e motion

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

## CSS e layout

- **L'attributo `height` di `<img>` vince su `aspect-ratio` CSS.** Card alte
  1405px. → nel reset, `img { height: auto }`. Pagata su [[sito-castiglione]],
  ripagata identica su V-BAG.
- **`<use>` di un `<symbol>` non eredita gli stili del documento**: sette
  boccette nere al primo giro. → la grafica che prende colore da CSS va inline.
  ([[sito-nails-mania]])
- **Un `.wrap` con `margin: auto` dentro una flex column si shrink-wrappa.** →
  `width: 100%`. ([[sito-castiglione]])
- **La specificità produce bug invisibili a occhio**: `.nav-links a` batteva
  `.btn` e il CTA in nav era verde su verde. Si trova misurando il contrasto,
  non guardando lo screenshot.
- **Un CTA che wrappa su due righe a 375px si toglie, non si comprime.**
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

## Git, account e pubblicazione

- **`gh` tiene un solo account nel keyring.** Con due account, il push sulla repo
  dell'altro dà `403` o `Repository not found`, e sembra un problema del repo. →
  `gh auth login` con l'account giusto. La paternità dei commit è un'altra cosa
  ancora: la decide il `git config` locale del repo.
- **`gh repo create --push` passa e il push successivo no**: il primo usa il
  proprio helper. → si svuota l'helper e si rimette quello di `gh`.
- **Una bozza non commissionata non si fa indicizzare.** Tre sbarramenti (`meta
  robots`, `X-Robots-Tag`, `robots.txt`) che si tolgono quando il sito diventa
  loro: indicizzarla mette un secondo sito col nome del lead su Google, cioè un
  danno fatto prima della vendita. Sta in [[netlify]].
- **Le credenziali non le digito io.** `netlify login` apre il browser e chiede
  l'accesso di Nicola: si prepara tutto e ci si ferma lì. [[credenziali]]

## Far modificare il sito al cliente

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

## Liste e banco DM

- **Una frase di verifica ripetuta su sessanta righe è un modello, non un
  controllo.** Lista dell'8 settembre: 62 righe su 68 con la stessa frase,
  almeno 20 su 72 col sito. → ogni riga dice cosa è stato cercato e cosa è
  uscito; `02-Sales/strumenti/controlla-lista.py` ferma la lista prima della
  pubblicazione. [[contattati]]
- **`python3 -m http.server` non scrive niente.** Se il browser deve lasciare
  traccia nel vault serve un handler `POST` (stdlib, `banco-server.py`): il
  file si aggiorna sul disco di chi clicca, e nel brain arriva solo col push —
  che il server fa da solo, con un timer, e alla chiusura via segnale. Con
  `SIGKILL` il timer non parte e il commit si perde.

## Skill e strumenti di processo

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
  l'assegnata e lo si scrive.

## Collegamenti

[[registro-interventi]] · [[processo-siti]] · [[convenzioni]] · [[netlify]] ·
[[design-frontend]]
