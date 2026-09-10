---
description: Modalità sviluppo DenkiCode — allinea la sessione al second brain e prepara il lavoro sui progetti software
argument-hint: "[progetto o compito, es. opero fatture]"
---

# /nicola — modalità sviluppo

Assisti **Nicola Larezza**, co-founder e lead dev. Registro Trevis: postura e
formule vietate stanno già in `~/.claude/CLAUDE.md`. Apri
`03-Storage/azienda/registro-trevis.md` **solo** se una risposta è uscita male e
serve il dettaglio. I testi destinati ai clienti hanno un altro registro e non
si scrivono in questa modalità.

Riprendi come se la conversazione non si fosse mai interrotta: niente
presentazioni, niente spiegazione del comando, prima riga agganciata allo stato
del lavoro.

## 1. Aggancia il brain

```bash
V="${DENKI_VAULT:-}"
for p in "$V" "$PWD" "$HOME/lavoro/denki-brain" "$HOME/Desktop/denki-brain"; do
  [ -n "$p" ] && [ -f "$p/CLAUDE.md" ] && V="$p" && break
done
cd "$V" && git pull --rebase --autostash -q 2>&1 | tail -2
python3 "$V/01-Coding/strumenti/installa-macchina.py"
ls -1 "$V/06-Daily" | sort | tail -1
```

⚠️ **La riga di `installa-macchina.py` non è opzionale e va dopo il pull.**
`~/.claude/` (protocollo, agente `operatore`, comandi, skill nostre) è locale
alla macchina: il pull porta le copie canoniche nel vault, non le installa.
Senza quella riga, su una macchina che non è quella dove il vault è stato
scritto si lavora con i comandi della settimana scorsa. Quello che riscrive vale
**dalla sessione dopo**: questa era già caricata.

Vault non trovato → **chiedi il percorso**, non cercarlo a tappeto.

## 2. Leggi il minimo, e verifica prima di fidarti

1. `CLAUDE.md` del vault — **salta se è già nel contesto**.
2. L'ultima nota di `06-Daily/`. Sono tarate a 40 righe: si legge intera.
3. **Solo se** `$ARGUMENTS` nomina un progetto: la sua riga in `indice.md`, e la
   nota solo se quella riga dice che serve.

Nient'altro. Niente `02-Sales/`, niente `03-Storage/`, niente scansioni di
cartelle. Se manca un dato, **chiedilo**: una domanda costa meno di cinque file.

**Il passaggio di verifica, prima di scrivere codice o di dare un fatto per
buono**: una nota `source: claude` senza `verificato:` è un'ipotesi. Il fatto si
controlla dove vive davvero — `git log` del repo, il sito online, lo schema del
database, o Nicola — e chi lo controlla scrive `verificato: <data>` nella nota.
Vale anche per la daily di ieri: la scrive Nicola a domande, ma un numero senza
data resta un numero da ricontrollare.

## 3. `trappole.md` — a sezioni, non tutto

Il file è la memoria degli errori già pagati ed è lungo. **Non si legge
intero.** Si legge l'indice delle sezioni in testa e si apre solo quella del
lavoro di oggi:

```bash
grep -n '^## ' 01-Coding/trappole.md
```

**Quello che c'è dentro è descrittivo, non prescrittivo.** Una trappola dice
cosa è andato storto una volta e come si è aggirata. Non è una regola di casa: le
regole stanno in `01-Coding/stack/convenzioni.md` e nel `CLAUDE.md` del repo. Le
voci marcate `[SCARTATO]` sono strade che non funzionano: non si ripropongono, e
se vanno riaperte si dichiara che le si sta riaprendo.

## 4. Dove stanno i repo — Mac di Nicola, tutto in `~/lavoro`

La cartella si chiama **come il repo**.

| Progetto | Cartella | Ramo | Memoria |
|---|---|---|---|
| **OperO** | `~/lavoro/opero-sito` | `main` | `CLAUDE.md` + `docs/handoff.md` |
| **DenkiShift** | `~/lavoro/smooth-duty` | `main` | `CLAUDE.md` + `docs/` |
| **OperO 1** (sola lettura) | `~/lavoro/sebapp-bolanos` | `origin/main` | è la specifica, non si tocca |
| **cococat** | `~/lavoro/cococat-site` | — | sito vetrina |

Il prodotto di `smooth-duty` è **DenkiShift**, il pacchetto npm `turni`. Su
un'altra macchina i percorsi sono altri: si correggono qui, non si smentiscono
altrove.

## 5. Quello che governa il lavoro tecnico

- **Sul tecnico ha ragione il repo.** Il suo `CLAUDE.md` viene prima di
  qualunque riassunto tu abbia in testa.
- **Due stack diversi, e restano diversi.** OperO è Vite 8 + Tailwind 3, commenti
  in inglese. DenkiShift è Next 16 + Tailwind 4, commenti in italiano. Non
  uniformare di tua iniziativa.
- **Il push non ha la stessa regola ovunque.** Conferma nel `CLAUDE.md` del repo.
  Il vault invece si pusha sempre e subito.
- **Credenziali mai nel vault**, e mai digitate da te.
- **Se emerge una scelta**, nota nuova in `05-Decisioni/`, corta. Quello
  che generi tu è `source: claude` e nasce senza `verificato:`.
- **Il Mac di Patrick applica le modifiche allo schema di DenkiShift in
  sviluppo.** La produzione no, su nessuno dei due prodotti.

## 6. Rispondi così, e poi fermati

Massimo otto righe:

```
Nicola — <data>. <una riga: dove sta il lavoro tecnico adesso>

Sul tavolo:
- <3 nodi tecnici aperti, una riga ciascuno>

<una riga: il vincolo che morderà oggi>
```

Niente preamboli, niente elenco dei file letti, **niente proposte su cosa fare
dopo**. Se `$ARGUMENTS` contiene già un compito, salta il riepilogo e attacca.
