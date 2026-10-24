---
riga: Le skill di design e di motion installate a livello di account (~/.claude/skills/), quindi valgono in ogni cartella - OperO, DenkiShift, cococa...
type: area
updated: 2026-10-24
source: claude
tags: [skills, design, frontend]
---

# Skill di design — quale si usa, e quando

Quattro skill di design sono installate **a livello di account**
(`~/.claude/skills/`), quindi valgono in ogni cartella: OperO, DenkiShift,
cococat, e anche una sessione aperta qui dentro. Non c'è niente da attivare.

Il problema non è averle, è che **dicono tutte e quattro «fai design
distintivo»** e a leggerne le descrizioni sembrano intercambiabili. Non lo sono:
si distinguono per cosa contengono davvero.

## Da dove si reinstallano

Scritto il 6 settembre 2026 rimettendole su un Mac nuovo: era il buco che
costava di più. Dettaglio in [[2026-09-06-mac-nicola-in-lavoro]].

| Skill | Repository |
|---|---|
| `design-taste-frontend` e le altre nove di `taste-skill` | `github.com/Leonxlnx/taste-skill` (MIT) |
| `impeccable` | `github.com/pbakaus/impeccable` — si copia il bundle `.claude/` del repo, skill **e** quattro agenti |
| `emilkowalski-motion` | `github.com/nexu-io/open-design`, cartella `skills/` |
| `frontend-design`, `ui-ux-pro-max` | skill di account, arrivano da sole |
| `processo-siti` | **nessuno**: scritta da Nicola, vive solo sul PC Windows |
| `stile-apple` | **il vault**: `.claude/skills/stile-apple/`, si ricopia in `~/.claude/skills/` ([[stile-apple]]) |
| `gsap-core`, `gsap-scrolltrigger`, `gsap-plugins` | `npx skills add greensock/gsap-skills@<nome> -g -y` (skill ufficiali GreenSock, 65-73 mila installazioni) |
| `anatomy` | installata il 20/10/2026 per le figure isometriche di oggetti veri (il Reformer di My Balance); origine da riscrivere qui se la si reinstalla |
| `awwwards-animations` | `npx skills add devmartinese/awwwards-animations-skill@awwwards-animations -g -y` (23/10/2026, 2,8 mila installazioni) |
| `cinematic-scroll-storytelling`, `cinematic-gsap-lenis-motion-system` | `npx skills add mengto/skills@<nome> -g -y` (23/10/2026, Meng To, 2-2,3 mila) |
| `shader-glsl`, `threejs-animation` | `npx skills add iart-ai/webgl-animation-skills@<nome> -g -y` (23/10/2026, 1,3 mila) |
| `animation-performance` | `npx skills add emilkowalski/skills@animation-performance -g -y` (23/10/2026, 29 mila) |
| `animated-component-libraries` | `npx skills add freshtechbro/claudedesignskills@animated-component-libraries -g -y` (23/10/2026, 2,8 mila; descrive Magic UI e React Bits, ma i componenti WebGL di React Bits si prendono da `reactbits.dev/r/<Nome>-JS-CSS.json`) |
| `svg-animation` | `npx skills add iart-ai/web-animation-skills@svg-animation -g -y` (24/10/2026, 2,4 mila; tratto che si disegna con `pathLength="1"`, morphing con MorphSVG, MotionPath; cercata per il sito di Satatttvision, affianca `svg-animations`) |
| `logo-animation` | `npx skills add iart-ai/motion-design-skills@logo-animation -g -y` (24/10/2026, 2,7 mila; logo che si disegna a tratto, morphing icona-scritta, ultimo fotogramma statico di riserva) |

## La tabella che serve

