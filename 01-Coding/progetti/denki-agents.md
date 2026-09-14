---
riga: Piattaforma interna multi-agente - ogni task sul suo modello via LiteLLM, costo di ogni chiamata in Postgres. Fase 1: solo il gateway.
type: progetto
status: attivo
client: interno
stack: [node-22, typescript, postgres-16, litellm, docker-compose, zod, pg, openai-sdk]
started: 2026-09-14
deadline: TODO
updated: 2026-09-14
source: denkicode
---

# denki-agents — piattaforma multi-agente

Piattaforma interna a due utenti: Nicola (siti, dal lead alla bozza) e Patrick
(analisi e outreach). Un database condiviso è l'unica memoria: gli agenti non
ricordano niente, leggono dal DB, fanno una cosa, scrivono sul DB. Cliente: interno.

**Repo**: `~/lavoro/denki-agents`, solo locale: il remote `Nixo999/denki-agents` non esiste (14/09/2026)
**Online**: il pacchetto dice VPS Hetzner CX22 con Docker; nel vault non risulta (14/09/2026)
**Memoria tecnica**: `CLAUDE.md`, `docs/spec-fase-1.md`, `docs/routing.md`, `docs/handoff.md` nel repo

## Stato

Pacchetto della fase 1 portato da Nicola: regole, spec, dati del seed. Repo
locale creato, spec corretta e listino controllato sulle pagine ufficiali;
nessuna riga di codice (14/09/2026) → [[registro-interventi]]. Le fasi dopo la
1 non sono scritte (14/09/2026).

La fase 1 è solo il gateway verso i modelli: tre tabelle Postgres (`modelli`,
`task_routing`, `esecuzioni`), LiteLLM come proxy unico, `esegui(task, input)`
e una CLI. 21 task (12 lato Nicola, 9 lato Patrick), 15 modelli su 8 provider.

## Soldi

| | |
|---|---|
| Entra | niente, è interno |
| Esce | API a consumo, limite 20 $/mese per account messo prima di generare le chiavi. VPS: TODO |
| Forma | nessuna ricevuta |

## Decisioni prese

- Si parte dal gateway, modello e prezzo di ogni task stanno nel database →
  [[2026-09-14-denki-agents-parte-dal-gateway]]
- Stack dal pacchetto: Node 22 (supporto fino al 30/04/2027), TypeScript
  strict, ESM, pnpm, Postgres 16, LiteLLM, Docker Compose, Zod, `pg`, SDK
  `openai` puntato su LiteLLM

## Aperto

Spec e listino si sono corretti nel repo prima del prompt (14/09/2026). I
dettagli stanno in `docs/spec-fase-1.md` e `docs/routing.md`, che vincono su
questa nota.

- [x] sette difetti corretti nella spec, più errori non recuperabili subito al fallback e nessun tetto giornaliero finché lancia solo la CLI (`0ee90d6`)
- [x] listino controllato sulle pagine ufficiali (`00591f7`): tre ID del pacchetto sbagliati (`mistral-large-3`, `gemini-3.1-pro`, `deepseek-v4-flash`), Mistral quattro volte più basso, `gpt-6-astra` a 50 in uscita. Senza `temperature` anche `gpt-6-astra` e i Gemini 3
- [x] Docker Desktop 4.91 sul Mac di Nicola: motore 29.8 e Compose 5.5 rispondono (14/09/2026)
- [ ] pnpm: sul Mac c'è solo corepack (14/09/2026)
- [ ] chiavi OpenAI e Google: le crea e le scrive Nicola → [[credenziali]]
- [ ] remote GitHub `Nixo999/denki-agents`, privato: non esiste (14/09/2026)
- [ ] poi il prompt del pacchetto, in una sessione aperta dentro `~/lavoro/denki-agents`
- [ ] `gpt-5.6-sol` in promozione almeno fino al 21/11/2026: il prezzo dopo non è pubblicato
- [ ] dal 01/01/2027 `gemini-3.8-flash` va a 1,50/7,50: i fallback di `seo_meta`, `qa_tecnico` e `report_periodico` diventano impossibili, la sola uscita tocca il tetto
- [ ] VPS: esiste? TODO
- [ ] vault o database per i lead: oggi i contattati stanno nei CSV del banco → [[contattati]]. Si decide quando arrivano le tabelle di business
- [ ] quando nasce il remote: riga nella tabella repo di `claude-md-globale` e di `/nicola`

## Collegamenti

[[stack]] · [[convenzioni]] · [[credenziali]] · [[processo-siti]] · [[generazione-lead]]
