---
type: progetto
riga: Bozza sito per p0t_tattoo (Ruben, tatuatore anime e cartoon, Collegno TO) - mondo «Rodovetro × Retino», linea → puntinato → colore, Unbounded + Hanken Grotesk. Online su p0t-tattoo.netlify.app dal 24/9, 8/8, slop 0, testo 0.
status: attivo
client: p0t-tattoo
stack: html-css-js
started: 2026-09-24
deadline:
updated: 2026-09-24
source: claude
verificato: 2026-09-24
tags: [sito, bozza, tattoo, collegno, torino, instagram]
---

# Sito p0t_tattoo — bozza, Collegno (TO)

Cartella `~/lavoro/p0t-tattoo-site`, dallo starter. Il cliente sta in
[[p0t-tattoo]]: ha risposto al DM di Patrick del 24/09 e la bozza la vuole su
Instagram.

## Il metodo, con più modelli

Regola di Nicola del 24/09 (in [[direttive-siti]]): stesso processo dei siti
precedenti, più modelli per risparmiare i token settimanali. Raccolta del
profilo e inventario competitor su **Sonnet** (due operatori in parallelo),
direzione e costruzione su **Opus**, il direttore su Fable che legge solo
`RACCOLTA.md` e `MONDI.md`.

## Il mondo scelto — «Rodovetro × Retino»

Tre mondi proposti (`MONDI.md` nel repo): «Scegli il personaggio» (schermata di
selezione di un picchiaduro, scartato: costume, non mestiere), «Rodovetro»
(scelto), «Retino» (innestato). Seed di impeccable `1c0d1160`, candidato 1/7,
`--kind pick`. La decisione per esteso in `MONDO.md`.

**La metafora.** Un fotogramma d'anime è fatto a strati — linea, ombra, tinta
piatta sul rodovetro — e un tatuaggio si fa nello stesso ordine. Il suo feed si
divide così: sola linea, puntinato, colore piatto.

**La spina.** Tre battute in pin, LINEA → PUNTINATO → COLORE, un contatore di
fotogrammi che avanza con lo scroll, il foglio di esposizione come tabella
pratica. Dal COLORE in giù la pagina è coperta dai rodovetri colorati (verde
Zoro, rosso Porco Rosso, giallo Pikachu, le tre carte da settimanale).

**L'apertura.** Foglio coi fori di registro, «p0t» tracciato a contorno, il
rodovetro che lo riempie, il foglio che si alza sui perni. Sotto 0,85 s.

## Cosa non c'è, e perché

Prezzi, caparra, età minima, i suoi giorni in studio, foto dei guariti, il
cognome: nessun dato suo. Le recensioni di K-Ink nominano altri artisti e non
si usano; il 4,9 su 196 compare solo come voto dello studio.

## Come è fatto

Apertura a 0,86 s: foglio coi fori di registro, «p0t» a contorno con lo 0
punzonato, il rodovetro verde che lo riempie, il foglio che sfila. Hero con
nome, «Tattoo Anime & Cartoon · Collegno», una frase, «Prenota su WhatsApp» e i
tre rodovetri dei lavori, leggibile a 1 s. Poi LINEA (Pikachu, Spider-Man,
Amor) → PUNTINATO (Onda, Lanterna, scala di tono 10→80 %) → COLORE (Zoro,
Porco Rosso, Attack on Titan) con il contatore di fotogrammi nella barra
laterale; progetti personalizzati in DM con le tre voci Anime · Cartoon ·
Guariti; la scheda K-Ink su rosa (via Adua 9b, orari dello studio, 4,9 su 196
dello studio, Ruben su appuntamento); prenota su verde col numero; footer.
14 `<svg>` inline, 10 foto ritagliate 1:1, nessuna emoji nel testo (le blocca
`controlla-slop`, deciso il 24/09 sera contro la traduzione del mondo).

**La spina colorata è in CSS** con `animation-timeline: view()`, non in GSAP:
al giro 1 un `scrollTo` a metà pagina lasciava due terzi di viewport bianchi
perché GSAP aspettava eventi di scroll. GSAP resta per contatore e scala.

## I giri, 24/09

1. Costruzione (Opus 5.5): 8/8 al primo giro, ma slop bloccava sulle emoji.
2. Direttore, sulla pagina vera a 1440: schermata bianca a metà pagina, hero
   leggibile solo a 1,5 s, 353 px di rosa vuoto sotto la scheda K-Ink.
3. Finish review (Sonnet, `impeccable-finish-reviewer`): Zoro e Porco Rosso
   erano il sorgente ridimensionato e non il ritaglio stretto; l'alt di
   Spider-Man diceva «ombra» per un cuoricino; commento stantio sul contrasto
   del bottone. Lanterna e Attack on Titan restano larghi: stringerli taglia
   il pezzo.

## Stato — online dal 24/09/2026

**<https://p0t-tattoo.netlify.app>**, progetto `p0t-tattoo` sul team
`nicola-la-rezza`, deploy dal CLI `--prod --no-build`, repo
`Nixo999/p0t-tattoo-site` (privata, `main`, pushata, `5bff752`).

**Tre sbarramenti verificati con `curl` sul permalink del deploy**: `meta
robots`, `x-robots-tag`, `robots.txt` con `Disallow: /`. RACCOLTA, MONDO,
MONDI, PRODUCT e `sorgenti/` rispondono 404.

| Misura | Esito |
|---|---|
| `controlla-sito.py` | **8/8** |
| `controlla-slop.py` | **exit 0**, un avviso voluto (la scala 10–80 %) |
| `controlla-testo.py` | **0 blocca, 0 avvisa** |
| Overflow | **0** a 1440, 1100, 1099, 899, 599, 375, 320 |
| Contrasto minimo | 4,37 sul contatore blu (testo grande); bottone 5,03 |
| Apertura | 0,86 s, nessun fotogramma a una tinta; hero leggibile a 1,0 s |
| Altezza documento | 5.619 px a 1440, 7.624 a 375 |
| Token | Sonnet 105k + 189k + 114k · Opus 188k + 358k · Fable direttore |

`TODO` il verdetto di Nicola; Safari su iPhone non provato; il DM col link è di
Patrick, su Instagram. Le domande per Ruben stanno in [[p0t-tattoo]].

## Collegamenti

[[p0t-tattoo]] · [[competitor-siti-tattoo]] · [[processo-siti]] · [[direttive-siti]] · [[registro-interventi]]
