---
riga: 100 aziende di facchinaggio e allestimento per le chiamate di Seba su OperO, da Seveso verso fuori (0,8-55 km), fatturato 250k-10M. Piu' 213 senza numero.
type: area
updated: 2026-09-25
source: claude
verificato: 2026-09-25
prodotto: opero
cliente: sebastian-torres
contatti: 100
stato: da-consegnare
---

# Lista 2026-09-25 — OperO, facchinaggio e allestimento

Chiesta il 24/09/2026 in sessione `/nicola`: 100 contatti telefonici per
[[sebastian-torres]], «come quello dei gestionali» ([[2026-09-17-brianza-gestionali-1m]]),
partendo da Seveso e allontanandosi. Il brief di Seba: fatturato fra 250.000 € e
10 M€, solo «Facchinaggio · Allestimento, senza allargare la comunicazione
commerciale ad altri settori».

| File | Righe | Cos'è |
|---|---|---|
| `2026-09-25-opero-facchinaggio-allestimento.xlsx` | **100 + 213** | **quello che va a Seba.** Fogli: come si usa, da chiamare, senza numero, com'è fatta. Esito a tendina coi sei valori di [[metriche]] |
| `…-allestimento.csv` | 100 | le stesse righe con P.IVA, indirizzo legale, link Pagine Gialle e livello di prova |
| `…-senza-numero.csv` | 213 | settore e fascia giusti entro 30 km, numero non trovato |
| `2026-09-25-opero-anagrafica.json` | 1.588 | i due giri grezzi più gli scarti col motivo: da qui si rifà un altro taglio |

## Come è fatta — due giri, perché uno solo non bastava

1. **ATECO → telefono.** Liste nazionali di companyreports per codice, dal
   fatturato più alto a 250k: `52.24.4` e `52.24` (il codice ATECO 2025) per il
   facchinaggio, `77.39.94` e `90.02.01` per il noleggio di strutture per
   manifestazioni, `82.3`, `90.02.09` e `16.23.21` solo se su Pagine Gialle si
   dichiarano «Eventi e manifestazioni - impianti ed attrezzature». 1.042 attive
   in nove province, **242 numeri** con la regola del 17/09 (nome identico e
   stesso comune).
2. **Pagine Gialle → bilancio.** Le 353 schede delle due categorie, raccolte da
   27 comuni attorno a Seveso, cercate nella lista companyreports del loro
   comune (Milano: 50.731 società sopra soglia, 1.100 pagine). **116
   abbinate.**

Poi il filtro, con il motivo scritto per ogni scarto nel JSON: categoria di
Pagine Gialle che smentisce il codice (176, quasi tutte agenzie di eventi in
`82.3`), fatturato fuori fascia (18), non attive o in liquidazione (9),
**costo del personale sotto 60.000 €** (10), attività prevalente fuori settore
(3), stesso centralino (1). **Blu Notte S.r.l. è fuori**: è il BluNotte di
Paolo, già nel giro di Seba ([[opero-intermediar-receive]]).

**Livelli di prova** sulle 100: nome identico e stesso comune 83; nome
identico con sede operativa in un altro comune entro 25 km dalla legale 10;
stesso nome tolto il titolare 4; nome in parte diverso ma stessa via 3.

## Com'è composta

34 facchinaggio, 66 allestimento. Distanze 0-10 km: 7, 10-20: 35, 20-30: 40,
30-50: 16, oltre: 2. **Milano città 29 righe**, provincia MI 64, BG 16. Fatturato
mediano 1,6 M€; 28 righe con costo del personale da 500.000 € in su.

## ⚠️ Cosa NON è verificato

- **Il referente non c'è per nessuna**, come il 17/09. Si chiede al centralino.
- **Nessun numero è stato chiamato.**
- **Il facchinaggio è sottorappresentato, e il motivo è la fonte, non il
  mercato.** Le cooperative di facchinaggio quasi non stanno su Pagine Gialle
  col nome del bilancio: entro 30 km ce ne sono **149 senza numero** contro 34
  in lista. Il bacino vero è il foglio «Senza numero», e lì il numero va
  cercato sul sito, a mano. Ricerca fallita non è ricerca negativa
  ([[metodo-liste]]).
- **«Allestimento» comprende anche il service tecnico** (audio, luci,
  tensostrutture a noleggio). Se Seba intende solo stand e fiere, si filtra
  sulla colonna «Cosa fanno».
- **Due soglie sono mie, non di Seba**: personale sotto 60.000 € fuori (chi
  non ha squadra non ha il problema di OperO) e l'esclusione per attività
  prevalente fuori settore. Scelte dichiarate, da confermare.
- **Distanze in linea d'aria** sull'indirizzo di Pagine Gialle; 14 righe sul
  centro del comune perché l'indirizzo non si trovava. 14 righe senza anno di
  bilancio.

## Aperto

- [ ] `TODO` — **la lista per Seba è lavoro in più.** A pagamento o dentro il
  rapporto OperO? Nessuno l'ha deciso, e i 2.000 € non sono entrati ([[opero]])
- [ ] `TODO` — chi chiama: Seba, o Giulia per conto suo?

Gli script stanno in `01-Coding/strumenti/liste-bilanci/`, questa volta salvati:
il 17/09 erano andati persi con la sessione.

## Collegamenti

[[sebastian-torres]] · [[opero]] · [[metodo-liste]] · [[metriche]] ·
[[2026-09-17-brianza-gestionali-1m]] · [[opero-intermediar-receive]] ·
[[2026-09-25-opero-facchinaggio]] (la versione solo facchinaggio)
