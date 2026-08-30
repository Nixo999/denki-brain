# Second brain di DenkiCode — leggere prima di toccare

Vault Obsidian versionato con git. Non è documentazione di codice: è la
**memoria dell'azienda** — chi siamo, cosa abbiamo costruito e con quali scelte,
come sta andando adesso. Il codice ha la sua documentazione, dentro i suoi repo.

**Chi scrive qui**: Nicola (da più PC) e Patrick (dal suo MacBook, con un
account GitHub proprio). Giulia **non** ha accesso: provvigioni e crediti
stanno in chiaro.

⚠️ **Patrick non scrive codice, ma il suo Mac non è più disarmato.** Dal
28 agosto 2026 su quel Desktop ci sono i repo (`smoothduty`, `opero-sito`,
`opero-core`, `capacitor`) e da lì **si applicano le modifiche al database di
DenkiShift, sul progetto di sviluppo**. Se ti chiede una modifica allo schema,
si può fare: il come sta in [[modifiche-al-database]], il perché in
[[2026-08-28-supabase-denkishift-sul-mac]]. **La produzione resta fuori**, su
tutti e due i prodotti.

## Chi siamo

DenkiCode, software house e digital agency, **Seveso (MB)**, attiva **da luglio
2026**. Tre persone:

| Chi | Ruolo | Cosa fa davvero |
|---|---|---|
| **Patrick Sappa** (21) | Co-founder | Unica voce commerciale. Liste, trattativa, chiusura, porta-a-porta |
| **Nicola Larezza** (22) | Co-founder, lead dev | Scrive tutto il codice. Parla al cliente solo su dettaglio tecnico |
| **Giulia Venneri** (21) | Cold calls, a provvigione | Primo contatto telefonico sulle liste di Patrick |

Quattro prodotti a listino: siti vetrina, e-commerce, **DenkiShift** (turni,
prodotto di punta), gestionali custom. Dettaglio in [[prodotti-e-listino]].

## Il protocollo — si applica prima di tutto

Dal 30 agosto 2026 l'assistente si chiama **Trevis** (prima JARVIS, vedi
[[2026-08-30-nome-trevis]]) e opera su un livello base
attivo a ogni avvio, in ogni cartella: [[protocollo-trevis]] (di cosa si occupa
e con che priorità) e [[registro-trevis]] (come parla). Fuori dal vault li
richiama `~/.claude/CLAUDE.md`, che è **locale alla macchina** e su un PC nuovo
va ricreato da [[claude-md-globale]].

Le regole qui sotto restano tutte valide: il protocollo non le sostituisce, dice
in che ordine si guardano.

## Le cose che sbaglieresti senza istruzioni

1. **Le credenziali non entrano mai qui.** Il vault sta su GitHub: una chiave
   scritta in una nota è scritta per sempre, anche cancellandola al commit dopo.
   Se qualcuno te ne passa una, **non scriverla in nessun file** — spiega come
   si distribuiscono e rimanda a [[credenziali]].
2. **Nessuna P.IVA.** Si opera in prestazione occasionale. Quando generi testi
   commerciali si dice **"ricevuta"** e **"collaborazione occasionale/
   promozionale"** — mai "fattura elettronica", mai contratti B2B di fornitura
   continuativa. Vincolo attivo finché Nicola non dà il via libera. Vedi
   [[vincoli-fiscali]].
3. **Scrivi per Patrick, non per Nicola.** Ogni testo che uscirà verso un
   cliente ha la voce di Patrick. Nicola compare solo se il cliente chiede
   dettagli tecnici, presentato come "Lead Developer".
4. **Due registri, da non confondere.** Quando *parli con loro*: il registro
   di Trevis, scritto per esteso in [[registro-trevis]] — **si legge prima di
   rispondere, in ogni modalità**, ed è quello che rende una sessione identica
   alla precedente. Niente gergo.
   Quando *scrivi materiale per i clienti*: tono DenkiCode — diretto, giovane,
   problem-solving, nessuna fuffa, con la voce di Patrick. Il primo registro
   non deve mai colare nel secondo, né viceversa.
5. **Il "Lei" e il "Tu" non sono gusto, sono posizione.** Giulia sempre "Lei"
   al telefono. Patrick apre col "Lei" e chiede il passaggio al "Tu" in
   apertura di meeting. Vedi [[stile-comunicazione]].
6. **Il collo di bottiglia è la generazione lead**, non il closing e non lo
   sviluppo. Quando proponi qualcosa, chiediti prima se aiuta lì. Vedi
   [[generazione-lead]], la cadenza fissa in [[ciclo-settimanale]] (4 liste
   ogni domenica, 5 report indietro), e il materiale operativo in
   [[metodo-liste]], [[script-giulia-denkishift]] e [[pattern-interrupt]].
