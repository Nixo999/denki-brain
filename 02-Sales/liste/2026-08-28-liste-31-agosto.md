---
type: area
updated: 2026-08-28
source: claude
prodotto: multi
contatti: 131
stato: da-chiamare
---

# Liste della settimana del 31 agosto 2026

Primo giro completo del [[ciclo-settimanale]], generato con un giorno di
anticipo. **Quattro file**, tutti nello schema a 8 colonne tranne quello di
Patrick, che ha il suo.

| File | Righe | Chi chiama | Prodotto |
|---|---|---|---|
| `2026-08-28-siti.csv` | **50** | Giulia | A — Vetrina, B — E-commerce |
| `2026-08-28-brianza-turni.csv` | **51** | Giulia | C — DenkiShift |
| `2026-08-28-indagine.csv` | **30** | Giulia | D — form, non si vende |
| `2026-08-28-blitz-patrick.csv` | **10** | Patrick, a piedi | A e C |

**131 numeri, tutti diversi**: nessuno viene chiamato due volte fra una lista e
l'altra. È una riga sopra il dimensionamento di [[metriche]], che ne prevede
130.

## Da dove vengono

Tutte da **Pagine Gialle**, categoria per categoria e comune per comune — la
stessa fonte che usa Patrick a mano. Nome, telefono e indirizzo sono copiati
dalla scheda, non ricostruiti.

## Lista 1 — Siti web (50)

| Blocco | Righe | Comuni |
|---|---|---|
| Ristorazione | 19 | Seveso, Desio, Lissone |
| Parrucchieri e barbieri | 10 | Seveso, Meda |
| Centri estetici | 7 | Cesano Maderno |
| Arredamento | 6 | Lissone |
| Bar e caffetterie | 5 | Seveso |
| Sport e fitness | 3 | Desio |

**Il segnale è osservato, non dedotto.** Ogni riga è in lista perché la sua
scheda Pagine Gialle **non linka un sito** o linka **solo Facebook**. È la
differenza con la lista di turni, dove il segnale era ricavato per logica di
segmento.

I sei mobilifici di Lissone sono gli unici marcati **E-commerce** invece di
Vetrina: è il distretto del mobile e vendono solo in showroom. Lì la leva è la
vendita online, non la vetrina — e con la vendita online arrivano le royalty,
che senza P.IVA non si sanno ancora incassare → [[vincoli-fiscali]].

## Lista 2 — DenkiShift (51)

È la lista di [[2026-08-28-brianza-turni]], **convertita allo schema a 8
colonne**. Contenuto invariato: 20 RSA, 8 cooperative, 19 imprese di pulizie,
3 RSA in gestione cooperativa, 1 cooperativa di servizi.

> [!warning] Analisi di Claude — 2026-08-28
> **Il protocollo dice "ristoranti, bar, locali" per DenkiShift, questa lista
> dice RSA e pulizie.** Non è una svista: [[metodo-liste]] sostiene che il
> segmento ovvio — i locali — è il più debole, e che il dolore vero sta dove
> si lavora H24 con sostituzioni continue. La settimana del 31 agosto tiene la
> lista com'è, perché era già costruita e perché è quella che prova l'ipotesi.
> **Se le RSA non convertono, la settimana dopo si passa ai locali** e si vede
> chi aveva ragione. I ristoranti e i bar di questa settimana stanno nella
> lista siti, che è dove il loro problema si vede da fuori.

## Lista 3 — Indagine di mercato (30)

Aziende strutturate, dove il gestionale custom ha senso. Giulia **non vende**:
porta al form.

| Blocco | Righe | Comuni |
|---|---|---|
| Carrozzerie | 6 | Cesano Maderno |
| Carpenterie metalliche | 6 | Seregno |
| Officine e automotive | 5 | Desio |
| Logistica e trasporti | 5 | Lissone, Meda, Monza |
| Tipografie | 4 | Lissone |
| Imprese edili | 3 | Seregno |
| Serramenti | 1 | Meda |

Ogni riga ha in `Note Strategiche` **la domanda da fare**, non una descrizione:
«dove segnate a che punto è ogni commessa», «come sapete a fine mese quanto è
costato il cantiere». Il form si compila da solo se la domanda tocca.

## Lista 4 — I 10 blitz di Patrick

**Tutti a Seveso tranne uno a Cesano Maderno**, e **tutti già dentro la lista
siti di Giulia**. È voluto: [[generazione-lead]] chiama questa cosa
*riscaldamento* — Patrick lascia il materiale, Giulia chiama entro 48 ore e non
apre più a freddo.

Sei sono aggancio sito, quattro sono aggancio turni. Il gancio d'ingresso di
ciascuno dice **cosa guardare prima di entrare**, non cosa dire: la frase esce
da quello che vedi.

Nella stessa uscita ci sono anche i **10 presìdi** di
[[2026-08-28-presidi-volantini]]: sono 20 fermate, ma di natura diversa — dal
blitz si esce con un appuntamento, dal presidio con 30 volantini appoggiati.

⚠️ Sui quattro DenkiShift la qualifica va fatta **sulla soglia**: sotto le 8
persone non è un cliente, ed è scritto nel gancio.

## Cosa NON ho verificato

- **«Nessun sito» significa «la scheda Pagine Gialle non ne linka uno».** Non è
  la stessa cosa di «non ce l'hanno». La verifica è la prima domanda di Giulia,
  e se ce l'hanno la riga diventa comunque un lead: un sito che il proprietario
  non ha nemmeno messo in scheda è un sito che non usa.
- **Nessun numero è stato chiamato.** Le schede di Pagine Gialle invecchiano.
- **Nessun organico verificato.** La soglia delle 8 persone di [[metodo-liste]]
  si conferma al telefono, sempre.
- **Nessun sito guardato davvero.** Non ho aperto le pagine delle attività per
  vedere com'è fatto il sito di chi ce l'ha: l'angolo «il vostro sito è vecchio»
  qui non si può usare, solo «non vi trovo».
- **`Bar della Stazione` e `Star S.r.l.`** risultano allo stesso indirizzo di
  Seveso (Piazza Mazzini 11). Ne ho tenuto in lista uno solo, ma il dubbio resta.
- **Le due `Bottega del Benessere` di Cesano** sono la stessa titolare su due
  sedi: sono due righe, ma è **una telefonata sola**, a Eleonora Spanò.

## Dopo il primo giro

La domanda a cui questa settimana deve rispondere è **quale delle tre liste
converte**, non quanti appuntamenti escono. Gli esiti tornano nei file, il
report di Patrick nel modulo Word, e la domenica si rigenera →
[[template-report-settimanale]].

## Collegamenti

[[ciclo-settimanale]] · [[metodo-liste]] · [[2026-08-28-brianza-turni]] ·
[[script-giulia-denkishift]] · [[pattern-interrupt]] · [[metriche]] ·
[[materiale-offline]] · [[generazione-lead]]
