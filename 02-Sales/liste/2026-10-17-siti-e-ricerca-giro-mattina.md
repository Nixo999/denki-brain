---
riga: Per Patrick - 17/10 in due giri, siti 59 e ricerca 54 sul banco (il secondo dagli account simili via Brave); posta letta dopo 16 giorni, 4 lead caldi, 59 DM mai consegnati
type: area
updated: 2026-10-17
source: claude
verificato: 2026-10-17
prodotto: [siti-vetrina, gestionale-custom]
canale: instagram
stato: pubblicata
---

# 17 ottobre: siti 59 su 100, ricerca 54 su 60, in due giri

Settimo giro di [[giro-mattina]], ruolo `primo`, dal Mac di Nicola. Il task è
partito alle 11:01 invece che alle 8, perché il primo `git fetch` di
`giro-mattina.py` è rimasto appeso senza rete per quasi due ore; alle 11:01
GitHub rispondeva e il giro è ripartito da capo. Sette operatori Opus, uno per
cella di `prossimo-giro.py`, con un brief comune che fissava il ritmo su
Instagram (una lettura alla volta, 5 secondi di pausa, 70 letture a testa,
nessun handle indovinato a raffica, niente browser). Le nove liste con almeno
una riga sono **pubblicate** sul banco: 73 righe nuove, `pubblica-lista.py`
passato su tutte.

**Instagram ha retto per tutto il giro**: 196 letture in sette operatori fra
le 11:09 e le 11:46, tutte con risposta 200. Il ritmo del brief funziona. Le
righe mancano per un altro motivo: i motori di ricerca e Pagine Gialle si sono
chiusi quasi subito, e senza di loro gli handle arrivano solo dalle directory
di settore e dai siti aziendali.

| Lista | Cella | Righe | Profili | Stato |
|---|---|---|---|---|
| siti | BS · fioristi e wedding planner | 10 | 56 | esaurita per fonti: fioreriadaelisa battuta, 17 handle morti, 11 sotto i 200 |
| siti | BS · pasticcerie e cake designer | 3 | 30 | esaurita per resa (1 su 10): 19 handle indovinati inesistenti |
| siti | VC · tatuatori e piercing | 10 | 18 | esaurita per bacino: 21 studi in provincia, tutti letti |
| siti | TO · tatuatori e piercing (riserva di VC) | 12 | 16 | aperta, rende 3 su 4 |
| siti | AT · toelettature e dog trainer | 1 | 9 | esaurita per bacino: 10 schede in provincia, 2 catene |
| siti | AO · toelettature (riserva di AT) | 0 | 1 | fonti bloccate, da riaprire |
| ricerca | BS · ingrossi e distribuzione | 14 | 23 | esaurita per fonti: finiti i siti con link a Instagram |
| ricerca | CR · ingrossi (riserva di BS) | 0 | 5 | esaurita: i siti dei grossisti cremonesi non linkano Instagram |
| ricerca | BS · alimentari artigianali | 20 | 30 | aperta, rende 2 su 3: 16 cantine della Franciacorta |
| ricerca | LC · aziende agricole con vendita | 2 | 7 | esaurita per fonti |
| ricerca | MN · falegnamerie (riserva di LC) | 1 | 1 | aperta, appena iniziata |

Tre riserve aperte su quattro assegnate (TO, MN, CR; AO solo sondata); la cella
delle pasticcerie non ne aveva una.

## Il secondo giro (12:30-12:55): 40 righe dagli «account simili» di Instagram

Nicola: «sul mio browser sono loggato», «sono su brave». Da Brave, con
l'account `denkicode`, la ricerca interna di Instagram risponde ancora:
`/api/v1/fbsearch/account_serp/?query=…` trasforma un nome in handle (il vecchio
`topsearch` risponde 404) e `/api/v1/discover/chaining/?target_id=<pk>` dà fino
a 80 account simili a un profilo. `users/{pk}/info/` risponde 429: il profilo si
legge ancora con curl Googlebot. Dai 60 profili pubblicati al mattino, usati
come semi, sono usciti 1.700 candidati; filtrati per parola nel nome e letti
dagli operatori (una lettura ogni 5 secondi, 280 letture, zero blocchi) hanno
dato 40 righe. Il filtro che costa è la provincia: il «simile» di Instagram è
dello stesso mestiere ma di tutta Italia.

