---
riga: Decisione. indice.md smette di essere una nota scritta a mano.
type: decisione
data: 2026-09-07
progetto: azienda
source: claude
---

# L'indice si genera, non si aggiorna a mano

**Decisione.** `indice.md` smette di essere una nota scritta a mano. Lo riscrive
`01-Coding/strumenti/genera-indice.py` dai file veri, e lo lancia
`/chiudi-sessione` prima del commit.

**Perché.** Il 7 settembre 2026 l'indice era fermo al 3 e non conosceva 10 note,
fra cui quattro progetti veri. Non per distrazione: **nessuna procedura lo
scriveva**. Le quattro volte in cui i comandi dicono «aggiorna l'indice»
parlano tutte della tabella dei progetti in `CLAUDE.md`, che è un'altra cosa.
`indice.md` era citato solo come file da *leggere*. Una regola senza niente che
la esegua è una regola che decade, e un indice vecchio fa concludere che una
nota non esiste: è così che nascono i doppioni che l'indice doveva evitare.

**Cosa fa lo script**, oltre a riscrivere l'indice: stampa i buchi che una
persona non vede da sola.

- link rotti, con quante volte sono citati
- progetti attivi fuori dalla tabella di `CLAUDE.md`
- righe del [[registro-interventi]] con il progetto scritto come testo semplice
  invece che come wikilink
- note senza `type` nel frontmatter, che spariscono dalle tabelle Dataview

**Cosa ha trovato al primo giro.** Due progetti veri, con repo e commit, senza
nessuna scheda nel vault: [[sito-castiglione]] (dieci wikilink verso il nulla) e
[[sito-ngbarber]] (nemmeno quelli, perché nel registro era testo semplice: un
progetto scritto senza link è invisibile anche a un controllo dei link rotti).
Più quattro progetti di settembre mai entrati nella tabella di `CLAUDE.md`.

**Il limite, dichiarato.** La colonna «Nodo aperto» della tabella dei progetti
**non si genera**: quella la sa solo chi ha lavorato. Lo script segnala la riga
mancante, non la scrive. E `01-Coding/strumenti/` adesso contiene codice, in un
vault che dice di non contenerne: è codice che serve al vault, non a un
prodotto, e resta l'unico.

## Collegamenti

[[trappole]] · [[2026-09-07-trappole-memoria-tecnica]] · [[registro-interventi]] ·
[[indice]]
