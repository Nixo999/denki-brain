---
riga: Le 87 righe di Gabriele ed Edoardo riordinate per Giulia nello schema del ciclo: 27 siti, 30 DenkiShift, 30 indagine. Siti riverificati a macchina il 13/09.
type: area
updated: 2026-09-13
source: claude
verificato: 2026-09-13
prodotto: multi
contatti: 87
stato: da-chiamare
---

# Le liste di Giulia — Groane e Vimercatese, dal 14 settembre 2026

Gabriele ed Edoardo sono fuori senza aver chiamato nessuno
([[2026-09-13-caller-fuori]]). Le loro 87 righe non si buttano: erano costruite
bene ([[2026-08-30-liste-gabriele-edoardo]]) e tornano indietro intatte, con la
colonna esito vuota su tutte. Qui sono riordinate nello schema di
[[ciclo-settimanale]] e intestate a Giulia.

## I file da mandarle

| File | Righe | Prodotto | Script |
|---|---|---|---|
| `2026-09-13-GIULIA-SITI.xlsx` | **27** | Sito Vetrina (24) + E-commerce (3) | [[script-siti-vetrina]] · [[script-ecommerce]] |
| `2026-09-13-GIULIA-DENKISHIFT.xlsx` | **30** | DenkiShift | [[script-denkishift]] + [[pattern-interrupt]] |
| `2026-09-13-GIULIA-INDAGINE.xlsx` | **30** | Indagine, al form | [[script-indagine]] |

Gli `.xlsx` sono la copia che compila lei; i `.csv` con lo stesso nome
minuscolo sono quelli che rileggo la domenica. **Otto colonne**, l'ultima si
chiama `Esito e Note Giulia` come nelle sue liste vecchie: niente formato nuovo
da imparare.

**Ordine delle righe: prima Groane, poi Vimercatese.** Si chiama una zona per
volta, altrimenti il «qui a Limbiate» non si può dire.

## Volume: 87 dove il ciclo ne chiede 130

| Lista | Ha | Il ciclo chiede | Manca |
|---|---|---|---|
| Siti | 27 | 50 | **23** |
| DenkiShift | 30 | 50 | **20** |
| Indagine | 30 | 30 | — |

Al passo con cui ha chiuso le 131 righe precedenti in due settimane, **queste
finiscono in quattro giorni scarsi**: giovedì è scoperta. Le 43 righe mancanti
sono lavoro di ricerca, non di riordino.

## Le cinque righe che la macchina ha marcato, lette a mano

`verifica-sito.py` ha girato sulle 27 righe di siti il 13 settembre: la verifica
precedente era del 30 agosto, e due settimane bastano perché un sito compaia.
Quattro «sito vivo» e un «probabile». **Aperte una per una:**

| Riga | Verdetto |
|---|---|
| **Venere Parrucchieri** (Limbiate) | falso positivo: `webesteticabenessere.com` e `top10posti.it` sono portali. Resta senza sito |
| **Estetica Bottega del Massaggio** (Bovisio) | falso positivo su `123estetica.com`. **Chiude il dubbio dichiarato il 30 agosto**: nessun dominio suo risponde |
| **Chic Estetica** (Bovisio) | `chicestetica.it` è vivo ma è un centro di **Castellammare del Golfo**. Omonimo, quindi **gancio**: chi la cerca finisce in Sicilia |
| **La Nova Sedia** (Varedo) | `lanovasedia.it` c'è, **senza carrello** (niente woocommerce/shopify/checkout, controllato il 13/09). Riga e-commerce corretta |
| **Beba Evolution** (Villasanta) | ⚠️ **il sito ce l'ha**: `bebaevolution.it`, copyright 2022, WooCommerce dentro. È un **restyling**, non un «non vi trovo» |

Le altre 22 righe hanno in colonna la prova compatta con la data:
`[riverifica 13/09] nessun dominio suo risponde…`. Su DenkiShift e indagine la
riverifica non serve: quei segnali non dipendono dal sito.

⚠️ **Due righe su 27 non si aprono con «non vi trovo su internet»**: Beba
Evolution e La Nova Sedia. Se Giulia parte così, la chiamata è persa in cinque
secondi — è scritto dentro la loro casella note, in maiuscolo.

## Cosa resta dichiarato, e non è coperto

- ⬜ **I numeri hanno quattordici giorni** e nessuno è mai stato chiamato: le
  schede di Pagine Gialle invecchiano. Il primo «numero inesistente» non è un
  errore di lista, è la lista che ha l'età che ha.
- ⬜ **Pogliani Antonella** e **Mirale** (Limbiate) potrebbero essere la stessa
  attività. Nei CSV i numeri sono diversi (`02 9965232` e `02 9964408`): lo
  scopre la prima chiamata.
- ⬜ **Il blocco e-commerce è corto**: 3 righe contro le 27 che servirebbero.
  Qualificare col metro del carrello è lento, va aperto ogni sito.
- ⬜ `controlla-lista.py` **non ha girato**: pretende le colonne del banco DM
  (`Account IG`, `Esito verifica sito`) e queste sono liste da telefono. Il
  controllo sulle frasi copiate e sulle righe non verificate l'ho fatto
  leggendo le cinque righe marcate, non a macchina.

## Da dire a Giulia insieme ai file

1. **«Lei» sempre** → [[stile-comunicazione]].
2. **`Esito e Note Giulia` comincia con una delle sei parole** di
   [[metodo-liste]]: `Non risponde` · `Richiamare` · `Non è il decisore` ·
   `No` · `Troppo piccoli` · `Fissato incontro`. Senza il prefisso [[metriche]]
   non si conta.
3. **Zone nuove**: Groane (Limbiate, Varedo, Bovisio, Senago, Paderno,
   Garbagnate, Arese, Saronno) e Vimercatese (Vimercate, Concorezzo, Agrate,
   Arcore, Villasanta, Brugherio). Non sono i suoi comuni di sempre.
4. **L'indagine non si vende**: si porta al form.
5. **Sotto gli 8 dipendenti su DenkiShift si saluta** senza insistere.

## Collegamenti

[[2026-09-13-caller-fuori]] · [[2026-08-30-liste-gabriele-edoardo]] ·
[[ciclo-settimanale]] · [[metodo-liste]] · [[metriche]] ·
[[2026-08-30-verifica-sito-reale]] · [[gabriele-edoardo]] ·
[[stile-comunicazione]] · [[prodotti-e-listino]]
