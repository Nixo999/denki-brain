---
type: risorsa
riga: La pipeline dei siti vetrina da un profilo Instagram - raccolta, catalogo, cancelli, skill. Cosa gira, cosa no, cosa aspetta Nicola.
updated: 2026-10-31
source: claude
verificato: 2026-10-31
tags: [siti, pipeline, instagram, cancelli, strumenti]
---

# Pipeline dei siti vetrina

Nicola, 31/10/2026: i siti vetrina «a volte vengono bene a volte male». Su 54
note di siti, 4 sono riusciti, 17 bocciati, 18 «bello ma…». La pipeline serve
a ridurre la casualità prendendo il metodo «compito ripetuto → skill →
automazione con cancelli». Parte dall'Instagram del cliente. Il gusto resta di
Nicola: la pipeline non sceglie la direzione al posto suo.

## I quattro pezzi e a che punto sono

| Pezzo | Stato al 31/10 | File |
|---|---|---|
| 1. Raccolta da Instagram | gira, provata su `@mikuma.dogs` | `raccogli-instagram.js`, `raccogli-instagram.py` |
| 2. Catalogo di sezioni approvate | fermo: cambia lo starter, aspetta Nicola | — |
| 3. Cancelli | gira, provata su Mikuma e Davide Milan | `cancelli-sito.py`, `cancelli-telefono.mjs` |
| 4. Skill `/nuovo-sito @profilo` | fermo: cambia il processo, aspetta Nicola | — |

## 1. Raccolta

