---
type: template
updated: 2026-08-28
source: claude
tags: [report, settimanale, processo]
---

# Template — report settimanale della domenica

Si compila e si incolla in chat la domenica, in un blocco solo. Alimenta il
[[ciclo-settimanale]] e i numeri di [[metriche]].

**Tre regole di compilazione**, che valgono più della bellezza del report:

1. **Gli esiti si scrivono con le parole della lista**, sempre le stesse, o il
   conteggio non torna. Il testo libero viene dopo il trattino.
2. **Le righe "Non risponde" non si incollano**: basta il numero totale. Si
   incollano solo le righe dove qualcuno ha parlato.
3. **Ogni cifra ha una data accanto.** «Incassati 200 EUR» senza data invecchia
   in una settimana.

Campo vuoto = non successo. Campo con `?` = non lo so, e allora te lo chiedo.

---

```
# REPORT SETTIMANA dal __/__ al __/__

## 1 — CHIAMATE GIULIA

Numeri composti: ___    Risposte vere: ___    Ore usate: ___
Appuntamenti fissati: ___    Form compilati (Indagine): ___

### 1a. Siti Web (50)
Righe con risposta — Nome | Esito | Note di Giulia
-
-
-

### 1b. DenkiShift (50)
Righe con risposta — Nome | Esito | Note di Giulia
-
-
-

### 1c. Indagine di Mercato (30)
Righe con risposta — Nome | Esito | Note di Giulia
-
-
-

### 1d. Obiezioni sentite più di una volta
- "____________________" → x__ volte, prodotto ____
- "____________________" → x__ volte, prodotto ____

### 1e. Cosa dice Giulia
Dove si è bloccata, cosa non le è uscito bene, cosa vuole cambiare:
____________________________________________


## 2 — BLITZ FISICI PATRICK (10 target)

Attività | Esito | Materiale lasciato | Note
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

Esito, sempre una di queste: Titolare ingaggiato / Parlato con un dipendente /
Solo materiale lasciato / Chiuso o assente / Rifiuto secco
Materiale: Volantino / Biglietto / Nessuno

Contatti diretti presi (nome + numero + cosa gli ho promesso):
-
-


## 3 — SECONDI INCONTRI E CHIUSURE PATRICK

Cliente | Prodotto | Esito | Obiezione principale | Prossimo step
 1.  |  |  |  |
 2.  |  |  |  |
 3.  |  |  |  |

Esito, sempre una di queste: Chiuso / In decisione / Perso
Prodotto: Vetrina / E-commerce / DenkiShift / Custom

Per ogni "Chiuso": importo ____ EUR, incassato il __/__, ricevuta sì/no
Per ogni "Perso": la frase esatta con cui mi ha detto no
____________________________________________

Riprogrammati per la prossima settimana:
-
```

---

## Cosa ne faccio

Nell'ordine: conto e aggiorno [[metriche]], riscrivo i looping delle obiezioni
ricorrenti, dico dove si è rotta ogni chiusura persa, e genero i 4 output della
settimana nuova. Il dettaglio sta in [[ciclo-settimanale]].

## Collegamenti

[[ciclo-settimanale]] · [[metriche]] · [[metodo-liste]] ·
[[script-giulia-denkishift]]