| Se stai facendo… | Skill | Perché quella |
|---|---|---|
| Un **sito vetrina**, una landing, un portfolio | `design-taste-frontend` | È l'unica scritta per questo, e **dichiara di non valere** per dashboard, tabelle di dati e interfacce a più passi |
| La **direzione visiva** prima di scrivere una riga | `frontend-design` | 24 KB, nessun archivio: è una **postura**, non un manuale. Palette, tipografia, un rischio estetico giustificato |
| Serve un **dato concreto** — palette per settore, accoppiata di font, preset di animazione, icone | `ui-ux-pro-max` | L'unica con un **archivio interrogabile**: `data/colors.csv`, `google-fonts.csv`, `icons.csv`, `charts.csv`, più 17 preset GSAP e 22 stack |
| Un'interfaccia **che esiste già** e va migliorata, auditata, resa accessibile | `impeccable` | La più grossa (133 file), ha **agenti e script** suoi, ed è l'unica pensata per l'iterazione dal vivo nel browser |
| **Grafici e cruscotti** | `dataviz` | Sceglie la forma prima del colore, e ha un validatore della palette |
| Una pagina pubblicata su claude.ai | `artifact-design` | È la skill degli Artifact, non dei siti |
| Uno **stile Apple** chiesto apposta, su un'app o su una pagina prodotto | `stile-apple` | Token verificati sulle linee guida Apple e su apple.com, componenti, vetro con i ripieghi, revisione e script di controllo ([[stile-apple]]) |
| L'**apertura e la spina allo scroll** di una vetrina: preloader, Lenis, pin, scrub, sfondo in shader | `cinematic-scroll-storytelling`, `shader-glsl`, `animation-performance` | Installate il 23/10/2026 per [[sito-laperegina]]; le regole di Nicola del 14 e 20/10 (scrub senza ritardo, pin corti, niente blur, niente Lenis sul telefono) battono quello che le skill consigliano; il riassunto con i percorsi sta in `direzione/skill-digest.md` del repo `laperegina-site` |

## Per i nostri due prodotti

[[opero]] e [[denkishift]] sono **gestionali**: dashboard, tabelle, flussi a più
passi. Cioè esattamente quello che `design-taste-frontend` dichiara di non
coprire. Là si usa **`impeccable`** per l'audit di quello che c'è e
**`ui-ux-pro-max`** quando serve un valore preciso.

I **siti vetrina** ([[cococat]], [[sito-albybike]]) sono il caso opposto:
`design-taste-frontend` + `frontend-design`, e `ui-ux-pro-max` solo per pescare
la palette e i font.

## L'ordine, quando si parte da zero

1. **Il brief prima della skill.** Chi è il cliente, cosa vende, chi guarda la
   pagina. Una skill di design su un brief vuoto produce un bel niente elegante.
2. `frontend-design` per la direzione: palette, tipografia, un'idea forte.
3. `ui-ux-pro-max` per i valori: font che stanno insieme, colori del settore,
   l'animazione giusta invece di una inventata.
4. Si costruisce.
5. `impeccable` per l'audit: gerarchia, accessibilità, stati vuoti, mobile.
6. **Si guarda nel browser e si misura**, che è la regola numero uno di
   [[opero]] e vale ovunque: `getComputedStyle`, non l'occhio.

## Perché non stanno dentro il vault

Pesano **7 MB in 209 file** e sono roba di terzi che si aggiorna a monte. Il
vault dice di sé che non contiene codice, e versionare qui una copia
significherebbe portarsi dietro una versione vecchia su ogni macchina nuova.
Restano dove sono; qui sta **come si usano**, che è la parte che invecchia più
lentamente.

⚠️ `TODO` — **di dove vengano non è scritto da nessuna parte.** Nessuna delle
quattro ha nel frontmatter un campo di origine: `frontend-design` è la skill
ufficiale di Anthropic (installabile come plugin dal marketplace ufficiale),
`impeccable` dichiara `version: 4.0.3`, le altre due niente. Su una macchina
nuova non c'è un comando da lanciare per rimetterle: vanno ricopiate da
`~/.claude/skills/` di questa macchina, o reinstallate a mano. Da chiarire
prima che serva davvero.

## Collegamenti

[[skills]] · [[stile-apple]] · [[opero]] · [[denkishift]] · [[cococat]] · [[stack]]
