---
type: area
updated: 2026-08-28
source: claude
---

# Patrick, come mettere il Mac in condizione di modificare DenkiShift

Guida passo passo, scritta per chi **non scrive codice**. Serve una volta sola:
finito questo, il sito si apre, si modifica e il database si aggiorna.

⚠️ **In questa nota non c'è nessuna chiave, e non ce ne deve finire mai.** Il
vault sta su GitHub. Qui c'è scritto **dove cliccare** per leggerle, non quali
sono → [[credenziali]].

## Il problema, detto semplice

Il codice di DenkiShift ce l'hai: sta nella cartella sul Desktop. Quello che
manca sono **tre valori** che dicono all'app *a quale database parlare e con
quale permesso*. Sono in tre righe dentro due file di testo che **non stanno su
GitHub apposta** — perché sono password, e le password non si spediscono: ognuno
se le legge da sé.

Senza quei tre valori l'app parte e non trova niente, e ogni comando che tocca
il database si ferma alla prima riga. Non è rotto: è vuoto.

## Cosa ti serve, in tutto

| # | Cosa | Dove |
|---|---|---|
| 1 | La cartella del codice | `~/Desktop/smoothduty` |
| 2 | Node installato | [[setup-macchina-nuova]] |
| 3 | Due file di testo con tre valori dentro | li crei tu, sotto |
| 4 | L'accesso al pannello Supabase | progetto **DenkiShift sviluppo**, `rytuurzafjxzlrpgforj` |

## I passi

Si fa tutto nel **Terminale** (⌘+Spazio → scrivi `Terminale` → Invio). I comandi
si copiano e si incollano uno alla volta, e dopo ognuno si preme Invio.

### 1 — Entra nella cartella e controlla che ci sia tutto

```bash
cd ~/Desktop/smoothduty
ls
node -v
```

`ls` deve elencare dei nomi fra cui `package.json` e `src`. Se dice
*No such file or directory*, la cartella si chiama diversamente: lancia
`ls ~/Desktop` e guarda com'è scritta davvero.

`node -v` deve rispondere con un numero (`v22.…`). Se dice
*command not found*, Node non c'è: quello si installa prima, vedi
[[setup-macchina-nuova]].

### 2 — Installa quello che serve al progetto

```bash
npm install
```

Ci mette un paio di minuti e stampa molte righe: è normale. Va lanciato una
volta sola, e **ogni volta che Nicola ti dice di rifare `npm install`**.

> Fino al 28 agosto 2026 qui mancava un pacchetto (`pg`) e i comandi del
> database si fermavano con `Cannot find package 'pg'`. Adesso è dichiarato nel
> progetto: `npm install` basta, non devi installare niente a mano.

### 3 — Riempi i due file dei valori

**Sul tuo Mac i due file esistono già**: sono stati predisposti il 28 agosto
2026, vuoti. Controlla:

```bash
ls -a | grep env
```

Se compaiono `.env.local` e `.env.db`, **salta al comando `open -e`** qui sotto.
Se non ci sono, si copiano dai modelli:

```bash
cp .env.local.example .env.local
cp .env.db.example .env.db
```

Si aprono in TextEdit, uno per volta:

```bash
open -e .env.local
```

Dentro trovi tre righe con delle parentesi angolari. **Sostituisci le parentesi
e quello che c'è dentro** con il valore vero — la parte prima dell'`=` non si
tocca, e non si mettono virgolette né spazi intorno all'`=`.

Poi salva (⌘+S) e chiudi. Stessa cosa con l'altro:

```bash
open -e .env.db
```

> Questi due file **non compaiono nel Finder**: iniziano con un punto e macOS li
> nasconde. Non li hai persi. Per vederli nel Finder: ⌘+⇧+. (punto).

### 4 — Dove si leggono i tre valori

Nel pannello Supabase, progetto **DenkiShift sviluppo**:

| Riga da riempire | Dove sta |
|---|---|
| `NEXT_PUBLIC_SUPABASE_URL` | *Project Settings › API* → **Project URL** |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | *Project Settings › API* → chiave **anon / publishable** |
| `SUPABASE_SERVICE_ROLE_KEY` | *Project Settings › API* → chiave **service_role / secret** |
| `SUPABASE_DB_PASSWORD` | *Project Settings › Database* → **Database password** |

Le prime tre vanno in `.env.local`, l'ultima in `.env.db`.

⚠️ **`service_role` scavalca ogni regola di sicurezza.** Resta in quel file e
basta: non si incolla in chat, non si manda su WhatsApp, non le si mette davanti
`NEXT_PUBLIC_` — quel prefisso la spedirebbe dentro il browser di chiunque apra
il sito.

⚠️ Se la *Database password* non l'hai mai vista, **non è recuperabile**: si
genera nuova da lì, e chi la usava sulle altre macchine deve rimettere quella
nuova. Sentì Nicola prima di rigenerarla.

### 5 — Verifica che funzioni

```bash
node --env-file=.env.local --env-file=.env.db scripts/verifica-schema.mjs
```

È il comando che dice se il database è a posto. Se risponde che va tutto bene,
**hai finito**: i tre valori sono giusti.

