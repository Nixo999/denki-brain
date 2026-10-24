---
type: progetto
riga: Bozza sito Satatttvision (tatuatori, Milano). Giro 1 dal 24/10, mondo «La vetrina di via Tadino»: saracinesca, insegna disegnata, flash.
updated: 2026-10-24
source: claude
verificato: 2026-10-24
status: attivo
client: satatttvision
stack: Astro 5 con isole React, GSAP ScrollTrigger e SplitText, Lenis da computer, svg-animation per i tratti, anatomy per la figura, Netlify
started: 2026-10-24
deadline: TODO
---

# Sito Satatttvision

Bozza di sito vetrina per Satatttvision, chiesta da Nicola il 24/10/2026 dopo la risposta al DM: «ce da fare questo sito fatto molto bene, trova delle skills per farlo in maniera particolare e dargli la personalità giusta che prendi dal suo Instagram, usa delle skill per fare dei disegni da mettere nel sito rispettando il suo stile di tatuaggi. deve essere fatto molto bene sia da telefono che da pc, e animalo il giusto e fai una bella animazione all'avvio». Cliente: [[satatttvision]].

**Cartella**: `~/lavoro/satatttvision-site` (git locale, ramo `main`; repo GitHub `TODO`).
**Online**: `TODO` (Netlify, con i tre sbarramenti).

## Chi è

Studio di tatuaggi in via Alessandro Tadino 3, 20124 Milano (zona Porta Venezia), sull'insegna «SATATTTVISION MLN». Aperto dal lunedì al sabato dalle 11 alle 20; la domenica non è scritta. Instagram @satatttvision (49K follower, 2.532 post, bio «Tattoo studio Milanese / DM per Info/Appuntamenti/News»), Facebook 6.158 follower e 100% positive su 64 recensioni, Google 4,7 su 90 recensioni. Telefono 02 4953 0720, mail satatttvision@gmail.com. Nessun sito: il tumblr indicato su Facebook è morto.

Artisti letti dai post taggati (resident e guest non si distinguono da sloggati): @dima_tabu (fineline contemporaneo, anime, blast-over; Milano e Madrid), @francescavendola (fineline con architettura gotica, nuvolette, fiori), @carlottacawa (serpenti, collage, astratto; Milano e Palermo), @naelenina (freehand e blackwork, in tour), @guiltykid (blackwork), @didigemz (gemme dentali), e nel B2B della Flash Night del 9/10/2026 @hilie.sata.ttt, @labaratta_tattoo (Elisa, manga), @_mindshapes_, @worldwidenoza, @yurisatacooletters. Le recensioni nominano «Yuri» e «Davide»; sul neon della vetrina c'è la firma «Sata».

Verificato il 24/10/2026 da un operatore Sonnet sulle pagine vere (Instagram da sloggati, Facebook, Maps): didascalie, recensioni e foto stanno in `riferimenti/` del repo, fuori da git. Trevis ha visto la facciata, la locandina, il logo e tre foto dei lavori.

## Le sue parole

Un solo testo è dello studio (il post della Flash Night, 28/9/2026): «Siamo lieti di invitarvi alla nostra prima FLASH NIGHT il prossimo 9 ottobre!», «100 flash disponibili per essere tatuati», «First come first served. NO PRENOTAZIONE.». Bio: «Tattoo studio Milanese», «DM per Info/Appuntamenti/News». I guest scrivono in inglese: «Booking open», «DM for appointment», «Done at @satatttvision», «MILANO ♾️».

## L'identità visiva

Insegna nera con il nome in grotesque bold bianco e «MLN» spaziato sotto, senza simbolo; vetrine con strisce diagonali bianche e nere; neon blu `#3144BE` con la firma «Sata»; lampadine nude. Locandina della Flash Night: verde acido `#30EE15` su nero, lettering gotico, smiley, retino a puntini. I lavori: linee nere fini, blackwork a chiazze, nero e grigio denso; colore raro.

