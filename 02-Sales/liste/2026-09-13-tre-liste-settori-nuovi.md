---
riga: Le tre liste del 13 settembre - 50 DenkiShift su RSA e poliambulatori, 50 siti su Brescia, 41 ricerca. Due settori nuovi che rendono, uno abbandonato.
type: area
updated: 2026-09-13
source: denkicode
verificato: 2026-09-13
prodotto: [siti-vetrina, denkishift, gestionale-custom]
canale: instagram
stato: pubblicata
---

# 13 settembre 2026 — tre liste, e due settori nuovi che funzionano

Costruite la sera del 12 su richiesta di Patrick, *«fai la lista ora così
domani la ho pronta»*, dopo che aveva sbattuto contro il limite di invii di
Instagram a metà pomeriggio.

| Lista | Consegnate | Dove | Settore, nuovo per noi |
|---|---|---|---|
| DenkiShift | **50** | tutta la Lombardia | RSA, cooperative sociali, poliambulatori, panifici |
| Siti vetrina | **50** | Brescia e provincia | nail, estetica, ciglia, trucco permanente |
| Ricerca di mercato | **41** | tutta la Lombardia | edilizia, fabbri, tipografie, traslochi, resine |

Sul banco di Patrick adesso: **102 siti, 94 DenkiShift, 91 ricerca** da mandare,
più 92 righe vecchie senza colonna prodotto che il banco mette sotto Siti.

## DenkiShift — il settore migliore che non avevamo ancora toccato

I ristoranti e gli alberghi erano già bruciati. Aperti quattro segmenti nuovi,
tutti scelti perché il turno **è** il loro problema e non un accessorio:

- **5 RSA e case di riposo** più 4 fra comunità educative e soccorso: assistenza
  sulle 24 ore, il caso da manuale.
- **7 cooperative sociali**: educatori distribuiti su più servizi e più orari.
- **17 poliambulatori e centri medici**: specialisti che ruotano sulle stesse
  stanze, con la segreteria che li incastra a mano.
- **13 panifici con laboratorio**: chi impasta di notte e chi vende di giorno
  non sono la stessa persona. Il Panificio Testa di Treviglio scrive in bio
  «ogni notte dal 1954», i Fratelli Longoni «non spegniamo mai il forno,
  aperti 7 su 7». Sono le due prove migliori di tutta la lista.

⚠️ **Tre righe sono state buttate leggendo i dati, non a occhio**: un panificio
«S. Giacomo» di Riva del Garda (TN), una panetteria di Preonzo (Ticino), e un
«Panificio Milano» che sta a Sant'Andrea Apostolo dello Ionio, in Calabria. Il
nome del profilo non dice dove sei.

## Siti — i fotografi rendono 14 su 88, abbandonati lo stesso giorno

Il settore del giorno doveva essere **fotografi e wedding a Milano**, che il
metodo dà come alto potenziale e che non avevamo mai fatto. Letti 88 profili:
**solo 14 senza un sito proprio**, il 16%. I fotografi vivono di portfolio, e
il portfolio è un sito.

Abbandonato subito, come i tatuatori della Brianza il 12. Al suo posto
**Brescia**, provincia con appena 9 righe sul banco, sul settore che converte
meglio di tutti: **46 profili su 57 senza sito, l'81%**.

Dentro: 22 onicotecniche, 8 fra estetica e estetica avanzata, 7 di trucco
permanente, 5 lash maker, 3 parrucchieri, 1 barber.
**12 righe hanno gancio 5**, cioè una piattaforma al posto del sito: Taplink,
Linktree, WhatsApp, Setmore, Google Maps, la scheda di un centro commerciale.
Il messaggio la nomina.

⚠️ **`verifica-sito.py` ha scartato 6 righe** che avevano un sito vivo col loro
nome, fra cui Barber Pro 2, che ha `barberpro2.it` per le prenotazioni. Sono
state sostituite e archiviate in `gia-col-sito.csv`, non buttate.
Altri 4 domini indovinati erano vivi ma **non erano loro**, e la colonna adesso
scrive perché: `dacciuntaglio.store` è un salone omonimo di Bareggio (MI),
`valenails.com` è in California, `flowernails.com` e `beautywax.net` sono in
vendita.

## Ricerca di mercato — 41, e il motivo è il bacino

**Consegnate 41 su 50.** Non è una scusa: è il bacino misurato due giorni di
fila. Il 12 settembre erano servite 80 query su dieci città per tenere 41 righe
su 154 profili; il 13 sono state fatte **circa 170 query e letti 271 profili**,
e ogni giro nuovo ripescava gli stessi handle già sul banco.

Le PMI industriali su Instagram ci stanno poco, e quelle che ci stanno le
abbiamo già. I settori aperti oggi sono quelli che una foto ce l'hanno:
edilizia e ristrutturazioni (12 righe), parquet e resine (5), fabbri (3),
tipografie (3), traslochi (2), vetrerie (2), autolavaggi (3), più carpenterie,
studi tecnici, aziende agricole, gommisti, ricambi, disinfestazioni.

⚠️ **Due righe dichiarano il proprio limite in colonna**: `azienda_agricola_bergamo`
e `traslochi_milano_l.b` hanno la bio vuota, e la zona la dichiara solo il nome
del profilo. Sta scritto nella prova, e va confermato aprendo i post prima di
scrivergli.

⚠️ **Due scartate leggendo i dati**: «Autotrasporti Bresciani» ha la sede a
Settimo Torinese, e «Carrozzeria Monza» sta a Trento. In tutti e due i casi il
nome è un cognome o un marchio, non il comune.

## Controlli

| | DenkiShift | Siti | Ricerca |
|---|---|---|---|
| `controlla-lista.py` | ok | ok | ok |
| `voce-check.py` | 0 tell su 50 | 0 tell su 50 | solo il link del modulo, che è voluto |
| `verifica-sito.py` | — | girato due volte, 0 siti vivi rimasti | — |

I messaggi sono stati riscritti più volte per il senso, non solo per i tell:
il controllo della voce toglie le tracce da macchina ma non si accorge se una
frase non dice niente. Regola di Patrick del 12 settembre, in
[[stile-comunicazione]].

## Collegamenti

[[metodo-liste]] · [[metodo-instagram]] · [[2026-09-12-cinquanta-per-tipologia]] ·
[[2026-09-12-rilanci-lead-aperti]] · [[dm-instagram-denkishift]] · [[script-indagine]]
