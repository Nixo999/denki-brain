---
type: area
updated: 2026-09-07
source: claude
prodotto: siti-vetrina
canale: instagram
anello: ticino
stato: pubblicata
---

# Liste Instagram — Ticino, 7 settembre 2026 (due account)

**Due liste, una per account**, perché dal 7 settembre il
[banco DM](../strumenti/banco-dm.html) ha due postazioni: il profilo personale
di Patrick e quello di DenkiCode ([[2026-09-07-due-account-dm]]).

| Lista | Account | Zona | Righe | File |
|---|---|---|---|---|
| Patrick, primo giro | profilo personale | Sotto Ceneri: Lugano, Chiasso, Mendrisio | 8 | `2026-09-07-instagram-ticino-patrick.csv` |
| Patrick, secondo giro | profilo personale | Sotto Ceneri allargato: Lugano e quartieri, Massagno, Paradiso, Vezia, Caslano, Tesserete, Mendrisiotto | 34 | `2026-09-07-instagram-ticino-patrick-2.csv` |
| Patrick, terzo giro | profilo personale | Sotto Ceneri, **campo nuovo: ristorazione e locali** | 60 | `2026-09-07-instagram-ticino-ristorazione.csv` |
| DenkiCode | account aziendale | Sopra Ceneri: Bellinzona, Locarno, Ascona | 9 | `2026-09-07-instagram-ticino-denkicode.csv` → pubblicata come `lista-denkicode.csv` |

**La divisione è geografica e non si incrocia**: un'attività riceve un
messaggio solo, da un account solo. Il controllo incrociato è passato su tutte
e 454 le handle già toccate e sulle due liste fra loro: zero duplicati.

## Perché sono corte

Richiesta di Patrick: clienti dal lato svizzero. **Il Ticino non è la Brianza.**
Ventotto profili esaminati, **diciassette hanno un dominio proprio e vivo**: il
39% è passato, contro il 12 su 14 senza sito che aveva dato la Lombardia
([[2026-08-30-verifica-siti-giulia]]). Chi non ha il sito qui ha comunque
Fresha o Treatwell, e chi ha il sito ce l'ha fatto da un'agenzia locale
(ticinoWEB, Swiss Web Studio, Antherica): il mercato è servito.

Le diciassette scartate non sono in nessun file: hanno un sito vero, il
messaggio direbbe una bugia alla prima riga.

## Il secondo giro, del pomeriggio — 34 righe

Chieste da Patrick: **«devo mandare 65 DM oggi e devono essere tutti della
Svizzera italiana»**. Ne sono uscite **34**, appese a `lista-corrente.csv`, che
passa da 153 a 187 righe e da 76 a 110 da mandare.

**Con le 8 del mattino, sul suo account oggi ci sono 42 righe svizzere, non
65.** Il numero non è una scelta: è quello che ha superato la verifica.
Novantacinque profili e attività guardati, trentaquattro passati — **il 36%**,
in linea col 39% del mattino. Il resto ha un sito vero, e a chi ha un sito vero
il messaggio direbbe una bugia nella prima riga.

Le zone: **18 righe Lugano città** (più Cassarate, Paradiso, Massagno, Vezia),
poi Caslano, Tesserete, e **11 nel Mendrisiotto-Chiassese** (Chiasso 6,
Balerna 2, Mendrisio, Novazzano). Sopra Ceneri mai toccato: è di DenkiCode
([[2026-09-07-due-account-dm]]).

I ganci: 21 senza sito, 7 su piattaforma (Fresha, Treatwell, Etsy,
hairlovers.style, la scheda dentro il sito del centro commerciale), 3 domini
morti, 2 fermi su una pagina di servizio, 1 segnaposto.

### Le tre cose imparate qui

- **Il resolver DNS di questa macchina mente, e per poco non ha prodotto cinque
  bugie.** `dig` e `curl` dalla sandbox danno «dominio inesistente» anche per
  domini vivissimi (`treatwell.ch`, `sirmarcus.ch`). Da qui in avanti ogni
  verdetto «dominio morto» si prende da **due resolver DoH** (Cloudflare e
  Google) e la pagina si scarica forzando l'IP risolto. Lo script sta in
  `scratchpad/ticino/check.py` del giorno, la regola vale sempre.
- **L'handle che sembra un dominio non è il dominio.** `@monsterhousetattoo.ch`
  (Lugano, 14k follower) sembrava perfetto: `monsterhousetattoo.ch` non esiste.
  Solo che il suo sito è `monsterhouse.ch`, vivo e curato. Riga scartata. Il
  nome del profilo non è una verifica.
- **Due profili, un negozio solo: succede spesso.** `@lugano.barbershop` (1194)
  e `@lvgano_barbershop` (465) sono lo stesso barbiere in Corso Pestalozzi 14;
  `@personal_hair_stylist_lugano` (1316) e `@phslugano` sono lo stesso salone di
  via Canova. In lista ne è entrato uno solo, e nella colonna `Scheda` c'è
  scritto qual è il gemello.

