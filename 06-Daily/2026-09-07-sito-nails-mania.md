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

## Pomeriggio — il banco DM, e 34 righe svizzere in più

Patrick ha chiesto due cose: **aggiorna il banco DM e aprimelo**, e poi
**«devo mandare 65 DM oggi, tutti della Svizzera italiana»**.

- **Il banco era aperto su una lista vecchia.** Il `git pull` d'avvio si era
  fermato su `.obsidian/graph.json` sporco, quindi la pagina servita era quella
  di prima delle liste ticinesi. Sistemato il file (conflitto sullo zoom del
  grafo, risolto tenendo il valore di questa macchina), il banco vede le liste
  di oggi.
- **Il conto vero degli invii vive nel browser, non nei file.** Patrick dice
  che sul suo banco risultavano tutte partite; `lista-corrente.csv` ne dava 68
  ancora da mandare. Le due cose non si contraddicono: le spunte stanno nel
  `localStorage` e nel CSV non ci arrivano mai. **Prima di ricaricare il banco
  va premuto «Scarica»**, o quelle date si perdono e i recuperi non si
  accendono.
- **34 righe nuove**, tutte Sotto Ceneri, appese a `lista-corrente.csv`: 153 →
  187 righe, 110 da mandare. Con le 8 del mattino, oggi sull'account di Patrick
  ci sono **42 righe svizzere, non 65** — 95 profili guardati, 36% passato.
  Dettaglio, scartati e trappole in [[2026-09-07-instagram-ticino]].
- **Il resolver DNS della macchina mente.** Dava per morti domini vivi
  (`treatwell.ch`, `sirmarcus.ch`): ogni verdetto «dominio morto» ora si
  incrocia su Cloudflare e Google DoH. Senza quel controllo cinque righe
  avrebbero detto una bugia.
- **Una riga del mattino corretta**: la pagina Wix di `@angolodiros_mendrisio`
  oggi risponde 404, quindi il gancio passa da «è una pagina su Wix» a «quella
  pagina non esiste più».

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

## Pomeriggio — il banco DM, e 34 righe svizzere in più

Patrick ha chiesto due cose: **aggiorna il banco DM e aprimelo**, e poi
**«devo mandare 65 DM oggi, tutti della Svizzera italiana»**.

- **Il banco era aperto su una lista vecchia.** Il `git pull` d'avvio si era
  fermato su `.obsidian/graph.json` sporco, quindi la pagina servita era quella
  di prima delle liste ticinesi. Sistemato il file (conflitto sullo zoom del
  grafo, risolto tenendo il valore di questa macchina), il banco vede le liste
  di oggi.
- **Il conto vero degli invii vive nel browser, non nei file.** Patrick dice
  che sul suo banco risultavano tutte partite; `lista-corrente.csv` ne dava 68
  ancora da mandare. Le due cose non si contraddicono: le spunte stanno nel
  `localStorage` e nel CSV non ci arrivano mai. **Prima di ricaricare il banco
  va premuto «Scarica»**, o quelle date si perdono e i recuperi non si
  accendono.
- **34 righe nuove**, tutte Sotto Ceneri, appese a `lista-corrente.csv`: 153 →
  187 righe, 110 da mandare. Con le 8 del mattino, oggi sull'account di Patrick
  ci sono **42 righe svizzere, non 65** — 95 profili guardati, 36% passato.
  Dettaglio, scartati e trappole in [[2026-09-07-instagram-ticino]].
- **Il resolver DNS della macchina mente.** Dava per morti domini vivi
  (`treatwell.ch`, `sirmarcus.ch`): ogni verdetto «dominio morto» ora si
  incrocia su Cloudflare e Google DoH. Senza quel controllo cinque righe
  avrebbero detto una bugia.
- **Una riga del mattino corretta**: la pagina Wix di `@angolodiros_mendrisio`
  oggi risponde 404, quindi il gancio passa da «è una pagina su Wix» a «quella
  pagina non esiste più».

## Collegamenti

[[trappole]] · [[indice]] · [[registro-interventi]] · [[sito-castiglione]] ·
[[sito-ngbarber]] · [[processo-siti]]

---

# 2026-09-07 (tarda sera) — Il banco DM raddoppia, e si passa il confine

