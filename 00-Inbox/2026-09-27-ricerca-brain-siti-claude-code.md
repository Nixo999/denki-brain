---
type: risorsa
riga: Ricerca del 27/09/2026 su cosa adottare per brain, siti e Claude Code - classifica per resa/sforzo, con fonti. Ipotesi da verificare prima di muoversi.
updated: 2026-09-27
source: claude
tags: [ricerca, vault, siti, claude-code, strumenti, netlify]
---

# Ricerca del 27/09/2026 — cosa c'è di nuovo per brain, siti e Claude Code

Tre ricerche in parallelo (memoria per agenti, siti vetrina 2026, funzioni di
Claude Code non usate), fonti aperte e lette dagli agenti il 27/09/2026. Le
voci sono **ipotesi**: nessuna è stata provata qui. Chiesta da Nicola.

## La classifica — cosa farei, in ordine

| # | Cosa | Perché qui | Sforzo | Dove |
|---|---|---|---|---|
| 1 | **Bozze come branch deploy su Netlify, non produzione** | Il Free dà 300 crediti/mese, un deploy di produzione costa 15: ~20 al mese per tutto il team. I 3-9 giri a sito hanno bruciato il credito il 18/09. I branch/preview deploy sono gratis | 1h | `netlify.md`, starter |
| 2 | **Hook `PreToolUse` che blocca `git commit` se `genera-indice.py --check` fallisce** | I tetti ora si misurano; con l'hook si impongono. Exit 2 = blocco | 1h | `~/.claude/settings.json`, `installa-macchina.py` |
| 3 | **Xcode sul Mac di Nicola per il Simulator iOS** | «Safari e iPhone veri mai provati» sta su 13 siti. Playwright WebKit non ha barra dinamica, safe-area, momentum scroll. Il Simulator è gratis e più fedele; il WKWebView di Instagram non lo replica nessuno: quello si prova sul telefono | 1h + download | processo-siti |
| 4 | **Scroll-driven animations in CSS al posto di GSAP ScrollTrigger** | Safari 26 le ha, dal 26.4 girano sul compositor come le transition: niente jank e niente pin che trattiene lo scroll, il difetto bocciato su Per un Pelo e Lei Beauty. Firefox ancora dietro flag: `@supports` con fallback fermo | 6-8h nello starter | starter-sito, direttive-siti |
| 5 | **Comandi → skill** | I file in `.claude/commands` sono deprecati. Con le skill: `context: fork` per `/banco` (gira in un subagente, il contesto principale resta pulito), `disable-model-invocation` per `/chiudi-sessione`, `allowed-tools` per pre-approvare git | 1h | `.claude/skills/` |
| 6 | **`controlla-sito.py` blocca ciò che riporta il banner cookie** | Garante FAQ 12: solo cookie tecnici → niente banner. Basta che non ci siano `fonts.googleapis.com`, iframe di Maps, embed Instagram, GA. Oggi lo fate a mano | 1h | controlla-sito.py |
| 7 | **`wa.me/39…?text=` diverso per sezione** | «Ciao, vorrei info sul balayage» invece del vuoto. Conversione a costo zero | 0,5h | starter, scrittura-web |
| 8 | **`superato_da:` nel frontmatter di decisioni e direttive** | La contraddizione dei 65 DM è durata 16 giorni perché nessuno script poteva vederla. Con il campo, `genera-indice.py` la stampa | 2h | come-si-scrive-una-nota, regola.py |
| 9 | **Ricerca ibrida: sqlite-vec + EmbeddingGemma dentro `cerca.py`** | `cerca.py` è solo FTS5: una domanda con parole diverse dalla nota non la trova. 40 righe di Python, stesso SQLite, 768 dimensioni, italiano coperto. Alternativa pronta: `qmd` (Karpathy la usa), ma vuole Node 22 e 2 GB di modelli su ogni Mac | 3-4h | cerca.py |
| 10 | **Routine cloud: «controlla i siti online» ogni mattina** | Una sessione Claude Code su VM Anthropic a orario, con il repo clonato: `curl` sui sbarramenti e sul deploy servito di ogni bozza, riga nel registro. `/banco` invece no: Instagram e i motori non ci arrivano da lì | 0,5h | `/schedule` |
| 11 | **`/doctor prompt-audit` e `/skill-doctor`** | Dicono quanto costano in token le 14 skill caricate a ogni sessione e quali non si usano mai | 10 min | — |
| 12 | **Batch API e cache a 1h per il cantiere di denki-agents** | Il sito a un dollaro non è interattivo: il batch dimezza il prezzo. Opus 5.5 costa 4/20 contro 5/25 di Opus 5 | 2h | denki-agents |
| 13 | **Remote Control per Patrick** | `claude remote-control` sul suo Mac, la sessione si guida dal telefono con QR e notifiche. È la sua sessione vera, con il vault | 5 min | setup-macchina-nuova |
| 14 | **Bozza come Artifact di claude.ai** | Link pubblico senza login, aggiornabile allo stesso URL, zero deploy Netlify. Contro: il link dice `claude.ai`, e il cliente lo vede | 0 | processo-siti |

