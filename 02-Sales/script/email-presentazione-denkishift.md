---
type: area
updated: 2026-09-01
source: claude
prodotto: denkishift
stato: da-provare
---

# Email — presentazione DenkiShift

Il testo che accompagna [[presentazione-denkishift|la presentazione PDF]] quando
un contatto chiede materiale via mail invece della demo. Nato il 1 settembre
2026 per **[[ms-service]]**, impresa di pulizie di Seveso trovata da Giulia.

> [!note] Analisi di Claude — 2026-09-01
> Testo generato, mai ancora mandato a nessuno. Va riletto da Patrick prima di
> partire: mancano il suo numero, il nome del referente e la data della
> telefonata di Giulia.

⚠️ **La mail non sostituisce la demo, la prenota.** Lo [[script-denkishift|script]]
dice che «mi mandi una mail» si gestisce riportando all'appuntamento: qui il
contatto la mail l'ha chiesta davvero, quindi si manda — ma il testo chiude
comunque con la richiesta dei dieci minuti, e l'allegato non contiene nessuna
data di attivazione.

## Oggetto

```
DenkiShift per M.S. Service — la presentazione, come d'accordo
```

## Corpo

```
Buongiorno [Nome],

sono Patrick Sappa di DenkiCode, la software house di Seveso. Le scrivo
come d'accordo con la mia collega Giulia, che l'ha sentita [giorno].

In allegato trova la presentazione di DenkiShift, il programma con cui
gestiamo i turni del personale. Sono quattro pagine, e le ho scritte
pensando a un'impresa di pulizie e non in generale: dentro trova cosa fa,
quanto costa e — soprattutto — cosa non fa ancora, che di solito nessuno
le scrive.

Le anticipo le due cose che contano:

- si costruisce la settimana una volta sola e ognuno vede la sua sul
  telefono; quando qualcuno salta all'ultimo, il programma le dice subito
  chi è libero e chi ha già fatto troppe ore;
- si paga una quota annuale con ricevuta, una volta l'anno: su dieci
  persone sono 240 € all'anno, tutto compreso.

Una cosa però gliela dico chiaramente, perché è quella che fa la
differenza: da un documento si capisce poco. La configurazione con i
vostri cantieri e le vostre persone gliela facciamo noi, e non la paga.
Se dopo averla vista non la convince, ci salutiamo e non ha speso un euro.

Sono dieci minuti, in videochiamata o passo io da voi.
Le va meglio [giorno] mattina o [giorno] pomeriggio?

A presto,

Patrick Sappa
DenkiCode — Seveso (MB)
[telefono]
denkicode.com
```

## Come si riusa su un altro contatto

L'allegato è generato da `presentazione-denkishift.html`: si cambia il blocco
`.forwhom` (nome azienda, settore, comune) e si riesporta con

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless \
  --no-pdf-header-footer --print-to-pdf=presentazione-denkishift-CLIENTE.pdf \
  presentazione-denkishift.html
```

La **sezione 01** è scritta su un'impresa di pulizie (cantieri diversi ogni
giorno, orari decisi dal committente). Su un altro segmento — RSA, vigilanza,
logistica — quella sezione si riscrive: è la parte che dimostra ascolto, ed è
l'unica che non si può riciclare.

## I quattro vincoli rispettati, per controllo

| Vincolo | Dove |
|---|---|
| **Nessuna data di attivazione** | Sezione 04 lo dichiara apertamente: la data la dà Patrick dopo aver visto l'organizzazione |
| **Prezzo come totale annuo**, mai «2 € al mese a persona» | Sezione 05, tabella per fasce |
| **Lessico**: quota annuale, ricevuta, collaborazione occasionale | Sezione 05 e piè di pagina |
| **Cosa NON è compreso** non si salta | Sezione 03, comprese **le notifiche che oggi non ci sono** |

I framework (regola 12 di `CLAUDE.md`): sezione 01 è **SPIN** — Problema e
Implicazione messi per iscritto, col costo del non risolvere prima del prezzo;
sezione 02 è **Challenger**, si insegna cosa fa e non si elencano vantaggi;
la garanzia e la scarsità della sezione 04 e 06 sono **Hormozi**, e stanno lì
al posto dello sconto ([[core-crescita-finanze]]).

## Collegamenti

[[script-denkishift]] · [[denkishift]] · [[ms-service]] · [[stile-comunicazione]] ·
[[vincoli-fiscali]] · [[prodotti-e-listino]] · [[core-crescita-finanze]] ·
[[core-commerciale]]