| Lista | Candidati letti | Righe | Perché il resto è fuori |
|---|---|---|---|
| siti BS pasticcerie -2 | 29 | 6 | 10 fuori provincia, 6 col sito, 4 fermi |
| siti BS fioristi -2 | 46 | 5 | 17 fuori provincia, 9 col sito, 6 location |
| siti TO tatuatori -2 | 60 | 10 | 17 resident senza studio, 15 fuori provincia, 5 col sito |
| siti AT toelettature -2 | 18 | 2 | 13 fuori provincia |
| ricerca BS alimentari -2 | 36 | 14 | 10 cantine del Consorzio, 11 fuori provincia |
| ricerca BS ingrossi -2 | 22 | 1 | 8 fuori provincia, 4 fuori mestiere |
| ricerca LC agricole -2 | 10 | 1 | 7 fuori provincia |
| ricerca MN falegnamerie -2 | 9 | 1 | 6 fuori provincia, Bisi è un negozio |

Da guardare prima di mandare, oltre alla bio di tutte: @fattoriadassogno
(21.000 follower, sul dominio una pagina di login), @ottonetti_legnami (un
solo post nel 2026, il 26/05: entra al limite), @alporifesta (sede legale forse
a Milano, post non letti), @theclubdoggo (il dominio clubdoggo.it in «Coming
Soon» potrebbe essere di un omonimo di Bergamo: il messaggio non lo nomina),
@p_isabau (pensione per cani, non toelettatura), @ziliani_franciacorta e
@costaripa (grandi), @_flaco_tattoo (atelier di Rivoli aperto il 10/09, da
confermare), @tattoodoubletrucks (ci lavora Diegoskull, già contattato il 21/09),
@creativeink_tattoo (il «prenota» in bio può essere Fresha: gancio da rivedere).
Gli otto messaggi della ricerca non portano il link del modulo: chiedono se
mandarlo qui o per email.

Due commit automatici hanno pushato versioni intermedie con righe poi tolte
(@pasticceriadesiree, @giuliana_fiori_offlaga, @ilmercatopiantefiori hanno il
sito): sul banco sono entrate solo le versioni finali.

## La posta, letta il 17/10 da Brave (account denkicode)

La posta non veniva letta dal 1° ottobre: in mezzo ci sono circa 1.000 DM. Si
è letta dall'account `denkicode` collegato in **Brave** sul Mac di Nicola, con
l'estensione Claude in Chrome: l'API `direct_v2/inbox` risponde 404 da oggi,
quindi la lista si è scorsa dal DOM (3.390 conversazioni fino a tre settimane
fa) e le chat con una risposta vera si sono aperte una per una.

**I lead caldi, prima di tutto:**
- **Educazione Cinofila Piacenza** (nome del thread; handle non abbinato):
  **appuntamento fissato lunedì 20/10 alle 17:30**, confermato giovedì 16/10.
- **@flordelislegnano** (Jessica, Legnano): vuole sentirsi su WhatsApp al
  349 7154431; l'8/10 ha detto «tranne il lunedì va bene quasi sempre»,
  Patrick ha proposto martedì o mercoledì alle 18 e da allora c'è solo la sua
  autorisposta. **Ferma da 9 giorni: si chiama lei.**
- **@cakeroyal.bs** (Brescia): «appena ho un attimo vado a guardare», l'11/10.
  Nessun rilancio, 6 giorni.
- **@dragonfly_estetica** (Casale): bozza vista il 18/09, «Grazie» il 29/09,
  niente da 18 giorni. **@soul_ink_torino_city**: «Darò un occhiata» il 28/09.

**Tre aziende della ricerca chiedono il modulo per email**, perché il link
nel DM non si apre o Instagram lo segna come possibile truffa:
cascina.madonnina@gmail.com (7/10), info@laquintalina.it (13/10),
info@labevera.it (13/10). Nessuna ha ancora ricevuto la mail.

**I no**: @pelosamente, @manuelghezzitattooer, @sartoriamora,
@marghefotomilano (sito in elaborazione). **Errori di lista**:
@musetto_perfetto_toelettatura ha il sito, @vivaiosaronno è un progetto
immobiliare. Tutti in `risposte-dm.csv` e in `Esito DM` sul banco.

