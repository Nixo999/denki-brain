---
type: area
updated: 2026-08-28
source: claude
---

# Modifiche al database — chi, dove, con quale comando

Il *perché* di questa possibilità sta in
[[2026-08-28-supabase-denkishift-sul-mac]]. Qui sta il **come**, perché una
decisione non la si rilegge ogni mattina e un comando sì.

⚠️ **Nessuna chiave in questa nota, e mai.** Il vault è su GitHub. Dove stanno
i valori e come si leggono: [[credenziali]].

## I due prodotti si toccano in due modi diversi

Non è un dettaglio: il comando giusto su un prodotto è il comando sbagliato
sull'altro.

| | [[opero]] | [[denkishift]] |
|---|---|---|
| Meccanismo | migrazioni Supabase CLI | script `node` nel repo |
| Cartella | `supabase/migrations/` | `supabase/NN-nome.sql`, numerati |
| Comando | `npx supabase db push` | `node --env-file=.env.local --env-file=.env.db scripts/esegui-sql.mjs supabase/NN-nome.sql` |
| Controllo prima | — | `scripts/verifica-schema.mjs`, stessi `--env-file` |
| Collegamento | `supabase/.temp/`, **non in git**: in un worktree nuovo si copia dalla cartella principale | nessuno: gli `.env` bastano |

Su DenkiShift **`supabase db push` non esiste**: cercare quel comando è
mezz'ora persa, ed è già successo.

## Su quale progetto Supabase si scrive

| Prodotto | Sviluppo | Produzione |
|---|---|---|
| [[opero]] | `oyoltwisdwujitsryzax` — è anche il database del sito di prova | `avsuihlxecpbmddhnyvo`, del cliente [[sebastian-torres]] — **mai toccare** |
| [[denkishift]] | `rytuurzafjxzlrpgforj` | un progetto diverso, dietro `denkishift.it` — **fuori**, si decide con Nicola |

**La produzione non si tocca di striscio mentre si prova qualcosa.** Su OperO
dentro ci sono i dipendenti veri delle aziende che pagano [[sebastian-torres]].

## Dal Mac di Patrick

Si può, **solo su DenkiShift in sviluppo**. Perché funzioni servono tre
condizioni, e non sono automatiche:

1. I tre valori nei file `.env.local` e `.env.db`, letti da lui dal pannello
   Supabase — vedi [[credenziali]]. Finché mancano, il comando si ferma subito
2. La sessione di Claude deve **arrivare al repo**: se è aperta sul vault,
   `~/Desktop/smoothduty` non è raggiungibile e va aggiunto come cartella di
   lavoro
3. ~~`pg` non dichiarato~~ — **risolto il 28 agosto 2026**: `pg` è in
   `devDependencies` di `smooth-duty`, quindi `npm install` basta e
   l'aggiramento con `--no-save` non serve più. Se un comando risponde ancora
   `Cannot find package 'pg'`, vuol dire che su quella macchina `npm install`
   non è mai stato lanciato

**Per Patrick, i passi in ordine e senza gergo: [[patrick-modifica-denkishift]].**

## Quello che vale su tutte le macchine

- **Le migrazioni si scrivono, non si improvvisano nel SQL Editor.** Un
  cambiamento applicato a mano e non scritto in un file è un cambiamento che
  la prossima macchina non avrà
- **Su OperO le policy RLS non interrogano mai un'altra tabella protetta**: si
  usano funzioni `SECURITY DEFINER`, altrimenti Postgres va in ricorsione
  infinita (errore 42P17)
- Dopo una modifica allo schema di OperO i tipi si rigenerano:
  `npx supabase gen types typescript --linked > src/lib/database.types.ts`

> [!note] Analisi di Claude — 2026-08-28
> Non ho eseguito nessuno di questi comandi dal Mac: li ho ricostruiti dalla
> decisione del 28 agosto e dai `CLAUDE.md` dei due repo. Il primo che li lancia
> davvero corregga qui quello che non torna.

## Collegamenti

[[credenziali]] · [[setup-macchina-nuova]] ·
[[2026-08-28-supabase-denkishift-sul-mac]] · [[opero]] · [[denkishift]]
