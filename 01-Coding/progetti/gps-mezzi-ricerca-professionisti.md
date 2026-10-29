---
type: risorsa
riga: Rapporto integrale del 29/10/2026 su cosa montano gli operatori italiani di telematica, le funzioni per livello, il tacografo, FMC650 e telecamere, tempi di installazione. Sintesi in gps-mezzi-opzioni.
updated: 2026-10-29
source: claude
tags: [gps, flotta, ricerca, telematica, tacografo]
---

> Rapporto scritto da un agente Sonnet il 29/10/2026 per [[gps-mezzi-opzioni]].
> Codici: L = pagina letta, R = da riassunto di ricerca, M = memoria del
> modello. Trevis ha ricontrollato il listino Trackyup sulla pagina. Le cifre
> di manodopera sono stime dell'agente, non listini.

# Cosa montano i professionisti: telematica per flotte in Italia

Rapporto di ricerca per DenkiCode, scritto il 29 ottobre 2026. Tutte le pagine citate sono state aperte o cercate in quel giorno.

**Codici usati in ogni tabella**
- **L**: pagina letta con WebFetch il 29/10/2026. Il testo che WebFetch restituisce è già riassunto da un modello piccolo, quindi i numeri sono riportati come tornati e vanno ricontrollati prima di finire in un'offerta a un cliente.
- **R**: dato che viene solo dal riassunto di una ricerca, senza aver letto la pagina (spesso perché la pagina rispondeva 403 o non si apriva).
- **M**: memoria o stima mia, non verificata. Dove compare, lo scrivo nella frase.

Le sigle tra parentesi quadre, per esempio [T2], rimandano alla sezione 7, dove ogni fonte ha URL, data di lettura e codice.

---

## 1. Cosa montano gli operatori italiani

### 1.1 Tabella degli operatori

| Operatore | Tipo di dispositivo | Marchio del tracker dichiarato | Cosa offre nel pacchetto | Canone e installazione pubblicati | Fonti |
|---|---|---|---|---|---|
| **Targa Telematics** (ha comprato Viasat nel 2023; il sito viasatonline.it ora rimanda a targatelematics.com) | Le pagine di prodotto non descrivono l'hardware. L'articolo su Viasat Fleet parla di «dispositivi di bordo» con installazione «rapida e non invasiva». Targa vende anche un localizzatore col proprio nome, il Targa Ghost GL51 (R). | Non dichiarato. Targa si presenta come indipendente dall'hardware (R). L'acquisto di Viasat ha escluso la progettazione e produzione dell'elettronica (L). | **Fleet Light**: posizione in tempo reale, report, soste, modalità privacy, manutenzione, sinistri. **Light & Security**: in più recupero del veicolo rubato e **blocco dell'avviamento da remoto**. **Fleet Start / Advanced**: geofencing, eco-driving, consumi, diagnostica remota (codici DTC), rilevamento incidenti, recupero H24. **Su richiesta**: identificazione del conducente e pulsante SOS. **Mezzi pesanti** (Targa Tacho): scarico remoto dei dati del tachigrafo, identificazione del conducente, temperatura. Telecamere e FMS: non nominati (L). | Non pubblicati: «richiedi una consulenza». | [A1][A2][A3][A4][A5][A6][A7][A8] L; Ghost e «hardware agnostic» [A9] R |
| **Viasat** (oggi dentro Targa) | Satellitari per auto e commerciali; per le auto elettriche e ibride a noleggio i modelli S-Box Evo e 2S Evo (articolo del 26/11/2022). Il Runtracker 5.5 è citato in un accordo con Nexive (R, data non letta). | Proprio, secondo la mia memoria (M); nel 2023 la progettazione e produzione dell'elettronica è rimasta fuori dalla vendita a Targa (L). | Piattaforma Viasat Digital Connect, centrale operativa H24 con chiamata di emergenza, recupero veicolo, perizia telematica dei sinistri. Il CAN non è citato. | Non pubblicati. Un forum del 2022 dice che per il Viasat 2S «l'installazione dipende dal singolo installatore» e che il 3S costa 235 euro all'anno (R, fonte debole). | [A8][A10] L; [A11][A12] R |
| **Trackyup** (marchio di YUP srls, Brescia) | Tutti Teltonika. Presa **OBD** (FMB003, FMC003), **cablati** (FMC920, FTC921 nascosto, FMC130, FMC650, FMC250 e altri), **a batteria** (TAT240, TAT140). | **Teltonika, dichiarato.** Dichiara anche che la piattaforma è di Gurtam (Lituania) con marchio Trackyup, e che non produce l'hardware. | Posizione, percorsi, soste, storico; avvisi su zone e orari; chilometri e ore motore; odometro e carburante da OBD «dove il veicolo li espone»; esportazione PDF/CSV; sensori di temperatura Bluetooth con l'FMC130. **Dichiara di non offrire**: blocco motore, centrale operativa, cronotachigrafo, dashcam, identificazione dell'autista. | **Kit con SIM e 12 mesi**: FMB003 159 euro, FMC003 188, FMC920 143, FTC921 145, FMC130 151, FMC250 212, FMC650 237, TAT240 205 (IVA inclusa). **Canone dopo i mesi inclusi: 6 euro + IVA al mese** per dispositivo, senza vincolo. Manodopera di installazione esclusa e senza importo. | [B1]–[B9] L |
| **Macnil / GT Alarm** (gruppo Zucchetti) | «Black box» a marchio GT Alarm; i modelli non sono elencati. L'app parla di GT Alarm Black Box 4.0 (R). | Proprio (GT Alarm). | **GT Fleet 365**: posizione in tempo reale, storico di percorsi, soste e velocità, **antifurto satellitare con centrale operativa H24** (livello 6 della Scala Vanini), **riconoscimento degli autisti**, **scarico remoto dei file del tachigrafo**, controllo carburante, stile di guida, scadenze di manutenzione. | Non pubblicati: preventivo da info@macnil.it. | [C1][C2][C3] L |
| **Octo Telematics** | Nata per le assicurazioni. Scatola sul parabrezza (SmartSOS Pro) e una versione OBD con chiave (SmartKeyLess, installazione sotto i 15 minuti), secondo comunicati (R). | Octo non produce: in Italia comprava da Magneti Marelli e Meta System (R, articolo datato). | Fleet Essentials: report su ore di guida e consumi, allarmi, geofencing, punteggio di guida, diagnostica remota, dati automatici in caso di incidente. Identificazione dell'autista e blocco motore: non confermati. | Non pubblicati. | [D1] L; [D2][D3][D4] R |
| **LoJack Italia** | Antifurto con radiofrequenza e telematica; per i mezzi da cantiere accordi con BigRent e CGTE (R). Si monta in un punto nascosto, senza collegarsi all'impianto (R, forum). | Proprio (tecnologia CalAmp, M). | AI Theft Detection con centrale operativa 24 ore su 24, app My LoJack, piattaforma flotte che unisce telematica del veicolo e dati LoJack, posizione, diagnostica, chilometri, consumi, stile di guida. CAN, blocco motore, tachigrafo e identificazione autista: non citati. | Non pubblicati per le flotte. Un forum del 2022 dà LoJack Go a 199 euro con un anno, rinnovo 100 euro l'anno (R, fonte debole). | [E1][E2] L; [E3] R |
| **Webfleet Italia** (gruppo Bridgestone) | **LINK 245**: OBD, installazione autonoma, Bluetooth. **LINK 640**: fisso, per auto e furgoni. **LINK 740**: fisso, qualsiasi veicolo. **LINK 340 / 350**: rimorchi e macchinari (batteria). **CAM Lite / CAM Pro**: dashcam con intelligenza artificiale, «progettate per l'installazione professionale con cablaggio». | Proprio. | Posizione, stile di guida, diagnostica, carburante e CO2, coaching, navigazione, **Tachograph Manager** per lo scarico remoto, dashcam con rilevamento di distrazione, fumo, cintura e telefono, driver ID. | Prezzi non pubblicati. Offerta in Italia sul LINK 245: 3 mesi di prova gratuita, contratto da 39 mesi, per contratti firmati dal 01/04/2023 al 31/12/2026. Il LINK 340 costa 253,99 euro da un rivenditore lettone (R). | [F1]–[F4] L; [F5] R |
| **Geotab Italia** (dal 2026 contiene anche Verizon Connect Italia / Visirun, ex Fleetmatics) | **GO9 / GO9+**: OBD II, «senza antenne, saldature né installatori professionisti». | Proprio. | MyGeotab: carburante, manutenzione, coaching, dashcam, tachigrafo digitale, veicoli elettrici, marketplace con oltre 200 soluzioni. | Non pubblicati in Italia. Un listino tedesco di Telefónica (ottobre 2023) mette il GO9 a 8,90 / 14,90 / 17,90 euro al mese con SIM (R, estero). Verizon Connect: 40 dollari al mese per veicolo con contratto di 36 mesi (R, Stati Uniti); nessun listino italiano. | [G1] L; [G2][G3] R |
| **Quartix Italia** | Dispositivo proprio; il sito parla di opzioni cablate, OBD e a batteria (R), senza dettagli. | Proprio. | **Info Point** (posizione ogni 2 minuti), **Info Plus** (ogni minuto, geofencing, comportamento di guida), **Info Drive** (gestione di conducente e veicolo, carta carburante). Identificazione del conducente come componente aggiuntivo. Telecamere: non citate. | **9,99 / 11,99 / 13,99 euro al mese per veicolo, installazione inclusa, contratto da 12 a 60 mesi.** La pagina si contraddice su rinnovo e sconti. | [H1][H2] L |
| **Movolytics** | Non è un operatore italiano. È una società inglese di Cambridge, comprata dal gruppo norvegese Abax il 5 dicembre 2023 (R); il sito movolytics.com ora rimanda ad Abax. | Non dichiarato. | Tracciamento, carburante, stile di guida, manutenzione (R). | Non cercati. | [I1] L (rimando); [I2] R |
| **Cartrack Italia, Vodafone Automotive** | Non trovati. cartrack.it non si risolve; per Cartrack escono solo pagine sudafricane. Per Vodafone Automotive nessun risultato italiano utile. | | | | R |

