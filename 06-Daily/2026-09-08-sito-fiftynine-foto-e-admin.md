---
type: daily
data: 2026-09-08
source: claude
tags: [daily, sito-fiftynine, frontend, admin]
---

# 8 settembre 2026 — le foto del bar, e il lunedì che chiude alle 19:30

Nicola ha portato una chiavetta («NO NAME») con il materiale del proprietario
del [[sito-fiftynine]] e ha chiesto due cose: **usare quelle foto al posto di
quelle prese da Instagram**, e **una pagina da cui il proprietario possa
cambiarsi foto e menù da solo**.

## Quello che c'era davvero sulla chiavetta

Non foto dei piatti: **le locandine esposte nel locale**. Dodici immagini, tutte
da 1024 px in su, contro i 640 px degli screenshot di Instagram. Sono la fonte
migliore che il progetto abbia avuto finora, e una di loro ha corretto il sito.

- **La locandina degli orari ha chiuso un buco dichiarato.** Nella nota di
  progetto il giorno di chiusura risultava ignoto e il sito prometteva
  «5:30–21:30» e basta. La locandina dice **lunedì 5:50–19:30, martedì–sabato
  5:30–21:30, domenica 7:00–21:30, nessun giorno di chiusura**. Cioè: il sito
  diceva **aperto un lunedì alle otto di sera**. Adesso `ORARI` è una tabella
  per giorno della settimana e la linea del giorno riscrive le ore agli estremi.
- **La lista cocktail passa dai due pannelli veri** al posto della foto a 640 px.
- **Otto locandine di menù del giorno** — pranzo 12 €, primo 9 €, speciale
  12/13 €, pizza 8/9 €, insalata da 8 €, insalata con pollo 10 €, maxi toast
  4,50 €, crea il tuo piatto — sono contenuto che il sito **non aveva**: ne è
  uscito il capitolo `#offerte`.
- **Un trittico di paste, chiaramente stock, l'ho scartato.** Su un locale vero
  una foto stock toglie credibilità invece di darne.
- **Colazione, frittini e gyoza restano di Instagram**: per quelle sezioni sulla
  chiavetta non c'era niente. Vanno chieste al proprietario, non inventate.

## La pagina di modifica: lo store è l'HTML, non un JSON

Su V-BAG lo store è `dati/borse.json` e la pagina lo rende in JS. Qui non
andava bene: **il menù è il contenuto principale**, e con un JSON senza JS
sarebbe una pagina vuota. Quindi lo store sono `index.html` e `menu.html`
stessi — ogni pezzo modificabile sta fra due commenti, si legge con `DOMParser`
e **si riscrive solo quello che sta fra i due**.

Il resto è lo schema di V-BAG, che regge: File System Access API dove c'è,
download dove non c'è, foto rimpicciolita in canvas, niente login perché da lì
non si scrive sul server.

**`prova-admin.html`**, 23 asserzioni: la più importante è che leggere e
riscrivere i listini senza cambiarli lasci i file **identici al byte**. È stata
utile subito — scappare l'apice dritto nel testo riscriveva quarantaquattro
righe di pizze per un prezzo cambiato, e il diff non diceva più niente. Due
funzioni invece di una: nel testo si chiudono solo `& < >`, nell'attributo
anche `"` e `'`.

## Trappole nuove → [[trappole]]

- **`sips` legge le dimensioni trasposte** quando il browser ruota la foto: su
  una locandina dava 733×1100 e il browser mostrava 1100×733, cioè coricata,
  con `sips -g orientation` che rispondeva `<nil>`. L'orientamento si verifica
  nel browser con `naturalWidth`/`naturalHeight`.
- **`sips` non scrive webp**: fallisce in silenzio.
- **Una voce in più in nav non si misura a 1440 e 375**, lì è sempre a posto:
  la quinta voce sforava di 36 px fra 761 e 899.
- **Un mosaico con la prima cella a tutta larghezza lascia un buco** quando le
  celle scendono a due.

## Verificato, e non verificato

✅ Zero overflow a 375, 761, 820, 899, 900, 980, 1280, 1440. 17 immagini su 17
caricate. Console pulita con la motion accesa. 44 pizze intatte dopo i
marcatori. Le tre righe degli orari e i due footer corretti. La mappa dei giorni
(`Sun`→0) controllata contro `getDay()` su sette giorni di fila. `prova-admin`
23 su 23. La pagina di modifica legge 8 foto, 8 locandine, 9 listini.

⬜ **Il ramo `showDirectoryPicker` non è mai stato eseguito**: nel pannello
parte sempre il fallback. Va provato a mano su Chrome da computer.
⬜ **Il lunedì e la domenica non sono stati visti a schermo**: la tabella è
letta con l'indice giusto, ma il render di quei due giorni non è stato forzato.
⬜ Safari su iPhone mai provato.
⬜ **Non pushato**: il commit `8324cd8` è locale. `bartabaccheria59` è pubblico
e il push scrive anche su `fiftynine-site` — aspetta l'ok di Nicola.

## Lista del giorno — 68 locali dell'anello 1

Patrick ha chiesto un settore ad alta conversione. Il fitness ticinese è caduto
subito: dodici su quindici avevano già il sito. Scartati anche detailing,
giardinieri, pet, wedding e B&B. **Il Sotto Ceneri è esaurito**: le due riserve
grosse le abbiamo prese ieri.

Quindi zona nuova, canale uguale: **anello 1, ristorazione** — 68 righe fra
Como (25), Varese (24) e Lecco (19). Il banco passa a 315 righe, 238 da
mandare. La resa lombarda conferma il motivo del cambio: **64 righe su 68 non
hanno nessun sito**, contro 52 su 60 in Ticino. Dettaglio in
[[2026-09-08-anello1-ristorazione]].

