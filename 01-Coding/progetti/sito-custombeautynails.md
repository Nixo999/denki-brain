---
type: progetto
riga: Custom Beauty Nails, onicotecnica a Treviglio (BG): bozza online su custombeautynails.netlify.app dal 16/9, mondo «Un centimetro di spazio», 21 SVG, 8/8.
status: attivo
client: custom-beauty-nails
stack: html-css-js
started: 2026-09-16
deadline:
updated: 2026-09-16
source: claude
verificato: 2026-09-16
tags: [sito, bozza, unghie, treviglio, bergamo]
---

# Sito Custom Beauty Nails — online, mondo «Un centimetro di spazio»

Bozza **non attesa**: il DM non è ancora partito, la costruzione è nata da uno
screenshot del profilo mandato da Nicola. Repo `~/lavoro/custombeautynails-site`,
dallo starter (`nuovo-sito.py`), **solo locale, nessun remote git**.

Online su <https://custombeautynails.netlify.app>, progetto `custombeautynails`
sul team `travis`, deploy dal CLI il 16 settembre 2026.

## Chi è, verificato il 16 settembre 2026

`@custombeautynailstreviglio`, `pk` 79006836739, categoria dichiarata
**Salute/bellezza**. **1.033 follower, 12 seguiti, 15 post** — la griglia
pubblica ne mostra 12, tutti fra il 3 e il 13 settembre 2026. Like fra 16 e 36,
**zero commenti su tutti e dodici**.

Bio, parola per parola:

```
💅  Nails
📍 Treviglio, Via Roma 21B
📲 Prenotazioni in DM o WhatsApp
3518692431 @mycustomshoes @mycustombarber
```

**Nessun link in bio, nessun sito.** Indirizzo **Via Roma 21B, Treviglio (BG)**,
telefono pubblico **351 869 2431**, dichiarati dall'API del profilo.

Fa parte di un gruppo **«Custom»**: `@mycustomshoes` e `@mycustombarber`. Se
condividano l'indirizzo **non è verificato** → `TODO`.

## Come si è letto il profilo

`web_profile_info` risponde ancora **429** e il feed della app **401**, ma il
`pk` si prende dall'HTML del profilo (`"profilePage_(\d+)"`) e
`/api/v1/users/{pk}/info/` con `x-ig-app-id` risponde in mezzo secondo.
Le didascalie stanno nell'`og:description` delle pagine dei post, prese in
parallelo dalla sessione loggata nel pannello. Vedi [[metodo-instagram]].

## Cosa fotografa

Sempre **mani in primo piano su un telo rosa acceso**, sfumato da `#FB73BB` a
`#F38EA0`: è il set fisso del suo tavolo, ed è dentro dieci scatti su dodici.
Le due eccezioni sono la mano che tiene l'iPhone su muro terracotta e la
stiletto cat-eye su rosa più spento.

**Watermark bianco del marchio in basso al centro su tutte e dodici.** Misurato
riga per riga sui pixel bianchi, la prima riga va dal **64,7%** (p10, p12) al
**76,3%** (p07, p09) dell'altezza: il taglio si fa file per file, non con un
numero solo.

Forme: mandorla, ballerina, stiletto. Decori: french, leopardato dipinto a mano,
cat-eye, ombré, foglia oro, strass, fiocchetti in rilievo, borchie.

## Le sue parole

«Unghie che non passano inosservate» (tre post su dodici) · «eleganza,
carattere e dettagli che fanno la differenza» · «super glossy» · «un tocco
wild» · «dal carattere deciso» · «per valorizzare le tue mani» · «Ti aspettiamo
da Custom Beauty» · «Prenota in DM».

Registro **glam, caldo, diretto, in seconda persona**. Non dice mai apex,
struttura, parallelismi: il contrario di [[sito-nails-robyy]].

## Il mondo scelto

**A «Un centimetro di spazio»**, scelto dal direttore sopra il B «La riga di
luce», che rilegava il rosa a colore di bottone su fondo nero: contro la
direttiva per cui l'identità del cliente vince sul nostro gusto. Il contratto
di direzione sta in `.impeccable/surfaces/index-html.md` nel repo.

La metafora è che il campo di lavoro è largo un centimetro. La spina dello
scroll è uno zoom che arretra, con un righello a sinistra che rinumera la
quota mentre si scende.

## Misurato il 16 settembre 2026

21 `<svg>` inline, 13 foto, `controlla-sito.py` **8/8**, overflow 0 e contrasti
AA su 16 larghezze da 320 a 1440, console pulita, pagina completa senza JS,
tocchi sopra 44 px, focus visibile. Tre sbarramenti verificati con `curl` sul
sito vivo, più i file di lavoro sbarrati con `force = true`.

## Aperto

- ⬜ **Badge «Powered by Netlify»** ancora acceso in basso a destra: `/.netlify/*`
  è riservato e nessun redirect lo ferma, si spegne dal pannello del progetto.
- ⬜ **Nessun remote git** per questo repo.
- ⬜ Il marchio del footer è un matte alpha derivato dal jpg, **non un `<svg>`
  tracciato**: per quello serve il file originale alla cliente.
- ⬜ Mai visto su un telefono fisico né su Safari iOS. Brave non è installato su
  questo Mac, `cattura-fette.mjs` gira solo puntato su Chrome.

## I dieci TODO da chiedere a lei

Nome della titolare · orari · prezzi e listino · durata di un appuntamento · se
Via Roma 21B è condivisa con `@mycustomshoes` e `@mycustombarber` · recensioni ·
il logo in vettoriale · foto senza watermark · se fa corsi · se lavora da sola.

## Collegamenti

[[custom-beauty-nails]] · [[processo-siti]] · [[direttive-siti]] · [[trappole]] ·
[[netlify]] · [[registro-interventi]]