## Filone 1 — memoria e vault

- **LLM Wiki di Karpathy** (gist, 4 apr 2026): `raw/` immutabile, `wiki/` scritta dall'LLM, schema in CLAUDE.md, `index.md` con una riga per pagina, `log.md` append-only; tre operazioni: ingest, query, **lint**. Il vault ha già indice, registro e schema. Manca la separazione raw/note (liste CSV e ricerche competitor stanno in mezzo alle note) e il lint, che da oggi `genera-indice.py` fa in parte. https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- **LLM Wiki v2, supersessione esplicita**: ogni contraddizione nuova «supersede» la vecchia, linkata, datata, conservata ma marcata. È la vostra regola resa leggibile da script → voce 8. https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2
- **Validità temporale**: Graphiti usa `valid_at`/`invalid_at`; MemStrata (arXiv, giu 2026) porta i fatti scaduti nel RAG dal 15-40% a ~0 con regole deterministiche di supersessione. Senza grafo: `valido_dal:`, `valido_al:`, `superato_da:`. https://arxiv.org/abs/2606.26511
- **qmd** (30k stelle): FTS5 + sqlite-vec + EmbeddingGemma-300M + Qwen3-Reranker, MCP server, tutto locale. https://github.com/tobi/qmd · **sqlite-vec** https://github.com/asg017/sqlite-vec · **EmbeddingGemma** https://huggingface.co/google/embeddinggemma-300m
- **Guida ufficiale CLAUDE.md**: sotto 200 righe per file; `.claude/rules/*.md` con `paths:` si caricano solo sui file toccati; `@import` non riduce il contesto; hook «per ciò che deve succedere sempre». Il vault è a 185 righe, il globale a 113: al limite ma dentro. https://code.claude.com/docs/en/memory · https://code.claude.com/docs/en/best-practices
- **Context engineering Anthropic**: identificatori leggeri e caricamento on demand, subagenti che tornano ≤ 2.000 token. «Si legge l'indice, non le note» è già questo. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **Obsidian Bases** è core (1.14.2, 15 set 2026): tabelle, kanban, mappe sulle stesse properties, senza plugin. Dataview è fermo ad aprile 2025. `dashboard.md` si rifà in Bases se qualcuno la apre: oggi ha zero link in entrata. https://obsidian.md/help/bases

## Filone 2 — siti vetrina

