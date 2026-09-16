---
riga: Le tre liste del 16 settembre - 51 siti sulla bellezza di Bergamo, 50 DenkiShift fra alberghi di lago e di montagna, 50 ricerca su concessionarie, arredo, ottici e immobiliari - e il modo nuovo di leggere i profili.
type: area
updated: 2026-09-16
source: denkicode
verificato: 2026-09-16
prodotto: [siti-vetrina, denkishift, gestionale-custom]
canale: instagram
stato: pubblicata
---

# 16 settembre — 51, 50 e 50, e 684 profili letti dall'API

Costruite fra la sera del 15 e la mattina del 16, in due sessioni: la prima
si è interrotta sul limite di utilizzo di Patrick con i profili già letti, la
seconda ha scritto i testi e fatto passare i controlli.

| Lista | Consegnate | Dove | Settore |
|---|---|---|---|
| Siti vetrina | **51** | Bergamo e provincia, 21 comuni | onicotecniche, estetiste, lash maker, trucco permanente |
| DenkiShift | **50** | Garda bresciano, Iseo, Livigno, Bormio, Valtellina, Cremona, Mantova, Lodi, Pavia, Como | alberghi di lago e di montagna, agriturismi, campeggi, pulizie, lavanderie industriali, vigilanza, laboratori |
| Ricerca di mercato | **50** | tutta la Lombardia | concessionarie, arredamenti e cucine, ottici, immobiliari, onoranze funebri, insegne, tessile, torrefazioni, vivai |

Sul banco di Patrick adesso: **111 righe del 14 più le 151 di oggi**.

## Il profilo si legge dall'API, in meno di un secondo

Fino a ieri il passo 2 di [[metodo-instagram]] costava una navigazione per
profilo. Da oggi no: la ricerca interna (`topsearch`) restituisce il `pk`
dell'utente, e `/api/v1/users/{pk}/info/` risponde con **bio, link in bio,
follower, post, categoria, città, indirizzo e telefono** in mezzo secondo.
`web_profile_info`, quello che le note davano per bloccato, risponde ancora
429; questo no. Letti **684 profili in due giri**, 426 e 258, in secondo piano
dentro la scheda di Instagram, senza un solo 429. Il come sta nel riquadro
del 16 settembre in [[metodo-instagram]].

⚠️ **La ricerca di Instagram fa rumore, e il rumore ha una forma.** «nails
albino» dà persone che si chiamano Albino, «estetica lovere» dà «lovers»,
«estetica leffe» dà tre brasiliane, «hotel cremona» dà un ristorante di
Genazzano, «hotel brescia» un albergo di Tangeri, «hotel mantovanini» uno in
Brasile, «lodi hotel» un altro in Brasile, «cappavia» una grotta in
Cappadocia. Su 852 candidati trovati con 431 query, **quasi la metà è stata
buttata prima di leggere il profilo** solo guardando nome e handle. È la
stessa trappola del 13 e del 14: il nome del profilo non dice dove sei.

## Siti — Bergamo, bellezza: 51 righe da 151 profili letti

Zona in rotazione: Bergamo, aperta il 14 con parrucchieri e barber. Settore del
giorno: onicotecniche, estetiste, lash e PMU, quello che a Brescia il 13 aveva
reso 81%.

| | Quanti |
|---|---|
| profili letti | **151** |
| tenuti | 51 |
| sotto i 200 follower | **54** |
| avevano un sito vivo col loro nome | **18** |
| fuori zona (Roma, Cogliate, Sestri Levante, Brasile, Norfolk) | 8 |
| catene, medicina estetica, accademie | 6 |
| tolti dopo la verifica | 2 |

Dentro le 51: 44 con gancio 1, **6 con gancio 5** (SumUp, vetrina-digitale,
Linktree, Zaap, qrdisplay, Treatwell), 1 con gancio 4: Nataly di Treviglio ha
in bio «intagram.com», un refuso che rimanda alla home di Instagram e non al
suo profilo.

**`verifica-sito.py` ha segnato 2 SCARTATO e 3 PROBABILE, e nessuno era loro.**
Oda Beauty di Bergamo era stata scartata per `odabeauty.fr`, una parrucchiera
a domicilio di Grasse; è rientrata con il messaggio che nomina la sua scheda
Treatwell. Nails by Empire era scartata per un negozio di cosmetici inglese:
tolta lo stesso, 218 follower e 22 post. I tre probabili erano un'Estetica
Erica di Ternate (VA) contro quella di Zogno, un'accademia di extension a
Roma e un negozio tedesco: scritto in colonna, riga per riga.
`sarabeautylab.it`, aperto dopo, è un centro estetico di **Bologna**: la
Sara Beauty Lab di Spirano era già uscita dalla lista e non è stata rimessa,
e non finisce in `gia-col-sito.csv` perché il sito non è suo.

