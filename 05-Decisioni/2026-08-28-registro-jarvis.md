---
type: decisione
data: 2026-08-28
progetto: azienda
source: denkicode
---

# Il registro dell'assistente si scrive, non si descrive

**Decisione**: la postura con cui l'assistente parla a Nicola, Patrick e Giulia
sta in un file solo — [[registro-trevis]] — e **ogni** comando del vault lo
carica prima di rispondere.

## Perché

Fino a oggi il registro era una riga dentro ogni comando: «composto, preciso,
ironia asciutta». Tre righe uguali in tre file diversi *descrivono* un tono, non
lo *riproducono*: la prima sessione `/nicola` del 28 agosto è uscita diversa da
quella che Nicola si aspettava — letture oltre il minimo, otto righe sforate, un
`git pull` aggirato in silenzio.

Su sua richiesta — «rendilo specificamente simile a quello di Trevis» e «come se
non avessi mai smesso di parlarti» — la descrizione è diventata una specifica:
formule vietate in tabella, cinque regole di continuità, e gli errori già
commessi scritti come casi di prova.

## Conseguenze operative

- Il registro si cambia **in un punto solo**. Chi modifica un comando non ci
  riscrive dentro il tono: aggiunge a [[registro-trevis]].
- Vale per tutti e nove i comandi in `.claude/commands/`, **e per le copie in
  `~/.claude/commands/`**, che vanno tenute allineate a mano: sono quelle che
  girano quando la sessione parte fuori dal vault.
- La regola 4 di `CLAUDE.md` resta, ma smette di essere la definizione: rimanda
  qui.

## Collegamenti

[[registro-trevis]] · [[stile-comunicazione]] · [[2026-08-28-push-automatico]]
