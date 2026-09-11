---
description: Apre il banco DM e, se oggi non ci sono, costruisce e pubblica le tre liste del giorno — 50 siti, 50 DenkiShift, 30 ricerca di mercato
argument-hint: "[apri | siti | denkishift | ricerca | un numero, es. «siti 30»]"
---

# /banco — il banco DM, con le liste del giorno già dentro

Lo lancia **Patrick**, che non usa il terminale e non scrive codice: qui dentro
si fa tutto da soli e alla fine si dice una cosa sola, cosa c'è sul banco.

Registro Trevis, già in `~/.claude/CLAUDE.md`: niente presentazioni, niente
«adesso procedo a», niente proposte su cosa fare dopo.

**Due velocità, e si sceglie da soli:**

| Se | Allora |
|---|---|
| le liste di **oggi** esistono già in `02-Sales/liste/` | si apre il banco e si risponde in tre righe. Costa un minuto |
| non ci sono, o l'argomento dice quale rifare | si costruiscono, si verificano, si pubblicano, poi si apre |

`/banco apri` salta sempre la costruzione. `/banco siti`, `/banco denkishift`,
`/banco ricerca` ne rifanno una sola. Un numero cambia le righe: `/banco siti 30`.

---

## 1 · Aggancio, e cosa c'è adesso

```bash
V="${DENKI_VAULT:-}"
for p in "$V" "$PWD" "$HOME/lavoro/denki-brain" "$HOME/Desktop/denki-brain"; do
  [ -n "$p" ] && [ -f "$p/CLAUDE.md" ] && V="$p" && break
done
cd "$V" && git pull --rebase --autostash -q 2>&1 | tail -2
python3 "$V/02-Sales/strumenti/stato-banco.py"
ls -1 "$V/02-Sales/liste"/$(date +%F)-*.csv 2>/dev/null || echo "nessuna lista di oggi"
```

L'ultima riga decide: se le tre liste di oggi ci sono, si va al passo 5.

⚠️ **Il conto vero degli invii sta nel browser di Patrick**, non nei CSV. Se
lui dice di averne mandati trenta e lo script dice zero, ha ragione lui.

---

## 2 · Le tre liste, e sono tre mestieri diversi

Regola di Patrick dell'11 settembre 2026, in [[metodo-liste]]: *«gli script e i
ganci devono essere inerenti alla tipologia di servizio per cui li contattiamo
e anche le aziende devono essere ad alta conversione in base al servizio che
stiamo offrendo»*. Quindi: **tre liste, tre target, tre testi. Non si mescolano.**

Il come si costruisce una riga — trovare il profilo, leggerlo, verificare, non
riscrivere a chi è già in lista — sta in [[metodo-instagram]] e non si ripete
qui. Qui c'è **chi ci va dentro** e **cosa gli si dice**.

### 2a · Siti vetrina — 50 righe, colonna `Prodotto: siti`

**Chi converte** (misurato, [[metodo-instagram]]): onicotecniche e nail center,
estetiste singole, parrucchieri piccoli, barber, toelettature, tatuatori e PMU,
fotografi e wedding. Nei comuni grossi i saloni con la vetrina il sito ce
l'hanno già: **restano le singole**, ed è lì che si pesca.
**Fuori**: mobilifici e arredamento (6 su 6 col sito), negozi (la domanda
giusta è «vende online», è un altro flusso), catene, chi ha un sito vivo e
curato, i profili sotto i ~200 follower.
**Comuni**: quelli che le liste degli ultimi dieci giorni non hanno toccato —
si guarda l'elenco nelle note delle liste in `02-Sales/liste/`.

**Il gancio è uno solo, e dall'11 settembre 2026 non si ammorbidisce**
([[stile-comunicazione]], regola di Patrick): *«per i siti il gancio deve
essere che la bozza è già stata fatta»*. Nel messaggio si scrive **«la bozza
del suo sito è già pronta»**, non «gliela preparo», non «le mando una prima
schermata».
⚠️ Il che vuol dire che quando uno risponde la bozza deve esistere: chi manda
questi cinquanta si compra il lavoro di farle. È il prezzo del gancio più
forte che abbiamo, e lo paga chi risponde per primo.

