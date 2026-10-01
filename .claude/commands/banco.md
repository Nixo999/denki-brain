---
description: Apre il banco DM e, se oggi non ci sono, costruisce e pubblica le due liste del giorno — 100 siti e 60 ricerca di mercato
argument-hint: "[apri | siti | ricerca | un numero, es. «siti 30»]"
---

# /banco — il banco DM, con le liste del giorno già dentro

Registro Trevis, già in `~/.claude/CLAUDE.md`: niente presentazioni, niente
«adesso procedo a», niente proposte su cosa fare dopo.

## 0 · La regola che viene prima di tutte

Lo lancia **Patrick**, e **Patrick scrive solo nella chat**. Non gli si chiede
mai di lanciare un comando, incollare codice in una console, aprire il
Terminale o rifare un passo a mano. Nicola, 1/10/2026, in [[metodo-liste]]:
*«patrick non deve mandare messaggi in terminale»*.

**Un blocco non ferma la lista e non si riferisce a metà.** Classificatore
della sessione, 429, captcha, anti-bot: si cambia fonte nell'ordine del passo
4 e si va avanti. Cosa non è passato si dice in **una riga**, nella risposta
finale. Il 25/09 le righe erano zero alle 00:04 e 163 all'01:43, dopo
*«sono stanco di dirtelo, crea i lead»*: è successo il 14, il 17, il 19 e il
25 settembre, e non succede più.

**100 siti e 60 ricerca, ogni volta** (Patrick, 24/09). Le righe vecchie
ancora ferme sul banco non sono un motivo per consegnarne meno.

| Se | Allora |
|---|---|
| le liste di **oggi** esistono già in `02-Sales/liste/` | si apre il banco (passo 8) e si risponde. Costa un minuto |
| non ci sono, o l'argomento dice quale rifare | passi 2-9, poi si risponde |

`/banco apri` salta sempre la costruzione. `/banco siti` e `/banco ricerca` ne
rifanno una sola. Un numero cambia le righe (`/banco siti 30`); senza numero
sono 100 e 60.

## 1 · Aggancio

```bash
V="${DENKI_VAULT:-}"
for p in "$V" "$PWD" "$HOME/lavoro/denki-brain" "$HOME/Desktop/denki-brain"; do
  [ -n "$p" ] && [ -f "$p/CLAUDE.md" ] && V="$p" && break
done
cd "$V" && git pull --rebase --autostash -q 2>&1 | tail -2
python3 "$V/01-Coding/strumenti/installa-macchina.py"   # comandi aggiornati in ~/.claude, valgono dalla sessione dopo
python3 "$V/02-Sales/strumenti/stato-banco.py"
ls -1 "$V/02-Sales/liste"/$(date +%F)-*.csv 2>/dev/null || echo "nessuna lista di oggi"
```

L'ultima riga decide la velocità. ⚠️ **Il conto vero degli invii sta nel
browser di Patrick**, non nei CSV: se lui dice trenta e lo script zero, ha
ragione lui.

## 2 · Il piano del giorno

```bash
python3 "$V/02-Sales/strumenti/prossimo-giro.py"
```

Stampa, per lista, le celle del giorno (4 per i siti, 3 per la ricerca) nella
forma **luogo · settore · quota righe**, 3 celle di riserva, i settori «al
telefono, non in DM», quelli in pausa, e quante righe mai mandate giacciono
sul banco. Legge `02-Sales/liste/settori.csv`, **l'unico elenco dei settori**
(stato `attivo`/`pausa`/`evitare`, canale `dm`/`telefono`), e
`02-Sales/liste/rotazione.csv`.

**La sessione non sceglie settore e luogo: esegue il piano.** Ogni cella si
riempie fino alla sua quota. Una cella che rende **meno di 1 riga su 5
profili dopo i primi 30** si chiude (`esaurito` in `rotazione.csv`, passo 9)
e la sua quota passa alla prima riserva. Una cella esaurita torna da sola dopo
30 giorni. I settori «al telefono» e quelli in pausa non entrano in DM. Se lo
script esce con errore si legge l'errore e lo si ripara da qui: niente scelta
a occhio.

La regola di Patrick del 29/09 («un settore fino in fondo, a 10 settori si
cambia luogo») è superata in parte l'1/10/2026 da `prossimo-giro.py`, Nicola:
*«voglio che ci sia sempre un ricircolo di settori e luoghi»*. Ne restano: si
parte da casa e ci si allontana; la bellezza è in pausa finché Patrick non la
riapre.

