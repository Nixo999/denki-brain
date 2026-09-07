---
description: Handoff di fine sessione — scrive la nota di giornata, aggiorna updated, commit e push
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
---

> **Base**: `03-Storage/azienda/protocollo-trevis.md` (di cosa ci si occupa) e
> `03-Storage/azienda/registro-trevis.md` (come si parla) — si leggono prima di
> rispondere, in questa come in ogni altra modalità. Niente presentazioni,
> niente «adesso procedo a», niente proposte su cosa fare dopo. Riprendi come se
> la conversazione non si fosse mai interrotta.

Chiudi la sessione di lavoro di oggi sul vault DenkiCode.

## 1. Capire su cosa si è lavorato

Non chiederlo se puoi dedurlo. Guarda, in quest'ordine:

- la conversazione di questa sessione
- `git status` e `git diff` nel vault
- se durante la sessione si è lavorato su un repo di codice
  (`opero-sito`, `smooth-duty`), guarda anche i suoi commit di oggi

Se dopo questo il progetto è ancora ambiguo, **chiedi**: una sola domanda,
con le opzioni che hai trovato.

## 2. Scrivere la nota di giornata

Crea `06-Daily/YYYY-MM-DD-<slug>.md` usando `99-Templates/template-daily.md`.
Se la nota di oggi esiste già, **aggiungici in coda invece di sovrascriverla**.

Lo slug descrive il lavoro, non la data: `2026-08-28-opero-liste-cliente.md`.

Compila tutte le sezioni:

- **Fatto** — solo cose finite, non tentativi
- **Come è stato fatto** — la strada tecnica presa. Non è il riassunto del
  codice: è quello che serve a chi riprende senza aver visto niente. Qui va il
  caso concreto
- **Deciso** — se una decisione è importante, aprile anche una nota in
  `05-Decisioni/` e qui lascia solo il link
- **Aperto** — a che punto esatto è rimasta la cosa a metà. Chi riprende deve
  ripartire da qui senza rileggere il codice
- **Prossimi passi** — il primo per primo
- **Non verificato** — cosa è stato scritto ma non provato, e perché.
  Non saltare questa sezione: è la regola di casa

## 3. La memoria tecnica

Ogni riga della sezione **Come è stato fatto** che vale anche su un progetto che
ancora non esiste va copiata in `01-Coding/trappole.md`, nella sua sezione,
ridotta a *trappola → contromisura → dove è stata pagata*. Se una trappola c'era
già, si aggiunge il progetto dove è ricomparsa: una ricomparsa è la prova che il
file serve.

Non ci va il resoconto della giornata — quello resta nella daily. Se non è
uscito niente di riutilizzabile, non si scrive niente: un file lungo non lo
rileggo.

## 4. Aggiornare le note toccate

Per ogni progetto o cliente su cui si è lavorato:

- porta `updated:` alla data di oggi
- aggiorna la sezione **Aperto** — spunta ciò che è chiuso, aggiungi il nuovo
- se sono cambiati soldi, stato o scadenza, aggiorna i campi del frontmatter
- aggiorna la tabella dei progetti in `CLAUDE.md` se è nato un progetto o è
  cambiato uno stato. La colonna «Nodo aperto» la scrive una persona: il
  generatore la segnala mancante, non la inventa

## 5. Rigenera l'indice — non si aggiorna a mano

```bash
python3 01-Coding/strumenti/genera-indice.py
```

Riscrive `indice.md` dai file veri e stampa i buchi: link rotti, progetti attivi
fuori dalla tabella di `CLAUDE.md`, righe del registro con un progetto scritto
come testo invece che come wikilink, frontmatter senza `type`. **I buchi si
guardano**: è così che un progetto vero resta senza scheda per una settimana.

Quello che non risolvi, dillo in due righe invece di lasciarlo passare.

## 6. Commit e push

```bash
git add -A
git status --short
```

Mostra cosa stai per committare. Poi committa con un messaggio che rispetta la
convenzione DenkiCode ([[convenzioni]]): **in italiano, dice cosa è cambiato e
perché**, non l'elenco dei file.

✅ `Il cliente di OperO ha rimesso l'XML in scope: da qui si quota`
❌ `update opero.md`

Poi `git push`. Se il push fallisce, **non forzare**: `git pull --rebase`,
guarda il risultato e riprova.

## 7. Chiudi

Due righe all'utente: cosa hai scritto e cosa resta per domani. Niente riepilogo
lungo — la nota di giornata è già il riepilogo.