Gancio `1-6` nella colonna, come oggi: 1 nessun sito, 2 dominio morto,
3 parcheggiato, 4 link rotto, 5 piattaforma (Fresha, Wix, Linktree: **il
messaggio la nomina**, o il titolare ti corregge), 6 vivo ma vecchio.

### 2b · DenkiShift — 50 righe, colonna `Prodotto: denkishift`

**Chi converte** (resa del 10 settembre: ristoranti con sito 71%, alberghi
43%): squadre da **8 a 50 persone su turni, indipendenti**. Alberghi con
ristorante o spa, ristoranti con doppio turno, RSA e cooperative
socio-assistenziali, imprese di pulizie, vigilanza privata, logistica e
magazzini, palestre con reception e istruttori, panetterie e pasticcerie con
laboratorio, poliambulatori.
**Il sito non c'entra: chi ce l'ha curato è un candidato migliore**, perché è
uno che investe. I profili scartati dalle liste siti «perché il sito ce
l'hanno» sono il bacino naturale di questa.
**Fuori**: catene e filiali (il software glielo impone la sede), sotto le 8
persone, orario fisso.

Gancio `T`. Il messaggio dice **una cosa vera vista sul profilo** (le trenta
camere, il post che cerca un cameriere, la seconda sede), **una domanda sui
turni**, cosa fa il programma in una frase, e chiede **dieci minuti in
videochiamata**. Mai una data di attivazione, mai il prezzo al mese, mai un
link → [[dm-instagram-denkishift]], [[denkishift]].

### 2c · Ricerca di mercato — 30 righe, colonna `Prodotto: ricerca`

**Chi converte**: aziende **strutturate**, che hanno già dei processi da
raccontare. Officine e carrozzerie, impiantisti elettrici e termoidraulici,
edilizia e serramenti, ingrossi e distribuzione, trasporti e logistica,
falegnamerie e lavorazioni meccaniche, aziende agricole con vendita, studi
tecnici. Su Instagram devono essere **vive**: post degli ultimi mesi, mezzi,
magazzino, gente al lavoro nelle foto.
**Fuori**: chi improvvisa, i negozi piccoli, i liberi professionisti singoli.

Gancio `R`. Il modulo è quello di [[script-indagine]] — *Analisi di Mercato:
Digitalizzazione e Sviluppo delle PMI del Territorio*, sei domande, anonimo,
il contatto solo in fondo e facoltativo:

```
https://docs.google.com/forms/d/e/1FAIpQLSe2cCfeAx8IVLRq-ocJe4MUpq43u_1D95IpBPjqOYX-90a9JA/viewform
```

⚠️ **Il link che gira ai lead è questo (`/viewform`).** Quello che finisce in
`/edit` è il pannello di chi il modulo lo scrive, e non si manda a nessuno.

**Qui non si vende niente, e non è un modo di dire**: zero prodotti, zero
prezzi, zero programmi nominati. Se nomini un prodotto la ricerca diventa una
scusa per vendere e la lista muore, per tutti e tre → [[script-indagine]].
Il contraccambio si promette e **si mantiene**: il riepilogo di cosa è venuto
fuori dalle aziende della zona.
Il ritorno vero è che **chi risponde si qualifica da solo**: due delle sei
domande chiedono com'è messo il sito e se i turni fanno male. Le risposte
tornano indietro come lead per le altre due liste.

### 2d · Il messaggio: uno per riga, mai un modello

Vale per tutte e tre. Ogni testo dice chi è Patrick, **cosa ha visto di quel
profilo**, il fatto verificato, cosa propone e **una domanda sola**. Tu o Lei
secondo il tono del profilo, e non si mescolano nello stesso testo.

```bash
python3 02-Sales/strumenti/voce-check.py --csv 02-Sales/liste/<lista>.csv
```

Toglie i tell da macchina: em dash, «quindi», elenchi di tre, «soluzione»,
frasi-cuscinetto, le tracce del nostro processo finite in un testo cliente.
Quello che resta lo rilegge una persona → [[voce-denkicode]].

---

## 3 · I due controlli, e il secondo deve uscire con 0

