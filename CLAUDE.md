# Second brain di DenkiCode

Vault Obsidian versionato con git. È la **memoria dell'azienda**: chi siamo,
cosa abbiamo costruito, come sta andando. Il codice ha la sua documentazione,
dentro i suoi repo.

DenkiCode, software house e digital agency, **Seveso (MB)**, attiva da luglio
2026. **Patrick Sappa** (unica voce commerciale), **Nicola Larezza** (lead dev,
scrive tutto il codice), **Giulia Venneri** (cold call a provvigione, **non ha
accesso al vault**: qui provvigioni e crediti stanno in chiaro).

## Come si legge questo vault — prima di tutto il resto

**Si leggono `FATTI.md` e `indice.md`, non le note.** Il primo dice lo stato di
adesso, il secondo dice cosa contiene ogni nota.

**Cerca per rilevanza, non a tentoni**: `python3 01-Coding/strumenti/cerca.py
<parole>` pesa più parole insieme e ordina le note. `grep` trova solo la parola
che hai scritto.

**Si legge `indice.md`, non le note.** Ogni nota dichiara nel frontmatter una
`riga:` che dice cosa contiene; l'indice le raccoglie tutte. Da lì si decide
quale file aprire. Aprire una nota per scoprire cosa c'è dentro è l'errore che
brucia il contesto prima del lavoro.

**Una nota `source: claude` senza `verificato:` è un'ipotesi.** Si legge per
orientarsi, non si cita come fatto, non ci si costruisce sopra codice, non ne
esce niente verso un cliente. Prima si controlla contro la cosa vera — il repo,
il sito online, il database, una persona — poi si scrive la data.

**Un errore registrato non è una regola.** [[trappole]] contiene trappole
pagate e strade scartate, non dottrina. Il modo giusto di fare una cosa sta in
[[convenzioni]], nel `CLAUDE.md` del repo o in una decisione, e ce lo mette una
persona di proposito.

Le tre cose per esteso, con i tetti di lunghezza delle note, stanno in
[[come-si-scrive-una-nota]]. Si legge una volta, non a ogni sessione.

## Le regole che costano se le sbagli

1. **Le credenziali non entrano mai qui.** Il vault sta su GitHub: una chiave
   scritta in una nota è scritta per sempre. Non si scrivono e non si digitano:
   le inserisce la persona. → [[credenziali]]
2. **Nessuna P.IVA.** Prestazione occasionale. Nei testi commerciali si dice
   **"ricevuta"** e **"collaborazione occasionale"**, mai "fattura elettronica",
   mai contratti B2B continuativi. → [[vincoli-fiscali]]
3. **Ogni testo che esce verso un cliente ha la voce di Patrick.** Nicola
   compare solo sul dettaglio tecnico, come "Lead Developer". Il registro con
   cui parlo a voi tre ([[registro-trevis]]) non cola mai nel testo che legge un
   cliente ([[stile-comunicazione]]), né viceversa.
4. **Sul tecnico ha ragione il repo, non il vault.** Qui sta quanto vale un
   progetto e chi lo paga; il `CLAUDE.md` e i `docs/` del repository dicono
   com'è fatto, e vincono su qualunque riassunto.
5. **DenkiShift non è "pronto".** È dimostrabile, non installabile in
   produzione. Non si promettono date. → [[denkishift]]
6. **OperO è il prodotto di un cliente, non il gestionale di un cliente.**
   [[sebastian-torres]] lo rivende alle aziende. Chi tocca l'area Super Admin
   sta toccando il suo conto economico. → [[opero]]
7. **La produzione resta fuori**, su tutti e due i prodotti. Il Mac di Patrick
   applica modifiche allo schema di DenkiShift **in sviluppo**. →
   [[modifiche-al-database]]
8. **Se non sai da dove viene un'informazione, scrivi `TODO` e chiedi.** Un buco
   dichiarato vale più di una certezza inventata.

Il resto non è una regola d'ingresso: si legge quando il compito lo chiede.
Il collo di bottiglia è la generazione lead ([[generazione-lead]]), i prezzi a
listino sono indicativi ([[prodotti-e-listino]]), i due gestionali hanno stack
diversi e restano diversi ([[stack]]), ogni progetto esce firmato
([[convenzioni]]), «non ha il sito» si verifica ([[metodo-liste]]). I quattro
core — [[core-commerciale]], [[core-strutturale]], [[core-crescita-finanze]],
[[core-produttivita-leadership]] — sono **materiale di consultazione, non un
obbligo**: si aprono quando servono davvero, e non si dichiara più quale
framework si sta usando.

