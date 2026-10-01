---
description: Apre il banco DM e, se oggi non ci sono, costruisce e pubblica le due liste del giorno — 100 siti e 60 ricerca di mercato
argument-hint: "[apri | siti | ricerca | un numero, es. «siti 30»]"
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

`/banco apri` salta sempre la costruzione. `/banco siti` e `/banco ricerca` ne
rifanno una sola. Un numero cambia le righe: `/banco siti 30`, ma **il valore
normale è 100 per i siti e 60 per la ricerca**.

> [!important] Dal 24 settembre 2026 le liste sono due, e DenkiShift non c'è più
> Patrick: *«elimina la sezione denkishift e i suoi 50 lead. aumenta la sezione
> siti a 100 lead e quella di ricerca a 60. quindi ora ogni volta che lancio il
> comando banco, fermo restando le vecchie regole, ora devi generare 100 lead
> per i siti e 60 per la ricerca.»*
>
> **100 siti e 60 ricerca, ogni volta.** Tutto il resto — ~~zone, un settore al
> giorno,~~ niente scuse, i due controlli, la posta — resta com'era. Scritta in
> [[metodo-liste]]. *Zone e settori superati il 29/09/2026, riquadro sotto.*

> [!important] Dal 29 settembre 2026 si pesca per luogo, e la bellezza è in pausa
> Patrick: *«prima sfondiamo un settore in un luogo. Una volta finiti i lead
> disponibili, sfondiamo un altro settore nello stesso luogo, poi un altro
> ancora. Una volta arrivato a 10 settori fatti in quel luogo, si cambia luogo
> e ci si allontana da casa. Piuttosto di fare come ora, che prima finiamo un
> settore in tutta Italia e cambiamo settore.»*
> E subito dopo: *«ora basta unghie ecc, cambiamo settore»*, *«non escono per
> sempre ma dopo 3 settimane sono stufo, cambiamo area, puntiamo su altro»*.
>
> **Il luogo è la provincia**, si parte da casa (Seveso, Monza e Brianza) e ci
> si allontana. Un settore si finisce, poi il prossimo nello **stesso** luogo.
> Unghie, estetica, ciglia e PMU, parrucchieri, barbieri e trucco sono **in
> pausa**: tornano quando lo dice Patrick. Come si fa sta al passo 2-bis, lo
> stato sta in `02-Sales/liste/rotazione.csv`. Le frasi sono in
> [[metodo-liste]].

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

L'ultima riga decide: se le due liste di oggi ci sono, si va al passo 5.

⚠️ **Il conto vero degli invii sta nel browser di Patrick**, non nei CSV. Se
lui dice di averne mandati trenta e lo script dice zero, ha ragione lui.

---

## 2 · Le due liste, e sono due mestieri diversi

Regola di Patrick dell'11 settembre 2026, in [[metodo-liste]]: *«gli script e i
ganci devono essere inerenti alla tipologia di servizio per cui li contattiamo
e anche le aziende devono essere ad alta conversione in base al servizio che
stiamo offrendo»*. Quindi: **due liste, due target, due testi. Non si
mescolano.** Erano tre fino al 24 settembre 2026, quando DenkiShift è uscito
dal banco (2b qui sotto).

> [!important] Il 12 settembre 2026 Patrick ha fissato quantità e perimetro
> *«io voglio 50 contatti per tipologia, non mi interessano scuse […] basta che
> siano in lombardia per denkishift e gestionali. per quanto riguarda i siti
> possono essere in tutta italia. ogni giorno facciamo settori diversi e per
> quanto riguarda i siti ogni volta che finiamo una zona ne iniziamo un'altra»*
>
> ~~**50 righe per lista, sempre.**~~ *Superato nei numeri il 24 settembre
> 2026: **100 siti e 60 ricerca**, vedi sopra.* Il resto vale ancora: il
> bacino non è una scusa, se un settore in una zona si esaurisce si cambia
> settore, e se sono finiti i settori si cambia zona. Si consegna 100 e 60.
>
> | Lista | Dove si pesca |
> |---|---|
> | Siti | **tutta Italia** |
> | ~~DenkiShift~~ | *tolta il 24 settembre 2026* |
> | Ricerca di mercato | **tutta la Lombardia** |
>
> ~~**Un settore al giorno.** La zona dei siti si esaurisce in circa quindici
> settori, cioè quindici giorni, poi si passa alla successiva:
> **Monza e Brianza → Milano → Como → Varese → Brescia → …** e così via
> scendendo fino alla Sicilia. Quale zona è aperta e quali settori sono già
> stati fatti si legge nelle note delle liste in `02-Sales/liste/`.~~
> *Superato il 29 settembre 2026.* In pratica la «zona» era diventata una
> regione intera e il settore si faceva su tutta la regione in un giorno: in
> nessuna provincia un settore è mai stato finito. Da oggi luogo per luogo,
> settore per settore, fino in fondo → passo 2-bis.
>
> ⚠️ **Il settore che rende zero si abbandona lo stesso giorno.** Il 12
> settembre i tatuatori della Brianza hanno dato 1 riga su 7: sei avevano il
> sito. Quando succede si cambia e si scrive perché, invece di consegnare meno.

