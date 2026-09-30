---
type: risorsa
riga: Testi integrali: specifica Intermediar + Receive di Seba (24/09) e riassetto CO-OPERO portato da Patrick (30/09). La sintesi sta altrove.
updated: 2026-09-30
source: denkicode
progetto: opero
tags: [opero, intermediar, receive, specifica, sebastian-torres]
---

# OperO — Intermediar + Receive · testo di Seba

Specifica funzionale e logica di prodotto, scritta da [[sebastian-torres]] e
girata a Nicola il 24/09/2026. **Parole sue, non riassunte**: la formattazione
è stata portata in markdown, il testo no. Sintesi e buchi →
[[opero-intermediar-receive]].

## 1. Obiettivo del progetto

Intermediar e Receive devono ampliare OperO dalla gestione interna di una singola azienda alla collaborazione operativa tra aziende.

Il concetto fondamentale è:

- OperO organizza le persone della propria azienda.
- Intermediar organizza le aziende che lavorano con/per la propria azienda.
- Receive permette a un'azienda esterna di ricevere e gestire in modo semplice le richieste provenienti da Intermediar.

Intermediar non deve essere sviluppato come un'applicazione separata da OperO.

È una funzione interna all'ecosistema OperO e deve sembrare OperO osservato da un'altra prospettiva.

Receive, almeno nella prima fase, non deve essere necessariamente un'app separata. Deve poter essere utilizzato entrando nell'app OperO con un account/workspace Receive e mostrando un'interfaccia adattata e fortemente limitata.

## 2. Caso d'uso principale

La prima versione deve essere progettata principalmente sul caso reale di Paolo / BluNotte.

Esempio: BluNotte necessita di 40 facchini. Paolo coordina diverse aziende e decide di distribuire il personale:

- 8 operatori → Bolanos;
- altri operatori → propria azienda;
- altri → La Scelta Giusta;
- ecc.

Oggi questo processo può avvenire attraverso WhatsApp, telefonate, messaggi e comunicazioni frammentate.

Intermediar deve trasformarlo in un flusso strutturato:

BluNotte → richiesta → azienda fornitrice → conferma → squadra/referente → esecuzione → chiusura → contabilità/storico.

## 3. Identità personale e workspace

Un utente deve avere un solo account personale, ma può operare all'interno di più contesti/workspace.

Esempio Paolo:

```
Paolo
→ propria azienda
→ BluNotte · Logistica
→ Music Info · Logistica
→ eventuali altri contesti.
```

Il cambio workspace deve essere estremamente semplice, idealmente con una logica simile al cambio account di Instagram.

È il workspace selezionato a determinare per conto di quale azienda/organizzazione l'utente sta operando.

Non bisogna chiederglielo nuovamente durante ogni operazione.

## 4. Accesso a Intermediar

La Home principale di OperO non deve essere ridisegnata.

Intermediar deve essere accessibile tramite un controllo separato posizionato alla destra della navigation bar inferiore esistente.

Non deve diventare una quinta voce incorporata nella barra attuale.

Una volta entrati in Intermediar, la navigazione principale sarà:

**Lavori | Richieste | Gestione | Conti**

e deve essere presente separatamente il controllo che permette di tornare alla parte normale di OperO.

## 5. Principio tecnico fondamentale

Una richiesta non deve generare copie indipendenti dello stesso lavoro.

Deve esistere un'unica entità logica condivisa, sulla quale OperO, Intermediar e Receive mostrano viste differenti in base:

- all'azienda;
- al ruolo dell'utente;
- ai permessi;
- allo stato del lavoro.

Esempio: BluNotte crea #1287. Bolanos non deve ricevere una copia scollegata #456. Receive non deve generare un'altra copia.

Deve esistere una relazione persistente che permetta di sapere che tutti stanno lavorando sulla stessa richiesta/interazione B2B.

## 6. Intermediar — Gestione

La sezione Gestione serve a costruire la rete privata di aziende con cui il workspace collabora.

Non è un marketplace pubblico. Non deve mostrare aziende casuali.

L'utente deve poter: cercare un'azienda già presente nell'ecosistema oppure creare rapidamente una nuova azienda esterna.

**Home Gestione.** Priorità: Ricerca aziende. Sotto possono essere presenti:

