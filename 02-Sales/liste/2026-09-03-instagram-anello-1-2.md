---
type: area
updated: 2026-09-03
source: claude
prodotto: siti-vetrina
canale: instagram
anello: 1-2
stato: inviata
---

# Lista Instagram — bellezza, per il 3 settembre 2026

**33 righe nuove, verificate una per una il 3 settembre 2026.** Metodo:
[[metodo-instagram]]. Messaggio: la **versione C** di [[dm-instagram-vetrina]],
quella che annuncia la bozza già fatta — decisa oggi in
[[2026-09-03-bozza-gia-fatta]].

Sono partite tutte e 33 la sera stessa — il conto dell'invio è più sotto.
`lista-corrente.csv` è pubblicata e il [banco DM](../strumenti/banco-dm.html)
è installato sul MacBook di Patrick. **In coda ci sono anche le 47 righe del
2 settembre**, che non erano mai partite: il testo è stato riscritto anche per
loro, quindi in tutto il banco ha **80 conversazioni**, cioè quasi tre giorni
al tetto di 30.

Segmento: **bellezza** — parrucchieri, estetiste, barber, unghie e ciglia, cioè
i tre segmenti che [[2026-08-30-verifica-siti-giulia]] dà come i più scoperti.
Nessuna riga in Monza Brianza o Milano, e nessuna che compaia in una lista
telefonica: il controllo incrociato sui 315 nomi già in archivio non ha trovato
sovrapposizioni.

## Perché si è aperto l'anello 2

**Sull'anello 1 la bellezza è quasi finita, ed è un numero, non un'impressione.**
Sui 38 candidati raccolti nella prima tornata di ricerche, **17 erano già in una
lista precedente**: il 45%. Quando quasi una ricerca su due ripesca un profilo
già contattato, l'anello non ha più molto da dare su quel segmento.

Da lì si è aperto il secondo anello — Gallarate, Busto Arsizio, Cassano
Magnago, Samarate, Treviglio, Caravaggio — dove il tasso di duplicati è tornato
sotto il 10%. **Treviglio da sola ha dato 7 righe buone**: è il posto da cui
ripartire domani.

## Cosa è stato verificato, e cosa no

| Controllo | Come | Esito |
|---|---|---|
| **L'attività esiste, e dove** | Ricerca mirata per nome e comune: indirizzo, telefono, orari, recensioni | ✅ tutte e 33 |
| **Il dominio è vivo o morto** | DNS su due risolutori autorevoli (Google e Cloudflare), con un dominio noto-vivo come controprova | ✅ affidabile |
| **Cosa c'è sulla pagina** | **Il sito aperto davvero**: codice HTTP, motore, versione, anno di copyright, e nei casi dubbi la pagina letta nel browser | ✅ **novità di oggi** |
| **Il profilo Instagram è vivo** | Solo dai risultati di ricerca | 🟡 **non aperto a mano** |
| **Follower** | Solo dove il motore li riportava | 🟡 **11 righe su 33** |

> [!warning] Le due cose che oggi non ho potuto fare, e vanno dette
> **Instagram non si apre da questa macchina.** Né il browser del pannello né
> `curl` passano il muro del login: ogni profilo risponde «Profile non è
> disponibile» o restituisce la pagina vuota. Quindi il controllo «l'account
> esiste ancora» di [[metodo-instagram]] — quello che sul primo giro aveva
> pescato 7 profili morti su 74 — **oggi è appoggiato ai risultati di ricerca,
> non all'occhio.** Il costo è basso e cade su Patrick: se un account non c'è
> più, `ig.me` non apre niente e si passa alla riga dopo.
> **I follower mancano su 22 righe su 33**, e non sono stati inventati: dove
> non li ho letti c'è scritto `n.d.`.

## Quello che invece oggi è migliorato

Il 1 e il 2 settembre le pagine dei siti piccoli non si aprivano, e per questo
le liste avevano **solo i ganci 1 e 5**. Da questo Mac si aprono: sono tornati
in gioco il **6** (sito vivo ma vecchio) e la lettura del motore, del copyright
e della versione. Da lì sono usciti i due casi migliori della lista dopo i
domini morti — Ninfea, ferma a WordPress 6.1.1, e Hair Center Simona, con una
pagina Aruba del 2015 che rimanda solo a Facebook.

**Quattro domini morti su 33 righe.** È il gancio più forte che esista
([[metodo-instagram]]) e non si trova senza aprire il DNS: quattro attività
hanno pagato un sito che oggi non risponde più, e le loro pagine sono ancora
nell'indice di Google.

