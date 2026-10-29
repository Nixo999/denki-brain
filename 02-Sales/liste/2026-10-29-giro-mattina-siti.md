---
riga: Giro del 29/10 - 48 righe di siti su 49, banco a 169; DuckDuckGo via r.jina.ai e Instagram via curl senza blocchi, posta non letta
type: area
updated: 2026-10-29
source: claude
verificato: 2026-10-29
prodotto: [siti-vetrina]
canale: instagram
stato: bozza
---

# 29 ottobre: 48 righe di siti, quasi tutte le celle finite per nomi

Giro di [[giro-mattina]], ruolo `primo`, dal Mac di Nicola, partito alle 08:01.
Sul banco c'erano 121 righe mai mandate (61 siti e 60 ricerca). Il piano
chiedeva 49 righe di siti e nessuna di ricerca. Sono entrate 48 righe, quindi
il banco è a 169 righe da mandare.

## Come si è lavorato

Quattro operatori Opus hanno lavorato insieme, uno per cella; quando una cella
si chiudeva, la sua quota passava alla riserva successiva. Le tre riserve sono
state usate tutte, e Piacenza, che rendeva ancora una riga ogni due profili, ha
preso anche le 4 righe mancate da Genova. Instagram non ha mai rimandato al
login: gli operatori hanno letto quasi tutto con curl e il browser dell'app è
servito solo per i link in bio e la griglia dei post.

La posta non è stata letta. Per leggerla bisognava aprire una finestra di
Claude in Chrome in Brave, e il 28/10 Nicola ha chiesto di usare il browser
interno e non il suo ([[registro-trevis]]).

| Cella | Quota | Righe | Profili letti | Esito |
|---|---|---|---|---|
| VC · sartorie | 13 | 3 | 10 | esaurita per nomi: ~60 nomi, 13 col sito, 13 solo Facebook |
| MB · toelettature (riaperta) | 12 | 11 | ~48 | esaurita per nomi; nessun nome nei file di Giulia |
| BI · tatuatori | 12 | 2 | 2 | esaurita per nomi: 10 studi in provincia, 5 già in lista il 23/10 |
| VB · fioristi | 12 | 4 | 25 | esaurita per nomi |
| GE · sartorie (riserva) | 10 | 6 | 44 | esaurita per resa (1 su 7) |
| AO · tatuatori (riserva) | 8 | 8 | 21 | esaurita per nomi: ~20 studi in regione |
| PC · pasticcerie (riserva) | 10+4 | 14 | 24 | aperta, ma il bacino è quasi finito |

## Righe da guardare prima di mandare

- **Ferme da mesi:** @santotattooer (BI, dal 27/07), @pasticceria_ferrari (PC,
  dall'8/05), @diego_bertelli (AO, dal 18/02), @_goodvibesink_ (AO, dal 13/01),
  @matteolaintattoo (AO, dal 3/12/2025, sede incerta fra Aosta e Pont-Saint-Martin).
- **Link in bio nascosti senza login:** @cioccostyle e @carladenegri (GE). Se uno
  è un sito loro, la riga si scarta.
- **Al limite del settore:** a Piacenza tre gelaterie (San Marco, Il Gelatiere,
  Gelati e Sorrisi), @deg.dolcegelato e due forni (Frolla Couture, Manzotti); in
  MB tre toelettature con un pet shop loro (@bautique_villa_raverio_,
  @bauatelierseveso, @coccoletoelettaturalazzate) e @asiloitinerante, che fa
  più asilo e pensione che educazione.
- **Comune non scritto:** @magda_educatrice.cinofila e @asiloitinerante (MB).
- **Complimento da controllare sul post:** @igortattoobiella (BI) e
  @hanselegretel_pasticceria (PC) sono scritti dagli hashtag; @dogscout.monza ha
  due post in memoria di cani morti, da non citare.
- **Escluso da decidere:** @ilfioristabaveno (VB) ha il link in bio rotto, ma il
  titolare ha un sito vivo (maurobarcellinievents.com).

## Cosa si è misurato

- **DuckDuckGo letto tramite r.jina.ai funziona da motore**:
  `r.jina.ai/https://html.duckduckgo.com/html/?q=...`, anche con
  `site:instagram.com`. Gli operatori hanno fatto circa 300 ricerche in tutto a
  5-8 secondi l'una, con due risposte vuote e nessun blocco. Ha dato quasi tutti
  gli handle di oggi. DuckDuckGo chiamato direttamente risponde «anomaly».
- **Instagram con curl e user-agent di un crawler** (`Googlebot` o
  `facebookexternalhit/1.1`) restituisce follower, bio intera e didascalia dei
  post. L'operatore di MB ha provato 490 handle a 2,5-3 secondi l'uno senza
  blocchi. Con lo user-agent di un browser la didascalia non esce.
- **toelettature.net** ha un'interfaccia WordPress
  (`wp-json/wp/v2/listing?region=<id>`) che dà tutte le schede di una provincia;
  **miotattoo.it** ha i tatuatori per comune.
- Restano fermi: ricerca interna di Instagram senza login (404), Brave (429),
  Overpass (502 a ore), Cylex, Infobel e Facebook (verifica o login).
- Il «e altri N» dei link in bio non si apre senza login.

[[metodo-liste]] · [[metodo-instagram]] · [[2026-10-27-giro-mattina-siti]]