- aziende recenti;
- loghi delle aziende utilizzate frequentemente;
- + Aggiungi nuova azienda;
- La tua rete · X aziende ›.

Non vogliamo una classica tabella da gestionale. Le aziende devono essere riconoscibili soprattutto attraverso: logo + nome azienda.

**Tipologie di azienda.** Un'azienda può essere:

- **A. Azienda con OperO completo.** È già presente nell'ecosistema. Non necessita di badge "OperO". È lo stato normale.
- **B. Azienda con Receive.** Mostrare eventualmente soltanto una piccola icona Receive. Non un badge enorme.
- **C. Azienda esterna.** Non utilizza né OperO né Receive. Deve comunque poter essere utilizzata immediatamente da Intermediar. Questo è fondamentale. Non bisogna obbligare un'azienda esterna a installare o acquistare Receive per poter lavorare con lei.

## 7. Creazione di un'azienda esterna

La creazione deve essere estremamente veloce.

NON vogliamo un modulo tradizionale con: ragione sociale, P.IVA, indirizzo, PEC, SDI, amministratore, ecc.

Nella prima fase chiediamo soltanto: **Nome azienda**, **Numero di telefono**.

Esempio: Facchini Rossi, +39 ...

Premendo Crea azienda, il sistema deve creare immediatamente una piccola entità/workspace isolata. Esempio ID interno: `FR-8K4P2`. L'ID reale deve naturalmente essere gestito dal backend e non deve dipendere necessariamente dal nome.

Successivamente: **Azienda creata**, con possibilità:

- Condividi con WhatsApp
- Invita su Receive
- Copia invito/link

L'invito è facoltativo. L'azienda deve essere utilizzabile da Paolo anche se nessuno accetta mai l'invito.

## 8. Evitare duplicati

Se successivamente l'azienda esterna attiva Receive, non deve essere creata una nuova azienda.

Se successivamente passa a OperO completo, ancora una volta non deve essere creata una nuova azienda.

La progressione deve essere: **Workspace esterno → Receive → OperO completo**, mantenendo la stessa identità persistente.

Questa parte deve essere pensata correttamente a livello database fin dall'inizio.

## 9. Intermediar — Creazione richiesta

Una richiesta può essere inviata soltanto a un'azienda precedentemente presente nella sezione Gestione.

Non voglio creare aziende casualmente mentre sto compilando una richiesta.

Prima: Gestione → azienda. Poi: Richiesta → azienda già disponibile.

## 10. Creazione della richiesta — un solo pannello

NON voglio un wizard da 6/8 passaggi. La richiesta deve essere creata attraverso un unico pannello semplice.

Campi principali:

- Azienda
- Luogo
- Data + ora
- Referente Intermediar (facoltativo)
- Ruolo/i + quantità
- Comunicazione (facoltativa)
- Allegati (facoltativi)

Esempio:

```
Bolanos Multi Services

Milano · Via Tortona 31
26 settembre · 08:00

Referente BluNotte
Salis

3 × Giardinieri
2 × Facchini
1 × Driver

Comunicazione:
"Presentarsi 15 minuti prima all'ingresso carraio."

[PDF] [Foto]

Invia richiesta
```

## 11. Ruoli dinamici

Intermediar non deve dipendere da una lista globale rigida di ruoli.

BluNotte deve poter chiedere: 3 Giardinieri, anche se Bolanos non possiede ancora il ruolo Giardiniere. La richiesta parte comunque.

Regola: **Richiesto ≠ ruolo creato. Accettato = ruolo acquisito.**

Se Bolanos accetta una richiesta contenente un nuovo ruolo, quel ruolo può entrare tra quelli utilizzabili dalla sua azienda.

Serve autocomplete intelligente per evitare duplicati del tipo: Facchino, facchini, FACCHINO — ma non dobbiamo impedire la creazione di ruoli nuovi.

## 12. Multi-ruolo

Una singola richiesta deve supportare più ruoli contemporaneamente. Esempio: 3 Facchini, 2 Allestitori, 1 Driver.

Non devono essere necessariamente tre lavori differenti.

## 13. Intermediar — Lavori

La Home di Intermediar deve permettere di capire immediatamente:

- cosa succede oggi;
- quale azienda gestisce il lavoro;
- quali richieste richiedono attenzione.

