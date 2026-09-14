---
riga: denki-agents parte dal gateway verso i modelli - modello, prezzo e tetto di ogni task nel database, mai nel codice.
type: decisione
data: 2026-09-14
progetto: denki-agents
source: denkicode
stato: presa
---

# denki-agents parte dal gateway: modello e prezzo di ogni task stanno nel database

## Il contesto

Nicola, 14 settembre 2026: «voglio creare da adesso questo nuovo sistema per
denkicode». Porta il pacchetto della fase 1 di una piattaforma multi-agente
interna: regole di progetto, spec tecnica, dati per il seed. Il nome lo sceglie
lui: «denki-agents (agenti in inglese)».

## La decisione

1. Si costruisce **denki-agents**: lato Nicola i siti, lato Patrick analisi e
   outreach, un database condiviso come unica memoria, agenti senza memoria.
2. **Si parte dal gateway e solo da quello**: `modelli`, `task_routing`,
   `esecuzioni`, LiteLLM, `esegui()` e una CLI.
3. **Nessun modello e nessun prezzo nel codice.** Cambiare il modello di un
   task è un `UPDATE`. Nessuna chiave fuori da `process.env`.
4. **Il tetto di costo si controlla prima della chiamata**, e ogni chiamata
   lascia una riga in `esecuzioni`, anche se fallisce.
5. Su `visual_astratti` e `scena_3d` gira `gpt-6-astra` o niente: il database
   rifiuta un fallback, il job si ferma e avvisa.
6. Stack: Node 22, TypeScript strict, Postgres 16, LiteLLM, Docker Compose,
   Zod, `pg`, SDK `openai` puntato su LiteLLM.

## Cosa si è scartato

- Chiamare gli SDK dei provider direttamente: il pacchetto lo vieta, tutto
  passa da LiteLLM.
- Agenti, interfaccia web, autenticazione e tabelle di business (aziende, lead,
  progetti) nella fase 1: esclusi dal pacchetto.

## Conseguenze aperte

- Il pacchetto ha sette difetti da correggere prima di darlo a Claude Code →
  [[denki-agents]]
- Il VPS Hetzner CX22 del pacchetto nel vault non risulta (14/09/2026)
- Quando aziende e lead entrano nel database, i contattati del banco smettono
  di vivere nel vault, oppure il database non è l'unica memoria → [[contattati]]

## Collegamenti

[[denki-agents]] · [[stack]] · [[generazione-lead]]
