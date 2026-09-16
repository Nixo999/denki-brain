---
riga: In denki-agents viene prima la parte che fa i siti - Nicola ci vuole spostare la produzione dei siti, a breve.
type: decisione
data: 2026-09-16
progetto: denki-agents
updated: 2026-09-16
source: claude
stato: presa
---

# In denki-agents viene prima la parte che fa i siti, perché la produzione dei siti si sposta lì

## Il contesto

16/09/2026, costruzione della fase 1 di [[denki-agents]], al punto 2 del prompt
(lo schema). Oggi i siti si fanno in sessioni di Claude Code col
[[processo-siti]].

## La decisione

Nicola: «voglio fare in modo che a breve sia pronta soprattutto la parte che fa
i siti, che voglio spostare lì la produzione».

## Cosa si è scartato

Niente di dichiarato.

## Conseguenze aperte

- La fase 1 resta la prima cosa: il `CLAUDE.md` del repo non fa costruire la
  fase 2 finché il gateway non è chiuso.
- In fase 1 `esegui()` accetta solo testo, e la spec fa entrare le immagini
  «col primo task visivo». `revisione_visiva` le immagini le deve vedere.
- `TODO`: quanto della parte siti copre `docs/spec-fase-2.md`, che copre gli
  otto agenti chiesti da Patrick. Non riletta il 16/09.
- `TODO`: gli agenti di Patrick vengono dopo i siti o insieme.

## Collegamenti

[[denki-agents]] · [[processo-siti]] · [[2026-09-16-cervello-denki-agents]]