## Mappa delle cartelle

```
00-Inbox/        catture al volo. Si svuota, non si accumula
01-Coding/       il lato tecnico
  registro-interventi.md   una riga per intervento: chi, quando, repo, DATABASE
  trappole.md              errori pagati e strade scartate. Non è un rulebook
  progetti/ stack/ skills/
  strumenti/  gli attrezzi. Qui sta l'unico codice del vault: starter-sito/
02-Sales/        clienti/ script/ liste/ contratti/ report/ processo/
03-Storage/      azienda/ team/ sistemi/ brand/
04-Archive/      progetti chiusi e lead persi. Non si cancella: si archivia
05-Decisioni/    una decisione per file, datata
06-Daily/        note di giornata, max 40 righe, scritte a domande
99-Templates/    da copiare quando si crea una nota nuova
```

Un progetto sta in `01-Coding/progetti/`, il cliente che lo paga in
`02-Sales/clienti/`: due note che si linkano.

## Naming e frontmatter

File in `kebab-case`. Note datate `YYYY-MM-DD-titolo.md` in `05-Decisioni/` e
`06-Daily/`. **Un nome, un file**: il sito è `sito-albybike`, il cliente
`albybike`.

Obbligatori su ogni nota: `type:`, `riga:`, `updated:`, `source:`. Le dashboard
Dataview leggono questi campi: un campo scritto male fa **sparire la nota**
dalla tabella.

```yaml
type: progetto | cliente | decisione | daily | area | risorsa | template
riga: una riga, max 140 caratteri, che dice cosa c'è dentro
updated: YYYY-MM-DD
source: denkicode | claude | repo
verificato: YYYY-MM-DD      # obbligatorio se source: claude
```

Progetto aggiunge `status` (`attivo|in-pausa|completato`), `client`, `stack`,
`started`, `deadline`. Cliente aggiunge `status`
(`lead|attivo|dormiente|chiuso`) e `progetti`. Decisione aggiunge `data` e
`progetto`.

## Come si aggiorna

1. **Prima di scrivere, leggi [[indice]].** Nove volte su dieci la nota esiste
   già e va aggiornata, non duplicata. L'indice non si scrive a mano:
   `python3 01-Coding/strumenti/genera-indice.py` lo riscrive e stampa i buchi.
2. **Si corregge la fonte, mai sopra la fonte.** Se un file dice una cosa
   sbagliata si modifica quel file. Scrivere la correzione altrove lascia due
   verità in circolo, ed è così che il vault ha smesso di funzionare.
   L'eccezione è `05-Decisioni/`, dove una scelta superata si linka da una nota
   nuova: lì la storia serve.
3. **`updated:` a ogni modifica sostanziale.** È il campo su cui gira
   `/settimana`.
4. **Ogni modifica si pusha, subito**, anche una riga:
   `git pull --rebase` → `add` → `commit` → `push`. Se non passa non si forza.
   L'unica eccezione è che l'utente dica di non pushare.
5. **Ogni modifica a un progetto va in due posti**: nel repo (commit col perché)
   e in [[registro-interventi]] — chi, quando, progetto, repository, **quale
   database**. Quella colonna è il motivo per cui il registro esiste: il push
   porta il codice e non lo schema.
6. **`git pull` prima di cominciare.** Nicola lavora da più macchine e Patrick
   scrive da sé.

## Lo stato non sta qui

`CLAUDE.md` è il **manuale**: come si lavora, e cambia di rado. Lo stato di
adesso — chi, soldi, cosa è aperto, cosa è bloccato — sta in **[[FATTI]]**, che
si legge a ogni sessione e **si riscrive** a ogni chiusura invece di accumulare.

Una tabella di progetti dentro il manuale invecchia in silenzio, ed è successo:
per giorni ha elencato progetti che non erano più a quel punto.

## Comandi

`/stato` a inizio sessione · `/chiudi-sessione` a fine · `/nicola` sviluppo ·
`/patrick` commerciale · `/giulia` telefonate · `/aggiorna-progetti` ·
`/settimana` · `/nuovo-progetto` · `/nuovo-cliente`.
