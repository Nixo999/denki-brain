---
type: risorsa
riga: Lo stato di DenkiCode adesso - chi, soldi, cosa e' aperto, cosa e' bloccato. Si legge a ogni sessione, si riscrive a ogni chiusura.
updated: 2026-09-14
verificato: 2026-09-14
source: denkicode
tags: [stato, fatti]
---

# I fatti — stato al 14 settembre 2026

**Questo file si riscrive, non si accumula.** È lo stato di adesso: quando un
fatto cambia si sostituisce la riga, non se ne aggiunge una sotto. La storia
sta in `05-Decisioni/` e nelle daily.

Ogni riga è marcata: **senza data** = non scade; **(data)** = vero a quel
giorno e da ricontrollare; **→** = non vive qui, vive là.

## Chi

- Patrick Sappa, 21, unica voce commerciale. **Non scrive codice e non usa il
  terminale**: quando lavora lui, il brain fa tutto da solo.
- Nicola Larezza, 22, lead dev. Scrive tutto il codice.
- Giulia Venneri, 21, cold call a provvigione. **Non ha accesso al vault.**
  **Unica persona al telefono** da oggi: ha chiuso le sue 131 righe in due
  settimane (13/09/2026), il reso conto lo deve ancora girare Patrick.
- Gabriele ed Edoardo **fuori** (13/09/2026): «non se la sentono», zero numeri
  chiamati in quattordici giorni. Non si contano nei piani
  → [[2026-09-13-caller-fuori]]
- Tutti e tre lavorano e studiano: DenkiCode è il terzo impegno → [[team-e-vincoli]]

## Soldi

- OperO: **2.000 € da incassare** (11/09/2026) → [[sebastian-torres]]
- Albybike: sito online e **mai pagato** (11/09/2026) → [[albybike]]
- Nessuna P.IVA, prestazione occasionale. Nei testi «ricevuta» → [[vincoli-fiscali]]

## Cosa è aperto adesso (13/09/2026)

- **Le 87 righe di Gabriele ed Edoardo passano a Giulia** — 27 siti/e-commerce,
  30 DenkiShift, 30 indagine, zone Groane e Vimercatese, siti riverificati a
  macchina il 13/09 → [[2026-09-13-liste-giulia-groane-vimercatese]]
- **Il reso conto di Giulia non è ancora arrivato**: senza quello le sue
  chiamate, risposte e appuntamenti restano `TODO` in [[metriche]], e oggi è
  l'unico canale che ha girato davvero
- **Mikuma Dogs** rifatto dal passo 2 col metodo nuovo e online su
  `mikumadogs.netlify.app` (11/09 sera, giro 7 «il bianco e il nero»). Nicola:
  «per il resto mi piace molto». Logo vero a 480 px, il file buono lo chiede
  Patrick. Safari su iPhone non provato → [[sito-mikuma-dogs]]
- **Lobidù** e **Da Caterina** online come bozze: zero grafica inventata,
  nessun racconto allo scroll. Sotto il livello.
- Bozze mai proposte: DSI, Atelier Selva, Salone di Andrea, Nails Mania,
  Tarilli, Fiftynine.
- **Castiglione** e **NG Barber** fermi. Il sorgente di NG Barber sta su una
  repo **pubblica**.
- **Pinkploy** (onicotecnica, Brescia) online su `pinkploy.netlify.app` (14/09),
  mondo «lo spessore», 8/8. Nicola ha bocciato solo l'hero, la correzione è
  online. Il DM col link è di Patrick, lei ha già risposto «si prova mandami»
  → [[sito-pinkploy]]

## Cosa è bloccato, e perché

- **La migrazione dello storico di OperO non si fa piu'** (13/09/2026). Seba:
  «non e' richiesta alcuna procedura automatizzata di migrazione per i dati
  storici», settembre lo inserisce a mano lui, e di giugno-agosto vuole solo un
  **report da consultare**. OperO 2 parte vuoto: trasformazione e caricamento
  del piano non servono, **e il blocco al go-live non c'e' piu'**. Il report lo
  scrive `strumenti/report-mesi.mjs` dai JSON dell'estrazione. ⚠️ **Manca solo
  la chiave**: `OPERO1_SERVICE` da Settings → API del pannello di OperO 1,
  oppure un login di segreteria. **La digita una persona**, non Claude
  → [[opero]]
- **DenkiShift non è installabile in produzione.** Dimostrabile, non vendibile
  con una data → [[denkishift]]
- **La produzione resta fuori** su tutti e due i prodotti. Patrick applica lo
  schema solo in sviluppo → [[modifiche-al-database]]
- **Le credenziali non entrano nel vault** e non le digita Claude → [[credenziali]]
- Il collo di bottiglia è la **generazione lead**, non il closing → [[generazione-lead]]

## Il livello dei siti

**NG Barber e Fiftynine passano, gli altri no.** Prima di pubblicare:

```bash
python3 01-Coding/strumenti/controlla-sito.py ~/lavoro/<cartella>
```

Quello che è già stato bocciato sta in [[direttive-siti]], e non si ripete.
