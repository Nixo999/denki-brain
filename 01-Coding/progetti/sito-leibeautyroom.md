---
type: progetto
riga: Bozza sito per Lei Beauty Room, centro estetico a Torino Cavoretto - materiale raccolto dal profilo (5 foto reali, tutte grafiche di marketing/stock, zero foto vere del locale), repo vuoto creato, in attesa di direzione e costruzione.
status: attivo
client: lei-beauty-room
stack: html-css-js
started: 2026-09-24
deadline:
updated: 2026-09-24
source: claude
verificato: 2026-09-24
tags: [sito, bozza, estetica, torino, cavoretto, instagram]
---

# Sito Lei Beauty Room — bozza, Torino Cavoretto

Cliente: [[lei-beauty-room]]. Cartella `~/lavoro/leibeautyroom-site`, repo git
locale inizializzata (`nuovo-sito.py`), **non ancora su GitHub e non
pubblicata** — lo fa chi verifica alla fine. Processo: [[processo-siti]].

## Materiale, verificato il 24/09

**Profilo**: `@lei_beauty_room_`, nome mostrato «LEI BEAUTY ROOM | TORINO
(CAVORETTO)», 671 follower, 131 seguiti, 82 post (`og:description`, curl
24/09). Bio verbatim: «Il tuo centro estetico by @tatta777 🇺🇦 / ~ Trattamenti
viso e corpo / ~ Manicure & Pedicure / ~ Epilazione laser / Indirizzo: 📍Via
alla Parrocchia 4/c Torino».

**Chi è**: la titolare si chiama **Tania** (confermato da torinoggi.it, vedi
sotto; il tag `@tatta777` in bio è coerente col nome). Nelle recensioni Google
compare anche **Anya**, seconda operatrice — è quasi certamente l'account
taggato nei post `@_annzh_` («AnnZh | nails & mood»), che spiega perché post e
reel di quell'account appaiono nella griglia di Lei Beauty Room.

**Apertura**: articolo **Torino Oggi, 23/10/2025**, «Cavoretto: Lei Beauty
Room e Petit Cafè tra benessere e gusto» (letto per intero con WebFetch,
24/09). Tania: «Vi invitiamo di venire a provare e di trovare benessere nel
nostro centro estetico» (citazione riportata dall'articolo). Accanto, **Petit
Cafè** gestito da Olga: i due locali formano un polo benessere+ristorazione a
Cavoretto. Inaugurazione festeggiata con apericena. Coerente con la storia in
evidenza **«Inaugurazione»** sul profilo.

**Servizi, con le loro parole** (bio + caption dei post): trattamenti viso e
corpo, manicure e pedicure, epilazione laser. Dalle storie in evidenza (titoli
soli, contenuto non leggibile senza login): Manicure, Massaggio, Prima/dopo,
Nostri clienti, Skin care, Pedicure, LISTINO, Laminazione, KOBIDO. **KOBIDO**
(massaggio viso giapponese) e **Laminazione** (ciglia/sopracciglia) sono gli
unici due servizi che non stanno in bio: si sa solo che esistono, non i
dettagli.

**Marchi usati**: **Juliette Armand** («The Personal Professional Skincare»),
linea **Elements Caviar** — unico marchio verificato, dal post del 19/06 sulla
«Terapia nutriente al caviale».

**Google Maps** (letto nel browser, 24/09): **5,0 su 16 recensioni**. Indirizzo
confermato «Via alla Parrocchia, 4, 10133 Torino TO». Telefono **392 969
2727** (coincide con la lista). Tre frasi letterali dal riepilogo:
- «Tutto veloce, curato e con un'atmosfera super rilassante.»
- «Le ragazze sono davvero preparate e molto gentili. Consigliatissimo!»
- «Ti fa sentire subito a tuo agio e lavora con tanta cura e passione.»

Recensione integrale di Loredana Ligori (3 settimane fa): «Il centro estetico
più accogliente e serio che mi sia mai capitato di trovare. Tanya e Anya sono
tanto gentili quanto professionali, il locale è bellissimo e curato in ogni
dettaglio, i servizi offerti sono tanti e completi e la loro disponibilità è
massima. Consigliatissimo!» — è la fonte del nome **Anya**.

Recensione di Sabrina Torchio (9 mesi fa): «Posto incredibile, le ragazze sono
eccezionali e bravissime, il negozio è una piccola bomboniera, curata nei
minimi dettagli! Prezzi super onesti per quanto sono brave e professionali.»
— nessun numero, solo il giudizio sul prezzo.

**Orario**: solo un dato certo, letto sulla scheda Google Maps il 24/09 —
«Chiuso · Apre ven alle ore 09» (24/09 è un giovedì). L'orario completo della
settimana non è stato aperto (l'interazione di click sulla scheda oraria non è
riuscita in sessione): `TODO` orario intero.

**leibeautyroom.it**: verificato con `curl` il 24/09 — risponde 200 su HTTP,
pagina Aruba con testo «il dominio è già registrato», nessun contenuto reale.
Confermato parcheggiato, non è il loro sito. Su HTTPS il TLS handshake cade
(`Recv failure: Connection reset by peer`).

**Facebook**: cercato con WebSearch, nessuna pagina Facebook riconducibile a
Lei Beauty Room trovata (solo omonimi in altre città). Non c'è, o non è
indicizzata.

**Linguaggio nei post**: registro misto. I tre post fotografici scaricabili
sono tutti **contenuti di marketing generico** (vedi sotto), non parole
proprie salvo le didascalie. Le didascalie osservate: hashtag tecnici uniti
senza spazi («onicotecnicaTorino#UnghiegelTorino#Ricostruzione
unghieTorino,#semipermanenterinforzatoTorino#Nail ArtistTorino») e un post
educativo in prima persona sull'epilazione laser, tono da consulenza («È una
delle domande che mi fanno più spesso… Il laser è un percorso, non una magia
in una sola seduta.»). Un commento di una follower, in russo/ucraino:
«Написала в Директ» («Ho scritto in Direct») — coerente con la bandiera 🇺🇦 in
bio e una parte di clientela ucraina/russofona.

**Cavoretto**: collina residenziale di Torino, sul lato est del Po. Non ci sono
descrizioni del quartiere nei post analizzati: l'unico riferimento è
l'articolo di Torino Oggi, che lo tratta come «polo del benessere» insieme al
Petit Cafè adiacente.

## Cosa non c'è, e perché

- **Prezzi: nessuno.** La storia in evidenza «LISTINO» esiste ma il contenuto
  non è leggibile senza login (il viewer blocca dietro il muro di
  autenticazione anche con `Escape` e attesa — a differenza dei post del feed,
  le storie in evidenza non hanno un fallback pubblico). Nessun listino altrove.
- **Foto vere del locale, dello staff o di lavori su clienti: zero, di
  proposito dichiarato.** I tre post fotografici pubblici (5 immagini, 2
  caroselli) sono risultati **tutti grafiche di marketing/stock**, non scatti
  del salone: dettaglio nell'inventario foto sotto. Le foto vere (interno,
  manicure, prima/dopo) stanno nelle storie in evidenza e nelle foto caricate
  su Google Maps, entrambe non raggiungibili senza login.
