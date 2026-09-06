---
type: progetto
status: attivo
client: nails-mania
stack: [html, gsap, netlify]
started: 2026-09-07
deadline: TODO
updated: 2026-09-07
source: claude
valore: TODO
incassato: 0
---

# Sito Nails Mania — bozza al buio, Seriate

Sito vetrina in una pagina per **Nails Mania**, centro di ricostruzione unghie
mani e piedi di **Lory Frosio** a **Seriate (BG)**. È la riga
`@nailsmaniabergamo` della [[2026-09-05-instagram-bg-va|lista del 5
settembre]]: **dominio `nailsmania.net` morto** (NXDOMAIN) ma la pagina dei
corsi è ancora nell'indice di Google. Brief di Nicola (6 settembre 2026):
«artistico e molto bello esteticamente, non un'altra estensione del loro
Instagram, un sito che effettivamente attirerebbe persone a fare le unghie da
loro».

**Repo**: `github.com/Nixo999/nailsmania-site` (privato, creato il 6
settembre 2026 con `gh`) — in locale `~/lavoro/nailsmania-site` sul MacBook
di Nicola.
**Online**: no — Netlify, come ogni bozza ([[netlify]]).
**Stack**: HTML puro, un solo `index.html`, GSAP 3.13 + ScrollTrigger da CDN
(motion additiva), 12 foto in `assets/ig/`, `netlify.toml` e `robots.txt`
con i tre sbarramenti: **noindex** finché il sito non è suo.

## Da dove vengono i dati

Tutto letto il 6 settembre 2026, niente inventato.

| Dato | Fonte |
|---|---|
| Bio: «Negozio di Ricostruzione Unghie mani e piedi Uomo e Donna. In Collaborazione con Medici, Podologi, Dermatologi. x info dm», 232 follower | profilo Instagram, dal pannello |
| 11 post del 2026 senza didascalia, 1080 px, foto da telefono con scritte sopra | pagine dei post |
| **Sede attuale: Via Brusaporto 1** | scheda Fresha e oraridiapertura24, **e il biglietto da visita nella foto del 6 giugno 2026** («Via Br…»). Via Dante 66 è la sede del sito del 2014 e delle directory vecchie |
| Tel 347 4824312 | post del 2 luglio 2026, vecchio sito, directory |
| Lory Frosio, onicotecnica dal 2005, motto «le unghie rispecchiano la nostra personalità» | vecchio sito, «Chi siamo» (Wayback 2016) |
| Servizi: ricostruzione gel nelle forme pipe/stiletto/edge/mandorla/square, tip/cartina/fiberglass, onicofagia, alluce, ipercheratosi, ciglia, trucco semipermanente, corsi | vecchio sito (Wayback 2016-2021, 8 pagine) |
| Orari: lun e dom chiuso, mar solo mattina, mer-ven fino alle 19, sab mattina | le due schede recenti divergono sui minuti: nel sito c'è solo la parte concorde |

⚠️ **Le foto non reggono una hero**: sono scatti da telefono con «nailsmania»
scritto sopra, una è una grafica dell'8 marzo presa da internet. Entrano solo
come prima/dopo dell'alluce, ritagliate. **I colori dei gel sono veri**:
campionati pixel per pixel dalle foto (arcobaleno del 2 luglio, cat-eye blu,
tiffany, smeraldo, fucsia, rosso, oro).
⚠️ Nessun prezzo, nessuna recensione, nessuna foto del negozio o di Lory.
Ciglia, trucco semipermanente e corsi risultano dal sito del 2016: nel sito
sono «su richiesta, chiedi in negozio».

## Com'è fatto

Metodo [[processo-siti]]: PRODUCT.md → `concept-seed` seed **`7989d0d3`** →
scelta di Nicola sul tool strutturato (la pagina di decisione nel pannello si
era chiusa senza risposta la volta prima). **Il dado ha assegnato «La vetrina
di smalti»** (candidato 7) e Nicola l'ha tenuto, sopra la mia scelta (la
cartella colori) e lo sfidante ebru.

Mondo: porcellana fredda, cromo dei tappi, vetro in gradiente, e **i loro gel
come unico colore pieno**. Bricolage Grotesque, unica famiglia. Hero: una
mensola con sette boccette disegnate in SVG, una per colore dell'arcobaleno
del post del 2 luglio 2026, etichetta «Nails Mania» e nome del colore.
**Interazione firma: tocchi una boccetta e il sito indossa quel colore**
(bottoni, titolo, forme, etichette). Poi: «Un centro di ricostruzione, non un
nail bar» con quattro fatti → campionario delle cinque forme nel colore
scelto → «Mani» in nove moduli rigati fitti (raise dalla densità giapponese,
sfidante declinato) con la riga del refil → «Piedi, e l'alluce» col
prima/dopo vero → tre servizi su richiesta → dove e quando con la mappa.

Errore trovato in costruzione: le boccette erano `<use>` di un `<symbol>` e
gli stili del documento non entrano nell'ombra di `use`: nere. Ora l'SVG è
inline per ognuna. Regola: **niente `<use>` per grafica che prende colore da
CSS.**

## Stato

🟡 **Bozza sul repo privato, misurata a 1440 e 375**: hero a due righe, la
mensola sta nel primo schermo, zero overflow, scelta del colore funzionante.
Finish review: vedi diario. **Non vista su browser vero né su telefono.**

## Soldi

| | |
|---|---|
| Pattuito | niente — nessun contatto ancora |
| Listino di riferimento | sito vetrina, [[prodotti-e-listino]] |
| Forma | Ricevuta prestazione occasionale → [[vincoli-fiscali]] |

## Aperto

- [ ] Pubblicazione su Netlify ([[netlify]])
- [ ] Il DM del 5 settembre è sul banco: la bozza entra nel secondo messaggio
- [ ] Da confermare con Lory: orari, sede (Brusaporto 1), se ciglia, trucco e corsi sono ancora attivi, foto senza scritte
- [ ] Il dominio `nailsmania.net` è libero: da riprendere se compra

## Collegamenti

[[netlify]] · [[processo-siti]] · [[dm-instagram-vetrina]] ·
[[2026-09-05-instagram-bg-va]] · [[nails-mania]] · [[registro-interventi]]
