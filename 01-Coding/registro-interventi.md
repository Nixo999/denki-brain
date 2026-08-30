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

## 2026-08-30

| Quando | Chi | Progetto | Repository | Database | Cosa | Commit |
|---|---|---|---|---|---|---|
| 02:5x | Nicola +claude | [[castiglione-furniture]] | `castiglione-site` | — | **Spazi e foto ribilanciati** su feedback di Nicola (capitoli semivuoti, crop stretto). Tre bug veri: reset `img` senza `height:auto` (l'attributo height teneva un'immagine a 340×1440), `.stat span` che colpiva anche il contatore dentro `b` (0 alto 10px), capitoli con colonna morta. Ora ogni capitolo ha principale + immagine di spalla con didascalia (entrano bagno marmo, libreria noce, bottigliera), parallax dimezzato, tolto il 1990 inventato (→ «100% prodotto nei nostri laboratori»). Verificato con viewport emulati e hook `?peek` temporaneo (rimosso prima del commit) | `a91ecb6` |
| 02:0x | Nicola +claude | [[castiglione-furniture]] | `castiglione-site` | — | **Riscrittura immersiva**: la v1 era «il sito più piatto della storia» (parole di Nicola). Ora scroll-telling scuro con GSAP da CDN (pattern e dosi dalla base dati `ui-ux-pro-max`: max 1 pin, scrub 0.5-1.5, parallax solo sulle immagini): sipario, hero didone Playfair 900 a tutta larghezza, capitoli con parallax, galleria orizzontale pinnata (desktop; su touch scroll-snap), count-up, marquee. Motion additiva: senza CDN o con reduced-motion il sito resta completo. ✅ Misurato a 1280/375: zero overflow, 2 righe di titolo, 1 pin, 23 trigger, 0 errori. ⚠️ Il pannello dipinge solo il primo frame dopo il load: le sezioni interne sono verificate a misure, la resa vera va vista su un browser | `8cb10ea` |
| 01:2x | Nicola +claude | [[castiglione-furniture]] | `castiglione-site` (nuovo, `Desktop/castiglione-site`, solo locale: nessun remote) | — (statico, nessun database) | **Sito vetrina per Castiglione Falegnameria** (Bronte, CT) costruito dai contenuti veri di `@castiglione_furniture`: profilo e 20 post scrapati con lo strumento **Apify** collegato a Claude Code, 31 foto scaricate in locale (gli URL CDN scadono), palette oliva+carta presa dai loro lavori. Un solo `index.html`. ⚠️ L'account si chiama `castiglione_furniture` (inglese), non «forniture»: la ricerca col nome italiano non lo trovava. ✅ Misurato a 1280 e 375 emulati: zero sfondamento, H1 su 2 righe, CTA nel viewport, contrasto nav 9:1 (era invisibile per specificità CSS, corretto). Reveal con fallback: il pannello browser a pane nascosto non consegna gli IntersectionObserver e la pagina restava bianca sotto la piega. Non verificato: resa su browser vero e telefono fisico; contatti solo IG/FB perché il profilo non pubblica email o telefono | `e0260f8` |

## 2026-08-29

| Quando | Chi | Progetto | Repository | Database | Cosa | Commit |
|---|---|---|---|---|---|---|
| 23:5x | Nicola +claude | [[sito-denkicode]] | `pixel-perfect-rebuild` | — (il sito non ha migrazioni; Supabase serve solo al form contatti) | **denkicode.com diviso in due metà**: siti web e gestionali, separate da una fascia e raggiungibili dai due bottoni dell'hero. Nella parte nuova: DenkiShift, i gestionali su misura, e una galleria sua con DenkiShift e OperO (dichiarato come **collaborazione**, è il prodotto di Sebastian). Blog tolto dal listino; vetrina da «600 sbarrato 300 −50%» a **«circa 300»**; degli abbonamenti resta il prezzo del solo **Base, 15-40 €**. DenkiShift a schermo non ha una cifra ma una **quota annuale sui dipendenti**, e nessuna data. ✅ Misurato a 1440 e 375: zero sfondamento orizzontale, bottoni pari, barra su una riga | `443f3ae` |
| 01:1x | Nicola +claude | [[opero]] | `opero-sito` | ✅ **sviluppo: `20260829120000_opero_choice.sql` eseguita** (`db push`), e con lei `20260829100000_super_admin_torres_ritenta.sql` che era rimasta indietro. Edge function `send-push` ridistribuita | **OperO Choice**: il Super Admin sceglie una o piu` persone fra tutti gli account di tutte le aziende, scrive, e alla loro prossima apertura esce un messaggio a schermo pieno col pulsante bloccato 5 secondi. Funzione **nuova**, senza originale in OperO 1 → da quotare. ✅ **Verificato nel browser** con Nicola dentro: blocco di 5 s misurato, esce una volta sola, `seen_at` scritto, `send-push` risponde 200 al Super Admin. Resta scoperta la consegna su un telefono vero | `01495b9` `760dda3` |

## 2026-08-30

| Quando | Chi | Progetto | Repository | Database | Cosa | Commit |
|---|---|---|---|---|---|---|
| 10:3x | Nicola +claude | [[denkishift]] | `smooth-duty` | — (letto, non toccato: diagnosi RLS 3,7ms, piano ottimale) | Indagine lentezza: colpa di Ohio e del freddo, non del DB. Ping programmato + `staleTimes: 30`. **Committato locale, NON pushato**: nel push c'è anche il lotto design | `032091c` `05e34fb` |

## 2026-08-28

| Quando | Chi | Progetto | Repository | Database | Cosa | Commit |
|---|---|---|---|---|---|---|
| 16:3x | Nicola +claude | — | `denki-brain` | — | Creato [[indice]] (70 note) e installato `ponytail` a livello utente | — |
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
