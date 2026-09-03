---
type: progetto
status: attivo
client: dsi-advertising
stack: [html, gsap, netlify]
started: 2026-09-02
deadline: TODO
updated: 2026-09-03
source: claude
valore: TODO
incassato: 0
---

# Sito D.S.I. Advertising — la bozza per il preventivo

Sito vetrina in una pagina per **D.S.I. Advertising di Piras Sebastiano**,
Merate (LC): dal 1992 progetta e produce articoli promozionali per il canale
HO.RE.CA (portatovaglioli, portabustine, rendiresto, orologi personalizzati con
il marchio di torrefazioni e bar). **Non è una bozza al buio**: è un
referral della figlia [[shari-piras]] arrivato dal DM del 2 settembre, e il
3 settembre Patrick e Nicola hanno deciso il prezzo (300 € + 180 €/anno, sito
vetrina **più gestionalino**). Scheda commerciale: [[dsi-advertising]].

⚠️ **Il preventivo vende anche un gestionalino** (pannello per le 14 famiglie di
prodotto) che questa bozza non ha: è una pagina statica. Va costruito come lo
stesso componente di [[shari-piras]], o il prezzo non regge.
⚠️ `www.dsi-advertising.com` oggi rimanda alla **versione inglese** (302 →
`en.`): la bozza è solo in italiano, l'inglese è da chiedere in trattativa.

**Repo**: `Desktop/dsi-site`, git locale su `main`, **senza remote** (dove
pubblicarlo lo decide Nicola).
**Online**: no. `netlify.toml` e `robots.txt` con lo schema di Fiftynine:
**noindex** finché il sito non è loro.
**Stack**: HTML puro, un solo `index.html`, zero build, GSAP 3.13 +
ScrollTrigger da CDN, 31 foto in `assets/foto/` (2,3 MB in tutto).

## Da dove vengono i dati

Tutto letto il 2 settembre 2026, niente inventato:

| Dato | Fonte |
|---|---|
| Nove modelli e le loro descrizioni (PY-MET, Class, Class 2000, Hi-Top, Pyramid, Lux, Portabustine, Rendiresto, Orologi), tre stampe, tracciati fustella e dime, kit, colori Pantone/RAL a richiesta, «dal 1992», «NON forniamo merci di importazione» | vecchio sito Wix `www.dsi-advertising.com` (22 pagine, testi via WebFetch) |
| Coppette per gelaterie e porta salse take away | due pagine del vecchio sito **non collegate al menù** |
| Orologi 30/40 cm tondi o quadrati, meccanismi italiani | didascalia Instagram del 31 luglio 2024 |
| Via Statale 40, 23807 Merate | PagineGialle + PagineBianche |
| Tel/fax 039 9903118, email `dsi.advertising@tin.it` | sito |
| Logo (tre portatovaglioli disegnati a linea con D S I sopra «ADVERTISING») | foto profilo Instagram `@dsi.advertising`, 1080 px, ricavato in bianco su trasparente |
| 250 foto prodotto con marchi veri (illy, Pellini, Nero Caffè, Musetti, Caffè New York, Poli, Mondial…) | vecchio sito: originali Wix fino a 6000 px, scaricati tutti (813 MB) e poi tenuti 31 ridotti |

⚠️ **Recensioni: non ne esistono di pubbliche.** Google indicizzato, PagineGialle
(profilo completo al 20 %, zero recensioni), PagineBianche, Facebook (nessuna
pagina trovata), Instagram 85 follower. Google Maps non verificabile dal
pannello: muro del consenso, «Rifiuta tutto» non passa. Il sito quindi non ha
testimonianze e non se ne inventano.
⚠️ **Tre email diverse in giro**: `dsi.advertising@tin.it` (sito),
`d.s.i.advertising@tin.it` (Instagram nov 2025), `dsi.advertising2@gmail.com`
(Instagram 2024). Nel sito c'è quella del sito; da confermare col titolare.

## Com'è fatto

**La direzione l'ha tirata il dado.** Metodo [[processo-siti]] completo:
`design-taste-frontend` → `high-end-visual-design` → `ui-ux-pro-max`
(design system: pattern scroll-storytelling, stile brutalist, nero + oro) →
`impeccable` (PRODUCT.md, `concept-seed` con seed `df5029de`, pagina di
decisione aperta nel pannello, scelta di Nicola). Assegnata la candidata 7 della
lista: **«L'insegna»**, cassonetti retroilluminati dei bar e delle tabaccherie.

