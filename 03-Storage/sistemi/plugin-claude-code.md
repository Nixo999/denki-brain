---
type: risorsa
updated: 2026-08-30
source: claude
tags: [setup, claude, plugin, mcp]
---

> **Inventario di quello che è agganciato a Claude Code sul PC di Nicola.**
> Come [[claude-md-globale]], è roba **locale alla macchina**: sta in
> `~/.claude/`, fuori da git. Su un PC nuovo — il Mac di Patrick compreso —
> non arriva da sola, va rifatta da qui.

# Plugin e MCP di Claude Code

Due meccanismi diversi, che si confondono facilmente:

- un **plugin** aggiunge comandi, skill e agenti *dentro* Claude Code, e gira
  sui token del piano Claude;
- un **MCP** è un processo esterno che espone dei tool, con **chiavi e conto
  suoi**. Un MCP «Connected» non vuol dire che funziona: vuol dire che il
  processo parte.

## Marketplace registrati

| Nome | Repo |
|---|---|
| `claude-plugins-official` | `anthropics/claude-plugins-official` (automatico) |
| `claude-community` | `anthropics/claude-plugins-community` |
| `ponytail` | `DietrichGebert/ponytail` |

⚠️ Il marketplace `anthropics/claude-plugins-community` si registra da solo col
nome **`claude-community`**, non col nome del repo: `install …@claude-plugins-community`
fallisce con «plugin not found» e sembra un problema del plugin.

## Plugin attivi

| Plugin | Cosa fa |
|---|---|
| `superdesign` | canvas di design multi-artboard |
| `playground` | pagine HTML interattive autonome |
| `modern-web-guidance` | ricerca sulle pratiche web attuali, obbligatoria prima di HTML/CSS |
| `ponytail` | forza la soluzione più corta che funziona (YAGNI, stdlib prima delle dipendenze) |
| `deep-research` | ricerca multi-agente, ⬇️ sotto |

## `deep-research` — il plugin

Installato il 30 agosto 2026 da `claude-community`, versione 1.3.1. Comando
`/deep-research --mode=web|repo|structured`. Non chiama servizi esterni: monta
squadre di subagent Claude (scout Haiku → specialisti Sonnet che si contestano
a vicenda → sintesi Opus) e **scrive file markdown in `docs/research/`** del
progetto, non messaggi in chat.

- `--mode=web "argomento"` — corpus di fonti da web search, lettura profonda,
  passata finale sui buchi di copertura.
- `--mode=repo /path [--compare /path/mio]` — inventario file, analisi
  architettura, sintesi. **`--compare` è l'uso che vale su OperO**: gap-analysis
  fra `sebapp-bolanos` e `opero-core` senza leggersi mezzo repo a mano.
- `--mode=structured spec.yaml` — ricerca a schema su N entità con verificatori
  che marcano ogni campo CONFIRMED / UPDATED / REFUTED / CONTESTED.

Richiede il flag sperimentale **Agent Teams**, scritto in `~/.claude/settings.json`:
`"env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" }`. Senza, ogni pipeline
parte e muore subito. **Vale dal riavvio di Claude Code**, non dalla scrittura.

⚠️ La prima riga del suo README è `# PoC -- John Stawinski`: è un
proof-of-concept in un marketplace **community**, non un prodotto Anthropic
supportato. Costa molti token del piano.

## `deep-research-mcp` — l'MCP, che è un'altra cosa

`github.com/teelaitila/deep-research-mcp`, clonato in
`~/.claude/mcp-servers/deep-research-mcp`, buildato (`npm install && npm run build`),
registrato user-scope:

```
claude mcp add deep-research-mcp -s user -- node --env-file=<repo>/.env.local <repo>/dist/mcp-server.js
```

Espone **un solo tool**, `deep-research`: `query`, `depth` 1-5, `breadth` 1-5,
`model`, `tokenBudget`, `sourcePreferences` (in linguaggio naturale, es. «evita
listicle SEO, forum, recensioni affiliate»). Fa ricerca ad albero, scrapa con
**Firecrawl**, pesa l'affidabilità delle fonti, ritorna **un report markdown**
come risultato del tool.

⬜ **Non funziona: `.env.local` è vuoto.** Le chiavi le scrive Nicola, non
Claude ([[credenziali]]). Servono due cose:

1. un provider modello — `ANTHROPIC_API_KEY`, oppure OpenAI / Google / xAI;
2. `FIRECRAWL_KEY` da firecrawl.dev, **oppure** `FIRECRAWL_BASE_URL=http://localhost:3002`
   con un'istanza Firecrawl locale, e allora la chiave non serve.

La spesa esce da quelle chiavi, **non** dal piano Claude. È la differenza con
il plugin: il plugin usa Claude e lascia artefatti versionabili nel repo,
l'MCP è un motore a sé che restituisce un report e manda un conto separato.

## Gli altri MCP agganciati

| MCP | Stato |
|---|---|
| Google Calendar | ✅ connesso |
| Apify (scraper Instagram) | ✅ connesso — è quello di [[2026-08-30-sito-castiglione]] |
| Figma | ⚠️ da autenticare |
| Tella | ⚠️ da autenticare |

## Collegamenti

[[claude-md-globale]] · [[credenziali]] · [[2026-08-30-sito-castiglione]] ·
[[modifiche-al-database]]