Ogni lavoro mostra principalmente: #numero, logo + nome azienda, luogo, data/orario, ruoli + quantità, eventuale referente.

## 14. Stati visivi

Vogliamo ridurre il testo e comunicare lo stato soprattutto visivamente.

- **Confermato.** Aspetto normale OperO. NON serve necessariamente scrivere continuamente: CONFERMATO. L'assenza di anomalie può significare confermato.
- **Da confermare.** Giallo. Deve essere immediatamente riconoscibile.
- **Modificato dopo conferma.** Giallo. La conferma precedente viene invalidata. L'azienda deve visualizzare nuovamente la richiesta e riconfermare.
- **Chiuso.** Card attenuata/opacizzata ma ancora leggibile. Possibile check minimale.

## 15. Modifica dopo conferma

Caso: BluNotte chiede 3 facchini, 08:00. Bolanos conferma. Successivamente BluNotte modifica: 08:00 → 07:30.

La richiesta non può rimanere automaticamente confermata. Deve passare a: **MODIFICATA / DA RICONFERMARE**.

Receive/OperO deve evidenziare cosa è cambiato. Esempio: *Orario modificato 08:00 → 07:30*.

L'azienda deve visualizzare e riconfermare.

## 16. Lato Bolanos — OperO completo

Se l'azienda che riceve la richiesta possiede OperO completo, la richiesta deve entrare direttamente nel suo ambiente OperO.

Prima vengono mostrati i dati ricevuti: azienda richiedente; numero richiesta; luogo; data/orario; referente Intermediar; ruoli e quantità; comunicazione; allegati.

Poi: **PREPARA SQUADRA**. Esempio:

```
Giardinieri 0/3   [Seleziona persone]
Facchini 0/2      [Seleziona persone]
Driver 0/1        [Seleziona persona]
```

OperO utilizza i lavoratori già presenti nell'azienda. Non bisogna reinserire nomi o numeri di telefono.

## 17. Assegnazione personale

Per ogni ruolo OperO deve permettere di selezionare lavoratori compatibili. Esempio:

```
Giardinieri 3/3 ✓
Mario Rossi
Luca Bianchi
Andrea Verdi

Facchini 2/2 ✓
ecc.
```

L'azienda sceglie inoltre il proprio: **Referente del servizio**, e procede con: **Conferma squadra / Conferma richiesta**.

## 18. Cosa vede Paolo dopo la conferma

Questo punto è molto importante.

Nel dettaglio di un lavoro confermato non voglio mostrare per prima cosa il riepilogo enorme di quello che Paolo stesso aveva scritto. Paolo sa già cosa ha richiesto. Vuole sapere: **Cosa mi ha risposto l'azienda?**

Gerarchia:

```
#1287 · Confermato
Bolanos Multi Services

Referente azienda
Mayra XXXXX
numero di telefono
azioni rapide: Chiama · WhatsApp

Convocati
Giardinieri
 1. Nome Cognome — telefono
 2. Nome Cognome — telefono
 3. Nome Cognome — telefono
Facchini
 1. Nome Cognome — telefono
 2. Nome Cognome — telefono
Driver
 1. Nome Cognome — telefono
```

Soltanto sotto: **Dettagli richiesta ›**, che permette di vedere ciò che BluNotte aveva originariamente richiesto.

## 19. Dati dei convocati

La visualizzazione dei nominativi/telefoni è possibile quando l'azienda fornitrice utilizza OperO completo e il flusso/permessi consentono la condivisione di quei dati operativi.

Receive invece non gestisce lavoratori. Quindi Receive non deve inventare o richiedere necessariamente una lista completa di dipendenti.

## 20. Receive — scopo

Receive deve essere volutamente limitato. Non deve diventare: "OperO gratis".

Receive serve esclusivamente a: ricevere richieste; leggerle; confermarle; indicare un referente; ricevere modifiche; riconfermare; comunicare; vedere/scaricare allegati; chiudere il servizio.

## 21. Receive — account

Ogni workspace Receive può avere: 1 responsabile/proprietario + massimo 2 utenti invitati. Totale: **MASSIMO 3 ACCESSI**.

Non devono esserci: lavoratori; turni del personale; convocazioni individuali; tariffe dipendenti; calendario del personale; gestione paghe; ruoli interni complessi.

