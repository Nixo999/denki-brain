---
type: risorsa
riga: Rapporto integrale del 29/10/2026 su tracker GPS per mezzi di lavoro - famiglie, reti 2G/3G in Italia, prezzi nei negozi, SIM, installazione, legge. Sintesi in gps-mezzi.
updated: 2026-10-29
source: claude
tags: [gps, flotta, ricerca, hardware]
---

> Rapporto scritto da un agente Sonnet il 29/10/2026 per [[gps-mezzi]]. Ogni
> dato porta un codice: L = letto aprendo la pagina, R = da riassunto di
> ricerca, M = memoria del modello. Nessuna persona ha ricontrollato i numeri,
> salvo il prezzo dell'FMC130 su Getic (Trevis, 29/10). Non è consulenza legale.

# Ricerca hardware GPS per mezzi di lavoro (Milano e area)

Data della ricerca: 29 ottobre 2026. Ricerca fatta solo con WebSearch e WebFetch, nessun repository toccato.

## Come leggere questo rapporto

Ogni dato porta un codice che dice quanto è solido.

| Codice | Significato |
|---|---|
| L | Letto oggi (2026-10-29) aprendo la pagina indicata con WebFetch. Lo strumento restituisce un riassunto fatto da un modello piccolo, quindi un numero può essere trascritto male. Dove ho potuto, ho controllato i prezzi con un calcolo incrociato (per esempio i prezzi Getic con IVA al 22% coincidono con quelli senza IVA moltiplicati per 1,22). |
| R | Riportato dal riassunto di un risultato di ricerca. La pagina non si è aperta, oppure l'ho vista solo come estratto. Va ricontrollato prima di citarlo a un cliente. |
| M | Lo so da memoria, non verificato in questa ricerca. |

Gli URL stanno nella tabella o nel testo accanto al dato, e sono ripetuti nella sezione 8.

---

## 1 Famiglie di dispositivi e reti

### 1.1 Le quattro famiglie e quando si usano

| Famiglia | Quando conviene | Costi indicati | Difetti | Esempi |
|---|---|---|---|---|
| Spina OBD-II plug-and-play | Auto e furgoni leggeri a 12 V; noleggio breve, car sharing aziendale, fringe benefit; attivazione immediata. | Hardware 60-90 euro, installazione 0 euro, tempo di montaggio pochi secondi (Companeo, guida aggiornata il 2 aprile 2026, L). | Si stacca facilmente ed è spesso visibile sotto il cruscotto (L, stessa pagina). Non adatta ai camion con presa a 9 poli (vedi 5.4). | Teltonika FMB003 (2G), Teltonika FMC003 (4G), Jimi VL502 (4G) |
| Cablato 12/24 V con rilevamento accensione e batteria di riserva | Priorità antifurto, mezzi pesanti, analisi di consumi e accensione. | Hardware 100-250 euro, manodopera 50-150 euro per veicolo (Companeo, pagina aggiornata il 12 marzo 2026, L). | Serve un tecnico, circa 45-60 minuti per veicolo (Companeo, L). | Teltonika FMB920, FMC920, FMB125, FMC130, FMB140, FMC150; Jimi JM-VL03 |
| A batteria con magnete | Rimorchi, container, generatori, macchinari senza alimentazione propria. | Hardware 100-180 euro, installazione 0 euro (Companeo, L). | Posizioni meno frequenti e batteria da monitorare (Companeo, L). | Teltonika TAT141 (LTE-M), TAT240 (4G Cat 1), Queclink GL320MG (LTE-M/NB-IoT con ripiego 2G), Jimi LL301 (4G, 10.000 mAh) |
| Con lettore iButton o RFID per sapere chi guida | Quando il cliente vuole associare il viaggio a una persona. | Lettore iButton 1-Wire 9,49 euro, chiave Dallas 1,35 euro, lettore RFID Teltonika 22,99 euro (GoTracker-Store, L); lettore RFID 1-Wire 33,40 euro (Getic, L). | Richiede l'ingresso 1-Wire: la scheda tecnica sul wiki Teltonika lo elenca per FMB125 e FMC130, e non lo elenca per FMB920 e FMC920 (L). L'identificazione dell'autista aumenta il peso del tema privacy (sezione 6). | Teltonika FMB125, FMC130 |

Fonti: https://www.companeo.it/localizzazione-satellitare-veicoli/guide/localizzatore-gps-obd-cablato-batteria , https://www.companeo.it/localizzazione-satellitare-veicoli/FAQ/costo-installazione-gps-auto-aziendale , https://wiki.teltonika-gps.com/view/FMC130_General_description , https://wiki.teltonika-gps.com/view/FMB125_General_description , https://wiki.teltonika-gps.com/view/FMB920_General_description , https://wiki.teltonika-gps.com/view/FMC920_General_description , https://gotracker-store.com/en/ , https://www.getic.it/shop/fleet-management

### 1.2 Le tecnologie di rete

| Tecnologia | A cosa serve | Note |
|---|---|---|
| 4G LTE Cat 1 | Standard per i tracker da veicolo. Funziona con qualsiasi SIM dati 4G, regge il passaggio da una cella all'altra e ha velocità sufficienti per aggiornamenti del firmware. | I modelli Teltonika FMC920 e FMC130 usano Cat 1 con ripiego su 2G; l'FMC130 nella variante con modulo EC21 ha anche l'UMTS (L, wiki Teltonika). |
| LTE-M (Cat M1) | Tracker a batteria per rimorchi e container; supporta il movimento. | Vodafone ha lanciato la prima rete LTE-M italiana a giugno 2022 (R, telecoms.com). Per WindTre e TIM non ho trovato dati sull'LTE-M. |
| NB-IoT | Sensori fermi. Chi cambia cella deve riconnettersi, quindi è la scelta peggiore per un mezzo in movimento (R, Wikipedia e guide di settore). | TIM ha lanciato l'NB-IoT nel 2017 e Vodafone dichiara di averlo su tutti i siti 4G (R, notizie 2017-2022). Non ho trovato dati 2026. |
| 3G | Da escludere. | Vedi 1.3. |
| 2G (GSM/GPRS) | Ancora attivo oggi, ma senza futuro garantito. | Vedi 1.3 e 1.4. |

Fonti: https://wiki.teltonika-gps.com/view/FMC130_General_description , https://telecoms.com/iot/vodafone-launches-italy-s-first-lte-m-network , https://en.wikipedia.org/wiki/LTE-M , https://www.lightreading.com/iot/telecom-italia-covers-73-of-italy-with-nb-iot

### 1.3 Che fine fanno 3G e 2G in Italia (stato al 29 ottobre 2026)

| Operatore | 3G | 2G |
|---|---|---|
| TIM | Spegnimento iniziato il 14 giugno 2022, con fine prevista il 15 ottobre 2022 (L, TuttoAndroid, articolo del 14 giugno 2022). Che sia stato completato in quella data lo riporta solo un riassunto di ricerca (R). | Attivo (L, Key4biz, 7 aprile 2026). |
| Vodafone | Spegnimento programmato per il 31 gennaio 2021 secondo un articolo dell'ottobre 2020 (L, Tecnoandroid); altre fonti indicano la fine di febbraio 2021 (R, Mondomobileweb). | Mantenuto di proposito per chiamate, SMS e sistemi di teleallarme (L, Tecnoandroid). Vodafone punta a smantellare tutto entro il 2030-2031 (L, Key4biz, 7 aprile 2026). |
| WindTre | La banda 2100 MHz è spenta dal 7 giugno 2024. La banda 900 MHz resta attiva; a settembre 2025 WindTre ha tolto la scadenza del 31 dicembre 2025 (L, Mondomobileweb, 21 settembre 2025). La delibera AGCOM 217/26/CONS, approvata il 10 settembre 2026 e pubblicata il 13 ottobre 2026, autorizza una prova di spegnimento "software" per alcuni clienti WindTre e Very Mobile, senza data di inizio (L, TLC World). | Attivo (L, Mondomobileweb 21 settembre 2025: "insieme al 2G"). |
| Iliad | Nessuna rete 3G propria nei miei risultati. La prova AGCOM di ottobre 2026 non la riguarda (L, TLC World). | Un forum e un articolo dicono che Iliad usa la rete WindTre in condivisione e il 2G WindTre in roaming nazionale (R, non verificato su fonte ufficiale). |

Sul 2G nessun operatore ha una data ufficiale. Key4biz scrive il 7 aprile 2026 che TIM, Vodafone, WindTre, Iliad e gli operatori virtuali lo supportano ancora, e SmartWorld scrive il 17 agosto 2026 che resta acceso per tutelare i dispositivi M2M e la copertura vocale in montagna e nelle zone rurali, con il 5,2% del tempo di connessione ancora su 2G o 3G (L, entrambi). Un riassunto di ricerca attribuisce a una risposta alla consultazione del Ministero la scadenza dei diritti d'uso su 900 e 1800 MHz al 31 dicembre 2029 (R, non verificato: il PDF era illeggibile).

Fonti: https://www.tuttoandroid.net/news/2022/06/14/switch-off-3g-tim-iniziato-date-951466/ , https://www.tecnoandroid.it/news/3g-addio-vodafone-spegne-rete-802685/ , https://www.mondomobileweb.it/307836-windtre-switch-off-3g-stop-al-2100-mhz-la-900-mhz-resta-attiva-per-ora/ , https://tlcworld.it/windtre-very-mobile-switch-off-3g-agcom-delibera-217-26-cons-sperimentazione-software/ , https://www.key4biz.it/2g-la-francia-avvia-lo-spegnimento-entro-il-2026-e-in-italia/568586/ , https://www.smartworld.it/news/spegnimento-reti-2g-3g-europa-italia.html

### 1.4 Un dispositivo solo 2G è ancora sensato nel 2026?

Oggi funziona su tutti e quattro gli operatori, quindi per una prova di pochi mesi è accettabile. Per un prodotto da vendere ad aziende con una vita attesa di cinque anni o più non lo consiglio, per tre motivi.

- Non c'è nessuna garanzia: manca una data ufficiale, ma le ipotesi di settore cadono tra il 2029 e il 2031 (sopra), cioè dentro la vita di un tracker comprato oggi.
- Teltonika stessa lo dice: un suo collaboratore ha risposto sul forum ufficiale il 5 maggio 2025 che l'FMB920 funziona solo con la rete 2G e che per il 4G serve l'FMC920, e il 23 giugno 2025 che l'FMC920 è stato pensato per la chiusura delle reti 2G (L, https://community.teltonika.lt/t/fmb920-4g-network/13591 ).
- La differenza di prezzo è piccola. Su Getic.it (prezzi con IVA 22%) l'FMB920 2G costa 36,40 euro e l'FMC920 4G 66,80 euro; su GoTracker-Store (senza IVA) 28,00 contro 41,00 euro (L, sezione 2).

