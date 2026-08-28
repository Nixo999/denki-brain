---
type: template
updated: 2026-08-28
source: claude
tags: [report, settimanale, processo]
---

# Il report della domenica — cosa si consegna

Quattro file, non un testo lungo. Alimentano il [[ciclo-settimanale]] e i numeri
di [[metriche]].

| # | File | Chi lo riempie | Come |
|---|---|---|---|
| 1 | `AAAA-MM-GG-siti.csv` | Giulia | Colonna `Esito e Note Giulia` |
| 2 | `AAAA-MM-GG-denkishift.csv` | Giulia | Colonna `Esito e Note Giulia` |
| 3 | `AAAA-MM-GG-indagine.csv` | Giulia | Colonna `Esito e Note Giulia` |
| 4 | `report-patrick-settimanale.docx` | Patrick | Blitz fisici + chiusure |

Le liste di Giulia **non si riassumono**: si riconsegnano com'è, con l'ultima
colonna piena. I conteggi — numeri composti, risposte, esiti per categoria — li
faccio io leggendo le righe. Riassumerle a mano è lavoro doppio e perde i "no".

**Tre regole di compilazione**, che valgono più della bellezza del report:

1. **Gli esiti si scrivono con le parole fisse**, sempre le stesse, o il
   conteggio non torna. Il testo libero viene dopo il trattino.
2. **Le righe non chiamate restano vuote.** Vuoto = non fatto, non "non
   risponde". Sono due cose diverse e cambiano il tasso di risposta.
3. **Ogni cifra ha una data accanto.** «Incassati 200 EUR» senza data invecchia
   in una settimana.

## Il modulo di Patrick

[report-patrick-settimanale.docx](report-patrick-settimanale.docx) — si apre in
Word o Pages e si scrive dentro le tabelle. Due colonne vanno a **lettera
singola**, per compilarlo in cinque minuti:

| Campo | Valori |
|---|---|
| Blitz · `ESITO` | `I` ingaggiato · `D` dipendente · `M` solo materiale · `C` chiuso · `R` rifiuto |
| Blitz · `MAT.` | `V` volantino · `B` biglietto · `N` niente |
| Chiusure · `ESITO` | `C` chiuso · `D` in decisione · `P` perso |

Si stampa anche: le righe sono alte abbastanza per scriverci a penna in
macchina, fra un blitz e l'altro.

## Se il Word non è a portata — la versione da incollare

Vale solo per la parte di Patrick, e solo se sta fuori. Stessa sostanza.

```
## BLITZ FISICI — settimana dal __/__ al __/__      fatti __ su 10

Attività e zona | Esito (I/D/M/C/R) | Materiale (V/B/N) | Note
 1.  |  |  |
 2.  |  |  |
 3.  |  |  |
 4.  |  |  |
 5.  |  |  |
 6.  |  |  |
 7.  |  |  |
 8.  |  |  |
 9.  |  |  |
10.  |  |  |

Contatti diretti presi (nome | telefono | cosa gli ho promesso):
-

## CHIUSURE E SECONDI INCONTRI

Cliente | Prodotto | Esito (C/D/P) | Obiezione principale | Prossimo step
 1.  |  |  |  |
 2.  |  |  |  |
 3.  |  |  |  |

Chiusi: importo ____ EUR, incassato il __/__, ricevuta sì/no
Persi: la frase esatta con cui mi ha detto no
-

## CODA
Ore usate da Giulia: ___    Cosa non le è uscito bene: ___
Una riga sulla settimana: ___
```

## Cosa ne faccio

Nell'ordine: conto e aggiorno [[metriche]], riscrivo i looping delle obiezioni
ricorrenti, dico dove si è rotta ogni chiusura persa, e genero i 4 output della
settimana nuova. Il dettaglio sta in [[ciclo-settimanale]].

## Collegamenti

[[ciclo-settimanale]] · [[metriche]] · [[metodo-liste]] ·
[[script-giulia-denkishift]]
