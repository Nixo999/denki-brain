---
description: Apre il banco DM e, se oggi non ci sono, costruisce e pubblica le tre liste del giorno — 50 siti, 50 DenkiShift, 50 ricerca di mercato
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
`/banco ricerca` ne rifanno una sola. Un numero cambia le righe: `/banco siti 30`,
ma **il valore normale è 50 per ognuna**.

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

> [!important] Il 12 settembre 2026 Patrick ha fissato quantità e perimetro
> *«io voglio 50 contatti per tipologia, non mi interessano scuse […] basta che
> siano in lombardia per denkishift e gestionali. per quanto riguarda i siti
> possono essere in tutta italia. ogni giorno facciamo settori diversi e per
> quanto riguarda i siti ogni volta che finiamo una zona ne iniziamo un'altra»*
>
> **50 righe per lista, sempre.** Il bacino non è una scusa: se un settore in
> una zona si esaurisce si cambia settore, e se sono finiti i settori si cambia
> zona. Si consegna 50, 50 e 50.
>
> | Lista | Dove si pesca |
> |---|---|
> | Siti | **tutta Italia** |
> | DenkiShift | **tutta la Lombardia** |
> | Ricerca di mercato | **tutta la Lombardia** |
>
> **Un settore al giorno.** La zona dei siti si esaurisce in circa quindici
> settori, cioè quindici giorni, poi si passa alla successiva:
> **Monza e Brianza → Milano → Como → Varese → Brescia → …** e così via
> scendendo fino alla Sicilia. Quale zona è aperta e quali settori sono già
> stati fatti si legge nelle note delle liste in `02-Sales/liste/`.
>
> ⚠️ **Il settore che rende zero si abbandona lo stesso giorno.** Il 12
> settembre i tatuatori della Brianza hanno dato 1 riga su 7: sei avevano il
> sito. Quando succede si cambia e si scrive perché, invece di consegnare meno.

Il come si costruisce una riga — trovare il profilo, leggerlo, verificare, non
riscrivere a chi è già in lista — sta in [[metodo-instagram]] e non si ripete
qui. Qui c'è **chi ci va dentro** e **cosa gli si dice**.

### 2a · Siti vetrina — 50 righe, tutta Italia, colonna `Prodotto: siti`

**Chi converte** (misurato, [[metodo-instagram]]): onicotecniche e nail center,
estetiste singole, parrucchieri piccoli, barber, toelettature, tatuatori e PMU,
fotografi e wedding. Nei comuni grossi i saloni con la vetrina il sito ce
l'hanno già: **restano le singole**, ed è lì che si pesca.
**Fuori**: mobilifici e arredamento (6 su 6 col sito), negozi (la domanda
giusta è «vende online», è un altro flusso), catene, chi ha un sito vivo e
curato, i profili sotto i ~200 follower.
**Dove**: la zona aperta in quel momento della rotazione, e dentro quella il
settore del giorno. La zona si chiude dopo una quindicina di settori.

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

### 2b · DenkiShift — 50 righe, tutta la Lombardia, colonna `Prodotto: denkishift`

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

### 2c · Ricerca di mercato — 50 righe, tutta la Lombardia, colonna `Prodotto: ricerca`

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

## 3-bis · La posta, e si legge sempre

Regola di Patrick del 12 settembre 2026: *«ora fallo da solo, d'ora in poi ogni
volta che lancio il comando /banco fallo in automatico»*. **Prima di aprire il
banco si legge la posta di Instagram**, si segnano gli esiti e si dice cosa non
funziona. **Si legge e si segna: nessun messaggio parte da qui.**

Dal browser con la sessione di Patrick, su `instagram.com/direct/inbox/`:

```js
// tutta la posta, a pagine di venti
const H={'x-ig-app-id':'936619743392459','x-requested-with':'XMLHttpRequest'};
let cursor=null, tutte=[];
for(let g=0; g<25; g++){
  let u='https://www.instagram.com/api/v1/direct_v2/inbox/?visual_message_return_type=unseen&thread_message_limit=20&persistentBadging=true&limit=20';
  if(cursor) u+='&cursor='+encodeURIComponent(cursor);
  const r=await fetch(u,{headers:H,credentials:'include'}); const j=await r.json();
  (j.inbox.threads||[]).forEach(t=>tutte.push(t));
  cursor=j.inbox.oldest_cursor; if(!cursor||!j.inbox.has_older) break;
}
```

Il `viewer_id` è Patrick: un `item` con `user_id` diverso è una loro risposta.
Poi si separano **le autorisposte** («grazie per averci contattato», «per
prenotazioni», «ti risponderemo»), che non sono risposte, dalle risposte vere.

Quello che va scritto, ogni volta:

1. **`Esito DM`** sulle righe che stanno ancora sul banco, con la data.
2. **`02-Sales/liste/risposte-dm.csv`**: handle, data, chi ha l'ultima parola,
   giorni fermo, tipo, cosa ha detto.
3. **I lead aperti**, con da quanti giorni aspettano e il rilancio già scritto,
   passato da `voce-check.py`. Chi ha l'ultima parola loro è fermo da noi.
4. **Cosa non ha funzionato**, con i numeri: quanti hanno risposto «ho già il
   sito» (è un difetto di lista, non un no), quante autorisposte per segmento,
   e ogni critica al testo va riportata parola per parola.

Il primo resoconto, con il metodo e i numeri di partenza, sta in
[[2026-09-12-posta-dm-primo-resoconto]]: **5,8% di risposte vere, 28% dei
rifiuti perché il sito ce l'avevano, e sette trattative ferme.**

⚠️ **I lead caldi vengono prima delle liste nuove.** Una lista nuova costa ore
e rende fra giorni; un «l'ha guardata?» a chi ha già la bozza in mano costa due
minuti. Se c'è un lead fermo da più di due giorni, si dice all'inizio della
risposta, prima di qualunque altra cosa.

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
Patrick — <data>. <se ci sono lead fermi: quanti e da quanto, per primi>
Banco DM aperto: <da mandare per account, recuperi>
Liste di oggi: siti <n> · DenkiShift <n> · ricerca <n>. <una riga su cosa c'è dentro>
<una riga solo se qualcosa non è passato: quale riga, perché è rimasta fuori>
```

Niente elenco dei file letti, niente riepilogo del procedimento, niente
proposte su cosa fare dopo.
