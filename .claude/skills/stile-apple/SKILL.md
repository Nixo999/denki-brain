---
name: stile-apple
description: Come si progetta un'interfaccia web che sembri fatta da Apple - gestionali, dashboard, app web e pagine prodotto nello stile di apple.com. Da usare quando si chiede «stile Apple», «come un'app del Mac o dell'iPhone», «stile iOS o macOS», Liquid Glass o «tipo apple.com», sia per progettare da zero sia per rifare il design di un'app esistente. Contiene token CSS verificati sulle linee guida Apple e sul CSS di apple.com (colori chiari, scuri e ad alto contrasto, tipografia macOS e iOS), i componenti, il vetro con i ripieghi, il metodo di revisione e uno script di controllo. Dentro un repository vince il suo CLAUDE.md; sui siti vetrina il processo resta quello di processo-siti.
---

# Stile Apple: interfacce web che sembrano fatte da Apple

Nicola il 20 ottobre 2026 ha chiesto una skill che insegni a rifare il design di
un'intera app «in stile Apple, ma seriamente». Questa skill nasce da quattro
ricerche fatte quel giorno:

- le Human Interface Guidelines (HIG) lette dal JSON ufficiale di developer.apple.com;
- i colori di macOS 26 misurati sul Mac di Nicola con uno script Swift;
- il CSS vero di apple.com (home, MacBook Air, iPhone);
- sei skill della community, confrontate fra loro e con le fonti Apple.

Le skill della community sbagliano parecchi valori, e qui sono corretti. Ad
esempio usano grigi che sul web non passano il contrasto, mettono un tracking
negativo su tutti i titoli e danno per supportata ovunque una preferenza di
sistema che Safari non legge. Ogni numero in `apple.css` dice da dove viene.

## Direttive di Nicola: valgono sopra le regole qui sotto

### 20/10/2026 — Nicola: «no allora cosi troppo poco, migliorato rispetto alla base, ma voglio molto piu simile a apple, voglio il liquid glass in giro e vogio animziomi stile apple ovunque»

Verdetto sulla prima prova su OperO e CO-OPERO, che aveva tenuto il vetro solo
su barre e isole e il movimento al minimo. Quando si applica lo stile Apple a
un'app si va fino in fondo: il Liquid Glass si vede sulle superfici (barre,
isole, pannelli, card, menu, tasti), con il fondo colorato che serve a farlo
leggere, e ogni interazione ha un'animazione Apple a molla. Le regole
«Vetro e materiali» 1 e 6 e «Movimento» 1 e 5 qui sotto sono **superate**
per le app: restano valide la leggibilità (4,5:1 anche sul vetro), i ripieghi
per Riduci trasparenza e Riduci movimento, e il divieto di toccare la
struttura.

## Cosa c'è nella cartella

| File | A cosa serve |
|---|---|
| `apple.css` | Token e componenti: colori, tipografia, forme, vetro, movimento, bottoni, campi, switch, liste, sidebar, tabelle, menu, sheet, avvisi, stati vuoti. |
| `esempio.html` | Una schermata di gestionale completa fatta solo con `apple.css`: sidebar, lista, scheda cliente, menu, sheet, avviso, tab bar su telefono. Si apre nel browser ed è il modello da copiare. |
| `riferimenti/componenti.md` | Per ogni componente: quando si usa, misure, stati e divieti delle HIG. |
| `riferimenti/applecom.md` | Lo stile delle pagine prodotto di apple.com, con i valori misurati sul CSS. |
| `controlla-apple.py` | Lo script che cerca gli errori nel codice. Con `--prova` verifica sé stesso. |

## Prima di tutto: quale Apple

Si dice «stile Apple» per due cose diverse, e mescolarle è l'errore più comune.

| Si sta facendo | Si segue | Come si riconosce |
|---|---|---|
| Un'app: gestionale, dashboard, area clienti, app per telefono | Le HIG, cioè le app del Mac sul computer e quelle dell'iPhone sul telefono | Corpo a 13 px e controlli da 28 px sul computer; corpo a 17 px e bersagli da 44 px sul telefono |
| Una pagina prodotto o una landing | `riferimenti/applecom.md` | Corpo a 17 px, titoli a peso 600 fino a 80 px, sezioni alte 160 px |

Un gestionale con titoli da 80 px sembra una brochure. Una landing con il corpo a
13 px sembra un pannello di controllo.

