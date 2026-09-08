---
type: progetto
status: bozza-online
cliente: "[[osteria-tarilli]]"
created: 2026-09-08
updated: 2026-09-08
source: claude
repo: Nixo999/tarilli-site
tags: [sito-vetrina, bozza, ticino, ristorazione]
---

# Sito Osteria Tarilli — bozza non commissionata

**Osteria Tarilli**, Via Ronco Nuovo 2, 6949 Comano (TI), a 300 m dalla RSI.
Riga della lista [[2026-09-07-instagram-ticino-ristorazione]], gancio 1.
Instagram `@osteria.tarilli`: 2.055 follower, 28 post. Nessun sito: solo
Instagram, Facebook, HappyCow, Tripadvisor e i portali.

⚠️ **Non è una pizzeria.** Nicola l'ha chiesta come «pizzeria Tarilli»: bio,
logo e dodici caption dicono «osteria, cucina italiana contemporanea». Di
pizza non c'è traccia in nessun post. Il sito non ne parla.

## Dati verificati (fonte: bio e caption Instagram)

| Cosa | Dato | Fonte |
|---|---|---|
| Telefono | 091 941 03 24 | bio |
| Email | osteria.tarilli@gmail.com | caption 24 ago |
| Indirizzo | Via Ronco Nuovo 2, Comano | caption (HappyCow dice 12: vince il titolare) |
| Parcheggio | 35 posti privati, gratuiti | bio |
| Pranzo | menù che cambia ogni giorno, sempre vegetariano + insalata | caption 24 ago |
| Brunch | sab e dom dalle 10:30, All You Can Brunch CHF 39, bambini ≤12 CHF 15, 50 posti, prenotazione obbligatoria, vegano e gluten free | caption 8 ago + locandina |
| Aperitivo per due | gio–sab dalle 18, tagliere + 2 spritz CHF 23 | caption 16 lug |
| Cuoco | Giuseppe, 46 anni di mestiere, cavatelli a mano ogni mattina | caption 12 ago |
| Orari | mar–dom 10:30–15:00, mar–sab 18:30–24:00, lunedì chiuso | **HappyCow, non il titolare: `TODO` confermare** |

Recensioni: HappyCow 3,5 su 6, una di aprile 2026 dice che la gestione è
cambiata. Non sono nel sito. Tripadvisor risponde 403.

## Identità

Logo tondo crema con «OSTERIA TARILLI» in serif bold verde bottiglia,
«cucina italiana contemporanea», corsivo «Cena Serale». Locandine crema +
verde + oro + rosso mattone, serif didone. **Il sito usa i loro colori e la
loro tipografia**: Bodoni Moda per i titoli, Karla per il testo. Il crema è
loro, non il nostro default (regola del processo, passo 0).

## La bozza

Repo `~/lavoro/tarilli-site` → `Nixo999/tarilli-site` (privata).
**Online su <https://tarilli.netlify.app>** dalle 23:1x dell'8 settembre: sito Netlify
`tarilli` sul team `denkicode`, deploy diretto dal CLI (`netlify deploy --prod`),
non collegato al repo: un push non ripubblica, si rilancia il deploy a mano.
Login Netlify autorizzato da Nicola nel browser, nessuna credenziale passata da me. Statico
puro: `index.html`, `assets/stile.css`, `assets/moto.js`, GSAP da CDN.
Processo [[processo-siti]] completo; impeccable seed **`b6c92fb4`**,
direzione assegnata 7/7 «il passe della cucina»: la pagina è il tragitto del
piatto, la nav è la barra dei bonghi con le comande appese, i piatti veri
fluttuano in tondo e derivano col puntatore. Pagina di decisione servita e
lasciata senza risposta per 4 minuti: si è proceduto con l'assegnata.

Sezioni: hero con sei piatti · pranzo (comanda del 24 agosto + sei piatti su
una baseline) · Giuseppe · brunch (fascia verde, prezzi, menù dalla
locandina, tre foto) · aperitivo · dove (terrazza, orari, mappa) · footer.

Foto: 12 da Instagram a 360×640, usate tonde (ritagli `sips -c`) o in
cornice. Una locandina si mostra intera. Niente pizza, niente stock.

Tre sbarramenti agli indici attivi (meta robots, `X-Robots-Tag`,
`robots.txt`).

## Finish review (impeccable, 8 settembre sera)

`disposition: fix`, otto punti. Applicati: piatti dell'hero su una griglia senza
coperture (il pancake era coperto all'80%), su mobile i piatti in una striscia
in flusso sotto il bottone (un piatto copriva «Cosa c'è oggi» sul telefono di
Nicola), comanda intitolata con la sua data invece di «oggi», via il «dalle
10:30» del brunch (era solo per il 1° agosto), avviso visibile «orari
indicativi, da confermare», micro-etichette in corsivo didone, via il bordo a
zig-zag, rivelazioni solo sulle figure. Due «claim inventati» erano invece
caption del cliente (parmigiana 8/9, bernese 11/7): fonti scritte in
`PRODUCT.md`. Non fatto: il «sans stretto» del contratto, Karla resta e
`DESIGN.md` lo registra. `DESIGN.md` scritto dal documenter.

## Da fare

- [ ] Collegare il sito Netlify al repo, o ricordarsi il deploy a mano.
- [ ] Confermare gli orari col titolare prima di pubblicarlo come suo.
- [ ] DM a Patrick: il messaggio è già nella riga della lista.
- [ ] Foto vere in alta risoluzione dal titolare, se risponde.

## Collegamenti

[[processo-siti]] · [[trappole]] · [[registro-interventi]] · [[netlify]] ·
[[2026-09-07-instagram-ticino-ristorazione]] · [[dm-instagram-vetrina]]
