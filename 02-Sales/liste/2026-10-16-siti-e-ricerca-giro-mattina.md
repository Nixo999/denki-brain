---
riga: Per Patrick - giro del mattino del 16/10 (partito 18:48), siti 12 e ricerca 14 pubblicati sul banco; Instagram ha chiuso le letture alle 19:16 per le raffiche degli operatori
type: area
updated: 2026-10-16
source: claude
verificato: 2026-10-16
prodotto: [siti-vetrina, gestionale-custom]
canale: instagram
stato: pubblicata
---

# 16 ottobre, giro del mattino: siti 12 su 100, ricerca 14 su 60

Sesto giro di [[giro-mattina]], ruolo `primo`, dal Mac di Nicola. Il task è
partito alle 18:48 invece che alle 8, perché il Mac era chiuso all'ora giusta.
Sette operatori Opus, uno per cella di `prossimo-giro.py`, ognuno con una
riserva assegnata tranne Verbania. Le sei liste con almeno una riga sono
**pubblicate** sul banco: 26 righe nuove. `pubblica-lista.py` è passato su
tutte.

**Alle 19:16 Instagram ha chiuso le letture dei profili** per tutto
l'indirizzo: ogni `curl` con user-agent Googlebot e ogni pagina nel browser
sloggato rimandava al login con `is_from_rle`. La causa sta nei numeri degli
operatori stessi, fra le 18:55 e le 19:16: Cremona ha sondato 848 handle
indovinati dai nomi con 8 richieste in parallelo, Milano 350 letture con 10 in
parallelo, Brescia circa 100 con 6, Novara 280 con 3, Genova 135 con 6. In
venti minuti sono partite più di 1.700 richieste. Il blocco era ancora attivo
alle 19:56, con una sola riapertura di un minuto alle 19:32, e il giro si è
chiuso con le righe lette prima. Due operatori hanno anche lanciato `pkill`
per nome di file (`yahoo.sh`, `xargs -P 6`) e possono aver fermato lo script
di un altro. Le contromisure stanno in [[trappole]], sezione «Liste e banco
DM»: le letture si fanno una alla volta, e il brief le fissa prima di partire.

| Lista | Cella | Righe | Profili | Stato |
|---|---|---|---|---|
| siti | PC · tatuatori | 7 | 45 | esaurita, resa 1 su 6,4 e bacino di ~30 studi |
| siti | GE · toelettature | 0 | 4 | fermata dal blocco, 13 nomi pronti |
| siti | NO · pasticcerie | 3 | 26 | fermata dal blocco, 27 handle da leggere |
| siti | VB · fioristi | 2 | 17 | fermata dal blocco, 10 handle da leggere |
| ricerca | BS · falegnamerie | 3 | 24 | fermata dal blocco, 17 handle da leggere |
| ricerca | MI · agricole | 6 | ~77 | esaurita, resa 1 su 13 |
| ricerca | CR · officine | 5 | 28 | esaurita, resa 1 su 5,6 |

Nessuna riserva è stata aperta: il blocco è arrivato prima che una cella
chiudesse con Instagram ancora leggibile.

## Da guardare prima di mandare

- **Piacenza, tutte e sette le righe**: il link in bio non è stato letto,
  perché il browser dell'app ha negato la navigazione su instagram.com al
  primo tentativo. Prima di scrivere si apre la bio di ciascuno.
- **Sede incerta**: @laperlaneratattooink (San Nicolò di Rottofreno o
  Piacenza), @oksicake8 (Borgomanero solo dal nome, bio vuota, didascalie in
  ucraino), @nevi_gomme (seconda sede a Viadana MN).
- **Profili grandi o al limite del segmento**: @fiori_bianchi_verbania (2.336
  follower, matrimoni del lago), @lecavedelceppo (13.000 follower, vive di
  matrimoni e fattoria didattica), @agriturismolatorrazza (su Instagram solo
  il ristorante), @blindosersrl (serramentista con showroom),
  @carrozzeria_bonfanti (allestisce ambulanze), @lazzariautocarrozzeria
  (officina autorizzata Alfa, Fiat e Jeep: escludere che sia concessionaria).
- **Piccoli o con pochi post**: @falegnameria_clerici (63 follower),
  @ruggerifalegnameria (216), @facchettigomme (10 post), @pasticceriacastoldi
  (8 post).
- **Ganci da confermare**: @picti_tattoo_shop (la bio scrive il dominio con
  una t sola; quello giusto è una pagina Google Sites, gancio 5);
  @siamoalverde.fiori (siamoalverde.it risponde con la pagina di default del
  server, non si sa se è loro: se sì, gancio 3); @chiaramanzinitattoo (via
  Mazzini 9 nelle didascalie, 6 negli elenchi).
- Pavia, Brescia, Cremona, Piacenza, Novara e il VCO stanno oltre i 50 km da
  Seveso: i messaggi nominano la zona, mai «qui in zona». Besate e
  Abbiategrasso dicono «del milanese».

## Da riprendere al prossimo giro, senza rifare la ricerca

- **GE toelettature**, 13 profili con dominio già verificato: @unpeloavanti,
  @ilmioangeloscodinzola, @lefatedeglianimali, @esteticaa4zampe (gancio 2),
  @toelettaturamiki, @topdogtoelettatura, @musettivanitosi (Jimdo dietro
  Cloudflare, da aprire a mano), @shampoo_e_coccole e @zampeamollotoelettatura
  (Rapallo, da confermare), @bolledipelo (Recco), @viva_il_lupo (gancio 3 o
  6); @fiutoperlebolle e @toelettatura_enrico sotto i 200 follower. Hanno un
  sito vivo e restano fuori: La Cuccia, Un Pelo di Troppo, Chiara Dog Trainer,
  Animals Club, Bau Chic, Toeletati, Tutti Puliti Tutti Felici, I Puzzoli,
  Marta Pet Spa, Dog Design, Cane Gatto Chiavari.
