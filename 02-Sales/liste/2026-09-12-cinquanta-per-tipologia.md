---
riga: Le liste portate a 50 per tipologia - ricerca su tutta la Lombardia, siti su Milano, e i tatuatori che il sito ce l'hanno.
type: area
updated: 2026-09-12
source: claude
verificato: 2026-09-12
prodotto: [siti-vetrina, denkishift, gestionale-custom]
canale: instagram
stato: pubblicata
---

# 12 settembre 2026 — cinquanta per tipologia, e il perimetro che cambia

Patrick: *«io voglio 50 contatti per tipologia, non mi interessano scuse […]
basta che siano in lombardia per denkishift e gestionali. per quanto riguarda i
siti possono essere in tutta italia»*. Regola scritta in [[metodo-liste]].

| Lista | Prima | Aggiunte oggi | Sul banco |
|---|---|---|---|
| Siti vetrina | 43 | **9** (Milano e hinterland) | **52** |
| DenkiShift | 43 | **7** (Brescia, Bergamo, Pavia) | **50** |
| Ricerca di mercato | 9 | **41** (tutta la Lombardia) | **50** |

## Ricerca di mercato — il perimetro largo risolve il problema

Ieri la lista si era fermata a 9 perché la ricerca di Instagram non trova gli
artigiani per comune. **Allargando a tutta la Lombardia il problema sparisce**:
con ottanta query su dieci città (Milano, Brescia, Bergamo, Pavia, Cremona,
Mantova, Lecco, Lodi, Varese, Como) sono usciti 154 profili e ne sono rimasti
41 buoni.

Dentro: carrozzerie e officine da Milano a Mantova, serramentisti da Bergamo a
Cremona, falegnamerie milanesi, carpenterie, impiantisti, imprese edili e
rivendite di materiali, trasportatori e una società che gestisce magazzini per
conto terzi.

⚠️ **Venti righe hanno il profilo aperto e letto, ventuno no**: per quelle la
prova in colonna dice esattamente questo, «letto dal titolo e dai contatori, la
bio non è stata aperta». Prima di scrivere a quelle righe si apre il profilo:
sta scritto anche nella scheda.

## Siti — il settore sbagliato si abbandona subito

Il settore del giorno per la Brianza erano **tatuatori e toelettature**. Ha
reso **1 riga su 7**: sei avevano già un sito vivo col loro nome. È lo stesso
esito dei mobilifici, e vale la pena saperlo prima di riprovarci.

Cambiata zona invece che insistere: **Milano e hinterland** (Sesto San
Giovanni, Cinisello, Rho, Legnano, Bollate), settore bellezza, che resta quello
che rende. Nove righe, tutte passate da `verifica-sito.py`: **zero avevano un
sito vivo**, due sono su una piattaforma di prenotazione e il messaggio la
nomina.

## DenkiShift — fuori dalla Brianza

Sette righe da Brescia, Bergamo e Pavia: due pasticcerie con laboratorio, un
panificio e pasticceria, due ristoranti, un albergo del 1913 e una bottega.
Una riga è stata scartata perché l'handle era già sul banco, e `controlla-lista.py`
l'ha fermata prima della pubblicazione.

## I controlli

`controlla-lista.py` **ok** su tutte e tre le liste nuove. `voce-check.py`:
**zero tell** su siti e DenkiShift, e sulla ricerca resta solo «link nel
messaggio», che lì è voluto.

## La rotazione, da adesso

Un settore al giorno. Quando i settori di una zona finiscono, circa quindici
giorni, si passa alla zona dopo: **Monza e Brianza → Milano → Como → Varese →
Brescia**, e così giù fino alla Sicilia. Sta scritto nel comando `/banco`.

## Collegamenti

[[metodo-instagram]] · [[metodo-liste]] · [[dm-instagram-ricerca]] ·
[[dm-instagram-vetrina]] · [[dm-instagram-denkishift]] ·
[[2026-09-11-tre-liste-brianza]] · [[2026-09-11-comando-banco]]
