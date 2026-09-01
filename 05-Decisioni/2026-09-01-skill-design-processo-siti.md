---
date: 2026-09-01
who: nicola
source: claude
---

# Le skill di design diventano un processo unico per i siti

**Decisione.** Da oggi ogni sito vetrina/landing/portfolio parte dalla skill
`processo-siti` (`~/.claude/skills/`, sul PC di Nicola), che mette in fila le
skill di design installate: design read prima del codice, una sola skill di
stile per progetto, brand kit se manca l'identità, immagini per sezione se c'è
un tool, impeccable in costruzione, motion per ultima, verifica misurata nel
browser.

**Cosa è installato** (in `~/.claude/skills/`):

- `design-taste-frontend` — direzione anti-slop, già presente da prima
- `emilkowalski-motion` — micro-interazioni, estratta dall'installer MCPmarket
- dal pacchetto [taste-skill](https://github.com/Leonxlnx/taste-skill) (MIT),
  installate il 1° settembre: `brandkit`, `industrial-brutalist-ui`,
  `minimalist-ui`, `high-end-visual-design`, `redesign-existing-projects`,
  `full-output-enforcement`, `image-to-code`, `imagegen-frontend-web`,
  `imagegen-frontend-mobile`
- scartate: `taste-skill-v1` (superata), `gpt-taste` (duplicherebbe il
  trigger della v2), `stitch` (serve solo a Google Stitch)

**Limite che resta vero.** Le skill di stile valgono per i siti, non per i
prodotti: nei repo OperO e DenkiShift vince il loro `CLAUDE.md` (OperO impone
lucide-react e token CSS, che alcune di queste skill vietano). Il conflitto è
scritto dentro `processo-siti`.

**Sul Mac di Patrick non c'è niente di tutto questo**: le skill vivono in
`~/.claude/skills/` della macchina di Nicola. Se servono di là, si reinstallano
dal repo GitHub — il pacchetto è pubblico.