### Corretta una riga del mattino

`@angolodiros_mendrisio` diceva «è una pagina su Wix». Oggi
`esteticaros5.wixsite.com` risponde **404**: la pagina non c'è più. Riga
riscritta da gancio 5 a gancio 2, in tutte e due i file. Il fatto è più forte di
prima, ma andava detto giusto.

### Chi è stato scartato, e perché

Trentacinque nomi con **un sito vero e vivo**, fra cui Nail Factory, Jenny
Nails, Elegance Beauty, Estetica Dream, Portofino's, Estetica Lugano Sagl, Oro
di Kinabalu, Salone by Franco, Dugoni, PrimaClasse, Alchimie, Borgo d'Oro, Be
Blonde, Estetica Fashion, Caracalla, Élite, Estetica Orchidea, Silvia Gasperi,
Sir Marcus, Matt's, Old Skull, Barberia L'Artisan, MisterX, Monster House,
Kevin Pomponi, Crazy for Art, Pensieri Permanenti, Inferno Ink, Centro Laser
Ticino, Muha Barbershop, ByLilla, Me-style, Sirienne Margot, Êtrebel.

Più le **trappole di geografia**, che su queste ricerche sono continue: Ponte
Chiasso e Lavena Ponte Tresa sono Italia, `@esteticaparadiso` è Collegno,
`@puertobellaok` è Buenos Aires, `@barberiasteri` è Roma, `@ivan.hairlab` è
Recanati. Un comune che suona ticinese non è un comune ticinese.

### Buchi dichiarati, secondo giro

- **I follower ci sono su 8 righe su 34.** Instagram non si apre da qui: dove
  non li ho letti c'è `n.d.`.
- **Nessun profilo aperto**, come al mattino: handle, indirizzi e telefoni
  vengono dalle SERP. `source: claude`, si guarda il profilo prima di scrivere.
- **Il Mendrisiotto minore resta vuoto**: Coldrerio, Rancate, Genestrerio,
  Ligornetto, Stabio, Vacallo, Morbio, Castel San Pietro non hanno restituito
  niente di verificabile. E i comuni piccoli del Luganese (Melide, Bissone,
  Agno, Bioggio, Manno, Monteceneri) danno solo directory: se il Ticino va
  continuato, quella fascia va pescata da `local.ch` e `ticinodigitale`, non
  dalle ricerche su Instagram.

## Il terzo giro — un campo nuovo: ristorazione e locali

Chiesto da Patrick: **«trova altri sessantacinque di un altro campo molto
convertibile, sempre nella Svizzera italiana»**. Il campo scelto è la
**ristorazione**: ristoranti, pizzerie, grotti, bar, gelaterie, pasticcerie,
take-away e food truck. **Sessanta righe**, appese a `lista-corrente.csv`, che
passa da 187 a 247 e da 110 a 170 da mandare. Sull'account di Patrick le righe
svizzere di oggi diventano **102**.

⚠️ **Sessanta, non sessantacinque.** Le altre cinque non esistono: sono state
esaminate circa centosessanta attività e queste sono quelle che hanno superato
la verifica. Il resto ha un sito vero.

### Perché questo campo, e cosa vale davvero

- **La densità.** Il solo distretto di Lugano ha più di trecentocinquanta
  esercizi pubblici: è l'unico segmento del Sotto Ceneri dove si possono fare
  sessanta righe senza uscire dai comuni già battuti.
- **Le foto ce le hanno già**, ed è il perno del messaggio: la bozza si guarda
  in cinque secondi perché dentro ci sono i loro piatti.
- **Il gancio è controllabile dal cliente in un istante**: cerca il proprio
  nome su Google e vede quello che vede il cliente.
- **Il tell del canale**: 52 righe su 60 sono «nessun sito». Nella ristorazione
  ticinese il sito ce l'hanno i ristoranti gastronomici e le catene; bar,
  gelaterie, take-away e pizzerie di quartiere vivono su Instagram e sui
  portali di consegna.

### I ganci, uno per uno

| Gancio | Righe | Esempio |
|---|---|---|
| 1 · nessun sito | 52 | Pub Number One, settemila follower e nessun dominio |
| 5 · su piattaforma | 4 | Pizza Style sta su Menustic, JO PIZZA su Grubbio, Acqua & Farina su Smood e Uber Eats, Biblio Cafè su Blogspot |
| 2 · dominio morto | 2 | `lapasticceriadiflavio.com` e `gelateriaparadiso.ch` non hanno più DNS |
| 6 · sito mai finito | 1 | Grotto dei Pescatori: sito Wix col titolo ancora «My Site 1» |
| 3 · sito rotto | 1 | Icon Sushi: in https risponde 503 con un certificato che non è suo |

