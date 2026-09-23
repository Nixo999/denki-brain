---
riga: Fiftynine - le modifiche della pagina di modifica vanno in Netlify Blobs, senza chiavi, e una edge function le rimette nelle pagine; parola iniziale admin, si cambia dalla pagina.
type: decisione
data: 2026-09-23
progetto: sito-fiftynine
updated: 2026-09-23
source: claude
stato: presa
tags: [decisione, fiftynine, netlify, gestionale, blobs]
---

# Le modifiche del Fiftynine vanno nell'archivio di Netlify

Supera, per il Fiftynine, [[2026-09-23-fiftynine-pubblica-da-solo]] (commit su
GitHub), presa la mattina stessa. Nicola, davanti alle impostazioni da mettere
su Netlify: «non voglio passare per natlify» e «fai in modo che semplicemente
scriendo admin si possa accedere alla pagina».

## Deciso

- **Archivio: Netlify Blobs.** Netlify lo dà alle sue funzioni senza chiavi e
  senza impostazioni: è l'unica strada con zero passaggi per Nicola. Il commit
  su GitHub chiedeva una chiave che solo lui può creare.
- **Si salvano solo i pezzi marcati cambiati**, la descrizione e le foto nuove.
  Una edge function su `/`, `/index.html`, `/menu`, `/menu.html` li rimette nella
  pagina a ogni visita e serve le foto su `/foto/*`. Online subito, senza deploy;
  il sito resta HTML già completo. Se l'archivio non risponde, si serve la
  pagina del repo com'è.
- **Parola d'ordine iniziale `admin`**, nel codice, per scelta di Nicola; si
  cambia dalla pagina stessa, e la nuova si salva come impronta scrypt.

## Il prezzo, detto chiaro

- **Il repo non vede le modifiche del proprietario.** Un pezzo che lui ha
  toccato resta suo sul sito anche se Nicola lo cambia nel repo.
- **Due fonti invece di una**: la struttura nel repo, il contenuto toccato
  nell'archivio. Per V-BAG Blobs era stato scartato per questo
  ([[2026-09-16-vbag-gestionale-login]]): per V-BAG la decisione resta quella.
- **`admin` è nel repo pubblico** finché non la si cambia dalla pagina.

## Come ci si è arrivati

Tre blocchi del sistema di permessi di Claude Code in modalità automatica (la
regola sulle credenziali nel `CLAUDE.md`, `admin` nel codice, questa strada),
fermati e riferiti a Nicola invece che aggirati; Nicola ha tolto il blocco e ha
deciso. Vedi [[trappole]].
