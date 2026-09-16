---
riga: Piattaforma interna multi-agente - ogni task sul suo modello via LiteLLM, costo di ogni chiamata in Postgres. Fase 1: solo il gateway.
type: progetto
status: attivo
client: interno
stack: [node-22, typescript, postgres-16, litellm, docker-compose, zod, pg, openai-sdk, claude-agent-sdk]
started: 2026-09-14
deadline: TODO
updated: 2026-09-17
source: denkicode
---

# denki-agents — piattaforma multi-agente

Piattaforma interna a due utenti: Nicola (siti, dal lead alla bozza) e Patrick
(analisi e outreach). Un database condiviso è l'unica memoria: gli agenti non
ricordano niente, leggono dal DB, fanno una cosa, scrivono sul DB. Cliente: interno.

**Repo**: `Nixo999/denki-agents` (privato) in `~/lavoro/denki-agents`, ramo `main` (16/09/2026)
**Online**: il pacchetto dice VPS Hetzner CX22 con Docker; nel vault non risulta (14/09/2026)
**Memoria tecnica**: `CLAUDE.md`, `docs/spec-fase-1.md`, `docs/routing.md`, `docs/handoff.md` nel repo

## Stato

Pacchetto della fase 1 portato da Nicola: regole, spec, dati del seed. Repo
locale creato, spec corretta e listino controllato sulle pagine ufficiali;
**fase 1 chiusa il 16/09/2026**: le cinque condizioni della definizione di fatto
provate con chiamate vere sul Mac, commit solo locali → [[registro-interventi]].
Adesso il cantiere autonomo, poi la piattaforma online →
[[2026-09-16-denki-agents-prima-i-siti]]. **Il cantiere gira come meccanismo**
(17/09/2026): `pnpm run cantiere` su Haiku ha fatto un giro di prova completo per
0,22 USD. Il primo sito vero aspetta budget e lead → `docs/spec-cantiere.md`.

La fase 1 è solo il gateway verso i modelli: tre tabelle Postgres (`modelli`,
`task_routing`, `esecuzioni`), LiteLLM come proxy unico, `esegui(task, input)`
e una CLI. 21 task (12 lato Nicola, 9 lato Patrick), 10 modelli di chat e uno di
embedding su 3 provider (16/09/2026).

**La fase 2, il cervello, è scritta** in `docs/spec-fase-2.md` (16/09/2026):
sette tabelle (aziende, liste, contatti, siti, trattative, lavori,
disiscrizioni) più `indice_semantico` in pgvector, un regista che legge la coda
ed è anche il calendario, nove flussi con le fermate di Nicola e Patrick, il
cruscotto per chi non ha il vault. Non si costruisce prima che la fase 1 sia
chiusa. Le fasi dopo la 2 non sono scritte (16/09/2026).

## Soldi

| | |
|---|---|
| Entra | niente, è interno |
| Esce | API a consumo, limite 20 $/mese per account messo prima di generare le chiavi. VPS: TODO |
| Forma | nessuna ricevuta |

## Decisioni prese

- Si parte dal gateway, modello e prezzo di ogni task stanno nel database →
  [[2026-09-14-denki-agents-parte-dal-gateway]]
- Il cervello sta in un database solo, Postgres con pgvector, e il prompt si
  compone a budget → [[2026-09-16-cervello-denki-agents]]
- **Per adesso tre provider: OpenAI, Anthropic, Google.** Nicola, 16/09/2026: «per
  adesso basiamoci solo su questi 3 e poi in futuro se tutto funziona come voglio
  aggiungiamo altre». Gli altri cinque restano verificati in fondo a `docs/routing.md`
  (`1fdf30b`)
- **Prima la parte che fa i siti.** Nicola, 16/09/2026: «voglio fare in modo che a
  breve sia pronta soprattutto la parte che fa i siti, che voglio spostare lì la
  produzione» → [[2026-09-16-denki-agents-prima-i-siti]]
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
- [x] pnpm 12.4.2 attivato con corepack sul Mac (16/09/2026)
- [x] chiavi OpenAI, Anthropic e Google nel `.env`, create da Nicola con credito iniziale: rispondono tutte e tre e i modelli del listino sono visibili sugli account (16/09/2026) → [[credenziali]]
- [x] remote GitHub `Nixo999/denki-agents` privato: creato e pushato da Claude, come da [[2026-09-03-gh-crea-repository]] (16/09/2026)
- [x] prompt del pacchetto eseguito e fase 1 chiusa (16/09/2026): numeri, scelte e problemi in `docs/handoff.md`
- [ ] Gemini 3.8 Flash ragiona coi token d'uscita: `seo_meta` esce troncato a 1.500 token. Manca un modo di regolare il ragionamento per task (16/09/2026)
- [ ] push dei commit: Nicola non ha ancora deciso se serve avere tutto su git (16/09/2026)
- [ ] cantiere, foto da Instagram in automatico: Apify costerebbe 0-19 USD al mese, ma i Termini di Instagram vietano la raccolta automatica e nelle foto ci sono persone. Decide Nicola (17/09/2026)
- [ ] cantiere, primo sito vero: budget da decidere e limite di 20 USD al mese della chiave Anthropic da alzare; un giro di prova a prezzi Fable costerebbe 1,73 USD (17/09/2026)
- [ ] cantiere, lead del primo sito: meglio una bozza gia' sotto il livello, Lobidu' o Da Caterina (17/09/2026)
- [ ] server: il CX22 del pacchetto non si vende dal 01/01/2026, e il 17/09 Hetzner segna non disponibili CX e CAX. Con un browser dentro servono 8 GB (17/09/2026)
- [x] fase 2: embedding su `text-embedding-3-small` a 768 dimensioni (`1c92389`, 16/09/2026). Non per il prezzo: è l'unico a 0,02 $ con l'endpoint embeddings documentato in LiteLLM. OpenAI non dichiara l'italiano: se il recupero è debole si cambia modello e si rifà l'indice, quattro centesimi
- [ ] fase 2: chi è `momo`? Una lista chiamate ha bisogno di un destinatario (16/09/2026)
- [ ] fase 2: i due CSV dei contattati si importano una volta sola, poi il banco scrive nel database → [[contattati]]
- [ ] mail a freddo: servono lista da Registro imprese, dominio secondario e 3-4 settimane di warm-up → [[2026-09-02-cold-email-gestionali]]
- [ ] `gpt-5.6-sol` in promozione almeno fino al 21/11/2026: il prezzo dopo non è pubblicato
- [ ] dal 01/01/2027 `gemini-3.8-flash` va a 1,50/7,50: i fallback di `seo_meta`, `qa_tecnico` e `report_periodico` diventano impossibili, la sola uscita tocca il tetto
- [ ] VPS: esiste? TODO
- [ ] vault o database per i lead: oggi i contattati stanno nei CSV del banco → [[contattati]]. Si decide quando arrivano le tabelle di business
- [x] righe del repo aggiunte in `claude-md-globale`, `/nicola` e `/aggiorna-progetti` (16/09/2026)

## Collegamenti

[[stack]] · [[convenzioni]] · [[credenziali]] · [[processo-siti]] · [[generazione-lead]]
