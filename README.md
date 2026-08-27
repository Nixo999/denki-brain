# Il second brain di DenkiCode — istruzioni per l'uso

Questa cartella è la memoria dell'azienda. Sta su GitHub, si legge con un
programma gratuito che si chiama **Obsidian**, e Claude Code la usa per sapere
chi siete e cosa state facendo senza che glielo rispieghiate ogni volta.

Questa guida è scritta per chi **non ha mai aperto Obsidian**. Se una parte ti
sembra ovvia, saltala.

---

## 1. Installare Obsidian e aprire il vault

### Cos'è Obsidian, in una riga

Un programma che apre una cartella di file di testo e li mostra bene, con i
collegamenti fra loro. **Non è un database e non è un servizio online**: i tuoi
file restano file `.md` normali sul tuo disco. Se domani disinstalli Obsidian,
li apri col Blocco note e ci sono tutti.

Per questo funziona bene con git e con Claude Code: sono solo file di testo.

### Installazione

1. Vai su **https://obsidian.md** e scarica la versione per Windows
2. Installa e apri
3. Alla prima schermata scegli **"Open folder as vault"**
   *(non "Create new vault": la cartella esiste già)*
4. Seleziona `C:\Users\User\Desktop\denkicode volt`
5. Obsidian chiede se ti fidi degli autori della cartella → **sì**, l'hai
   scritta tu

Ora vedi a sinistra le cartelle da `00-Inbox` a `99-Templates`.

**"Vault" vuol dire semplicemente "questa cartella".** Non c'è niente di magico.

### La prima cosa da fare

Apri `dashboard.md`. Per ora vedrai dei blocchi di codice grigi invece di
tabelle: è normale, manca un plugin. Lo installi al punto 3.

---

## 2. Le quattro cose che devi capire

### Le note

Ogni file `.md` è una nota. Si scrive in **Markdown**, che è testo normale con
qualche simbolo:

```markdown
# Titolo grande
## Titolo più piccolo

Testo normale, **grassetto**, *corsivo*.

- elenco
- puntato

- [ ] cosa da fare
- [x] cosa fatta
```

È tutto. Non serve altro.

### I wikilink — le doppie parentesi quadre

Questa è la parte che rende il vault diverso da una cartella di documenti.

Scrivendo `[[opero]]` dentro una nota, crei un **collegamento cliccabile** alla
nota `opero.md`, ovunque essa sia nel vault.

Esempio vero, preso da `02-Areas/clienti/cliente-opero.md`:

```markdown
Ci ha commissionato la ricostruzione: [[opero]].
```

Clicchi su `opero` e sei nella scheda del progetto.

**La cosa utile viene dopo.** Apri `01-Projects/opero.md` e guarda in fondo:
c'è un pannello **"Backlinks"** (se non lo vedi: menu in alto a destra della
nota → *Backlinks*). Ti mostra **tutte le note che parlano di OperO**, senza che
tu le abbia mai elencate. Al momento sono la scheda cliente, due decisioni, la
dashboard, le note su stack e listino.

Questo è il vero valore: **non devi ricordarti cosa è collegato a cosa.**

Se scrivi `[[qualcosa-che-non-esiste]]`, il link appare più chiaro. Non è un
errore: è un promemoria che quella nota va ancora scritta. Cliccandolo, Obsidian
la crea.

### Il frontmatter — il blocco in cima con i trattini

Apri `01-Projects/opero.md`. Le prime righe sono queste:

```yaml
---
type: progetto
status: attivo
client: cliente-opero
stack: [react-19, typescript, vite-8, tailwind-3, ...]
started: 2026-07-20
deadline: TODO
updated: 2026-08-28
valore: 2400
incassato: 400
---
```

Sono **etichette leggibili da un programma**. Obsidian le mostra come proprietà
in cima alla nota, e puoi modificarle cliccandoci sopra.

A cosa servono: grazie a `valore: 2400` e `incassato: 400`, la dashboard può
calcolare da sola che OperO deve ancora incassare 2.000 € — senza che tu lo
scriva da nessuna parte.

⚠️ **Se sbagli a scrivere un campo, non ricevi nessun errore: la nota
semplicemente sparisce dalle tabelle.** È l'unico modo in cui questo sistema si
rompe in silenzio. Gli schemi giusti sono in `CLAUDE.md`, e i comandi
`/nuovo-progetto` e `/nuovo-cliente` li scrivono per te.

### La graph view — il grafo

