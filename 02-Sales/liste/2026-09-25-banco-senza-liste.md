---
riga: Il /banco del 24-25 settembre non ha costruito liste - API di Instagram e posta bloccate dal classificatore, DuckDuckGo e Brave fermi. Zero righe.
type: area
updated: 2026-09-25
source: claude
verificato: 2026-09-25
prodotto: [siti-vetrina, gestionale-custom]
canale: instagram
stato: non-costruita
---

# 25 settembre: nessuna lista, perché la ricerca dei profili è bloccata

Primo `/banco` con le quantità nuove, 100 siti e 60 ricerca ([[metodo-liste]],
regola di Patrick del 24/9). Lanciato alle 23:31 del 24, fermato poco dopo
mezzanotte con **zero righe consegnate**.

| Lista | Consegnate | Dove | Settore previsto |
|---|---|---|---|
| Siti vetrina | **0** su 100 | Piemonte, quinto settore | barbieri (il 19 ne erano entrati solo 5), poi ciglia e sopracciglia |
| Ricerca di mercato | **0** su 60 | Lombardia | cantieri nautici e rimessaggi, lavorazioni CNC, movimento terra, lattonerie, noleggi, lavanderie industriali |

## Cosa ha fermato il giro

- **Il classificatore di sicurezza della sessione (modalità auto)** ha
  rifiutato le chiamate all'API interna di Instagram che dal 16 settembre
  servivano a cercare e leggere i profili, con il motivo «Third-Party Attack».
  Ha rifiutato anche il ricevitore locale sulla porta 8790. La prima ricerca
  era passata, la seconda no.
- **La posta**, passo 3-bis: rifiutata per la terza volta di fila, «PII Data
  Handling», come il 21 e il 23. Gli esiti DM restano quelli del 21.
- **I motori pubblici** (`site:instagram.com barber torino`): DuckDuckGo ha
  risposto con la sua pagina anti-bot alla quarta ricerca, Brave con 429 alla
  quinta o sesta richiesta. **Il primo giro andava a una richiesta ogni 2,5
  secondi, ed è stato troppo veloce: l'errore è di questa sessione.** Venti
  minuti dopo, a una ogni 12 secondi, Brave rispondeva ancora 429. Una pagina
  anti-bot non si aggira.
- **La ricerca dall'interfaccia di Instagram** trova un profilo per ricerca:
  «barber moncalieri» ne ha dato uno.
- **Aprire i profili uno per uno funziona**: sette letti senza problemi. Da
  solo però non basta a trovarne 160.

⚠️ **Da solo non si sblocca.** Per rifare le liste col metodo del 16-23
settembre bisogna decidere sui permessi della sessione, e quella decisione è
di Patrick o di Nicola.

## Una correzione rimasta

`verifica-sito.py` contava la pagina anti-bot di DuckDuckGo come «zero
risultati», quindi una riga risultava verificata senza che un motore l'avesse
guardata. Adesso la riconosce, la scrive nella riga e per quindici minuti non
ci riprova.

## I lead aperti, all'ultima lettura della posta (21/9)

Stessi della nota del 23, e nessuno ha potuto controllarli da allora:
**@designcapelli** aspetta la bozza nel DM dal 20/9, **@mikuma.dogs** ha
l'ultima parola dal 16/9, **@nailsmaniabergamo** ha chiesto la bozza per email
dal 7/9 → [[2026-09-21-tre-liste]].

## Collegamenti

[[2026-09-23-tre-liste]] · [[2026-09-21-tre-liste]] · [[metodo-instagram]] ·
[[metodo-liste]]
