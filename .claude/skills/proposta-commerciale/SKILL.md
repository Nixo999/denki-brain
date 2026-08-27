---
name: proposta-commerciale
description: Genera preventivi e proposte commerciali DenkiCode - messaggio WhatsApp per i siti vetrina, PDF tipo "Piano di Sviluppo" per i gestionali. Da usare quando serve quotare un lavoro, scrivere un preventivo o formalizzare un accordo con un cliente.
---

# Proposte commerciali DenkiCode

## Prima di scrivere

Leggi:

1. `03-Resources/prodotti-e-listino.md` — prezzi e cosa comprende ogni prodotto
2. `02-Areas/business/vincoli-fiscali.md` — **il lessico è vincolante**
3. `03-Resources/stile-comunicazione.md` — la voce è quella di Patrick

## Due formati, non uno

### Siti vetrina ed e-commerce → messaggio, non documento

Un riepilogo su WhatsApp o email. **Niente PDF**: la leggerezza è parte
dell'offerta "cassa rapida". Struttura:

```
Cosa facciamo          3-5 righe, concrete. Le pagine, non "la presenza digitale"
Cosa serve da te       testi, foto, logo — e quando
Tempi                  giorni, non settimane vaghe
Quanto                 cifra + cosa comprende la quota annuale
Come si parte          acconto e ricevuta
```

### Gestionali → PDF impaginato

Formato di riferimento: il *"Piano di Sviluppo e Migrazione Software"* già
consegnato al cliente di [[opero]]. Struttura:

```
1. Cosa abbiamo capito del vostro lavoro   ← la parte che vende. Dimostra ascolto
2. Cosa costruiamo                          elenco puntuale delle funzioni
3. Cosa NON è compreso                      ← esplicito, sempre
4. Fasi e tempi                             con le date
5. Investimento                             cifra, acconto, saldo
6. Come lavoriamo                           consegne frequenti, si prova insieme
```

## La sezione 3 non si salta mai

⚠️ **"Cosa NON è compreso" è la sezione più importante del documento.**

Su [[opero]] è successo l'opposto: il piano consegnato prometteva funzioni poi
tolte dallo scope, il documento non è mai stato corretto, e al go-live quelle
voci risulteranno **mancanti anziché rinunciate**. Vedi
`05-Decisioni/2026-08-11-opero-scope-allargato.md`.

Regola che ne discende, da scrivere nel documento stesso:

> Ogni funzione non elencata qui è lavoro nuovo: viene quotata a parte e sposta
> la data di consegna.

## Lessico obbligatorio

| ✅ | ❌ |
|---|---|
| ricevuta | fattura, fattura elettronica |
| collaborazione occasionale / promozionale | fornitura, contratto continuativo |
| quota annuale | canone mensile addebitato |
| acconto | anticipo su fattura |

## Prezzi

Quelli in `prodotti-e-listino.md` sono **indicativi**. Prima di scrivere una
cifra, chiedi cosa ha chiesto il cliente: l'aggancio a 200-300 € vale sulla
bozza standard, non su un lavoro su misura.

Riferimento reale per un gestionale custom: **2.400 €** ([[opero]]).

## Sempre

- Voce di **Patrick**, mai di Nicola
- Tono diretto, niente fuffa, niente superlativi
- Cifre e date esplicite: se non si sanno, si chiedono prima di scrivere
- Il documento generato va salvato con `source: claude` finché Patrick non lo
  ha riletto