### 1.2 Cosa se ne ricava

- **Un solo operatore dichiara il marchio del tracker**: Trackyup (Teltonika, con piattaforma Gurtam). Per i colleghi più grandi il tracker è proprio o non è nominato. Per DenkiCode, che vuole i dati sul proprio server, questo significa che il mercato italiano delle piccole flotte è raggiungibile con hardware Teltonika, perché lo fa già un integratore bresciano allo stesso prezzo di listino.
- **Il dispositivo cambia con il servizio venduto.** Chi vende solo posizione e report (Geotab GO9, Webfleet LINK 245, Octo KeyLess) usa un dispositivo OBD che si monta da soli. Chi vende antifurto con centrale operativa (Macnil, LoJack, Targa e Viasat) monta una scatola nascosta. Chi vende tachigrafo (Targa Tacho, Macnil, Webfleet) lavora sui camion con un dispositivo cablato che legge il tachigrafo. L'attribuzione a ogni operatore è mia, perché le pagine non descrivono sempre l'hardware.
- **Le tre funzioni che gli operatori italiani mettono davanti** (lettura mia dei pacchetti pubblicati, non una classifica di vendite, che non esiste in pubblico):
  1. posizione in tempo reale con storico di percorsi e soste (presente in tutti gli operatori; secondo Geotab il 66% delle flotte italiane la usa quasi in tempo reale, su 200 fleet manager intervistati [G4] L);
  2. antifurto e recupero del veicolo rubato con centrale operativa (Targa, Viasat, Macnil, LoJack, Octo);
  3. stile di guida, consumi e scadenze di manutenzione (Targa Fleet Start, Macnil, Octo, Quartix, Webfleet).
  Sui mezzi pesanti compare in quarta posizione lo scarico remoto del tachigrafo (Targa Tacho, Macnil, Webfleet).
- **Prezzi pubblicati**: solo due operatori mostrano un listino italiano, Trackyup (6 euro + IVA al mese e kit da 143 a 237 euro) e Quartix (da 9,99 a 13,99 euro al mese, installazione inclusa). Gli altri chiedono un preventivo. Il confronto utile per DenkiCode è quindi tra 6 e 14 euro al mese per veicolo sul mercato visibile.
- Nelle ricerche sono comparsi due dati incoerenti su Trackyup (la homepage letta il 29/10/2026 dice 6 euro e 143 euro; uno snippet di ricerca parlava di 4,5 euro e 72 euro). Vale la pagina letta [B2].

