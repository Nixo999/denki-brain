---
riga: Il prompt del giro del mattino - la lista del giorno parte da sola alle 8 dal Mac di Nicola, alle 8:30 da quello di Patrick se la conferma non c'e'.
type: risorsa
updated: 2026-10-17
source: claude
tags: [banco, liste, automazione]
---

# Il giro del mattino

Nicola, 11/10/2026 (frase intera in [[metodo-liste]]): ogni mattina la lista del
giorno parte da sola. **Alle 8:00 dal Mac di Nicola**, che prima scrive nel
vault che parte; **alle 8:30 dal Mac di Patrick**, che parte solo se quella
conferma non c'è. La conferma è una riga in `02-Sales/liste/giri-mattina.csv`,
scritta da `giro-mattina.py`.

Su ogni Mac c'è un task pianificato dell'app Claude, `banco-mattina`, il cui
prompt dice solo di leggere questa nota. Quello che fa il giro si cambia qui,
non nei task.

| Mac | Ora | Ruolo |
|---|---|---|
| di Nicola | `0 8 * * *` | `primo` |
| di Patrick | `30 8 * * *` | `riserva` |

Il task di Patrick si crea **dal suo Mac**, chiedendolo in una chat dell'app:
«crea il task pianificato `banco-mattina` alle 8:30, ruolo riserva, col prompt
di `02-Sales/strumenti/giro-mattina.md`». Scriverlo dentro `/patrick` o `/banco`
perché lo faccia da solo è stato fermato dal classificatore dei permessi
(11/10/2026): un comando che crea task pianificati senza chiedere non passa.
Subito dopo, **«Esegui ora» una volta con qualcuno davanti**: i permessi
approvati durante un giro restano sul task e valgono per i giri dopo.
⚠️ Corretto il 13/10/2026: restano, ma legati al testo esatto del comando, e il
modello lo cambia a ogni giro. Il dettaglio sta in [[trappole]], sezione «Liste e
banco DM».
`giro-mattina.py --installato` dice se su una macchina il task c'è.

## Il prompt del task

> Giro del mattino del banco DM, ruolo `<primo|riserva>`. Trova il vault (il
> primo fra `~/lavoro/denki-brain` e `~/Desktop/denki-brain` che contiene
> `CLAUDE.md`), leggi `02-Sales/strumenti/giro-mattina.md` e seguilo.

## Cosa fa chi lo esegue

Nessuno è davanti allo schermo: **non si fanno domande e non si aspettano
risposte.**

1. Nel vault: `python3 02-Sales/strumenti/giro-mattina.py --ruolo <ruolo>`. Se
   esce con un codice diverso da 0 ci si ferma, e la risposta è la riga che ha
   stampato.
2. Se esce 0 si costruiscono le liste del giorno: si legge
   `.claude/commands/banco.md` e si segue dal passo 1 al passo 9 come se Patrick
   avesse scritto `/banco`. Il passo 8 si salta: il banco è online su
   <https://banco-denkicode.netlify.app> e la lista ci arriva da sola col push.
   Un blocco non ferma la lista (passo 0): si cambia fonte e lo si dice in una
   riga.
3. A giro finito, anche con liste corte:
   `python3 02-Sales/strumenti/giro-mattina.py --fine`.
4. La risposta ha il formato del passo 10 di `banco.md`.

## Limiti noti

- **La posta (passo 6) dal Mac di Nicola si legge da Brave**, dove l'account
  `denkicode` è collegato, con gli strumenti di Claude in Chrome; il browser
  dell'app non è collegato. L'API `direct_v2/inbox` risponde 404 dal 17/10: si
  scorre la lista dell'inbox nel DOM e si aprono le chat una per una.

- Se il giro del Mac di Nicola parte e si pianta a metà, quello di Patrick non
  lo rifà: la conferma c'è. Lo dice la riga `partito` senza `finito` in
  `giri-mattina.csv`.
- Il task gira solo con l'app Claude aperta e il Mac acceso. Se all'ora giusta
  è chiusa, parte alla riapertura e trova la conferma dell'altro, se c'è.
- **E il Mac deve restare sveglio per tutto il giro, circa due ore.** Il
  13/10/2026 il giro delle 11:04 è passato dall'hook senza una richiesta di
  permesso, ma il Mac si è addormentato alle 12:46; al risveglio delle 13:48 la
  rete non c'era e i sette operatori sono morti insieme («Can't reach the API
  server»). Li ha ripresi Nicola alle 15:31 con un «Riprova» nella sessione.
  L'opzione dell'app «Keep computer awake while Claude works» impedisce il sonno
  da inattività mentre una sessione lavora; il coperchio chiuso addormenta
  comunque.
- Un giro senza i permessi già approvati si ferma alla prima richiesta: per
  questo il primo «Esegui ora» si fa con qualcuno davanti, su ogni Mac.
- **Verificato il 13/10/2026**: la sessione del task parte in modalità permessi
  `default`, non `auto`, e il task non ha un campo per cambiarla. Il 12/10 e il
  13/10 il giro si è fermato alle 8 sul primo comando, `giro-mattina.py --ruolo
  primo`, e il 12/10 è ripartito alle 17:43 solo perché Nicola ha messo la
  sessione in `auto` a mano. Finché la modalità non è risolta, il giro delle 8
  non è autonomo.
- **La correzione (13/10/2026)**: l'hook `permessi-giro.py` (PreToolUse, a
  livello di account come gli altri tre) riconosce una sessione avviata dal task
  dal tag `<scheduled-task>` nel suo primo messaggio e approva da solo i suoi
  strumenti dentro il vault; fuori da un task non decide niente. Lo mette in
  opera Nicola, perché il classificatore ferma un modello che si scrive da solo
  un hook sui permessi. Finché non è installato, vale il punto sopra.

[[2026-10-11-banco-online]] · [[metodo-liste]]
