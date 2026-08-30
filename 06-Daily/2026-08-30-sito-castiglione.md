---
type: daily
data: 2026-08-30
updated: 2026-08-30
source: claude
progetti: [castiglione-furniture]
---

# 2026-08-30 — Il sito di Castiglione, nato da Instagram

Primo uso vero dello **scraper Instagram di Apify** agganciato a Claude Code:
profilo e 20 post di `@castiglione_furniture` (Castiglione Falegnameria
Sartoriale, Bronte CT) estratti in due run, 31 foto scaricate in locale, e da
lì un sito vetrina statico in `Desktop/castiglione-site` — un solo
`index.html`, committato (`e0260f8`), **senza remote**: dove pubblicarlo non è
deciso.

L'azienda **un sito non ce l'ha** (campo sito vuoto sul profilo): quello che
esce da qui sarebbe il primo. 940 follower, 30 anni dichiarati, 200+ progetti
nel recap 2023, tre segmenti (ricettivo, residenziale, ville / contract),
collaborazioni con architetti e general contractor. Materiale commerciale già
scritto da loro nelle caption: il sito riusa quello, non inventa.

## Cosa è rimasto scritto strada facendo

- ⚠️ **L'account è `castiglione_furniture`**, furniture in inglese. La ricerca
  utenti con «castiglione forniture» e quattro username italiani indovinati
  hanno dato zero: l'ha risolta uno screenshot di Nicola. Prima di scrapare,
  farsi dare l'handle esatto.
- **Gli URL delle foto Instagram scadono** (firme CDN a giorni): scaricare
  subito in locale, sempre. 31 file in `assets/img/`.
- **Il pannello browser a pane nascosto non consegna gli IntersectionObserver**
  e non fa ripartire il lazy loading: reveal-on-scroll = pagina bianca sotto la
  piega, e gli screenshot dopo scroll fotografano il nulla. Due conseguenze:
  nel sito il reveal ha un **fallback a tempo** (1 s senza callback → tutto
  visibile), e la verifica è passata alle **misure** (`getBoundingClientRect`,
  computed style) su viewport **emulati** con `resize_window`, che funzionano
  anche a pane nascosto.
- Un bug vero trovato misurando: `.nav-links a` batteva `.btn` per specificità
  e il CTA in nav era **verde su verde**. A occhio non si vedeva dal primo
  screenshot.

## Secondo giro: da vetrina piatta a scroll-telling

La v1 non è passata: «il sito più piatto della storia». Il rifacimento
(`8cb10ea`) è scuro, a capitoli, con GSAP 3.13 da CDN, e le dosi vengono
dalla base dati di `ui-ux-pro-max` (che sul PC di Nicola **è completa**, al
contrario del Mac): pattern scroll-storytelling, massimo un pin per pagina,
scrub 0.5-1.5, parallax solo sui layer immagine. Playfair Display 900 come
didone del monogramma CF. Tre cose da riusare altrove:

- **La motion è additiva o non è**: gsap.from + CDN esterno = se il CDN manca
  o c'è reduced-motion, la pagina resta completa. Il sipario ha un timer di
  sicurezza per i tab caricati in background (rAF fermo = sipario eterno).
- **gsap.matchMedia legge il viewport del momento**: a pane nascosto il load
  avviene su una finestra minuscola e i blocchi `min-width` non partono. Non è
  un bug del sito: su browser vero il viewport è giusto dal primo istante.
- Il CTA in nav che wrappa su due righe a 375px si toglie, non si comprime:
  sotto i 640px resta solo quello dell'hero.

## Aperto

- ⬜ Il sito è **locale e basta**: niente remote, niente hosting, dominio non
  discusso. E Castiglione non è (ancora) un cliente: è materiale pronto per
  Patrick, se si decide di proporglielo.
- ⬜ Contatti: sul profilo non ci sono email né telefono → il sito punta a
  Instagram e Facebook. Da sostituire coi recapiti veri se arriva un contatto.
- ⬜ Non verificato su browser vero né su telefono fisico: solo misure su
  viewport emulati e screenshot del primo frame.

## Collegamenti

[[registro-interventi]] · [[prodotti-e-listino]] · [[2026-08-29-interfaccia-denkishift]]