- **Orario settimanale completo**: solo il venerdì (apertura alle 9) letto da
  Google Maps.
- **Formazione/percorso della titolare Tania**: non in bio, non nell'articolo.
- **Prezzo dei trattamenti Juliette Armand / Kobido / Laminazione**: nessuno
  pubblicato.

## Inventario foto

5 immagini scaricate da `assets/img/`, tutte ≥1080 px sul lato lungo, più il
profilo a 150 px (sotto minimo, dichiarato — Instagram non serve l'avatar oltre
150 px senza login, stessa trappola di [[sito-laurafranzoni]]).

| File | Px | Cosa mostra |
|---|---|---|
| `post1-01.jpg` | 1402×1753 | Template «Le tendenze della manicure Autunno 2026»: mano con manicure bordeaux scura su sfondo grigio, incorniciata da foto stock di cioccolato e rose. **Non è una foto del salone.** |
| `post2-01.jpg` | 941×1254 | Slide 1/2 di un post educativo sul laser: gambe/mano stock con crema, testo «Scopri la mia storia». Stock. |
| `post2-02.jpg` | 1365×1818 | Slide 2/2: fumetto con due bambole Barbie che parlano di epilazione laser (FAQ ricrescita peli). Stock/grafica. |
| `post3-01.jpg` | 960×1267 | Primo piano di un occhio con crema sulla guancia, foto stock del brand. |
| `post3-02.jpg` | 1024×1345 | Locandina prodotto **Juliette Armand**, linea Caviar (uova di salmone e caviale nero in due vaschette). Materiale del fornitore. |
| `profilo-150.jpg` | 150×150 | Logo: cerchio oro-tortora con profilo di volto stilizzato in linea, «LEI» in serif maiuscolo, «BEAUTY ROOM» in maiuscoletto piccolo sotto. **Sotto il minimo di 1080**, è il massimo ottenibile senza login (firma URL rifiuta `s1080x1080`, stessa trappola già pagata su [[sito-designcapelli]] e [[sito-laurafranzoni]]). |

**Colori campionati dal logo** (pixel presi a mano dal profilo): sfondo
oro-tortora tra `#9A8D7D` e `#B3AB9E`, highlight crema-oro `#E6CFAF`.

