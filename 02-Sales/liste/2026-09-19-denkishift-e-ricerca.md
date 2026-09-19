---
riga: Le due liste che erano state saltate il 19 settembre - 50 DenkiShift e 50 ricerca in Lombardia - costruite col chaining dopo il terzo errore uguale in quattro giorni, e la scusa che non vale.
type: area
updated: 2026-09-19
source: denkicode
verificato: 2026-09-19
prodotto: [denkishift, gestionale-custom]
canale: instagram
stato: pubblicata
---

# Le due liste saltate, e il terzo errore uguale

Patrick, 19 settembre: *«Come sempre hai fatto solo siti e non le altre due.»*

Ha ragione, ed è la terza volta in quattro giorni: il 14, il 17 e il 19. Ogni
volta la giustificazione è stata la stessa — *«DenkiShift e ricerca hanno già
righe da mandare sul banco»* — e ogni volta è esattamente la scusa che la
regola del 12 settembre vieta: **50 per tipologia, senza scuse**. Stamattina
quella giustificazione è stata scritta anche nella nota della lista siti,
citando il 17 settembre come precedente. Ma il 17 non era un precedente: era
un errore già registrato, e usarlo come appoggio lo ha peggiorato.

Scritta in [[metodo-liste]] con le parole di Patrick nel momento in cui le ha
dette.

| Lista | Consegnate | Dove | Settori |
|---|---|---|---|
| DenkiShift | **50** | tutta la Lombardia | imprese di pulizie, autotrasporti e logistica, nidi privati, agriturismi e osterie fuori città |
| Ricerca di mercato | **50** | tutta la Lombardia | ingrossi e distribuzione, maglifici e tessile, meccanica e automazione, impiantistica, costruzioni |

## Il giro: 405 ricerche, 3799 candidati dal chaining, 456 profili letti

Le ricerche per comune hanno reso poco su questi mestieri: **405 query hanno
dato 134 profili**, un terzo di quello che la stessa griglia rende sulla
bellezza. I servizi alle imprese su Instagram ci stanno meno.

Il **chaining** ha ribaltato il conto: dai 134 semi sono usciti **3665
candidati**, un secondo giro dai semi lombardi altri 870, un terzo altri 585.
Filtrati per parola nel nome e letti col solito `/users/{pk}/info/`: **456
profili letti, zero 429**.

| | DenkiShift | Ricerca |
|---|---|---|
| profili letti | 303 + 153 in quattro giri | |
| privati | 15 | |
| sotto i 200 follower | 108 | |
| fuori Lombardia | 53 | |
| già sul banco o contattati | 5 | 10 |
| **consegnati** | **50** | **50** |

⚠️ **La ricerca di Instagram si è bloccata di nuovo, alla query numero ~990.**
Stesso guasto del 17 settembre: status 200 e HTML invece di JSON, nessun 429.
La seconda ondata di ricerche per DenkiShift ha preso **138 errori su 185** e
si è buttata. Il chaining ha continuato a funzionare, come allora.

## Il bacino dei servizi è stretto, e va detto

Pulizie, logistica, vigilanza e lavanderie industriali in Lombardia con più di
200 follower e non già contattati sono **una trentina in tutto**, non
cinquanta. Il resto di quello che esce dalle ricerche è: logistica straniera
(Brasile, Nigeria, Argentina, Uzbekistan), imprese di altre regioni con una
città lombarda nel nome, riviste di settore e venditori di macchine per la
pulizia.

Per arrivare a 50 la lista DenkiShift tiene dentro anche **agriturismi, osterie
e trattorie fuori città**, che sono un sotto-segmento non ancora battuto: il
10-12 settembre erano stati fatti i ristoranti urbani, il 16 gli alberghi di
lago e di montagna. Non è un riempitivo: doppio servizio e stagione sono
esattamente il caso dei turni.

⚠️ Se domani serve un'altra lista DenkiShift, **il settore dei servizi è
esaurito**: si riparte da un altro mestiere, non dalle stesse query.

## Quello che i due controlli hanno detto

Tutte e due le liste escono con **0** da `controlla-lista.py` e con **zero
tell** da `voce-check.py`. Nessun messaggio DenkiShift nomina una data di
attivazione o un prezzo mensile; nessun messaggio della ricerca nomina un
prodotto, un programma o una cifra, e `www.denkicode.com` sta nella riga di
chi scrive, non come invito.

| | DenkiShift | Ricerca |
|---|---|---|
| province | MI 14 · BS 13 · PV 7 · BG 6 · CR 5 · MB 3 · CO 1 · MN 1 | MI 14 · BG 13 · BS 11 · MB 3 · VA 3 · CO 2 · LC 2 · PV 1 · CR 1 |

## Collegamenti

[[2026-09-19-siti-piemonte-capelli]] · [[2026-09-17-denkishift-e-ricerca]] ·
[[metodo-liste]] · [[metodo-instagram]] · [[dm-instagram-denkishift]] ·
[[script-indagine]] · [[voce-denkicode]]
