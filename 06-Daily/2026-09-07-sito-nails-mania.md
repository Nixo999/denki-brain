---
type: daily
data: 2026-09-07
updated: 2026-09-07
source: claude
progetti: [sito-nails-mania, sito-salone-di-andrea]
canali: [instagram]
---

# 2026-09-07 — Nails Mania sullo scaffale, e la coda del Salone

Sessione a cavallo della mezzanotte, in `/nicola`. Due blocchi: la coda del
[[sito-salone-di-andrea]] (lo specchio che spariva allo scroll, chiuso in
`af2a148`) e il **secondo sito della giornata**, [[sito-nails-mania]].

## Cosa c'è a fine giornata

**Repo `Nixo999/nailsmania-site` (privato), pushato.** Un `index.html`, 12
foto, PRODUCT.md, `netlify.toml` e `robots.txt` con i tre sbarramenti. Non è
online.

## Le tre cose da tenere

- **Il brief di Nicola vale come vincolo di prodotto, e va scritto in
  PRODUCT.md prima del dado**: «artistico, molto bello, non un'estensione del
  loro Instagram». Con foto da telefono e scritte sopra, il sito si regge su
  un sistema grafico suo: le boccette in SVG nei colori veri dei loro gel,
  campionati dalle foto. Il dado ha tirato «la vetrina di smalti», Nicola
  l'ha tenuta.
- **La sede si verifica sulle foto, non solo sulle directory.** Tre fonti
  dicevano Via Dante 66 (sito del 2014, directory vecchie), due dicevano Via
  Brusaporto 1: il biglietto da visita nella foto del 6 giugno 2026 ha
  deciso. Regola 14 del CLAUDE.md, applicata a un indirizzo.
- **Un'idea può essere bella e sbagliata.** Le boccette con la scelta del
  colore erano il dado, Nicola le aveva scelte, ed erano una cosa da guardare:
  «non deve essere un test per vedere le unghie, deve essere un sito vetrina
  di roba già fatta da loro». Rifatto in un'ora come vetrina dei lavori: le
  loro foto, ritagliate per togliere le scritte, in cornici di vetro. Regola:
  **quando il brief dice "vetrina", il contenuto sono i lavori del cliente**,
  anche se le foto sono brutte; il design serve a farle sembrare belle, non a
  sostituirle.
- **«Piatto» vuol dire chiaro.** La seconda versione, porcellana e vetro, era
  passata dalla review ed era pulita: Nicola l'ha bocciata in una riga
  («troppo piatto, mi fa schifo»). Il livello atteso è sempre NG Barber:
  scuro, sipario, titolo gigante, un capitolo appuntato. Per i siti vetrina
  DenkiCode **il registro notte è il default**, non un'opzione: la versione
  chiara si fa solo se la chiede lui. E le foto brutte del cliente non si
  mettono neanche se sono l'unica prova: si scrive che il servizio esiste.
- **`<use>` di un `<symbol>` non prende gli stili del documento**: sette
  boccette nere al primo giro. Grafica che prende colore da CSS va inline.

## Buchi dichiarati

- Orari: le due schede recenti divergono sui minuti; nel sito c'è la parte
  concorde con «da confermare al telefono».
- Ciglia, trucco semipermanente e corsi: dal sito del 2016, non confermati
  nel 2026.
- Finish review di impeccable: due ricatture e un giro di otto fix, dettaglio
  nella scheda del progetto. Le catture headless hanno un'altra trappola:
  `scrollTo(0,y)` con `html{scroll-behavior:smooth}` si ferma a metà; nei
  wrapper serve `behavior:'instant'`.

## Collegamenti

[[sito-nails-mania]] · [[nails-mania]] · [[sito-salone-di-andrea]] ·
[[2026-09-05-instagram-bg-va]] · [[processo-siti]] · [[registro-interventi]]

---

# 2026-09-07 (sera) — Il vault si riordina: indice generato e memoria tecnica

Seconda sessione della giornata, su richiesta di Nicola. Non è lavoro su un
progetto: è lavoro sul brain. Sta in coda a questa nota e non in un file suo
perché a inizio sessione si legge **l'ultima daily in ordine alfabetico**, e un
file `2026-09-07-riorganizzazione-vault.md` verrebbe prima di
`2026-09-07-sito-nails-mania.md`: si perderebbe.

## Fatto

- **`01-Coding/strumenti/genera-indice.py`**: riscrive `indice.md` dai file veri
  e stampa i buchi (link rotti, progetti fuori dalla tabella di `CLAUDE.md`,
  righe del registro senza wikilink, frontmatter senza `type`). Lo lancia
  `/chiudi-sessione`, passo 5. Decisione: [[2026-09-07-indice-generato]].
