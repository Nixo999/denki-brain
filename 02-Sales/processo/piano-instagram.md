---
type: risorsa
riga: Cosa pubblica @denkicode, quanto, quando, con che didascalie e hashtag. Deciso da Trevis il 30/09/2026 su delega di Patrick, si rivede a 4 settimane.
updated: 2026-09-30
source: claude
tags: [social, instagram, piano, lead]
---

# Piano Instagram di @denkicode

Patrick l'ha delegato il 30/09/2026: «decidi cosa postare, quanto, come,
quando, con che descrizioni e hashtag». Le prove stanno in
[[ricerca-instagram]]. Pubblica lo script di
[[2026-09-30-instagram-pubblicazione-api]]; finche' Nicola non lo costruisce,
si pubblica a mano con gli stessi orari.

## A cosa serve il profilo

1. **Convincere chi ha appena ricevuto un DM dal banco.** Apre @denkicode e in
   cinque secondi deve capire chi siamo, per chi lavoriamo e che dietro c'e'
   una persona. E' il pubblico piu' sicuro che abbiamo: arriva ogni giorno.
2. **Farsi trovare da titolari che non ci conoscono.** Ci arrivano solo i Reel
   e gli invii in DM: a 87 follower un post raggiunge otto persone.

L'obiettivo non sono i follower: sono le visite al profilo e i DM in entrata.

## Subito, a mano, una volta sola (Patrick)

- **Campo nome**: `DenkiCode | Siti web per negozi`. E' l'unico campo del
  profilo che la ricerca legge. Se Instagram lo taglia, `DenkiCode | Siti web`.
- **Bio**, al posto di quella di adesso (139 caratteri, limite 150):
  ```
  Siti web per chi lavora in negozio o in salone.
  Prima ti facciamo vedere la bozza del tuo sito, gratis.
  Se ti piace, ne parliamo. Seveso (MB)
  ```
  «Milano» diventa «Seveso (MB)», che e' dove siamo. La bio di adesso e' a
  slogan, lo stesso errore dei profili che non rendono.
