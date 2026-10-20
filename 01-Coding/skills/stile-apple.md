---
type: risorsa
riga: Catalogo della skill stile-apple - interfacce web nello stile delle app Apple e di apple.com, token verificati, script di controllo.
updated: 2026-10-20
source: claude
verificato: 2026-10-20
tags: [skill, design, apple, frontend]
---

# stile-apple — interfacce web che sembrano fatte da Apple

La skill sta in `.claude/skills/stile-apple/` e si invoca con `/stile-apple`.
Una copia sta in `~/.claude/skills/stile-apple/` sul Mac di Nicola, così vale in
ogni cartella. Serve a progettare o a rifare un'interfaccia web nello stile
Apple: un gestionale o un'app come le app del Mac e dell'iPhone, oppure una
pagina prodotto come quelle di apple.com.

L'ha chiesta Nicola il 20 ottobre 2026: una skill per rifare il design di
un'intera app «in stile Apple, ma seriamente». Lo stesso giorno ha detto di non
applicarla ancora a nessuna app o sito: per ora esiste solo la skill.

## Cosa contiene

| File | Cosa |
|---|---|
| `SKILL.md` | Il metodo per rifare un'app, le regole per colore, tipografia, vetro, forme, icone, movimento e testi, la revisione e le licenze |
| `apple.css` | Token e componenti; ogni valore dice se viene dalle HIG, da macOS misurato, da apple.com o da una scelta nostra |
| `esempio.html` | Una schermata di gestionale completa fatta solo con `apple.css` |
| `riferimenti/componenti.md` | Componente per componente: quando si usa, misure, stati, divieti |
| `riferimenti/applecom.md` | Lo stile delle pagine prodotto, misurato sul CSS di apple.com |
| `controlla-apple.py` | Lo script che cerca gli errori; `--prova` lo verifica |

## Da dove viene

Quattro ricerche del 20/10/2026: le Human Interface Guidelines lette dal JSON
ufficiale di Apple, i colori di macOS 26 misurati sul Mac di Nicola, il CSS di
tre pagine di apple.com e sei skill della community (le più usate:
`dickwu/apple-design-skill` e `axiaoge2/apple-hig-designer`).

Due scelte vanno contro le app native, e sono volute:

- **I grigi del testo sono opachi** (`#6e6e73`, come su apple.com). I grigi
  trasparenti di iOS sul web fanno 3,4:1 e non passano la soglia di 4,5:1.
- **Il testo colorato usa i colori «ad alto contrasto» di Apple**, che in chiaro
  Apple ha tarato sopra 4,5:1 su bianco. I colori normali servono per
  riempimenti e icone.

## Verificato il 20/10/2026

- `esempio.html` nel browser dell'app, a 1440×900 e a 375×812, in chiaro e in
  scuro, con menu, sheet e avviso aperti. Nessun testo sotto soglia di
  contrasto e nessuno scorrimento orizzontale.
- `python3 controlla-apple.py --prova` trova i 15 errori di un esempio sbagliato
  e passa sulla skill stessa.

## Cosa resta aperto

- Se Safari regola da solo la spaziatura di SF con il font di sistema. Su
  Chromium la misura dice di sì.
- Le misure dei componenti di iOS 26 e macOS 26: Apple le pubblica solo nei kit
  di design, che non abbiamo aperto. In `apple.css` sono segnate «[nostra]».

## Collegamenti

[[design-frontend]] · [[processo-siti]] · [[skills]] · [[opero]] · [[denkishift]]
