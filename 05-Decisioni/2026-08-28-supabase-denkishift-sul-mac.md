---
type: decisione
data: 2026-08-28
progetto: denkishift
source: denkicode
stato: attiva
updated: 2026-08-28
---

# Le migrazioni di DenkiShift si possono lanciare anche dal Mac di Patrick

**Chiesto da Patrick il 28 agosto 2026**, poche ore dopo la decisione di far
pushare git da quella macchina ([[2026-08-28-push-automatico]]).

Corregge in parte quanto scritto la mattina stessa al punto 0 di
[[setup-macchina-nuova]] — «sul Mac di Patrick non si mettono i repo né le
chiavi Supabase» — che era già superato dai fatti prima di essere scritto.

## Cosa si è scoperto guardando la macchina

Il vault diceva una cosa, il disco ne diceva un'altra:

| Il vault sosteneva | Sul Mac c'è davvero |
|---|---|
| Repo assenti «per scelta» | `smoothduty`, `opero-sito`, `opero-core`, `capacitor` — **tutti sul Desktop**, non in `~/denkicode/` |
| Nessuna chiave Supabase | `opero-sito/.env.local` **c'è già** |
| DenkiShift: migrazioni solo a mano nel SQL Editor | Il repo ha `scripts/esegui-sql.mjs`, che le esegue dal terminale |

La regola del `CLAUDE.md` ha funzionato: sul tecnico ha ragione il repo. Le
prime due righe erano una fotografia sbagliata, la terza era vera mesi fa e non
lo è più.

## La decisione

**Sì, da questo Mac si lanciano le migrazioni di DenkiShift**, sul progetto di
**sviluppo** `rytuurzafjxzlrpgforj`. Il «push su Supabase» di DenkiShift è
questo, e non `supabase db push`, che su questo progetto non esiste:

```bash
cd ~/Desktop/smoothduty
node --env-file=.env.local --env-file=.env.db scripts/verifica-schema.mjs
node --env-file=.env.local --env-file=.env.db scripts/esegui-sql.mjs supabase/NN-nome.sql
```

**La produzione resta fuori.** `denkishift.it` gira su un progetto Supabase
diverso, e toccarlo è una decisione a sé, da prendere con Nicola. Non è una
cosa che capita di striscio mentre si prova qualcosa in sviluppo.

## Cosa manca per chiuderla

Tre valori, che nessuno può recuperare al posto di Patrick perché stanno dietro
al suo login Supabase. I file sono già pronti e già ignorati da git:

| File | Riga | Dove si legge |
|---|---|---|
| `.env.local` | `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Supabase → *Project Settings › API* |
| `.env.local` | `SUPABASE_SERVICE_ROLE_KEY` | idem, sezione secret |
| `.env.db` | `SUPABASE_DB_PASSWORD` | Supabase → *Project Settings › Database* |

**Non si passano su WhatsApp e non si passano per email**, come già scritto in
[[setup-macchina-nuova]]: si leggono dal pannello, sul Mac, e si incollano lì.

> [!note] Analisi di Claude — 2026-08-28
> Il rischio di questa decisione è basso, ma non è zero, e vale la pena dire
> dov'è. `SUPABASE_SERVICE_ROLE_KEY` **scavalca ogni regola di sicurezza** del
> database: chi ce l'ha legge e scrive tutto, comprese le causali di assenza
> che il resto dell'app protegge apposta. Qui però parliamo del progetto di
> **sviluppo** di un prodotto con **zero clienti paganti** ([[denkishift]]): i
> dati dentro sono squadre inventate e un foglio orari di prova. È il posto
> giusto dove sbagliare.
>
> Il confronto è con [[opero]], dove la stessa chiave sul progetto di
> produzione vede i dipendenti veri delle aziende di [[sebastian-torres]]. Lì
> la cautela del punto 0 resta intera.
>
> Due cose da tenere d'occhio, entrambe già vere oggi: **FileVault** su questo
> Mac (una chiave su un disco non cifrato è una chiave regalata a chi trova il
> portatile), e il fatto che le chiavi di OperO siano **già** qui senza che
> nessuno l'avesse deciso. La seconda è più grossa della prima.

## Un difetto trovato per strada

`scripts/lib-db.mjs` importa `pg`, ma **`pg` non è dichiarato nel
`package.json`** di `smooth-duty`. Su una macchina appena installata i comandi
delle migrazioni si fermano con `Cannot find package 'pg'`. Sul Mac è stato
aggirato con `npm install pg --no-save --no-package-lock`, che non sporca il
repo.

**Da dire a Nicola**: la correzione è una riga nel suo `package.json`, e sta
nel suo repo — non si tocca da qui.

## Collegamenti

[[denkishift]] · [[setup-macchina-nuova]] · [[2026-08-28-push-automatico]] ·
[[opero]] · [[stack]]
