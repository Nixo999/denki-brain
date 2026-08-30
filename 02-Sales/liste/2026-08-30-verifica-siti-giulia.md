---
type: area
updated: 2026-08-30
source: claude
prodotto: siti
contatti: 33
stato: da-chiamare
---

# Verifica della lista siti di Giulia — 50 righe, una per una

Patrick il 30 agosto 2026: *«ho preso in mano la lista di Giulia e già il primo
era sbagliato, La Rustica ha un sito»*. Aveva ragione, e non era un caso
isolato.

## Il risultato in una riga

**Su 50 righe, 30 avevano la nota falsa.** La colonna diceva «Nessun sito su
Pagine Gialle» su aziende che un sito ce l'hanno, o ce l'avevano.

| Esito della verifica | Righe | Cosa se ne fa |
|---|---|---|
| ✅ **Nessun sito, confermato** | 20 | Restano, nota invariata |
| ⚠️ **Dominio morto, parcheggiato o su piattaforma** | 10 | Restano, ma **l'angolo cambia**: sono i lead migliori |
| 🔧 **Sito vivo ma vecchio** | 3 | Restano come **restyling**, non come «non avete un sito» |
| ❌ **Sito vivo e curato, o catena** | 17 | **Escono dalla lista** |

Lista corretta: `2026-08-30-siti-giulia-corretta.csv`, **33 righe**. Le 17 che
mancano ai 50 del [[ciclo-settimanale]] vanno rigenerate: vedi *Cosa manca*.

## Perché è successo

Il segnale della lista del 28 agosto era: *«la scheda Pagine Gialle non linka un
sito»*. Quella nota lo dichiarava già come limite, in *Cosa NON ho verificato*.
Il limite si è rivelato **il difetto centrale**: Pagine Gialle non elenca il sito
di chi non ha comprato la scheda a pagamento. **Assenza dalla scheda ≠ assenza
del sito.**

Il metodo nuovo è in [[2026-08-30-verifica-sito-reale]] e in [[metodo-liste]].

## Le 17 righe che escono

Hanno un sito vivo e curato: chiamarle con «non vi trovo su internet» brucia la
chiamata nei primi cinque secondi.

| # | Azienda | Cosa hanno davvero |
|---|---|---|
| 2 | La Sprelunga (Seveso) | `lasprelunga.it` — WordPress, copyright **2026**, menu e storia |
| 14 | Bottega Ristobar (Seveso) | `bottegaristobar.it` — WordPress, 9.2 su TheFork |
| 19 | I Morandi Parrucchiere Uomo (Meda) | `imorandi-meda.it` |
| 20 | I Morandi di Morandi Orlando (Meda) | **stessa attività della 19**: era anche un doppione |
| 26 | Bottega del Benessere (Cesano) | `bottegadelbenessere.net` + `bottegadelbenesseredieleonoraspano.com` |
| 27 | Bottega del Benessere - Molino Arese | **stessa titolare della 26**: doppione già segnalato |
| 30 | EpiLate (Cesano) | `epilate.it` — **catena** nazionale di epilazione laser |
| 31 | Pulsazione (Cesano) | `pulsazione.it` — «Pulsazione Italia», **rete**, non indipendente |
| 33 | Domus Arredi (Lissone) | `domusarredilissone.it` **+ altri due domini** |
| 34 | Formarredo Due (Lissone) | `cucinelissone.it` + `stosacucinelissone.it` |
| 35 | Viscardi Arreda (Lissone) | `viscardiarreda.it` |
| 36 | Meroni Arreda (Lissone) | `meroniarreda.it` |
| 37 | Tappezzeria dell'Orto (Lissone) | `tappezzeriadellorto.it` |
| 38 | Dassi Gino (Lissone) | `dassigino.it` |
| 39 | Maredivino (Desio) | `maredivino.it` |
| 42 | La Nostra (Desio) | `lanostratrattoria.it` |
| 50 | Scherma Desio (Desio) | `schermadesio.com` — aggiornato al 2026 |

> [!warning] I sei mobilifici di Lissone erano marcati **E-commerce**, non Vetrina
> Per loro il segnale «non ha sito» era **la domanda sbagliata**: ce l'hanno
> tutti e sei. Quella giusta è **«ha un sito ma non vende online»** — che è
> ancora un lead, ma si qualifica guardando se c'è un carrello, non se c'è un
> dominio. Da rifare con quel metro.

## I 10 lead diventati più forti

Qui la lista aveva torto **a favore nostro**: non è che manchi il sito, è che il
sito è rotto. Dirlo al telefono non è una proposta commerciale, è una notizia —
ed è il pattern interrupt più forte che abbiamo in mano.

| Azienda | Cosa succede davvero |
|---|---|
| **Officina della Pizza** (Lissone) | Il dominio è scaduto e oggi ospita un **casinò online** |
| **Pizzeria del Corso** (Seveso) | `pizzeriadelcorso.it` **reindirizza a JustEat**: il loro nome porta traffico a chi prende la commissione |
| Moxi Sushi (Seveso) | Aveva un e-commerce OpenCart: dominio spento |
| Vecchia Brianza (Seveso) | Hotel+ristorante, dominio spento: le camere passano dai portali |
| Burnout Pub (Seveso) | `burnoutpub.com` spento, ma le schede lo indicano ancora |
| Bistrot 59 (Seveso) | Dominio vivo, **pagina vuota da 436 byte** |
| Il Tramonto (Desio) | Dominio spento, resta una pagina `eatbu` |
| Pasnu (Lissone) | Sito Wix su sottodominio gratuito, oggi **404** |
| Pizza Express (Lissone) | Dominio scaduto |
| Dai Rosky (Lissone) | Nessun dominio, solo pagina `xmenu` |

## La lezione che cambia le liste future

**Il segmento decide più del comune.** Contando le verifiche:

| Segmento | Ha un sito | Non ce l'ha |
|---|---|---|
| **Parrucchieri ed estetiste** | 2 su 14 | **12 su 14** |
| Ristoranti, bar, pizzerie | ~11 su 22 | ~11 su 22 |
| **Mobilifici e arredamento** | **6 su 6** | 0 |

Per la lista siti si parte dal **wellness**, non dalla ristorazione: stesso
lavoro di ricerca, il doppio di righe buone. I mobilifici in lista siti non ci
vanno affatto.

## Cosa manca

- ⬜ **17 righe di rimpiazzo** per tornare a 50. Vanno costruite sul wellness
  dei comuni non ancora battuti, con la verifica nuova.
- ⬜ **I sei mobilifici di Lissone** vanno riqualificati col metro
  «ha carrello / non ha carrello», non con quello del dominio.
- ⬜ Nessun numero è stato richiamato: le schede invecchiano comunque.

## Collegamenti

[[metodo-liste]] · [[2026-08-30-verifica-sito-reale]] · [[ciclo-settimanale]] ·
[[2026-08-28-liste-31-agosto]] · [[metriche]] · [[core-commerciale]]