## 22. Receive — Gestione

La sezione Gestione di Receive deve essere estremamente semplice.

**Profilo azienda**: Logo, Nome azienda. L'editing deve sembrare più simile alla modifica di un profilo social che alla configurazione di un ERP.

**Accessi Receive**: Responsabile, Utente 2, Utente 3 — con possibilità di invitare/rimuovere/sostituire nei limiti previsti.

NON creare una sezione: Referenti. Il referente viene scelto direttamente durante la conferma della richiesta.

## 23. Receive — lista lavori

Ogni card deve mostrare almeno: #numero; azienda richiedente; luogo; data/orario; ruoli + quantità; stato.

- **Giallo**: richiesta che necessita conferma. Vale sia per: nuova richiesta; richiesta precedentemente confermata ma successivamente modificata.
- **Verde / normale**: confermata.
- **Chiuso**: attenuato.

## 24. Apertura e lettura

Non voglio pulsanti "Letto" direttamente sulla card.

La richiesta viene considerata visualizzata quando l'utente entra nel dettaglio secondo la logica che verrà implementata.

Le azioni importanti devono stare dentro il dettaglio, non riempire la lista.

## 25. Dettaglio Receive

Mostrare: #numero; azienda mittente; luogo; data; orario; ruoli + quantità; eventuali modifiche; comunicazione; allegati scaricabili.

Deve esistere inoltre un piccolo controllo **Info** per mostrare: creatore; data/ora creazione; eventuale ultima modifica; chi ha effettuato la modifica.

## 26. Conferma Receive

Premendo: Conferma — non confermiamo immediatamente. Apriamo bottom sheet/modal:

```
Chi sarà il referente?
Nome referente
Telefono, se necessario
eventuale selezione di un utente Receive già presente.

Conferma richiesta
```

A quel punto Intermediar riceve: azienda confermata; referente; stato confermato; timestamp.

## 27. Cambio referente

Una richiesta già confermata deve permettere: **Cambia referente**.

Cambiare referente non annulla la conferma del lavoro.

## 28. Niente "Annulla partecipazione"

Una volta confermato il lavoro non voglio un generico bottone: Annulla partecipazione, perché potrebbe creare problemi operativi.

Le eccezioni/annullamenti devono essere trattati con una logica specifica successivamente.

## 29. Chiusura del servizio

Receive deve permettere di chiudere il servizio. La chiusura è a livello del servizio, non del singolo lavoratore.

Possibili dati: ora fine; eventuale nota; eventuale segnalazione.

Se l'azienda esterna non effettua la chiusura, Paolo deve poter inserire/gestire manualmente la fine del servizio da Intermediar.

Principio: **OperO non deve mai bloccare il lavoro reale perché l'altra azienda non ha completato un'azione digitale.**

## 30. Intermediar — Conti

Conti serve a vedere il rapporto economico con le aziende fornitrici.

Home: ricerca; mese; lista aziende con: logo + nome.

Aprendo un'azienda: **PANORAMICA** — Totale del periodo, Numero lavori, Categorie: Facchinaggio, Allestimento, Driver, Trasferte, ecc.

Le categorie devono derivare dai servizi effettivamente utilizzati.

## 31. Dettaglio categoria

Esempio:

```
Facchinaggio
#1287 — 03/10 — €…
#1294 — 07/10 — €…
#1302 — 11/10 — €…
Totale: €…
```

Deve essere possibile: **Esporta Excel**.

## 32. Fatture

Tab: **Panoramica | Fatture**.

Dentro Fatture i filtri devono rappresentare tipologie di servizio, non stati della fattura. Esempio: Tutti | Facchinaggio | Allestimento | Driver | Trasferte.

Nel caso BluNotte, normalmente è l'azienda fornitrice a fatturare direttamente BluNotte.

## 33. Receive → OperO completo

Receive deve essere progettato fin dall'inizio per poter diventare OperO.

Possibile CTA: Passa a OperO, oppure: Converti a OperO.

La conversione NON deve creare una nuova azienda. Il workspace esistente viene evoluto.

Devono essere mantenuti almeno: identità aziendale; storico delle richieste; rapporti con altre aziende; comunicazioni; eventuali ruoli acquisiti; dati compatibili.

Poi parte l'onboarding delle funzioni proprie di OperO: lavoratori; segreteria; tariffe; impostazioni operative; ecc.

