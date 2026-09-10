---
name: processo-siti
description: Come si costruisce un sito vetrina DenkiCode. Da usare prima di scrivere una riga di HTML per un sito cliente o una bozza. Divide il lavoro fra direttore (decide, non scrive codice) e operatore su Opus (scrive e misura), parte dallo starter e dall'essenza del cliente da Instagram, impone un'apertura animata e una metafora sola. Non vale per OperO e DenkiShift, dove comanda il CLAUDE.md del repo.
---

# Il processo, in ordine

Saltare un passo ha già bruciato tre prime versioni: Castiglione v1 («il sito
più piatto della storia»), DSI v1 («sta venendo malissimo»), Da Caterina v1
(«da telefono è orribile»). Tutte e tre costruite tirando dritto sul codice.

## 0. Direttore e operatore — chi fa cosa

**Il direttore non scrive codice.** Decide, scrive il brief, giudica il
risultato, pubblica. Regola dal 10 settembre 2026.

| | Direttore (la sessione, di solito Fable) | Operatore (subagente, Opus) |
|---|---|---|
| Legge | Instagram del cliente, questa skill, la nota di progetto | Il brief, le skill di design, `trappole.md` |
| Decide | La metafora, la direzione, cosa esce | Come si scrive, quali valori, quale tecnica |
| Produce | Un brief da 40 righe | Il sito, e le misure |
| Non fa | Non apre le skill di design, non scrive HTML | Non pubblica, non parla al cliente, non decide la direzione |

Si lancia con l'agente `operatore`, che gira su Opus con `effort: high`. Il
motivo è di costo: la catena di design è ~17.500 parole, e quelle stanno nel
contesto dell'operatore, non in quello del direttore. Il direttore spende
quaranta righe di brief e ne legge dieci di rapporto.

**Se il direttore si trova a scrivere CSS, il processo è già saltato.**

## 1. Lo starter, prima di tutto

```bash
python3 01-Coding/strumenti/nuovo-sito.py <nome-cliente>
```

Porta reset, `--vh`, `.cattura`, rivelazioni, tre sbarramenti, cache giusta e
la firma DenkiCode nel footer. **Non porta gusto**: colori, font, griglia e
sezioni nascono ogni volta. Vedi `starter-sito/LEGGIMI.md`.

## 2. L'essenza del cliente — la fa il direttore, e la scrive

Prima di qualunque skill: il logo, il vecchio sito, i post. Cosa fotografano,
con che parole, il ritmo del mestiere, gli oggetti fisici del posto, e **cosa
non c'è** (recensioni, prezzi: si dichiara, non si inventa).

Le foto si scaricano subito: gli URL Instagram scadono in giorni.

Da lì esce **una metafora sola**, scritta nella nota di progetto. Se si
potrebbe spostare su un altro cliente, non è quella giusta. Il metodo per
esteso, con i tre casi che hanno funzionato, sta in
`01-Coding/stack/essenza-e-motion.md`.

## 3. Il brief — l'unica cosa che attraversa il confine

Massimo quaranta righe. Contiene: la metafora in una riga, i colori campionati,
i font, le sezioni con il contenuto vero, quale skill di stile usare (**una**,
mai due), l'apertura animata voluta, i quattro tipi di motion del passo 4 di
`essenza-e-motion.md`, e cosa è `TODO` perché non verificato.

Quello che il brief non dice, l'operatore lo decide. Un brief che detta i pixel
è il direttore che scrive codice con altre parole.

## 4. Cosa fa l'operatore

Nell'ordine, nel suo contesto:

1. `design-taste-frontend` — la direzione anti-slop. Si legge per decidere cosa
   **non** fare.
2. **Una** skill di stile: `high-end-visual-design`, `minimalist-ui` o
   `industrial-brutalist-ui`. Due si contraddicono e il risultato è una media
   senza carattere.
3. `brandkit` **solo se** il cliente non ha identità. Se ha logo e font, si salta.
4. `ui-ux-pro-max` per pescare un valore preciso: palette di settore, accoppiate
   di font, preset GSAP.
5. `impeccable` **durante**, non alla fine. `PRODUCT.md` prima del dado, il seed
   scritto nella nota di progetto, il detector meccanico che gira mentre si
   costruisce.
6. `voce-denkicode` sul copy prima della finish review: il detector guarda
   marquee e spaziature, non le parole.
7. `emilkowalski-motion` per ultima, sopra l'apertura e i quattro tipi.

**Precedenza quando due skill si contraddicono**: brief > skill di stile >
`design-taste`.

## 5. Verifica misurata, non a occhio

1440×900 e 375×812, più i bordi di ogni media query: una voce in più in nav
rompe nella banda stretta in mezzo, non ai due estremi. Overflow zero,
contrasti AA, console pulita. **Uno screenshot conferma, non dimostra**: il
pannello dipinge solo il primo frame.

## 6. Finish review di impeccable — non è opzionale

È il passo che ha pagato di più: diciotto didascalie false, un bollino prezzo
mancante, promesse scritte a nome di un cliente che non le aveva mai fatte.
**Le didascalie si scrivono guardando la foto, non il nome del file.**

## 7. Pubblicazione e chiusura

Netlify, e i **tre sbarramenti restano** finché il sito non è suo. Li toglie il
direttore, tutti e tre insieme, il giorno della consegna.

Poi la riga in `01-Coding/registro-interventi.md` — chi, quando, progetto,
repository, database — e push.

## Dove questo processo NON vale

OperO e DenkiShift. Sono gestionali, e nei loro repo comanda il `CLAUDE.md` del
repo. Là si usa `impeccable` per l'audit e `ui-ux-pro-max` per un valore
preciso, e basta.
