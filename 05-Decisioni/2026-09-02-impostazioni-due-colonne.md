---
type: decisione
data: 2026-09-02
progetto: denkishift
source: claude
---

# Le Impostazioni parlano a chi decide, e su un monitor stanno su due colonne

Chiesta da Nicola il 2 settembre 2026 con un brief esplicito: «i testi sono
infantilizzati, poco professionali e strutturati male, e da desktop
l'interfaccia è illeggibile perché disposta su una singola colonna infinita».
Applicata e pubblicata lo stesso giorno, commit `14df68c` su `main`.

**Sostituisce la scelta del 30 agosto 2026** sul registro dei testi. Quella non
si riscrive: sta ancora nei commenti del componente e nel diario del repo, ed
era motivata — descrizioni «per chi gestisce un negozio», una riga per
controllo. La riga per controllo resta. La confidenza no.

## Cosa si decide

**1. Da 1024 px la pagina sta su due colonne.** Il guscio dell'app dà fino a
`max-w-[100rem]` e le Impostazioni ne usavano `max-w-2xl`: su un monitor erano
672 px di nastro verticale, nove schede in fila e novecento pixel vuoti a
destra, con il salvataggio automatico annunciato a tre schermate dalla leva
appena toccata.

Le misure, perché non si rimettano in discussione a occhio:

| Scelta | Perché quella |
|---|---|
| `lg:` (1024), non `md:` | A 768 le colonne stanno a ~350 px e la descrizione va a quattro righe per far passare la levetta da 44 |
| `lg:max-w-6xl`, non oltre | Colonne da ~552 px → descrizioni sui 72 caratteri. A `max-w-[100rem]` si superano i 90 e si legge peggio di prima |
| Due wrapper di colonna, non figli diretti in `grid-cols-2` | L'ordine del DOM resta 1→2→3→4, che è l'ordine di lettura sul telefono; il Tab scorre per colonne; un `<details>` aperto allunga solo la sua colonna |
| `items-start` | Senza, le due colonne prendono la stessa altezza e il richiudibile aperto lascia un vuoto nell'altra |
| Mai `columns-2`, mai masonry | Il multi-column CSS spezza una scheda fra due colonne; il masonry cambierebbe l'ordine a seconda della finestra |

**Sotto i 1024 px non cambia una riga.** L'app da telefono è il caso d'uso
primario e questa modifica non le costa niente.

**2. Quattro sezioni per ambito, al posto di sei «per gesto».** Moduli attivi ·
Visibilità e richieste del personale · Pubblicazione e modifiche · Nuovi turni
e personale a chiamata. Sei intestazioni che cominciavano tutte per «Quando»
erano un indice inutile su una colonna, e su due sarebbero state sei volte la
stessa parola nella stessa schermata. **Il gesto non è sparito**: è sceso di un
livello e sta nella riga «Quando scatta», che è dove uno lo cerca davvero.

**3. Il registro dei testi è tecnico, non confidenziale.** Chi apre questa
pagina è un titolare o un responsabile turni, e sta **decidendo**, non
imparando. Cinque regole, per chi tocca questi testi dopo:

- l'etichetta è un sostantivo, massimo quattro parole: «Accettazione dei turni
  in straordinario», non «Straordinari da accettare»;
- la descrizione sta in una o due righe e dice **cosa cambia in azienda**, non
  come funziona il software;
- la rassicurazione è un fatto — «il turno resta valido» — non una pacca sulla
  spalla («se non risponde nessuno, va bene»);
- il «tu» solo dove l'azione è dell'utente. «Assegni un turno» sì; «chi ti può
  dire di no» era un narratore, e in una pagina di configurazione non serve;
- ogni controllo dichiara cosa significa acceso **e** cosa significa spento.

Fuori anche `non in uso` → **Disattivato**, `Se dice no` → **In caso di
rifiuto**, `Impostazioni avanzate` → **Opzioni avanzate**, e un'etichetta nuova
**Esito** per i tre regimi a chiamata, dove l'app blocca il salvataggio invece
di far rifiutare: lì «se dice no» descriveva una cosa che non succede.

**Resta valido il divieto del 29 agosto**: «Conferma» non torna come verbo di
sistema. Si usano *accetta* e *rifiuta*. Le colonne `conferma_*` del database
restano come sono — rinominarle costa una migrazione e non le legge nessuno.

**4. Un salvataggio fallito resta scritto.** Prima era un toast che passava e
una levetta che tornava indietro da sola; su due colonne quella levetta può
stare nella metà di schermo che non si sta guardando. Lo stato `errore` tiene
«Modifica non salvata» finché un salvataggio nuovo non riesce.

## Cosa non si decide qui

- **Il turno rifiutato: eliminato o scoperto?** La domanda è aperta dal
  29 agosto e resta aperta. I due «In caso di rifiuto» della quarta sezione
  dicono *eliminato, giorno libero*, che è il comportamento di oggi. Se cambia,
  cambiano quelle due righe e nient'altro.
- **«Messaggi» o «da leggere».** La decisione del 29 agosto prevede il
  rinomino, ma a schermo la parola è ancora «messaggi» in Turni e Supervisione.
  I testi nuovi usano quella: quando il rinomino arriva è una sostituzione
  secca in cinque punti.
- **Lo stesso trattamento a due colonne su Squadra.** Il modello è riusabile,
  ma nessuno l'ha chiesto.

## Il buco dichiarato

**Non verificato su schermo.** `npm run prove` e `npm run build` passano, le
utility Tailwind sono nel CSS costruito, ma la pagina non è stata guardata da
un browser: qui non si avvia niente in locale e si verifica dopo aver
pubblicato. Su `main` la vede la squadra del cliente appena Netlify finisce.

## Trovato di striscio

- Il sottotitolo diceva «Tre si possono spegnere» sopra a **quattro** moduli.
- `docs/03-pagine.md` contava «undici impostazioni» quando in
  `lib/impostazioni.ts` sono **dodici**: `pagina_disponibilita` è arrivata dopo
  quel testo. Corretti tutti e due nello stesso commit.

## Collegamenti

[[denkishift]] · [[registro-interventi]] ·
[[2026-08-29-architettura-interfaccia-denkishift]] ·
[[2026-08-28-stack-non-uniforme]] · [[denkishift-interfaccia]]
