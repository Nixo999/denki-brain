# Componenti Apple tradotti per il web

Per ogni componente: quando si usa, le misure, gli stati e i divieti. Le regole
vengono dalle Human Interface Guidelines (HIG) lette il 20 ottobre 2026; la
pagina di origine è `developer.apple.com/design/human-interface-guidelines/<pagina>`.

Le HIG di oggi non scrivono quasi nessuna misura dei componenti: altezze, raggi
e larghezze stanno nei kit di design di Apple, che non abbiamo aperto. Per
questo ogni misura qui sotto dice da dove viene: **[HIG]** se è scritta nelle
linee guida, **[apple]** se è misurata sul CSS di apple.com, **[nostra]** se è
una scelta nostra da confrontare con i kit.

La classe CSS di ogni componente è in `apple.css`; `esempio.html` li mostra
tutti insieme.

## Come si traducono le piattaforme sul web

| Sul web | Si imita | Cosa cambia |
|---|---|---|
| Computer con mouse, da 1024 px | macOS | Corpo a 13 px, controlli da 28 px, sidebar fissa, barra in alto, menu con scorciatoie, hover, tabelle a più colonne |
| Telefono e tablet | iOS e iPadOS | Corpo a 17 px, bersagli da 44 px, tab bar in basso, una colonna alla volta, sheet dal basso, liste raggruppate |

La regola delle HIG è che decide lo spazio disponibile, non il tipo di
dispositivo, e che le funzioni restano le stesse: cambia quante se ne vedono.

## Bottoni — `.btn`

Pagina HIG: `buttons`.

- **Quando**: per un'azione. Non per scegliere uno stato (switch o controllo
  segmentato) né per scegliere da un elenco (menu a comparsa).
- **Stili**: `.btn` grigio per le azioni normali; `.btn-primary` pieno con
  l'accento, al massimo uno o due per vista [HIG]; `.btn-plain` solo testo, per
  le azioni nelle barre; `.btn-destructive` con il testo rosso.
- **Misure**: altezza 28 px sul computer e 44 sul telefono [HIG: bersagli
  28×28 e 44×44]. La capsula grande `.btn-lg` è alta 36 e 50 px [nostra].
- **Stati**: la pressione abbassa l'opacità o scurisce lo sfondo, senza scala
  [apple]. Un'azione lunga mostra un indicatore al posto dell'icona e cambia
  l'etichetta, ad esempio «Salva» diventa «Salvataggio…» [HIG].
- **Non fare**: dare lo stile primario a un'azione distruttiva; distinguere la
  scelta preferita con la dimensione invece che con lo stile; scrivere «Clicca
  qui». Un bottone che apre un altro passo finisce con «…» [HIG].

## Switch — `.switch`

Pagina HIG: `toggles`.

- **Quando**: per due stati opposti di un'impostazione. Su iPhone lo switch sta
  solo dentro una riga di lista, che gli fa da etichetta. Sul Mac, per una
  singola opzione dentro un modulo, va bene anche la casella di spunta.
- **Misure**: 51×31 px sul telefono [memoria del vecchio UISwitch, confermata da
  axiaoge2], 38×22 sul computer [nostra].
- **Colore**: verde sul telefono, accento sul Mac [HIG].
- **Non fare**: switch nelle barre; più di cinque pulsanti di opzione (oltre
  cinque si usa un menu a comparsa) [HIG].

## Controllo segmentato — `.segmented`

Pagina HIG: `segmented-controls`.

- **Quando**: per scegliere fra due e cinque viste o filtri strettamente legati,
  ad esempio Tutti, Attivi, Archiviati. Non serve per le sezioni dell'app, che
  vanno nella sidebar o nella tab bar.
- **Regole** [HIG]: segmenti larghi uguali; solo testo o solo icone, mai
  mescolati; etichette che sono nomi; circa cinque segmenti al massimo su
  iPhone e sette su uno schermo largo.
- **Misure**: alto 24 px sul computer e 36 sul telefono [nostra]; testo a 13 px
  su tutti e due; il segmento scelto è bianco in chiaro e `#636366` in scuro
  [HIG iOS].

## Liste raggruppate — `.group`, `.row`

Pagine HIG: `lists-and-tables`, `settings`.

- **Quando**: per impostazioni, schede di dettaglio, elenchi di voci con un
  valore a destra. È il disegno delle Impostazioni dell'iPhone e del Mac.
