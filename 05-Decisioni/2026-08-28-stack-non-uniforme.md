---
type: decisione
data: 2026-08-28
progetto: azienda
source: claude
stato: aperta
---

# Lo stack non è uniforme — decisione aperta

> [!note] Nota generata da Claude
> Questa non è una decisione presa da Nicola o Patrick: è un rilievo che ho
> fatto leggendo i repo, messo qui perché diventi una decisione **vostra**.
> Finché resta `stato: aperta`, non è una convenzione e non va applicata.

## Il rilievo

Al 28 agosto 2026, DenkiCode ha **cinque basi di codice e cinque stack**:

| Progetto | Stack |
|---|---|
| [[opero]] | Vite 8 · Tailwind 3 · React Router · TanStack Query · oxlint · commenti inglese |
| [[denkishift]] | Next 16 · Tailwind 4 · App Router · Server Actions · eslint · commenti italiano |
| [[sito-albybike]] | SPA React + Vite |
| [[cococat]] | HTML puro, zero build |
| [[sito-dropout]] | Google AI Studio |

Anche i due gestionali, che fanno cose simili, non condividono né il build né
la versione di Tailwind né il modo di scrivere sul database.

## Perché oggi non è un problema

Un mese di attività, un solo sviluppatore, ogni progetto nato in un momento
diverso con lo strumento più veloce disponibile allora. **È la scelta giusta per
partire**, e riscrivere qualcosa oggi sarebbe tempo tolto ai lead.

## Perché lo diventa

L'obiettivo dichiarato è **20 clienti a canone di manutenzione**
([[obiettivi-6-mesi]]). Un canone è la promessa di poter mettere le mani su un
sito fra otto mesi, in fretta. Se ogni sito è un ambiente diverso, ogni
intervento comincia con mezz'ora di riscoperta — e il canone da ricavo diventa
costo.

Lo stesso vale per Claude: ogni sessione su un progetto diverso riparte da capo.

## Le due domande da decidere

**1. Qual è lo stack standard del prodotto A (siti vetrina)?**
Il candidato è **HTML + Tailwind statico**, come [[cococat]]: un sito vetrina
non ha stato né login, si pubblica in cinque minuti, si carica all'istante e si
indicizza meglio di una SPA. `albybike.com` oggi è una SPA React — più lenta e
più fragile del necessario per quel che fa.

**2. Qual è lo stack standard per un gestionale nuovo?**
Next 16 o Vite? La risposta pratica è probabilmente *quello di DenkiShift*,
perché è il più recente e ha i test — ma va detto, non lasciato al caso.

**Non è in discussione riscrivere OperO.** Quello che è fatto resta com'è.

## Stato

**Aperta.** Da decidere e chiudere con una nota nuova in `05-Decisioni/`.

## Collegamenti

[[stack]] · [[convenzioni]] · [[obiettivi-6-mesi]] · [[prodotti-e-listino]]