- **`01-Coding/trappole.md`**: la memoria tecnica che sopravvive all'ultima
  daily. Seminata con quello che era già sparso nel registro e nelle daily.
  `/nicola` la legge a inizio sessione. Decisione:
  [[2026-09-07-trappole-memoria-tecnica]].
- **Il template della daily ha la sezione «Come è stato fatto»**, e
  `/chiudi-sessione` ha il passo che ne travasa il riutilizzabile in
  `trappole.md`.
- **Due progetti veri sono usciti dal buio**: [[sito-castiglione]] (+ cliente
  [[castiglione-furniture]]) e [[sito-ngbarber]] (+ cliente [[ng-barber]]).
  Avevano repo, commit e in un caso un sito pubblicato, e **nessuna scheda**.
- **`indice.md` rigenerato**: 128 note su 128, era fermo al 3 settembre e ne
  conosceva 108. La tabella dei progetti in `CLAUDE.md` passa da 5 righe a 11.
- Corretti: 15 celle del registro che nominavano progetti senza wikilink, il
  frontmatter di due decisioni (`date`/`who` → `type`/`data`), lo `status: lead`
  aggiunto alla specifica dei clienti, e il percorso `~/lavoro/denki-brain` nel
  loop di aggancio di `/nicola`, `/patrick`, `/giulia` — su questo Mac nessuno
  dei tre trovava il vault da solo.
- Nuova nota di catalogo [[processo-siti]]: era il wikilink più citato del vault
  (quindici volte) e non puntava a niente.

## Come è stato fatto

- **La diagnosi non è partita dai file ma dai comandi.** L'indice non era
  indietro per distrazione: le quattro volte in cui i comandi dicono «aggiorna
  l'indice» parlano tutte della **tabella dei progetti in `CLAUDE.md`**, che è
  un altro oggetto. `indice.md` era citato solo come file da leggere. Prima di
  aggiungere una regola conviene cercare quella che c'è già e non viene eseguita.
- **Il generatore fa due mestieri di proposito**: riscrive l'indice (meccanico) e
  segnala quello che una persona deve decidere (la riga della tabella, il nodo
  aperto). Quello che non si può derivare dal frontmatter non lo inventa.
- **Il controllo dei link rotti non basta.** [[sito-ngbarber]] era invisibile
  proprio perché nel registro era **testo semplice**: un progetto scritto senza
  `[[ ]]` non produce nemmeno un link rotto. Da lì il secondo controllo, sulla
  colonna «Progetto» del registro.
- Due errori miei nell'estrazione delle descrizioni, trovati rileggendo l'output
  invece che fidandosi: lo split di frase su `:` tagliava a metà («Obiettivo
  dichiarato:»), e saltare le righe che iniziano con `*` faceva partire la
  descrizione **da metà paragrafo** su ogni nota che apre in grassetto. Si legge
  sempre quello che il generatore ha prodotto, non solo il suo exit code.

## Deciso

- [[2026-09-07-indice-generato]] — l'indice si genera, non si aggiorna a mano.
- [[2026-09-07-trappole-memoria-tecnica]] — le daily diventano la memoria di
  sessione, le lezioni si sedimentano in `trappole.md`.

## Aperto

- ⬜ **[[sito-castiglione]] è davvero online?** Il registro dice «il sito va
  online» e destinazione Netlify, nessuna riga conferma il deploy. Da verificare,
  e se è su vanno controllati i tre sbarramenti anti-indicizzazione.
- ⬜ **[[sito-ngbarber]]: due repo divergenti**, una privata di Nicola indietro di
  un commit e una pubblica di Patrick. Va scelta quale è la buona.
- ⬜ La skill `proposta-commerciale` è citata due volte come wikilink e non ha una
  nota: unico link rotto rimasto, dichiarato.
- ⬜ La tabella dei progetti in `CLAUDE.md` è a 11 righe e cresce di una a
  settimana. Prima o poi va spezzata o ridotta ai soli progetti vivi.

## Non verificato

- Il generatore gira su questo Mac con `python3` di sistema. **Sul PC di Nicola
  non è stato provato**: se là `python3` non è nel PATH, il passo 5 di
  `/chiudi-sessione` fallisce e va detto, non aggirato.
- Le descrizioni dell'indice sono estratte a macchina: sono state lette a
  campione, non tutte e 128.

## Collegamenti

[[trappole]] · [[indice]] · [[registro-interventi]] · [[sito-castiglione]] ·
[[sito-ngbarber]] · [[processo-siti]]
