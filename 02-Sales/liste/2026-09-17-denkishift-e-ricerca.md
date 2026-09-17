---
riga: Le due liste che mancavano al 17 settembre - 50 DenkiShift e 50 ricerca di mercato in Lombardia - costruite col chaining di Instagram dopo che l'endpoint di ricerca si e' bloccato, e il difetto del banco che le faceva sembrare vuote.
type: area
updated: 2026-09-17
source: denkicode
verificato: 2026-09-17
prodotto: [denkishift, gestionale-custom]
canale: instagram
stato: pubblicata
---

# Le due liste che mancavano, e la regola che era gia' scritta

Patrick, 17 settembre: *«guarda meglio, ricerca e denkishift non hanno righe 1,
e 2 ci siamo già detti che se faccio quel comando tu mi fai 150 lead 50 per
tipologia no scuse»*. La regola sta in [[metodo-liste]], scritta il 14 e
ripetuta oggi. **Secondo errore uguale in quattro giorni.**

| Lista | Consegnate | Dove | Settori |
|---|---|---|---|
| DenkiShift | **50** | tutta la Lombardia | cooperative sociali, RSA e comunita', gastronomie e macellerie con laboratorio, pasticcerie e panifici, trasporto sanitario, centri clinici |
| Ricerca di mercato | **50** | tutta la Lombardia | stampa e serigrafia, packaging e cartotecnica, carpenteria e automazione, antincendio, ponteggi, caseifici, edilizia |

## «Non hanno righe» era vero, e non era colpa dei dati

I CSV avevano 50 righe DenkiShift e 51 ricerca da mandare, tutte del 13-14
settembre. **Sul banco non si vedevano.** Il motivo sta in `banco-dm.html`: la
pagina di un prodotto calcola **il giorno piu' recente fra le liste di quel
prodotto** e mostra in pagina solo quelle; il resto va sotto, chiuso.

Per DenkiShift e ricerca il giorno piu' recente era il 16, e le righe del 16
Patrick le aveva **gia' mandate tutte**. Risultato: pagina vuota, con cento
righe buone nascoste nel cassetto.

⚠️ **Conseguenza operativa, e conferma della regola di Patrick.** Il banco e'
costruito per lavorare sulla lista del giorno. Se un prodotto non ha la lista
di oggi, quel prodotto per Patrick **non esiste**. Non c'e' modo di «riciclare»
le righe vecchie parlandone: o si consegnano 50 righe nuove per tipologia, o
quella pagina resta vuota.

Verificato anche il contrario: nessuno dei 107 handle fermi sul banco ha un
thread nella posta di Instagram (1200 conversazioni lette). Quei DM non erano
partiti: le righe erano vere, era il banco a non mostrarle.

## L'endpoint di ricerca si e' bloccato a meta' lavoro

Dopo oltre mille query in una giornata,
`/web/search/topsearch/?context=blended&query=…` ha smesso di rispondere JSON e
ha iniziato a restituire **la pagina HTML di Instagram**, status 200. Nessun
429: sparisce solo il campo `users`. Le prime 1030 query di oggi (410 per la
lista siti, 620 per queste due) sono passate; dalla 1031 in poi, niente.

> [!tip] Quando la ricerca si blocca, il chaining no
> `GET /api/v1/discover/chaining/?target_id=<pk>` restituisce **fino a 36
> account simili** a un profilo dato, e ha continuato a funzionare quando la
> ricerca era gia' morta. Da 46 semi in target sono usciti **1885 candidati**,
> da un secondo giro su quelli buoni altri **1258**. Filtrati per parola nel
> nome, letti col solito `/users/{pk}/info/`, hanno dato tutto il bacino delle
> due liste.
>
> **E' il modo migliore di cercare, non il piano B**: il chaining parte da
> un'azienda giusta e restituisce aziende dello stesso mestiere, mentre la
> ricerca per comune restituisce chiunque abbia quella parola nel nome.

## Le query per comune sono state uno spreco

410 ricerche «settore + comune» hanno prodotto 388 profili letti e **49
pertinenti**. Il rumore ha una forma prevedibile e oggi era grottesco:

- **«rsa <comune>»** pesca *Rosa*, *Rosario*, *Rosalinda*: la sigla e' dentro
  decine di nomi propri. Su 215 candidati, i target veri erano una manciata.
- **«rifugio <comune>»** pesca i **canili** (Canile Rifugio di Brescia, Parco
  Canile di Milano) e i rifugi antispecisti.
- **«gastronomia como»** pesca un programma TV delle Canarie, **«rsa crema»**
  una gelateria di Santa Rosa in Brasile, **«carpenteria como»** una ditta di
  alluminio messicana.

⚠️ **E i settori erano gia' battuti.** RSA, cooperative sociali, poliambulatori
e panifici li aveva fatti il **13 settembre**; vigilanza, lavanderie e
pasticcerie il **16**. L'ho scoperto a giro finito, leggendo i CSV vecchi
invece di leggerli prima. Gli handle sono nuovi e le righe valgono, ma mezz'ora
e' andata.

## Quello che e' rimasto fuori

- **Catene e filiali**: Rosa Grand Milano (Starhotels), la mensa di Banca
  Intesa (gruppo Pellegrini).
- **Fuori Lombardia per il nome**: Caseificio Savarese (Vico Equense), Le
  Leccornie (Montecchio Emilia), tre gastronomie brasiliane.
- **Non sono aziende**: la fiera *Lamiera* a Rho, *Print4All*, gli Scavi di
  Nora dell'Universita' di Milano, un'accademia tessile, due profili di corsi
  di cucito.
- **Enti senza turni**: due fondazioni culturali e una che assegna
  appartamenti.
- **Undici handle erano gia' in `contattati.csv`** e sono stati sostituiti uno
  per uno: sei nella lista DenkiShift, tre nella ricerca, piu' due scoperti al
  secondo giro di `controlla-lista.py`.

## Controlli

| | DenkiShift | Ricerca |
|---|---|---|
| `voce-check.py` | 3 tell, riscritti, poi **0** | 15 tell, riscritti, poi **0** |
| `controlla-lista.py` | tre passaggi, poi **0** | due passaggi, poi **0** |

I quindici tell della ricerca venivano tutti dalla stessa cucitura: il
connettivo «, e» del modulo piu' due «e» nella frase specifica facevano la
catena di tre. Risolto con due varianti dell'attacco, scelte a seconda di
quante «e» ha la frase.

## Collegamenti

[[metodo-liste]] · [[metodo-instagram]] · [[2026-09-17-siti-piemonte]] ·
[[2026-09-14-denkishift-e-ricerca]] · [[dm-instagram-denkishift]] ·
[[script-indagine]] · [[denkishift]]
