---
type: progetto
riga: Online su mikumadogs.netlify.app per Martina Carneli (mikuma.dogs), Como - giro 7 'il bianco e il nero', logo vero, Nicola: 'mi piace molto'.
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

## Giro 4, la mattina dell'11 — l'attrezzatura

Seed impeccable **`7ded081f`**, indice 5 (la carta del Lario), sfidante
competitivo «busta da cartamodello» che ha dato la regola del rosso: un rosso
solo, `#F60B35` campionato dal giubbotto, sulla cucitura dell'etichetta Water
Games CIS. Sette nastri da 6-14 px, due cuciti con due filze ai bordi (una
filza sola al centro leggeva come `border: dashed`), **una fibbia** in linea
piatta dopo tre versioni scartate (connettore USB, scalino, busta da lettere).
Apertura: le due metà della cinghia si tendono in 500 ms, la fibbia scatta con
un fotogramma di sovraccorsa, il titolo si aggancia. GSAP tolto, zero JS
esterno. **Il dato vero non c'è, ed è dichiarato**: senza l'acqua l'ora del
visitatore non ha motivo, e un dato onesto non c'era.

Misurato: overflow 0 su 31 larghezze da 320 a 1600, 17 coppie AA, console
pulita, h1 su una riga da 761 in su, 35 rivelazioni entrate, stato finale
senza JS, in `?cattura` e con `reduced-motion`. Guardato dal direttore sulle
catture a 1440 e a 375: foto nude a ritmo, etichette cucite, nessun buco.
Non visto girare: l'apertura è letta via `getAnimations()`, mai a occhio.