```bash
python3 02-Sales/strumenti/verifica-sito.py   02-Sales/liste/<lista>.csv   # solo la lista siti
python3 02-Sales/strumenti/controlla-lista.py 02-Sales/liste/<lista>.csv
```

Il primo verifica il sito riga per riga su due motori e scrive la prova in
colonna. Il secondo rifiuta la lista se una riga è verificata a occhio, se una
frase di verifica si ripete, se un handle è già in `contattati.csv` o su un
banco, se un dominio indovinato risponde e nessuno ha scritto perché non è
loro, se i motori hanno risposto 429 o 403.

La prova che il controllo cerca in colonna cambia col prodotto:
`[verifica-sito]` per i siti, `[verifica-turni]` per DenkiShift (la prova è la
squadra: camere, sale, orari, il post che cerca personale), `[verifica-azienda]`
per la ricerca (la prova è che è strutturata: mezzi, magazzino, dipendenti
visibili, più sedi).

⚠️ **Non si pubblica una lista che non è uscita con 0**, nemmeno se Patrick la
chiede di corsa. L'8 settembre 2026 ha scritto a gente col sito perché questo
passo non c'era.

---

## 4 · Pubblicare: si appende, non si sostituisce

Le liste vivono in `02-Sales/liste/<data>-instagram-<prodotto>-<zone>.csv` e
finiscono sul banco dentro `02-Sales/strumenti/lista-corrente.csv` (account di
Patrick) o `lista-denkicode.csv` (account DenkiCode).

**Si appendono.** Un CSV sostituito porta via le date degli invii, e con esse i
recuperi, che sono metà del valore del canale. Ogni riga porta:

- `Lista` = il nome del file della lista, che comincia con la data;
- `Prodotto` = `siti`, `denkishift` o `ricerca`, ed è la colonna su cui il
  banco divide le pagine;
- `Messaggio` = il testo di quella riga;
- `Scheda` = quello che si è letto del profilo, che Patrick legge prima di
  aprire la chat.

Le colonne devono restare quelle di `lista-corrente.csv`, nello stesso ordine.
Dopo l'append:

```bash
python3 02-Sales/strumenti/allinea-contattati.py    # chi è già stato scritto non torna da mandare
python3 02-Sales/strumenti/stato-banco.py
```

---

## 5 · Aprire il banco

```bash
if curl -s -o /dev/null --max-time 2 "http://localhost:8770/strumenti/banco-dm.html"; then
  open "http://localhost:8770/strumenti/banco-dm.html"
else
  open "$V/02-Sales/strumenti/Banco DM.command"
fi
```

Il `.command` apre una finestra di Terminale che deve **restare aperta**: è il
server che scrive gli invii nel vault. Il selettore in testata sceglie
l'account, le cinque linguette sono Siti, DenkiShift, Ricerca, Da ricontattare,
Già contattati.

**Le cose che a Patrick servono e che si dicono solo se le chiede**: `↩ Annulla
l'ultimo` in testata (o ⌘Z) rimette in cima l'ultimo profilo segnato, per
quando la chat si chiude prima di premere invio; `/` cerca; i tasti da 1 a 5
cambiano pagina.

---

## 6 · Prima di rispondere, si scrive

1. **La nota della lista** in `02-Sales/liste/<data>-<nome>.md`: quante righe
   da quanti profili aperti, cosa è stato scartato e perché, la resa per
   settore, le trappole nuove. È il file che dice se il segmento vale un altro
   giro → [[metodo-instagram]].
2. **[[registro-interventi]]**: una riga con chi, quando, progetto, repository
   e **quale database** (qui nessuno).
3. `python3 01-Coding/strumenti/genera-indice.py`, poi `git add`, `commit`,
   `push`. Una modifica non pushata è una modifica persa.

---

## 7 · Come si risponde, e poi si tace

Massimo sei righe:

```
Patrick — <data>. Banco DM aperto: <da mandare per account, recuperi>
Liste di oggi: siti <n> · DenkiShift <n> · ricerca <n>. <una riga su cosa c'è dentro>
<una riga solo se qualcosa non è passato: quale riga, perché è rimasta fuori>
```

Niente elenco dei file letti, niente riepilogo del procedimento, niente
proposte su cosa fare dopo.
