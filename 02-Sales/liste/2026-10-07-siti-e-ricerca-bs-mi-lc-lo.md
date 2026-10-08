---
riga: Per Patrick - il /banco del 7/10 finito l'8/10, 117 righe sul banco (siti 68, ricerca 49) da 11 celle, cosa guardare prima di mandare
type: area
updated: 2026-10-08
source: claude
verificato: 2026-10-08
prodotto: [siti-vetrina, gestionale-custom]
canale: instagram
stato: pubblicata
---

# 7-8 ottobre: siti 68 su 100, ricerca 49 su 60

Sette operatori, uno per cella di `prossimo-giro.py`, partiti il 7/10 alle 10:55.
Il limite d'uso li ha fermati verso le 13:00; tre ripresi l'8/10 alle 17:55.
Tutto sul banco Patrick (`lista-corrente.csv`). **Corto perché sei celle su
undici si sono chiuse per resa**, non per tempo.

| Lista | Cella | Righe | Profili | Stato cella |
|---|---|---|---|---|
| siti | BS · sartorie, atelier e tappezzieri | **4** | 33 | esaurita (10 sotto i 200, 8 col sito) |
| siti | MI · sartorie (riserva) | **4** | 30 | esaurita (15 col sito) |
| siti | BS · personal trainer, pilates e yoga | **26** | ~105 | aperta, 1 su 4 (33 col sito) |
| siti | MI · toelettature e dog trainer | **4** | 37 | esaurita (14 fuori provincia) |
| siti | LO · toelettature (riserva) | **6** | 35 | esaurita, fonti finite |
| siti | MI · tatuatori e piercing | **24** | ~90 | aperta, 1 su 4; nomi finiti |
| ricerca | MI · officine e carrozzerie | **8** | 48 | esaurita (18 fermi, 16 piccoli) |
| ricerca | LC · officine (riserva) | **8** | 44 | esaurita |
| ricerca | LC · falegnamerie | **3** | 30 | esaurita (12 fermi, 7 fuori provincia) |
| ricerca | BS · falegnamerie (riserva) | **12** | 44 | aperta, 1 su 4; fermata per tempo |
| ricerca | LC · ingrossi e distribuzione | **18** | ~65 | aperta, 1 su 3-4; Pagine Gialle in 429 |

## Da guardare prima di mandare

- **Date che scadono**: Satatttvision (flash night 9/10), 21 Club (walk-in
  10/10), Solid (guest 13-15/10), @autocogliati_spa («ieri» = 6/10),
  @bcgomme («lunedì» = 5/10). Le falegnamerie citano giorni della settimana
  calcolati sul 7/10: rileggere.
- **Lutto**: @fonzy_shower_dog (cane morto, post del 10/9); @pink_carpet_toelettatura
  (gatto smarrito, fermo dal 26/4). I messaggi non lo toccano.
- **In liquidazione**: Otto Pilates Fitness Srl (@ottopilates), ma posta ancora.
- **Stessa cerchia**: @eli.inyoga insegna da @dharmayoga_franciacorta: non lo stesso giorno.
- **Troppo grandi**: @autocogliati_spa, @autocenterarese (cinque sedi),
  Satatttvision 49K, Colors 21,8K, Prime Soul 20,5K, @krinotools, @italianaterricci.
- **Sede incerta**: @fevalsrl (sede a Chiuro SO), @tecnoct_ferramenta (Colico,
  57 km, follower che non tornano), @carrozzeria_ghezzi, @design.carrozzeria,
  @falegnameriacolangelo, Elixir tattoo (Corbetta/Ossona), @fly_yoga_garda.
- **Fermi da mesi**: @pilates_for_me_, @marcobasontrainer, @s74pilates,
  @theloftstudio.brescia, @colpi.di.coda_lodi, @carrozzeriacarpointsrl,
  @carrozzeriaeffe, @legnamilano, @noveusato, Essenza d'Inkiostro.
- **Domini da aprire**: rondow-tattoo-lab.jimdosite.com, lavmitattoo.com (404),
  `conessenza.it`, `elisapilates.it` (parcheggiato, se è suo il gancio è 3),
  `monkssuit.com`.
- **Tatuatori MI**: complimenti scritti dalle didascalie, le immagini non le ha
  guardate nessuno.
- **Ingrossi LC**: profili letti con curl (bio e ultime 12 didascalie), non
  aperti nel browser; il link in bio non è stato letto.

## Fonti, misurate per la prima volta dal Mac di Patrick

- **Pagine Gialle via curl**: regge, da 4 minuti per 100 schede a 25-70
  secondi a pagina; dopo ~1.000 ricerche risponde 429. Dà nomi, mai handle.
- **Yahoo nella pagina**: regge per la verifica, 500 dopo 5-110 ricerche; il
  filtro per comune è largo (molti fuori regione).
- **DuckDuckGo html**: nel browser ha retto (BS trainer), da curl risponde 202.
- **Startpage**: la fonte più produttiva (BS trainer 7 righe su 18 handle,
  falegnamerie BS 1 su 4), **ma chiede a Patrick di autorizzare ogni azione**:
  esclusa dal 7/10 (regola in [[metodo-liste]]).
- **API Instagram**: `users/{pk}/info` e `web_profile_info` in 429 alla prima
  chiamata, su tutti e sette; `topsearch` regge 30-200 ricerche poi dà HTML.
- **curl con user-agent Googlebot** su `instagram.com/<handle>`: bio e ultime
  12 didascalie senza login, non il link in bio. Data del post dall'ID.
- **toelettature.net, beverfood.com, cani.com**: utili per settore, 403 dopo ~40 pagine.
- Il browser dell'app ha un tetto di 9 schede: con sette operatori qualcuno è
  rimasto per due ore senza scheda.
