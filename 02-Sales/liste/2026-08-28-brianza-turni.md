---
type: area
updated: 2026-08-28
source: claude
prodotto: denkishift
contatti: 51
stato: da-chiamare
---

# Lista 2026-08-28 — Brianza, DenkiShift

Prima lista operativa. File: `2026-08-28-brianza-turni.csv`, **51 contatti**,
pronto da importare in Google Sheets.

⚠️ **Convertita allo schema a 8 colonne il 28 agosto 2026** ([[ciclo-settimanale]]).
Il contenuto non è cambiato: `Comune` è finito dentro `Nome Azienda`, `Segnale` e
`Note` si sono fuse in `Note Strategiche`, e le colonne di tracking sono
diventate l'unica colonna di Giulia. È la **lista DenkiShift** della settimana
del 31 agosto → [[2026-08-28-liste-31-agosto]].

Costruita secondo [[metodo-liste]]. Da chiamare con
[[script-denkishift]] e negli orari indicati là.

## Cosa c'è dentro

| Blocco | Righe | Priorità |
|---|---|---|
| **RSA e case di riposo** | 25 | 🔴 Prima — H24, organici grandi, dolore massimo |
| **Cooperative sociali e assistenza domiciliare** | 7 | 🔴 Prima — personale sparso su orari diversi |
| **Imprese di pulizie con numero fisso** | 8 | 🟡 Poi — struttura organizzata |
| **Imprese di pulizie solo cellulare** | 11 | ⚪ Ultime — spesso sotto le 8 persone |

Comuni coperti: Desio, Seregno, Meda, Cesano Maderno, Lentate sul Seveso,
Barlassina, Seveso, Giussano, Lissone, Limbiate, Lazzate, Nova Milanese,
Muggiò, Carate, Verano, Bovisio Masciago, Albiate. Sei righe sono fuori zona e
segnate come tali.

## Le tre righe da chiamare per prime

1. **Rsa Don Emilio Meani** (Cesano Maderno) — 90 posti letto su **6 nuclei da
   15**. Sei squadre da incastrare ogni settimana: è il profilo di dolore più
   alto di tutta la lista.
2. **Punto Service Cooperativa Sociale** (Meda + Desio) — la stessa cooperativa
   su più sedi. Un solo sì entra su tutte.
3. **Adomicilio** (Giussano, Carate, Brugherio) — assistenza **a domicilio**:
   personale che ogni giorno va in un posto diverso a un'ora diversa. È il caso
   che a mano non si pianifica, si sopporta.

## Il filtro del numero di telefono

> [!note] Analisi di Claude — 2026-08-28
> Nelle imprese di pulizie ho separato **numero fisso** da **solo cellulare**.
> Non è pedanteria: un'impresa con centralino ha quasi sempre una struttura e
> un organico; una raggiungibile solo al cellulare è spesso il titolare che
> pulisce di persona con due collaboratori — sotto la soglia delle 8 persone
> di [[metodo-liste]], quindi non è un cliente.
>
> Le ho lasciate in fondo invece di buttarle: costano trenta secondi di
> qualifica a testa, e in paese (M.S. Service sta a Seveso) valgono comunque
> come contatto per il porta-a-porta di Patrick.

## ⚠️ Cosa NON ho verificato

Dichiarato invece che sottinteso, come si fa nei repo:

- **I numeri di telefono vengono da elenchi pubblici** (Pagine Gialle e simili).
  Non li ho chiamati: qualcuno sarà cambiato. Il primo squillo è la verifica.
- **Non ho verificato gli orari di apertura** di nessuna struttura. La colonna
  `Segnale` è compilata **per logica di segmento** — una RSA è H24 per
  definizione, un'impresa di pulizie ha squadre su più cantieri — non per
  osservazione diretta su Google Maps come prescrive [[metodo-liste]].
- **Non ho verificato il numero di dipendenti** di nessuno, tranne dove la fonte
  lo dichiarava (Don Meani: 90 posti letto; Don Orione: 69 ospiti). La soglia
  delle 8 persone va confermata al telefono, con la domanda che è già nello
  script.
- **Due righe di Seregno potrebbero essere la stessa realtà**: `Centro Don
  Gnocchi` e `Rsa Ronzoni Villa` risultano allo stesso indirizzo, Viale Piave 12.
  Se al telefono risponde lo stesso centralino, si cancella una riga.
- **Piccolo Cottolengo Don Orione (Seregno)** è in lista **senza numero**: la
  fonte non lo riportava. 69 ospiti di cui 20 con Alzheimer, assistenza 24 ore —
  vale la pena cercarlo su `orioneseregno.it`.

## Dopo il primo giro

I risultati si scrivono **nel foglio**, non qui. Poi si aggiornano
[[metriche]] e il registro delle prove in [[script-denkishift]].

La domanda a cui questa lista deve rispondere non è "quanti appuntamenti" ma
**quale dei tre blocchi risponde meglio**. Se le RSA convertono e le pulizie no,
la lista della settimana dopo è tutta RSA sui comuni accanto.

## Collegamenti

[[metodo-liste]] · [[script-denkishift]] · [[generazione-lead]] ·
[[denkishift]] · [[metriche]] · [[materiale-offline]]
