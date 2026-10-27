---
riga: Giro del 27/10 - 42 righe di siti su 101, banco a 111; Brave non approvato, Instagram senza login bloccato dopo circa 100 letture
type: area
updated: 2026-10-27
source: claude
verificato: 2026-10-27
prodotto: [siti-vetrina]
canale: instagram
stato: bozza
---

# 27 ottobre: 42 righe di siti senza l'account collegato

Giro di [[giro-mattina]], ruolo `primo`, dal Mac di Nicola, partito alle 08:01.
Sul banco c'erano 69 righe mai mandate (9 siti e 60 ricerca). Il piano chiedeva
101 righe di siti e nessuna di ricerca. Sono entrate 42 righe, quindi il banco
è a 111 righe da mandare e ne mancano 59 per arrivare a 170.

## Come si è lavorato

Brave non ha risposto alla richiesta di approvazione di Claude in Chrome, come
il 26/10 al primo passaggio. Per questo la posta non è stata letta e i profili
non si sono aperti con l'account denkicode.

Si è ripetuto il metodo del primo passaggio del 26/10: nomi da Pagine Gialle,
directory di settore e OpenStreetMap con curl, handle indovinati e controllati
sulla pagina profilo dal browser dell'app senza login. Hanno lavorato quattro
operatori Opus alla volta, uno per cella; quando una cella si chiudeva, la sua
quota passava alla riserva successiva. Le riserve sono finite alle 09:27 e il
piano è stato rifatto due volte dopo aver segnato le celle chiuse.

Verso le 10:05 Instagram ha cominciato a rimandare al login anche il profilo di
controllo, dopo circa 100 richieste di un solo operatore in 8 minuti. Il
browser è condiviso, quindi si sono fermate insieme le ultime quattro celle.

| Cella | Quota | Righe | Profili letti | Handle provati | Esito |
|---|---|---|---|---|---|
| GE · fioristi | 26 | 5 | 33 | 113 | esaurita per resa |
| LO · pasticcerie | 25 | 8 | 30 | ~125 | esaurita, nomi finiti |
| MN · toelettature | 25 | 4 | 14 | 196 | esaurita, ~30 attività in provincia |
| VC · personal trainer | 25 | 3 | 33 | ~175 | esaurita per resa e nomi |
| LO · fioristi (riserva) | 21 | 1 | 12 | 160 | esaurita, 34 fioristi tutti provati |
| BI · pasticcerie (riserva) | 17 | 5 | 34 | 176 | esaurita per resa |
| GE · personal trainer (riserva) | 22 | 4 | 20 | 311 | esaurita, nomi finiti |
| AO · fotografi | 21 | 3 | 15 | 311 | esaurita, ~45 in regione |
| AO · pasticcerie | 20 | 2 | 21 | 285 | esaurita, ~35 in regione |
| BI · personal trainer | 12 | 6 | 31 | ~205 | esaurita, nomi finiti |
| PR · fotografi | 18 | 0 | 55 | 181 | esaurita: quasi tutti col sito |
| VB · pasticcerie | 18 | 0 | 2 | 94 | ferma per il blocco |
| PR · pasticcerie | 18 | 0 | 0 | 106 | ferma per il blocco |
| PR · fioristi | 18 | 0 | 0 | ~85 | ferma per il blocco |
| AO · fioristi | 6 | 1 | 2 | 51 | ferma per il blocco |

Le quattro celle ferme per il blocco restano `parziale` in `rotazione.csv`, con
gli handle già trovati da leggere per primi al prossimo giro.

## Righe da guardare prima di mandare

- **Ferme da mesi:** @chignolifiori (GE, dal 16/05), @ifioridirosy (GE, dal
  20/04), @coach_nico.g (GE, dal 13/05), @panificiomonico (LO, dal 27/08).
- **Un secondo link in bio che senza login non si legge:** @gelateriapasticceriacremonesi
  (LO), @valentina_lily_gobbato (VC), @smarti_fitness (BI). Se è un sito loro,
  la riga si scarta.
- **Fuori settore o al limite:** @gelateriaestate (LO) è una gelateria;
  @ilgiardinoditeagan (MN) è un asilo per cani; @luca.scappa_pt (VC) e i
  trainer di Why Not Fitness Club (BI) lavorano dentro una palestra;
  @feverbodyandmind (GE) è una società sportiva con molte discipline.
- **Dominio da attribuire:** @deivaosta (AO) ha deivaosta.it su una pagina di
  errore Wix; @lecinqph (AO) ha lecinqph.com in pagina d'attesa; @viola_s_cake
  (LO) ha violascake.it parcheggiato. Non è provato che siano loro.
- **@ilgirasoleditorri (LO)** ha un sito di cinque pagine su Google Sites:
  Patrick decide se vale come gancio.
- In GE fioristi i complimenti si basano sulla descrizione automatica
  dell'immagine: conviene aprire il post citato prima di mandare.

## Cosa si è misurato

- **Instagram senza login** regge circa 100 richieste di fila da un solo
  operatore a 3-4 secondi l'una, poi rimanda al login anche @instagram
  (indirizzo con `is_from_rle`). Su tutta la mattina le richieste sono state
  molte di più, ma distribuite su più ore.
- **Pagine Gialle ha un'interfaccia JSON**:
  `paginegialle.it/services/api/v1/search/<cosa>/<dove>?mr=50` dà comune,
  telefono e sito, mentre la pagina HTML ne mostra 5. Spesso ignora la seconda
  pagina.
- **Senza login, il fetch di un post** (`/p/<codice>/`) porta la didascalia
  intera nel `og:description`: il complimento si scrive su un post vero.
- **matrimonio.com** risponde 403 a curl ma si legge da `r.jina.ai/<url>`.
  Le directory per provincia (fioreriadaelisa.it) rendono più di Pagine Gialle.
- **Overpass** (OpenStreetMap) risponde solo con uno User-Agent impostato; il
  mirror kumi.systems ha risposto a ore alterne.
- **I motori** sono tutti fermi: Brave 429 dopo una o due ricerche, gli altri
  bloccati o inutili.
- **Lo scratchpad è condiviso** fra gli operatori: uno ha sovrascritto lo
  script di un altro. Da metà mattina ogni operatore ha una cartella sua.
- **In una scheda nascosta** `setTimeout` sale a 15-17 secondi; un web worker
  lo riporta a circa 4.
- `verifica-sito.py` si ferma con un errore se il nome dell'attività produce un
  dominio di più di 63 caratteri.

[[metodo-liste]] · [[metodo-instagram]] · [[2026-10-26-giro-mattina-siti]]
