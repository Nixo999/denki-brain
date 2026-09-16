---
type: progetto
riga: Sito vetrina di Andrea, barbiere al Villaggio SNIA di Cesano Maderno, che fa anche da tramite per i trapianti in Albania. Primo presidio volantini, gratis.
status: attivo
client: parrucchiere-morgan
stack: HTML statico + GSAP, starter DenkiCode, Netlify
started: 2026-09-16
deadline:
updated: 2026-09-16
source: claude
verificato:
tags: [sito, barbiere, presidio, cesano-maderno]
---

# Sito Barbershop SNIA — Andrea, Cesano Maderno

Il parrucchiere-presidio portato da [[morgan]] il 15 settembre. Non paga: il
sito è il corrispettivo dell'esposizione di volantini e del passaparola
→ [[parrucchiere-morgan]].

## Chi è, verificato

| | |
|---|---|
| Titolare | **Andrea** (nelle dieci recensioni è sempre «Andrea») |
| Insegna | Barbershop, Instagram `barbershop_snia` — 325 post, 380 follower |
| Dove | Via Friuli 22D, **Villaggio SNIA**, Cesano Maderno (MB) |
| Telefono | 340 416 1806 |
| Email | `andreailcarlot@libero.it` |
| Orari | mercoledì, venerdì e sabato, **10-22**. Gli altri quattro giorni chiuso |

⚠️ **Il civico non torna**: la sua bio dice 22D, gli elenchi (Fresha,
ItaliaRecensioni) dicono 20. **In pagina va 22D**, che è quello che scrive lui.
Da far confermare a voce.

## Le due cose che fa

1. **Taglio e barba.** Classico e «tattico ultima moda», rasatura barba alla
   vecchia maniera, e una reputazione precisa coi bambini che hanno paura.
2. **Tramite per i trapianti di capelli in Albania.** DHI e FUE, **da 1.800 €**,
   copertura 100%, con hotel, navetta dall'aeroporto, visita e analisi compresi.
   Preventivo gratuito. Un suo post del 2025 lo mostra a passeggio in centro a
   Tirana: in Albania ci va.

## Materiale raccolto il 16/09

- **11 foto Instagram scaricate, tutte a 1080 px o più** — sopra il minimo, non
  serve chiederne altre. Due sono fonti e non immagini (la locandina e un suo
  cartello scritto), nove sono usabili. L'inventario con **cosa si vede
  davvero in ognuna** sta in `PRODUCT.md` nel repo.
- **Dieci recensioni, tutte positive**, dal dicembre 2021 all'novembre 2023, da
  ItaliaRecensioni. Sono in `PRODUCT.md` verbatim, e sono il copy migliore che
  abbiamo: «non è il classico barber, è come uno di famiglia», «uno dei pochi
  che esegue rasatura barba come ai vecchi tempi», «NUMERO UNO X LE BARBE».
- **La sua voce scritta**, da un post: «vi propongo il nostro pacchetto per
  informazioni contattatemi pure oppure passate in barberia per una consulenza».

## Il vincolo che comanda

Nicola: il cliente «vuole che ci sia tanta pubblicità di DenkiCode, deve essere
visibile il nostro logo, deve essere visibile il fatto che l'abbiamo fatto noi
perché lui vuole aiutarci». Il marchio non è la firmetta del footer: è una
presenza dichiarata in pagina, e deve leggersi come un pregio del sito.

## Cosa non c'è, e non si inventa

Listino prezzi (le recensioni dicono solo «onesti»), il nome del suo assistente,
la data di apertura, il nome della clinica in Albania, la partita del civico.

## Il mondo scelto — «Il filo»

Tre mondi proposti dall'operatore di direzione il 16/09, scelto il primo con
due innesti dagli altri due.

Il Villaggio SNIA è nato negli anni Venti attorno allo stabilimento SNIA
Viscosa, che filava viscosa, e le vie portano nomi di regioni: la sua è Via
Friuli. **Andrea lavora sul filo**: lo taglia, lo rade, e dove non c'è più lo fa
rimettere uno alla volta — la DHI è un innesto bulbo per bulbo. È la stessa
materia presa dai due lati, ed è il motivo per cui le sue due attività stanno
sulla stessa pagina senza sembrare due mestieri.

Spina dello scroll: un filo rosso continuo scende lungo la pagina e si disegna
allo scrub; a metà, in pin, le forbici a X del suo logo si chiudono e lo
tagliano; sotto si sfila in filamenti singoli che si piantano su un arco di
cranio, riparte unico verso Tirana e alla fine si annoda nel simbolo DenkiCode.

Innestati dagli altri due mondi: **l'apertura col suo logo capovolto** che ruota
di 180° finché BARBERSHOP diventa leggibile (il marchio vero è così), e
**l'arco delle ore vivo** che legge l'ora di Roma e dice se è aperto.

Palette piastrella `#f1f1ee`, nero `#121212`, filo rosso `#d1271b`, grigio
`#8d8f8a`. Display **Anybody** variabile sull'asse `wdth`, testo **Onest**.