Terza sessione, in `/nicola`, su richiesta di Patrick. Non è lavoro su un sito:
è lo strumento di outreach più il pescato.

## Fatto

- **Il [banco DM](../02-Sales/strumenti/banco-dm.html) ha due postazioni**:
  Patrick Sappa e DenkiCode. Selettore in testata, una memoria per account, una
  lista per account, **un tetto per account** — 65 e 15. Decisione:
  [[2026-09-07-due-account-dm]].
- **Due liste ticinesi**, 8 righe per Patrick (Sotto Ceneri) e 9 per DenkiCode
  (Sopra Ceneri), col messaggio già scritto in colonna →
  [[2026-09-07-instagram-ticino]].
- Allineati [[dm-instagram-vetrina]] (gancio 1 impersonale, variante aziendale)
  e il percorso del vault in `Banco DM.command`, che su questo Mac non lo
  trovava.

## Come è stato fatto

- **Il tetto è dell'account, non di Instagram.** È la sola parte del banco che
  poteva fare danno copiata così com'era: 65 è una misura fatta su un profilo
  maturo, e applicarla a un profilo nato ieri è il modo di perderlo.
- **Il testo aziendale è stato sbagliato al primo giro**, e l'errore si vedeva
  solo leggendo il messaggio generato: «abbiamo guardato il profilo» seguito da
  un gancio in prima persona singolare. Le due varianti condividono il
  dizionario dei ganci, quindi i ganci devono essere impersonali. Si legge
  sempre l'output, non il diff.
- **Le liste ticinesi sono corte perché il Ticino è servito.** 28 profili
  esaminati, 17 col dominio proprio: passa il 39%, contro il 12 su 14 della
  Brianza. Chi il sito non ce l'ha, ha Fresha o Treatwell; chi ce l'ha, gliel'ha
  fatto un'agenzia locale.
- **Trappola geografica**: `@lugano.barbershop` sembra perfetto e sta a Buenos
  Aires (indirizzo Av. Larrazabal, prefisso argentino). Su una ricerca per nome
  di città il comune si verifica sempre, come il sito.

## Aperto

- ✅ **Chiuso in coda di sessione**: le 8 righe ticinesi di Patrick sono state
  appese a `lista-corrente.csv` (76 da mandare), e `/patrick` adesso apre dal
  banco. Vedi la sezione di chiusura, sotto.
- ⬜ Il tetto di DenkiCode va alzato a mano, dieci al giorno, ogni giorno che
  regge. Nessuno lo fa da solo.
- ⬜ Mendrisiotto e Chiassese hanno dato due righe: per quella zona serve un
  altro modo di pescare.

## Non verificato

- Nessuno dei 17 profili è stato aperto su Instagram: handle, follower e
  attività vengono dalle SERP. Vale il passo 2 di [[metodo-instagram]] prima di
  scrivere.
- Il messaggio ticinese non è passato dalla skill [[voce-denkicode]]: è scritto
  applicandone le regole a mano.

## Pomeriggio — il banco DM, e 34 righe svizzere in più

Patrick ha chiesto due cose: **aggiorna il banco DM e aprimelo**, e poi
**«devo mandare 65 DM oggi, tutti della Svizzera italiana»**.

- **Il banco era aperto su una lista vecchia.** Il `git pull` d'avvio si era
  fermato su `.obsidian/graph.json` sporco, quindi la pagina servita era quella
  di prima delle liste ticinesi. Sistemato il file (conflitto sullo zoom del
  grafo, risolto tenendo il valore di questa macchina), il banco vede le liste
  di oggi.
- **Il conto vero degli invii vive nel browser, non nei file.** Patrick dice
  che sul suo banco risultavano tutte partite; `lista-corrente.csv` ne dava 68
  ancora da mandare. Le due cose non si contraddicono: le spunte stanno nel
  `localStorage` e nel CSV non ci arrivano mai. **Prima di ricaricare il banco
  va premuto «Scarica»**, o quelle date si perdono e i recuperi non si
  accendono.
- **34 righe nuove**, tutte Sotto Ceneri, appese a `lista-corrente.csv`: 153 →
  187 righe, 110 da mandare. Con le 8 del mattino, oggi sull'account di Patrick
  ci sono **42 righe svizzere, non 65** — 95 profili guardati, 36% passato.
  Dettaglio, scartati e trappole in [[2026-09-07-instagram-ticino]].
