---
description: Chiusura di sessione — scrive la daily, promuove nelle note di dominio, aggiorna i fatti. Funziona anche se nessuno risponde.
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, AskUserQuestion
---

# /chiudi-sessione

Registro Trevis, già in `~/.claude/CLAUDE.md`. Niente preamboli.

**Deve funzionare anche con Patrick, che non sa cos'è un commit.** Ogni passo
qui sotto si fa da solo. Le domande servono a far salire la qualità, non a
sbloccare il processo: se non arriva risposta, si va avanti e si dichiara.

## 1. Scrivi la daily subito, non alla fine

`06-Daily/YYYY-MM-DD-<slug>.md` da `99-Templates/template-daily.md`, **massimo
40 righe**, ricavata da `git status`, `git diff`, i commit di oggi e la
conversazione.

Nasce `source: claude` **senza `verificato:`** — cioè dichiarata come ipotesi.
Si scrive prima delle domande, non dopo: così esiste comunque.

Non entrano mai: il riassunto di cosa hai letto, i comandi eseguiti, il
racconto dei tentativi, il diff, i numeri senza data.

## 2. Poi chiedi, una volta sola

Un messaggio solo, cinque domande già compilate con la tua versione.

```
Daily del <data> — <progetto>. Correggi quello che è sbagliato, «ok» sul resto.

1. Finito oggi: <riga>
2. Rimasto a metà, a che punto: <riga>
3. Deciso: <riga o «niente»>
4. Non verificato: <riga>
5. Trappola nuova o strada da scartare: <riga o «niente»>
```

Se rispondono: correggi la nota, `source: denkicode`, `verificato:` con la data.
**Se non rispondono: non insistere.** La daily resta com'è, marcata ipotesi, e
lo dici in una riga.

Se durante la sessione una bozza è stata **bocciata**, chiedi anche la frase
esatta: serve al passo 4.

**Rete di sicurezza, non la strada.** Una regola detta durante la sessione si
scrive con `regola.py` nel momento in cui è detta. Qui si controlla solo se ne è
sfuggita una: rileggi la conversazione, e se c'è un «da adesso» o un «voglio
sempre» che non è finito da nessuna parte, scrivilo ora e dillo.

## 3. Promuovi — è il passo che mancava

Una daily è un registro di giornata. Se la conoscenza resta lì, fra una
settimana non esiste: nessuna sessione apre una nota datata. **Quello che vale
oltre oggi si sposta dove verrà riletto**, e nella daily resta il link.

| Cosa è uscito | Dove va |
|---|---|
| Stato, soldi, cosa è aperto o bloccato | **`FATTI.md`**, riscrivendo la riga |
| Un fatto su un progetto o un cliente | la sua nota in `01-Coding/progetti/` o `02-Sales/clienti/` |
| Una trappola tecnica o una strada morta | `01-Coding/trappole.md`, `[TRAPPOLA]` o `[SCARTATO]`, max 4 righe |
| Una bocciatura su un sito | `01-Coding/stack/direttive-siti.md` |
| Il modo giusto di fare una cosa, da ora in poi | `01-Coding/stack/convenzioni.md` |
| Una scelta che cambia rotta | nota nuova in `05-Decisioni/` |

`FATTI.md` **si riscrive**, non si accumula: un fatto che cambia sostituisce la
riga vecchia. Ogni numero porta la data accanto, o la freccia verso dove vive.

**Non si promuove niente a regola per conto tuo.** In `trappole.md` va l'errore;
se il modo giusto va reso dottrina lo proponi in una riga e ti fermi.

## 4. Se si è toccato un sito

```bash
python3 01-Coding/strumenti/controlla-sito.py ~/lavoro/<cartella>
```

Se esce 1, il sito è sotto il livello di NG Barber e Fiftynine: **lo dici e non
si pubblica**. Se è stato bocciato, la frase esatta va in `direttive-siti.md`
con la data e la regola che ne esce. Quel file cresce e non si accorcia: è il
motivo per cui i siti migliorano invece di oscillare.

## 5. Aggiorna e controlla

Per ogni progetto o cliente toccato: `updated:` a oggi, sezione **Aperto**
allineata, frontmatter se sono cambiati soldi o stato. **Si corregge il file
sbagliato, non si scrive la correzione altrove.**

Se hai verificato contro la realtà un fatto che stava in una nota `source:
claude`, scrivi `verificato:` con la data in quella nota.

```bash
python3 01-Coding/strumenti/genera-indice.py
python3 01-Coding/strumenti/installa-macchina.py --check
```

Il primo riscrive l'indice e stampa i buchi. Il secondo dice se `~/.claude/` è
indietro rispetto al vault; se lo è, rilancialo senza `--check`.

## 6. Il push lo fa l'hook

Non serve che lo faccia tu: l'hook di fine sessione fa `pull --rebase`, commit e
push da solo. **Committa lo stesso durante la sessione**, con un messaggio che
dice il perché: quello dell'hook dice solo cosa è cambiato, ed è la rete, non la
strada.

Se l'hook si ferma e te lo dice, risolvi quello che segnala. **Non forzare mai.**

## 7. Chiudi

Due righe: cosa hai scritto, cosa resta. Se la daily è rimasta un'ipotesi
perché nessuno ha risposto, dillo in una di quelle due.