## 3 · Chi ci va dentro e cosa gli si dice

Patrick, 11/09: *«gli script e i ganci devono essere inerenti alla tipologia di
servizio per cui li contattiamo e anche le aziende devono essere ad alta
conversione in base al servizio che stiamo offrendo»*. Due liste, due target,
due testi. **Non si mescolano.**

### Siti vetrina — `Prodotto: siti`

**Il criterio**: attività singole o piccole, che vivono di foto, senza sito.
Nei comuni grossi chi ha la vetrina il sito ce l'ha già: restano le singole.
**Fuori**: mobilifici e arredamento (6 su 6 col sito), negozi (la domanda è
«vende online», è un altro flusso), catene, chi ha un sito vivo e curato, i
profili sotto i ~200 follower, palestre e studi con reception (8/09 in Ticino:
12 su 15 col sito; dei personal trainer solo i singoli).

**Il gancio è uno solo e non si ammorbidisce**, Patrick 11/09
([[stile-comunicazione]]): *«per i siti il gancio deve essere che la bozza è
già stata fatta»*. Si scrive **«la bozza del suo sito è già pronta»**, non
«gliela preparo». ⚠️ Quando uno risponde la bozza deve esistere: è il prezzo
del gancio più forte che abbiamo.

**Quattro passi**, Patrick 13/09: *«il nostro gancio di vendita principale per
i siti è che ABBIAMO GIÀ CREATO UNA BOZZA/ANTEPRIMA INTERATTIVA DEL SITO per il
prospect, basata sui contenuti del loro profilo social»*.

1. **Complimento vero**, su un dettaglio specifico del loro lavoro. Si scrive
   aprendo il profilo: non si genera da una colonna.
2. **Il problema**, in una riga.
3. **La bozza**: *«abbiamo preso ispirazione dal tuo profilo e abbiamo
   realizzato una bozza del tuo sito»*.
4. **Chiusura a frizione zero**: *«preferisci che te la mandi qui su
   Instagram, o prima ne parliamo due minuti al telefono? In ogni caso zero
   costi e zero impegno: se ti piace, poi ne parliamo. Se vuoi vedere cosa
   facciamo: denkicode.com»*. La scelta prima, la rassicurazione dopo.

Niente aperture istituzionali: «Ciao, sono Patrick di DenkiCode» va bene, il
paragrafo di presentazione no. **Cinque o sei righe**, da leggere sul telefono.
**Tre errori di lingua** (Patrick, 13/09): si dice **«ho notato però una
cosa»**; manca **un sito**, non «un posto tuo»; **«ho preso le tue foto» sembra
da stalker**, si scrive che le hai guardate e ti è venuta voglia di provarci.

Gancio `1-6` in colonna: 1 nessun sito, 2 dominio morto, 3 parcheggiato,
4 link rotto, 5 piattaforma (Fresha, Wix, Linktree: **il messaggio la nomina**,
o il titolare ti corregge), 6 vivo ma vecchio.

### Ricerca di mercato — `Prodotto: ricerca`

**Il criterio**: aziende **strutturate**, con processi da raccontare, e **vive**
su Instagram: post degli ultimi mesi, mezzi, magazzino, gente al lavoro.
**Fuori**: chi improvvisa, i negozi piccoli, i liberi professionisti singoli.

Gancio `R`. Il modulo è quello di [[script-indagine]], e il link che gira è
questo:

```
https://docs.google.com/forms/d/e/1FAIpQLSe2cCfeAx8IVLRq-ocJe4MUpq43u_1D95IpBPjqOYX-90a9JA/viewform
```

⚠️ `/viewform`, mai `/edit`: quello è il pannello di chi scrive il modulo.

**Qui non si vende niente**: zero prodotti, zero prezzi, zero programmi
nominati. `www.denkicode.com` sta nella riga di chi scrive, non come invito.
Il contraccambio si promette e si mantiene: il riepilogo di cosa è venuto fuori
dalle aziende della zona. Chi risponde male sul sito torna come lead siti; chi
risponde male sui turni si dice a Patrick. **«Qui in zona» solo entro 50 km da
Seveso**: oltre si scrive la zona vera, «le falegnamerie della Valtellina» (il
29/09 era sbagliato su 19 righe su 60).

### Per tutte e due

- **In Monza e Brianza e a Milano chiama Giulia.** Prima di pubblicare, i nomi
  di quelle due province si cercano in `02-Sales/liste/*giulia*`: nessuno
  riceve sia la chiamata sia il DM.
