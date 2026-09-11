---
type: risorsa
riga: Lo stato di DenkiCode adesso - chi, soldi, cosa e' aperto, cosa e' bloccato. Si legge a ogni sessione, si riscrive a ogni chiusura.
updated: 2026-09-11
verificato: 2026-09-11
source: denkicode
tags: [stato, fatti]
---

# I fatti — stato al 11 settembre 2026

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
- Tutti e tre lavorano e studiano: DenkiCode è il terzo impegno → [[team-e-vincoli]]

## Soldi

- OperO: **2.000 € da incassare** (11/09/2026) → [[sebastian-torres]]
- Albybike: sito online e **mai pagato** (11/09/2026) → [[albybike]]
- Nessuna P.IVA, prestazione occasionale. Nei testi «ricevuta» → [[vincoli-fiscali]]

## Cosa è aperto adesso (11/09/2026)

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

## Cosa è bloccato, e perché

- **La migrazione dello storico di OperO aspetta che qualcuno apra il pannello
  del progetto** (11/09/2026). Piano, mappatura campo-per-campo, SQL del
  censimento verificato contro lo schema vero e script di estrazione sono nel
  repo e pronti. ⚠️ **Non serve nessuna password del database**, e cercarla per
  due giorni è stato un errore mio: su Supabase si genera dal pannello con un
  bottone, serve solo a `pg_dump`, e chi costruisce da dentro Lovable non la
  incontra mai. Dall'editor SQL del pannello il censimento si chiude in due
  minuti; con la `service_role` key l'estrazione prende tutte e 38 le tabelle.
  **Da verificare, ed è l'unica cosa che manca**: se il progetto Lovable di
  `sebapp-bolanos` si apre dall'account di Nicola. Se sì, non c'è più blocco
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
