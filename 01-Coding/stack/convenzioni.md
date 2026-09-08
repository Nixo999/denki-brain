---
type: risorsa
updated: 2026-09-08
source: repo
---

# Convenzioni

Estratte dai repo di [[opero]] e [[denkishift]] il 28 agosto 2026. Non sono
preferenze di stile: **ognuna è costata un errore vero**.

⚠️ Le regole specifiche di un progetto stanno nel suo repo. Qui c'è quello che
vale ovunque, o che vale la pena rendere standard.

## Git

**Commit** — il messaggio dice **cosa non tornava e perché la soluzione è
quella**, non l'elenco dei file toccati. In italiano.

✅ `Un'assenza costa le ore da contratto, non i turni che erano scritti`
✅ `L'autista esterno guida e basta: da lì venivano cinque doppioni su dieci`
❌ `fix prospetto.ts`

**Rami** — si lavora su `main` (o `master` in OperO). Nessuna convenzione di
naming per i branch: non se ne usano.

**Il rituale multi-macchina** — Nicola lavora da Windows e da Mac, e Patrick
scrive nel vault:

1. `git pull` **prima di cominciare**, e di nuovo prima di ogni push
2. Nei repo di codice: dopo il pull, verificare lo schema del database
3. **Commit piccoli, push subito.** Il lavoro tenuto in locale mezza giornata è
   il lavoro che poi non entra
4. Prima di toccare un file: `git log -1 <file>` — se l'ha appena cambiato un
   altro, si legge cosa ha fatto
5. **Il push non passa? Non forzare.** `git pull --rebase` e si guarda il
   risultato. Un `--force` cancella il lavoro di qualcun altro senza chiedere

## Lingua

| Cosa | Lingua |
|---|---|
| Interfaccia utente | Italiano |
| Nomi di dominio (cantiere, lavoratore, turno, copertura) | Italiano |
| Commenti e nomi di funzione | **Italiano** in DenkiShift · inglese storico in OperO, italiano dal 7 agosto |
| Tabelle e colonne del database | **Inglese** |
| Messaggi di commit | Italiano |

I commenti spiegano il **perché**, non il cosa. Quasi tutti raccontano il
problema che quella riga evita — stesso criterio dei commit.

## Come si lavora con Claude — regole trasversali

Presenti in tutti e due i repo, quindi valgono per DenkiCode:

1. **«Compila» non è una verifica.** Si apre il browser e si guarda.
2. **Misurare, non guardare a occhio.** Per centrature, colori e spazi si chiede
   al browser il valore calcolato (`getComputedStyle`,
   `getBoundingClientRect`). Un bug di colori è rimasto invisibile per mesi
   perché leggendo il codice sembrava giusto.
3. **Mai avviare il server da Bash.** Si usa il pannello browser.
4. **Password mai.** Non si digitano credenziali in nessun campo: si chiede
   all'utente di entrare lui. Vale anche per gli account di prova.
5. **Dire cosa non si è verificato.** Meglio un buco dichiarato di una
   sicurezza inventata.
6. **Dopo ogni pezzo finito**: voce nel diario del progetto, commit, push.
7. **Prima di cercare nel codice, cercare nei `docs/`.** Sette volte su dieci
   evita la ricerca.

## Regole tecniche che hanno già salvato una giornata

**Date** (da DenkiShift, ma vale ovunque)
- Le date sono **civili**, stringhe `YYYY-MM-DD`, mai istanti con orario. Un
  turno del 3 marzo resta del 3 marzo per chiunque lo guardi
- Le stringhe a lunghezza fissa si confrontano direttamente: ordine alfabetico
  = ordine cronologico
- Se serve un `Date` da una data civile, si costruisce a **mezzogiorno**
- La settimana comincia **di lunedì**, ovunque
- **«Oggi» non si chiede mai a `new Date()`**: in produzione il server gira in
  UTC, e fra mezzanotte e le due italiane è ancora al giorno prima

**Colori**
- Solo **token CSS** (`--surface`, `--accent`, `--danger`...), con versione
  chiara e scura. Mai un colore scritto a mano in un componente: è l'unico modo
  perché tema chiaro e scuro restino coerenti

