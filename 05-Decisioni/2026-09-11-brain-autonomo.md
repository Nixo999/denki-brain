---
type: decisione
riga: Il brain si chiude, promuove, pusha e controlla i siti da solo, perche' Patrick non sa fare niente di tutto questo.
data: 2026-09-11
progetto: azienda
source: denkicode
stato: presa
updated: 2026-09-11
verificato: 2026-09-11
---

# Il brain fa da solo, perché Patrick non sa farlo

## Il contesto

Nicola: «Patrick di tutto ciò non capisce niente, quindi quando lo usa lui deve
essere tutto fatto in maniera autonoma dal brain». Più la ricerca sui sistemi di
memoria per agenti, che nomina l'antipattern preciso in cui eravamo: *ideas rot
in daily notes*. La catena che usano è sessione → riassunto → lezione → **nota
di dominio**. Da noi la daily era il capolinea: dodici note di giornata, e
quello che c'era dentro ci restava.

## La decisione

1. **Promozione.** La daily smette di essere il capolinea. A fine sessione ogni
   cosa che vale oltre oggi si sposta dove verrà riletta: `FATTI.md`, la nota
   del progetto, `trappole.md`, `direttive-siti.md`, `convenzioni.md`,
   `05-Decisioni/`. Nella daily resta il link.
2. **`FATTI.md`.** `CLAUDE.md` torna a essere il **manuale** e basta; lo stato
   di adesso sta in un file corto che **si riscrive** invece di accumulare. La
   tabella dei progetti è uscita dal manuale: là invecchiava in silenzio.
3. **Marcatura per affermazione.** Ogni fatto che può invecchiare porta il suo
   segno dentro la riga: niente = non scade, **(data)** = da ricontrollare,
   **→** = vive altrove. `verificato:` sulla nota intera era troppo grosso.
4. **La daily si scrive prima delle domande**, come ipotesi, e le domande la
   promuovono a fonte. **Ribalta l'ordine del 10 settembre**: così esiste anche
   quando nessuno risponde, che è il caso di Patrick.
5. **Il push lo fa l'hook.** Non ricorda più di pushare: fa `pull --rebase`,
   commit e push. Non forza mai, e se si ferma lo dice.
6. **`cerca.py`.** Ricerca per rilevanza con FTS5 di sqlite, solo libreria
   standard: nessuna installazione, funziona identico sul Mac di Patrick. Non è
   semantica vera — servirebbe un modello di embedding da scaricare, e lui non
   può — ma copre il caso che rompeva `grep`.
7. **`controlla-sito.py`.** Misura un sito contro il livello di NG Barber e
   Fiftynine, che passano 8 su 8. Se esce 1 non si pubblica. È il «mai
   peggiorare» reso eseguibile.
8. **`direttive-siti.md`.** Ogni bocciatura di Nicola, verbatim, con la regola
   che ne esce. Cresce e non si accorcia: è il «migliorare nel tempo».

## Cosa si è scartato

**La ricerca semantica con embedding.** Vorrebbe Ollama e un modello da
scaricare: su questa macchina non c'è, e sul Mac di Patrick non ci arriverà.
Un pezzo che funziona solo dove c'è Nicola non è autonomia.

**Gli agenti schedulati notturni** che riconciliano il vault da soli: girano
solo se l'app è aperta, e nessuno se ne accorgerebbe se smettessero.

## Conseguenze aperte

L'hook che pusha da solo può committare lavoro a metà: il commit lo dichiara.
`FATTI.md` è scritto a mano oggi, e resta vero solo se ogni chiusura lo
riscrive. Gli undici siti già fatti non passano il controllo tranne quattro.

## Collegamenti

[[FATTI]] · [[direttive-siti]] · [[come-si-scrive-una-nota]] ·
[[2026-09-10-memoria-verificata]]
