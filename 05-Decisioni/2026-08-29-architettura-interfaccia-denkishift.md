---
type: decisione
data: 2026-08-29
progetto: denkishift
source: claude
---

# Il menu di DenkiShift è l'elenco delle domande, non delle pagine

> [!warning] Proposta di decisione, non ancora ratificata
> Le decisioni in questa cartella le prendono Nicola e Patrick. Questa la
> propone Claude e ha bisogno di due sì: **Nicola** sulle etichette e sulla
> voce nuova, **Patrick** sul nome del prodotto a schermo. Finché non
> arrivano, `layout.tsx` non si tocca — ed è il primo file che si aprirebbe.

Il ragionamento completo sta in [[denkishift-interfaccia]]. Qui c'è solo la
parte che va firmata prima di scrivere codice, perché l'etichetta di menu è
**una stringa sola per indirizzo** e tre proposte diverse davano tre valori agli
stessi due indirizzi.

## Cosa si decide

**1. Il menu è per domande, non per moduli.** Le voci sono quelle che un
titolare di negozio si chiede: *com'è messa la settimana · devo scrivere i turni
· chi c'è adesso · chi mi manca · quante ore*. Non «Supervisione», «Prospetto»,
«Permessi», che sono i nomi che le pagine hanno preso quando le ha scritte chi
le ha costruite.

| Indirizzo | Capo | Dipendente |
|---|---|---|
| `/oggi` **(nuova)** | Oggi | — |
| `/turni` | Turni | I miei turni |
| `/supervisione` | Chi c'è | Chi c'è |
| `/permessi` | Assenze | Permessi |
| `/prospetto` | Ore *(titolo di pagina: Ore e assenze)* | — |
| `/disponibilita` | — | Quando posso / Quando non posso, secondo il regime |

**Nessuna rotta cambia.** Sono stringhe, e il meccanismo per differenziare
l'etichetta per ruolo esiste già ed è usato oggi su `/turni`.

**2. Squadra, Impostazioni e Aziende escono dalla barra** e vanno nella tendina
dell'iniziale. Si aprono una volta a settimana o una volta al mese; «Aziende»
in particolare cambia guscio, titolo e menu senza preavviso, e sta nella barra
dell'unico account con cui si fa la demo.

**3. Le pagine spegnibili restano spegnibili, e lo restano tutte.** Chi tocca
il menu tiene insieme i due controlli — quello che nasconde la voce e quello
dentro la pagina — perché l'indirizzo se lo ricorda il browser. Il rimbalzo di
una pagina spenta smette di essere muto e **cambia destinazione secondo il
ruolo**: la home nuova non esiste per il dipendente.

**4. Una parola per cosa, un verbo per gesto.** «Pubblica» significa una cosa
sola: farlo vedere ai dipendenti. «Conferma» sparisce come verbo di sistema.
«Da assegnare» e «turno scoperto» diventano **scoperto**. «Posta» e «Messaggi»
diventano **da decidere** e **da leggere**. Il vocabolario completo sta in
[[denkishift-interfaccia]] e va scritto nel repo, in `docs/`, o fra tre mesi si
sfalda di nuovo.

## Cosa non si decide qui

- **Il nome del prodotto a schermo.** Oggi l'app dice «Turni» ovunque l'utente
  guardi, il materiale commerciale dice DenkiShift. Non costa ore di sviluppo,
  costa una risposta di Patrick, e blocca due pezzi del lavoro.
- **Se il turno rifiutato resta scoperto o sparisce.** Oggi viene cancellato. Il
  testo delle Impostazioni non si può scrivere finché non è deciso quale dei due
  è il comportamento giusto: è una domanda per Nicola, non per chi scrive il
  copy.
- **`/admin`**, che resta fuori perimetro finché qualcuno non dice il contrario.

## Perché adesso

Perché il lavoro sulla riprogettazione comincia da `layout.tsx`, e con tre
etichette in ballo per lo stesso indirizzo quel file non si può scrivere. E
perché in demo Patrick deve dire **un nome solo** per ogni schermata: se lo
schermo e la sua voce non coincidono, se ne accorge il cliente prima di lui.

## Collegamenti

[[denkishift-interfaccia]] · [[denkishift]] · [[obiezione-non-sapranno-usarlo]] ·
[[2026-08-28-stack-non-uniforme]]
