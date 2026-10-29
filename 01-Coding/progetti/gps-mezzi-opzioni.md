---
type: risorsa
riga: Cinque kit GPS Teltonika da comprare oggi, dalla spina OBD al camion con tacografo - prezzi letti il 29/10/2026 su Getic.it e gpstelematics.eu, manodopera, cosa si ottiene.
updated: 2026-10-29
source: claude
tags: [gps, flotta, teltonika, prezzi, ricerca]
---

# GPS sui mezzi: le cinque opzioni, dalla più semplice alla più completa

Chiesta da Nicola il 29/10/2026 per [[gps-mezzi]]. Prezzi **con IVA**, letti
il 29/10/2026 da due operatori e ricontrollati a campione da Trevis (FMC003,
FMC920, FMC150, FMC650 e LV-CAN200 su Getic.it; FMC130 e lettore iButton su
gpstelematics.eu; listino Trackyup). Spedizione e SIM a parte. I rapporti
integrali: [[gps-mezzi-ricerca-kit]] e [[gps-mezzi-ricerca-professionisti]].

Due cose valgono per tutti i kit. **I negozi**: Getic.it (Lettonia, sito in
italiano, IVA 22 % italiana, si dichiara distributore ufficiale Teltonika) e
gpstelematics.eu (Lituania, IVA 21 %, un po' più economico; al carrello per un
cliente italiano l'aliquota potrebbe salire al 22 %). DenkiCode non ha
partita IVA, quindi i listini «senza IVA» (Getic.com, GoTracker-Store, Lieske,
Ascend) non valgono per noi. **Il riferimento italiano**: Trackyup (Brescia)
vende gli stessi Teltonika in kit con SIM e 12 mesi da 143 a 237 € IVA
inclusa, poi 6 € + IVA al mese a mezzo, manodopera esclusa: è il prezzo di
mercato con cui si confronterà il servizio di Seba.

## La scala

| | Kit | Hardware a mezzo, con IVA | Chi lo monta | Cosa si ottiene in più |
|---|---|---|---|---|
| 1 | FMC003, spina OBD | 103,24 € Getic.it (93 € gpstelematics) | il cliente, meno di 2 minuti | posizione, accensione, chilometri e carburante veri «a seconda del veicolo» |
| 2 | FMC920, cablato tre fili | 66,80 € Getic.it (60 €) | elettrauto, 30-60 minuti | nascosto, batteria di riserva, accensione dal filo sotto chiave |
| 3 | FMC130 + iButton + relè + sonda | 132 € gpstelematics (su Getic manca il lettore iButton) | elettrauto, 1,5-2,5 ore (stima) | chi guida, blocco motore, temperatura del vano, 3 ingressi e 3 uscite |
| 4 | FMC150 + ECAN02, o FMC130 + LV-CAN200 | 143,11 € o 144,16 € Getic.it (122 € o 140 €) | installatore con lo schema del veicolo, 1-2,5 ore (stima) | chilometri veri, livello e consumo carburante, giri, porte, temperatura motore |
| 5 | FMC650 + cavo tacho + sensore carburante + DualCam | 471,19 € gpstelematics | installatore di flotte, mezza giornata o una (stima) | scarico remoto del tacografo, dati FMS dei camion, carburante dal serbatoio, video cabina e strada |

### 1. Spina OBD: Teltonika FMC003

4G con ripiego 2G, si infila nella presa diagnostica e parte. Legge dalla
centralina fino a 32 parametri, tra cui chilometri e carburante veri, ma solo
sui veicoli che li espongono. Limiti: si vede, si stacca con una mano, occupa
la presa che usa l'officina, e sui camion la presa non è quella delle auto.
Non esiste un OBD Teltonika più recente; l'FMB003 a 71,17 € è solo 2G e non
conviene. Trackyup lo vende in kit a 188 €.

### 2. Cablato base: Teltonika FMC920

Tre fili (positivo permanente, positivo sotto chiave, massa), nascosto dietro
il cruscotto, batteria interna da 170 mAh, da 10 a 30 V quindi anche sui
mezzi a 24 V. Dà posizione, accensione, chilometri da GPS e stile di guida
dall'accelerometro. Non ha il bus 1-Wire: niente iButton né sonde. Non è
fuori produzione: la tabella EOL di Teltonika non lo elenca, il wiki non ha
avvisi, tre negozi lo vendono come corrente. Trackyup lo vende a 143 €.

### 3. Cablato avanzato: FMC130 con chi guida, blocco motore e temperatura

Distinta su gpstelematics.eu: FMC130 71 €, lettore iButton PPEX00000060 15 €,
una chiave magnetica 14 € (una per autista), relè Teltonika 12 V 30/40 A
9 €, sonda DS18B20 23 €. Su Getic.it l'FMC130 costa 71,36 €, il lettore
iButton non c'è (c'è un lettore RFID a 33,40 €), chiave e sonda sono
esaurite. Il relè Teltonika è a 12 V: per i camion a 24 V non ne abbiamo
trovato uno. Il blocco motore agisce sul motorino d'avviamento, non sul mezzo
in marcia; Trackyup dichiara di non offrirlo. La sonda serve ai furgoni
frigo; se serve un registro valido per i controlli, va verificata la
certificazione del sensore.

