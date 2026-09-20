---
riga: Il registro dei testi che legge un cliente - Lei o Tu, voce di Patrick. Non e' il registro di Trevis.
type: risorsa
updated: 2026-09-20
source: denkicode
---

# Stile di comunicazione

Come parliamo, a chi, con che parole. Vale per Giulia al telefono, per Patrick
in trattativa, e per ogni testo che Claude genera.

## Tono di voce DenkiCode

**Diretto, giovane, problem-solving. Nessuna fuffa.**

Significa: si dice cosa fa una cosa e quanto costa, non "soluzioni innovative
per il tuo business". Se non sappiamo una cosa, si dice.

> [!warning] Regola operativa dal 6 settembre 2026
> **Ogni testo che Claude scrive per un cliente passa dalla skill
> `voce-denkicode` prima di essere mostrato**, sempre — WhatsApp, DM
> Instagram, email, copy dei siti. Nata dopo che un lead ha sgamato un DM di
> Patrick come scritto da un LLM (em dash, poi trovati elenchi di tre e
> connettivi da tema). Non è facoltativa e non si chiede ogni volta: è
> l'ultimo passo prima di consegnare, come il lessico fiscale qui sotto.
> Dettaglio in [[2026-09-06-skill-voce-denkicode]].

## Il "Lei" e il "Tu" — non è cortesia, è posizione

| Chi | Fase | Come |
|---|---|---|
| **Giulia** | Primo contatto a freddo | Sempre **"Lei"** (o "Voi" aziendale). Tono istituzionale, non invadente |
| **Patrick** | Trattativa e chiusura | Apre col **"Lei"**, poi chiede subito: *"Per comodità operativa, possiamo darci del tu?"* |

Il passaggio al "tu" chiesto da Patrick lo posiziona come **partner e
consulente alla pari**, non come venditore. È una mossa deliberata: non
saltarla e non anticiparla al telefono.

## Canali, per fase

| Fase | Canale |
|---|---|
| **Prospezione** | Chiamate a freddo (Giulia, Gabriele, Edoardo) **sul vicino**, DM Instagram (Patrick) **sul lontano**, email. Il porta-a-porta a freddo è chiuso dal 31 agosto 2026 → [[2026-08-31-stop-porta-a-porta-a-freddo]] |
| **Trattativa e chiusura** | Telefonata, video-call, incontro dal vivo |
| **Operatività e assistenza** | **WhatsApp** — canale principale con le PMI locali |
| **Comunicazioni formali** | Email |

WhatsApp non è un ripiego: con le PMI locali è il canale che tiene il rapporto
diretto. L'email serve quando serve una traccia.

## Chi parla al cliente

**Patrick è l'unico volto e l'unica voce commerciale.**

Nicola interviene **solo** se il cliente chiede dettagli molto tecnici,
introdotto da Patrick come **"Lead Developer"**.

> Conseguenza operativa per Claude: ogni testo destinato a un cliente si scrive
> **con la voce di Patrick**. Se il testo è tecnico e firmato Nicola, va detto
> esplicitamente.

## Lessico obbligatorio

Vincolo fiscale attivo, dettaglio in [[vincoli-fiscali]]:

| ✅ | ❌ |
|---|---|
| ricevuta | fattura, fattura elettronica |
| collaborazione occasionale / promozionale | fornitura, contratto continuativo |
| quota annuale | canone mensile addebitato |

## Come si formalizza un accordo

- **Siti vetrina**: messaggio riepilogativo su WhatsApp o email + ricevuta
  all'acconto. Nessun documento complesso — la leggerezza è parte dell'offerta
  "cassa rapida"
- **Gestionali**: PDF impaginato, tipo *"Piano di Sviluppo"*. **Template ancora
  da creare** → [[flusso-vendita]]

## Come documentiamo

| Cosa | Dove |
|---|---|
| Stato tecnico di un progetto | `docs/` dentro il repo — vedi [[convenzioni]] |
| Stato commerciale, clienti, soldi | Questo vault |
| Liste e stati di chiamata | Google Sheets su Drive |
| Handoff di fine giornata | `06-Daily/`, con `/chiudi-sessione` |

## Una regola imparata sui progetti