---
## Como e provincia — anello 1 · 6

| # | Account | Attività | Comune | Fw | G | Cosa ho verificato |
|---|---|---|---|---|---|---|
| 1 | `@beautyzone_olgiatecomasco` | BeautyZone | Olgiate Comasco | 688 | **2** | Dominio morto: beautyzoneolgiate.it non risolve più |
| 2 | `@hcparrucchieri_olgiate` | HC Parrucchieri | Olgiate Comasco | 450 | **4** | L'unico sito che risulta è una scheda Google che dà 404 |
| 3 | `@beautyfarm_appianogentile` | Beauty Farm | Appiano Gentile | n.d. | **2** | Dominio morto: beautyfarm-como.com non risolve più |
| 4 | `@sararusso_beauty` | Little Beauty Diamond | Appiano Gentile | n.d. | **1** | Nessun sito: solo Fresha e Facebook |
| 5 | `@newfantasy_parrucchieri` | New Fantasy Acconciature | Lurate Caccivio | 3199 | **1** | Nessun sito: solo directory, Fresha e Facebook |
| 6 | `@betty_style_lurate_caccivio` | Betty Style | Lurate Caccivio | 275 | **1** | Nessun sito: solo Facebook |

## Lecco e provincia — anello 1 · 3

| # | Account | Attività | Comune | Fw | G | Cosa ho verificato |
|---|---|---|---|---|---|---|
| 7 | `@cinzia_estetica_osnago` | Cinzia Estetica e Parrucchieri | Osnago | n.d. | **2** | Dominio morto: cinziaparrucchieriestetica.it non risolve più |
| 8 | `@ninfeaesteticabarzano` | Ninfea Estetica e Benessere | Barzanò | n.d. | **6** | Sito vivo ma fermo: WordPress 6.1.1, di fine 2022 |
| 9 | `@sabry_hairsalon` | Sabry Hair Salon | Oggiono | 525 | **1** | Nessun sito: solo Fresha e Facebook |

## Varese e provincia — anello 1 e 2 · 16

| # | Account | Attività | Comune | Fw | G | Cosa ho verificato |
|---|---|---|---|---|---|---|
| 10 | `@londacislago` | L'Onda Acconciature | Cislago | n.d. | **1** | Nessun sito: solo directory e Facebook |
| 11 | `@blackstar_parrucchiere` | Black Star | Gerenzano | n.d. | **1** | Nessun sito: solo Fresha e Instagram |
| 12 | `@sb.esteticaeunghie` | SB Estetica e Unghie | Caronno Pertusella | n.d. | **1** | Nessun sito: solo Treatwell |
| 13 | `@pettinatobiagio_parrucchiere` | Kreatif Studio | Tradate | n.d. | **1** | Nessun sito: solo Facebook e directory |
| 14 | `@barbershop.tradate.bandidos` | Barber Shop Bandidos | Tradate | 9314 | **2** | Dominio morto: barbershop-bandidos.it non risolve più |
| 15 | `@iltuostile.cdj` | Il Tuo Stile - Degradé Joelle | Tradate | n.d. | **5** | Su piattaforma: il sito è una pagina Treatwell |
| 16 | `@beauty.and.charme` | Beauty & Charme | Castiglione Olona | n.d. | **1** | Nessun sito: solo Fresha e Instagram |
| 17 | `@massimoesimone_barbershop` | Massimo & Simone Barbershop | Gallarate | n.d. | **1** | Nessun sito: solo Treatwell, Uala e directory |
| 18 | `@hh_salon_gallarate` | H&H Salon | Gallarate | n.d. | **1** | Nessun sito: solo directory locali |
| 19 | `@diamond_gallarate` | Diamond Beauty Studio | Gallarate | n.d. | **1** | Nessun sito: solo Fresha e Facebook |
| 20 | `@adelis_beauty_gallarate` | AdeliS Beauty | Gallarate | n.d. | **1** | Nessun sito: solo Instagram e WhatsApp |
| 21 | `@estetica_il_sogno` | Estetica Il Sogno | Busto Arsizio | n.d. | **1** | Nessun sito: solo Treatwell, Fresha, Groupon e CutApp |
| 22 | `@next.bustoarsizio` | Next Beauty Clinique | Busto Arsizio | n.d. | **5** | Su piattaforma: le prenotazioni girano su un sottodominio Reservio |
| 23 | `@noemiemotion` | Noemi Emotion | Cassano Magnago | 1097 | **1** | Nessun sito: solo Fresha, Groupon e Facebook |
| 24 | `@lucaparrucchiere` | Luca Parrucchiere | Cassano Magnago | 404 | **4** | L'unico sito che risulta è una scheda Google che dà 404 |
| 25 | `@beauty_unique_va` | Beauty Unique | Varese | 2700 | **1** | Nessun sito: solo Fresha e Facebook |

