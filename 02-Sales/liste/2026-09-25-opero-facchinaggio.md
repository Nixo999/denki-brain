---
riga: 100 aziende di solo facchinaggio per Seba su OperO, da Seveso a Firenze (9,8-265 km), fatturato 250k-10M. 29 gia' nella lista mista. Piu' 149 senza numero.
type: area
updated: 2026-09-25
source: claude
verificato: 2026-09-25
prodotto: opero
cliente: sebastian-torres
contatti: 100
stato: da-consegnare
---

# Lista 2026-09-25 — OperO, solo facchinaggio

Chiesta il 25/09/2026 subito dopo [[2026-09-25-opero-facchinaggio-allestimento]]:
«100 aziende solo ed esclusivamente settore facchinaggio, con gli stessi limiti
di prima». Limiti tenuti: fatturato 250.000 €-10 M€, attiva, niente
liquidazione, telefono con la regola del 17/09, da Seveso verso fuori, fuori il
personale sotto 60.000 €, fuori BluNotte.

| File | Righe | Cos'è |
|---|---|---|
| `2026-09-25-opero-facchinaggio.xlsx` | **100 + 149** | **quello che va a Seba.** Come la lista mista, senza colonna Settore; in più «Attività prevalente» e «Già nella lista del 25/09» |
| `…-facchinaggio.csv` | 100 | con P.IVA, link Pagine Gialle, livello di prova, colonna `gia_25_09` |
| `…-facchinaggio-senza-numero.csv` | 149 | facchinaggio in fascia entro 30 km, numero non trovato |
| `…-facchinaggio-anagrafica.json` | 1.110 + 297 | i due giri grezzi, gli scarti col motivo e le 106 tenute |

## Cosa vuol dire «esclusivamente»

Una riga entra se **tutte e due** le fonti dicono facchinaggio:

- **attività prevalente** `52.24.4` o `52.24` (movimentazione merci) **e** una
  categoria Pagine Gialle coerente: facchinaggio, cooperative di lavoro,
  consorzi, pulizie, magazzinaggio, selezione del personale;
- oppure **categoria Pagine Gialle «Facchinaggio»** e un'attività prevalente
  compatibile: logistica `52`, servizi integrati e pulizie `81`, imballaggio
  conto terzi `82.92`, servizi alle imprese `82.99`, lavoro `78`.

**Fuori, in più rispetto alla lista mista**: chi ha come attività prevalente il
trasporto merci su strada (`49.41`) anche se su Pagine Gialle si dichiara
facchinaggio: 12 scarti per attività fuori dal facchinaggio, fra cui Viganò
Musica. E i `52.24` che su Pagine Gialle sono «Autotrasporti», «Trasporti» o
«Traslochi» (12). Restano due società col nome
«Traslochi» e l'attività in movimentazione merci: si presentano come
facchinaggio.

## Perché si arriva a Firenze

Nel raggio della lista mista (55 km) il facchinaggio col numero verificato si
ferma a **35**. Per arrivare a 100 il raggio è salito a 265 km: 1.110 società
di movimentazione merci in fascia (Lombardia, Piemonte, Liguria, Emilia,
Veneto, Toscana del nord), 778 attive, **140 numeri**; più 297 schede
«Facchinaggio» di Pagine Gialle da 54 città, **94 abbinate** a un bilancio.
Dopo gli scarti ne restano 106: la centesima è a 265 km.

Distanze: 22 righe entro 30 km, 7 fra 30 e 50, 7 fra 50 e 100, 20 fra 100 e
150, **44 oltre 150**. Province: MI 17, VR 12, MO 7, BS 6, FI 6.

## ⚠️ Cosa NON è verificato

- **Il bacino vicino è nel foglio «Senza numero», non nelle 100.** Entro 30 km
  ci sono 149 società di facchinaggio in fascia senza un numero su Pagine
  Gialle, contro le 22 in lista. Chiamare Verona prima di Seregno è l'effetto
  della fonte. Il numero di quelle 149 va cercato sul sito, a mano.
- **Oltre i 220 km c'è solo il giro per codice ATECO**, non quello per
  categoria di Pagine Gialle: fra 220 e 265 km mancano le società che si
  dichiarano facchinaggio con un altro codice.
- **60 righe su 100 senza anno del bilancio**, quasi tutte cooperative: la
  scheda companyreports non ha il bilancio, il fatturato viene solo dalla
  classifica per codice. Nel file è «n.d.».
- Referente assente, numeri mai chiamati, distanze in linea d'aria: come nella
  lista mista.

## Aperto

- [ ] `TODO` — le stesse due domande della lista mista: a pagamento o no, e chi
  chiama.

## Collegamenti

[[2026-09-25-opero-facchinaggio-allestimento]] · [[sebastian-torres]] ·
[[opero]] · [[metodo-liste]] · [[metriche]]
