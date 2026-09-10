---
type: area
updated: 2026-09-10
source: claude
prodotto: [siti-vetrina, denkishift]
canale: instagram
anello: 1-2
stato: pubblicata
---

# Liste Instagram del 10 settembre 2026 — 50 siti e 30 DenkiShift, un messaggio per ognuno

**Due liste**, come chiesto da Patrick in
[[2026-09-10-liste-50-30-messaggi-personalizzati]]. Tutte e due per il suo
account, appese a `lista-corrente.csv` con la colonna `Lista`: sul banco stanno
in due sezioni, «Siti vetrina» e «DenkiShift, i turni».

| Lista | File | Righe |
|---|---|---|
| Siti | `2026-09-10-instagram-siti-va-co-lc-bg.csv` | **50** |
| DenkiShift | `2026-09-10-instagram-denkishift-va-co-lc-bg.csv` | **30** |

## La lista siti: 50 righe da 230 profili aperti

Settore scelto: **bellezza**, il segmento che il vault dà per il migliore dal
31 agosto (12 su 14 senza sito, [[metodo-instagram]]), sui comuni che le
liste di inizio settembre non avevano toccato: Saronno, Cantù, Luino, Merate,
Oggiono, Gavirate, Tradate, Somma, Cassano Magnago, Castiglione Olona,
Busto, Gallarate, Varese, Como, Erba, Seriate, Osio Sotto, Bergamo,
Treviglio. Dentro: 23 fra onicotecniche e nail center, 14 centri estetici,
10 parrucchieri, 2 barbieri, e **una riga sonda** di un settore mai provato,
gli artigiani della casa (CG Decor, imbianchino e cartongessista).

| Provincia | Righe |
|---|---|
| Varese | 30 |
| Como | 9 |
| Lecco | 5 |
| Bergamo | 6 |

**Ogni riga è passata da quattro controlli**: il profilo letto per intero
(follower, bio, indirizzo, link), una ricerca a mano per nome e comune,
`verifica-sito.py` con i motori e i domini indovinati, e per i domini vivi
`esamina-sito.py`, che dice com'è fatto il sito. Si scrive solo a chi non ha
un sito, o ne ha uno che non è suo (Wix, Linktree, Unobooking, la vetrina di
un fornitore) o che è morto.

| Gancio | Righe | Cosa c'è dietro |
|---|---|---|
| 1 nessun sito | 42 | nelle ricerche solo Fresha, Treatwell, Pagine Gialle e le schede degli altri |
| 5 piattaforma | 6 | MissDarling (Wix), Valentina Cauli (Linktree), Verde Salvia (Unobooking), Bio Estetica (vetrina Comfort Zone), Barber Shop Gold 2 (barbierefacile), più i casi in scheda |
| 2 dominio morto | 2 | DeiPregi (`deipregy.com`) e Solestetica (`solesteticaluino.it`): domini che compaiono ancora nelle schede e non aprono più |

Cosa ha scartato la lettura: **48 profili col sito** (fra cui Poppy, Ornizoo,
HER Cantù, Matrioska, BS Hair, Simo e Cami, Eccentrica Nails, Noire Elite,
Momento Hair, Perfect Nails, V-TOP, Incomincia da te), **28 troppo piccoli o
vuoti** (sotto i 200 follower, meno di 10 post, «agenda chiusa»), **9
privati o morti**, **14 già nel vault** (contattati nelle liste di inizio
settembre: Vibes, Aura, Barber Zone, Nice Nails, Vola, Beauty Lab, Atelier
dell'Estetica, Crisalide, Primaclasse, Magic Nails, Namaste, Lotus Noir,
Eos, Shine Lab, Bes Hair, Feelgold, Couture, Simona…), **7 fuori zona**
(Senigallia, Padova, Brasile, Bekasi), **3 catene** (Josef Barber, Compagnia
della Bellezza, Prior).

## La lista DenkiShift: 30 righe da 52 profili aperti

Criterio diverso: non «senza sito» ma **con una squadra a turni, da 8 a 50
persone, indipendente**. Chi ha un sito curato qui è un candidato migliore,
non peggiore. Sono usciti così:

- **6 alberghi** del lago di Como e del Maggiore: De Charme Laveno (30
  suite, spa), Camin Luino (ristorante gourmet), Du Lac Bellagio (bistrot,
  fine dining, rooftop), Asnigo, Belvedere, Centrale.