- **Un messaggio per riga, mai un modello**: chi è Patrick, cosa ha visto di
  quel profilo, il fatto verificato, cosa propone, **una domanda sola**. Tu o
  Lei secondo il tono del profilo, mai mescolati.
- Ogni lista passa da
  `python3 02-Sales/strumenti/voce-check.py --csv 02-Sales/liste/<lista>.csv`
  ([[voce-denkicode]]).

## 4 · Trovare i profili

Il dettaglio di ogni riga (leggere il profilo, gli otto esiti, le trappole) sta
in [[metodo-instagram]]. Qui c'è l'ordine delle fonti, ed è la strada normale,
non un ripiego. Si legge soltanto: nessun follow, like o messaggio.

**(1) Fonti che non eseguono JavaScript e non dipendono da un'API privata.**
- **Pagine Gialle**: elenco per categoria e città, poi la scheda per sito e
  indirizzo, poi Instagram dal sito o cercato per nome. Allarga fuori regione:
  si filtra sulla regione della scheda. Il 25/09 ha dato la ricerca di mercato,
  circa un'azienda buona ogni otto schede.
- **I motori, aperti nel browser dell'app**, navigando alla pagina dei
  risultati e leggendone il testo: `site:instagram.com "<parola del settore>"
  "<comune>"`. **Un motore alla volta, piano**, e al primo captcha o 429 si
  passa al successivo senza riprovare. Il 30/09 Google è andato in captcha
  dopo poche decine di ricerche; hanno retto DuckDuckGo html, Yahoo e
  Startpage; Mojeek, Ecosia e Brave in captcha subito. Il 25/09 DuckDuckGo e
  Brave sono morti per una richiesta ogni 2,5 secondi.
- **Il profilo** si apre navigando a `instagram.com/<handle>` e leggendo il
  testo intero della pagina: follower, bio, link, indirizzo. Il solo `meta`
  perde il link in bio. «Pagina non trovata» vuol dire account morto.

⚠️ **La (1) dal Mac di Patrick non è ancora stata misurata**: resa e tempi
`TODO`, si scrivono nella nota lista del primo giro che la usa.

**(2) L'API interna di Instagram** (topsearch, `users/{pk}/info`, gli hashtag
dei comuni), con gli snippet di [[metodo-instagram]], **solo se passa senza
chiedere niente a nessuno**. Al primo rifiuto del classificatore o al primo 429
si torna alla (1): non si riprova e non si chiedono permessi a Patrick. Il
30/09 topsearch è morta dopo 150-600 query della giornata.

Con più operatori: una scheda a testa, chiusa a fine lavoro (il browser ne
tiene 9); lotti da 20, ogni riga subito su disco; file di lavoro nominati per
luogo, perché la scratchpad è condivisa.

## 5 · I due controlli

```bash
python3 02-Sales/strumenti/verifica-sito.py   02-Sales/liste/<lista>.csv   # solo la lista siti
python3 02-Sales/strumenti/controlla-lista.py 02-Sales/liste/<lista>.csv   # deve uscire 0
```

Prima dello script, ogni riga ha la sua ricerca nella forma
`cercato «"nome" comune» → <domini visti>`. Lo script appende la prova
`[verifica-sito]` (siti); per la ricerca la prova è `[verifica-azienda]`:
mezzi, magazzino, dipendenti visibili, più sedi. Con i motori fermi si lancia
`verifica-sito.py --senza-motori`. Dopo: le righe `SITO` si rileggono, le
`PROBABILE SITO` si aprono tutte.

`controlla-lista.py` rifiuta verifiche a occhio, frasi ripetute, handle già
contattati o già su un banco, domini indovinati vivi senza il perché, 429 e
403. Le righe che ferma si tolgono e si sostituiscono **dalla stessa cella**
del piano. **Una lista che non esce 0 non si pubblica**, e `pubblica-lista.py`
non lo permette.

## 6 · La posta

Regola di Patrick del 12/09, in [[metodo-liste]]: a ogni `/banco` si legge la
posta di Instagram e si segnano gli esiti. **Si legge e si segna: nessun
messaggio parte da qui.** I DM partono dall'account DenkiCode (Patrick, 30/09:
*«li mando da denkicode»*), quindi si legge quello, se è aperto nel browser
dell'app. **Se non è aperto o la lettura è bloccata, si salta**: una riga nella
risposta finale, e a Patrick non si chiede di incollare o rifare niente.

Da una scheda su `instagram.com/direct/inbox/`:

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