Icona a sinistra che sembra una costellazione (o `Ctrl+G`).

Vedi tutte le note come palline collegate dai wikilink. Oggi, nel tuo vault,
vedrai tre grappoli:

- attorno a **`opero`**: il cliente, le due decisioni, lo stack, i vincoli fiscali
- attorno a **`denkishift`**: listino, flusso di vendita, obiettivi
- attorno a **`generazione-lead`**: metriche, flusso di vendita, ruoli, materiale

**A cosa serve davvero**: a vedere cosa è isolato. Una nota senza collegamenti
sta ai bordi del grafo da sola, e quasi sempre vuol dire che è stata scritta e
poi dimenticata. Oggi ci trovi `webolt-v1` — che infatti è un repo vuoto.

Non guardarlo tutti i giorni. Guardalo una volta al mese: ti dice come sta il
vault.

---

## 3. I plugin da installare

Obsidian di base non fa quasi niente. Tre plugin lo rendono utile.

Si installano tutti allo stesso modo:

> **Impostazioni** (rotella in basso a sinistra) → **Community plugins** →
> se chiede, **Turn on community plugins** → **Browse** → cerca il nome →
> **Install** → **Enable**

### Dataview — le tabelle che si aggiornano da sole

**Installalo per primo.** È quello che fa funzionare `dashboard.md`.

Senza Dataview, per sapere quali progetti sono attivi devi aprirli uno per uno.
Con Dataview scrivi una domanda e lui la risponde ogni volta che apri la nota.

Questa, che è già dentro la tua dashboard, elenca i progetti non chiusi in
ordine di quanto sono fermi:

````markdown
```dataview
TABLE WITHOUT ID
  file.link AS "Progetto",
  client AS "Cliente",
  status AS "Stato",
  updated AS "Aggiornato"
FROM "01-Projects"
WHERE type = "progetto" AND status != "completato"
SORT updated ASC
```
````

**Non devi imparare a scriverle.** Se ti serve una tabella nuova, chiedi a
Claude: *"aggiungi alla dashboard una tabella dei clienti che non sentiamo da
più di un mese"*.

Dopo l'installazione, apri `dashboard.md`: i blocchi grigi sono diventati
tabelle.

### Obsidian Git — il salvataggio automatico su GitHub

Fa i commit e i push da solo, così non devi ricordartene.

Impostazioni consigliate (**Impostazioni → Obsidian Git**):

| Opzione | Valore | Perché |
|---|---|---|
| Vault backup interval (minutes) | `10` | Salva ogni 10 minuti se hai cambiato qualcosa |
| Auto pull interval (minutes) | `10` | Scarica quello che ha scritto Patrick |
| **Pull updates on startup** | **ON** | ⚠️ La più importante: vedi il punto 7 |
| Commit message | `vault: {{date}}` | Messaggio automatico |

⚠️ I commit automatici hanno messaggi generici. Quando fai un lavoro vero,
usa `/chiudi-sessione` da Claude Code: scrive un messaggio che spiega **cosa** è
cambiato e **perché**, come si fa nei vostri repo di codice.

### Bases — le tabelle senza scrivere codice

È il costruttore di viste integrato in Obsidian (versioni recenti): crei una
tabella filtrabile cliccando, senza sintassi.

**Per te è il secondo, non il primo.** Dataview è già configurato e funziona.
Bases è comodo il giorno in cui vuoi una vista tua — per esempio i clienti
ordinati per credito aperto — senza chiedere a nessuno. Guardalo fra un mese.

### Un quarto, opzionale ma comodo

**Templater**: ti fa creare una nota nuova già compilata dai file in
`99-Templates/`. Senza, i template li copi a mano (o li fa Claude coi comandi
`/nuovo-progetto` e `/nuovo-cliente`, che è già più veloce).

---

## 4. Le dashboard

**La dashboard c'è già**: apri `dashboard.md`. Contiene:

| Sezione | Cosa mostra |
|---|---|
| 🔨 Progetti attivi | Tutto ciò che non è chiuso, il più fermo in cima |
| ⏰ Fermi da 14+ giorni | Quello che stai dimenticando |
| 💰 Soldi in ballo | Pattuito, incassato, da incassare — oggi: **2.000 € da OperO** |
| 👥 Clienti | Con settore e progetti collegati |
| 🧭 Decisioni aperte | Le scelte che avete lasciato a metà |
| ✅ Cose da fare | Ogni `- [ ]` di tutto il vault, raccolto in un posto |
| 📥 Inbox da svuotare | Le catture non ancora sistemate |