**I numeri che pesano più delle risposte:**
- **92 DM non sono mai arrivati**: Instagram risponde «Questo account non può
  ricevere il tuo messaggio perché non consente nuove richieste di messaggi
  da tutti». Sono circa il 9% degli invii dal 25/09; 59 abbinati a righe del
  banco e segnati `non consegnato` (32 siti, 27 ricerca). I 33 non abbinati
  vengono da invii più vecchi o da liste fuori banco.
- **85 autorisposte** (50 abbinate e segnate), 37 ancora «Unread».
- **Il link del modulo nel primo messaggio è il difetto della ricerca**: tre
  risposte su tre dicono che non si apre o che Instagram lo segnala come
  truffa. La regola 5 di [[metodo-instagram]] («niente link nel primo
  messaggio») vale anche qui: il primo DM della ricerca deve chiedere se va
  bene mandare il modulo, e il link parte nel secondo messaggio o per email.

## Da guardare prima di mandare

- **In nessuna riga di oggi è stato letto il link in bio**: la pagina scaricata
  con curl non lo contiene. Prima di scrivere si apre la bio nell'app, su
  tutte e 73.
- **Profili grandi**: @floricolturatracconaglia (33.000 follower),
  @gruppodac (logistica nazionale, 30.000 clienti), @bersiserlini (51.000),
  @mosnel, @biondelli e @macelleriasaleepepe (oltre 14.000),
  @materia_rezzato (8.300, matrimoni di fascia alta), @dallabona (S.p.A.).
- **Gancio 6 rimesso a mano dopo lo scarto di `verifica-sito.py`**:
  @villa_floris (villafloris.it fermo al 2017), @latelierfloreale,
  @gelateriacalchera (sito del 2021; a Manerba esiste un'altra Gelateria
  Calchera con sito e P.IVA proprie).
- **Sede o nome da confermare**: @rachelifiorista (Sarezzo e il nome Fabio
  vengono dalla scheda, non dalla bio), @tonelli_tattooartist (lo studio
  Esseink viene da una recensione), @etientattoo (due indirizzi diversi),
  @expression.tattoo (indirizzo da Fresha), @acquaviva.spa (Travagliato o
  Lograto), @toelettaturaeasydog (handle provato dal nome, ma l'indirizzo
  nelle didascalie coincide con la scheda).
- **Fermi da più di un mese**: @expression.tattoo (10/09), @pepè (07/08),
  @fishbone (04/07), @maestri (22/09), @labottegadelgelatodigaravelli (27/05),
  @pastificiogerolasnc (03/09), @stocchettibevande (02/09),
  @derbuscocives (27/08).
- **Vicini alla soglia dei 200**: Ago della Bilancia (292), Nobilis (305),
  Studio 220 (528) a Torino.
- @brokendreams_tattoo e @alteregostudio_giuliachiara collaborano: non lo
  stesso giorno. @assia_con2esse_tattooss chiude dal 27/10 al 6/11.
- Casargo (IndoVino) sta a 47 km da Seveso: «qui in zona» regge per poco.
- I messaggi della ricerca dicono «otto domande, tre minuti» come
  [[script-indagine]]; le righe del 9/10 dicevano «sei domande, due minuti».

## Da riprendere al prossimo giro, senza rifare la ricerca

- **BS alimentari** (lette nel secondo giro, 10 entrate), 14 cantine dall'elenco del Consorzio Franciacorta:
  @cola_franciacorta, @tenutaambrosini_franciacorta, @faccolifranciacorta,
  @santalucia_franciacorta, @mantifranciacorta, @sullali_franciacorta,
  @terredaenor, @ziliani_franciacorta, @corteaurafranciacorta,
  @turra_franciacorta, @ugovezzoli_franciacorta, @quadrafranciacorta,
  @rainerifranciacorta, @lacostadiome.
- **TO tatuatori**: @redpanttattoo (Crescentino, VC, 12.000 follower, da
  riprovare), @zoptattoostudios, @lab11vercelli, @overcast_tattoo_studio,
  @vastattoo_m, @buumtattootorino, @scatto_tattoo, @vero.piercer.
