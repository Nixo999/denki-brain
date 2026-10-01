---
type: decisione
riga: Prototipo di CO-OPERO chiesto da Nicola il 1/10 - quattro scelte tecniche proposte da Claude, in attesa del suo verdetto. Niente pubblicato.
data: 2026-10-01
progetto: opero
updated: 2026-10-01
source: claude
tags: [opero, co-opero, prototipo, architettura]
---

# CO-OPERO: il prototipo, e le quattro scelte da confermare

**Chiesto da Nicola il 1 ottobre 2026**: «prova usando più agenti a disegnare e
creare una versione di coopero intanto sito […] devono già parlarsi, usa lo
stesso database di opero». Le scelte qui sotto le ha fatte Claude costruendo:
**valgono come proposta finché Nicola non le guarda.** Il perché esteso sta nel
repo, `docs/coopero.md`.

## Le scelte

1. **Due siti, un database.** Il portale è una seconda radice Vite dentro
   `opero-sito` (`coopero/`), con un indirizzo suo: sotto lo stesso dominio di
   OperO il service worker risponderebbe con la pagina sbagliata.
2. **Il cliente non è un utente.** Entra da un link con un segreto lungo, non
   da un account: `profiles` vuole un'azienda sola e fa nascere chiunque come
   lavoratore. Il codice tipo `VERT001` identifica, non protegge.
3. **Accettare una richiesta apre «Nuovo lavoro» già compilato.** Nessun
   secondo modo di creare un lavoro: la squadra si compone con le regole di
   sempre. Richieste resta una pagina a sé, come voleva Patrick (30/09).
4. **La stima la calcola il browser dell'ufficio** con `invoiceEngine`, e la
   salva. Arriva quando l'ufficio apre OperO, non all'istante della chiusura:
   per farla arrivare da sola serve una funzione lato server.

## Cosa non è deciso da nessuno

Le regole su modifica e annullo del cliente dopo la conferma, il motivo del
rifiuto, la conferma senza nomi: nel prototipo c'è la versione più semplice,
**aspettano [[sebastian-torres]]** come il 30/09 → [[co-opero-clienti]].
Lo stato del prototipo → [[co-opero-prototipo]].

## Collegamenti

[[co-opero-prototipo]] · [[co-opero-clienti]] · [[opero-intermediar-receive]] · [[opero]] ·
[[registro-interventi]]
