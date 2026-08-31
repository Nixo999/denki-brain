---
type: daily
data: 2026-08-29
updated: 2026-08-29
source: claude
progetti: [denkishift]
---

# 2026-08-29 — La riprogettazione dell'interfaccia di DenkiShift

Richiesta arrivata in sessione: rifare l'interfaccia perché **si venda da sola
in demo**, su due utenti che non sono due gradini dello stesso ruolo. Consegnata
l'architettura delle informazioni, il vocabolario, le impostazioni riscritte e
il design system. Tutto in [[denkishift-interfaccia]].

Metodo: sei letture parallele sul codice vero di `smoothduty` (menu e shell, le
undici impostazioni, la lingua dell'interfaccia, il percorso del dipendente,
quello del responsabile, il contesto commerciale del vault), poi quattro pezzi
di progetto, poi **tre giudici** con l'incarico di smontarli. Hanno smontato,
ed è la parte che vale.

## Cosa è stato deciso — e cosa aspetta una firma

[[2026-08-29-architettura-interfaccia-denkishift]] è decisa a metà.

**Deciso e chiuso**: i nomi delle pagine restano quelli di oggi. Erano state
proposte quattro rinomine — «Chi c'è», «Assenze», «Ore», e un nome che cambiava
col regime per la Disponibilità — ed è stato detto di rimetterli come prima.
Cade con esse la mezz'ora che avrebbe corretto la voce «Disponibilità» sotto il
regime in cui il gesto fa l'opposto: resta un difetto noto, non un lavoro.

**Ancora una proposta**: la voce nuova `Oggi`, e Squadra, Impostazioni e Aziende
che escono dalla barra per andare nella tendina dell'iniziale. Il menu diventa
`Oggi · Turni · Supervisione · Permessi · Prospetto`. Nessuna rotta cambia.
⚠️ La misura che reggeva la barra a cinque voci era tarata sulle etichette
corte: con i nomi di oggi va guardata a 375px prima di scriverla.

## Cosa è emerso guardando il codice, e non lo sapevamo

- ⚠️ **Non esiste nessun posto in cui il responsabile legge se la settimana
  PROSSIMA è pubblicata.** La query ne chiede una sola, quella del lunedì che
  sta guardando. È il buco operativo più caro del prodotto e si chiude con una
  query allargata a cinque lunedì.
- ⚠️ **Le barre verde e rossa della copertura, in scala di grigi, sono lo stesso
  grigio.** Per un uomo su dodici quella schermata non dice niente, e il
  bersaglio sono bar, ristoranti e RSA. È un difetto che esiste già, non una
  cosa da non commettere.
- ⚠️ **Sotto i 640px il menu è fino a sette icone mute**, senza tooltip, e le
  pagine non hanno un titolo: da telefono non c'è un solo elemento testuale che
  dica dove sei. È l'utente di massa del prodotto.
- ⚠️ **La settimana del dipendente non pubblicata mostra sette «Riposo» e «0h in
  settimana»**, e il totale ore conta anche i turni che lui ha rifiutato. Tre
  affermazioni false sulla prima schermata dell'utente più numeroso, e si
  correggono in tre ore.
- **Il conto di chi sta sotto le ore da contratto si accende solo premendo
  Pubblica**, e dopo non è più richiamabile: il numero che evita l'errore in
  busta paga si vede una volta sola.
- **Quaranta punti passano al toast il messaggio grezzo di Postgres.** Davanti a
  un negoziante, in demo, l'app mostra le viscere — e il componente d'errore gli
  chiede di aprire il pannello del database e lanciare dei file SQL.
- **Il motore della generazione automatica è scritto, puro e provato, e non lo
  chiama nessun componente.** È valore già pagato in ore di Nicola.
- **`scripts/dati-di-prova.mjs` esiste** e riempie un'azienda: era dato per
  ignoto in tre analisi su quattro. Crea però «Pizzeria Prova» con sei persone e
  due settimane non pubblicate — cioè non regge una demo.

## Cosa i giudici hanno tolto dal progetto

- Il cookie «secondo ingresso della giornata»: con zero clienti l'unico che apre
  l'app due volte al giorno è Patrick, e gli aprirebbe il tabellone davanti al
  cliente mentre dice «guarda, si apre sulla home».
- L'importazione Excel nello stato vuoto a zero persone: **l'importazione non
  crea nessuno**, abbina solo a chi è già in squadra.
- La demo che apre sulla home nuova: Giulia al telefono promette «chi è libero e
  chi è già sopra le sue ore», e il conto degli straordinari nella prima
  versione non c'è.

## Materiale commerciale

[[obiezione-non-sapranno-usarlo]] — l'obiezione costruita su **Belfort**
(looping sul primo dei 3 Dieci) con l'isolamento di **Blount** in chiusura, il
gesto da fare in demo, le due domande che arrivano subito dopo e il percorso di
otto minuti. ⚠️ Dentro c'è anche un allineamento da fare: il prezzo va detto
come **quota annuale in una ricevuta**, mai «due euro al mese» — e
[[script-denkishift]] oggi dice «due euro al mese».

## Aperto

- ⬜ **Nicola: il sì sulle etichette** → [[2026-08-29-architettura-interfaccia-denkishift]]
- ⬜ **Patrick: il nome a schermo.** L'app dice «Turni» ovunque, il commerciale
  dice DenkiShift. Blocca due pezzi su quattro e costa una risposta
- ⬜ **Il turno rifiutato: resta scoperto o sparisce?** Oggi viene cancellato, e
  il testo delle Impostazioni non si può scrivere finché non è deciso
- ⬜ **La migrazione `19`**, ancora non eseguita da nessuna parte: senza, le
  Impostazioni non si salvano. La password del database di sviluppo sul Mac non
  funziona dal 28 agosto
- ⬜ Le cose di ieri restano tutte: chiamare la lista, estenderla a 130-150,
  provare lo script su 40 chiamate, l'SMTP proprio

## Non verificato

- **Niente è stato visto a schermo.** Nessuna delle schermate progettate è stata
  aperta, né su desktop né su telefono: il vincolo era sola lettura. Le tre
  misure su cui poggiano due pezzi interi — le cinque etichette a 375px, i
  cinque elementi sopra la piega a 1280×800, la barra in basso che non collide
  con quella della Disponibilità — sono dedotte dalle classi
- Il file dei token del design system è scritto ma **non compilato**: non c'è la
  prova che passi il build su questa versione di Tailwind
- Le stime in ore sono di Claude e non sono state riscontrate da Nicola
- La skill di design consultata è installata a metà sulla macchina (manca la
  base dati): palette e tipografia vengono dal ragionamento sul codice vero e da
  un calcolo del contrasto, non da un riscontro

## Collegamenti

[[denkishift]] · [[denkishift-interfaccia]] · [[obiezione-non-sapranno-usarlo]] ·
[[2026-08-29-architettura-interfaccia-denkishift]] · [[core-commerciale]]
