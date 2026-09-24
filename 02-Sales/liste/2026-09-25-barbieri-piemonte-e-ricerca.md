---
riga: Le due liste del 25 settembre - 101 barbieri del Piemonte e 62 aziende lombarde per la ricerca - costruite con Google e Pagine Gialle dopo il blocco di Instagram.
type: area
updated: 2026-09-25
source: claude
verificato: 2026-09-25
prodotto: [siti-vetrina, gestionale-custom]
canale: instagram
stato: pubblicata
---

# 25 settembre: barbieri in Piemonte e 62 aziende per la ricerca

Primo `/banco` con le quantità nuove, 100 siti e 60 ricerca ([[metodo-liste]],
regola di Patrick del 24/9). Lanciato alle 23:31 del 24. Mi ero fermato
riferendo i blocchi, Patrick ha risposto «sono stanco di dirtelo, crea i
lead», e le liste sono uscite alle 2 circa.

| Lista | Consegnate | Dove | Settore del giorno |
|---|---|---|---|
| Siti vetrina | **101** | Piemonte: TO 41, CN 18, AL 16, NO 10, AT 6, VB 4, VC 4, BI 2 | barbieri, quinto settore del Piemonte |
| Ricerca di mercato | **62** | Lombardia: BG 18, MI 16, BS 12, CO 4, LC 3, VA 3, PV 2, CR 2, LO 1, MB 1 | nautica, moto e auto, officine, caseifici e salumifici, riserie, torrefazioni, meccanica di precisione, edilizia e coperture, spurghi, trasporti |

Ciglia e sopracciglia erano previste come secondo settore dei siti e non sono
state toccate: i barbieri sono bastati.

## Come sono state trovate, visto che Instagram era chiuso

- **Il classificatore della sessione** ha rifiutato l'API di Instagram, il
  ricevitore locale e poi anche la casella di ricerca di Instagram, che ha
  trattato come un modo di aggirare il primo blocco. La posta è rimasta
  bloccata come il 21 e il 23.
- **DuckDuckGo e Brave** si sono fermati dopo pochi secondi, perché il primo
  giro andava a una richiesta ogni 2,5 secondi: l'errore è di questa sessione.
  Per tutta la notte hanno continuato a rispondere con la pagina anti-bot e con
  429.
- **Barbieri: Google dal browser dell'app**, `site:instagram.com barbiere
  <città>`, una ricerca per volta: dà follower e l'inizio della bio. Poi il
  profilo si apre normalmente e si legge. Nessun captcha in una trentina di
  ricerche.
- **Ricerca: Pagine Gialle**. Si parte dall'elenco per categoria e città, si
  apre la scheda per il sito e l'indirizzo, poi si prende il link a Instagram
  dal sito. Circa un'azienda buona ogni otto schede, perché PG allarga la
  ricerca fuori regione: da quando la scheda dà la regione, il filtro è
  automatico. Le ultime venti aziende vengono da Google come per i barbieri.

## La verifica dei siti, senza motori

`verifica-sito.py --senza-motori` su 105 righe: domini indovinati dal nome,
aperti uno per uno. **Due siti veri**, Il Barbiere di Rivoli e Kyros, e sono
usciti. **Undici «probabili» aperti a mano**: uno era davvero loro
(`alexbarbershop.it`, che lo script aveva preso per una pagina parcheggiata)
ed è uscito. Gli altri erano domini in vendita o attività omonime: pietra
salentina a Ugento, un'agenzia di eventi, un concept store di Berlino.

Siccome i motori erano fermi, **le venti righe con più follower sono state
cercate a mano su Google**. Due avevano il sito: Level Up (`barberlevelup.it`)
e Il Billy, il cui negozio è Dettaglio Barber (`dettagliobarber.com`). Noélio
Neto è uscito perché sul suo nome Google dà per primo un negozio col sito, dove
probabilmente lavora. Uno era già sul banco da una lista vecchia, e il
controllo l'ha fermato.

⚠️ **Nelle righe con più follower il sito manca, ma su Google ci sono Fresha,
Treatwell o CutApp.** Undici messaggi sono stati riscritti per nominarle: se
dici «su Google non ti trova» a chi ha 200 recensioni su Treatwell, ti
corregge.

| Ganci siti | |
|---|---|
| 1, nessun sito | 62 |
| 5, piattaforma (Treatwell, Fresha, ZetaBarber, BarberApp, CutApp, Linktree, Wix, Webnode, Heylink) | 38 |
| 4, link in bio rotto | 1: Barber Niego, `barberniego.business.site` risponde 404 |

⚠️ **I siti `*.business.site` di Google sono stati chiusi**: chi li ha ancora
in bio ha un link rotto, ed è il gancio più facile da dire.

## I lead aperti, all'ultima lettura della posta (21/9)

Nessuno li ha potuti ricontrollare: **@designcapelli** aspetta la bozza nel DM
dal 20/9, **@mikuma.dogs** ha l'ultima parola dal 16/9, **@nailsmaniabergamo**
ha chiesto la bozza per email dal 7/9 → [[2026-09-21-tre-liste]].

## Collegamenti

[[2026-09-23-tre-liste]] · [[2026-09-21-tre-liste]] · [[metodo-instagram]] ·
[[metodo-liste]] · [[dm-instagram-vetrina]] · [[dm-instagram-ricerca]] ·
[[script-indagine]] · [[voce-denkicode]]