Il come si costruisce una riga — trovare il profilo, leggerlo, verificare, non
riscrivere a chi è già in lista — sta in [[metodo-instagram]] e non si ripete
qui. Qui c'è **chi ci va dentro** e **cosa gli si dice**.

### 2a · Siti vetrina — 100 righe, tutta Italia, colonna `Prodotto: siti`

**Chi converte** (misurato, [[metodo-instagram]]): onicotecniche e nail center,
estetiste singole, parrucchieri piccoli, barber, toelettature, tatuatori e PMU,
fotografi e wedding. Nei comuni grossi i saloni con la vetrina il sito ce
l'hanno già: **restano le singole**, ed è lì che si pesca.
⚠️ *Dal 29 settembre 2026 la cura della persona è in pausa* (unghie,
estetica, ciglia e PMU, parrucchieri, barbieri, trucco). **Resta vero il
criterio**: attività singole o piccole, che vivono di foto, senza sito. I
settori attivi sono quelli del passo 2-bis.
**Fuori**: mobilifici e arredamento (6 su 6 col sito), negozi (la domanda
giusta è «vende online», è un altro flusso), catene, chi ha un sito vivo e
curato, i profili sotto i ~200 follower.
**Dove**: ~~la zona aperta in quel momento della rotazione, e dentro quella il
settore del giorno. La zona si chiude dopo una quindicina di settori.~~ Il
luogo e il settore aperti in `rotazione.csv`, passo 2-bis.

**Il gancio è uno solo, e dall'11 settembre 2026 non si ammorbidisce**
([[stile-comunicazione]], regola di Patrick): *«per i siti il gancio deve
essere che la bozza è già stata fatta»*. Nel messaggio si scrive **«la bozza
del suo sito è già pronta»**, non «gliela preparo», non «le mando una prima
schermata».
⚠️ Il che vuol dire che quando uno risponde la bozza deve esistere: chi manda
questi cento si compra il lavoro di farle. È il prezzo del gancio più
forte che abbiamo, e lo paga chi risponde per primo.

**La struttura, dal 13 settembre 2026 e sono quattro passi.** Patrick: *«il
nostro gancio di vendita principale per i siti è che ABBIAMO GIÀ CREATO UNA
BOZZA/ANTEPRIMA INTERATTIVA DEL SITO per il prospect, basata sui contenuti del
loro profilo social»*.

1. **Complimento vero**, su un dettaglio specifico del loro lavoro. È la riga
   che dimostra che una persona ha guardato quel profilo.
2. **Il problema**, in una riga sola.
3. **La bozza.** Le parole le ha date Patrick il 13 settembre: *«abbiamo preso
   ispirazione dal tuo profilo e abbiamo realizzato una bozza del tuo sito»*.
4. **Chiusura a frizione zero**, e anche questa è sua: *«preferisci che te la
   mandi qui su Instagram, o prima ne parliamo due minuti al telefono? In ogni
   caso zero costi e zero impegno: se ti piace, poi ne parliamo. Se vuoi vedere
   cosa facciamo: denkicode.com»*.
   ⚠️ **La scelta viene prima, la rassicurazione dopo.** «Zero costi» messo in
   apertura di paragrafo suona come una giustificazione; messo dopo la domanda
   è una rassicurazione.

