---
description: Scansiona i progetti, controlla i commit dei repo, aggiorna gli status e segnala i fermi da 14+ giorni
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
---

> **Base**: `03-Storage/azienda/protocollo-jarvis.md` (di cosa ci si occupa) e
> `03-Storage/azienda/registro-jarvis.md` (come si parla) — si leggono prima di
> rispondere, in questa come in ogni altra modalità. Niente presentazioni,
> niente «adesso procedo a», niente proposte su cosa fare dopo. Riprendi come se
> la conversazione non si fosse mai interrotta.

Fai il giro di controllo dei progetti DenkiCode.

## 1. Leggere lo stato dichiarato

Leggi ogni file in `01-Coding/progetti/` e raccogli dal frontmatter: `status`,
`updated`, `deadline`, `client`, `valore`, `incassato`.

## 2. Confrontarlo con la realtà dei repo

Per ogni progetto che ha un repository, controlla l'attività vera. I repo noti:

| Progetto | Repo |
|---|---|
| opero | `github.com/Nixo999/opero-sito` |
| denkishift | `github.com/Nixo999/smooth-duty` |

Se il repo è già clonato da qualche parte sul disco, usalo. Altrimenti leggi i
commit recenti via API senza clonare:

```bash
curl -s "https://api.github.com/repos/Nixo999/<repo>/commits?per_page=10" \
  | grep -E '"(message|date)"'
```

Per ogni progetto stabilisci:

- **data dell'ultimo commit** vs `updated` nella nota
- se ci sono commit **dopo** l'ultimo aggiornamento della nota, la nota è
  indietro: leggi i messaggi e proponi cosa aggiungere
- se il repo ha un `docs/handoff.md` o `docs/07-diario.md`, controlla se dice
  cose che la nota del vault non sa

## 3. Segnalare i fermi

Elenca ogni progetto con `status: attivo` il cui `updated` è più vecchio di
**14 giorni**. Per ciascuno chiedi all'utente una cosa sola: è finito, è in
pausa, o è stato dimenticato?

Se risponde "in pausa", metti `status: in-pausa`. Se "finito", spostalo in
`04-Archive/` e togli la riga dall'indice in `CLAUDE.md`.

## 4. Controllare le scadenze e i soldi

- Progetti con `deadline` passata o entro 14 giorni → segnalali
- Progetti con `valore` > `incassato` → mostra il credito aperto e da quanto
  tempo è fermo
- Somma i crediti aperti e confrontala col tetto in
  `03-Storage/azienda/vincoli-fiscali.md`

## 5. Aggiornare

Applica le modifiche concordate: `updated`, `status`, sezioni **Aperto**, e
l'indice progetti in `CLAUDE.md`.

**Non inventare stati.** Se non riesci a stabilire come sta un progetto, scrivi
`TODO` e dillo.

## 6. Riportare

Una tabella sola:

| Progetto | Stato | Ultimo commit | Nota aggiornata | Da incassare | Azione |
|---|---|---|---|---|---|

Poi le tre cose più urgenti, in ordine.