Scartati: «A testa in giù» (il panno che copre il viewport rischia di leggere
come una transizione da template, e il teal era campionato a occhio da una
locandina che non è sua) e «Tre giorni» (le facciate delle case del villaggio
rischiavano il cartoon, e il cartoon è già stato bocciato su Mikuma).

## Com'è venuto — giro 1, 16/09

Costruito in `~/lavoro/barbershop-snia-site` (repo locale, **nessun remote**),
commit `3b9754f` più la correzione del copy. `controlla-sito.py` **8/8**.

Capitoli: hero col marchio capovolto che ruota di 180° e l'h1 che si tende
sull'asse `wdth` di Anybody · nastro in corsa · «Il taglio e la barba» con sei
foto in bianco e nero e le didascalie sul servizio · pin «Sulla poltrona», dove
le forbici si chiudono e spezzano il filo · «Chi si siede da me», quattro
recensioni verbatim col nome · «Tre giorni, dalle 10 alle 22», telaio a sette
fili e arco delle ore che legge l'ora di Roma · «Quando i capelli non ci sono
più», cranio a 214 punti con 44 innesti che si piantano allo scrub, i quattro
nodi verso Tirana · **capitolo DenkiCode**, dove il filo disegna il simbolo ·
footer. **17 `<svg>` inline.**

Misurato: console pulita, `scrollWidth == innerWidth` su dieci larghezze da 320
a 1440, zero testi sotto AA, pagina completa senza JS e in `?cattura`, arco
delle ore verificato in due stati reali («aperto fino alle 22» e «chiuso,
riapre venerdì alle 10» — quest'ultimo alle 22:24 di mercoledì, ed è giusto).
Il filo è un solo path da 8.292 px con `y` monotòna: la ricerca binaria costa
0,56 ms a frame.

**Corretto dal direttore**: il copy diceva «chi lo vuole lo accompagno a fare
il trapianto in Albania». Non è verificato da nessuna parte. Adesso dice solo
quello che è dimostrabile — il pacchetto lo propone lui (suo post) e a Tirana
c'è stato (suo post).

## Giro 2 — le correzioni di Nicola, 16/09

> «togli il carosello di frasi, migliora le espressioni, sintassi errata, tono
> sbagliato, impostazione delle frasi errata ecc ecc, il logo di denki in basso,
> deve essere il nostro ufficiale in rosso al posto di quel simbolo che hai
> messo... metti qualcossa su di noi e sui trapianti anche in alto, cosi uno non
> deve scorrere tutto il sito»

Tutte e quattro finite in [[direttive-siti]] nel momento in cui sono state dette.

- **Via il nastro di frasi in corsa.** Al suo posto, subito sotto l'hero, le due
  cose che fa in due carte — taglio e barba, trapianto da 1.800 € — e sotto una
  riga con il logo DenkiCode rosso e la frase di Andrea. Chi arriva per il
  trapianto adesso lo trova senza scorrere la pagina intera.
- **Copy riscritto riga per riga.** Le frasi lunghe c'erano già, ma l'italiano
  no: «il classico lo taglio di forbice e pettine» senza preposizione, «il
  discorso cambia e lo faccio in bottega» con il pronome che non si capisce a
  cosa si riferisce, «il taglio viene fuori mentre si parla d'altro».
- **Il logo DenkiCode è quello ufficiale, in rosso**, nel capitolo e nella
  firma. I gradienti viola-magenta sono stati mappati su `currentColor` tenendo
  i `<linearGradient>` al loro posto (cancellarli fa sparire metà marchio,
  perché il 気 e la parola CODE sono riempiti dal gradiente), e la tavola di
  presentazione è stata potata di tutto quello che stava fuori dal `viewBox`:
  **da 148 KB a 25 KB**. I due file mono sono in [[identita-visiva]].
- Il titolo del capitolo non è più «DenkiCode», che il logo dice già: è
  **«Chi mi ha fatto il sito»**.
- Aggiunto `--filo-chiaro:#e8442f` per il testo rosso su nero: il rosso del filo
  su `#121212` dà 3,58 e sotto i 18 px non passa AA.

Rimisurato: 8/8, **overflow 0 su tredici larghezze** da 320 a 1440, **0 testi
sotto AA** (con il fondo composito, non quello dichiarato), console pulita.

## Non verificato, e aperto

- ⬜ **Non pubblicato**: il comando Netlify è stato bloccato dal classificatore
  dell'auto mode. Lo lancia Nicola. Finché non è online, la bozza non esiste
  → [[netlify]]
- Safari e iOS reali mai provati: `font-variation-settings` animato, la
  proprietà `translate`, il pin con la barra indirizzi che si ridimensiona
- Hover e focus scritti e non misurati (un `::focus-visible` universale, rosso
  su nero: contrasto 3,0 — al limite)
- La riga «chiamateli pure da parte mia» attribuita ad Andrea **va fatta
  leggere a lui** prima del go-live: è l'accordo, ma non gliel'ha detta nessuno
- Restano `TODO` il listino prezzi, il CAP, il nome della clinica e il civico
  (22D contro 20)

## Collegamenti

[[parrucchiere-morgan]] · [[morgan]] · [[processo-siti]] · [[direttive-siti]] ·
[[presidi-volantini]] · [[netlify]]
