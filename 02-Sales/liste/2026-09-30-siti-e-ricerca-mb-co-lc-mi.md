---
riga: Liste del 29-30/9, prime con la regola dei luoghi: 100 siti da MB, CO, LC e MI senza bellezza, 61 ricerca da MB e CO. Resa e trappole.
type: area
updated: 2026-09-30
source: claude
verificato: 2026-09-30
prodotto: [siti-vetrina, gestionale-custom]
canale: instagram
stato: pubblicata
---

# 29-30 settembre: la prima lista luogo per luogo

Le prime liste con le regole di Patrick del 29/9, in [[metodo-liste]] e al
passo 2-bis di `/banco`: luogo per luogo, un settore fino in fondo, bellezza in
pausa. Partite la sera del 29, chiuse alle 21:30 del 30. Patrick ha chiesto
due volte più velocità, ma la bellezza l'ha lasciata in pausa.

| Lista | Righe | Da dove |
|---|---|---|
| Siti | **100** | MB 22 · CO 50 · LC 25 · MI 3 |
| Ricerca | **61** | MB 49 · CO 12 |

Ganci siti: 68 nessun sito, 20 piattaforma, 7 link in bio rotto, 3 dominio con
la pagina di prova o «in costruzione», 1 vivo ma mai finito, 1 dominio morto.

## La resa, che spiega il tempo

- **Siti fuori dalla bellezza: circa una riga ogni 6-10 profili.** Col
  Piemonte delle ciglia del 29/9 era una ogni 2. In MB 22 righe da circa 200
  profili: fotografi e fioristi da matrimonio hanno quasi tutti il sito,
  toelettature e personal trainer sono sotto i 200 follower o dentro palestre e
  pet shop.
- **Rendono**: la ristorazione piccola di Como (una ogni 3) e le pasticcerie
  (una ogni 5). **Non rendono**: fotografi, fioristi, sartorie.
- **Ricerca in MB: una riga ogni 7-10 profili.** Le officine strutturate sono
  quasi solo concessionarie, gli impiantisti e gli autotrasportatori non stanno
  su Instagram. Rendono le aziende agricole con vendita e i produttori
  alimentari (birrifici, distillerie, salumifici).
- **MB è chiusa per tutte e due le liste.** Lo stato per luogo e settore sta
  in `rotazione.csv`: la prossima lista siti riparte dalla ristorazione di
  Como, la ricerca dalle officine di Como.

## Correzioni fatte in rilettura, prima di pubblicare

- **Complimenti senza verbo.** Dopo un'istruzione mia («si ferma sul fatto»)
  14 complimenti di Como erano elenchi di sostantivi. Riscritti come frasi con
  il verbo («Mi è piaciuta la torta di Shrek che…»), e la forma è finita nel
  brief degli operatori.
- **Deduzioni spacciate per fatti.** «Per i trent'anni di un cliente» non
  stava nel post: tolto dal banco prima che partisse. Anche un mio «rivestito
  da capo» su un tappezziere, tolto.
- **Frasi a effetto** tolte: «meglio di un calendario», «otto secoli di
  storie», «sono i cavalli a insegnare a rallentare», «quello che in bio chiami
  sito».
- **Domini col nome giusto e di altri**, aperti uno per uno: ilbagnodifido.it
  (casinò), scodinzolando.com (farmacia veterinaria), pasticceriacentrale.com
  (Orzinuovi), pinkopallino.net (agenzia di Milano), pasticceriapontiggia.it
  (Seregno), donnarumma.it (parrucchiere di Napoli), pizzamore.com (Oregon),
  pannaefragola.com (Spagna).
- **Il Forno Bakery** di Cantù ha due post di lutto ad agosto: scritto nella
  scheda, i tempi del DM li decide Patrick.

## La posta

I DM partono dall'account DenkiCode (Patrick, 30/9), e il browser dell'app ha
aperto `@patrick.sappa`: le risposte ai 160 del 29/9 non si vedono da qui.
Scritto al passo 3-bis di `/banco`. Per leggerle Patrick deve aprire DenkiCode
nel browser dell'app.

## Trappole nuove

- **Google va in captcha dopo poche decine di ricerche e non torna in una
  notte.** Si è lavorato con un motore per operatore: DuckDuckGo html (Como),
  Yahoo (Lecco), Startpage (Milano). Mojeek, Ecosia e Brave sono andati in
  captcha subito.
- **La ricerca di Instagram (topsearch) muore dopo circa 150-600 query della
  giornata**, sommate fra tutti gli operatori. Gli **hashtag dei comuni**
  (`tags/web_info`, per esempio #olgiatecomasco) sono stati la fonte migliore,
  ma vanno distanziati.
- **Il browser tiene 9 tab.** Gli operatori morti le lasciano aperte e il
  quinto resta fuori: ogni operatore ne usa una e la chiude.
- **Gli operatori si piantano** se una chiamata supera i 10 minuti, e perdono
  quello che hanno in memoria: lotti da 20, ogni riga subito su disco.
- **La scratchpad è condivisa**: due operatori si sono sovrascritti `add.py`.
  I file di lavoro vanno nominati per luogo.
- **Da Bash il DNS non risolve** i siti delle aziende e a tratti nemmeno
  github.com. I domini si aprono con `apri()` di `verifica-sito.py`, che passa
  da DNS-over-HTTPS.
- **`controlla-lista.py` cerca parole, non fatti**: vuole «altra attività» per
  un dominio vivo che non è loro, e segnala una piattaforma scritta in verifica
  anche se è di un'omonima.
- Ai profili `@nazionale_trasporti_srl`, `@salumificio.terruzzi`,
  `@civico21homerestaurant` e `@fotografiamo_mariano_comense_` dal browser
  manca il tasto Messaggio: il DM va aperto da Direct.

## Collegamenti

[[2026-09-29-ciglia-piemonte-e-ricerca]] · [[metodo-liste]] ·
[[metodo-instagram]] · [[dm-instagram-vetrina]] · [[dm-instagram-ricerca]] ·
[[voce-denkicode]]