## Bergamo — anello 2 · 8

| # | Account | Attività | Comune | Fw | G | Cosa ho verificato |
|---|---|---|---|---|---|---|
| 26 | `@haircentersimona` | Hair Center Simona | Treviglio | 1533 | **6** | Sito vivo ma del 2015: manda solo a Facebook, di Instagram nessuna traccia |
| 27 | `@club_parrucchieri_treviglio_` | Club Parrucchieri | Treviglio | n.d. | **1** | Nessun sito: solo directory locali |
| 28 | `@prestige_parrucchieri` | Prestige Salon | Treviglio | n.d. | **1** | Nessun sito: solo Fresha, Groupon e Facebook |
| 29 | `@manu_di_forbici` | Manu di Forbici | Treviglio | n.d. | **1** | Nessun sito: solo Fresha e Facebook |
| 30 | `@unique___your_style_` | Unique Your Style | Treviglio | 726 | **1** | Nessun sito: solo Facebook e Instagram |
| 31 | `@skinline.esteticabenessere` | Skinline Estetica & Benessere | Treviglio | n.d. | **1** | Nessun sito: solo Treatwell e directory |
| 32 | `@nice.nails1118` | Nice Nails | Treviglio | n.d. | **1** | Nessun sito: solo Fresha, Facebook e Beauty Passport |
| 33 | `@il_diadema_caravaggio` | Estetica Il Diadema | Caravaggio | n.d. | **1** | Nessun sito: solo Instagram |
---

## L'invio — la sera del 3 settembre 2026

**Partite 75 conversazioni in giornata**: tutte e **33** le righe di questa
lista e **42 delle 47** riportate dal 2 settembre. Sono le date scritte nei
tre CSV, riprese dal banco.

| Cosa | Numero |
|---|---|
| Aperte e mandate il 3 settembre | **75** |
| — di cui bellezza, questa lista | 33 su 33 |
| — di cui tatuatori e wedding, lista del 2 settembre | 42 su 47 |
| Ferme, con il motivo | 5 |
| Testi corretti a mano dentro il banco | **0** |
| Risposte segnate finora | 0 |

**Le cinque che non sono partite**, e nessuna per sbaglio:

- `@miguelrtat2` e `@tropicalflowers.saronno` — marcate SCARTATO, il tasto non
  c'è proprio: hanno già un sito e buono.
- `@artemista_tattoo` — gancio 5 col buco mai tappato: il banco tiene il tasto
  spento finché non si scrive cosa c'è al posto della `[X]`. Ha funzionato
  esattamente per questo.
- `@inchiostrorossotattoo` e `@golden_skin_tattoo` — saltate. Il messaggio è
  pronto: sono le prime due del giro dopo.

**Nessun testo è stato corretto a mano**, e questo è il dato che vale più degli
altri: la versione C è uscita parola per parola com'era scritta, su tutte e 75.
Il confronto con la versione A di [[dm-instagram-vetrina]] è quindi pulito —
stessa promessa, stessa chiusura, e in mezzo un fatto verificato.

⚠️ Una sola riga è partita **senza che sappiamo cosa c'era scritto**:
`@minimaltattoovarese` risulta inviata ma la colonna `Messaggio` è vuota, era
un gancio 5 col buco. Se risponde, il testo esatto non è ricostruibile.

**Il recupero cade mercoledì 9 settembre** — quattro giorni lavorativi da
giovedì — e lo accende il banco da solo, con la domanda orientata al «No».
Fino ad allora non si scrive più a nessuno di questi.

> [!note] Settantacinque in un giorno, e nessun blocco — [[2026-09-03-tetto-dm-65]]
> Il giro è uscito oltre il doppio del tetto di 30 che il banco portava, e
> **non è scattato niente**: nessuna limitazione, nessun avviso, verificato da
> Patrick sull'account. I 25-35 al giorno della ricerca del 2 settembre erano
> una stima, e su questo profilo sono risultati prudenti.
> Da qui il tetto del banco è salito a **65** — il massimo osservato meno un
> margine — e accanto è comparso il conto degli invii **dell'ultima ora**,
> perché 65 in venti minuti non sono 65 in due ore. Il limite di questa misura
> è che vale per un giorno solo: è scritto nella decisione.