## 34. Modello commerciale Receive

Ipotesi attuale da predisporre tecnicamente, ma non necessariamente da rendere definitiva nella prima demo: **30 giorni gratuiti**, poi circa: **€49,90/mese**.

Il trial deve iniziare quando l'azienda accetta l'invito e attiva realmente Receive, non quando Paolo crea l'azienda in Gestione.

La semplice esistenza di un workspace esterno non deve generare abbonamenti.

## 35. Interazione con aziende esterne

Questo principio è fondamentale: Intermediar deve funzionare anche se l'altra azienda non utilizza né Receive né OperO.

Altrimenti il prodotto diventa inutilizzabile finché tutta la rete non viene convertita.

Receive deve rendere la collaborazione migliore. OperO completo deve renderla ancora più potente. Ma nessuno dei due deve essere requisito per creare e utilizzare un fornitore.

## 36. Gerarchia dell'ecosistema

```
ESTERNO          collaborazione minima
   ↓
RECEIVE          ricezione e gestione strutturata delle richieste
   ↓
OPERO COMPLETO   gestione completa azienda + personale + Intermediar
```

La conversione deve mantenere la stessa identità aziendale.

## 37. UX/UI

NON vogliamo un gestionale tradizionale.

Evitare: tabelle enormi; form infiniti; menu tecnici; badge ovunque; pagine piene di testo; dashboard SaaS generiche.

Intermediar deve utilizzare lo stesso linguaggio grafico dell'OperO attuale: nero/petrolio molto scuro; bordi teal sottili; card integrate nello sfondo; forme morbide; logo azienda molto visibile; poco testo; controlli grandi e semplici da toccare; animazioni leggere; interazioni immediate.

Il principio è: **La complessità deve stare nel sistema, non davanti all'utente.**

## 38. Intelligenza contestuale

In fase di creazione richiesta, il sistema può progressivamente suggerire: luoghi recentemente utilizzati con quella società; ruoli frequentemente richiesti; referenti utilizzati; orari ricorrenti.

In futuro possiamo permettere: incolla testo; dettatura; foto; PDF; e utilizzare AI per precompilare lo stesso pannello strutturato.

L'AI non deve creare un secondo flusso. Deve semplicemente accelerare quello esistente.

## 39. Demo — obiettivo minimo

La prima demo non deve contenere tutto. Il percorso fondamentale che deve funzionare è:

1. Paolo entra nel workspace BluNotte.
2. Entra in Intermediar.
3. Seleziona Bolanos.
4. Crea una richiesta.
5. Bolanos la riceve in OperO.
6. Bolanos prepara la squadra.
7. Bolanos seleziona il referente.
8. Bolanos conferma.
9. Paolo vede automaticamente referente + convocati.
10. Paolo modifica un dato della richiesta.
11. La conferma viene invalidata.
12. Bolanos vede chiaramente la modifica e riconferma.
13. Il servizio viene successivamente chiuso.

Parallelamente deve essere dimostrabile anche: Intermediar → azienda Receive → conferma + referente → Intermediar.

Questo è il cuore da validare sul campo.

## 40. Principi da non rompere durante lo sviluppo

Questi punti sono vincolanti nella progettazione:

- Una persona = un'identità, potenzialmente più workspace.
- Una società = un'identità persistente che può evolvere da esterna → Receive → OperO.
- Una richiesta = un'unica entità condivisa, non copie scollegate.
- Intermediar è dentro OperO.
- Receive non deve diventare OperO gratuito.
- Un'azienda esterna deve essere utilizzabile anche senza accettare Receive.
- Una modifica importante dopo la conferma richiede riconferma.
- Il referente Intermediar e il referente dell'azienda fornitrice sono due soggetti differenti.
- Receive gestisce il servizio, non i lavoratori.
- OperO completo può gestire e condividere la squadra.
- Il sistema non deve bloccare un lavoro reale per un'azione digitale mancante.
- La UX deve restare semplice anche quando la logica sottostante diventa complessa.

---

## Riassetto del 30/09/2026 — CO-OPERO bilaterale

