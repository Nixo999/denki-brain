---
riga: Prima lista della ricerca di mercato - 9 righe da 26 profili aperti, e la scoperta che Instagram non trova gli artigiani per comune.
type: area
updated: 2026-09-11
source: claude
verificato: 2026-09-11
prodotto: gestionale-custom
canale: instagram
anello: 1-2
stato: pubblicata
---

# Lista ricerca di mercato dell'11 settembre 2026 — 9 righe, e il canale che non si apre con la ricerca di Instagram

Prima lista del terzo prodotto, chiesta con [[2026-09-11-comando-banco]]. Doveva
essere da 30 righe. **Ne sono uscite 9**, ed è il numero che racconta il canale.

| | |
|---|---|
| File | `2026-09-11-instagram-ricerca-mb-va-co.csv` |
| Righe | **9**, tutte sul banco di Patrick, pagina Ricerca |
| Query di ricerca lanciate | ~200 |
| Profili trovati | 107 |
| Profili aperti e letti | 26 |
| Tenuti | 9, **resa 35% sugli aperti** |

## Chi è dentro

Tre serramentisti (Giussano Serramenti, Monza Serramenti in via Borgazzi,
Onda Group a Varese), tre fra officine e carrozzerie (Top Car a Limbiate, che
tiene insieme carrozzeria, meccanica, gommista e noleggio; Tecnocar RS a
Castelnuovo Bozzente; Autofficina Cantù, aperta dal 1965), una officina di
preparazioni (Monza Evoluzione), un impiantista su due province (MEV
Electronics, fotovoltaico e automazione) e un'impresa edile (Comodo, Besozzo).

**Il criterio non è «non ha il sito».** Qui il sito non c'entra: entra chi ha
processi da raccontare, cioè ordini, magazzino, cantieri, ore. Sei su nove il
sito ce l'hanno, ed è un motivo in più.

## Cosa ha scartato la lettura

| Perché | Quanti |
|---|---|
| **Fuori zona** (Genova, Mira, Napoli, Sant'Antimo, Montesarchio, Trento, Vicenza, Borgosatollo, Riva del Garda) | 9 |
| **Mestiere sbagliato**: «officina» che è un personal trainer, una pizzeria, un informagiovani, un brand di moda, un fotografo | 5 |
| **Profilo privato** | 2 |
| **Zona non confermata**, e senza quella non si scrive | 3 |

## La trappola che vale più della lista

**La ricerca di Instagram non trova gli artigiani per comune.** Venti query
mirate — `carrozzeria seregno`, `autofficina lissone`, `impresa edile seveso`,
`gommista desio`, `idraulico brianza` — hanno prodotto **un solo profilo nuovo**
in tutto.

Il motivo è quello già scritto per le toelettature in [[metodo-instagram]] e
qui morde molto di più: **la ricerca pesa il nome del profilo**, e mentre
un'onicotecnica si chiama «nails_tradate», una carrozzeria si chiama col
cognome del titolare. Il comune nel nome non c'è, quindi per la zona non si
trova niente. Le nove righe di oggi vengono quasi tutte da nomi che il comune
ce l'hanno per caso (`monzaserramenti`, `carrozzeria_top_car_limbiate`,
`autofficinacantu`).

**Conseguenza operativa**: per la ricerca di mercato il canale non parte da
Instagram. Parte da un elenco di categoria (Pagine Gialle, elenchi camerali,
Google Maps per comune) e l'handle si cerca dopo, per nome dell'azienda. È lo
stesso giro fatto per le toelettature il 9 settembre, e costa di più dei due
minuti a riga della bellezza.

## La seconda trappola: la bio nel sorgente è di un altro

Provato a leggere i profili scaricando l'HTML con `fetch` invece di aprire la
pagina: **i follower e i post nel `og:description` sono giusti, la
`biography` e l'`external_url` nel sorgente no.** Nella pagina c'è una sola
occorrenza di `"biography"` e non è del profilo richiesto. Chi si fidasse
scriverebbe messaggi costruiti sulla bio di qualcun altro: nella prova, la
stessa bio identica su settanta profili diversi.

Quindi il passo 2 di [[metodo-instagram]] resta com'è: **la pagina si apre**.
Il `fetch` serve solo come filtro grosso, per follower e numero di post.

## Il messaggio

Nove testi, uno per riga, tutti passati da `voce-check.py`: **zero tell**,
tranne «link nel messaggio», che qui è voluto e dichiarato. Il link del modulo
sta nel primo DM perché è la richiesta, e sul banco ci sono i due tasti per
mandarlo dopo → [[dm-instagram-ricerca]].

Il modulo è quello di [[script-indagine]]: sei domande, anonimo, due minuti.
Due delle sei chiedono com'è messo il sito e dove servirebbe un programma:
**chi risponde si qualifica da solo** per gli altri due prodotti.

## Cosa manca

⬜ **La lista siti da 50 e quella DenkiShift da 50 non sono state costruite.**
Sul banco ci sono già **292 righe siti** pendenti, che al tetto di 65 sono
quattro giorni e mezzo di lavoro, e 30 DenkiShift. Il buco vero era la
ricerca, che stava a zero.
⬜ La resa del canale è da misurare: quanti rispondono, quanti compilano.
Si scrive nella tabella di [[dm-instagram-ricerca]].

## Collegamenti

[[dm-instagram-ricerca]] · [[script-indagine]] · [[metodo-instagram]] ·
[[metodo-liste]] · [[2026-09-11-comando-banco]] · [[generazione-lead]]
