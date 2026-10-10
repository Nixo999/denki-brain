---
type: risorsa
riga: Ecosistema OperO + CO-OPERO (30/09) sopra Intermediar + Receive (24/09) - da conoscere, non da fare. Modello, cosa dice il repo oggi, buchi.
updated: 2026-10-10
source: claude
progetto: opero
tags: [opero, intermediar, receive, co-opero, specifica, sebastian-torres]
---

# OperO — Intermediar, Receive, CO-OPERO

**Da conoscere, non da fare.** Seba ha mandato la specifica il 24/09/2026 per
farla conoscere, **non per iniziarla**. Il 30/09 Patrick ha portato un
riassetto, anche quello da imparare e non da costruire: «non mettere mano al
codice». L'hanno riorganizzato **Patrick e Seba insieme** (30/09). Niente
codice, niente quotazione, niente date. Testi integrali →
[[opero-intermediar-receive-testo]].

⚠️ **Dal 1/10 esiste un prototipo del flusso 1**, chiesto da Nicola: ramo
`coopero` di `opero-sito`, in locale, non pubblicato e con la migrazione non
applicata → [[co-opero-prototipo]].

⚠️ **Dal 10/10 esiste anche il flusso 2, solo in locale**, chiesto da Nicola
(«aggiungiamo a opero per adesso solo in locale sul mio pc la parte di
intermediar») sul PDF di Seba di ottobre: ramo `intermediar` di `opero-sito`
(`1aab6fe`, non pushato), migrazione solo sul banco locale. Com'è fatto lo
dice `docs/intermediar.md` del ramo → [[registro-interventi]].

## Il modello del 30/09: OperO al centro, CO-OPERO doppio ponte

- **OperO** è il gestionale a pagamento dell'azienda. **CO-OPERO** è un portale web **gratuito** con due sezioni, per chi OperO non ce l'ha. Deciso da Patrick e Seba (30/09): supera il Receive a pagamento del 24/09.
- **Perché è gratis**, parole di Patrick (30/09): «coopero è gratuito perché serve alle aziende che non hanno opero», «probabilmente in futuro diventerà a pagamento anche coopero, ma l'obiettivo è anche che chi utilizza coopero sia talmente tanto preso da questa cosa che gli venga voglia di acquistare opero». **CO-OPERO è l'amo, OperO è la vendita.**
- **Flusso 1, in entrata.** CO-OPERO Clienti ha **tre pagine e basta** (Patrick, 30/09): **Nuovo lavoro** (chi serve, data e ora, luogo, note), **Lavori** (in corso e tutti), **Conti**. **Conti è solo una stima**: a lavoro chiuso il cliente vede, all'incirca, quanto dovrà pagare. Niente saldo, niente pagamenti. In OperO la richiesta atterra nella pagina **Richieste**: elenco di aziende clienti con l'aspetto di WhatsApp, **non una chat** (Patrick, 30/09), con gli stati di [[co-opero-clienti]]. Accettare vuol dire mettere nomi e cellulari dei lavoratori e le note: nasce il lavoro in OperO e la conferma torna al cliente.
- **Flusso 2, in uscita.** Dalla pagina **Gruppo** (Intermediar) l'azienda chiede manodopera a una cooperativa o a un fornitore. Il fornitore, da CO-OPERO Fornitori, accetta o rifiuta. Se accetta mette ruoli e nomi, conferma, e lo stato torna nella scheda di Gruppo.
- **Richieste** riceve solo dai clienti, **Gruppo** manda solo ai fornitori.
- **Prima il flusso 1** (Patrick, 30/09): «il portale fornitori [...] lo vedremo in un secondo momento, ora ci dobbiamo concentrare solo su questa parte». Gruppo e CO-OPERO Fornitori aspettano.

> [!note] Analisi di Claude — 30/09/2026, il riassetto letto contro il 24/09
> - CO-OPERO Fornitori è il **Receive** del 24/09, la pagina Gruppo è
>   **Intermediar**. Il flusso 1 è **nuovo**: il 24/09 i clienti di
>   un'azienda non entravano da nessuna parte.
> - I due flussi sono **la stessa richiesta vista dai due capi**: BluNotte che
>   chiede a Bolanos è flusso 2 per BluNotte e flusso 1 per Bolanos. È il
>   principio del 24/09, «una richiesta, un'entità sola», e regge ancora.
> - **Il gratis regge se si ferma dove OperO comincia.** Il §40 del 24/09,
>   «Receive non deve diventare OperO gratuito», vale ancora nello spirito:
>   CO-OPERO riceve, conferma e fa vedere i conti, ma non gestisce lavoratori,
>   turni e paghe. Se il gratis fa tutto, nessuno compra. E il passaggio va
>   fatto senza rifare niente: l'identità che evolve del 24/09, esterna →
>   CO-OPERO → OperO, è il gancio della vendita.
> - **«Richieste» cambia significato**: il 24/09 era una tab dentro
>   Intermediar, in uscita. Il 30/09 è la pagina in entrata.

