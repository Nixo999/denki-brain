---
type: daily
data: 2026-09-05
updated: 2026-09-05
source: claude
progetti: []
canali: [instagram]
---

# 2026-09-05 — I 65 DM di oggi, sul banco

Un blocco solo, chiesto da Patrick: **«crea i 65 dm di oggi in banco dm»**.
Lista in [[2026-09-05-instagram-bg-va]], pubblicata su `lista-corrente.csv`.

## Cosa c'è sul banco adesso

**145 righe: 68 da mandare, 75 in attesa di recupero.** Le 65 nuove sono state
**aggiunte in coda**, non hanno sostituito il file: se il CSV venisse
riscritto da zero, le 75 righe partite il 3 settembre perderebbero la data e il
recupero automatico di **mercoledì 9** non si accenderebbe più. Le altre 3 da
mandare sono quelle del 2 settembre rimaste ferme.

Il messaggio è già scritto riga per riga dentro la colonna `Messaggio`, in
versione C: sul banco non compare il campo «manca:» e Patrick non incolla
niente a mano.

## Le righe

Anello 2, **34 BG · 30 VA · 1 CO**, ventuno comuni, niente Monza Brianza né
Milano. Treviglio, che il 3 settembre era «il posto da cui ripartire», è
**finita**: sette ricerche su sette hanno ripescato profili già contattati e ne
è uscito un barbiere solo. Il pescato vero è Bergamo città, Dalmine, Seriate,
Romano di Lombardia, e sul lato varesino Gallarate, Busto Arsizio, Cassano
Magnago, Sesto Calende.

**Sette domini morti su 65** (quattro su 33 il 3 settembre): la resa del gancio
più forte tiene. Più due siti rotti in modo diverso — uno risponde «Database
Error», uno è una pagina vuota di 3,6 KB con dentro solo Google Tag Manager — e
una vecchia pagina Google Business che dà 404.

## Le tre cose da tenere

- **Il dedup si fa sul file finito, non sui candidati.** Tredici righe su 65
  erano già state contattate e me ne sono accorto solo al momento di
  pubblicare: i profili trovati *durante* la verifica non passano dal filtro
  fatto all'inizio. Quattro di quei tredici avevano ricevuto il messaggio due
  giorni prima. Il controllo è ora il **passo 4** di [[metodo-instagram]], con
  lo script che gira in dieci secondi, e va contro **tutte** le liste: tre su
  quattro hanno gli handle solo dentro le tabelle Markdown, non nei CSV.
- **`inkfactorybergamo.com` è cambiato di mano.** Non è in questa lista — è
  stato contattato il 3 settembre — ma oggi il dominio redirige a `to388.me`,
  un sito di scommesse, e le pagine `/lo-staff` e `/chi-siamo` sono ancora
  nell'indice di Google. Al recupero di mercoledì non gli si scrive «ha
  lasciato perdere l'idea di avere un sito»: gli si scrive dove porta oggi il
  suo indirizzo.
- **Uno scarto vecchio può tornare buono in cinque giorni.** `@la_charmerie`
  (Gallarate) era stata messa fuori il 31 agosto come «sito vero, vivo e
  aggiornato». Oggi `lacharmerie.it` **e** `lacharmerie.com` sono tutti e due
  senza DNS, con cinque pagine interne ancora nell'indice. Chi è stato scartato
  e mai contattato vale la pena riguardarlo, non è bruciato.

## Quello che resta aperto

- **`Esito DM` è ancora vuoto su tutte le 75 righe del 3 settembre.** Era il
  passo che la nota del 3 indicava come prossimo e non è stato fatto: senza
  quella colonna il giro 3 non si può misurare, e le tre domande di
  [[dm-instagram-vetrina]] restano `TODO`.
- **I follower mancano su 50 righe su 65.** Instagram non si apre da nessuna
  delle nostre macchine: dove non li ho letti c'è scritto `n.d.`, non un numero
  inventato.

## Collegamenti

[[2026-09-05-instagram-bg-va]] · [[metodo-instagram]] ·
[[dm-instagram-vetrina]] · [[2026-09-03-tetto-dm-65]] ·
[[2026-09-03-bozza-gia-fatta]] · [[2026-09-03-instagram-anello-1-2]] ·
[[metriche]] · [[generazione-lead]]