Se elenca delle migrazioni mancanti, stampa anche il comando da lanciare per
ciascuna. Lanciali nell'ordine in cui li scrive:

```bash
node --env-file=.env.local --env-file=.env.db scripts/esegui-sql.mjs supabase/NN-nome.sql
```

Si possono rilanciare senza danni e **nessuno cancella turni**.

### 6 — Guarda il sito

**Su [denkishift.it](https://denkishift.it), non in locale.** Dal 28 agosto 2026
l'app sta online ed è quello il posto in cui si guarda: stessa build, stesso
database, PWA vera, telefono vero.

L'avvio in locale (`npm run dev` → `http://localhost:3000`) non è stato tolto,
ma serve solo nei casi rari — nessuna rete, oppure un guasto da smontare
leggendo i log del server. Non è più il giro normale.

⚠️ **La conseguenza pesa**: si verifica *dopo* aver pubblicato, e quello che
finisce online lo vede la squadra di un cliente. Non è il posto dove si prova
una cosa a caso.

## Se qualcosa non va — cosa vuol dire davvero

| Ti risponde | Vuol dire | Cosa fai |
|---|---|---|
| `command not found: node` | Node non è installato | [[setup-macchina-nuova]] |
| `No such file or directory` | sei nella cartella sbagliata | `cd ~/Desktop/smoothduty` |
| `Cannot find package 'pg'` | manca l'installazione | `npm install` |
| `password authentication failed` | la password del database è sbagliata | rileggi il punto 4, riga `SUPABASE_DB_PASSWORD` |
| `Invalid API key` | una delle chiavi in `.env.local` è sbagliata o troncata | ricopiala intera, senza spazi |
| `Could not find the column … in the schema cache` | **non è un errore tuo**: il database ha la colonna, l'app ha in memoria una copia vecchia | aspetta un minuto e ricarica. Se resta, scrivi a Nicola |
| il sito si apre ma è vuoto | il database non ha i dati, o manca una migrazione | rilancia `verifica-schema.mjs` |
| `password authentication failed` **dopo che prima funzionava** | qualcuno ha rigenerato la password del database: la vecchia non vale più su nessuna macchina | rileggila dal pannello e avvisa Nicola, che deve rimetterla anche sulla sua |

## ⚠️ Due database, e i tuoi valori arrivano a uno solo

Da chiarire con Nicola **prima** di usare questa guida per cambiare qualcosa:

- I tre valori che riempi puntano al progetto di **sviluppo**
  (`rytuurzafjxzlrpgforj`). Lì si può sbagliare senza danni.
- Il sito che si guarda, `denkishift.it`, gira su un progetto Supabase
  **diverso**, di produzione, che quei file non raggiungono.

Dalla decisione del 28 agosto la migrazione al database di produzione va fatta
**prima** del push, altrimenti il codice pubblicato chiede colonne che là non
esistono e il tabellone si apre vuoto. Quel passaggio **non è coperto da questa
guida** e oggi non lo fa il tuo Mac: chiedi a Nicola come si fa, o falla fare a
lui.

## Le tre righe che non si superano

1. **Solo sviluppo.** Questi comandi valgono sul progetto DenkiShift di
   sviluppo. La **produzione** — di DenkiShift e di [[opero]] — non si tocca da
   qui: là dentro ci sono i dipendenti veri delle aziende che pagano.
2. **Le modifiche al database si scrivono in un file**, non si digitano nel SQL
   Editor del pannello. Una modifica fatta a mano e non scritta è una modifica
   che la prossima macchina non avrà, e il giorno dopo le due non tornano.
3. **Le chiavi non si spostano.** Non si incollano in chat né si mandano per
   messaggio: si rileggono dal pannello, ogni volta, su ogni macchina.

## Per cambiare il sito, non solo il database

Il codice si modifica con Claude Code, che però **deve arrivare alla cartella**:
se la sessione è aperta sul vault, `~/Desktop/smoothduty` non è raggiungibile e
va aggiunta come cartella di lavoro. Poi vale la regola del repo: si guarda la
modifica nel browser prima di dire che funziona.

> [!note] Analisi di Claude — 2026-08-28
> Questa guida l'ho ricostruita dai `docs/` del repo e dai file di esempio
> `.env.local.example` / `.env.db.example`, **non l'ho eseguita su un Mac**: i
> comandi macOS (`open -e`, ⌘+⇧+.) e i nomi delle voci del pannello Supabase
> sono la parte da correggere per prima se non tornano. Il primo che la segue
> davvero scriva qui cosa era diverso.
>
> Quello che invece **è stato verificato da quella macchina** il 28 agosto sta
> in [[setup-macchina-nuova]], punto 7-ter: i due file esistono già vuoti, e la
> catena verso il database arriva fino in fondo — l'host risponde, si ferma
> solo sulla password. Cioè: manca davvero solo il punto 4.

## Collegamenti

[[credenziali]] · [[modifiche-al-database]] · [[setup-macchina-nuova]] ·
[[denkishift]] · [[2026-08-28-supabase-denkishift-sul-mac]]
