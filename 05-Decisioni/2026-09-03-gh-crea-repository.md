---
type: decisione
data: 2026-09-03
progetto: azienda
source: claude
---

# I repository su GitHub li crea Claude, il login lo fa la persona

**Decisione di Nicola**, 3 settembre 2026: «voglio impostare che da adesso tu
possa creare le mie repository». Prima serviva aprire github.com/new a mano
prima di ogni push.

## Cosa è stato fatto

- **`gh` non c'era su questo PC** (cercato nel PATH e in Program Files,
  LocalAppData, chocolatey, scoop; il [[registro-interventi]] del 2 settembre
  lo diceva già). Installato con `winget install --id GitHub.cli`: versione
  2.99.0 in `C:\Program Files\GitHub CLI\gh.exe`, nel PATH dalla sessione
  successiva.
- **Il login l'ha fatto Nicola**, `gh auth login --web`, account `Nixo999`,
  scope `repo` e `workflow`. ⚠️ Al primo tentativo il comando è uscito prima
  della riga `Logged in as` e il codice del device flow è scaduto: va lasciato
  aperto fino alla conferma.
- **Permessi in `~/.claude/settings.json`** (locale alla macchina, come
  [[claude-md-globale]]: su un PC nuovo si rifà):

| | |
|---|---|
| passa senza chiedere | `gh repo create`, `gh repo view`, `gh repo list`, `git push`, `git remote add` |
| chiede sempre | `gh repo edit` (rende pubblico un repo), `git push --force` |
| vietato | `gh repo delete`, `gh repo archive` |

## Il vincolo che resta

**Le credenziali non le digita Claude.** Il token GitHub è nel gestore
credenziali di Windows: estrarlo per chiamare l'API sarebbe maneggiare una
credenziale in chiaro, e non si fa nemmeno per comodità. Per questo il login
è l'unico passaggio che resta a mano, una volta per macchina.

## La regola sulla visibilità

**I repository nascono privati.** Le bozze commerciali portano il marchio di
aziende che non sono clienti e i loro `robots.txt` sbarrano gli indici: vale
per `dsi-site` e `fiftynine-site`. Pubblico solo su richiesta esplicita, e
`gh repo edit` chiede comunque conferma prima di cambiare visibilità.

## Collegamenti

[[credenziali]] · [[setup-macchina-nuova]] · [[sito-dsi-advertising]] ·
[[registro-interventi]]