- **20 ristoranti e pizzerie** con squadra: Villa Cocca (7/7, 11-24, eventi,
  piscina), Autentiko (due sedi), Tarantola (dal 1969, wedding), Da Pietro
  (dal 1955, piazza Duomo), Tabula Rosa (due sedi, nuova apertura), Maistà
  (due sedi), Mòrso (13 servizi a settimana), Harry's Bar (aperto tutto
  l'anno dal 2026), San Vigilio, Gattopardo, Onda, e gli altri.
- **2 palestre** (Gymnasium Lecco 7-22.30, New Way Varese con piscina e
  crossfit) e **2 pasticcerie** (Capriccio dal 1984, Dolci di Bea 7/7).

Quattordici di questi erano gli **scartati per sito vivo** delle liste
ristorazione dell'8 e 9 settembre: mai contattati, ed è esattamente il
motivo per cui il sito ce l'hanno. Le due liste si alimentano a vicenda.

**Cosa non è stato verificato**: il numero esatto di dipendenti. È una
stima da camere, sale e orari (scritta in colonna, riga per riga); la
conferma è la prima domanda della demo. Grand Hotel Menaggio (forse sopra
i 50), Hotel Internazionale e La Stadera (forse sotto gli 8) sono rimasti
fuori per questo.

## Il messaggio: uno per riga

Nessun modello con un buco. Ogni testo dice chi è Patrick, **cosa ha visto
di quel profilo** (le sei colleghe di GLAM, la Stanza Quantica di Samsara,
la manicure curativa di Debora, i tredici servizi di Mòrso), **il fatto
verificato**, cosa propone, e una domanda sola. Passati tutti da
`voce-check.py` e riletti: frasi corte e irregolari, niente em dash, niente
«quindi», niente elenchi di tre, niente «soluzione». Tu o Lei a seconda
del tono del profilo: alle onicotecniche che si presentano col nome si dà del
tu, ai centri e agli alberghi del Lei.

La promessa è cambiata: **non «la bozza è già pronta»** ma «le preparo una
prima schermata con le sue foto e gliela mando qui». È quello che chiedeva
[[2026-09-08-test-dm-chiuso]], e si mantiene con una schermata, non con un
sito. Per DenkiShift la richiesta è dieci minuti in videochiamata, nessuna
data, nessun prezzo al mese: [[dm-instagram-denkishift]].

## Cosa ha reso

| Settore | Profili aperti | Col sito | Tenuti | Resa |
|---|---|---|---|---|
| Bellezza (nails, estetica, parrucchieri, barber) | ~220 | 48 | 49 | 22% |
| Artigiani casa (sonda) | 6 | 3 | 1 | 17% |
| Alberghi, per DenkiShift | 14 | tutti | 6 | 43% |
| Ristoranti con sito, per DenkiShift | 31 | tutti | 22 | 71% |

La bellezza resta il pozzo per i siti, ma il 22% dice che nei comuni grossi
è già stata pettinata: i profili buoni senza sito sono le onicotecniche e le
estetiste singole, non i saloni con la vetrina. Gli artigiani della casa
sono da riprovare con più righe prima di giudicare.

## Trappole

- **Il link con il nome del salone.** «Sillabi Nails & Beauty e altri 1»
  in bio era un sito (`studionailsestetica.com`, con il vecchio nome).
  «Incomincia da te Estetica di Chiara» pure. Il testo del link è un sito
  finché non si prova il contrario.
- **La vetrina del fornitore.** Bio Estetica ha `prodotticomfortzone.com`,
  L'Alchimia ha una pagina QR su `workingroupitalia.it`: sembrano siti, sono
  pagine che un marchio o un fornitore regala. Gancio 5, e va detto così.
- **Il profilo «generato dall'IA».** Instagram lo scrive su alcuni profili
  (Oda Beauty, Estetica dell'Anima, Kopi Club): non si sa cosa voglia dire,
  e i primi due sono rimasti fuori.
- **Il rebrand.** NEA di Mariano è l'ex «A due passi dal mare», che il sito
  ce l'ha ancora. Recute di Cantù è `parrucchiericantu.com`.
- **Il DNS del Mac.** Per tutta la mattina `verifica-sito.py` non risolveva
  nessun dominio e segnava tutto «morto»: la lista animali era passata con
  zero siti trovati, e riverificata ne ha trovati tre falsi positivi e
  nessun vero. Ora risolve con Cloudflare.

## Collegamenti

[[2026-09-10-liste-50-30-messaggi-personalizzati]] · [[metodo-instagram]] ·
[[dm-instagram-vetrina]] · [[dm-instagram-denkishift]] · [[voce-denkicode]] ·
[[2026-09-10-animali-va-co-lc-bg-ti]] · [[2026-09-09-ristorazione-va-co-lc-bg]] ·
[[generazione-lead]]