Il 3G invece è un vicolo cieco: i modelli solo 3G, come il Queclink GV300W (UMTS 850/1900/2100 con ripiego GSM, L su Visiotech) o il Sinotrack ST-906W, vanno scartati perché TIM e Vodafone lo hanno già spento.

Un'avvertenza sull'FMC920: un riassunto di ricerca riporta che la pagina Teltonika dell'FMC920 e quella dell'FMB920 portano l'etichetta "End of life" con un rimando a un prodotto sostitutivo, senza date (R). Non ho potuto confermarlo perché le pagine Teltonika si caricano con JavaScript e lo strumento ne vede solo il titolo. Il wiki Teltonika però raccomanda ancora per l'FMC920 un firmware del 1 luglio 2025 (L, https://wiki.teltonika-gps.com/view/FMC920_Firmware_Changelog ). Prima di ordinare scorte conviene chiedere al distributore se l'FMC920 è ancora in produzione, e in alternativa guardare l'FMC130 o l'FMC003.

### 1.5 Vincolo di architettura: serve un ricevitore TCP, non una funzione HTTP

Questa nota non era nella richiesta, ma cambia la scelta. I tracker Teltonika, Queclink, Jimi e simili aprono una connessione TCP o UDP verso l'indirizzo e la porta impostati e parlano un protocollo binario o testuale proprio (Teltonika usa Codec 8 e Codec 8 Extended, con l'IMEI inviato per primo e una risposta di conferma del server; L, https://wiki.teltonika-gps.com/view/Teltonika_Data_Sending_Protocols ). Le Netlify Functions sono documentate come richiesta-risposta HTTP (L, https://docs.netlify.com/build/functions/overview/ ), e la pagina dei limiti delle Edge Functions di Supabase non parla di ascolto su porte TCP in ingresso (L, https://supabase.com/docs/guides/functions/limits ). Concludo, come inferenza mia e non come fatto letto, che Supabase e Netlify non possono essere il punto di arrivo diretto dei tracker.

Serve quindi un piccolo servizio sempre acceso con un IP pubblico (un VPS) che riceva i pacchetti, li decodifichi e li inoltri a Supabase via HTTPS. Traccar, software libero, decodifica tutti i protocolli di questa ricerca (Teltonika sulla porta 5027, Queclink gl200 su 5004, Concox GT06 su 5023, Jimi VL502 jt808 su 5015, Sinotrack ST-901 h02 su 5013, Micodus MV720 h02 su 5013, Coban TK103 su 5002, Ruptela su 5046; L, https://www.traccar.org/devices/ ) e può inoltrare ogni posizione a un URL in formato JSON (L, https://www.traccar.org/forward/ ).

---

## 2 Modelli e prezzi

Tutti i prezzi sono stati visti il 29 ottobre 2026. La colonna "Cod." dice se il prezzo è stato letto sulla pagina (L) o riportato da una ricerca (R). Per i negozi che mostrano prezzi senza IVA ho aggiunto, solo dove utile, il calcolo con IVA 22% come mia aritmetica, ma non so se quel negozio applichi l'IVA italiana a un acquirente italiano (sezione 3).

### 2.1 Schede tecniche

| Modello | Tipo | Rete | Alimentazione | Protocollo | Server configurabile |
|---|---|---|---|---|---|
| Teltonika FMB920 | Cablato compatto, 1 ingresso digitale, 1 analogico, 1 uscita | Solo 2G (GSM/GPRS quad-band) | 6-30 V, batteria di riserva 170 mAh, nessun 1-Wire (L) | Codec 8 / 8 Extended; Traccar "teltonika" porta 5027 | Sì. Nel Configurator, "First Server Settings": dominio o IP, porta, TCP o UDP (L, wiki FMC920 GPRS settings) |
| Teltonika FMC920 | Come FMB920 ma 4G | LTE Cat 1 (10/5 Mbps) con ripiego 2G; moduli QJIB0 (bande B1/3/7/8/20/28) e QKIB0 | 10-30 V, batteria 170 mAh, nessun 1-Wire (L) | Come sopra | Sì, come sopra |
| Teltonika FMB003 | Spina OBD-II | Solo 2G | 12-30 V, batteria di riserva 45 mAh; legge dati CAN e OBD (L, Xpatit) | Come sopra | Sì |
| Teltonika FMC003 | Spina OBD-II | LTE Cat 1 con ripiego 2G; bande FDD 1/3/7/8/20/28, TDD 38/40/41; Micro-SIM (L, Getic.it) | Non letta | Come sopra | Sì |
| Teltonika FMB140 | Cablato con lettore dati CAN | 2G (L, GoTracker-Store) | Non letta | Come sopra | Sì |
| Teltonika FMC130 | Cablato avanzato | LTE Cat 1; 3G e 2G di ripiego nelle varianti con modulo EC21 | 10-30 V, batteria 170 mAh; 1-Wire per iButton o sensore di temperatura, CAN a bassa velocità, 3 ingressi digitali, 2 analogici, 3 uscite (L) | Come sopra | Sì |
| Teltonika FMB125 | Cablato avanzato | Solo 2G (modulo TM2500 quad-band, GPRS classe 12) | 10-30 V, batteria 170 mAh; 1-Wire, RS232, RS485 (L) | Come sopra | Sì |
| Teltonika FMC150 | Cablato con CAN integrato | 4G Cat 1 (L, GoTracker-Store e Getic) | Non letta | Come sopra | Sì |
| Teltonika FTC134 | Per rimorchi e logistica, alimentato con batteria di riserva 320 mAh | LTE Cat 1 con ripiego GSM; bande 1/3/5/8/20/28 | 8-32 V (L, Getic.com) | Come sopra | Sì |
| Teltonika TAT141 | A batteria con magnete | LTE Cat M1 | Batteria | Come sopra | Sì |
| Teltonika TAT240 | A batteria, antimanomissione | LTE Cat 1 con ripiego 3G/2G | Batteria | Come sopra | Sì |
| Queclink GV300W | Cablato | Solo 3G/2G (UMTS 850/1900/2100 più GSM) | Non letta | @Track (Traccar "gl200", porta 5004) | Sì, con comandi AT (M) |
| Queclink GL320MG | A batteria, SOS | LTE Cat M1 e Cat NB2 con ripiego 2G; molte bande (L, cctvengros.dk) | Batteria ricaricabile, circa 300 ore (R) | Come sopra | Sì (M) |
| Queclink GV310LAU | Cablato | LTE Cat 4 (R, catalogo) | Non letta | Come sopra | Sì (M) |
| Jimi VL502 | Spina OBD-II | LTE Cat 1 con ripiego 2G (L, kosprod.com). Esistono due varianti di bande (R) | Non letta | JT808 (Traccar, porta 5015); "jimi" (Navixy) | Sì, via SMS o piattaforma; il comando esatto non l'ho letto |
| Jimi JM-VL03 | Cablato nascondibile | 4G LTE | 9-90 V (L, Navixy) | "jimi" (Navixy, porta 47755); in Traccar non ho trovato la voce esatta | Sì: comando SMS SERVER,0,IP,porta,0# riportato da un rivenditore (R); da verificare sul manuale |
| Concox/Jimi GT06N | Cablato mini | Esiste in 2G e in 4G, secondo il venditore (R) | Non letta | gt06 (Traccar, porta 5023) | Sì, via SMS (R) |
| Ruptela FM-Eco4, FM-Pro4 | Cablato professionale | Famiglia 2G e 4G (R) | FM-Pro4: 10-32 V (R) | ruptela (Traccar, porta 5046) | Sì (M) |
| Sinotrack ST-901 | Cablato mini | 2G/3G con batteria 150 mAh; la ST-901L è 4G (L, GPS-Trace e titoli AliExpress) | Dati discordanti nelle schede: da 9 a 36, 80 o 90 V (R) | h02 (Traccar, porta 5013) | Sì: SMS 804, password, spazio, IP, spazio, porta; risposta "SET OK" (L, GPS-Trace) |
| Micodus MV720 | Cablato con relè, 2G | 2G (R, scheda Alibaba) | Non letta | h02 (Traccar, porta 5013) | Sì: SMS adminip, password, IP, porta (L, GPS-Trace) |
| Micodus MV730 / MV730G | Come sopra, versione 4G | 4G (L, AliExpress) | 9-90 V (titolo AliExpress) | h02 | Come sopra |
| Coban TK103 | Cablato 2G | GSM/GPRS quad-band (L, AliExpress) | Non letta | tk103 (Traccar, porta 5002) | Teoricamente sì con adminip; sui cloni i comandi spesso non funzionano (R, forum Traccar) |

Fonti delle schede: https://wiki.teltonika-gps.com/view/FMB920_General_description , https://wiki.teltonika-gps.com/view/FMC920_General_description , https://wiki.teltonika-gps.com/view/FMC130_General_description , https://wiki.teltonika-gps.com/view/FMB125_General_description , https://wiki.teltonika-gps.com/view/FMC920_GPRS_settings , https://www.xpatit.gr/en/iot-smart/teltonika-fmb003-advanced-plug-and-track-device-with-bluetooth-detail.html , https://www.getic.it/product/teltonika-fmc003 , https://www.getic.com/product/teltonika-ftc134 , https://www.traccar.org/devices/ , https://www.navixy.com/devices/jimi-iot-concox/jimi-iot-jm-vl03 , https://gps-trace.com/devices/sinotrack-st-901 , https://gps-trace.com/en/devices/micodus-mv720 , https://www.visiotechsecurity.com/en/products/mobility/trackers-884/queclink-883/ql-gv300w-detail , https://cctvengros.dk/produkt/ql-gl320mg/

### 2.2 Prezzi nei negozi

| Modello | Negozio | Prezzo | Condizione | Disponibilità | URL | Data | Cod. |
|---|---|---|---|---|---|---|---|
| FMB920 | Getic.it (Lettonia) | 36,40 euro | IVA 22% Italia inclusa (intestazione pagina) | In magazzino | https://www.getic.it/product/teltonika-fmb920 | 2026-10-29 | L |
| FMB920 | GoTracker-Store (Francia) | 28,00 euro | IVA esclusa sulle schede FMC130 e FMB003; sulla scheda FMB920 non l'ho aperta (circa 34,16 euro con IVA 22%, mio calcolo) | In offerta | https://gotracker-store.com/en/ | 2026-10-29 | L |
| FMB920 | Industry-Electronics/Lieske (Germania) | 33,87 euro (28,46 netti) | Solo aziende | 1 pezzo, consegna circa 13 giorni lavorativi, spedizione 24 euro | https://industry-electronics.com/teltonika/fmb920-tracker-gps-vehicle-gnss-gsm-ble-4.0-lieske_530736.htm | 2026-10-29 | L |
| FMB920 | Secutek.it (Italia) | 55,00 euro | IVA inclusa (45,08 netti) | Non disponibile, 20 giorni lavorativi | https://www.secutek.it/localizzatore-gps-teltonika-fmb920-e128143.htm | 2026-10-29 | L |
| FMC920 | Getic.it | 66,80 euro | IVA 22% | In magazzino | https://www.getic.it/shop/teltonika-gps-trackers | 2026-10-29 | L |
| FMC920 | GoTracker-Store | 41,00 euro; scatola da 20 pezzi 799,80 euro (39,99 l'uno) | Come sopra | Non indicata | https://gotracker-store.com/en/tracker-3g-4glte/33-fmc920-lte4g.html | 2026-10-29 | L (dall'elenco in home) |
| FMC920 | iot-shop.de (Germania) | 51,05 euro | IVA tedesca 19% inclusa, spedizione a parte, spedizione verso l'Italia non indicata | Non indicata | https://iot-shop.de/en/shop/tet-fmc920-teltonika-telematics-fmc920-tracker-11126 | 2026-10-29 | L |
| FMC920 | Lieske | 57,22 euro (48,08 netti) | Solo aziende | Su ordinazione, circa 20 giorni lavorativi | https://industry-electronics.com/teltonika/fmc920-tracker-gps-lieske_1994104.htm | 2026-10-29 | L |
| FMC920 | Linitx (Regno Unito) | 56,39 sterline | IVA britannica inclusa | Esaurito | https://linitx.com/product/teltonika-fmc920-4g-lte-cat1-obd-gnss-bluetooth-advanced-gps-tracker-fmc920lo7801/17219 | 2026-10-29 | L |
| FMB003 | Getic.it | 71,17 euro | IVA 22% | In magazzino | https://www.getic.it/shop/fleet-management | 2026-10-29 | L |
| FMB003 | GoTracker-Store | 56,00 euro (5 pezzi: 50,99; 20 pezzi: 49,50) | IVA esclusa | 60 pezzi | https://gotracker-store.com/en/tracker-2g/29-teltonika-fmb003.html | 2026-10-29 | L |
| FMB003 | Xpatit (Grecia) | 79,00 euro (63,71 netti) | IVA greca 24% inclusa | Disponibile | https://www.xpatit.gr/en/iot-smart/gps-trackers/3073-teltonika-fmb003-advanced-plug-and-track-device-with-bluetooth | 2026-10-29 | L |
| FMC003 | Getic.it | 103,24 euro | IVA 22% | In magazzino | https://www.getic.it/product/teltonika-fmc003 | 2026-10-29 | L |
| FMC003 | GoTracker-Store | 72,00 euro | IVA esclusa | Non indicata | https://gotracker-store.com/en/ | 2026-10-29 | L (elenco in home) |
| FMB140 | Getic.it | 108,38 euro | IVA 22% | Esaurito, in preordine | https://www.getic.it/product/teltonika-fmb140 | 2026-10-29 | L |
| FMB140 | GoTracker-Store | 71,99 euro | IVA esclusa | Non indicata | https://gotracker-store.com/en/ | 2026-10-29 | L (elenco in home) |
| FMB140 | Wifi-Stock | 85,21 dollari (ordini fino a 500 dollari) | Prezzo in dollari | Meno di 10 pezzi | https://wifi-stock.com/details/teltonika-gprsgnss-tracker-with-can-data-reading-feature-fmb140.html | 2026-10-29 | L |
| FMC130 | Getic.it | 71,36 euro | IVA 22% | In magazzino | https://www.getic.it/product/teltonika-fmc130 | 2026-10-29 | L |
| FMC130 | GoTracker-Store | 48,00 euro (10 pezzi: 43,99) | IVA esclusa | 190 pezzi, spedizione entro 24 ore | https://gotracker-store.com/en/tracker-3g-4glte/34-fmc130-4g.html | 2026-10-29 | L |
| FMB125 | Voelkner.de (Germania) | 36,05 euro | IVA inclusa, spedizione a parte, spedizione verso l'Italia non indicata | In magazzino, consegna 4-6 giorni | https://www.voelkner.de/products/4847843/FMB125-GNSS-GSM-Bluetooth-Tracker.html | 2026-10-29 | L |
| FMB125 | GoTracker-Store | 33,00 euro | IVA esclusa | Non indicata | https://gotracker-store.com/en/ | 2026-10-29 | L (elenco in home) |
| FMC150 | Getic.it | 113,24 euro | IVA 22% | In magazzino | https://www.getic.it/shop/fleet-management | 2026-10-29 | L |
| FMC150 | GoTracker-Store | 80,00 euro | IVA esclusa | Non indicata | https://gotracker-store.com/en/ | 2026-10-29 | L (elenco in home) |
| FTC134 (rimorchi, 4G) | Getic.com | 44,33 euro | IVA esclusa | In magazzino | https://www.getic.com/product/teltonika-ftc134 | 2026-10-29 | L |
| TAT141 (LTE-M, batteria) | Ascend (Germania) | 71,38 euro | IVA esclusa, solo clienti aziendali | Non disponibile | https://shop.ascend.de/en/products/teltonika-telematics-tat141-asset-tracker-4g-tat141bkbp01 | 2026-10-29 | L |
| TAT240 (4G, batteria) | Wifi-Stock | 89,03 dollari | Prezzo in dollari | Esaurito | https://wifi-stock.com/details/teltonika-tamper-proof-asset-tracker-with-4g-lte-cat-1-connectivity.html | 2026-10-29 | L |
| FMC920 e FMC150 | Galaxus.it | FMC920 59,94 euro, FMC150 circa 119 euro meno l'8% | IVA inclusa, spedizione gratuita | Non so | https://www.galaxus.it/en/s4/product/teltonika-4g-bluetooth-small-gps-gps-navigation-accessories-37723311 | 2026-10-29 | R (le pagine vanno in timeout) |
| Queclink GV300W | Visiotech | Prezzo visibile solo dopo il login | Non so | Non so | https://www.visiotechsecurity.com/en/products/mobility/trackers-884/queclink-883/ql-gv300w-detail | 2026-10-29 | L (assenza di prezzo) |
| Queclink GL320MG | cctvengros.dk (Danimarca) | 1.031,25 corone danesi, circa 138 euro a 7,46 corone per euro (conversione mia) | IVA esclusa, negozio per installatori e aziende | In magazzino, consegna 1-4 giorni | https://cctvengros.dk/produkt/ql-gl320mg/ | 2026-10-29 | L |
| Queclink GV310 | Nessuno | Nessun prezzo trovato | | | | | |
| Jimi VL502 | kosprod.com | 83,71 euro | IVA non indicata; contatto con prefisso +383 (Kosovo), quindi probabilmente fuori dall'UE | Arrivo indicato dal 30 ottobre al 2 novembre 2026 | https://kosprod.com/product/vl502 | 2026-10-29 | L |
| Jimi JM-VL03 (listato come Concox VL03) | AliExpress | 93,39 euro | Venditore non indicato | Non indicata | https://www.aliexpress.com/w/wholesale-jimi-vl502.html | 2026-10-29 | L |
| Concox GT06N 4G | AliExpress | 26,19 euro | Venditore non indicato; esistono anche GT06 2G a 26,89 euro | Spedizione gratuita da 10 euro | https://www.aliexpress.com/w/wholesale-gt06n.html | 2026-10-29 | L |
| Jimi LL301 (magnetico, 4G, 10.000 mAh) | aio.lv (Lettonia) | 111 euro | IVA non indicata | Esaurito | https://aio.lv/en/product--concox-ll301--11039940.md | 2026-10-29 | L |
| Ruptela FM-Eco4 e FM-Pro4 | Nessuno | Nessun prezzo pubblico trovato; solo distributori e preventivi | | | | | |
| Sinotrack ST-901 (varie versioni) | AliExpress | Da 16,39 euro (ST-901AL 2G/4G) a 30,19 euro (ST-901L 4G); la maggior parte 19-27 euro | Spedizione gratuita; la pagina avverte degli oneri di importazione extra UE | Non indicata | https://www.aliexpress.com/w/wholesale-sinotrack-st-901.html | 2026-10-29 | L |
| Sinotrack ST-901L, ST-902L (OBD), ST-906L, ST-915L | Amazon.it | Prezzo non leggibile con lo strumento | | | https://www.amazon.it/ST-901L-4G-localizzatore-Localizzazione-dispositivo/dp/B09NCZMNNM | 2026-10-29 | L (pagina esiste, prezzo non estratto) |
| Micodus MV730G (4G, relè) | AliExpress | 43,39 e 47,29 euro; MV730 2G/4G 23,09 euro; MV710G 27,29 euro | Spedizione gratuita sui primi due | | https://www.aliexpress.com/w/wholesale-micodus-mv730.html | 2026-10-29 | L |
| Micodus MV720 | AliExpress | Non in elenco; la scheda Alibaba lo dà a 10,99-12,75 dollari con ordine minimo di 2 pezzi | | | https://electronics.alibaba.com/product/mv720-micodus | 2026-10-29 | R |
| Coban TK103 | AliExpress | 20,09 euro | 2G quad-band, spedizione non indicata | | https://www.aliexpress.com/w/wholesale-coban-tk103.html | 2026-10-29 | L |
| Coban TK103-B | eBay.it | 39,99 euro | Venditore professionale | | https://www.ebay.it/itm/272003264352 | 2026-10-29 | R (eBay blocca lo strumento) |

### 2.3 Giudizio sui modelli economici cinesi

- Sinotrack ST-901 e Micodus MV720: sono comprabili e il server si cambia con un SMS, ma le schede danno informazioni contraddittorie su rete e tensione. La ST-901 base è 2G/3G (L), quindi inutile in futuro. Per il Micodus MV720 la CISA ha pubblicato nel luglio 2022 l'avviso ICSA-22-200-01 con sei vulnerabilità, la più grave valutata 9,8 su 10 (CVE-2022-2107, una password master scritta nel codice del server). La prima versione dell'avviso diceva che non c'erano correzioni; l'aggiornamento A dice che Micodus avrebbe corretto, ma è una dichiarazione del produttore (R, https://www.cisa.gov/ics/advisories/icsa-22-200-01 e https://pcper.com/tag/mv720-gps-tracker/ ). Se i dati vanno al nostro server il rischio sulla piattaforma del produttore diminuisce, ma il dispositivo resta senza aggiornamenti verificabili.
- Coban TK103: è il capostipite di una famiglia di cloni. I thread del forum Traccar descrivono cloni che si connettono e si disconnettono senza mandare dati e comandi SMS che non funzionano (R, https://www.traccar.org/forums/topic/data-from-tk103b-clone-does-not-reach-the-server/ ). È 2G, quindi vale quanto detto in 1.4.
- Sulla stessa AliExpress compare un servizio a pagamento di "attivazione IMEI" per i tracker DAGPS (GT02, GT06, TK200) a 10,29 euro (L): segnala che alcuni modelli sono legati alla piattaforma del venditore.
- Non li consiglierei per un prodotto che il cliente rivende ad altre aziende: nessuna garanzia europea utilizzabile, nessun canale di aggiornamento del firmware, qualità variabile da un lotto all'altro. Vanno bene per un banco di prova.

---

## 3 Dove si comprano

DenkiCode non ha partita IVA (vincolo aziendale), quindi i negozi riservati alle aziende non sono utilizzabili da noi. Li potrebbe usare l'impresa del padre di Sebastian, che una partita IVA ce l'ha.

| Negozio | Sede | Vende a | URL | Spedizione | Note |
|---|---|---|---|---|---|
| Getic.it e Getic.com | Lettonia (Getic SIA, Liepaja) | Non dichiara limiti; il sito in italiano mostra prezzi con IVA 22% Italia (L) | https://www.getic.it/shop/teltonika-gps-trackers | Il costo si calcola per prodotto in base al paese e al numero di pezzi, non visibile senza carrello. Corrieri UPS, FedEx, DHL, GLS; spedizione entro 24-48 ore lavorative; consegna tipica espressa 1-2 giorni (L) | Sulla scheda prodotto si dichiara "Official Teltonika Distributor" (L); non l'ho potuto confermare sul sito Teltonika. Garanzia 24 mesi, reso 30 giorni, pagamento con carta o bonifico. La versione .com mostra gli stessi prezzi senza IVA. |
| GoTracker-Store | Francia (Thiais) | Non dichiarato (le parole "distributor" e "reseller" nel sito suggeriscono anche rivenditori) | https://gotracker-store.com/en/ | Solo UPS con tracking, spedizione entro 2 giorni dal pagamento (pagina Delivery) o 24 ore (scheda prodotto). Paesi serviti e costi non indicati (L) | Prezzi senza IVA (sulle schede FMC130 e FMB003) e sconti a quantità. Per l'Italia serve chiedere per email: contact@gotracker-store.com. Catalogo più ampio: tutti i modelli della sezione 2 più accessori. |
| Industry-Electronics (Lieske) | Germania | Solo clienti industriali, commerciali e enti pubblici (L) | https://industry-electronics.com/delivery-costs-to-italy | Verso l'Italia con GLS 24,00 euro o DHL 22,50 euro per la spedizione di esempio; 3-4 giorni lavorativi al Nord e al Centro, 4-5 al Sud. Con partita IVA UE l'IVA si paga in Italia (inversione contabile); senza, si applica il 19% tedesco (L) | Prezzi bassi ma su ordinazione per molti articoli (13-20 giorni). |
| Ascend (shop.ascend.de) | Germania | Solo clienti aziendali (L) | https://shop.ascend.de/en/products/teltonika-telematics-tat141-asset-tracker-4g-tat141bkbp01 | Non indicata | Utile per TAT141 e altri asset tracker. |
| Voelkner.de | Germania | Privati (30 giorni di reso gratuito per i prodotti venduti da loro) | https://www.voelkner.de/products/4847843/FMB125-GNSS-GSM-Bluetooth-Tracker.html | Prezzo a parte, destinazione Italia non indicata | Non l'ho usato per altro che FMB125. |
| iot-shop.de | Germania | Non dichiarato | https://iot-shop.de/en/shop/tet-fmc920-teltonika-telematics-fmc920-tracker-11126 | Spese a parte, paesi non indicati | Prezzi con IVA tedesca 19%. |
| Xpatit | Grecia | Non dichiarato | https://www.xpatit.gr/en/iot-smart/gps-trackers/3073-teltonika-fmb003-advanced-plug-and-track-device-with-bluetooth | Calcolatore di spedizione senza importi in pagina | Prezzi con IVA greca 24%. |
| Secutek.it | Italia | Privati e aziende (prezzi IVA inclusa) | https://www.secutek.it/localizzatore-gps-teltonika-fmb920-e128143.htm | 20 giorni lavorativi per l'FMB920 in arrivo | Unico negozio italiano trovato con un prezzo Teltonika; modello solo 2G, ora non disponibile. |
| Mirifica | Germania/UE (negozio con sito .it) | Non dichiarato | https://www.mirifica.it/teltonika/vehicle-telematics/vehicle-trackers/teltonika-fmb920-fota-web-technical-support_100003_1076/ | Non letta (la pagina ha risposto 404) | Vende l'FMB920 con accesso a Teltonika FOTA Web e un anno di supporto tecnico (R). L'accesso FOTA Web lo gestisce solo chi ha venduto il dispositivo (R, wiki Mirifica). |
| Galaxus.it | Svizzera | Privati | https://www.galaxus.it/en/s4/product/teltonika-4g-bluetooth-small-gps-gps-navigation-accessories-37723311 | Spedizione gratuita secondo il riassunto di ricerca (R) | Le pagine hanno dato timeout; esistono schede per FMC920, FMB920, FMB003 e FMC150. |
| Amazon.it | Italia | Privati e aziende | https://www.amazon.it/s?k=sinotrack+st-901 | Spedizione gratuita su ordini idonei (meta descrizione della pagina, L) | Ci sono SinoTrack ST-901L, ST-902L (OBD), ST-906L, ST-915L, TKMARS TK915 e TK918, e le SIM Things Mobile. Nei risultati non ho trovato Teltonika, Micodus o Jimi su Amazon.it. Il prezzo non si legge con lo strumento. |
| AliExpress | Cina (prezzi mostrati in euro per l'Italia) | Privati | https://www.aliexpress.com/w/wholesale-sinotrack-st-901.html | Molte inserzioni con spedizione gratuita; la pagina avverte che per i pacchi extra UE si applicano oneri di importazione (L) | Vedi sotto. |

Distributori ufficiali Teltonika in Italia: non sono riuscito a trovare una lista. La pagina "dove comprare" del sito Teltonika non l'ho trovata (404), e il wiki dice solo che Teltonika vende già in Italia senza fare nomi (R). L'unico che si dichiara distributore ufficiale è Getic (sulla propria scheda); non ho verificato la dichiarazione. Per saperlo con certezza si può scrivere al commerciale Teltonika. Una nota utile: sul forum Teltonika un collaboratore ha ricordato che la scelta del dispositivo e il canale di vendita restano responsabilità del cliente, che deve rivolgersi al proprio sales manager (L, forum Teltonika).

AliExpress, dogana e IVA. Dal 1 luglio 2026 l'Unione europea applica un dazio fisso temporaneo di 3 euro per articolo sui pacchi extra UE di valore fino a 150 euro; si conta per voce doganale, non per quantità (L, Commissione europea, https://commission.europa.eu/news-and-media/news/ensuring-fairness-and-safety-eur3-customs-duty-low-value-parcels-2026-06-29_it ). L'IVA resta dovuta. Sulla Commissione il venditore o l'importatore dichiara e paga il dazio, ma altri siti scrivono che il costo ricade sul compratore su piattaforme come AliExpress, e le fonti non concordano (R, https://www.shippypro.com/blog/it/riforma-doganale-ue-2026 e https://www.mysolution.it/fisco/informazioni/news/2026/07/03/dazio-forfettario-di-3-euro-su-pacchi-extra-ue.-nuove-faq-della-commissione-europea ). I tempi di consegna dalla Cina non li ho verificati.

---

## 4 SIM dati

### 4.1 Quanti MB al mese consuma un tracker

| Situazione | MB al mese | Fonte |
|---|---|---|
| Una posizione ogni 5 minuti, pacchetto da 175 byte | circa 1,44 | GPS-Trace, calcolo con formula (L) |
| Una posizione ogni 10 secondi, pacchetto da 175 byte | circa 43,3 | GPS-Trace (L) |
| Una posizione ogni ora | circa 0,12 | GPS-Trace (L) |
| Utente reale: una posizione ogni 20 secondi, 8 ore al giorno, SIM emnify | circa 27; l'operatore arrotonda ogni sessione al KB, quindi chiudere la connessione dopo ogni pacchetto fa salire il totale | Forum Traccar (L) |
| Valore generico per un tracker | da 1 a 10, di più se invia più dati più spesso | Things Mobile (L) |
| Localizzatore per auto o moto | da 100 MB a 1 GB secondo la frequenza (stima larga) | Selectra (L) |
| Record Teltonika | minimo 45 byte con tutti gli I/O spenti, massimo 783 | Wiki Mirifica (R) |

Per un mezzo di lavoro con una posizione ogni 30 secondi per 8 ore al giorno in 22 giorni lavorativi i record sono 21.120 al mese. A 60-100 byte l'uno fanno circa 1,3-2,1 MB di dati utili, e con intestazioni TCP/IP e arrotondamenti dell'operatore la stima sale a 5-15 MB. Questa stima è mia, non è un dato di fonte. Per pianificare i costi conviene contare 10-30 MB al mese per veicolo.

Fonti: https://gps-trace.com/en/blog/consumption-of-mobile-traffic-gps-trackers , https://www.traccar.org/forums/topic/new-user-data-consumption/ , https://www.thingsmobile.com/q-a/how-much-data-traffic-does-a-gps-tracker-use , https://selectra.net/internet/attualita/sim-2-50-euro-allarme-casa-localizzatore-gps , https://mirifica.atlassian.net/wiki/x/FYBZHg , https://community.teltonika.lt/t/monitor-used-mobile-traffic-on-fmc920/16680

### 4.2 Confronto delle SIM

| Fornitore | Prezzo | Copertura e tecnologie | Note | URL | Data | Cod. |
|---|---|---|---|---|---|---|
| Things Mobile (IoT) | Business con canone: 0,02 euro/MB in Zona 1 più 2 euro al mese per SIM, 0,25 euro il primo collegamento di ogni mese, 3 euro al mese per l'account del portale. Business senza canone: 0,10 euro/MB con addebito minimo di 5 MB. Privati senza canone: 0,12 euro/MB. SIM gratuita con 2,50 euro di attivazione. | La Zona 1 comprende l'Italia, gli altri paesi UE e gli USA; multi-operatore 2G/3G/4G (inserzioni Amazon) | Si compra su thingsmobile.com e su amazon.it, da privati e da aziende. Le inserzioni Amazon parlano di 10 euro di credito incluso, senza canone fisso né scadenza. La pagina dei prezzi che ho letto non ha data. Il mio calcolo: il piano con canone conviene sopra 25 MB al mese, quello senza canone sotto. | https://faq.thingsmobile.com/article/719-what-are-the-features-of-the-pay-as-you-go-plans , https://faq.thingsmobile.com/article/820-where-can-i-purchase-a-things-mobile-sim-card | 2026-10-29 | L |
| 1NCE | 12 euro una tantum per 10 anni, 500 MB e 250 SMS | 2G, 3G, 4G/LTE-M e NB-IoT dove disponibile, oltre 170 paesi; l'Italia non è nominata nelle pagine che ho letto, serve la lista per paese scaricabile | Ordine da shop.1nce.com, SIM in 2-3 giorni lavorativi. IVA non indicata sulla pagina; un risultato di ricerca dice che i 10 euro del lancio erano netti, con IVA e spedizione a parte (R). 500 MB in 10 anni sono 4,2 MB al mese: bastano per un rimorchio che segnala poco, non per un mezzo attivo. Un thread del forum Arduino del 2022 riporta SIM 1NCE non funzionanti acquistate da un rivenditore italiano e accesso al portale negato a chi ne compra una sola (R). | https://1nce.com/en-eu/1nce-connect , https://1nce.com/en-eu/1nce-connect/our-coverage , https://forum.arduino.cc/t/sim-providers-for-mkr-nb-1500-europe-italy/956217.md | 2026-10-29 | L (prezzo e copertura generale); R (forum) |
| emnify | Nessun prezzo pubblico: la pagina dei prezzi non ha cifre e rimanda al commerciale | Piano Europa senza costi aggiuntivi dal 31 gennaio 2022 | Un utente del forum Traccar riporta un pacchetto base da circa 5 MB e un costo che sale di 3-4 volte oltre 30 MB al mese (L, post non datato). | https://www.emnify.com/pricing , https://www.emnify.com/blog/new-emnify-iot-tariffs-europe-usa | 2026-10-29 | L |
| Hologram | 3 dollari per SIM, 1 dollaro al mese, 0,03 dollari/MB, 0,19 dollari per SMS inviato | Oltre 550 reti in più di 190 paesi; l'Italia non è nominata | Per 10 MB al mese fanno circa 1,30 dollari (mio calcolo). Prove gratuite disponibili. | https://www.hologram.io/pricing/ | 2026-10-29 | L |
| Soracom (Plan X3-EU) | Da 4,50 euro per un anno con 25 MB al mese, poi 0,38 euro al mese; IVA esclusa | LTE-M, 4G e NB-IoT dove disponibili | I dati vengono da comunicati del 2023 e 2024; la pagina ufficiale dei prezzi non si è letta e il costo della SIM non è indicato. | https://www.iotevolutionworld.com/iot/articles/456512-soracoms-new-affordable-data-plan-european-innovators-iot.htm , https://iotbusinessnews.com/?p=41660 | 2026-10-29 | R |
| Telnyx | 1 dollaro per SIM, da 0,0125 dollari/MB in Italia, nessun minimo | Più di 650 reti, 4G, 3G, 2G e LTE-M; passa da solo a un'altra rete se una cade | Non richiesto nell'incarico, lo cito perché ha un prezzo chiaro. | https://telnyx.com/sim-cards/italy | 2026-10-29 | L |
| Very Mobile, offerta "Very Things" | 1,99 euro al mese per 2 GB, 3,99 euro al mese per 10 GB; SIM e spedizione gratuite | Very Mobile è un marchio WindTre (M; la delibera AGCOM li cita insieme, L). 5G fino a 30 Mbps, valida in Europa tranne il Regno Unito (R, Tecnoandroid) | Offerta "per dispositivi smart", solo per nuovi numeri. Al superamento dei GB la navigazione si blocca. Niente eSIM. L'articolo del 25 luglio 2025 dava le condizioni valide fino al 4 agosto 2025, quindi vanno riverificate; il prezzo di oggi invece è letto sul sito di Very. | https://www.verymobile.it/offerte , https://www.tecnoandroid.it/2025/07/25/very-mobile-liot-diventa-accessibile-con-le-nuove-very-things-1598046/ | 2026-10-29 | L (prezzi); R (condizioni) |
| CoopVoce "ConMe Casa" | 2,50 euro al mese (primo mese gratis), 500 MB in 4G; attivazione 10 euro, di cui 1 euro resta come credito; solo numero nuovo | 4G | Descritta come "pensata per gli oggetti connessi"; l'articolo avverte che alcuni dispositivi datati funzionano solo su reti vecchie. Tre anni costano 97,50 euro. | https://selectra.net/internet/attualita/sim-2-50-euro-allarme-casa-localizzatore-gps | 2026-10-26 (data dell'articolo) | L |
| Iliad, ho., Kena (prepagate consumer) | Iliad: attivazione 9,99 euro; Giga 150 a 7,99 euro, Giga 200 a 9,99 euro al mese. ho.: 5,95 euro al mese per 100 GB (Sostariffe, ottobre 2026), ma un altro sito dice che l'offerta è stata tolta. Kena: 4,99 euro per 150 GB, 5,99 euro per 200 GB | 4G e 5G | Prezzi riportati da siti di confronto tra giugno e ottobre 2026, mai dal sito dell'operatore: i siti ufficiali di Iliad, ho. e Kena davano errore 404 allo strumento. Sono troppi GB per un tracker: pagano un servizio da telefono. | https://www.sostariffe.it/news/mobile-5g-e-tanti-giga-le-offerte-sotto-10-euro-da-confrontare-a-ottobre-2026-411272/ , https://offerta-internet.it/operatori/kena-mobile/70-giga | 2026-10-29 | R |

### 4.3 I problemi della SIM consumer

- Scadenza per inattività. Iliad disattiva la SIM dopo 12 mesi consecutivi senza uso né ricarica (R: la Carta dei servizi riportata dai riassunti; SmartWorld del 2021 conferma l'avviso di sospensione dopo 12 mesi, L), e il numero resta recuperabile per altri 12 mesi. Secondo Money.it del 23 aprile 2024 TIM disattiva dopo 12 mesi più 1, Vodafone dopo 11 mesi più circa 4 settimane, WindTre dopo 12 mesi più 30 giorni (L). Money.it non tratta Kena (Vodafone) né Very (WindTre), quindi non confermo che valgano le stesse regole. Un tracker che trasmette ogni giorno non resta mai inattivo, ma una SIM scorta ferma sullo scaffale sì.
- Ricarica e credito. Le offerte mensili si pagano dal credito residuo o con ricarica automatica: se la carta scade o il credito finisce, la SIM si ferma e il mezzo sparisce dalla mappa. Con Very Things la navigazione si blocca anche al raggiungimento dei GB (R).
- PIN. Il PIN della SIM va disattivato prima di inserirla nel tracker, altrimenti il dispositivo non si collega (M, non verificato in questa ricerca).
- Titolarità. Le prepagate italiane si attivano a nome di una persona con documento (M, non verificato qui); per le SIM di mezzi di clienti diversi è scomodo e non scala.
- Condizioni d'uso. Non sono riuscito a verificare se Iliad, ho., Kena e Very vietino l'uso in dispositivi M2M. Una guida consiglia di leggere nelle condizioni la voce su IoT, M2M o router (R). Very Things e CoopVoce ConMe Casa sono le uniche offerte consumer trovate che dichiarano di essere per oggetti connessi.
- Roaming. Le SIM IoT estere (1NCE, Things Mobile, Hologram, emnify) lavorano in roaming su reti italiane: non ho trovato né una conferma né un divieto di "roaming permanente" in Italia, quindi va provato con una SIM prima di ordinarne molte (sezione 7).

### 4.4 Valutazione

Per la prova con pochi mezzi la scelta più pratica è Things Mobile Business: costo chiaro per MB, Italia inclusa, portale per vedere il consumo, acquistabile anche su Amazon.it e senza scadenza. Una SIM Very Things a 1,99 o 3,99 euro costa meno al mese ma è consumer, intestata a una persona e con condizioni da leggere. La 1NCE da 12 euro conviene solo per rimorchi e container che segnalano poche volte al giorno. Per una flotta da gestire per conto di terzi servono SIM con portale e API (Things Mobile, Hologram, emnify, Soracom), perché permettono di attivare, sospendere e leggere il consumo senza toccare le schede.

---

## 5 Installazione

### 5.1 Chi installa e quanto costa

Nessuna fonte che ho trovato pubblica un listino reale di elettrauto. Le cifre vengono tutte da fornitori e comparatori, e vanno trattate come ordini di grandezza.

| Voce | Cifra | Fonte |
|---|---|---|
| Manodopera per un tracker cablato | 50-150 euro per veicolo; pacchetti con installazione inclusa per flotte di 5-10 mezzi o più | Companeo, pagina aggiornata il 12 marzo 2026 (L) |
| Stessa voce, altra guida dello stesso sito | 80-150 euro nella tabella, 150-250 euro nel testo: la pagina è incoerente | Companeo, aggiornata il 2 aprile 2026 (L) |
| Installazione indicata da un altro sito, data non visibile | circa 70 euro; 35 euro se si installa un solo dispositivo | Bonifica-ambientale (L) |
| Tempo di lavoro | 45-60 minuti (Companeo), 30-60 minuti con un elettrauto o un installatore (Trackyup) | L |
| Spostare il dispositivo da un veicolo a un altro | circa 100 euro a intervento | Riassunto di ricerca (R) |
| Costo del servizio di un operatore italiano per confronto | canone di 6 euro più IVA per veicolo al mese, con la manodopera dell'installatore esclusa dal canone e dal prezzo del kit | Trackyup, Brescia (L) |

Chi installa: un elettrauto o un installatore di autoradio. Trackyup spiega di non avere tecnici propri e di appoggiarsi a installatori locali; per l'area di Milano non cita nomi (L). Per avere un prezzo vero bisogna chiedere due o tre preventivi a elettrauto della zona, specificando modello, numero di mezzi e se serve la batteria di riserva.

Fonti: https://www.companeo.it/localizzazione-satellitare-veicoli/FAQ/costo-installazione-gps-auto-aziendale , https://www.companeo.it/localizzazione-satellitare-veicoli/guide/localizzatore-gps-obd-cablato-batteria , https://www.bonifica-ambientale.it/quanto-costa-installare-un-gps-in-auto/ , https://trackyup.com/installazione-assistenza/

### 5.2 OBD-II: autoinstallazione

Si infila nella presa diagnostica, in meno di due minuti se la presa è libera (Trackyup, L). Il lato negativo è che si vede e si stacca (Companeo, L). Per nasconderla si può usare una prolunga OBD2: Getic.it ne vende a 9,96 euro e 12,54 euro (L, https://www.getic.it/shop/fleet-management ). Il FMB003 legge dati CAN e OBD con diversi protocolli per auto (ISO 9141-2, ISO 14230-4, ISO 15765-4, ISO 14229, J2819; L, Xpatit), quindi è pensato per auto e furgoni leggeri.

### 5.3 Cablato: dove si nasconde

Companeo lo descrive come "nascosto nel veicolo e collegato alla centralina" (L). Non ho trovato una guida con i punti di montaggio. Da memoria mia, non verificata: si monta dietro il cruscotto o sotto il piantone, con l'antenna GNSS rivolta verso il cielo e non sotto lamiere, e con tre fili da collegare (positivo permanente, massa, accensione sotto chiave); l'installatore sa fare questo lavoro.

### 5.4 Mezzi a 24 V e camion

Elettricamente i Teltonika cablati reggono i 24 V: FMC130, FMC920 e FMB125 vanno da 10 a 30 V, l'FMB920 da 6 a 30 V, l'FMB003 da 12 a 30 V, l'FTC134 da 8 a 32 V (L, wiki Teltonika, Xpatit e Getic). Nel Jimi JM-VL03 l'ingresso va da 9 a 90 V (L, Navixy). La presa OBD dei camion invece non è quella delle auto: i camion usano spesso J1939 o FMS su connettore a 9 poli. Teltonika vende un adattatore da OBD-II a 9 poli, ma è pensato per il mercato nordamericano; per i camion europei esiste un adattatore da OBD-II a FMS da usare con modelli come l'FMC880 (R, https://teltonika-gps.com/products/accessories/data-cables/obd-ii-to-9-pin-adapter e https://www.teltonika-gps.com/products/accessories/data-cables/obd-ii-to-fms-adapter ). Per i furgoni da 12 V la spina OBD va bene. Per i camion o i mezzi a 24 V conviene un cablato 10-30 V come l'FMC130, senza affidarsi alla presa OBD.

---

## 6 La legge in Italia

Premessa: questa è una raccolta di fonti, non una consulenza legale. I tre punti centrali sono confermati da fonti dirette (testo di legge, comunicato del Ministero del lavoro, provvedimenti del Garante). I dettagli di alcune circolari vengono da commenti di terzi e li segnalo con "R".

### 6.1 Chi decide: i clienti sono i titolari, noi siamo il fornitore

Le aziende clienti che mettono il GPS sui propri mezzi sono i titolari del trattamento dei dati. Chi gestisce la piattaforma per loro è il fornitore del servizio di localizzazione, che il datore di lavoro deve nominare responsabile del trattamento con un contratto ai sensi dell'articolo 28 del GDPR (L, Agenda Digitale, 11 settembre 2024, https://www.agendadigitale.eu/sicurezza/privacy/tracciamento-gps-sul-lavoro-come-rispettare-statuto-dei-lavoratori-e-gdpr/ ; già il provvedimento del Garante del 2011 imponeva di nominare responsabili i fornitori esterni, L). Se il servizio fosse offerto da Sebastian Torres, o da DenkiCode per lui, sarebbe quindi il responsabile, con obblighi propri (contratto, misure di sicurezza, divieto di usare i dati per altro).

### 6.2 Articolo 4 dello Statuto dei lavoratori (legge 300/1970, come modificato dal D.Lgs. 151/2015)

Il testo vigente sta su Normattiva (https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1970-05-20;300~art4 ). Il riassunto letto è questo.

- Comma 1. Gli impianti e gli strumenti da cui deriva anche la possibilità di controllo a distanza dei lavoratori si possono usare solo per esigenze organizzative e produttive, per la sicurezza del lavoro e per la tutela del patrimonio aziendale. Per installarli serve un accordo con le rappresentanze sindacali aziendali (RSA) o unitarie (RSU). Se l'impresa ha unità in più province o regioni, l'accordo può essere firmato dalle associazioni sindacali più rappresentative a livello nazionale. In mancanza di accordo serve l'autorizzazione della sede territoriale dell'Ispettorato nazionale del lavoro, o della sede centrale se le unità ricadono in più sedi territoriali. Questi provvedimenti sono definitivi.
- Comma 2. Le regole del comma 1 non valgono per gli strumenti che il lavoratore usa per rendere la prestazione e per gli strumenti di registrazione degli accessi e delle presenze.
- Comma 3. Le informazioni raccolte si possono usare per tutti i fini connessi al rapporto di lavoro, compresi quelli disciplinari, solo se il lavoratore riceve un'adeguata informazione sulle modalità d'uso degli strumenti e dei controlli, e nel rispetto del Codice privacy.

### 6.3 Il GPS non è "strumento di lavoro" secondo l'INL

- Circolare INL n. 2 del 7 novembre 2016. Il comunicato del Ministero del lavoro, che ho letto, riassume così: i sistemi di localizzazione satellitare sono in generale un elemento aggiunto agli strumenti di lavoro, non servono in via primaria a rendere la prestazione, rispondono a esigenze assicurative, organizzative, produttive o di sicurezza, e quindi ricadono nell'articolo 4, comma 1. L'installazione è ammessa con accordo sindacale o con autorizzazione dell'Ispettorato (L, https://lavoro.gov.it/node/8311 ). Il testo integrale della circolare non l'ho letto. Un commento di EC News del 24 maggio 2017 aggiunge che il GPS rientra tra gli strumenti di lavoro solo se la prestazione non si può rendere senza di esso o se una norma lo impone (esempio: il trasporto di valori sopra una soglia di 1.500.000 euro), e che la nota 5689/2016 della Direzione del lavoro di Milano, che la pensava diversamente, è stata superata (R, https://www.ecnews.it/lavoro/speciale-della-settimana/geolocalizzazione-veicoli-aziendali-luce-indicazioni-inl-garante/ ).
- Conferme nel 2026. La nota INL n. 1511 del 16 febbraio 2026 (guardie giurate) ribadisce che il GPS non è strumento necessario alla prestazione, che un decreto ministeriale non può derogare alla legge e che va seguita la procedura del comma 1 (L, commento su https://www.testo-unico-sicurezza.com/geolocalizzazione-delle-guardie-giurate.html ). La nota INL n. 831 del 28 gennaio 2026 (tracciabilità dei rifiuti, RENTRI) dice che il GPS usato solo per adempiere a quell'obbligo non ricade nell'articolo 4, ma che ogni altro uso lo riporta dentro, perché conta anche la sola possibilità di controllo (L, commento su https://www.securlav.it/2026/02/23/rentri-e-controlli-a-distanza-linl-chiarisce-lapplicazione-dellart-4-dello-statuto-dei-lavoratori/ ). Per i furgoni e i camion di cui parliamo non ho trovato un obbligo di legge che imponga il GPS (diverso dal caso dei portavalori o dei rifiuti): l'eccezione degli "strumenti di lavoro" quindi, con ogni probabilità, non si applica.

Conseguenza pratica: prima di montare il primo GPS su un mezzo guidato da un dipendente, il cliente deve avere l'accordo sindacale o l'autorizzazione dell'Ispettorato. Il Garante ha sanzionato anche aziende che avevano l'accordo ma non rispettavano i suoi limiti (sotto, casi 2025 e 2026).

### 6.4 I provvedimenti del Garante privacy

| Data e numero | Contenuto | Fonte |
|---|---|---|
| 4 ottobre 2011, n. 370, doc. web 1850581: "Sistemi di localizzazione dei veicoli nell'ambito del rapporto di lavoro" | Provvedimento generale. Il consenso non è necessario perché la base è l'interesse legittimo, ma solo se si rispettano le garanzie dell'articolo 4. Informativa completa ai dipendenti e cartello visibile sul veicolo, con modello nell'allegato 1. Accesso ai dati solo a chi ne ha bisogno. Posizione da non monitorare in modo continuo. I dati serviti per il Libro unico del lavoro si conservano 5 anni, solo per le informazioni obbligatorie; gli altri vanno cancellati o resi anonimi quando il servizio è concluso. Parte del testo (la notifica al Garante) è superata dal GDPR. | https://www.garanteprivacy.it/garante/doc.jsp?ID=1850581 (L) |
| 16 marzo 2017, n. 138 | Verifica preliminare su un'azienda. Un commento riporta tra le prescrizioni: trattamento non continuativo, 90 giorni di conservazione con cancellazione automatica per le contestazioni, 30 secondi prima e dopo l'evento in caso di sinistro, 5 anni per il Libro unico. Non ho aperto il provvedimento. | https://www.ecnews.it/lavoro/speciale-della-settimana/geolocalizzazione-veicoli-aziendali-luce-indicazioni-inl-garante/ (R) |
| 24 maggio 2017, n. 247, doc. web 6495708 | Anconambiente. Una rilevazione ogni 30 secondi è sproporzionata; deve avvenire "ad eventi". La visione in tempo reale è ammessa solo per anomalie predeterminate, come una sosta oltre un tempo massimo non inferiore a cinque minuti. I percorsi si possono conservare 5 anni solo dopo anonimizzazione dell'intera flotta. | https://www.garanteprivacy.it/garante/doc.jsp?ID=6495708 (L) |
| 11 ottobre 2018, n. 467, doc. web 9058979 | Elenco dei trattamenti per cui la valutazione d'impatto (DPIA) è obbligatoria. Secondo commenti di terzi vi rientrano i trattamenti nel rapporto di lavoro con strumenti tecnologici, tra cui la geolocalizzazione, da cui possa derivare un controllo a distanza. L'allegato con l'elenco non l'ho letto. | https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9058979 (L per titolo e data); contenuto R, Agenda Digitale |
| 16 gennaio 2025, n. 7, doc. web 10112287 | Sanzione di 50.000 euro a Autotrasporti Cuccu Riccardo S.r.l. Unipersonale, per circa 50 dipendenti geolocalizzati. Contestati: informativa piena di incongruenze, posizione rilevata anche durante le pause (monitoraggio continuo), conservazione di 180 giorni non conforme alla minimizzazione, funzioni non rispettose dell'autorizzazione dell'Ispettorato, mancata risposta alle richieste del Garante. Ordinato di rifare l'informativa e adeguare il trattamento entro 60 giorni. | https://www.garanteprivacy.it/garante/doc.jsp?ID=10112287 (L) |
| 28 maggio 2026, n. 382, doc. web 10259916 | Sanzione di 6.000 euro all'Azienda Tutela della Salute per la Liguria. Posizione rilevata ogni 60 secondi, giudicata pervasiva (poi portata a 15 minuti); visualizzazione in tempo reale che l'azienda ha disattivato; DPIA fatta in ritardo, con violazione dell'articolo 35; accordo sindacale del 2018 necessario ma non sufficiente; dati usati in un procedimento disciplinare senza le condizioni del comma 3. Conservazione dichiarata dall'azienda: 6 mesi. | https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10259916 (L) |
| 2026 (numero non letto) | Sanzione di 39.000 euro a una società di vigilanza: ha negato a un lavoratore l'accesso ai dati GPS che gli servivano per difendersi in un procedimento disciplinare e non aveva dato l'informativa. Commento del 16 ottobre 2026; resto dell'articolo a pagamento. | https://www.mysolution.it/lavoro/approfondimenti/commenti/2026/10/gps-sullauto-aziendale-dal-garante-sanzione-da-39mila-euro/ (R) |

Un provvedimento del Garante del 2016 sul tema non l'ho trovato. Gli atti del 2016 che ho trovato sono la circolare INL e la nota della Direzione del lavoro di Milano (6.3).

### 6.5 Informativa, conservazione dei dati, DPIA

- Informativa a due livelli. Un'informativa breve, come un adesivo sul vetro con la scritta che il veicolo è sottoposto a localizzazione (modello nell'allegato 1 del provvedimento del 2011), e un'informativa estesa ai sensi dell'articolo 13 del GDPR che spiega dati raccolti, finalità, base giuridica, funzionamento del sistema, intervalli di rilevazione e tempi di conservazione (L, Agenda Digitale; L, Garante 2011). Il Garante nel 2025 ha ritenuto insufficiente un'informativa con tempi di conservazione generici e senza indicare la rilevazione continuativa. Per i dipendenti il consenso non è una base valida (R, Agenda Digitale).
- Tempi di conservazione. La legge non fissa un numero unico: dipendono dalla finalità. I riferimenti dei provvedimenti sono 5 anni per i soli dati del Libro unico, 90 giorni per le contestazioni e una finestra di 30 secondi attorno a un sinistro (questi ultimi due solo da commento, R). Nel 2025 il Garante ha giudicato eccessivi 180 giorni; nel 2026 non ha sanzionato la conservazione di 6 mesi, ma ha sanzionato la frequenza di 60 secondi.
- DPIA. È obbligatoria per questi trattamenti secondo commenti che citano l'elenco del 2018 (R) e il Garante l'ha contestata nel 2026 (L).
- Registro dei trattamenti, lettere di incarico al personale che accede ai dati e contratto con il fornitore sono richiesti dallo stesso commento di Agenda Digitale (L).
- Diritto di accesso. Il lavoratore può chiedere i propri dati di localizzazione e il titolare deve rispondere; è l'oggetto delle sanzioni del 2023 (20.000 euro a una società di lettura contatori, R, dottrinalavoro.it) e del 2026 (39.000 euro, R).

### 6.6 Se il mezzo è guidato dal titolare o da un collaboratore non dipendente

Non ho trovato una fonte che tratti questo caso: la ricerca specifica non ha dato risultati (le fonti parlano solo di dipendenti). Quello che segue è ragionamento mio, da fare confermare da un consulente del lavoro.

- L'articolo 4 tutela i lavoratori subordinati. Se il mezzo è guidato solo dal titolare dell'impresa, dai soci che lavorano in proprio o da lavoratori autonomi con partita IVA, la procedura sindacale o dell'Ispettorato probabilmente non serve.
- Il GDPR si applica comunque, perché la posizione di una persona fisica identificabile è un dato personale anche se la persona è il titolare. Servono informativa e una base giuridica; per un autonomo il consenso è più difendibile che per un dipendente, ma resta meglio basarsi sul contratto o sull'interesse legittimo.
- Le zone grigie sono le collaborazioni coordinate e continuative organizzate dal committente e le cooperative di facchinaggio con soci lavoratori: se è presente anche un solo lavoratore subordinato sul mezzo, torna l'articolo 4. Nel settore facchinaggio e traslochi capita spesso, quindi la regola prudente è trattare ogni mezzo come guidato da dipendenti.

### 6.7 Cosa significa per l'app

Dalle sanzioni 2025 e 2026 discende che la piattaforma dovrebbe permettere a ogni cliente di scegliere una frequenza di rilevazione bassa, di non vedere il tempo reale in modo permanente, di spegnere il tracciamento durante pause e fuori dall'orario di lavoro, di impostare un tempo di cancellazione automatica, di tenere un registro degli accessi ai dati e di esportare i dati di un lavoratore che li chiede. Sono considerazioni mie sul prodotto, tratte dalle motivazioni dei provvedimenti.

---

## 7 Cosa non ho potuto verificare

Strumenti. WebFetch restituisce il riassunto di un modello piccolo, non il testo grezzo: un numero o una frase possono essere trascritti male. Ho incrociato i prezzi dove potevo, ma i dati che finiranno in un preventivo vanno ricontrollati aprendo la pagina. La data "2026-10-29" nelle tabelle è il giorno in cui ho letto la pagina, non il giorno in cui il negozio ha fissato il prezzo.

Prezzi e negozi.
- Amazon.it: le pagine esistono, ma pesano circa 1 MB di codice e lo strumento non arriva al prezzo. Nessun prezzo Amazon.it nel rapporto.
- eBay.it e eBay.de: lo strumento viene bloccato (errore 403). I prezzi eBay compaiono solo come riassunti di ricerca.
- Galaxus.it: timeout su tutte le pagine; i prezzi riportati sono solo da riassunto di ricerca.
- Queclink: i prezzi di Visiotech sono dietro login, l'unico prezzo trovato è un negozio danese per aziende; per GV310 non ho trovato né prezzo né negozio europeo.
- Ruptela: nessun prezzo pubblico; vende tramite distributori con preventivo.
- Jimi VL502: l'unico negozio con prezzo in euro è probabilmente fuori dall'UE (Kosovo). Non ho trovato un rivenditore UE con prezzo del VL502 o del JM-VL03.
- Spedizione verso l'Italia: non ho visto il costo di Getic (si calcola nel carrello), né di GoTracker-Store, Voelkner, iot-shop, Xpatit. Non so se GoTracker-Store venda a privati né se applichi l'IVA italiana a un privato italiano.
- Distributore ufficiale Teltonika in Italia: non trovato; la lista sul sito Teltonika non si è aperta. La dichiarazione di Getic non è verificata.
- Stato di fine vita dell'FMC920 e dell'FMB920: da un riassunto di ricerca, non confermato.

Reti.
- Completamento dello spegnimento 3G di TIM e Vodafone: verificate le date programmate, non la data di completamento reale.
- Come Iliad usi il 2G e il 3G in Italia: solo da forum e articoli, non da fonte ufficiale.
- Scadenza dei diritti d'uso 900/1800 MHz al 31 dicembre 2029: viene da un riassunto di ricerca; il PDF della consultazione era illeggibile.
- Copertura 1NCE in Italia: la lista per paese da scaricare non è stata aperta.
- Se le reti italiane accettano senza problemi SIM IoT estere in roaming permanente (1NCE, Things Mobile, Hologram, emnify, Soracom): non ho trovato né conferma né divieto. Va provato con una SIM sola prima di ordinarne molte.
- Disponibilità attuale di LTE-M e NB-IoT per ciascun operatore nel 2026: i dati sono del 2017-2022.

SIM.
- Condizioni d'uso M2M di Iliad, ho., Kena, Very: non verificate. I siti ufficiali di Iliad, ho. e Kena davano errore 404.
- Scadenza per inattività di Kena e Very: non trovata.
- Prezzi di emnify, Soracom e Simbase: pagine ufficiali non leggibili (emnify non ha prezzi pubblici).
- La data della pagina dei prezzi Things Mobile che ho letto non c'è.

Installazione.
- Nessun listino di elettrauto: tutte le cifre vengono da fornitori e comparatori, e due guide dello stesso sito si contraddicono.
- Posizioni di montaggio e cablaggio: da memoria mia.
- Comandi SMS di Jimi, Queclink e Coban: i comandi per Sinotrack e Micodus li ho letti su GPS-Trace; quello di Jimi viene da un rivenditore; quelli di Queclink e Ruptela sono da memoria. Prima di usarli servono i manuali.

Legge.
- Il testo integrale della circolare INL 2/2016 e quello del provvedimento del Garante 138/2017 non li ho letti; il secondo è noto solo da un commento. L'elenco allegato al provvedimento 467/2018 non si è aperto.
- Il caso dei non dipendenti (titolare, soci, autonomi, collaboratori): nessuna fonte trovata, la sezione 6.6 è ragionamento mio.
- La notifica al Garante dei sistemi di localizzazione, richiesta fino al 2018, non serve più con il GDPR: lo ricordo a memoria e i provvedimenti 2025 e 2026 non la citano. Non l'ho verificato.
- Il numero e la data del provvedimento da 39.000 euro non compaiono nel testo accessibile.
- Questo rapporto non sostituisce un consulente del lavoro o un avvocato.

Specifiche non lette: tensione e bande di FMC003, FMB140, FMC150, GV310 e VL502; batteria di riserva dell'FMB140 e dell'FMC150.

Architettura. L'affermazione che Supabase e Netlify non possono ricevere direttamente i pacchetti dei tracker è una mia inferenza dalla documentazione: la documentazione non lo dice con una frase esplicita.

---

## 8 Fonti

Dispositivi, documentazione e protocolli
- https://wiki.teltonika-gps.com/view/FMB920_General_description
- https://wiki.teltonika-gps.com/view/FMC920_General_description
- https://wiki.teltonika-gps.com/view/FMC130_General_description
- https://wiki.teltonika-gps.com/view/FMB125_General_description
- https://wiki.teltonika-gps.com/view/FMC920_GPRS_settings
- https://wiki.teltonika-gps.com/view/FMC920_Firmware_Changelog
- https://wiki.teltonika-gps.com/view/Teltonika_Data_Sending_Protocols
- https://community.teltonika.lt/t/fmb920-4g-network/13591
- https://community.teltonika.lt/t/monitor-used-mobile-traffic-on-fmc920/16680
- https://mirifica.atlassian.net/wiki/x/FYBZHg
- https://www.traccar.org/devices/
- https://www.traccar.org/forward/
- https://www.traccar.org/forums/topic/new-user-data-consumption/
- https://www.traccar.org/forums/topic/data-from-tk103b-clone-does-not-reach-the-server/
- https://www.navixy.com/devices/jimi-iot-concox/jimi-iot-jm-vl03
- https://www.navixy.com/devices/jimi-iot-concox/jimi-jm-vl502/
- https://gps-trace.com/devices/sinotrack-st-901
- https://gps-trace.com/en/devices/micodus-mv720
- https://gps-trace.com/en/blog/consumption-of-mobile-traffic-gps-trackers
- https://www.cisa.gov/ics/advisories/icsa-22-200-01
- https://pcper.com/tag/mv720-gps-tracker/
- https://teltonika-gps.com/products/accessories/data-cables/obd-ii-to-9-pin-adapter
- https://www.teltonika-gps.com/products/accessories/data-cables/obd-ii-to-fms-adapter
- https://docs.netlify.com/build/functions/overview/
- https://supabase.com/docs/guides/functions/limits

Negozi
- https://www.getic.it/product/teltonika-fmb920
- https://www.getic.it/product/teltonika-fmc003
- https://www.getic.it/product/teltonika-fmb140
- https://www.getic.it/product/teltonika-fmc130
- https://www.getic.it/shop/teltonika-gps-trackers
- https://www.getic.it/shop/fleet-management
- https://www.getic.it/delivery
- https://www.getic.com/delivery
- https://www.getic.com/shop/teltonika-gps-trackers
- https://www.getic.com/product/teltonika-ftc134
- https://gotracker-store.com/en/
- https://gotracker-store.com/en/tracker-3g-4glte/34-fmc130-4g.html
- https://gotracker-store.com/en/tracker-2g/29-teltonika-fmb003.html
- https://gotracker-store.com/en/content/1-delivery
- https://industry-electronics.com/teltonika/fmb920-tracker-gps-vehicle-gnss-gsm-ble-4.0-lieske_530736.htm
- https://industry-electronics.com/teltonika/fmc920-tracker-gps-lieske_1994104.htm
- https://industry-electronics.com/delivery-costs-to-italy
- https://shop.ascend.de/en/products/teltonika-telematics-tat141-asset-tracker-4g-tat141bkbp01
- https://iot-shop.de/en/shop/tet-fmc920-teltonika-telematics-fmc920-tracker-11126
- https://linitx.com/product/teltonika-fmc920-4g-lte-cat1-obd-gnss-bluetooth-advanced-gps-tracker-fmc920lo7801/17219
- https://www.xpatit.gr/en/iot-smart/gps-trackers/3073-teltonika-fmb003-advanced-plug-and-track-device-with-bluetooth
- https://www.xpatit.gr/en/iot-smart/teltonika-fmb003-advanced-plug-and-track-device-with-bluetooth-detail.html
- https://www.voelkner.de/products/4847843/FMB125-GNSS-GSM-Bluetooth-Tracker.html
- https://wifi-stock.com/details/teltonika-gprsgnss-tracker-with-can-data-reading-feature-fmb140.html
- https://wifi-stock.com/details/teltonika-tamper-proof-asset-tracker-with-4g-lte-cat-1-connectivity.html
- https://www.secutek.it/localizzatore-gps-teltonika-fmb920-e128143.htm
- https://www.mirifica.it/teltonika/vehicle-telematics/vehicle-trackers/teltonika-fmb920-fota-web-technical-support_100003_1076/
- https://www.galaxus.it/en/s4/product/teltonika-4g-bluetooth-small-gps-gps-navigation-accessories-37723311
- https://cctvengros.dk/produkt/ql-gl320mg/
- https://www.visiotechsecurity.com/en/products/mobility/trackers-884/queclink-883/ql-gv300w-detail
- https://kosprod.com/product/vl502
- https://aio.lv/en/product--concox-ll301--11039940.md
- https://www.aliexpress.com/w/wholesale-sinotrack-st-901.html
- https://www.aliexpress.com/w/wholesale-micodus-mv730.html
- https://www.aliexpress.com/w/wholesale-micodus-mv720.html
- https://www.aliexpress.com/w/wholesale-coban-tk103.html
- https://www.aliexpress.com/w/wholesale-jimi-vl502.html
- https://www.aliexpress.com/w/wholesale-gt06n.html
- https://electronics.alibaba.com/product/mv720-micodus
- https://www.amazon.it/ST-901L-4G-localizzatore-Localizzazione-dispositivo/dp/B09NCZMNNM
- https://www.amazon.it/SinoTrack-Tracker-ST-902L-Tracking-tracciamento/dp/B09JZ3LF6Y
- https://www.ebay.it/itm/272003264352
- https://commission.europa.eu/news-and-media/news/ensuring-fairness-and-safety-eur3-customs-duty-low-value-parcels-2026-06-29_it
- https://www.shippypro.com/blog/it/riforma-doganale-ue-2026
- https://www.mysolution.it/fisco/informazioni/news/2026/07/03/dazio-forfettario-di-3-euro-su-pacchi-extra-ue.-nuove-faq-della-commissione-europea

Reti
- https://www.tuttoandroid.net/news/2022/06/14/switch-off-3g-tim-iniziato-date-951466/
- https://www.tecnoandroid.it/news/3g-addio-vodafone-spegne-rete-802685/
- https://www.mondomobileweb.it/307836-windtre-switch-off-3g-stop-al-2100-mhz-la-900-mhz-resta-attiva-per-ora/
- https://tlcworld.it/windtre-very-mobile-switch-off-3g-agcom-delibera-217-26-cons-sperimentazione-software/
- https://www.key4biz.it/2g-la-francia-avvia-lo-spegnimento-entro-il-2026-e-in-italia/568586/
- https://www.smartworld.it/news/spegnimento-reti-2g-3g-europa-italia.html
- https://telecoms.com/iot/vodafone-launches-italy-s-first-lte-m-network
- https://www.lightreading.com/iot/telecom-italia-covers-73-of-italy-with-nb-iot
- https://en.wikipedia.org/wiki/LTE-M

SIM
- https://faq.thingsmobile.com/article/719-what-are-the-features-of-the-pay-as-you-go-plans
- https://faq.thingsmobile.com/article/820-where-can-i-purchase-a-things-mobile-sim-card
- https://www.thingsmobile.com/q-a/how-much-data-traffic-does-a-gps-tracker-use
- https://1nce.com/en-eu/1nce-connect
- https://1nce.com/en-eu/1nce-connect/our-coverage
- https://forum.arduino.cc/t/sim-providers-for-mkr-nb-1500-europe-italy/956217.md
- https://www.emnify.com/pricing
- https://www.emnify.com/blog/new-emnify-iot-tariffs-europe-usa
- https://www.hologram.io/pricing/
- https://www.iotevolutionworld.com/iot/articles/456512-soracoms-new-affordable-data-plan-european-innovators-iot.htm
- https://iotbusinessnews.com/?p=41660
- https://telnyx.com/sim-cards/italy
- https://www.verymobile.it/offerte
- https://www.tecnoandroid.it/2025/07/25/very-mobile-liot-diventa-accessibile-con-le-nuove-very-things-1598046/
- https://selectra.net/internet/attualita/sim-2-50-euro-allarme-casa-localizzatore-gps
- https://www.sostariffe.it/news/mobile-5g-e-tanti-giga-le-offerte-sotto-10-euro-da-confrontare-a-ottobre-2026-411272/
- https://offerta-internet.it/operatori/kena-mobile/70-giga
- https://www.money.it/Scadenza-SIM-Tim-Vodafone-Wind-e-Tre
- https://www.smartworld.it/news/iliad-avvisa-clienti-della-disattivazione-del-numero-caso-sim-inattiva-mesi-279415.html

Installazione
- https://www.companeo.it/localizzazione-satellitare-veicoli/FAQ/costo-installazione-gps-auto-aziendale
- https://www.companeo.it/localizzazione-satellitare-veicoli/guide/localizzatore-gps-obd-cablato-batteria
- https://www.bonifica-ambientale.it/quanto-costa-installare-un-gps-in-auto/
- https://trackyup.com/installazione-assistenza/

Legge
- https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1970-05-20;300~art4
- https://lavoro.gov.it/node/8311
- https://www.ecnews.it/lavoro/speciale-della-settimana/geolocalizzazione-veicoli-aziendali-luce-indicazioni-inl-garante/
- https://www.fiscal-focus.it/quotidiano/il-quotidiano/articoli-lavoro/gps-sull-auto-aziendale-non-e-considerato-strumento-di-lavoro,3,81152
- https://www.testo-unico-sicurezza.com/geolocalizzazione-delle-guardie-giurate.html
- https://www.securlav.it/2026/02/23/rentri-e-controlli-a-distanza-linl-chiarisce-lapplicazione-dellart-4-dello-statuto-dei-lavoratori/
- https://www.garanteprivacy.it/garante/doc.jsp?ID=1850581
- https://www.garanteprivacy.it/garante/doc.jsp?ID=6495708
- https://www.garanteprivacy.it/garante/doc.jsp?ID=10112287
- https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10259916
- https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9058979
- https://www.agendadigitale.eu/sicurezza/privacy/tracciamento-gps-sul-lavoro-come-rispettare-statuto-dei-lavoratori-e-gdpr/
- https://www.cybersecurity360.it/legal/privacy-dati-personali/geolocalizzazione-di-veicoli-aziendali-dopo-il-gdpr-gps-a-norma/
- https://www.cybersecurity360.it/news/il-confine-tra-sicurezza-e-privacy-il-garante-sanziona-il-monitoraggio-gps-della-flotta-aziendale/
- https://www.osservatorio-dataprotection.it/data-protection/controllo-a-distanza-dei-dipendenti-il-garante-privacy-torna-a-sanzionare-luso-improprio-dei-sistemi-di-geolocalizzazione/
- https://www.dataprotectionlaw.it/2026/10/06/geolocalizzazione-dipendenti-gps-veicoli-aziendali-sanzioni/
- https://www.mysolution.it/lavoro/approfondimenti/commenti/2026/10/gps-sullauto-aziendale-dal-garante-sanzione-da-39mila-euro/
- https://www.dottrinalavoro.it/notizie-c/garante-privacy-il-dipendente-ha-diritto-di-accedere-ai-dati-sulla-geolocalizzazione
