---
riga: In denki-agents prima la parte che fa i siti - Nicola ci sposta la produzione e ne descrive il flusso, dal login alla chat per progetto.
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

## Il flusso che vuole Nicola

Nicola, 16/09/2026, subito dopo (refusi corretti, parole sue):

«voglio una schermata sulla piattaforma di accesso a denki agent, che vorrei
fosse su un sito, e io devo avere la pagina progetti, da lì deve esserci
l'elenco di tutti i siti e gli altri progetti attivi, cliccando su uno già
esistente o su crea nuovo, deve aprirsi su uno già esistente la chat con la AI
che si occupa di interfacciarsi con me che conosce tutto su quel progetto, e mi
permette scrivendo a lei di modificarlo, mentre se nuovo mi fa inserire prima il
nome del progetto, e poi subito mi fa le domande per crearlo, la creazione deve
essere fatta tutta in modo autonomo dopo le prime domande a cui rispondo io, e
deve seguire come la facciamo adesso, usando fable e astra gpt6 in combinazione
per fare dei siti bellissimi e che non devono sembrare fatti con ai, infatti
voglio che sia possibile addestrarla dandogli esempi e altro come anche le skill
di claude code, in modo che migliori sempre»

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