**Il prossimo numero da riempire è l'unico che conta**: la colonna `Esito DM`,
coi sei valori fissi di [[metodo-instagram]]. Le risposte si segnano lì, non a
memoria, o il giro non ha misurato niente.

---

## Gli scarti, con il motivo

Sedici candidati sono usciti dopo la verifica. Si scrivono qui perché **la
prossima volta non vanno ricontrollati**, e perché il motivo è il dato che
dice dove il canale non rende.

| Chi | Perché è fuori |
|---|---|
| `@dea.parrucchierisamarate` | `dea-parrucchieri.it` — WordPress vivo, blog, pagine per servizio |
| `@mastri.parrucchieri` | `mastriparrucchieri.it` — © 2025, sito curato |
| `@ilbrand_tradate` | `ilbrandtradate.it` — © 2026, responsive, WhatsApp e social attivi |
| `@il_salonedilisa` | `ilsalonedilisa.it` — Wix su dominio proprio, © 2025 |
| `@siparrucchieri.treviglio` | `siparrucchieritreviglio.com` — Wix su dominio proprio, aggiornato |
| `@e_parrucchieri_` | `eparrucchieri.com` — sito grande e mantenuto |
| `@couturetreviglio` | È un salone di una catena: `atelierhaircouture.com` è della S.r.l. |
| `@caggiano_parrucchieri` | `caggianoparrucchieri.com` — WordPress, © 2026 |
| `@centro.estetico.girasole` | `centroesteticogirasole.it` — vivo, © 2021-2024 |
| `@iris_esteticatreviglio` | `iristreviglio.it` — WordPress, © 2026 |
| `@steel.haircolourexperience` | `parrucchieralecco.it` — vivo e aggiornato al 2025 |
| `@3dunisexhairtrend` | ⚠️ `3dhairtrend.com` **rimanda al sito di Ribaudo**, un altro salone. O sono stati rilevati o hanno perso il dominio: finché non si sa, il messaggio è un campo minato |
| `@scarpabarbershop` | È di **Salerno**, non di Saronno |
| `@bellomo_parrucchieri_` | È di **Concordia Sagittaria (VE)** |
| `@alessia_estetica` | 200 follower e 38 post: sotto la soglia di [[metodo-instagram]] |
| `@caterina_ciglia_gallarate` | Comune e indirizzo non confermati da nessuna fonte |

**Sulla bellezza il canale tiene**: 33 righe buone su 49 candidati verificati,
cioè il 67%. Sul segmento wedding e fotografia del 2 settembre era sotto il
50%, e la differenza è tutta qui: chi vive di portfolio il sito ce l'ha.

## Come si lavora questa lista

1. **Doppio click su «Banco DM»** sul Desktop. La lista è già dentro, il
   messaggio già scritto riga per riga.
2. **Trenta al giorno, non uno di più**, e diluiti su due ore: il tetto è di
   Instagram, non del banco ([[2026-09-02-automazione-dm-instagram]]).
3. **Prima si guarda il profilo, poi si scrive.** Aprirlo, seguirlo, due like,
   e solo dopo il messaggio: cambia la casella in cui atterra.
4. **Il testo si corregge dentro il banco.** Quello che si legge è quello che
   parte, e rientra nel CSV scaricato.
5. **Il recupero parte da solo dopo 4 giorni lavorativi**, una volta sola.

> [!warning] La bozza adesso è promessa come fatta
> La versione C dice **«la bozza del suo sito è già pronta»**. Chi risponde
> «me la mandi» si aspetta un file, non un preventivo di tempo. La regola delle
> **5 bozze aperte** di [[dm-instagram-vetrina]] non è più un consiglio: al
> sesto sì bisogna dire un giorno, nella stessa giornata. È il prezzo di questa
> versione, ed è scritto in [[2026-09-03-bozza-gia-fatta]].

## Collegamenti

[[dm-instagram-vetrina]] · [[metodo-instagram]] ·
[[2026-09-03-bozza-gia-fatta]] · [[2026-09-02-automazione-dm-instagram]] ·
[[2026-09-02-instagram-tattoo-wedding]] · [[2026-09-01-instagram-anello-1-b]] ·
[[2026-08-31-instagram-anello-1]] · [[2026-08-30-verifica-sito-reale]] ·
[[core-commerciale]] · [[core-crescita-finanze]] · [[metriche]]
