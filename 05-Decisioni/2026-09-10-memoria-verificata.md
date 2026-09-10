---
type: decisione
riga: Il brain smette di leggersi addosso - riga obbligatoria, verificato, tre classi di memoria, core non piu' obbligatori.
data: 2026-09-10
progetto: azienda
source: denkicode
stato: presa
updated: 2026-09-10
verificato: 2026-09-10
---

# Il brain si legge meno e si fida meno di se stesso

## Il contesto

Nicola: «si ricorda le cose, ma le fa male, quasi peggio di quando non lo
usavo». Misurato: 93 note `source: claude` contro 47 `source: denkicode`,
~14.400 parole caricate prima di ogni compito, 17 regole in `CLAUDE.md`, 34
decisioni in sei settimane, la daily del 7 settembre a 5.341 parole scritta da
me. Ogni sessione partiva dal mio riassunto della precedente: un errore di
lunedi' diventava premessa martedi' e regola giovedi'.

## La decisione

1. **`riga:` obbligatoria** in ogni frontmatter. Si legge `indice.md`, si apre
   solo cio' che serve.
2. **`verificato:`** su ogni nota `source: claude`. Senza, e' un'ipotesi: non si
   cita, non ci si costruisce sopra, non esce verso un cliente. L'indice la
   marca `⚠️`.
3. **Tre classi separate**: REGOLA in [[convenzioni]], `[TRAPPOLA]` e
   `[SCARTATO]` in [[trappole]]. Un errore non diventa una regola da solo.
4. **La daily si scrive a cinque domande**, la conferma Nicola, tetto 40 righe.
   Senza risposte non si scrive.
5. **I core non sono piu' obbligatori** e non si dichiara il framework.
6. **Si corregge la fonte, mai sopra la fonte.** `CLAUDE.md` da 3.031 a 1.319
   parole, i percorsi Windows tolti da `/nicola` invece che smentiti altrove.

## Cosa si e' scartato

Riorganizzare le cartelle: il problema era la densita' e la fiducia, non dove
stanno i file. Timbrare `verificato:` sulle 90 note esistenti: sarebbe la stessa
bugia che ha rotto il vault.

## Conseguenze aperte

90 note restano ipotesi. 116 `riga:` seminate dal generatore, da riscrivere
quando si tocca la nota. Le daily vecchie restano lunghe: sono il registro di
com'e' andata, non si riscrivono. `genera-indice.py` conta i buchi a ogni
`/chiudi-sessione`.

## Collegamenti

[[come-si-scrive-una-nota]] · [[trappole]] · [[convenzioni]]
