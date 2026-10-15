---
riga: Per Patrick - giro del mattino del 15/10 (partito 9:10), siti 43 e ricerca 36 pubblicati sul banco; quasi tutte le celle esaurite per resa o fonti
type: area
updated: 2026-10-15
source: claude
verificato: 2026-10-15
prodotto: [siti-vetrina, gestionale-custom]
canale: instagram
stato: pubblicata
---

# 15 ottobre, giro del mattino: siti 43 su 100, ricerca 36 su 60

Quinto giro di [[giro-mattina]], ruolo `primo`, dal Mac di Nicola, partito alle
9:10. Sette operatori Opus, uno per cella di `prossimo-giro.py`, ognuno con una
riserva assegnata (la cella PC sartorie senza riserva, perché le riserve del
piano erano tre per quattro celle). Tutte le liste sono **pubblicate** sul banco:
79 righe nuove, più le 11 dei fioristi di Lecco del 13/10, mai pubblicate prima
e contate nella quota di oggi. `pubblica-lista.py` è passato senza fermarsi.

Verso le 9:50 la rete è caduta per qualche minuto e ha fermato quattro operatori;
li ho ripresi e hanno finito. Quasi tutte le celle si sono chiuse per resa
bassa o per fonti finite: per questo le quote non si sono riempite.

| Lista | Cella | Righe | Profili | Stato |
|---|---|---|---|---|
| siti | LC · fioristi | 2 + 11 del 13/10 | 44 | esaurita, fonti finite |
| siti | LO · fioristi (riserva) | 5 | ~28 | aperta, nomi quasi finiti |
| siti | BS · personal trainer | 3 | 30 | esaurita (9 col sito) |
| siti | VB · personal trainer (riserva) | 7 | ~40 | aperta, Yahoo fermo |
| siti | VB · fotografi | 6 | 55 | esaurita (20 omonimi, 9 col sito) |
| siti | PV · fotografi (riserva) | 3 | ~25 | aperta, cercato poco |
| siti | PC · sartorie | 6 | 38 | esaurita, elenchi finiti |
| ricerca | LC · ingrossi | 1 | ~30 | esaurita, non stanno su Instagram |
| ricerca | PV · ingrossi (riserva) | 5 | ~45 | aperta, rende 1 su 9 |
| ricerca | LC · alimentari | 3 | 35 | esaurita, già nelle liste del 5 e 12/10 |
| ricerca | PV · alimentari (riserva) | 10 | ~40 | aperta, rende 1 su 4 |
| ricerca | BG · edilizia | 17 | 143 | aperta, fonti finite |

## Da guardare prima di mandare

- **Sede incerta**: @tatianaferrariofotografa (scrive solo «VCO e Alto
  Novarese»), @ericaferrari_fotografa (Masera viene da matrimonio.com),
  @luna.photographyfamily (Pavia e Milano), @bottega_della_sarta (sede dal solo
  nome), @glemserramenti (Dalmine o Curno).
- **Profili grandi**: @molinovigevano 32K, @jonigjepali 9K (ultimo post 12/5),
  @impresa_bergamelli 6,8K, @jessicaflowerslab 3,4K (bio in inglese),
  @auto.tappezzeria 2,4K, @cignolielettroforniture.
- **Al limite del segmento**: @neri.cillis (link in bio a gmail.com, dipendente
  del Castello del Sole), @cb_osteopilates e @mandir_cannobio (centri con più
  professionisti), @danilo_nolli_photo, @boutique_sorellevecchia (vende anche
  capi finiti), @raviolificiogaddi (137 follower), @pasticceriabordoni,
  @termocommerciale (190 follower), @impresavirgiliogherardi (10 follower).
- **Fermi o quasi**: @coriofiori (27/4), @fiorartenegozio (24/5), @milli.garden
  (1/6), @pericorenatosrl (13/7), @distilleriabellomi (9/8),
  @cb_osteopilates (17/3).
- **Abbinamento per indizi**: @gambaserramenti, @sgssistemi,
  @bonacinacostruzioni (il sito linka un altro handle), @marengosrl.
- **Stesso indirizzo**: @tractor.ricambi.pavia e @ferramenta_sardi (via
  Vigentina 9/11, Pavia): non lo stesso giorno.
- @luppolina_birraagricola è anche azienda agricola: controllare che non sia
  nelle liste agricole di Lecco. Nel messaggio di @impresaedileazzola il «ieri»
  è diventato «il 14 ottobre».
- Pavia e la Bergamasca stanno oltre i 50 km da Seveso: i messaggi nominano la
  zona vera, mai «qui in zona».

## Fonti, 15/10 dal Mac di Nicola (9:10-10:30)

- **Hanno retto**: curl con UA Googlebot sui profili (~1.200 letture, zero 429,
  le date dei post ricavate dall'ID), il browser dell'app sloggato per il link
  in bio, PagineBianche e PagineGialle via curl, fioreriadaelisa.it,
  yogapills.it (nuova, rende più dei motori), sartist.it, reteimprese.it, i
  siti aziendali, le @menzioni nei post dei produttori già in lista.
- **Yahoo** con `--http1.1` e pause di 25-30 s regge 25-80 ricerche, poi
  risponde 500. È stato il limite di quasi tutte le celle.
- **Bloccate o inutili**: Bing e Startpage via curl (nessun risultato),
  DuckDuckGo html (202), l'API di Instagram (401), cylex (403), europages.
- **Posta non letta**: Instagram non è collegato nel browser dell'app.
- Un commit automatico «Chiusura automatica» ha salvato a metà alcuni CSV
  mentre gli operatori lavoravano; le versioni finali entrano nel commit del
  giro.

[[metodo-liste]] · [[giro-mattina]]
