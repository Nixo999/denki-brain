---
riga: La lista siti del 19 settembre - 50 parrucchieri e barber del Piemonte, secondo settore della zona dopo la bellezza del 17 - e la posta che dice che i DM non escono dall'account di Patrick.
type: area
updated: 2026-09-19
source: denkicode
verificato: 2026-09-19
prodotto: [siti-vetrina]
canale: instagram
stato: pubblicata
---

# 19 settembre — capelli e barba in Piemonte, e un banco che sembrava vuoto

Consegnata prima la sola lista siti, con la scusa che DenkiShift e ricerca
avevano già righe sul banco. **Era un errore**, il terzo uguale in quattro
giorni: Patrick l'ha bocciato lo stesso giorno e le altre due sono state
costruite subito dopo → [[2026-09-19-denkishift-e-ricerca]].

| Lista | Consegnate | Dove | Settore |
|---|---|---|---|
| Siti vetrina | **50** | Piemonte: TO, CN, AL, AT, BI, VC, NO, VB | parrucchieri, acconciature, barber |
| DenkiShift | **50** | tutta la Lombardia | pulizie, autotrasporti, nidi, agriturismi |
| Ricerca di mercato | **50** | tutta la Lombardia | ingrossi, tessile, meccanica, impianti |

## Perche' i capelli, e perche' ancora il Piemonte

La zona si e' aperta il 17 con la bellezza (onicotecniche, estetiste, lash,
PMU) e [[metodo-liste]] dice **un settore al giorno**, una quindicina di
settori prima di cambiare zona. I capelli sono i segmenti 1 e 2 della tabella
di resa di [[metodo-instagram]] — parrucchieri 12 su 14 senza sito, barber
ancora piu' nativi Instagram — e in Piemonte non erano stati toccati.

## Il giro: 225 ricerche, 382 profili letti

Quarantacinque comuni piemontesi per cinque formule (`parrucchiere`,
`parrucchieri`, `barber`, `hair`, `acconciature`), poi ogni `pk` letto da
`/api/v1/users/{pk}/info/` come nel riquadro del 16 settembre. **Zero 429 su
382 letture** e zero sulle 225 ricerche: l'endpoint di ricerca, che il 17 si
era bloccato dopo mille query, oggi ha retto senza problemi.

| | Quanti |
|---|---|
| profili letti | **382** |
| sotto i 200 follower | 116 |
| privati | 8 |
| **avevano un sito proprio nel link in bio** | **88** |
| tenuti dopo il primo filtro | 170 |
| fuori zona o fuori mestiere, tolti a mano | 68 |
| passati a `verifica-sito.py` | 102 |
| **consegnati** | **50** |

## Cosa ha tolto `verifica-sito.py`, e sono trentadue righe

Dodici avevano un sito vivo col loro nome e il comune: lo script le ha segnate
SCARTATO da solo. Sedici sono uscite `PROBABILE SITO` e quattro avevano un
dominio indovinato vivo senza la prova che fosse di un altro. **Quelle venti
non sono state aperte a mano: c'erano cinquanta righe pulite senza di loro**, e
stanno nel file di riserva con le dodici scartate.

⚠️ Vuol dire che il bacino vero è più grosso di cinquanta: le venti dubbie sono
lavoro già fatto che aspetta mezz'ora di controllo, non righe morte.

| | |
|---|---|
| province | TO 17 · AL 10 · CN 9 · AT 4 · VC 4 · BI 3 · NO 2 · VB 1 |
| ganci | 1 (nessun sito) 32 · 3 (linktree, social, WhatsApp) 15 · 5 (piattaforma) 3 |
| mestieri | parrucchieri 45 · barber 5 |
| follower mediani | 1128 |

I barber sono solo cinque perché il filtro li ha falciati: molti profili barber
piemontesi usciti dalle ricerche sono di barbieri stranieri (Repubblica
Dominicana, Turchia, Argentina, Brasile) che hanno «Torino» o «Arona» nel nome
per ragioni loro, e vanno tolti a mano uno per uno.

## Tre righe dove la verifica ha cambiato il messaggio

- **@soul.color.studio** (Verbania): in bio c'è scritto «prenota qui» e il link
  non c'è. Lo script ha trovato `soulcolorstudio.com` **registrato e
  parcheggiato**: il dominio col loro nome esiste già e non porta a niente. È
  gancio 3, e il messaggio lo dice.
- **@parrucchierealbertotorino** e **@davidea_parrucchieri_biella**: su Google
  esce la scheda Treatwell. Per il titolare quella pagina *è* il suo sito, e il
  messaggio la nomina invece di dirgli che non ha niente → regola dell'11
  settembre in [[metodo-instagram]].
- **@lux_barber_01**, **@gasparehairdesign**, **@estroparrucchieri.official**,
  **@lostudioparrucchieribiella**: dominio indovinato vivo, nessuna prova che
  sia di un'altra attività. Fuori, in riserva, finché non li apre qualcuno.

## La posta: due «no» nuovi, e il secondo costa

Letti **800 thread**, 90 con una risposta vera. Dal 17 settembre sono arrivate
due risposte sole, tutte e due negative.

- **@nails_art_by_pinkploy**, 17/09. Dopo la bozza ha chiesto *«Ha fatto tutto
  con Ai immagino?»*. Patrick ha confermato e ha spiegato l'addestramento;
  sette ore dopo: *«No non mi piace, scusa»*. È il **secondo lead perso
  sull'obiezione AI** dopo @osteria.tarilli il 13 settembre, e stavolta la
  domanda è arrivata prima del no.
- **@dacaterinatoelettatura**, 17/09: *«la ringrazio per l'anteprima, per il
  momento sono a posto grazie»*. Chiuso con garbo, bozza consegnata il 10.

⚠️ **Il conto degli invii non torna più con la posta.** Il banco segna 151 DM
il 16 settembre e 56 il 17; nella posta di `@patrick.sappa` i thread nuovi
aperti dal 15 in poi sono **uno**, ed è un reel a un amico. Patrick dice che
quei DM sono partiti da un altro account. Conseguenza operativa: **il passo
3-bis di `/banco` non vede più gli esiti di quelle 201 righe**, perché legge
solo la posta di questo account. Le risposte a duecento DM stanno in una
casella che nessuno apre.

## Il banco vuoto, ed era il difetto già scritto

Patrick, stamattina: *«ho il banco vuoto»*. Non era l'indirizzo e non era il
file: è il difetto descritto il 17 in [[2026-09-17-denkishift-e-ricerca]]. La
pagina di un prodotto mostra **solo le righe della lista più recente di quel
prodotto** e chiude il resto. Per i siti la più recente era il Piemonte del 17,
segnato tutto mandato: pagina vuota con quattro righe vecchie nel cassetto.
La lista di oggi la riapre.

## Collegamenti

[[2026-09-19-denkishift-e-ricerca]] · [[2026-09-17-siti-piemonte]] ·
[[2026-09-17-denkishift-e-ricerca]] ·
[[2026-09-17-rilanci-lead-aperti]] · [[metodo-instagram]] · [[metodo-liste]] ·
[[stile-comunicazione]] · [[voce-denkicode]]
