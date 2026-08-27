---
type: area
updated: 2026-08-28
source: denkicode
---

# Metriche

## A cosa serve questa nota

Ogni venerdì si scrivono **due numeri**. Nient'altro. Servono a rispondere a una
domanda sola: *la macchina commerciale sta girando, o ci stiamo raccontando che
gira?*

Senza questi numeri, "questa settimana è andata male" è una sensazione. Con
questi numeri si sa **dove** è andata male: se le chiamate erano poche, il
problema è la lista; se erano tante e gli appuntamenti zero, il problema è lo
script.

## I due numeri, e da dove si prendono

| Numero | Cos'è, in concreto | Dove sta | Target |
|---|---|---|---|
| **Chiamate** | Quante volte Giulia ha alzato il telefono e chiamato qualcuno della lista, in tutta la settimana. Contano anche quelle in cui non ha risposto nessuno | Il Google Sheet delle liste: si contano le righe con un esito segnato | **50** |
| **Appuntamenti** | Quante volte una chiamata è finita con qualcosa di concreto: un incontro fissato con Patrick, o un sì a ricevere la bozza | Stesso foglio: le righe con esito "Fissato incontro" o equivalente | **4** |

Il rapporto atteso è **8%** (4 su 50). Se scende, guarda la lista o lo script.
Se sale, quella lista era buona: **segnati da dove veniva**.

## Come si compilano

Venerdì, in due minuti:

1. Apri il Google Sheet delle liste
2. Conta le righe con un esito segnato questa settimana → è il numero chiamate
3. Conta quelle con "Fissato incontro" → è il numero appuntamenti
4. Scrivili nella tabella qui sotto

Oppure, più semplice: lancia `/settimana` da Claude Code. Te li chiede lui e li
scrive al posto tuo.

**Se una settimana non li avete contati, scrivi `n.d.` invece di inventarli.**
Un buco dichiarato non rompe niente; un numero inventato falsa il confronto per
sempre.

## Storico settimanale

La settimana si scrive come `2026-W35` (anno + numero della settimana). W35 è
quella dal 24 al 30 agosto 2026.

| Settimana | Chiamate | Appuntamenti | Chiusure | Incassato |
|---|---|---|---|---|
| 2026-W35 | | | | |

## La capacità di Giulia, e cosa ne consegue

**Un'ora al giorno**, circa cinque a settimana (2026-08-28). Può crescere se
cresce il guadagno, e in quel caso crescono anche i target qui sopra.

> [!note] Analisi di Claude — 2026-08-28
> Il conto, fatto con le proporzioni normali di una chiamata a freddo: su 50
> numeri, più o meno 28 non rispondono (mezzo minuto ciascuno), 11 finiscono in
> un centralino o nella persona sbagliata (un minuto), 11 diventano una
> conversazione vera (quattro-cinque minuti). **Totale: circa due ore, comprese
> le note sul foglio.**
>
> Giulia ne ha cinque. **Il target di 50 chiamate occupa meno di metà del suo
> tempo disponibile**, e questo cambia la diagnosi: il limite non è quanto può
> chiamare, è quanto ha da chiamare.
>
> Due conseguenze pratiche:
>
> 1. **La lista settimanale va dimensionata a 70-80 contatti, non a 50.**
>    Altrimenti finisce i numeri il giovedì e l'ora del venerdì è persa.
> 2. **Alzare il target a 50 chiamate non costa nulla in ore**, ma non serve
>    finché la lista non c'è. È il motivo per cui [[metodo-liste]] viene prima
>    di qualunque revisione dei numeri.
>
> ⚠️ Con un'ora al giorno, **quando la si chiama conta quanto chi si chiama**:
> un'ora sbagliata su un segmento sbagliato è una giornata buttata, e ne avete
> solo cinque. Le fasce per segmento stanno in [[metodo-liste]].

## Cosa non stiamo misurando, e dovremmo

> [!note] Analisi di Claude — 2026-08-28
> I due numeri sopra coprono la cima e il centro dell'imbuto. Mancano i due
> estremi, che sono quelli che dicono se l'azienda guadagna:
>
> | Metrica mancante | Perché serve |
> |---|---|
> | **Contatti nuovi in lista / settimana** | Se Giulia fa 50 chiamate su una lista di 60, la settimana dopo non ha più nessuno da chiamare. È il collo di bottiglia dichiarato, e non è misurato |
> | **Chiusure / settimana** | 4 appuntamenti valgono zero se Patrick ne chiude zero. Senza questo numero non si sa se il problema è la lista o la trattativa |
> | **Incassato / mese** | L'unico numero che paga la P.IVA a novembre |
> | **Residuo sul tetto** | Va guardato prima di ogni incasso → [[vincoli-fiscali]] |
>
> Non serve uno strumento nuovo: bastano tre colonne in più sul Google Sheet
> (esito, data appuntamento, esito appuntamento) e leggerlo una volta a
> settimana. Le due colonne "Chiusure" e "Incassato" della tabella qui sopra
> sono già pronte ad accoglierli.

## Collegamenti

[[stato-azienda]] · [[obiettivi-6-mesi]] · [[generazione-lead]] ·
[[flusso-vendita]] · [[vincoli-fiscali]]
