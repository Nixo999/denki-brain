---
type: risorsa
riga: Errori tecnici già pagati e strade scartate, per dominio. Descrittivo, non è un rulebook - le regole stanno in convenzioni.
updated: 2026-09-11
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

## CSS e layout

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

## Git, account e pubblicazione

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
- **I motori di ricerca senza chiave non reggono una lista.** DuckDuckGo html
  risponde 403 dopo ~50 richieste, Brave 429 dopo ~10, Bing ignora le
  virgolette e risponde con un'altra città. → la base è quello che non dipende
  da nessuno: indovinare i domini dal nome e aprirli (`verifica-sito.py`); i
  motori sono un extra con 12 s di pausa.
- **Una regola scritta cede sotto il volume.** «Verificato, mai dedotto» stava
  nel metodo dal 30 agosto ed è stata violata su 62 righe. → il passo si
  trasforma in uno script che scrive la prova nella riga, e un secondo script
  rifiuta la lista senza prova. La regola resta, ma non è più lei a reggere.
- **`python3 -m http.server` non scrive niente.** Se il browser deve lasciare
  traccia nel vault serve un handler `POST` (stdlib, `banco-server.py`): il
  file si aggiorna sul disco di chi clicca, e nel brain arriva solo col push —
  che il server fa da solo, con un timer, e alla chiusura via segnale. Con
  `SIGKILL` il timer non parte e il commit si perde.

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

## Collegamenti

[[registro-interventi]] · [[processo-siti]] · [[convenzioni]] · [[netlify]] ·
[[design-frontend]]