7. **Tutti e tre lavorano e studiano.** DenkiCode è il terzo impegno di
   ciascuno: ~25h di negozio e l'università in corso. Prima di proporre
   qualcosa che costa ore, leggi [[team-e-vincoli]].
8. **DenkiShift non è "pronto".** Il materiale di vendita dice che lo è: è
   ottimismo commerciale. È dimostrabile, non installabile in produzione.
   Non promettere date senza leggere [[denkishift]].
9. **OperO non è il gestionale di un cliente: è il prodotto di un cliente.**
   [[sebastian-torres]] è un privato che sta aprendo la sua attività, e la sua
   attività è quell'app. Lui la rivende alle aziende — la prima è l'impresa di
   suo padre. Chi tocca l'area Super Admin sta toccando il suo conto economico.
10. **I prezzi a listino sono indicativi.** 200-300€ è l'aggancio costruito
   sulla bozza che immaginiamo noi; il prezzo vero si adatta alla richiesta.
11. **Due gestionali, due stack diversi.** OperO è Vite 8 + Tailwind 3, commenti
   in inglese. DenkiShift è Next 16 + Tailwind 4, commenti in italiano. Non
   confonderli e non "uniformare" niente di tua iniziativa: è una
   [[2026-08-28-stack-non-uniforme|decisione aperta]].
12. **Gli script non si improvvisano.** Ogni testo commerciale — script di
   Giulia, obiezioni, aperture di blitz, chiusure, analisi dei report — si
   costruisce su uno dei framework di [[core-commerciale]], e si dichiara
   quale. Il consiglio di vendita generico è vietato dal 28 agosto 2026, vedi
   [[2026-08-28-core-commerciale]].
13. **Ogni operazione si guarda come processo, non come favore.** Dal 30 agosto
   2026 vale il [[core-strutturale]]: quello che si fa due volte diventa una
   SOP delegabile (E-Myth), una funzione nuova entra solo se il mercato l'ha
   chiesta e nella versione minima che risolve (Lean), un servizio si vende a
   pacchetto e il fuori-pacchetto costa tariffa piena o si rifiuta (Built to
   Sell). Sta **sopra** al [[core-commerciale]], che resta il come si scrive un
   testo. Vedi [[2026-08-30-core-strutturale]].

14. **«Non ha il sito» è una cosa che si verifica, non che si deduce.** Dal
   30 agosto 2026 il segnale di una lista siti **non si prende da Pagine
   Gialle**: si cerca su Google, si controlla il dominio e lo si apre. Se
   scrivo «non ha sito», il sito non deve esistere; se scrivo «ce l'ha ed è
   vecchio», devo aver visto cosa lo rende vecchio e dirlo. Una riga non
   verificata **non entra in lista**. Vedi [[2026-08-30-verifica-sito-reale]] e
   [[metodo-liste]].

15. **L'offerta si costruisce, il prezzo non si sconta, l'utile si mette via
   per primo.** Dal 30 agosto 2026 vale il [[core-crescita-finanze]]: un
   pacchetto si ingegnerizza sull'equazione del valore e porta sempre una
   garanzia su ciò che controlliamo (Hormozi), il materiale si costruisce anche
   per il 97% che oggi dice «non adesso» e che buttiamo (Suby), e ogni incasso
   si alloca a **Incassi − Utile = Spese** prima di guardare le spese
   (Michalowicz). **Quando la trattativa si blocca sulla cifra la risposta è un
   bonus o una garanzia, mai un prezzo più basso.** Sta accanto al
   [[core-strutturale]], sopra al [[core-commerciale]]. Vedi
   [[2026-08-30-core-crescita-finanze]].

## Mappa delle cartelle

Tre cartelle per il **lavoro**, divise per lato: tecnico, commerciale, il resto.
Le altre non sono argomenti, sono strati di tempo e di stato — una nota ci passa,
non ci abita.

