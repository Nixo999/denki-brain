---
type: area
updated: 2026-08-28
source: claude
---

# Credenziali — dove stanno e come si spostano

⚠️ **In questa nota non c'è nessuna chiave, e non ce ne devono finire mai.**
Il vault è un repository git che sta su GitHub: quello che si scrive qui dentro
è scritto per sempre, anche se lo si cancella al commit dopo.

È la stessa regola che governa il codice, e viene da `docs/05-convenzioni.md`
di [[denkishift]]: *«una password nel codice finisce su GitHub e da lì non si
toglie più»*.

## La regola, in tre righe

1. **Le credenziali non stanno in nessun repository.** Né nel vault, né nei repo
   di codice. Stanno in file `.env` che ogni macchina si costruisce da sé
2. **Non si mandano in chat, su WhatsApp, per email.** Una chiave incollata in
   una conversazione resta nella cronologia di due dispositivi e in un backup
   cloud, per sempre
3. **Ognuno se le legge da sé dal pannello Supabase.** È la via più corta e
   l'unica che non lascia copie in giro

## Dove vivono, su ogni macchina

**DenkiShift** (`smooth-duty`) — due file, entrambi fuori da git:

| File | Contiene | Da dove si prende |
|---|---|---|
| `.env.local` | `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY` | *Project Settings › API* |
| `.env.db` | `SUPABASE_DB_PASSWORD` | *Project Settings › Database › Database password* |

I modelli sono già nel repo e si copiano:
```bash
cp .env.local.example .env.local
cp .env.db.example .env.db
```

⚠️ `SUPABASE_SERVICE_ROLE_KEY` **non prende mai il prefisso `NEXT_PUBLIC_`**:
quel prefisso la manda dritta nel browser, e quella chiave scavalca ogni regola
di sicurezza.

**OperO** (`opero-sito`) — `.env.local` con `VITE_SUPABASE_URL` e
`VITE_SUPABASE_ANON_KEY`, puntati al progetto di **sviluppo**. Il
`.env.production` che sta in git contiene solo URL e chiave pubblica, ed è
committato apposta con il commento che spiega perché.

## Chi ne ha bisogno davvero

| Macchina | Serve? |
|---|---|
| PC Windows di Nicola | ✅ Sì — è la macchina di sviluppo |
| Mac, quando ci lavora Nicola | ✅ Sì |
| Mac, per l'uso di Patrick | ⚠️ **Una alla volta.** Dal 28 agosto 2026 quel Mac applica le modifiche allo schema di [[denkishift]] **in sviluppo**: gli servono le chiavi di quel progetto, non le altre → [[2026-08-28-supabase-denkishift-sul-mac]] |

> [!note] Analisi di Claude — 2026-08-28
> «Da tutti i dispositivi si deve poter accedere al database» è un obiettivo
> ragionevole, ma **la strada non è distribuire la chiave: è che ogni macchina
> che ne ha bisogno se la legga dal pannello.** Sono due minuti, e non lascia
> copie.
>
> La differenza pratica: se una chiave gira per WhatsApp fra tre persone, il
> giorno in cui va rigenerata bisogna ricordarsi di tutti i posti in cui è
> finita — e non ci si riesce mai. Se ognuno se l'è letta dal pannello, si
> rigenera e basta: alla prossima apertura ognuno rilegge quella nuova.

## Le due chiavi non sono la stessa cosa

| Chiave | Cos'è | Dove può stare |
|---|---|---|
| `anon` / `sb_publishable_…` | Pubblica per progetto. Finisce comunque nel bundle che il browser scarica | Nel browser, in un file `.env`, anche in git se serve al build |
| `service_role` / `sb_secret_…` | **Scavalca ogni policy RLS.** Legge e scrive i dati di tutte le aziende, causali di malattia comprese | Solo in `.env.local`, solo su una macchina di sviluppo, mai in git, mai in una chat |

Ciò che protegge i dati non è la segretezza della prima: sono le **policy RLS**,
verificate il 7 agosto 2026 su OperO — con la sola chiave pubblica e senza
login, 14 tabelle rispondono vuoto.

## Se una chiave esce

Non è un dramma, ma va fatto subito e in quest'ordine:

1. **Rigenerare la chiave** — *Project Settings › API Keys › Revoke* o *Rotate*
2. **Cambiare la password del database** se è quella — *Settings › Database ›
   Reset database password*
3. **Aggiornare i `.env`** su ogni macchina che li ha
4. **Controllare che non sia mai entrata in git**:
   ```bash
   git grep -I -l "sb_secret_" $(git rev-list --all)
   ```
   Se risponde qualcosa, la chiave è nella storia dei commit e **rigenerarla è
   l'unica soluzione**: cancellarla dal file non la toglie dalla storia
5. **Non riusare la stessa password altrove**, e se lo si è fatto, cambiarla lì
   per prima

## Registro

| Data | Cosa è successo | Stato |
|---|---|---|
| 2026-08-28 | Chiave `sb_secret_` e password del database di [[denkishift]] incollate in una conversazione. Non sono state scritte in nessun file né in nessun commit | ⚠️ **Da rigenerare** — vedi i punti 1 e 2 qui sopra |

## Collegamenti

[[setup-macchina-nuova]] · [[convenzioni]] · [[denkishift]] · [[opero]] ·
[[team-e-vincoli]]
