---
type: progetto
status: attivo
client: il-salone-di-andrea
stack: [html, gsap, netlify]
started: 2026-09-06
deadline: TODO
updated: 2026-09-06
source: claude
valore: TODO
incassato: 0
---

# Sito Il Salone di Andrea — bozza al buio, Dalmine

Sito vetrina in una pagina per **Il Salone di Andrea**, parrucchiere donna e
uomo di **Andrea Bielli** a **Dalmine (BG)**, Viale Natale Betelli 58. È la
riga `@ilsalonediandrea` della [[2026-09-05-instagram-bg-va|lista Instagram
del 5 settembre]]: **dominio `ilsalonediandrea.it` morto** (NXDOMAIN) ma
ancora indicizzato con le pagine chi-siamo, acconciature-sposa, contatti,
servizio barber. Il DM di Patrick parte da lì; la bozza è l'esca del secondo
messaggio ([[dm-instagram-vetrina]]).

**Repo**: `github.com/Nixo999/salonediandrea-site` (privato, creato il
6 settembre 2026 con `gh`) — in locale `~/lavoro/salonediandrea-site` sul
MacBook nuovo di Nicola.
**Online**: no — va su Netlify come ogni bozza ([[netlify]]).
**Stack**: HTML puro, un solo `index.html`, zero build, GSAP 3.13 +
ScrollTrigger da CDN (motion additiva), 16 foto in `assets/ig/`.
`netlify.toml` e `robots.txt` con lo schema di NG Barber: **noindex** finché
il sito non è suo.

## Da dove vengono i dati

Tutto letto il 6 settembre 2026, niente inventato. **Instagram si apre dal
pannello del MacBook**: la nota del 5 settembre («non si apre da nessuna
delle nostre macchine») vale per il PC Windows e il Mac di Patrick, non qui.

| Dato | Fonte |
|---|---|
| 935 follower, 100 post, bio «Dalmine - Viale Natale Betelli 58. Tel 344 4976360», storie in evidenza Backstage · Biondi · Bride | profilo Instagram, dal pannello |
| 12 post con didascalia (gli unici raggiungibili senza login), foto a 1440 px e copertine reel a 640 px | pagine dei post; tabella in `assets/ig/didascalie.md` |
| Aperto nel **2018**, **nuovo atelier a maggio 2023**, «le mie ragazze», Mary Corti hair colorist | post del 18 maggio 2024 e del 5 ottobre 2024 |
| Orari: mar-mer 9-18, gio 12-21, ven-sab 9-18, lun e dom chiuso | tutti-gli-orari.it e oraridiapertura24 (Virgilio dice gio 10-21: si scrive 12-21) |
| Vecchia sede Via Cesare Battisti 5, tel 035 566369, titolare Andrea Bielli | Virgilio (sede vecchia: il numero non si usa) |
| «Andrea è stato bravissimo» | reel di @dario_beloli_ifbbpro, 29 gennaio 2026 |
| Logo: wordmark IL SALONE DI ANDREA / HAIR CARE | foto profilo a 150 px, ricomposto in Archivo |

⚠️ **Nessun prezzo, nessuna recensione leggibile, nessuna email in bio**: il
sito non ne scrive. ⚠️ **Il vecchio sito è irrecuperabile**: Wayback risponde
500 sulla home e non ha le sottopagine. ⚠️ Foto in mano: 9 a 1440 px e 4
copertine a 640 px. Le altre 88 vanno chieste ad Andrea.

## Com'è fatto

Metodo [[processo-siti]] completo, con un giro in più:
`design-taste-frontend` → `high-end-visual-design` → `impeccable` (PRODUCT.md,
`concept-seed` seed **`e5bd3d89`**, pagina di decisione nel pannello).
**Il dado ha assegnato «Il rullo»** (candidato 3: un fotogramma a schermo
intero per lavoro, come il profilo scorso davanti allo specchio) e Nicola l'ha
scelto sul tool strutturato, perché la pagina di decisione si era chiusa senza
risposta.