⚠️ **Niente aperture istituzionali.** «Sono Patrick Sappa della software house
X, a Seveso» è il tono che fa chiudere la chat. **«Ciao, sono Patrick di
DenkiCode» va benissimo**: il problema era il paragrafo di presentazione, non
il nome. Linguaggio fluido, moderno, empatico. **Massimo cinque o sei righe**,
che si leggano dal telefono.

⚠️ **Tre errori di lingua da non rifare**, Patrick il 13 settembre: si dice
**«ho notato però una cosa»** e non «una cosa l'ho notata»; quello che manca è
**un sito**, non «un posto tuo»; e **«ho preso le tue foto» sembra da stalker**
— si scrive che le foto le hai guardate e ti è venuta voglia di provarci.

⚠️ **Il complimento non si genera da una colonna.** È l'unico pezzo che va
scritto aprendo il profilo, ed è il motivo per cui il testo di ripiego del
banco qui vale meno che per la ricerca.

Gancio `1-6` nella colonna, come oggi: 1 nessun sito, 2 dominio morto,
3 parcheggiato, 4 link rotto, 5 piattaforma (Fresha, Wix, Linktree: **il
messaggio la nomina**, o il titolare ti corregge), 6 vivo ma vecchio.

### 2b · DenkiShift — tolta il 24 settembre 2026

Non si costruisce più. Patrick: *«elimina la sezione denkishift e i suoi 50
lead»*. Quel giorno sono uscite da `lista-corrente.csv` le 246 righe DenkiShift
mai mandate (le liste restano in `02-Sales/liste/`); le 184 già partite
restano sul banco fra i già contattati, e chi aveva letto o risposto resta fra
i recuperi con il suo testo. Target, gancio e messaggio di prima stanno in
[[dm-instagram-denkishift]] e nella storia di questo file.

### 2c · Ricerca di mercato — 60 righe, tutta la Lombardia, colonna `Prodotto: ricerca`

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
prezzi, zero programmi nominati. Dal 13 settembre 2026 `www.denkicode.com` sta
anche qui, ma **nella riga di chi scrive, non come invito**: dice da dove
arriva la ricerca, e non è un prodotto da guardare. Se nomini un prodotto la ricerca diventa una
scusa per vendere e la lista muore, per tutti e tre → [[script-indagine]].
Il contraccambio si promette e **si mantiene**: il riepilogo di cosa è venuto
fuori dalle aziende della zona.
Il ritorno vero è che **chi risponde si qualifica da solo**: due delle sei
domande chiedono com'è messo il sito e se i turni fanno male. Chi risponde
male sul sito torna come lead per la lista siti; chi risponde male sui turni
si dice a Patrick, perché DenkiShift dal 24 settembre non ha più una lista.

### 2d · Il messaggio: uno per riga, mai un modello

Vale per tutte e due. Ogni testo dice chi è Patrick, **cosa ha visto di quel
profilo**, il fatto verificato, cosa propone e **una domanda sola**. Tu o Lei
secondo il tono del profilo, e non si mescolano nello stesso testo.

```bash
python3 02-Sales/strumenti/voce-check.py --csv 02-Sales/liste/<lista>.csv
```

Toglie i tell da macchina: em dash, «quindi», elenchi di tre, «soluzione»,
frasi-cuscinetto, le tracce del nostro processo finite in un testo cliente.
Quello che resta lo rilegge una persona → [[voce-denkicode]].

---

## 2-bis · Dove si pesca: luogo per luogo, settore per settore

Regola di Patrick del 29 settembre 2026, in testa a questo file. Vale per
tutte e due le liste: i siti partono da casa e vanno verso tutta Italia, la
ricerca fa lo stesso dentro la Lombardia.

