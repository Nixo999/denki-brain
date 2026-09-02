---
type: progetto
status: attivo
client: bar-tabacchi-fiftynine
stack: [html, netlify]
started: 2026-09-01
deadline: TODO
updated: 2026-09-02
source: claude
valore: TODO
incassato: 0
---

# Sito Bar Tabacchi Fiftynine — bozza in trattativa

Sito vetrina in una pagina per **Bar Tabacchi Fiftynine**, bar tabaccheria e
pizzeria in via Nazionale dei Giovi 59, **Cesano Maderno (MB)**. Il locale
**non ha un sito**: ha un profilo Instagram da 7 post
(`@bartabacchi__fiftynine`, 57 follower), la scheda Google e un menù stampato.
Cliente: [[bar-tabacchi-fiftynine]] — nato come bozza al buio il 1° settembre
2026 (schema Castiglione, [[2026-08-30-sito-castiglione]]), **il 2 settembre
il proprietario ha mandato il menù in PDF**: da lì è una trattativa.

**Repo**: `github.com/Nixo999/fiftynine-site` (privato, creato il 1° settembre 2026) — in locale `Desktop/fiftynine-site` sul Mac di Patrick
**Online**: no — va su Netlify come ogni bozza ([[netlify]])
**Stack**: HTML puro, un solo `index.html`, zero build. `netlify.toml` e
`robots.txt` con lo schema di NG Barber: **noindex** finché il sito non è loro.

## Da dove vengono i dati

Tutto letto il 1° settembre 2026, niente inventato:

| Dato | Fonte |
|---|---|
| Orario **5:30–21:30**, colazioni · pizzeria · aperitivi · tabacchi | bio Instagram |
| Telefono **0362 528451**, 4,4 su **31 recensioni**, 10–20 € a persona, tavoli all'aperto, cani ammessi | scheda Google (screenshot di Nicola) |
| Listino cocktail (Spritz 6 €, Negroni 7 €…), birre, frittini, **formula special 12 €** = drink + frittini misti | locandina fotografata nel post del 6 agosto 2025 |
| Gyoza, marocchino con Nutella, waffle, cappuccino e brioche, tranci di pizza con patatine | i 7 post, foto scaricate in `assets/img/` |
| **Menù completo**: 44 pizze, calzoni, focacce, sfiziosità, panini, pizze baby e menù bimbi, bevande; asporto, **consegna a domicilio**, sala su prenotazione, pizzate di gruppo; tabaccheria, sigarette elettroniche, pagamenti, ricariche, Gratta e Vinci, SuperEnalotto | **PDF del proprietario** (6 pannelli, Illustrator, 15 gennaio 2026), mandato via WhatsApp il 2 settembre 2026 |
| «Ottimo sia per colazione che per pranzo», «Servizio rapido e gentilezza», «Perfetto per una pausa caffè o un aperitivo con amici» | recensioni Google incollate da Nicola |

⚠️ **Due listini con date diverse.** Il menù del proprietario (gennaio 2026)
comanda su pizze, sfiziosità, panini e bevande; i cocktail e la formula
aperitivo a 12 € restano dalla locandina dell'agosto 2025, perché il menù non
li riporta. Dove i due divergono (birra alla spina: 5/6 € sulla locandina,
3/5 € sul menù) vince il menù. Il sito scrive «prezzi del menù in vigore da
gennaio 2026».
⚠️ **Il giorno di chiusura non è noto**: Google dice solo «apre mer alle 5:30».
Il sito non promette «tutti i giorni».
⚠️ **Le foto sono a 640 px**: Instagram rifiuta la risoluzione piena senza
login (403). Bastano per le card, non per un'immagine a tutto schermo — per
questo l'hero è l'insegna, non una foto.

## Il menù nel sito

Capitolo `#menu` dopo la pizzeria, **nei colori del menù stampato** (legno
scuro, pannelli chiari): 44 pizze su due colonne con la Fiftynine marcata
come pizza della casa, poi calzoni e focacce, sfiziosità, panini con doppio
prezzo focaccia/panino, bevande. Il PDF originale pesa 21 MB: nel sito c'è
una **versione ricompressa da 1 MB** (`assets/menu-bar-tabacchi-fiftynine.pdf`,
pagine rasterizzate a ~160 dpi), scaricabile dal capitolo e dal footer.

## Com'è fatto

L'idea è **la giornata del bar**: le ore vere (5:30 colazione, 12:00 pranzo,
18:00 aperitivo, 21:30 chiusura) fanno da capitoli, e nell'hero una linea del
giorno legge l'ora di Roma e dice **«Aperto adesso · aperitivo»** o **«Chiuso
adesso · riapre alle 5:30»**. È l'unica cosa che un sito di bar deve dire
prima di tutto. Colori dall'insegna (blu, il 59 rosso, bianco); il giallo del
loro piattino solo sull'indicatore. Syne per i titoli, Yellowtail per lo
script «fiftynine», Public Sans per il testo. Motion con **GSAP 3.13 +
ScrollTrigger** da CDN, additiva (senza libreria o con reduced-motion la pagina
è completa): intro dell'insegna, parallasse nelle foto, listini a scaletta, il
4,4 che conta da zero. **Sotto la nav, lasciata l'insegna, la linea del giorno
si riempie con lo scroll**: lo scroll è la giornata.

## Stato

🟡 **Bozza fatta, sul repo privato, guardata con gli occhi.** Il 2 settembre
sera il capitolo menù è stato visto e non solo misurato: il pannello del
browser consegna le animazioni e gli screenshot **solo quando la scheda è in
primo piano**. Due difetti che le misure non davano — il pannello Bevande
allungato a vuoto, marchio e pillola del telefono che non ci stavano in nav
sotto i 560px — trovati e corretti guardando.

🟡 **Bozza fatta, sul repo privato.** Verificata nel pannello a 1440 e 375
emulati, dal server e non dall'istantanea statica (che non mostra né JS né
foto): zero overflow a 1440, 7 foto su 7, console pulita, motion a fine corsa
senza elementi rimasti invisibili, indicatore «chiuso» giusto alle 23:40 e
**«Aperto adesso · pranzo»** il 2 settembre a mezzogiorno, col punto sulla
linea al posto giusto: lo stato aperto non è più un buco. **Non vista su browser vero né su telefono.**

## Soldi

| | |
|---|---|
| Pattuito | niente — nessun contatto ancora |
| Listino di riferimento | sito vetrina, [[prodotti-e-listino]] |
| Forma | Ricevuta prestazione occasionale → [[vincoli-fiscali]] |

## Aperto

- [ ] Pubblicazione su Netlify (login di Nicola, vedi [[netlify]]); repo privata finché non si decide se renderla pubblica
- [ ] Primo contatto: è a Cesano Maderno, zona di Giulia — DM Instagram
      ([[dm-instagram-vetrina]]) o passaggio di Patrick dopo una chiamata
- [ ] Telefonata di controllo su prezzi e giorno di chiusura prima di mandare il link
- [ ] Se rispondono: foto in risoluzione piena da loro, e via il `noindex`

## Collegamenti

[[netlify]] · [[prodotti-e-listino]] · [[script-siti-vetrina]] ·
[[dm-instagram-vetrina]] · [[2026-08-30-sito-castiglione]] · [[registro-interventi]]
