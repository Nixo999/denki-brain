---
riga: Il cantiere di denki-agents costa al massimo un dollaro a sito, gira in locale, raccoglie le foto da Instagram in automatico.
type: decisione
data: 2026-09-17
progetto: denki-agents
updated: 2026-09-17
source: claude
stato: presa
---

# Il cantiere costa al massimo un dollaro a sito, e gira in locale

## Il contesto

17/09/2026. Il cantiere autonomo di [[denki-agents]] gira come meccanismo: il giro
di prova su Haiku è costato 0,22 USD, e lo stesso giro a prezzi di Fable sarebbe
costato 1,73. Restavano aperte quattro decisioni: budget, lead del primo sito,
foto da Instagram in automatico, server → [[2026-09-16-denki-agents-prima-i-siti]].

## La decisione

Nicola, 17/09/2026, refusi corretti, parole sue:

«il budget per singolo sito lo bloccherei sul dollaro, cerca tutti i metodi
possibili per usare meno token possibili sfruttando comunque tutta la capacità
di fable e astra. non stiamo a rifare tutti i siti adesso, le foto da instagram
non ti preoccupare che vietano la raccolta automatica continua con questa
traiettoria, il server per adesso non ci pensiamo, fai funzionare tutto in
locale, poi pensiamo a spostarci in un server»

1. **Un dollaro a sito**, tutte le chiamate ai modelli comprese.
2. **Meno token possibile**, senza rinunciare a quello che sanno fare Fable e Astra.
3. **I siti esistenti non si rifanno** adesso.
4. **Le foto da Instagram si raccolgono in automatico**, sapendo che i Termini di
   Instagram lo vietano.
5. **Tutto in locale.** Il server si decide dopo.

Nello stesso messaggio: la ricerca sull'AI slop diventa il metro dei controlli sui
siti futuri, scritta con `regola.py` in [[direttive-siti]].

## Cosa si è scartato

Il server adesso.

## Conseguenze aperte

- Con un dollaro il cantiere va ridisegnato: aprire una sessione dell'Agent SDK
  col prompt di Claude Code costa 0,27 USD su Fable prima di fare qualunque cosa.
  Le ricerche del 17/09 sui token servono a questo.
- La raccolta da Instagram passa da Apify: servono un account e un token, che crea
  e inserisce Nicola → [[credenziali]].
- Nelle foto ci sono persone: il rischio sui Termini e sul GDPR lo ha preso Nicola
  il 17/09.

## Collegamenti

[[denki-agents]] · [[2026-09-16-denki-agents-prima-i-siti]] · [[processo-siti]] ·
[[direttive-siti]]
