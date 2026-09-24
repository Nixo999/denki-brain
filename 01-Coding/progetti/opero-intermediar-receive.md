---
type: risorsa
riga: Intermediar + Receive, il prossimo pezzo di OperO chiesto da Seba il 24/09 - da conoscere, non da fare. Principi, demo minima, buchi della specifica.
updated: 2026-09-24
source: claude
progetto: opero
tags: [opero, intermediar, receive, specifica, sebastian-torres]
---

# OperO — Intermediar + Receive

**Da conoscere, non da fare.** Seba ha mandato la specifica il 24/09/2026 con
l'indicazione di farla conoscere a Trevis, **non di iniziarla**: niente codice,
niente quotazione, niente date. Parole sue → [[opero-intermediar-receive-testo]].

**In una riga**: OperO organizza le persone della propria azienda, Intermediar
le aziende che lavorano per lei, Receive fa ricevere e confermare le richieste
a un'azienda che OperO non ce l'ha.

**Il caso che la guida**: Paolo, per BluNotte, deve coprire 40 facchini e li
spartisce fra Bolanos (8), la sua azienda e La Scelta Giusta. Oggi è tutto su
WhatsApp. Flusso: richiesta → fornitore → conferma → squadra e referente →
esecuzione → chiusura → conti.

## Il modello, in cinque righe

- **Una persona, più workspace.** Il cambio è alla Instagram, e il workspace attivo decide per chi si opera.
- **Un'azienda, un'identità che evolve**: esterna (nome + telefono, usabile subito) → Receive → OperO completo. Mai una seconda riga.
- **Una richiesta, un'entità sola** vista da due aziende: niente copia #456 della #1287.
- **Intermediar sta dentro OperO**: un controllo a destra della bottom nav, non una quinta voce. Dentro: Lavori · Richieste · Gestione · Conti.
- **Receive è OperO ridotto**, non gratis: 3 accessi, nessun lavoratore; trial di 30 giorni **dall'attivazione**, poi ~49,90 €/mese (ipotesi).

## Stati e regole del flusso

- Da confermare e modificata dopo conferma: **giallo**. Confermato: aspetto normale, senza etichetta. Chiuso: card attenuata.
- Una modifica dopo la conferma la **invalida** e mostra il diff (`08:00 → 07:30`). Cambiare referente **non** la invalida.
- Niente «Annulla partecipazione»: gli annullamenti avranno una logica loro, dopo.
- La chiusura è del servizio, non del lavoratore. Se il fornitore non chiude, **chiude Paolo** da Intermediar.
- Dopo la conferma Paolo vede per prima cosa **referente e convocati** con telefono. Quello che aveva chiesto sta sotto, in «Dettagli richiesta ›».
- Ruoli liberi: **richiesto ≠ ruolo creato, accettato = ruolo acquisito**, con autocomplete contro `Facchino`/`facchini`/`FACCHINO`.

**Demo minima (§39)**: BluNotte → richiesta a Bolanos → Bolanos prepara la
squadra, sceglie il referente e conferma → Paolo vede i convocati → Paolo
modifica → la conferma cade → Bolanos riconferma → chiusura. Più lo stesso giro
con un'azienda Receive, senza squadra.

## Cosa morde

> [!note] Analisi di Claude — 2026-09-24, non verificata
> Il repo OperO non è sul Mac dove è stata scritta: le righe sullo schema sono
> ipotesi finché qualcuno non le controlla nel repo.

1. **È lavoro nuovo, fuori dai 2.400 €**, e più grande di XML SDI e OperO
   Choice messi insieme: è un secondo prodotto dentro il primo. I 2.000 € del
   primo non sono ancora entrati → [[opero]].
2. **Il legame utente-azienda.** Se oggi un utente appartiene a una sola
   azienda, «una persona, più workspace» è il primo muro: servono le membership
   e una RLS che legga il workspace attivo. `TODO`: controllare nel repo.
3. **Una richiesta con due proprietari.** Le policy oggi ragionano per una
   azienda sola, qui la stessa riga la leggono il richiedente e il fornitore con
   campi diversi. Serve anche lo storico delle modifiche, perché il diff e
   l'invalidazione della conferma ne dipendono.
4. **Receive tocca il ricavo di Seba**: un piano nuovo in `workspace_plans`,
   con un trial che parte all'attivazione e non alla creazione.
5. **Nomi e telefoni dei lavoratori di Bolanos finiscono a BluNotte.** Sono
   dati personali che passano da un'azienda all'altra. Serve una base, e non
   è una scelta tecnica.

## Buchi nella specifica — da chiedere a Seba quando si parte

- **Da dove vengono i € dei Conti?** Il pannello della richiesta non ha un
  prezzo né una tariffa concordata, e i Conti mostrano totali per categoria.
- **I 40 facchini** non esistono come entità: si vedono solo le richieste per
  azienda. Manca il fabbisogno padre, e con lui il «40 su 40 coperti».
- **Quali modifiche sono «importanti»** (§40) e fanno cadere la conferma, e
  quali no.
- **Lavori e Richieste**: il §13 descrive Lavori, la tab Richieste non è
  descritta. Pannello di creazione o lista?
- **Fatture**: se fattura il fornitore a BluNotte, cosa ci sta dentro
  Intermediar, un PDF caricato o un dato?
- **Il referente Receive** è un nome libero o uno dei 3 accessi? Il §26 li
  ammette tutti e due.

## Collegamenti

[[opero]] · [[sebastian-torres]] · [[opero-intermediar-receive-testo]] ·
[[stack]] · [[modifiche-al-database]]
