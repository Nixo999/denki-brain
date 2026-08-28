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
| **Chiamate** | Quante persone hanno **effettivamente risposto** e ci hanno parlato. ⚠️ **Non** i numeri composti: le chiamate a vuoto non contano | Il foglio: le righe con un esito **diverso da `Non risponde`** | **50** |
| **Appuntamenti** | Quante volte una chiamata è finita con qualcosa di concreto: un incontro fissato con Patrick, o un sì a ricevere la bozza | Stesso foglio: le righe con esito "Fissato incontro" o equivalente | **4** |

Il rapporto atteso è **8%** (4 appuntamenti su 50 conversazioni). Se scende,
guarda lo script; se sale, quella lista era buona — **segnati da dove veniva**.

## Come si compilano

Venerdì, in due minuti:

1. Apri il Google Sheet delle liste
2. Conta le righe con un esito **diverso da `Non risponde`** → è il numero
   chiamate. Chi non ha risposto non conta
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

> [!warning] Analisi di Claude — 2026-08-28, corretta in giornata
> **Avevo sbagliato il conto.** Avevo letto "50 chiamate" come 50 numeri
> composti, e ne avevo dedotto che a Giulia avanzasse tempo. Sono **50 risposte
> vere**, ed è tutta un'altra cosa.
>
> Per ottenere 50 conversazioni servono circa **130 numeri composti** (tasso di
> risposta realistico del 40% su utenze aziendali). Il tempo:
>
> | Voce | Conto | Tempo |
> |---|---|---|
> | Numeri a vuoto | 80 × 25 s | ~35 min |
> | Risposte brevi (persona sbagliata, no secco) | 20 × 1 min | ~20 min |
> | Conversazioni vere | 30 × 4-5 min | ~2 h 15 |
> | Note sul foglio | 130 × 20 s | ~45 min |
> | **Totale** | | **~3 h 55** |
>
> Giulia ne ha **cinque**. Il target la porta a circa l'**80% della sua
> capacità**: è un obiettivo pieno, non comodo. Le due conseguenze si ribaltano
> rispetto a quanto avevo scritto prima:
>
> 1. **La lista settimanale va dimensionata a 130-150 contatti**, non a 70-80 e
>    tantomeno a 50. La prima lista da 51 righe
>    ([[2026-08-28-brianza-turni]]) copre **due giorni**, non una settimana.
> 2. **Non c'è margine per le chiamate sprecate.** Ogni minuto speso su
>    un'azienda sotto le 8 persone toglie una conversazione utile: la qualifica
>    rapida nello script smette di essere una cortesia e diventa il modo di far
>    tornare i conti.
>
> ⚠️ E l'orario pesa più di prima: con quattro ore di lavoro su cinque
> disponibili, un'ora nella fascia sbagliata è il **20% della settimana**. Le
> fasce stanno in [[metodo-liste]].

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
