---
riga: Il cervello di denki-agents - memoria, regista e fermate umane in un Postgres solo con pgvector, e il prompt si compone a budget.
type: decisione
data: 2026-09-16
progetto: denki-agents
source: denkicode
stato: presa
---

# Il cervello sta in un database solo: Postgres con pgvector, e il prompt si compone a budget

## Il contesto

Nicola, 16 settembre 2026: «costruisci il brain», e subito dopo «il database del
brain voglio che sia vettoriale e studiato al minimo dettaglio, la ricerca deve
essere super efficiente e deve richiedere pochissimi token per chiamata».

Patrick intanto ha chiesto otto agenti: i due banchi DM, le liste chiamate per
Giulia e per momo, due che mandano posta, uno che manda le mail segnate da chi
telefona, e uno che analizza i DM. Il pacchetto della fase 1 copre solo il
gateway verso i modelli: la memoria, la sequenza e le fermate non esistevano.

## La decisione

1. **Il cervello e' memoria, sequenza e fermate**, scritto in `docs/spec-fase-2.md`
   dentro il repo, che sul tecnico vince su questa nota. Sette tabelle nuove, un
   regista che legge la coda ed e' anche il calendario, nove flussi.
2. **Un database solo: Postgres con pgvector.** Niente servizio vettoriale
   separato. Il `WHERE` esatto e la somiglianza stanno nella stessa query, e il
   backup e' uno.
3. **I vettori stanno in una tabella sola**, `indice_semantico`, con un indice
   HNSW parziale per tipo e la ricerca **ibrida**: vettore piu' testo italiano,
   fusi con RRF. Ogni pezzo porta il suo `riferimento`, quindi si cita e si
   controlla.
4. **Il prompt si compone a budget**: scheda dei fatti da SQL, regole ed esempi
   recuperati, tetto per task in `task_routing.tetto_token_input`. La misura vera
   e' `esecuzioni.token_input`, non il preventivo.
5. **Le fermate umane restano**: Nicola approva le bozze, Patrick approva ogni
   testo e ogni prezzo, i DM li manda una persona.
6. **La posta obbedisce alla decisione del 2 settembre**: si scrive a chi l'ha
   chiesto e alle persone giuridiche con casella generica, agli altri no.

## Cosa si e' scartato

- **Un database vettoriale separato** (Pinecone, Qdrant, Chroma): un servizio in
  piu' da tenere acceso e da salvare, e due verita' da riallineare, per un indice
  che sta in poche decine di migliaia di righe.
- **Portare i file interi nel prompt**: i file delle direttive e degli script
  crescono, e il costo cresce con loro a ogni chiamata.
- **Far mandare i DM a un agente**: Instagram non permette il primo messaggio da
  API, ed e' gia' agli atti dal 2 settembre.

## Conseguenze aperte

- La fase 1 non e' ancora costruita: il cervello non parte prima.
- Il modello di embedding non e' scelto: verifica in corso sulle pagine ufficiali.
- Il cantiere dei siti resta una sessione Claude Code con gli strumenti, non una
  chiamata sola: e' da li' che escono i siti a 8/8.
- `momo` non si sa chi sia, e una lista chiamate ha bisogno di un destinatario.

## Collegamenti

[[denki-agents]] · [[2026-09-14-denki-agents-parte-dal-gateway]] ·
[[2026-09-02-cold-email-gestionali]] · [[2026-09-02-automazione-dm-instagram]]