Instagram senza login non risponde più a `curl`: l'API pubblica dà `401
require_login` ([[trappole]], sezione Scraping). Nel browser dell'app sloggato
invece profilo, griglia, didascalie e foto a 1440 px si leggono ancora.

Il giro è questo:

1. Si apre `instagram.com/<utente>/` nel browser dell'app, scheda in primo
   piano, e si incolla `raccogli-instagram.js` in `javascript_tool`. L'esito
   si salva in `~/lavoro/raccolte/<utente>/grezzo/profilo.json`.
2. Per ogni post di tipo `p` della griglia si apre la sua pagina, si rilancia
   lo stesso snippet e si salva `grezzo/<codice>.json`. I Reel si saltano:
   danno solo fotogrammi a 640 px.
3. `python3 01-Coding/strumenti/raccogli-instagram.py <utente>` scarica le foto,
   le misura con `sips`, scarta i Reel e tutto sotto i 1080 px, campiona i
   colori della foto profilo e scrive `scheda.md` e `scheda.json`.

Gli URL delle foto sono firmati e scadono in pochi giorni, quindi il passo 3 si
fa nella stessa sessione. Lo script esce 1 se le foto buone sono meno di sei.

Limiti verificati: il contenuto delle storie in evidenza da sloggati non si
apre, quindi la scheda ha solo i titoli. La pagina di Instagram non può
mandare dati a un server locale, quindi chi guida il browser copia il JSON su
file; un URL copiato male si riconosce perché lo script lo scarta come «file
finto» o «scaricamento fallito».

## 3. Cancelli

`python3 01-Coding/strumenti/cancelli-sito.py ~/lavoro/<nome>-site` lancia i
tre controlli sui file e poi `cancelli-telefono.mjs`, che apre la pagina a
375x812 con CPU rallentata 4 volte e misura lag e nove bocciature ricorrenti
di [[direttive-siti]]: pagina più larga del telefono, apertura di sola
scritta, numerazione delle sezioni, muro di foto, disegni inline, sottolineature,
cambi di sfondo netti, barra appiccicata al titolo, peso della pagina.

**Il lag non si misura come fotogrammi lenti in headless.** Su quattro siti
approvati e cinque bocciati per il lag, lo scroll dà a tutti un p95 di 17-18 ms.
Si misura invece una causa vera, quella che il giro 4b di Groavel ha trovato e
tolto il 27/10: `will-change` su livelli grandi (44 livelli composti, 1,4 GB di
memoria grafica all'apertura). Il controllo «livelli» somma l'area degli
elementi con `will-change` e la conta in schermi:

| Versione | A 375 px | A 1440 px |
|---|---|---|
| Groavel prima del giro 4b (`0fcbb78`, laggava) | 20 schermi | 29 |
| Groavel adesso (`a6a1751`, piace a Nicola) | 0 | 1,1 |
| Fiftynine, NG Barber, Mikuma, Davide Milan | da 0 a 13,8 | da 0,1 a 7,3 |

Sopra i 15 schermi il cancello avvisa. Gli altri quattro siti bocciati per il
lag hanno quest'area vicina a zero, quindi il loro lag aveva altre cause, che
questo controllo non vede. Non so se le loro `dist/` di oggi siano la versione
bocciata o una versione già corretta.

Il numero di elementi della pagina, che sembrava separare i gruppi (approvati
181-450, bocciati 500-1625), vale poco: Groavel ne ha 693 e a Nicola piace.
Resta un avviso.

## Groavel come modello, 31/10

Nicola: «considera che ad esempio quello nuovo di groavle a me piace, ce
qualche dettaglo da aggiuate ma con quello siamo sulla strada giusta». È la
versione del 30/10 (`a6a1751`), già passata al cliente e senza sbarramenti.
Con `--consegnato` passa tutti i cancelli; restano gli avvisi su apertura
(la foto più grande copre il 7% del primo schermo a 375 px), 13 disegni
inline e 693 elementi. Quali siano i «dettagli da aggiustare» va chiesto a
Nicola, non dedotto dalle note.

Cosa ne ricavo per la pipeline:
- **Astro non è la causa del lag.** Groavel è in Astro con GSAP e oggi non ha
  `will-change` su livelli grandi. Il lag stava in una scelta di CSS che si
  misura, quindi Astro resta ammesso e il cancello «livelli» sta in fondo.
- **Più operatori hanno funzionato, con un contratto.** Groavel l'hanno
  costruito tre operatori Opus con un contratto di DOM scritto prima, e poi
  cinque giri di correzioni con Nicola che guardava dal telefono. La
  conclusione «una sola testa» quindi non regge da sola: regge «una sola
  direzione e un contratto scritto», più i giri guardati da Nicola.
- **Un disegno ricalcato da una cosa vera è passato.** I disegni inline di
  Groavel sono le cuciture fra le sezioni e la forma del percorso ricalcata
  dalla mappa Strava dell'evento. «Non disegnare niente tu» colpiva disegni
  inventati (il guinzaglio e il cane del 12/10), non tracciati da dati veri.
  È un'ipotesi da confermare con Nicola.
- **Sezioni candidate per il catalogo**: l'hero con la foto a destra da
  computer e tolta sotto i 900 px; «La prossima uscita» con data, locandina e
  ritrovo; le uscite per distanza; i corsi e le guide con foto piccole; la
  galleria Memories a griglia irregolare; il contatto finale. I componenti
  `Foto.astro` (formato e larghezze responsive) e `Cucitura.astro` (colore di
  partenza e di arrivo) sono già parametrici.

## Contraddizioni aperte con processo-siti

- `processo-siti` rende obbligatori «la grafica inventata e lo scroll-telling»,
  e `controlla-sito.py` chiede almeno 3 `<svg>` inline o un racconto
  tipografico. Nicola ha scritto più volte di non disegnare niente noi
  ([[direttive-siti]], 12/10 e 23/10). In `cancelli-sito.py` quei due
  controlli escono come CONTRADDIZIONE e non bloccano, finché Nicola non
  decide.
- Lo starter dice «nessun componente, nessuna sezione». Il catalogo di sezioni
  approvate lo contraddice per costruzione.
- `processo-siti` divide la direzione e la costruzione fra più operatori. NG
  Barber, Fiftynine e Mikuma li ha fatti una sola testa, Groavel tre operatori
  con un contratto di DOM: la regola da scrivere è ancora da decidere.

## Collegamenti

[[processo-siti]] · [[direttive-siti]] · [[strumenti]] · [[trappole]] ·
[[sito-ngbarber]] · [[sito-fiftynine]] · [[sito-mikuma-dogs]] · [[sito-davidemilan]] · [[sito-groavel]]