---

## 2. Le funzioni che fanno la differenza tra i livelli

Il marchio di riferimento è Teltonika, perché è quello che DenkiCode può comprare. Le specifiche vengono dal wiki Teltonika salvo dove indicato.

| Funzione | Hardware necessario | Quando serve | Fonti |
|---|---|---|---|
| **Posizione, percorsi, soste** | Qualsiasi tracker GNSS con SIM. | Sempre. È il livello base. | [B3] L |
| **Dati letti dalla presa OBD** (chilometri, carburante «dove il veicolo li espone») | Tracker con presa OBD (FMB003 solo 2G, FMC003 con 4G). | Quando basta una lettura semplice e il cliente monta da solo. | [B3][B4] L |
| **Identificazione dell'autista** | Chiave **iButton** (Dallas) con lettore sul bus 1-Wire; in alternativa tessera RFID o beacon Bluetooth. Ogni ID va inserito per intero (16 caratteri esadecimali); con il firmware 03.27.xx l'elenco arriva a 4000 chiavi. Una chiave iButton Teltonika costa 2,03 euro IVA esclusa (non disponibile al momento); un lettore circa 9,30 euro più 14 di spedizione su un negozio maltese (R, dubbio). | Quando lo stesso mezzo lo usano più persone, o per collegare un viaggio a un nome. Targa e Quartix la vendono come aggiunta. | [W6] L; [J1] L; [J2] R |
| **Blocco motore a distanza e immobilizer** | Un'uscita digitale del tracker (open collector, 0,5 A, commuta verso massa) che comanda un **relè** a 5 pin sul circuito del motorino d'avviamento, con fusibile. Il wiki dice che l'immobilizer può agire sul relè di avviamento o della pompa del carburante e che si sblocca con iButton, RFID o beacon. La guida del produttore sconsiglia di toccare carburante o accensione, per non spegnere un mezzo in marcia. Il blocco da remoto vero e proprio compare solo sulla serie FMB con firmware 03.28.02 o successivo (R). | Quando il cliente vuole impedire l'avvio a chi non è autorizzato, o fermare un mezzo rubato. Trackyup non lo vende e ricorda che sui mezzi in garanzia può non essere ammesso. Targa lo vende nel pacchetto Light & Security. | [W7] L; [W13] L; [B9] L; [A3] L; [J3] R |
| **Lettura del bus CAN** | **LV-CAN200**: auto leggere, furgoni, camion, autobus; legge chilometri, livello e consumo di carburante, giri motore, temperatura del liquido. **ALL-CAN300**: in più circa 100 parametri (stato porte, AdBlue, olio, ore motore, airbag) e anche macchine agricole e da cantiere. **CAN-CONTROL**: legge VIN, freno a mano e consumo, e chiude porte e finestrini da remoto. **ECAN02**: lettore senza contatto che si affianca a LV-CAN200 o ALL-CAN300 per leggere il CAN senza tagliare i fili; per due linee CAN ne servono due (R). Lo schema di collegamento dipende da marca, modello e anno e lo fornisce la rete vendita Teltonika (R). I trackers FMC150 hanno l'adattatore integrato (R); l'FMC650 ha due CAN J1939 nativi per l'FMS dei camion. Lo stato delle **cinture** non compare nelle schede che ho letto: non lo posso confermare. | Quando servono chilometri veri (manutenzione, rimborsi), livello carburante dal vano, giri motore. Sui camion con FMS non serve l'adattatore. | [W8] L; [W12] L; [J4][J5] R |
| **Stile di guida** (frenate, accelerazioni e curve brusche) | Nessun hardware in più: l'accelerometro interno del tracker. Il wiki dice che l'accelerometro è più preciso del solo GPS a 1 Hz. | Quando il cliente vuole un punteggio per autista o un avviso. Targa, Macnil, Octo, Quartix e Webfleet lo vendono. | [W7] L |
| **Temperatura del vano frigo** | Sensore **EYE Sensor** (BTSMP1) Bluetooth con batteria propria: da -20 a +60 gradi, umidità 0-100%, portata circa 80 metri (R); Trackyup lo abbina all'FMC130 (kit 151 o 217 euro; prezzo dei sensori non pubblicato). In alternativa fino a 4 sonde cablate Dallas (DS18B20) sul bus 1-Wire dell'FMC130 (L). Una variante certificata EN 12830 compare in un elenco di rivenditore (R, da verificare). | Furgoni frigo e trasporto alimentare. Se serve un registro valido per i controlli, vanno verificati la certificazione e la taratura del sensore (M). | [B7] L; [W6] L; [W14] L; [J6][J7] R |
| **Tachigrafo digitale** (scarico remoto dei file DDD) | **FMC650 / FMC640 / FMB640 / FMM650** (sezione 4) oppure **FMx150** con firmware speciale; collegamento ai contatti CAN2 del tachigrafo (C5 e C7) e K-Line; servizio **TachoSync** con carta aziendale in un lettore. Tachigrafi supportati: VDO DTCO 1381 (versione 1.3a o successiva), Stoneridge SE5000 (7.1 o successiva), Intellic EFAS 4.5 o successiva; per l'FMx150 il wiki indica VDO DTCO 4.0 o successivo. Segnale FMS di scarico previsto per DAF, Iveco, Renault e Volvo; per MAN, Mercedes e Scania occorre il costruttore. | Camion sopra 3,5 tonnellate; furgoni 2,5-3,5 t in trasporto internazionale dal 1 luglio 2026 (sezione 3). | [W2] L; [W12] L; [T17] L |
| **FMS / J1939** | FMC650 / FMC640 (due CAN J1939). | Camion e autobus che espongono i dati FMS. | [W1][W3] L |
| **Telecamere** | **DualCam** su RS232 (una verso la strada e una verso l'abitacolo): FMC125, FMC225 (e FMB125/225) e FMC650. **DSM** (monitoraggio dell'autista): FMC650. Sull'FMC650 le due porte RS232 permettono di averle entrambe. | Camion e mezzi che richiedono prove video o prevenzione della stanchezza. Servono nuove cautele privacy (non trattate qui). | [W9][W10] L |
| **Sensori di livello carburante** | **Technoton DUT-E** (sonda a immersione, varianti RS485, RS232, Bluetooth): Technoton dichiara la compatibilità confermata con l'FMC125 (R); la scheda tecnica dell'FMC650 elenca RS485 con sonde digitali e analogiche, LV-CAN200 e FMS (R). **Escort TD-BLE** (Bluetooth): si configura nella scheda «Bluetooth 4.0» del tracker con il preset «escortfuel», fino a 4 sensori per tracker (R). Prezzi: DUT-E 485 a 139 euro sullo shop Technoton (valuta non indicata); TD-BLE a 82 dollari su un rivenditore americano (R). | Serbatoi grandi, flotte con rischio di furto di carburante. La sonda a immersione richiede di intervenire sul serbatoio e di tararla (M). | [K1][K2][K3] R |
| **Rimorchi e attrezzature** | Tracker a **batteria**: Trackyup TAT240 (205 euro, 4G, IP68, allarme di rimozione), TAT140 (191); Webfleet LINK 340 (fino a 90 giorni con batteria piena, posizione una volta al giorno senza alimentazione esterna). | Rimorchi, container, macchinari senza corrente. | [B3] L; [F5] R |

