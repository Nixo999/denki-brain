---
riga: 64 righe sul banco (65 nel file - Da Bassano è rimasta dentro come SCARTATO), tutte per l'account personale di Patrick, appese a lista-corren...
type: area
updated: 2026-09-09
source: claude
prodotto: siti-vetrina
canale: instagram
anello: 1-2
stato: pubblicata
---

# Lista Instagram — ristorazione, anelli 1 e 2, 9 settembre 2026

**64 righe sul banco** (65 nel file: Da Bassano è rimasta dentro come SCARTATO), tutte per l'account personale di Patrick, appese a
`lista-corrente.csv` con la colonna `Lista` valorizzata: sul banco stanno nella
pagina «Da contattare» insieme alle 22 dei cani, perché escono lo stesso giorno.
File: `2026-09-09-instagram-ristorazione-va-co-lc-bg.csv`.

Patrick ne ha chieste **70**. Sono 64 perché le sei che mancano non le ho
trovate pulite: il bacino dei comuni non ancora battuti si è svuotato prima del
numero, e una riga non verificata non entra ([[metodo-instagram]], passo 4).

| Provincia | Righe | Comuni |
|---|---|---|
| Varese | 25 | Busto Arsizio, Tradate, Somma Lombardo, Sesto Calende, Luino, Laveno Mombello, Cassano Magnago, Malnate, Cardano al Campo, Solbiate Arno, Porto Ceresio, Arcisate, Bisuschio, Besozzo, Angera |
| Lecco | 14 | Merate, Valmadrera, Mandello del Lario, Casatenovo, Calolziocorte, Brivio, Cesana Brianza, Costa Masnaga |
| Como | 13 | Erba, Fino Mornasco, Cernobbio, Bellagio, Inverigo, Lurago Marinone, Lomazzo, Menaggio, Lipomo, Lurate Caccivio, Faloppio |
| Bergamo | 12 | Bergamo (Città Alta e Borgo Palazzo), Treviglio, Seriate, Dalmine, Treviolo |

Segmenti dentro la ristorazione: 32 pizzerie, 14 fra ristoranti e osterie, 9
gelaterie e pasticcerie, 5 bar e vinerie, 2 alberghi con ristorante, 2 lounge.
È **lo stesso settore della lista dell'8 settembre**, spostato sui comuni che
quella lista non aveva toccato: là c'erano Como, Cantù, Varese, Saronno,
Gallarate, Lecco, Oggiono; qui il resto dei due anelli.

## Ogni riga è stata aperta

È la prima lista di ristorazione fatta col profilo davanti, come i cani di
stamattina: **112 profili letti** dal browser dell'app, sul Mac di Patrick, in
sola lettura. Per ognuna delle 65 righe la colonna «Esito verifica sito»
riporta la ricerca a mano per nome e comune, i portali che escono, e cosa c'è
in bio; poi lo script `verifica-sito.py` ha aggiunto la sua prova. **E ha
preso una riga che a me era sfuggita**: Da Bassano di Caravaggio ha
`pizzeriadabassano.it`, sito vero con telefono e indirizzo, che nelle SERP
lette a mano non compariva. Lo script ha indovinato il dominio dal nome: è il
motivo per cui passa dopo la lettura, non al posto. Follower e
bio sono di oggi, non «n.d.».

Cosa ha scartato la lettura:

- **17 handle morti** («Pagina non trovata»): fra gli altri `pizzeria_alsud`,
  `pizzeriadaattilio3.0`, `picnic_garlate`, `osteriadelsass.besozzo`,
  `locanda_delcastello`, `thevoodoo`, `pizzeria_40_missaglia`. Le SERP li
  danno ancora vivi.
- **una sessantina con sito vero e vivo**, fra cui Tigarba, Calma e Gesso,
  Villa Cocca, La Stadera, Asnigo, Harry's Bar, Autentiko, Tarantola, Plinio,
  Marascia, La Filanda, Scrocchia, San Vigilio, Morso, Maista, Da Mimmo,
  Gattopardo, Casa Grandate, Lido di Montorfano, Il Gallo, Vecchio Pozzo,
  Sartori, Do' Siciliano (`dosiciliano.it` in bio).
