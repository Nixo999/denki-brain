---
type: progetto
riga: Localizzazione GPS dei mezzi di lavoro, idea di Seba per più avanti - ricerca del 29/10/2026 su dispositivi, negozi, SIM, piattaforma e legge. Non iniziato.
status: in-pausa
client: sebastian-torres
stack: [teltonika, traccar, supabase, postgis, maplibre]
started: TODO
deadline: TODO
updated: 2026-10-29
source: claude
valore: TODO
incassato: 0
tags: [gps, flotta, opero, ricerca]
---

# GPS sui mezzi di lavoro

Seba vuole, più avanti, mettere un GPS sui furgoni e sui camion delle aziende
che lavorano con l'impresa del padre (consegne, facchinaggio, traslochi) e
offrirlo come servizio: posizione in tempo reale e uno storico per studiare
l'andamento. Se stia dentro [[opero]] o in una piattaforma a parte non è
deciso. Cliente: [[sebastian-torres]]. Nessun repository, nessuna data.

Sintesi di due ricerche fatte da agenti il 29/10/2026. I rapporti integrali,
con le fonti numerate, stanno in [[gps-mezzi-ricerca-hardware]] e
[[gps-mezzi-ricerca-piattaforma]]. Trevis ha ricontrollato tre fonti a
campione (prezzo dell'FMC130 su Getic, prezzo del VPS Hetzner, nomi delle
opzioni di inoltro di Traccar); il resto l'hanno letto gli agenti, non una
persona. Nessun dispositivo è stato comprato né provato.

## La risposta corta

- **Dispositivo**: Teltonika **FMC130** (cablato, 4G, da 10 a 30 V, lettore
  iButton per sapere chi guida), 71,36 € con IVA su Getic.it. Per i furgoni a
  12 V senza elettrauto, l'**FMC003** a spina OBD, 103,24 €.
- **Dove**: **Getic.it**, in italiano, prezzi con IVA, in magazzino, si
  dichiara distributore ufficiale Teltonika. GoTracker-Store (Francia) costa
  meno (FMC130 a 48 € più IVA) ma va chiesto se spedisce in Italia.
- **SIM**: **Things Mobile Business**, 2 € al mese per SIM più 0,02 €/MB in
  Italia. Un tracker consuma 5-30 MB al mese.
- **Dati a noi**: i tracker parlano binario su TCP, non HTTP. Serve
  **Traccar** (open source) su un VPS da 6 € al mese, che inoltra ogni
  posizione in JSON a una Edge Function di **Supabase**; mappa con MapLibre.
- **Legge**: il GPS sul mezzo di un dipendente è controllo a distanza. Prima
  di montarlo il cliente deve avere l'accordo sindacale o l'autorizzazione
  dell'Ispettorato del lavoro, poi informativa, cartello sul mezzo e DPIA.

## I dispositivi

Tutti Teltonika, protocollo Codec 8, server impostabile con un SMS
(`setparam` con APN, dominio, porta) o dal Configurator. Prezzi del 29/10/2026.

| Modello | Tipo | Tensione | Getic.it (con IVA) | GoTracker (senza IVA) | Nota |
|---|---|---|---|---|---|
| FMC130 | cablato 4G, iButton | 10-30 V | 71,36 € | 48 € (10 pezzi: 43,99) | la scelta per furgoni e camion |
| FMC003 | spina OBD 4G | 12 V | 103,24 € | 72 € | autoinstallazione, solo auto e furgoni |
| FMC920 | cablato 4G compatto | 10-30 V | 66,80 € | 41 € | un risultato lo dà «end of life»: chiedere prima |
| FTC134 | batteria, 4G | 8-32 V | 44,33 € + IVA (Getic.com) | — | rimorchi e container |
| FMB920 | cablato 2G | 6-30 V | 36,40 € | 28 € | solo prove: il 2G chiude fra il 2029 e il 2031 secondo le ipotesi |

