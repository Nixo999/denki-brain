---
type: risorsa
riga: Lo stato di DenkiCode adesso - chi, soldi, cosa e' aperto, cosa e' bloccato. Si legge a ogni sessione, si riscrive a ogni chiusura. Max 80 righe.
updated: 2026-10-01
verificato: 2026-09-16
source: denkicode
tags: [stato, fatti]
---

# I fatti — stato al 27 settembre 2026

**Questo file si riscrive, non si accumula: massimo 80 righe.** Una riga per
cosa aperta. Il racconto dei giri sta nella nota progetto, la giornata nel
[[registro-interventi]]. Senza data = non scade; (data) = vero quel giorno;
→ = vive là.

## Chi

- Patrick Sappa, 21, unica voce commerciale. Non scrive codice, non usa il terminale.
- Nicola Larezza, 22, lead dev. Scrive tutto il codice.
- Giulia Venneri, 21, cold call a provvigione, **unica al telefono**, senza vault. 131 righe chiuse (13/09), **reso conto mai arrivato** → [[metriche]]
- Morgan, fratello di Patrick, segnalatore dal 15/09: compenso e ore `TODO` → [[morgan]]
- Gabriele ed Edoardo fuori in via definitiva (15/09) → [[gabriele-edoardo]]
- DenkiCode è il terzo impegno di tutti e tre → [[team-e-vincoli]]
- Patrick, Nicola e Seba «probabilmente» soci in OperO (30/09): forma, quote e credito da chiarire → [[sebastian-torres]]

## Soldi

- OperO: **1.400 € incassati, 1.000 € da incassare**, gli ultimi della prima tranche (30/09); ricevuta dei 1.000 entrati `TODO` → [[sebastian-torres]]
- Albybike: online e **mai pagato** (11/09) → [[albybike]]
- Nessuna P.IVA: «ricevuta», «collaborazione occasionale» → [[vincoli-fiscali]]

## Siti aperti — bozza online, il DM col link è di Patrick

| Sito | Online su | Stato (data) | Prossimo passo |
|---|---|---|---|
| [[sito-petliving]] | petliving.netlify.app | giro 2 (30/09) dopo il verdetto di Nicola; 375 guardata, 1440 no; loro: «Se vuole mandarci qualcosa intanto» | verdetto di Nicola sul giro 2, poi il DM col link; foto di stripping e logo da chiedere |
| [[sito-soul-ink]] | soul-ink-torino.netlify.app | giro 3 (26/09), verdetto di Nicola `TODO` | DM Instagram; lo studio non ha contatti pubblici |
| [[sito-perunpelo]] | perunpelo.netlify.app | giro 3 (25/09), verdetto `TODO`; lei ha detto sì il 25/09 | DM, domande per Ambra in [[perunpelo]] |
| [[sito-leibeautyroom]] | leibeautyroom.netlify.app | giro 7 (25/09): stanze chiuse che si aprono dal menu | ok di Tania sulle 3 foto prese da Google e Instagram; DM |
| [[sito-p0t-tattoo]] | p0t-tattoo.netlify.app | giro 9 (25/09) | DM Instagram: prezzi, caparra, giorni, foto dei guariti |
| [[sito-designcapelli]] | designcapelli.netlify.app | giro 1 (21/09); lei vuole la bozza nel DM | orari in conflitto PagineGialle/Fresha, li conferma Daniela; DM |
| [[sito-adelinanails]] | adelinanails-site.netlify.app | giro 3 (19/09); lei ha risposto «ok» | DM con le domande su prezzi, orari, indirizzo |
| [[sito-barbershop-snia]] | barber-shop-snia.netlify.app | giro 16 (19/09), Nicola non l'ha rivisto | consenso dei genitori per il viso del bambino, o la foto si toglie |
| [[sito-newfantasy]] | newfantasy-parrucchieri.netlify.app | giro 1 (16/09); DM finito in un autorisponditore | link su WhatsApp; prenotazioni su `localStorage`, PIN `1234`: per venderlo serve uno store ospitato |
| [[sito-hairstylebrescia]] | hairstylebrescia.netlify.app | 16/09; sbarramenti verificati nei file, non con `curl` | DM mai partito |
| [[sito-laurafranzoni]] | laurafranzoni.netlify.app | online il giro 2; il giro 3 (`93081ec`) è in locale, non pushato | push, poi il DM mai partito |
| [[sito-nails-robyy]] | nailsrobyy.netlify.app | 14/09; lei: «Ciao ok vediamo» | DM col link |
| [[sito-pinkploy]] | pinkploy.netlify.app | 14/09; lei: «si prova mandami» | DM col link |
| [[sito-mikuma-dogs]] | mikumadogs.netlify.app | giro 7 (11/09) | il file buono del logo lo chiede Patrick |

