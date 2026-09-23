---
riga: Fiftynine - la pagina di modifica pubblica da sola come V-BAG (Netlify Function + commit su GitHub), ma in un commit solo e con la parola d'ordine in sessionStorage.
type: decisione
data: 2026-09-23
progetto: sito-fiftynine
updated: 2026-09-23
source: claude
stato: presa
tags: [decisione, fiftynine, netlify, gestionale]
---

# La pagina di modifica del Fiftynine pubblica da sola

Nicola, 23 settembre 2026, guardando `admin.html` online: «la ho vista ma non fa
quello che deve [...] e le modifiche devono andare direttamente online, fallo
cosi». Regola scritta nelle [[direttive-siti]].

## Deciso

**La stessa strada di V-BAG** ([[2026-09-16-vbag-gestionale-login]]), che era
già una decisione presa: una Netlify Function (`/api/pubblica`) con
`ADMIN_PASSWORD` e `GITHUB_TOKEN` fine-grained nelle variabili di Netlify,
che committa su GitHub; il commit fa ripartire il deploy. Nessun database,
nessun servizio di identità. Senza le impostazioni risponde 503: fallisce chiusa.

## Dove è diversa da V-BAG, e perché

- **Un commit solo** (Git Data API: blob, albero, commit, ref) invece di un file
  per chiamata. Qui un salvataggio tocca due pagine più le foto: con un commit
  per file partono tre deploy, e fra un deploy e l'altro il sito è mezzo vecchio
  e mezzo nuovo.
- **La parola d'ordine a ogni richiesta, tenuta in `sessionStorage`**, invece di
  un token HMAC di 30 giorni. `index.html` carica GSAP da un CDN, cioè codice di
  altri sulla stessa origine della pagina di modifica: `sessionStorage` non lo
  legge nessun'altra scheda, un token in `localStorage` sì, per 30 giorni. Il
  costo è riscriverla a ogni scheda nuova; sul telefono la riempie il
  portachiavi (`autocomplete="current-password"`).
- **`GITHUB_REPO` obbligatorio**, senza un valore di ripiego: il sito ha due repo
  su GitHub, e scrivere su quello sbagliato vorrebbe dire pubblicare dove Netlify
  non guarda.
- **La parola d'ordine è un permesso limitato**: fuori dai pezzi marcati le pagine
  devono restare identiche al byte, e dentro non può comparire codice che prima
  non c'era. V-BAG committa un JSON e non ne ha bisogno; qui si committa l'HTML
  che vedono i clienti del bar.
- **Si legge dal repo, mai dal sito**: Netlify rielabora l'HTML che serve (vedi
  [[trappole]]).

## Cosa si è scartato

- Tenere il disco e i download come strada di riserva: è proprio quello che è
  stato bocciato.
- Supabase, Netlify Identity, Netlify Blobs: stesse ragioni di V-BAG.

## Resta a Nicola

Le tre variabili su Netlify (`ADMIN_PASSWORD`, `GITHUB_TOKEN`, `GITHUB_REPO`) e un
nuovo deploy. Il giro vero online non è provato: la funzione è provata con
GitHub finto (`prova-pubblica.mjs`, 30 asserzioni) e con il corpo prodotto dal
browser.
