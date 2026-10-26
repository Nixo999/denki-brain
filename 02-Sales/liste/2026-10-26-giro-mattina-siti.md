---
riga: Giro del 26/10 - 24 righe di siti su 110 in sette celle, tutte chiuse; nomi da Pagine Gialle e handle indovinati, profili letti senza login
type: area
updated: 2026-10-26
source: claude
verificato: 2026-10-26
prodotto: [siti-vetrina]
canale: instagram
stato: bozza
---

# 26 ottobre: 24 righe di siti con Instagram non collegato

Giro di [[giro-mattina]], ruolo `primo`, dal Mac di Nicola, partito alle 08:01.
Sul banco c'erano 60 righe mai mandate, tutte di ricerca. Il piano chiedeva 110
righe di siti in quattro celle, e le tre riserve sono state usate tutte. Sono
entrate 24 righe, quindi il banco resta a 86 righe dalle 170.

## Come si è lavorato

Brave non ha risposto alla richiesta di approvazione, quindi la posta non è
stata letta. Il browser dell'app invece **legge le pagine profilo di Instagram
anche senza login**: bio, link, storie in evidenza e una decina di post con la
descrizione dell'immagine. La ricerca e le API di Instagram restano chiuse.

I nomi vengono da Pagine Gialle con curl, più OpenStreetMap, toelettatura.info
e toelettature.net. L'handle si indovina dal nome e si controlla con `fetch`
della pagina profilo, leggendo il `meta og:description`. Ha reso fra un handle
esistente su 5 e uno su 12, e molti esistenti erano omonimi di altre città.

Cinque operatori Opus, uno per cella, hanno lavorato circa 75 minuti ciascuno.

| Cella | Quota | Righe | Profili letti | Handle provati | Chiusa perché |
|---|---|---|---|---|---|
| AL · pasticcerie | 29 | 5 | 31 | 289 | resa |
| GE · toelettature | 27 | 8 | 29 | ~330 | nomi finiti (resa 1 su 3,6) |
| AL · personal trainer | 27 | 2 | 30 | ~120 | resa |
| BG · sartorie | 27 | 2 | 30 | 409 | resa |
| AO · toelettature (riserva) | 25 | 2 | 8 | 267 | nomi finiti, ~12 attività in regione |
| VC · pasticcerie (riserva) | 24 | 4 | 30 | 417 | resa |
| VC · fioristi (riserva) | 25 | 1 | 41 | 326 | resa |

Gli scarti per cella stanno nella colonna `Nota` di `rotazione.csv`.

## Righe da guardare prima di mandare

- @gretajyoti_ e @osteopatia_pilates_casale (AL): l'ultimo post è di agosto.
- @patrizia_altieri_couture (BG): sembra un marchio di maglieria più che una
  sarta, e non pubblica da agosto. Patrick decide se mandare.
- @pasticceria_rossa e @pasticceria_ferraris (VC): ferme a fine luglio.
- @il_mulino_dei_fiori (VC): è più un centro giardinaggio che un fiorista.
- @lo_stregatto_toelettatura (GE): fermo dal 13/08.

## Cosa si è misurato

- **Brave Search con curl** regge circa 8 ricerche, poi risponde con una pagina
  di blocco fissa di 77419 byte, o 429 se l'hanno già consumato altri.
- **Bing** ignora `site:` e dà risultati di Ravenna. DuckDuckGo, Mojeek,
  Qwant, matrimonio.com, Cylex rispondono con un blocco.
- **La rete di questo Mac** (filtro WindTre Home Protect) intercetta alcuni
  domini, per esempio `*.webnode.it`: curl legge la pagina del filtro.
  `curl --doh-url https://cloudflare-dns.com/dns-query` legge il sito vero.
  `verifica-sito.py` usa il DNS di sistema e sbaglia allo stesso modo.
- **In una scheda nascosta** le pause con `setTimeout` salgono a 5-10 secondi;
  un `MessageChannel` o un web worker riporta il ritmo a circa 2,5 secondi.
- **Pagine Gialle** dà spesso la stessa lista provinciale per ogni comune:
  rende di più cambiare categoria che comune.
- Alcuni domini vecchi di pasticcerie rimandano a siti di casinò
  (pasticceriabonadeo.it, pasticceriacasali.it).

[[metodo-liste]] · [[metodo-instagram]] · [[2026-10-25-giro-mattina-fermo]]