Da qui in poi il collo di bottiglia non è più la lista: a 65 DM al giorno, sul
banco ci sono quattro giorni di lavoro già pronti.

## Sera — venti su settantadue avevano il sito

Nicola: «su 72 almeno 20 avevano già il sito, perché non controlli?». Ha
ragione, e il motivo è nel CSV: **62 righe su 68 con la stessa frase di
verifica**. Non era una ricerca riga per riga, era un modello. Le contromisure
sono tre e stanno tutte nel repo, non in una promessa:

- **Il banco tiene i contattati in un elenco a parte** — sezione «Contattati»
  in fondo, ultimi in cima, col conto in testata — e ogni «Segna inviato» va
  al server nuovo (`banco-server.py`, al posto di `http.server`), che scrive
  `02-Sales/liste/contattati.csv` e **committa e pusha da solo** due minuti
  dopo l'ultimo gesto. Seme: i 75 del 3 settembre. Scheda: [[contattati]].
- **Tasto «Ha già il sito»** su ogni riga da mandare: la riga esce dal banco e
  finisce in `gia-col-sito.csv`, che è il numero con cui si misura chi fa le
  liste. Cioè me.
- **`controlla-lista.py`** prima di pubblicare: frase ripetuta più di tre
  volte o handle già scritto, e la lista non passa. Sulla lista di oggi
  segnala subito le 62 righe.

✅ Provato sul server locale: segna → riga nel CSV e nell'elenco, annulla →
riga tolta, «ha già il sito» → riga in `gia-col-sito.csv`, file sconosciuto →
400, doppione → una riga sola. Cambiando account l'elenco resta quello giusto.
✅ Commit automatico visto partire alla chiusura del server (SIGTERM). Il
`git pull --rebase` però si è rifiutato per le modifiche non committate nel
vault, e senza pull niente push: aggiunto `--autostash`. ⬜ Il push dal server
non è ancora stato visto arrivare su GitHub. ⬜ **Sul Mac di Patrick serve un `git pull`**
prima del prossimo banco, o `Banco DM.command` lancia un file che non ha.
⬜ I 20 di oggi non si sanno quali sono: Patrick li marca dal banco.

## Notte — la firma è dentro dieci siti

Patrick aveva provato dal suo Mac e non poteva: i repo dei siti là non ci sono.
Nicola l'ha chiesto come «powered by opero», ma la decisione del pomeriggio
dice **DenkiCode**, e OperO è escluso apposta — applicata quella. Dieci repo
firmati e nove pushati (Netlify pubblica da solo); `bartabaccheria59` resta a
due commit locali perché il push scrive anche su `fiftynine-site` e aspettava
già l'ok di Nicola.

Misurato, non guardato — 13 pagine, 1440 e 375: contrasto fra 5,56 e 14,97,
simbolo 150×150 reso 18×18 ovunque, riga propria sotto i recapiti, zero
overflow salvo i 76 px preesistenti di Drop Out. Due cose trovate solo perché
misurate: su Atelier Selva `.firma` era già la scritta a mano di Shari (lì la
classe è `.powered`), e sui footer flex il link occupava 1.296 px cliccabili
(ora sta in un `<p>`). Dettaglio nel [[registro-interventi]], trappole in
[[trappole]].

Poi Nicola: «ma Bellastoria, albybike?». Cercati fra i 25 repo di `Nixo999`
per `<title>`: **albybike è `vibrant-web-foundation`** (chiude il `TODO` della
nota), Bellastoria è `bellastoria_sito`. Firmati e pushati anche quei due.

⬜ Fuori: **Groavel** (nessun repo su `Nixo999`), [[sito-castiglione]] (PC di
Nicola), [[denkishift]] (app, non sito), [[opero]] (escluso). ⬜ Da vedere se
albybike.com e bellastoria.netlify.app si aggiornano dal push.

## Notte — il passo 3 non lo fa più il modello

Nicola, dopo: «aggiorna il metodo con cui cerchi, non deve succedere che
Patrick scrive a gente che ha già il sito». Il metodo diceva già «verificato,
mai dedotto» e non è bastato: una regola scritta cede sotto 68 righe. Quindi
il passo 3 di [[metodo-instagram]] diventa uno script, `verifica-sito.py`:

- **indovina i domini dal nome** e li apre. Certo se titolo e comune tornano,
  probabile se torna solo il nome. Non dipende da nessun motore: sempre acceso;
- **i motori senza chiave non reggono**: DuckDuckGo 403 dopo ~50 richieste,
  Brave 429 dopo ~10, Bing ignora le virgolette. Restano un extra;
- `controlla-lista.py` pretende la prova a mano (`cercato «…» → …`) **e** quella
  dello script, e non passa finché resta un `PROBABILE SITO`.

**Sulla lista di oggi**: 7 siti certi trovati dallo script, 24 probabili aperti
a mano, 8 veri. **13 su 68 tolti dal banco**, Esito DM propagato su
`lista-corrente.csv`: 225 da mandare invece di 238. I 20 di Patrick non sono
tutti qui: quelli col sito solo nel link in bio da qui non si vedono, e restano
al tasto «Ha già il sito».

⚠️ Trovato guardando `avvio()`: **ogni pubblicazione resetta la memoria del
banco** — se il testo di `lista-corrente.csv` cambia, la pagina ricarica il
file e perde gli invii del giorno non ancora scaricati. Da stasera gli invii
stanno anche in `contattati.csv`, quindi il danno è il conto a video, non la
storia. Da sistemare: ricaricare unendo per handle, non sostituendo.

## Collegamenti

[[sito-fiftynine]] · [[contattati]] · [[metodo-instagram]] · [[trappole]] · [[registro-interventi]] · [[sito-vbag]] ·
[[netlify]] · [[processo-siti]]
