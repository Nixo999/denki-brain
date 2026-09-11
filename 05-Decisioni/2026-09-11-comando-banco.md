---
riga: /banco apre il banco DM e costruisce le tre liste del giorno; cinque pagine, annulla l'ultimo, e per i siti la bozza si annuncia gia' fatta.
type: decisione
data: 2026-09-11
progetto: azienda
source: denkicode
tags: [banco-dm, dm-instagram, generazione-lead, liste, ricerca-di-mercato, comandi]
---

# Il comando `/banco`, le tre liste al giorno e l'annulla

**Chiesto da Patrick l'11 settembre 2026**, in cinque punti:

> «crea comando /banco che permetta di aprire banco dm per fare ciò che abbiamo
> già detto ma aggiungi e migliora queste cose: 1 un pulsante per annullare
> l'ultimo, per esempio a volte mi succede che per sbaglio chiudo la chat prima
> di premere invio e perdo l'ig […] 2 voglio che lanciando il comando tu crei
> una lista da 50 contatti per i siti, una lista da 50 contatti per denkishift
> e una lista da 30 contatti per la ricerca di mercato […] mi raccomando gli
> script e i ganci devono essere inerenti alla tipologia di servizio per cui li
> contattiamo e anche le aziende devono essere ad alta conversione in base al
> servizio che stiamo offrendo. 3 aggiungi la divisione in pagine […] 4 per i
> siti il gancio deve essere che la bozza è già stata fatta. 5 migliora
> l'estetica e l'usabilità di banco dm in generale»

## Cosa si è deciso

**1. Un comando solo, con due velocità.** `/banco` apre il banco. Se le liste
di oggi ci sono già, costa un minuto; se non ci sono, le costruisce, le
verifica, le pubblica e poi apre. `/banco apri` salta sempre la costruzione,
`/banco siti` ne rifà una sola. Il comando sta in `.claude/commands/banco.md` e
arriva sulle macchine con `installa-macchina.py`.

**2. Tre liste al giorno, e sono tre mestieri diversi**: 50 siti, 50
DenkiShift, 30 ricerca di mercato. Supera le due liste (50 + 30) di
[[2026-09-10-liste-50-30-messaggi-personalizzati]], che resta valida su tutto
il resto. Ogni lista ha il suo target ad alta resa, il suo gancio e il suo
testo, e il comando li scrive per esteso: le onicotecniche e le estetiste
singole per i siti, le squadre a turni da 8 a 50 persone per DenkiShift, le
aziende strutturate (officine, impiantisti, logistica, ingrossi) per la
ricerca.

**3. La ricerca di mercato diventa un canale DM**, non solo telefonico:
[[dm-instagram-ricerca]]. Il modulo è quello di [[script-indagine]] — sei
domande, anonimo, meno di due minuti. Due delle sei chiedono **com'è messo il
sito** e **dove servirebbe un programma**: chi risponde si qualifica da solo, e
le risposte tornano indietro come lead per le altre due liste. Qui non si vende
niente, e non è un modo di dire.
⚠️ Il link che Patrick ha passato finisce in `/edit`: è il pannello di chi il
modulo lo scrive. Ai lead va quello con `/viewform`, che è lo stesso modulo già
in [[script-indagine]] — verificato aprendolo l'11/09/2026.

**4. Per i siti la bozza si annuncia fatta.** Regola sua, scritta verbatim in
[[stile-comunicazione]]. Torna alla versione C di [[dm-instagram-vetrina]] e
supera la promessa più prudente («le preparo una prima schermata») introdotta
il 10 settembre. **Le 50 righe siti già pubblicate sono state riscritte**: solo
la frase della promessa e la domanda finale, il resto di ogni messaggio è
rimasto quello scritto su quel profilo. Passate da `voce-check.py`, zero tell
su 50.
⚠️ Il prezzo del gancio è che **la bozza deve esistere quando rispondono**. Chi
manda questi cinquanta si compra il lavoro di farle.

**5. Il banco diventa a cinque pagine** — Siti, DenkiShift, Ricerca, Da
ricontattare, Già contattati — e impara tre cose nuove:

- **`↩ Annulla l'ultimo`** (o ⌘Z): rimette in cima alla sua pagina l'ultimo
  profilo segnato e toglie la riga da `contattati.csv`. Nasce dal guasto che
  Patrick ha descritto: chiude la chat prima di premere invio e l'handle è
  perso. La pila dei gesti vive nel `localStorage`, quindi sopravvive alla
  ricarica, e vale anche per lo scarto «ha già il sito» e per i recuperi.
- **`Recupero (data)`**, colonna nuova: quando il secondo messaggio parte, la
  riga esce dai recuperi invece di restarci per sempre. Prima non usciva, e i
  75 recuperi maturi erano destinati a essere riscritti due volte.
- **Ricerca** ha tre tasti invece di uno: col link, senza il link, solo il
  link. Un link nel primo DM è la cosa che fa limitare un account, e la scelta
  resta di Patrick messaggio per messaggio.

## Cosa non è stato fatto

⬜ **Le tre liste di oggi non esistono ancora.** Il comando le costruisce
quando lo si lancia, e costano circa due minuti a riga: 130 righe sono più di
quattro ore di lavoro vero. Sul banco restano le 322 righe già pubblicate.

⬜ La resa delle tre liste non è misurata: DenkiShift sale da 30 a 50 righe e
la ricerca parte da zero. I numeri si scrivono nelle note delle liste.

## Collegamenti

[[2026-09-10-liste-50-30-messaggi-personalizzati]] · [[metodo-instagram]] ·
[[metodo-liste]] · [[dm-instagram-vetrina]] · [[dm-instagram-denkishift]] ·
[[dm-instagram-ricerca]] · [[script-indagine]] · [[stile-comunicazione]] ·
[[generazione-lead]] · [[registro-interventi]]
