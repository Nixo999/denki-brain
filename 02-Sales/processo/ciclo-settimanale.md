---
type: risorsa
updated: 2026-08-28
source: denkicode
tags: [processo, liste, report, settimanale]
---

# Il ciclo settimanale — domenica → domenica

Dettato da Patrick il 28 agosto 2026. **È il processo fisso.** Da qui in avanti
la settimana commerciale ha questa forma e non si decide più il lunedì cosa
chiamare.

⚠️ Non sostituisce [[metodo-liste]]: quello dice **come si costruisce** una
lista, questo dice **quante ne servono, quando arrivano e cosa torna indietro**.

## La settimana in una tabella

| Quando | Chi | Cosa |
|---|---|---|
| Lun–Sab | Giulia | Chiama le sue 3 liste, compila `Esito e Note Giulia` |
| Lun–Sab | Patrick | 10 blitz fisici + i secondi incontri sui lead qualificati |
| Domenica | Patrick | Carica i **5 input** compilati |
| Domenica | JARVIS | Analizza, affina gli script, genera i **4 output** nuovi |
| Lunedì | tutti | Si riparte con la macchina nuova |

## I 4 output della domenica

| # | Output | Volume | Destinatario | Prodotto |
|---|---|---|---|---|
| 1 | Lista Siti Web | **50** | Giulia | A — Vetrina / B — E-commerce |
| 2 | Lista DenkiShift | **50** | Giulia | C — DenkiShift |
| 3 | Lista Indagine di Mercato | **30** | Giulia | D — Custom, via form |
| 4 | Target fisici | **10** | Patrick | A o C, porta-a-porta |

Le prime tre escono come **CSV scaricabile**, una tabella per lista. La quarta
esce come elenco, non come foglio: si legge in macchina, non si compila.

### Chi sta in quale lista

- **Siti Web** — PMI locali con sito obsoleto, assente o mal posizionato
- **DenkiShift** — ristoranti, bar, locali, attività con personale a turni.
  Vale la qualifica di [[metodo-liste]]: **8-50 dipendenti**, turni variabili,
  niente catene
- **Indagine di Mercato** — aziende strutturate, officine, logistica, negozi
  con gestione complessa. Giulia **non vende**: fa compilare il form

## Le 8 colonne — schema unico per tutte e tre le liste

```
Nome Azienda | Telefono / Cellulare | Tipo Azienda | Settore |
Servizio da Vendere | Prezzo Indicativo | Note Strategiche (Claude) |
Esito e Note Giulia
```

| Colonna | Cosa ci va |
|---|---|
| Nome Azienda | Ragione sociale o insegna, seguita dal **comune** |
| Telefono / Cellulare | Numero diretto. Un numero per riga |
| Tipo Azienda | Ristorante, barbiere, officina, showroom, RSA… |
| Settore | Ristorazione, wellness, servizi B2B, artigianato… |
| Servizio da Vendere | Sito Vetrina · E-commerce · DenkiShift · Indagine Mercato |
| Prezzo Indicativo | Vedi tabella sotto. **Mai un canone mensile nudo** |
| Note Strategiche (Claude) | L'angolo d'attacco: il **segnale osservato**, non un aggettivo |
| Esito e Note Giulia | Vuota alla consegna. La riempie lei |

**`Esito e Note Giulia` comincia sempre con una delle sei parole di
[[metodo-liste]]**, poi un trattino e il testo libero:

`Non risponde` · `Richiamare` · `Non è il decisore` · `No` · `Troppo piccoli` ·
`Fissato incontro`

> `Fissato incontro - giovedì 4/9 ore 15, parlato col titolare, ha 22 dipendenti`

Senza quel prefisso [[metriche]] non si conta da sola e la domenica diventa
lettura a mano di 130 righe.

### Prezzo Indicativo — le forme ammesse

| Servizio | Si scrive così | Perché |
|---|---|---|
| Sito Vetrina | `200 EUR + 180 EUR/anno` | Il canone si incassa **annuale anticipato** → [[vincoli-fiscali]] |
| E-commerce | `da 500 EUR + 360 EUR/anno` | Idem. Le royalty non si nominano al telefono |
| DenkiShift | `2 EUR/dipendente/mese` | Unico caso in cui il mensile si dice: lo paga l'azienda, non è un canone nostro |
| Indagine Mercato | `Ricerca Form` | Non c'è prezzo: non si sta vendendo |

