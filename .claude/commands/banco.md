---
description: Apre il banco DM e, se oggi non ci sono, costruisce e pubblica le due liste del giorno — 100 siti e 60 ricerca di mercato
argument-hint: "[apri | siti | ricerca | un numero, es. «siti 30»]"
---

# /banco — il banco DM, con le liste del giorno già dentro

## 0 · La regola che viene prima di tutte

Lo lancia **Patrick**, e **Patrick scrive solo nella chat**: non gli si chiede
mai di lanciare un comando, incollare codice in una console, aprire il
Terminale, rifare un passo a mano. Nicola, 1/10/2026: *«patrick non deve
mandare messaggi in terminale»*.

**Un blocco non ferma la lista e non si riferisce a metà.** Classificatore,
429, captcha: si cambia fonte nell'ordine del passo 4 e si va avanti. Cosa non
è passato si dice in **una riga**, nella risposta finale. Il 25/09: zero righe
alle 00:04, 163 all'01:43 dopo *«sono stanco di dirtelo, crea i lead»*.

**100 siti e 60 ricerca, ogni volta** (Patrick, 24/09), anche con righe vecchie
ferme sul banco. Se le liste di **oggi** esistono già: passo 8 e si risponde.
Se no: passi 2-9. `/banco apri` salta la costruzione, `/banco siti` e `/banco
ricerca` ne rifanno una sola, un numero cambia le righe (`/banco siti 30`).

## 1 · Aggancio

```bash
V="${DENKI_VAULT:-}"
for p in "$V" "$PWD" "$HOME/lavoro/denki-brain" "$HOME/Desktop/denki-brain"; do
  [ -n "$p" ] && [ -f "$p/CLAUDE.md" ] && V="$p" && break
done
cd "$V" && git pull --rebase --autostash -q 2>&1 | tail -2
python3 "$V/01-Coding/strumenti/installa-macchina.py"   # comandi aggiornati in ~/.claude: valgono dalla sessione dopo
python3 "$V/02-Sales/strumenti/stato-banco.py"
ls -1 "$V/02-Sales/liste"/$(date +%F)-*.csv 2>/dev/null || echo "nessuna lista di oggi"
```

```bash
python3 "$V/02-Sales/strumenti/sondaggi.py"   # il sondaggio di oggi lo pubblica Patrick a mano: se c'e', va in testa alla risposta
```

Il conto vero degli invii sta nel browser di Patrick: se non torna, ha ragione lui.

## 2 · Il piano del giorno

```bash
python3 "$V/02-Sales/strumenti/prossimo-giro.py"
```

Stampa le celle del giorno (4 siti, 3 ricerca) come **luogo · settore · quota
righe**, 3 riserve, i settori «al telefono, non in DM» e quelli in pausa, le
righe mai mandate sul banco. Legge `02-Sales/liste/settori.csv`, **l'unico
elenco dei settori**, e `rotazione.csv`.

**La sessione non sceglie settore e luogo: esegue il piano.** Ogni cella si
riempie fino alla quota. Sotto **1 riga su 5 profili dopo i primi 30** si
chiude (`esaurito`, passo 9) e la quota passa alla prima riserva; torna da sola
dopo 30 giorni. Se lo script si rompe, si ripara da qui: niente scelta a occhio.

La regola di Patrick del 29/09 («un settore fino in fondo, a 10 settori si
cambia luogo») è superata in parte l'1/10/2026, Nicola: *«voglio che ci sia
sempre un ricircolo di settori e luoghi»*. Ne restano: si parte da casa e ci si
allontana; la bellezza è in pausa finché Patrick non la riapre.

## 3 · Chi ci va dentro e cosa gli si dice

Due liste, due target, due testi: **non si mescolano** (Patrick, 11/09).
**Siti, `Prodotto: siti`.** Attività singole o piccole, che vivono di foto,
senza sito. **Fuori**: mobilifici e arredamento (6 su 6 col sito), negozi (la
domanda è «vende online», altro flusso), catene, chi ha un sito vivo e curato,
i profili sotto i ~200 follower, palestre e studi con reception.

Il gancio non si ammorbidisce, Patrick 11/09: *«per i siti il gancio deve
essere che la bozza è già stata fatta»*. Si scrive **«la bozza del suo sito è
già pronta»**, non «gliela preparo», e quando uno risponde la bozza deve
esistere. Patrick 13/09: *«il nostro gancio di vendita principale per i siti è
che ABBIAMO GIÀ CREATO UNA BOZZA/ANTEPRIMA INTERATTIVA DEL SITO per il
prospect, basata sui contenuti del loro profilo social»*. Quattro passi:

1. **Complimento vero** su un dettaglio del loro lavoro, scritto aprendo il
   profilo: non si genera da una colonna.
2. **Il problema**, in una riga.
3. **La bozza**: *«abbiamo preso ispirazione dal tuo profilo e abbiamo
   realizzato una bozza del tuo sito»*.
4. **Chiusura**: *«preferisci che te la mandi qui su Instagram, o prima ne
   parliamo due minuti al telefono? In ogni caso zero costi e zero impegno: se
   ti piace, poi ne parliamo. Se vuoi vedere cosa facciamo: denkicode.com»*.
   La scelta prima, la rassicurazione dopo.

«Ciao, sono Patrick di DenkiCode» va bene, il paragrafo di presentazione no.
Cinque o sei righe. **Tre errori di lingua** (Patrick, 13/09): si dice **«ho
notato però una cosa»**; manca **un sito**, non «un posto tuo»; **«ho preso le
tue foto» sembra da stalker**: le hai guardate e ti è venuta voglia di provarci.
Gancio `1-6`: 1 nessun sito, 2 dominio morto, 3 parcheggiato, 4 link rotto,
5 piattaforma (Fresha, Wix, Linktree: **il messaggio la nomina**), 6 vecchio.

**Ricerca, `Prodotto: ricerca`.** Aziende **strutturate**, con processi da
raccontare, **vive** su Instagram: post recenti, mezzi, magazzino, gente al
lavoro. **Fuori**: chi improvvisa, i negozi piccoli, i professionisti singoli.
Gancio `R`, il modulo di [[script-indagine]]; gira **solo `/viewform`**, mai
`/edit`, che è il pannello di chi lo scrive:
`https://docs.google.com/forms/d/e/1FAIpQLSe2cCfeAx8IVLRq-ocJe4MUpq43u_1D95IpBPjqOYX-90a9JA/viewform`
**Qui non si vende niente**: zero prodotti, prezzi, programmi. `www.denkicode.com`
sta nella riga di chi scrive, non come invito. Il contraccambio (il riepilogo
della zona) si promette e si mantiene. Chi risponde male sul sito torna lead
siti, sui turni si dice a Patrick. **«Qui in zona» solo entro 50 km da
Seveso**: oltre, la zona vera («le falegnamerie della Valtellina»).

**Per tutte e due.** In Monza e Brianza e a Milano **chiama Giulia**: i nomi di
quelle province si incrociano con `02-Sales/liste/*giulia*` prima di
pubblicare. **Un messaggio per riga, mai un modello**: cosa ha visto di quel
profilo, il fatto verificato, cosa propone, una domanda sola; Tu o Lei, mai
mescolati. Ogni lista passa da `voce-check.py --csv` ([[voce-denkicode]]).

## 4 · Trovare i profili

Il dettaglio di una riga sta in [[metodo-instagram]]; qui l'ordine delle fonti,
ed è la strada normale. Si legge soltanto: nessun follow, like o messaggio.
Patrick, 10/10/2026: *«stop chiedere autorizzazioni fai da solo non chiedermi
piu niente»*. Ogni dominio nuovo aperto nel browser dell'app gli chiede il
permesso: **nel browser solo instagram.com**, il resto con curl. Una fonte che
chiede permesso o viene negata si abbandona e non si riprova.

**(1) Fonti senza JavaScript e senza API privata.** ⚠️ **Dal Mac di Patrick
non sono ancora state misurate**: resa e tempi `TODO`, da scrivere nella nota
lista del primo giro che le usa.
- **Pagine Gialle**: categoria e città, scheda per sito e indirizzo, poi
  Instagram dal sito o per nome. Allarga fuori regione: si filtra sulla scheda.
- **Motori aperti nel browser dell'app**, navigando ai risultati e leggendo il
  testo della pagina: `site:instagram.com "<parola del settore>" "<comune>"`.
  Un motore alla volta, piano; al primo captcha o 429 si passa al successivo.
  Il 30/09 hanno retto DuckDuckGo html, Yahoo, Startpage; Google in captcha
  dopo poche decine; Mojeek, Ecosia, Brave subito.
- **Il profilo**: si naviga a `instagram.com/<handle>` e si legge il testo
  intero (follower, bio, link, indirizzo). «Pagina non trovata» = morto.