- **Anatomia**: titolo del gruppo sopra (`.group-title`, piccolo e grigio, in
  maiuscolo/minuscolo); righe con etichetta a sinistra e valore grigio a
  destra; nota sotto il gruppo (`.group-footer`) per spiegare cosa succede.
- **Separatori**: partono dal testo, non dal bordo; se la riga ha un'icona,
  partono dopo l'icona (`--sep-inset`).
- **Selezione**: in una lista che porta a un dettaglio la riga scelta resta
  evidenziata in blu, con il testo bianco [HIG, macOS].
- **Non fare**: titoli dei gruppi in maiuscolo (iOS 26 li ha tolti); una card
  dentro un'altra card. Per i sottogruppi si usano lo spazio e l'allineamento
  [HIG `boxes`].

## Sidebar — `.sidebar`, `.nav-item`

Pagina HIG: `sidebars`.

- **Quando**: sul computer, per le sezioni principali dell'app. Sul telefono
  diventa la tab bar.
- **Regole** [HIG]: al massimo due livelli; icone nel colore d'accento; titoli
  di gruppo brevi; la sidebar si può nascondere ma non è nascosta all'inizio;
  niente azioni importanti in fondo.
- **Misure**: larghezza fra 220 e 260 px [nostra; `esempio.html` usa 232];
  righe alte 28 px [nostra].
- **Selezione**: sfondo grigio, non blu pieno. L'icona resta nel colore
  d'accento.

## Barra degli strumenti — `.toolbar`

Pagina HIG: `toolbars`.

- **Anatomia** [HIG]: a sinistra il ritorno indietro e il titolo; al centro le
  azioni comuni; a destra le azioni importanti, la ricerca e il menu «…».
- **Regole** [HIG]: al massimo tre gruppi; un solo elemento in evidenza, a
  destra; icone senza contorno; titolo sotto i 15 caratteri e mai il nome
  dell'app; il pulsante indietro mostra la freccia e il nome della schermata
  precedente, mai la parola «Indietro».
- **Vetro**: la barra è di vetro solo se il contenuto le scorre sotto.

## Tabelle — `.table`

Pagina HIG: `lists-and-tables`.

- **Quando**: dati a più colonne sul computer. Sul telefono una tabella diventa
  una lista con due righe per voce.
- **Regole** [HIG macOS]: clic sull'intestazione per ordinare, secondo clic per
  invertire; colonne ridimensionabili; righe alternate nelle tabelle larghe;
  intestazioni con nomi, senza punteggiatura finale.
- **Misure**: righe alte 28 px sul computer [nostra]; righe alternate
  `#f4f5f5` [macOS misurato]; selezione `#0064e1` con testo bianco [macOS
  misurato].
- Gli importi sono allineati a destra e usano `.num`; le date restano a
  sinistra.

## Menu e popover — `.menu` con l'attributo `popover`

Pagine HIG: `menus`, `pull-down-buttons`, `pop-up-buttons`, `context-menus`, `popovers`.

- **Menu a tendina** (bottone «…»): comandi legati alla vista, da tre voci in su.
- **Menu a comparsa** (un `select`): una scelta fra opzioni che si escludono; il
  bottone mostra la scelta attuale.
- **Regole** [HIG]: voci con un verbo; «…» se la voce chiede altro; gruppi
  separati da linee, al massimo circa tre; un solo livello di sottomenu; le
  voci non disponibili sono grigie nei menu e nascoste nei menu contestuali; le
  voci distruttive sono rosse e stanno per ultime; le scorciatoie compaiono
  solo nei menu principali.
- **Aspetto**: sul Mac la voce sotto il puntatore diventa blu con il testo
  bianco [HIG]; raggio 12 e padding 5, voci con raggio 7 [nostra, regola
  concentrica].
- **Popover**: punta verso l'elemento che l'ha aperto, se ne apre uno alla
  volta e mai uno dentro l'altro, si chiude con un clic fuori e salva quello
  che c'è dentro [HIG].

## Sheet — `dialog.sheet`

Pagina HIG: `sheets`.

- **Quando**: per un compito breve, ad esempio un nuovo cliente o una modifica.
  Per un flusso lungo serve una pagina intera.
- **Regole** [HIG]: una sheet alla volta; sempre Annulla accanto a Salva o
  Fine; se ci sono modifiche non salvate, chiudere chiede conferma. Su iPhone
  la sheet sale dal basso con la maniglia; sul Mac compare al centro sopra la
  finestra oscurata.
