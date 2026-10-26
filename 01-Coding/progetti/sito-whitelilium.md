---
riga: Sito White Lilium Photography (Isidora Francescati, fotografa maternity/newborn/famiglia, Trezzano). Giro 2-bis del 26/10: otto pagine Astro, gallerie con uno schema per pagina sul telefono.
type: progetto
status: attivo
client: whitelilium
stack: [astro, gsap, webgl, netlify]
started: 2026-10-07
deadline: TODO
updated: 2026-10-26
source: claude
verificato: 2026-10-26
valore: 0
incassato: 0
---

# Sito White Lilium Photography

Sito per [[whitelilium]], Isidora Francescati, fotografa di maternità, neonati, bambini e famiglia a Trezzano sul Naviglio
(MI). Esca del flusso A diventata lavoro vero: il 07/10 ha risposto al DM di Patrick («Stavo già pensando di fare un sito»),
il 22/10 ha mandato per mail 59 foto a piena risoluzione, il suo ritratto, la sua storia in PDF e le sei schede che vuole.

**Repo**: `~/lavoro/whitelilium-site`, **solo locale** (nessun remoto). Astro 5 a uscita statica, GSAP con ScrollTrigger e
SplitText, WebGL nudo per la luce, nessun React.
**Online**: whiteliliumphotography.netlify.app (sito Netlify `e96a0b8a-791a-45e2-b98e-a5ee472ad53e`, team denkicode). Si
ripubblica con `npm run build && netlify deploy --dir dist --prod --no-build --site e96a0b8a-791a-45e2-b98e-a5ee472ad53e`.
Tre sbarramenti attivi, più 404 forzato su `PRODUCT.md`, `direzione/*`, `riferimenti/*`, `raccolta/*`, `prove/*`, `scripts/*`.
**Memoria tecnica nel repo**: `PRODUCT.md` (verità di prodotto), `direzione/DIREZIONE.md` (il mondo del giro 2),
`direzione/contratto.md` (il DOM fra gli operatori), `direzione/{scheletro,pagina,schede,motion,skill-digest}.md` (i
rapporti), `riferimenti/foto.md` (una riga per foto, scritta guardandola), `riferimenti/concorrenti-schede.md`,
`raccolta/` (07/10). Il giro 1 «Il controluce» sta in `direzione/giro1-il-controluce.md`.

## Le otto pagine
Home, `/maternity` (Classico e, su campo bruno, Editorial), `/newborn`, `/oldborn`, `/baby`, `/smash-cake`, `/family`,
`/chi-sono`. Le sei schede sono quelle che ha scritto lei nella mail, nel suo ordine e con i suoi nomi («oldborn» è parola
sua: gli altri fotografi dicono «sitter»). Ogni scheda: testa con la sua frase e una foto come stampa, «Com'è la sessione»
scritto guardando le sue foto, «Quando» e «Cosa indossare» senza dati inventati, galleria con tutte le foto della cartella
senza didascalie, «Prossimo capitolo», Scrivimi.

## Giro 2 «Un anno in sei capitoli» (24-26/10)
La metafora è sua: «Il tempo non possiamo fermarlo, ma possiamo scegliere come custodire ciò che conta». Le sei schede
sono un anno di una famiglia, dall'attesa alla famiglia che cresce, e la home li legge come capitoli con sei campi che si
scaldano (avorio → miele chiaro). Apertura «la tenda»: le tende bianche del suo studio (stanno in venti foto) coprono lo
schermo, il nome si scrive, una luce WebGL (fbm dal ricettario di `shader-glsl`) si accende dietro, i teli si aprono di
lato e le tre stampe dell'hero (pancione, primi giorni, primo anno) si aprono a ventaglio: 1,7 s, un gesto solo. Da computer
la scena dei capitoli è sticky e la foto cambia con una tendina a ogni capitolo (0,45 s, senza scrub); sul telefono sei
blocchi colorati, niente scrub. Lenis spento: scroll nativo (Nicola, 20/10). Font del giro 1: Fraunces, Figtree, Pinyon.
Nessun disegno: luce, tipografia e le sue foto.

