---
type: progetto
riga: Bozza sito Marta Cesena, fotografa a Piacenza: giro 1 «Dove ti porto» (la carta della provincia dai dati OSM con i posti veri dei suoi servizi), Astro con GSAP, 26/10/2026.
status: attivo
client: martacesena
stack: [astro, gsap, netlify]
started: 2026-10-26
deadline: TODO
updated: 2026-10-26
source: claude
tags: [sito, fotografa, piacenza, astro, gsap]
---

# Sito Marta Cesena — giro 1 «Dove ti porto»

Bozza di sito vetrina per [[martacesena]], fotografa a Piacenza (lauree, ritratti, coppie, battesimi, maternità,
eventi). Nicola il 26/10/2026: «nuovo sito, fallo seguendo le stesse istruzioni che ti ho dato per gli ultimi siti».

**Cartella**: `~/lavoro/martacesena-site`, ramo `main`, nessun remoto per ora.
**Online**: sito Netlify `martacesena` (id `85cff1b5-296e-491b-a298-80bbd8c16845`, team denkicode), indirizzo
<https://martacesena.netlify.app>. Si ripubblica con `npm run build` e
`netlify deploy --dir dist --prod --no-build --site 85cff1b5-296e-491b-a298-80bbd8c16845` (sempre con `--site`: la
CLI di questa macchina è collegata a un altro progetto).
**Memoria tecnica nel repo**: `PRODUCT.md` (verità di prodotto), `direzione/DIREZIONE.md` (il mondo),
`direzione/contratto.md` (il DOM fra gli operatori), `direzione/{scheletro,mappa,pagina,motion,skill-digest}.md` (i
rapporti), `raccolta/RACCOLTA.md` (Instagram, Linktree, Maps, Facebook letti il 26/10), `riferimenti/foto.md` (una riga
per foto, scritta guardandola), `riferimenti/concorrenti.md`.

## Il mondo

Marta non ha uno studio: i suoi set sono la provincia di Piacenza, e i geotag dei suoi post lo dicono (Palazzo
Farnese, Collegio Morigi, Cattolica, Grazzano Visconti, Rivalta sul Trebbia, Castell'Arquato, Vigoleno, Villanova
sull'Arda, Fiorenzuola, Gambaro). La pagina risponde alla prima domanda di chi le scrive: «dove facciamo le foto?».

- **La carta della provincia** è generata da uno script dai dati di OpenStreetMap (confine, fiumi, coordinate dei
  luoghi) e dai km d'auto di OSRM: nessun tratto disegnato a mano. È la scelta che rispetta la regola di Nicola sui
  disegni (12/10, 20/10, 23/10): un dato reso dal codice, come le isoipse di Groavel.
- **Apertura «la carta»**: il confine si disegna, i luoghi spuntano, il nome sale per righe, la carta vola nella sua
  sede nell'hero (Flip), 1,8 s al massimo.
- **Spina «Dove ti porto»**: da computer la carta è sticky, il percorso fra i luoghi si traccia allo scroll e la foto
  della tappa cambia in cross-fade; otto tappe dalla città ai borghi alle feste. Palazzo Farnese è l'unica tappa su
  campo notte, perché le sue tre foto con luce da studio sono su nero. Sul telefono ogni tappa è un blocco con uno
  schema suo e la miniatura della carta.
- Poi «Cosa fotografo» (sei schede con le sue frasi verbatim, carosello sul telefono), «Come si prenota» (DM, modulo,
  il posto e l'ora della luce), «Chi sono», contatti su notte.
- **Palette**: carta `#F4F1EA`, carta scura, notte `#17120F`, un accento solo, la terracotta dei mattoni di Piacenza
  `#B4503A`. **Font**: Instrument Serif, Hanken Grotesk, IBM Plex Mono.
- **Metodo**: Fable dirige e non costruisce. Quattro Sonnet in parallelo per la raccolta (Instagram, Linktree, Maps,
  Facebook e foto), i concorrenti al volo, lo scheletro Astro e il digest delle skill; la carta su un quinto Sonnet;
  pagina e motion su due Opus in parallelo con un contratto di DOM. Il limite d'uso ha fermato la raccolta alle 17:58
  e il lavoro è ripreso alle 20:01.

## Stato

**Giro 1 in costruzione** (26/10/2026, sera). Misure, verdetto e pubblicazione: `TODO` a fine giro.

## Da chiedere a lei (via Patrick)

Elenco in `PRODUCT.md`: prezzi o «a partire da»; durata, numero di foto e consegna; studio o esterni; WhatsApp; mail;
matrimoni da titolare o seconda; la sua storia; foto originali e liberatorie; dominio.

## Collegamenti

[[martacesena]] · [[processo-siti]] · [[direttive-siti]] · [[sito-whitelilium]] · [[sito-groavel]]
