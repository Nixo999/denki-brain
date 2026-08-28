---
description: Intervista guidata per creare la scheda di un cliente nuovo
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
---

> **Registro**: `03-Storage/azienda/registro-jarvis.md` — si legge prima di
> rispondere, in questa come in ogni altra modalità. Niente presentazioni,
> niente «adesso procedo a», niente proposte su cosa fare dopo. Riprendi come se
> la conversazione non si fosse mai interrotta.

Crea la scheda di un cliente nuovo. **Intervista prima, scrivi dopo.**

Se l'utente ha già passato un nome (`$ARGUMENTS`), usalo e non richiederlo.

## Regole dell'intervista

- Una domanda alla volta, o due se collegate
- Domande concrete. Se non lo sa, `TODO` e avanti
- **Non inventare** nomi, cifre o date

## Le domande

1. **Ragione sociale** e settore. Il nome completo, quello che scrivereste su
   una ricevuta — non il soprannome.
2. **Referente**: chi è la persona che decide, e chi segnala i problemi.
   Possono essere due persone diverse.
3. **Come è arrivato**: chiamata di Giulia, porta-a-porta di Patrick,
   passaparola, conoscenza personale? Se è arrivato da una lista, quale fonte
   (Google Maps, Instagram, Pagine Gialle)? Serve a
   `02-Sales/processo/generazione-lead.md`: sapere quale canale porta clienti
   veri è più utile di sapere quante chiamate sono state fatte.
4. **Canale abituale**: WhatsApp, email, telefono?
5. **Cosa gli abbiamo venduto o consegnato**, e quando.
6. **Soldi**: pattuito, incassato, credito aperto. Su chi è stata emessa la
   ricevuta (`03-Storage/azienda/vincoli-fiscali.md`).
7. **Com'è come cliente**: paga puntuale? cambia idea? risponde? Anche una riga
   sola, se c'è. Vale più di qualsiasi anagrafica fra sei mesi.

Poi **riassumi e chiedi conferma**.

## Scrivere la scheda

- File: `02-Sales/clienti/<slug-kebab-case>.md`
- Base: `99-Templates/template-cliente.md`
- ⚠️ **Se esiste già un progetto con lo stesso nome**, distingui gli slug: il
  cliente è `albybike`, il progetto è `sito-albybike`. Due file con lo stesso
  nome rompono i wikilink
- `source: denkicode`, `updated:` a oggi
- Compila `progetti:` con gli slug dei progetti collegati
- Aggiorna il campo `client:` nelle note dei progetti coinvolti
- Se ha portato soldi, aggiorna il conto del tetto in
  `03-Storage/azienda/vincoli-fiscali.md`

Alla fine: percorso del file e `TODO` rimasti.
