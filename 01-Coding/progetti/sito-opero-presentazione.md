---
type: progetto
riga: Sito di presentazione di OperO per Seba (29/10/2026) - giro 3: scuro, hero con pezzi veri dell'app, mattina a fumetti con tre figure anatomy, scena ferma con il logo che ruota, passaggi a soglia; bozza su Netlify.
status: attivo
client: sebastian-torres
stack: [astro, gsap, netlify]
started: 2026-10-29
deadline: TODO
updated: 2026-10-29
source: claude
tags: [opero, sito, presentazione, astro, gsap, apple]
---

# Sito di presentazione di OperO — giro 3 «pezzi veri, fumetti, passaggi a soglia»

Sito che presenta [[opero]] alle aziende a cui [[sebastian-torres]] lo vende. Nicola il 29/10/2026: «deve spiegare in
modo molto semplificato cosa fa OperO e come funziona, Seba vuole che non sia per niente un muro di testo, colori di
OperO, molto più animato dei siti che facciamo di solito, deve sembrare una presentazione animata quasi come un video,
fluido, niente lag, pulizia totale, come un sito di quelli che fa la Apple, italiano perfetto, poche spiegazioni
all'inizio e più premesse di cosa risolve, poi le spiegazioni serie».

**Cartella**: `~/lavoro/opero-presentazione-site`, ramo `main`, nessun remoto per ora. Non è dentro `opero-sito`: è un
sito statico a parte, con il suo `CLAUDE.md`.
**Online**: sito Netlify `opero-presentazione` (id `89281cd5-6c67-4fb0-86d1-8d8374c4fc64`, team denkicode), indirizzo
<https://opero-presentazione.netlify.app>. Si ripubblica con `npm run build && npx netlify-cli deploy --prod --dir dist
--site 89281cd5-6c67-4fb0-86d1-8d8374c4fc64` (sempre con `--site`: la cartella non è collegata). I tre sbarramenti
restano finché Seba non lo adotta.
**Memoria tecnica nel repo**: `direzione/DIREZIONE.md` (il mondo, la palette, la motion, le regole di prestazione, il
contratto fra gli operatori), `direzione/testi.md` (ogni frase del sito, parola per parola), `direzione/pagina.md` e
`direzione/motion.md` (i rapporti dei due operatori), `CLAUDE.md`.

## Com'è fatto

- **La spina** è il ciclo vero di un lavoro in OperO, nell'ordine in cui si usano le pagine: nasce in ufficio (Nuovo
  lavoro) → arriva sul telefono (Turni) → si chiude dal cantiere (Chiudi chiamata) → diventa conti → diventa fattura; poi
  calendario, CO-OPERO e dove gira. Prima, una scena scura con cinque righe una alla volta e sei bolle di chat: la
  mattina del caos. Alla fine, la stessa mattina con il telefono in tasca.
- **Niente foto, niente disegni**: la grafica sono gli schermi di OperO ricostruiti in DOM (moduli, schede, una tabella
  dei conti, un foglio di fattura, un calendario) dentro cornici di telefono e di computer fatte in CSS, che si
  costruiscono da soli quando entrano. L'unico disegno è il simbolo di OperO, ricostruito in SVG dalle misure del PNG
  (scarto massimo 1 px sulla riga centrale, 1,9 % di pixel diversi). Il manico misurato è largo 40 px, non 50.
- **Colori di OperO**, presi da `src/index.css` dell'app e dal logo: carta `#FAF9F7`, inchiostro `#0D1E26`, notte
  `#0B1B25`, blu marchio `#0E3049`, ciano `#00A7CF`, menta `#4DCBBB` per le spunte. Due campi soli, carta e notte, e il
  passaggio è sempre una dissolvenza su uno schermo sticky. Font **Inter** variabile, perché è il font dell'app:
  `controlla-slop.py` lo segnala e la scelta è dichiarata qui.
- **La motion**: apertura di 1,1 s (il simbolo si disegna e si riempie, le lettere salgono, poi la riga e la barra),
  due sole scene sticky (`#mattina` e `#domani`) con `scrub: true`, le tre frasi dell'ordine attaccate al dito, gli
  schermi che si compongono pezzo per pezzo, parallasse leggera solo da computer. Solo `transform` e `opacity`, niente
  `will-change` in CSS, niente blur sulla barra. I testi li ha scritti Trevis su Fable; la pagina e la motion due
  operatori Opus in parallelo con un contratto di DOM.

