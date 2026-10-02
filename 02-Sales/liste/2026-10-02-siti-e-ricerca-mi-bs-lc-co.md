---
riga: Per Patrick - il /banco lasciato a meta' l'1/10 finito da Nicola il 2/10: 144 righe sul banco (siti 86, ricerca 58), cosa guardare prima di mandare
type: area
updated: 2026-10-02
source: claude
verificato: 2026-10-02
prodotto: [siti-vetrina, gestionale-custom]
canale: instagram
stato: pubblicata
---

# 2 ottobre: il banco che avevi lasciato a metà

Patrick, l'1/10 sera il tuo `/banco` aveva letto la posta di `@patrick.sappa`
(commit `021fdbf`) e si era fermato lì: nessuna lista. Il 2/10 Nicola l'ha
finito dal suo Mac: piano di `prossimo-giro.py`, un operatore per cella.

**Sul banco ci sono 144 righe nuove, tutte sul banco Patrick
(`lista-corrente.csv`)**: siti 86 su 100, ricerca 58 su 60. In tutto ora
**877 da mandare**, 7 recuperi maturi. Le righe le vedi da `/banco apri`.

| Lista | Cella | Righe | Profili | Stato cella |
|---|---|---|---|---|
| siti | MI · tatuatori e piercing | **25** | 50 | aperta, 1 su 2 |
| siti | BS · toelettature (+ NO di riserva) | **21** (17 + 4) | 99 + 30 | tutte e due esaurite |
| siti | MI · sartorie, atelier, tappezzieri | **23** | non contati | aperta |
| siti | LC · fotografi e videomaker | **10** | 35 | aperta, fonti finite |
| siti | MI · personal trainer, pilates, yoga (riserva) | **7** | non contati | aperta |
| ricerca | MI · alimentari artigianali | **20** | 67 | aperta, 1 su 3,4 |
| ricerca | CO · edilizia e serramenti | **20** | 64 | aperta, 1 su 3 |
| ricerca | MI · edilizia e serramenti (riserva) | **11** | non contati | aperta |
| ricerca | MI · falegnamerie (+ CO di riserva) | **7** (5 + 2) | 31 + 27 | tutte e due esaurite |

Mancano 14 siti e 2 ricerca: le celle e le riserve del piano si sono chiuse
per resa, o gli operatori si sono fermati prima. Il prossimo `/banco` riparte
da celle nuove: `rotazione.csv` è aggiornato.

## Da guardare prima di mandare

- **@zampamore.toelettatura**: post di lutto il 29/9. **@petrelli.tattoo**:
  ultimo post (28/7) ricorda un animale scomparso. I tempi li decidi tu.
- **Fermi da qualche mese**, scritto in scheda: @_lucatanti (marzo),
  @amico_valentina (luglio, 235 follower), @toelettatura_simona,
  @gingerstoelettatura, @doggycare_vale_ (luglio-agosto), Guzzafame (4/9).
- **@francescasandoliphotographer**: Facebook la dà anche a La Spezia.
- **Ricerca CO, oltre i 50 km**: Gravedona (FGS) e Menaggio (Greco) dicono
  «lago di Como», non «qui in zona». Nettare dei Santi (San Colombano) dice
  «del Milanese».
- **Infissi e Dintorni** è più negozio con posa che impresa: decidi tu.
- **@puntounoarreda**: indirizzo non letto, il sito si carica via script.
- **Quattro tatuatori nominano Fresha**: sono schede Fresha che la pagina
  stessa dice non collegate allo studio, e il messaggio lo dice. Non è il
  caso «è su Fresha e gli dici che non ha il sito».

## Cosa non è passato

- **La posta di DenkiCode non è letta.** Nel browser dell'app di Nicola
  Instagram non è loggato. Dall'1/10 resta da leggere la posta dei DM partiti
  da DenkiCode (16-17/09 e 29/09, più i 160 del 29/09).
- **Instagram letto da sloggati**: follower, bio, date e didascalie dei post
  si leggono senza login, più di 400 profili in giornata senza muro.
- **Startpage è vietato** (Nicola, 2/10, in [[metodo-liste]]): nel browser
  dell'app chiede il permesso a ogni azione. Motori che hanno retto: Yahoo
  (letto come testo, mai bloccato), DuckDuckGo html (captcha dopo 13-24
  query). Pagine Gialle dà nomi e indirizzi, quasi mai l'Instagram.
- **Resa della fonte (1)**, finalmente misurata: le query
  `site:instagram.com <settore> <comune>` portano profili di tutta Italia;
  rende cercare **per nome** le attività trovate su Pagine Gialle,
  matrimonio.com (fotografi) o nelle zone note (cascine del Parco Sud).

## Trappole nuove

- Le date dei post passate per `toISOString()` escono un giorno indietro:
  corrette, si usa la data scritta nell'alt.
- `verifica-sito.py` dava «morto» o «parcheggiato» a domini vivi sul `www.`
  (toelettaturaeself.it, giadacalamida.it) e «vivo» a pagine Coming Soon con
  3000 caratteri di CSS davanti: corretto il 2/10, riprova il `www` e legge il
  testo visibile.
- Tre operatori si sono fermati da soli a metà (sartorie, personal trainer,
  edilizia MI): le righe erano già nel file, la verifica dei siti l'ha
  lanciata Nicola. Per questo lì i profili aperti non sono contati.
