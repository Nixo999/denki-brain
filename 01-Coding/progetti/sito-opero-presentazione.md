---
type: progetto
riga: Sito di presentazione di OperO per Seba (29/10/2026) - «Una mattina, messa in ordine», stile pagina prodotto Apple, schermi di OperO ricostruiti in DOM, Astro e GSAP; bozza su Netlify.
status: attivo
client: sebastian-torres
stack: [astro, gsap, netlify]
started: 2026-10-29
deadline: TODO
updated: 2026-10-29
source: claude
tags: [opero, sito, presentazione, astro, gsap, apple]
---

# Sito di presentazione di OperO — giro 1 «Una mattina, messa in ordine»

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

## Aperto

- Il bottone «Chiedi una dimostrazione» punta a `#domani`: manca l'indirizzo mail a cui mandare chi chiede. Lo dà Nicola
  (o Seba).
- Nessun prezzo nel sito, di proposito: il listino di OperO è di Seba ([[opero]]).
- CO-OPERO è presentato come portale gratuito dei clienti (flusso 1, online sul sito di prova dall'8/10): la pagina
  Gruppo e i fornitori non ci sono, perché stanno su un ramo locale ([[opero-intermediar-receive]]).
- Nessuna promessa fuori dal prodotto: niente notifiche push, niente App Store, niente chat.
- Dominio: `opero-presentazione.netlify.app` è una bozza; il dominio vero lo decide Seba (ha già `operoworkspace.com`).

## Collegamenti

[[opero]] · [[sebastian-torres]] · [[co-opero-prototipo]] · [[processo-siti]] · [[direttive-siti]] · [[trappole]]
