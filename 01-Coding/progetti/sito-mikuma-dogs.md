---
type: progetto
riga: Bozza attesa da Martina Carneli (mikuma.dogs), istruttrice cinofila a Como - acqua scartata dopo tre giri, giro 4 sull'attrezzatura.
status: attivo
client: mikuma-dogs
stack: html-css-js
started: 2026-09-11
deadline:
updated: 2026-09-11
source: claude
verificato: 2026-09-11
tags: [sito, bozza, cinofilia, como, water-games]
---

# Sito Mikuma Dogs — bozza attesa

Chiesto da Nicola l'11 settembre 2026, all'una di notte, con lo screenshot del
profilo: «nuovo sito, con la tecnica nuova, basato su questo profilo Instagram».
**Le è già stato scritto e la bozza la aspetta** (Nicola, 11 settembre): non è
un'esca fredda, è materiale che verrà mostrato. `TODO` — scheda cliente in
`02-Sales/clienti/`: chi ha scritto, quando e cosa si è detto non li so.

**Nessun indirizzo sul sito.** Deciso da Nicola l'11 settembre: si scrive che
lavora a Como e basta. Niente sezione «dove», niente mappa.

## Chi è, verificato dal profilo l'11 settembre 2026

**Martina Carneli**, `@mikuma.dogs`, 1.718 follower e 1.752 seguiti. Bio intera,
sue parole:

```
Martina Carneli • Istruttrice Cinofila • Como
🐾 Istruttrice cinofila CSEN e ACSI
🏅 Obedience e obbedienza sportiva
💧 Istruttrice Water Games CIS
💻 Consulenze cinofile online
🐺 @kuma_kratosgodofwar
```

Nessun link in bio: **non ha un sito**. Storie in evidenza: STUDENTI, FEEDBACK,
KUMA, RANDOM, DOGSITTING, TRASFERTE, FRIDA, ADOLESCEMENZA, 88 nonna, Sis.

Il cane è **Kuma**, pastore olandese tigrato, nero brindle, nei reel anche
«Kumino». Altri cani che compaiono col nome sui cartelli: Mirtilla, Iris & Hoty.

## Cosa fotografa

Metà del feed è **acqua**: lago (sponde del Lario), piscina, giubbotti da
salvataggio rossi, il ring tug viola, cani che imparano a galleggiare. L'altra
metà è terra: boschi d'autunno, sentieri, vette, il muso di Kuma sull'obiettivo.
Un solo scatto in bianco e nero, lei accovacciata col cane nel prato: è il
migliore che ha.

**Il suo linguaggio grafico è il cartello del reel**: fascia crema in basso,
titolo condensato tutto maiuscolo, prima riga arancione e seconda nera. Sempre
uguale, su ogni copertina. «LA TAGLIA PICCOLA È GESTIBILE», «KUMA VS NUOTO»,
«Mirtilla impara a nuotare!», «Un giorno da HYDRODOG», «PASTORE TEDESCO vs
LABRADOR RETRIEVER», «Un cane da lavoro nella QUOTIDIANITÀ».

Colori campionati dal logo, pixel per pixel: arancione **`#EB6F1F`**, nero
`#000000`, bianco `#FFFFFF`. Il logo è uno yin-yang di due teste di cane, una
nera e una bianca, col wordmark `MIKUMA.DOGS` sotto.

## Cosa NON c'è, e non si inventa