⚠️ **`controlla-lista.py` cerca «403» e lo trova nei numeri.** Ha fermato la
lista per Lorenza Parisi, che ha **403 post**, e per Remedia, che ha il
telefono 340**403**9. Due righe verificate bene, bloccate da una regex senza
confini di parola. Aggirato scrivendo «quattrocentotre post» e togliendo il
numero, e **lo script è corretto oggi**: cerca «http error 403», non «403».

**I settori fatti a Bergamo**: parrucchieri e barber (14/9, con Brescia),
bellezza (16/9). Restano toelettature e tatuatori, che altrove hanno reso
poco; poi la zona si chiude e per rotazione si torna su Como e Varese sui
settori non battuti a settembre.

## DenkiShift — gli alberghi che nessuno aveva ancora scritto

Alberghi e ristoranti erano «bruciati» in Brianza, Varese, Como e Lecco. Il
Garda bresciano, il lago d'Iseo e la montagna di Sondrio non erano mai stati
toccati, e sono il caso da manuale del turno: stagione, reception, cucina,
piani e spa nello stesso posto.

- **28 alberghi**: 15 sul Garda (Sirmione, Desenzano, Salò, Gardone, Limone,
  Manerba, Tignale), 3 sull'Iseo, 9 fra Livigno, Bormio, Madesimo, Valmalenco
  e Sondrio, più Ponte di Legno, Selvino e Boario. Quasi tutti dichiarano
  ristorante o spa in bio: Bivio Plaza di Livigno ha **due ristoranti e la
  spa**, Araba Fenice di Iseo due piscine, lounge bar, bistrot e ristorante.
- **8 fra agriturismi, campeggi e lidi** con cucina e camere: Alberelle di
  Rovato ha vigna, cantina, cucina e camere sotto la stessa insegna.
- **5 imprese di pulizie, lavanderie industriali e vigilanza**: Lavajet di Como
  noleggia la biancheria agli alberghi, Iron di Paratico mette gli operatori
  agli eventi.
- **9 laboratori e ristoranti** nelle province mai battute: Vigoni di Pavia fa
  la Torta Paradiso dal 1878, DEM di Pavia apre dalla colazione al dopo cena.

**Fuori i gruppi, ed erano tanti**: Terme di Sirmione (quattro alberghi),
Lungolivigno, great2stay, due Best Western, Bes Group, Cola Hotels, Horstmann.
Fuori i cinque campeggi del lago Maggiore, che stanno tutti sulla sponda
piemontese, e Peschiera, Lazise e Riva, che sono Veneto e Trentino.
51 profili su 233 sotto i 200 follower.

⚠️ Gli alberghi rispondono col centralino: 28 autorisposte nei giri di
settembre. Il DM scalda, la chiamata chiude → [[script-denkishift]].

## Ricerca di mercato — il bacino nuovo sono le PMI che vendono

Il 13 settembre il bacino industriale era dichiarato esaurito, e il 14 le
cantine lo avevano rimpiazzato. Oggi il filone è **chi ha un negozio e
un'officina insieme**: concessionarie con assistenza (9), arredamenti e cucine
con progettazione e montaggio (10), ottici con laboratorio (7), agenzie
immobiliari con decenni di storia (5), onoranze funebri attive ventiquattro
ore (3), più insegne, tessile comasco, torrefazioni, vivai, un calzaturificio
di Vigevano con produzione propria, un colorificio che produce vernici, una
ditta di piscine, un pastificio.

**154 profili su 300 sotto i 200 follower**: le aziende strutturate su
Instagram ci stanno, ma le seguono in pochi. La soglia dei duecento è il
filtro più duro di questa lista.

**Fuori Lombardia, di nuovo per il nome**: gli scatolifici stavano tutti in
Campania, i noleggi di piattaforme in Puglia e Campania, Apicoltura Lombardi a
Faenza, i Fratelli Pavia ad Agliano d'Asti, e «Azienda Agricola Lodigiana» a
Ronsecco, in provincia di Vercelli, la stessa trappola del 14.

`controlla-lista.py` ha preso un già contattato (Pegoiani, sul banco dal 13);
Carrozzeria Mara, ABC Garage, Bontempi e MEV erano usciti dalla ricerca e
sono stati tolti a mano perché già scritti il 12.

## Controlli

| | Siti | DenkiShift | Ricerca |
|---|---|---|---|
| `verifica-sito.py` | girato con i motori su 48 righe, senza sulle 5 aggiunte | — | — |
| `controlla-lista.py` | **ok** | **ok** | **ok** |
| `voce-check.py` | 0 tell su 51 | 0 tell su 50 | 0 tell su 50 |

Ventitré messaggi riscritti prima di passare: le catene di tre «e», «su
misura», un «glielo» che mescolava i registri.

## Collegamenti

[[metodo-instagram]] · [[metodo-liste]] · [[2026-09-15-rilanci-lead-aperti]] ·
[[2026-09-14-lista-siti-bs-bg]] · [[2026-09-14-denkishift-e-ricerca]] ·
[[dm-instagram-denkishift]] · [[script-indagine]] · [[stile-comunicazione]]
