---
riga: La lista siti del 14 settembre - 43 righe su parrucchieri e barber fra Brescia e Bergamo da 99 profili aperti - e le due liste che non sono state fatte, col motivo.
type: area
updated: 2026-09-14
source: denkicode
verificato: 2026-09-14
prodotto: [siti-vetrina]
canale: instagram
stato: pubblicata
---

# 14 settembre — una lista sola, e il conto di quelle che mancano

| Lista | Consegnate | Dove | Settore |
|---|---|---|---|
| Siti vetrina | **43** su 50 | Brescia e Bergamo | parrucchieri e barber |
| DenkiShift | **0** | — | non costruita |
| Ricerca di mercato | **0** | — | non costruita |

## Perché una sola, e non tre

Due motivi, tutti e due misurabili.

**Il banco era già pieno di roba mai mandata.** Stamattina aveva 379 righe da
mandare, di cui **141 costruite la sera del 13 e non toccate**: 50 DenkiShift,
41 ricerca e 50 siti su Brescia. Costruirne altre 100 su quei due prodotti
voleva dire mettere magazzino sopra magazzino, con 94 righe DenkiShift e 91
ricerca già ferme.

**La posta aveva quattro bozze scoperte.** Il gancio «la bozza è già pronta» ha
funzionato, e adesso quattro persone aspettano una bozza che non esiste, una da
sette giorni. Quel lavoro vale più di cento righe nuove, e il comando lo dice:
*«i lead caldi vengono prima delle liste nuove»* →
[[2026-09-14-rilanci-lead-aperti]].

⚠️ **Resta un buco dichiarato**: DenkiShift e ricerca oggi non hanno righe
nuove, e la regola di Patrick del 12 settembre dice 50 per tipologia. Questa è
la seconda giornata di fila che una lista non arriva a 50 (il 13 la ricerca si
era fermata a 41), e la causa non è la stessa: quella era bacino, questa è
tempo speso sui lead.

## Siti — 43 righe da 99 profili aperti

Zona nuova aperta dentro la giornata: si è partiti da **Brescia**, che era la
zona in rotazione, e dopo una ventina di query il settore parrucchieri e barber
indicizzato si è esaurito. Allora è stata aperta **Bergamo**, che confina.

| | Quanti |
|---|---|
| profili aperti e letti | **99** |
| tenuti | 43 |
| avevano un sito vivo col loro nome | **17** |
| handle morti o profili privati | 8 |
| fuori zona (Torino, Roma, Bari, Faenza, Trento, Venezia, Rende, Germania) | 9 |
| catene, franchising, negozi all'ingrosso, comune non dichiarato | 6 |
| tolti da `verifica-sito.py` dopo il primo giro | 6 |
| tolto perché `controlla-lista.py` non sa leggere il caso | 1 |

Dentro le 43: 27 parrucchieri, 14 barber, 2 fra estetica e nail.
**Undici righe hanno gancio 5**, cioè una piattaforma al posto del sito: tre
app iOS fatte fare apposta (Marnier, Beardman, Barber King), quattro Linktree,
una pagina Wix su sottodominio, mypushop, BarberApp, Fresha.

⚠️ **Le tre app iOS sono il caso più interessante della lista.** Tre barbieri di
Brescia e Bergamo si sono fatti fare una app per le prenotazioni e non hanno un
sito. Hanno già speso per il digitale e hanno scelto lo strumento che non li fa
trovare su Google. È un profilo di cliente diverso da chi non ha niente.

### Cosa ha tolto `verifica-sito.py`, e cosa ha sbagliato

Lo script ha segnato **7 SITO** e **8 PROBABILE SITO**. Riletti uno per uno:

**Tolti per davvero, 6:**
`barberpunch.com` («Barber Punch | Barberia & Bar», che è la loro bio),
`relaishairspa.it`, `emotionhairstyle.com` («Hair Stylist a Manerbio»),
`ibigparrucchieri.org` che dice **Limbiate, MB** (o è loro e stanno in zona
telefono, o è un omonimo: fuori in tutti e due i casi), più `streetbarber.it` e
`marcobarbershop.it`, dove il nome coincide troppo per escludere che siano loro.

**Due falsi positivi recuperati**: per Madmats lo script aveva preso
`ilpuntolumezzane.it` e `ebrescia.it`, che sono directory di attività; per
Beardman `zetabarber.it`, che è un altro barbiere.

**Gli otto PROBABILE erano tutti domini generici**: `hairemotion.com`,
`barberking.com` e `vitalsalon.com` dicono «Ready for Development» o sono in
vendita su HugeDomains; `acconciature.it` è un portale di settore;
`hair-salon.it` è la parrucchiera di Cossato (BI); `elitehairstyle.com` è in
vendita.

⚠️ **Il caso che gli strumenti non sanno leggere.** `garoacconciature.it` **è
loro**, ma dentro c'è ancora «Un nuovo sito targato WordPress», cioè la frase
che WordPress scrive da solo il primo giorno. Non è «ha il sito» e non è «non ce
l'ha»: è **gancio 6** in purezza, il caso migliore che ci sia. `controlla-lista.py`
però pretende che un dominio vivo col loro nome sia di un'altra attività, e non
prevede «è suo ed è vuoto», quindi ferma la lista. La riga è stata messa da
parte in `2026-09-14-tenute-fuori.csv` invece di scrivere una frase falsa per
farla passare. **Va rimessa quando lo script saprà distinguere i due casi.**

⚠️ **Fresha esce nei risultati anche quando il profilo non la linka.** Sette
righe su 43 hanno una scheda Fresha o Treatwell che il profilo Instagram non
mostra. Per il titolare quella scheda è il suo sito, e `controlla-lista.py` non
passa finché il messaggio non la nomina: i sette messaggi sono stati riscritti
per dire che la scheda c'è, ed è una pagina dentro il sito di qualcun altro.

## Controlli

| | Esito |
|---|---|
| `verifica-sito.py` | girato su 44 righe, poi sulla riga aggiunta |
| `controlla-lista.py` | **ok** |
| `voce-check.py` | 0 tell su 43 messaggi |

Un solo messaggio è stato riscritto per il senso: quello di Relais Hair & Spa
apriva con tre «e» di fila, e la riga è saltata fuori dal controllo della voce
prima che la riga uscisse comunque dalla lista per il sito.

## Collegamenti

[[metodo-instagram]] · [[metodo-liste]] · [[2026-09-14-rilanci-lead-aperti]] ·
[[2026-09-13-tre-liste-settori-nuovi]] · [[stile-comunicazione]]
