---
type: progetto
riga: Bozza di sito vetrina non commissionata per Shaddai Extension Lash, lash artist a Bergamo, costruita il 16 settembre 2026 dai contenuti veri del profilo Instagram.
updated: 2026-09-16
source: claude
verificato: 2026-09-16
status: attivo
client: shaddai-extension-lash
stack: [html, css, gsap]
started: 2026-09-16
deadline: 
---

# Sito Shaddai Extension Lash

Bozza **non commissionata**, cartella `~/lavoro/shaddai-site`, nessun remote e
nessuna pubblicazione: serve come gancio per il DM. Il profilo era gia' nella
lista `02-Sales/liste/2026-09-16-instagram-siti-bergamo.csv`, gancio 1, DM non
ancora inviato.

## Come e' stato estratto il materiale

Lo **scraper Apify non e' agganciato su questa macchina** (lo era su quella di
[[2026-08-30-sito-castiglione]]). Estrazione fatta dal **browser in-app gia'
loggato su Instagram**, con JS sul DOM: bio, contatori, storie in evidenza,
caption dal campo `alt` delle immagini, URL foto in piena risoluzione.

Due cose che si riusano:
- Il grid di Instagram **non carica altri post a pane nascosto** (nessun
  IntersectionObserver, la stessa trappola di Castiglione): con sette scroll il
  bottino resta quello del primo schermo, 12 immagini. Va bene per un profilo
  da 100 post, non per uno da 1000.
- La dimensione vera di una foto sta nel parametro `efg` dell'URL, che e'
  **base64**: `atob()` e dentro c'e' `regular_photo` con la larghezza. Filtrare
  cosi' separa le foto dai fotogrammi dei Reel senza scaricarle.

I fatti verificati stanno nel repo, in `BRIEF.md`.

## I fatti, in breve

- 103 post, 736 follower (16/09/2026). **Nessun sito**, l'unico contatto e'
  WhatsApp `350 926 2986`.
- Lavora **a domicilio**, zona Bergamo, suo hashtag
  `#extensioncigliasanpaolodargon` → San Paolo d'Argon.
- Bilingue italiano/spagnolo, latina, diploma «Diseño Avanzado de Pestañas»
  maggio 2024, in bio «futura lashtrainer».
- Gli effetti li nomina lei: **Natural, Arabo, V.tech, Anime, Cat Eye, Fox Eye**.
- La frase che tiene in piedi il sito e' sua: «**Il problema non sono le tue
  ciglia. E' il mapping.**»

## Foto: tre, e si vede

`ritratto-occhi-chiusi.jpg` 1440×1800, `quattro-effetti.jpg` 1350×1688 (da cui
quattro ritagli 880×422 dell'occhio senza etichetta), `shaddai-ritratto.jpg`
1080×1350 ma con testo grafico sopra. **Tutto il resto del feed sono copertine
di Reel a 640 px.** Dichiarata la strada 2 del passo 1 di [[processo-siti]]: il
sito regge su grafica inventata, non sulle foto.

## TODO — chiesti a lei, non inventati

prezzi · indirizzo o raggio del domicilio · orari · nome proprio · recensioni
testuali (stanno in una storia in evidenza)

## Il mondo scelto — «La messa a fuoco»

Il banco di prova dell'oculista: lei non vende ciglia, tara uno sguardo. Guarda,
misura, prova, corregge. Gli strumenti non sono una metafora prestata, sono i
suoi numeri veri — diametro 0.07, curvatura CC, lunghezze da 8 a 11 mm. Seed di
impeccable `d11e5a6f`, scope `direction`, modo `persuade`. I due mondi e i sette
candidati scartati stanno in `MONDO.md` dentro il repo.

Tenuti fuori di proposito: la vetrina beauty crema + serif alto contrasto + oro
rosa, e il suo opposto prevedibile, nero + neon.

**26 `<svg>` inline**, un pin solo, calibro 8-11 mm che corre col cursore,
rotaia a quattro stazioni, diaframma che apre le domande, braccio rotante sulla
mappa della zona. Il copy e' preso dal registro dei siti lash veri
(`lenalashes.it`, `daianalashartist.it`; `giulialashartist.it` letto come
contro-esempio e scartato), poi passato da [[voce-denkicode]].

`controlla-sito.py` **8 su 8**. Overflow orizzontale zero a sette larghezze,
nessun contrasto sotto AA a 1440 e 375, console pulita, pagina completa senza JS
(8112 px, zero elementi invisibili).

## Giro 2 — il copy, rifatto impersonale

Nicola ha bocciato i testi del giro 1 («solito problema, gli script, le frasi
fanno cagare») e ha scelto il registro: **professionale, impersonale**. Il
difetto non erano «alcune frasi» ma quattro tic ripetuti — ogni paragrafo che
chiudeva con una battuta in seconda persona, «Ideale per chi» dieci volte su
dieci schede, titoli che aprivano col no, e un lessico da chat. Riscritte 41
stringhe: soggetto il trattamento, verbi impersonali, titoli affermativi, e
«one to one» definito una volta sola invece di tre. Prima persona solo in «Chi
sono» e nelle citazioni sue.

**I siti di lash artist veri non si sono potuti leggere**: il DNS di questa
macchina blocca i domini piccoli (lenalashes, lashbar, ilariamari, herbeauty,
accademiadellosguardo). L'impostazione delle frasi e' stata presa da Clio
Makeup, Grazia, Passione Beauty e dalle schede salone di Treatwell. Se la
direttiva «guarda i siti veri del mestiere» deve valere davvero, serve una
macchina con la rete aperta.

## Aperto

- **Mai vista su un browser vero ne' su un telefono fisico**: le misure sono
  tutte da Chrome headless via CDP.
- `detect.mjs` di impeccable gira **DEGRADED** (mancano htmlparser2, css-select,
  css-tree): il suo `[]` e' un sotto-conteggio, non un via libera.
- Su 375 le foto degli effetti stanno dentro card: da guardare contro la
  direttiva «niente foto in cornicette» di [[direttive-siti]].
- Le descrizioni tecniche dei sei effetti e dei quattro trattamenti sono
  mestiere standard, **non parole sue verificate**: nessuno gliele ha fatte
  confermare.
- Non pubblicata. Nessun remote, i tre sbarramenti sono al loro posto.