Portato da Patrick il 30/09/2026 con «abbiamo riorganizzato le idee»: «siamo
io e Seba insieme che abbiamo riorganizzato la struttura». È il prompt che si erano preparati per Claude, scritto
con un assistente AI: qui sta com'è arrivato, tolto il preambolo della chat.
Cosa cambia rispetto al 24/09 → [[opero-intermediar-receive]].

> OperO è il cervello centrale, mentre CO-OPERO fa da doppio ponte (in entrata
> per i clienti e in uscita per i fornitori).

**1. Visione d'insieme dell'ecosistema**

- **OperO**: è il gestionale principale (a pagamento) usato dall'azienda principale.
- **CO-OPERO**: è un portale web gratuito bilaterale che gestisce sia le richieste in entrata (dai clienti dell'azienda) sia le richieste in uscita (verso i fornitori dell'azienda).

**2. Mappatura dei collegamenti (OperO ↔ CO-OPERO)**

L'integrazione tra le due piattaforme si divide in due flussi speculari.

*Flusso 1: Clienti → OperO (gestione lavoro in entrata)*

- Lato CO-OPERO (Sezione Clienti):
  - È il portale gratuito usabile dai clienti dell'azienda (che non possiedono OperO).
  - Il cliente entra, va su "Richiedi Nuovo Lavoro", inserisce chi gli serve, data/ora, luogo e note.
  - Ha una sezione "Lavori Richiesti" (per monitorare lo stato) e una sezione "Conti" (per vedere i costi e la rendicontazione a lavoro finito).
- Collegamento dentro OperO → pagina "Richieste":
  - In OperO, tutte le chiamate/richieste provenienti da CO-OPERO (Sezione Clienti) atterrano nella pagina "Richieste".
  - È strutturata come un'interfaccia tipo chat/WhatsApp: c'è l'elenco delle aziende clienti con un pallino di stato:
    - 🔵 Pallino blu: nuova richiesta in arrivo.
    - 🔴 Pallino rosso: richiesta rifiutata dall'operatore.
    - 🟢 Pallino verde: richiesta accettata. Quando l'operatore accetta, inserisce i nominativi dei lavoratori, cellulari ed eventuali note. Questa azione crea automaticamente la commessa/lavoro dentro OperO e rimanda la conferma con i dettagli al cliente su CO-OPERO.

*Flusso 2: OperO → Fornitori (gestione lavoro in uscita / subappalto)*

- Collegamento dentro OperO → pagina "Gruppo / Intermediar":
  - Quando l'azienda che usa OperO deve richiedere manodopera/servizi esternamente a una cooperativa o fornitore (che non usa OperO), avvia la procedura dalla sezione "Gruppo" (Intermediar).
- Lato CO-OPERO (Sezione Fornitori):
  - La richiesta inviata da OperO (Gruppo) arriva alla Sezione Fornitori di CO-OPERO.
  - Il fornitore esterno riceve la richiesta nel suo portale gratuito CO-OPERO, decide se accettare o rifiutare.
  - Se accetta, il fornitore inserisce i ruoli, i nominativi delle persone inviate e conferma.
  - L'accettazione torna indietro ad OperO nella sezione Gruppo, aggiornando lo stato della scheda operativa.

**3. Sintesi dei punti di contatto dentro OperO**

1. Pagina "Richieste": riceve ed elabora solo i dati da CO-OPERO (Sezione Clienti).
2. Pagina "Gruppo" (Intermediar): invia ed elabora le richieste verso CO-OPERO (Sezione Fornitori).

> Tieni in considerazione questa struttura bipolare per definire la logica di
> routing delle API, i dati di DB da scambiare (payload richieste, nominativi,
> cambi di stato del pallino 🔵/🟢/🔴) e l'interfaccia utente.

**Precisazioni di Patrick, 30/09/2026**