```
00-Inbox/        catture al volo, non ancora sistemate. Si svuota, non si accumula
01-Coding/       il lato tecnico
  progetti/      un file per progetto ATTIVO. Chiuso → si sposta in 04-Archive/
  stack/         tecnologie e convenzioni di codice
  strumenti/     gli attrezzi e come sono configurati
  skills/        quale skill si usa per quale lavoro
02-Sales/        il lato commerciale
  clienti/       un file per cliente o per lead qualificato
  script/        cosa si dice: aperture, script, obiezioni
  liste/         chi si chiama: il metodo e le liste vere
  contratti/     accordi e ricevute
  report/        i numeri del funnel
  processo/      come si vende: flusso, lead, listino, stile, materiale offline
03-Storage/      il resto del materiale di lavoro
  azienda/       stato, obiettivi, vincoli fiscali
  team/          chi fa cosa, orari, macchine
  sistemi/       dove stanno le credenziali — mai quali sono
  brand/         logo e sorgenti di stampa: gli unici binari del vault
04-Archive/      progetti chiusi e lead persi. Non si cancella niente: si archivia
05-Decisioni/    una decisione per file, datata. Non si riscrive: se ne aggiunge una nuova
06-Daily/        note di giornata e handoff di fine sessione
99-Templates/    template da copiare quando si crea una nota nuova
```

**Un progetto sta in `01-Coding/progetti/`, il cliente che lo paga in
`02-Sales/clienti/`.** Sono due note diverse che si linkano: la prima dice com'è
fatto, la seconda quanto vale e a che punto è la trattativa.

## Naming

- File in `kebab-case`, sempre. `sito-albybike.md`, non `Sito Albybike.md`.
- Note datate: `YYYY-MM-DD-titolo.md`. Vale per `05-Decisioni/` e `06-Daily/`.
- **Un nome, un file.** Il sito di Albybike è `sito-albybike`, il cliente è
  `albybike`. Se collidono, i wikilink puntano alla cosa sbagliata.

## Frontmatter

Obbligatorio su ogni nota. Le dashboard di Dataview leggono questi campi: un
campo scritto male non dà errore, fa **sparire la nota** dalla tabella.

```yaml
# Progetto
type: progetto
status: attivo | in-pausa | completato
client: nome-cliente        # slug del file in 02-Sales/clienti/
stack: [next, supabase]
started: YYYY-MM-DD
deadline: YYYY-MM-DD        # o TODO
updated: YYYY-MM-DD
```

```yaml
# Cliente
type: cliente
status: attivo | dormiente | chiuso
progetti: [slug, slug]
updated: YYYY-MM-DD
```

```yaml
# Decisione
type: decisione
data: YYYY-MM-DD
progetto: nome              # o "azienda" se è una scelta trasversale
```

Campi trasversali usati anche altrove: `type: area | risorsa | daily |
template`, `updated`, `source`, `tags`.

## Separazione dei contenuti — la regola che non si negozia

Quello che scrivono Nicola e Patrick è **conoscenza autentica**. Quello che
genero io è **materiale derivato**, e va sempre riconoscibile.

- `source: denkicode` → detto o scritto da voi. È la verità.
- `source: claude` → analisi, riassunto o bozza mia. Va verificato prima di
  usarlo con un cliente.
- `source: repo` → estratto dal codice o dai `docs/` di un repository. È
  affidabile ma **fotografa il momento in cui l'ho letto**: controlla `updated`.

Dentro una nota `source: denkicode`, ogni blocco mio va marcato così:

```markdown
> [!note] Analisi di Claude — 2026-08-28
> Testo generato. Non è farina del sacco di Nicola o Patrick.
```

**Non mescolare mai le due cose senza segnalarlo.** Se non sei sicuro di dove
viene un'informazione, scrivi `TODO` e chiedi. Un buco dichiarato vale più di
una certezza inventata — è la stessa regola che vale nei repo di codice.

## Come si aggiorna il vault

1. **Prima di scrivere, cerca — e cerca in [[indice]].** Nove volte su dieci la
   nota esiste già e va aggiornata, non duplicata: due note sullo stesso cliente
   producono due verità. L'indice elenca tutte le note con una riga a testa e
   **costa meno di una ricerca**. Una nota nuova ci si aggiunge subito: un
   indice vecchio fa concludere che una nota non esiste, ed è così che nasce il
   doppione.
2. **`updated` si tocca a ogni modifica sostanziale.** È il campo su cui gira
   `/settimana` e il controllo dei progetti fermi.
3. **Le decisioni non si riscrivono.** Se una scelta cambia, si crea una nota
   nuova in `05-Decisioni/` che cita quella vecchia. La storia serve.
4. **I wikilink si mettono generosamente.** `[[opero]]`, `[[sebastian-torres]]`,
   `[[stack]]`. Un link a una nota che non esiste ancora non è un errore: è un
   promemoria di cosa manca.
5. **Numeri con la data accanto.** "400€ incassati" senza data invecchia male e
   nessuno sa più se è ancora vero.
