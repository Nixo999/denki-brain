---
type: progetto
riga: Bozza sito per Soul Ink Torino City (studio tattoo, via Cremona 27/b Torino, Franco Roggia giapponese + Alessandro Audino tradizionale) - mondo «Munewari × cartigli», giro 3 online su soul-ink-torino.netlify.app dal 26/09, 8/8, slop 0, testo 0.
status: attivo
client: soul-ink-torino-city
stack: html-css-js
started: 2026-09-26
deadline:
updated: 2026-09-26
source: claude
verificato: 2026-09-26
tags: [sito, bozza, tattoo, torino, instagram, giapponese]
---

# Sito Soul Ink Torino City — bozza, Torino

Cartella `~/lavoro/soul-ink-site`, dallo starter. Il cliente sta in
[[soul-ink-torino-city]]: studio a due mani, nessun sito, nessuna scheda
Google, nessun contatto in bio. Nicola il 26/09: «nuovo sito da fare sempre
con il metodo nuovo, fallo ispirandoti molto allo stile dei suoi tatuaggi e
fallo molto vivo e delle belle animazioni ad apparizione. analizza i competitor
e dagli molta personalità».

## Il metodo, con più modelli

Come p0t ([[sito-p0t-tattoo]], regola del 24/09 in [[direttive-siti]]):
raccolta e competitor su **Sonnet** in parallelo (`RACCOLTA.md`,
`COMPETITOR.md` nel repo, più la sezione 9 di [[competitor-siti-tattoo]]),
direzione e costruzione su **Opus**, il direttore su **Fable** che legge solo
`RACCOLTA.md`, `MONDI.md` e scrive `PRODUCT.md` e `MONDO.md`.

Raccolta: 39 foto a risoluzione nativa (38 sopra 1080 px, fino a 3024×4016),
15 soggetti distinti, 5 pezzi grandi; la fenice fissata sul profilo esiste solo
come prima seduta a sola linea (sta sul profilo di Franco, non dello studio).
Competitor: 10 siti aperti oggi (6 Torino, 4 specialisti di giapponese):
nessuno usa onde, koi o peonie nella grafica del sito, solo nelle foto; FAQ su
2 siti su 10; prezzi e caparra non li pubblica nessuno.

## Il mondo scelto — «Munewari × cartigli»

Tre mondi proposti (`MONDI.md`): «La Serie» (i 108 eroi di Kuniyoshi, un
foglio per pezzo, assegnato dal tiro), «Munewari» (scelto), «Il Paravento» (il
telaio a maglie davanti a cui Franco fotografa, scartato: a un passo dal muro
di foto). Seed di impeccable `f83da0c6`, candidato 1/7, `--kind pick`. La
decisione per esteso in `MONDO.md`.

**La metafora.** Nel body suit il tatuaggio si ferma lungo una curva sul petto
e lascia libera una striscia al centro. Le due foto fissate in cima al profilo
hanno la stessa composizione, una per mano: due maniche piene e il petto
libero. La pagina è quel corpo: manica sinistra di Franco (archi *seigaiha*
indaco), manica destra di Alessandro (scaglie con filetto oro a puntini), al
centro il petto libero dove si legge.

**La spina, senza pin.** Manica sinistra (i pezzi grandi di Franco) → la linea
del petto (la curva attraversa il cover up: il vecchio arciere diventa la
hannya; le cinque prime sedute a sola linea; la bambola dal grigio al colore)
→ manica destra (i quattro pezzi di Alessandro, il suo numero). In chiusura il
sigillo hanko si stampa sui contatti. Dalla «Serie» restano i cartigli sui
pezzi con la parola loro («free hand», «cover up», «first session»).

**L'apertura.** Emblema al centro su sumi, le maniche crescono dai bordi, le
curve si tracciano in oro, il nome sale nel petto libero. Sotto 0,9 s.