- **Netlify Free 2026**: 300 crediti/mese per team, banda 20 cr/GB, produzione 15 cr a deploy, preview e branch deploy gratis, form illimitati. Finiti i crediti si spengono i deploy di tutto il team → voce 1. https://netli.fyi/blog/netlify-free-plan-limits-2026 · https://www.netlify.com/pricing
- **Cloudflare Workers Static Assets**: richieste statiche gratis e illimitate, 20.000 file, 100 domini. Piano B senza tetto di banda; niente form e niente Image CDN inclusi. Vercel Hobby vieta l'uso commerciale, GitHub Pages vieta «online business». https://developers.cloudflare.com/workers/platform/limits
- **Scroll-driven animations**: Safari 26.0 (set 2025), compositor dal 26.4 (mar 2026). https://webkit.org/blog/17333 · https://webkit.org/blog/17862
- **View transitions cross-document**: `@view-transition { navigation: auto }`, Safari 18.2+, chi non supporta ignora. Solo per siti a più pagine. https://webkit.org/blog/16967
- **Anchor positioning + popover** senza JS in tutti i browser da gennaio 2026; Safari 27 ha rinominato due proprietà: si ritesta a ogni release. https://webkit.org/blog/18325
- **Netlify Image CDN**: `/.netlify/images?url=…&w=800&fm=avif`, si paga come banda. Voi fate già WebP con Pillow: serve solo se le foto tornano pesanti. https://docs.netlify.com/build/image-cdn/overview
- **Zero banner**: Garante FAQ cookie 12; font self-hosted (Monaco 2022, 100 € per Google Fonts remoto); Maps come immagine + link; embed Instagram carica JS Meta comunque. https://www.garanteprivacy.it/faq/cookie
- **EAA**: micro-imprese esenti, e solo e-commerce, banche, trasporti, ebook. Un sito vetrina è fuori due volte.
- **Prenota con Google via Fresha**: Fresha integra Reserve with Google (GBP con nome e indirizzo identici). ⚠️ Pagine help di Fresha e lista partner Google **non verificate**.
- **Recensioni Google**: Places API max 5 recensioni scelte da Google, chiave da custodire, credito gratis finito nel 2025. Meglio rating a mano + link «Leggi le recensioni». ⚠️ SKU non verificati.
- **Foto**: chi paga il fotografo non ne compra i diritti; foto scattate dal cliente sono sue; volti → consenso. Una domanda nel messaggio di conferma. Immagini AI per sfondi: Nano Banana 2 a 0,067 $ a 1K; un volto AI nell'hero di un parrucchiere si vede. https://ai.google.dev/gemini-api/docs/pricing
- **Safari vero**: Playwright WebKit non è iOS; BrowserStack senza free tier; TestMu 5 sessioni/mese gratis. Il Simulator di Xcode è la via → voce 3. https://www.testmuai.com/blog/playwright-ios-testing
- **Slop, i sei tell** (925studios, mar 2026): Inter + system font, gradiente viola-blu, headline vaghe, stock e blob 3D, radius 16 px uniforme, motion assente. Da confrontare con `controlla-slop.py`.
- **Concorrenti**: Framer Basic 10 $/mese, v0 Plus 30 $, Lovable a crediti, Wix 17 €+. Vendono l'abbonamento, voi il sito finito. Il buco è l'editor per il cliente: Fiftynine e V-BAG lo hanno, gli altri no.

## Filone 3 — Claude Code e piattaforma (verificato su code.claude.com il 27/09/2026)