### 4. Lettura del bus CAN

L'ECAN02 (29,87 € Getic.it) è un morsetto che legge i fili CAN senza
tagliarli e **non funziona da solo**: va con l'FMC150 (CAN integrato,
113,24 €) oppure con un adattatore sull'FMC130. L'LV-CAN200 (72,80 €) copre
auto, furgoni, camion e autobus, anche elettrici; l'ALL-CAN300 (139,13 €,
totale 210,49 € con l'FMC130) aggiunge mezzi agricoli, speciali, cinture,
luci e spie. Quale copra un'auto precisa dipende dagli elenchi di Teltonika,
e lo schema di collegamento si chiede al loro commerciale con marca, modello
e anno. Regola pratica: FMC150 + ECAN02 se il veicolo è in elenco,
altrimenti FMC130 + LV-CAN200. È il kit che rende vere le analisi (chilometri
e carburante dal veicolo, non dal GPS).

### 5. Camion e flotte: FMC650

Su gpstelematics.eu: FMC650 141 € (148,83 € su Getic.it), cavo tacho 10 €,
sensore carburante Technoton DUT-E 485 168,19 € (spedizione da 24 €),
DualCam 152 €: 471,19 €. In più TachoSync per i file DDD, 49 € l'anno (da
riassunto di ricerca), e il kit di taratura del sensore, 306 € una tantum
per l'installatore. La telecamera DSM (sonno, distrazione) lavora solo con
l'FMC650 e il prezzo non è affidabile (da 144 € + IVA a 389 €). L'FMC650 ha
due CAN J1939, K-Line, due RS232, una RS485, quattro ingressi e quattro
uscite. Il tacografo va scaricato per legge ogni 90 giorni (unità di bordo)
e 28 giorni (carta del conducente) sui mezzi sopra 3,5 t, e dal 1/7/2026
anche sui furgoni da 2,5 a 3,5 t in trasporto internazionale: il tracker fa
da ponte, servono carta aziendale e un servizio di scarico. Trackyup vende
l'FMC650 a 237 €.

## SIM, manodopera, cosa manca

- **SIM Things Mobile** (IVA esclusa): SIM 2,50 € più 2,50 € di attivazione;
  0,02 €/MB più 2 € al mese per SIM e 3 € al mese di portale per account.
  Su Amazon.it la SIM da 10 € risulta non disponibile.
- **Manodopera**: nessuna fonte italiana pubblica un listino. Trackyup dà
  solo i tempi (OBD meno di 2 minuti, cablato 30-60 minuti). Le ore dei kit
  3, 4 e 5 sono stime; servono due preventivi di elettrauto a Milano e, per
  il kit 5, due centri tacografo.
- **Non verificato**: le spedizioni di Getic e gpstelematics; se la FMC150
  di gpstelematics è la versione europea; la compatibilità FMC650 con il
  DUT-E 485; il contenuto della scatola DualCam; le pagine di Amazon.it.