## Misurato il 29/10/2026, in headless (nessuna finestra sul Mac di Nicola)

| Cosa | 1440×900 | 375×812 |
|---|---|---|
| fotogramma peggiore nello scroll | 18 ms | 18 ms |
| fotogrammi oltre 20 ms | 0 | 0 |
| larghezza del documento | 1440 | 375 |
| `controlla-sito.py` | 8/8 | |
| `controlla-slop.py` | 0 blocca, 5 avvisi (Inter, «davvero», og:image, impeccable) | |
| `controlla-testo.py` | 0 | |

L'apertura è ferma a 1,1 s (i fotogrammi a 1100 e 1400 ms sono identici). **Mai visto su un browser vero né su un
iPhone**, e Seba non l'ha ancora visto.

## Giro 2 (29/10, mattina): il verdetto di Nicola e cosa è cambiato

Nicola sul giro 1: «non mi piace su sfondo bianco, e va bene la teatralità fatta così ma forse un po' troppo tutto il
sito che scorre sempre, a un certo punto fai stare fermo il sito e anima qualcosa magari con il logo in grande a
sinistra che si gira o che si muove e a destra delle slide che spiegano, non troppo lungo», e sui testi: «ho detto di
scrivere come un professionista ma a me sembrano frasi di un bambino con poco senso. prima fatti uno schema tuo dove
metti in ordine cosa vuoi dire, poi come vuoi dirlo e poi scrivilo seguendo delle regole». Tutte e due le frasi sono in
[[direttive-siti]].

- **Tutta la pagina è scura**, sul blu notte del disco del logo (`#08141C`), con tre luci ciano; gli schermi usano il
  tema scuro vero di OperO (`.dark` in `src/index.css`), il foglio della fattura resta chiaro.
- **La scena ferma** (`#presentazione`): la pagina sta ferma, a sinistra il disco con il simbolo ruota di 72° a ogni
  passaggio (ghiera con cinque tacche), a destra cinque slide nell'ordine del ciclo di un lavoro: Nuovo lavoro, Turni,
  Chiudi chiamata, Conti e fattura, Calendario. I sette quadri e la sezione «L'ordine» del giro 1 spariscono; la
  mattina scende a tre righe. La pagina passa da 13.766 a 9.573 px a 1440.
- **I testi, in tre passi**: `direzione/schema-testi.md` (cosa dire, in che ordine), `direzione/regole-scrittura.md`
  (ricerca di un operatore Opus su otto pagine prodotto italiane misurate, Apple compresa, e sulle guide di Carrada,
  Sapienza, Microsoft, più le skill `scrittura-sito`, `voce-denkicode`, `copy-generation` e `copywriting` di Corey
  Haines, trovata e non installata), poi `direzione/testi.md` v2. La diagnosi: il giro 1 aveva copiato da Apple i
  titoli corti senza il paragrafo da 30 parole che Apple mette sotto, metà delle righe senza soggetto o verbo,
  metafore da decifrare («entrano dalla porta giusta»), «chiamata» mai spiegata. Nella v2 ogni frase ha soggetto e
  verbo, i titoli dicono un fatto, si dà del tu al titolare e i ruoli restano in terza persona.

| Misurato il 29/10 in headless, sulla porta giusta | 1440×900 | 375×812 |
|---|---|---|
| fotogramma peggiore nello scroll | 18 ms | 18 ms |
| fotogrammi oltre 20 ms | 0 | 0 |
| controlli sito / slop / testo | 8/8, 0 blocca (3 avvisi: gruppi di tre, Inter, sezioni senza numero), 0 | |
| contrasti (titoli / corpo / indici) | 17,7 / 9,4 / 5,1 | |

