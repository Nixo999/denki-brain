---
type: decisione
riga: verificato lo scrive /chiudi-sessione sulle note toccate in sessione che Nicola o Patrick approvano. 109 note su 246 erano ipotesi. 27/09/2026.
data: 2026-09-27
progetto: vault
updated: 2026-09-27
source: denkicode
tags: [vault, verificato, chiusura]
---

# `verificato:` lo scrive la chiusura, sulle note approvate in sessione

**Approvata da Nicola il 27 settembre 2026**, nello stesso giro di
[[2026-09-27-daily-abolita]].

## Il fatto

151 note su 246 erano `source: claude`, 109 senza `verificato:`: per le regole
del vault il 44% del suo contenuto era un'ipotesi. `genera-indice.py` lo
stampava a ogni giro e nessuno chiudeva il buco. Le note dei siti sono scritte
con Nicola presente che approva i giri: il lavoro le verifica, il campo non lo
diceva.

## La scelta

- Alle cinque domande di `/chiudi-sessione`, se Nicola o Patrick rispondono,
  ogni nota `source: claude` **toccata in quella sessione** riceve
  `verificato: <oggi>`. La risposta è la verifica.
- Se non rispondono, le note restano ipotesi e la chiusura lo dice in una riga.
- Le 109 note vecchie **non si marcano in blocco**: si verificano quando si
  riaprono per lavorarci, contro la cosa vera. Il conteggio di
  `genera-indice.py` deve scendere per lavoro, non per decreto.

## Scartato

- Marcare verificate tutte le note progetto scritte dopo il 10/09: verifica per
  decreto, e il campo tornerebbe a non dire niente.
- Togliere il campo: il punto 3 di [[come-si-scrive-una-nota]] resta giusto,
  mancava solo chi lo scrive.

## Collegamenti

[[come-si-scrive-una-nota]] · [[2026-09-27-daily-abolita]] ·
[[registro-interventi]]