⚠️ Sui siti **non si scrive "15 EUR/mese"**: Giulia lo direbbe al telefono e
noi non possiamo incassarlo così senza P.IVA.

## L'output 4 — i 10 target fisici di Patrick

Area Monza e Brianza. Per ciascuno:

- **Nome attività e indirizzo/zona**
- **Tipologia / settore**
- **Servizio da proporre** — Sito Vetrina o DenkiShift
- **Gancio d'ingresso** — il *pattern interrupt visivo*: cosa guardare **prima
  di entrare** (vetrina senza orari, menù cartaceo rovinato, nessun social,
  cartello "cercasi personale") per rompere il ghiaccio nei primi 10 secondi

Materiale: volantini per i siti, biglietti da visita per i gestionali →
[[materiale-offline]]. Il biglietto lasciato è il riscaldamento della chiamata
di Giulia entro 48 ore → [[metodo-liste]].

## I 5 input della domenica

Patrick carica, in un blocco solo, il [[template-report-settimanale|template]]:

1. Lista Siti Web compilata
2. Lista DenkiShift compilata
3. Lista Indagine di Mercato compilata
4. Report dei 10 blitz fisici
5. Report dei secondi incontri e delle chiusure

## Il compito di JARVIS alla domenica

Nell'ordine:

1. **Contare.** Chiamate, risposte, esiti per categoria, appuntamenti fissati,
   chiusure. I numeri vanno in [[metriche]] prima di qualunque commento
2. **Trovare le obiezioni ricorrenti** e riscriverne il looping in
   [[script-giulia-denkishift]] e [[pattern-interrupt]]
3. **Diagnosticare le chiusure mancate.** Per ogni secondo incontro perso: dove
   esattamente si è fermata la vendita e la contromisura esatta, non un consiglio
   generico
4. **Ricalibrare il targeting.** I segmenti che rispondono pesano di più nella
   settimana dopo; quelli muti escono. Vale sia per le liste di Giulia sia per
   le tipologie di locale dei blitz di Patrick
5. **Generare i 4 output nuovi** con angoli d'attacco affinati sui dati appena
   letti

> [!note] Analisi di Claude — 2026-08-28. Quattro rilievi sul protocollo, da verificare sul campo.
>
> **Il volume è giusto, e non per caso.** 50+50+30 fa **130 numeri**, che è
> esattamente il dimensionamento calcolato in [[metriche]]: al 40% di risposta
> sono ~50 conversazioni vere, ~4 ore delle 5 che Giulia ha. Il protocollo la
> porta all'80% della capacità. Non c'è spazio per una quarta lista.
>
> **Ma le 50 conversazioni si dividono in tre.** Su tre prodotti diversi fanno
> ~20 risposte vere per script a settimana. Il test "40 chiamate su un solo
> segmento" aperto in [[generazione-lead]] **richiede due settimane**, non una:
> se ogni domenica cambio anche gli script, nessuna versione arriva mai a un
> campione leggibile. **Gli script si toccano ogni due settimane, le liste ogni
> settimana.**
>
> **Due colonne sono sparite.** `Comune` e `Segnale` di [[metodo-liste]] non
> esistono più come campi: le assorbo dentro `Nome Azienda` e
> `Note Strategiche`. Il costo è reale — non si filtra più per comune su Excel,
> e la regola «una lista = un segmento + un comune» va tenuta a mano
> raggruppando le righe. Stessa sorte per `Data richiamo` e `Appuntamento`, che
> finiscono nel testo libero di Giulia.
>
> **La lista [[2026-08-28-brianza-turni]] è a 12 colonne.** Va convertita allo
> schema nuovo prima del primo lunedì, o Giulia lavora su due formati diversi.

## Collegamenti

[[metodo-liste]] · [[template-report-settimanale]] · [[generazione-lead]] ·
[[metriche]] · [[script-giulia-denkishift]] · [[pattern-interrupt]] ·
[[materiale-offline]] · [[prodotti-e-listino]] ·
[[2026-08-28-ciclo-settimanale]]