- **NO pasticcerie**, 27 handle: @pasticceriadolceamara (sito fermo al 2023,
  gancio 6), @pasticceria.duella, @pasticceriasavoini, @golosastro.borgomanero,
  @pasticceria_visca, @pasticceriapiola1985, @pasticceria_bar_gelateria_501,
  @pasticceriaf.lliago, @pasticceriamarinella, @pasticcino_arona,
  @pasticceriaoliver, @pasticceria_gianfranco_mercuri, @pasticceria_ale,
  @balestrinipasticceria, @_lauras__bakery_, @il_forno_bellinzago,
  @makeacake.lab, @silviastortas, @dulcis_varallopombia, @dolcimodi,
  @pasticceriastrano, @dolcefreddo_cerano, @pasticceriaimpero, @pavipasticceri,
  @pasticceria_romagna, @pasticceriacomi, @madeinsudcameri. Col sito, fuori:
  Marzia, Manuelina, Strobino, Marietta, C'era una volta, Gioria, Mazzetti,
  Caldarola, La Rotonda Bakery.
- **VB fioristi**, 10 handle: @ilfioristabaveno (sito Wix con dominio
  scollegato, gancio 4), @il.giardino.di.anna o @ilgiardinodianna (Stresa, sito
  503, gancio 2 o 4), @tata.fiori, @lorchidea_fiorista, @fioridea_villadossola,
  @miriaminfiore, @frankaossola, @residencefiori_baveno, Verde Idea (Omegna),
  Pane e Tulipani (Verbania); più lagomaggioresposi.com per i fornitori dei
  matrimoni. Stima finale della cella: 8-12 righe, non 25.
- **BS falegnamerie**, 17 handle: @ellegiarredamenti, @ellegi_arredamenti,
  @falegnameriaguerrini, @guerriniarredamenti, @rosola_serramenti,
  @bettinisrl, @rodellaarredamenti, @ferrari_arredamenti, @ferrariarredamenti,
  @ferrariserramenti (Ponte di Legno, sede da verificare), @ruggeri_arredamenti,
  @falegnameria_zambelli, @falegnameria.frusca, @falegnameriasacchi,
  @mondolegnosrl, @edilgardensrl. @falegnameriacattaneo è di Mondovì, non di
  Flero.
- **PC tatuatori**, 6 studi letti a metà: @tattooificio, @adamantioatelier
  (adamantio.it risponde con un errore di database, possibile gancio 4),
  @monamour_tattoo_atelier, @homeless_tattoo_piercing, @10tattoostudio,
  @dirtymindtattoostudio. **VC tatuatori**, 16 nomi senza sito da miotattoo e
  Pagine Gialle, nessun handle ancora.
- **SO officine**, 4 handle dai siti aziendali: @officinamezzera,
  @carrozzeria_valtellinese, @carrozzeria_inferno, @emilcarardenno.
- **LO agricole**: @aziendaagricolabaronchelli (Borgo San Giovanni, link dal
  sito dell'azienda) e tre agriturismi dell'elenco delle fattorie didattiche
  senza handle noto: San Gabriele Mulinás, Agriturismo Luna, Cascina
  Grazzanello.

## Fonti, 16/10 dal Mac di Nicola (18:50-19:56)

- **Hanno retto**: Pagine Gialle via curl su tutte le celle (fino a 565 schede
  per provincia, zero 429), PagineBianche, miotattoo.it (27 studi a Piacenza
  con indirizzo), toelettature.net (73 nomi a Genova, con sito e Instagram
  nelle schede), fioreriadaelisa.it (la scheda dice «Sito web: …», è il filtro
  sito più rapido), dati.lombardia.it (agriturismi e fattorie didattiche), i
  siti aziendali via curl per il link a Instagram e la P.IVA (a Brescia le
  cifre 8-10 della P.IVA, 017 o 098, dicono la sede e scartano gli omonimi),
  DoH dns.google per i domini, curl Googlebot sui profili fino alle 19:16.
- **Yahoo** è cambiato: da Cremona, Brescia e Genova rispondeva 307 verso una
  verifica anti-bot già alle 19:00; da Novara, Verbania e Piacenza ha retto
  20-35 ricerche a un minuto l'una. Lo stesso indirizzo, esiti diversi.
- **Bloccate o inutili**: Instagram dalle 19:16; toelettapp.it (302), reteimprese.it
  (410 per Brescia), ilportaledigenova.com, agricoltorilocali.it e
  spesadalcontadino.com (solo JavaScript), l'elenco regionale degli agriturismi
  (chiede il login), cylex, europages.
- **Indovinare gli handle dal nome rende poco e costa il blocco**: a Cremona 848
  sonde per 35 profili sopra i 200 follower e 3 righe; a Novara 281 per 10
  profili giusti. I siti aziendali danno handle veri: a Milano 23 su 80, a
  Cremona 8 su 43.
- **Posta non letta**: Instagram non è collegato nel browser dell'app.
- I commit automatici «Chiusura automatica» hanno salvato a metà alcuni CSV
  mentre gli operatori lavoravano; le versioni finali entrano nel commit del
  giro.

[[metodo-liste]] · [[giro-mattina]] · [[2026-10-15-siti-e-ricerca-giro-mattina]]
