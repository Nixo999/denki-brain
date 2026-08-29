---
type: risorsa
updated: 2026-08-29
source: denkicode
tags: [registro, interventi, repo, database]
---

# Registro degli interventi — chi ha toccato cosa, quando, e dove

Una riga per **intervento**, non per commit. Il più recente in cima.

Serve a rispondere in dieci secondi a tre domande che altrimenti costano
mezz'ora di `git log` su due macchine: *chi ha cambiato questa cosa*, *quando*,
e soprattutto **se il database è andato dietro al codice** — perché il push
porta il codice e non lo schema, ed è il modo in cui questo progetto si è già
rotto due volte.

## La regola

**Ogni modifica a un progetto va in due posti**, sempre, dal 28 agosto 2026:

1. **Nel repository del progetto** — commit con il *perché*, e voce nel diario
   del repo se ce l'ha (`docs/07-diario.md` su [[denkishift]],
   `docs/handoff.md` su [[opero]]).
2. **Qui**, una riga. Si scrive **quando il lavoro è finito**, non quando si
   comincia, e prima di chiudere la sessione.

Le regole di push restano quelle di ciascun repo — su [[denkishift]] si pusha
dopo ogni pezzo, su [[opero]] si chiede prima — e il vault si pusha sempre.

⚠️ **La colonna che conta è `Database`.** Se un intervento cambia lo schema e la
migrazione non è stata eseguita, la riga si scrive lo stesso, con ⬜ e il nome
del file: è l'unico posto in cui quel debito resta visibile. Un codice
pubblicato senza la sua migrazione apre un tabellone vuoto.

Colonne: **Quando** (data e ora) · **Chi** (persona, e `+claude` se il lavoro è
stato fatto in sessione) · **Progetto** · **Repository** · **Database**
(`—` se non toccato, `sviluppo`/`produzione` + stato) · **Cosa** · **Commit**.

## 2026-08-29

| Quando | Chi | Progetto | Repository | Database | Cosa | Commit |
|---|---|---|---|---|---|---|
| 01:1x | Nicola +claude | [[opero]] | `opero-sito` | ✅ **sviluppo: `20260829120000_opero_choice.sql` eseguita** (`db push`), e con lei `20260829100000_super_admin_torres_ritenta.sql` che era rimasta indietro. Edge function `send-push` ridistribuita | **OperO Choice**: il Super Admin sceglie una o piu` persone fra tutti gli account di tutte le aziende, scrive, e alla loro prossima apertura esce un messaggio a schermo pieno col pulsante bloccato 5 secondi. Funzione **nuova**, senza originale in OperO 1 → da quotare. ✅ **Verificato nel browser** con Nicola dentro: blocco di 5 s misurato, esce una volta sola, `seen_at` scritto, `send-push` risponde 200 al Super Admin. Resta scoperta la consegna su un telefono vero | `01495b9` `760dda3` |

## 2026-08-28

| Quando | Chi | Progetto | Repository | Database | Cosa | Commit |
|---|---|---|---|---|---|---|
| 16:0x | Nicola +claude | — | — | — | Installati `superdesign`, `playground`, `modern-web-guidance` (~1.030 tok/sessione). **Solo sul PC di Nicola**: i plugin non stanno in git | — |
| 15:2x | Nicola +claude | [[denkishift]] | — | ✅ **sviluppo: `19-lavoratori-a-chiamata.sql` eseguita** dal SQL Editor. `verifica-schema`: 19 su 19 | — |
| 14:5x | Nicola +claude | tutti | `denki-brain` + `smooth-duty` + `opero-sito` | — | **Regola nuova**: ogni modifica va nel repo *e* qui. Registro creato e agganciato ai tre `CLAUDE.md` | `1763144` + questo |
| 14:26 | Nicola +claude | — | `denki-brain` | — | Controllo incrociato dei due repo, guida e nota database allineate alla decisione «non più in locale» | `665e9f0` |
| 14:16 | Nicola +claude | [[denkishift]] | `smooth-duty` | — | **Decisione**: non si avvia più niente in locale, si guarda su `denkishift.it`; migrazione in produzione *prima* del push | `ee6ae92` |
| 14:10 | Nicola +claude | [[denkishift]] | `smooth-duty` | — | `pg` dichiarato in `devDependencies`: su macchina nuova gli script del database non si fermano più | `201f939` `6e31ab9` `d7018da` |
| 14:14 | Nicola +claude | — | `denki-brain` | — | [[patrick-modifica-denkishift]]: guida passo passo per chi non scrive codice | `72eb66e` |
| 13:36 | Patrick +claude | — | `denki-brain` | — | Modulo Word del report settimanale, `.gitattributes` per i binari | `dc13ec5` |
| 13:18 | Nicola +claude | [[denkishift]] | `smooth-duty` | ⬜ **sviluppo: `19-lavoratori-a-chiamata.sql` non eseguita** | Disponibilità del responsabile nel tabellone | `d6a4335` |
| 13:10 | Patrick +claude | — | `denki-brain` | — | Ciclo settimanale: 4 liste la domenica, 5 report indietro | `bdbb8a3` |
| 12:13 | Nicola +claude | — | `denki-brain` | — | Protocollo JARVIS come livello base a ogni avvio | `f563e75` `f84f378` |
| 12:09 | Nicola +claude | [[denkishift]] | `smooth-duty` | ⬜ **sviluppo: `19-lavoratori-a-chiamata.sql` non eseguita** | Lavoratori a chiamata: chi tace non ha accettato | `1b160ea` |
| ~12:00 | Patrick +claude | [[denkishift]] | `denki-brain` | 🟡 sviluppo: catena provata fino alla password, `.env` predisposti e vuoti | Corretta la fotografia del Mac in [[setup-macchina-nuova]]; su DenkiShift `db push` non esiste | `9358c87` |

## Il debito aperto, in chiaro

- ✅ **`19-lavoratori-a-chiamata.sql` eseguita sullo sviluppo** il 28/08 alle
  15:2x, incollata nel SQL Editor da Nicola. `verifica-schema.mjs` risponde
  **19 su 19**: sviluppo e produzione sono allineati fra loro e a `main`
- ✅ **Password del database rimessa.** Era stata **davvero cambiata**: il
  valore vecchio veniva letto e rifiutato, quello nuovo passa. Chi ha ancora
  il vecchio in `.env.db` — qualunque altra macchina — deve rifare il giro
- ✅ **La produzione ha la 19** — verificato nel browser il 28/08 alle 15:0x, da
  una sessione già autenticata: la vista **Disponibilità** si apre e spiega il
  regime, il filtro **«A chiamata»** c'è, il tabellone della settimana 24-30
  agosto è pieno. Quindi `availability_days` e `company_settings.regime_chiamata`
  esistono là. **Il disallineamento è al contrario di come sembrava**: è lo
  *sviluppo* a essere indietro rispetto alla produzione, non il viceversa
- 🟡 Restano due errori in console (`404` e `UnrecognizedActionError: Server
  Action non trovata`), ma sono **del caricamento precedente**: dopo un reload
  pulito nessuna richiesta fallisce. È il caso classico della scheda rimasta
  aperta su una build vecchia mentre ne è stata pubblicata una nuova

## Collegamenti

[[denkishift]] · [[opero]] · [[modifiche-al-database]] ·
[[patrick-modifica-denkishift]] · [[2026-08-28-registro-interventi]]
