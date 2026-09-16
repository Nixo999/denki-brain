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
- `docs/spec-fase-2.md`, riletta il 16/09: il flusso `bozza_sito` c'è, ma «il
  cantiere resta una sessione Claude Code» guidata da noi, il cruscotto «non
  esce su internet aperto» e l'ordine di costruzione parte dal banco DM di
  Patrick. Il flusso di Nicola cambia tutti e tre i punti, e aggiunge pagina
  progetti e chat per progetto: la spec della fase 2 va riscritta prima di
  costruire.
- Il pezzo difficile è il cantiere autonomo: i siti arrivano a 8/8 da un giro
  agentico che scrive, apre nel browser, misura e corregge. `esegui()` fa una
  chiamata sola.
- L'Agent SDK di Claude, dalla documentazione letta da un agente il 16/09:
  carica le stesse skill di Claude Code, gira con `claude-fable-5-1`, accetta
  tool propri che possono chiamare Astra dal gateway, riprende una
  conversazione dal suo id, vuole la chiave API e non il login di claude.ai.
  Dietro un gateway si mette con `ANTHROPIC_BASE_URL`, ma l'endpoint di
  LiteLLM non è documentato: va provato. Il costo che stima viene dai listini
  suoi, non dal gateway. I permessi limitano i tool: l'isolamento del server
  va fatto a parte.
- Il fallback di `revisione_visiva` su Fable lascia 5.000 token d'ingresso: le
  catture delle pagine lo riempiono subito.
- `TODO`: «su un sito» vuol dire internet aperto con un login serio, o accesso
  solo da una rete privata.
- `TODO`: quali sono gli «altri progetti attivi». Solo siti, o anche OperO e
  DenkiShift, che hanno repo e regole di produzione loro.
- `TODO`: gli agenti di Patrick vengono dopo i siti o insieme.

## Collegamenti

[[denki-agents]] · [[processo-siti]] · [[2026-09-16-cervello-denki-agents]]