**Il luogo è la provincia.** Si parte da casa e ci si allontana, in quest'ordine
(distanza in linea d'aria da Seveso, calcolata il 29/09/2026):

| Lista | Ordine dei luoghi |
|---|---|
| Siti | MB → CO → MI → LC → VA → BG → NO → LO → PV → VB → VC → PC → SO → BS → BI → CR → AL → AT → TO → PR → GE → MN → AO → VR → … |
| Ricerca | MB → CO → MI → LC → VA → BG → LO → PV → SO → BS → CR → MN |

**I settori, nell'ordine in cui si aprono in ogni luogo:**

| # | Siti (8 attivi) | Ricerca (10) |
|---|---|---|
| 1 | toelettature e dog trainer | officine e carrozzerie |
| 2 | personal trainer singoli, istruttori di pilates e yoga | impiantisti elettrici e termoidraulici |
| 3 | pasticcerie e cake designer | edilizia e serramenti |
| 4 | sartorie, atelier e tappezzieri | falegnamerie |
| 5 | tatuatori e piercing | meccanica e carpenterie |
| 6 | fotografi e videomaker | ingrossi e distribuzione |
| 7 | fioristi e wedding planner | trasporti e logistica |
| 8 | ristorazione piccola: gelaterie, pizzerie d'asporto, bar | aziende agricole con vendita |
| 9 | — | alimentari artigianali: caseifici, salumifici, pastifici, torrefazioni |
| 10 | — | studi tecnici |

- **Toelettature per prime** perché hanno già dato due lead caldi, Per Un
  Pelo e Mikuma, e in Monza e Brianza non sono mai state fatte.
- **Personal trainer** li ha scelti Patrick il 29/09 fra quattro, «uno di
  quelli con più alto tasso di conversione». Nessuno dei quattro era misurato.
  L'unico dato è dell'8/09 in Ticino: 12 fra palestre e studi su 15 avevano il
  sito. Quindi **solo i singoli**: niente palestre, niente studi con reception.
- **In pausa**: unghie, estetica, ciglia e PMU, parrucchieri, barbieri, trucco
  sposa. Non si aprono finché Patrick non lo dice.

**Quando un settore è finito in un luogo.** Quando la ricerca l'ha passato
tutto. Le parole del settore, almeno tre varianti («toelettatura», «dog
grooming», «toelettatrice»), si incrociano con i comuni della provincia sopra
i 5.000 abitanti, sull'API di Instagram e su Google `site:instagram.com`. E gli
ultimi 20 profili nuovi aperti non hanno dato una riga. Vale ancora la regola
del 12/09: un settore che rende quasi zero, meno di una riga ogni cinque
profili dopo i primi trenta, si chiude lo stesso giorno e conta come finito.

**Come si riempiono le righe del giorno.** Il settore aperto nel luogo aperto,
fino in fondo. Se finisce prima delle 100 (o delle 60), si apre il settore
successivo **nello stesso luogo**. Un giorno può toccare più settori, e un
settore può durare più giorni: non c'è più «un settore al giorno».

**Quando si cambia luogo**: a **10 settori finiti** in quel luogo, oppure
quando non ne resta nessuno attivo da aprire. Con 8 settori attivi, oggi i
siti chiudono il luogo all'ottavo. Allora si passa al luogo successivo
dell'ordine, e si riparte dal settore 1.

**Lo stato sta in `02-Sales/liste/rotazione.csv`**, una riga per lista, luogo
e settore: `Stato` (`parziale` o `esaurito`), `Righe`, `Ultima lista`, `Nota`.
È stato ricostruito il 29/09 dalle righe del banco. Tutto quello che c'era
prima è `parziale`, perché nessun settore era mai stato finito in una
provincia. Si legge prima di cominciare:

```bash
python3 -c "
import csv
for r in csv.DictReader(open('02-Sales/liste/rotazione.csv')):
    if r['Luogo'] in ('MB',): print(r['Lista'], r['Settore'], r['Stato'], r['Righe'])"
```

E si aggiorna al passo 6: righe aggiunte, `esaurito` quando lo è, e in
`Nota` il perché («ultimi 20 profili senza una riga», «18 su 25 col sito»).

⚠️ **In Monza e Brianza e a Milano chiama Giulia.** Prima di pubblicare, i nomi
delle righe di quelle due province si cercano nelle sue liste
(`02-Sales/liste/*giulia*`): un'attività non riceve sia la chiamata sia il DM
([[metodo-instagram]], regola del 31/08).

⚠️ **Nella ricerca «qui in zona» vale solo vicino a casa.** Oltre i 50 km da
Seveso si scrive la zona vera: «le falegnamerie della Valtellina». Il 29/09
era sbagliato su 19 righe su 60.

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
`[verifica-sito]` per i siti, `[verifica-azienda]` per la ricerca (la prova è
che è strutturata: mezzi, magazzino, dipendenti visibili, più sedi).
`[verifica-turni]` era di DenkiShift, e dal 24 settembre non serve più.

⚠️ **Non si pubblica una lista che non è uscita con 0**, nemmeno se Patrick la
chiede di corsa. L'8 settembre 2026 ha scritto a gente col sito perché questo
passo non c'era.

---

## 3-bis · La posta, e si legge sempre

Regola di Patrick del 12 settembre 2026: *«ora fallo da solo, d'ora in poi ogni
volta che lancio il comando /banco fallo in automatico»*. **Prima di aprire il
banco si legge la posta di Instagram**, si segnano gli esiti e si dice cosa non
funziona. **Si legge e si segna: nessun messaggio parte da qui.**

> [!warning] I DM partono dall'account DenkiCode — Patrick, 30/09/2026: *«li mando da denkicode»*
> Nel browser dell'app la sessione aperta è quella di `@patrick.sappa`: da lì
> il 29/09 i 160 DM del giorno non si vedevano, e nemmeno Design Capelli e
> Adelina. **La posta da leggere è quella dell'account DenkiCode.** Finché
> quell'account non è aperto nel browser dell'app, e ce lo apre Patrick perché
> le password nelle pagine web non si digitano da qui, il passo 3-bis vede
> solo `@patrick.sappa` e lo dice nella risposta.

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
- `Prodotto` = `siti` o `ricerca`, ed è la colonna su cui il banco divide le
  pagine. `denkishift` dal 24 settembre non si scrive più: resta solo sulle
  righe già partite;
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
python3 "$V/02-Sales/strumenti/banco-server.py" --apri
```

Accende il server se è spento, staccato dalla chat, e apre la pagina. **Nessuna
finestra di Terminale, e a Patrick non si chiede di lanciare niente**: regola
di Nicola dell'1 ottobre 2026, in [[metodo-liste]]. ~~Il `.command` apre una
finestra di Terminale che deve restare aperta~~ *superato l'1/10/2026*: il
doppio click su `Banco DM.command` funziona ancora, ma fa la stessa cosa e la
finestra si può chiudere. Se il comando dice che il server non parte, si legge
il log che nomina e si ripara da qui, senza passare il problema a Patrick.

Il selettore in testata sceglie l'account, le quattro linguette sono Siti,
Ricerca, Da ricontattare, Già contattati. La linguetta DenkiShift è stata
tolta il 24 settembre 2026.

**Le cose che a Patrick servono e che si dicono solo se le chiede**: `↩ Annulla
l'ultimo` in testata (o ⌘Z) rimette in cima l'ultimo profilo segnato, per
quando la chat si chiude prima di premere invio; `/` cerca; i tasti da 1 a 4
cambiano pagina.

---

## 6 · Prima di rispondere, si scrive

1. **La nota della lista** in `02-Sales/liste/<data>-<nome>.md`: quante righe
   da quanti profili aperti, cosa è stato scartato e perché, la resa per
   settore, le trappole nuove. È il file che dice se il segmento vale un altro
   giro → [[metodo-instagram]].
   Per ogni settore toccato: luogo, profili letti, righe, finito sì o no.
2. **`02-Sales/liste/rotazione.csv`**: le righe aggiunte per luogo e settore,
   `esaurito` sui settori finiti, e il perché in `Nota`. Se il luogo è
   arrivato a dieci settori finiti, o non ne ha più di attivi, lo si dice
   nella nota: la prossima lista parte dal luogo successivo.
3. **[[registro-interventi]]**: una riga con chi, quando, progetto, repository
   e **quale database** (qui nessuno).
4. `python3 01-Coding/strumenti/genera-indice.py`, poi `git add`, `commit`,
   `push`. Una modifica non pushata è una modifica persa.

---

## 7 · Come si risponde, e poi si tace

Massimo sei righe:

```
Patrick — <data>. <se ci sono lead fermi: quanti e da quanto, per primi>
Banco DM aperto: <da mandare per account, recuperi>
Liste di oggi: siti <n> · ricerca <n>. <luogo e settori: quali finiti, quale resta aperto>
<una riga solo se qualcosa non è passato: quale riga, perché è rimasta fuori>
```

Niente elenco dei file letti, niente riepilogo del procedimento, niente
proposte su cosa fare dopo.