- **Misure**: larghezza fino a 560 px e raggio 28 [nostra]; fondo oscurato al
  35 % [HIG usa il 35 % per il velo dietro il vetro; qui lo riprendiamo].

## Avvisi — `dialog.alert`

Pagina HIG: `alerts`.

- **Quando**: solo per un problema o per un'azione distruttiva e irreversibile.
  Non per informare: per quello basta un messaggio nel punto giusto. Non per le
  azioni che si possono annullare: per quelle si offre Annulla dopo.
- **Testo** [HIG]: un titolo che dice cosa succede, al massimo due righe; una
  riga di spiegazione solo se aggiunge qualcosa; da uno a tre bottoni con un
  verbo, mai «Sì» e «No».
- **Bottoni**: Annulla c'è sempre e si attiva anche con Esc. Il rosso va solo
  sull'azione distruttiva.
- **Aspetto**: testo allineato a sinistra [HIG, dal 2025]; larghezza 300 px
  [nostra].

## Stati vuoti — `.empty`

Pagine HIG: `tab-bars`, `loading`, `writing`.

- Un simbolo, un titolo, una riga che spiega e un'azione per uscirne. Una
  schermata con scritto solo «Nessun elemento» è un vicolo cieco.
- I casi sono quattro: prima volta (l'azione è «Crea il primo…»); ricerca senza
  risultati (si ripete il testo cercato e si propone di cancellare la
  ricerca); errore di caricamento («Riprova»); svuotato di proposito
  («Annulla»).

## Caricamento — `.skeleton`

Pagine HIG: `loading`, `progress-indicators`.

- Si mostra subito la struttura e poi la si riempie. Lo scheletro ha la stessa
  forma del contenuto vero.
- La barra di avanzamento si usa quando la durata è nota, la rotellina quando
  non lo è. Non si passa dalla rotellina alla barra, e un avanzamento non si
  ferma mai [HIG].

## Campi e moduli — `.field`

Pagine HIG: `text-fields`, `entering-data`.

- Ogni campo ha un'etichetta sopra. Il segnaposto mostra un esempio
  («nome@esempio.it») e non sostituisce l'etichetta.
- Si usa la tastiera giusta (`type="email"`, `inputmode="tel"`) e
  `autocomplete`.
- L'email si controlla quando si esce dal campo, i campi obbligatori al
  salvataggio. L'errore compare sotto il campo con `aria-invalid`.
- Il bordo è `#86868b` (3,6:1), come nei moduli di apple.com. Sul Mac i campi
  hanno un bordo più chiaro, che sul web non passa la soglia di 3:1.

## Ricerca — `.search`

Pagine HIG: `search-fields`, `searching`.

- Sul computer sta a destra nella barra o in cima alla lista; sul telefono in
  cima alla lista.
- Cerca mentre si scrive. Il segnaposto dice cosa si cerca («Cerca per nome o
  email»). C'è un modo evidente per cancellarla.

## Tab bar — `.tabbar`

Pagina HIG: `tab-bars`.

- Solo sul telefono e solo nelle app, mai su un sito vetrina.
- Da tre a cinque sezioni con etichette di una parola. Le sezioni non si
  nascondono e non si disattivano: se una è vuota, la schermata spiega perché.
- In iOS 26 è una capsula di vetro che galleggia in basso.

## Icone: dal nome Apple a Lucide

Le HIG indicano un simbolo standard per ogni azione comune. Sul web si usa il
corrispondente di Lucide.

| Azione | SF Symbol | Lucide |
|---|---|---|
| Aggiungi | `plus` | `plus` |
| Altre azioni | `ellipsis` | `ellipsis` |
| Elimina | `trash` | `trash-2` |
| Modifica | `square.and.pencil` | `square-pen` |
| Rinomina | `pencil` | `pencil` |
| Duplica | `plus.square.on.square` | `copy-plus` |
| Condividi | `square.and.arrow.up` | `share` |
| Cerca | `magnifyingglass` | `search` |
| Filtra | `line.3.horizontal.decrease` | `list-filter` |
| Fatto | `checkmark` | `check` |
| Chiudi, annulla | `xmark` | `x` |
| Annulla l'azione | `arrow.uturn.backward` | `undo-2` |
| Archivia | `archivebox` | `archive` |
| Calendario | `calendar` | `calendar` |
| Profilo | `person.crop.circle` | `circle-user` |
| Impostazioni | `gearshape` | `settings` |
| Mostra la sidebar | `sidebar.left` | `panel-left` |
| Allega | `paperclip` | `paperclip` |
