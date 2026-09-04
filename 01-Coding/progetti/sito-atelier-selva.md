---
type: progetto
status: attivo
client: shari-piras
stack: [html, gsap, netlify]
started: 2026-09-03
deadline: TODO
updated: 2026-09-03
source: claude
valore: 200
incassato: 0
---

# Sito Atelier Selva — la bozza che deve far dire a Shari che le serve

Sito per **Shari Piras**, tatuatrice fineline a Merate (LC), e per il suo
studio privato **Atelier Selva** (Via Statale 147). Lei ha detto che un sito
per sé non le serve, e ci ha girato l'attività dei genitori
([[sito-dsi-advertising]]). Il brief di Nicola, 3 settembre 2026: «col solito
processo, però molto in stile suo e particolare, artistico: deve far dire alla
ragazza che ne ha bisogno». Cliente: [[shari-piras]] (preventivo di Patrick
già scritto: realizzazione regalata in cambio di galleria, recensione e
citazione, 200 €/anno).

**Repo**: `Desktop/atelier-selva-site` → **`github.com/Nixo999/atelier-selva-site`
(privato)**, ramo `main`, creato con `gh` ([[2026-09-03-gh-crea-repository]]).
**Online**: no. `netlify.toml` e `robots.txt` con lo schema di Fiftynine:
**noindex** finché non è suo.
**Stack**: HTML puro, `index.html` (home) e `lavori.html` (galleria completa),
`assets/style.css` e `assets/main.js` condivisi, GSAP 3.13 da CDN, 42 foto in
`assets/foto/` (6,3 MB). L'archivio grezzo dei post sta in `assets/ig/`, fuori
da git.

## Da dove vengono i dati

Tutto letto il 3 settembre 2026, niente inventato:

| Dato | Fonte |
|---|---|
| Fineline, botanica, miniature; no cover-up, no AI; chiusa il sabato; atelier a Merate | bio di `@shari_tattooer` (4.506 follower, 493 post) |
| «Sabato e domenica chiuso», Via Statale 147, «Owner @shari_tattooer» | bio di `@atelierselva_` (⚠️ profilo limitato ai maggiori di 16 anni: Apify non legge i post) |
| Flash: disegni pronti, 5-6 cm, rosa 60 € / blu 70 € / verde 80 € | post fissato del 23 giugno 2026, 303 like |
| Regola dell'estate («entro un mese dal mare/piscina», altrove «3 settimane»), chiusura di due settimane ad agosto, prenotazioni solo in DM | didascalie dei post |
| Soggetti e nomi ringraziati (Celeste, Michela, Sara, Asia, Giada, Barbara, Federica, Emma, Silvia, Veronica, Giulia) | didascalie dei 36 post scaricati (aprile-settembre 2026) |
| «Feels like home», «carta bianca», il segno ⸭ nel nome | i suoi post e il suo nome profilo |
| Link Google Maps `maps.app.goo.gl/vht53Xpq7NvgycdS6` | link in bio |

⚠️ **Recensioni**: stanno nella storia in evidenza `/Recensioni` e su Google
Maps, non leggibili da qui. Nessuna testimonianza nel sito.
⚠️ **Aftercare**: nel sito ci sono la sua regola (un mese senza mare e piscina)
e due righe generiche (pulito e asciutto; scrivimi se qualcosa non convince).
**Da far confermare a lei prima di pubblicare.**
⚠️ **Orari**: i due profili dicono cose diverse sul sabato; nel sito c'è la
versione prudente (sabato e domenica chiuso, su appuntamento).
⚠️ Nessuna email né telefono pubblicati: il sito manda solo al DM.

## Com'è fatto

