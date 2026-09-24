---
riga: Gli attrezzi con cui si costruisce, e come sono configurati da noi.
type: area
updated: 2026-09-25
source: claude
---

# Strumenti

Gli attrezzi con cui si costruisce, e **come sono configurati da noi**. Non
manuali: quelli stanno online. Qui va la parte che nessun manuale sa — quale
account, quale progetto, quale trappola ci ha già fatto perdere un pomeriggio.

Una nota per attrezzo, in `kebab-case`.

| Attrezzo | A cosa serve | Nota |
|---|---|---|
| Claude Code | scrivere codice e tenere aggiornato il brain | `TODO` |
| Obsidian | leggere e scrivere il vault | vedi `README.md` |
| GitHub | i repo e il vault, account `Nixo999` | `TODO` |
| Supabase | database di [[opero]] e [[denkishift]] | due progetti distinti, non confonderli |
| Netlify | pubblicazione dei siti **e delle bozze da mostrare** | → [[netlify]] |

- `liste-bilanci/` — liste di aziende per **codice ATECO e fatturato**, col telefono verificato: companyreports per il bilancio, Pagine Gialle per il numero (nome identico e stesso comune), distanza da Seveso sull'indirizzo. Due giri, ATECO → telefono (`parallelo.py`) e categoria Pagine Gialle → bilancio (`pg_categorie.py`, `abbina.py`), poi `unisci.py` ed `excel.py`. Scrivono cache accanto a sé: **si copiano in una cartella di lavoro fuori dal vault** e si lanciano da lì. Primo uso → [[2026-09-25-opero-facchinaggio-allestimento]]
- `cattura-fette.mjs` — catture di pagina con **Brave o Chrome** headless via CDP (prende il primo che trova, o `BROWSER_CATTURE`: su alcune macchine Brave non e' installato): fette di viewport a 1440 e a 375 più cinque posizioni dentro ogni pin di ScrollTrigger. Il pannello non fotografa in modo attendibile dopo lo scroll; questo sì. `node 01-Coding/strumenti/cattura-fette.mjs <url> <w> <h> <mobile 0|1> <cartella> <prefisso>`
- `cattura-apertura.mjs` — campiona **l'apertura** del sito: un PNG a ogni millisecondo che gli chiedi, dal `navigate` in poi, headless a 1440. Serve a trovare i fotogrammi vuoti, che nel pannello non si vedono: si contano le tinte distinte di ogni fotogramma, e `1 tinta` vuol dire schermo vuoto. `node 01-Coding/strumenti/cattura-apertura.mjs <url> <cartella> 100,200,300,…`
- `controlla-testo.py` — controlla **il testo**, non la grafica: didascalie che ripetono il testo alternativo o che non dicono niente che la foto non dica, micro-titoli che ripetono la categoria del contenuto sotto («Dove», «Quando», «Telefono»), frasi sopra le 30 parole, Gulpease sotto 55, punti esclamativi fuori dalle citazioni. Esce 1 se qualcosa blocca. `python3 01-Coding/strumenti/controlla-testo.py <cartella>` oppure `--tutti`

Le credenziali **non stanno qui**: vedi [[credenziali]].
