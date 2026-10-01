---
type: decisione
riga: Post e storie di DenkiCode li pubblica uno script con l'API ufficiale di Instagram. Deciso da Patrick il 30/09/2026, tocca a Nicola.
data: 2026-09-30
progetto: azienda
updated: 2026-10-01
source: denkicode
tags: [social, instagram, automazione, nicola]
---

# Post e storie Instagram: li pubblica l'API, non una persona

**Deciso da Patrick il 30 settembre 2026**: «ok facciamo la tre». Le tre
strade messe davanti erano Meta Business Suite (gratis, si programma a mano),
contenuti preparati da Trevis e messi in coda da Patrick, e la pubblicazione
automatica con l'API ufficiale di Instagram. Ha scelto la terza.

**Scartati in partenza i bot che entrano con la password**: Instagram li
riconosce e limita l'account, e gli account in gioco sono quelli da cui
partono i DM del banco.

**Tocca a Nicola.** Patrick non scrive codice, e il token lo crea una persona,
non Trevis ([[credenziali]]).

## Cosa fa

Uno script che all'ora fissata prende il prossimo JPEG della coda e lo
pubblica sul profilo di DenkiCode: post, caroselli, storie. I contenuti
nascono dove nascono oggi, `genera-storie.py` e `rendi-storie.sh` in
`03-Storage/brand/social/` ([[materiale-social]]).

Post e storie non portano lead nuovi: servono al profilo quando uno lo apre
dopo il DM ([[generazione-lead]]).

## Cosa dice la documentazione Meta

⚠️ **Letta da Claude il 30/09/2026** su
`developers.facebook.com/docs/instagram-platform/content-publishing`: da
ricontrollare prima di costruirci sopra.

- Solo account **professionale**, business o creator.
- Due passi: `POST /<IG_ID>/media` crea il contenitore,
  `POST /<IG_ID>/media_publish` lo pubblica.
- Immagini **solo JPEG**, su un indirizzo **pubblico** al momento della
  chiamata: l'API le scarica da li', dal Mac non si caricano.
- Tetto di 100 pubblicazioni via API ogni 24 ore. Non morde.
- Permessi: con Instagram Login `instagram_business_basic` e
  `instagram_business_content_publish`; con Facebook Login `instagram_basic`,
  `instagram_content_publish`, `pages_read_engagement` e la Pagina Facebook
  collegata.
- Niente filtri, niente tag prodotto. **Gli sticker non risultano
  supportati**, e lo sticker link sta sulla copertina di ogni serie di storie.

Non letto nella pagina, da verificare: il token lungo di Meta scade (di solito
60 giorni) e va rinnovato, o lo script smette di pubblicare senza dirlo a
nessuno.

## Cosa manca, e a chi tocca

| Cosa | Chi |
|---|---|
| ~~L'handle del profilo~~: **`@denkicode`**, dallo screenshot di Patrick del 30/09 | fatto |
| ~~Il profilo e' professionale?~~ **Si'**: ha la dashboard (1042 visualizzazioni in 30 giorni al 30/09). Collegato a una Pagina Facebook? | Patrick `TODO` |
| App sviluppatore Meta e token | Nicola o Patrick, non Trevis |
| Dove stanno le immagini pubbliche, dove e quando gira lo script | Nicola |
| Il token in una variabile d'ambiente, mai nel vault | Nicola |
| Calendario: quanti post e storie, che giorni, che ore | Patrick l'ha passato a Trevis il 30/09 → [[piano-instagram]] |
| La copertina con lo sticker link: a mano o senza sticker | Patrick |

**La serie del 25/09 non entra in coda** finche' Patrick non l'ha riletta
([[materiale-social]]).

## Costruito il 1 ottobre 2026

Script e cron nel repo `~/lavoro/denkicode-social` (Instagram Login, `graph.instagram.com`, niente Pagina Facebook; le immagini servite da `raw.githubusercontent.com`, quindi repo pubblico). Setup e limiti nel suo `README.md`. Mai provato con un token vero.
