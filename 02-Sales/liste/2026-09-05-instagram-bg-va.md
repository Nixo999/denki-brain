---
type: area
updated: 2026-09-05
source: claude
prodotto: siti-vetrina
canale: instagram
anello: 2
stato: pubblicata
---

# Lista Instagram — anello 2, per il 5 settembre 2026

**65 righe nuove, verificate una per una il 5 settembre 2026.** Metodo:
[[metodo-instagram]]. Messaggio: la **versione C** di [[dm-instagram-vetrina]].
Il tetto è quello misurato il 3 settembre — 65 al giorno,
[[2026-09-03-tetto-dm-65]] — e la lista è tagliata esattamente su quello.

`lista-corrente.csv` è pubblicata: sul [banco DM](../strumenti/banco-dm.html)
ci sono **68 conversazioni da mandare** (queste 65 più le 3 del 2 settembre mai
partite) e **75 recuperi che si accendono da soli mercoledì 9 settembre**.
Le 75 righe del 3 settembre sono rimaste dentro il file apposta: se il CSV
venisse sostituito invece che allungato, il recupero sparirebbe.

## Dove si è pescato

**L'anello 2, dal lato che non era ancora stato aperto: Bergamo ovest.** Il
3 settembre Treviglio aveva dato 7 righe buone e la nota diceva di ripartire da
lì — Treviglio invece è **finita**: tutte e sette le ricerche sui parrucchieri
hanno ripescato profili già contattati, e resta una riga sola (un barbiere).
Il pescato vero è venuto da **Bergamo città, Dalmine, Seriate, Romano di
Lombardia** e dai comuni della cintura, e sul lato varesino da **Gallarate,
Busto Arsizio, Cassano Magnago e Sesto Calende**.

| Provincia | Righe |
|---|---|
| **BG** | 34 |
| **VA** | 30 |
| **CO** | 1 |

Ventuno comuni, nessuno in Monza Brianza o Milano. Un candidato buono è stato
buttato proprio per questo: `@labarbieria_dipiazzasanlorenzo` sembrava di
Bergamo e sta a **Trezzano sul Naviglio (MI)**, cioè nel territorio del
telefono ([[2026-08-31-stop-porta-a-porta-a-freddo]]).

## I ganci

| # | Esito | Righe |
|---|---|---|
| **1** | Nessun sito | 47 |
| **2** | Dominio morto | 7 |
| **3** | Sito rotto (errore server / pagina vuota) | 2 |
| **4** | Link rotto | 1 |
| **5** | Su piattaforma | 5 |
| **6** | Vivo ma vecchio | 3 |

**Sette domini morti su 65**, contro i quattro su 33 del 3 settembre: la resa
del gancio più forte tiene. Sono `carusobarbershop.it`, `ilsalonediandrea.it`,
`nailsmania.net`, `oemabarbieri.it`, `qesse.it`, `lacharmerie.it` e
`blackbladebarbershop.it` — tutti NXDOMAIN su Google **e** su Cloudflare, tutti
ancora presenti nei risultati di ricerca.

Due meritano una riga a parte:

- **`@q.esse_quality_stylist_azzano`**: la loro pagina Facebook si chiama
  ancora `facebook.com/www.qesse.it`. Il nome del sito è rimasto scritto
  sull'insegna digitale, il sito no.
- **`@la_charmerie`** (Gallarate): il 31 agosto era stata **scartata** come
  «sito vero, vivo e aggiornato» e non è mai stata contattata. Oggi
  `lacharmerie.it` **e** `lacharmerie.com` sono tutti e due senza DNS, mentre
  nelle ricerche compaiono ancora cinque pagine interne
  (`/epilazione-laser-gallarate`, `/ricostruzione-unghie-gallarate`,
  `/parrucchiere-uomo-gallarate`, `/microblading-gallarate`, `/estetica/`).
  Avevano un sito costruito bene: in cinque giorni è sparito.

Le altre tre righe che non entrano in nessuna delle sei formule hanno il
gancio scritto a mano nel campo `Messaggio`:

- **`@manomortatattoo`** — `manomortatattoo.com` risponde **HTTP 500** con la
  scritta «Database Error» e basta.
- **`@segretidibellezzanails`** (Castellanza) — `segretidibellezza.net` c'è e
  risponde 200, ma la pagina è **3.668 byte con dentro solo il tag di Google
  Tag Manager**: chi ci arriva vede bianco.
- **`@incanto_e_bellezza`** (Gallarate) — l'unico sito nei risultati è la
  vecchia pagina `*.business.site`, che oggi dà **404**. Google ha chiuso
  quel servizio: il link gira ancora e non porta più da nessuna parte.

## La cosa trovata per caso, e che vale per il 9 settembre

**`@ink_factory_tattooshop_` (Bergamo) non è in questa lista — è già stato
contattato il 3 settembre — ma il suo dominio è cambiato di mano.**
`inkfactorybergamo.com` risponde 200 e **redirige a `to388.me`, un sito di
scommesse**. Le pagine `/piercing`, `/lo-staff`, `/chi-siamo` sono ancora
nell'indice di Google e portano tutte lì.

Serve saperlo prima di mercoledì: al recupero non gli si scrive «ha lasciato
perdere l'idea di avere un sito». Gli si scrive che l'indirizzo con il suo nome
oggi porta i suoi clienti su un sito di gioco d'azzardo. È il gancio più forte
che abbiamo trovato da quando il canale esiste, ed è su un account che ha già
ricevuto un messaggio senza rispondere.