## Dove vale e dove comanda altro

- **Dentro un repository comanda il suo `CLAUDE.md`.** OperO (Tailwind 3) e
  DenkiShift (Tailwind 4) hanno già token CSS e `lucide-react`. Lì i valori di
  `apple.css` si copiano dentro i token che esistono già: non si aggiunge un
  secondo sistema di token accanto al primo.
- **Sui siti vetrina il processo resta `processo-siti`.** Questa skill può
  essere la skill di stile del passo 3 solo se la direzione scelta è Apple. Le
  direttive dei siti restano tutte: la personalità del cliente, le sue foto, lo
  studio dei font.
- **I testi** seguono `scrittura-sito` e, se li legge un cliente, `voce-denkicode`.

## Il metodo per rifare un'app

0. **Una riga di contesto.** Si scrive che superficie è, chi la usa e su che
   schermo. Un gestionale usato al banco su un portatile non è un'app da
   telefono.
1. **Audit senza toccare il codice.** Si fa l'elenco delle schermate e dei
   componenti. Per ogni elemento si scrive a quale strato appartiene:
   contenuto, controlli e navigazione, oppure elemento temporaneo (menu, sheet,
   avvisi). Poi si lancia `controlla-apple.py` e si scrivono i rilievi nel
   formato della sezione «La revisione».
2. **I token.** I valori di `apple.css` vanno nei token del progetto. Da qui in
   poi nessun colore si scrive a mano in un componente.
3. **Una schermata alla volta**, partendo dalla più usata. Dopo ogni schermata
   si fanno le catture a 1440×900 e a 375×812, in chiaro e in scuro, si rilancia
   lo script e si rifà la revisione. Si passa alla schermata successiva solo
   quando non restano rilievi critici o alti.
4. **Alla fine si cerca una cosa da togliere.** Se non c'è, lo si scrive.

Per un'app nuova si parte da `esempio.html` e se ne sostituisce il contenuto.

## Le regole che fanno la differenza

### Gerarchia e impaginazione

1. Sul computer si usa la vista divisa delle app del Mac: sidebar, lista e
   dettaglio, con la selezione sempre visibile. Sul telefono si vede una colonna
   alla volta, si entra nel dettaglio e si torna con «‹ Clienti». La tab bar in
   basso ha da tre a cinque sezioni.
2. Il passaggio da una forma all'altra lo decide lo spazio, non il modello del
   dispositivo. In `apple.css` è la media query `(pointer: fine) and
   (min-width: 1024px)`.
3. Si raggruppa con lo spazio e con le superfici, non con bordi e ombre. Il
   modello sono i gruppi bianchi su fondo `#f5f5f7` delle Impostazioni.
4. C'è una sola azione primaria per vista, a destra nella barra. Le altre azioni
   vanno nel menu «…».
5. Le informazioni e le azioni importanti non vanno in fondo alla sidebar o alla
   finestra, perché la finestra può uscire dallo schermo.

### Colore

1. Un solo colore d'accento, `#0071e3`, per le azioni e la selezione. Il colore
   del marchio del cliente va nel contenuto (foto, illustrazioni, grafici) e non
   sui controlli: lo dice la pagina Branding delle HIG.
2. **Il testo colorato usa i token `--*-text`**, cioè la colonna «contrasto
   aumentato» della tabella dei colori Apple. In chiaro Apple li ha tarati tutti
   fra 4,5:1 e 6:1 su bianco. I colori normali (`--red`, `--green` e gli altri)
   servono per riempimenti, icone, pallini e grafici: come testo su bianco
   scendono fino a 1,5:1.
3. **I grigi del testo sono opachi**: `#6e6e73` come su apple.com. I grigi
   trasparenti delle app Apple sul web danno 3,4:1 e non passano. È la sola
   differenza voluta rispetto alle app native, ed è scritta qui perché nessuno la
   «corregga».
4. Uno stato si mostra con un pallino colorato più una parola, mai con il solo
   colore.
5. Il tema scuro non è un'inversione. Lo sfondo è `#000`, le superfici
   `#1c1c1e`, menu e sheet `#2c2c2e`. Ogni schermata si guarda in tutti e due i
   temi.

### Tipografia

1. Si usa il font di sistema e non si carica nessun file. Su Mac e iPhone il
   browser mostra SF, altrove il font del sistema. SF Pro non si può caricare
   come font web: la licenza di Apple lo vieta.