---

## 3. Il tacografo in Italia

### 3.1 Cosa dice la norma

- **Il regolamento (UE) 165/2014 non fissa gli intervalli di scarico.** L'articolo 33 chiede all'impresa di conservare fogli di registrazione, stampe e dati scaricati, in ordine cronologico e leggibili, **per almeno un anno** dall'uso, e di consegnarli ai controllori. L'articolo 33, comma 2, prevede anche che l'impresa consegni al conducente che li chiede le copie dei dati scaricati dalla sua carta [T6] L.
- **Gli intervalli stanno nel regolamento (UE) 581/2010, articolo 1, comma 3**: il periodo massimo entro cui scaricare non deve superare **90 giorni per i dati dell'unità di bordo** (la memoria del veicolo) e **28 giorni per i dati della carta del conducente** [T1] L. I termini sono massimi: gli Stati possono fissarne di più brevi.
- **In Italia** una circolare FAI del 5 luglio 2010 ricordava che il decreto del Ministero del Lavoro del 31 marzo 2006 imponeva **tre mesi** per l'unità e **tre settimane** per la carta, e riteneva quei termini ancora applicabili finché i ministeri non chiarivano [T2] L. Non ho trovato un testo recente che dica se il decreto del 2006 sia stato abrogato. Le fonti italiane del 2016-2026 che ho letto (LeggiOggi, Tach Consulting, Gruppo Valiani, Webfleet Italia) riportano tutte **90 e 28 giorni** [T3][T4][T5][T12] L. La prudenza dice di scaricare la carta ogni 21 giorni e l'unità ogni 2 mesi, finché non si legge il testo in vigore (M).
- **Conservazione**: almeno 12 mesi dei dati scaricati [T3][T4] L.
- **Controllo su strada**: dal 31 dicembre 2024 il conducente deve poter mostrare le registrazioni del giorno in corso e dei **56 giorni** solari precedenti, non più 28 [T7] L. È un obbligo di esibizione al controllo, non un intervallo di scarico. Un blog spagnolo di Geotab scrive che la carta dei tachigrafi G2V2 si scarica ogni 56 giorni [T15] L: non l'ho trovato in nessun testo normativo e **non lo uso**.

### 3.2 Per quali mezzi

| Mezzo | Obbligo | Fonti |
|---|---|---|
| Veicoli sopra 3,5 tonnellate e autobus con più di 9 posti | Tachigrafo digitale già obbligatorio. | [T8] L |
| Veicoli e complessi da **più di 2,5 fino a 3,5 tonnellate** (rimorchi inclusi) in **trasporto internazionale di merci o cabotaggio**, dal **1 luglio 2026** | **Tachigrafo intelligente di seconda generazione, versione 2 (G2V2)** con carta del conducente. Circolare MIT n. 9674 del 16 aprile 2026. Valgono i tempi di guida e riposo dei mezzi pesanti (9 ore al giorno, 45 minuti di pausa dopo 4,5 ore, 11 ore di riposo). | [T9][T10][T11] L |
| Stesso furgone, ma **trasporto nazionale** | Nessun tachigrafo: l'obbligo del 2026 riguarda solo internazionale e cabotaggio. | [T10] L |
| Furgone 2,5-3,5 t che porta merci **proprie** (conto proprio) | Un articolo di trans.info (FAQ) riporta una deroga ai sensi dell'articolo 3 del regolamento 561/2006 se guidare non è l'occupazione principale del dipendente. Due fonti sulla circolare MIT dicono invece che il testo non distingue tra conto terzi e conto proprio. **Fonti discordanti: da verificare sulla circolare.** | [T11][T9][T10] L |

- **Sanzioni in Italia** (trans.info, FAQ): da 866 a 3.464 euro, installazione entro 10 giorni, sospensione della patente da 15 giorni a 3 mesi [T11] L. Un altro titolo parla di 7.000 euro (R), non verificato.
- **Chi installa**: solo un'officina certificata, che provvede anche alla taratura [T13] L.
- **Costo**: il tachigrafo G2V2 costa circa 1.000 euro più installazione (trans.info, R). Una stima di settore da PMI.it dice **900-2.400 euro per veicolo** per adeguare un furgone (R: la pagina rispondeva 403). La carta del conducente costa 37 euro alla Camera di commercio (R).

### 3.3 Cosa decide per i livelli

- **Il livello «camion» (sopra 3,5 tonnellate) deve includere il tacografo**: il mezzo ce l'ha per legge e l'azienda deve scaricare la carta ogni 28 giorni e l'unità ogni 90. Lo scarico remoto è la funzione che i clienti pagano di più (Targa Tacho, Macnil, Webfleet).
- Il tracker **non sostituisce** il tachigrafo e non produce dati validi per il controllo dei tempi di guida: lo dice anche Trackyup [B5] L. Il tracker fa da ponte per scaricare i file DDD; servono la carta aziendale e un servizio come TachoSync.
- **Per i furgoni delle piccole aziende milanesi** il tachigrafo serve solo se il cliente fa **trasporto internazionale o cabotaggio** con mezzi tra 2,5 e 3,5 tonnellate. Per il giro di consegne in Lombardia non è richiesto, quindi non va nei livelli da 1 a 4. Conviene chiedere al cliente, in fase di vendita, se attraversa il confine.
- Teltonika propone l'**FMx150** (non l'FMC650) per scaricare i file dai furgoni [T17] L, perché richiede meno cablaggio: è un'alternativa più economica dell'FMC650 per il caso «furgone internazionale».

