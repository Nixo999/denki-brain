---
name: scrittura-sito
description: Come si scrive il testo che sta dentro un sito DenkiCode - didascalie, titoli di sezione, micro-etichette, bottoni, title e meta description, punteggiatura italiana, lunghezza delle frasi. Da usare mentre si scrive il copy di una pagina e prima di dire che è finita, su ogni sito vetrina. Risponde a «cosa scrivo sotto questa foto», «come chiamo questa sezione», «che cosa metto su questo bottone». Non riguarda il tono di voce, che sta in voce-denkicode, né il processo di costruzione, che sta in processo-siti.
---

# Scrittura di un sito — quello che si misura

Nasce il 21 settembre 2026 da una bocciatura di Nicola sulla bozza Design
Capelli: *«controlla perché sotto le foto hai scritto delle cose completamente
inutili a uno spettatore del sito, tipo descrizioni della foto o titoletti
completamente inutili»*.

**Non era un errore di quella bozza.** Misurato lo stesso giorno su tutto
`~/lavoro` con `controlla-testo.py`: **82 didascalie da buttare su 16 siti**, e
fra quei siti ci sono **NG Barber (6)** e **Fiftynine (5)**, cioè i due che
teniamo come metro di qualità. Sulle prime 97 didascalie contate, **35
ripetevano parola per parola il testo alternativo dell'immagine**.

Questa skill esiste perché quel numero torni a zero e ci resti.

## La regola che rompevamo

**`alt` e `figcaption` parlano a due persone diverse.**

| | chi la legge | dove vive |
|---|---|---|
| `alt` | chi la foto **non** la vede: uno screen reader, un caricamento fallito | mai a video |
| `figcaption` | chi la foto **la sta guardando** | in pagina, sotto l'immagine |

Scrivere la stessa frase in tutti e due i posti vuol dire dire la stessa cosa a
due pubblici diversi, e sprecarne uno. Chi guarda la foto vede già il taglio, il
colore, la posa: una riga che glielo ripete non aggiunge niente, e si prende la
prima attenzione che dà alla pagina. Nell'eyetracking di NN/g **il 78% delle
prime fissazioni cade sul testo** e non sull'immagine: una didascalia vuota
occupa quel momento e non lo restituisce.

**Quando una didascalia ha diritto di esistere:** solo se porta un dato che la
foto e l'`alt` non dicono già. Un prezzo, una durata, un nome proprio, una data,
un materiale.

> «Taglio scalato con frangia laterale» → è la foto scritta. Si toglie.
> «Taglio scalato, 45 minuti, 28 euro» → è quello che la foto non può dire. Resta.

**La soglia controllabile:** una `figcaption` resta solo se, tolte le parole
vuote, condivide **meno del 50%** delle parole piene con l'`alt` della stessa
immagine. Sopra, è una parafrasi.

**Se non hai il dato, non inventarlo: togli la riga.** Su Design Capelli non
avevamo né prezzi né la tecnica usata su ogni testa, quindi le otto didascalie
sono uscite e basta. Una foto senza didascalia non è un buco.

## Gli stessi conti valgono per i titoletti

Se il micro-titolo ripete la categoria di quello che etichetta, uno dei due è di
troppo. Sopra un indirizzo non ci va «Dove», sopra un orario non ci va «Quando»,
sopra un numero non ci va «Telefono»: il contenuto si presenta da solo, e
l'icona fa il resto.

**Correzione giusta, non cancellazione:** l'etichetta esce dalla pagina e resta
per chi legge con la voce, con una classe che la toglie dallo schermo
(`.solo-lettori`). Chi vede la pagina non la legge, chi la ascolta sì.

## Cosa fanno i saloni veri — 11 siti aperti e letti

Ricerca del 21/09, sei saloni di quartiere fra Torino e la Brianza e cinque di
fascia alta o catena. Per esteso in [[copy-siti-competitor]].

- **Dieci su undici non scrivono niente sotto le foto.** L'undicesimo, Rossano
  Ferretti, mette due righe sotto le foto prodotto: «Idrata e ammorbidisce»,
  «Rimuove il crespo e disciplina». Sono benefici, non descrizioni. **Nessuno
  descrive cosa si vede nell'immagine.** Era l'unica cosa che facevamo noi e
  loro no.
- **Il titolo del primo schermo sta in cinque parole**, minimo due, massimo
  otto. Due siti su undici non ne hanno nessuno e aprono con un paragrafo: è la
  cosa che li fa sembrare vecchi.
- **«Scopri di più» sta su nove siti su undici**, su Franco Curletto nove volte
  nella stessa pagina. È il default del settore ed è quello che non si usa: non
  dice dove porta.
- **«Prenota» è il verbo del bottone in sei su undici**, spesso ripetuto per
  sede o per servizio. È la parola che il cliente cerca, e va tenuta anche
  quando il canale è WhatsApp: **«Prenota su WhatsApp»**, non «Scrivi».
- **Sette su undici dichiarano l'anzianità** in prima schermata, «da oltre
  trent'anni», «dal 1998». Noi la usiamo già: è la prova sociale che regge
  quando non ci sono i prezzi.
