---
type: decisione
riga: V-BAG - il gestionale di Giulia ha un login vero e pubblica dal telefono via Netlify Function + commit su GitHub. Store a file confermato.
updated: 2026-09-16
source: claude
data: 2026-09-16
progetto: vbag-site
tags: [decisione, vbag, netlify, gestionale]
---

# Il gestionale di V-BAG ha un login, e pubblica da solo

Nicola, 15 settembre 2026: «il suo gestionale deve avere un logon e così è
troppo basico, deve essere più funzionale».

## Deciso

- La password sta in una variabile di Netlify (`ADMIN_PASSWORD`) e la
  controlla una Netlify Function (`/api/borse`) che rilascia un token HMAC di
  30 giorni. Nessun servizio di identità, nessun database.
- Lo store resta il repo (decisione del 7 settembre confermata): la funzione
  committa `dati/borse.json` e le foto con la Contents API di GitHub
  (`GITHUB_TOKEN`, fine-grained, solo quel repo). Il push riparte il deploy.
- Colori e manici sul sito sono disegnati in SVG, non fotografati: le foto
  hanno lo sfondo del negozio.

## Cosa si è scartato

- Supabase: già bocciato il 7 settembre («sono poche borse»).
- Netlify Identity + Git Gateway: deprecati.
- Netlify Blobs: dipendenza npm e store fuori dal repo.
- Password solo lato client: non protegge niente se la pagina non scrive.

## Resta a Nicola

Le due variabili su Netlify. Finché mancano la funzione risponde 503 e non
pubblica nessuno: fallisce chiuso. Il giro vero online non è provato.