- **Il resolver DNS della macchina mente.** Dava per morti domini vivi
  (`treatwell.ch`, `sirmarcus.ch`): ogni verdetto «dominio morto» ora si
  incrocia su Cloudflare e Google DoH. Senza quel controllo cinque righe
  avrebbero detto una bugia.
- **Una riga del mattino corretta**: la pagina Wix di `@angolodiros_mendrisio`
  oggi risponde 404, quindi il gancio passa da «è una pagina su Wix» a «quella
  pagina non esiste più».

## Collegamenti

[[2026-09-07-due-account-dm]] · [[2026-09-07-instagram-ticino]] ·
[[dm-instagram-vetrina]] · [[metodo-instagram]] · [[registro-interventi]]

---

# 2026-09-07 (mattina) — V-BAG: Giulia pubblica da sola, e il primo giro col modello operatore

Terza sessione della giornata. Sta in coda qui per lo stesso motivo delle
altre: a inizio sessione si legge l'ultima daily in ordine alfabetico.

## Fatto

- **Modalità direttore/operatore**, chiesta da Nicola: `~/.claude/agents/operatore.md`
  con `model: opus`. Il direttore legge, decide e rivede; l'operatore implementa,
  misura e dichiara i buchi. Non pubblica e non digita credenziali.
- **`vbag-site` è su GitHub**, `Nixo999/vbag-site` privato, ramo `master`. La
  repo l'ha creata Nicola dal PC Windows: fino a stamattina il sito esisteva solo
  su quel Desktop, senza remote. Clonato in `~/lavoro`.
- **`admin.html`**: Giulia entra con mail e password, carica una foto, scrive
  nome, descrizione e due campi facoltativi, e la borsa compare in fondo ai
  modelli e nel menu del form ordine. Può anche toglierla.
- **`supabase.sql`** con tabella, bucket e RLS. **Non eseguito**: il progetto
  Supabase non esiste ancora.
- Corretto un difetto vecchio del sito: `button.link-line` batteva `[hidden]` e
  il pulsante «Esci» era visibile prima del login.

## Come è stato fatto

- **Il repo comanda, e ha deciso l'architettura.** Il `CLAUDE.md` di `vbag-site`
  dice «niente build, niente dipendenze» e self-hosta i font per il GDPR: da lì
  la scelta di chiamare Supabase con `fetch` nudo invece di `@supabase/supabase-js`
  da CDN. Non è purismo, è la regola scritta nel repo che vince sul comodo.
- **Le due borse esistenti non si migrano.** Hanno foto scontornate con rembg su
  pannelli tarati a mano; quelle di Giulia arrivano dal telefono con lo sfondo.
  Sono due trattamenti diversi (`.look-stage` galleggia, `.look-foto` inquadra) e
  mescolarli avrebbe rotto la direzione. Deciso prima di passare il brief, non
  dopo aver visto il risultato.
- **La sicurezza non poteva dipendere da un interruttore nel pannello.** La
  chiave anon sta in chiaro nella pagina: se le registrazioni restano aperte,
  chiunque si iscrive e diventa `authenticated`. Le policy adesso controllano la
  mail di chi entra, con un segnaposto che **fallisce chiuso**. Rivisto in
  direzione, non era nel brief.
- **Il primo giro col modello operatore ha funzionato**, con due cose da tenere:
  l'operatore ha riportato una trappola nuova che non conoscevo (a pane nascosto
  è stale anche `getComputedStyle`, non solo il pixel), e ha silenziosamente
  cambiato `python` in `python3` nel `launch.json` perché qui `python` non
  esiste. La prima è finita in [[trappole]], la seconda va detta a Nicola: su
  Windows quel comando è `python`.

## Aperto

- ⬜ **Tocca a Nicola**: creare il progetto Supabase, eseguire `supabase.sql`,
  incollare URL e chiave anon in `supabase.js`, creare l'utente di Giulia con
  «Auto Confirm User», spegnere le registrazioni e **scrivere la sua mail dentro
  `puo_pubblicare()`**. Finché non è fatto il sito è identico a ieri.
