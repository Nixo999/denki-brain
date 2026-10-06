---
type: progetto
riga: Bozza sito Davide Milan, fotografo di diciottesimi e matrimoni, Milano. Mondo A «Il provino», giro 1 del 06/10 su davidemilan.netlify.app, pubblicato da Nicola.
status: attivo
client: davidemilan
stack: html-css-js
started: 2026-10-05
deadline: TODO
updated: 2026-10-06
source: claude
verificato: 2026-10-05
tags: [sito, bozza, fotografia, milano, instagram]
---

# Sito Davide Milan — bozza, Milano

Cartella `~/lavoro/davidemilan-site`, dallo starter. **Repo solo locale**, nessun
remote, niente online. Cliente: [[davidemilan]]. Ha risposto al DM «Manda pure
qui, sono curioso» (05/10): la bozza è la risposta.

## Cosa c'è nella cartella

- `PRODUCT.md`: la verità di prodotto, scritta dal direttore.
- `MONDI.md`: i tre mondi dell'operatore di direzione (Opus), seed impeccable
  `7ca53cfa`, modo Persuade, skill di stile `high-end-visual-design`.
- `raccolta/` (fuori da git): `RACCOLTA.md` con bio, testi dell'Adobe Portfolio,
  12 caption, locali, personalità con le prove; `foto/MANIFESTO.md` con 35 foto
  sopra i 1080 px.

## Il materiale, in una riga

Non fa serate né concerti, come diceva la lista: **9 post su 12 sono
diciottesimi**, 3 lo stesso matrimonio a Sestri Levante. Flash diretto e vicino,
inquadrature storte, luce colorata dei locali, bianco e nero su emozione e
folla, quasi tutto verticale. Foto dall'Adobe Portfolio
`milandavide15.myportfolio.com` a 1920-3840 px. Concorrenti:
[[competitor-siti-fotografi-eventi]].

## Cosa ha chiesto Nicola (05/10)

Telefono come schermo principale, «animato molto attentamente». Apertura nata
dal suo carattere. Seconda schermata fissata: la pagina sembra ferma e
scrollando succede qualcosa. Tela Claude Design prima, con più opzioni
([[direttive-siti]]).

## I tre mondi (`MONDI.md`)

- **A «Il provino»**: il sito è il provino a contatto di una festa. Apertura: la
  pellicola avanza a scatti fino al fotogramma 18, un rettangolo rosso lo
  sceglie e lo apre a tutto schermo. Pin: un foglio di 12 fotogrammi, il rosso
  ne stacca tre. Carta fredda, nero, rosso; Funnel Display + Sometype Mono.
  Rischio: freddo, come «Due occhi».
- **B «Flash»**: il buio del locale, ogni foto entra col lampo che l'ha fatta.
  Apertura: la ragazza con le peonie quasi al buio, lampo, nome con l'ombra dura,
  inquadratura storta. Pin: tre lampi che impilano tre stampe. Nero sala, bianco
  lampo, un rosso; Big Shoulders Display + Martian Mono. Rischio: fondo tutto
  uguale.
- **C «La serata»**: il fondo va dal tramonto al faro viola. Apertura: un cono
  di luce continua il faro della foto del palloncino «18». Pin: quattro campi di
  colore, una parola per fase. Ambra, rosa, cobalto, viola, oro; Anybody.
  Rischio: gradienti e viola letti come sito fatto con l'AI.

L'operatore raccomandava B. **Nicola ha scelto A «Il provino» il 06/10** («io direi di fare il mondo a»), dalle tavole di apertura e scroll; le pagine intere di B e C non sono state finite, fermate per risparmiare token (90% del limite settimanale).

## Tela di design (05/10)

<https://claude.ai/artifact/4WnNZAxC4fMZvYYAt1HKws> (privata). 22 foto caricate
con il sì di Nicola («carica le foto»): il controllo dei permessi le aveva
bloccate come uscita di dati. Tre tavole per mondo: apertura animata, seconda
schermata allo scroll, pagina intera da telefono.

## I giri

- **Giro 0** (05/10): raccolta e concorrenti su Sonnet, direzione e tavole su
  Opus. Nessun codice del sito ancora.
- **Giro 1** (06/10, mattina): copy (`COPY.md`) e foto web (`assets/img/`, 30 in
  due taglie) in parallelo alle tavole; `BRIEF-COSTRUZIONE.md` scritto prima
  della scelta; costruzione del mondo A su un operatore Opus, scadenza di Nicola
  «prima delle 11». Sito Netlify `davidemilan` creato da Nicola sul team
  `nicola-la-rezza` (il controllo permessi blocca a Trevis creazione e deploy),
  badge spento, `.deploy/` è la copia da pubblicare senza `raccolta/`.
  **Consegnato alle 11:02** (commit `6eb73c1`): apertura trasportata dalla tavola,
  pin con scrub e i quattro stati, copy com'è; controlla-sito 8/8, testo 0, slop
  1 blocco (regex sui segnaposto); 1440 scritto e mai guardato; catena
  (impeccable, trappole, direttive) non caricata per la scadenza. L'operatore
  Opus si è bloccato due volte sulle scritture lunghe; una costruzione parallela
  su Fable (ramo `fable`, worktree `~/lavoro/davidemilan-site-fable`, commit
  `e253248`) è arrivata alle 11:03 con 6/8, slop 2 e niente guardato: resta come
  riserva, non si pubblica. Online su `davidemilan.netlify.app`.

## Giro 2, da fare

Guardare il 1440 · slop a 0 (segnaposto o regola) · favicon e og:image ·
contrasti (20 segnalazioni) · passo bolder/delight/animate · `impeccable polish`
· pagina senza JS, `?cattura`, reduced motion · mail del modulo Netlify Forms.

## Da chiedere a Davide

Prezzi e pacchetti · ore di copertura, numero di foto, tempi di consegna ·
acconto e disdetta · mail, telefono, WhatsApp · liberatorie per i visi dei
ragazzi dei diciottesimi · permesso sul commento della cliente del matrimonio ·
file del logo (c'è solo a 150 px) · prova di battesimi e lauree, che stanno
solo nella bio.

## Non verificato

Le caption oltre i primi 12 post e le sei storie in evidenza (serve il login) ·
circa 250 foto dell'Adobe Portfolio mai guardate: le 35 tenute sono un campione
a passo costante, viste in fogli-contatto · il pin sul telefono contrasta con
la direttiva del 25/09 «lo scroll resta di chi legge»: tenuto perché chiesto
da Nicola, massimo 2,5 schermi.
