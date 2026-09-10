---
description: Handoff di fine sessione — daily scritta a domande, max 40 righe, poi commit e push
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, AskUserQuestion
---

# /chiudi-sessione

Registro Trevis, già in `~/.claude/CLAUDE.md`. Niente preamboli.

## 1. Prepara la bozza, non la nota

Guarda `git status`, `git diff`, i commit di oggi nel vault e nei repo toccati,
e la conversazione. Da lì ricavi **la tua versione dei fatti**. È `source:
claude`: è una proposta, non un verbale.

## 2. Chiedi — è il passaggio che rende la daily una fonte

Mandi **un messaggio solo** con le cinque domande, ognuna già compilata con la
tua risposta. Nicola conferma o corregge. Non scrivi niente prima di aver
ricevuto le risposte.

```
Daily del <data> — <progetto>. Correggi quello che è sbagliato, «ok» sul resto.

1. Finito oggi: <la tua riga>
2. Rimasto a metà, a che punto: <la tua riga>
3. Deciso: <la tua riga, oppure «niente»>
4. Non verificato: <cosa hai scritto senza provarlo>
5. Trappola nuova o strada da scartare: <la tua riga, oppure «niente»>
```

Regole delle domande:

- **Cinque, mai di più.** Se ne servisse una sesta, la cosa non è una daily: è
  una decisione, e va in `05-Decisioni/`.
- **Una riga a domanda.** Se la tua proposta è lunga tre righe l'hai scritta
  male.
- **Non chiedere quello che puoi leggere** da `git diff`. Chiedi quello che solo
  Nicola sa: se una cosa è davvero finita, se una decisione è davvero presa.
- Se Nicola non risponde e chiude la sessione, la daily **non si scrive**.
  Meglio nessuna nota che una nota non controllata: è quella che diventa la
  premessa di domani.

## 3. Scrivi la nota — 40 righe, tetto duro

`06-Daily/YYYY-MM-DD-<slug>.md` da `99-Templates/template-daily.md`. Se la nota
di oggi esiste, si aggiunge in coda.

Il contenuto sono **le risposte di Nicola**, non il tuo riassunto. Frontmatter:
`source: denkicode` e `verificato:` con la data di oggi — le ha confermate una
persona.

```bash
wc -l 06-Daily/<file>.md   # oltre 40, si taglia contenuto
```

Non entrano mai: il riassunto di cosa hai letto, i comandi eseguiti, il racconto
dei tentativi, il diff, i ringraziamenti. La daily del 7 settembre era 5.341
parole e nessuno l'ha riletta.

## 4. La memoria degli errori — con la classe scritta

Se la risposta 5 dice qualcosa, va in `01-Coding/trappole.md`, nella sua
sezione, **max 4 righe**, aperta dalla classe:

- `[TRAPPOLA]` — è successo, ecco la contromisura, ecco dove è stata pagata.
- `[SCARTATO]` — provato, non funziona, non si ripropone.

**Non si promuove niente a regola qui.** Se il modo giusto va reso dottrina, lo
scrive Nicola in `01-Coding/stack/convenzioni.md` o in una decisione, di
proposito. Tu lo proponi in una riga e ti fermi.

Se non è uscito niente di riutilizzabile non si scrive niente.

## 5. Aggiorna le note toccate

Per ogni progetto o cliente su cui si è lavorato: `updated:` a oggi, sezione
**Aperto** allineata, campi del frontmatter se sono cambiati soldi o stato, e la
riga nella tabella di `CLAUDE.md` se è nato un progetto o è cambiato uno stato.

**Si corregge il file sbagliato, non si scrive la correzione altrove.**

Se hai verificato contro la realtà un fatto che stava in una nota `source:
claude` — il repo, il sito online, lo schema — scrivi `verificato:` con la data
di oggi in quella nota. È l'unico modo in cui il campo si popola.

## 6. Registro interventi

Se si è toccato un progetto: una riga in `01-Coding/registro-interventi.md` con
chi, quando, progetto, repository e **quale database**. Quella colonna è il
motivo per cui il registro esiste.

## 7. Indice, e `~/.claude/` allineato

```bash
python3 01-Coding/strumenti/genera-indice.py
python3 01-Coding/strumenti/installa-macchina.py --check
```

Il secondo dice se protocollo, comandi, agente e skill sulla macchina sono
indietro rispetto al vault: `~/.claude/` è locale e il `git pull` non lo tocca.
Se sono indietro, si rilancia senza `--check`.

Riscrive `indice.md` e stampa i buchi: `riga:` mancanti, `verificato:` scaduti,
link rotti, progetti attivi fuori dalla tabella. **I buchi si guardano.** Quello
che non risolvi lo dici in due righe.

## 8. Commit e push

```bash
git add -A && git status --short
```

Messaggio in italiano, dice cosa è cambiato e perché, non l'elenco dei file. Poi
`git push`. Se fallisce non forzare: `git pull --rebase` e riprova.

## 9. Chiudi

Due righe: cosa hai scritto, cosa resta per domani.