- «per quanto riguarda WhatsApp si intende solo l'aspetto, non una chat»
- «Va benissimo aggiungere il pallino giallo se viene modificato»
- «per la questione pallini, decidi tu, nel senso, magari cambia anche il tipo, io ho pensato ai pallini perché era comodo a livello visivo»
- «coopero è gratuito perché serve alle aziende che non hanno opero, ok? Invece opero è quello a pagamento e l'obiettivo è far diventare a pagamento, o meglio, probabilmente in futuro diventerà a pagamento anche coopero, ma l'obiettivo è anche che chi utilizza coopero sia talmente tanto preso da questa cosa che gli venga voglia di acquistare opero»
- «conti è proprio sbagliata, infatti conti deve essere solo che quando si chiude il lavoro il, ehm cliente, vede, pressa poco, in maniera non precisa, quindi una stima, di quanto dovrà pagare. E basta. E anche le pagine devono essere semplicemente il nuovo lavoro, lavori in corso, barra, lavori in generale, e conti. Fine.»
- «il portale fornitori non devi vederlo ora lo vedremo in un secondo momento ora ci dobbiamo concentrare solo su questa parte»
- «l'invito di Coopero è letteralmente che se io ho un'azienda cliente che ora mi sta scrivendo su WhatsApp, io gli invio semplicemente un link per accedere a Coopero e poi le richieste le mando direttamente su Coopero entrando con il suo eh, numero token, come vuoi chiamarlo, come Alus001. E, mh, accede e manda le richieste»
- «per quanto riguarda le richieste a me io avrei un'altra pagina [...] perché eh, voglio tenere staccato richieste dal nuovo lavoro perché il nuovo lavoro deve essere una cosa manuale prettamente e sì, lo so che è ridondante ma preferisco così Anche perché l'obiettivo è in un futuro che non ci dovrà neanche essere nuovo lavoro perché si farà tutto tramite Coopero. O meglio, l'integrazione tra Coopero e Opero non va scritto a mano perché non ci dovranno essere clienti che non usano Coopero. Però questo è in futuro, quindi per ora voglio un'altra pagina.»
- «per quanto riguarda chi ti serve, sì, si possono indicare anche più eh, lavoratori di, di diversi tipi»
- «Per quanto riguarda le altre domande, io per ora non ti darei una risposta e aspetterei che mi dice qualcosa Seba.» (accetto con modifica e motivo del rifiuto, modifica e annullamento del cliente, cambio di un lavoratore)
- «per quanto riguarda la stima dei conti, sì, quando il lavoro lo chiude e lo chiude come, a, come succede su Opero, cioè quando si chiude su Opero eh, arriva una stima di conti»
- «per quanto riguarda la notifica, sì, è meglio che si riceva una notifica»

**Mockup di Patrick, 30/09/2026**

«questo è un mockup MOLTO GROSSOLANO da prendere con le pinze di come immagino
le interfacce, come vedi ci sono tante cose errate e anche brutte
esteticamente ma è solo per darti un idea». L'immagine non è nel vault: qui le
otto schermate, com'erano.

1. **CO-OPERO, dashboard cliente**: saluto, bottone «Richiedi nuovo lavoro», tre contatori (lavori attivi, in attesa, completati negli ultimi 30 giorni), ultime richieste con lo stato. Menu: Home, Richiedi nuovo lavoro, I miei lavori richiesti, Conti.
2. **CO-OPERO, richiedi nuovo lavoro**: «Chi ti serve?» (una figura o un servizio da un elenco), data, ora, luogo, note fino a 500 caratteri, «Invia richiesta».
3. **CO-OPERO, lavori richiesti**: schede Tutti, In corso, Completati, Annullati; ogni riga ha servizio e città, data e ora, stato.
4. **CO-OPERO, conti**: «Saldo disponibile € 1.240,00»; rendicontazione con schede Tutti, Lavori, Pagamenti; righe in uscita «Pagato», in entrata «Accredito».
5. **OperO, pagina Richieste**: ricerca, elenco di aziende clienti con data e ora della richiesta e lo stato sulla riga (nuova, accettata, rifiutata, lavoro in corso, lavoro completato). Menu: Home, Richieste, Lavori, Conti, Gruppo, Report, Impostazioni.
6. **OperO, dettaglio richiesta e accettazione**: figura, data e ora, luogo e note del cliente; sotto, nominativi da scegliere o aggiungere, cellulari, note interne, bottone «Accetta e crea commessa».
7. **OperO, Gruppo / Intermediar**: «Nuova richiesta», schede Tutte, In attesa, Accettate, Rifiutate; ogni riga ha fornitore, ruolo o servizio, data, stato.
8. **CO-OPERO, dashboard fornitore**: saluto, «Richieste in arrivo» col numero delle nuove, elenco con Da valutare, Accettata, Rifiutata. Menu: Home, Richieste (col numero), Lavori, Conti.
