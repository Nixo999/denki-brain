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
| `.claude/hooks/ricorda-push.sh` + `.claude/settings.json` | Hook `Stop`: a fine turno controlla se ci sono modifiche non committate o commit non inviati, e in quel caso lo segnala. Dipende solo da bash e git — **niente `jq`**, vedi sotto |
| `.claude/settings.json`, sezione `permissions` | `git add`, `commit`, `push`, `pull` non chiedono più conferma a ogni giro; `push --force` e `reset --hard` restano **negati** |

L'hook parla **una volta sola per sessione**: se l'eccezione è stata invocata —
«questo non pusharlo» — il secondo controllo lascia passare e non insiste.

> [!note] Verificato sul PC Windows — 2026-08-28, stessa giornata
> Il dubbio era fondato, ma la causa era un'altra: **Git Bash c'è** (5.2.37,
> msys), quello che manca è **`jq`**. La prima versione dell'hook lo usava per
> leggere l'id di sessione e per comporre la risposta: senza, moriva con
> `jq: command not found` **senza stampare niente e uscendo con 0**. Cioè il
> fallimento peggiore possibile — nessun errore visibile e nessuna rete di
> sicurezza, proprio sulla macchina dove si lavora di più.
>
> **Risolto togliendo `jq`**: l'id di sessione si estrae con `sed`, la risposta
> è JSON scritto a mano. Nessuna dipendenza oltre a bash e git.
>
> Verificate tutte e tre le condizioni su Windows: albero pulito → tace; albero
> sporco → emette JSON valido con `decision: block`; secondo Stop della stessa
> sessione → tace, così l'eccezione «non pushare» regge.
>
> ⚠️ La lezione generale, che vale oltre questo hook: **un hook che fallisce in
> silenzio è peggio di un hook che non esiste**, perché ci si conta sopra. Se se
> ne scrive un altro, va provato sulla macchina più povera di strumenti, non
> sulla più ricca.

## Collegamenti

[[setup-macchina-nuova]] · [[convenzioni]] · [[team-e-vincoli]]
