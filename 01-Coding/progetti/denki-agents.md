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

**Repo**: `Nixo999/denki-agents` in `~/lavoro/denki-agents` — non ancora creato (14/09/2026)
**Online**: il pacchetto dice VPS Hetzner CX22 con Docker; nel vault non risulta (14/09/2026)
**Memoria tecnica**: `CLAUDE.md`, `docs/spec-fase-1.md`, `docs/routing.md`, `docs/handoff.md` nel repo

## Stato

Pacchetto della fase 1 portato da Nicola: regole, spec, dati del seed. Nessuna
riga di codice (14/09/2026). Le fasi dopo la 1 non sono scritte (14/09/2026).

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

Il pacchetto si corregge **prima** di incollare il prompt: Claude Code lo segue
alla lettera (14/09/2026).

- [ ] `temperatura` 0.7 su ogni task: Fable 5.1, Opus 5 e Sonnet 5 la rifiutano con un 400 → `modelli.accetta_temperatura`
- [ ] SDK `openai` ritenta già 2 volte da solo: `maxRetries: 0`, retry di LiteLLM a zero
- [ ] timeout fisso a 120 s con uscite fino a 24.000 token → 120 s o 25 ms a token, il più alto
- [ ] Postgres e LiteLLM pubblicati solo su `127.0.0.1`: le porte di Docker scavalcano UFW
- [ ] punti 3 e 4 della definizione di fatto su modelli con chiave, non su `mistral-large-3`
- [ ] `NOT NULL` su `fallback_vietato`, `modello_primario` e booleani: a NULL il CHECK passa
- [ ] fuori dalla fase 1: `ContentPart[]` (la stima token non sa contare le immagini) e la cache di 60 s
- [ ] default proposti, non ancora nella spec: si ritentano solo 429/5xx/timeout, ogni altro errore va al fallback; tetto giornaliero nel codice solo quando qualcosa gira da solo (14/09/2026)
- [ ] listino: 11 prezzi non Anthropic non verificati, `gpt-6-astra` in output e `mistral-large-3` sono segnaposto. Le 4 righe Anthropic tornano col riferimento di giugno 2026
- [ ] dal 01/01/2027 `gemini-3.8-flash` va a 1,50/7,50: i fallback di `seo_meta`, `qa_tecnico` e `report_periodico` diventano impossibili, la sola uscita tocca il tetto
- [ ] Mac di Nicola: manca Docker, pnpm solo via corepack (14/09/2026)
- [ ] chiavi OpenAI e Google: le crea e le scrive Nicola → [[credenziali]]
- [ ] VPS: esiste? TODO
- [ ] vault o database per i lead: oggi i contattati stanno nei CSV del banco → [[contattati]]. Si decide quando arrivano le tabelle di business
- [ ] quando nasce il repo: riga nella tabella repo di `claude-md-globale` e di `/nicola`

## Collegamenti

[[stack]] · [[convenzioni]] · [[credenziali]] · [[processo-siti]] · [[generazione-lead]]
