---
type: decisione
riga: Le daily non si scrivono più - la giornata sta nel registro interventi, lo stato in FATTI sotto le 80 righe. Approvata da Nicola il 27/09/2026.
data: 2026-09-27
progetto: vault
updated: 2026-09-27
source: denkicode
tags: [vault, daily, registro, fatti]
---

# Le daily chiudono: la giornata sta nel registro, lo stato in FATTI

**Approvata da Nicola il 27 settembre 2026**, dopo l'analisi del vault:
«ok va bene applica queste modifiche».

## Il fatto

- 12 daily in un mese, l'ultima del 13/09. Dopo: 12 giorni di lavoro con
  commit, 21 chiusure automatiche, zero daily.
- `/stato` leggeva «la daily più recente»: per due settimane ogni sessione ha
  letto il 13/09 come «ieri».
- Il [[registro-interventi]] nello stesso periodo ha ricevuto 275 commit: chi,
  quando, che giro, che verdetto. Era già la daily, con un altro nome.
- `FATTI.md` è passato da 69 righe (11/09) a 223 (26/09) assorbendo il
  racconto dei giri: il file che dice «si riscrive, non si accumula» accumulava.

## La scelta

1. **Niente più daily.** `06-Daily/` resta come storia: non si cancella, non si
   scrive.
2. **La giornata sta nel registro**: `/chiudi-sessione` scrive la riga lì, e le
   cinque domande di chiusura correggono quella riga e le note toccate.
3. **`FATTI.md` sotto le 80 righe, tetto duro**: una riga per cosa aperta, il
   racconto dei giri nella nota progetto. `genera-indice.py` lo misura.
4. `/stato`, `/nicola`, `/patrick`, `/giulia` e `/settimana` leggono FATTI e la
   testa del registro invece della daily.

## Scartato

- Rimettersi a scrivere la daily: due file per la stessa giornata, e uno dei
  due è rimasto vuoto per quattordici giorni.
- Tenere FATTI come diario: a 223 righe non era più «lo stato di adesso», e
  costava 14.000 caratteri a ogni sessione.

## Conseguenze

- [[come-si-scrive-una-nota]]: la riga «Daily, 40 righe» è superata, entra
  «FATTI, 80 righe».
- `99-Templates/template-daily.md` resta, non si usa.
- Com'è andata un giorno prima del 13/09 sta in `06-Daily/`; dopo, nel registro.

## Collegamenti

[[registro-interventi]] · [[FATTI]] · [[come-si-scrive-una-nota]] ·
[[2026-09-27-verificato-in-chiusura]]