## Flusso 1, stati e mockup → [[co-opero-clienti]]

Le decisioni di Patrick sul flusso dei clienti, gli stati delle richieste e il
mockup del 30/09 stanno in una nota a sé.

## Cosa dice il repo oggi

Letto il 30/09/2026 in `Nixo999/opero-sito`, commit `3f980c6` (24/09). Niente
toccato.

- **Un utente, un'azienda.** `profiles.company_id` è obbligatorio, non c'è una tabella di appartenenze, il login chiede il codice azienda e `has_role()` non guarda l'azienda. Una cooperativa fornitrice di due aziende OperO, o cliente e fornitore insieme, oggi non ha dove stare.
- **I clienti non hanno login né portale.** `clients` è un nome dentro l'azienda; il referente del cliente è testo libero sul singolo lavoro.
- **Fornitori e aziende esterne non esistono.** «Aziende» nell'Admin è la lista dei workspace del Super Admin.
- **Chi sta in un lavoro deve avere un account** (`job_assignments.worker_id` → `auth.users`). Nomi e telefoni battuti da un fornitore lì non entrano. Il concetto più vicino sono i lavoratori provvisori, mai iniziati.
- **I prezzi al cliente ci sono**: tariffe per cliente e per mansione, calcolate da `lib/invoiceEngine.ts`. I Conti del flusso 1 sanno da dove prendere i €. Per i fornitori del flusso 2 una tariffa non esiste.
- **Niente tempo reale, niente notifiche web.** Le push sono solo native (FCM, APNs) e partono dalla segreteria: un portale web oggi non riceve niente da solo.
- **La chat c'è nel database e non si usa**: tabelle `chat_*` mai collegate, chat tolta da Seba il 4/08. «Tipo WhatsApp» è solo l'aspetto (Patrick, 30/09): la chat resta fuori.
- **Il menu della segreteria** oggi è Lavori, Nuovo lavoro, Conti, Clienti, più Gestione e Amministrazione per chi li ha (`lib/navConfig.tsx`). Sul telefono è l'isola in basso, sul computer la colonna a sinistra: una voce in più sul telefono si paga.
- **Un lavoro non ha una colonna di stato**: si ricava da annullato, chiuso, fatturato. Gli stati della richiesta sarebbero i primi scritti.

## Regole del flusso, dal 24/09

- Una modifica dopo la conferma la **invalida** e mostra il diff (`08:00 → 07:30`). Cambiare referente no. Quali modifiche contano: `TODO` (§40).
- La chiusura è del servizio, non del lavoratore. Se il fornitore non chiude, chiude chi ha chiesto.
- Dopo la conferma chi ha chiesto vede per primi **referente e convocati** con telefono; la richiesta sta sotto, in «Dettagli richiesta ›».
- Ruoli liberi: **richiesto ≠ ruolo creato, accettato = ruolo acquisito**, con autocomplete.

**Demo minima** → §39 in [[opero-intermediar-receive-testo]].

## Cosa morde

1. **Lavoro nuovo, fuori dai 2.400 €**, e col flusso 1 più grande del 24/09: sono tre facce nuove (Richieste, Gruppo, il portale). Del primo mancano 1.000 € (30/09) → [[opero]].
2. **Una richiesta con due proprietari**: la stessa riga letta da chi chiede e da chi esegue, con campi diversi, e lo storico delle modifiche per il diff. Le policy oggi ragionano per un'azienda sola.
3. **Il ricavo**: con CO-OPERO gratis il piano di Receive in `workspace_plans` non serve più. Il portale rende solo se porta aziende a OperO, e da quando i soci sono tre (30/09) è ricavo anche nostro → [[sebastian-torres]].
4. **Nomi e telefoni passano da un'azienda all'altra**, ora in tutti e due i versi: i lavoratori dell'azienda al cliente (flusso 1), quelli del fornitore all'azienda (flusso 2). Serve una base, e non è una scelta tecnica.
5. **L'accordo del 25/09** mette «Coopero/cOperO» nel perimetro della non concorrenza → [[accordo-riservatezza-opero]].

## Buchi — da chiedere a Seba quando si parte

- **Le quattro del flusso 1 che aspettano lui** (30/09) → [[co-opero-clienti]].
- **Come entra un fornitore su CO-OPERO**: il cliente entra con link e codice (30/09), il fornitore non è deciso.
- **Da dove vengono i € dei Conti del flusso 2**: il fornitore non ha tariffa.
- **I 40 facchini** non esistono come entità: manca il fabbisogno padre, e con lui il «40 su 40 coperti».
- **Fatture**: se fattura il fornitore, cosa ci sta dentro, un PDF caricato o un dato?
- **Il referente del fornitore** è un nome libero o un accesso (§26)?

## Collegamenti

[[opero]] · [[co-opero-clienti]] · [[sebastian-torres]] · [[opero-intermediar-receive-testo]] ·
[[accordo-riservatezza-opero]] · [[stack]] · [[modifiche-al-database]]