- **Cinque su undici richiamano il listino dalla home**, anche solo come
  rimando. Se il cliente i prezzi ce li dà, il listino va in pagina: è la
  seconda cosa che cercano dopo gli orari.
- **Quasi tutti hanno una sezione sul titolare o sul team** col nome e gli anni
  di mestiere: «quasi vent'anni di gavetta», «Joseph Zarra, oltre 30 anni». Noi
  ci mettiamo una riga. Il nome della persona si chiede, non si inventa.
- **Tutti hanno almeno un punto esclamativo o un imperativo entusiasta**
  («Prenota ora!», «...fiducia !»). Noi zero, e si resta a zero: è la cosa che
  distingue un testo scritto da uno gridato.

Le parole che ricorrono di più nel loro copy: *scopri* (9/11), l'anzianità
dichiarata (7/11), *prenota* (6/11), *listino* (5/11), *stile* (5/11), *cura*
(5/11), *esperienza* (4/11), *bellezza* (4/11), *su misura* (3/11),
*professionalità* (3/11). Le ultime quattro sono anche parole da densità per
`controlla-slop.py`: si nominano solo se accanto c'è un fatto.

## Il testo che resta

- **Una persona non legge, scansiona.** Il 79% scansiona sempre una pagina
  nuova, solo il 16% legge parola per parola, e su una pagina media si legge il
  **20-28%** delle parole. Metà pagina si legge solo **sotto le 111 parole**.
- **Piramide rovesciata**: il punto nella prima riga, i dettagli dopo. Chi
  scansiona deve potersi fermare alla prima riga e avere già capito.
- **Lo sguardo fa una F**: due bande in alto e poi giù sul margine sinistro. Il
  peso va a inizio riga e nelle prime due righe, mai in fondo al paragrafo.
- **Un paragrafo, un'idea.** La seconda idea nello stesso paragrafo non viene
  letta. Non esiste un numero di parole giusto: esiste l'idea sola.
- **Gulpease sopra 60.** `89 + (300 × frasi − 10 × lettere) / parole`. Sotto 60
  il testo è faticoso per chi ha la licenza media, e il cliente di un
  parrucchiere di quartiere è chiunque.
- Riscrivere in forma scansionabile, concisa e oggettiva vale **+124% di
  usabilità misurata**: non è gusto, è il numero di Morkes e Nielsen.

## Punteggiatura, in italiano

- **Virgola** per liste e incisi veri. Non per spezzare una frase che si dice
  intera.
- **Due punti** per annunciare: introducono, non separano.
- **Punto e virgola**: quasi mai in una vetrina. Serve dentro elenchi lunghi già
  pieni di virgole.
- **Trattino breve** unisce e non ha spazi (`macro-obiettivo`). **La lineetta**
  separa e li ha. Non sono lo stesso segno. Il trattino lungo resta fuori dai
  testi che legge un cliente → [[voce-denkicode]].
- **Puntini di sospensione**: in un sito leggono come indecisione, non come
  stile.
- **Punto esclamativo**: mai su un prezzo, un orario, un dato. Segnala
  emotività, ed è incompatibile con un tono oggettivo. Dentro una recensione
  citata alla lettera invece resta: è di chi l'ha scritta.
- **Nei titoli si maiuscola solo la prima parola e i nomi propri.** Il Title
  Case è inglese.

## Title, meta description, nome del comune

- Il `<title>` porta il marchio in modo conciso, separato dal resto con due
  punti, un trattino o una barra. **Google non fissa un numero di caratteri**:
  tronca in base alla larghezza dello schermo. Chi cita 155 o 160 lo prende da
  misure di terzi.
- La `meta description` è univoca per pagina e non è un elenco di parole chiave.
- **Sul comune Google non dà un numero, dà un divieto**: elencare città per
  posizionarsi, o ripetere lo stesso termine fuori contesto, è keyword stuffing
  per loro. Il comune compare dove serve al senso: nel title, in un H1,
  nell'indirizzo. Non a ogni paragrafo.

## Bottoni ed etichette

Microcopy ha tre compiti: informare, influenzare, aiutare a fare la cosa.

**«Scopri di più» non dice dove porta.** Con più bottoni uguali in pagina
diventa ambiguo, per chi usa uno screen reader il link isolato non ha senso, e
non porta nessuna parola chiave. Al suo posto va la parola chiave della
destinazione: «Il listino», «Le foto del salone», «Scrivi su WhatsApp».

**La prova:** copri il resto della pagina e leggi solo l'etichetta. Se non dice
dove porta, si riscrive.

## Prima di dire che il copy è finito

```bash
python3 01-Coding/strumenti/controlla-testo.py ~/lavoro/<cartella>
```

Deve uscire **0 blocca**. Gli avvisi si guardano uno per uno: un punto
esclamativo dentro una recensione citata è giusto, uno su un orario no.

Poi `voce-denkicode` sul tono, che è un'altra cosa e viene dopo.

## Le fonti

Stanno per esteso, con i link, in [[scrittura-web]] (18 fonti: NN/g, W3C/WAI,
MDN, Treccani, Accademia della Crusca, Google Search Central, Poynter) e in
[[copy-siti-competitor]] per quello che fanno i saloni veri. La direttiva con le
parole di Nicola sta in [[direttive-siti]], lo strumento in [[strumenti]].