- **Quattro storie in evidenza**, quante se ne vedono senza scorrere: `Lavori`,
  `Come funziona`, `Consigli` (la serie del 16/09 c'e' gia'), `Chi siamo`.
- **Non si segue per farsi seguire.** 27 seguiti contro 87 follower: resta
  cosi'. Piu' seguiti che follower, a chi riceve il DM, sembra un bot.

## Quanto e quando

Ora di Roma. Lo script gira su `Europe/Rome`, non su UTC: il 25/10 si torna
all'ora solare e un cron in UTC sposterebbe tutto di un'ora.

| Cosa | Quando | Perche' |
|---|---|---|
| Reel | domenica 21:00 | la sera prima del lunedi' chiuso di saloni e studi; i Reel rendono la domenica |
| Carosello | martedi' 13:30 | pausa pranzo, finestra feriale di tutti gli studi |
| Carosello, o il Reel di Patrick | giovedi' 21:00 | dopo la chiusura |
| Una storia | ogni giorno alle 8:00 | dura fino a sera: chi apre il profilo dopo il DM trova il cerchio acceso |

Tre post a settimana: sotto i tre la crescita si dimezza, sopra non ci sono
le ore. **Il sabato niente**, i negozi lavorano. Gli orari sono un'ipotesi,
perche' nessuno studio dice quando usano Instagram i titolari: restano fermi
quattro settimane, poi si guarda.

## Cosa si pubblica: quattro serie fisse

Una serie ha un nome e un modello: non si inventa ogni volta.

1. **«Il sito di…»**: Reel di 10-15 secondi, un nostro sito online che scorre
   sullo schermo di un telefono, una riga di testo sopra. Senza musica: l'API
   non la mette. Solo siti su un dominio loro, **mai bozze**.
   ⚠️ **Oggi uno solo senza riserve: Albybike.** Fiftynine per la sua nota e'
   ancora una bozza in trattativa su `netlify.app`, anche se la galleria
   scrive `bartabacchi59.it`; Dropout non e' un lavoro per un cliente; V-BAG
   ha il pulsante d'ordine morto; Bellastoria sta su `netlify.app`.
2. **«Una scena per mestiere»**: carosello di cinque slide 1080x1350, un
   mestiere per volta (parrucchiere, estetista, tatuatore, barbiere, nail,
   lash, pasticceria). La prima slide e' una scena col cliente del titolare;
   la seconda regge da sola, perche' Instagram ripropone il carosello partendo
   da li'; l'ultima e' la bozza gratis. I testi vengono dalle due serie di
   storie gia' scritte.
   ⚠️ **L'agenda nel sito non si promette** finche' Nicola non dice che si
   vende: su [[sito-newfantasy]] le prenotazioni stanno nel `localStorage`.
3. **«Chi c'e' dietro»**: Reel di Patrick in faccia, 20-30 secondi, uno ogni
   due settimane. Lo gira e lo pubblica lui a mano, con un audio di tendenza.
   Si presenta come «Patrick, del team di DenkiCode», non come il capo
   ([[stile-comunicazione]], 20/09). Quasi tutti i profili visti rendono di
   piu' col post personale.
4. **Storie**: nei giorni del post, la copertina del post; negli altri, una
   delle sei storie del 16/09 a giro, e quelle del 25/09 quando Patrick le ha
   rilette. Sticker e link solo in una storia messa a mano.

**Fuori, finche' Patrick non dice altro**: la scheda Google e il «come
lavoriamo» (tolti da lui il 16/09), le bozze ai lead, i rifacimenti non
chiesti di siti di altri, le grafiche fatte con l'AI, i numeri che non
possiamo sostenere.

## Didascalie e hashtag

- **Prima riga sotto i 125 caratteri**: la scena o il fatto. E' l'unica che si
  legge prima di «altro». Mai una domanda in apertura.
- **Reel sotto i 200 caratteri. Carosello 300-500**, con il mestiere e la
  parola «sito» scritti per esteso: li leggono la ricerca e Google.
- **Chiusura: «scrivici BOZZA in DM».** Mai «commenta SI'»: e' esca, e
  Instagram toglie reach.
- **Tre hashtag**: il mestiere, uno di contorno, `#sitoweb`. Il limite e' 5 ma
  ne e' stato provato 3, e comunque non portano reach.
- Ogni didascalia passa da `voce-denkicode`. Voce di Patrick al plurale, come
  i DM dall'account aziendale.

## Le prime due settimane

| Sett. | Giorno | Cosa | Mestiere |
|---|---|---|---|
| 1 | dom 21:00 | Reel «Il sito di Albybike» | negozio di bici |
| 1 | mar 13:30 | Carosello «Il telefono in una mano» | estetista |
| 1 | gio 21:00 | Carosello «L'indirizzo e il telefono» | tatuatore |
| 2 | dom 21:00 | Reel «Chi c'e' dietro», Patrick | tutti |
| 2 | mar 13:30 | Carosello «Le foto» | parrucchiere |
| 2 | gio 21:00 | Carosello «Chi cerca su Google» | barbiere |

Le didascalie, pronte da copiare, stanno in [[didascalie-instagram]].

## Cosa serve a Nicola

Lo script della decisione, con il cron su `Europe/Rome`; il generatore di
`03-Storage/brand/social/` che faccia anche il carosello 1080x1350 oltre alla
storia 1080x1920; il Reel «Il sito di…» registrato da solo, un sito che
scorre su uno schermo da telefono. Il come lo decide lui.

## Come si misura, a quattro settimane dal primo post

Da Insights, Patrick: visite al profilo, account raggiunti che non ci
seguono, invii dei Reel, DM in entrata con «BOZZA». **Si cambia una cosa per
volta**: prima l'orario del Reel, poi i mestieri.

## Cosa manca

- Patrick: quali siti oltre Albybike si possono mostrare; nome e bio; tipo di
  account, Business o Creator (le storie via API forse solo Business);
  Pagina Facebook collegata; rilettura della serie del 25/09. `TODO`
- Nicola: se l'agenda nel sito si puo' vendere. `TODO`
