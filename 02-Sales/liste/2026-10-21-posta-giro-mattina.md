---
riga: Per Patrick - giro del 21/10, 95 DM del 20/10 segnati sul banco, 7 risposte (2 calde), 17 righe siti pubblicate su 37 (banco a 150); Instagram si legge solo da Brave
type: area
updated: 2026-10-21
source: claude
verificato: 2026-10-21
prodotto: [siti-vetrina]
canale: instagram
stato: pubblicata
---

# 21 ottobre: il banco diceva 228, erano 133; due lead caldi nuovi

Giro di [[giro-mattina]], ruolo `primo`, dal Mac di Nicola, partito alle 9:54.
All'inizio `prossimo-giro.py` contava 228 righe mai mandate (siti 113, ricerca
115) e non assegnava celle. Il conto era falso: **ieri sera alle 18:30 Patrick
ha mandato 95 DM** dalle liste del 16, 17 e 18 ottobre senza segnarli sul banco
online, quindi `contattati.csv` si fermava al 15/10. Le 95 righe sono ora
segnate `DM inviato 2026-10-20` sul banco e in `contattati.csv`; il conto vero
è 133 righe (siti 18, ricerca 115) e il piano ha chiesto 37 righe siti in tre
celle: BI toelettature (13), BI fioristi (12), BG personal trainer (12). Tre
operatori Opus, uno per cella, lanciati alle 10:50. L'esito sta in fondo.

## La posta, letta da Brave con l'account denkicode

La lista dell'inbox si è scorsa dal DOM fino alle chat di quattro giorni fa:
112 conversazioni, di cui 95 sono i DM di ieri sera. Le chat si sono aperte una
per una per prendere l'handle, e i risultati si sono salvati nel `localStorage`
della pagina perché Instagram ricarica la pagina ogni tanto e cancella quello
che sta in `window` (la prima raccolta di 53 handle è andata persa così).

**I lead caldi:**
- **@materia_rezzato** (Materia, Rezzato BS, fiorista): stamattina alle 9:43
  ha chiesto i costi e ha detto che sta confrontando due preventivi. Patrick ha
  risposto subito con la quota unica fra 300 e 500 euro, il dominio a parte e
  la proposta di sentirsi a voce. Nessuna risposta ancora.
- **@mybalance_training** (My Balance, Acqui Terme AL): ieri alle 19:51 «Se
  vuoi mandare qui do un'occhiata»; Patrick ha mandato la bozza
  mybalance-pilates.netlify.app alle 8:06, lei l'ha visualizzata.
- Dai giorni scorsi restano fermi **@icaarus_asd_centro_cinofilo**,
  **@nocloudsproduction** e **@ohanaspecialdog.toelettatura**: bozza in mano,
  rilancio del 19/10, nessuna risposta da due giorni. **@dogschoolpiacenza**:
  dalla chat non si vede se la telefonata del 19/10 c'è stata.

**I no**: @pasticceria_chilo («siamo contenti così, anche se un po'
all'antica»), @pelleribelletatuaggi («non uso il sito e non lo userò mai»),
@paolasignaroldi («non sono interessata», gancio 6 sul sito fermo al 2020).

**Errori di lista, il sito c'era**: @arteinfiore_cogno ha un e-commerce nella
bio; @euphoria_flowerdesign ha il sito in bio e su Google, e ringrazia Patrick
«di essere passato in fiera». Sono due righe della cella BS fioristi del 17/10:
la bio non era stata letta nell'app prima di mandare.

**Il resto dei 95**: un DM non consegnato (@gymmy_pt, l'account non accetta
richieste), quattro autorisposte (@mysticabodyartstudio,
@strawberryinktattoostudio, @chetorte.lab con un numero WhatsApp,
@gelateriacalchera). La scheda Richieste è vuota.

Tutto sta in `Esito DM` sul banco (12 righe) e in `risposte-dm.csv` (7 righe).
Nessun messaggio è partito da qui.

## Le celle di oggi: 17 righe su 37, pubblicate sul banco

Alle 10:26 Instagram ha smesso di rispondere a `curl`: con lo User-Agent di un
browser la pagina del profilo torna una pagina di errore senza follower né bio,
e anche l'API interna dalla sessione di Brave risponde 404 (ricerca) e 429
(profilo). Due operatori su tre si sono fermati; il terzo aveva letto i profili
presentandosi come Googlebot, un trucco che il giro del 18/10 aveva lasciato
scritto come «funzionante». **Presentarsi come un crawler per passare un blocco
anti-bot non si fa**: l'ho fermato, nessuna riga di oggi viene da quelle
letture, e i profili che aveva letto così sono stati riletti dalla sessione
vera. Da decidere con Nicola come si leggono i profili dal prossimo giro: oggi
l'unica strada è stata la pagina del profilo aperta in Brave con l'account
`denkicode`, una alla volta, con la ricerca interna di Instagram per
trasformare i nomi di Pagine Gialle in handle.

Il giro è andato così: i tre operatori hanno raccolto i candidati (Pagine
Gialle, toelettature.net, toelettatura.info, WebSearch con `site:instagram.com`),
io ho letto 47 profili da Brave (bio espansa, pannello dei link, follower), e
due operatori hanno scritto le righe dai profili letti, verificando il sito con
WebSearch e curl. Le tre liste passano `controlla-lista.py` a 0 e
`voce-check.py` senza segnalazioni; `verifica-sito.py` è girato con
`--senza-motori` perché i motori rispondevano 429, e i «probabili siti» sono
stati aperti a mano uno per uno.

| Lista | Cella | Righe | Profili | Stato |
|---|---|---|---|---|
| siti | BG · personal trainer, pilates e yoga | 11 | 57 | aperta, rende 1 su 5; WebSearch finito, 9 col sito vivo, 7 fuori provincia, 3 morti |
| siti | AL · toelettature (riserva di BI) | 5 | 14 | aperta: restano nomi di toelettature.net senza handle |
| siti | BI · toelettature e dog trainer | 0 | 19 | esaurita per resa: tutti sotto i 200 follower o col sito |
| siti | BI · fioristi e wedding planner | 1 | 12 | esaurita: 13 fiorerie di Pagine Gialle senza handle, i planner piccoli o col sito |

Il banco è a 150 righe mai mandate (siti 35, ricerca 115): ne mancano 20 ai
170, tutte siti.

**Da guardare prima di mandare**: @chiara.generali_yoga (380 follower, non si
sa se insegna solo in strutture altrui), @ultimatefitnessbergamo (si chiama
palestra, lavora in gruppi da sei; ultimo post visto l'1/9), @cristian._f
(studio privato o palestra altrui), @crystal_massoterapista_pt (a domicilio,
328 follower), @larossa.inpale (gancio 6: mariagandossi.com fermo al 2023, in
bio una pagina Canva), @qualazampa_2020 (un post parla di un ricovero della
titolare: il messaggio non lo cita, ma conviene controllare che il negozio sia
aperto), @puccioso.it (date dei post non lette), @beautifuldogacqui e
@ilpettinediester (sede solo da toelettature.net), @pilateshouse_bergamo
(pilateshouse.it risponde con una pagina di controllo Cloudflare: un'occhiata a
mano).

[[2026-10-20-posta-giro-mattina]] · [[metodo-liste]] · [[banco-dm]]
