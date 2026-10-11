---
riga: Il banco DM esce dal Mac di Patrick e va online su Netlify - stato in Blobs, login, giro ogni 30 minuti che riporta contattati.csv nel vault.
type: decisione
data: 2026-10-11
progetto: banco-dm
updated: 2026-10-11
source: claude
stato: presa
tags: [banco, liste, netlify, outreach]
---

# Il banco DM sta online, e il vault resta la fonte delle liste

## Il contesto

Nicola, 11 ottobre 2026: il banco «sta dando un sacco di problemi», Patrick si
vede chiedere il permesso per i comandi JavaScript «molte volte» a ogni lista,
e il banco serve anche per gli accordi con Bolanos (messaggi e mail ad agenzie).
Va «reso più facilmente accessibile, magari mettendolo online». Poi: «deve
funzionare esattamente come quella di adesso … basta che poi sia ad accesso
online e sia il più comodo possibile».

Perché il banco locale si rompeva, letto sul codice:

- lo stato stava in tre posti che non si parlano: il localStorage del browser
  di Patrick, `lista-corrente.csv` (2,1 MB in git) e `contattati.csv`, scritto
  da un server Python sulla porta 8770 che committava e pushava da solo;
- esisteva solo su un Mac con vault, python, git e quella porta libera;
- i «comandi java» sono le chiamate `javascript_tool` del browser dell'app nella
  costruzione delle liste (`/banco`), non il banco: quella parte non cambia qui.

## La decisione

1. **La pagina va su Netlify**: <https://banco-denkicode.netlify.app>, codice in
   `02-Sales/banco/`, sito collegato al vault (ramo `main`, base
   `02-Sales/banco`). Ogni push che tocca il banco o le due liste ripubblica da
   solo: la lista che `/banco` pubblica arriva online senza nessuno in mezzo.
2. **Lo stato sta in Netlify Blobs** (store `banco`): `contattati.csv` e
   `gia-col-sito.csv` con lo stesso formato e le stesse regole di
   `banco-server.py`, più i testi corretti a mano, che prima vivevano solo nel
   browser. Un gesto che non arriva al server resta in coda nel browser e riparte
   da solo.
3. **Accesso con nome e password** (`patrick`, `nicola`), sessione di 180
   giorni. Le password stanno solo in `~/.config/denkicode/banco-dm.txt` sul Mac
   di Nicola, mai nel vault, che è pubblico.
4. **Il vault resta la fonte delle liste e riceve gli invii**:
   `.github/workflows/banco-sync.yml` ogni 30 minuti fa l'unione di
   `contattati.csv` e `gia-col-sito.csv` con quelli online
   (`sincronizza-banco.py`, non toglie mai righe) e lancia
   `allinea-contattati.py`. Gli script di `/banco` continuano a leggere i CSV come
   prima.
5. **Stessa pagina, ridisegnata**: barra del prodotto sulla cartella, uscita
   animata, linguette con indicatore, scheletro di caricamento, telefono senza
   scroll orizzontale, installabile con «Aggiungi a Home». «Già contattati» si
   disegna 100 righe per volta: con 2.265 righe bloccava la scheda per più di 45
   secondi, anche sul banco vecchio.

6. **Un banco solo, «DenkiCode»** (Nicola, 11/10: «Rinomina»). Dal 30/09
   Patrick manda tutto dall'account DenkiCode, ma le liste stavano sotto
   «Patrick Sappa». Il selettore sparisce, `lista-denkicode.csv` (9 righe del
   7/09) non si apre più, i nuovi invii si scrivono con `Da` = `DenkiCode`.
7. **Sopra la lista non si scrive niente**: la nota della pagina e i nomi delle
   liste stanno dietro un tasto «Spiegazioni». Nicola: «questa parte sopra non
   mi piace per niente, lascia solo un tasto al massimo chiamato spiegazioni».
8. **La lista del giorno parte da sola alle 8** → [[giro-mattina]].

## Cosa si è scartato

- **Supabase**: un progetto nuovo, un account e chiavi in più per uno stato che
  sta in due CSV. Si riapre se il banco diventa multi-cliente (Bolanos).
- **Il vault come database** (commit a ogni gesto via API di GitHub): centinaia
  di commit al giorno e lo stesso difetto di prima.
- **Una funzione che serve la lista**: le funzioni Netlify rispondono al massimo
  6 MB e la lista cresce di ~90 KB al giorno. La lista è un file statico dietro
  una edge function che controlla la sessione.

## Conseguenze aperte

- Il giro di sincronizzazione non parte finché `BANCO_TOKEN` e `BANCO_URL` non
  sono fra i secret del repo (comandi nel registro interventi dell'11/10).
- Il passaggio va fatto in un colpo: quando Patrick ha la password, il passo 8
  di `/banco` e i lanciatori `Banco DM.command` puntano all'indirizzo nuovo e il
  server locale non si accende più. Usarli insieme lascia fuori dalla pagina
  online gli invii fatti dal vecchio finché non gira `allinea`.
- Limite noto: un «Annulla» su un invio la cui data è già finita nel CSV con una
  sincronizzazione torna «inviato» alla ricarica.
- Bug del banco vecchio trovato per strada: il recupero riusava la data del
  primo messaggio come chiave e cancellava la riga `primo` (43 recuperi su 25
  handle doppi in `contattati.csv`). Corretto nella versione online.
- Bolanos (agenzie, DM e mail) non c'è ancora: oggi c'è la stessa pagina di
  prima, online.

[[2026-10-01-banco-ricircolo]] · [[2026-09-02-cold-email-gestionali]] · [[contattati]]