**Le foto non reggono il sito**: dal feed si arriva a 640 px, le otto di Facebook a 1440 sono fotogrammi di video (tre usabili come momenti del lavoro: stencil, guanti con la macchina, gemme dentali), la facciata di Maps a 1800×2400 è l'unica foto buona. Il tracciato vettoriale di un tatuaggio da 640 px (vtracer, `direzione/prove/`) non regge: linee spezzate. Il logo tracciato dalla copertina Facebook invece è pulito (`assets/logo-satatttvision.svg`, 16 tracciati).

## Il giro 1 (24/10/2026): «La vetrina di via Tadino»

La direzione l'ha scritta Trevis (Fable) in `direzione/DIREZIONE.md` dopo aver guardato Fiftynine, p0t e Snia a 375 px e lo specimen dei font (`direzione/font.html`, 20 font, fatto da un operatore Sonnet). Costruzione su quattro operatori in parallelo con un contratto di DOM (`direzione/contratto.md`): «pagina» (Opus) HTML, CSS e testi; «motion» (Opus) apertura, spina e i flash tipografici; «foto» (Sonnet) i ritagli in bianco e nero; «figura» (Opus) la macchina rotativa con `anatomy`. Prima, in parallelo su Sonnet: raccolta, ricerca delle skill (`direzione/skill-trovate.md`), scheletro Astro copiato da [[sito-laperegina]].

- **Metafora**: il loro negozio visto dalla strada, com'è davvero: insegna, strisce diagonali sul vetro, neon, più il verde acido e il gotico della locandina. Il sito è la vetrina che si apre alle 11.
- **Apertura** (1,8 s, a ogni caricamento): la saracinesca a strisce bianche e nere si alza, l'insegna vera (il logo tracciato) si disegna con un tratto verde lettera per lettera e poi si riempie di bianco (skill `svg-animation` e `logo-animation`), la riga neon blu si accende una volta, entrano frase, tasti e orario di oggi.
- **Spina**: dalla strada alla sedia. Chi tatua qui (schede degli artisti, carosello sul telefono), Flash (campo nero con il retino verde: «100 flash», «First come first served», «No prenotazione», e il muro dei flash tipografici: dieci parole in Grenze Gotisch 800 trasformate in tracciati a build con `fontkit` e disegnate dall'ago allo scroll, contorno e poi riempimento, più lo smiley della locandina), Dallo stencil alla macchina (i tre fotogrammi veri e la figura isometrica della macchina), Dicono (campo verde pieno con 4,7 su 90 e 100% su 64, tre citazioni), Via Tadino 3 (facciata, orari, contatti).
- **Palette**: nero `#0B0B0B`, carta `#F2F1EC`, bianco, verde acido `#30EE15` come accento unico, blu neon `#3144BE` una volta sola, grigio `#8E8E8A`. Nero e carta si alternano sezione per sezione.
- **Font**: l'insegna è il logo tracciato; Grenze Gotisch (variabile) per le parole grandi; Archivo (variabile, asse `wdth`) per titoli e testo; JetBrains Mono per le etichette. Scelti sullo specimen a 375 px: Grenze Gotisch 800 è il gotico più leggibile (nome largo 258 px a 56 px), Pirata One è la riserva.
- **Skill cercate e installate** il 24/10 (`direzione/skill-trovate.md`): `svg-animation` e `logo-animation` (iart-ai, 2,4 e 2,7 mila installazioni); scartate quelle per React/WebGPU e quelle sotto le mille. Nessuno strumento sul Mac genera immagini raster: le skill `imagegen-*`, `brandkit`, `image-to-code` presuppongono un generatore che qui non c'è.
- **Lasciato fuori**: i disegni dai loro tatuaggi (servono gli originali a 1080+ dagli artisti), la storia «Residents», prezzi e caparra.

## Com'è andata la verifica

`TODO`: si scrive a fine giro.

## Da chiedere allo studio

Chi è resident e chi guest; foto originali dei lavori a 1080+ e dell'interno; prezzi, caparra e tempi; la domenica; le prossime Flash Night; nomi dei titolari; il file vettoriale del logo; consenso per le foto degli artisti prese dai loro post.

## Collegamenti

[[satatttvision]] · [[processo-siti]] · [[direttive-siti]] · [[competitor-siti-tattoo]] · [[design-frontend]] · [[sito-laperegina]] · [[sito-p0t-tattoo]]
