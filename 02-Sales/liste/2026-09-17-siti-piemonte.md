---
riga: La lista siti del 17 settembre - 50 righe di bellezza fra Torino e il resto del Piemonte, zona nuova aperta perche' la Lombardia della bellezza e' finita, e le toelettature abbandonate dopo 110 ricerche.
type: area
updated: 2026-09-17
source: denkicode
verificato: 2026-09-17
prodotto: [siti-vetrina]
canale: instagram
stato: pubblicata
---

# 17 settembre — il Piemonte, e le toelettature buttate a meta' mattina

Costruita una lista sola, non tre. DenkiShift e ricerca **hanno gia' 50 righe
ciascuna sul banco dal 14 settembre, mai mandate**: aggiungerne altre 50 per
tipologia avrebbe portato a 100 righe ferme per prodotto. Le righe siti da
mandare erano **4**, e quelle si sono rifatte.

| Lista | Consegnate | Dove | Settore |
|---|---|---|---|
| Siti vetrina | **50** | Piemonte: Torino e provincia, Alessandria, Asti, Cuneo, Novara, Biella, Vercelli, VCO | onicotecniche, estetiste, lash maker, trucco permanente |
| DenkiShift | — | gia' 50 sul banco dal 14/09 | — |
| Ricerca di mercato | — | gia' 51 sul banco dal 13-14/09 | — |

## Perche' il Piemonte, e perche' oggi

La bellezza lombarda e' battuta in tutte le province della rotazione: Varese,
Como, Lecco e Bergamo il 10, Brianza l'11, Milano il 12, Brescia il 13,
Brescia e Bergamo il 14, Bergamo il 16. La rotazione dei comandi dice di
scendere, e [[metodo-instagram]] mette **Torino nell'anello 4**. Quindi: zona
vergine, e dentro la zona **il settore che rende di piu'** invece di un settore
di riserva in una zona esaurita.

## Le toelettature: 110 ricerche, 38 candidati, chiuse

Primo tentativo del giorno, sbagliato: toelettature e dog grooming fra Milano,
Brianza, Brescia, Bergamo e la bassa. **110 query hanno dato 38 candidati**,
0,35 per ricerca. La bellezza in Piemonte, con le stesse identiche query, ne ha
dati **4,8 per ricerca**, quattordici volte tanto.

⚠️ **Era gia' scritto, e non e' stato letto prima di partire.** La tabella dei
segmenti di [[metodo-instagram]] dice che gli animali sono **il settore col
tasso di sito piu' alto trovato finora** (33 profili su 84 il 10 settembre) e
che il bacino e' stretto perche' meta' delle toelettature non ha Instagram.
Mezz'ora persa per non aver aperto la tabella che quella mezz'ora la risparmia.

## Il giro: 300 ricerche, 692 profili letti

Cinquanta comuni piemontesi per sei formule di ricerca (`nails`, `unghie`,
`estetica`, `beauty`, `centro estetico`, `lashes`), poi ogni `pk` letto da
`/api/v1/users/{pk}/info/` come nel riquadro del 16 settembre. **Zero 429 su
692 letture.**

| | Quanti |
|---|---|
| profili letti | **692** |
| sotto i 200 follower | **221** |
| fuori Piemonte | 130 |
| **avevano un sito proprio** | **74** |
| privati | 53 |
| meno di 20 post | 28 |
| tenibili | 186 |
| **consegnate** | **50** |

Le 136 tenibili non usate restano il bacino di domani: la zona non e' finita,
e' appena aperta.

> [!tip] La scheda nascosta dimezza tutto, e sei worker lo risolvono
> Il pannello del browser resta `visibilityState: hidden` anche quando lo si
> porta in primo piano, e Chrome rallenta la scheda: **13 profili al minuto**
> con un ciclo solo. Sei cicli paralleli sulla stessa mappa, con un `Set` di
> prenotazione per non leggere due volte lo stesso profilo, sono saliti a
> **68 al minuto**. Il 16 settembre il problema non si era visto perche' la
> scheda era davanti.

## Cosa e' stato buttato a mano, dopo i filtri

- **@anchierinadia** (Uruguay) e **@unasconro.sf** (Cordoba, Argentina): la
  ricerca «nails alba» e «nails bra» tira dentro il Sudamerica.
- **@nails_alba_adriatica**: Alba Adriatica e' in Abruzzo. **@alba.odith_nails**
  e **@skincareconalba**: si chiamano Alba. Quattro profili su una parola sola.
- **@lidiatianails**: in bio «NON STO LAVORANDO».
- **@beauty_center_torino** e **@dottoressalauramarello**: medicina estetica,
  fuori come a Bergamo il 16.
- **@ejiro_beauty_academy_biella**: accademia, e ha `ejiroacademy.weblium.site`.
- **@bodycharmeborgomanero**: il `bit.ly` in bio porta a
  **esteticabodycharme.com**. Il sito ce l'hanno.
- Bio vuota, quindi complimento impossibile: **@nails_davida**,
  **@estetica_afrodite_tortona**, **@unghie_gel_verbania**,
  **@solariumbeautyglobalrivoli**, **@verka_nails_novara**, **@antobeauty89**.

⚠️ **Gli accorciatori vanno aperti, sempre.** Due `bit.ly` in bio: uno portava
al sito loro (fuori lista), l'altro al negozio online di un fornitore
(`shop.dermophisiologique.it`, dentro come gancio 5). Senza `curl -I` sarebbero
finiti tutti e due nel mucchio sbagliato.

## I ganci

40 righe con gancio 1 e 10 con gancio 5: Linktree (2), Treatwell (2), pagine
`my.canva.site` (2), Taplink (1), Calendly (1), un Linktree intestato a un
altro nome (1) e il negozio online di un fornitore (1).

Le province: Torino 25, Alessandria 11, Cuneo 5, Asti 4, Novara 2, poi una
riga a testa per Biella, Vercelli e il Verbano.
Una riga sola merita una nota: **@studiogirotto.it** ha l'handle che finisce in
`.it` e il dominio `studiogirotto.it` **non ha DNS**. Tenuta fuori dalle 50
perche' il centro apre il 10 ottobre e la bozza avrebbe poco da mostrare.

## Controlli

| | Esito |
|---|---|
| `voce-check.py` | 1 tell su 50 (tre «e» in fila su @anastasia.nailstudio), riscritto, poi **0** |
| `verifica-sito.py` | girato con i motori su 50 righe |
| `controlla-lista.py` | **0** |

## Collegamenti

[[metodo-instagram]] · [[metodo-liste]] · [[2026-09-16-tre-liste-bergamo-lago-aziende]] ·
[[2026-09-17-rilanci-lead-aperti]] · [[stile-comunicazione]] · [[dm-instagram-vetrina]]
