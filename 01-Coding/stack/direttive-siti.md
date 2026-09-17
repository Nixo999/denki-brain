---
type: risorsa
riga: Ogni correzione che Nicola ha dato su un sito, diventata regola permanente. Si legge prima di costruire e prima di pubblicare.
updated: 2026-09-17
verificato: 2026-09-11
source: denkicode
tags: [siti, design, direttive, qualita]
---

# Direttive sui siti — quello che è già stato bocciato

**Questo file cresce e non si accorcia.** Ogni volta che una bozza viene
bocciata, la frase esatta entra qui insieme alla regola che ne esce. Un sito
nuovo non può ripetere niente di quello che c'è scritto sotto: è il meccanismo
per cui i siti migliorano invece di oscillare.

Si legge **due volte**: dall'operatore di direzione prima di proporre i mondi, e
dall'operatore di costruzione prima di dire che ha finito. Il controllo
meccanico è `01-Coding/strumenti/controlla-sito.py`, ma quello misura solo ciò
che si può contare. Qui c'è il resto.

⚠️ Le frasi fra virgolette sono di Nicola, verbatim. Non si ammorbidiscono.

## Il metro

**NG Barber e Fiftynine passano, gli altri no.** Sono gli unici due approvati
senza riserve, e li ha fatti un processo che non aveva brief: chi leggeva il
cliente e chi inventava erano la stessa testa. Se una bozza non regge accanto a
quelle due, non è pronta.

## Le direttive, dalla più recente


### 17/09/2026 — Nicola: «crea cose in 3d per i tagli e per i trapianti, rendilo piu pieno, lo vedo vuoto, trova qualcosa che mi accompagni per tutto il sito»

Bozza Barbershop SNIA giro 10, dopo che la struttura a due porte era stata approvata come base. Tre cose: il 3D sulla materia del mestiere (non decorazione), la densita' - le pagine ariose lette da Nicola sembrano vuote, non eleganti - e un elemento che accompagni tutta la pagina. ATTENZIONE: il filo era esattamente questo ed e' stato bocciato, quindi non una linea che segue lo scroll: deve essere l'oggetto del mestiere

### 17/09/2026 — Nicola: «no il filo fa proprio cagare, reimpagina, reimposta, rifai le animazioni, rifai lo sfondo, cerca di non renderlo un ai slop»

Bozza Barbershop SNIA giro 8, dopo due giri di correzioni sul filo. Un elemento grafico che attraversa tutta la pagina non si aggiusta a colpi di opacita' e spessore: se al secondo giro non regge, la direzione e' finita e si torna al passo 2 del processo. E la spina dello scroll non deve essere una linea che segue lo scroll: e' il pattern piu' riconoscibile come AI

### 17/09/2026 — Nicola: «il filo lagga e non è bello sovrasta e non gasa, va bene l'idea ma non l'esecuzione»

Bozza Barbershop SNIA giro 7. Tre difetti distinti in una frase: lo scrub di GSAP a 0.8 fa trascinare l'elemento dietro lo scroll e si legge come lag; un tratto pieno di colore acceso lungo tutta la pagina compete col contenuto invece di accompagnarlo; e una linea che cresce e basta non e' un momento. La spina dello scroll si fa con una scia spenta e sottile e il colore vivo solo negli ultimi 150 px, dove il lettore sta guardando

### 17/09/2026 — Nicola: «sono professionali, modici nei prezzi e molto veloci»

Bozza Barbershop SNIA giro 6, al posto di 'lavorano bene, consegnano in fretta e costano poco'. E' la formula con cui DenkiCode si descrive dentro il sito di un cliente: si usa questa, non una parafrasi

### 17/09/2026 — Nicola: «fai una ricerca approfondita su internet di cosa serve per annullare l'AI slop sui siti, e tutti i metodi per far sembrare che un sito non sia fatto dall'AI, usa poi quei risultati come base per controllare i siti futuri»

i siti non devono sembrare fatti con l'AI: la ricerca diventa il metro con cui si controlla ogni sito nuovo

