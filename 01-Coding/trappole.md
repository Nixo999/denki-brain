---
type: risorsa
updated: 2026-09-07
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
- **`file://` non è il sito**: aperto come istantanea statica (URL `data:`) non
  gira JS e non carica le immagini relative. Si riapre dal server prima di
  concludere che qualcosa è rotto. ([[sito-fiftynine]])

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

## Scraping

- **Gli URL delle foto Instagram scadono** (firme CDN a giorni). → si scaricano
  in locale subito, nella stessa sessione.
- **L'handle esatto va chiesto, non indovinato.** `castiglione_furniture` è
  inglese: quattro username italiani tentati, zero risultati, risolto da uno
  screenshot di Nicola.
- **Il dump grezzo dello scraping non si committa.** Su [[sito-ngbarber]] è
  finito nel commit iniziale di una repo pubblica e adesso resta nella storia.

## Collegamenti

[[registro-interventi]] · [[processo-siti]] · [[convenzioni]] · [[netlify]] ·
[[design-frontend]]
