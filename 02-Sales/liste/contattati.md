---
type: area
updated: 2026-09-08
source: claude
canale: instagram
---

# Contattati — a chi abbiamo già scritto su Instagram

Due CSV, scritti dal banco e non a mano. Sono la memoria del canale che prima
stava solo nel localStorage del Mac di Patrick.

| File | Cosa c'è dentro | Chi lo scrive |
|---|---|---|
| `contattati.csv` | Una riga per ogni DM segnato come mandato: data, da quale account, handle, nome, comune, segmento, `primo` o `recupero`, da che lista | `banco-server.py`, al click su «Segna inviato» o «Copia e apri». «Annulla» toglie la riga |
| `gia-col-sito.csv` | I profili che Patrick ha scartato dal banco perché **il sito ce l'avevano**: è il conto degli errori di chi ha fatto la lista | il tasto «Ha già il sito» |

Il server committa e pusha da solo due minuti dopo l'ultimo gesto, e alla
chiusura della finestra. Quindi il file è vero solo se il Mac di Patrick ha
fatto `git pull` una volta dopo l'8 settembre 2026 e il push gli funziona
(verificato il 28 agosto in [[setup-macchina-nuova]]).

**Le 75 righe del 3 settembre** sono il seme: prese da `lista-corrente.csv`,
dove le date erano già segnate. Prima di quel giorno non c'è traccia.

Chi genera una lista nuova passa da qui **prima di pubblicarla**:

```bash
python3 02-Sales/strumenti/controlla-lista.py 02-Sales/liste/<lista>.csv
```

Ferma gli handle già scritti e la verifica del sito copiata uguale su decine
di righe — vedi [[metodo-instagram]], passi 3 e 4.

## Collegamenti

[[metodo-instagram]] · [[2026-09-07-due-account-dm]] · [[setup-macchina-nuova]]
