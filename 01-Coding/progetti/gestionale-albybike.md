---
type: progetto
riga: Gestionale dell'officina Albybike - bici dei clienti con scheda tecnica, lavori fatti, promemoria di manutenzione nel gestionale e via mail. Locale, non ancora online.
status: attivo
client: albybike
stack: HTML statico senza librerie, Netlify Functions, Netlify Blobs, Resend, skill stile-apple
started: 2026-10-20
deadline:
updated: 2026-10-20
source: claude
valore: 0
incassato: 0
tags: [gestionale, albybike, officina, stile-apple]
---

# Gestionale Albybike — l'officina di Alby

Richiesta di Nicola del 20/10/2026: un gestionale su un sito a parte rispetto ad
`albybike.com`, dove Alby tiene le bici dei clienti, la data d'acquisto, la
scheda tecnica e i lavori fatti, con un avviso quando tocca la manutenzione:
una mail al cliente e una sezione apposta nel gestionale. Stile di
albybike.com, ma premium, con la skill [[stile-apple]]. Cliente: [[albybike]].

**Repo**: `~/lavoro/albybike-gestionale`, ramo `main`, **solo locale**: nessun
remote, nessun sito Netlify. Come è fatto, come si prova e come si pubblica sta
nel `CLAUDE.md` del repo, che sul tecnico ha ragione lui.

## Stato al 20/10/2026

- 🟡 **Costruito e provato in locale**, non online. `node prova.mjs`: 59/59
  controlli (date, scadenze, API con l'archivio locale di Netlify, mail del
  mattino con un Resend finto). Guardato da Trevis nel browser dell'app a
  1440×900 in scuro e in chiaro e a 375×812: niente scorrimento orizzontale,
  flussi provati (nuova bici, lavoro registrato, segna come avvisato, rinvio
  con Annulla, tema).
- ⬜ Mai visto da Nicola, mai su Safari e su un iPhone vero.
- ⬜ La mail vera non è mai partita: servono `RESEND_API_KEY` e `MAIL_FROM` su
  Netlify e il dominio `albybike.com` verificato su Resend. Le chiavi le crea
  Nicola.
- ⚠️ Primo ingresso `admin` / `admin`: va fatto subito dopo la pubblicazione,
  altrimenti chi conosce l'indirizzo sceglie la password al posto di Alby.

## Scelte

- **Netlify Blobs e non Supabase**: un utente o due al banco, nessuna chiave da
  creare, la stessa strada del [[sito-barbershop-snia]]. Un documento solo per
  tutti i dati; il limite è scritto nel repo.
- **Le scadenze stanno in un file solo** (`modello.js`), letto dalla pagina e
  dalla mail del mattino.
- **Una voce mai fatta parte dal primo giro dopo l'inserimento della bici**: alla
  prima prova una bici di tre anni inserita oggi risultava «scaduta da due
  anni» su ogni voce, e i promemoria si riempivano di falsi allarmi.
- **WhatsApp e telefonata accanto alla mail**: la mail parte solo con il
  consenso del cliente; per gli altri il promemoria resta da avvisare a mano.

## Da chiedere ad Alby

- Se gli intervalli di default gli tornano: spurgo freni e cuscinetti sono stime,
  il resto viene da Fox, RockShox, Bosch e Muc-Off.
- Se vuole il primo tagliando gratuito a un mese su tutte le bici vendute.
- Indirizzo e telefono del negozio per il fondo delle mail.

## Collegamenti

[[albybike]] · [[sito-albybike]] · [[stile-apple]] · [[sito-barbershop-snia]]
