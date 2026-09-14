---
riga: Le due liste che stamattina mancavano - 50 DenkiShift e 50 ricerca di mercato, tutte in Lombardia - costruite dopo la bocciatura di Patrick sul 50-50-50.
type: area
updated: 2026-09-14
source: denkicode
verificato: 2026-09-14
prodotto: [denkishift, gestionale-custom]
canale: instagram
stato: pubblicata
---

# Le due liste che mancavano, e perché mancavano

Patrick, 14 settembre: *«ci eravamo detti n50 50 en 50, mi hai dato solo 43 siti
(che ho fatto) non mi hai dato gli altri, provvedi ora e cjhe non capitin mai
più»*. La regola è scritta in [[metodo-liste]].

**L'errore non era il bacino, era l'ordine delle priorità.** Stamattina avevo
consegnato 43 righe siti e zero sulle altre due, giustificandomi col banco
pieno e coi lead caldi da recuperare. I lead caldi si fanno **in più**, non al
posto delle liste.

| Lista | Consegnate | Dove | Settori, nuovi per noi |
|---|---|---|---|
| DenkiShift | **50** | tutta la Lombardia | palestre e centri sportivi, cliniche veterinarie, spa, catering, nidi, studi dentistici |
| Ricerca di mercato | **50** | tutta la Lombardia | cantine, serramenti e falegnamerie, verniciature industriali, agricole, birrifici |

## DenkiShift — il settore che nessuno aveva ancora toccato sono le palestre

Ristoranti e alberghi erano bruciati, RSA e panifici li aveva fatti il 13.
Aperti sei segmenti nuovi, tutti scelti perché **il turno è il loro problema**:

- **18 fra palestre e centri sportivi**. Il caso migliore è Special One di
  Sarezzo, che in bio dichiara *palestra, piscina, spa, beauty e ristorante*:
  cinque reparti con orari diversi nello stesso posto. Tre scrivono l'orario da
  soli — World of Fitness Treviglio e New Fitness Cremona sono **H24 sette
  giorni**, Enjoy Fitness Brescia apre alle 6 e chiude alle 22:30.
- **7 cliniche veterinarie**, dove la prova è il pronto soccorso o la degenza.
  La Clinica del Cane di Brescia ha pure **hotel e asilo diurno**: un hotel per
  animali non chiude la notte.
- **5 centri benessere** con cabine e massaggiatori da incastrare.
- **6 catering e banqueting**: il personale lo chiamano evento per evento, ed è
  esattamente il problema che il programma risolve.
- **5 studi dentistici e centri medici**: specialisti e igieniste che ruotano
  sulle stesse poltrone. San Benedetto ne ha **due sedi**, Brescia e Pavone del
  Mella.
- **2 nidi e una cooperativa sociale**: il rapporto educatrici-bambini è fissato
  per legge, e quando ne manca una il buco va coperto per forza.

⚠️ **Fuori le catene, e una era nascosta**: Anytime Fitness, FitActive, Hello
Fit e FitUP sono franchising, e l'Ospedale Veterinario di Bergamo dichiara in
bio di essere «parte di @gruppo_animalia». Fuori anche AniCura, che possiede
sia la CMV di Varese sia la Malpensa: il software glielo impone la sede.

⚠️ **Fuori anche chi è troppo piccolo**: Ultimate Fitness fa allenamenti «in
piccoli gruppi massimo 6 persone», P-Club sono due personal trainer che si
firmano in bio. Sotto le otto persone il programma non serve.

## Ricerca di mercato — le cantine sono il bacino che mancava

I settori del 12 e del 13 erano dichiarati esauriti, ed è vero: officine,
carrozzerie, impiantisti, edilizia e tipografie ripescavano gli stessi handle.
Il filone nuovo sono **le aziende del vino e del cibo**, che su Instagram ci
stanno e ci stanno bene.

- **16 cantine** fra Franciacorta, Valcalepio, Lugana, Valtellina e Oltrepò.
  Sono aziende che dichiarano da sole quanto sono strutturate: Montonale scrive
  *trentacinque ettari vitati*, Le Marchesine *cinque generazioni*, Castelveder
  *dal 1975*, Casa Vinicola Nera *dal 1940*.
- **11 fra serramenti e falegnamerie** con produzione interna dichiarata.
  Bugada è una **falegnameria dal 1870**.
- **5 aziende agricole e agriturismi** che trasformano e vendono: La Camosciata
  fa formaggio a latte crudo e salame di capra con 34 mila follower.
- **2 verniciature industriali** (40 e 50 anni di impianto), **2 birrifici**,
  **2 pastifici storici**, più marmi, vetrerie, ingrossi e autodemolizioni.

⚠️ **Quattro righe buttate per il nome che mente**, la stessa trappola del 13
settembre: «Impresa Costruzioni **Bergamo**» ha sede a **Venezia**, «Azienda
Agricola **Lodigiana**» sta a **Ronsecco, in provincia di Vercelli**,
«Autotrasporti **Bresciani**» a **Settimo Torinese** e «Metalmeccanica Barillà»
a **Reggio Calabria**. Il nome del profilo non dice dove sei.

⚠️ **Undici righe pronte sono uscite perché erano già state contattate**, e
`controlla-lista.py` le ha prese tutte: mvserramenti, vetreriabonometti,
rimag_official, rs_serramenti_group, la_tipografia_group_brescia, rgmnewsrl,
abcgaragebg, bontempiimpianti, falegnameriamaffeisvertova, edilporte_brescia,
autofficinamantovansnc. Sostituite con le cantine.

## Quanto è costato

| | DenkiShift | Ricerca |
|---|---|---|
| profili aperti e letti | ~85 | ~75 |
| tenuti | 50 | 50 |
| morti, privati o con due post | 14 | 13 |
| fuori Lombardia | 5 | 7 |
| catene, franchising, gruppi | 6 | — |
| già contattati, sostituiti | 5 | 11 |

## Controlli

| | DenkiShift | Ricerca |
|---|---|---|
| `controlla-lista.py` | **ok** | **ok** |
| `voce-check.py` | 0 tell su 50 | 0 tell su 50 |

Sei messaggi sono stati riscritti per il senso, non per i tell: la chiusura di
DenkiShift metteva `www.denkicode.com` dopo un punto e il controllo lo leggeva
come refuso, quindi adesso è *«Qui c'è quello che facciamo:»*; il messaggio
della ricerca chiudeva dando del Lei dopo aver dato del voi, e adesso è voi
dall'inizio alla fine.

⚠️ **Nella ricerca non si nomina nessun prodotto**, come vuole
[[script-indagine]]: `www.denkicode.com` sta nella riga di chi scrive e dice
solo da dove arriva la ricerca.

## Collegamenti

[[metodo-liste]] · [[metodo-instagram]] · [[dm-instagram-denkishift]] ·
[[script-indagine]] · [[2026-09-14-lista-siti-bs-bg]] · [[denkishift]]
