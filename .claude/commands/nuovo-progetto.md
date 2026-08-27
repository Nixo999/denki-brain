---
description: Intervista guidata per creare la nota di un progetto nuovo con il frontmatter giusto
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
---

Crea la nota di un progetto nuovo. **Intervista prima, scrivi dopo.**

Se l'utente ha già passato degli argomenti (`$ARGUMENTS`), usali come nome di
partenza e non richiederli.

## Regole dell'intervista

- Una domanda alla volta, o due se sono strettamente collegate
- Domande **concrete**. Non "che tipo di progetto è": "è un sito vetrina, un
  e-commerce, DenkiShift per un cliente, o un gestionale custom?"
- Se una risposta è vaga, chiedi il chiarimento invece di riempire il buco
- Se non lo sa, scrivi `TODO` e vai avanti
- **Non inventare mai** stack, date o prezzi

## Le domande

1. **Nome del progetto** e in due righe cosa fa.
2. **Cliente**: chi è? Controlla se esiste già in `02-Areas/clienti/`. Se non
   c'è, offri di crearlo dopo con `/nuovo-cliente`. Se è un prodotto interno
   (come DenkiShift), `client: interno`.
3. **Quale dei quattro prodotti è?** (A vetrina, B e-commerce, C DenkiShift,
   D gestionale custom — vedi `03-Resources/prodotti-e-listino.md`)
4. **Stack**: cosa userai? Proponi il default coerente col prodotto leggendo
   `03-Resources/stack.md`, e fatti confermare. ⚠️ Ricorda che lo stack standard
   è una decisione ancora aperta.
5. **Soldi**: prezzo pattuito, acconto preso, e su chi si emette la ricevuta
   (`02-Areas/business/vincoli-fiscali.md`).
6. **Date**: quando è iniziato, che scadenza è stata **detta al cliente**. Se
   una data è stata promessa a voce, va scritta lo stesso.
7. **Decisioni architetturali già prese**, se ce ne sono.
8. **Repo**: esiste? Qual è l'URL?

Dopo le domande, **riassumi e chiedi conferma** prima di scrivere.

## Scrivere la nota

- File: `01-Projects/<slug-kebab-case>.md`
- Base: `99-Templates/template-progetto.md`
- `source: denkicode`, `updated:` a oggi
- Wikilink al cliente, a `[[stack]]`, a `[[convenzioni]]`
- Aggiungi la riga all'**indice progetti attivi in `CLAUDE.md`**
- Se il cliente esiste, aggiungi lo slug del progetto al suo campo `progetti:`
- Se sono emerse decisioni, proponi di aprirle in `05-Decisioni/`

Alla fine: mostra il percorso del file e cosa resta `TODO`.
