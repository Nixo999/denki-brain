---
type: area
updated: 2026-09-08
source: claude
prodotto: [siti-vetrina, denkishift]
stato: da-provare
---

# Metodo nuove aperture — dove si vede chi sta aprendo

> [!note] Nota generata da Claude — 2026-09-08
> Nasce dalla domanda di Patrick dopo la chiusura del test DM
> ([[2026-09-08-test-dm-chiuso]]). **Le fonti sono verificate, la resa no**:
> nessuna riga di questo metodo è ancora stata provata sul campo.

## Perché chi apre vale più di chi c'è già

Tre differenze rispetto a una lista normale di [[metodo-instagram]], e la terza
è quella che conta:

1. **Il budget è già stanziato.** Chi apre ha messo da parte i soldi per farsi
   vedere: insegna, menù, volantini. Il sito è nella stessa voce di spesa, e
   non deve essere strappato a un bilancio che gira da anni.
2. **Non è ancora saturo.** Un'attività aperta da dieci anni ha detto no a
   trenta agenzie. Una che apre non l'ha ancora sentita nessuno.
3. **Ha una data, e la data è nostra alleata.** È l'unico lead che porta con sé
   una scadenza vera, e una scadenza è ciò che manca a tutte le trattative
   ferme di [[metriche]]. «Fine ottobre» non esiste per chi apre il 15.

⚠️ **Il gancio cambia, e va riscritto.** I sei ganci di
[[dm-instagram-vetrina]] parlano di siti morti, vecchi o parcheggiati: a chi
apre non si applicano. Il suo problema non è un sito brutto, è che **il giorno
che apre non esiste su Google**.

## Le fonti, in ordine di costo

### 1. Google Maps, gratis e immediata

Il posto dove il segnale è **doppio**: dice che è nuovo e dice se ha il sito.

- Si cerca la categoria nel comune e si guarda **la data delle recensioni**.
  Poche recensioni, tutte degli ultimi due mesi, è un'attività appena aperta.
- Sulla stessa scheda si legge se il campo **sito web** è vuoto: è il passo 3
  di [[metodo-instagram]] già mezzo fatto.
- Le schede nuove restano spesso senza sito per settimane: è la finestra.

### 2. Instagram, gratis

Chi apre lo annuncia, e lo annuncia **prima**: «nuova apertura», «coming
soon», «vi aspettiamo dal», il conto alla rovescia nelle storie. Si cerca per
località e si guarda **la data del primo post**: un profilo con dodici post,
tutti di questo mese, è un'attività che sta nascendo.

### 3. Gli annunci di lavoro, gratis — e valgono doppio

**Chi apre assume.** Un annuncio «cercasi personale per nuova apertura» sul
gruppo Facebook del paese, su Subito o su Indeed è il segnale più forte che
esista, e vale per tutti e due i prodotti:

- per il **sito**, dice che sta aprendo;
- per [[denkishift]], dice una cosa che nessun'altra fonte dice: **ha dei
  dipendenti**, quindi ha dei turni. È il filtro degli 8 dipendenti dello
  script, letto da fuori, senza chiedere niente a nessuno.

### 4. La stampa locale online, gratis

Le testate locali pubblicano le aperture, ed è il loro pane. Per Milano
esistono rubriche mensili dedicate (`cibotoday.it`), e il circuito copre anche
il territorio di Lecco (`leccotoday.it`).
⬜ `TODO` **da verificare**: se esiste la rubrica «nuove aperture» anche per
Como, Varese e Bergamo, o se lì la notizia va cercata a mano.

### 5. L'elenco della Camera di Commercio, a pagamento — la fonte pulita

**Verificato l'8 settembre 2026.** Le Camere di Commercio vendono gli
**elenchi merceologici**: liste di imprese estratte dal Registro Imprese e
filtrate per **codice ATECO**, **comune o provincia**, stato dell'impresa e
**data di iscrizione**. È esattamente la query che serve: *le imprese iscritte
dopo il tal giorno, con quel codice, in questi comuni*.

| | |
|---|---|
| Camera competente per Como e Lecco | **Como-Lecco**, una sola richiesta per due province |
| Diritti di segreteria | **20 €**, qualunque sia l'elenco |
| Costo totale | variabile sul numero di imprese: l'ufficio manda un preventivo, che **scade in 5 giorni** se non lo si accetta |
| Consegna | **CSV via email**, cioè già il formato del banco |
| Pagamento | pagoPA dal portale SIPA, causale «Richiesta elenchi» |

Varese e Bergamo hanno camere proprie: stessa procedura, preventivo a parte.

> [!warning] La lista dice chi ha aperto, non autorizza a scrivergli
> Il Registro Imprese contiene indirizzi PEC ed email, e **quelle non si usano
> per il primo contatto commerciale**: è esattamente il caso sanzionato dal
> Garante e già messo a verbale in [[2026-09-02-cold-email-gestionali]] — un
> dato pubblico non è un dato consentito.
> Il contatto parte dal **numero pubblico dell'attività**, per telefono, o di
> persona. La lista serve a sapere **chi chiamare**, non a mandare mail.

### Quello che non è una fonte affidabile

**Le SCIA e le pratiche SUAP.** Sono l'atto con cui un'attività apre davvero e
sarebbero il segnale perfetto, ma passano da `impresainungiorno.gov.it` e dai
portali dei singoli comuni, e **non esiste un elenco pubblico consultabile**
delle pratiche presentate. Verificato l'8 settembre 2026. Andrebbe controllato
comune per comune, e costa più di quanto rende.

## Il momento in cui si chiama

> [!note] Ipotesi di Claude — 2026-09-08, da misurare
> **Chi ha appena aperto ha speso tutto e non ha una lira**, e nelle prime
> settimane è nel caos. **Chi apre fra un mese ha il budget ancora in mano.**
> L'ipotesi è che la finestra utile stia **prima dell'apertura o dopo le prime
> quattro settimane**, e che il mese subito dopo l'inaugurazione sia il momento
> peggiore. Non è misurato: si segna la data di apertura in lista e dopo venti
> chiamate si guarda quale gruppo ha risposto.

## Come si usa, senza aprire un canale nuovo

Non è un canale: **è una lista diversa per il telefono che esiste già**. Le
regole restano quelle di casa:

- **Il telefono lavora vicino** e Instagram lontano
  ([[2026-08-31-stop-porta-a-porta-a-freddo]]): una nuova apertura in Brianza
  si chiama, una a Bergamo si scrive.
- La lista passa da `controlla-lista.py` e da `verifica-sito.py` come le altre
  ([[metodo-instagram]], passi 3 e 4).
- L'esito si scrive con le sei parole fisse, o il giro non misura niente.

## Collegamenti

[[metodo-instagram]] · [[metodo-liste]] · [[generazione-lead]] · [[metriche]] ·
[[2026-09-08-test-dm-chiuso]] · [[2026-09-02-cold-email-gestionali]] ·
[[denkishift]] · [[dm-instagram-vetrina]]
