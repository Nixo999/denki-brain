---
riga: La posta a freddo dei gestionali - aziende B2B lombarde da 1 a 15 M€, mail con la voce di Patrick dalle caselle di denkicode.it.
type: risorsa
updated: 2026-10-18
source: claude
tags: [posta, outreach, gestionali, automazione]
---

# La posta a freddo per i gestionali

Chiesta da Nicola il 18/10/2026: trovare aziende B2B fra 1 e 15 milioni di
fatturato e scrivere loro per un gestionale su misura, da sole e ogni giorno,
con più mail possibile. Si manda dalle caselle di `denkicode.it` per non
pagare niente ([[2026-10-18-posta-fredda-da-denkicode]]).

## Come gira

| Quando | Chi | Cosa |
|---|---|---|
| ogni mattina feriale, 7:30 | Claude, task `posta-mattina` | legge le risposte, scrive una frase personale per ogni azienda dei due giorni dopo ([[giro-posta]]) |
| ogni 5 minuti, 9:00-17:30 feriali | launchd, `giro.py` | ogni casella manda al massimo una mail, spalmando la quota sulla giornata |
| ogni 30 minuti, 8-20 | launchd, `giro.py` | legge posta in arrivo e Spam: risposte, fuori sede, rimbalzi, «no grazie» |
| quando una risposta è vera | Patrick | risponde lui, dalla sua casella: le risposte arrivano tutte a `patrick@` |

## I numeri che decidono il volume

- **Rampa per casella**: 10 mail al giorno la prima settimana, 20 la seconda,
  30 dalla terza (`config.py`, `RAMPA`). Register.it ne permetterebbe 500, ma
  oltre 30-50 i filtri cominciano a buttare in spam ([[2026-09-02-cold-email-gestionali]]).
- **Tre caselle**: circa 90 mail al giorno a regime, seguiti compresi. Ogni
  azienda ne riceve due, quindi sono **circa 45 aziende nuove al giorno**.
  Per salire servono più caselle, cioè domini secondari.
- **Due mail per azienda al massimo**: la prima e un seguito dopo 4 giorni
  lavorativi, nello stesso filo. Chi risponde, anche solo «fuori sede», non
  riceve il seguito se la risposta è vera.
- **Freno**: sopra il 5% di rimbalzi in un giorno, o al primo rifiuto per spam,
  l'invio si ferma da solo. Si riparte con `manda.py --togli-freno` dopo aver
  letto il motivo in `dati/manda.log`.

## Chi riceve la mail

Solo **persone giuridiche** (Srl, SpA, cooperative, consorzi), attive, in
Lombardia, fra 1 e 15 milioni di fatturato dall'ultimo bilancio depositato
(companyreports.it), con almeno 6 dipendenti, nei settori dove un gestionale
morde: officine, manifattura, impianti, edilizia, ingrosso, trasporti,
logistica, pulizie. Solo **caselle generiche** (`info@`, `commerciale@`)
trovate sul sito dell'azienda, mai PEC e mai nomi di persona: è il perimetro
che la decisione del 2 settembre giudica difendibile.

## La mail

Lo scheletro fisso sta in `testi.py`, con una variante per settore; Claude
scrive solo una frase personale presa dal sito dell'azienda. Le scelte e i
libri da cui vengono sono scritti in testa a `testi.py`: Gitomer per la frase
personale, Challenger per il problema del settore, SPIN per la domanda,
Klaff e Voss per la richiesta di mezz'ora («se state già bene così, ve lo dico
e vi saluto»), lo script di Patrick per il resto ([[script-gestionali-brianza]]).
Ogni mail passa da `voce-check.py` prima di entrare in coda.

In fondo a ogni mail c'è da dove viene l'indirizzo e come non ricevere altro:
non è una traccia del processo, la chiede la legge.

## Quante aziende ci sono — misurato il 19/10

Sul campione di Milano e Monza (officine 25.53 e 25.62, ingrosso 46.64 e 46.69):