- ⬜ Hosting mai deciso: il sito non è online da nessuna parte.
- ⬜ Il numero WhatsApp è ancora vuoto in `script.js`.

## Non verificato

- **Tutto il percorso con Supabase vero**: login, upload nel bucket, insert,
  delete e RLS effettivamente applicate. Servono progetto e credenziali, che non
  digito io. `supabase.sql` non è mai passato da Postgres: la sintassi non è
  validata.
- Safari su iPhone: encoding webp del canvas e orientamento EXIF delle foto fatte
  col telefono. È il browser da cui Giulia userà la pagina, quindi è il buco che
  pesa di più.
- La scadenza del token dopo un'ora: gestita a 401 con «sessione scaduta», mai
  vista succedere.

## Pomeriggio — il banco DM, e 34 righe svizzere in più

Patrick ha chiesto due cose: **aggiorna il banco DM e aprimelo**, e poi
**«devo mandare 65 DM oggi, tutti della Svizzera italiana»**.

- **Il banco era aperto su una lista vecchia.** Il `git pull` d'avvio si era
  fermato su `.obsidian/graph.json` sporco, quindi la pagina servita era quella
  di prima delle liste ticinesi. Sistemato il file (conflitto sullo zoom del
  grafo, risolto tenendo il valore di questa macchina), il banco vede le liste
  di oggi.
- **Il conto vero degli invii vive nel browser, non nei file.** Patrick dice
  che sul suo banco risultavano tutte partite; `lista-corrente.csv` ne dava 68
  ancora da mandare. Le due cose non si contraddicono: le spunte stanno nel
  `localStorage` e nel CSV non ci arrivano mai. **Prima di ricaricare il banco
  va premuto «Scarica»**, o quelle date si perdono e i recuperi non si
  accendono.
- **34 righe nuove**, tutte Sotto Ceneri, appese a `lista-corrente.csv`: 153 →
  187 righe, 110 da mandare. Con le 8 del mattino, oggi sull'account di Patrick
  ci sono **42 righe svizzere, non 65** — 95 profili guardati, 36% passato.
  Dettaglio, scartati e trappole in [[2026-09-07-instagram-ticino]].
- **Il resolver DNS della macchina mente.** Dava per morti domini vivi
  (`treatwell.ch`, `sirmarcus.ch`): ogni verdetto «dominio morto» ora si
  incrocia su Cloudflare e Google DoH. Senza quel controllo cinque righe
  avrebbero detto una bugia.
- **Una riga del mattino corretta**: la pagina Wix di `@angolodiros_mendrisio`
  oggi risponde 404, quindi il gancio passa da «è una pagina su Wix» a «quella
  pagina non esiste più».

## Collegamenti

[[trappole]] · [[registro-interventi]] · [[2026-09-07-instagram-ticino]] ·
[[2026-09-07-due-account-dm]] · [[metodo-instagram]] · [[dm-instagram-vetrina]] · [[credenziali]]

---

# 2026-09-07 (chiusura) — `/patrick` apre dal banco, non dal riepilogo

Coda della sessione precedente. Chiesto da Nicola: quando Patrick lancia il suo
comando, la prima cosa che deve avere in mano sono le liste e un banco già
aggiornato.

## Fatto

- **`02-Sales/strumenti/stato-banco.py`**: legge i due CSV pubblicati e stampa,
  per account, quante conversazioni restano, quante sono partite oggi e quali
  recuperi sono maturi. **I tetti li legge dall'HTML del banco** con una regex,
  così i due numeri non possono divergere.
- **`/patrick` ha un passo nuovo, prima della lettura del vault**: lancia lo
  script e apre la risposta con quella riga. Se una lista sta in
  `02-Sales/liste/` e non è ancora sul banco, la pubblica **appendendola**.
- **Le 8 righe ticinesi di Patrick sono sul banco**: `lista-corrente.csv` passa
  a 153 righe, 76 da mandare. DenkiCode resta a 9 con tetto 15.
- Le copie in `~/.claude/commands/` erano ferme al 6 settembre (quattro file):
  allineate a quelle versionate nel vault.

## Come è stato fatto