---

## 4. FMC650, FMC640/FMB640, DualCam e DSM

### 4.1 Confronto con l'FMC130

| Caratteristica | FMC130 | FMC650 | FMC640 | FMB640 |
|---|---|---|---|---|
| Rete | 4G | 4G | 4G; doppia SIM più eSIM | solo 2G |
| Ingressi digitali | 3 | **4** | 4 | 4 |
| Ingressi analogici | 2 | **4** (0-10 V e 0-30 V) | 4 | 4 |
| Uscite digitali (open collector, 0,5 A) | 3 | **4** | 4 | 4 |
| CAN | 2 linee LVCAN (adattatore esterno) | **2 CAN J1939 più J1708** | 2 CAN J1939 più J1708 | 2 CAN J1939 più J1708 |
| K-Line (dati live del tachigrafo) | no | **sì, integrata** | sì | sì |
| RS232 / RS485 | non citate | **2 RS232 e 1 RS485** | 2 RS232 e 1 RS485 | 2 RS232 e 1 RS485 |
| 1-Wire | sì (termometri Dallas, iButton) | sì | sì | n.d. |
| Bluetooth | 4.0 LE | 5.0 | n.d. | n.d. |
| Tachigrafo, scarico remoto | no | **sì** | sì (dettagli assenti) | non citato nella pagina |
| Alimentazione | 10-30 V | **8-32 V** | 10-30 V | 10-30 V |
| Memoria | n.d. | 16 MB (10 usati per i record) più microSD | n.d. | n.d. |
| Batteria interna | 170 mAh Li-ion | 550 mAh Ni-MH | n.d. | n.d. |

Fonti: [W5] [W1] [W3] [W4] L. Il datasheet dell'FMC650 v2.2 (10/11/2025) conferma i numeri e aggiunge una porta mini-USB (R). Navixy scrive 5 ingressi digitali: vale il wiki Teltonika (4).

- Lo scarico del tachigrafo **Smart v2** è supportato solo su FMC650, FMM650, FMB641, FMB640, FMC640 e FMM640 [W2] L.
- L'**FMB640 è solo 2G**: per un prodotto nuovo conviene l'FMC650 (4G). Trackyup vende ancora dispositivi «solo 2G (Italia)», ma non ho trovato fino a quando la rete 2G resterà attiva.
- **FMx150**: ha il tachigrafo come funzione opzionale con firmware dedicato (attivabile a pagamento su unità già vendute), supporta VDO, Stoneridge e EFAS; Teltonika consiglia l'FMx650 per le flotte grandi che vogliono più funzioni [T17] L. Il wiki dell'FMx150 non nomina FMC150/FMB150 e non parla di Smart v2.

### 4.2 DualCam e DSM