La ricerca e i controlli: [[anti-slop-siti]]. Lo strumento: `python3 01-Coding/strumenti/controlla-slop.py <cartella>`, al passo 5-bis del processo.

### 17/09/2026 — Nicola: «elimina frasi senza senso, migliora l'armonia delle frasi, ogni tanto sparli e metti frasi fatte ancora sintatticamente da un bimbo»

Shaddai giro 2, sesta bocciatura di fila sul copy: il registro impersonale era giusto ma dentro restano frasi che non vogliono dire niente (la lettura e' di volume, si leggono da tre metri), frasi fatte da post Instagram (si nota che qualcosa c'e', non si capisce cosa) e periodi tutti della stessa lunghezza. Impersonale non basta: le frasi devono anche stare in piedi da sole e avere ritmo diverso

### 17/09/2026 — Nicola: «nel banner di denkicode togli a seveso, aggiungi che siamo bravi veloci ed economici»

Bozza Barbershop SNIA giro 5. Il blocco DenkiCode dentro un sito cliente non dice dove stiamo, che restringe il bacino: dice che lavoriamo bene, in fretta e che costiamo poco. E' l'unica pubblicita' che abbiamo su quella pagina

### 17/09/2026 — Nicola: «frasi sotto le foto dei tagli»

Bozza Barbershop SNIA giro 5, nell'elenco delle cose da eliminare. Le didascalie sotto le foto di una galleria si tolgono: la foto si spiega da sola, e una riga di testo sotto ognuna spezza la griglia e aggiunge parole che nessuno legge

### 17/09/2026 — Nicola: «professionale, impersonale»

Bozza Barbershop SNIA giro 4, detto subito dopo 'analizza le frasi, sparli e fai un pasticcio ogni volta'. Il copy dei siti non si scrive in prima persona come il titolare: si scrive in impersonale, come Antica Barbieria Colla - 'il trattamento dura 25 minuti e viene eseguito con rasoio monouso sterile'. Supera la direttiva del 16/09 su New Fantasy ('fai sembrare che scriva lui le note'), che resta valida solo sul non dichiarare da dove viene un contenuto

### 17/09/2026 — Nicola: «professionale, impersonale»

Registro scelto per il copy dei siti dopo la bocciatura di Shaddai giro 1: via l'impalcatura io/tu, le azioni si dicono col soggetto vero (il mapping, le lunghezze, la laminazione). Supera in parte la direttiva del 16/09 sulla prima persona, che resta valida solo sul non dire mai da dove viene un'informazione

### 17/09/2026 — Nicola: «solito problema, gli script, le frasi fanno cagare»

Bozza Shaddai giro 1, quinta bocciatura di fila sul copy dopo Mikuma, Custom Beauty Nails, New Fantasy e Barbershop. Far leggere all'operatore i siti veri del mestiere non ha spostato il risultato: il testo esce parlato, da messaggio, e deve essere scritto

### 16/09/2026 — Nicola: «l'impostazione delle frasi è completamente sbagliata, guarda dei bei siti di gente che ha saloni eccetera, copia quella impostazione verbale e delle frasi»

Bozza Barbershop SNIA giro 2, quarta bocciatura di fila sul copy. Il modo di scrivere non si inventa a tavolino: prima di scrivere si vanno a leggere i siti veri di quel mestiere fatti bene, e si prende da li la lunghezza delle frasi, la persona, come aprono i paragrafi e come sono scritti i titoli di sezione

### 16/09/2026 — Nicola: «questo deve essere il nostro logo»

Bozza Barbershop SNIA giro 2: nel capitolo DenkiCode restava un path SVG che imitava a mano l'anello e il 気. Nel punto dove va il nostro marchio ci va il file ufficiale, mai un ridisegno - vale anche quando il ridisegno serve a farlo animare

### 16/09/2026 — Nicola: «migliora le espressioni, sintassi errata, tono sbagliato, impostazione delle frasi errata»

Bozza Barbershop SNIA giro 1, terza bocciatura di fila sul copy dopo Mikuma e Custom Beauty Nails. Non basta che le frasi siano lunghe e col mestiere dentro: devono essere scritte bene in italiano, con la sintassi giusta e il tono di chi parla

### 16/09/2026 — Nicola: «il logo di denki in basso, deve essere il nostro ufficiale in rosso al posto di quel simbolo che hai messo»

Bozza Barbershop SNIA giro 1: nel capitolo DenkiCode il marchio era ridisegnato e nel footer stava la versione a gradiente. Il logo DenkiCode non si ridisegna mai e non si ricolora a gusto del sito: si usa il file ufficiale

### 16/09/2026 — Nicola: «metti qualcossa su di noi e sui trapianti anche in alto, cosi uno non deve scorrere tutto il sito»

Bozza Barbershop SNIA giro 1: DenkiCode e il servizio secondario stavano solo in fondo. Quello che conta - il secondo servizio e la firma DenkiCode quando il cliente l'ha chiesta - va anche sopra la piega, non solo in fondo alla spina dello scroll

### 16/09/2026 — Nicola: «togli il carosello di frasi»

Bozza Barbershop SNIA giro 1: il nastro di parole in corsa sotto l'hero (marquee). Non si mette su nessun sito: e' un elemento da template che non dice niente e mangia una fascia intera

### 16/09/2026 — Nicola: «è bellissimo ma devi rifare tutta la parte di script, le scritte fanno schifo sembra fatto da un bambino di 10 anni devono essere professionali»

bozza Custom Beauty Nails online, giro 1: il copy era tutto in frasi corte e spezzate ('Rosso pieno, mandorla, niente altro sopra'), lessico da conversazione e nessuna competenza di mestiere in vista. E' la seconda volta dopo Mikuma dell'11 settembre: 'discorsivo' non vuol dire frasi da due parole, vuol dire periodi interi con dentro il mestiere

### 16/09/2026 — Nicola: «aggiusta i testi, non dire mai da dove lo prendi, e fai sembra che scriva lui le note»

New Fantasy giro 2: in pagina c'era «Dal profilo Instagram del salone» sotto la citazione e «il colore è preso dai suoi capelli». Il sito parla in prima persona come il titolare, e la provenienza di frasi, foto e numeri non si scrive mai

### 16/09/2026 — Nicola: «non hai capito niente, non dovevi fare solo un sito asato sul fatto che sia un gestionale, rifai la parte del sito, aggiungendo un po di vita e fai capire la personaita del cliente»

bozza New Fantasy, 16/09: la vetrina leggeva come un software di prenotazioni. La prenotazione e' una funzione dentro il sito, la pagina deve raccontare il salone: la voce loro, i tre nomi, le promo, le foto, movimento

### 14/09/2026 — Nicola: «patrick dice che è vuoto. metti qualche animazione piccola in più, rimpicciolisci le foto un pochino, e aggiungi dei disegni di qualche tipo»

Sito bozza laurafranzoni_lashmaker visto online da Patrick al giro 2: la pagina tolte le note di regia sembra vuota. Una vetrina si riempie di disegni e micro-animazioni nella stessa lingua, non di foto piu grandi

### 14/09/2026 — Nicola: «da telefono si vede così, allontana instagram dal suo nome, e mettilo che si noti meno»

barra di nails.robyy a 375: il bottone Instagram in riquadro pesante stava attaccato a ROBERTA. Sul telefono la voce di contatto in barra va al bordo destro, staccata dal marchio, e pesa meno del nome

### 14/09/2026 — Nicola: «questa frase che spiega cosa hai messo non ha senso, eliminala e anche tutte quelle simili»

sul sito nails.robyy la riga «Il quinto profilo è vuoto: è il posto di chi impara.» sopra il disegno della convergenza: il copy che spiega la grafica o la metafora al lettore non serve a chi legge, va tolto, non riscritto

### 14/09/2026 — Nicola: «aggiusta le scritta, non lasciare note scritte da te, solo frasi utili, e sensate. rimuovi cose che dicono come, la migliore del modno o la piu sottile»

Detto il 14 settembre 2026 sulla bozza Pinkploy online: il copy portava la frase della bio «le unghie più sottili e più belle che tu abbia mai avuto» e frasi nostre di contorno. Sul sito restano solo frasi utili a chi legge; niente superlativi e niente autopromozione, nemmeno se li ha scritti il cliente in bio.

### 14/09/2026 — Nicola: «aggiusta le scritte, non lasciare note scritte da te, solo frasi utili, e sensate. rimuovi cose che dicono come, la migliore del mondo o la più sottile»

Sito bozza laurafranzoni_lashmaker, giro 3: il copy aveva frasi nostre che spiegavano la pagina (perché le foto sono storte, note di regia) e superlativi non verificabili. Sul sito restano solo frasi che dicono cosa fa, per chi, e come contattarla

### 14/09/2026 — Nicola: «bello ma la hero section sostituisci il titolo deve essere il suo nome e sotto una frase, e poi la foto subito sotto occupa troppo spazio così è un po' brutto sembra un mega zoom sulla faccia della ragazza»

Sito bozza laurafranzoni_lashmaker, mondo «Dall'alto»: la fascia 21:9 sotto l'hero resa a tutta larghezza (1440 px CSS) legge come uno zoom sul viso, non come un punto di vista. L'h1 e' il nome della cliente con una frase sotto, come gia' detto su Pinkploy

### 14/09/2026 — Nicola: «tutto bello ma la hero section non mi piace. fai come al solito un titolo con il suo nome e una frase sotto in piccolo, non un frase cosi lunga come titolo. non sta bene. come introduzione al sito»

Detto il 14 settembre 2026 sulla bozza Pinkploy, dove l'h1 era la frase della bio su due righe. Stessa bocciatura di Mikuma («la frase su tre righe non può essere il titolo»): da qui è regola. L'h1 di ogni sito è il nome del cliente; la frase sua sta sotto, piccola.

### 11/09/2026 — «sembra che non usi più le skill nel modo di prima»

Tre operatori su sette non avevano caricato niente. **Nessun giro tocca la UI
senza `impeccable context` e `craft-floor`.** Un giro di sola correzione copy è
l'unica eccezione, e si dichiara.

### 11/09/2026 — «per NG Barber non gli ho detto niente e ha fatto un sito bellissimo»

La direzione non si decide prima di aver letto le skill di design. L'operatore
di direzione torna con due o tre mondi, il direttore sceglie.

### 10-11/09/2026, Mikuma — «fa schifo, sembra fatto da un bambino di due anni»

Bocciati: acqua a righe generata, foto dentro cornici da widget, hero da
template. Ne escono tre regole:

- **Niente materiali finti generati in CSS.** «Sembra finta, non stare a
  generare acqua finta.» Acqua, legno, marmo, fumo: o è una foto vera o è un
  segno grafico dichiaratamente astratto, mai una imitazione.
- **Niente foto in cornicette.** Una foto o riempie il suo spazio o sta in una
  griglia dichiarata. Quattro foto a quattro rapporti e quattro altezze diverse
  leggono come disordine.
- **Niente hero da template.** Parola gigante, sottotitolo, bottone, vuoto: è
  la forma che esce da sola quando non c'è una direzione. Se l'hero si potrebbe
  mettere su un altro cliente cambiando la parola, è quello.

### 11/09/2026, Mikuma — «scrivi come un bambino»

Il copy va in frasi complete, con il verbo. Le didascalie dicono il servizio,
non ripetono il nome del file né le caption dei post. Passa da
`voce-denkicode` prima della review.

### 10/09/2026, Da Caterina v1 — «da telefono è orribile, i ritagli fanno pena, sembra tutto buttato a caso»

**Il mobile si guarda, non si deduce.** E i ritagli automatici dei soggetti
vanno guardati uno per uno: un contorno sbagliato si vede subito e squalifica
la pagina intera.

### 08/09/2026, Tarilli — «un sacco di animazioni», «pizze che si muovono e fluttuano»

Quando Nicola chiede movimento, ne chiede **tanto e visibile**. La dose
prudente è una sua lamentela ricorrente, non una virtù.

### 01-03/09/2026 — Castiglione v1 «il sito più piatto della storia», DSI v1 «sta venendo malissimo»

Le due prime versioni costruite con la sola `design-taste-frontend`. Da lì nasce
la catena: una sola skill non basta, e il passo di carattere
(`bolder`, `delight`, `animate`) non è opzionale.

### Sempre — l'identità del cliente vince sul nostro gusto

La versione notte di DSI era bella e sbagliata: era il gusto Denki, non il
loro. Se il cliente ha logo, colori e voce, quelli comandano.

## Parlato e scritto — la lista da passare prima di dire che il copy è finito

Cinque bocciature di fila sul copy (Mikuma, Custom Beauty Nails, New Fantasy,
Barbershop, Shaddai) hanno tutte la stessa causa, e il 17 settembre 2026 l'ha
detta Nicola: **il testo esce parlato, da messaggio, e deve essere scritto.**
Leggere i siti veri del mestiere non è bastato, perché il difetto non è il
lessico né il tono: è la sintassi. Sette segni, ognuno con l'esempio vero preso
dal giro 3 di [[sito-barbershop-snia]], e la correzione.

| Il segno | Com'era | Com'è |
|---|---|---|
| **Soggetto che manca** | «Sopra la testa si dirada, dietro la nuca resta folta» — chi si dirada? | «Quando i capelli si diradano sopra e restano folti dietro la nuca» |
| **Pronome senza antecedente** | «nessun taglio **lo** nasconde» — che cosa? | «nessun taglio riesce più a mascherare la differenza» |
| **Soggetto sbagliato per vicinanza** | «si aprono i canali, poi **si innestano**» — l'ultimo nominato erano i canali | «si aprono i canali, e lì i bulbi vengono innestati» |
| **Dislocazione a sinistra** | «Questo sito **me l'**hanno fatto», «in Albania **ci** sono stato» | il soggetto in testa: «DenkiCode ha costruito questo sito» |
| **`gli` per `loro`** | «**gli** faccio sentire il rumore» | «la macchinetta viene accesa a distanza» |
| **Participi e gerundi appesi** | «se ne parla in bottega, **seduti, guardando** la testa» | «se ne parla in bottega, davanti allo specchio» |
| **Modi di dire orali** | «vogliono pazienza», «ci fanno l'orecchio», «trova posto», «e intanto», «come si deve» | «richiedono pazienza», «finché il rumore non diventa familiare», «passa dopo cena» |

E un errore di grammatica vero, che nessuna delle due letture aveva preso:
**«si lavora una persona alla volta»**. `Si lavora` è impersonale e non regge un
oggetto diretto. Si scrive «la bottega lavora su appuntamento» o «si riceve una
persona alla volta».

La prova è meccanica e si fa prima di consegnare: **si legge ogni frase da sola,
fuori dal paragrafo.** Se fuori contesto non si capisce chi è il soggetto o a
cosa si riferisce un pronome, quella frase è parlata e va riscritta.

## Come si aggiunge una direttiva

**Nel momento in cui viene detta**, non a fine sessione:

```bash
python3 01-Coding/strumenti/regola.py siti "la frase esatta" --chi nicola --perche "..."
```

Vale per una bocciatura **e per una preferenza detta a freddo**. Fino all'11
settembre 2026 il meccanismo era agganciato solo alla bocciatura e a
`/chiudi-sessione`: un «da adesso sui siti voglio sempre X» detto a metà
sessione non scattava, e si perdeva con la conversazione.

Non si riscrivono le vecchie: una direttiva superata si marca superata, non si
cancella. Questo file cresce e non si accorcia.

## Collegamenti

[[processo-siti]] · [[essenza-e-motion]] · [[trappole]] · [[convenzioni]]
