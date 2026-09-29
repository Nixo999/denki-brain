---
riga: Liste del 29/9 - 100 tecniche di ciglia e sopracciglia del Piemonte, 60 aziende lombarde per la ricerca. Google su ogni riga siti.
type: area
updated: 2026-09-29
source: claude
verificato: 2026-09-29
prodotto: [siti-vetrina, gestionale-custom]
canale: instagram
stato: pubblicata
---

# 29 settembre: ciglia e sopracciglia in Piemonte, 60 aziende per la ricerca

`/banco` lanciato da Patrick il 28 sera, liste pubblicate il 29. Patrick ha
chiesto una cosa sola in corsa: «fai bene la ricerca e i messaggi».

| Lista | Consegnate | Dove | Settore |
|---|---|---|---|
| Siti vetrina | **100** | Piemonte: TO 43, AL 13, NO 12, CN 11, BI 7, AT 5, VB 5, VC 4 | ciglia, sopracciglia, PMU: sesto settore del Piemonte dopo bellezza, capelli, tatuatori, fotografi e trucco sposa, barbieri |
| Ricerca di mercato | **60** | Lombardia: BG 10, VA 7, MB 6, LC 6, BS 6, SO 6, CO 5, CR 4, PV 4, LO 3, MN 2, MI 1 | impiantisti 14, falegnamerie e legno 15, aziende agricole con vendita 14, ingrossi 9, studi tecnici 8 |

Tutti e due i file sono passati da `controlla-lista.py` con 0 e da
`voce-check.py` con 0 tell.

## Siti: come è stata fatta

- **Circa 190 profili letti per 100 righe.** Più di 60 scartati perché sotto i
  200 follower o fermi. **Sette avevano il sito**: lashdesignbeautylab.it,
  giulialashartist.it, victoriajohnsonpmu.com, profartofficial.com,
  lashbeautyboutique.it, alexandralashes.com, leciglia.it. Tolti anche due
  doppi profili e un dominio che apre solo un login.
- **Google su tutte e cento le righe.** L'operatore l'aveva fatto su 70; le
  altre 30 le ho cercate io il 29 mattina, una per una, e la prova sta in
  colonna dopo `Google 29/9`. Nessuna aveva un sito suo. Due casi da sapere:
  `leciglia.it` è di Linda Massocco, non di Elena né di Dani che stanno in
  lista a Biella; il vecchio profilo di Jackelin, `@gackelin.kicima`, non
  esiste più.
- **Ganci**: 83 nessun sito, 14 su piattaforma (Treatwell, Setmore,
  SimplyBook, Beauty Places, Bio Sites, Wix, B-Vanity, SumUp: il messaggio la
  nomina), 3 link in bio rotto (`@touche.torino` Leadpages in 404,
  `@unique_by_alina` AppyPro in errore, `@valery.lashtrainer` pagina chiusa da
  password).
- **Il complimento viene dai post e dagli highlight**, non dalla bio: set con i
  millimetri in didascalia, highlight sui lavori guariti, gare e ruoli da
  giudice. Uno citava un post personale (un «Davide dal 2012») ed è stato
  riscritto: nei DM non si nomina la vita privata.
- «Un sito tuo non esiste» è diventato «non c'è» su cinque righe: il fatto è
  lo stesso, il tono no.
- `@extensionscigliaverbania` ha 10 post e segue 2.946 profili: resta, ma è la
  riga più debole della lista.

## Ricerca: come è stata fatta

- **Circa 110 profili aperti per 60 righe.** Fuori regione circa 35 (il 20-30%
  dei risultati «falegnameria + città lombarda» sta fuori), fermi da più di
  3-4 mesi circa 30, sotto i 200 follower circa 25. Due handle già usati il
  19/9 (`luis_ingrosso`, `macchivarese1941`) tolti prima del controllo.
- Ogni riga ha il profilo aperto e **un fatto preso dalle didascalie**: il
  collaudo allo studentato Value One, i 400 serramenti in centro a Milano, i
  tre mercati a settimana di Montevecchia.
- **«Qui in zona» era falso su 19 righe**: da Seveso non si scrive così a
  Valtellina, Oltrepò, Mantovano, Cremonese e Lodigiano. Ora c'è la zona vera
  («le falegnamerie della Valtellina») e la chiusura dice «della zona».
- Tre righe hanno l'ultimo post fra fine giugno e metà luglio.

## La posta, letta il 28 e il 29

Nessuna risposta nuova da lead fra il 21 e il 29/9 nella posta di
`@patrick.sappa`. L'unica mossa è **Per Un Pelo**: «si me la mandi pure» il
25/9 alle 8:51, link mandato alle 20:39, nessuna risposta. Aggiornati
`risposte-dm.csv` e l'esito sul banco.

⚠️ **La posta che si legge da qui non è quella da cui partono i DM.** Era già
scritto il 19/9 in [[2026-09-19-siti-piemonte-capelli]]: dal 16/9 Patrick
manda da un altro account. Il 29/9 sera il banco segna **tutte le 160 righe
di oggi come mandate**, e nella posta di `@patrick.sappa` il 29/9 non si apre
nessun thread nuovo. Quindi le risposte a questi DM, e con ogni probabilità
Design Capelli e Adelina (che [[FATTI]] dà in attesa della bozza dal 20 e dal
19/9), stanno in una casella che il passo 3-bis non legge. Quale account sia,
e come leggerlo: `TODO` Patrick.

*Corretto il 29/9 sera:* qui c'era scritto «nessun DM parte dal banco dal
17/9». Era dedotto da `contattati.csv`, che fra il 17 e il 29 è fermo. Il
server del banco funziona, lo mostrano i 160 di oggi. Degli invii fra il 17 e
il 29, se ci sono, il file non sa niente.

## Trappole nuove

- **Due operatori sullo stesso browser si pestano le schede**: le tab non sono
  isolate, uno ha navigato quella dell'altro. Un operatore alla volta sul
  browser, o si lavora a turno.
- **Le API di Instagram vanno in 429 dopo circa 600 letture in due**, e
  `feed/user/` risponde HTML invece di JSON. Si legge il profilo dalla pagina:
  il testo alternativo delle foto della griglia è la didascalia.
- **La ricerca di Instagram con più parole** («impianti elettrici como») torna
  vuota: una parola e la città nel nome.
- **Google regge una ricerca ogni 20 secondi**; a raffica chiede il captcha
  dopo circa 56. Brave va in 429 dopo 8 righe e prima dà SITO falsi sui nomi
  generici («Microblading»).
- **Google cifra i link dei risultati** (`/goto?url=…`): il dominio si legge
  dal `cite` sotto il titolo.
- **L'hook di fine sessione ha committato una bozza non verificata** a 104
  righe (`a8b1f12`). La versione giusta è quella di questo commit.
- `controlla-lista.py` segnala una piattaforma scritta in verifica anche quando
  è di un'altra attività (il Fresha di un'omonima): si scrive «scheda di
  prenotazione di X, altra attività».

## Collegamenti

[[2026-09-25-barbieri-piemonte-e-ricerca]] · [[metodo-instagram]] ·
[[metodo-liste]] · [[dm-instagram-vetrina]] · [[dm-instagram-ricerca]] ·
[[script-indagine]] · [[voce-denkicode]]
