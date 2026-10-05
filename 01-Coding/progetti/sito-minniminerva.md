---
type: progetto
riga: Bozza sito Minerva Esposito, make-up artist ad Alessandria. Online dal 04/10; giro 2 bocciato il 05/10 (non è nel suo stile sposa), si rifà la direzione.
status: attivo
client: minniminerva
stack: html-css-js
started: 2026-10-04
deadline:
updated: 2026-10-05
source: claude
verificato: 2026-10-04
tags: [sito, bozza, make-up, sposa, alessandria, instagram]
---

# Sito Minerva Esposito — bozza, Alessandria

Cartella `~/lavoro/minniminerva-site`, dallo starter. **Repo solo locale**, 14
commit, nessun remote. **Online su <https://minervaesposito.netlify.app>** dal
04/10 (progetto `minervaesposito`, id `b65feb44-f910-459f-a359-89fec5fcd600`,
team `denkicode`). Il deploy l'ha lanciato Nicola: a Trevis lo blocca il
classificatore dell'auto mode. La cliente sta in [[minniminerva]].

Nicola, 04/10: «deve essere strutturato e fatto con un design che stupisca ma
che sia molto utile, perché la ragazza è titubante sull'utilità».

Metodo: raccolta del direttore (Fable), concorrenti su Sonnet
(`COMPETITOR.md`), direzione e costruzione sullo stesso operatore Opus, due giri.

## Giro 2 bocciato (05/10): «non è per niente nello stile della sposa»

Nicola: «questo sito fa cagare, non è per niente nello stile della sposa della
cliente. dagli più personalità, e cambia completamente l'animazione all'avvio».
Il mondo «Due occhi» (due tondi con gli occhi, grigio `#EEF0EF`, Jost) era
un'idea concettuale e fredda. **La falla era nella raccolta**: le otto
copertine delle sue storie in evidenza sono tutte bianco su bianco (seta, rose,
petali in rilievo, brillantini, calligrafia) e non le avevamo guardate. Ora
stanno in `RACCOLTA.md` e in `sorgenti/_copertine-evidenza.jpg`. Si è tornati
alla direzione: tre mondi nuovi nel suo stile, contenuti e pezzi utili restano.

## Cosa fa di utile, cioè cosa Instagram non fa

- **La richiesta che compone il messaggio** (servizio, data, ora, luogo,
  persone, prova, stile, note): «Copia e apri Instagram» lo copia e apre la
  chat. WhatsApp è cablato e nascosto: il numero va nella costante `WHATSAPP`
  in testa a `assets/sito.js`.
- Sei percorsi, sette domande con risposta, il triangolo Torino–Milano–Genova.
- `<title>` e JSON-LD per «truccatrice sposa Alessandria», dove su Google non
  c'è il sito di nessuna truccatrice. Anteprima del link (`og.jpg`).

## Verificato il 04/10

- `controlla-sito.py` 8/8, `controlla-slop.py` 0 blocca e 3 avvisi,
  `controlla-testo.py` 0/0. Overflow zero a 375, 900 e 1440.
- Catture a 375 e a 1440 **guardate dal direttore** nei due giri; la richiesta
  provata dal direttore nel pannello a 375: il messaggio esce completo.
- **Online, con `curl` sul deploy `6ac234760593faba148f36ac`**: HTTP 200,
  `x-robots-tag: noindex, nofollow`, `robots.txt` con `Disallow: /`, `meta
  robots` in pagina; RACCOLTA, MONDO, MONDI, PRODUCT, DESIGN, COMPETITOR,
  `sorgenti/`, `catture/`, `.impeccable/` rispondono 404; `og.jpg` 200. Badge
  «Powered by Netlify» spento dall'API. Pagina viva guardata a 375: console
  pulita, overflow zero, nessuna foto rotta.
- **Non verificato**: copia negli appunti e apertura di Instagram su un
  telefono vero; Safari iOS; il tocco sull'occhio l'ha provato l'operatore, non
  il direttore; a 2x da computer il ritaglio dell'occhio è un po' morbido
  (sorgente 717 px).

## Come si pubblica

Solo i file pubblici: `catture/` pesa 321 MB e il CLI caricherebbe tutto.

```bash
cd ~/lavoro/minniminerva-site && rm -rf /tmp/pubblica-minerva && mkdir /tmp/pubblica-minerva && rsync -a --exclude '*.json' index.html robots.txt netlify.toml assets /tmp/pubblica-minerva/ && cd /tmp/pubblica-minerva && netlify deploy --prod --no-build --dir . --site b65feb44-f910-459f-a359-89fec5fcd600
```

Dopo ogni deploy: tre sbarramenti con `curl`. Prima del DM: link da un iPhone.

## Da chiederle

Elenco intero in `MONDO.md`. I primi: file del logo, numero WhatsApp, un prezzo
di partenza, quando si fa la prova, se lavora a domicilio (oggi è in pagina),
consenso su recensioni e foto delle clienti.
