---
type: risorsa
updated: 2026-08-28
source: claude
---

# Dashboard DenkiCode

Questa nota si aggiorna **da sola**. Richiede il plugin **Dataview** attivo, con
l'opzione *JavaScript Queries* NON necessaria (bastano le query normali).
Se vedi il codice invece delle tabelle, il plugin non è installato — vedi
`README.md`.

Aprila ogni mattina.

## 🔨 Progetti attivi

```dataview
TABLE WITHOUT ID
  file.link AS "Progetto",
  client AS "Cliente",
  status AS "Stato",
  deadline AS "Scadenza",
  updated AS "Aggiornato"
FROM "01-Coding/progetti"
WHERE type = "progetto" AND status != "completato"
SORT updated ASC
```

## ⏰ Fermi da più di 14 giorni

Se qualcosa compare qui, o è finito o è stato dimenticato.

```dataview
TABLE WITHOUT ID
  file.link AS "Progetto",
  updated AS "Ultimo aggiornamento",
  (date(today) - date(updated)).days AS "Giorni fermo"
FROM "01-Coding/progetti"
WHERE type = "progetto" AND status = "attivo"
  AND date(updated) < date(today) - dur(14 days)
SORT updated ASC
```

## 💰 Soldi in ballo

```dataview
TABLE WITHOUT ID
  file.link AS "Progetto",
  valore AS "Pattuito",
  incassato AS "Incassato",
  (valore - incassato) AS "Da incassare"
FROM "01-Coding/progetti"
WHERE valore
SORT (valore - incassato) DESC
```

## 👥 Clienti

```dataview
TABLE WITHOUT ID
  file.link AS "Cliente",
  status AS "Stato",
  settore AS "Settore",
  progetti AS "Progetti",
  updated AS "Aggiornato"
FROM "02-Sales/clienti"
WHERE type = "cliente"
SORT status ASC, updated DESC
```

## 🧭 Decisioni ancora aperte

```dataview
TABLE WITHOUT ID
  file.link AS "Decisione",
  data AS "Data",
  progetto AS "Progetto"
FROM "05-Decisioni"
WHERE stato = "aperta"
SORT data DESC
```

## 📋 Tutte le decisioni, dalla più recente

```dataview
TABLE WITHOUT ID
  file.link AS "Decisione",
  data AS "Data",
  progetto AS "Progetto"
FROM "05-Decisioni"
SORT data DESC
LIMIT 10
```

## ✅ Cose da fare, prese da tutto il vault

Raccoglie ogni casella `- [ ]` non spuntata, ovunque sia scritta.

```dataview
TASK
FROM "01-Coding" OR "02-Sales" OR "03-Storage"
WHERE !completed
GROUP BY file.link
```

## 📥 Inbox da svuotare

```dataview
LIST
FROM "00-Inbox"
WHERE file.name != "come-si-usa-inbox"
SORT file.ctime DESC
```

## 🗓️ Ultime note di giornata

```dataview
TABLE WITHOUT ID
  file.link AS "Giorno",
  progetti AS "Progetti toccati"
FROM "06-Daily"
SORT file.name DESC
LIMIT 7
```

## ❓ Dove mancano informazioni

Dataview non sa cercare dentro il testo delle note, quindi i `TODO` si trovano
in due modi:

- **In Obsidian**: `Ctrl+Shift+F` e cerca `TODO`
- **Con Claude**: *"quali TODO sono rimasti nel vault?"*

I sette che contano di più al 28 agosto 2026 sono elencati in
[[2026-08-28-avvio-vault]].
