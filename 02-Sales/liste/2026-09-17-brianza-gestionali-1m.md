---
riga: 100 aziende +1M di fatturato entro 10 km da Seveso per la campagna gestionali. File - 2026-09-17-brianza-gestionali-1m.csv, piu' 237 di riserva.
type: area
updated: 2026-09-17
source: claude
verificato: 2026-09-17
prodotto: gestionale-custom
contatti: 100
stato: da-chiamare
---

# Lista 2026-09-17 — Brianza, gestionali e automazioni, +1M di fatturato

Chiesta da Patrick: cold call su PMI B2B strutturate entro 10 km da Seveso, solo
sopra il milione di fatturato. Schema a 8 colonne di [[ciclo-settimanale]].

| File | Righe | Cos'è |
|---|---|---|
| `2026-09-17-brianza-gestionali-1m.csv` | **100** | la lista da chiamare |
| `2026-09-17-brianza-gestionali-1m-riserva.csv` | **237** | stesso filtro, stessa verifica: si pesca da qui quando le 100 finiscono |
| `2026-09-17-brianza-anagrafica-1m.json` | 2.855 | l'anagrafica grezza, per rifare il taglio senza riscaricare niente |

## Da dove escono i numeri

Niente è stato dedotto a memoria. Il procedimento, in quattro passaggi:

1. **Fatturato** — `companyreports.it`, comune per comune, 35 comuni. Sono
   bilanci depositati, non stime: **2.893 società sopra il milione**.
2. **Anagrafica** — letta la scheda di ognuna: **ATECO, indirizzo, banda
   dipendenti, stato attività, anno del bilancio**. 2.855 schede.
3. **Filtro** — settori del brief, comune entro 10 km, **stato «Attiva»**,
   fatturato 1–60 M€, fuori holding/immobiliari/consulenza/dettaglio →
   **1.752 candidate**. Poi fuori chi ha meno di sei persone (senza squadra non
   c'è né un turno né una commessa) e una riga sola per centralino.
4. **Telefono** — cercato su Pagine Gialle riga per riga. Vale **solo** se i
   token del nome coincidono esattamente **e** l'indirizzo è nel comune giusto:
   «2 Emme» non è «3 Emme Project», «Colombo R.» non è «Antonio Colombo e C.».
   **367 numeri** su 1.752; **337** dopo aver tolto chi ha meno di sei persone e
   le società dello stesso gruppo sullo stesso centralino. La prova — quale
   ricerca, quale scheda, quale indirizzo — sta riga per riga nella colonna
   `Note Strategiche`.

⚠️ **Gli script che hanno prodotto tutto questo vivevano nella sessione e non
ci sono più.** Quello che resta e che conta è il JSON: da lì si rifà qualunque
altro taglio — un altro settore, un altro raggio, un'altra soglia — senza
riscaricare niente.

## Com'è composta la lista

| Settore | Righe |
|---|---|
| Metalmeccanica e officine | 30 |
| Manifattura (arredo, plastica, chimica, alimentare) | 20 |
| Impiantistica e cantieri | 18 |
| Ingrosso e distribuzione | 12 |
| Logistica e trasporti | 12 |
| Pulizie e servizi strutturati | 5 |
| Autoriparazione | 3 |

**26 comuni, tutti coperti.** **77 righe su 100 dichiarano almeno 20
dipendenti.** Distanza massima 10 km, fatturato mediano attorno ai 4 M€.

## I tre settori su cui puntare — **ipotesi, non misura**

> [!warning] Il tasso di conversione non esiste ancora
> DenkiCode non ha **nessun appuntamento chiuso al telefono** da registrare:
> in [[metriche]] il canale telefono ha 131 righe chiuse, risposte `TODO`,
> una trattativa e **0 € incassati**. Chi scrive «settore ad alta conversione»
> sta inventando. Quello che segue è un ordine costruito sulla **densità di
> aziende strutturate**, che è un dato, più il dolore operativo descritto in
> [[metodo-liste]]. Si conferma o si smentisce dopo 40 chiamate su un settore
> solo, non prima.

Densità di aziende con **almeno 20 dipendenti**, sul bacino sopra il milione
entro 10 km:

| Settore | Sopra 1M | Con ≥20 dip. | Quota | Perché fa male |
|---|---|---|---|---|
| **Pulizie e servizi strutturati** | 45 | 20 | **44%** | Personale sparso su più cantieri, ogni giorno diverso. È il segmento 2 di [[metodo-liste]] |
| **Logistica e trasporti** | 84 | 31 | **37%** | Turni autisti su fasce, viaggi da assegnare, picchi stagionali |
| **Metalmeccanica e officine conto terzi** | 328 | 103 | **31%** | Commessa che attraversa quattro reparti e nessuno sa a che punto è |

**Perché non l'impiantistica**, che pure ha il gancio più bello (il rapportino
di cantiere ribattuto in ufficio): 310 aziende sopra il milione ma solo il
**14%** arriva a 20 persone. Fatturato alto, organico piccolo — il dolore c'è,
la disponibilità a pagare molto meno. Resta in lista con 18 righe, non in testa.