Safari e iPhone veri **mai provati** su nessuno: il link si apre da un iPhone
prima del DM. Fermi o mai proposti: DSI, Atelier Selva, Salone di Andrea,
Nails Mania, Tarilli, Fiftynine, Castiglione, NG Barber (repo **pubblica**),
Lobidù, Da Caterina: lo stato sta nella loro nota.

## Altro aperto

- **Edilida** (edile, Travagliato): modulo compilato il 18/09, Patrick punta a una videochiamata; il riepilogo di zona promesso a Penta ed Edilida **non esiste** → [[edilida]]
- **V-BAG**, gestionale con login pushato il 16/09: spento finché Nicola non mette `ADMIN_PASSWORD` e `GITHUB_TOKEN` su Netlify → [[2026-09-16-vbag-gestionale-login]]
- **OperO, Intermediar + Receive → CO-OPERO** (30/09): portale gratuito con Clienti in entrata e Fornitori in uscita. Deciso da Patrick e Seba, supera il Receive a pagamento del 24/09. Da conoscere, non da fare; lavoro nuovo fuori dai 2.400 € → [[opero-intermediar-receive]]
- **Instagram in automatico** (30/09): Patrick ha scelto l'API ufficiale, post e storie li pubblica uno script. **Script scritto** (01/10, repo pubblico `Nixo999/denkicode-social`, mai provato con un token vero); **tocca a Nicola**: app Meta, token e secret; profilo `@denkicode`, gia' professionale; Pagina Facebook `TODO`. Piano: 3 post a settimana + 1 storia al giorno, testi delle prime due settimane da rileggere per Patrick → [[piano-instagram]]
- **Riservatezza + non concorrenza a 5 anni** (25/09): penali 5.000-30.000 €, **non firmato**, controproposta legata al saldo, ora 1.000 € (30/09); da rileggere se si diventa soci → [[accordo-riservatezza-opero]]
- **denki-agents**: gateway chiuso (16/09), cantiere a **un dollaro a sito** in locale, 0,57-0,82 USD a bozza; manca il token Apify per un giro con foto vere → [[denki-agents]]
- Le 87 righe di Gabriele ed Edoardo sono passate a Giulia (13/09) → [[2026-09-13-liste-giulia-groane-vimercatese]]

## Bloccato, e perché

- **Banco DM** (01/10): `/banco` riscritto, il piano lo stampa `prossimo-giro.py`, mai girato sul Mac di Patrick. La posta non è letta dal 21/09 (367 DM senza esito, il campo «Chat» resta vuoto) e **733 righe sono sul banco mai mandate** → [[2026-10-01-banco-ricircolo]]
- **OperO, storico**: la migrazione non si fa più (13/09), Seba vuole solo un report giugno-agosto da `strumenti/report-mesi.mjs`; manca la chiave `OPERO1_SERVICE` da Settings → API di OperO 1, o un login di segreteria → [[opero]]
- **DenkiShift non è installabile in produzione**: dimostrabile, senza date → [[denkishift]]
- **La produzione resta fuori** su tutti e due i prodotti → [[modifiche-al-database]]
- **Le chiavi non entrano nel vault.** Le password le imposta Trevis dal 23/09 su richiesta; pagine web e account restano fuori → [[credenziali]]
- Il collo di bottiglia è la **generazione lead** → [[generazione-lead]]

## Il livello dei siti

Passano NG Barber, Fiftynine e le bozze fatte col [[processo-siti]] intero
(8/8). Prima di pubblicare: `python3 01-Coding/strumenti/controlla-sito.py ~/lavoro/<cartella>`.
Quello che è già stato bocciato sta in [[direttive-siti]] → [[livello-siti]]
