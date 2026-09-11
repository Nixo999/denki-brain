---
riga: Le tre liste dell'11 settembre - 43 siti e 43 DenkiShift sulla Brianza mai battuta, piu' 9 di ricerca di mercato.
type: area
updated: 2026-09-11
source: claude
verificato: 2026-09-11
prodotto: [siti-vetrina, denkishift, gestionale-custom]
canale: instagram
anello: 1
stato: pubblicata
---

# Le tre liste dell'11 settembre 2026 — la Brianza, che non era mai stata toccata

Primo giro completo di `/banco`, dopo che Patrick ha detto che il banco era
vuoto: *«non ci sono nuovi siti da contattare, i 225 sotto li ho già
contattati, 0 persone da contattare per denkishift e solo 9 per la ricerca»*.

| Lista | File | Righe |
|---|---|---|
| Siti vetrina | `2026-09-11-instagram-siti-brianza.csv` | **43** |
| DenkiShift | `2026-09-11-instagram-denkishift-mb-va-co-lc.csv` | **43** |
| Ricerca di mercato | `2026-09-11-instagram-ricerca-mb-va-co.csv` | **9** |

## Prima di tutto: il banco mentiva, e adesso no

Sul banco risultavano **292 righe siti da mandare**. Erano false: 225 venivano
dalle liste di inizio settembre, senza data di invio nel file perché **gli
invii dal 4 al 7 settembre non sono mai stati salvati nel vault**, e Patrick a
quella gente aveva già scritto.

Sono state spostate in `archivio-2026-09-11-contattati-senza-data.csv`, con
l'esito scritto in chiaro. **Il conto del banco adesso è vero.** Era anche il
motivo per cui la sessione precedente aveva deciso di non costruire la lista
siti: un numero gonfiato, e una decisione sbagliata presa sopra.

## La zona: la Brianza, mai battuta

Le liste di settembre avevano pettinato Varese, Como, Lecco, Bergamo, Cantù,
Erba, Treviglio, Gallarate, Busto, Saronno. **La Brianza no**, ed è casa
nostra: Seveso, Meda, Seregno, Desio, Lissone, Giussano, Carate, Barlassina,
Cesano Maderno, Bovisio, Varedo, Misinto, Nova Milanese, Muggiò, Biassono,
Besana, Arcore, Vimercate, Agrate, Concorezzo, Brugherio, Usmate, Briosco.

**157 profili trovati, nessuno dei quali era già nel vault.** Zero
sovrapposizioni su 509 handle già visti: la zona era intonsa.

## Siti — 43 righe da 157 profili

Filtro: vivi (almeno 200 follower e 10 post), non privati, in zona. Restano 84.
Poi `verifica-sito.py` su 67, che ha girato **cinquanta minuti** e ha trovato:

| | righe |
|---|---|
| **sito vivo col loro nome** → scartate | 10 |
| **PROBABILE SITO** da aprire a mano → fuori | 12 |
| dominio indovinato vivo ma **di un'altra attività** (Vero Beach, Svezia, un market americano) → tenute con la prova scritta | 4 |
| dominio indovinato vivo e **probabilmente loro** → fuori | 2 |
| **tenute** | **43** |

Ganci: 28 senza nessun sito, 11 su piattaforma (Fresha o Treatwell, **e il
messaggio la nomina**), 4 con un dominio parcheggiato.

**Il gancio è quello nuovo di Patrick**: «la bozza del suo sito è già pronta»,
non «gliela preparo» → [[stile-comunicazione]]. Tu alle onicotecniche che si
presentano col nome, Lei ai centri.

## DenkiShift — 43 righe da 98 profili

Criterio diverso: **squadra a turni, il sito non conta**. Alberghi del lago e
di città, ristoranti e pizzerie con doppio servizio, pasticcerie con
laboratorio, palestre.

Dentro: **11 alberghi** (Bis e Art Hotel a Varese, Capolago, Palace Grand Hotel
del 1913, Royal Falcone e de la Ville a Monza, Pioppeto a Saronno, Alberi e
Bellavista sul lago di Lecco, Mímesis 11 e Posta Moltrasio sul Como), **16 fra
ristoranti e pizzerie** (Eurotaverna con la sala concerti, Casa Cuomo, Boom con
l'area bimbi, Bistrot Cattaneo con tre reparti, Matura, Fiorillo aperto 7/7,
Unico Cantù che la squadra la mostra in evidenza), **5 pasticcerie** (Passerini
dal 1919 con quattro sedi, Lievito con undici ore al giorno per sette giorni,
Dolci con il catering), **5 palestre**, un agriturismo con azienda agricola.

Ogni messaggio parte da **un fatto vero letto sul profilo**: gli orari
dichiarati in bio, le quattro sedi, la sala concerti, la storia in evidenza
sulla squadra. Nessuna data di attivazione, nessun prezzo al mese, nessun link.

Scartati: 13 fuori zona (Paraguay, Brasile, Russia, Val di Fassa, Bari, Marche,
Toscana, Sicilia), quelli sotto i 400 follower, un profilo «generato dall'IA».

## Ricerca di mercato — 9 righe, e il motivo

Restano le 9 di prima. **La ricerca di Instagram non trova gli artigiani per
comune**: venti query mirate hanno dato un solo profilo nuovo, perché una
carrozzeria si chiama col cognome del titolare e non col nome del paese. Il
dettaglio in [[2026-09-11-ricerca-mb-va-co]].

## I controlli

`controlla-lista.py` esce **ok** su tutte e tre. `voce-check.py`: **zero tell**
su 43 messaggi siti, **zero** su 43 DenkiShift, zero sui 9 della ricerca a
parte il link, che lì è voluto.

## Il tetto giornaliero non c'è più

Patrick: **«togli il limite giornaliero»**. Tolto dal banco, da
`stato-banco.py` e da [[metodo-instagram]]. Restano il contatore di quanti ne
sono partiti oggi e quello dell'ultima ora, che sono misure e non freni. Il
fatto misurato resta: 75 DM in una sera non hanno fatto scattare blocchi, e
sopra quel numero non c'è nessuna misura.

## Cosa manca

⬜ Le liste sono da **43 e 43**, non da 50. Mancano 14 righe: il bacino della
Brianza sopra i 200 follower si è esaurito lì, e allargare vuol dire un anello
in più o un settore nuovo.
⬜ **12 righe siti con un PROBABILE SITO** sono rimaste fuori: si aprono a mano
e la metà probabilmente rientra.
⬜ La resa dei due segmenti nuovi è da misurare.

## Collegamenti

[[metodo-instagram]] · [[metodo-liste]] · [[dm-instagram-vetrina]] ·
[[dm-instagram-denkishift]] · [[2026-09-11-ricerca-mb-va-co]] ·
[[2026-09-11-comando-banco]] · [[stile-comunicazione]] · [[generazione-lead]]
