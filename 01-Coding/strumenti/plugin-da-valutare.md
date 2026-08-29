---
type: area
updated: 2026-08-28
source: claude
tags: [plugin, mcp, design, strumenti]
---

# Plugin e connettori da valutare — per fare siti e applicazioni

Elenco ragionato, non un catalogo. Il marketplace ufficiale
(`claude-plugins-official`, già registrato su questa macchina) ne ha **289**:
qui stanno i pochi che cambiano qualcosa per come lavoriamo noi.

Si installano dal terminale con `/plugin`. **Quasi tutti chiedono un account o
una chiave API: le inserisce la persona, mai io, e non finiscono nel vault**
([[credenziali]]).

## Installati il 28 agosto 2026 — solo sul PC di Nicola

Tre, a livello utente (`--scope user`), quindi validi in ogni cartella di questa
macchina. **Sul Mac vanno rifatti**: i plugin non stanno in git.

```bash
claude plugin install superdesign@claude-plugins-official -y --scope user
claude plugin install playground@claude-plugins-official -y --scope user
claude plugin install modern-web-guidance@claude-plugins-official -y --scope user
```

Costo misurato con `claude plugin details`, non dedotto:

| Plugin | Sempre attivo | Quando si usa | Cosa porta |
|---|---|---|---|
| `superdesign` 0.5.0 | ~181 tok | ~5,5k | 1 skill, **nessun server MCP**, nessuna chiave |
| `playground` | ~91 tok | ~1,2k | 1 skill |
| `modern-web-guidance` 0.0.184 | ~757 tok | ~1,8k | 2 skill — la seconda è `chrome-extensions`, che a noi non serve e si porta via ~360 tok |
| **totale** | **~1.030 tok a sessione** | | |

Si tolgono con `claude plugin uninstall <nome>@claude-plugins-official`, e si
disattivano senza disinstallarli con `disable`. Hanno effetto **dalla sessione
dopo**.

⚠️ Il marketplace `claude-plugins-official` **era già registrato**: scaricarne
lo zip da GitHub non serve a niente, i plugin si prendono da lì con un comando.

## 1. Design — la cosa che oggi manca davvero

Le quattro skill installate ([[design-frontend]]) **consigliano**. Nessuna
**produce**: non c'è un posto dove vedere tre varianti di una pagina prima di
scriverla.

| Plugin | Cosa aggiunge | Nota |
|---|---|---|
| **`superdesign`** ✅ installato | Canvas infinito: legge il codice esistente, genera e itera schermate, poi restituisce il codice. È l'unico che chiude il giro disegno → repo | **Il primo da provare.** Fuori dal marketplace esiste anche come skill: `npx skills add superdesigndev/superdesign-skill` |
| `playground` ✅ installato | Pagine HTML interattive autonome, con controlli e anteprima dal vivo | Per far toccare un'idea a un cliente senza pubblicare niente |
| `modern-web-guidance` ✅ installato | Tiene aggiornato l'agente sulle pratiche web correnti | Costa poco, evita di scrivere il 2024 nel 2026 |
| `frontend-design` | La versione ufficiale, come plugin | **Già presente come skill di account**: installarlo è una copia doppia. Serve solo per tenerla aggiornata da sola |

⚠️ `ui-theme-designer` **non** è quello che sembra: è il theme designer di
**SAP BTP**. Non ci riguarda.

## 2. Prendere spunto dai clienti — Instagram e siti

| Strumento | Cosa fa | Il costo vero |
|---|---|---|
| **`firecrawl`** | Trasforma un sito in markdown pulito, una pagina o tutto il dominio | Il più utile in assoluto: il sito del cliente diventa leggibile in un colpo. Piano gratuito limitato |
| **Apify MCP** *(fuori dal marketplace ufficiale)* | Migliaia di scraper pronti, fra cui **Instagram profili, post e post taggati** | È **l'unica strada vera per Instagram**: l'API ufficiale di Meta non dà i profili altrui. Si paga a esecuzione, e sta in una zona grigia rispetto ai termini di Instagram — su un cliente che ci ha ingaggiati è difendibile, su un lead freddo meno |
| `exa` · `tavily` | Ricerca web e estrazione con citazioni | Per capire un settore prima di scrivere il testo di una vetrina |
| `brightdata-plugin` · `nimble` · `zyte-web-data` | Scraping industriale | Sovradimensionati per noi |

## 3. Grafica e materiale

| Plugin | Cosa fa |
|---|---|
| `canva` | Crea, ridimensiona e fa il **controllo di coerenza col brand**. Il più vicino al lavoro di [[patrick]] sui materiali |
| `adobe-for-creativity` | Ritocco immagini, scontorni, automazioni creative |
| `figma` | Legge file, componenti e **design token**, e li traduce in codice. Serve il giorno in cui un cliente arriva con un file Figma |
| `hyperframes` | HTML → video, con GSAP. Una demo filmata di [[denkishift]] senza aprire un editor video |
| `runway-api` | Generazione di video e immagini |

