---
type: progetto
status: attivo
client: cliente-opero
stack: [react-19, typescript, vite-8, tailwind-3, react-router-7, tanstack-query, supabase, capacitor-6]
started: 2026-07-20
deadline: TODO
updated: 2026-08-28
source: repo
valore: 2400
incassato: 400
---

# OperO — gestionale cantieri e fatturazione

Gestionale multi-azienda per un'impresa di **facchinaggio, allestimenti e
traslochi**. La segreteria gestisce clienti, cantieri, squadre, conti dei
lavoratori e la fatturazione. Cliente: [[cliente-opero]].

**Repo**: `github.com/Nixo999/opero-sito` (npm: `opero-core`)
**Memoria tecnica**: `CLAUDE.md` + `docs/handoff.md` nel repo — 4.400 righe di
storico. Leggerli prima di toccare qualsiasi cosa.

## Cos'è davvero

Non è un'app nuova: è la **ricostruzione pulita** di `sebapp-bolanos`, un'app
già in produzione presso il cliente, costruita con **Lovable**. La regola
fondante era *stessa app, codice migliore* — nessuna funzione in più, nessuna in
meno, e l'app vecchia resta la specifica di riferimento.

⚠️ **Dall'11 agosto 2026 quella regola non regge più**: il committente ha
iniziato a chiedere funzioni che nella vecchia app non esistono (sospensione
utenti, ruoli personalizzati, preferiti, liste super admin, notifiche con
immagini, creazione account). Vedi [[2026-08-11-opero-scope-allargato]].

## Soldi

| | |
|---|---|
| Prezzo pattuito | **2.400 €** |
| Incassato al 2026-08-28 | **400 €** |
| **Da incassare** | **2.000 €** |
| Forma | Ricevuta per prestazione occasionale — nessuna P.IVA, vedi [[vincoli-fiscali]] |

⚠️ Da soli, i 2.400 € di questo progetto occupano **quasi metà** del tetto
annuo dei 5.000 € su una singola testa. Va deciso su chi vengono emesse le
ricevute prima di incassare i 2.000.

## A che punto siamo

**~60%** (rilevazione del 21 agosto 2026, dal repo). Quattro aree vive sul
database:

| Area | Cosa fa |
|---|---|
| **Segreteria** | Clienti, tariffe, cantieri, conti, fatture PDF/Excel |
| **Lavoratore** | Turni, chiusura chiamata, ore, calendario, rubrica ufficio |
| **Visualizer** | Lavori, conti, disponibilità — sola lettura |
| **Admin** | Utenti, tipo lavoratore, Plus, aziende, cruscotto workspace |

**Non iniziati**: lavoratori provvisori, **migrazione dello storico**, app
native compilate.

> [!warning] La migrazione dello storico è il rischio numero uno
> Il piano la dava chiusa a fine settimana 1. Non è mai stata toccata, ed è
> l'unico pezzo che al go-live non si può rimandare: senza storico il cliente
> perde i dati di anni. Lo schema nuovo copre 31 tabelle sulle 45 di produzione.

## Il piano consegnato vs la realtà

Il PDF *"Piano di Sviluppo e Migrazione Software (V2)"* consegnato al cliente
dichiara: **inizio 20 luglio 2026, fine indicativa 21 agosto 2026**.

Siamo oltre quella data. Secondo Nicola (28 agosto) **la scadenza non è più
stringente**: il lavoro attuale è correzione su segnalazione, non sviluppo.

⚠️ **Il documento consegnato al cliente non è mai stato corretto** e promette
ancora Chat, Disponibilità, XML FatturaPA e area Direzione. Chat e Direzione
sono fuori scope per decisione del committente stesso; Disponibilità è
rientrata il 20 agosto. Al go-live quelle voci risulteranno **mancanti anziché
rinunciate**, e la differenza la nota il cliente, non noi.

## Lo scope si muove — cronologia

| Data | Cosa è successo |
|---|---|
| 2026-08-04 | Committente toglie Chat e Disponibilità |
| 2026-08-05 | Committente toglie XML FatturaPA e area Direzione |
| 2026-08-11 | Chiede funzioni **nuove**, non presenti nella vecchia app |
| 2026-08-20 | Disponibilità **rientra**, sviluppata in giornata |
| 2026-08-22 | **XML SDI richiesto di nuovo** → [[2026-08-22-xml-sdi-da-quotare]] |
| 2026-08-25/27 | Tre liste di segnalazioni in tre giorni |

## Il ritmo attuale, e cosa dice

Dal 25 al 27 agosto sono arrivate **tre liste di segnalazioni** dal
committente. Nella seconda, **tre punti su nove erano regressioni** introdotte
dal lavoro consegnato poche ore prima. Nella terza, **cinque punti su dieci**
nascevano da un'unica regola mancante ("l'autista esterno guida e basta").

> [!note] Analisi di Claude — 2026-08-28
> Il pattern è consegna rapida → il cliente prova → segnala anche quello che
> abbiamo appena rotto. Non è cattiva volontà del cliente: è che consegniamo
> senza un giro di verifica nostro, e il collaudo lo sta facendo lui. Costa
> credibilità in un progetto già oltre la data. Il repo lo dice esplicitamente:
> *"Non erano difetti vecchi scoperti da lui — li ha trovati perché avevamo
> consegnato."*

## Ambienti

| Ambiente | Progetto Supabase | Nota |
|---|---|---|
| Produzione cliente | `avsuihlxecpbmddhnyvo` | Usata da `sebapp-bolanos`. **Mai toccare** |
| Sviluppo | `oyoltwisdwujitsryzax` | Collegato al repo, è anche il sito di prova |

**Nessun test automatico** in questo progetto: la verifica è nel browser,
misurando con `getComputedStyle` / `getBoundingClientRect`. Vedi [[convenzioni]].

## Aperto

- [ ] Incassare i **2.000 €** residui — decidere su chi emettere la ricevuta
- [ ] **Quotare l'XML SDI** come lavoro nuovo, non regalarlo
- [ ] **Correggere il PDF consegnato** al cliente sulle funzioni rinunciate
- [ ] Migrazione dello storico: almeno stimarla
- [ ] Lavoratori provvisori (4 tabelle + edge function)
- [ ] Applicare la migrazione `20260826110000` (trigger finestra)
- [ ] Decidere una data di go-live e dirla al cliente

## Collegamenti

[[cliente-opero]] · [[stack]] · [[convenzioni]] · [[vincoli-fiscali]] ·
[[2026-08-11-opero-scope-allargato]] · [[2026-08-22-xml-sdi-da-quotare]]
