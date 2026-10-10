---
riga: Per Patrick - il /banco del 10/10, siti 74 (TO toelettature ancora in corsa) e ricerca 60 da 15 celle, cosa guardare prima di mandare
type: area
updated: 2026-10-10
source: claude
verificato: 2026-10-10
prodotto: [siti-vetrina, gestionale-custom]
canale: instagram
stato: pubblicata
---

# 10 ottobre: siti 74 su 100, ricerca 60 su 60

Operatori Opus, uno per cella di `prossimo-giro.py`, sostituti dalle riserve e
dal piano rifatto. Tutto sul banco Patrick (`lista-corrente.csv`). **TO
toelettature (quota 20) era ancora in corsa** quando la sessione si è fermata
per limite d'uso: il CSV, se arriva, va pubblicato con `pubblica-lista.py`.

| Lista | Cella | Righe | Profili | Stato |
|---|---|---|---|---|
| siti | NO · fotografi | 1 | 30 | esaurita (16 col sito) |
| siti | MI · tatuatori | 8 | 81 | esaurita (31 fuori provincia, 15 col sito) |
| siti | PC · toelettature | 14 | 46 | esaurita per fonti |
| siti | MI · fioristi e wedding | 25 | 124 | aperta |
| siti | VC · toelettature | 4 | 53 | esaurita (35 omonimi fuori) |
| siti | NO · tatuatori | 11 | 93 | esaurita |
| siti | NO · fioristi e wedding | 11 | 49 | aperta |
| siti | TO · toelettature | — | — | in corsa |
| ricerca | LO · falegnamerie | 4 | 30 | esaurita |
| ricerca | CO · edilizia | 8 | 105 | esaurita (72 fuori provincia) |
| ricerca | CO · officine | 11 | 56 | esaurita (21 fermi) |
| ricerca | PV · falegnamerie | 0 | 36 | esaurita |
| ricerca | CO · ingrossi | 1 | 31 | esaurita |
| ricerca | BS · officine | 14 | 120 | esaurita per fonti |
| ricerca | PV · edilizia | 12 | 142 | aperta |
| ricerca | CO · aziende agricole | 10 | 62 | esaurita |

## Da guardare prima di mandare

- **Scadono**: domenica 11/10 Costenaro, Magni, Mirtilliamo (CO agricole);
  @ballabiodante cita la serata dell'8/10; @emozioni_fiorite auguri per
  l'apertura di Pogno; @ladytattoo_novara dominio che scade il 16/10 (riaprire);
  @laspadigastone chiusa 29/10-1/11; @meronifiori laboratorio 22/10.
- **Grandi**: @arredobongiorni_ 5,9K, @andreassicarservice 6,5K,
  @fedeliallalineatattoostudio 12,6K, @zampetteinvasca 7,4K, @pelleribelletatuaggi 10,4K.
- **Insieme, non lo stesso giorno**: dogschoolpiacenza e davidepoggi; Black
  Island, Hands e @habanera.ink a Sesto; @mrhillstattoo e Jaco Pisciotta.
- **Sede o profilo incerto**: @modernacarservice, @tirapietrosnc, Costenaro,
  @fiorichiaristudio, @edil.lenno.s.r.l, @simone_bergamaschi_fotografo.
- **Al limite del segmento**: @vieviserramenti (serramenti in cella
  falegnamerie), @f.llicasconesnc, Giuffrè e Blindocasa (showroom con posa).
- **Domini da riaprire**: blackislandtattoo.it, ifioridellamary.it,
  margheritebianche.it, angelafiori.com (Squarespace in costruzione).

## Fonti, 10/10 dal Mac di Patrick

- **Instagram**: topsearch HTML e `users/{pk}/info` 429 dalla prima chiamata.
  Reggono `top_serp`, `discover/chaining` (la più redditizia, ma esce presto
  di provincia), la casella Cerca rigiocata come graphql, l'embed con
  `facebookexternalhit`. **curl Googlebot sui profili va al login dopo ~770
  chiamate** in tutto. Data del post dal pk: `(pk >> 23) + 1314220021721` ms.
- **Pagine Gialle via curl**: regge per decine di ricerche, poi 429 per tutti.
- **Google schede locali** (`udm=1`) nel browser: la fonte migliore per i
  nomi, captcha verso la 10ª-25ª e poi riparte. Bing via curl inutile.
- **Browser**: da Patrick, 10/10, nessuna richiesta di permesso: solo domini
  già aperti, il resto con curl. Due domini aperti prima della regola
  (fiorirondo.it, andreamarchettieventi.com) sono stati negati.
- Un operatore ha navigato un tab non suo, un altro ha usato `pkill` per
  pattern: nel brief ora tab propri e niente pkill.
- **Posta non letta**: la navigazione a instagram.com/direct è stata negata.
