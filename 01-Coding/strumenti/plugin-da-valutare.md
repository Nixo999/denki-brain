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

## 1. Design — la cosa che oggi manca davvero

Le quattro skill installate ([[design-frontend]]) **consigliano**. Nessuna
**produce**: non c'è un posto dove vedere tre varianti di una pagina prima di
scriverla.

| Plugin | Cosa aggiunge | Nota |
|---|---|---|
| **`superdesign`** | Canvas infinito: legge il codice esistente, genera e itera schermate, poi restituisce il codice. È l'unico che chiude il giro disegno → repo | **Il primo da provare.** Fuori dal marketplace esiste anche come skill: `npx skills add superdesigndev/superdesign-skill` |
| `playground` | Pagine HTML interattive autonome, con controlli e anteprima dal vivo | Per far toccare un'idea a un cliente senza pubblicare niente |
| `modern-web-guidance` | Tiene aggiornato l'agente sulle pratiche web correnti | Costa poco, evita di scrivere il 2024 nel 2026 |
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
