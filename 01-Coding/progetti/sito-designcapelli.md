---
type: progetto
riga: Bozza sito per Design Capelli (Nichelino, TO) in ~/lavoro/designcapelli-site - mondo «la luce della via», la pagina schiarisce di un tono a sezione, Cabinet Grotesk + Gambetta, recensioni Google vere. In costruzione il 21/9.
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

1. **I marchi sono due.** La foto profilo è un **corsivo calligrafico**
   bordeaux; la vetrina porta un **serif in maiuscoletto** più vecchio, con D e C
   ingrandite, ripetuto su tutto il vetro. In testa va il corsivo, che è la
   faccia di adesso.
2. **Il bordeaux è campionato, non stimato**: `#73343E`, letto dai pixel più
   scuri del logo. Spento e polveroso, non un rosso saturo.

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

## Stato

`TODO` — esito di `controlla-sito.py` e `controlla-slop.py`, indirizzo Netlify,
verdetto di Nicola.

## Collegamenti

[[design-capelli]] · [[processo-siti]] · [[direttive-siti]] · [[anti-slop-siti]]
· [[netlify]] · [[registro-interventi]]
