---
type: area
updated: 2026-08-28
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

## La tabella che serve

| Se stai facendo… | Skill | Perché quella |
|---|---|---|
| Un **sito vetrina**, una landing, un portfolio | `design-taste-frontend` | È l'unica scritta per questo, e **dichiara di non valere** per dashboard, tabelle di dati e interfacce a più passi |
| La **direzione visiva** prima di scrivere una riga | `frontend-design` | 24 KB, nessun archivio: è una **postura**, non un manuale. Palette, tipografia, un rischio estetico giustificato |
| Serve un **dato concreto** — palette per settore, accoppiata di font, preset di animazione, icone | `ui-ux-pro-max` | L'unica con un **archivio interrogabile**: `data/colors.csv`, `google-fonts.csv`, `icons.csv`, `charts.csv`, più 17 preset GSAP e 22 stack |
| Un'interfaccia **che esiste già** e va migliorata, auditata, resa accessibile | `impeccable` | La più grossa (133 file), ha **agenti e script** suoi, ed è l'unica pensata per l'iterazione dal vivo nel browser |
| **Grafici e cruscotti** | `dataviz` | Sceglie la forma prima del colore, e ha un validatore della palette |
| Una pagina pubblicata su claude.ai | `artifact-design` | È la skill degli Artifact, non dei siti |

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

[[skills]] · [[opero]] · [[denkishift]] · [[cococat]] · [[stack]]
