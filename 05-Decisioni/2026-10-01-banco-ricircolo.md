---
riga: /banco riscritto l'1 ottobre - perche' la lista non usciva al primo colpo, il piano del giorno lo stampa uno script, Patrick non lancia piu' niente, e la resa misurata dei DM.
type: decisione
data: 2026-10-01
progetto: banco-dm
updated: 2026-10-01
source: claude
verificato: 2026-10-01
stato: presa
tags: [banco, liste, instagram]
---

# Settori e luoghi li sceglie uno script, e Patrick scrive solo nella chat

## Il contesto

Nicola, 1 ottobre 2026: il banco DM «dà un sacco di problemi», Patrick «ogni
volta deve mandare un comando in java», la lista non esce al primo tentativo,
le ricerche sono «sbagliate e ridondanti nei settori». Le due frasi esatte
stanno in [[metodo-liste]], sezione Regole.

**Perché non usciva al primo colpo** (letto su commit e note lista, 24-30/09):

1. Trovare i profili non era uno script: snippet JavaScript sull'API interna di
   Instagram, dentro la sessione del browser. Bloccati il 21, 23 e 25/09; la
   procedura scritta diceva «va rifatto a mano da Patrick».
2. Davanti a un blocco la sessione si fermava e riferiva. 25/09: zero righe
   alle 00:04, 163 all'01:43 dopo «sono stanco di dirtelo, crea i lead».
3. `/banco` era a 480 righe con le regole superate ancora dentro, in
   contraddizione fra loro.
4. La regola del 29/09 («un settore fino in fondo, luogo per luogo») ha portato
   il costo da 1,9 a 7,2 profili aperti per riga: 25 commit in quattro ore.
5. Settori riaperti dopo essere stati bocciati (fotografi, tatuatori) e settori
   della ricerca che su Instagram non esistono (studi tecnici: 1 su 376 schede).

## La decisione

1. **Il piano del giorno lo stampa `prossimo-giro.py`**: celle luogo × settore
   ordinate per resa misurata (settore e provincia), con la freschezza che fa
   girare settori e luoghi e una cella esaurita che torna dopo 30 giorni.
   L'elenco dei settori è uno solo, `02-Sales/liste/settori.csv`, con stato e
   **canale**: quello che non vive su Instagram va al telefono, non in DM.
2. **Patrick scrive solo nella chat.** Il server del banco parte staccato con
   `banco-server.py --apri`, senza Terminale. Un blocco non ferma la lista: si
   cambia fonte, e lo si dice in una riga a fine risposta.
3. **`pubblica-lista.py`** appende al banco: nessuno apre più il CSV da 2,1 MB.
4. **`resa-dm.py`** rimisura la resa quando la posta viene letta.

## La resa misurata (815 DM letti, al 14/09)

- Positivi **1,7%** (14 su 815), piatto sui tre prodotti. Nessun settore supera
  3 positivi: le differenze fra settori sono rumore.
- **Ristorazione: 0 positivi su 157**, 11 risposte su 23 sono autorisposte.
- Settori in pausa 2,2% (7/321), gli altri 2,6% (3/117): indistinguibili. La
  pausa del 29/09 non è né confermata né smentita.
- Province: BS 5/103, BG 3/108, MI 2/53; VA, MB e Ticino 0 su 227.
- **Buchi**: la posta non è letta dal 21/09 (367 DM senza esito); le chiamate
  di Giulia non hanno un esito scritto; WhatsApp ed email mai misurati.

## Cosa si è scartato

- **Un LaunchAgent che tiene il server sempre acceso**: sul Mac di Patrick il
  vault sta sul Desktop, e un processo di launchd lì chiede un permesso suo.
- **Togliere la pausa alla bellezza**: è una regola di Patrick, i dati non la
  smentiscono.

## Conseguenze aperte

- Supera in parte la regola di Patrick del 29/09: restano «si parte da casa» e
  «la bellezza è in pausa», non «un settore fino in fondo». Da dire a Patrick.
- **Sul banco ci sono 733 righe mai mandate** (ricerca 374, siti 355): 184 sono
  di settori in pausa, 250 della ricerca hanno 8-17 giorni.
- La strada senza JavaScript per trovare i profili dal Mac di Patrick non è
  ancora stata misurata.
- `lista-denkicode.csv` non ha le colonne `Lista` e `Prodotto`.