**(2) L'API interna di Instagram** (topsearch, `users/{pk}/info`, hashtag dei
comuni) con gli snippet di [[metodo-instagram]], **solo se passa senza chiedere
niente a nessuno**. Al primo rifiuto o 429 si torna alla (1), senza riprovare e
senza chiedere permessi a Patrick.

## 5 · I due controlli

```bash
python3 02-Sales/strumenti/verifica-sito.py   02-Sales/liste/<lista>.csv   # solo siti; --senza-motori se i motori sono fermi
python3 02-Sales/strumenti/controlla-lista.py 02-Sales/liste/<lista>.csv   # deve uscire 0
```

Ogni riga porta la sua ricerca (`cercato «"nome" comune» → <domini visti>`) e
la prova: `[verifica-sito]` per i siti (`SITO` si rilegge, `PROBABILE SITO` si
apre), `[verifica-azienda]` per la ricerca (mezzi, magazzino, dipendenti, più
sedi). Le righe fermate si sostituiscono dalla stessa cella.

## 6 · La posta

Patrick, 12/09: a ogni `/banco` si legge la posta e si segnano gli esiti;
**nessun messaggio parte da qui**. I DM partono da DenkiCode (30/09: *«li mando
da denkicode»*): si legge quell'account, se è aperto nel browser dell'app, da
`instagram.com/direct/inbox/`. **Se non è aperto o la lettura è bloccata, si
salta**: una riga nella risposta, a Patrick non si chiede niente.

```js
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

Un `item` con `user_id` diverso dal `viewer_id` è una loro risposta; le
autorisposte («grazie per averci contattato») no. Si scrive: **`Esito DM`**
con la data sulle righe del banco; **`risposte-dm.csv`** (handle, data, chi ha
l'ultima parola, giorni fermo, tipo, cosa ha detto); **i lead aperti**, da
quanti giorni, col rilancio passato da `voce-check.py`; **cosa non ha
funzionato**, coi numeri: quanti «ho già il sito» (difetto di lista),
autorisposte per segmento, critiche al testo parola per parola. ⚠️ **I lead
caldi vengono prima delle liste nuove**: uno fermo da più di due giorni si dice
in testa alla risposta.

## 7 · Pubblicare: si appende, non si sostituisce

```bash
python3 02-Sales/strumenti/pubblica-lista.py 02-Sales/liste/<data>-instagram-<siti|ricerca>-<luoghi>.csv   # --prova: dice cosa entrerebbe
```

Colonne `Lista` (il nome del file), `Prodotto` (`siti`/`ricerca`: divide le
pagine del banco), `Messaggio`, `Scheda` (cosa si è letto del profilo). Lancia
`controlla-lista.py` e si ferma se non esce 0, appende in coda (un banco
riscritto perde date degli invii e recuperi), poi `allinea-contattati.py` e
`stato-banco.py`. **`lista-corrente.csv` non si apre mai**: senza `--banco` le
righe vanno lì, come tutte le liste fino al 30/09.

## 8 · Aprire il banco

```bash
python3 "$V/02-Sales/strumenti/banco-server.py" --apri
```

Accende il server staccato dalla chat e apre la pagina, senza Terminale. Se il
server non parte, si legge il log che nomina e si ripara da qui.

## 9 · Prima di rispondere, si scrive

1. **La nota**, `02-Sales/liste/<data>-<nome>.md`: per cella profili letti,
   righe, chiusa o no; scarti e perché; fonti bloccate; resa e tempi della (1).
2. **`rotazione.csv`**: per cella righe aggiunte e `Ultima lista`; su una cella
   chiusa `Stato` = `esaurito` e in `Nota` **«N profili, M righe»** più il
   perché («34 profili, 5 righe: 22 col sito»). Lo legge `prossimo-giro.py`.
3. **[[registro-interventi]]** (database: nessuno), poi
   `python3 01-Coding/strumenti/genera-indice.py`, `add`, `commit`, `push`.

## 10 · Come si risponde, e poi si tace

```
Patrick — <data>. <se ci sono lead fermi: quanti e da quanto, per primi>
Banco DM aperto: <da mandare per account, recuperi>
Liste di oggi: siti <n> · ricerca <n>. <celle: luogo · settore · righe, quali chiuse>
<una riga solo se qualcosa non è passato: fonte bloccata, posta non letta, righe fuori>
<una riga solo se sul banco giacciono più di 300 righe mai mandate: quante>
```

Niente file letti, niente riepilogo del procedimento, niente proposte.

La storia delle regole sta in [[metodo-liste]] e in `git show 4116676:.claude/commands/banco.md`.