**Il caso Gelateria Paradiso vale da solo il giro**: l'account si chiama
`@gelateriaparadiso.ch`, e quel dominio non esiste. Il nome del profilo promette
un sito che non c'è.

### Cosa è stato scartato

Una quarantina di nomi con **un sito vero e vivo** — Basara, Ciani, Vitti,
Roots, Trinity, Class Café, Caffè Milano, Speedy Pizza, Alchimia, 9CENTO,
Locanda dei Mulini, Be Blonde, La Cicchetteria, Grotto Figini, Golosone,
Vedeggio Bistrot, Danesi, La Colombina, Mustis, Al Faro, Locanda Gandriese,
Kin-D Thai, Pinsa&Pokè, Maui Poke, Grotto del Mulino, Osteria BarAtto,
Ristorante Stazione Balerna, Ristorante Fresco, Ristorante del Sole, Negio Food.
Più i **gruppi**, che il sito ce l'hanno a livello di casa madre: Spaghetti
Gastro Group (Martini Lounge, Birrificio di Bioggio), Lanchetta (Eight Sushi).

E le trappole di geografia, che in questo campo sono peggio che nell'estetica:
`@pizzeria_chiasso_brus` è **Brus, in Serbia**; `@ristoranteilchiasso1973` è
**Capoliveri, all'Elba**; `@esteticaparadiso` era Collegno; Grotto America è a
Ponte Brolla, cioè Sopra Ceneri, cioè di DenkiCode; Grotto Bagat e Consoli
Massimo sono a Lavena Ponte Tresa, cioè Italia. **Un nome ticinese non è un
indirizzo ticinese.**

### Da sapere prima di mandare

- ⚠️ **Due coppie di profili gemelli**: `@gelateriavenetalugano` e
  `@gelateria_veneta_lugano_` sono la stessa gelateria di via al Chioso;
  `@grottodelmulinomorbio` e `@grottodelmulino_saceba_` sono lo stesso grotto
  (fuori lista, il sito ce l'ha). Se ne scrive a uno solo.
- **`@lugano_fruangen` è fuori** per la regola dei 200 follower: ne ha 166.
- I follower stanno solo dove la ricerca li ha detti: 4 righe su 60.
- Nessun profilo aperto su Instagram: `source: claude`, si guarda il profilo
  prima di scrivere.

## Il messaggio è diverso, e non solo nella firma

Tutte le righe arrivano con la colonna `Messaggio` **già scritta**, quindi il
banco non genera niente e non c'è rischio che parta il testo dell'account
sbagliato. Due differenze rispetto al testo lombardo di [[dm-instagram-vetrina]]:

- **Dall'account DenkiCode si scrive al plurale** («le scrive Patrick della
  DenkiCode», «l'abbiamo fatta noi»), la firma resta di una persona. Un DM
  aziendale senza nessuno dietro si legge come un annuncio.
- **Sparisce l'ancora di prezzo.** «Poche centinaia di euro» in Ticino è un
  numero che squalifica: là un sito vetrina si paga in migliaia di franchi.
  Resta il disinnesco («non si parla di migliaia di franchi»), senza cifra.

## Da sapere prima di mandare

- ⚠️ **L'account DenkiCode è nuovo: il tetto è 15, non 65.** La rampa di
  [[metodo-instagram]] vale in pieno, si sale di dieci al giorno alzando
  `tetto` a mano nel banco. Il 65 è una misura fatta sul profilo di Patrick e
  non si eredita ([[2026-09-03-tetto-dm-65]]).
- ⚠️ **@momobarbershop2021 ha un gemello**, `@momobarber67`: stesso negozio,
  due handle. Va guardato quale è vivo prima di scrivere.
- I follower stanno solo dove la ricerca li ha detti: dove c'è `n.d.` il
  profilo non è stato aperto, e sotto i 200 follower la riga andrebbe tolta.
- **Pubblicate tutte e due**, il 7 settembre: le 8 righe di Patrick sono state
  **appese** a `lista-corrente.csv`, che passa da 145 a 153 righe e da 68 a 76
  da mandare. Appese e non sostituite: le date degli invii lombardi restano, e
  con esse i 75 recuperi che maturano mercoledì 9 settembre.

## Buchi dichiarati

- Nessun profilo è stato aperto su Instagram: handle, follower e attività
  vengono dalle SERP. `source: claude`, da verificare aprendo il profilo prima
  di scrivere, come dice il passo 2 di [[metodo-instagram]].
- Il Mendrisiotto e il Chiassese hanno dato due righe in tutto: la ricerca per
  quei comuni restituisce quasi solo directory. Se il Ticino va continuato,
  quella zona va pescata con un metodo diverso.

## Collegamenti

[[metodo-instagram]] · [[dm-instagram-vetrina]] · [[2026-09-07-due-account-dm]] ·
[[2026-09-03-tetto-dm-65]] · [[2026-09-05-instagram-bg-va]] · [[voce-denkicode]]
