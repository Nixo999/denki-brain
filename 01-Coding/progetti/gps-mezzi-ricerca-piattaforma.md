---
type: risorsa
riga: Rapporto integrale del 29/10/2026 su come ricevere le posizioni dei tracker - Codec 8, Traccar e inoltro, Supabase, tessere, costi, fase zero coi telefoni. Sintesi in gps-mezzi.
updated: 2026-10-29
source: claude
tags: [gps, flotta, ricerca, traccar, supabase]
---

> Rapporto scritto da un agente Sonnet il 29/10/2026 per [[gps-mezzi]]. Le
> etichette sono spiegate in testa. Nessuna persona ha ricontrollato i dati,
> salvo i nomi delle opzioni di inoltro di Traccar e il prezzo Hetzner
> (Trevis, 29/10). Le configurazioni d'esempio non sono state provate.

# Piattaforma di localizzazione GPS dei mezzi: ricerca tecnica

Data della ricerca: 29/10/2026. Autore: ricercatore tecnico (solo WebSearch e WebFetch, nessun repository toccato).

## Come leggere le etichette

- **[n]** rimanda alla fonte numero n nella sezione 7. La pagina è stata aperta e letta il 29/10/2026.
- **(sec.)** la notizia viene da una fonte secondaria: forum, aggregatore di prezzi, pagina di un terzo, oppure l'estratto di un risultato di ricerca senza aver aperto la pagina.
- **(mem.)** lo so da memoria e non l'ho verificato adesso.
- **(stima)** è un calcolo o un giudizio mio, non un dato di una fonte.

Quando una pagina non si apriva o non conteneva la risposta, lo scrivo nella sezione 6.

## Sintesi per chi ha fretta

