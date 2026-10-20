---
type: decisione
riga: Prova del 20/10/2026 sul sito di Dog School Piacenza - Astro con isole React per usare React Bits, magic-ui-ux per i token, find-skills.
updated: 2026-10-20
source: claude
data: 2026-10-20
progetto: sito-dogschoolpiacenza
---

# Prova: Astro, React Bits e magic-ui-ux sul giro 2 di Dog School Piacenza

Il 20/10/2026 Nicola ha chiesto di provare sul rifacimento di
[[sito-dogschoolpiacenza]] tre strumenti nuovi per la costruzione dei siti:
il plugin magic-ui-ux, i componenti React Bits e la skill find-skills.

## Cosa si è scelto

- **Astro 5 con isole React.** React Bits è una libreria di componenti React,
  e i nostri siti vetrina sono HTML statico con GSAP. Astro tiene le pagine
  in HTML completo anche senza JavaScript e carica React solo dove serve un
  componente. La configurazione `build.format: 'file'` e
  `build.assets: 'assets'` fa uscire `dist/` con la stessa forma dei siti
  statici, così `controlla-sito.py`, `controlla-slop.py` e
  `controlla-testo.py` girano su `dist/` senza modifiche.
- **React Bits** si usa dentro il sito del cliente: la licenza (MIT con
  Commons Clause) lo permette, vieta solo di rivendere i componenti.
- **magic-ui-ux** serve per estrarre i token dalle schermate di Instagram,
  per assegnare i principi alle sezioni e per la coreografia. La parte che
  genera le schermate usa Google Stitch e non gira.
- **find-skills** ha trovato e fatto installare le skill ufficiali di GSAP
  ScrollTrigger e quella di Astro.

## Cosa resta da decidere

Se dopo il verdetto di Nicola sul giro 2 questi strumenti entrano nel
[[processo-siti]] per tutti i siti, o restano una prova. Finché non lo dice
una persona, il processo non cambia.

## Collegamenti

[[sito-dogschoolpiacenza]] · [[plugin-claude-code]] · [[processo-siti]]