### Come tenerla a portata

1. Aprila
2. Click destro sul titolo della scheda in alto → **Pin**
3. Diventa la nota che trovi aperta ogni volta

Se vuoi che sia la prima cosa all'avvio: **Impostazioni → Appearance →**
oppure semplicemente lasciala pinnata, Obsidian riapre l'ultima sessione.

### Perché funziona

Le tabelle leggono il **frontmatter**. Quindi: se aggiorni il campo
`updated:` di un progetto, la dashboard si riordina da sola. Se metti
`status: completato`, il progetto sparisce dagli attivi.

**Non c'è niente da aggiornare a mano nella dashboard.** Aggiorni le note,
lei segue.

---

## 5. La routine

### All'apertura (2 minuti)

1. Apri **`dashboard.md`**
2. Guarda **"Fermi da 14+ giorni"**. Se c'è qualcosa, decidi: lo riprendi, lo
   metti in pausa, o lo archivi
3. Guarda **"Soldi in ballo"**. Se un credito è fermo da settimane, quello è il
   lavoro più redditizio della giornata

### Durante il giorno — catturare

Ti dicono una cosa importante? **Non decidere dove va.** Apri una nota in
`00-Inbox/`, scrivi due righe, chiudi.

`Ctrl+N` crea una nota nuova. Il nome puoi metterlo a caso.

Esempi di cose da buttare in Inbox:
- *"Il cliente di OperO al telefono ha detto che vuole l'XML entro settembre"*
- *"Il barista di via Roma ha chiesto quanto costa un sito"*
- *"Idea: nello script di Giulia partire dall'orario di apertura"*

Una volta a settimana chiedi a Claude: **"svuota l'inbox"**, e le smista lui.

### A fine sessione di lavoro

Da Claude Code, in questa cartella:

```
/chiudi-sessione
```

Scrive la nota di giornata in `06-Daily/`, aggiorna i campi `updated`, fa commit
e push. È il comando che tiene vivo il vault: se lo salti, fra due settimane la
dashboard mente.

### Il lunedì

```
/settimana
```

Cosa è cambiato, cosa è fermo, e i numeri di [[metriche]] — chiamate e
appuntamenti — confrontati coi target (50 e 4).

### Ogni due settimane

```
/aggiorna-progetti
```

Controlla i commit veri dei repo `opero-sito` e `smooth-duty` e ti dice dove le
note del vault sono rimaste indietro rispetto al codice.

---

## 6. Come interrogare Claude Code

Apri il terminale in questa cartella e lancia `claude`. Non serve spiegargli
niente: legge `CLAUDE.md` da solo e sa già chi siete.

**Dieci domande vere che puoi fargli, oggi:**

1. *"Quanto ci devono in totale i clienti, e da quanto tempo?"*
2. *"Riassumimi lo stato di OperO come se dovessi spiegarlo a Patrick in due
   minuti prima di una call col cliente."*
3. *"Cosa manca esattamente a DenkiShift per poterlo installare dal primo
   cliente pagante? Mettili in ordine di quanto bloccano la vendita."*
4. *"Scrivimi lo script telefonico per Giulia sul flusso A, per un negozio di
   parrucchieri che ha Instagram ma non ha il sito."*
5. *"Ho un'azienda di 15 dipendenti interessata ai turni. Prepara a Patrick la
   traccia della demo e le tre obiezioni più probabili."*
6. *"Quanto ci resta sul tetto dei 5.000 € della prestazione occasionale, e cosa
   succede se incassiamo i 2.000 di OperO questo mese?"*
7. *"Guarda i commit di `opero-sito` dell'ultima settimana e aggiorna la nota
   del progetto con quello che è cambiato."*
8. *"Prepara la bozza del PDF di proposta commerciale per un gestionale custom
   da 2.500 €."*
9. *"Quali decisioni sono ancora aperte e da quanto tempo?"*
10. *"Mi hanno chiesto un e-commerce. Non abbiamo mai fatto un prezzo per il
    prodotto B: propone tu una struttura di prezzo coerente col resto del
    listino."*
11. *"Quali TODO sono rimasti nel vault? Elencali per importanza."*
12. *"Il cliente vuole una funzione che non era nel piano. Scrivimi il messaggio
    che Patrick gli manda su WhatsApp per dirgli che è lavoro nuovo, senza
    farlo sembrare un no."*