2. Inter si carica solo se una pagina vetrina deve sembrare uguale anche su
   Windows. È un font libero (licenza OFL) e il più vicino a SF, ma fa scattare
   l'avviso di `controlla-slop`, quindi è una scelta da dichiarare.
3. Sul font di sistema non si scrive `letter-spacing`, perché il sistema regola
   già da sé la spaziatura in base alla dimensione. Lo abbiamo dedotto da una
   misura su Chromium del 20/10/2026; su Safari non è ancora provato.
   L'eccezione sono i titoli da 48 px in su delle pagine prodotto
   (`riferimenti/applecom.md`).
4. La scala è quella del Mac sul computer e quella dell'iPhone sul telefono:
   `apple.css` cambia i valori da sola. I pesi sono 400 e 600; il 700 solo per i
   titoli grandi. Ultralight, Thin e Light non si usano.
5. I numeri in colonna (importi, date, orari) usano `font-variant-numeric:
   tabular-nums`, cioè la classe `.num`.

### Vetro e materiali

1. ~~Il vetro è lo strato dei controlli: barre, tab bar, menu, popover, sheet.
   Non va mai su card, righe di lista, sezioni o sfondi.~~ *Superata il
   20/10/2026 per le app (direttiva di Nicola in cima): il vetro va anche
   sulle card e sui pannelli, con il fondo colorato dietro.*
2. La ricetta è quella della barra di apple.com: `rgba(250,250,252,.8)` con
   `saturate(180%) blur(20px)`. Ha sempre un ripiego a sfondo pieno per
   `@supports`, Riduci trasparenza, Aumenta contrasto e colori forzati, e la
   classe `.glass` lo fa già.
3. Sul vetro va solo testo primario. Nel caso peggiore il grigio secondario
   scende a 3:1.
4. Il vetro serve solo se dietro scorre del contenuto. Su uno sfondo piatto la
   sfocatura non si vede, quindi lì si usa uno sfondo pieno.
5. Il Liquid Glass di iOS 26, con la rifrazione, sul web non si fa: funziona
   solo su Chrome e costa a ogni fotogramma.
6. ~~Si vedono al massimo due o tre superfici di vetro alla volta.~~ *Superata
   il 20/10/2026 per le app (direttiva di Nicola in cima).*

### Forme e ombre

1. I raggi seguono la regola concentrica delle HIG: un angolo dentro un altro ha
   come raggio quello esterno meno lo spazio fra i due. Il menu ha raggio 12 e
   padding 5, quindi le voci hanno raggio 7.
2. Sul computer i controlli sono rettangoli arrotondati da 8 px; sul telefono
   sono capsule. Le card hanno raggio 18 px, le sheet 28 px.
3. Le ombre vanno solo su ciò che galleggia: menu, popover, sheet. Le card non
   hanno ombra e si staccano dal fondo grazie al colore.

### Icone

1. Si usa un solo set, Lucide, che OperO e DenkiShift hanno già. Il tratto è
   1,75 e la dimensione segue il testo: 16 px sul computer e 22 px sul telefono.
   Le icone della sidebar sono nel colore d'accento, come su macOS.
2. SF Symbols non si possono usare sul web, perché la licenza li limita alle
   piattaforme Apple. I loro nomi però servono a scegliere l'icona giusta: la
   tabella è in `riferimenti/componenti.md`.
3. Le emoji non si usano come icone.

### Movimento

1. ~~Sulle azioni frequenti il movimento è poco e breve, come chiedono le HIG:
   hover e pressione cambiano il colore in 150 ms. Il bottone non si
   rimpicciolisce.~~ *Superata il 20/10/2026 per le app (direttiva di Nicola
   in cima): ogni interazione ha una molla Apple, compresa la pressione.*
2. Sheet e pannelli entrano con `--spring`, la molla predefinita di SwiftUI
   (response 0,55, smorzamento 1, nessun rimbalzo), campionata in CSS.
3. Il resto usa `cubic-bezier(.4, 0, .6, 1)`, la curva più usata su apple.com.
4. Con Riduci movimento gli spostamenti diventano dissolvenze, e `apple.css` lo
   fa da solo.
5. ~~Niente rimbalzi, contatori che salgono o scene allo scroll dentro un'app.~~
   *Superata il 20/10/2026 per le app (direttiva di Nicola in cima): le molle
   con un rimbalzo leggero, come `.snappy` e `.bouncy` di SwiftUI, sono
   ammesse. Restano vietati i contatori che salgono.*