⚠️ Le misure del giro 1 attribuite al direttore erano fatte sulla porta sbagliata (un'anteprima di Marta Cesena di
un'altra sessione rispondeva su 4342): valgono solo quelle dell'operatore motion sulla sua copia. Trappola scritta in
[[trappole]]. Sul telefono il corpo della slide 1 occupa sette righe e lo schermo è piccolo (148×306): da guardare.

## Giro 3 (29/10, tarda mattina): il verdetto sul giro 2 e cosa è cambiato

Nicola: «la frase sotto il titolo OperO nella hero section non mi piace, dai un po' più di dettaglio alla hero section
aggiungendo qualche elemento decorativo preso da qualcosa di reale in OperO, poi l'inizio con solo la scritta grande non
mi piace, metti delle immagini o dei disegni e accorcia le frasi, fai tipo fumetti magari. e poi allo scroll non risulta
abbastanza fluido per essere una presentazione allo scroll». Le tre frasi sono regole in [[direttive-siti]].

- **L'hero**: occhiello `Facchinaggio · Allestimenti · Traslochi`, riga nuova («Il gestionale che organizza le squadre
  in cantiere e trasforma le ore in fatture.»), e attorno al simbolo cinque componenti veri dell'app (scheda Turni, riga
  Richieste che passa da In attesa ad Accettata, etichette della squadra, isola di navigazione, riga dei conti) in
  prospettiva, che galleggiano e hanno una parallasse allo scroll; due sotto 768 px.
- **La mattina a fumetti**: tre quadri, ognuno con una figura isometrica prodotta dalla skill `anatomy` (l'unico disegno
  ammesso dalla direttiva del 23/10): la scrivania alle sei con il telefono sganciato e l'orologio su 06:00, il furgone
  con le porte aperte e il transpallet, il foglio delle ore sotto la lampada con la calcolatrice. Tre operatori Opus in
  parallelo con un contratto di stile (quattro toni per materiale, stessa camera a 35,26°, 53-59 KB l'una, nessun
  filtro, una o due animazioni CSS). Nuvoletta con chi parla e frase corta («Chi va a Rho stamattina?»), didascalia di
  una frase. Le righe lunghe del giro 2 e le bolle di chat sono sparite.
- **I passaggi a soglia**: slide, disco, fumetti e svolta non sono più legati alla rotella in scrub, ma scattano a una
  soglia e si completano in 0,5-0,6 s con una curva morbida; il disco va sempre alla rotazione assoluta (0, 72, 144,
  216, 288 letti dopo scatti di rotella da 100 px e dopo salti con `scrollTo`); l'hero e la parallasse dei pezzi restano
  in scrub. Scena ferma a 60vh per slide, mattina a 340vh: pagina da 9.573 a 8.763 px.

| Misurato il 29/10 in headless, porta e titolo controllati | 1440×900 | 375×812 |
|---|---|---|
| fotogramma peggiore nello scroll | 20 ms | 23 ms (uno) |
| fotogrammi oltre 32 ms | 0 | 0 |
| peso di `dist/` | 588 KB | |
| controlli sito / slop / testo | 8/8, 0 blocca (3 avvisi), 0 | |

La fluidità vera si giudica solo con la rotella sul Mac di Nicola: in headless e nel pannello nascosto dell'app la
motion non gira. Trappole nuove in [[trappole]]: lo `<style>` di un SVG inline vale per tutta la pagina (prefissi su
classi e id), Chrome headless sul Mac non scende sotto i 500 px, gli operatori in parallelo condividono pannello e
scratchpad.

## Aperto

- Il bottone «Chiedi una dimostrazione» punta a `#domani`: manca l'indirizzo mail a cui mandare chi chiede. Lo dà Nicola
  (o Seba).
- Resta da guardare su un browser vero e su un iPhone; Seba non l'ha visto.
- Nessun prezzo nel sito, di proposito: il listino di OperO è di Seba ([[opero]]).
- CO-OPERO è presentato come portale gratuito dei clienti (flusso 1, online sul sito di prova dall'8/10): la pagina
  Gruppo e i fornitori non ci sono, perché stanno su un ramo locale ([[opero-intermediar-receive]]).
- Nessuna promessa fuori dal prodotto: niente notifiche push, niente App Store, niente chat.
- Dominio: `opero-presentazione.netlify.app` è una bozza; il dominio vero lo decide Seba (ha già `operoworkspace.com`).

## Collegamenti

[[opero]] · [[sebastian-torres]] · [[co-opero-prototipo]] · [[processo-siti]] · [[direttive-siti]] · [[trappole]]