**Il modo giusto di chiedere**: dagli il contesto che ha in testa un umano.
Non *"scrivi uno script"* ma *"scrivi lo script per un ferramenta di Seveso, che
ha 4 dipendenti e non risponde mai al telefono la mattina"*. La differenza è
tutta lì.

**Due cose da sapere**

- Claude marca quello che genera lui con `source: claude` nel frontmatter, o con
  un riquadro *"Analisi di Claude"* dentro la nota. Quello che avete scritto voi
  è `source: denkicode`. **Non fidarti di un'analisi mia come di un fatto vostro**
- Se non sa una cosa, scrive `TODO` invece di inventarla. Quando ne vedi uno,
  riempilo: sono i buchi veri del vault

---

## 7. Sincronizzare su un secondo PC, senza conflitti

### La prima volta, sul PC nuovo

```bash
git clone https://github.com/<tuo-utente>/<nome-repo>.git
```

Poi apri Obsidian → **Open folder as vault** → scegli la cartella appena
scaricata. Trovi tutto: note, plugin, impostazioni.

*(I plugin ti seguono perché `.gitignore` traccia apposta `.obsidian/plugins/`.
Quello che non ti segue è la disposizione delle finestre — ed è voluto: è
l'unica cosa che genererebbe conflitti a ogni singolo salvataggio.)*

### La regola per non avere conflitti

**Una sola, e vale sempre:**

> ### `git pull` prima di cominciare a scrivere. Sempre.
> ### Push prima di chiudere. Sempre.

È la stessa regola che c'è già scritta nei `docs/` di OperO e DenkiShift, per lo
stesso motivo: chi comincia da un albero vecchio scrive contro un'azienda che
non esiste più.

Se hai attivato **Obsidian Git** con *Pull on startup*, il pull lo fa lui
all'apertura. Ma se lasci Obsidian aperto per giorni, quel pull non riparte:
quando torni al PC dopo qualche giorno, forzalo a mano dal comando
*"Obsidian Git: Pull"* (`Ctrl+P` → scrivi "pull").

### Le altre due precauzioni

1. **Non tenere il vault aperto su due PC contemporaneamente.** Il conflitto
   nasce quasi sempre così: due copie aperte, due modifiche allo stesso file,
   nessuna delle due sa dell'altra
2. **Tu e Patrick scrivete in note diverse.** Git risolve da solo le modifiche
   a file diversi. Se invece scrivete tutti e due in `stato-azienda.md` nello
   stesso pomeriggio, il conflitto arriva. Regola pratica: **Patrick tocca
   `02-Areas/clienti/` e `business/`, tu il resto** — e se dovete lavorare
   insieme sullo stesso file, sentitevi prima

### Se il conflitto succede lo stesso

Non è grave e non si perde niente. Il file si riempie di righe così:

```
<<<<<<< HEAD
Incassato: 400 €
=======
Incassato: 900 €
>>>>>>> origin/main
```

Sopra c'è la tua versione, sotto quella arrivata dall'altro PC. Cancelli le tre
righe di marcatori e tieni il testo giusto (spesso: tutti e due, uniti). Salvi,
committi.

Oppure apri Claude Code in cartella e scrivi: **"risolvi i conflitti git nel
vault"**. Li legge e ti propone l'unione.

### ⚠️ La cosa da non fare mai

**Non usare `git push --force`.** Su un repo condiviso cancella il lavoro
dell'altro senza chiedere. Se il push viene rifiutato:

```bash
git pull --rebase
```

...guarda cosa è arrivato, e riprova.

---

## Riferimento rapido

| Voglio... | Faccio... |
|---|---|
| Vedere come va | Apro `dashboard.md` |
| Segnare una cosa al volo | Nota nuova in `00-Inbox/`, due righe |
| Chiudere la giornata | `/chiudi-sessione` |
| Riepilogo settimanale | `/settimana` |
| Controllare i progetti | `/aggiorna-progetti` |
| Aggiungere un progetto | `/nuovo-progetto` |
| Aggiungere un cliente | `/nuovo-cliente` |
| Sapere cosa è collegato a cosa | Apro la nota e guardo i **Backlinks** |
| Trovare qualcosa | `Ctrl+Shift+F` |
| Capire le regole del vault | Leggo `CLAUDE.md` |

---

## Se ti dimentichi tutto

Ricordati solo queste tre:

1. **`dashboard.md` la mattina**
2. **`00-Inbox/` per tutto quello che non sai dove mettere**
3. **`/chiudi-sessione` alla fine**

Il resto lo fa Claude.