**Quello che il direttore ha cambiato**: `high-end-visual-design` invece di
`minimalist-ui` (gli ultimi verdetti chiedono spessore e vita); il telefono non
è una versione ridotta (le maniche si aprono a polsino in testa a ogni
artista); niente stampe d'archivio; apparizioni solo su titoli, polsini, pezzi
grandi e cartigli.

## Cosa non c'è, e perché

Prezzi, caparra, età minima, orari (Facebook li nasconde dietro login, Maps
non ha la scheda), il CAP (10152 su Maps, 10124 su Facebook), chi fa i
piercing, «Nino» di una recensione del 2021, la fenice a colori, i ritratti
dei due. L'emblema esiste solo a 150 px: ricostruito in SVG e verificato per
sovrapposizione contro l'avatar. Il numero di Alessandro compare solo sulla sua
scheda, come suo.

## I giri, 26/09

1. Costruzione (Opus 5.5): 8/8 al primo giro, emblema in SVG con IoU 0,902
   contro l'avatar, font self-hosted, WebP a 480/800/1200 con Pillow, spina in
   CSS `animation-timeline`. Badge «Powered by Netlify» spento via API.
2. Direttore sulla pagina vera e finish review (Sonnet): hero a 1440 vuota (solo
   le curve su nero) → le due foto dentro le maniche; cartigli con la sola data
   → soggetto; la manica di Alessandro era mostrata due volte (05 = 02); strisce
   fisse ai bordi tolte dopo il verdetto «riga blu a sinistra».
3. Operatore nuovo dopo «da telefono fa cagare, sembra molto una cosa
   economica», «lo sfondo blu così fa schifo», «intendevo anche per il pc»:
   ogni sezione col suo campo (lacca vermiglia per Franco, carta rosa peonia per
   il cover up, verde hannya per le prime sedute, foglio flash per Alessandro,
   indaco notte per come si lavora, washi per dove), scala di spazi
   `--s1…--s6`, niente indaco piatto, niente seigaiha come fondo. Struttura,
   copy, cartigli, emblema, apertura e spina invariati.

## Stato — online dal 26/09/2026

**<https://soul-ink-torino.netlify.app>**, progetto `soul-ink-torino` sul team
`nicola-la-rezza`, deploy dal CLI `--prod --no-build`, repo
`Nixo999/soul-ink-site` (privata, `main`, pushata, `39adf82`). Tre sbarramenti
con `curl`; RACCOLTA, MONDI, MONDO, PRODUCT, COMPETITOR e `sorgenti/` 404.
`index.html` si genera da `sorgenti/lavoro/pagina.src.html` con `costruisci.py`
(fuori da git): si modifica il sorgente, non la pagina.

| Misura | Esito |
|---|---|
| `controlla-sito.py` | **8/8** |
| `controlla-slop.py` | **exit 0**, un avviso sul copy (sezione senza cifra) |
| `controlla-testo.py` | **0 blocca, 0 avvisa** |
| Overflow | **0** a 320, 375, 900, 1440 |
| Contrasto minimo | 4,51 (rosso flash su carta, testo grande); corpo mai sotto 5,2 |
| Apertura | 0,9-1,0 s, rigioca a ogni caricamento, nessun fotogramma a una tinta |
| Altezza documento | 8.289 px a 375, 7.370 a 1440 |
| Primo caricamento a 375 | 521 KB (giro 2), di cui 362 di immagini |
| Token | Sonnet 405k + 97k + 179k · Opus 262k + 496k + 274k · Fable direttore |

`TODO` il verdetto di Nicola sul giro 3; Safari e iPhone veri mai provati; il
DM col link è di Patrick. Le domande per lo studio stanno in
[[soul-ink-torino-city]].

## Collegamenti

[[soul-ink-torino-city]] · [[competitor-siti-tattoo]] · [[sito-p0t-tattoo]] · [[processo-siti]] · [[direttive-siti]] · [[registro-interventi]]
