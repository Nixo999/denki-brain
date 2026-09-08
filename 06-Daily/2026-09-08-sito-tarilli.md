---
type: daily
data: 2026-09-08
source: claude
tags: [daily, sito-osteria-tarilli, frontend, impeccable]
---

# 8 settembre 2026, sera — «pizzeria Tarilli» che è un'osteria

Nicola ha chiesto un sito per «pizzeria Tarilli, cercali su Instagram»,
con «un sacco di animazioni» e «pizze che si muovono e fluttuano».

## Il rilievo prima di tutto

**Non è una pizzeria.** È [[sito-osteria-tarilli|Osteria Tarilli]] a Comano,
riga della lista Ticino del 7 settembre: bio, logo e dodici caption dicono
«cucina italiana contemporanea», pasta a mano, brunch, aperitivo. Di pizza
non c'è una riga. Nel sito fluttuano i loro piatti veri: cavatelli, tortelli
di burrata, parmigiana, arrosto, tortino, il tagliere dell'aperitivo.
Mettere pizze inventate sopra il marchio di un lead è il danno fatto prima
della vendita.

## Cosa si è trovato senza login

Il profilo pubblico dà 2.055 follower e le prime dodici anteprime a 640 px.
La bio troncata («🚗 35…») si legge intera nel `meta description` della
pagina; le caption si leggono dagli `og:title` di ogni post con `curl`. Da
lì: 35 parcheggi, telefono, email, indirizzo (Via Ronco Nuovo 2, non il 12
di HappyCow), brunch CHF 39/15 con 50 posti, aperitivo per due CHF 23,
Giuseppe e i 46 anni. Gli orari vengono da HappyCow e restano `TODO`.

## Il processo, passo per passo

Tutti i passi di [[processo-siti]], con due buchi dichiarati: lo script di
ricerca di `ui-ux-pro-max` non esiste al percorso che la skill indica
(passo 4 saltato), e nessun generatore di immagini (passo 6 saltato,
code-led in impeccable).

Impeccable: `PRODUCT.md`, seed **`b6c92fb4`**, indice assegnato **7 su 7**
della mia lista: «il passe della cucina», la pagina come tragitto del piatto
dal passe al tavolo. Pagina di decisione servita nel pannello e **lasciata
senza risposta per quattro minuti**: si è proceduto con l'assegnata, il
server è rimasto su. Sei sfidanti del catalogo, tutti declinati tranne il
folio botanico (competitivo su chiarezza): da ognuno un'imposizione,
scritta nel contratto di direzione.

Identità: la loro. Crema, verde bottiglia, oro, rosso mattone, didone.
Il crema è quello che `design-taste` vieta come default: qui non è un
default, è la locandina del cliente.

## Quello che ha morso

- **L'oro sul crema è a 2,4:1.** Bello in locandina, illeggibile come testo
  a 11 px. Due token: `--oro` per i filetti, `--oro-testo` (#7a6220,
  4,97:1) per le parole.
- **La nav sforava di 95–288 px fra 641 e 899**, e la classe `.nascondi-m`
  non esisteva. Misurata su nove larghezze prima di dirla a posto.
- **Un tween GSAP in attesa è overflow.** `gsap.from` con `x:90` sui piatti
  della baseline li teneva 90 px a destra finché lo ScrollTrigger non
  partiva, e la pagina scrollava di lato. `overflow-x:clip` sulle sezioni, e
  la rivelazione è passata a CSS con il fallback a tempo.
- **Il conteggio del prezzo è un prezzo falso.** La cattura headless ha
  fotografato «CHF 34». Tolto.
- **Le catture a tutta pagina con `vh`**: una finestra alta 6.800 px allunga
  l'hero a 6.800 px. Ora l'hero misura in `--vh` e `?cattura` la fissa.

## Verificato, e non verificato

✅ Overflow zero a 375, 641, 761, 899, 901, 1024, 1100, 1101, 1440. CTA
nel viewport a 1440×900 (fondo a 758 px) e a 375 (550 px). Console pulita,
Bodoni Moda e Karla caricati, 17 immagini su 17 rispondono 200. Catture
headless con Brave a 1440×900, 390×844 e a tutta pagina.

✅ **Online: <https://tarilli.netlify.app>.** Nicola ha detto «mettilo su
netlify», ha autorizzato il login nel browser, il CLI ha creato il sito e
fatto il deploy; sbarramenti verificati sul sito vivo (`x-robots-tag`, meta,
`robots.txt`).

✅ Finish review: otto punti, applicati e ripushati (`83dd71a`), dettaglio
in [[sito-osteria-tarilli]]. Il punto vero l'ha visto Nicola dal telefono
prima del reviewer: un piatto copriva «Cosa c'è oggi». Causa: piatti ancorati
al fondo dell'hero mentre il testo cresce dall'alto, e su un viewport basso si
incontrano. Sotto i 640 i piatti stanno in una striscia in flusso dopo il
bottone. Nel farlo, la flex column aveva ancora `align-items:center` dalla
griglia e la striscia era larga zero: i piatti partivano tutti dal centro.

⬜ Orari mai confermati dal titolare. ⬜ Safari su iPhone mai provato.
⬜ Il sito Netlify non è collegato al repo: un push non ripubblica.

## Collegamenti

[[sito-osteria-tarilli]] · [[processo-siti]] · [[trappole]] ·
[[registro-interventi]] · [[2026-09-07-instagram-ticino-ristorazione]]