**Perché non l'ingrosso**: 412 aziende, stessa quota del 14%. Molte sono
società commerciali con tre persone e un magazzino di terzi.

## I ganci, per settore

Scritti nella colonna `Note Strategiche` riga per riga. In sintesi:

| Settore | Gancio |
|---|---|
| Pulizie e servizi | Turni multi-cantiere: chi va dove domani, sostituzioni e ore comprese |
| Trasporti | Turni autisti e assegnazione mezzi, senza il foglio in portineria |
| Magazzinaggio | Giri di consegna e stato del carico senza telefonate al magazzino |
| Officine e carpenterie | Tracciamento commesse: quale pezzo a che fase, senza girare a chiedere |
| Impiantistica | Rapportini di cantiere dal telefono: ore, materiali, stato commessa |
| Costruzioni | Stato avanzamento e SAL: quanto è fatto e quanto è fatturabile |
| Ingrosso | Ordini e magazzino sincronizzati: giacenza vera col cliente al telefono |
| Manifattura | Ordine di produzione tracciato, dalla conferma alla spedizione |

L'apertura è quella di [[script-indagine]]: **non si vende niente**, si fa la
ricerca e si fa compilare il modulo. Su pulizie e trasporti si può aprire anche
con [[script-denkishift]], che è l'unico caso in cui il prodotto si nomina.

## ⚠️ Cosa NON è verificato

- **Il referente non c'è, per nessuna delle 100.** Nome e ruolo di chi decide
  non stanno nelle fonti gratuite: il legale rappresentante su companyreports è
  dietro pagamento. In lista c'è `referente TODO`. Lo si chiede al centralino
  con la domanda che è già nello script — «chi è che fa i turni / segue le
  commesse?» — e da quel momento la riga ha un nome.
- **I numeri non sono stati chiamati.** Vengono da Pagine Gialle, con la prova
  scritta accanto. Il primo squillo è la verifica.
- **L'anno del bilancio cambia da azienda ad azienda** (dal 2020 al 2024): è
  l'ultimo depositato, ed è scritto in chiaro nella colonna. Un fatturato 2020
  vale come ordine di grandezza, non come numero di oggi.
- **La banda dipendenti è quella dichiarata alla camera di commercio**, non un
  organico contato. Dove manca c'è `n.d.` — sono quasi tutte cooperative.
- **Le distanze sono da centro paese a centro paese**, non stradali.
- **337 numeri su 1.752 candidate**: il 19%. Le altre non sono «senza
  telefono», sono **non verificate** — Pagine Gialle non le ha o le ha scritte
  in un modo che non coincide. Ricerca fallita non è ricerca negativa
  ([[metodo-liste]]).

## Collegamenti

[[metodo-liste]] · [[script-indagine]] · [[script-denkishift]] ·
[[generazione-lead]] · [[metriche]] · [[prodotti-e-listino]] ·
[[2026-08-28-brianza-turni]] · [[ciclo-settimanale]]