- I tracker non parlano HTTP/JSON. Teltonika manda binario su TCP o UDP (Codec 8, 8 Extended, 16), Queclink manda soprattutto testo ASCII, Concox/Jimi e Ruptela mandano binario. Serve sempre un server in mezzo che ascolti su una porta TCP.
- La via consigliata è **Traccar in Docker su un VPS Hetzner piccolo**, che decodifica i protocolli e inoltra ogni posizione in JSON a **una Edge Function di Supabase**, che scrive in una tabella con **PostGIS**. Il browser riceve le posizioni da **Supabase Realtime** e le disegna con **MapLibre GL**.
- Le tessere della mappa si possono servire da un file **PMTiles** (Protomaps) ospitato su Supabase Storage, senza canone di un servizio terzo (il costo di Storage ed egress per quel file non l'ho verificato). Le tessere pubbliche di OpenStreetMap non sono vietate per uso commerciale dal testo della policy, ma sono senza garanzie e revocabili in qualsiasi momento.
- Costo mensile stimato per 10 mezzi, SIM escluse: circa 6 euro di VPS (IVA esclusa) più 25 dollari di Supabase Pro. Se esiste già un progetto Supabase Pro che può ospitare i dati, il costo aggiuntivo è solo il VPS.
- Una posizione ogni 30 secondi per 8 ore al giorno per 22 giorni per 10 mezzi produce 211.200 righe al mese, cioè circa 30-65 MB al mese (stima), contro 8 GB inclusi nel piano Pro. Lo spazio non è un problema; le query storiche e le aggregazioni lo diventano solo con centinaia di mezzi (stima).
- Per la fase zero senza hardware, l'app **Traccar Client** (gratuita, Android e iOS) manda posizioni al server Traccar già pronto. Va bene per validare dashboard e analisi in 2-4 settimane con pochi autisti; non va bene come prodotto.

---

## 1. Come parlano i tracker e come si configurano

### 1.1 Protocolli dei quattro marchi

| Marchio | Protocollo | Formato | Trasporto | Porta predefinita in Traccar | Come si punta al server |
|---|---|---|---|---|---|
| Teltonika (FMB, FMC) | Codec 8 (0x08), Codec 8 Extended (0x8E), Codec 16 (0x10); Codec 12 (0x0C) per i comandi verso il dispositivo | Binario | TCP o UDP [3][4] | 5027 [12] | SMS `setparam` o Teltonika Configurator [1] |
| Queclink | @Track Air Interface Protocol | **ASCII** nei dispositivi più vecchi (esempio `+RESP:GTFRI,270F01,...`); binario "Track Protocol Pro" nei più recenti, un solo formato per modello [9] | TCP o UDP (sec.) | 5004, ricavato dal nome della cartella dei documenti `5004-gl200` [11] | Comandi SMS `AT+GTBSI` (APN) e `AT+GTSRI` (server), da un sito di terzi [10] (sec.) |
| Concox / Jimi (GT06 e derivati) | GT06 | Binario: pacchetti che iniziano con 0x78 0x78 (corti) o 0x79 0x79 (lunghi), numero di protocollo 0x01 per il login, fine 0x0D 0x0A (sec., dai risultati di ricerca sui PDF Concox [16]) | TCP | 5023 [11] | SMS tipo `SERVER,0,IP,porta,0#` su un modello, ma la sintassi varia con modello e firmware (sec. [16]) |
| Ruptela | Protocollo Ruptela | Binario (sec. [17]) | TCP/UDP | 5046 [11] | Ruptela Configurator, parametri che cambiano con il firmware (sec.) |

Una correzione alla premessa: Queclink non usa solo protocolli binari. Il sito di flespi dice che i dispositivi Queclink più vecchi parlano un protocollo ASCII e quelli recenti un protocollo binario, e che ogni modello ne supporta uno solo [9].

Le porte di Traccar per Queclink, Concox e Ruptela le ho ricavate dai nomi delle cartelle dei documenti di protocollo sulla pagina `/protocols/` [11], che elenca 91 documenti. Per Teltonika la porta 5027 è scritta nella tabella dei dispositivi supportati [12]. Prima di fare il firewall conviene controllare le porte sul `traccar.xml` o sui log della propria installazione.

### 1.2 Come si configura un Teltonika FMB (esempio FMB920)

La pagina "First Start" del wiki Teltonika descrive due strade [1].

**Prima strada, SMS.** Si inserisce una micro-SIM con la richiesta del PIN disattivata, si alimenta il dispositivo a 6-30 V, e si manda un SMS con due spazi iniziali e questo formato [1]:

```
  setparam 2001:APN;2002:utente_APN;2003:password_APN;2004:dominio;2005:porta;2006:0
```

Gli identificatori hanno questo significato [1][2]:

| ID | Parametro | Valore predefinito | Note |
|---|---|---|---|
| 2001 | APN | vuoto | Access point della SIM |
| 2002 | Utente APN | vuoto | |
| 2003 | Password APN | vuota | |
| 2004 | Dominio del server | vuoto | Fino a 55 caratteri; la pagina GPRS dice che accetta indirizzo IP o nome di dominio [6] |
| 2005 | Porta | 0 | 0-65535 |
| 2006 | Protocollo di trasporto | 0 | 0 = TCP, 1 = UDP, 3 = MQTT [2] |
| 113 | Data Protocol | 1 (Codec 8 Extended) | La tabella indica l'intervallo 0-1, ma le opzioni includono 2 = Codec JSON [2] |
| 1000 | Open Link Timeout | 300 s | Quanto tempo il dispositivo tiene aperta la connessione dopo l'invio; 30-259200 s [2] |

Il limite di un SMS è 160 caratteri, e i comandi distinguono maiuscole e minuscole [7]. Dopo un SMS riuscito il dispositivo sincronizza l'ora e comincia a mandare i record al server [1].

**Seconda strada, Teltonika Configurator.** È un programma per Windows 10 (1607 o successivo) o Windows 11 a 64 bit con .NET 8 Desktop Runtime. Il dispositivo si collega via Micro-USB, dopo aver installato il driver COM, oppure via Bluetooth (nome "FMB920_" più le ultime 7 cifre dell'IMEI, password predefinita 5555). Le impostazioni del server e dell'APN stanno nella sezione **GPRS**, gli intervalli di invio nella sezione **Data Acquisition**, e le modifiche valgono solo dopo il pulsante **Save to device** [1].

### 1.3 Periodo di invio: in movimento e da fermo

Il dispositivo distingue due fasi: **registrare** un record (Min Period, Min Distance, Min Angle, Min Speed Delta) e **inviarlo** (Send Period). Zero disattiva il criterio corrispondente [8]. Valori predefiniti sulla rete "Home" dell'FMB920, dalla lista dei parametri [2]:

| Stato | Parametro | ID | Predefinito |
|---|---|---|---|
| Fermo ("Vehicle on STOP") | Min Period | 10000 | 3600 s |
| Fermo | Min Saved Records | 10004 | 1 |
| Fermo | Send Period | 10005 | 120 s |
| In movimento ("Vehicle MOVING") | Min Period | 10050 | 300 s |
| In movimento | Min Distance | 10051 | 100 m |
| In movimento | Min Angle | 10052 | 10 gradi |
| In movimento | Min Speed Delta | 10053 | 10 km/h |
| In movimento | Min Saved Records | 10054 | 1 |
| In movimento | Send Period | 10055 | 120 s |

La pagina "First Start" riassume lo stesso comportamento così: in movimento il dispositivo registra ogni 300 secondi, o dopo una curva di 10 gradi, o dopo 100 metri, o con una variazione di velocità sopra 10 km/h; da fermo con quadro spento registra dopo un'ora; un record registrato parte verso il server ogni 120 secondi [1].

Per ottenere una posizione ogni 30 secondi in movimento, con invio immediato, bisogna abbassare Min Period e Send Period della fase "in movimento". Un esempio costruito da me con gli ID letti sopra (da provare su un dispositivo vero, non l'ho potuto testare) è questo SMS, sempre con due spazi iniziali:

```
  setparam 10050:30;10055:30
```

Attenzione: gli ID 10000-10055 valgono per la rete "Home". Esistono gruppi separati per le reti "Roaming" (10100-10155) e "Unknown" (10200-10255), con valori predefiniti diversi; per esempio il Send Period in movimento in roaming parte da 0 [2]. Se la SIM è di un operatore estero o di un operatore IoT che il dispositivo non riconosce come "Home", valgono quei gruppi. Il dispositivo cerca l'operatore ogni 15 minuti [8].

Per i comandi dal server verso il dispositivo (per esempio riavviarlo) serve il Codec 12 su una sessione GPRS aperta; un dispositivo in Deep Sleep non riceve comandi GPRS [3][7].

### 1.4 Esiste un modo per fargli mandare JSON via HTTPS?

Nelle pagine Teltonika lette: no. La pagina "First Start" non cita HTTP né JSON e offre solo TCP o UDP [1]. La pagina sui protocolli di invio dati descrive TCP e UDP e non cita HTTP, MQTT o JSON [4]. La pagina delle impostazioni GPRS dell'FMB920 offre TCP o UDP [6], anche se la lista dei parametri ammette per l'ID 2006 anche il valore 3 = MQTT [2].

C'è un "Codec JSON", ma è fatto per **AWS IoT**: manda JSON su **MQTT con TLS** e un certificato x509, in due modi (AWS Shadow e AWS Custom, quest'ultimo con nomi dei topic a scelta), con firmware 03.28.00 Rev.00 o successivo. La pagina non cita HTTP né HTTPS [5]. Se un FMB possa pubblicare su un broker MQTT generico (per esempio Mosquitto) non l'ho trovato: un utente del forum di flespi racconta di non aver trovato nel Configurator dell'FMB920 i campi per utente, password e topic MQTT (sec. [14]).

Quindi in mezzo serve sempre un programma che ascolti una porta TCP (o UDP) e decodifichi il binario. Può essere Traccar, un gateway ospitato come flespi, oppure un server scritto da noi. Le Edge Function di Supabase e Netlify rispondono a richieste HTTP e non possono ascoltare una porta TCP aperta ai tracker (ragionamento mio, (stima)); per questo il VPS serve comunque.

### 1.5 Che cosa deve fare il server per un Teltonika (Codec 8)

Il protocollo ha due obblighi che un server fatto in casa deve rispettare [3]:

1. **Handshake dell'IMEI.** Il dispositivo manda 2 byte di lunghezza e l'IMEI in ASCII; il server risponde con un solo byte, 0x01 per accettare o 0x00 per rifiutare.
2. **Conferma dei dati (ACK).** Dopo ogni pacchetto di dati il server risponde con un intero di 4 byte che contiene il numero di record accettati. Se non coincide con quanto il dispositivo ha mandato, il dispositivo reinvia gli stessi dati.

Il pacchetto TCP ha un preambolo di quattro byte a zero, la lunghezza dei dati, il Codec ID, il numero di record (ripetuto in fondo) e un CRC-16/IBM [3].

Traccar fa esattamente questo: nel suo decodificatore Teltonika risponde con 1 o 0 all'IMEI secondo che il dispositivo sia registrato o no, e invia il numero di record come ACK sul TCP [44]. Conseguenza pratica: **un tracker il cui IMEI non è registrato in Traccar viene rifiutato senza messaggi evidenti**. L'opzione `database.registerUnknown` registra in automatico i dispositivi sconosciuti [19].

---

## 2. Le vie per ricevere i dati

### 2.1 Tabella di confronto

I prezzi sono quelli letti il 29/10/2026. I costi per 10 mezzi non comprendono le SIM né l'hardware.

| Via | Chi fa girare il server | Costo per 10 mezzi al mese | Marchio e app | Dati nostri | Manutenzione | Note principali |
|---|---|---|---|---|---|---|
| **Traccar su VPS nostro** | Noi | VPS Hetzner CX23: 5,49 euro + 0,50 di IPv4, IVA esclusa [68][69] | Nostri (usiamo solo l'API e l'inoltro) | Sì, nel Postgres di Traccar e in Supabase | Media: un servizio Java, un database, aggiornamenti frequenti | Licenza Apache 2.0, oltre 200 protocolli [26] |
| **Traccar ospitato da Traccar** | Traccar | Da 49,95 dollari al mese per un "Tracking Server" dedicato con marchio e configurazione propri; da 9,95 per un account su server condiviso. Prezzo per dispositivo non pubblicato [34] | Marchio proprio solo sul server dedicato | Sul loro server | Bassa | Alternativa senza amministrazione, non l'ho approfondita |
| **flespi** (gateway ospitato) | flespi | Piano gratuito: 10 dispositivi, "per test e sviluppo", limiti non estendibili. Piano commerciale: da 130 euro al mese [54] | Nostri | Nei loro server, con storage a pagamento oltre 1 GiB [55] | Bassa | Il minimo di 130 euro è circa 22 volte il costo del VPS; vedi 2.3 |
| **Server TCP nostro in Node (solo Codec 8)** | Noi | Lo stesso VPS, 5,99 euro | Nostri | Sì | Alta: tutto il protocollo è a nostro carico | Vedi 2.5 |
| **GpsGate Cloud** | GpsGate | 3 dollari per dispositivo al mese, minimo 5 unità: 30 dollari per 10 [57] | La pagina non parla di marchio proprio | Loro | Bassa | Prova di 30 giorni con simulatore; API solo per i piani enterprise [57] |
| **Navixy** | Navixy | Prezzo a consumo senza livelli, non pubblicato; si chiede un preventivo [59] | Esiste un percorso da agente/rivenditore [59] | Loro | Bassa | Le cifre sugli aggregatori sono incoerenti tra loro (sec. [60]) |
| **Wialon (Gurtam)** | Gurtam | Abbonamento mensile, prezzo non pubblicato; sconti per fatturato e per funzioni attivate [58] | Marchio proprio tramite Wialon Platform, non quantificato [58] | Loro | Bassa | Un aggregatore cita 150 dollari al mese di partenza (sec.) |
| **Teltonika** | n/d | n/d | n/d | n/d | n/d | Vedi 2.4: ha FOTA WEB, che gestisce i dispositivi, non è una piattaforma di tracciamento |

### 2.2 Traccar in dettaglio

**Versione attuale.** La pagina di download e quella Docker indicano la 6.16.0 [23][25]. Nella pagina delle release 6.16.0 risulta pubblicata il "27 Sep", senza anno; seguono la 6.15.3 il 26 agosto e le 6.15.2, 6.15.1, 6.15.0 il 23 agosto [25]. Cinque rilasci in cinque settimane significano aggiornamenti frequenti da seguire.

**Licenza e protocolli.** Licenza Apache 2.0. Il README dice "più di 200 protocolli" e "oltre 2000 modelli" [26]; la pagina dei dispositivi elenca circa 90 modelli Teltonika, tutti sul protocollo `teltonika` e sulla porta 5027 [12].

**Immagine Docker.** Si chiama `traccar/traccar`, con i tag `latest`, `6.16.0`, `6.16`, `6`, e le varianti `-alpine` (predefinita), `-debian`, `-ubuntu`, per linux/amd64 e linux/arm64 [23]. Comando ufficiale con database H2 predefinito [23]:

```bash
docker run \
--name traccar \
--hostname traccar \
--detach --restart unless-stopped \
--publish 80:8082 \
--publish 5000-5300:5000-5300 \
--publish 5000-5300:5000-5300/udp \
traccar/traccar:latest
```

La pagina avverte che pubblicare l'intero intervallo di porte avvia un processo `docker-proxy` per porta, che "consuma molta memoria e può perdere connessioni sotto carico"; suggerisce di pubblicare solo le porte dei protocolli usati, oppure di impostare `"userland-proxy": false` in `/etc/docker/daemon.json` [23]. Il database H2 non è raccomandato in produzione: la pagina indica TimescaleDB per le installazioni grandi e MySQL per i server piccoli, e rimanda a due file compose di esempio (`traccar-mysql.yaml`, `traccar-timescaledb.yaml`) [23]. Per PostgreSQL le quattro voci da cambiare nel `traccar.xml` sono `database.driver` (`org.postgresql.Driver`), `database.url`, `database.user`, `database.password` [31].

**Requisiti della macchina.** La documentazione ufficiale non pubblica una tabella di CPU e RAM [24][30]. Dice solo che l'esempio di heap Java è `-Xmx1G`, che l'H2 serve alle installazioni semplici, e che con molti dispositivi bisogna alzare il limite dei file aperti [24]. Dai forum (sec. [51]): per una flotta piccola il manutentore consiglia almeno 1 GB di RAM; per circa 1000 dispositivi con 50 utenti web ha suggerito 8 GB; un utente stima 4 GB e due core per 1000 dispositivi con posizioni ogni 15 secondi. Per 10 mezzi la CX23 (2 vCPU, 4 GB di RAM, 40 GB di disco; specifiche da fonti secondarie (sec.)) è larga con ampio margine (stima).

**API REST.** Dallo schema OpenAPI ufficiale [22]:

| Percorso | Parametri | Risposta |
|---|---|---|
| `GET /positions` | `deviceId` con `from` e `to` obbligatori, oppure `id` ripetuto | Elenco di `Position`; sono previsti anche CSV e GPX |
| `GET /devices` | `all`, `userId`, `id`, `uniqueId`, `limit`, `offset`, `keyword` | Elenco di `Device` |
| `GET /reports/trips` | `deviceId[]`, `groupId[]`, `from`, `to` (obbligatori) | Elenco di `ReportTrips` oppure foglio xlsx |
| `GET /reports/stops` | stessi | `ReportStops` oppure xlsx |
| `GET /reports/summary` | stessi | `ReportSummary` oppure xlsx |
| `GET /reports/route` | stessi | Elenco di `Position` oppure xlsx |
| `GET /reports/events` | più `type[]` (`%` per tutti) | Elenco di `Event` oppure xlsx |

Campi di `Position`: `id`, `deviceId`, `protocol`, `deviceTime`, `fixTime`, `serverTime`, `valid`, `latitude`, `longitude`, `altitude`, `speed` (**in nodi**), `course`, `address`, `accuracy`, `network`, `geofenceIds`, `attributes` [22]. Campi di `ReportTrips`: `distance` (metri), `maxSpeed` e `averageSpeed` (nodi), `duration` (secondi), `startTime`/`endTime`, `startAddress`/`endAddress`, coordinate di partenza e arrivo, `spentFuel`, `driverUniqueId`, `driverName`. `ReportStops`: `duration`, `startTime`, `endTime`, `address`, `lat`, `lon`, `spentFuel`, `engineHours`. `ReportSummary`: `maxSpeed`, `averageSpeed`, `distance`, `spentFuel`, `engineHours`; **non** contiene l'odometro iniziale e finale [22].

**Autenticazione.** Cookie di sessione creato da `/api/session`, intestazione HTTP di autorizzazione, token bearer, oppure token di accesso passato come parametro: `/api/session?token=TOKEN_UTENTE` [21]. Ogni utente può generare un token dalle proprie preferenze, con scadenza scelta; la pagina lo presenta soprattutto per viste incorporate o pubbliche [33].

**WebSocket per il live.** Il percorso è `/api/socket`; l'**unica** autorizzazione supportata è il cookie di sessione. Ogni messaggio è un JSON con le liste facoltative `devices`, `positions`, `events`, e la chiave manca se la lista è vuota [21]. Se la nostra app sta su un dominio e Traccar su un altro, il cookie di sessione diventa un problema di dominio e di `SameSite` (ragionamento mio, (stima)); la soluzione normale è un reverse proxy che serva Traccar sotto lo stesso dominio.

**Utenti e permessi.** Tre ruoli: amministratore, manager (crea utenti entro il proprio limite) e utente; più le restrizioni "sola lettura" e "dispositivi in sola lettura". L'accesso ai dispositivi nasce dalle "connessioni" assegnate a ogni utente o gruppo. La pagina non usa il termine multi-tenant, ma descrive un modello in cui l'amministratore crea un manager per cliente e il manager crea i propri utenti e dispositivi [33].

#### Inoltro delle posizioni a un'altra app

Questo è il punto che serve all'architettura. La documentazione ufficiale è la pagina "Forwarding" [20] e la pagina del file di configurazione [19]; per lo stato del codice ho letto anche `Keys.java` [40].

**Opzioni di inoltro delle posizioni** (nomi esatti, da [19][20]):

| Opzione | Significato | Predefinito |
|---|---|---|
| `forward.type` | Formato: `url` (richiesta HTTP con parametri), `json`, `amqp`, `kafka`, `mqtt`, `redis`, `wialon` | `url` |
| `forward.url` | Destinazione, obbligatoria. Si può impostare globalmente o per dispositivo. Nel tipo `url` supporta segnaposto come `{uniqueId}`, `{latitude}`, `{longitude}` | nessuno |
| `forward.header` | Intestazione HTTP aggiuntiva per l'autenticazione | nessuno |
| `forward.exchange` | Exchange AMQP | `traccar` |
| `forward.topic` | Topic Kafka, chiave di routing AMQP o topic MQTT | `positions` |
| `forward.retry.enable` | Abilita i nuovi tentativi se la consegna fallisce (server irraggiungibile o risposta non 2xx) | nessuno |
| `forward.retry.delay` | Ritardo del primo tentativo, in millisecondi; raddoppia a ogni insuccesso | 100 |
| `forward.retry.count` | Numero massimo di tentativi | 10 |
| `forward.retry.limit` | Posizioni in attesa al massimo; le successive vengono **scartate** | 100 |

**Opzioni di inoltro degli eventi** (geofence, movimento, accensione e simili): `event.forward.type` (`json`, `amqp`, `kafka`, `mqtt`; predefinito `json`), `event.forward.url` (obbligatoria), `event.forward.header` (un'intestazione per riga, nel formato `Nome: valore`), `event.forward.exchange`, `event.forward.topic` (predefinito `events`) [19][20][40]. Inoltre `server.forward` inoltra i **dati grezzi** dei dispositivi a un altro host, sulla stessa porta di ascolto del protocollo, e `server.forward.connectTimeout` / `server.forward.writeTimeout` valgono 5000 ms [19][20].

**Attenzione ai nomi che circolano in rete.** Le opzioni `forward.enable` e `forward.json`, che appaiono in molti messaggi dei forum e nella traccia che mi era stata data, **non esistono più nel codice attuale**: `Keys.java` contiene `forward.type`, `forward.url`, `forward.header`, le quattro `forward.retry.*` e le `event.forward.*`, ma non `forward.enable` né `forward.json` [40]. Un thread del forum sulla versione 5.5 mostra la correzione: sostituire `forward.json` con `forward.type` impostato a `json` risolse il problema [47]. Una guida di terzi (GeoPulse) usa ancora `forward.enable` insieme a `forward.type` [49] (sec.): probabilmente la riga è innocua, ma non ne ho verificato l'effetto. In `Keys.java` la descrizione di `forward.type` elenca ancora solo "url, json e kafka", mentre la cartella `forward` del repository contiene i forwarder per AMQP, MQTT, Redis e Wialon [40][46]; la pagina ufficiale elenca tutti i valori [20]. Vale la pagina ufficiale, ma conviene provare.

**Che cosa arriva in realtà con `forward.type=json`.** Dal codice sorgente [41][42]: Traccar manda **una richiesta HTTP POST per ogni posizione**, senza raggruppare. Il corpo è un oggetto JSON con due chiavi, `position` e `device`, i campi nulli sono omessi. Il tipo di contenuto predefinito è `application/json`. Le intestazioni di `forward.header` sono applicate **solo quando l'URL è quello globale**, non agli URL per dispositivo. Una risposta 2xx vale come consegna riuscita, qualsiasi altro codice è un errore. Con `forward.type=url` invece parte una richiesta GET con i segnaposto sostituiti [43].

Frammento di configurazione, costruito da me con i nomi verificati sopra e **non ancora provato**:

```xml
<entry key='forward.type'>json</entry>
<entry key='forward.url'>https://PROGETTO.supabase.co/functions/v1/ingest-traccar</entry>
<entry key='forward.header'>x-webhook-secret: SEGRETO_LUNGO_E_CASUALE</entry>
<entry key='forward.retry.enable'>true</entry>
<entry key='forward.retry.limit'>2000</entry>

<entry key='event.forward.type'>json</entry>
<entry key='event.forward.url'>https://PROGETTO.supabase.co/functions/v1/ingest-traccar-eventi</entry>
<entry key='event.forward.header'>x-webhook-secret: SEGRETO_LUNGO_E_CASUALE</entry>
```

Con i valori predefiniti i tentativi raddoppiano da 100 ms per 10 volte, cioè coprono circa 102 secondi di interruzione in totale (100 ms per 2^10 meno 1: calcolo mio dalla regola del raddoppio dichiarata in [20]). Oltre quella durata la posizione viene persa dalla coda di inoltro. Per questo, anche se tutto va in Supabase, **conviene tenere lo storico anche nel database di Traccar** e prevedere un recupero dei buchi con `GET /api/positions` (vedi sezione 3).

**Variante senza Edge Function.** PostgREST mappa le chiavi di un corpo JSON sugli argomenti di una funzione SQL [83]: una funzione `ingest_posizione(position jsonb, device jsonb)` chiamata su `/rest/v1/rpc/ingest_posizione` riceverebbe esattamente l'oggetto che Traccar spedisce. L'inconveniente è che la chiave API di Supabase va scritta nel `traccar.xml` del VPS. Ho verificato la regola di PostgREST, non l'intera catena con le intestazioni di Supabase (stima).

**Come si protegge una Edge Function che riceve da un sistema esterno.** Si disattiva il controllo del JWT di Supabase con `verify_jwt = false` in `supabase/config.toml` e si verifica il chiamante nel codice; la pagina avverte che disattivare il controllo toglie ogni verifica automatica [77]:

```toml
[functions.ingest-traccar]
verify_jwt = false
```

**Inoltro degli eventi.** Una configurazione di esempio dal forum (versione non indicata, sec. [50]) usa anche `event.forward.enable` e voci `event.*Handler`; il manutentore ha avvertito che quelle impostazioni potrebbero essere superate. Per gli eventi valgono le opzioni in `Keys.java` [40].

### 2.3 flespi

flespi è un gateway ospitato: i tracker si collegano al "canale" di flespi (indirizzo e porta propri) e i messaggi arrivano normalizzati in JSON con nomi uniformi, via API REST o MQTT [56]. Per Teltonika supporta Codec 8 e Codec 8 Extended (raccomanda il secondo, perché il primo non può portare parametri con AVL ID sopra 255), UDP, TCP e TLS opzionale, più alcuni comandi [13]. La pagina Teltonika letta non cita il Codec 16.

**Piano gratuito.** 0 euro, "per test e sviluppo", con limiti non estendibili: 10 dispositivi, 2 canali, 1 stream, 1 plugin, 10 geofence [54]. Limiti operativi del gratuito: 500 messaggi al minuto sui canali, 200 richieste REST al minuto, 50 sessioni MQTT, 20.000 messaggi MQTT al minuto [55]. Lo storage ha limiti per tipo di elemento (per esempio 100 MiB per i dispositivi); oltre il limite alcuni dati vengono scartati [55].

**Piani commerciali.** Start 130 euro, Pro 400, Enterprise 1.000, Ultimate 3.000 al mese [54][55]. Ogni piano commerciale include 1.000 dispositivi e 1 GiB di storage; ogni 100 dispositivi in più costano 2 euro e ogni GiB in più 1 euro [55]. Non vengono addebitati i dispositivi in base all'attività ma tutti gli elementi presenti nell'account, anche disattivati [55].

Valutazione mia: per 10 mezzi il piano gratuito basta tecnicamente per un pilota, ma la dicitura "per test e sviluppo" lo esclude da un servizio a pagamento; il minimo commerciale di 130 euro è circa 22 volte il costo del VPS. Resta una buona uscita se non vogliamo gestire un server. Un punto che non ho verificato: come i dati escono da flespi verso Supabase senza un processo sempre acceso. La pagina principale elenca MQTT, REST e "stream" per inoltrare i dati a altri sistemi [56], ma non ho letto la documentazione degli stream.

### 2.4 Piattaforme in marca bianca

| Piattaforma | Prezzo pubblicato | Marchio proprio | Note |
|---|---|---|---|
| GpsGate Cloud | 3 dollari per dispositivo al mese, minimo 5 unità, nessun contratto, 30 giorni di prova con simulatore [57] | La pagina non ne parla | Volumi alti e installazione "On-site" su richiesta; un aggregatore cita 1,5 dollari (sec.) e un altro 3 euro (sec.), valori in contrasto con la pagina ufficiale |
| Navixy | Nessuno: "prezzi basati su prodotto e consumo, senza livelli rigidi", modulo di richiesta [59] | Percorso "agente/rivenditore" con tutela dei margini; il marchio proprio non è descritto [59] | Aggregatori citano 99, 149, 499 dollari o 250, 500, 1000: non affidabili (sec. [60]) |
| Wialon Hosting / Platform | Nessuno; dipende dal numero medio di veicoli connessi e dai servizi, con sconti per fatturato semestrale e per poche funzioni attive [58] | Wialon Platform è un costruttore di soluzioni senza codice; prezzo "in base alle funzioni" [58] | Un aggregatore cita 150 dollari al mese di partenza (sec.) |
| Teltonika | n/d | n/d | Ho trovato **FOTA WEB**, una piattaforma cloud di gestione dei dispositivi (aggiornamenti firmware e configurazione), disponibile ai clienti diretti e collegabile a sistemi di flotta, ERP e CRM; contiene anche la versione web del Telematics Configuration Tool (sec. [15], risultati di ricerca sul wiki e sul sito Teltonika, pagina non aperta). Non ho trovato un'interfaccia di tracciamento della flotta |

Risposta alla domanda diretta: Teltonika non ha, per quanto ho potuto verificare, una piattaforma di tracciamento della flotta propria; ha uno strumento di gestione dei dispositivi. Non l'ho confermato sulla pagina del prodotto.

### 2.5 Scriversi il parser

**Fattibilità.** Un server TCP per il solo Codec 8 è un compito piccolo e ben definito: handshake dell'IMEI, lettura del pacchetto con CRC-16/IBM, conferma con il conteggio dei record [3]. La parte che costa tempo è tutto il resto (stima): ricomporre i pacchetti spezzati dal flusso TCP, gestire connessioni che cadono e si riaprono, tenere la lista degli IMEI autorizzati, scrivere in modo idempotente, monitorare il processo e aggiornarlo. Per un prototipo di Codec 8 Extended stimo 1-3 giorni di un buon sviluppatore Node; per un servizio che regge mesi senza sorveglianza, settimane (stima, non ho dati).

**Librerie npm.** Date e versioni lette dal registro npm il 29/10/2026 [61]-[66]:

| Pacchetto | Versione | Ultima pubblicazione | Codec dichiarati | Licenza | Note |
|---|---|---|---|---|---|
| `teltonika-parser` | 0.0.15 | 27/07/2018 | Codec 8 e 7, "Codec 16 in lavorazione" | assente | Nessun campo repository; un manutentore [61] |
| `teltonika-parser-ex` | 0.0.16 | 22/10/2020 | 8, 8E, 7 | non indicata | Fork del precedente [64] |
| `teltonika-parser-extended` | 1.0.1 | 09/10/2019 | 7, 8, 8E | n/d | [66] |
| `teltonika-parser-flex` | 0.0.17 | 22/12/2021 | 8, 8E, 7 | n/d | [66] |
| `complete-teltonika-parser` | 0.3.6 | 22/07/2022 | "codec Teltonika" in generale | ISC | Repository TimeLord2010/TeltonikaParser [63] |
| `teltonika-codec-parser` | 1.0.3 | 05/01/2026 | 8, 8E, 16, pacchetti UDP/TCP | ISC | Creato il 17/12/2025; un solo manutentore; solo decodifica [62] |
| `@groupe-savoy/teltonika-sdk` | 0.3.3 | 10/08/2026 | Server TCP, parser, comandi Codec 12 | MIT | Creato il 19/12/2025 [65] |

I nomi `node-teltonika` e `codec8` **non esistono** nel registro npm (risposta 404 per entrambi) [66].

Lo SDK di Groupe Savoy è la base più completa: ha un server TCP pronto e comandi. La sua pagina segnala come "implementato e provato in condizioni reali" il Codec 8E e il Codec 12 sul server, come "implementato ma non provato" il Codec 8 e il Codec 16; TCP e TLS sono implementati e provati, UDP non è implementato [67]. L'esempio mostrato sulla pagina non mostra l'invio dell'ACK, quindi non è documentato come lo gestisce [67].

**Che cosa si perde rispetto a Traccar:**

- Gli altri protocolli (Queclink, Concox, Ruptela e oltre 200 altri) [26].
- La maturità dell'ACK, delle riconnessioni e dei casi limite: Traccar risponde con IMEI 0/1 e conteggio dei record e decodifica Codec 8, 8E e 16 più il Codec 12 per i comandi seriali e la fotocamera [44]; le librerie npm sono giovani o ferme.
- I comandi verso il dispositivo con interfaccia (la pagina `/commands/` esiste, non l'ho letta [18]).
- Utenti, permessi, geofence, eventi (movimento, fermata, geofence, eccesso di velocità, accensione e spegnimento, offline), notifiche, report di viaggi e soste, filtri sui punti, geocodifica inversa, attributi calcolati [18][29].
- Una comunità che aggiorna i decodificatori quando un firmware cambia.

Conclusione: scriversi il parser ha senso solo per un uso con un unico modello e un solo marchio; con più marchi Traccar fa risparmiare mesi.

---

## 3. Architettura consigliata e costi

### 3.1 Schema

```
Tracker (FMB, TCP, Codec 8 Extended)          Telefono con Traccar Client (HTTP, OsmAnd, porta 5055)
        |                                                     |
        +---------------------+-------------------------------+
                              v
          VPS Hetzner CX23, Docker Compose: Traccar + PostgreSQL
          (storico di sicurezza, filtri, eventi, report)
                              |  forward.type=json, un POST per posizione
                              v
          Supabase Edge Function "ingest-traccar"
          (verifica il segreto, associa IMEI -> mezzo -> azienda, scrive)
                              v
          Supabase Postgres + PostGIS: posizioni, ultima_posizione, viaggi, soste
                  |                               |
                  | trigger + Realtime Broadcast   | job pianificati (pg_cron)
                  v                               v
          Browser: MapLibre GL, mappa live      Viaggi, soste, riepiloghi giornalieri
```

Scelta di fondo: **Traccar fa il lavoro sporco dei protocolli e resta il registro di sicurezza; Supabase è il sistema di record per l'app**, con multi-tenancy, permessi (RLS) e SQL spaziale che già conosciamo. Il costo è un doppio salvataggio delle posizioni.

**Alternativa più semplice per il pilota.** L'app chiama direttamente l'API REST e il WebSocket di Traccar, e i clienti diventano manager e utenti di Traccar [33]. Meno pezzi e nessuna Edge Function, ma l'app dipende dal modello dati di Traccar, il WebSocket richiede il cookie di sessione [21], e le analisi nostre sono più scomode. Lo giudico adatto alla fase zero, non al prodotto.

### 3.2 Pezzi e costi per 10 mezzi

| Pezzo | Costo | Fonte e data |
|---|---|---|
| VPS Hetzner CX23 (2 vCPU, 4 GB di RAM, 40 GB di disco secondo fonti secondarie), Germania o Finlandia | 5,49 euro al mese, IVA esclusa. Era 3,99 fino al 14/06/2026; il nuovo prezzo vale per ordini e ridimensionamenti dal 15/06/2026 [68] | Pagina ufficiale Hetzner, 29/10/2026 |
| Alternativa ARM CAX11 | 5,99 euro al mese, IVA esclusa [68]. L'immagine Traccar esiste per arm64 [23] | idem |
| IPv4 primario | 0,50 euro al mese; IPv6 gratuito [69]. Un server senza IP primario non ha interfaccia pubblica [69] | idem |
| Supabase Pro | Da 25 dollari al mese. Include 8 GB di disco per progetto (poi 0,125 dollari per GB), 250 GB di egress, 2 milioni di invocazioni di Edge Function (poi 2 dollari per milione), 500 connessioni Realtime contemporanee, 5 milioni di messaggi Realtime al mese, credito di calcolo di 10 dollari che copre un'istanza Micro [71][75] | Pagina prezzi ufficiale Supabase, 29/10/2026 |
| Mappa e tessere | 0 se si servono tessere PMTiles da Supabase Storage (vedi 3.4); 20 dollari con Stadia Starter; 30 dollari con MapTiler Flex | [90][87] |
| Geocodifica inversa | 0 con cache e volumi bassi (vedi 3.5) | [85][100] |
| SIM | Fuori dal mio perimetro | |
| Dominio, backup del VPS, monitoraggio | Non verificati | |

**Totale indicativo per 10 mezzi: circa 6 euro (VPS con IPv4) più 25 dollari (Supabase Pro), cioè poco più di 30 euro al mese con un cambio non verificato**, IVA e SIM escluse. Se esiste già un progetto Supabase Pro che può ospitare questi dati, il costo aggiuntivo è il solo VPS; un nuovo progetto Pro costa altri 25 dollari. Non ho verificato come Supabase fattura più progetti della stessa organizzazione.

Confronto: flespi parte da 130 euro, GpsGate Cloud costerebbe 30 dollari per 10 dispositivi senza che l'app sia nostra, Navixy e Wialon vanno richiesti.

### 3.3 Supabase: che cosa serve e che cosa dice la documentazione

**PostGIS.** Disponibile. Si abilita da Dashboard (Database, Extensions) o con SQL; la guida consiglia di installarlo in uno schema dedicato e non in `public`, perché in `public` la tabella `spatial_ref_sys` finirebbe esposta dall'API dati. Esempio ufficiale di colonna e indice [72]:

```sql
create extension postgis with schema "extensions";

-- Dalla pagina ufficiale, la colonna dell'esempio:
--   location extensions.geography(POINT) not null
-- e il relativo indice spaziale:
create index restaurants_geo_index
  on public.restaurants
  using GIST (location);
```

**Bozza della tabella (mia proposta, non provata)**:

```sql
create table public.posizioni (
  mezzo_id     uuid        not null references public.mezzi(id),
  rilevata_il  timestamptz not null,                 -- fixTime del dispositivo
  geo          extensions.geography(point, 4326) not null,
  velocita_kmh real,
  rotta        smallint,
  accensione   boolean,
  odometro_m   bigint,                               -- AVL ID 16, se presente
  valida       boolean not null default true,
  attributi    jsonb,
  primary key (mezzo_id, rilevata_il)                -- rende idempotenti i reinvii
);
create index posizioni_geo_idx on public.posizioni using gist (geo);
```

La chiave primaria `(mezzo_id, rilevata_il)` permette di scrivere con "ignora se esiste già", così i nuovi tentativi di Traccar e il recupero dei buchi non duplicano nulla. La velocità di Traccar è in nodi [22]: va convertita in km/h (moltiplicare per 1,852).

**Partizionamento.** Con 10 mezzi (circa 2,5 milioni di righe l'anno) non serve (stima). Se servirà: l'estensione `timescaledb` è **deprecata nei progetti Postgres 17** e la guida di Supabase consiglia il partizionamento nativo gestito da `pg_partman` [80]; la pagina di `pg_partman` mostra come abilitarlo e pianificare la manutenzione con `pg_cron` [81], ma non dice esplicitamente che sia disponibile in ogni progetto, quindi va verificato nell'elenco delle estensioni del progetto reale.

**Realtime.** La documentazione raccomanda **Broadcast dal database** (`realtime.broadcast_changes`, con un trigger per tabella e canali privati con policy RLS di autorizzazione) rispetto a "Postgres Changes", che "non scala altrettanto bene" [79]. Limiti del piano Pro: 500 connessioni contemporanee, 500 messaggi al secondo, 500 ingressi in canale al secondo, payload Broadcast fino a 3.000 KB [73]. Conteggio dei messaggi: un Broadcast conta come un messaggio inviato più uno per ogni client abbonato che lo riceve; una modifica del database conta uno per ogni client in ascolto; 2,50 dollari per milione oltre i 5 milioni inclusi [74].

**Edge Function.** Limiti: 150 secondi di durata complessiva sul piano gratuito e 400 sui piani a pagamento, 2 secondi di tempo CPU per richiesta, 256 MB di memoria, dimensione della funzione 20 MB se compilata in locale [76]. Una posizione ogni richiesta resta molto sotto questi limiti.

**Storage.** Il limite globale di dimensione file non può superare 50 MB sul piano gratuito; sul Pro si può portare fino a 500 GB [78].

### 3.4 Mappa e tessere

**Libreria.** MapLibre GL JS: licenza BSD a tre clausole, nata come fork del codice open source di Mapbox, disegna tessere vettoriali con WebGL [94]. La versione 6 viene distribuita solo come moduli ES [94]. Leaflet pesa circa 42 KB, è pensata per tessere raster e vettori semplici; la pagina annuncia solo la 2.0.0-alpha.1 (agosto 2025) e non cita il supporto nativo alle tessere vettoriali [95]. Per una mappa live con centinaia di punti e tracce preferisco MapLibre (giudizio mio).

**Policy delle tessere di OpenStreetMap (`tile.openstreetmap.org`).** Ho letto il testo il 29/10/2026 [84]. Contrariamente a quanto mi era stato detto, **il testo non vieta l'uso commerciale**. Dice però: "Commercial services, or those that seek donations, should be especially aware" e avverte che si può perdere l'accesso a ogni momento ("you may no longer be able to serve your paying customers"); che la disponibilità è "best-effort", senza accordi di livello di servizio; che servono un User-Agent chiaro che nomini l'app e un Referer valido; che l'attribuzione OpenStreetMap va mostrata in modo evidente; che il precaricamento delle tessere e l'uso offline sono vietati; che si devono rispettare le intestazioni di cache o, in mancanza, tenere ogni tessera almeno 7 giorni. Chi non può rispettare le regole è indirizzato a un servizio alternativo o a tessere proprie [84]. Per un prodotto a pagamento la conclusione pratica è che non dobbiamo appoggiarci a quel servizio, anche se il testo non lo proibisce. I dati OpenStreetMap sono sotto licenza ODbL: va dato credito e va chiarito che i dati sono disponibili sotto ODbL [86].

| Alternativa | Piani e prezzi letti il 29/10/2026 | Uso commerciale | Note |
|---|---|---|---|
| **Protomaps (PMTiles) autoospitato** | Nessun canone; il file del pianeta pesa circa 120 GB fino a zoom 15; si estrae una regione con `pmtiles extract` e un riquadro; ogni livello di zoom in più raddoppia circa la dimensione [93] | Codice BSD, dati ODbL [93] | Estratti da fonti secondarie: Berlino 84 MB, Puglia circa 200 MB (sec.); per la Lombardia o il Nord Italia non ho un numero. Supabase Storage supporta le richieste Range necessarie e un articolo di Supabase mostra la configurazione con MapLibre; i bucket pubblici accettano qualsiasi origine e, al momento dell'articolo, il CORS non era modificabile [82] |
| **Stadia Maps** | Free 0 (200.000 crediti, uso commerciale non consentito); Starter 20 dollari (1.000.000 crediti, extra 3 centesimi ogni 1.000); Standard 80 (7.500.000); Professional 250 (25.000.000). Una tessera vettoriale o raster = 1 credito [90] | Sì dai piani a pagamento | Prova di 14 giorni del piano Professional senza carta [90] |
| **MapTiler Cloud** | Free 0 (5.000 sessioni, 100.000 richieste, 1.000 sessioni di ricerca), Flex 30 dollari (25.000 sessioni, 500.000 richieste, 3.000 sessioni di ricerca; extra 2,50 dollari per 1.000 sessioni e 0,15 per 1.000 richieste) [87] | Il gratuito è limitato a "uso non commerciale e ricerca e sviluppo per prodotti commerciali" [88]; il Flex non è dichiarato esplicitamente nella pagina letta | |
| **Mapbox** | 50.000 caricamenti di mappa GL JS gratuiti al mese, poi da 5 dollari per 1.000 [91] | I termini richiedono una licenza commerciale separata, con ordine attivo, per le applicazioni "legate all'uso di veicoli" [92] | Una app di tracciamento flotte ricade con ogni probabilità in quella dicitura (lettura mia); da evitare senza una conferma commerciale |

**Raccomandazione per le tessere:** PMTiles su Supabase Storage con MapLibre, e un piano Stadia Starter come ripiego se la gestione del file diventa un peso. Il rischio da provare: il comportamento di Supabase Storage sotto richieste Range ripetute e il costo di egress con molti utenti (non l'ho misurato).

### 3.5 Geocodifica inversa

Servono indirizzi per le soste (stima: 10 mezzi per 10-15 soste al giorno per 22 giorni, cioè 2.200-3.300 ricerche al mese). Un piccolo numero.

| Servizio | Regole e prezzi letti il 29/10/2026 | Giudizio |
|---|---|---|
| **Nominatim pubblico (OSMF)** | Massimo assoluto di 1 richiesta al secondo; User-Agent o Referer che identifichi l'app; "i risultati devono essere messi in cache da voi"; vietate le ricerche inverse "a griglia" e il completamento automatico dal lato client; una richiesta periodica da app conta come geocodifica di massa ed è "fortemente sconsigliata"; "le applicazioni e i servizi la cui funzione principale è la geocodifica devono avere un servizio proprio"; la policy può cambiare senza preavviso [85] | Accettabile per poche migliaia di richieste al mese con cache e un'identificazione chiara, fragile per un servizio a pagamento |
| **Photon (Komoot)** | Apache 2.0; Java 21; per il pianeta circa 95 GB di disco e almeno 64 GB di RAM consigliati; il server pubblico photon.komoot.io è una demo con "limiti ragionevoli" e nessuna garanzia [96] | Troppo pesante da ospitare per noi |
| **MapTiler geocoding** | Endpoint `GET https://api.maptiler.com/geocoding/{lon},{lat}.json?key=...` [89]; nel piano gratuito (non commerciale) 1.000 sessioni di ricerca, 3.000 nel Flex [87] | Utile se si prende già il Flex |
| **LocationIQ** | Gratuito: 5.000 richieste al giorno e 2 al secondo, uso commerciale ammesso con un link "Search by LocationIQ.com"; cache dei risultati consentita per **48 ore** nel gratuito, per tutta la durata del contratto nei piani a pagamento [100] | Salvare l'indirizzo nella tabella delle soste per sempre richiede un piano a pagamento (il più basso con geocodifica è Developer a 100 dollari al mese, lettura mia dalla pagina) |
| **Mapbox Geocoding (Temporary)** | 100.000 richieste gratuite al mese, poi 0,75 dollari per 1.000 [91] | Valgono le riserve sulla licenza veicoli di cui sopra; "Temporary" significa in genere che i risultati non si possono conservare (mem.) |

**Come ridurre il problema alla radice:** far censire ai clienti i loro luoghi (depositi, clienti abituali) come geofence con nome. La geocodifica serve solo per le soste in luoghi sconosciuti e può partire con Nominatim e cache, per poi passare a un servizio a pagamento se i volumi o la policy lo richiedono.

### 3.6 Percorsi e map matching (per le analisi, non per il live)

| Strumento | Cosa fa | Condizioni lette il 29/10/2026 |
|---|---|---|
| **OSRM** | Servizi Match (allinea una traccia GPS rumorosa alla rete stradale), Route, Table, Trip; licenza BSD-2 [97] | Il server demo è per uso "ragionevole e non commerciale", un massimo di 1 richiesta al secondo, nessuna garanzia [97]. Ospitarlo: per il pianeta servono circa 123 GiB di RAM per il profilo auto e le dimensioni crescono in modo circa lineare con i dati in ingresso; per un estratto italiano non ho un numero [97] |
| **Valhalla** | Instradamento, matrici, isocrone, map matching con la libreria Meili; licenza MIT [98] | Parametri di Meili: `search_radius` 50 m (massimo `max_search_radius` 100 m), `sigma_z` 4,07, `beta` 3, `breakage_distance` 2000 m, `interpolation_distance` 10 m [98]. La pagina di riferimento dell'API di map matching rimanda ad altra posizione e non l'ho letta, quindi i nomi delle azioni `trace_route` e `trace_attributes` vengono da un risultato di ricerca (sec.) |
| **OpenRouteService** | Instradamento, isocrone, matrici | L'ultima cifra ufficiale trovata è del 2019: più di 8.000 richieste al giorno nel piano gratuito [99]; la pagina dei piani non si apriva. Non ho verificato se offra il map matching |
| **Mapbox Map Matching** | 100.000 richieste gratuite al mese, poi 2 dollari per 1.000 [91] | Valgono le riserve sulla licenza veicoli |

Giudizio mio: per 10 mezzi basta fare il map matching **solo quando serve** (per esempio per disegnare un viaggio chiuso o per confrontare percorsi ricorrenti), con Valhalla sullo stesso VPS o su un secondo VPS piccolo, con un estratto regionale. Non ho il fabbisogno di RAM di un estratto regionale: va misurato. OSRM pubblico è escluso (non commerciale).

### 3.7 Stima del volume dei dati

Caso richiesto: una posizione ogni 30 secondi, 8 ore al giorno, 22 giorni al mese, 10 mezzi.

Calcolo: 120 posizioni all'ora per 8 ore per 22 giorni = 21.120 per mezzo, per 10 mezzi = **211.200 righe al mese**, cioè 2.534.400 all'anno.

Dimensione di una riga: intestazione della riga (24 byte), chiave (16 byte per il `uuid` più 8 per il timestamp), punto geografico (circa 32 byte), velocità, rotta, accensione, validità, odometro (circa 16 byte), più l'indice sulla chiave (circa 32 byte con l'overhead) e l'indice spaziale (circa 50-60 byte). Con 0-100 byte di JSON aggiuntivo la riga completa di indici va da circa 150 a circa 300 byte. Uso **250 byte** come valore medio. **È una stima mia, non una misura**: va verificata con `pg_total_relation_size` su una tabella di prova.

| Scenario | Righe al mese | MB al mese (250 byte) | GB all'anno | Messaggi Realtime se 3 abbonati (4 per riga) | Invocazioni Edge |
|---|---|---|---|---|---|
| A. Richiesto: 10 mezzi, 30 s, 8 h, 22 giorni | 211.200 | circa 53 | circa 0,63 | 844.800 | 211.200 |
| B. 10 mezzi, 10 s, 8 h, 22 giorni | 633.600 | circa 158 | circa 1,9 | 2,5 milioni | 633.600 |
| C. 10 mezzi, 10 s, 24 h, 30 giorni (caso limite) | 2.592.000 | circa 648 | circa 7,8 | 10,4 milioni | 2,6 milioni |
| D. 50 mezzi, 30 s, 8 h, 22 giorni | 1.056.000 | circa 264 | circa 3,2 | 4,2 milioni | 1,06 milioni |
| E. 100 mezzi, 30 s, 8 h, 22 giorni | 2.112.000 | circa 528 | circa 6,3 | 8,4 milioni | 2,1 milioni |

Nel piano Pro il disco incluso è di 8 GB e ogni GB in più costa 0,125 dollari al mese [75]: **lo spazio non è un costo che conta**, nemmeno nello scenario E. Quello che cresce è il costo dei messaggi Realtime (5 milioni inclusi, poi 2,50 dollari per milione [74]) e la lentezza delle query storiche sulle tabelle grandi. Per la fase di pilota con 10 mezzi nessun limite del piano Pro viene toccato nello scenario A, e nemmeno nello scenario B.

Rete mobile: un record Codec 8 con pochi elementi di I/O pesa dell'ordine di 50-100 byte (stima mia dalla struttura del pacchetto [3]); per lo scenario A sono pochi MB al mese per SIM, ma non ho verificato i dati reali di consumo.

### 3.8 Che cosa conviene archiviare e che cosa aggregare

Proposta mia, da discutere:

1. **Punti grezzi**: tenerli tutti per 12-24 mesi nella tabella `posizioni` (a questi volumi sono pochi GB), poi spostare a una tabella di archivio o ridurli con `ST_Simplify` conservando i punti di inizio, fine e sosta (la funzione la conosco da memoria (mem.)).
2. **Viaggi e soste**: calcolarli una volta, quando il viaggio è chiuso, e salvarli in `viaggi` e `soste` con inizio, fine, distanza, durata, velocità massima e media, indirizzo, geofence toccate. Le analisi leggono queste tabelle, non i punti.
3. **Riepilogo giornaliero per mezzo**: chilometri, ore di guida, ore di motore acceso, ore di sosta, numero di soste, velocità massima. È la tabella da mostrare e da esportare.
4. **Ultima posizione**: una riga per mezzo, aggiornata a ogni punto; è la tabella da collegare al canale Realtime, perché il browser riceva un solo messaggio per mezzo e non si ascolti la tabella grande.
5. **Eventi** (geofence, eccesso di velocità, accensione): una tabella a parte, alimentata dall'inoltro `event.forward.*` di Traccar.
6. **Dati grezzi dei pacchetti**: non salvarli in Supabase; Traccar può conservarli con `database.saveOriginal` se serve a diagnosticare [19].
7. **Recupero dei buchi**: un job pianificato che, per ogni mezzo, confronta l'ultimo `rilevata_il` con l'API di Traccar (`GET /api/positions` con `from` e `to`) e riempie i vuoti, grazie alla chiave primaria idempotente.
8. **Sicurezza e privacy**: la porta del tracker è aperta a Internet, quindi il firewall deve ammettere solo le porte usate; le interfacce web sotto HTTPS con un reverse proxy come Caddy [32]. I dispositivi Teltonika supportano TLS 1.1 e 1.2 [6], ma nelle pagine Traccar lette non ho trovato come far terminare il TLS dei dispositivi su Traccar [32]; flespi dichiara TLS per Teltonika [13]. Le posizioni dei veicoli sono dati personali dei conducenti: vedi sezione 6.

---

## 4. Fase zero con i telefoni degli autisti

### 4.1 Come funziona

**Traccar Client** è l'app ufficiale di Traccar. Su iOS è gratuita, senza acquisti in-app, richiede iOS 15 o successivo, pesa 28,9 MB e alla data della lettura era alla versione 10.2.3; la scheda dice che gira in background e manda rapporti periodici di posizione al server scelto dall'utente, senza pubblicità e senza raccolta di dati da parte dello sviluppatore [39]. Su Android la pagina Traccar rimanda a Google Play o a un APK scaricabile [36]; la scheda di Google Play non si è aperta, quindi prezzo e versione Android non sono verificati. Di default l'app si collega a un server demo, e si può puntare a un server proprio o a un'altra piattaforma compatibile [36]. Esiste anche un SDK con lo stesso motore di tracciamento per Android e iOS nativi, Flutter e React Native, utile se un giorno volessimo un'app autisti con il nostro marchio [36].

**Protocollo.** L'app usa il protocollo **OsmAnd**, cioè richieste HTTP con parametri nell'indirizzo o nel corpo. Il solo parametro obbligatorio è `id` (o `deviceid`); gli altri sono `lat` e `lon` (o `location`), `timestamp`, `speed` (in nodi per impostazione predefinita), `bearing` (o `heading`), `altitude` (metri), `accuracy` (metri) e `batt`; ogni altro parametro diventa un attributo personalizzato. Esempio della pagina, sulla porta 5055 [35]:

```
http://demo.traccar.org:5055/?id=12345&lat=48.8566&lon=2.3522&timestamp=1609459200000&speed=15&bearing=270&altitude=35&accuracy=10&batt=75
```

**Impostazioni dell'app** [37]: "Device identifier" (l'identificatore che il server usa per il dispositivo), "Server URL" (deve essere un URL completo, non solo il nome host; la porta 5055 è quella giusta per la versione più recente), "Interval" (aggiornamenti a tempo, quando "Distance" è 0 su Android o la precisione è la massima), "Distance" (un aggiornamento ogni N metri in movimento), "Angle" (aggiornamento al cambio di direzione), "Location accuracy" (Highest, High, Medium, Low; Highest tiene il GPS sempre acceso), "Offline buffering" (salva le posizioni durante le interruzioni di rete e le carica dopo; se spento, gli invii falliti vanno persi), "Wake lock" (solo Android; tiene sveglio il telefono in movimento, più affidabile ma consuma di più), "Stop detection" (attivo per impostazione predefinita). Per il pilota conviene puntare l'app al nostro Traccar sulla porta 5055, perché così la catena resta identica a quella di produzione.

Una possibilità non verificata: puntare l'app direttamente a una Edge Function di Supabase che interpreti i parametri OsmAnd, senza il VPS. La pagina OsmAnd descrive il formato lato server [35], ma non ho trovato se l'app invii GET o POST e con quale corpo; andrebbe visto con un test.

### 4.2 Che cosa si perde rispetto a un tracker fisso

| Aspetto | Telefono con Traccar Client | Tracker fisso sul veicolo |
|---|---|---|
| Alimentazione | Batteria del telefono; "Highest" tiene il GPS sempre acceso e il wake lock consuma di più [37] | Alimentato dal veicolo a 6-30 V (esempio FMB920) [1] |
| Spegnimento | Su iOS, chiudere l'app con il gesto verso l'alto uccide il processo e l'app non riporta più [38]; su Android serve l'esenzione dall'ottimizzazione della batteria e molti produttori aggiungono blocchi propri [38] | Il conducente non lo può chiudere (resta scollegarlo) |
| Pause automatiche | Con "Stop detection" (attivo) un messaggio "StationaryEnter: pausing" indica che gli aggiornamenti regolari si sono fermati; l'heartbeat da fermo è spento di default [38] | Registra da fermo ogni ora per impostazione predefinita [1] |
| Precisione | Medium su iOS richiede circa 100 m e Low circa un chilometro; gli edifici peggiorano il segnale; su Android senza i servizi Google la precisione Low usa il provider passivo, con aggiornamenti rari [38] | Ricevitore dedicato (mem.) |
| Falsi | "Location accepted" significa che il filtro dell'app ha accettato il punto, non che il server lo abbia ricevuto [38]; posizioni approssimate da celle o Wi-Fi si possono scartare con `filter.approximate` [19] | Il campo `valid` e i filtri di Traccar |
| Perdite di rete | Perse se il buffer offline è spento [38] | Memorizza nella memoria interna e rimanda (mem.) |
| Dati del veicolo | Nessun contachilometri, nessuna accensione, nessun CAN; invia batteria e quanto altro configurato [35] | Accensione (239), movimento (240), odometro (16), tensione (66) [44] |
| Sorveglianza della persona | Segue la persona anche fuori dal turno, se l'app resta accesa (stima) | Segue il mezzo |

I forum riportano problemi di iOS: sul thread di un utente il client smetteva di riportare dopo 1-1,5 ore e il manutentore rispondeva che l'aggiornamento in background non è necessario e non sapeva spiegarlo (sec. [52]); un thread più recente (iPhone 14 e 16 Pro con iOS 26.x) segnala dati interrotti in background dopo l'aggiornamento al client 10, con la risposta del manutentore di provare la 10.0.7 che "dovrebbe avere una correzione per iOS" (sec. [52]). Il manutentore ha dichiarato di non avere risorse per supportare bene questi casi (sec. [52]). La pagina di risoluzione dei problemi conferma la tensione di fondo: "Apple e Google limitano i processi in background" e l'app ne soffre [38].

### 4.3 È un modo serio di fare un pilota?

Sì, a condizioni precise, e per uno scopo limitato.

- **Serve** per provare l'intera catena (Traccar, inoltro, Supabase, mappa live, viaggi, soste, riepiloghi) con 2-3 autisti in 2-4 settimane, senza comprare hardware, e per far vedere al cliente come appare il servizio.
- **Non serve** per misurare chilometri e ore di motore reali, né per vendere il servizio: senza accensione e contachilometri le analisi sono approssimate, e la continuità del dato dipende dal sistema operativo del telefono.
- **Condizioni:** telefoni Android dedicati ai mezzi (non i telefoni personali), con ricarica in cabina; esenzione dall'ottimizzazione della batteria; precisione "Highest"; buffer offline acceso; un intervallo di 30 secondi; consenso scritto e informativa ai conducenti prima di accendere l'app (sezione 6).
- **Controllo di qualità:** montare **un solo tracker vero** su uno dei mezzi nello stesso periodo, per confrontare i chilometri e le soste misurati dal telefono con quelli del tracker. È l'unico modo per sapere quanto sbaglia il pilota.

---

## 5. Le analisi

### 5.1 Che cosa danno già i report di Traccar

| Report / evento | Contenuto | Fonte |
|---|---|---|
| Viaggi (`/api/reports/trips`) | Inizio e fine con ora, coordinate e indirizzo; distanza in metri; durata in secondi; velocità media e massima in nodi; carburante speso; autista | [22] |
| Soste (`/api/reports/stops`) | Inizio, fine, durata, indirizzo, coordinate, ore di motore, carburante | [22] |
| Riepilogo (`/api/reports/summary`) | Distanza, velocità media e massima, carburante, ore di motore, per dispositivo o gruppo e per periodo. Non contiene l'odometro iniziale e finale | [22] |
| Percorso (`/api/reports/route`) | Le posizioni del periodo | [22] |
| Eventi | Dispositivo online/offline, in movimento/fermo, soglia di velocità superata (serve l'attributo `speedLimit`), geofence entrata/uscita (il geofence va collegato al dispositivo o al gruppo), accensione/spegnimento (il dispositivo deve riportare l'accensione in continuo), carburante, manutenzione e altri | [29] |

**Come Traccar decide viaggi e soste** [27]. Logica predefinita (`report.trip.newLogic` attiva): un'area di movimento di `report.trip.minDistance` (200 m) e una durata minima di `report.trip.minDuration` (180 s) per riconoscere una sosta; `report.trip.stopGap` (3600 s) spezza il movimento quando c'è un vuoto tra due posizioni; `report.trip.useIgnition` (spenta di default) usa l'accensione quando il dispositivo la riporta. Logica precedente (`report.trip.newLogic=false`): `report.trip.minimalTripDuration` 300 s, `report.trip.minimalTripDistance` 500 m, `report.trip.minimalParkingDuration` 300 s, `report.trip.minimalNoDataDuration` 3600 s, basata sull'attributo `motion`, calcolato dalla velocità e da `speedThreshold` se il dispositivo non lo riporta.

**Un'avvertenza importante.** Per periodi più lunghi di `report.fastThreshold` (un giorno di default) Traccar usa la versione "veloce" dei report, che riusa gli eventi in tempo reale: è più rapida ma meno precisa, e la velocità massima risulta zero. Le posizioni arrivate fuori ordine possono spostare gli eventi. La versione "lenta" rielabora tutte le posizioni con la configurazione corrente [27]. Se i report di Traccar diventano la base di un conteggio che il cliente paga, questa soglia va gestita.

**Come Traccar calcola i chilometri.** Il suo gestore delle distanze somma la distanza tra posizioni consecutive, a meno che il dispositivo riporti già una distanza; **non legge** il contachilometri del dispositivo per il totale [45]. Il decodificatore Teltonika salva l'AVL ID 16 come attributo `odometer`, l'ID 199 come `tripOdometer`, l'ID 239 come `ignition` e l'ID 240 come `motion` [44]. Quindi in Traccar convivono due numeri: `totalDistance` da coordinate e `odometer` dal dispositivo.

### 5.2 Come calcoliamo noi le stesse cose

**Soste per velocità e tempo.** Un punto è "fermo" se la velocità è sotto una soglia (per esempio 3 km/h) oppure l'accensione è spenta (AVL 239); una sosta è una sequenza di punti fermi lunga almeno 3 minuti, in linea con i 180 secondi di Traccar [27]; una fermata più breve (semaforo, coda) non conta. Un movimento di pochi punti dentro una sosta lunga va assorbito (isteresi). Se tra due punti passa più di un'ora si chiude il viaggio e si segnala il buco, come fa `stopGap`. In SQL si ottiene con le funzioni a finestra, numerando le sequenze consecutive con la tecnica "gaps and islands". Schema, non provato:

```sql
with p as (
  select mezzo_id, rilevata_il, geo,
         (coalesce(velocita_kmh, 0) < 3 or accensione is false) as fermo
  from posizioni
  where mezzo_id = $1 and rilevata_il >= $2 and rilevata_il < $3 and valida
), s as (
  select *, sum((fermo is distinct from lag(fermo) over w)::int) over w as grp
  from p window w as (order by rilevata_il)
)
select fermo, min(rilevata_il) as inizio, max(rilevata_il) as fine
from s group by grp, fermo order by inizio;
```

**Chilometri.** Tre metodi, da confrontare e non da scegliere a caso:

| Metodo | Come | Pregi | Difetti |
|---|---|---|---|
| Differenza di odometro | Ultimo meno primo valore dell'AVL ID 16 nel periodo (in metri) [44] | È il numero più vicino a quello del cruscotto se il dispositivo legge il CAN (mem.) | L'elemento va attivato nel Configurator; senza CAN molti modelli danno un odometro virtuale calcolato dal GPS (sec., dalla ricerca sul wiki Teltonika); può azzerarsi dopo una sostituzione del dispositivo (stima) |
| Haversine sui punti | Somma delle distanze tra punti consecutivi | Funziona con qualunque sorgente | Con un punto ogni 30 secondi taglia le curve e sottostima; il rumore da fermo la sovrastima |
| `ST_Length` su `geography` | Lunghezza della linea costruita con i punti, in metri sullo sferoide per impostazione predefinita [101] | Una riga di SQL | Stessi difetti dell'haversine |

Formula dell'haversine (formula standard, scritta da memoria (mem.)):

```js
function haversineM(lat1, lon1, lat2, lon2) {
  const R = 6371008.8;                    // raggio medio terrestre, metri
  const rad = d => d * Math.PI / 180;
  const dLat = rad(lat2 - lat1), dLon = rad(lon2 - lon1);
  const a = Math.sin(dLat / 2) ** 2 +
            Math.cos(rad(lat1)) * Math.cos(rad(lat2)) * Math.sin(dLon / 2) ** 2;
  return 2 * R * Math.asin(Math.sqrt(a));
}
```

Lo stesso in SQL con PostGIS, per giorno e mezzo (schema non provato):

```sql
select mezzo_id, date_trunc('day', rilevata_il) as giorno,
       sum(st_distance(geo, lag(geo) over (partition by mezzo_id order by rilevata_il))) / 1000 as km
from posizioni
where valida
group by mezzo_id, giorno;
```

Una regola semplice (mia, da discutere): usare la differenza di odometro quando il valore esiste ed è crescente, ricadere sull'haversine quando manca, e conservare entrambi per il confronto. Quanto sottostimi l'haversine a 30 secondi non l'ho trovato in una fonte; va misurato sul pilota, con il tracker di controllo della sezione 4.

**Ore di motore e ore di guida.** Le ore di motore sono la somma degli intervalli con accensione (AVL 239) uguale a 1; le ore di guida sono la somma dei viaggi (intervalli in movimento); la differenza è il tempo a motore acceso da fermi. Il riepilogo di Traccar espone `engineHours` [22], ma non ho letto come lo calcola. Le ore di motore lette dal CAN dipendono dall'hardware (mem.).

**Zone (geofence).** Con PostGIS: `ST_DWithin` su `geography` dice se un punto è entro N metri da un luogo e può usare l'indice spaziale [101]; per un poligono si usa un'intersezione (mem.). Entrata e uscita si ottengono confrontando lo stato di punti consecutivi. In alternativa i geofence di Traccar generano gli eventi di entrata e uscita, che arrivano con `event.forward.*` [29][20].

**Percorsi ricorrenti.** Passi proposti: raggruppare le soste con `ST_ClusterDBSCAN` (una funzione a finestra su `geometry`; lavora in unità della geometria, quindi va applicata dopo una proiezione in un sistema metrico) [101]; abbinare ogni viaggio a una coppia (gruppo di partenza, gruppo di arrivo); dentro ogni coppia misurare la somiglianza dei tracciati con `ST_FrechetDistance`, che tiene conto dell'ordine dei punti e richiede GEOS 3.7 o successivo [101]. Il map matching prima del confronto stabilizza il risultato (sezione 3.6).

**Filtraggio dei punti sporchi.** Traccar offre filtri che **scartano** il punto prima di salvarlo [19]:

| Opzione | Effetto | Predefinito |
|---|---|---|
| `filter.enable` | Attiva o disattiva il filtraggio | true |
| `filter.invalid` | Scarta le posizioni con `valid` falso | non indicato |
| `filter.zero` | Scarta latitudine e longitudine zero | non indicato |
| `filter.duplicate` | Scarta i record con lo stesso orario | non indicato |
| `filter.outdated` | Scarta i messaggi senza fix GPS | non indicato |
| `filter.future` / `filter.past` | Scartano record con orario troppo avanti o indietro rispetto al server (secondi) | 86400 / non indicato |
| `filter.accuracy` | Scarta le posizioni con precisione peggiore del valore (metri) | non indicato |
| `filter.approximate` | Scarta le posizioni da celle o Wi-Fi | non indicato |
| `filter.static` | Scarta le posizioni con velocità esattamente zero | non indicato |
| `filter.distance` | Scarta le posizioni più vicine di N metri all'ultima | non indicato |
| `filter.maxSpeed` | Scarta i salti che implicano una velocità sopra il valore (nodi) calcolata da distanza e tempo; la pagina suggerisce un punto di partenza intorno a 25000, un valore molto alto che andrebbe controllato | non indicato |
| `filter.minPeriod` | Scarta i punti arrivati meno di N secondi dopo il precedente | non indicato |
| `filter.dailyLimit`, `filter.dailyLimitInterval`, `filter.skipLimit`, `filter.skipAttributes` | Limiti giornalieri e deroghe | non indicato |

Parere mio: tenere in Traccar solo i filtri non distruttivi di analisi (`filter.invalid`, `filter.zero`, `filter.duplicate`), perché un punto scartato non si può più recuperare. Filtri come `filter.static` e `filter.distance` cancellano proprio i punti che servono a riconoscere le soste. Le regole più fini vanno in SQL, dove il punto resta e riceve un flag `valida`: salti con velocità implicita sopra un massimo realistico per un furgone (parametro nostro, per esempio 150 km/h), punti senza fix o con pochi satelliti (mem.: il campo satelliti sta nel record GPS Teltonika), orari fuori ordine, deriva da fermo (congelare la posizione quando la velocità è sotto la soglia). Il rumore del GPS da fermo è la prima causa di chilometri fasulli.

---

## 6. Cosa non ho potuto verificare

### 6.1 Su Traccar e sull'inoltro

- **`forward.enable`**: non compare in `Keys.java` letto oggi [40] né nella pagina ufficiale [19][20], ma compare in guide di terzi [49] e in thread di forum [47][48]. Non ho provato Traccar per vedere se la riga viene ignorata, accettata o necessaria.
- **Inoltro per dispositivo** (`forward.url` come attributo del dispositivo): il codice del forwarder JSON lo prevede, ma in un thread di forum un utente non riuscì a farlo funzionare e il manutentore non chiarì [42][48].
- **Anno della versione 6.16.0**: la pagina delle release mostra "27 Sep" senza anno [25]. È coerente con ottobre 2026, ma non c'è scritto.
- **Dove vive la coda dei nuovi tentativi** (memoria o disco): non l'ho trovato. Se sta in memoria, un riavvio di Traccar durante un'interruzione perde le posizioni in coda (ipotesi mia).
- **Requisiti hardware**: non esiste una tabella ufficiale; le indicazioni sono di forum [51].
- **TLS dei dispositivi su Traccar**: le pagine lette parlano solo di HTTPS per l'interfaccia web [32].
- **Pagina `/commands/` di Traccar** (comandi ai dispositivi) e **`/computed-attributes/`**: elencate nell'indice [18], non lette.
- **Come Traccar calcola `engineHours`** nei report: non l'ho trovato.
- **Traccar Client**: la scheda Google Play non si è aperta; non ho verificato se l'app invii GET o POST e con quale forma [36][37].

### 6.2 Su Teltonika e sugli altri marchi

- **Pubblicazione diretta su un broker MQTT generico** da un FMB: non l'ho trovata; il Codec JSON documentato è per AWS IoT [5]. Il valore `3 = MQTT` dell'ID 2006 esiste [2], ma non so con quali impostazioni.
- **HTTP/HTTPS**: nessuna pagina Teltonika letta lo menziona.
- **Pagina "Data acquisition" dell'FMB920**: non si apriva; per le definizioni dei parametri ho usato quella dell'FMM920 [8] e la lista dei parametri dell'FMB920 [2].
- **Esempio di SMS a 30 secondi** (`setparam 10050:30;10055:30`): costruito da me dalla lista dei parametri, non provato su un dispositivo.
- **Teltonika FOTA WEB**: letto solo negli estratti dei risultati di ricerca [15]; non ho aperto la pagina del prodotto e non ho trovato un'interfaccia di tracciamento flotta.
- **Queclink**: il PDF ufficiale del protocollo non è leggibile con gli strumenti a disposizione (flusso binario compresso); la sintassi `AT+GTSRI` viene da un sito di terzi [10]. La conferma che il formato è ASCII viene da flespi [9]. Le porte Traccar di Queclink, Concox e Ruptela sono ricavate dai nomi delle cartelle [11].
- **Concox/Jimi e Ruptela**: la struttura dei pacchetti e le sintassi SMS vengono da estratti di risultati di ricerca [16][17], non dai manuali originali, e variano con modello e firmware.
- **Parametri della SIM e consumo di dati**: fuori dal mio incarico; ho solo una stima di ordine di grandezza dalla struttura del pacchetto.

### 6.3 Sui prezzi e sui piani

- **Hetzner**: la pagina del prodotto è generata da JavaScript e non mostra i modelli [70]; il prezzo di CX23 e CAX11 viene dalla pagina di documentazione ufficiale dell'adeguamento prezzi del 15/06/2026 [68]. Le specifiche della CX23 (2 vCPU, 4 GB, 40 GB) vengono da fonti secondarie; la sostituzione della CX22 con la CX23 pure (sec.). Non ho controllato il prezzo dei backup, né se il server possa funzionare solo con IPv6 (la pagina non lo dice [69]).
- **Supabase**: i prezzi sono in dollari e non so se includano l'IVA [71]. Non ho letto le specifiche dell'istanza Micro, il prezzo dello Storage e dell'egress per i PMTiles, né come Supabase fattura più progetti nella stessa organizzazione. La pagina sull'uso delle Edge Function dava 404; i numeri inclusi (2 milioni di invocazioni, poi 2 dollari per milione) vengono dalla pagina dei prezzi [71]. La disponibilità di `pg_partman` nei progetti Postgres 17 non è dichiarata esplicitamente [81].
- **flespi**: la tabella dei prezzi e quella della knowledge base non dicono la stessa cosa in una voce (blocco di dispositivi in più): ho usato la knowledge base (2 euro per 100 dispositivi aggiuntivi) [55]. Non ho letto il documento dei limiti ("Restrictions") né la documentazione degli stream.
- **GpsGate, Navixy, Wialon**: nessun prezzo di marca bianca pubblicato. I prezzi degli aggregatori sono incoerenti e li ho segnalati come tali.
- **MapTiler Flex**: la pagina letta non conferma esplicitamente l'uso commerciale; i termini del piano gratuito lo limitano [88].
- **Stadia**: non ho verificato quante tessere consuma in media una sessione di mappa.
- **Mapbox**: i termini richiedono una licenza commerciale per le applicazioni "legate all'uso di veicoli" [92]. Che un'app di tracciamento flotte vi rientri è una mia lettura; la pagina non cita il tracciamento di flotte né dei beni.
- **OpenRouteService**: le quote attuali non le ho trovate; la cifra letta è del 2019 [99].
- **LocationIQ**: il prezzo del piano più basso con geocodifica l'ho letto dalla tabella dei piani; la distinzione tra piani con e senza geocodifica è una mia lettura.

### 6.4 Su mappe, geocodifica e percorsi

- **Dimensioni degli estratti PMTiles** per la Lombardia o il Nord Italia: non trovate; Berlino 84 MB e Puglia circa 200 MB vengono da fonti secondarie.
- **CORS e comportamento di Supabase Storage con i PMTiles**: letto in un articolo senza data certa [82].
- **Fabbisogno di RAM e disco** di OSRM, Valhalla e Nominatim per l'Italia o per la Lombardia: non trovato. OSRM sul pianeta richiede circa 123 GiB di RAM [97].
- **Valhalla**: la pagina del riferimento API rimanda altrove e non l'ho letta. I parametri di Meili vengono dalla pagina di configurazione [98].
- **Aggiornamento di Leaflet**: la pagina menziona solo una 2.0.0-alpha; non ho verificato l'ultima versione stabile [95].
- **Versione di MapLibre**: la pagina cita `maplibre-gl@^6.16.0` negli esempi; non l'ho confermata con il registro npm [94].

### 6.5 Sulle stime mie

- La dimensione di una riga (250 byte con indici) e i MB al mese sono una stima da verificare con `pg_total_relation_size`.
- I tempi di sviluppo di un server Node per il Codec 8E (1-3 giorni per un prototipo, settimane per un servizio solido) sono un giudizio mio, senza dati.
- La sottostima dell'haversine a 30 secondi non ha una fonte.
- Il numero di ricerche inverse al mese (2.200-3.300) dipende da un numero di soste al giorno che ho supposto.
- Il cambio dollaro-euro non è verificato.

### 6.6 Una questione fuori dal perimetro tecnico: lavoro e privacy

Il progetto traccia veicoli guidati da persone. Dai risultati di ricerca (articoli di settore, non i provvedimenti del Garante, che non ho aperto) emerge che in Italia la geolocalizzazione dei mezzi aziendali richiede in generale un accordo sindacale o l'autorizzazione dell'Ispettorato del lavoro ai sensi dell'art. 4 dello Statuto dei lavoratori, salvo il caso in cui lo strumento sia usato dal lavoratore per rendere la prestazione; il Garante ha sanzionato con 50.000 euro (provvedimento del 16/01/2025) un'azienda di autotrasporto che registrava in tempo reale gli spostamenti dei mezzi, e quindi dei conducenti, e ha vietato il controllo continuativo (sec. [102]). Il provvedimento generale del 2011 sui sistemi di localizzazione nei rapporti di lavoro è citato negli stessi articoli (sec. [102]). Non è la mia materia e non l'ho verificato su fonti primarie: va consegnato a un consulente prima di vendere il servizio, perché cambia come si presenta la mappa live (per esempio accesso a posizione continua o solo a viaggi e soste) e cosa si conserva.

---

## 7. Fonti

Tutte le pagine sono state lette il 29/10/2026 con WebFetch o, dove indicato "(sec.)", viste come risultato di ricerca. Le pagine che non si sono aperte o non contenevano la risposta sono elencate nella sezione 6.

**Teltonika e altri marchi**

1. https://wiki.teltonika-gps.com/view/FMB920_First_Start
2. https://wiki.teltonika-gps.com/view/FMB920_Parameter_list
3. https://wiki.teltonika-gps.com/view/Codec
4. https://wiki.teltonika-gps.com/view/Teltonika_Data_Sending_Protocols
5. https://wiki.teltonika-gps.com/view/Codec_JSON
6. https://wiki.teltonika-gps.com/view/FMB920_GPRS_settings
7. https://wiki.teltonika-gps.com/view/FMB920_SMS/GPRS_Commands
8. https://wiki.teltonika-gps.com/view/FMM920_Data_acquisition_settings
9. https://flespi.com/protocols/queclink
10. https://docs.plaspy.com/devices/queclink/gl300/configuration (sec., sito di terzi)
11. https://www.traccar.org/protocols/
12. https://www.traccar.org/devices/
13. https://flespi.com/protocols/teltonika
14. https://forum.flespi.com/d/1116-need-assistance-with-connecting-teltonika-fmb920-device-to-flespi-via-mqtt/1 (sec., risultato di ricerca)
15. https://wiki.teltonika-gps.com/view/FOTA_WEB e https://teltonika-gps.com/product/fota/ (sec., risultati di ricerca, pagine non aperte)
16. Concox/GT06 (sec., risultati di ricerca): https://www.traccar.org/protocol/5023-gt06/X1-GPRS%20Communication%20Protocol%20V1.1.pdf e https://gps-trace.com/devices/concox-gt06n
17. https://flespi.com/protocols/ruptela (sec., risultato di ricerca)

**Traccar**

18. https://www.traccar.org/documentation/
19. https://www.traccar.org/configuration-file/
20. https://www.traccar.org/forward/
21. https://www.traccar.org/traccar-api/
22. https://raw.githubusercontent.com/traccar/traccar/master/openapi.yaml
23. https://www.traccar.org/docker/
24. https://www.traccar.org/optimization/
25. https://github.com/traccar/traccar/releases e https://www.traccar.org/download/
26. https://github.com/traccar/traccar
27. https://www.traccar.org/trips-stops/
28. https://www.traccar.org/reports/
29. https://www.traccar.org/events/
30. https://www.traccar.org/install-vps/
31. https://www.traccar.org/postgresql/
32. https://www.traccar.org/secure-connection/
33. https://www.traccar.org/user-management/
34. https://www.traccar.org/pricing/
35. https://www.traccar.org/osmand/
36. https://www.traccar.org/client/
37. https://www.traccar.org/client-configuration/
38. https://www.traccar.org/client-troubleshooting/
39. https://apps.apple.com/us/app/traccar-client/id843156974
40. https://raw.githubusercontent.com/traccar/traccar/master/src/main/java/org/traccar/config/Keys.java
41. https://raw.githubusercontent.com/traccar/traccar/master/src/main/java/org/traccar/forward/PositionData.java
42. https://raw.githubusercontent.com/traccar/traccar/master/src/main/java/org/traccar/forward/PositionForwarderJson.java
43. https://github.com/traccar/traccar/blob/master/src/main/java/org/traccar/forward/PositionForwarderUrl.java
44. https://raw.githubusercontent.com/traccar/traccar/master/src/main/java/org/traccar/protocol/TeltonikaProtocolDecoder.java
45. https://raw.githubusercontent.com/traccar/traccar/master/src/main/java/org/traccar/handler/DistanceHandler.java
46. https://github.com/traccar/traccar/tree/master/src/main/java/org/traccar/forward
47. https://www.traccar.org/forums/topic/forward-positions-not-working-in-v55/ (sec., forum)
48. https://www.traccar.org/forums/topic/forward-url-per-device/ (sec., forum)
49. https://geopulse.cc/docs/user-guide/gps-sources/traccar (sec., guida di terzi)
50. https://www.traccar.org/forums/topic/how-do-i-forward-events/ (sec., forum)
51. https://www.traccar.org/forums/topic/recommended-hardware-requirements/ e https://www.traccar.org/forums/topic/traccar-system-requirements2/ (sec., forum, da un risultato di ricerca)
52. https://www.traccar.org/forums/topic/traccar-client-on-ios-not-permitted-on-background/ e altri thread elencati in un risultato di ricerca (sec., forum)
53. https://www.traccar.org/forums/topic/calculating-distance-covered-and-time-data-is-sent/ (sec., risultato di ricerca)

**flespi e piattaforme**

54. https://flespi.com/pricing
55. https://flespi.com/kb/how-flespi-pricing-works
56. https://flespi.com/
57. https://gpsgate.com/pricing
58. https://wialon.com/en/pricing
59. https://www.navixy.com/pricing/
60. https://www.softwaresuggest.com/navixy/pricing (sec., aggregatore, risultato di ricerca)

**Librerie npm**

61. https://registry.npmjs.org/teltonika-parser
62. https://registry.npmjs.org/teltonika-codec-parser
63. https://registry.npmjs.org/complete-teltonika-parser
64. https://registry.npmjs.org/teltonika-parser-ex
65. https://registry.npmjs.org/@groupe-savoy%2Fteltonika-sdk
66. https://registry.npmjs.org/-/v1/search?text=teltonika&size=25 (e `text=teltonika%20codec`); le richieste a https://registry.npmjs.org/node-teltonika e https://registry.npmjs.org/codec8 hanno dato 404
67. https://groupe-savoy.github.io/teltonika-sdk/index.html

**Hosting, Supabase, PostgREST**

68. https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/
69. https://docs.hetzner.com/cloud/servers/primary-ips/overview/
70. https://www.hetzner.com/cloud/
71. https://supabase.com/pricing
72. https://supabase.com/docs/guides/database/extensions/postgis
73. https://supabase.com/docs/guides/realtime/limits
74. https://supabase.com/docs/guides/platform/manage-your-usage/realtime-messages
75. https://supabase.com/docs/guides/platform/manage-your-usage/disk-size
76. https://supabase.com/docs/guides/functions/limits
77. https://supabase.com/docs/guides/functions/auth
78. https://supabase.com/docs/guides/storage/uploads/file-limits
79. https://supabase.com/docs/guides/realtime/subscribing-to-database-changes
80. https://supabase.com/docs/guides/database/extensions/timescaledb
81. https://supabase.com/docs/guides/database/extensions/pg_partman
82. https://supabase.com/blog/self-host-maps-storage-protomaps
83. https://docs.postgrest.org/en/stable/references/api/functions.html

**Mappe, geocodifica, percorsi**

84. https://operations.osmfoundation.org/policies/tiles/
85. https://operations.osmfoundation.org/policies/nominatim/
86. https://www.openstreetmap.org/copyright
87. https://www.maptiler.com/cloud/pricing/
88. https://www.maptiler.com/terms/cloud/
89. https://docs.maptiler.com/cloud/api/geocoding/
90. https://stadiamaps.com/pricing/
91. https://www.mapbox.com/pricing
92. https://www.mapbox.com/legal/tos
93. https://docs.protomaps.com/ e https://docs.protomaps.com/basemaps/downloads
94. https://github.com/maplibre/maplibre-gl-js e https://maplibre.org/maplibre-gl-js/docs/
95. https://leafletjs.com/
96. https://github.com/komoot/photon
97. https://github.com/Project-OSRM/osrm-backend , https://github.com/Project-OSRM/osrm-backend/wiki/Demo-server , https://github.com/Project-OSRM/osrm-backend/wiki/Disk-and-Memory-Requirements
98. https://valhalla.github.io/valhalla/ e https://valhalla.github.io/valhalla/contributing/architecture/meili/configuration/
99. https://ask.openrouteservice.org/t/updated-api-quotas/500 (sec., forum, post del 06/05/2019)
100. https://locationiq.com/pricing
101. https://postgis.net/docs/ST_ClusterDBSCAN.html , https://postgis.net/docs/ST_FrechetDistance.html , https://postgis.net/docs/ST_Length.html , https://postgis.net/docs/ST_DWithin.html

**Lavoro e privacy**

102. https://www.agendadigitale.eu/sicurezza/privacy/tracciamento-gps-sul-lavoro-come-rispettare-statuto-dei-lavoratori-e-gdpr/ e https://www.quotidianopiu.it/dettaglio/11245943/geolocalizzazione-dei-veicoli-aziendali-trattamento-illecito-di-dati (sec., articoli di settore da un risultato di ricerca)