- **Auto memory** (`~/.claude/projects/<repo>/memory/MEMORY.md`): attiva di default, locale alla macchina, non sincronizzata. Per un vault che deve valere su due Mac è una seconda verità: si spegne (`autoMemoryEnabled: false`) o si accetta con la regola «niente lì che non stia nel vault». https://code.claude.com/docs/en/memory#auto-memory
- **Hook 2026**: exit 2 blocca su PreToolUse, UserPromptSubmit, Stop; campo `if: "Bash(git commit *)"`; eventi nuovi PreCompact, PostCompact, FileChanged, SubagentStop. https://code.claude.com/docs/en/hooks
- **Routine cloud**: VM Anthropic a orario (min 1h), repo clonato, connettori, push su `claude/*`; nessun accesso ai file locali; research preview, tetto giornaliero di run. ⚠️ Costo per run **non verificato**. https://code.claude.com/docs/en/routines
- **Skill**: `context: fork`, `agent:`, `paths:`, `disable-model-invocation`, `user-invocable: false`, `hooks` di skill, `!`cmd`` per iniettare output. https://code.claude.com/docs/en/skills
- **Misura**: `/skill-doctor`, `/doctor prompt-audit` (2.1.283), `claude plugin eval` con grader e 3 run con/senza. https://code.claude.com/docs/en/plugins/measure
- **Subagenti**: `isolation: worktree`, `memory: project`, `maxTurns`, `SendMessage` per riprenderli. Agent teams: sperimentali, ~7× token: no. https://code.claude.com/docs/en/sub-agents
- **Workflow** (`ultracode`): script JS con `agent()`/`pipeline()`/`parallel()`, fino a 16 agenti concorrenti, salvabile in `.claude/workflows/`. Caso: 100 siti da verificare in parallelo. Costa. https://code.claude.com/docs/en/workflows
- **Patrick senza terminale**: sessione cloud da claude.ai/code o app mobile (repo + branch + compito, apre PR); Remote Control sul suo Mac; Channels Telegram (bot in una sessione aperta, allowlist: chi è dentro può approvare permessi → non per Giulia, il vault ha le provvigioni in chiaro). https://code.claude.com/docs/en/remote-control · https://code.claude.com/docs/en/channels
- **Connettori MCP di claude.ai**: GitHub, Gmail, Calendar, Drive, Notion, Netlify, Slack; valgono anche nelle routine. Obsidian: solo community, e il filesystem basta. https://code.claude.com/docs/en/mcp
- **Prezzi ($/MTok in/out)**: Fable 5.1 10/50, Opus 5.5 4/20, Opus 5 5/25, Sonnet 5 2/10, Haiku 4.5 1/5. Batch −50 %, cache 1h ×2 in scrittura e 0,1× in lettura. Stima di un sito a tre modelli a listino API: 10-15 $ (**stima**, non misurata; in abbonamento non si paga a token). https://platform.claude.com/docs/en/about-claude/pricing
- **Artifacts**: pagina HTML pubblicata da Claude Code, link pubblico senza login su Pro/Max, 16 MiB, CSP stretta. https://code.claude.com/docs/en/artifacts
- **Claude in Chrome** (`claude --chrome`): usa il Chrome vero con i login; si ferma su CAPTCHA; injection dai contenuti. Il pannello integrato non ha i cookie. https://code.claude.com/docs/en/chrome

## Scartato, e perché

- Letta, Mem0, Zep/Graphiti, Cognee, LightRAG: server e un LLM in estrazione per 262 note curate. I loro benchmark misurano chat, non un vault.
- MCP per Obsidian: Claude legge già i file; aggiunge un processo e una chiave per zero funzioni.
- Confidence decimale e decadimento: nessuno li calibra in tre. Bastano `verificato:` e `superato_da:`.
- Registro in JSONL con FATTI generato da script: doppia verità appena qualcuno scrive a mano. Il registro resta prosa.
- Datacore: WIP fuori dallo store. Agent teams: 7× token.
- `llms.txt`: Google lo chiama speculativo (2 giu 2026), Ahrefs: il 97% dei file non viene mai richiesto. Speculation rules: Safari non le ha mai spedite.
- Maps iframe e Instagram embed: costano il banner e 300 KB di JS Meta.
- Places API per le recensioni: 5 recensioni scelte da Google e una chiave da custodire; il link a GBP rende uguale.
- Lighthouse «Agentic» e «AI SEO» tecnico: per un locale contano GBP completo, NAP coerente e FAQ in linguaggio parlato, non il markup.
- Claude Agent SDK: serve a impacchettare Claude in un'app propria, si paga API.

## Collegamenti

[[FATTI]] · [[processo-siti]] · [[direttive-siti]] · [[anti-slop-siti]] ·
[[denki-agents]] · [[come-si-scrive-una-nota]] · [[plugin-da-valutare]] ·
[[registro-interventi]]
