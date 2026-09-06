---
type: decisione
data: 2026-09-06
progetto: azienda
source: claude
---

# Il Mac di Nicola: tutto in `~/lavoro`, e le skill di design hanno finalmente una provenienza scritta

**Decisione di Nicola**, 6 settembre 2026: messa in piedi da zero una seconda
macchina sua, un MacBook Pro, e **tutto sta in `~/lavoro`** — vault e repo di
codice nella stessa cartella, senza Desktop e senza `~/denkicode/`.

## Quello che cambia rispetto a [[setup-macchina-nuova]]

1. **La cartella si chiama come il repo.** `opero-sito`, non `opero-core`;
   `smooth-duty`, non `turni`. Sul PC Windows i nomi divergono per ragioni
   storiche: qui non si ripete. Chi legge la tabella di `/nicola` o del
   `CLAUDE.md` trova percorsi Windows — valgono là, non qui.
2. **`DENKI_VAULT` in `~/.zshenv`.** Le tre modalità leggono quella variabile
   per prime e non cercano più a tappeto. Senza, lo script di aggancio di
   `/nicola` non trovava niente: cerca `denkicode volt`, che su un Mac non
   esiste.
3. **Dodici repo clonati, non tre.** Oltre a `denki-brain`, `smooth-duty` e
   `opero-sito` ci sono anche i nove dei siti. Lo script che li rimette
   ovunque sta in `~/lavoro/clona-repo.sh`: rilanciabile, salta quello che
   trova già.

## La provenienza delle skill di design, che mancava

[[2026-09-01-skill-design-processo-siti]] elencava cosa era installato ma non
**da dove** venisse, tranne il pacchetto `taste-skill`. Su una macchina nuova
questo è il buco che costa: le skill non arrivano da sole. Adesso è scritto:

| Skill | Da dove |
|---|---|
| le nove di `taste-skill` + `design-taste-frontend` | `github.com/Leonxlnx/taste-skill` (MIT) |
| `impeccable` | `github.com/pbakaus/impeccable` — bundle `.claude/` del repo, versione 4.2.1, più i suoi quattro agenti |
| `emilkowalski-motion` | `github.com/nexu-io/open-design`, cartella `skills/` |

⚠️ **Gli hook di `impeccable` non si installano a livello di account.** Il suo
bundle porta un `settings.json` con `PostToolUse` e `Stop` che lanciano il
detector usando `$CLAUDE_PROJECT_DIR`: sono scritti per stare dentro un
progetto. A livello globale girerebbero anche nel vault — dove lo `Stop` è già
occupato da `ricorda-push.sh` — e dentro [[opero]] e [[denkishift]], dove il
craft floor contraddice i loro `CLAUDE.md`. Si copiano nel repo del singolo
sito.

## `processo-siti` su questo Mac è una ricostruzione

`TODO` **Nicola.** La skill originale vive solo in `~/.claude/skills/` del PC
Windows e non è su nessun repository. Su questo Mac c'è una versione rimessa
insieme da questa nota, da [[2026-09-01-skill-design-processo-siti]], da
[[sito-dsi-advertising]], [[sito-atelier-selva]] e [[2026-09-03-sito-dsi]]:
i dieci passi in ordine, lo stile del cliente prima del dado, la precedenza
`brief > skill di stile > design-taste`, il `PRODUCT.md` prima del
`concept-seed`, la finish review, le misure su 1440×900 e 375×812, i tre
sbarramenti `noindex`.

**Va confrontata con l'originale appena il PC Windows è raggiungibile.** Dove
divergono vince l'originale. Il riquadro che lo dice sta in cima al file della
skill.

## Cosa resta fuori da git, su ogni macchina

Gli MCP ([[plugin-claude-code]]) — Apify, Figma, Tella — hanno account e chiavi
personali e si agganciano dalle impostazioni di Claude, non da riga di comando.
I `.env` dei due gestionali sono predisposti e vuoti: le chiavi le mette la
persona, mai io ([[credenziali]]).

## Collegamenti

[[setup-macchina-nuova]] · [[claude-md-globale]] · [[plugin-claude-code]] ·
[[design-frontend]] · [[skills]] · [[2026-09-01-skill-design-processo-siti]]
