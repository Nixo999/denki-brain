---
description: Riepilogo di cosa è cambiato nel vault negli ultimi 7 giorni
allowed-tools: Bash, Read, Glob, Grep
---

> **Base**: `03-Storage/azienda/protocollo-trevis.md` (di cosa ci si occupa) e
> `03-Storage/azienda/registro-trevis.md` (come si parla) — si leggono prima di
> rispondere, in questa come in ogni altra modalità. Niente presentazioni,
> niente «adesso procedo a», niente proposte su cosa fare dopo. Riprendi come se
> la conversazione non si fosse mai interrotta.

Riepiloga cosa è successo in DenkiCode negli ultimi 7 giorni.

## 1. Cosa è cambiato nel vault

```bash
git log --since="7 days ago" --pretty=format:"%ad  %s" --date=short
git diff --stat "@{7 days ago}" HEAD
```

Se il repo ha meno di una settimana di storia, usa `git log` intero e dillo.

Poi guarda le note nuove o modificate:

```bash
git log --since="7 days ago" --name-only --pretty=format: | sort -u | grep -v '^$'
```

## 2. Cosa è cambiato nei progetti

Leggi le note in `06-Daily/` degli ultimi 7 giorni: sono già il diario, non
riscriverle — estraine i fatti.

Controlla i commit degli ultimi 7 giorni nei repo di codice
(`opero-sito`, `smooth-duty`) via API GitHub, senza clonare.

## 3. Cosa NON è cambiato

Questa è la parte utile. Elenca:

- progetti `attivo` con `updated` più vecchio di 7 giorni
- decisioni con `stato: aperta` da più di 7 giorni
- caselle `- [ ]` che erano aperte anche la settimana scorsa
- note in `00-Inbox/` mai smistate

## 4. I numeri

Leggi `02-Sales/report/metriche.md`. Se lo storico settimanale non è stato
compilato, **chiedi i due numeri**: chiamate fatte da Giulia e appuntamenti
fissati. Poi scrivili nella tabella dello storico.

Confronta con i target: 50 chiamate, 4 appuntamenti.

## 5. Riportare

Struttura fissa, breve:

```
## Fatto questa settimana
## Fermo
## Numeri          (chiamate / appuntamenti / vs target)
## La settimana prossima   ← max 3 cose, in ordine di priorità
```

Se una settimana è stata vuota, dillo in una riga invece di gonfiarla.