### Stati e testi

1. Sotto i 100 ms di attesa non si mostra niente. Fino a 10 secondi si mostra uno
   scheletro della stessa forma del contenuto. Oltre i 10 secondi si mostra una
   barra di avanzamento con il pulsante Annulla.
2. Uno stato vuoto ha un simbolo, un titolo, una riga di spiegazione e
   un'azione per uscirne.
3. Un errore si scrive vicino al campo e dice cosa fare: «Scrivi un'email
   completa, ad esempio nome@esempio.it». Non si scrive mai solo «Errore» o
   «Non valido».
4. Si chiede conferma solo per ciò che non si può annullare. Per il resto si
   offre Annulla dopo l'azione.
5. I bottoni hanno un verbo: «Salva», «Elimina cliente». Se aprono un passo in
   più finiscono con i puntini («Condividi scheda…»). Accanto a Salva o Fine c'è
   sempre Annulla.
6. I titoli dei gruppi sono in maiuscolo/minuscolo, non tutti in maiuscolo: è
   così da iOS 26.

## Accessibilità: le soglie

| Cosa | Soglia | Dove è già risolto |
|---|---|---|
| Testo | 4,5:1; 3:1 da 24 px, o da 19 px in grassetto | token `--label*`, `--*-text`, `--link` |
| Bordo di un campo | 3:1 | `--border-input` |
| Bersaglio | 44×44 px sul telefono, 28×28 sul computer (WCAG: minimo 24) | `--control-h` |
| Focus da tastiera | sempre visibile | `:focus-visible` in `apple.css` |
| Preferenze di sistema | contrasto, movimento, trasparenza, colori forzati | blocchi `@media` in `apple.css` |

Un'eccezione è voluta: lo switch acceso usa il verde di Apple, che su bianco fa
2,2:1. Se il cliente ha obblighi di accessibilità stretti, ad esempio un ente
pubblico, si usa `--green-text`.

## Tailwind

Con Tailwind 4 (DenkiShift) i token si espongono così; i nomi a sinistra vanno
adattati a quelli che il repo usa già:

```css
@import "tailwindcss";
@import "./apple.css";
@theme inline {
  --color-label: var(--label);
  --color-label-2: var(--label-2);
  --color-accent: var(--accent);
  --color-page: var(--bg-page);
  --color-surface: var(--bg-surface);
  --color-separator: var(--separator);
  --font-sans: var(--font);
  --radius-control: var(--radius-control);
}
```

Con Tailwind 3 (OperO) si fa lo stesso in `tailwind.config.js`, sotto
`theme.extend.colors`, scrivendo ad esempio `label: 'var(--label)'`. I
modificatori di opacità come `bg-accent/50` non funzionano con queste variabili:
per le trasparenze ci sono i token `--fill-*`.

## La revisione

Il metodo viene da `dickwu/apple-design-skill`, la skill della community più
usata. Si guarda con cinque lenti, sempre in quest'ordine:

1. **Accessibilità.** Un fallimento qui è sempre critico.
2. **Convenzioni**: quelle Apple di questa skill e quelle del web.
3. **Mestiere visivo**: gerarchia, spazio, coerenza dei raggi e delle icone. Ci
   si chiede se la schermata sembra un modello preso da un catalogo.
4. **Interazione**: caricamento, risposta ai clic, sheet, annullamento,
   inserimento dei dati.
5. **Testi**: verbi sui bottoni, errori che dicono cosa fare, stati vuoti con
   un'uscita.

Ogni rilievo si scrive così, con numeri e non con aggettivi:

```
[Critico | Alto | Medio | Basso]  Clienti › lista, .row .email  (oppure file:riga)
Regola:     testo secondario 4,5:1 (WCAG 1.4.3)
Misura:     rgba(60,60,67,.6) su #fff = 3,44:1, calcolato
Correzione: var(--label-2), cioè #6e6e73 = 5,07:1
Verifica:   cattura a 375 px in chiaro, script di contrasto
```

Il giudizio finale si ricava dai rilievi. Con un rilievo critico la schermata
«ha problemi critici». Con più rilievi alti «va rifatta». Senza critici e con
al massimo due alti «è buona». È «ottima» solo se non c'è niente sopra il medio
e la schermata ha un'idea riconoscibile. Ciò che non si è potuto misurare si
scrive come limite, non come rilievo.