Metodo [[processo-siti]] completo, con la lezione della notte prima
([[2026-09-03-sito-dsi]]): **prima del dado, lo stile del cliente**. Le sette
direzioni candidate erano tutte prese dal suo mondo (erbario, foglio dei flash,
stencil, la pelle, l'atelier di casa, la selva, il quaderno degli schizzi); il
dado di impeccable (seed `511bfdbc`) ha assegnato la sesta, **«La selva»**, il
bosco da cui lo studio prende il nome, e Nicola l'ha confermata sulla pagina di
decisione senza steer.

- **Fondo color pelle** (`#efe2d5`): i tatuaggi vivono sulla pelle, le foto non
  hanno cornici né ombre. Inchiostro `#171311`, **un solo verde selva**
  `#2e4a33` come segnale attivo, carta `#fbf8f3` per il foglio dei flash.
- **Cormorant leggero** (300) per i titoli: la linea sottile come l'ago. Karla
  per il testo. Il segno **⸭** che lei usa nel nome come marchio tipografico.
- **La linea che si disegna**: un percorso SVG fisso a sinistra si traccia con
  lo scroll (è il progresso di lettura, disegnato come l'ago). Sotto 900 px
  sparisce.
- Home: hero con il ramo lungo la schiena (per Celeste) → «Niente cover-up,
  niente intelligenza artificiale» → lavori in tre gruppi (botanica, fineline,
  miniature; 10 foto, il resto in `lavori.html`) → i flash con i bollini →
  **«Scrivimi, ma scrivimi tutto»**: un compositore del DM (soggetto, zona,
  misura, budget, riferimenti) che scrive il messaggio da copiare e incollare
  su Instagram, senza backend → l'atelier («Sembra casa») → dopo il tatuaggio →
  «Sono Shari» → chiusura in inchiostro con il pulsante Instagram.
- Le didascalie dicono soggetto, posizione e il nome ringraziato nel post:
  scritte guardando la foto, non il nome del file (la lezione di D.S.I.).

## La seconda hero: i suoi disegni, non i nostri

Nicola, alla prima versione: «bello ma molto piatto, la hero non mi piace per
niente: rifalla, prendi spunto dal suo stile e aggiungi qualche disegno».
Commit `9abe774`. La regola «NO AI» vale anche per noi: nessun disegno inventato.
I motivi che ora popolano il sito (colibrì, fata, peonia, nastro di stelle, la
firma «with love», il sole, l'ibisco, la mano con la bacchetta, la casetta, il
barattolo di stelle, «Soft souls see more») sono **ritagliati dalle foto dei
suoi fogli dei flash** e portati a inchiostro su trasparente con PIL:
sottrazione dello sfondo (sfocatura larga della luminanza) e soglia a 2,4 sigma
sul rumore della carta; il filtro mediano, provato prima, mangiava le linee
sottili. Sono in `assets/disegni/`, 31 pezzi. L'unico tratto nostro è il ramo
SVG con quattro foglie che si disegna all'apertura dell'hero.

Hero: titolo su tre righe, la schiena con le farfalle e le peonie appoggiate
una sull'altra con una rotazione leggera, i motivi che galleggiano, la firma
sotto i pulsanti. Da telefono la foto piccola sta in flusso e la didascalia
sotto; il nastro di stelle sparisce.

## Stato

🟡 **Bozza fatta e misurata**, commit `9abe774` (hero rifatta), repo privato. Verifiche nel
pannello su 1440×900 e 375×812: hero nel viewport, Cormorant e Karla caricati,
nessuna immagine rotta, nessuno scroll orizzontale, masonry 3/1 colonne,
compositore del DM che produce il testo giusto, nav da telefono su una riga
(«Scrivimi» corto), nessun errore in console.

✅ **Finish review di impeccable fatta e applicata** (commit `486869d`): il subagente
generico col riferimento degradato ha letto le foto una per una e trovato nove
didascalie sbagliate (il «pelosetti» era un ritratto di famiglia, la «fatina»
due amorini), il listino flash senza il bollino rosso da 90 €, l'aftercare
generico e due promesse a nome suo. Tutto corretto, più il floor: linea nel
margine anche a 1366 px, contrasti AA, misure vere delle foto, h2 in
`lavori.html`, stati del pulsante «Copia», nav con fondo senza JS.
✅ `DESIGN.md` (commit `3cd422a`): il primo documenter l'ha scritto sulla versione
prima dell'hero rifatta ed è caduto per sovraccarico (529) alla fine; il
secondo è caduto due volte allo stesso modo. Le parti cambiate (hero, disegni,
linea nel margine, nav, bollini, niente righe sopra i titoli) le ho riscritte
a mano nel documento del primo, che per il resto era giusto.
⬜ Non visto su browser vero né su telefono fisico: solo misure e screenshot
del primo viewport (a pane nascosto rAF e scroll non girano).
⬜ Il **gestionalino** promesso nel preventivo non è in questa bozza: è lo
stesso componente del sito dei genitori, da costruire una volta sola.
⬜ Hosting e dominio: non decisi. Da mostrare a Shari **prima** o comunque non
peggio del sito dei genitori: è lei che ha portato il referral.

## Sera del 3 settembre: «Dal foglio alla pelle»

Nicola ha bocciato la home a galleria («è solo uno showroom, non ha vita»).
Fra tre strutture proposte ha scelto la trasformazione: video dello studio
nell'hero, capitolo appuntato in cui il suo disegno diventa il tatuaggio vero
(colibrì, fata, drago, conchiglia, spada: coppie prese dai suoi post), prova
di un flash a misura su un braccio (trascinabile, 3–9 cm, scala dichiarata e
detta «indicativa»), quattro storie con le sue parole. Commit `0933542`.
⬜ `ciao.mp4` pesa 12,5 MB: parte solo da desktop, da comprimere (ffmpeg
manca su questa macchina). Il video breve dello studio (post 23) non si è
scaricato: CDN Instagram irraggiungibile, da riprovare.

⬜→✅ Telefono: passaggio mobile fatto (`ec34253`), verificato con il giro completo a 375 px nel pannello; resta da vedere su un telefono fisico.

## Collegamenti

[[shari-piras]] · [[sito-dsi-advertising]] · [[processo-siti]] ·
[[registro-interventi]] · [[2026-09-03-sito-dsi]]
