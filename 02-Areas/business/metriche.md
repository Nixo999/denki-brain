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