> [!note] Analisi di Claude — 2026-08-28
> Da [[opero]]: quando il cliente chiede una funzione che non era nello scope,
> **va detto che è un'aggiunta nel momento in cui la chiede** — non dopo averla
> fatta. Il repo lo prescrive già ("ogni aggiunta va detta al committente come
> aggiunta, perché sposta piano e data"), ed è successo il contrario abbastanza
> volte da meritarsi una riga qui. Non è una discussione: è una frase.
>
> *"Questa nella versione attuale non c'è, quindi è lavoro nuovo: te la quoto e
> ti dico quanto sposta la consegna."*


## Regole date a voce

Scritte da `regola.py` nel momento in cui sono state dette.

### 20/09/2026 — Patrick: «io devo far finta di lavorare per la stra up non essere il capo»

al telefono si presenta come uno del team commerciale, non come co-founder: abbassa la posta per chi ascolta e gli lascia la leva del «lo chiedo al mio responsabile tecnico» per chiudere data e prezzo in un secondo tempo

### 20/09/2026 — Patrick: «devo veendere non fare la ricerca, capire si che problemi hanno ma l'obbiettivo deve essere quello di vendere»

lo script indagine chiudeva sul modulo Google e vietava di nominare il prodotto: su questa lista l'obiettivo e' l'appuntamento conoscitivo con un'azienda che paga, le domande sui problemi servono a costruire la vendita non a fare statistica

### 19/09/2026 — Patrick: «il tono deve essere professionale ma deve capire che sono un ragazzo che vuole partire ma che le cose le sa fare»

detto il 19/09 sulla mail a Edilida, il primo lead uscito dalla ricerca di mercato. Vale su ogni testo che Patrick firma: l'eta' non si dichiara e non si scusa, si dimostra con la precisione di quello che si chiede e si porta

### 16/09/2026 — Patrick: «non so che problemi tu abbia, ma c'e' sempre qualcosa che non va un umano non si porrebbe mai cosi, non hanno senso, cerca di parlare normalmente»

secondo giro bocciato sulle stesse storie: le frasi erano costruite per antitesi («non X, ma Y») e chiudevano con la morale, cioe' aforismi. Chi parla davvero dice una situazione concreta e si ferma li': in fila alla cassa, la luce della finestra, un pomeriggio di lavoro. Niente frase che riassume il senso di quella prima

### 16/09/2026 — Patrick: «mi piace molto, ma le scritte non sono umane e discorsive, mantieni il significato ma aggiusta le frasi e i titoli»

le otto storie del 16 settembre erano scritte per sentenze: titolo assertivo e corpo telegrafico, corretti ma da manuale. Un testo che sta su un'immagine si legge come parlato, con il soggetto esplicito e le frasi che si tengono, non come una riga di documentazione

### 14/09/2026 — Patrick: «non hanno proprio senso le frasi, non aggiungono niente di valore, sono solo senza senso, piuttosto togliele tanto metto la descrizione»

sull'immagine di un post ci va il nome e la prova, non una riga di prosa: il testo e' il mestiere della didascalia, e una frase in piu' sull'immagine e' solo una frase da correggere

### 14/09/2026 — Patrick: «le frasi sotto il nome dell'attività non hanno senso modificale rendile sensate, in italiano e sintatticamente corrette»

in un'immagine o in un titolo la riga di testo e' l'unica prosa che c'e': i frammenti nominali incollati con la virgola, senza verbo, si leggono come sciatteria

### 13/09/2026 — Patrick: «per la bozza: «abbiamo preso ispirazione dal tuo profilo e abbiamo realizzato una bozza sito». Per la chiusura: «preferisci se te la mando qua su ig oppure prima vuoi che ne parliamo 2 minuti al telefono?, in ogni caso zero costi e zero impegno, se ti piace poi ne si parla, Se vuoi vedere cosa facciamo: denkicode.com»»

la scelta fra messaggio e telefono va offerta prima, non dopo, e il «zero costi» arriva dopo la domanda come rassicurazione: messo prima suona come una giustificazione

### 13/09/2026 — Patrick: «si dice «ho notato pero' una cosa» in italiano; la frase «perche' un posto tuo non c'e'» non ha senso, al massimo un sito tuo; non mi piace la frase «ho preso le tue foto», sembra da stalker; puoi dire che sono di denkicode senza problemi»

tre errori di lingua e uno di tono nei messaggi dei siti: l'ordine delle parole italiano, «posto» usato dove ci va «sito», e un verbo che fa sembrare che gli abbiamo rubato le foto invece di averle guardate

### 13/09/2026 — Patrick: «il nostro gancio di vendita principale per i siti e' che ABBIAMO GIA' CREATO UNA BOZZA/ANTEPRIMA INTERATTIVA DEL SITO per il prospect, basata sui contenuti del loro profilo social. Struttura: 1 apertura con complimento vero su un dettaglio specifico del loro lavoro, 2 il problema identificato in una riga, 3 il gancio della bozza come iniziativa spontanea senza vincolo economico, 4 call to action a frizione zero. Niente toni istituzionali o freddi. Linguaggio fluido, moderno, empatico e professionale. Specifica che guardare la bozza NON costa nulla e NON c'e' obbligo d'acquisto. Massimo 5-6 righe, leggibili da smartphone»

l'apertura «sono Patrick Sappa della software house» e' il tono che fa chiudere la chat: il messaggio deve dimostrare in prima riga che una persona vera ha guardato quel profilo

### 13/09/2026 — Patrick: «per tutti e tre linka il nostro sito www.denkicode.com»

senza un posto dove controllare chi siamo il messaggio resta la parola di uno sconosciuto su Instagram

### 13/09/2026 — Patrick: «per i siti il messaggio da troppe info inutili»

il testo dei siti era di cinque paragrafi e spiegava anche il costo prima che qualcuno avesse chiesto: la bozza pronta e' il gancio, il resto si dice quando rispondono

### 13/09/2026 — Patrick: «per denkishift dire che i primi due mesi sono gratuiti»

il DM dei turni non aveva nessuna leva sul prezzo e chiedeva dieci minuti a freddo: due mesi gratis abbassano il rischio percepito senza promettere una data di attivazione

### 12/09/2026 — Patrick: «migliora un minimo ancora le frasi, non sempre sono di senso compiuto e dai un impostazione ancora piu umana anche se sei già a buon punto»

alcune frasi dei rilanci del 12 settembre stanno in piedi grammaticalmente ma non dicono una cosa sensata: voce-check.py toglie i tell da macchina, non controlla che la frase abbia senso

### 11/09/2026 — Patrick: «per i siti il gancio deve essere che la bozza è già stata fatta»

il DM dei siti torna alla promessa piena: non «le preparo una schermata», ma la bozza esiste gia' e gliela mando

## Collegamenti

[[flusso-vendita]] · [[vincoli-fiscali]] · [[ruoli-e-responsabilita]] ·
[[prodotti-e-listino]] · [[convenzioni]]
