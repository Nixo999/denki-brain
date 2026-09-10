---
description: Allineamento rapido a inizio sessione — legge solo l'ultima nota di giornata e risponde in poche righe
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
2. **Leggi un solo file**: la nota più recente in `06-Daily/`. Nient'altro.
3. **Non aprire** `01-Coding/`, `02-Sales/`, `03-Storage/`. La tabella dei
   progetti attivi ce l'hai in `CLAUDE.md`; se cerchi altro, la `riga:` di ogni
   nota sta in `indice.md` e dice se vale la pena aprirla.
4. Se manca qualcosa, **chiedi invece di cercare**.

## Cosa fare

```bash
git pull --rebase --autostash -q 2>&1 | tail -2
python3 01-Coding/strumenti/installa-macchina.py
ls -1 06-Daily/ | sort | tail -1
```

`installa-macchina.py` va **dopo** il pull: `~/.claude/` è locale e il pull non
lo tocca. Se stampa dei file, la sessione in corso usa ancora i comandi vecchi —
si dice in una riga e vale dalla prossima.

Poi leggi **solo** quel file. Le daily sono tarate a 40 righe: si legge intera.
Se quella di oggi non c'è, l'ultima sessione si è chiusa senza risposte di
Nicola e la daily non è stata scritta: dillo in una riga invece di ricostruirla.

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
