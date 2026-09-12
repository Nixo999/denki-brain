---
riga: Primo resoconto della posta Instagram - 490 DM in sei giorni, 5,8% di risposte vere, sette trattative aperte e ferme.
type: risorsa
updated: 2026-09-12
source: denkicode
verificato: 2026-09-12
tags: [dm-instagram, metriche, generazione-lead, banco-dm]
---

# La posta di Instagram, letta per la prima volta — 12 settembre 2026

Patrick: *«ora fallo da solo, d'ora in poi ogni volta che lancio il comando
/banco fallo in automatico. impara cosa c'è di sbagliato e orientati su quello,
dammi una mano a capire cosa sbaglio io e aiutami a chiudere i lead»*.

**Letto, non scritto**: nessun messaggio è partito da qui. L'invio resta suo.

## I numeri

| | |
|---|---|
| Conversazioni uno a uno | **499** |
| DM partiti dal 6 settembre | **490** (59 il 6, 93 il 7, 66 l'8, 86 il 9, 91 il 10, 95 il 12) |
| Risposte | **52**, cioè il **10,4%** |
| Di cui **autorisposte** | **23** |
| **Risposte vere** | **29**, cioè il **5,8%** |
| Rifiuti perché **hanno già il sito** | **8** su 29, il **28% delle risposte vere** |
| Trattative aperte | **7** |
| Conversazioni ferme con l'ultima parola a loro | **18** |

Il 5,8% è dentro la forchetta che [[metodo-instagram]] si aspetta. Il problema
non è quanti rispondono. È cosa succede dopo.

## Le sette trattative aperte, e da quanto aspettano

| Chi | Cosa ha detto | Ferma da |
|---|---|---|
| **@nailsmaniabergamo** | «mi mandi la voce se riuscisse, per email preferirei: frr85milo@gmail.com» — **lo ha chiesto due volte** | **5 giorni** |
| **@ilsalonediandrea** | «apprezzo il modo in cui ti sei posto, mandami pure, poi se mi piace ne parliamo» — la bozza l'ha avuta | **6 giorni** |
| **@shari_tattooer** | «ho preso visione, mando tutto ai miei e vediamo cosa valutano» | **7 giorni** |
| **@osteria.tarilli** | «diamo un'occhiata in questi giorni con calma» | **3 giorni** |
| **@dacaterinatoelettatura** | «vediamo» | **2 giorni** |
| **@pizzeria_lobidu** | «stiamo valutando la vostra opzione con quella di un content creator» | **1 giorno** |
| **@mikuma.dogs** | «stasera apro il link e guardo con calma» | **1 giorno** |

**Sono sette trattative, non sette messaggi.** Quattro di queste hanno già la
bozza in mano: è il momento in cui si chiude o si perde.

## Le cinque cose che non funzionano

**1. Chi chiede una cosa precisa non la riceve.** Nails Mania ha chiesto il
materiale **via email**, due volte, scrivendo l'indirizzo. Ha ricevuto un
**messaggio vocale** su Instagram, e ha dovuto ripetere la richiesta. Da cinque
giorni non è partito niente. È il lead più vicino al sì di tutta la posta.

**2. Nessuno torna sui caldi.** Il Salone di Andrea ha la bozza dal 6 settembre
e da allora il silenzio. Un «l'ha guardata?» dopo due giorni è la cosa che
costa meno e rende di più, e non è mai stata fatta.

**3. Si scrive a chi il sito ce l'ha.** Otto rifiuti su ventinove risposte
vere, e due scritti male: *«faccia meglio le sue ricerche, il sito ce l'abbiamo
e appare in SERP»*, *«la premessa su cui hai costruito la proposta non è
corretta»*. Ogni riga sbagliata non è solo un no: è un profilo che si ricorda
il nome.

**4. Il testo si fa riconoscere.** Angolo Relax, il 6 settembre: *«nemmeno il
messaggio è tuo: è un banale copy poco professionale per chatGPT. Leva le em
dashes che ti fanno sgamare all'istante»*. Aveva ragione: il messaggio di quel
giorno conteneva l'em dash. È il motivo per cui esiste [[voce-denkicode]] e per
cui `voce-check.py` adesso gira su ogni lista.
⚠️ **La risposta è stata peggiore dell'errore**: *«è il modo più veloce per
sviluppare lead, si riescono a inviare 600 messaggi all'ora»*. Al lead che ti
dice «sei uno dei tanti» si è confermato che è uno dei tanti.

**5. Sui ristoranti e sugli alberghi risponde il centralino.** Delle sei
risposte arrivate il 12 settembre, **sei su sei sono automatiche**: Mimesis,
Area Dima, Lait, Matura, Palace, Posta Moltrasio. Il DM a un profilo con la
risposta automatica non arriva a una persona, arriva a un filtro. Per
DenkiShift il telefono resta il canale, e il DM serve a scaldare, non a
chiudere → [[script-denkishift]].

## Cosa si fa adesso

1. **Mandare l'email a Nails Mania Bergamo.** È l'unica cosa urgente della
   giornata.
2. **Un solo messaggio ai quattro che hanno la bozza**, corto, senza rilanci.
3. **Le otto righe «ha già il sito» sono un difetto di lista**: sono tutte
   precedenti a `verifica-sito.py`, che dal 10 settembre gira su ogni riga.
   Se dopo il 12 settembre ne esce ancora una, il controllo non basta.

## Da dove vengono questi dati

Posta di Instagram letta dalla sessione di Patrick nel browser, con l'API
interna della inbox: 500 conversazioni scaricate, filtrate le uno a uno,
separate le autorisposte con il loro schema di frase. Gli esiti sono stati
scritti in `Esito DM` sulle righe che stanno ancora sul banco, **19 righe**;
le altre 26 risposte vengono da liste vecchie, ormai archiviate.

Il dettaglio riga per riga sta in `02-Sales/liste/risposte-dm.csv`.

## Collegamenti

[[metodo-instagram]] · [[metriche]] · [[dm-instagram-vetrina]] ·
[[dm-instagram-denkishift]] · [[voce-denkicode]] · [[flusso-vendita]] ·
[[2026-09-12-cinquanta-per-tipologia]]
