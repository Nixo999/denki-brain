---
type: decisione
data: 2026-08-29
progetto: denkishift
source: claude
---

# Il menu di DenkiShift è l'elenco delle domande, non delle pagine

> [!warning] Decisa a metà
> La parte sui **nomi delle pagine è decisa e chiusa**: restano quelli di oggi,
> detto in sessione il 29 agosto 2026. Il resto — la voce nuova `/oggi`, le tre
> voci che escono dalla barra — resta una proposta di Claude e aspetta il sì di
> chi scrive il codice. `layout.tsx` non si tocca prima.

Il ragionamento completo sta in [[denkishift-interfaccia]]. Qui c'è solo la
parte che va firmata prima di scrivere codice, perché l'etichetta di menu è
**una stringa sola per indirizzo** e tre proposte diverse davano tre valori agli
stessi due indirizzi.

## Cosa si decide

**1. I nomi delle pagine restano quelli.** Erano stati proposti «Chi c'è» per
la Supervisione, «Assenze» per i Permessi, «Ore» per il Prospetto e un nome che
cambia col regime per la Disponibilità, sull'argomento che sono i nomi che
userebbe un titolare di negozio. **Scartato.** Un nome di pagina lo impara chi
la apre ogni giorno, e cambiarlo è un costo per loro prima che un guadagno per
chi la guarda dieci minuti in demo.

| Indirizzo | Capo | Dipendente |
|---|---|---|
| `/oggi` **(nuova)** | Oggi | — |
| `/turni` | Turni | I miei turni |
| `/supervisione` | Supervisione | Supervisione |
| `/permessi` | Permessi | Permessi |
| `/prospetto` | Prospetto | — |
| `/disponibilita` | — | Disponibilità |

Restano fuori dalla decisione, perché non sono nomi di pagina: le parole
**dentro** le schermate — «da assegnare» e «turno scoperto» che diventano una
parola sola, «Conferma» che sparisce come verbo di sistema, «bozza» che diventa
«la vedi solo tu». Quelle valgono, e stanno in [[denkishift-interfaccia]].

⚠️ **Un effetto collaterale, dichiarato**: la misura che reggeva la barra a
cinque voci era tarata sulle etichette corte. «Supervisione» e «Prospetto» sono
più lunghe e la barra a 375px non è mai stata guardata. Se non ci stanno, si
allarga la barra o si passa a quella in basso — non si accorciano i nomi.

**2. Squadra, Impostazioni e Aziende escono dalla barra** e vanno nella tendina
dell'iniziale. Si aprono una volta a settimana o una volta al mese; «Aziende»
in particolare cambia guscio, titolo e menu senza preavviso, e sta nella barra
dell'unico account con cui si fa la demo.

**3. Le pagine spegnibili restano spegnibili, e lo restano tutte.** Chi tocca
il menu tiene insieme i due controlli — quello che nasconde la voce e quello
dentro la pagina — perché l'indirizzo se lo ricorda il browser. Il rimbalzo di
una pagina spenta smette di essere muto e **cambia destinazione secondo il
ruolo**: la home nuova non esiste per il dipendente.

**4. Una parola per cosa, un verbo per gesto — dentro le schermate.** «Pubblica» significa una cosa
sola: farlo vedere ai dipendenti. «Conferma» sparisce come verbo di sistema.
«Da assegnare» e «turno scoperto» diventano **scoperto**. «Posta» e «Messaggi»
diventano **da decidere** e **da leggere**. Il vocabolario completo sta in
[[denkishift-interfaccia]] e va scritto nel repo, in `docs/`, o fra tre mesi si
sfalda di nuovo.

## Cosa non si decide qui

- **Se le tre voci escono davvero dalla barra**, e se `/oggi` si fa. Serve il sì
  di chi scrive il codice.
- **Il nome del prodotto a schermo.** Oggi l'app dice «Turni» ovunque l'utente
  guardi, il materiale commerciale dice DenkiShift. Non costa ore di sviluppo,
  costa una risposta di Patrick, e blocca due pezzi del lavoro.
- **Se il turno rifiutato resta scoperto o sparisce.** Oggi viene cancellato. Il
  testo delle Impostazioni non si può scrivere finché non è deciso quale dei due
  è il comportamento giusto: è una domanda per Nicola, non per chi scrive il
  copy.
- **`/admin`**, che resta fuori perimetro finché qualcuno non dice il contrario.

## Perché adesso

Perché il lavoro sulla riprogettazione comincia da `layout.tsx`, e con tre
etichette in ballo per lo stesso indirizzo quel file non si poteva scrivere.
Adesso si può: i nomi sono quelli di oggi e la discussione è chiusa.

## Collegamenti

[[denkishift-interfaccia]] · [[denkishift]] · [[obiezione-non-sapranno-usarlo]] ·
[[2026-08-28-stack-non-uniforme]]