6. **Ogni modifica si pusha, subito.** Anche una riga, anche un `updated`
   corretto. Vale da qualunque macchina e in qualunque sessione: si finisce il
   lavoro con `git pull --rebase` → `git add` → `git commit` → `git push`, senza
   aspettare la fine della giornata e senza che nessuno lo chieda. **L'unica
   eccezione è che l'utente dica esplicitamente di non pushare.** Se il push non
   passa, non si forza: `git pull --rebase` e si riprova. Decisione del
   28 agosto 2026, vedi [[2026-08-28-push-automatico]].
7. **Ogni modifica a un progetto va in due posti.** Nel repository del
   progetto (commit col perché, e voce nel diario del repo se ce l'ha) **e**
   in [[registro-interventi]], una riga: chi, quando, che progetto, che
   repository, **che database**. Quest'ultima colonna è il motivo per cui il
   registro esiste: il push porta il codice e non lo schema, e una migrazione
   non eseguita resta invisibile finché non apre un tabellone vuoto. La riga si
   scrive a lavoro finito, prima di chiudere la sessione. Decisione del
   28 agosto 2026, vedi [[2026-08-28-registro-interventi]].
8. **Fine sessione: `/chiudi-sessione`.** Scrive l'handoff, aggiorna `updated`,
   committa e pusha. Non sostituisce il punto 6: è il riepilogo della giornata,
   non il primo momento in cui il lavoro esce dal portatile.
9. **`git pull` prima di cominciare.** Nicola lavora da più macchine e Patrick
   scrive da sé: partire da un albero vecchio significa scrivere contro
   un'azienda che non esiste più.

## Progetti attivi — indice

| Progetto | Cliente | Stato | Nodo aperto |
|---|---|---|---|
| [[opero]] | [[sebastian-torres]] | 🟡 ~60%, in correzione | 2.000€ da incassare, storico mai migrato, XML SDI da quotare |
| [[denkishift]] | prodotto interno | 🟡 quasi completo, non pubblicato | SMTP proprio, UI generazione turni, 0 clienti |
| [[sito-albybike]] | [[albybike]] | 🟢 Online | Mai pagato, dominio in scadenza fra un anno |
| [[sito-denkicode]] | interno | 🟢 Online | È la **galleria dei lavori**: strumento di vendita, non vetrina passiva |

Archiviati: [[cococat]] (bozza mai riscontrata — lead ancora vivo),
[[sito-dropout]] (eventi di Patrick, sito da galleria), [[webolt-v1]] (vuoto).

## Dove sta il codice

Il vault **non contiene codice**. I repo hanno la loro memoria, ed è buona:

| Progetto | Repo | Memoria del progetto |
|---|---|---|
| OperO | `github.com/Nixo999/opero-sito` | `CLAUDE.md` + `docs/handoff.md` ← leggere per primo |
| DenkiShift | `github.com/Nixo999/smooth-duty` | `CLAUDE.md` + `docs/` (8 file) |

**Se ti serve lo stato tecnico di un progetto, leggi i suoi `docs/`, non questo
vault.** Qui sta il "quanto vale, chi lo paga, dove siamo messi"; là sta il
"come è fatto". Quando le due versioni divergono, ha ragione il repo sul
tecnico e il vault sul commerciale.

## Slash command disponibili

| Comando | Cosa fa |
|---|---|
| `/stato` | **Da lanciare per primo a ogni sessione.** Pull, legge solo l'ultima nota di giornata, risponde in otto righe |
| `/chiudi-sessione` | Handoff di fine giornata, aggiorna `updated`, commit + push |
| `/aggiorna-progetti` | Scansiona i progetti, guarda i commit dei repo, segnala i fermi da 14+ giorni |
| `/settimana` | Cosa è cambiato nel vault negli ultimi 7 giorni |
| `/nuovo-progetto` | Intervista guidata → nota progetto con frontmatter giusto |
| `/nuovo-cliente` | Intervista guidata → nota cliente |
| `/nicola` | **Modalità sviluppo**: aggancia il brain e prepara il lavoro sui progetti software |
| `/patrick` | **Modalità commerciale**: lead, trattative, preventivi, testi che escono verso il cliente |
| `/giulia` | **Modalità telefonate**: liste, script, aperture, obiezioni. Materiale *per* Giulia, che il vault non ce l'ha |

Gli ultimi tre sono **modalità di lavoro**, non procedure: trovano il vault da
soli, leggono solo `CLAUDE.md` e l'ultima nota di giornata, e allargano la
lettura a domanda. Girano da qualunque cartella se copiati anche in
`~/.claude/commands/` — qui dentro sono versionati, così valgono su ogni
macchina.