- **Il conteggio dei giorni lavorativi è stato copiato dal banco, non
  riscritto.** Al primo giro contava da domani invece che dal giorno
  dell'invio: uno sfasamento di un giorno che avrebbe acceso i recuperi con
  ventiquattr'ore di anticipo, e nessuno se ne sarebbe accorto guardando il
  numero. Provato sulle date vere: il 3 settembre matura mercoledì 9, che è
  quello che diceva la nota della lista del 5.
- **Appendere, non sostituire.** È la regola che il canale ha già pagato una
  volta: un CSV sostituito porta via le date degli invii, e con esse i
  recuperi. Scritta nel comando, non solo qui.
- **Lo script non sa quanti DM sono partiti davvero.** Quel conto vive nel
  localStorage del browser di Patrick e rientra nel CSV solo quando scarica la
  lista aggiornata. Scritto nel comando come avvertimento: se lui dice venti e
  lo script dice zero, ha ragione lui.

## Aperto

- ⬜ Il tetto di DenkiCode resta da alzare a mano, dieci al giorno.
- ⬜ Nessuno dei 17 profili ticinesi è stato aperto su Instagram prima di
  finire sul banco: la verifica del profilo tocca a chi manda.

## Pomeriggio — il banco DM, e 34 righe svizzere in più

Patrick ha chiesto due cose: **aggiorna il banco DM e aprimelo**, e poi
**«devo mandare 65 DM oggi, tutti della Svizzera italiana»**.

- **Il banco era aperto su una lista vecchia.** Il `git pull` d'avvio si era
  fermato su `.obsidian/graph.json` sporco, quindi la pagina servita era quella
  di prima delle liste ticinesi. Sistemato il file (conflitto sullo zoom del
  grafo, risolto tenendo il valore di questa macchina), il banco vede le liste
  di oggi.
- **Il conto vero degli invii vive nel browser, non nei file.** Patrick dice
  che sul suo banco risultavano tutte partite; `lista-corrente.csv` ne dava 68
  ancora da mandare. Le due cose non si contraddicono: le spunte stanno nel
  `localStorage` e nel CSV non ci arrivano mai. **Prima di ricaricare il banco
  va premuto «Scarica»**, o quelle date si perdono e i recuperi non si
  accendono.
- **34 righe nuove**, tutte Sotto Ceneri, appese a `lista-corrente.csv`: 153 →
  187 righe, 110 da mandare. Con le 8 del mattino, oggi sull'account di Patrick
  ci sono **42 righe svizzere, non 65** — 95 profili guardati, 36% passato.
  Dettaglio, scartati e trappole in [[2026-09-07-instagram-ticino]].
- **Il resolver DNS della macchina mente.** Dava per morti domini vivi
  (`treatwell.ch`, `sirmarcus.ch`): ogni verdetto «dominio morto» ora si
  incrocia su Cloudflare e Google DoH. Senza quel controllo cinque righe
  avrebbero detto una bugia.
- **Una riga del mattino corretta**: la pagina Wix di `@angolodiros_mendrisio`
  oggi risponde 404, quindi il gancio passa da «è una pagina su Wix» a «quella
  pagina non esiste più».

## Collegamenti

[[2026-09-07-instagram-ticino]] · [[2026-09-07-due-account-dm]] ·
[[metodo-instagram]] · [[registro-interventi]]

---

# 2026-09-07 (mezzogiorno) — V-BAG senza database: lo store diventa un file

Nicola ha bocciato Supabase a poche ore dall'averlo montato: «sono poche borse,
non serve un database vero, sfrutta file interni». Rifatto.

## Fatto

- **Supabase via**, non svuotato: `supabase.js` e `supabase.sql` cancellati.
  Con loro se ne vanno login, token, RLS e la mappatura di 401 e 403. Il
  progetto Supabase non era ancora stato creato, quindi non resta niente da
  disfare: nessuna migrazione in sospeso.
- **Lo store è `dati/borse.json` più le foto in `assets/borse/`**, letti dalla
  home al caricamento.
- **`admin.html` cambia natura**: non è più un'area riservata, è uno strumento
  locale. Non protegge niente perché non scrive da nessuna parte se non sul
  disco di chi la apre. Con la File System Access API scrive foto e JSON dentro
  la cartella del sito; senza, consegna gli stessi due file da scaricare.
- 197 righe di codice contro 251.