✅ **Online su <https://mikumadogs.netlify.app>** dalle 9:4x dell'11 settembre,
via di Nicola («mettilo online con netlify»). Sito `mikumadogs`, team
`denkicode`, deploy dal CLI. Tre sbarramenti verificati con `curl`: `meta
robots`, `X-Robots-Tag`, `robots.txt`. CSS con `must-revalidate`.
✅ Repo `Nixo999/mikuma-site`, privata, `main`.
**Giro 5** (Nicola, 10:0x: «la frase su tre righe non può essere il titolo»):
l'h1 è **MIKUMA DOGS**, su una riga da 761 in su e impilato come nel logo sul
telefono; «Un cane che entra in acqua è un cane che si fida» scende a
sottotitolo, un sesto del corpo del nome. L'aggancio sul nastro resta. Trovato
per strada: il font di ripiego allargava il titolo del 19% e spostava
l'apertura di 193 px, corretto con `size-adjust`. Ripubblicato.
**Giro 6, il copy** (Nicola, 10:3x: «scrivi come un bambino, sembra che non
sai l'italiano; solo cose utili, niente frasi copiate dai suoi post»). Tutto il
testo riscritto dal direttore, frase per frase, e passato all'operatore da
inserire tale e quale: ogni frase con un verbo, ogni didascalia dice il
servizio o non c'è, il bottone diventa «Scrivimi su Instagram». Metro: NN/g
(conciso, scandibile, oggettivo). **Da far confermare a Martina** quando il
sito diventa suo: le descrizioni dei cinque servizi e la sequenza del lavoro
in acqua (primo contatto, giubbotto, nuoto, riporto) sono scritte da noi
sulla base della bio e delle foto, non dette da lei.
✅ Copy inserito e ripubblicato alle 10:5x: nessuna frase vecchia rimasta,
bottone «Scrivimi su Instagram» (in barra solo «Instagram» sotto i 480, dove
si sovrapponeva al marchio), `og:description` allineata alla meta description.

⬜ Safari su iPhone. ⬜ Il DM con il link è di Patrick. ⬜ Scheda cliente.
⬜ Safari su iPhone. ⬜ Scheda cliente in `02-Sales/clienti/`.

## Giro 7 — si riparte dal passo 2, col metodo nuovo

Nicola, 11 settembre: «usando il nuovo metodo per fare i siti creato oggi,
rimodifica il sito». Il mondo «attrezzatura» dei giri 4-6 e' **bocciato e
bruciato**: nastri, cuciture, etichette cucite e fibbie non si ripropongono.

**Passo 1, strada dichiarata: il sito non dipende dalle foto.**
`controlla-sito.py` dava 7/8 e l'unico sbarramento erano le foto: 9 su 10 sotto
1080 px, le copertine dei reel a 360x640. Strada 2 del processo (grafica
inventata, tipografia, colore). Strada 1 resta aperta: chiedere a Martina gli
originali e' anche un motivo per scriverle - e' di Patrick.

**Passo 2: tre mondi da un operatore di direzione su Opus** che ha caricato
`impeccable context`, `reference/new-work.md`, `design-taste-frontend` e
`high-end-visual-design`, e ha letto NG Barber e Fiftynine sul Mac. Proposti: A
«la distanza» (asta graduata in metri), B «il bianco e il nero», C «lo schema di
condotta» (il foglio di gara sul crema).

**Scelto B — il bianco e il nero.** Il suo logo e' gia' il concetto: due teste
di cane incastrate, una nera e una bianca, le due meta' del mestiere - in
obedience il cane resta fermo, in acqua si butta. Il sito e' quel marchio
aperto. Spina: le due teste si incastrano e la linea di incastro diventa il
bordo della pagina; sopra la linea la meta' nera (obedience, lavoro a distanza),
a meta' pagina la linea taglia il centro e la pagina si ribalta **una volta
sola** su fondo bianco (water games, dogsitting, trasferte); in fondo le due
meta' si richiudono nel marchio piccolo sopra il DM.

Grafica inventata: l'incastro in apertura; la linea di taglio, un `path` alto
quanto il documento disegnato sullo scroll, che comanda da che lato sta il
contenuto; il ribaltamento su due variabili CSS, una sola inversione in tutta la
pagina; sei coppie di contrari in condensato da 96 a 260 px (FERMO/VAI,
PIEDE/VENTI METRI, ASCIUTTO/BAGNATO, RING/RIVA) che si scambiano di lato.

Perche' non si sposta su un'altra istruttrice: il taglio non e' un vezzo, e' il
suo marchio che si apre e si richiude.

Palette: `#000000` e `#FFFFFF` a blocchi pieni, `#EB6F1F` solo su linea, numeri
e bottone. Tipografia: Archivo variabile su tre larghezze dell'asse `wdth` come
fa il suo logo. Foto: griglia dichiarata 4x2, gutter 2 px, tutte in bianco e
nero ad alto contrasto con un trattamento unico.

**Il copy dei giri 5-6 si tiene.** L'ha riscritto il direttore frase per frase
dopo «scrivi come un bambino»: si riusa tale e quale dove la struttura nuova lo
consente, non si rigenera.

**Costruito e online, 11 settembre sera.** Seed impeccable **`68e9cbb6`**, indice
assegnato 4, sfidante competitivo «Blue Note». Operatore di costruzione su Opus,
poi il giro di correzione l'ho chiuso io (Fable) perche' Nicola aveva fretta.
Nicola sul primo giro: «per il resto mi piace molto», e quattro correzioni sue,
tutte applicate:

- **il logo non si ridisegna**: in hero, in barra e in chiusura c'e' la sua
  immagine di profilo (`logo-tondo.jpg`, 480px) ritagliata al cerchio col
  `clip-path`. **480 px e' il tetto**: nell'hero non si mostra oltre. Il file
  buono lo chiede Patrick a Martina quando le scrive;
- entra **ruotando e sfumando da 0 a 100**, niente incastro delle due meta';
- la linea di taglio e' **tutta arancione** (5 px), via la costura bianca/nera;
- in fondo la linea **passa dietro** al marchio, non sopra.

Piu' i buchi visti sulle catture: la linea che a 375 passava sopra il testo (era
la normalizzazione su `scrollHeight`, corretta sulla scatola della pagina), le
coppie dei contrari che sul telefono si leggevano a meta' (sotto i 900 vanno a
capo sullo slash), il vuoto in «chi sono» e quello prima della griglia.

Misurato: overflow 0 a 375 e 1440, console headless vuota su tutte e due,
sbarramenti verificati con `curl`, CSS `?v=32` online. **`controlla-sito.py`
da' 7/8**: il logo in bitmap ha tolto tre `<svg>` e il conteggio scende sotto
i sei che chiede con foto piccole. E' la scelta di Nicola, non una regressione.

⬜ Safari su iPhone vero: non provato. ⬜ Il rapporto dell'operatore (giro di
fix interrotto) sta in `git stash` del repo, con un hero a colonna sola
scartato perche' a Nicola piace quello a due colonne.

## Collegamenti

[[processo-siti]] · [[essenza-e-motion]] · [[trappole]] · [[registro-interventi]]