## Cosa è stato verificato, e cosa no

| Controllo | Come | Esito |
|---|---|---|
| **L'attività esiste, e dove** | Ricerca per nome e comune: indirizzo, telefono, orari | ✅ tutte e 65 |
| **Il dominio è vivo o morto** | `dig` su Google (8.8.8.8) e Cloudflare (1.1.1.1) | ✅ affidabile |
| **Cosa c'è sulla pagina** | Sito aperto davvero: codice HTTP, motore, versione, anno, peso | ✅ 39 domini interrogati, 26 aperti |
| **Il profilo Instagram è vivo** | Solo dai risultati di ricerca | 🟡 **non aperto a mano** |
| **Follower** | Solo dove il motore li riportava | 🟡 **15 righe su 65** |

> [!warning] Le due cose che non ho potuto fare, e vanno dette
> **Instagram continua a non aprirsi da qui.** Vale in pieno l'avvertimento del
> 3 settembre: il controllo «l'account esiste ancora» è appoggiato ai risultati
> di ricerca, non all'occhio. Se un profilo non c'è più, `ig.me` non apre
> niente e si passa alla riga dopo.
> **I follower mancano su 50 righe su 65**, e non sono stati inventati: dove
> non li ho letti c'è scritto `n.d.`.

## Gli scarti, e perché — così domani non tornano

**Hanno un sito vero, vivo e aggiornato** (❌ fuori):
`@joyprojectit` (Bergamo, Elementor 2024) · `@parrucchieri.elite` (Dalmine,
catena di 6 saloni) · `@cassaraparrucchieri` e `@lodi_hairspa` (Busto Arsizio,
copyright 2026) · `@centroesteticogirasole` (Busto, PrestaShop) ·
`@esteticanicol` (Rovellasca, Divi 2025) · `@esteticapescanoce` (Olgiate Olona,
copyright 2025) · `@5stelle_estetica` (Cassano Magnago) · `@iza.barber`
(Dalmine, `figarobarbershop.com` aggiornato al 2026) · `@queen_nail_gallarate` ·
`@estetica__venere__` (Stezzano) · `@dor.care` (Sesto Calende) ·
`@cameliaestetica` (Stezzano, `esteticamilli.it` vivo).

**Catene e franchising** — il sito non lo decidono loro:
`@littleitalybarberia_` · `@evos.sommalombardo` e `@evos_ccconad_merate` ·
`@tagliatixilsuccesso_merate` · `@prior.colognoalserio` (dentro
`prioritaly.com`) · `@crystalnails_gallarate` (dentro `wearecrystalnails.it`).

**Fuori zona**: `@labarbieria_dipiazzasanlorenzo` (Trezzano sul Naviglio, MI).

**Non risolti — identità o comune incerti, quindi fuori**: `@berber.barbershop`
· `@glamour_curno` · `@zarina_beauty_center` · `@glam_nails_bergamo` ·
`@the_style_parrucchieri` · `@lashes.treviglio` · `@m_k_beauty_salon` ·
`@crystal_beauty_saleterapia` (il sito `saleterapia.it` è vecchissimo, tutto in
`.php`, ma non ho trovato un anno scritto: senza l'anno il gancio 6 non si può
dire, e senza gancio la riga non entra).

**Rientrata dopo lo scarto**: `@centroesteticoalba` (Tavernerio). Il 31 agosto
era stata messa fra i «sito vero, vivo e aggiornato» **senza aprire la pagina**
— da quel PC i siti piccoli non si aprivano. Aperta oggi: è un Wix. Non è mai
stata contattata, quindi rientra col gancio 5.

## L'errore di oggi, e come si evita domani

**Tredici righe erano già state contattate, e me ne sono accorto solo al
momento di pubblicare.** Il controllo incrociato l'avevo fatto sui *candidati*
raccolti nella prima tornata di ricerche, non sulla **lista finita**: i profili
trovati durante la verifica — quelli che nascono dopo il primo giro — non erano
passati da nessun filtro. Undici di quei tredici erano nelle liste del 31
agosto, 1, 2 e 3 settembre; quattro avevano già ricevuto il messaggio il
3 settembre.

Il costo, se fosse partita così, non era una riga sprecata: era **il secondo
messaggio identico allo stesso account in due giorni**, cioè la cosa che
[[dm-instagram-vetrina]] mette per iscritto fra quelle da non fare mai.

**Regola nuova, da oggi**: il dedup si fa **sul file finito**, non sul pool dei
candidati, e si fa contro *tutte* le liste — CSV e note `.md`, perché tre delle
quattro liste vecchie hanno gli handle solo dentro le tabelle in Markdown. È un
controllo da dieci secondi che si esegue dopo aver scritto il CSV, non prima.

## Il file

`2026-09-05-instagram-bg-va.csv`, stesse 11 colonne del 3 settembre, con il
messaggio **già scritto riga per riga** — quindi sul banco non compare il campo
«manca:» e Patrick non deve incollare niente a mano.

## Collegamenti

[[metodo-instagram]] · [[dm-instagram-vetrina]] · [[2026-09-03-tetto-dm-65]] ·
[[2026-09-03-bozza-gia-fatta]] · [[2026-09-03-instagram-anello-1-2]] ·
[[2026-09-02-instagram-tattoo-wedding]] · [[2026-08-31-instagram-anello-1]] ·
[[2026-08-30-verifica-sito-reale]] · [[2026-08-31-canale-dm-instagram]] ·
[[metriche]] · [[generazione-lead]] · [[ciclo-settimanale]]
