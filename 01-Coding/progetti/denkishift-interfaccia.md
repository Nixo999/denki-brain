---
type: risorsa
updated: 2026-08-29
source: claude
progetto: denkishift
tags: [interfaccia, ux, demo, denkishift]
---

# DenkiShift — riprogettazione dell'interfaccia

> [!note] Analisi di Claude — 2026-08-29
> Tutto questo file è materiale derivato. È costruito leggendo il codice vero in
> `smoothduty` e i documenti del vault, con i riferimenti riga per riga, e poi
> passato sotto tre revisioni che hanno tolto quello che non stava in piedi.
> Non è farina del sacco di Nicola o Patrick, e **niente qui è stato visto a
> schermo**: il vincolo era sola lettura. Prima di trattare per acquisita una
> qualunque misura di ingombro, si apre `denkishift.it` a 375px e a 1280×800.

Obiettivo dichiarato: un'interfaccia che **si venda da sola durante la demo di
Patrick**, calibrata su due utenti che non sono due gradini dello stesso ruolo.
Il datore di lavoro deve pensare «ho la mia azienda sotto controllo»; il
dipendente non deve imparare niente.

## Le precondizioni — vengono prima di qualunque riga

1. **La migrazione `19` non è mai stata eseguita** (`docs/08-aperto.md`). Finché
   non gira, il `select` su `company_settings` fallisce intero perché chiede
   `regime_chiamata`: le Impostazioni mostrano i valori di default come se
   fossero quelli dell'azienda e al primo «Salva» danno errore, e il menu mostra
   tutte le pagine accese qualunque cosa l'azienda abbia scelto. Ogni parola di
   questo file poggia lì sotto. Vedi [[modifiche-al-database]].
2. **Il login dice «Turni», non DenkiShift.** È la prima schermata della demo e
   l'unica che il titolare vede prima dei dati; in videochiamata anche la scheda
   del browser dice «Turni». Mezz'ora di lavoro, e viene prima delle venti ore
   della schermata nuova.
3. **I dati di prova non reggono una demo.** Lo script `scripts/dati-di-prova.mjs`
   crea «Pizzeria Prova» con sei persone — il nome dell'azienda è quello che
   l'app stampa in alto a sinistra per tutta la demo, e sei persone stanno sotto
   la soglia con cui Giulia squalifica un cliente al telefono. Inoltre nasce con
   **tutte e due le settimane non pubblicate**, e nessun rifiuto, nessuna
   risposta, nessuna richiesta di ferie: cioè tutte le cose che la schermata
   nuova serve a mostrare valgono zero e spariscono.
4. **Si guarda su `denkishift.it`.** Tre decisioni di questo file poggiano su
   misure dedotte dalle classi e non viste: le cinque etichette nella barra a
   375px — e sono i nomi lunghi di oggi, non quelli corti che erano stati
   proposti — i cinque elementi sopra la piega a 1280×800, e la barra in basso
   che non collide con la barra fissa della Disponibilità.

## Il glossario

**I nomi delle pagine non si toccano.** Decisione del 29 agosto 2026, vedi
[[2026-08-29-architettura-interfaccia-denkishift]]: Supervisione, Permessi,
Prospetto e Disponibilità restano quelli, in tutte e due le viste. Le rinomine
proposte — «Chi c'è», «Assenze», «Ore», «Quando posso» — sono state scartate e
non si ripropongono.

| Indirizzo | Capo | Dipendente |
|---|---|---|
| `/oggi` *(nuova)* | **Oggi** | non esiste |
| `/turni` | **Turni** | **I miei turni** |
| `/supervisione` | **Supervisione** | **Supervisione** |
| `/permessi` | **Permessi** | **Permessi** |
| `/prospetto` | **Prospetto** | non ce l'ha |
| `/disponibilita` | non ce l'ha | **Disponibilità** |

⚠️ Resta aperto, ed è l'unico punto in cui la scelta costa qualcosa: sotto il
regime «segnala quando non puoi» la voce **Disponibilità** nomina l'opposto del
gesto che quella pagina fa. Il titolo dentro la pagina è già corretto e cambia
col regime — è solo l'etichetta di menu a restare fissa. Chi lo vede è il
dipendente a chiamata, non il titolare in demo.