## Il controllo

```bash
python3 ~/.claude/skills/stile-apple/controlla-apple.py <cartella del progetto>
```

Lo script esce con 1 se trova un errore che blocca: SF Pro caricato come font,
glifi di SF Symbols, `prefers-contrast: high` (valore che non esiste), zoom
bloccato, focus tolto senza alternativa, animazioni senza Riduci movimento.
Avvisa invece su vetro senza prefisso o senza ripiego, vetro sul contenuto,
`transition: all`, animazioni di misure, curve che rimbalzano, testo tutto
maiuscolo, pesi 800 e 900, font caricati, scala alla pressione, emoji, colori
scritti a mano, troppi raggi diversi. Un avviso è un indizio: si apre il file e
si guarda.

Nessuno script vede la gerarchia, l'idea della schermata o la qualità delle
foto. Quelle si guardano nelle catture.

## Gli errori che fanno sembrare finta un'imitazione Apple

- Vetro su tutto, anche su card e righe, oppure vetro su uno sfondo piatto.
- Grigi trasparenti illeggibili, copiati dai valori di iOS.
- Più colori d'accento, gradienti viola o azzurri, colore del marchio su ogni
  controllo.
- Titoli a peso 700-800 e tracking negativo su tutti i titoli.
- Font SF Pro caricato dal sito, oppure Inter senza un motivo.
- Bottoni che si rimpiccioliscono, curve che rimbalzano, `transition: all`.
- Card con bordo da 1 px più ombra, con raggi diversi a ogni livello.
- Icone di set diversi, emoji al posto delle icone, glifi di SF Symbols.
- Titoli dei gruppi tutti in maiuscolo.
- Tab bar in basso su un sito vetrina: va bene solo nelle app.
- Tema scuro che inverte i colori invece di usare i fondi `#000` e `#1c1c1e`.
- Un modale per ogni cosa, «OK» e «Sì/No» invece di verbi.

## Licenze

- **SF Pro e SF Symbols** non si usano sul web. La pagina developer.apple.com/fonts
  vieta di incorporare il font e di usarlo per contenuti web. Per SF Symbols il
  divieto risulta da thread del forum sviluppatori Apple. Il testo originale
  delle licenze sta nei pacchetti `.dmg` di Apple, che non abbiamo aperto.
- **Lucide** ha licenza ISC; `esempio.html` ne contiene 13 icone.
- Dalle skill della community senza licenza dichiarata (`dickwu`, `bkhoi0311`)
  abbiamo preso idee e verificato numeri, senza copiare testo o codice.
  `axiaoge2` e `Armitanemati` sono MIT.

## Fonti

Lette il 20 ottobre 2026.

- HIG: https://developer.apple.com/design/human-interface-guidelines (pagine
  color, typography, materials, layout, motion, accessibility, dark-mode, icons,
  sf-symbols, writing, branding e le pagine dei componenti), lette dal JSON
  `developer.apple.com/tutorials/data/design/human-interface-guidelines/<pagina>.json`.
- SwiftUI, animazione predefinita: https://developer.apple.com/documentation/swiftui/animation/default
- apple.com: i fogli di stile di `/`, `/macbook-air/` e `/iphone/`.
- https://github.com/dickwu/apple-design-skill (metodo di revisione)
- https://github.com/axiaoge2/apple-hig-designer (MIT)
- https://github.com/Armitanemati/liquid-glass-claude-skill (MIT, ripieghi del vetro)
- https://github.com/bkhoi0311/liquid-glass-design (stati e pagine prodotto, solo idee)
- https://github.com/VoltAgent/awesome-design-md, file `design-md/apple/DESIGN.md` (MIT)
- WebKit, font di sistema nel web: https://webkit.org/blog/3709/using-the-system-font-in-web-content/

## Cosa resta da verificare

- Se Safari applica da solo il tracking di SF con `system-ui`. Su Chromium la
  misura dice di sì.
- Le misure dei componenti di iOS 26 e macOS 26 (altezze, raggi, larghezze delle
  sheet). Apple le pubblica solo nei kit di design, che non abbiamo aperto. Le
  misure segnate «[nostra]» in `apple.css` vanno confrontate con quei kit.
- I colori semantici di iOS vengono da fonti del 2019-2020 e non sono stati
  rimisurati su iOS 26. Per questo `apple.css` usa i grigi di apple.com.
