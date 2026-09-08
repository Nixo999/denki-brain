---
type: daily
data: 2026-09-09
source: claude
tags: [daily, sito-albybike, frontend, motion, impeccable]
---

# 9 settembre 2026, notte — Albybike prende un linguaggio di motion

Nicola, dal suo Mac: «riprendi questa conversazione su questo pc», e il
compito di ieri sera dal Mac di Patrick: «rendi ancora più bello, con
animazioni il sito di albybike, usa tutti i plug in e le skill». Là il clone
era fallito per l'account `gh` sbagliato; qui il repo stava già in
`~/lavoro/vibrant-web-foundation`.

## Il rilievo

**È un sito online di un cliente vero, il papà di Patrick.** Quindi
redesign-preserve, non rifacimento: identità, IA e rotte non si toccano.
E il push pubblica: Netlify legge dal repo, la firma di ieri era online in
tre minuti. Il commit `77ead7f` è **locale** finché Nicola non dice di sì.

## Cosa c'era

Motion tutta uguale: `whileInView` fade-up di 20 px con ritardi ad hoc in
ogni componente, niente `reduced-motion` sul JS, niente rete se
l'IntersectionObserver non arriva. Uno scroll cue («Scroll»), due em dash
nel testo Pardus, `bg-black` su una pagina a `0 0% 5%`. E un difetto vero:
nel footer telefono e mail stavano sulla stessa riga per un `</div>` chiuso
nel posto sbagliato.

## Il processo

[[processo-siti]], versione redesign: passo 0 identità del cliente (vince su
tutto), `design-taste` letta per il read (`Redesign - Preserve`, dial
6/7/4), `high-end-visual-design` come unica skill di stile, `brandkit` e
`imagegen` saltate (identità e foto esistono), `emilkowalski-motion` per
ultima, finish review di impeccable in **modalità degradata** (niente comp,
niente PRODUCT.md, subagente sul solo sorgente): 12 punti, 11 applicati.
I tre che valevano di più: il timer di `Reveal` che accendeva tutto sotto
la piega, il motion value e l'`animate` in lite sullo stesso nodo della
foto, `transition-all` che spegneva `hover-lift` su due card di pagine non
toccate.

## Cosa c'è ora

Un vocabolario (`src/lib/motion.ts`) ripetuto in Tailwind e nel CSS; un solo
`Reveal`; un solo momento autoriale nell'hero; barra d'avanzamento; nav che
si compatta; hamburger che ruota nella X; dissolvenza fra le pagine con
ritorno in cima. Dettaglio in [[sito-albybike]].

## Misurato

1440×900 e 375×812: overflow 0, CTA a 579 e 487 px, nav su una riga,
contrasti oro 11,5:1 e muted 6,8:1, menu mobile apre e chiude, parallasse a
scroll 700 = scala 1,09 / y 112, card sotto la piega a opacità 1 dopo lo
scroll su scheda visibile. `tsc`, eslint sui file toccati, build ok.

✅ Push su «si pusha». ⬜ Safari su iPhone. ⬜ I due `any` in `CookieBanner` sono di prima.

## Collegamenti

[[sito-albybike]] · [[processo-siti]] · [[trappole]] · [[registro-interventi]]
