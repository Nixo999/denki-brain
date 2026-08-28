---
description: Allineamento rapido a inizio sessione — legge solo l'ultima nota di giornata e risponde in poche righe
allowed-tools: Bash, Read, Glob
---

Allinea la sessione allo stato attuale di DenkiCode. **Deve costare poco.**

## Regole di economia — vincolanti

1. **`CLAUDE.md` è già nel tuo contesto**: non rileggerlo, non riassumerlo e non
   ripetere all'utente cose che ci sono già scritte.
2. **Leggi un solo file**: la nota più recente in `06-Daily/`. Nient'altro.
3. **Non aprire** `01-Coding/`, `02-Sales/`, `03-Storage/`, né la dashboard.
   L'indice dei progetti attivi ce l'hai già in `CLAUDE.md`.
4. Se dopo questo manca qualcosa, **chiedi invece di cercare**. Una domanda
   costa meno di cinque file letti.

## Cosa fare

```bash
git pull --rebase -q 2>&1 | tail -2
ls -1 06-Daily/ | sort | tail -1
```

Poi leggi **solo** quel file — e se supera le 200 righe, leggine le ultime 120:
le sezioni recenti stanno in fondo.

## Cosa rispondere

Massimo **otto righe in totale**, in questa forma:

```
Stato al <data>: <una riga sulla situazione>

Aperto:
- <le 3 cose più urgenti, una riga ciascuna>

Prossimo passo: <una riga>
```

Niente preamboli, niente riepilogo di ciò che hai letto, niente elenco dei file
aperti. Se il `git pull` ha portato commit di un'altra macchina, aggiungi **una
riga sola** che dice cosa è arrivato e da chi.

Poi fermati e aspetta.