**Prima versione bocciata da Nicola a metà costruzione**: «fallo molto più
professionale, ispirati al sito di NG Barber, deve essere spettacolare, così
è solo una rivisitazione del suo Instagram». Il rischio scritto sulla carta si
era avverato. Il vincolo dell'utente batte il dado
([[2026-09-06-sito-salone-andrea-direzione]]).

**Seconda versione, quella nel repo**: scroll-telling cinematografico nella
grammatica di `ngbarber-site`, nel mondo del salone (notte petrolio, ottone,
Archivo espanso maiuscolo, Parisienne per una riga di script per capitolo,
grana, alone ottone che segue lo scroll). Sipario con il wordmark che si
compone lettera per lettera → hero con la foto di Cristina e Andrea allo
specchio e il titolo a due righe da 148 px → manifesto parola per parola con
le parole vere di Andrea («Il risultato parla da sé») → marquee dei servizi →
sei lavori in griglia sfalsata con parallasse → **«Il salone», l'unico
capitolo appuntato**: lo specchio tondo con la foto di Andrea che si mette a
fuoco e i tre anni (2018, maggio 2023, maggio 2024) che si accendono con lo
scrub → copertine dei reel e la voce di Dario Beloli → finale «Chiama /
Prenota» che scorre con lo scroll, orari e mappa.

Regole imparate qui, che valgono per i prossimi siti: **mai posizionare con un
`transform` CSS un elemento che GSAP anima** (lo sovrascrive al primo frame e
l'elemento salta); **niente `filter:blur` su cose che scorrono** e la luce che
segue lo scroll si muove in `transform`, non ridipingendo un gradiente.

Buchi dichiarati: lo script di ricerca di `ui-ux-pro-max` non è su questo Mac
(c'è solo il SKILL.md): il passo 4 è andato a tabella di priorità. Nessun tool
di generazione immagini: build code-led.

## Stato

🟡 **Bozza fatta, sul repo privato, passata dalla finish review.** Hero a
due righe a 1440 e a 375, zero overflow, GSAP e font caricati, sipario che si
chiude. Catture in `.impeccable/review/` (desktop intera, mobile a otto
schermate). **Finish review di impeccable**: prima passata «fix» con otto
rilievi materiali (wordmark da incidere nello specchio, due citazioni non
alla lettera, pillola Chiama sparita sotto i 640 px, griglia che sembrava il
profilo, date come eyebrow, «lui al taglio» che nessun post dice, due fasce
vuote, riga donna/uomo che si fondeva su telefono), tutti applicati; verdetto
sei risolti, uno parziale e una regressione, chiusi al secondo verdetto; resta
un residuo di 30 px sulla fascia prima di «Chiama», chiuso senza terzo giro.
**Nicola l'ha vista nel pannello** e ha segnalato lo specchio che spariva allo
scroll e la pagina a scatti: era un `transform` CSS che GSAP sovrascriveva e
tre effetti ridipinti a ogni frame (`filter:blur`, gradiente animato via
variabile, grana): corretti in `299d5bb`. **Non vista su telefono.**

## Soldi

| | |
|---|---|
| Pattuito | niente — nessun contatto ancora |
| Listino di riferimento | sito vetrina, [[prodotti-e-listino]] |
| Forma | Ricevuta prestazione occasionale → [[vincoli-fiscali]] |

## Aperto

- [ ] Pubblicazione su Netlify (login di Nicola, [[netlify]])
- [ ] Il DM del 5 settembre è già sul banco: la bozza entra nel secondo messaggio, se risponde
- [ ] Da confermare con Andrea: orario del giovedì, email, foto in risoluzione piena, le storie Bride per la sezione sposa
- [ ] Se compra: via il `noindex`, dominio `ilsalonediandrea.it` da riprendere (è libero: NXDOMAIN)

## Collegamenti

[[netlify]] · [[processo-siti]] · [[dm-instagram-vetrina]] ·
[[2026-09-05-instagram-bg-va]] · [[2026-09-06-sito-salone-andrea-direzione]] ·
[[registro-interventi]]