| | DualCam | DSM |
|---|---|---|
| Cosa fa | Unità sul parabrezza con due telecamere (il wiki dice anteriore e posteriore; il rivenditore la chiama «abitacolo e strada»). Registra il video prima e dopo un evento come un incidente, scatta foto periodiche o su richiesta e manda i dati al server. | Telecamera di monitoraggio dell'autista con apprendimento automatico: **sonnolenza, distrazione, sbadigli**, con invio periodico di eventi e immagini o video. Il wiki **non** cita telefono, fumo o cintura: non li posso confermare. |
| Con quali tracker | FMC125, FMC225 (e FMB125, FMB225), **FMC650**, via RS232 | **Solo FMC650**, via RS232 (cavo incluso) |
| Insieme | Sull'FMC650 le due porte RS232 permettono DSM su una e DualCam o DashCam sull'altra. | |
| Prezzo (rivenditore tedesco Lieske, netto) | **111,69 euro** (132,91 con IVA tedesca), più 24 euro di spedizione in Italia; su ordinazione, circa 20 giorni lavorativi | Kit **DSM più FMC650: 371,44 euro** netti (442,01 con IVA tedesca), più 24 euro di spedizione; su ordinazione, circa 20 giorni lavorativi |
| Non verificato | Risoluzione, ADAS, capacità di archiviazione: il wiki non li riporta (c'è un datasheet v1.3 del 15/11/2025 che non ho letto). | Altri tracker compatibili. |

Fonti: [W9][W10][J8][J9] L.

---

## 5. Tempi e costi di installazione per livello

Riga per riga, dico se la cifra è un **listino vero** (L, pubblicato da un operatore italiano o da un rivenditore) o una **stima mia** (M). Un solo operatore italiano pubblica tempi: Trackyup. **Nessuna fonte italiana pubblica il prezzo della manodopera.**

| Livello | Chi installa | Tempo | Manodopera | Hardware (listino) |
|---|---|---|---|---|
| **1. OBD** | Il cliente, da solo | **meno di 2 minuti** se la presa è libera (Trackyup, L). Geotab: senza installatori (L). Octo KeyLess: meno di 15 minuti (R). | Zero. | FMB003 159 euro (solo 2G), FMC003 188 euro (4G), con SIM e 12 mesi, IVA inclusa (L). |
| **2. Cablato base** | Elettrauto o installatore; Trackyup manda lo schema e assiste al telefono | **30-60 minuti** (Trackyup, L) | **Non pubblicata** (L: «la pagina non ne indica l'importo»). **Stima mia (M): circa 55-66 euro + IVA**, ricavata da un'ora di lavoro alla tariffa oraria 2026 delle carrozzerie di Livorno e Piombino (60-66 euro + IVA, R); non ho trovato la tariffa di un elettrauto milanese. Riferimenti esteri: 50-150 sterline per veicolo nel Regno Unito (R); 120-159 dollari l'ora in negozio negli Stati Uniti, un'ora di minimo (L, articolo del 27/04/2026). | FMC920 143 euro, FTC921 145 euro (nascosto, 10-90 V), con 12 mesi, IVA inclusa (L). |
| **3. Cablato con relè** (blocco motore) | Elettrauto | Non pubblicato. **Stima mia (M): 1,5-2 ore**, perché si aggiungono relè, fusibile e il filo dell'uscita digitale sul circuito del motorino d'avviamento (schema nella guida del produttore, L). | Non pubblicata (M: circa 80-130 euro + IVA con la stessa tariffa oraria). | Tracker come sopra (FMC130 151 euro); il relè a 5 pin non ha un prezzo trovato. Targa vende il blocco nel pacchetto Light & Security senza prezzo. |
| **4. iButton e CAN** | Elettrauto con lo schema del costruttore | Non pubblicato. **Stima mia (M): 2-3 ore.** Lo schema del CAN dipende da marca, modello e anno e si chiede a Teltonika (R); l'ECAN02 senza contatto evita di tagliare i fili. | Non pubblicata (M: 110-200 euro + IVA). | FMC130 151 euro o FMC250 212 euro (con CAN, IP67) (L). Chiave iButton 2,03 euro netti, lettore circa 9 euro (L/R). **LV-CAN200, ALL-CAN300, ECAN02: prezzo non trovato.** |
| **5. Camion con tacografo e telecamere** | Il tracker: installatore specializzato. Il tachigrafo: **solo officina certificata** (L) | Non pubblicato. La guida Teltonika per l'Actros ha 7 passi (coppia CAN, K-Line, resistenza, alimentazione e accensione, antenna, configurazione, verifica con l'SMS «tachocheck») senza indicare i tempi (L). **Stima mia (M): mezza giornata a una giornata**, più i giorni di attesa dell'officina. | Non pubblicata. Webfleet scrive che le dashcam sono «progettate per l'installazione professionale con cablaggio» (L). | FMC650 237 euro (Trackyup, L); DualCam 111,69 euro netti; kit DSM più FMC650 371,44 euro netti (Lieske, L). Tachigrafo G2V2 circa 1.000 euro (R) o 900-2.400 euro per veicolo tutto compreso (R). |

**Note**
- **Il listino vero**: solo la colonna «Hardware» e i tempi di Trackyup. Tutte le cifre di manodopera sono stime mie o riferimenti esteri.
- **Dove chiedere preventivi veri**: almeno due elettrauto della zona di Milano per i livelli 2-4, e due centri tecnici autorizzati al tachigrafo per il livello 5. TBS Services (officina mobile con sede a Rho) pubblicizza un prezzo di installazione fisso su tutto il territorio ma la cifra non è nell'articolo del 2019 [L1] L.
- **Cosa Trackyup esclude**: la manodopera non è inclusa nel kit né nel canone, «salvo accordo scritto diverso» [B4] L.

---

## 6. Cosa non ho potuto verificare

1. **Prezzi di Targa/Viasat, Macnil, Octo, LoJack, Webfleet, Geotab/Verizon Connect in Italia**: non sono pubblicati. Ho trovato solo cifre estere (Telefónica Germania per Geotab, Stati Uniti per Verizon Connect) e due prezzi di forum del 2022 su Viasat e LoJack.
2. **Hardware attuale di Targa e Viasat**: le pagine non nominano i modelli. Il Targa Ghost GL51 compare solo in un opuscolo che non ho letto.
3. **Il testo ufficiale su EUR-Lex**: gli articoli dei regolamenti 165/2014 e 581/2010 non si sono aperti da EUR-Lex. Ho usato legislation.gov.uk (che per l'articolo 33 ha risposto, ma per il 581/2010 ha restituito una pagina troncata), una riproduzione di lawplayer.com e le fonti italiane. Il comma 3 dell'articolo 1 del regolamento 581/2010 è stato letto su lawplayer.com, non sulla Gazzetta ufficiale.
4. **Se il decreto del Ministero del Lavoro del 31 marzo 2006** (tre mesi e tre settimane) sia ancora in vigore: la fonte più chiara è del 2010.
5. **Conto proprio e furgoni 2,5-3,5 t**: le fonti si contraddicono. Non ho letto la circolare MIT n. 9674 (è un PDF collegato in un articolo).
6. **Il termine di 56 giorni per scaricare la carta dei tachigrafi G2V2** (blog spagnolo di Geotab): non confermato da nessun testo.
7. **Tempi di installazione** per relè, iButton, CAN, tachigrafo e telecamere, e **tutta la manodopera**: nessuna fonte italiana. Le cifre del capitolo 5 marcate M sono stime mie.
8. **Prezzi di LV-CAN200, ALL-CAN300, ECAN02, relè, sensori EYE, Technoton e Escort in euro** per l'Italia: non trovati (DUT-E 139 senza valuta; TD-BLE 82 dollari da un rivenditore americano).
9. **Cinture e porte via CAN**: le schede dell'LV-CAN200 e dell'ALL-CAN300 elencano le porte (ALL-CAN300), non le cinture.
10. **DSM**: il wiki non conferma il rilevamento di telefono, fumo e cintura (Webfleet dichiara questi rilevamenti per le sue dashcam). **DualCam**: risoluzione e ADAS non verificati.
11. **Documenti PDF illeggibili dallo strumento**: il volantino FMx650 e il rapporto Geotab «Flotte connesse in Italia 2026». Dal rapporto ho solo il 66% di uso della posizione in tempo reale (dalla pagina HTML). Le percentuali per stile di guida, tachigrafo e dashcam non le ho.
12. **Cartrack Italia, Vodafone Automotive, Texa, Telepass Fleet**: Cartrack e Vodafone non trovati; Telepass Fleet riguarda i pedaggi e non il GPS; Texa non cercato.
13. **Scadenza della rete 2G in Italia** (che decide la vita degli FMB640 e dei dispositivi «solo 2G»): non cercata.
14. **Certificazione EN 12830 dei sensori EYE** per la catena del freddo: compare solo come titolo di un rivenditore.
15. **Sanzioni**: 3.464 euro (trans.info, PMI.it) contro 7.000 euro (autoblog.it, titolo): non risolta.

---

## 7. Fonti

Data di lettura per tutte: **2026-10-29**. Tra parentesi, dove la conosco, la data di pubblicazione.

### Operatori
| Sigla | URL | Codice |
|---|---|---|
| A1 | https://targatelematics.com/it-it/ | L |
| A2 | https://targatelematics.com/it-it/soluzioni/fleet-management/ | L |
| A3 | https://targatelematics.com/it-it/fleet-light-e-light-and-security/ | L |
| A4 | https://targatelematics.com/it-it/fleet-start-e-advanced/ | L |
| A5 | https://targatelematics.com/it-it/soluzioni/flotte-di-mezzi-pesanti/ | L |
| A6 | https://targatelematics.com/it-it/soluzioni/targa-tacho/ | L |
| A7 | https://targatelematics.com/uk-en/solutions/heavy-fleets/ | L |
| A8 | https://www.missionline.it/mission-fleet-post/targa-telematics-acquisisce-viasat/ (27/02/2023) | L |
| A9 | https://targatelematics.com/it-it/wp-content/uploads/sites/4/2025/07/Brochure_Targa-Ghost_GL51_A4.pdf (nei risultati di ricerca, non letto) | R |
| A10 | https://www.missionline.it/?p=112102 (Viasat Fleet, 26/03/2024) | L |
| A11 | https://www.missionline.it/mission-fleet-post/viasat-per-la-green-mobility-di-flotte-e-noleggi/ (26/11/2022) | L |
| A12 | https://www.trasporti-italia.com/?p=31277 (Viasat-Nexive, Runtracker 5.5); https://areasosta.com/faq/quanto-costa-installare-un-antifurto-per-auto (agg. 03/08/2022) | R / L |
| B1 | https://trackyup.com/ | L |
| B2 | https://trackyup.com/prezzi/ (pagina aggiornata a ottobre 2026) | L |
| B3 | https://trackyup.com/localizzatori-gps/ | L |
| B4 | https://trackyup.com/installazione-assistenza/ | L |
| B5 | https://trackyup.com/gps-camion-mezzi-pesanti/ | L |
| B6 | https://trackyup.com/obd2-vs-gps-cablato-flotte/ | L |
| B7 | https://trackyup.com/gps-catena-del-freddo/ | L |
| B8 | https://trackyup.com/gps-furgoni/ | L |
| B9 | https://trackyup.com/antifurto-gps/ ; https://trackyup.com/chi-siamo/ | L |
| C1 | https://macnil.it/brand/gt-fleet-365/ | L |
| C2 | https://www.macnil.it | L |
| C3 | https://www.missionline.it/mission-fleet-post/macnil-gt-fleet-365-gestione-e-sicurezza-dei-veicoli-aziendali/ (24/04/2024); https://www.missionline.it/mission-fleet-post/macnil-gtalarm-lancia-pm-connette-flotta-con-postemobile/ (19/05/2017, agg. 30/03/2022) | L |
| D1 | https://www.missionline.it/mission-fleet-post/octo-fleet-essentials-una-flotta-piu-connessa-e-sostenibile-con-meno-costi/ (23/06/2022) | L |
| D2 | https://www.fintechfutures.com/press-releases/octo-telematics-announces-octo-smart-keyless | R |
| D3 | https://www.startmag.it/?p=187354 ; https://techprincess.it/?p=148682 | R |
| D4 | https://www.01net.it/octo-rivoluziona-la-sicurezza-dei-veicoli-con-lai-nasce-il-sistema-antifurto-proattivo-e-predittivo/ | R |
| E1 | https://www.missionline.it/mission-fleet-post/novita-lojack-2026-piu-intelligenza-artificiale-e-sicurezza-connessa/ (22/05/2026) | L |
| E2 | https://www.smartworld.it/mobilita/lojack-connect-telematica-ai-proteggere-flotte-aziendali.html (23/09/2026) | L |
| E3 | https://www.calamp.com/press-releases/cgte-selects-calamps-telematics-technology-for-equipment-fleet-management-in-italy/ | R |
| F1 | https://www.webfleet.com/it_it/webfleet/ | L |
| F2 | https://www.webfleet.com/it_it/webfleet/products/link/ | L |
| F3 | https://www.webfleet.com/it_it/webfleet/products/fleet-dash-cams/ | L |
| F4 | https://www.webfleet.com/it_it/webfleet/lp/digital-tachograph/ | L |
| F5 | https://aio.lv/en/product--tomtom-1kgv00103--12078896 ; https://webfleet.com/en_us/webfleet/products/link/340 | R |
| G1 | https://www.geotab.com/it/ | L |
| G2 | https://iot.telefonica.de/wp-content/uploads/2023/09/Telefonica_IoT-Smart_Mobility-Geotab-Preisliste-Oktober_2023.pdf | R |
| G3 | https://ratings.freightwaves.com/?p=379083 ; https://www.capterra.it/software/124641/fleetmatics-work | R |
| G4 | https://www.geotab.com/it/risorse/ebook/flotte-connesse-in-italia-2026/ | L |
| H1 | https://www.quartix.com/it-it/offerte/ | L |
| H2 | https://www.quartix.com/it-it/ | L |
| I1 | https://www.movolytics.com (rimanda ad Abax, risposta 308) | L |
| I2 | https://www.abax.com/en-gb/newsroom/telematics-brand-abax-strengthens-uk-market-position-through-movolytics-acquisition-c3888524 | R |

### Tachigrafo
| Sigla | URL | Codice |
|---|---|---|
| T1 | https://lawplayer.com/eu/act/32010R0581 (regolamento 581/2010, art. 1 c. 3) | L |
| T2 | https://www.fai.it/eur10123-tachigrafo-digitale-trasferimento-dei-dati-dalla-carta-del-conducente-e-dallapparecchio-di-controllo-regolamento-u-e-n-581-2010/ (05/07/2010) | L |
| T3 | https://www.leggioggi.it/responsabilita-imprese-di-trasporto-come-funzionano-le-conservazioni-fogli-e-dati-tachigrafici/ (05/06/2016) | L |
| T4 | https://www.tachconsulting.it/ogni-quanto-e-come-vanno-scaricati-i-dati-della-carta-del-conducente-e-del-tachigrafo-lazienda-per-quanto-tempo-deve-conservare-tali-dati/ (02/05/2017) | L |
| T5 | https://www.gruppovaliani.it/obbligo-scarico-dati-tachigrafo-digitale.htm | L |
| T6 | https://legislation.gov.uk/eur/2014/165/article/33/adopted (regolamento 165/2014, art. 33) | L |
| T7 | https://enna.ance.it/2025/01/15/autotrasporto-obblighi-del-conducente-sulle-registrazioni-dei-tachigrafi-novita-in-vigore-dal-31-dicembre-2024/ (15/01/2025) | L |
| T8 | https://www.patente.it/attualita/obbligo-tachigrafo-intelligente-1-luglio-2026-veicoli-sopra-2-5-tonnellate?idc=5076 (18/03/2026) | L |
| T9 | https://www.dottrinalavoro.it/notizie-c/mit-obbligo-del-tachigrafo-su-veicoli-leggeri-dal-1-luglio-2026 (circolare MIT 9674 del 16/04/2026) | L |
| T10 | https://www.ecnews.it/lavoro/rapporto-di-lavoro/gestione-del-rapporto/autotrasporto-chiarimenti-mit-obbligo-tachigrafo-g2v2-veicoli-leggeri-1-luglio-2026/ (29/04/2026) | L |
| T11 | https://trans.info/it/tachigrafo-sui-furgoni-dal-1-luglio-2026-obblighi-esenzioni-e-sanzioni-faq-484869 | L |
| T12 | https://www.webfleet.com/it_it/webfleet/lp/digital-tachograph/ | L |
| T13 | https://trans.info/it/dal-2026-tachigrafo-obbligatorio-sui-furgoni-da-2-5-a-3-5-t-456733 (20/02/2026) | L |
| T14 | https://www.pmi.it/impresa/contabilita-e-fisco/496960/tachigrafo-obbligatorio-furgoni-trasporto-internazionale.html (risposta 403, dato da riassunto di ricerca) | R |
| T15 | https://www.geotab.com/es/blog/gestionar-datos-tacografo-digital/ (affermazione dei 56 giorni non confermata) | L |
| T16 | https://www.geotab.com/it/blog/tachigrafo-intelligente-2-scadenza-pmi-luglio-2026/ (10/04/2026) | L |
| T17 | https://www.teltonika-gps.com/fr/blog/how-cross-border-van-fleets-can-manage-tachograph-compliance-remotely (agg. 17/09/2026) | L |

### Teltonika e accessori
| Sigla | URL | Codice |
|---|---|---|
| W1 | https://wiki.teltonika-gps.com/view/FMC650_General_description | L |
| W2 | https://wiki.teltonika-gps.com/view/FMM650_and_Tachograph_Solution | L |
| W3 | https://wiki.teltonika-gps.com/view/FMC640_General_description | L |
| W4 | https://wiki.teltonika-gps.com/view/FMB640_General_description | L |
| W5 | https://wiki.teltonika-gps.com/view/FMC130_General_description | L |
| W6 | https://wiki.teltonika-gps.com/view/FMC130_1-Wire | L |
| W7 | https://wiki.teltonika-gps.com/view/FMC130_Features_settings | L |
| W8 | https://wiki.teltonika-gps.com/view/CAN_Adapters | L |
| W9 | https://wiki.teltonika-gps.com/view/Teltonika_DualCam | L |
| W10 | https://wiki.teltonika-gps.com/view/DSM | L |
| W11 | https://wiki.teltonika-gps.com/view/How_to_install_FMC650_to_MB_Actros | L |
| W12 | https://wiki.teltonika-gps.com/view/FMx150_Tachograph_solution | L |
| W13 | https://community.teltonika.lt/t/keypad-fmc130-immobiliser-wiring-and-configuration-guide-from-the-manufacturer/20492 | L |
| W14 | https://wiki.teltonika-gps.com/view/TEMPERATURE_TRACKING_WITH_BLE_SENSORS | L |
| J1 | https://shop.ascend.de/it/products/teltonika-telematics-ibutton-key-ppex00000700 | L |
| J2 | https://www.skroutz.mt/s/55023041/Ibutton-Tag.html | R |
| J3 | https://wiki.teltonika-gps.com/view/FMB130_Firmware_Changelog (e ricerca «secure engine cut-off», firmware 03.28.02) | R |
| J4 | https://wiki.teltonika-gps.com/view/CAN_adapter_supported_vehicles | R |
| J5 | https://galaxus.fr/en/s1/product/teltonika-fmc150-4g-cat-1-gnssgsmbluetooth-tracker-with-integrated-can-adapter-trackers-24462569 | R |
| J6 | https://wiki.teltonika-gps.com/images/b/b8/Datasheet-BTSMP1_EYE_SENSOR_4.3.pdf | R |
| J7 | https://m.alza.cz/teltonika-eye-sensor-en12830-btsmp183cb02-d13094625.htm | R |
| J8 | https://industry-electronics.com/teltonika-telematics/dsmcam3ut801-driver-safety-monitoring-dsm-fmc650-camera-visual-lieske_1611855.htm | L |
| J9 | https://industry-electronics.com/teltonika-telematics/dualcadgy501-dualcam-cabin-road-video-monitoring-solution-lieske_1611877.htm | L |
| K1 | https://e-shop.jv-technoton.com/product/dut-e-485/ | R |
| K2 | https://wikien.escortsensors.com/index.php/Teltonika-BLE | R |
| K3 | https://reach.dog/shop/thegpscompany/products/escort-td-ble-explosion-proof-fuel-level-sensor | R |
| K4 | https://download.axilogi.com/Teltonika/Datasheet/FMC650.pdf (datasheet FMC650 v2.2, 10/11/2025) | R |

### Costi di installazione
| Sigla | URL | Codice |
|---|---|---|
| L1 | https://it.motor1.com/news/307126/tbs-italia/ (28/02/2019) | L |
| L2 | https://logistimatics.com/blogs/guides/gps-tracker-installation-cost (27/04/2026, dollari USA) | L |
| L3 | https://www.expertmarket.com/uk/vehicle-tracking/vehicle-tracking-systems-cost (sterline, riassunto di ricerca) | R |
| L4 | https://lg.camcom.gov.it/sites/default/files/contenuto_redazione/REGOLAZIONE%20DEL%20MERCATO%20E%20TUTELA%20CONSUMATORE/MARCHIO%20DI%20GARANZIA%20DEL%20CONSUMATORE/TABELLA%20TARIFFE%202026%20rev.08.07.26.pdf (tariffe orarie 2026 delle carrozzerie di Livorno e Piombino) | R |
