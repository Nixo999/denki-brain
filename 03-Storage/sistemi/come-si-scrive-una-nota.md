---
type: risorsa
riga: Le quattro regole di scrittura del vault - riga, verificato, le tre classi di memoria, i tetti di lunghezza.
updated: 2026-09-10
verificato: 2026-09-10
source: denkicode
tags: [convenzioni, memoria, frontmatter, verifica]
---

# Come si scrive una nota

Deciso il 10 settembre 2026, dopo la diagnosi in
[[2026-09-10-memoria-verificata]]. Il vault era arrivato a 93 note scritte da
Claude contro 47 scritte da noi, e a 14.400 parole caricate prima di ogni
compito. Queste quattro regole esistono per invertire le due cose.

## 1. `riga:` — obbligatoria, e serve a non aprire il file

Ogni nota dichiara nel frontmatter **una riga sola**, max 140 caratteri, che
dice cosa c'e' dentro. Non il titolo, non l'argomento: il contenuto.

```yaml
riga: OperO e' il prodotto che Sebastian rivende, non un gestionale nostro. 2.000 EUR aperti, storico mai migrato.
```

`genera-indice.py` mette quella riga in `indice.md`. Da li' si decide **se**
aprire il file. Chi legge il vault legge l'indice, non le note: apre solo
quelle che la riga dichiara utili al compito di oggi.

Una `riga:` che non aiuta a decidere e' scritta male. Il test e' uno: leggendo
solo quella, uno sa se gli serve aprire o no.

## 2. `verificato:` — la data in cui una persona ha controllato

```yaml
source: claude
verificato: 2026-09-10
```

**Una nota `source: claude` senza `verificato:` e' un'ipotesi, non un fatto.**
Si puo' leggere per orientarsi. Non si puo' citare come vero, non ci si
costruisce sopra codice, e non ci esce niente verso un cliente.

Prima di usarla si controlla contro la cosa vera — il repo, il sito online, il
database, una persona — e allora si scrive la data. Se il controllo la smentisce
si corregge la nota, non si scrive una nota nuova che la contraddice.

`verificato:` piu' vecchio di 30 giorni su una nota che cambia (progetti,
clienti, metriche) vale come assente: si ricontrolla.

Le note `source: denkicode` non hanno bisogno del campo: le ha scritte una
persona, sono gia' la fonte.

## 3. Le tre classi — un errore non diventa mai una regola

Quello che si impara lavorando si scrive in una di tre forme, **dichiarata**.
Non sono sfumature dello stesso appunto: si leggono in tre momenti diversi e
solo la prima si applica.

| Classe | Cos'e' | Dove sta | Quando si legge |
|---|---|---|---|
| **REGOLA** | Il modo giusto di fare una cosa, da qui in avanti | [[convenzioni]], `CLAUDE.md` del repo, `05-Decisioni/` | Prima di costruire |
| **TRAPPOLA** | Un errore gia' pagato, con la contromisura | [[trappole]] | Prima di ripetere quel gesto |
| **SCARTATO** | Una strada provata che non funziona | [[trappole]], sezione «Scartato» | Quando qualcuno la ripropone |

Le tre regole che le tengono separate:

1. **Una TRAPPOLA non diventa una REGOLA da sola.** Sta in `trappole.md` come
   errore. Se il modo giusto va reso dottrina, lo scrive una persona in
   [[convenzioni]] o in una decisione, di proposito. Nessuno promuove niente
   leggendo.
2. **Uno SCARTATO non si ripropone.** Se ricompare in una risposta e' un errore
   della risposta, non un'idea nuova. Riaprirlo si puo', ma si dichiara che lo
   si sta riaprendo e perche'.
3. **Una TRAPPOLA e' descrittiva, mai prescrittiva fuori dal suo caso.** «Su
   Brave headless sotto 500 px il layout mente» non e' «non si misura a 375».

Ogni voce nuova in `trappole.md` si apre con la sua classe fra parentesi
quadre: `[TRAPPOLA]` o `[SCARTATO]`. Le voci scritte prima del 10 settembre
2026 sono tutte trappole, ed e' scritto in testa al file.

## 4. I tetti — una nota lunga non viene riletta

**Due tetti sono duri, perche' su quei due file la lunghezza costa a ogni
sessione.** Gli altri sono un'indicazione: una nota che si apre di rado e di
proposito puo' essere lunga quanto serve, purche' ogni riga cambi qualcosa.

| Nota | Tetto | Perche' |
|---|---|---|
| Daily | **40 righe, duro** | Si legge a ogni sessione. Quella del 7 settembre era 5.341 parole |
| Voce di `trappole.md` | **4 righe, duro** | Trappola, contromisura, dove e' stata pagata |
| Decisione | ~50 righe | Contesto, scelta, scartato, conseguenze. Il resto e' racconto |
| Progetto, cliente | ~80 righe | Oltre, e' un archivio: si spezza |

Fuori tetto si taglia il contenuto, non si comprime la sintassi.

**Le note scritte prima del 10 settembre 2026 restano come sono.** Le daily
vecchie arrivano a 662 righe: sono il registro di com'e' andata quel giorno e
riscriverle vorrebbe dire riscrivere la storia. Il tetto vale su quello che si
scrive da adesso, e su una nota vecchia solo quando la si sta gia' rifacendo.

**Cosa non entra mai in una nota**: il riassunto di quello che si e' letto,
l'elenco dei file aperti, i comandi eseguiti, il racconto dei tentativi, i
numeri senza data, il ringraziamento a fine sezione. Se una riga non cambia
cosa fara' chi la legge, non si scrive.

## Collegamenti

[[convenzioni]] · [[trappole]] · [[2026-09-10-memoria-verificata]] ·
[[registro-interventi]]
