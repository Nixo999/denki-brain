---
description: Allineamento rapido a inizio sessione — legge FATTI e la testa del registro interventi, risponde in poche righe
allowed-tools: Bash, Read, Glob
---

# /stato

Registro Trevis, già in `~/.claude/CLAUDE.md`. Niente presentazioni, niente
«adesso procedo a», niente proposte su cosa fare dopo. Riprendi come se la
conversazione non si fosse mai interrotta.

Allinea la sessione allo stato attuale di DenkiCode. **Deve costare poco.**

## Regole di economia — vincolanti

1. **`CLAUDE.md` è già nel tuo contesto**: non rileggerlo, non riassumerlo, non
   ripetere all'utente cose che ci sono già scritte.
2. **Leggi due cose**: `FATTI.md` intero e le prime dieci righe della tabella
   di `01-Coding/registro-interventi.md`, che il comando sotto stampa da solo.
   Nient'altro. `FATTI.md` è lo stato di adesso, sotto le 80 righe; il
   registro dice cosa è stato fatto ieri, da chi e su che repo. Le daily
   non esistono più dal 27/09/2026: `06-Daily/` è storia.
3. **Non aprire** `01-Coding/`, `02-Sales/`, `03-Storage/`. Se cerchi altro:
   `python3 01-Coding/strumenti/cerca.py <parole>` ordina le note per
   rilevanza, e la `riga:` in `indice.md` dice se vale la pena aprirle.
4. Se manca qualcosa, **chiedi invece di cercare**.

## Cosa fare

```bash
git pull --rebase --autostash -q 2>&1 | tail -2
python3 01-Coding/strumenti/installa-macchina.py
grep '^| ' 01-Coding/registro-interventi.md | grep -v '^| Quando' | head -10 | cut -c1-300
```

`installa-macchina.py` va **dopo** il pull: `~/.claude/` è locale e il pull non
lo tocca. Se stampa dei file, la sessione in corso usa ancora i comandi vecchi —
si dice in una riga e vale dalla prossima.

Poi leggi `FATTI.md` intero. Le dieci righe del registro le hai già dal
comando: non aprire il file. Se l'ultima riga del registro è di giorni fa,
l'ultima sessione si è chiusa senza scriverla: dillo in una riga invece di
ricostruirla.

**Quello che leggi lì è confermato da Nicola** (`source: denkicode`,
`verificato:`). Se apri altro e trovi `source: claude` senza `verificato:`,
quella è un'ipotesi: si dichiara come tale, non si riporta come stato.

## Cosa rispondere

Massimo **otto righe in totale**:

```
Stato al <data>: <una riga sulla situazione>

Aperto:
- <le 3 cose più urgenti, una riga ciascuna>

Prossimo passo: <una riga>
```

Niente preamboli, niente riepilogo di ciò che hai letto, niente elenco dei file
aperti. Se il `git pull` ha portato commit di un'altra macchina, **una riga
sola** su cosa è arrivato e da chi.

Poi fermati e aspetta.
