---
type: progetto
riga: Bozza sito Studio fotografico JPP, Merate. Mondo C «Il libro fustellato», giro 1 online su jppmerate.netlify.app dal 06/10; chiusura su Fable, verdetto di Nicola da avere.
status: attivo
client: jpp-merate
stack: html-css-js
started: 2026-10-05
deadline: 2026-10-06
updated: 2026-10-05
source: claude
verificato: 2026-10-05
tags: [sito, bozza, fotografia, merate, instagram]
---

# Sito Studio fotografico JPP — bozza, Merate

Cartella `~/lavoro/jpp-merate-site`, dallo starter. **Repo solo locale**, nessun
remote, niente online. Cliente: [[jpp-merate]]. La chiamata di Patrick con
Stefania è attesa il 06/10 fra le 17 e le 19: la bozza serve per allora.

## Cosa c'è nella cartella

- `PRODUCT.md`: la verità di prodotto, scritta dal direttore.
- `COPY.md`: il copy frase per frase, impersonale, coi segnaposto `[TRA QUADRE]`
  dove il dato manca. Si inserisce com'è.
- `raccolta/` (fuori da git): `RACCOLTA.md` con le parole loro, i quattro
  pacchetti testuali, 17 recensioni Google, i conflitti tra fonti;
  `foto/MANIFESTO.md` con 30 foto sopra i 1080 px, guardate una per una.
- `MONDI.md`: i tre mondi dell'operatore di direzione (Opus).

## Il materiale, in una riga

Due registri di foto: colore pieno su fondali ocra e terracotta per famiglie e
bimbi, bianco e nero su fondo scuro per maternità e neonati. Colore loro: malva
`#823c78` con crema-oro e pesca. Logo al tratto a 500 px, vettoriale assente.
Concorrenti: [[competitor-siti-fotografi]] (48 siti; in Italia nessuno dà
acconto e disdetta, 3 su 31 i tempi di consegna).

## I tre mondi (`MONDI.md`, seed impeccable `039ca394`)

- **A «Uno, due, tre, stella»**: in studio si scatta giocando a 1-2-3 stella.
  Apertura: la conta su malva, lampo, la silhouette `gm-1` si ferma nitida.
  Malva a tutto campo, Shrikhand + Figtree. Rischio: festa di compleanno.
- **B «Il fondale»**: ogni sezione ha il colore del fondale della sua foto.
  Apertura: scende il rotolo ocra, si accende la luce, due tagli a terracotta
  e nero. Lexend Giga + Lexend. Rischio: dipende dai volti dei bambini.
- **C «Il libro fustellato»**: cartoncini con un foro che si apre come un
  diaframma, linguette come indice. Gabarito + Onest. Rischio: spostabile su
  un altro fotografo per bambini.

L'operatore raccomandava A coi campi di B. **Nicola ha scelto C il 05/10 sera**,
con un verdetto sulle tavole: «però dagli un po di vita», «fatto così come è
un po piatto». Sta in `MONDO.md`: le tavole sono il punto di partenza, il sito
deve avere più spessore e più movimento.

## Le tavole (05/10) — in locale, niente online

Dodici comp in `sorgenti/tela/project`, quattro per mondo: apertura in quattro
battute, apertura animata, telefono, computer. Si guardano col visore:

```bash
cd ~/lavoro/jpp-merate-site/sorgenti/tela && python3 -m http.server 8793 --bind 127.0.0.1
```

Nicola ha fermato la pubblicazione sulla tela Claude Design («non pubblicare 3
siti diversi online», regola in [[direttive-siti]]): le opzioni si mostrano in
locale. Sulla tela privata <https://claude.ai/artifact/CQywDvzNzfnZSJyqEKMj7s>
restano 16 foto e i due loghi caricati prima dello stop, nessuna tavola.
Le foto del visore stanno in `sorgenti/tela/_blob`, fuori da git.

Bocciata il 05/10 la foto della famiglia con la giacca arancio
(`canva-famiglia-colore-2400`): non si usa. In C apre la bambina con la
macchinetta giocattolo.

## I giri

- **Giro 0** (05/10): raccolta e concorrenti su Sonnet, direzione su Opus.
- **Giro 1** (05/10 sera → 06/10 mattina): costruzione del mondo C. Lavoro
  diviso per file per fare in parallelo: `index.html` e apertura su Opus,
  `stile.css` (telefono), `computer.css` (da 1024 px) e il resto della motion
  (`motion.css`, `sito.js`) su Sonnet, chiusura su Fable. Sette stalli a 600 s
  degli operatori, ripresi dal contesto. **Online dal 06/10**: Netlify
  `jppmerate`, id `f6025060-2129-476b-90d4-5d735e9e4af7`, team `denkicode`,
  deploy `6ac4b9497e293b512f4d0f3e` lanciato da Nicola con `./pubblica.sh`
  (a Trevis il classificatore blocca `sites:create` e `deploy`). Tre
  sbarramenti e file di lavoro a 404 verificati con `curl` sul permalink.
  **Verdetto di Nicola dal telefono**: «principalmente va bene», ma l'apertura
  «lagga un pochettino, rendila tutta di un fiato, non lasciare pause tra lo
  scorrere delle pagine bucate» e sulle schede Dolce attesa e Percorso 12 mesi
  «le scritte sotto nell'elenco non si vedono»; poi «smetti di controllare».
  Corretto dal direttore (`d2a7157`) e ripubblicato (deploy
  `6ac4bc858967a5a7513211a7`): sul telefono i cartoncini scorrono via invece
  di girare in 3D, partono ogni 0,25 s sovrapposti, niente `filter`, tetto
  2,2 s; elenco e prezzo bianchi su ardesia e malva.
- **Giro 2, da fare**: i tre controlli (`controlla-sito.py`, `controlla-slop.py`,
  `controlla-testo.py`) non sono mai arrivati a fine corsa, il polish da
  computer non è stato guardato, Safari e iPhone veri no.

## Come si pubblica

```bash
cd ~/lavoro/jpp-merate-site && ./pubblica.sh
```

Copia in una cartella temporanea solo `index.html`, `robots.txt`,
`netlify.toml` e `assets`, poi `deploy --prod --no-build` sul sito per id.
Dopo ogni deploy: i tre sbarramenti con `curl` sul permalink del deploy.

## Da chiedere a Stefania

Liberatoria per i minori nelle foto · prezzi veri (12 mesi 390 o 490 €,
famiglia 280 o 350 €, buono 120 o 315 €) · tempi di consegna · acconto e
disdetta · giorni per il newborn · come si riconosce l'ingresso · ruolo di
Massimo e cognomi · file del logo · foto di stampe, tele e album.

## Non verificato

Storie in evidenza e post oltre i dodici (serve il login) · il video YouTube
«Dentro il perché del nostro lavoro», non trascritto · che la donna con le due
macchine fotografiche sia Stefania.
