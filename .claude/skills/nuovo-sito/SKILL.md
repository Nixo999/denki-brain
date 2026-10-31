---
name: nuovo-sito
description: Costruisce un sito vetrina DenkiCode nuovo partendo da un profilo Instagram, con /nuovo-sito @profilo. Raccolta del profilo (e del vecchio sito, se c'è), tre tavole di direzione fra cui sceglie Nicola, una sola testa che costruisce partendo dal catalogo delle sezioni approvate, i cancelli, le catture a 1440 e a 375. Da usare per ogni sito vetrina nuovo; per un sito già avviato o per i ritocchi vale processo-siti. Non vale per OperO e DenkiShift.
---

# /nuovo-sito @profilo

Nicola l'ha approvato il 31/10/2026: «Sì» alla domanda se un sito nuovo si fa
con una sola testa che costruisce e tre tavole di direzione
([[direttive-siti]], in cima). Serve a rendere costante la qualità: su 54 siti,
4 riusciti e 17 bocciati. Il gusto resta di Nicola: la pipeline prepara le
scelte, non le fa.

Lo stato della pipeline, le misure e le contraddizioni ancora aperte stanno in
`01-Coding/strumenti/pipeline-siti.md`. Il resto del processo (foto, catena
delle skill, consegna, sbarramenti) resta in `processo-siti`, che vale anche
qui dove questa skill non dice altro.

Chi lancia `/nuovo-sito` fa il **direttore**: raccoglie, lancia gli operatori,
misura e porta le scelte a Nicola. Non disegna e non scrive il codice del sito.

## 0. Prima di partire

- Il nome della cartella: `~/lavoro/<nome>-site`, kebab-case, come il repo.
- Il profilo Instagram e, se esiste, **il vecchio sito del cliente**. Su
  Groavel (31/10) Instagram ha dato 3 foto buone su 12 post, perché 9 erano
  Reel; le foto buone del sito che piace a Nicola venivano dal vecchio sito.
- `git pull` nel vault, poi si legge `01-Coding/stack/direttive-siti.md`.

## 1. La raccolta

1. Instagram, senza login, dal browser dell'app (mai una finestra di Nicola):
   si apre `instagram.com/<utente>/`, si incolla
   `01-Coding/strumenti/raccogli-instagram.js` in `javascript_tool` e si salva
   l'esito in `~/lavoro/raccolte/<utente>/grezzo/profilo.json`. Per ogni post
   di tipo `p` si apre la sua pagina, si rilancia lo snippet e si salva
   `grezzo/<codice>.json`. I Reel si saltano. Da sloggati la griglia mostra
   solo gli ultimi 12 post.
2. `python3 01-Coding/strumenti/raccogli-instagram.py <utente>` scarica e
   misura le foto e scrive `scheda.md`. Gli URL scadono: si fa subito.
3. **Il vecchio sito**, se c'è: testi, contatti, orari e foto originali
   (Squarespace le dà intere con `?format=original` e l'intestazione
   `Accept: image/png,image/jpeg`). Le foto vanno in
   `~/lavoro/raccolte/<utente>/foto/` e si misurano con `sips` come le altre.
4. Se le foto sopra i 1080 px restano meno di sei, si dichiara quale strada
   si prende: **si chiedono gli originali al cliente**, oppure la direzione
   parte dalla tipografia e dal colore. Mai disegni nostri al posto delle foto
   (Nicola, 31/10: la grafica inventata non è più obbligatoria; 12/10 e 23/10:
   non disegnare niente noi).
5. Quello che manca (prezzi, orari, recensioni, telefono, indirizzo) resta
   scritto come mancante. Non si inventa.

## 2. Le tre tavole di direzione

Una tavola è una pagina HTML statica che mostra **come sarà il sito**, non un
moodboard: il primo schermo composto con le foto vere a 1440 e a 375, la
palette come `token.css` compilato, i due font con il loro campione, l'ordine
delle sezioni prese dal catalogo, la spina dello scroll in tre battute e una
riga su cosa manca.

Le fa **un operatore su Fable** (Nicola, 07/10: la direzione e il design di un
sito vanno su Fable), lo stesso che poi costruirà. Gli si dà:
- la scheda della raccolta e la cartella delle foto;
- `01-Coding/stack/direttive-siti.md`;
- `01-Coding/strumenti/catalogo-sezioni/LEGGIMI.md` e i modelli: Groavel
  (`~/lavoro/groavel-site`, la versione che a Nicola piace), NG Barber,
  Fiftynine, Mikuma giro 7, Davide Milan;
- la catena: `impeccable context`, `reference/new-work.md`,
  `design-taste-frontend`, una sola skill di stile.

Le tre tavole devono essere **diverse davvero**: tre metafore prese dal
mestiere del cliente, non tre palette sulla stessa pagina. Vanno in
`~/lavoro/<nome>-site/direzione/tavola-a.html`, `-b`, `-c`.

Il direttore le cattura in headless, senza aprire finestre:

```bash
node 01-Coding/strumenti/cattura-fette.mjs <url-tavola> 1440 900 0 <cartella> tavola-a-1440
node 01-Coding/strumenti/cattura-fette.mjs <url-tavola> 375 812 1 <cartella> tavola-a-375
```

**Nicola sceglie una tavola**, o chiede di incrociarne due. Senza la sua
scelta non si costruisce. La scelta e le sue parole si scrivono nella nota
progetto.

## 3. La costruzione: una sola testa

Costruisce **lo stesso operatore che ha fatto le tavole**: gli si riscrive con
SendMessage invece di lanciarne uno nuovo, così la direzione e il codice
restano nella stessa testa. Prima di toccare la pagina scrive **il contratto**
in `direzione/contratto.md`: le sezioni in ordine, il loro DOM, i token, le
foto per ogni sezione, cosa si muove allo scroll. Su Groavel il contratto
scritto prima ha tenuto insieme il lavoro (vedi pipeline-siti).

1. `python3 01-Coding/strumenti/nuovo-sito.py <nome>` crea la cartella dallo
   starter.
2. Copia da `01-Coding/strumenti/catalogo-sezioni/` `token.css` e le sezioni
   scelte, e compila i token con i valori della tavola.
3. Carica, in quest'ordine: `direttive-siti.md`, `impeccable context`,
   `reference/craft-floor.md` subito prima della UI, `scrittura-sito` mentre
   scrive i testi, `voce-denkicode` prima di finire.
4. Lo scroll-telling resta obbligatorio (processo-siti, passo 4); i disegni
   inline no.

## 4. I cancelli

```bash
python3 01-Coding/strumenti/cancelli-sito.py ~/lavoro/<nome>-site
```

Lancia controlla-sito, controlla-slop, controlla-testo e il telefono simulato
a 375×812 con la CPU rallentata 4 volte. Se esce 1 il sito torna
all'operatore con l'elenco di quello che blocca. Gli avvisi si leggono uno per
uno e si riportano a Nicola.

## 5. Le catture e il giudizio di Nicola

Catture a pagina intera a 1440 e a 375 con `cattura-fette.mjs`, in headless.
Si mostrano a Nicola insieme agli avvisi dei cancelli. La pagina vera si apre
nel browser dell'app, non in una finestra sul suo Mac.

Poi la riga in `01-Coding/registro-interventi.md` (chi, quando, progetto,
repository, database), la nota progetto con la tavola scelta, commit e push.

## Cosa questa skill non fa

- Non sceglie la direzione al posto di Nicola.
- Non pubblica: i tre sbarramenti restano finché il sito non è del cliente.
- Non usa Apify o altri servizi a pagamento senza chiedere.