Il vincolo del materiale è diventato il mondo: **tutte le foto hanno il fondo
studio chiaro**, che su una pagina scura sarebbe un rettangolo sbagliato; dentro
una cornice scura con un'unica luce ambra dietro diventa **un'insegna accesa**.
Ogni cassonetto **si accende entrando** (buio, due sfarfallii, luce piena: è
l'unico momento di motion autoriale, ripetuto come le insegne di una via).
Barlow Condensed maiuscolo per le scritte, Barlow per il testo.

Capitoli: hero (titolo a due righe + PY-MET Caffè New York acceso) → manifesto
(«un caffè al banco dura tre minuti») → **«Quattro posti sul banco»**, l'unica
sezione appuntata: davanti / accanto / alla cassa / sulla parete, e le quattro
insegne si alternano con lo scroll → nove modelli in griglia asimmetrica →
binario dei marchi (scroll a mano, niente marquee) → tre stampe con la
hairline che si disegna + serigrafia in parallasse → kit come cassonetti
sovrapposti sul banco → «Non forniamo merci di importazione» con il disegno
dello stampo come lightbox → gelaterie e take away → contatti.

Cose scartate strada facendo, con il perché:
- la **prima versione** (chiara, griglia catalogo, Archivo, accento blu):
  «malissimo» → rifatta con il metodo degli altri siti;
- il **marquee** automatico: segnalato dal detector di impeccable, sostituito da
  un binario con scroll-snap manuale;
- i **numeri grandi** (34 anni, 9 modelli…): il craft floor li rifiuta come
  template e i numeri erano magri, meglio «dal 1992» nel testo;
- gli **eyebrow** sopra i titoli: vietati dal craft floor, i titoli condensati
  reggono da soli.

## La terza versione: lo stile loro, non il nostro

La seconda (notte, insegne) è stata scartata da Nicola con una riga che vale
come regola: **«nero così è stile Denki, ma non è quello che piacerebbe al
cliente: rifallo dandogli più vita e in stile loro»**. Lo stile loro sta in
tre posti: il logo (un Bodoni, su bianco), il vecchio sito (chiaro) e i post
Instagram (bar veri, tavolini rossi, «porta-zucchero con buon umore»).
Direzione pinnata dall'utente, che batte il dado (commit `b98d4a5`):

- bianco `#fdfcfa` e carta `#f4f3ef`, **Bodoni Moda** per i titoli (è il
  carattere del loro logo), Hanken Grotesk per il testo, pulsanti a pillola;
- **un solo rosso** `#c8102e`, che regge per intero il blocco «Made in D.S.I.»
  (il loro titolo storico) e altrove è accento;
- le foto senza cornice, raggio 16 e ombra calda: il fondo studio chiaro delle
  foto **sparisce sul bianco**, che è il motivo per cui la pagina chiara era la
  strada giusta fin dall'inizio;
- **le 13 foto Instagram scaricate in locale** (gli URL CDN scadono) fanno la
  striscia «Paparazzati al bar», con le loro parole: «se li vedete anche voi
  mentre bevete il caffè, mandateci una foto». L'hero è il bar bianco con il
  Caffè Teti, non una foto da studio.

**La finish review di impeccable** (subagente generico con il riferimento
degradato, senza screenshot su file) ha trovato nove didascalie che
contraddicevano le foto (Minuscoli, non Musetti; Giacomelli; Rallo Caffè; la
foto «take away» erano coppette da gelato), un contatto che prometteva un
montaggio mai dichiarato, «tre minuti» e proprietà delle stampe inventate, un
kit inesistente e il sipario eterno senza JS. Tutto corretto nella terza.

## La quarta: due pagine, il logo dal vero, il carosello

Nicola, 3 settembre: «aggiungi alla hero più vita sfruttando il logo, una
barra di scorrimento fatta bene per le immagini orizzontali, dividi il sito in
un paio di pagine con bottoni nella principale: così è troppo lungo».
Commit `4b2f188`:

- **Hero «il logo dal vero»**: il logo D.S.I. sono tre portatovaglioli
  disegnati; nell'hero ci sono tre portatovaglioli veri (illy, Perlanera,
  Pyramid rosso) con le lettere D. S. I. in Bodoni rosso sopra, che arrivano
  sul tavolo uno alla volta e poi galleggiano piano. Al passaggio del mouse
  compare il cubo disegnato (`logo-d/s/i.png`, ritagliati dal logo con PIL).
- **Carosello «Paparazzati al bar»** fatto bene: scroll-snap con
  `scroll-padding-left` (senza, lo snap mangiava il padding iniziale), barra
  rossa che segue lo scorrimento, frecce che si spengono ai bordi,
  trascinamento col mouse, tastiera nativa.
- **Due pagine**: `index.html` racconta (hero, bar veri, manifesto, quattro
  posti, quattro card-bottone verso i modelli, Made in D.S.I., contatti);
  `modelli.html` elenca (nove modelli, stampe, kit, gelaterie e take away,
  contatti). CSS e JS condivisi in `assets/`, con `?v=` contro la cache.

## Stato

🟡 **Quarta versione fatta e misurata**, commit `4b2f188` e `57f2f28`. Verifiche nel
pannello su viewport emulati 1440×900 e 375×812: titolo su due righe da
desktop, hero nel viewport, nessuno scroll orizzontale, sezione appuntata
funzionante e impilata da telefono, pulsanti su una riga, ancore corrette.

✅ `DESIGN.md` scritto dal documenter degradato (30 KB, otto sezioni, in italiano); ha trovato le didascalie del blocco rosso sotto AA e un peso Bodoni caricato a vuoto, corretti.
⬜ Non visto su browser vero né su telefono fisico: solo misure e screenshot
del pannello, che a pane nascosto ferma il rAF (sipario e reveal si vedono in
ritardo, non è un bug del sito).
⬜ Hosting e dominio: non decisi (il repo c'è, Netlify no). Patrick non l'ha ancora proposto.
⬜ Le tre email diverse: da confermare col titolare prima di pubblicare.

## Collegamenti

[[sito-castiglione]] · [[sito-fiftynine]] · [[processo-siti]] ·
[[registro-interventi]] · [[2026-09-03-sito-dsi]]