**Metodo**: Fable dirige e non costruisce. Quattro Sonnet in parallelo (foto in WebP con provini e catalogo, scheletro
Astro, digest delle skill con `npx skills find`, concorrenti al volo), direzione e contratto scritti da Fable, poi tre
Opus in parallelo su un contratto di DOM («pagina»: home, Chi sono, `stile.css`; «schede»: le sei pagine; «motion»: i
quattro moduli). Il 24/10 alle 21:40 il limite di utilizzo ha fermato «pagina» e «motion»; ripresi il 26/10 da dove
erano. Tempo di lavoro: circa 55 minuti il 24/10 più 25 il 26/10.

**Misurato** (26/10): `controlla-sito` **8/8**, `controlla-slop` 0 blocchi e 4 avvisi (il «davvero» è in una frase sua, i
gruppi di tre sono frasi sue e la barra, i numeri 01-06 sono i capitoli), `controlla-testo` 0/0. Apertura 1.671 ms in home
e 597 ms sulle schede, nessun fotogramma vuoto (309-9091 tinte a 100-1600 ms), 57 fotogrammi al secondo in 5 s di scroll a
1440 (un fotogramma da 133 ms), overflow 0 a 1440 e 375 su home, Chi sono e Maternity, console pulita (headless). Guardato
dal vivo nel pannello a 1440 e a 375: home, Maternity, Chi sono. Peso del 800 px: 41 KB in media.
**Deboli**: da computer la colonna dei capitoli ha poco testo accanto alla scena sticky (un occhiello, un titolo, una riga);
la foto di testa delle schede e le rivelazioni nel pannello nascosto arrivano in ritardo (artefatto del pannello, non del
sito). Non visto: iPhone e Safari veri, il passaggio da 1440 a 375 senza ricaricare, la finish review di impeccable.
**Verdetto di Nicola sul giro 2** (26/10, dal telefono): «ok bello ma da telefono risulta un po troppo ripetitivo e muro di foto,
prova magari a disporle in modi piu particolari in base alla pagine, e da telelfono togline magari giustoun paio in modo che non
semnbri un muro di foto». Regola in [[direttive-siti]].

## Giro 2-bis (26/10, stessa mattina)
Sotto 768 px ogni scheda ha il suo schema di galleria, calcolato da `src/components/scheda/FotoGriglia.astro` sulle sole foto
che si vedono dal telefono: Maternity «la rivista» (una intera, due 3:4; 12 foto su 16), Editorial «la pellicola» (colonna al
72% alternata; 6 su 8), Newborn «l'album» (3:2, due quadrate; 8 su 11), Oldborn «le cartoline» (4), Baby «la striscia» (tre
quadrati, una grande; 6 su 8), Smash cake «il carosello» (scroll-snap, puntini in CSS; 5 su 7), Family «il racconto» (3 su 4).
Le foto tolte sono le più deboli del catalogo (`riferimenti/foto.md`) e restano da 768 in su. Home sotto 1024: i capitoli pari
hanno la foto al 56% con il numero a sinistra, Dove e Come si svolge hanno la seconda foto ridotta. Da computer niente è
cambiato. Controlli 8/8, slop 0, testo 0; le sette gallerie guardate a 375 nel pannello e in cattura headless. Online, commit
`2aabc60`. **Verdetto di Nicola sul 2-bis**: TODO. Da computer resta aperto: sotto le due foto orizzontali nella griglia a 3-4
colonne c'è una striscia vuota di circa 20 px.

## Da chiedere a lei (via Patrick: «sentiamoci per capire i dettagli»)
Prezzi o «a partire da»; durata, numero di foto e tempi di consegna; quando prenotare maternity e newborn; le età di
oldborn e baby; se il bagnetto fa parte di ogni smash cake; dove sta lo studio; WhatsApp; logo; il dominio `.it`; il via
libera sui visi dei bambini nelle gallerie; se vuole le recensioni Google; se l'editorial resta scuro.

## Trappole pagate qui
`Astro.url.pathname` con `format: 'file'` in build porta `.html`; `gsap.matchMedia` con sole condizioni «grande» e
«ridotto» non parte sotto 1024 px (anche Mon Amour ha il difetto). Tutte e due in [[trappole]].
