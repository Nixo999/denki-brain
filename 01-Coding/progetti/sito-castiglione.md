---
type: progetto
status: in-pausa
client: castiglione-furniture
stack: [html, gsap, netlify]
started: 2026-08-30
deadline: TODO
updated: 2026-09-07
source: claude
valore: TODO
incassato: 0
---

# Sito Castiglione — la falegnameria di Bronte, nata da Instagram

Sito vetrina non commissionato per [[castiglione-furniture]], costruito il
30 agosto 2026 dai contenuti veri del loro profilo Instagram. È **materiale
per Patrick**, non un lavoro venduto: loro non ci hanno chiesto niente.

Questa nota è nata il 7 settembre 2026, otto giorni dopo il lavoro: il
progetto esisteva solo come righe del [[registro-interventi]] e dieci wikilink
che non puntavano a niente. I fatti qui sotto vengono da quelle righe e dalla
daily [[2026-08-30-sito-castiglione]].

## Com'è fatto

Un solo `index.html` statico, niente build. Scroll-telling scuro con GSAP 3.13
da CDN, sipario in apertura, hero didone Playfair Display 900, capitoli con
parallax, galleria orizzontale pinnata (su touch diventa scroll-snap),
count-up, marquee. Palette oliva e carta presa dai loro lavori. La motion è
additiva: senza CDN o con `reduced-motion` la pagina resta completa.

Contenuti e 31 foto estratti da `@castiglione_furniture` con lo scraper
**Apify** agganciato a Claude Code, primo uso vero di quello strumento.

## Dove sta

| Cosa | Dove |
|---|---|
| Cartella | `Desktop/castiglione-site` (PC di Nicola) |
| Repository | `vetrina_castigliano_furniture`, push di `master` su `origin/main` |
| Database | nessuno, è statico |
| Hosting | Netlify dichiarato come destinazione |

## Aperto

- ⬜ **Pubblicato davvero?** Il registro dice «il sito va online» e destinazione
  Netlify, ma non c'è una riga che confermi il deploy fatto. `TODO` da
  verificare prima di dire a chiunque che è online.
- ⬜ Se è online senza essere loro, valgono i tre sbarramenti anti-indicizzazione
  di [[netlify]]: una bozza col marchio di un'azienda che non è cliente non deve
  finire su Google.
- ⬜ Contatti: il profilo non pubblica né email né telefono, il sito punta a
  Instagram e Facebook. Da sostituire coi recapiti veri al primo contatto.
- ⬜ Mai visto su browser vero né su telefono fisico: solo misure su viewport
  emulati.

## Cosa ha lasciato al resto

Lo «schema Castiglione» è diventato il modo standard di fare una bozza vetrina
da Instagram: scraping, foto scaricate subito, scroll-telling scuro, verifica a
misure. Riusato su [[sito-ngbarber]] e [[sito-fiftynine]]. Le trappole tecniche
trovate qui stanno in [[trappole]].

## Collegamenti

[[castiglione-furniture]] · [[trappole]] · [[netlify]] · [[registro-interventi]] ·
[[2026-08-30-sito-castiglione]] · [[processo-siti]]
