---
type: cliente
status: attivo
progetti: [opero]
updated: 2026-08-28
source: denkicode
settore: software, in fase di avvio
---

# Sebastian Torres — "Seba"

**Privato, non un'azienda.** Sta aprendo la sua attività, e l'attività **è
[[opero]]**: l'app che stiamo costruendo noi è la sua idea imprenditoriale.
Noi siamo i suoi sviluppatori, non i suoi fornitori di gestionale.

## La catena, che va capita bene

```
DenkiCode  ──sviluppa──▶  OperO  ──venduto da Seba a──▶  aziende clienti
                                                          └─ 1ª: il padre di Seba
                                                             (facchinaggio,
                                                              allestimenti, traslochi)
                                                          └─ 2ª: in attesa
```

Questo spiega l'architettura del prodotto, che altrimenti sembra
sovradimensionata: OperO è **multi-azienda** perché Seba deve poterlo rivendere.
L'area Super Admin con il **cruscotto mensile di quanto ogni workspace paga a
OperO** (`lib/pianoWorkspace.ts`, listino datato in `workspace_plans`) non è una
funzione di comodo: **è il suo modello di ricavo**.

L'app precedente, `sebapp-bolanos`, è quella che gira **oggi** presso l'azienda
del padre. È la sua prima installazione reale, non un prototipo.

## Il rapporto

| | |
|---|---|
| Chi è | Sebastian Torres, detto **Seba**. Privato, aspirante imprenditore |
| Come è arrivato | `TODO` |
| Referente | Lui stesso — decide, collauda e segnala |
| Canale | `TODO` (presumibilmente WhatsApp) |
| Chi gli parla | Patrick |
| Suoi clienti | 1 attivo (il padre) + 1 in attesa |

## Conto economico

| | |
|---|---|
| Pattuito | **2.400 €** |
| Incassato | **400 €** (al 2026-08-28) |
| **Credito aperto** | **2.000 €** |
| I 400 € presi | **Nessuna ricevuta emessa** — accordo fra privati |
| I 2.000 € da incassare | Ricevuta per prestazione occasionale su **Patrick** → [[vincoli-fiscali]] |

## Come si comporta

Osservato dal lavoro di agosto 2026:

- **Muove lo scope in tutte e due le direzioni.** Ha tolto Chat, Disponibilità,
  XML FatturaPA e area Direzione fra il 4 e il 5 agosto; ha rimesso
  Disponibilità il 20 e **richiesto l'XML SDI il 22** →
  [[2026-08-22-xml-sdi-da-quotare]]
- **Chiede funzioni nuove**, non presenti nell'app vecchia, dall'11 agosto
- **Collauda lui, e bene.** Tre liste di segnalazioni strutturate fra il 25 e il
  27 agosto, con foto delle schermate
- **Spiega il proprio mestiere per iscritto.** La regola dell'autista esterno
  ("l'esterno guida soltanto, è l'interno che guida *e* lavora") l'ha scritta
  lui per esteso: da quella riga sono caduti cinque punti su dieci di una lista

## Perché questo cliente è diverso dagli altri

> [!note] Analisi di Claude — 2026-08-28
> Sapere che Seba è un fondatore e non un'azienda cambia tre cose.
>
> **1. Il rischio di incasso è diverso da come sembrava.** I 2.000 € non
> arrivano dal budget IT di un'impresa avviata: arrivano da un privato che sta
> aprendo un'attività con **un cliente pagante, suo padre**. La sua capacità di
> pagare dipende dal fatto che il suo secondo cliente firmi. Non è un cattivo
> pagatore — è un rischio d'impresa che si eredita.
>
> **2. Il suo comportamento adesso ha senso.** Chi muove lo scope venti volte
> in un mese e collauda ogni consegna il giorno stesso non è un cliente
> pignolo: è un fondatore che sta scoprendo il proprio prodotto mentre lo fa
> costruire. Continuerà a farlo. La difesa non è irrigidirsi — è **quotare ogni
> aggiunta nel momento in cui la chiede**, che è già la regola scritta in
> [[2026-08-11-opero-scope-allargato]] e che nella pratica sta scivolando.
>
> **3. Vale più come partner che come commessa.** Se OperO gli funziona, ogni
> suo cliente nuovo è manutenzione ed evoluzione per DenkiCode — l'unico
> ricavo ricorrente che oggi avete davvero a portata, visto che
> [[denkishift]] è a zero clienti. Vale la pena chiedersi se i 2.400 € una
> tantum siano la forma giusta dell'accordo, o se abbia più senso una quota
> legata alle sue installazioni. **Da discutere con lui, non da decidere qui.**
>
> ⚠️ Attenzione al lessico se se ne parla: una quota ricorrente legata ai suoi
> ricavi è esattamente la forma che [[vincoli-fiscali]] dice di non
> formalizzare finché non c'è la P.IVA.

## Aperto

- [ ] Incassare i **2.000 €** — ricevuta su Patrick
- [ ] Quotare l'XML SDI prima di svilupparlo
- [ ] Correggere il PDF del piano sulle funzioni rinunciate
- [ ] `TODO` — come è arrivato a noi? Serve a [[generazione-lead]]
- [ ] `TODO` — nome dell'azienda del padre (è la prima installazione reale)
- [ ] **Secondo cliente di Seba: si saprà nella settimana del 31 agosto 2026.**
      È la cosa da cui dipende il nostro incasso — segnarlo qui appena si sa

## Collegamenti

[[opero]] · [[vincoli-fiscali]] · [[stile-comunicazione]] ·
[[2026-08-11-opero-scope-allargato]] · [[2026-08-22-xml-sdi-da-quotare]] ·
[[denkishift]]