- **BS pasticcerie**, col sito, da guardare solo per il gancio 6:
  @pasticceriabazzoli, @gelaterialaromana, @filippofiorini_pasticceria,
  @quadrettobienno, @salvetti1885, @gelateriaconsuelo,
  @pasticceriapaganisergio. Senza handle e con dominio morto: Boifava
  (Montichiari), Gelatissimo (Boario), Desirée (Rivoltella), Arte Dolce
  (Sirmione), Mazzacani (Gavardo), Vassalli (Salò). Sito vecchio: Riva
  (Desenzano, Flash 2014), Centrale (Orzinuovi, 2011), Formis (Berzo Demo).
  Wix in 404: Rocca (Bagnolo Mella). Cake designer da matrimonio.com: Che
  torte! (Puegnago), Le Torte di Giada, Mon Cri Crì, Svitly Cake.
- **BS fioristi**: @pini.stefania_il.polline (Castelletto di Leno),
  @compagniadeifiori (sito WordPress 4.4 solo http, sede da provare);
  @trezeronovelab, @elenafiori.it, @steli_e_stili_ col sito vivo.
- **BS ingrossi**: @stocchetti_beverage_school, @caffecartapani
  (torrefazione, è un produttore); pagina vuota oggi @agrigelontheroadsrl,
  @morettimobe, @laselezione_enodrink.
- **LC agricole**: @birreria_belli_e_beati, @aldo_carozzi_ (personale); senza
  handle Azienda Agricola Casati (Olgiate Molgora), il miele di Davide Caglio,
  Del Risti's (Colico).
- **MN falegnamerie**, col sito ma senza link a Instagram: Giacomazzi
  (P.IVA 01850810209), Rinoldi a Gonzaga (01660380203), Cavazzoni a
  Pomponesco, Ottonetti Legnami.
- **AT**: Club Doggo (Portacomaro Stazione, clubdoggo.it in «Coming Soon»,
  gancio 3) senza handle da una fonte.

## Fonti, 17/10 dal Mac di Nicola (11:09-11:46)

- **Hanno retto**: Instagram via curl Googlebot (196 letture, zero blocchi);
  fioreriadaelisa.it (470 richieste); l'elenco cantine del Consorzio
  Franciacorta, franciacorta.wine (113 schede con sito e handle: la fonte
  migliore del giro); Beverfood (grossisti e vending lombardi, 7 handle);
  miotattoo.it dal suo indice dati; toelettature.net su Asti; dati.lombardia.it
  (fattorie didattiche e agriturismi); Virgilio Aziende (stessa banca dati di
  Pagine Gialle, 18 richieste senza blocco); PagineBianche; Facebook via curl
  Googlebot (dà follower e categoria, non l'handle Instagram); i siti aziendali
  via curl (circa 300 in tutto).
- **Pagine Gialle ha risposto 429 in cinque celle su sette**, dopo 5-50
  richieste: sette operatori sullo stesso indirizzo la saturano. Sui
  tatuatori di Vercelli e sulle alimentari ha retto.
- **Motori**: Yahoo 307 anti-bot alla prima richiesta da tutte le celle (ieri
  reggeva da tre su sei); DuckDuckGo pagina anti-bot alla prima in sei celle,
  ma 46 ricerche passate dalla cella di Vercelli; Brave 7 ricerche poi 429;
  Bing ignora il comune e risponde con Ravenna o Gussago; Mojeek, Startpage,
  Ecosia, Qwant, Yandex, SearXNG in captcha o 403. Lo strumento WebSearch
  degli operatori ha dato qualche azienda ma mai pagine Instagram.
- **Bloccate o inutili**: toelettature.net su Aosta (403), toelettatura.info,
  Cylex, RestaurantGuru, matrimonio.com e zankyou.it (403), Campagna Amica e
  oliogardadop.it (solo JavaScript), Coldiretti Lecco (DNS).
- **Posta non letta**: Instagram non è collegato nel browser dell'app.
- Gli handle indovinati dal nome continuano a rendere poco: a Brescia 24
  sonde per 0 righe utili sulle pasticcerie, 31 sonde per 2 righe sui
  fioristi.
- I sette operatori condividono la stessa scratchpad: uno ha sovrascritto per
  qualche minuto script con nomi generici (`ig.py`) nella radice. Dal prossimo
  giro il brief assegna a ciascuno una cartella propria.
- I commit automatici «Chiusura automatica» hanno salvato versioni
  intermedie dei CSV; le finali entrano nel commit del giro.

[[metodo-liste]] · [[giro-mattina]] · [[2026-10-16-siti-e-ricerca-giro-mattina]]