## Come è stato fatto

- **Il vincolo vero non è tecnico, è di flusso.** Con i file, pubblicare vuol
  dire fare un commit: dal computer Giulia arriva ai file pronti, dal telefono
  no. Su iOS la File System Access API non esiste e un download non entra in
  git. L'ho scritto nel `CLAUDE.md` e fatto dire alla pagina con parole sue,
  invece di lasciarlo scoprire a lei. Era la condizione per non avere un
  database: si accetta, ma dichiarata.
- **Il difetto vero l'ha trovato la revisione, non l'operatore.** Il `fetch` di
  `dati/borse.json` prendeva la copia in cache — `http.server` manda
  `Last-Modified` e nessun `Cache-Control` — quindi una borsa appena messa
  online non si vedeva. Non era un problema del test: sarebbe successo anche in
  produzione. Corretto con `cache: 'no-cache'`, che rivalida invece di saltare
  la cache. L'ho visto perché le due voci finte non comparivano e ho misurato
  invece di ricaricare e sperare.
- **La modalità operatore regge, ma la revisione non è una formalità.** In due
  giri l'operatore ha consegnato codice giusto e misurato, e in tutti e due ho
  trovato in revisione una cosa che cambiava il comportamento vero: la prima
  volta le regole di scrittura che si fidavano del solo `authenticated`, la
  seconda la cache. Il direttore che si limita a leggere il rapporto non serve
  a niente.

## Aperto

- ⬜ **Il ramo `showDirectoryPicker` non è mai stato eseguito**: serve un gesto e
  un permesso veri, nel pannello parte sempre il fallback. Va provato a mano su
  Chrome da computer prima di dire a Giulia che funziona.
- ⬜ Safari su iPhone mai provato: encoding webp del canvas, orientamento EXIF e
  i due download di fila.
- ⬜ Hosting mai deciso, numero WhatsApp ancora vuoto.

## Non verificato

- Tutto quello che sta sopra, più: nessun test runnable lasciato nel repo.
  L'unica logica isolabile è `slug()`, provata a mano.

## Pomeriggio — il banco DM, e 34 righe svizzere in più

Patrick ha chiesto due cose: **aggiorna il banco DM e aprimelo**, e poi
**«devo mandare 65 DM oggi, tutti della Svizzera italiana»**.

- **Il banco era aperto su una lista vecchia.** Il `git pull` d'avvio si era
  fermato su `.obsidian/graph.json` sporco, quindi la pagina servita era quella
  di prima delle liste ticinesi. Sistemato il file (conflitto sullo zoom del
  grafo, risolto tenendo il valore di questa macchina), il banco vede le liste
  di oggi.
- **Il conto vero degli invii vive nel browser, non nei file.** Patrick dice
  che sul suo banco risultavano tutte partite; `lista-corrente.csv` ne dava 68
  ancora da mandare. Le due cose non si contraddicono: le spunte stanno nel
  `localStorage` e nel CSV non ci arrivano mai. **Prima di ricaricare il banco
  va premuto «Scarica»**, o quelle date si perdono e i recuperi non si
  accendono.
- **34 righe nuove**, tutte Sotto Ceneri, appese a `lista-corrente.csv`: 153 →
  187 righe, 110 da mandare. Con le 8 del mattino, oggi sull'account di Patrick
  ci sono **42 righe svizzere, non 65** — 95 profili guardati, 36% passato.
  Dettaglio, scartati e trappole in [[2026-09-07-instagram-ticino]].
- **Il resolver DNS della macchina mente.** Dava per morti domini vivi
  (`treatwell.ch`, `sirmarcus.ch`): ogni verdetto «dominio morto» ora si
  incrocia su Cloudflare e Google DoH. Senza quel controllo cinque righe
  avrebbero detto una bugia.
- **Una riga del mattino corretta**: la pagina Wix di `@angolodiros_mendrisio`
  oggi risponde 404, quindi il gancio passa da «è una pagina su Wix» a «quella
  pagina non esiste più».

## Collegamenti

[[trappole]] · [[registro-interventi]] · [[2026-09-07-instagram-ticino]] ·
[[2026-09-07-due-account-dm]] · [[metodo-instagram]] · [[dm-instagram-vetrina]]
