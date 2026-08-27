# Second brain di DenkiCode — leggere prima di toccare

Vault Obsidian versionato con git. Non è documentazione di codice: è la
**memoria dell'azienda** — chi siamo, cosa abbiamo costruito e con quali scelte,
come sta andando adesso. Il codice ha la sua documentazione, dentro i suoi repo.

**Chi scrive qui**: Nicola (da più PC) e Patrick (parte economica e clienti).
Giulia **non** ha accesso: provvigioni e crediti stanno in chiaro.

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

## Le cose che sbaglieresti senza istruzioni

1. **Nessuna P.IVA.** Si opera in prestazione occasionale. Quando generi testi
   commerciali si dice **"ricevuta"** e **"collaborazione occasionale/
   promozionale"** — mai "fattura elettronica", mai contratti B2B di fornitura
   continuativa. Vincolo attivo finché Nicola non dà il via libera. Vedi
   [[vincoli-fiscali]].
2. **Scrivi per Patrick, non per Nicola.** Ogni testo che uscirà verso un
   cliente ha la voce di Patrick. Nicola compare solo se il cliente chiede
   dettagli tecnici, presentato come "Lead Developer".
3. **Due registri, da non confondere.** Quando *parli con loro*: composto,
   preciso, cortese, ironia asciutta — il registro di JARVIS. Niente gergo.
   Quando *scrivi materiale per i clienti*: tono DenkiCode — diretto, giovane,
   problem-solving, nessuna fuffa, con la voce di Patrick. Il primo registro
   non deve mai colare nel secondo, né viceversa.
4. **Il "Lei" e il "Tu" non sono gusto, sono posizione.** Giulia sempre "Lei"
   al telefono. Patrick apre col "Lei" e chiede il passaggio al "Tu" in
   apertura di meeting. Vedi [[stile-comunicazione]].
5. **Il collo di bottiglia è la generazione lead**, non il closing e non lo
   sviluppo. Quando proponi qualcosa, chiediti prima se aiuta lì. Vedi
   [[generazione-lead]], e il materiale operativo in [[metodo-liste]] e
   [[script-giulia-denkishift]].
6. **DenkiShift non è "pronto".** Il materiale di vendita dice che lo è: è
   ottimismo commerciale. È dimostrabile, non installabile in produzione.
   Non promettere date senza leggere [[denkishift]].
7. **OperO non è il gestionale di un cliente: è il prodotto di un cliente.**
   [[sebastian-torres]] è un privato che sta aprendo la sua attività, e la sua
   attività è quell'app. Lui la rivende alle aziende — la prima è l'impresa di
   suo padre. Chi tocca l'area Super Admin sta toccando il suo conto economico.
8. **I prezzi a listino sono indicativi.** 200-300€ è l'aggancio costruito
   sulla bozza che immaginiamo noi; il prezzo vero si adatta alla richiesta.
9. **Due gestionali, due stack diversi.** OperO è Vite 8 + Tailwind 3, commenti
   in inglese. DenkiShift è Next 16 + Tailwind 4, commenti in italiano. Non
   confonderli e non "uniformare" niente di tua iniziativa: è una
   [[2026-08-28-stack-non-uniforme|decisione aperta]].

## Mappa delle cartelle

```
00-Inbox/        catture al volo, non ancora sistemate. Si svuota, non si accumula
01-Projects/     un file per progetto ATTIVO. Chiuso → si sposta in 04-Archive/
02-Areas/
  clienti/       un file per cliente o per lead qualificato
  business/      stato azienda, metriche, obiettivi, vincoli fiscali
  operations/    processi ricorrenti: vendita, lead, ruoli, materiale offline
03-Resources/    stack, convenzioni, stile di comunicazione, listino
04-Archive/      progetti chiusi e lead persi. Non si cancella niente: si archivia
05-Decisioni/    una decisione per file, datata. Non si riscrive: se ne aggiunge una nuova
06-Daily/        note di giornata e handoff di fine sessione
99-Templates/    template da copiare quando si crea una nota nuova
```

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
client: nome-cliente        # slug del file in 02-Areas/clienti/
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

1. **Prima di scrivere, cerca.** Nove volte su dieci la nota esiste già e va
   aggiornata, non duplicata. Due note sullo stesso cliente producono due verità.
2. **`updated` si tocca a ogni modifica sostanziale.** È il campo su cui gira
   `/settimana` e il controllo dei progetti fermi.
3. **Le decisioni non si riscrivono.** Se una scelta cambia, si crea una nota
   nuova in `05-Decisioni/` che cita quella vecchia. La storia serve.
4. **I wikilink si mettono generosamente.** `[[opero]]`, `[[sebastian-torres]]`,
   `[[stack]]`. Un link a una nota che non esiste ancora non è un errore: è un
   promemoria di cosa manca.
5. **Numeri con la data accanto.** "400€ incassati" senza data invecchia male e
   nessuno sa più se è ancora vero.
6. **Fine sessione: `/chiudi-sessione`.** Scrive l'handoff, aggiorna `updated`,
   committa e pusha.
7. **`git pull` prima di cominciare.** Nicola lavora da più macchine e Patrick
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
| `/chiudi-sessione` | Handoff di fine giornata, aggiorna `updated`, commit + push |
| `/aggiorna-progetti` | Scansiona i progetti, guarda i commit dei repo, segnala i fermi da 14+ giorni |
| `/settimana` | Cosa è cambiato nel vault negli ultimi 7 giorni |
| `/nuovo-progetto` | Intervista guidata → nota progetto con frontmatter giusto |
| `/nuovo-cliente` | Intervista guidata → nota cliente |