**Un calcolo, un posto solo**
- Quando la stessa domanda viene fatta da due punti, la risposta sta in un file
  solo. Non è astrazione per bellezza: due risposte diverse producono bug che
  sembrano fantasmi
- I calcoli stanno in **funzioni pure** fuori dai componenti, così si possono
  provare senza browser

**Supabase e RLS**
- Mai una policy che interroga una tabella a sua volta protetta: ricorsione
  infinita, errore `42P17`. Si passa da funzioni `SECURITY DEFINER`
- **RLS è la rete, non il filtro**: le pagine mettono comunque il
  `.eq("company_id", ...)`
- I vincoli fra aziende stanno in **trigger**, non nel codice: così valgono
  anche per importazioni e script

**Errori di lettura**
- Un errore di lettura **non deve mai diventare una lista vuota**. Un tabellone
  senza turni è indistinguibile da un tabellone cancellato — solo che nel primo
  caso i turni ci sono tutti e a non funzionare è la domanda

**Segreti**
- `.env.local` e simili fuori da git, sempre
- Una chiave di servizio **non deve mai avere il prefisso `NEXT_PUBLIC_`**:
  quel prefisso la manda nel browser, e quella chiave scavalca ogni regola

## La firma nel piè di pagina — su ogni progetto

Regola dell'8 settembre 2026, il perché sta in
[[2026-09-08-firma-powered-by-denkicode]]. Ultima riga del footer, sotto il
copyright del cliente:

```html
<a class="firma" href="https://denkicode.com" target="_blank" rel="noopener">
  <img src="/logo-denkicode.svg" alt="" width="18" height="18">
  <span>Powered by <strong>DenkiCode</strong></span>
</a>
```

- **Il file del simbolo** si copia nel progetto da
  `03-Storage/brand/logo/logo-simbolo.svg` (fondi chiari) o
  `logo-simbolo-scuro.svg` (fondi scuri), 4,5 KB l'uno. ⚠️ **`logo-lockup.svg`
  no**: 151 KB e 346 tracciati, perché contiene tutte e quattro le versioni e il
  `viewBox` ristretto le nasconde soltanto.
- **`alt=""`**: il nome è già nel testo accanto, altrimenti uno screen reader
  legge «DenkiCode» due volte.
- **`width`/`height` sull'`<img>`**, e nel CSS `height` fissa con `width:auto` —
  il simbolo è quadrato e l'attributo `height` vince su `aspect-ratio`
  ([[trappole]]).
- **Colore secondario del tema, contrasto ≥ 4.5:1.** Non si nasconde e non si
  sbiadisce: una firma illeggibile non porta lead.
- **Su una bozza entra subito**, prima di mandare il link al lead.
- Su [[opero]] non si mette di iniziativa: è il prodotto che il cliente rivende.

## Mettere in piedi una macchina nuova

Procedura completa — strumenti, GitHub, `.env`, Supabase, JDK, Obsidian — in
[[setup-macchina-nuova]].

⚠️ **«Push su Supabase» esiste solo su [[opero]]** (`npx supabase db push`). Su
[[denkishift]] le migrazioni si incollano a mano nel SQL Editor, in ordine
numerico, e l'allineamento si controlla con `verifica-schema.mjs`.

## Convenzioni del vault

- File in `kebab-case`. Note datate `YYYY-MM-DD-titolo.md`
- Frontmatter obbligatorio, schemi in [[CLAUDE|CLAUDE.md]]
- `source:` sempre valorizzato — `denkicode`, `claude` o `repo`
- Wikilink generosi. Un link a una nota che non esiste è un promemoria
- `updated` si tocca a ogni modifica sostanziale

## Da decidere

- [ ] Uniformare lo stack dei siti vetrina → [[2026-08-28-stack-non-uniforme]]
- [ ] Struttura standard di cartelle per un progetto nuovo — `TODO`
- [ ] Policy sui test: DenkiShift ne ha 132, OperO zero. Quale è lo standard?
- [ ] Compilare la lista "cosa non usiamo mai" in [[stack]]

## Collegamenti

[[stack]] · [[opero]] · [[denkishift]] · [[stile-comunicazione]]
