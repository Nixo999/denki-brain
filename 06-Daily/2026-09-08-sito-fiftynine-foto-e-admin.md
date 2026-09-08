---
type: daily
data: 2026-09-08
source: claude
tags: [daily, sito-fiftynine, frontend, admin]
---

# 8 settembre 2026 — le foto del bar, e il lunedì che chiude alle 19:30

Nicola ha portato una chiavetta («NO NAME») con il materiale del proprietario
del [[sito-fiftynine]] e ha chiesto due cose: **usare quelle foto al posto di
quelle prese da Instagram**, e **una pagina da cui il proprietario possa
cambiarsi foto e menù da solo**.

## Quello che c'era davvero sulla chiavetta

Non foto dei piatti: **le locandine esposte nel locale**. Dodici immagini, tutte
da 1024 px in su, contro i 640 px degli screenshot di Instagram. Sono la fonte
migliore che il progetto abbia avuto finora, e una di loro ha corretto il sito.

- **La locandina degli orari ha chiuso un buco dichiarato.** Nella nota di
  progetto il giorno di chiusura risultava ignoto e il sito prometteva
  «5:30–21:30» e basta. La locandina dice **lunedì 5:50–19:30, martedì–sabato
  5:30–21:30, domenica 7:00–21:30, nessun giorno di chiusura**. Cioè: il sito
  diceva **aperto un lunedì alle otto di sera**. Adesso `ORARI` è una tabella
  per giorno della settimana e la linea del giorno riscrive le ore agli estremi.
- **La lista cocktail passa dai due pannelli veri** al posto della foto a 640 px.
- **Otto locandine di menù del giorno** — pranzo 12 €, primo 9 €, speciale
  12/13 €, pizza 8/9 €, insalata da 8 €, insalata con pollo 10 €, maxi toast
  4,50 €, crea il tuo piatto — sono contenuto che il sito **non aveva**: ne è
  uscito il capitolo `#offerte`.
- **Un trittico di paste, chiaramente stock, l'ho scartato.** Su un locale vero
  una foto stock toglie credibilità invece di darne.
- **Colazione, frittini e gyoza restano di Instagram**: per quelle sezioni sulla
  chiavetta non c'era niente. Vanno chieste al proprietario, non inventate.

## La pagina di modifica: lo store è l'HTML, non un JSON

Su V-BAG lo store è `dati/borse.json` e la pagina lo rende in JS. Qui non
andava bene: **il menù è il contenuto principale**, e con un JSON senza JS
sarebbe una pagina vuota. Quindi lo store sono `index.html` e `menu.html`
stessi — ogni pezzo modificabile sta fra due commenti, si legge con `DOMParser`
e **si riscrive solo quello che sta fra i due**.

Il resto è lo schema di V-BAG, che regge: File System Access API dove c'è,
download dove non c'è, foto rimpicciolita in canvas, niente login perché da lì
non si scrive sul server.

**`prova-admin.html`**, 23 asserzioni: la più importante è che leggere e
riscrivere i listini senza cambiarli lasci i file **identici al byte**. È stata
utile subito — scappare l'apice dritto nel testo riscriveva quarantaquattro
righe di pizze per un prezzo cambiato, e il diff non diceva più niente. Due
funzioni invece di una: nel testo si chiudono solo `& < >`, nell'attributo
anche `"` e `'`.

## Trappole nuove → [[trappole]]

- **`sips` legge le dimensioni trasposte** quando il browser ruota la foto: su
  una locandina dava 733×1100 e il browser mostrava 1100×733, cioè coricata,
  con `sips -g orientation` che rispondeva `<nil>`. L'orientamento si verifica
  nel browser con `naturalWidth`/`naturalHeight`.
- **`sips` non scrive webp**: fallisce in silenzio.
- **Una voce in più in nav non si misura a 1440 e 375**, lì è sempre a posto:
  la quinta voce sforava di 36 px fra 761 e 899.
- **Un mosaico con la prima cella a tutta larghezza lascia un buco** quando le
  celle scendono a due.

## Verificato, e non verificato

✅ Zero overflow a 375, 761, 820, 899, 900, 980, 1280, 1440. 17 immagini su 17
caricate. Console pulita con la motion accesa. 44 pizze intatte dopo i
marcatori. Le tre righe degli orari e i due footer corretti. La mappa dei giorni
(`Sun`→0) controllata contro `getDay()` su sette giorni di fila. `prova-admin`
23 su 23. La pagina di modifica legge 8 foto, 8 locandine, 9 listini.

⬜ **Il ramo `showDirectoryPicker` non è mai stato eseguito**: nel pannello
parte sempre il fallback. Va provato a mano su Chrome da computer.
⬜ **Il lunedì e la domenica non sono stati visti a schermo**: la tabella è
letta con l'indice giusto, ma il render di quei due giorni non è stato forzato.
⬜ Safari su iPhone mai provato.
⬜ **Non pushato**: il commit `8324cd8` è locale. `bartabaccheria59` è pubblico
e il push scrive anche su `fiftynine-site` — aspetta l'ok di Nicola.

## Collegamenti

[[sito-fiftynine]] · [[trappole]] · [[registro-interventi]] · [[sito-vbag]] ·
[[netlify]] · [[processo-siti]]
