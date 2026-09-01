---
type: progetto
status: attivo
client: nessuno
stack: [html, netlify]
started: 2026-09-01
deadline: TODO
updated: 2026-09-01
source: claude
valore: TODO
incassato: 0
---

# Sito Bar Tabacchi Fiftynine — bozza non commissionata

Sito vetrina in una pagina per **Bar Tabacchi Fiftynine**, bar tabaccheria e
pizzeria in via Nazionale dei Giovi 59, **Cesano Maderno (MB)**. Il locale
**non ha un sito**: ha un profilo Instagram da 7 post
(`@bartabacchi__fiftynine`, 57 follower) e la scheda Google. Cliente: nessuno,
ancora — è materiale pronto per Patrick, come il sito di NG Barber e
quello di Castiglione ([[2026-08-30-sito-castiglione]]).

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
| «Ottimo sia per colazione che per pranzo», «Servizio rapido e gentilezza», «Perfetto per una pausa caffè o un aperitivo con amici» | recensioni Google incollate da Nicola |

⚠️ **I prezzi sono quelli della locandina dell'agosto 2025**: il sito lo dice
in una riga («quella al banco vale più di questa pagina»), ma prima di mandare
la bozza conviene una telefonata di controllo.
⚠️ **Il giorno di chiusura non è noto**: Google dice solo «apre mer alle 5:30».
Il sito non promette «tutti i giorni».
⚠️ **Le foto sono a 640 px**: Instagram rifiuta la risoluzione piena senza
login (403). Bastano per le card, non per un'immagine a tutto schermo — per
questo l'hero è l'insegna, non una foto.

## Com'è fatto

L'idea è **la giornata del bar**: le ore vere (5:30 colazione, 12:00 pranzo,
18:00 aperitivo, 21:30 chiusura) fanno da capitoli, e nell'hero una linea del
giorno legge l'ora di Roma e dice **«Aperto adesso · aperitivo»** o **«Chiuso
adesso · riapre alle 5:30»**. È l'unica cosa che un sito di bar deve dire
prima di tutto. Colori dall'insegna (blu, il 59 rosso, bianco); il giallo del
loro piattino solo sull'indicatore. Syne per i titoli, Yellowtail per lo
script «fiftynine», Public Sans per il testo. Nessuna libreria: reveal con
IntersectionObserver e rete di sicurezza a tempo.

## Stato

🟡 **Bozza fatta, locale.** Verificata nel pannello a 1440 e 375 emulati:
zero overflow, 7 foto su 7 caricate, console pulita, indicatore «chiuso» giusto
alle 23:40. **Non vista su browser vero né su telefono.** Lo stato «aperto»
dell'indicatore non è stato provato: alle 23:40 il bar era chiuso.

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
