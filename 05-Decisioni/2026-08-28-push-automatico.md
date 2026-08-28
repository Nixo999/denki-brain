---
type: decisione
data: 2026-08-28
progetto: azienda
source: denkicode
stato: attiva
updated: 2026-08-28
---

# Ogni modifica al vault si pusha subito, da qualunque macchina

**Deciso da Patrick il 28 agosto 2026.** Parole sue: ogni volta che si cambia
qualcosa nel vault, anche minima, si pusha su git — da qualunque dispositivo
avvenga — **a meno che non venga specificato il contrario**.

Non è una raccomandazione di igiene: è la regola operativa del vault. Sostituisce
l'abitudine di accumulare il lavoro fino a `/chiudi-sessione`.

## Cosa cambia, in pratica

| Prima | Adesso |
|---|---|
| Si scriveva, e il push arrivava a fine sessione con `/chiudi-sessione` | Si scrive, si committa e si pusha **subito**, ogni volta |
| Il push era un passaggio che si poteva scordare | Se resta lavoro non pushato, un hook lo ricorda prima che la sessione chiuda |
| `/chiudi-sessione` era il momento in cui il lavoro usciva dal portatile | `/chiudi-sessione` resta, ma come **riepilogo della giornata**, non come unico salvataggio |

La sequenza è sempre la stessa: `git pull --rebase` → `git add` → `git commit`
→ `git push`. Se il push non passa non si forza mai: si rifà il pull e si
riprova, come già scritto in [[setup-macchina-nuova]].

## Perché

Tre persone che scrivono nello stesso vault da macchine diverse — Nicola da più
PC, Patrick dal suo MacBook — e nessuna delle tre ci lavora a tempo pieno. Il
lavoro tenuto in locale mezza giornata è lavoro che l'altro non vede, e su cui
rischia di scrivere sopra. Un conflitto in un vault di note si risolve male:
non c'è un test che dica quale versione era quella giusta.

## Come è stata resa automatica

Non è affidata alla memoria. Sta scritta in due posti, **entrambi versionati nel
repo**, quindi vale su tutte le macchine senza doverla reinstallare:

| Dove | Cosa fa |
|---|---|
| `CLAUDE.md`, punto 6 di *Come si aggiorna il vault* | La regola che Claude legge a ogni sessione, su qualunque macchina |
| `.claude/hooks/ricorda-push.sh` + `.claude/settings.json` | Hook `Stop`: a fine turno controlla se ci sono modifiche non committate o commit non inviati, e in quel caso lo segnala |
| `.claude/settings.json`, sezione `permissions` | `git add`, `commit`, `push`, `pull` non chiedono più conferma a ogni giro; `push --force` e `reset --hard` restano **negati** |

L'hook parla **una volta sola per sessione**: se l'eccezione è stata invocata —
«questo non pusharlo» — il secondo controllo lascia passare e non insiste.

> [!note] Analisi di Claude — 2026-08-28
> L'unico punto in cui la regola può rompersi in silenzio è una macchina Windows
> senza Git Bash: lo script dell'hook è bash, e lì non partirebbe. Non è un
> problema di correttezza — il vault resta a posto e la regola in `CLAUDE.md`
> vale comunque — ma su quella macchina verrebbe a mancare la rete di sicurezza.
> Da verificare la prima volta che si apre una sessione dal PC Windows di Nicola.

## Collegamenti

[[setup-macchina-nuova]] · [[convenzioni]] · [[team-e-vincoli]]