Nessun prezzo, nessun orario, nessun indirizzo, nessun telefono, nessuna mail,
nessuna recensione leggibile (l'evidenza FEEDBACK vuole il login). Le caption non
si leggono: `og:title` vuoto su 11 post su 12, verificato con `curl`. Il campo
dove lavora non è mai nominato: c'è scritto solo **Como**.

L'unico canale di contatto verificato è il DM di Instagram.

## La metafora — l'attrezzatura (dal giro 4)

**Prima di lavorare si allaccia qualcosa.** Il giubbotto di salvataggio rosso
con le cinghie e le fibbie, la pettorina, il collare giallo: stanno in metà
delle sue foto. Il sito è costruito come un'attrezzatura: nastri piatti che
reggono le sezioni, cuciture tratteggiate, le certificazioni come etichette
cucite, una fibbia sola. L'apertura è la cinghia che si tende e la fibbia che
scatta. **Niente natura simulata**: l'acqua esiste solo dentro le foto.

**Scartata: la linea dell'acqua** (giri 1-3). «Un cane che entra in acqua è un
cane che si fida» resta vero come frase, ma resa in CSS l'acqua è uscita a
righe nel giro 1 e a nebbia nel giro 3. Nicola, 2:4x dell'11: «l'acqua sembra
finta, eliminala; inventati qualcos'altro, ma non stare a provare a generare
acqua finta, che non viene bene». Trappola da scrivere: la natura simulata in
CSS non regge il confronto con una foto vera nella stessa pagina.

## Le foto scaricate

Undici anteprime a 640 px in `assets/img/`, scaricate l'11 settembre: gli URL
Instagram scadono. **A 640 px non reggono a tutta larghezza**: si usano in
cornice, mai fondo pagina. Le copertine dei reel sono 360×640, verticali.

## Come è venuto — due giri, 11 settembre

Impeccable seed **`ee8ad76c`**, indice assegnato **5**, una sola famiglia di
caratteri (Archivo su due larghezze dell'asse `wdth`). Sei sezioni: apertura,
chi ti allena, cosa faccio, la linea dell'acqua, e poi la terra, si parte da un
DM. Il **cartello del reel è diventato il titolo di sezione**, e le foto sono
state ritagliate per togliere la fascia impressa: senza quel taglio il sito
sembra uno screenshot di Instagram.

Motion: l'apertura è la linea che scende e scopre il titolo; la luce dell'acqua
viene dall'ora di chi guarda; la superficie si increspa in loop; il momento
autoriale è uno solo, il ritratto tagliato dalla linea di galleggiamento che
sale con lo scroll finché il cane è dentro.

**Giro 2**, chiesto dal direttore sulle catture vere: «e poi la terra» era due
foto e un buco nero alto quanto lo schermo, ricomposta su tre pannelli allineati
al bordo basso; la foto in vetta mostrava due persone in costume con le loro
cose sparse ed è uscita, resta il solo paesaggio; la colonna destra di «chi ti
allena» stava a 172px invece di 380, la traccia era `auto`.

Misurato: overflow 0 su diciotto larghezze da 320 a 1440, bordi delle media
query compresi; contrasti AA, con l'arancione del cartello abbassato a `#D25C0D`
solo lì; console pulita; pagina completa senza JS e in `?cattura`.

**Il copy in prima persona è nostro, non suo.** Sono fatti verificati, ma le
frasi le abbiamo scritte noi: se il sito diventa suo, glielo si fa rileggere.

## Bocciato, e il giro 3

Nicola, alle 2:2x dell'11, sul sito in locale: «fa veramente schifo, sembra
fatto da un bambino di due anni, rifallo. Vanno bene i colori e l'idea
dell'acqua, ma fatto davvero male». La falla è mia: ho giudicato sulle misure
(overflow, contrasti, console) e sulle catture spezzate, e ho fatto passare
un'acqua fatta di righe ripetute, foto in cornici da widget, un hero a due
colonne da template e tutto piccolo su un nero vuoto. Le misure dicono se una
cosa è rotta, non se è bella. Contromisura: il brief del giro 3 elenca le
sette cose sbagliate una per una, dà come metro `ngbarber-site` e
`fiftynine-site` che stanno sul Mac, e obbliga l'operatore a guardare le sue
catture sezione per sezione prima di riferire.

Giro 3 fermato due volte: prima per l'emersione, poi per l'acqua stessa.
⬜ Giro 4 in corso. ⬜ Netlify e repo remota: in attesa del via.
⬜ Safari su iPhone. ⬜ Scheda cliente in `02-Sales/clienti/`.

## Collegamenti

[[processo-siti]] · [[essenza-e-motion]] · [[trappole]] · [[registro-interventi]]
