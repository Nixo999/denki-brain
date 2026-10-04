---
type: progetto
riga: Bozza sito Minerva Esposito, make-up artist ad Alessandria - mondo «Due occhi», richiesta che compone il messaggio. In locale, deploy da lanciare.
status: attivo
client: minniminerva
stack: html-css-js
started: 2026-10-04
deadline:
updated: 2026-10-04
source: claude
verificato: 2026-10-04
tags: [sito, bozza, make-up, sposa, alessandria, instagram]
---

# Sito Minerva Esposito — bozza, Alessandria

Cartella `~/lavoro/minniminerva-site`, dallo starter. **Repo solo locale**, 14
commit, nessun remote. Progetto Netlify **creato e vuoto**:
`minervaesposito.netlify.app` (id `b65feb44-f910-459f-a359-89fec5fcd600`, team
`denkicode`). ⚠️ **Il deploy non è partito**: il classificatore dell'auto mode
l'ha bloccato il 04/10, lo lancia Nicola. La cliente sta in [[minniminerva]].

Nicola, 04/10: «fallo ispirandoti per bene alla loro personalità e fai una buona
ricerca sui competitor per cosa scrivere di utile nel sito, fallo per bene
soprattutto da telefono e anche da pc, deve essere strutturato e fatto con un
design che stupisca ma che sia molto utile, perché la ragazza è titubante
sull'utilità».

## Il metodo

Raccolta del profilo dal direttore (Fable) nel pannello: 12 post, 40 foto sopra
i 1080 px. Concorrenti su **Sonnet** (`COMPETITOR.md`, 69 KB). Direzione e
costruzione sullo **stesso operatore Opus**, due giri. Il direttore ha letto
`MONDI.md`, il copy e le catture.

## Il mondo: «Due occhi» (`MONDO.md`, seed `009985d9`)

La sua prova trucco a due occhi diversi (Reel dell'11/09) diventa il modo di
chiederle un appuntamento. In testa due tondi con due occhi truccati in due
modi, «Più naturale» e «Più deciso»: toccarne uno preseleziona quella scelta
nella richiesta. Allo scroll gli occhi si aprono sui due volti (pin solo da
768 px in su). Innesti: un capitolo nero «divisa» con lei al lavoro e la toppa
del logo; «5,0» e «7 recensioni» grandi col link a matrimonio.com; domande in
ordine di calendario. Jost, fondo `#EEF0EF`, accento rossetto `#B4536A`.

## Cosa fa di utile, cioè cosa Instagram non fa

- **La richiesta che compone il messaggio**: servizio, data, ora, luogo,
  persone, prova, stile, note. Esce un testo completo; «Copia e apri Instagram»
  lo copia e apre la chat. Il bottone WhatsApp è cablato e nascosto: basta
  scrivere il numero nella costante `WHATSAPP` in testa a `assets/sito.js`.
- Sei percorsi da un selettore compatto, ognuno con la sua prova.
- Sette domande con risposta, quelle a cui i file rispondono già.
- Il triangolo Torino–Milano–Genova con Alessandria al centro.
- `<title>` e JSON-LD scritti per «truccatrice sposa Alessandria», dove oggi
  su Google non c'è il sito di nessuna truccatrice. Anteprima del link
  (`og.jpg`) coi due occhi e il nome.

## Verificato il 04/10

- `controlla-sito.py` 8/8, `controlla-slop.py` 0 blocca e 3 avvisi,
  `controlla-testo.py` 0/0. Overflow zero a 375, 900 e 1440.
- Catture a 375 e a 1440 **guardate dal direttore** nei due giri; la richiesta
  provata dal direttore nel pannello a 375: il messaggio esce completo.
- **Non verificato**: copia negli appunti e apertura di Instagram su un
  telefono vero; Safari iOS; il tocco sull'occhio l'ha provato l'operatore, non
  il direttore; a 2x da computer il ritaglio dell'occhio è un po' morbido
  (sorgente 717 px). Niente è stato verificato online.

## Come si pubblica

Solo i file pubblici, da una cartella di sola pubblicazione: `catture/` pesa
321 MB e `sorgenti/` 44 MB, e il CLI caricherebbe tutto.

```bash
cd ~/lavoro/minniminerva-site && rm -rf /tmp/pubblica-minerva && mkdir /tmp/pubblica-minerva && rsync -a --exclude '*.json' index.html robots.txt netlify.toml assets /tmp/pubblica-minerva/ && cd /tmp/pubblica-minerva && netlify deploy --prod --no-build --dir . --site b65feb44-f910-459f-a359-89fec5fcd600
```

Poi i tre sbarramenti con `curl` (`x-robots-tag`, `robots.txt`, `meta robots`)
e il link aperto da un iPhone prima del DM.

## Da chiederle

L'elenco intero sta in `MONDO.md`. I primi: file del logo, numero WhatsApp, un
prezzo di partenza, quando si fa la prova, se lavora a domicilio (oggi è in
pagina), consenso su recensioni e foto delle clienti.