Il `viewer_id` è l'account aperto: un `item` con `user_id` diverso è una loro
risposta. Le autorisposte («grazie per averci contattato», «per
prenotazioni») non sono risposte. Si scrive:

1. **`Esito DM`** sulle righe ancora sul banco, con la data.
2. **`02-Sales/liste/risposte-dm.csv`**: handle, data, chi ha l'ultima parola,
   giorni fermo, tipo, cosa ha detto.
3. **I lead aperti**, da quanti giorni aspettano, col rilancio già scritto e
   passato da `voce-check.py`. Chi ha l'ultima parola loro è fermo da noi.
4. **Cosa non ha funzionato**, coi numeri: quanti «ho già il sito» (difetto di
   lista, non un no), autorisposte per segmento, critiche al testo parola per
   parola. Il primo resoconto: [[2026-09-12-posta-dm-primo-resoconto]].

⚠️ **I lead caldi vengono prima delle liste nuove.** Un lead fermo da più di
due giorni si dice all'inizio della risposta, prima di qualunque altra cosa.

## 7 · Pubblicare: si appende, non si sostituisce

La lista è `02-Sales/liste/<data>-instagram-<siti|ricerca>-<luoghi>.csv`. Ogni
riga porta `Lista` (il nome del file, che comincia con la data), `Prodotto`
(`siti` o `ricerca`: il banco divide le pagine su questa), `Messaggio` (il
testo di quella riga) e `Scheda` (cosa si è letto del profilo).

```bash
python3 02-Sales/strumenti/pubblica-lista.py 02-Sales/liste/<lista>.csv --prova   # dice cosa entrerebbe
python3 02-Sales/strumenti/pubblica-lista.py 02-Sales/liste/<lista>.csv
```

Lancia `controlla-lista.py` e si ferma se non esce 0, appende in coda senza
riscrivere le righe esistenti, poi `allinea-contattati.py` e `stato-banco.py`.
Un banco sostituito porta via le date degli invii, e con esse i recuperi.
**`lista-corrente.csv` (2,1 MB) non si apre mai.** Senza `--banco` le righe
vanno lì, dove sono andate tutte le liste fino al 30/09; `--banco denkicode`
scrive in `lista-denkicode.csv`.

## 8 · Aprire il banco

```bash
python3 "$V/02-Sales/strumenti/banco-server.py" --apri
```

Accende il server se è spento, staccato dalla chat, e apre la pagina. Nessuna
finestra di Terminale. Se dice che il server non parte, si legge il log che
nomina e si ripara da qui. Il selettore in testata sceglie l'account; le
linguette sono Siti, Ricerca, Da ricontattare, Già contattati. Solo se Patrick
lo chiede: `↩ Annulla l'ultimo` (o ⌘Z) rimette in cima l'ultimo profilo
segnato, `/` cerca, i tasti da 1 a 4 cambiano pagina.

## 9 · Prima di rispondere, si scrive

1. **La nota della lista**, `02-Sales/liste/<data>-<nome>.md`: per ogni cella
   luogo, settore, profili letti, righe, chiusa sì o no; cosa è stato scartato
   e perché; le fonti usate e quali si sono bloccate; resa e tempi della fonte
   (1) finché non sono misurati; le trappole nuove.
2. **`02-Sales/liste/rotazione.csv`**: per ogni cella le righe aggiunte e
   `Ultima lista`; su una cella chiusa `Stato` = `esaurito` e in `Nota`
   **«N profili, M righe»** seguito dal perché («34 profili, 5 righe: 22 col
   sito»). Quel formato lo legge `prossimo-giro.py`.
3. **[[registro-interventi]]**: chi, quando, progetto, repository e **quale
   database** (qui nessuno).
4. `python3 01-Coding/strumenti/genera-indice.py`, poi `git add`, `commit`,
   `push`.

## 10 · Come si risponde, e poi si tace

```
Patrick — <data>. <se ci sono lead fermi: quanti e da quanto, per primi>
Banco DM aperto: <da mandare per account, recuperi>
Liste di oggi: siti <n> · ricerca <n>. <celle: luogo · settore · righe, quali chiuse>
<una riga solo se qualcosa non è passato: fonte bloccata, posta non letta, righe rimaste fuori>
<una riga solo se sul banco giacciono più di 300 righe mai mandate: quante>
```

Niente elenco dei file letti, niente riepilogo del procedimento, niente
proposte su cosa fare dopo.

---

La storia delle regole sta in [[metodo-liste]] e nella versione precedente di
questo file: `git show 2098832:.claude/commands/banco.md`.
