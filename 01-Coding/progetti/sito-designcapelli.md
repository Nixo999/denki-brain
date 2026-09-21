---
type: progetto
riga: Bozza sito per Design Capelli (Nichelino, TO) - mondo «la luce della via», la pagina schiarisce di un tono a sezione, logo vero del cliente in testa, Cabinet Grotesk + Gambetta. Online su designcapelli.netlify.app dal 21/9, giro 4, 8/8 e slop 0.
status: attivo
client: design-capelli
stack: html-css-js
started: 2026-09-21
deadline:
updated: 2026-09-21
source: claude
verificato: 2026-09-21
tags: [sito, bozza, parrucchiere, nichelino, torino, instagram]
---

# Sito Design Capelli — bozza, Nichelino (TO)

Repo `Nixo999/designcapelli-site` (privata), cartella
`~/lavoro/designcapelli-site`. Il cliente sta in [[design-capelli]]: ha risposto
**«Buonasera qui grazie»** al DM del 20/09 e la bozza la vuole nel DM.

## Il mondo scelto — «la luce della via»

Proposti tre mondi dall'operatore di direzione (`MONDI.md` nel repo), scelto il
secondo con due innesti e tre correzioni (`MONDO.md`).

**La metafora.** Sei foto su sette del suo feed sono girate **sul marciapiede di
via XXV Aprile o contro la vetrina**, con le auto e i mattoni dentro
l'inquadratura: qui il colore si guarda **alla luce della via**, non sotto i
faretti. E il colore ha una notazione vera — livello e riflesso, `6.34`, `9.1` —
che è l'unico punto in cui questo mestiere scrive già in codice. Un salone che si
chiama «Design» quel codice ce l'ha in mano da dieci anni.

**La spina.** La pagina **schiarisce di un tono a sezione**, dal castano della
radice al platino della punta. La schiaritura *è* il movimento della pagina:
niente linea che segue lo scroll.

**Gli scarti.** «La vetrina» (il marchio ripetuto come carta da parati) scartato
perché un fondo a motivo dietro al testo è già stato bocciato tre volte su
[[sito-barbershop-snia]]; ne resta l'innesto, il motivo **solo** dietro la fascia
finale dei contatti. «Programma» (manifesti Olivetti) scartato perché i campi
astratti sono la bocciatura «forme messe a caso».

## Le due cose che il direttore ha verificato a mano

1. **I marchi sono due.** Quello di adesso è un **corsivo calligrafico rosso**;
   la vetrina porta un **serif in maiuscoletto** più vecchio, con D e C
   ingrandite, ripetuto su tutto il vetro. In testa va il corsivo — dal giro 4
   nel **suo file**, non ricostruito — e il serif resta nel motivo dei contatti.
2. **I rossi in pagina sono due, e la differenza è spiegata sotto**: il logo è
   `#E10736`, letto dal file a 720 px; il bordeaux dell'interfaccia è `#73343E`,
   campionato quando del logo si aveva solo l'avatar a 150 px, sbiadito
   dall'anti-aliasing.

## Cosa non c'è, e perché

- **Prezzi: nessuno.** Non ne pubblica né Fresha né PagineGialle. Nessun «a
  partire da».
- **Fresha non si linka**: la scheda dichiara in pagina che il salone **non è
  affiliato**, l'unico bottone è «Call to book». La prenotazione è WhatsApp, come
  dice la sua bio.
- **Gli orari confliggono** fra PagineGialle e Fresha. In pagina è andata la
  versione martedì–sabato 09:30–19:00, e **Patrick la fa confermare a Daniela
  prima del go-live**. Il confronto sta in `RACCOLTA.md`.
- **Le foto sono a 512×640**, sotto il minimo di 1080: Instagram non serve
  l'originale senza login e la firma dell'URL rifiuta la richiesta a 1080. Stanno
  in pagina **sotto i 260 px**, e il sito regge anche senza. Gli originali si
  chiedono a Daniela.

## Cosa c'è di vero, e viene usato

- **Google: 4,5 su 21 recensioni**, tre testi letterali con nome e piattaforma.
- **«HAIR AND PASSION»**, il loro «In breve» su Facebook.
- **Dal 2015** nella stessa vetrina: la prova che sostituisce prezzi e listino.
- **GHD**, dalle storie in evidenza.

## Come è fatto — otto sezioni, un tono ciascuna

