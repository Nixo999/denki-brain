---
type: decisione
data: 2026-08-28
progetto: azienda
source: denkicode
---

# Chi tocca un progetto lo scrive nel brain, non solo nel repo

**Decisione di Nicola.** Dal 28 agosto 2026 ogni modifica a un progetto va in
**due posti**: nel repository del progetto, e in [[registro-interventi]] — una
riga con **chi, quando, che progetto, che repository e che database**.

## Perché, e perché la colonna del database

Il `git log` c'è già e basterebbe a dire chi ha fatto cosa. Non basta a dire
**se il database è andato dietro al codice**, ed è lì che questo prodotto si è
già rotto due volte:

- il 25 agosto 2026 il codice chiedeva colonne che nel database non c'erano e
  l'app mostrava un tabellone vuoto al posto di 429 turni;
- il 28 agosto, di nuovo: la funzione «a chiamata» è su `main` dalle 12:09, e la
  migrazione `19-lavoratori-a-chiamata.sql` non è mai stata eseguita.

La causa è strutturale, non distrazione: **il push porta il codice e non lo
schema.** Un debito del genere non lascia traccia da nessuna parte — non nel
`git log`, che vede il file `.sql` committato e non sa se è stato eseguito, e
non nel database, che semplicemente non ha quella tabella. Il registro è
l'unico posto in cui quel buco è visibile a chi non l'ha creato.

## Come si applica

- Una riga per **intervento**, non per commit: un lavoro fatto in tre commit è
  una riga con tre hash.
- Si scrive **a lavoro finito**, prima di chiudere la sessione.
- `Chi` è la persona, con `+claude` se il lavoro è passato da una sessione.
- `Database` è `—` se non toccato, altrimenti `sviluppo` o `produzione` con lo
  stato: ⬜ se la migrazione **non** è stata eseguita, col nome del file.
- Le regole di push non cambiano e restano diverse per repo:
  [[denkishift]] si pusha dopo ogni pezzo, [[opero]] si chiede prima, il vault
  si pusha sempre.

Il rimando sta in tre posti perché la regola scatti dove si lavora: `CLAUDE.md`
del vault, `~/.claude/CLAUDE.md` (attivo in ogni cartella) e il `CLAUDE.md` dei
due repository.

## Collegamenti

[[registro-interventi]] · [[modifiche-al-database]] · [[denkishift]] ·
[[opero]] · [[2026-08-28-push-automatico]]
