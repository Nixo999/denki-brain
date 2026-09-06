---
type: daily
data: 2026-09-06
updated: 2026-09-06
source: claude
progetti: [sito-salone-di-andrea]
canali: [instagram]
---

# 2026-09-06 — Il sito del Salone di Andrea, sul MacBook nuovo

Un blocco solo, chiesto da Nicola in `/nicola`: **«nuovo progetto: sito per
l'account Instagram ilsalonediandrea, come al solito, seguendo il processo e
usando tutte le skill; crea già anche la repository»**. È la riga di Dalmine
della [[2026-09-05-instagram-bg-va|lista del 5 settembre]], quella col
dominio morto.

## Cosa c'è a fine giornata

**Repo `Nixo999/salonediandrea-site` (privato), un commit, pushato.** Un
`index.html`, 16 foto, PRODUCT.md, `netlify.toml` e `robots.txt` con i tre
sbarramenti. Non è online: manca il login Netlify di Nicola, come per le
altre bozze ([[netlify]]). Scheda: [[sito-salone-di-andrea]].

## Le tre cose da tenere

- **Instagram si apre dal pannello del MacBook.** La riga del 5 settembre
  («non si apre da nessuna delle nostre macchine») era vera sul PC Windows e
  sul Mac di Patrick, non qui: profilo, 12 post con didascalia, foto a
  1440 px. L'API `web_profile_info` che aveva funzionato per NG Barber
  risponde 401 (rate limit): la via buona è il pannello, un post alla volta.
  Il resto dei 100 post resta dietro il login.
- **Il dado si ritira quando Nicola appunta.** La direzione assegnata («Il
  rullo», un fotogramma a schermo intero per lavoro) portava scritto il suo
  rischio, «somiglia a Instagram», e si è avverato al primo sguardo:
  «fallo molto più professionale, ispirati a NG Barber, spettacolare». Rifatta
  nella grammatica di `ngbarber-site`. Poi un secondo vincolo: **niente foto
  del titolare come primo sfondo**, al suo posto lo specchio tondo
  retroilluminato del salone disegnato in SVG. Tutto in
  [[2026-09-06-sito-salone-andrea-direzione]].
- **Le catture headless mentono in tre modi diversi**, e ci è andata mezza
  sessione: Chrome headless impone una larghezza minima (~500 px) e taglia il
  mobile; `sips` con `--cropOffset` restituisce un PNG nero; le entrate GSAP
  restano invisibili se nessun frame gira dopo lo scroll. Soluzioni che
  restano nel repo: un iframe da 375 px dentro una finestra larga, un
  ritaglio PNG in Python puro (`.impeccable/review/crop.py`), e l'interruttore
  `?still=1` nella pagina che spegne sipario ed entrate per la verifica.

## Buchi dichiarati

- Lo script di ricerca di `ui-ux-pro-max` non è su questo Mac (c'è solo il
  SKILL.md del plugin): il passo 4 di [[processo-siti]] è andato a tabella.
- La pagina di decisione di impeccable si è chiusa senza risposta: la scelta
  è passata dal tool strutturato, come prevede il riferimento.
- Il vecchio sito è irrecuperabile: Wayback risponde 500 sulla home, nessuno
  snapshot delle sottopagine.
- Finish review di impeccable: `TODO` esito, vedi la scheda del progetto.

## Collegamenti

[[sito-salone-di-andrea]] · [[il-salone-di-andrea]] ·
[[2026-09-06-sito-salone-andrea-direzione]] · [[2026-09-05-instagram-bg-va]] ·
[[processo-siti]] · [[registro-interventi]]