- **10 troppo piccoli**: sotto i 200 follower o con due post, come
  `pizzeria_al_cantuccio` (187, 2 post) e `pizzeria_ladolcepizza` (3 follower).
- **13 mai controllati** per esaurimento delle ricerche web di giornata
  (Zanica, Caravaggio, Porto Ceresio, Maccagno): restano nel sacco per la
  prossima lista.

## I ganci

| Gancio | Righe | Esempi |
|---|---|---|
| 1 nessun sito | 58 | il grosso: nelle SERP solo portali, in bio niente o Glovo, Telegram, allmylinks, un PDF su un dominio altrui |
| 4 link in bio rotto | 2 | Piazza Abba (`piazzaabbalareclame.it`) e MG Cavour (`ristorantebarcavour.it`), NXDOMAIN su Cloudflare |
| 5 piattaforma | 2 | O' Sarracino (Google Sites), Da Lino Seriate (res-menu) |
| 3 parcheggiato | 1 | Il Ristorante di Paolo, Menaggio: pagina di default del server. HappyCow lo dà chiuso, in scheda c'è l'avviso |
| 6 vecchio | 1 | La Scommessa, Arcisate: WordPress vivo, titolo «Just another WordPress site», telefono dentro |

**I siti generati dalle reti** (`pizzeria-<nome>-<comune>.it`, titolo «Pizzeria X
- Comune - Pizza», niente telefono del locale) compaiono su Doppio Zero,
Papillon, Da Aldo e Romeo: non sono del titolare, il gancio 1 resta vero e la
scheda lo dice, così Patrick non si fa fregare se il titolare lo cita.

## Trappole nuove

- **Il dominio in bio può essere di un altro.** `dosiciliano.it` è del locale
  di Pontirolo Nuovo (sito vivo, scartato); `do-siciliano.it` è una pagina
  generata. Stesso nome, un trattino di differenza, due verità opposte.
- **Al Sesto Gusto** di Sesto Calende ha un omonimo a Sesto San Giovanni con
  sito (`sestogustobistrot.it`): il sito è dell'altro.
- **Il sito che le SERP non mostrano.** Da Bassano: nessuna ricerca lo dava,
  il dominio `pizzeriadabassano.it` c'era. Quattro domini «indovinati» dallo
  script erano invece omonimi (la rivista Doppiozero, Tropp' Assaje di
  Alessandria, uno studio di architettura Verderosa, una Pizzeria Smile
  altrove): aperti e scritti in colonna.
- **De Vita** ad Angera: in bio «chiusi dal 6 al 15 settembre 2026». La scheda
  dice di scrivere dal 16; il banco non lo sa.
- **Douglas** di Bisuschio ha aperto a Varese il 4 settembre: è nell'anello 2
  per la sede storica, ma il profilo parla anche della nuova.

## Buchi dichiarati

- Lo script `verifica-sito.py` ha girato coi motori: dove DuckDuckGo ha
  risposto «0 risultati» la prova buona resta quella a mano scritta prima del
  tag.
- Le 6 righe che mancano a 70 e i 13 profili mai controllati sono il primo
  materiale della prossima lista di ristorazione, se ne serve un'altra.
- Il messaggio è ancora la versione C con «la bozza è già pronta»: la decisione
  dell'8 settembre ([[2026-09-08-test-dm-chiuso]]) chiede di riscriverla o di
  tenerla con uno screenshot, e non è ancora stato fatto.

## Collegamenti

[[metodo-instagram]] · [[2026-09-09-anello1-pet]] ·
[[2026-09-08-anello1-ristorazione]] · [[dm-instagram-vetrina]] ·
[[voce-denkicode]] · [[2026-09-08-test-dm-chiuso]] · [[generazione-lead]]