Il resto del vocabolario vale, e riguarda le parole **dentro** le schermate, non
i nomi delle pagine. Non arrivano più a schermo: *preapprovato* → «vale subito» ·
*monte ore* → «ore a settimana» · *causale* → «motivo» · *bozza* → «la vedi solo
tu» · *con riserva* → «in attesa» · *da assegnare* / *turno scoperto* → una
parola sola, **scoperto** · *Posta* e *Messaggi* → **da decidere** (serve una
risposta) e **da leggere** (non c'è niente da decidere) · *RLS*, *migrazione*,
*Supabase* → mai, in nessun messaggio.

Il verbo **Pubblica** significa una cosa sola — farlo vedere ai dipendenti — e
vale sia per la settimana sia per le modifiche a una settimana già pubblicata
(oggi lo stesso gesto si chiama «Pubblica modifiche» in una schermata e
«Conferma modifiche» nell'altra). **Conferma** sparisce come verbo di sistema:
diventa «Approva», «Pubblica», «Sono rientrato», «Sì, elimina».

## Il capo — cinque voci e una risposta

**Il principio**: si entra su una risposta, non su una griglia. Il tabellone
resta sempre a un tocco.

`Oggi · Turni · Supervisione · Permessi · Prospetto` — e basta. **Squadra,
Impostazioni e Aziende escono dalla barra** e vanno nella tendina dell'iniziale
in alto a destra: si aprono una volta a settimana o una volta al mese e
occupano tre dei sette posti che oggi mandano la barra in sofferenza. «Aziende» in particolare
oggi sta nella barra e un tocco accidentale cambia guscio, titolo e menu senza
preavviso — e capita all'unico account con cui si fa la demo.

Un solo pallino in tutta la barra, su «Oggi»: le cose che aspettano una
decisione. Due contatori sullo stesso dato insegnano a non fidarsi di nessuno
dei due.

### `/oggi` — la schermata nuova, elemento per elemento

Colonna unica, fondo unico, niente riquadri dentro riquadri. **Cinque elementi**,
e ognuno è una frase che Patrick dice in demo.

1. **La riga di stato**, una riga sottile con un punto colorato: «Settimana
   24–30 agosto · pubblicata martedì. La prossima la vedi solo tu.» È il buco
   operativo più caro del prodotto e si chiude con una query: oggi nessuna
   schermata dice se la settimana **prossima** è pubblicata.
2. **Il numero grande.** Ore che verranno lavorate davvero contro ore da
   contratto, sulla settimana — dove il conto è esatto. ⚠️ Due correzioni
   obbligatorie: `attesi` **non** si riduce per le assenze mentre il blocco
   «sotto contratto» accanto le riduce (due definizioni di «ore dovute» sulla
   stessa schermata), e va deciso cosa si mostra quando nessuno ha ore da
   contratto scritte — cioè lo stato di ogni cliente nuovo.
3. **Cosa manca**: ore scoperte e chi sta sotto le sue ore, coi nomi. Il motore
   c'è già e oggi si accende **solo** premendo Pubblica: il numero che evita
   l'errore in busta paga si vede una volta sola e mai più.
4. **Da decidere**, e il blocco sparisce del tutto quando è a zero: rifiuti,
   risposte alla settimana, richieste di ferie, ciascuna con una frase in
   italiano e una freccia.
5. **Oggi**: chi è in turno, chi è assente e con che motivo, e i buchi di
   copertura della giornata. Se non ce ne sono dice «giornata coperta», ed è
   l'unico punto in cui l'app dice una cosa positiva.

Un bottone pieno solo, in fondo: «Apri il tabellone». Ogni altro numero è già un
link verso il posto dove si rimedia.

## Il dipendente — una domanda sola

**Il principio**: «quando lavoro?» ha risposta a schermo **prima di qualunque
tocco**. Tutto ciò che l'app gli chiede sta in un riquadro solo, subito sotto.

In cima, il blocco più grande della schermata, sempre nello stesso punto:
«DOMANI, giovedì 3 · 09:00 – 17:00 · Sala». Se non c'è niente in programma lo
dice, e se il motivo è che la settimana non è pubblicata lo scrive: «Il
responsabile non ha ancora pubblicato. Quando lo fa, compare qui: non devi fare
niente.»

Sotto, le cose a cui rispondere. Sotto ancora, l'elenco dei prossimi giorni a
scorrimento — **non** la settimana con le frecce: il dipendente non pensa
«settimana», pensa «i prossimi giorni», e oggi quelle due frecce occupano lo
spazio migliore della schermata per servire il caso più raro. In basso una barra
con **le etichette sempre scritte**: sotto i 640px oggi restano fino a sette
icone mute, senza tooltip, in un'app il cui utente di massa sta su telefono.

### Le due bugie che si tolgono per prime — due ore e mezza

- Il totale ore in cima **conta anche i turni rifiutati**: sulla stessa
  schermata convivono «Hai rifiutato questo turno» e un totale che quel turno lo
  somma.
- Quando la settimana non è pubblicata l'app disegna **sette schede «Riposo»** e
  «0h in settimana». Non è riposo: è che non si sa ancora.

La terza era la voce di menu che dice «Disponibilità» anche sotto il regime in
cui il gesto serve a dire quando **non** puoi. Costava mezz'ora ed è stata
lasciata dov'è con la decisione sui nomi: resta un difetto noto, non un lavoro.

## Le impostazioni — sette gruppi, per gesto

Le quattro sezioni di oggi sono le quattro pagine dell'app. Nessuno cerca
«l'impostazione della pagina Permessi»: si cerca «cosa succede quando uno mi
chiede le ferie». I gruppi diventano sette e sono gesti: *quando pubblichi la
settimana · quando cambi un turno già pubblicato · quando aggiungi un turno ·
quando dai un turno a chi lavora a chiamata · quando qualcuno chiede ferie ·
quando vuoi sapere chi c'è adesso · quando fai i conti a fine mese*.

Ogni interruttore dice su due righe separate **quando scatta** e **cosa succede
se la persona dice di no**. Le venti causali e le due levette che un negozio non
tocca mai finiscono dietro «Impostazioni avanzate», con una riga di riepilogo
che dice lo stato reale — senza quella riga il richiudibile è una trappola.

In cima alla pagina, prima di tutto: *«In quest'app il turno vale appena lo
scrivi. Le impostazioni qui sotto non cambiano questo: decidono solo chi ti può
dire di no, e su cosa. Se non risponde nessuno, vuol dire che va bene.»*

⚠️ **Un testo non si può scrivere finché il codice non è deciso**: le
impostazioni proposte dicono «se dice no il turno resta scoperto», ma oggi il
turno rifiutato **viene cancellato**, e un turno cancellato non compare fra gli
scoperti. O il testo dice la verità, o si cambia il codice. Da chiudere con
Nicola prima di pubblicare la stringa.

## La lingua — le regole che valgono ovunque

- **L'app dà del tu**, in tutte e due le viste. Il «Lei» è il registro di
  Giulia al telefono e dell'apertura di Patrick: dentro il prodotto suona come
  il portale dell'INPS. Vedi [[stile-comunicazione]].
- **L'app non dice mai «io» né «noi»**: parla di sé in terza persona o nomina
  chi ha fatto la cosa.
- **Nessun messaggio d'errore si ferma sul guasto.** Due frasi fisse: cosa è
  successo (e cosa **non** è successo ai dati), cosa fai adesso. Oggi quaranta
  punti passano al toast il messaggio grezzo di Postgres, e uno schermo che
  dice «new row violates row-level security policy» davanti a un negoziante
  smette di essere un prodotto e diventa un cantiere.
- **Non si rimanda a un'assistenza che non esiste**: si nomina Patrick, o il
  numero sul biglietto. Un ufficio che non c'è è una promessa che si scopre al
  primo errore vero — e il canale, quando ci sarà, è WhatsApp
  ([[stile-comunicazione]]), non una casella.
- **Uno stato vuoto ha sempre quattro pezzi**: icona, cosa manca, cosa ci
  finirà dentro, e il bottone che ce lo mette.
- **Il toast di successo dice l'effetto sull'altra persona**, non l'operazione
  riuscita: «Settimana pubblicata. Da adesso i tuoi la vedono sul telefono.»
  ⚠️ Mai «i tuoi sono stati avvisati»: non esistono notifiche fuori dall'app.
- Mai punti esclamativi, mai emoji, mai «soluzione», «innovativo»,
  «piattaforma». Il confine del pacchiano è questo: personalità vuol dire
  scegliere le parole di chi lavora lì dentro, non aggiungere aggettivi.

## Il design system — «ferro battuto»

**Il colore è una risorsa scarsa e ha un significato solo.** Rosso: c'è un buco
e lo chiudi tu. Ambra: costa, o qualcuno non ha ancora risposto. Verde: da te
non serve niente. Indigo: azione e selezione, **mai** uno stato. Una schermata
senza problemi è una schermata grigia — ed è quella la resa grafica di «ho la
mia azienda sotto controllo».

Oggi il tabellone è azzurro dappertutto perché ogni turno assegnato è colorato:
quando tutto è colorato niente lo è, e «dove sono scoperto» — la domanda che
vale il prezzo — richiede di leggere invece di guardare.

**Un difetto di accessibilità che esiste già**: nella pagina della giornata le
barre verde e rossa affiancate, spente in scala di grigi, sono lo stesso grigio.
Per un uomo su dodici quella schermata non dice niente, e il bersaglio sono
titolari di bar, ristoranti e RSA. Ogni stato viaggia su almeno due canali:
colore, geometria, e un glifo con testo per il lettore di schermo.

Tipografia: resta Inter, con `tabular-nums` e `slashed-zero` sugli orari — le
cifre incolonnate si leggono per forma, senza mettere a fuoco, che è come si
guarda un telefono in magazzino. **Pavimento a 12px**: oggi ci sono 51 punti
sotto quella soglia, il peggiore è il calendario dei permessi con bottoni da
10,5px su sette colonne.

Il file dei token è **pronto e scritto** (sostituisce `src/app/globals.css`), con
i rapporti di contrasto calcolati e nessun fallimento. Non sta nel vault perché
qui dentro non entra codice: chiedere a Claude, o rifarlo. ⚠️ Tre correzioni
prima di copiarlo: vanno tenuti gli alias `--radius-2xl` e le tre ombre già in
uso (93 punti di chiamata che altrimenti cambiano valore in silenzio), e i
quattro colori che vivono **fuori** da `globals.css` — barra di sistema del
browser, splash del PWA, fondo della finestra Android — vanno allineati o si
scollano dal fondo pagina.

## L'ordine dei lavori

Le stime sono di Claude e vanno ricontrollate da Nicola. Il totale è **circa 45
ore**, che con 25h di negozio e l'università sono sei-otto settimane di sere.
Non si fa tutto: si fa in quest'ordine e ci si ferma dove serve.

| # | Cosa | Ore | Perché lì |
|---|---|---|---|
| 0 | Migrazione `19` sul database | — | senza, le Impostazioni non si salvano |
| 1 | Nome e logo sul login | 0,5 | è la prima schermata della demo |
| 2 | Dati di prova veri: 12-14 persone, nome plausibile, settimana in corso pubblicata, un rifiuto, una risposta, due richieste di ferie | 4 | senza, la schermata nuova mostra cinque zeri |
| 3 | Guardare `denkishift.it` a 375px e 1280×800 | 1 | tre decisioni poggiano su misure mai viste |
| 4 | File dei token, barre di copertura, pastiglia di turno, 48 sostituzioni tipografiche | 6 | sono le quattro cose che si vedono in demo |
| 5 | Le due bugie del dipendente | 2,5 | è la schermata dell'utente più numeroso |
| 6 | `errori.ts` + le tre letture che ingoiano l'errore | 6 | toglie dalla demo il momento in cui l'app mostra le viscere |
| 7 | `/oggi` | 8-10 | è la schermata del «controllo» |
| 8 | Impostazioni riscritte e raggruppate per gesto | 5 | è la schermata che vende «configurabile» |
| 9 | Stati vuoti, conferme, toast | 6 | è il primo minuto del cliente |

**Se c'è una sera sola prima di una demo**: i punti 1, 4 e 5. Sei ore, e tolgono
le cose false che si vedono per prime.

## Cosa i giudici hanno tolto

Perché non torni in circolo fra un mese.

- **Il cookie «secondo ingresso della giornata»** (l'app apre il tabellone
  invece della home a chi entra due volte). Con zero clienti l'unica persona al
  mondo che apre l'app due volte in un giorno è Patrick: se ha provato la demo
  la mattina, alle tre del pomeriggio l'app gli apre il tabellone davanti al
  cliente mentre sta dicendo «guarda, si apre e ti dice come sta la settimana».
- **L'importazione Excel nello stato vuoto a zero persone.** L'importazione
  **non crea nessuno**: abbina solo a chi è già in squadra. Con zero persone
  restituisce una settimana di turni senza nessuno sopra, cioè lo stato che
  tutto il resto dipinge di rosso. Va mostrata su una squadra già popolata.
- **La demo che apre su `/oggi`.** Giulia al telefono promette che il sistema
  dice «chi è libero e chi è già sopra le sue ore»: la prima versione della home
  mostra chi sta **sotto**. O rientra anche il conto degli straordinari (2-3h),
  o la demo apre sul tabellone e `/oggi` è la seconda schermata.
- **Le rinomine delle voci di menu**, tutte. Erano il pezzo più economico della
  proposta — sono stringhe — e sono state scartate lo stesso: il nome di una
  pagina lo impara chi la usa ogni giorno, e cambiarlo è un costo per loro
  prima che un guadagno per chi la vede in demo dieci minuti. ⚠️ Cade con esse
  anche la misura che le reggeva: cinque etichette brevi stavano nella barra a
  375px, «Supervisione» e «Prospetto» sono più lunghe. Va guardato a schermo
  prima di scriverle, e se non ci stanno la soluzione è la barra in basso del
  dipendente applicata anche al capo, non l'accorciamento dei nomi.

## I buchi dichiarati

- **Niente notifiche fuori dall'app**, né mail né push. È la seconda domanda del
  titolare in demo — «e se non guarda?» — e oggi la risposta onesta è che non lo
  sa. L'SMTP proprio chiude quel buco **e** il recupero password insieme.
- **Le persone senza account** (metà di una squadra vera) non ricevono nessuna
  domanda e nessun avviso, e nel tabellone la loro riga è identica alle altre.
  Nessuno l'ha ancora progettato — ed è anche la risposta più forte
  all'obiezione sull'usabilità: «a questi tre non serve il telefono, li metti in
  turno lo stesso».
- **`/admin` è rimasta fuori.** 618 righe di interfaccia, un pannello di
  impostazioni con un secondo vocabolario, ed è il guscio in cui gira l'account
  della demo. O si dichiara fuori perimetro per iscritto, o serve un pezzo suo.
- **Le quattro schermate di accesso** (login, password dimenticata, cambio
  password, atterraggio del link) hanno un guscio loro e non sono state
  progettate: vanno nello stesso commit dei token, perché sono l'unico punto in
  cui il cliente vede il prodotto prima di avere un ruolo.
- **Il nome del prodotto è irrisolto**: lo schermo dice «Turni», il materiale
  commerciale dice DenkiShift. Non costa ore di sviluppo, costa una risposta di
  Patrick — e blocca due pezzi su quattro.

## Collegamenti

[[denkishift]] · [[2026-08-29-architettura-interfaccia-denkishift]] ·
[[obiezione-non-sapranno-usarlo]] · [[stile-comunicazione]] ·
[[modifiche-al-database]] · [[core-commerciale]] · [[vincoli-fiscali]]