Il 3G è spento da TIM e Vodafone: i modelli solo 3G si scartano. I cinesi da
16 a 47 € su AliExpress (Sinotrack, Micodus, Coban) servono per un banco di
prova, non per un prodotto da rivendere: il Micodus MV720 ha un avviso CISA
del 2022 con sei vulnerabilità. I camion hanno la presa a 9 poli, non l'OBD:
lì si va di cablato. L'elettrauto chiede 50-150 € a mezzo (comparatori, non
un listino). DenkiCode non ha partita IVA: i negozi solo per aziende (Lieske,
Ascend) li può usare l'impresa del padre di Seba, non noi.

## Come arrivano i dati e quanto costa

Il tracker manda pacchetti Codec 8 su TCP e vuole una risposta all'IMEI e la
conferma dei record. Una Edge Function non ascolta una porta TCP, quindi in
mezzo serve Traccar (Apache 2.0, oltre 200 protocolli, Docker), che inoltra
ogni posizione come POST JSON `{position, device}` con `forward.type=json` e
`forward.url` (i vecchi `forward.enable` e `forward.json` non esistono più).
Scriversi il parser conviene solo con un marchio solo; flespi parte da 130 €
al mese.

```
tracker ──TCP──▶ Traccar + Postgres su VPS Hetzner CX23 (5,49 € + 0,50 € IPv4)
                   │ un POST per posizione
                   ▼
   Edge Function Supabase ──▶ posizioni (PostGIS) ──▶ Realtime ──▶ MapLibre
                              + viaggi, soste, riepilogo giornaliero (pg_cron)
```

Tessere: un file PMTiles (Protomaps) su Supabase Storage, o Stadia Maps a
20 $ al mese; Mapbox chiede una licenza a parte per le app «legate ai
veicoli». Dieci mezzi a una posizione ogni 30 secondi fanno 211.200 righe al
mese, circa 50 MB. **Costo mensile per 10 mezzi**: circa 6 € di VPS, 25 $ di
Supabase Pro se il progetto è nuovo, 20-30 € di SIM, IVA esclusa; una tantum
70-100 € di tracker e 50-150 € di elettrauto a mezzo. Traccar dà già viaggi,
soste e riepilogo via API; il contachilometri vero è l'AVL ID 16 del
dispositivo. Rischio: i reinvii verso Supabase coprono 102 secondi e la coda
tiene 100 posizioni, poi scarta: si tiene lo storico anche in Traccar e si
recuperano i buchi da `/api/positions`. **Fase zero senza hardware**: l'app
Traccar Client sui telefoni, per un pilota di 2-4 settimane con un tracker
vero su un mezzo come controllo; non è un prodotto.

## La legge, che decide il prodotto

- Art. 4 dello Statuto dei lavoratori (D.Lgs. 151/2015): accordo con RSA/RSU
  o autorizzazione dell'Ispettorato. La circolare INL 2/2016 dice che il GPS
  **non** è «strumento di lavoro»; due note INL del 2026 lo ribadiscono. Il
  titolare è l'azienda cliente, noi responsabili del trattamento per contratto.
- Il Garante sanziona il tracciamento continuo: 50.000 € il 16/01/2025
  (posizione anche nelle pause, 180 giorni di conservazione), 6.000 € il
  28/05/2026 (una posizione ogni 60 secondi, tempo reale, DPIA in ritardo).
- Per l'app: frequenza bassa impostabile dal cliente, niente tempo reale
  permanente, spegnimento in pausa e fuori orario, cancellazione automatica,
  registro degli accessi, esportazione dei dati di chi li chiede. Il caso del
  titolare o del collaboratore non dipendente non ha fonti: si tratta ogni
  mezzo come guidato da dipendenti. Prima di vendere, un consulente del lavoro.

## Non verificato

Se l'FMC920 è ancora in produzione; le spedizioni verso l'Italia; un listino
vero di elettrauto; il roaming permanente delle SIM IoT estere; i termini M2M
delle SIM consumer; l'effetto di `forward.enable`; il costo di Storage ed
egress Supabase per i PMTiles; i prezzi di Navixy e Wialon.