## 4. Pubblicare — quelli che tocchiamo già

| Plugin | Perché |
|---|---|
| **`netlify-skills`** | [[opero]] **sta su Netlify**: funzioni, CDN immagini, form, cache, CLI. È quello con la resa più immediata |
| `lovable` | `sebapp-bolanos`, la vecchia app del cliente, è stata costruita con Lovable |
| `vercel` · `hostinger` | Se cambiamo hosting o per i siti dei clienti |
| `build-with-wordpress` · `wix` · `shopify-ai-toolkit` | Solo se decidiamo di vendere su quelle piattaforme. Oggi non è così |

## 5. Verifica — poco da guadagnare

`playwright` e `browser-use` danno un browser vero. **Ce l'abbiamo già**: il
pannello browser integrato apre, clicca, misura e legge la console. Si
installano solo se serve una suite di test automatici, che oggi non esiste su
nessuno dei due prodotti.

## Valutati e scartati

### `obsidian-second-brain` (v0.14.0, MIT) — **no, non così com'è**

Guardato il 28 agosto 2026 su richiesta di Nicola, che ne aveva scaricato lo
zip. È un progetto serio — 46 comandi, tre hook, adattatori per otto agenti — e
fa esattamente il contrario di quello che serve a noi.

**1. La sua promessa centrale contraddice la nostra regola.** Il README dice:
«ogni fonte aggiorna le pagine esistenti invece di aggiungerne di nuove, le
contraddizioni si riconciliano da sole». La regola 3 di `CLAUDE.md` dice che
**le decisioni non si riscrivono**: se una scelta cambia si scrive una nota
nuova che cita la vecchia, perché la storia serve. Uno strumento che riscrive e
riconcilia da solo cancella anche la separazione fra `source: denkicode` e
`source: claude`, che è la cosa meno negoziabile che abbiamo.

**2. Impone una struttura parallela alla nostra.** Vuole `_CLAUDE.md`,
`index.md`, `Logs/`, `Bases/`, e cartelle `Projects/` `People/` `Tasks/`.
Riconosce due stili di vault, «obsidian» e «wiki»: il nostro non è né l'uno né
l'altro, quindi ci costruirebbe accanto un secondo vault invece di leggere
questo.

**3. L'hook di scrittura litiga con come scriviamo.** `validate-ai-first.sh`
gira **dopo ogni Write/Edit — in ogni progetto, non solo nel vault** — e mette
in guardia se il file non ha `ai-first: true`, il preambolo `## For future
agent`, e se contiene lineette lunghe, virgolette curve o apostrofi tipografici.
Le nostre note sono piene di lineette lunghe, e l'hook scatterebbe anche
lavorando su [[opero]] e [[denkishift]].

**4. Il presupposto è opposto al nostro.** Scritto testualmente nel comando di
init: *«The vault is for future agent retrieval - not human reading»*. Il
nostro vault lo leggono Nicola e Patrick, e Patrick lo legge **dal terminale**,
perché su quel Mac Obsidian non c'è.

**Quello che invece vale la pena rubargli**, senza installarlo:

- **`index.md`**: un catalogo di tutte le note con una riga di descrizione, che
  l'agente legge *prima* di cercare. Costa meno di una ricerca. `CLAUDE.md` ha
  l'indice dei progetti, non delle note.
- **Il log per giornata append-only**: è la stessa idea di
  [[registro-interventi]], che però la nostra versione la batte — ha la colonna
  del database, che a loro non serve e a noi sì.
- La *freshness policy*: ogni fatto è senza tempo, datato, o un puntatore. La
  regola 5 del vault («numeri con la data accanto») è la stessa cosa detta più
  corta.

Un falso allarme, per onestà: temevo che gli hook si rompessero perché chiamano
`python3`, che su Windows spesso non esiste. Su questa macchina c'è
(3.13.11). Non è quello il problema.

## Se se ne installasse uno solo

`superdesign`. È l'unico che copre il buco vero — vedere prima di costruire — e
non si sovrappone a niente di quello che c'è.

> [!note] Analisi di Claude — 2026-08-28
> Nessuno di questi l'ho installato o provato: l'elenco viene dal catalogo del
> marketplace già scaricato su questa macchina e da una ricerca in rete.
> Descrizioni e nomi sono di chi li pubblica, e le note sui costi vanno
> verificate sul sito di ciascuno prima di metterci una carta.

## Collegamenti

[[design-frontend]] · [[skills]] · [[credenziali]] · [[opero]] · [[denkishift]]
