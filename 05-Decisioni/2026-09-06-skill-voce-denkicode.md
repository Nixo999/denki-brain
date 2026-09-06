---
type: decisione
data: 2026-09-06
progetto: azienda
source: claude
---

# Nasce la skill voce-denkicode

**Il fatto.** Un lead, angolorelax_nembro, ha risposto a un DM Instagram
scritto da Claude per conto di Patrick dicendo, testuale: *"è un banale copy
poco professionale per chatGPT... leva le em dashes che ti fanno sgamare
all'istante"*. Screenshot mostrato da Nicola il 6 settembre 2026. Lead perso
sulla forma del messaggio, non sul prezzo o sull'offerta.

**La causa.** `stile-comunicazione.md` dice il tono ("diretto, giovane, no
fuffa") ma non elenca i pattern concreti che tradiscono un testo generato da
LLM: em dash, triadi retoriche, aperture a domanda, frasi-cuscinetto. Senza
una blacklist esplicita, ogni testo generato rischiava lo stesso tell.

**La decisione.** Creata `voce-denkicode` come skill a parte (non una
modifica a `stile-comunicazione.md`, che resta la fonte del tono):
`.claude/skills/voce-denkicode/SKILL.md` nel vault, copiata in
`~/.claude/skills/` su questo Mac perché sia caricabile. Si applica a:

- ogni messaggio diretto al cliente (WhatsApp, DM, email), insieme a
  [[proposta-commerciale]]
- il copy testuale dei siti vetrina, agganciata dentro `processo-siti` prima
  della finish review — vedi `~/.claude/skills/processo-siti/SKILL.md`, passo
  7bis

**Cosa resta aperto.** La skill non ha ancora un caso di verifica: la prossima
bozza di copy o il prossimo messaggio a un lead è il primo test reale. Se
sgama di nuovo, il problema non è la blacklist ma il fatto che nessuno la
rilegge prima di mandare — a quel punto serve un passaggio umano dichiarato,
non una skill più lunga.

## Collegamenti

[[stile-comunicazione]] · [[registro-trevis]] · [[proposta-commerciale]]