| | |
|---|---|
| In filtro dopo la lista | 158 |
| Sito trovato | 65, cioè il 41%; 54 provati con la partita IVA |
| **Pronte, con casella generica** | **48**, dopo aver rimesso dentro cinque esportatrici italiane |
| Senza sito / senza casella | 93 / 9 |
| Filiali di gruppi esteri, scartate | 8 |
| Tempo | circa 14 minuti ogni 100 aziende, 6 in parallelo |

Stima per la Lombardia, più o meno il 20%: circa **40.000 aziende nei filtri**,
quindi circa 10.000 pronte a questa resa. A 45 aziende nuove al giorno sono più
di un anno di invii: il collo di bottiglia sono le caselle, non le aziende.
Ogni sera alle 19 `giro.py` cerca un settore nuovo, a turno, se la scorta di
pronte scende sotto 200.

## I file

| File | Cosa fa |
|---|---|
| `aziende.py` | scarica le aziende da companyreports.it per codice ATECO e applica i filtri |
| `trova-mail.py` | trova il sito (la prova forte è la P.IVA nel piè di pagina) e la casella generica |
| `scrivi.py` | prepara le aziende per Claude, importa le frasi, compone e controlla le mail |
| `manda.py` | manda, con rampa, finestra, freno e copia nella posta inviata |
| `leggi-risposte.py` | riconosce risposte, automatiche, disiscrizioni e rimbalzi |
| `mattina.py` | i due comandi fissi del giro del mattino |
| `giro.py` + `com.denkicode.posta.plist` | il giro ogni cinque minuti, via launchd |
| `testi.py` | i testi fissi: si cambiano solo qui |
| `config.py`, `caselle.example.env` | rampa, orari, feste; il modello del file delle caselle |

**Le password e i dati stanno fuori da git.** Le caselle sono in
`~/.config/denki-posta/caselle.env` (permessi 600). La base dati, il registro
degli invii e il riassunto delle risposte stanno in `02-Sales/posta/dati/`, che
git ignora: il vault è un repository **pubblico** su GitHub (controllato il
18/10/2026), e lì dentro ci sono indirizzi, nomi e testi di chi risponde.

## Prima di accendere — `TODO`

- [x] launchd installato il 19/10 (`~/Library/LaunchAgents/com.denkicode.posta.plist`):
      il primo avvio è uscito senza errori. Si ferma con
      `launchctl unload ~/Library/LaunchAgents/com.denkicode.posta.plist`.
- [x] Task `posta-mattina` creato il 19/10, alle 7:30 dei giorni feriali, salvato in
      modalità automatica. Se il primo giro si ferma ad aspettare un permesso,
      serve la parola `"posta-mattina"` in `TASK_NOSTRI` di `.claude/hooks/permessi-giro.py`,
      e la mette Nicola a mano.
- [x] **DMARC e DKIM su `denkicode.it`**, messi da Nicola il 19/10: DMARC `p=none` con
      i rapporti a `nicola@`, DKIM `key-regi001` allineato. Antispam di register.it da 0,43 a −1,60.
- [ ] Le prime 10 mail vere, in `dati/prime-10-da-rileggere.txt`, rilette da
      Nicola; poi `ATTIVO=1` in `~/.config/denki-posta/caselle.env`.
- [ ] Il numero di Patrick sotto la firma, se lo vuole (`TELEFONO`).
- [ ] Patrick sa che le risposte arrivano in `patrick@denkicode.it` e la legge.

Finché `ATTIVO=0` il giro del mattino scrive le mail per i due giorni dopo e
si ferma lì: la coda arriva a circa 60 mail e non cresce oltre.

## Collegamenti

[[2026-10-18-posta-fredda-da-denkicode]] · [[2026-09-02-cold-email-gestionali]] ·
[[giro-posta]] · [[core-commerciale]] · [[generazione-lead]] · [[italiano-chiaro]]