**Conclusione per chi farà la direzione**: il materiale fotografico pubblico
non ha un solo scatto reale del posto. Le cinque immagini raccontano solo il
*registro* con cui comunicano (educativo, un po' da rivista, cita marchi),
utile per il tono ma inutile come hero — un hero da queste immagini
userebbe contenuto stock non loro, il che è esattamente ciò che le note vietano
di inventare. Le foto vere esistono (Google Maps ne mostra, «Interno»,
«Manicure», «Dal proprietario») ma non sono scaricabili senza login: **vanno
chieste alla cliente**, come già successo su [[sito-designcapelli]] e
[[sito-adelinanails]].

## Cosa dicono i competitor (da [[competitor-siti-estetica]])

- **Obbligatorio quasi ovunque** (12 home confrontate): indirizzo esplicito
  (12/12), titolare nominata (11/12), un contatto diretto tel/whatsapp (12/12).
  Lei Beauty Room ha tutti e tre: indirizzo, Tania, telefono.
- **Nessuno pubblica un listino con prezzi in home** (0/12): chi ha un
  listino lo linka a parte. Coerente con l'assenza di prezzi qui.
- **Orari pubblicati solo nel 50%** (6/12): qui manca quasi del tutto, un
  buco comune, non un'anomalia.
- **Recensioni Google** presenti in 5/12: qui ci sono ed sono ottime (5,0/16),
  vanno usate — è uno dei pochi dati "di lusso" (le altre hanno 0-100
  recensioni, qui la % è impeccabile anche se il numero assoluto è basso).
- **Frasi fatte da evitare**, dalla sintesi della ricerca: «oasi (di
  benessere)», «viaggio interiore», «nel cuore di [città]», «la cura di te è
  la mia passione», «prodotti di ultima generazione». Nessuna è nei testi
  raccolti qui, ma il registro dei post di Lei Beauty Room (specie il primo,
  di sapore rivista patinata) rischia di scivolarci se non si sta attenti.
- **Il modello più vicino per completezza pratica** resta A&B (orari + FAQ +
  100 recensioni + metodo nominato): Lei Beauty Room ha meno dati (niente
  orari completi, niente FAQ), ma il punteggio recensioni è più alto.

## Mondo scelto — «La stanza», 24/09

Tre mondi proposti dall'operatore di direzione su Opus (`MONDI.md` nel repo),
scelto il primo con otto correzioni del direttore (`MONDO.md`).

**La metafora.** Una beauty room è una stanza, e una recensione la chiama
«piccola bomboniera». L'arco del logo diventa la porta, ed è **l'unica forma del
sito**: porta nell'apertura, cornice ferma al centro durante le stanze, badge nei
contatti. Mai sparsa come decorazione.

**La spina.** Si entra dalla soglia con nome e indirizzo; l'arco resta fermo e
dentro si passa da una stanza all'altra, cinque servizi con una lacca ciascuno,
e **il colore della stanza è il colore della pagina** (sfondo, testo, arco
cambiano insieme). In fondo l'arco incornicia il 5,0 di Google e si richiude nel
badge dei contatti.

**L'apertura**, a ogni caricamento: l'arco si disegna, cresce, ci si passa
attraverso, il colore cambia, LEI sale lettera per lettera, il badge si sistema
in barra. 1,0-1,5 s.

**Palette e font.** Tortora `#A59886`, tortora scuro `#6E6356`, crema-oro
`#E6CFAF`, prugna `#241A22`, bordeaux `#4E1422` (dal suo post «Autunno 2026»).
Zodiak 300/800 + Switzer 400/500; Ballet solo per il nome delle cinque stanze.

**Gli scarti.** «Lei» (tre lettere giganti come struttura): il rosa `#E0218A`
è gusto nostro, e le lettere a tutta finestra rischiano l'hero da template. «La
collina» (si sale dal Po a via alla Parrocchia): racconta il posto e non il
mestiere, andrebbe bene anche al bar accanto, e giallo e verde tolgono spazio
al tortora del marchio. La tenda giapponese del Kobido, uscita da impeccable,
scartata dall'operatore: un servizio su sei non fa un'identità.

**Le regole di costruzione date dal direttore.** Il profilo di donna del logo
non si ridisegna: marchio ricomposto in Zodiak con l'arco in SVG geometrico,
l'originale a 150 px solo in barra a 48 px o meno, il vettoriale si chiede a
Tania. Le 5 grafiche stock del feed non vanno in pagina: **strada 2 del
processo, dichiarata** — il sito regge senza foto, le foto vere si chiedono
dopo. `tel:` come bottone principale e DM Instagram come secondo, **niente
`wa.me`** finché WhatsApp non è confermato. Nessun prezzo, nessun «a partire
da», orari solo quello confermato.

## Collegamenti

[[lei-beauty-room]] · [[processo-siti]] · [[competitor-siti-estetica]] ·
[[direttive-siti]] · [[trappole]] · [[registro-interventi]]
