---
type: area
updated: 2026-09-03
source: claude
prodotto: siti-vetrina
canale: instagram
stato: in-prova
---

# Il DM di Instagram — un messaggio solo, sei ganci

> [!note] Nota generata da Claude — 2026-08-31
> Da provare su **200 invii**. Deciso in [[2026-08-31-canale-dm-instagram]].

> [!tip] Lo strumento: [banco-dm.html](../strumenti/banco-dm.html)
> Si apre con doppio click, e per ogni riga prepara la **versione C** col gancio
> della colonna, copia il testo e apre la conversazione. Segna la data, riconosce i recuperi dopo 4 giorni
> lavorativi e restituisce il CSV aggiornato. **Non manda niente**: l'invio
> resta un gesto di Patrick, ed e` la riga che separa un aiuto da un account
> bloccato — vedi [[2026-09-02-automazione-dm-instagram]].

**Lo manda Patrick, dal suo account personale.** Non Giulia, non un account
aziendale: i mille follower e la faccia sono metà del messaggio.

**Framework** (regola 12 di `CLAUDE.md`): apertura e gancio = **Gitomer** — il
gancio non è «facciamo siti», è la falla precisa che ho trovato guardando.
Corpo = **Hormozi**, equazione del valore: risultato alto (le sue foto già
online), sforzo zero (non deve produrre niente), rischio zero (garanzia su ciò
che controlliamo). Chiusura = **Blount**, la richiesta più piccola possibile —
non un appuntamento, il **permesso di mandare la bozza**. Recupero = **Voss**,
domanda orientata al «No».

---

## Versione A — quella mandata davvero il 31 agosto 2026

> [!note] Testo di Patrick — `source: denkicode`
> È il messaggio uscito sul primo giro dell'anello 1. **Non si riscrive: si
> misura.** Il metro con cui confrontarla è la **versione C**, in fondo:
> la B, che stava in mezzo, non è mai uscita.

> Buongiorno, sono Patrick Sappa, ho una piccola azienda di software a Seveso,
> DenkiCode.
>
> Le scrivo perché ho guardato il profilo e il mio team le ha già preparato una
> bozza di sito.
>
> Se mi dà l'ok gliela giro qua su Instagram, la guarda, e se non le piace me
> lo dice e non ci sentiamo più.
>
> Sul costo non le faccio girare la testa: si parla di un paio di centinaia di
> euro, non di migliaia, più una quota annuale per tenerlo online. Il numero
> preciso glielo riesco a fare dopo aver visto il lavoro e dopo aver ascoltato
> le sue richieste e solo se la cosa le interessa davvero.
>
> Gliela mando?

### Cosa cambia rispetto alla B, e cosa costa

Tre differenze, in ordine di peso.

1. **Il gancio non c'è.** «Ho guardato il profilo» senza dire *cosa* ho visto è
   la frase che scrive anche chi non ha guardato niente. È esattamente il
   contrario di Gitomer ([[core-commerciale]]): il gancio non è «facciamo
   siti», è la falla precisa. Costo diretto: la verifica di
   [[2026-08-31-instagram-anello-1]] — tre domini senza DNS, una pagina cPanel,
   uno Shopify chiuso, un link rimasto su `TUONUMERO` — **non entra nel
   messaggio**, quindi non lavora.
2. **«Già preparata» invece di «gliela preparo».** È l'esca storica di casa
   ([[prodotti-e-listino]], flusso A), quindi è coerente col vault. Ma sposta
   il messaggio da una promessa a un'affermazione, e **mette un orologio
   addosso a Patrick**: chi risponde «mandamela» si aspetta un file, non due
   giorni di attesa. Vedi *La promessa che va mantenuta*, sotto.
3. **«Il mio team» in un messaggio che apre con «una piccola azienda».** Le due
   cose si contraddicono di mezza riga. Il team è Nicola.

**Il verso in cui potrebbe andare meglio della B, e va detto:** più vago e più
generoso significa quasi sempre **più risposte**, non meno — «mandamela» costa
zero a chi legge. Il rischio non è il tasso di risposta, è la **qualità**: chi
risponde per curiosità non è chi compra, e ognuno di quei sì è una bozza da
produrre. Il numero da guardare quindi **non è «quante risposte»**, è
**«quanti sì alla bozza si trasformano in una trattativa»**.

---

## Versione B — con il gancio, mai uscita

> [!info] Superata dalla versione C il 3 settembre 2026 — [[2026-09-03-bozza-gia-fatta]]
> Non è mai stata mandata: la lista del 2 settembre è rimasta ferma. Resta qui
> perché è il passaggio in cui è nato il gancio, e perché il corpo della C è il
> suo, con una promessa in più.

Una sola cosa cambia da un invio all'altro: **la riga del gancio**, scelta fra
le sei della tabella sotto in base a quello che è stato verificato in lista.

> Buongiorno, sono Patrick Sappa — ho una piccola software house a Seveso,
> DenkiCode.
>
> Le scrivo perché ho guardato il profilo di **[NOME ATTIVITÀ]** e
> **[GANCIO]**.
>
> Le foto che pubblica sono già metà del lavoro: con quelle le preparo la
> prima schermata di come sarebbe il vostro sito e gliela mando qui. Gratis e
> senza impegno — la guarda, e se non le piace me lo dice e non ci sentiamo
> più.
>
> Sul costo non le faccio girare la testa: si parla di poche centinaia di euro
> una volta, non di migliaia, più una quota annuale per tenerlo online. Il
> numero preciso glielo faccio solo se la cosa le interessa davvero.
>
> Gliela preparo?

### I sei ganci

Si copiano così come sono. Quello giusto è già scritto nella colonna
`Gancio` della lista.

| # | Quando | Riga da incollare |
|---|---|---|
| **1** | Nessun sito | «su Google non trovo un vostro sito: c'è Instagram, ci sono le schede degli altri, ma un sito vostro no» |
| **2** | Dominio morto | «il dominio **[X]** che compare ancora nelle ricerche non si apre più» |
| **3** | Parcheggiato / senza https | «**[X]** non apre il vostro sito: risponde con la pagina di default del server» |
| **4** | Link in bio rotto | «il link che avete in bio non porta più da nessuna parte» |
| **5** | Su piattaforma | «quello che avete non è un sito vostro: è una pagina su [Wix / Jimdo / Google], e si vede dall'indirizzo» |
| **6** | Vivo ma vecchio | «il vostro sito c'è, ma è fermo al **[ANNO]**» |

### Perché è scritto così

- **Il gancio è al secondo rigo, non al primo.** Il primo rigo dice chi sono e
  da dove vengo: senza quello, la frase sul sito suona come l'apertura di un
  truffatore. Con quello, suona come uno che ha guardato.
- **Il gancio è un fatto, mai un giudizio.** «Il dominio non si apre» è
  verificabile e non offende nessuno. «Il vostro sito è brutto» chiude la
  conversazione e se lo sono pagato loro.
- **Non si chiede un appuntamento.** Si chiede il permesso di **dare** una
  cosa: è la richiesta più piccola che esista, e sposta il frame da «mi sta
  vendendo» a «mi sta regalando». È il *permesso di mandare la demo* che
  Patrick ha già fissato per i cold caller il 30 agosto
  ([[briefing-prodotti-gabriele-edoardo]]).
- **Il prezzo si fa capire senza dirlo.** «Poche centinaia, non migliaia» toglie
  di mezzo la paura vera — che sia un preventivo da agenzia — senza inchiodare
  una cifra che poi Patrick deve difendere. Il numero preciso è suo, dopo.
- **La garanzia è solo su ciò che controlliamo**: la bozza è gratis e non
  obbliga a niente. Nessuna promessa di risultato, nessuna data
  ([[core-crescita-finanze]]).
- **Si dà del «Lei».** Primo contatto, e vale [[stile-comunicazione]]: il
  passaggio al «tu» lo chiede Patrick in apertura di meeting, non prima.

---

## Versione C — la bozza è già fatta · **è questa che parte**

> [!note] Decisa da Nicola il 3 settembre 2026 — [[2026-09-03-bozza-gia-fatta]]
> Prende il gancio verificato della B e ci rimette sopra l'esca storica di casa
> ([[prodotti-e-listino]], flusso A): **la bozza non si propone, si annuncia
> già pronta.** È l'unica leva su cui siamo forti, e agisce su tre termini su
> quattro dell'equazione del valore ([[core-crescita-finanze]]).

> Buongiorno, sono Patrick Sappa — ho una piccola software house a Seveso,
> DenkiCode.
>
> Le scrivo perché ho guardato il profilo di **[NOME ATTIVITÀ]** e
> **[GANCIO]**.
>
> Le sue foto erano già metà del lavoro: l'altra metà l'ho fatta io. La bozza
> del suo sito è già pronta, con le sue immagini e il suo nome — non deve
> scrivere testi, non deve mandarmi materiale, non deve decidere niente.
>
> Gliela mando qui, la guarda con calma, e se non le piace me lo dice e non ci
> sentiamo più. Non le costa un euro e non la impegna a niente.
>
> Sul costo non le faccio girare la testa: se poi decidesse di metterlo online,
> si parla di poche centinaia di euro una volta — non di migliaia — più una
> quota annuale per tenerlo attivo. Il numero preciso glielo faccio solo se la
> cosa le interessa davvero.
>
> Gliela mando?

### I sei ganci, al «Lei»

Si copiano così come sono. Quello giusto è già scritto nella colonna `Gancio`
della lista, e nelle liste pubblicate sul banco è **già dentro il messaggio**.

| # | Quando | Riga da incollare |
|---|---|---|
| **1** | Nessun sito | «su Google non trovo un suo sito: c'è Instagram, ci sono le schede degli altri, ma un sito suo no» |
| **2** | Dominio morto | «il dominio **[X]**, che compare ancora nelle ricerche, non si apre più» |
| **3** | Parcheggiato / senza https | «**[X]** non apre il suo sito: risponde con la pagina di default del server» |
| **4** | Link rotto | «il link al sito che risulta ancora online non porta più da nessuna parte» |
| **5** | Su piattaforma | «quello che ha non è un sito suo: è una pagina su **[X]**» |
| **6** | Vivo ma vecchio | «il suo sito c'è, ma è fermo al **[ANNO]**» |

I ganci **4** e **5** sono cambiati anche nella sostanza, non solo nel
pronome: il 4 non nomina più la bio, che dalle nostre macchine non si legge, e
il 5 non promette più che «si vede dall'indirizzo», che è falso quando la
piattaforma sta sotto un dominio proprio. Il perché è in
[[2026-09-03-bozza-gia-fatta]].

### Cosa cambia rispetto alla B, riga per riga

1. **«L'altra metà l'ho fatta io.»** Spiega in cinque parole perché uno
   sconosciuto ha già lavorato per lei senza chiedere niente: è la frase che
   toglie l'aria da truffa alla promessa.
2. **I tre «non deve»** sono lo *sforzo* dell'equazione del valore portato a
   zero, detto in modo che si senta: non testi, non materiale, non decisioni.
3. **La garanzia è scritta.** «Non le costa un euro e non la impegna a niente»
   non aggiunge niente a quello che facevamo: aggiunge che adesso lo diciamo, e
   una garanzia non detta non vale (Hormozi).
4. **«Gliela mando?»** al posto di «Gliela preparo?». La richiesta più piccola
   che esista (Blount): non chiede lavoro a nessuno, chiede il permesso di
   consegnare.
5. **Il prezzo è al condizionale** — «se poi decidesse di metterlo online» —
   così la cifra resta lontana dalla bozza, che è gratis.

⚠️ **Il prezzo di questa versione è l'orologio**: chi risponde si aspetta un
file. Vale in pieno *La promessa che va mantenuta*, qui sotto, e il tetto delle
5 bozze aperte non è più un consiglio.

---

## Il recupero, uno solo

Dopo **4 giorni lavorativi**, nella stessa conversazione, se non ha risposto:

> Le scrivo una volta sola e poi la lascio in pace: ha lasciato perdere l'idea
> di avere un sito suo?
>
> Se è «adesso no» va benissimo, me lo scriva in due parole. Se invece la
> bozza la vuole ancora vedere, gliela mando oggi.

**Perché.** «Avete lasciato perdere?» si risponde *no* per coerenza con se
stessi, e quel *no* riapre la conversazione (Voss). «Ha visto il mio
messaggio?» fa l'opposto: mette in imbarazzo chi non l'ha letto, e chi è in
imbarazzo non risponde.

**Dopo il secondo messaggio non se ne mandano altri.** Si segna
`Nessuna risposta` e l'account non si ricontatta per sei mesi.

---

## Le quattro risposte che tornano

| Rispondono | Si risponde |
|---|---|
| **«Sì, mandamela»** | «Perfetto. Me la dia un paio di giorni e gliela mando qui. Intanto: c'è qualcosa che vuole assolutamente dentro — listino, prenotazioni, un servizio in particolare?» → e **la bozza si consegna** |
| **«Quanto costa?»** | «Duecento-trecento euro una volta, più circa centoventi all'anno per tenerlo online e per l'assistenza. Il numero preciso dipende da cosa ci mettiamo dentro: prima le faccio vedere la bozza, poi ne parliamo.» |
| **«Chi siete? Non vi conosco»** | «Giusto, ho scritto io a lei. DenkiCode, siamo a Seveso, io e il mio socio Nicola che sviluppa. Qui c'è quello che abbiamo fatto: denkicode.com — ci guardi con calma.» *(unico messaggio in cui entra un link)* |
| **«Ce l'abbiamo già / ci pensa un altro»** | «Meglio così. Allora le faccio una domanda sola e poi la saluto: quando ha chiesto l'ultima modifica, in quanto gliel'hanno fatta?» |

---

## Quello che non si scrive mai

| Mai | Perché |
|---|---|
| **Un link nel primo messaggio** | È il segnale di spam più forte che esista: il messaggio finisce nel filtro e l'account si espone al blocco |
| **Una data di consegna** | Nel primo contatto non si promettono tempi. Nemmeno «in una settimana» |
| **«abbonamento», «contratto», «fattura»** | [[vincoli-fiscali]] — si dice **quota annuale** e **ricevuta** |
| **Un prezzo secco** | Nel DM si fa capire l'ordine di grandezza. La cifra la fa Patrick in trattativa |
| **«Il vostro sito è brutto / vecchio / da rifare»** | Se l'è pagato lui. Si dice il fatto — l'anno, il dominio che non apre — e si sta zitti |
| **Lo stesso messaggio a chi è già in una lista telefonica** | Un'attività riceve un canale solo → [[2026-08-31-stop-porta-a-porta-a-freddo]] |

---

## La promessa che va mantenuta

Chi dice sì riceve la bozza. **Non più di 5 bozze aperte per volta**: se ne
arrivano di più, si risponde subito con un giorno («gliela mando giovedì»), non
si lascia cadere.

⚠️ **Con la versione A e con la C l'orologio parte più stretto**, perché
entrambe dicono che la bozza c'è già: chi risponde «mandamela» si aspetta un
file, non due giorni di attesa. Se la coda supera le 5, la frase che tiene in
piedi la promessa senza smentirla è una sola, e va detta nella stessa giornata:

> «Gliela sto rifinendo con le sue foto — gliela mando [giorno]. Intanto:
> c'è qualcosa che vuole assolutamente dentro?»

Una bozza promessa e non consegnata brucia il canale più lentamente di un
blocco di Instagram, ma lo brucia meglio.

**La bozza si consegna come link, non come screenshot.** Va pubblicata su
Netlify: è la regola di casa per tutte le bozze → [[netlify]]. Una bozza che
sta sul Desktop non è consegnata.

> [!warning] Da fare prima del primo giro — 2026-08-31
> A *«fammi vedere un esempio»* serve una risposta pronta, e l'esempio giusto
> è [[castiglione-furniture]]: nato il 30 agosto proprio dalle foto di un
> profilo Instagram. Il repo è ancora in locale e senza remote
> ([[2026-08-30-sito-castiglione]]) — **pubblicarlo su Netlify è il primo
> passo della campagna**, non un lavoro a parte.

## Il test — come si chiude la questione senza discutere

Le due versioni non si valutano a opinione: si mandano e si contano, come i
quattro [[pattern-interrupt]].

| Giro | Versione | Inviati | Risposte | Sì alla bozza | Trattative aperte |
|---|---|---|---|---|---|
| 1 — 31 ago 2026, anello 1 | **A** (senza gancio, bozza già fatta) | `TODO` | | | |
| 2 — mai partito | **B** (con gancio, bozza da fare) | — | — | — | — |
| 3 — 3 set 2026, bellezza + tattoo | **C** (gancio + bozza già fatta) | **75** | `TODO` | `TODO` | `TODO` |

⚠️ **Settantacinque in un giorno solo, contro un tetto di trenta.** Il giro 3
è uscito tutto la sera del 3 settembre — 33 righe di bellezza e 42 di tatuatori
([[2026-09-03-instagram-anello-1-2]]) — cioè oltre il doppio della soglia di
blocco di Instagram. Se le risposte di questo giro dovessero arrivare basse, il
numero **non si legge come un verdetto sul testo**: si legge insieme a questa
riga, perché un account rallentato consegna peggio. Il confronto pulito, se
serve, si rifà su un giro dentro la rampa.

**Nessuno dei 75 testi è stato corretto a mano nel banco.** Quello che è
uscito è esattamente la versione C qui sopra: su questo il giro misura bene.

⚠️ **Il confronto A contro B non si potrà più fare**: la B non è mai uscita e
la C la sostituisce. Quello che si misura da qui in avanti è **A contro C**,
cioè il solo gancio — stessa promessa, stessa chiusura, e in mezzo un fatto
verificato invece di «ho guardato il profilo».

**Regola del test**: stesso segmento, stesso anello, stessa fascia oraria.
Se cambia anche il target, il confronto non vale niente.

Le tre domande al secondo giro, le stesse di [[script-denkishift]]:

1. **Quanti rispondono?** Sotto il 5% il messaggio non tiene, qualunque sia la
   versione.
2. **Quanti dei sì alla bozza arrivano a parlare di prezzo?** È il numero che
   dice se le risposte sono curiosità o clienti.
3. **Quale gancio ha risposto meglio?** Sei varianti: se una regge e cinque no,
   le liste future si costruiscono su quel segnale.

## Collegamenti

[[metodo-instagram]] · [[2026-09-03-bozza-gia-fatta]] ·
[[2026-09-03-instagram-anello-1-2]] · [[2026-08-31-instagram-anello-1]] ·
[[2026-08-31-canale-dm-instagram]] · [[core-commerciale]] ·
[[core-crescita-finanze]] · [[stile-comunicazione]] · [[vincoli-fiscali]] ·
[[prodotti-e-listino]] · [[flusso-vendita]] · [[sito-denkicode]] · [[metriche]] ·
[[netlify]]
