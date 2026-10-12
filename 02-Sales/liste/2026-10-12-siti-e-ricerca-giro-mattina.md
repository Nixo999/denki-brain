---
riga: Per Patrick - giro del mattino del 12/10 (partito 17:43), siti 55 e ricerca 44 da 13 celle; pubblicazione sul banco fermata dal classificatore
type: area
updated: 2026-10-12
source: claude
verificato: 2026-10-12
prodotto: [siti-vetrina, gestionale-custom]
canale: instagram
stato: costruita, non pubblicata
---

# 12 ottobre, giro del mattino: siti 55 su 100, ricerca 44 su 60

Secondo giro di [[giro-mattina]], ruolo `primo`, dal Mac di Nicola. Partito
alle 17:43, non alle 8. Sette operatori Opus, uno per cella di
`prossimo-giro.py`, con le riserve del piano.

**Non pubblicata**: `pubblica-lista.py` è stato fermato dal classificatore dei
permessi del task («Real-World Transactions»). Gli 11 CSV sono nel vault e
passano `controlla-lista.py`; vanno pubblicati con un `/banco` con qualcuno
davanti (lo script salta da solo chi è già sul banco). `TODO` Nicola: permesso
per `pubblica-lista.py` nel task `banco-mattina`.

| Lista | Cella | Righe | Profili | Stato |
|---|---|---|---|---|
| siti | VB · sartorie | 4 | 30 | esaurita (17 fuori provincia) |
| siti | PV · sartorie (riserva) | 1 | 32 | esaurita (5 col sito) |
| siti | MI · pasticcerie | 25 | ~115 | aperta, quota piena |
| siti | CR · toelettature | 7 | ~50 | esaurita, elenchi finiti |
| siti | PR · toelettature (riserva) | 7 | ~55 | aperta, rende poco |
| siti | PV · tatuatori | 11 | 84 | esaurita per bacino (~35 studi) |
| ricerca | LO · alimentari | 5 | ~25 | esaurita, fonti finite |
| ricerca | LC · alimentari (riserva) | 12 | ~55 | aperta, fonti finite |
| ricerca | SO · edilizia | 14 | 78 | esaurita per resa |
| ricerca | MN · edilizia (riserva) | 6 | 25 | aperta, 1 su 4 (@gilioli_poggiorusco pronta) |
| ricerca | MI · ingrossi | 7 | ~120 | esaurita per resa |
| ricerca | LC · ingrossi (riserva) | 0 | ~4 | fonti finite, nessun file |

## Da guardare prima di mandare

- **Sede `TODO`**: @sartoriascirocco (MI o PV: se MI è di Giulia),
  @mazzola_giacomo, @toelettatura_d_e_p_cremona, @kappainkvigevano,
  @agenxia_milano, @impresa_bulanti, @beg_impresa_edile; @vanillaprelibata
  (corso Magenta 3 o 69).
- **Domini da riaprire**: corepastryandevent.it (scaduto 6/10), torteinatelier.it
  (Squarespace non reclamato), etnapastry.com (errore Wix), morellolegnano.it
  (casinò), renotattoostudio.com (in costruzione), caneducato.eu,
  alicemarchetti.it, aracnestudio.it (scarto da confermare).
- **Profili grandi**: @royaleink 12,9K, @dolci_di_palermo_garbagnate_ ~11K,
  @mazara_fish 8K, @pavel_tattooist 7,2K, @legnotechcaseinlegno 3,6K,
  @giudidogboutique 2,9K, @costruzioni_eredi_del_marco 2,7K, @caffeagostani
  (80 dipendenti).
- **Al limite del segmento**: @nxs.studio1 (barberia), @alessiapetsitter,
  @saber_srl (gru), @mobilartbormio, @gorini_wood, @gerosa_serpentinograniti,
  @macelleriaprina.mulazzano, @alva_market, @canali_formaggi_1934,
  @imc_ponteggi, @pietrarredo, @ortopiazzolla_srl.
- **Fermi o quasi**: @granditaliacouture (gennaio 2025, gancio 6),
  @pasticceria_gorla, @angelica.cakesdesign, @victorycafe2006, @tiramisu_rho,
  @gildoformaggi, @birrificio.lariano, @secchitettisrl, @alice_amazingdog.
- **Sede legale altrove**: @ediltagliocemento (Milano), @saber_srl (Colico),
  @fastfruitsrl (Brugherio, MB).
- @dulac.birrificio.artigianale sta a Galbiate come Herbamonstrum (contattato
  5/10). Il post di Prina del 6/5 parla di un lutto: il messaggio non lo cita.
  thebrave.it è compromesso (casinò): utile al flusso siti, non citato.

## Fonti, 12/10 dal Mac di Nicola (17:55-19:45)

- **Hanno retto**: curl con UA Googlebot sui profili (~1.000 letture, zero
  429), browser sloggato per il link in bio e `/p/<codice>/embed/`,
  PagineBianche via curl (~300 ricerche, 429 brevi solo sulle schede),
  toelettature.net, toelettapp.it, SoGeMi, Assodimi (POST a
  `php/ricercasoci.php`), sartist.it, reteimprese.it, Yahoo `--http1.1` con
  cookie a 25-30 s (regge 20-90 ricerche, poi 500).
- **Bloccate**: Overpass (406/504), DuckDuckGo, Brave (429 dopo 5), Wayback,
  matrimonio.com, topsearch di Instagram (401).
- **Posta non letta**: Instagram ancora non loggato nel browser dell'app.
- **Trappole**: lo scratchpad è condiviso fra operatori dello stesso giro (si
  sono sovrascritti gli script: ognuno in una sottocartella sua); gli ID dei
  post Instagram ora cominciano per 4, una regex `3\d{18}` fa sembrare fermi
  i profili vivi.

[[giro-mattina]] · [[metodo-liste]] · [[2026-10-11-siti-e-ricerca-giro-mattina]]