Radice scura → platino. 1 il logo con i tre fatti e la scala dei
dieci livelli · 2 dieci anni nella stessa vetrina · 3 il colore ha un numero
(livelli e sei riflessi) · 4 alla luce della via · 5 la schiaritura, con le
barre che salgono da 4 a 10 · 6 quello che non ha un codice (i servizi) · 7
quello che scrivono (le recensioni) · 8 i contatti, con il marchio vecchio della
vetrina a motivo su tutta la fascia.

**L'apertura**: cinque salti di tono con le cifre 10·8·6·4·1, il marchio che
scende a 360 ms mentre l'ultima cifra è ancora lì, sipario aperto a 555 ms,
tutto finito in **~0,80 s** (era 1,18 s). Parte a ogni caricamento, si spegne con
`prefers-reduced-motion` e con `?cattura`.

**Tipografia**: Cabinet Grotesk 700/800 per il display e le cifre, Gambetta
400/500 e italico per il testo.

## Il marchio — giro 4, 21/09

Nicola: **«sostituisci desing capelli con il loro logo»**. In testa c'era il nome
composto in Pinyon Script, scelto su saggio contro cinque corsivi come
ricostruzione fedele. Non basta: dove sta il marchio del cliente ci va **il suo
file**. Preso a **720×720 dalla pagina Facebook** — l'avatar di Instagram è 150 px
— fondo bianco tolto dal canale verde, inchiostro tenuto com'è.

**Il rosso vero del logo è `#E10736`**, molto più acceso del bordeaux `#73343E`
che la pagina usa per bottoni e link: quel valore era stato campionato
dall'avatar a 150 px, che è sbiadito dall'anti-aliasing. Il resto della pagina
resta com'è — «per il resto va bene» — quindi in pagina convivono il rosso del
logo e il bordeaux dell'interfaccia.

## Stato — online dal 21/09/2026

**<https://designcapelli.netlify.app>**, progetto `designcapelli` sul team
`nicola-la-rezza`, deploy dal CLI `--prod --no-build`, repo
`Nixo999/designcapelli-site` (`main`, pushato). Badge Netlify **spento dall'API**.

**Tre sbarramenti verificati con `curl` sul deploy pubblicato**: `meta robots` in
pagina, `x-robots-tag` negli header, `robots.txt` con `Disallow: /`. I quattro
file di lavoro (`RACCOLTA`, `RICERCA`, `MONDO`, `MONDI`) rispondono **404**.

| Misura | Esito |
|---|---|
| `controlla-sito.py` | **8/8** |
| `controlla-slop.py` | **exit 0**, due avvisi guardati e approvati |
| Contrasto | 91 nodi, zero falliti, minimo **7,05:1** |
| Overflow | **0** a 1440, 1280, 1024, 901, 899, 768, 621, 619, 375, 320 |
| Apertura | **~0,80 s**, zero fotogrammi a una tinta sola (misurati con `cattura-apertura.mjs`) |
| Altezza documento | da 6590 px del giro 1 a **4677** |

I due avvisi di slop restano di proposito: «qualità» e «professionalità» stanno
dentro recensioni citate alla lettera, e i sette `cramped-padding` sono falsi
positivi sullo shorthand con `var()`.

**Quattro giri.** Il giro 1 era giusto di contenuto e **vuoto di desktop** — sezioni
a metà finestra e bande verticali morte, la bocciatura «lo vedo vuoto» già presa
due volte. Il giro 2 ha densificato. Il giro 3 ha chiuso tre cose: il vuoto
residuo in «La schiaritura», il motivo della vetrina che era diventato un
rettangolo di texture, e **300 ms di schermo vuoto dentro l'apertura**, che nel
pannello non si vedevano e sono usciti contando le tinte dei fotogrammi.

**Giro 4** (21/09): il logo vero al posto della ricostruzione, apertura da 1,18 a
0,80 s, e un difetto trovato misurando — il sipario viveva sotto `.js`, che il
boot in fondo al body accende **dietro a GSAP dalla CDN**: la pagina compariva
intera e mezzo secondo dopo il sipario le cadeva sopra. Ora si accende da uno
script in testa e la sua uscita è in CSS. **Lo starter è stato corretto lo stesso
giorno**, così non lo ripete nessun sito nuovo.

`TODO` **il verdetto di Nicola** sul giro 4, e il DM col link è di Patrick.

## Collegamenti

[[design-capelli]] · [[processo-siti]] · [[direttive-siti]] · [[anti-slop-siti]]
· [[netlify]] · [[registro-interventi]]
