---
type: progetto
riga: Bozza di sito per la Gelateria L'Ape Regina (Calcinato, BS). Giro 1 del 23/10 col mondo «Prima l'ingrediente»: crema in shader all'avvio, cartellini del banco, binario delle stagioni, esagono; Astro con GSAP.
updated: 2026-10-23
source: claude
verificato: 2026-10-23
status: attivo
client: laperegina
stack: Astro 5 con isole React, GSAP ScrollTrigger e SplitText, Lenis da computer, shader WebGL da shader-glsl, Netlify
started: 2026-10-23
deadline: TODO
---

# Sito L'Ape Regina

Bozza di sito vetrina per la Gelateria L'Ape Regina, chiesta da Nicola il 23/10/2026 dopo la risposta al DM: «dobbiamo fare il sito per questa gelateria, deve essere impattante e creativo, animazione all'avvio, e animato bene». Cliente: [[laperegina]].

**Cartella**: `~/lavoro/laperegina-site` (git locale su `main`, nessun remote ancora).
**Online**: TODO (il giro 1 è in costruzione mentre scrivo).

## Chi è

Gelateria L'Ape Regina S.r.l., via Rovadino 20, 25011 Calcinato (BS), aperta nel 2015. Gelato artigianale a produzione giornaliera con ingredienti di stagione e di origine dichiarata, torte gelato e semifreddi, dolci da forno caserecci, miele delle loro api e marmellate; anche gluten free e vegan. Consegna a domicilio (ordini entro le 14 da martedì a venerdì, entro le 11 sabato e domenica) e carretto dei gelati per gli eventi. Instagram @gelaterialaperegina (3.871 follower, 676 post), Facebook (2.609 follower), pagina link `zaap.bio/laperegina`. Google Maps 4,8 su 632 recensioni, Tripadvisor 5,0 su 104, Facebook 100% positive su 96. Telefono e WhatsApp 340 372 6622, mail gelaterialaperegina@gmail.com. Orari (zaap.bio): lunedì chiuso, martedì-giovedì 15-22, venerdì 15-22.30, sabato 11-13 e 15-22.30, domenica 11-13 e 15-22; Maps dice orari diversi di sera, da chiarire. Una recensione dice che d'inverno chiudono: non confermato.

Verificato il 23/10/2026 da Trevis sul profilo Instagram, su zaap.bio e sulla scheda Maps letta tramite Wanderlog; le didascalie, le recensioni e le foto le ha raccolte un operatore Sonnet dalle pagine vere (stanno in `riferimenti/` del repo, fuori da git).

## Le sue parole

Dalle dodici didascalie visibili senza login, alla lettera:

1. «Prima ancora della gelateria, ci sono state le api, il miele, il rispetto per i ritmi della vita e la voglia di trasformare ingredienti veri in qualcosa di buono da condividere.» (reel del 14/05/2026)
2. «Per noi creare gelato è rispettare gli ingredienti, la stagionalità e la natura.» (stesso reel)
3. «Crediamo che ogni materia prima di eccellenza abbia una propria identità e che il nostro compito è valorizzarla senza alterarne l'essenza» (post della mandorla, 8/10)
4. «Prima lo prepariamo. Poi lo trasformiamo in gelato.» (reel dello strudel, 15/10)
5. «L'Italia non è solo bella, è anche buona.» (formula dei post sui gusti con un'origine)
6. Bio: «Dal 2015 trasformiamo ingredienti di stagione in gelato gourmet d'eccellenza | Gelato artigianale | Torte | Dolci | anche gluten free e vegan».

Gusti con l'origine: noce della Contea di Gavello, liquirizia di Calabria, mandorla cruda della Val di Noto, yogurt di Vipiteno, nocciola del Piemonte, vaniglia del Madagascar; di stagione: zucca, strudel, la «frutta realistica estiva»; sui cartellini del banco: zabaione, crema dell'Ape Regina, pan di zenzero, fiordilatte, Biscottò; citati dai clienti: pane, camomilla, cacio e pepe, tiglio, fieno, Cremino Torinese, sambuco con un agrume.

## La personalità

Parlano da artigiani istruiti: frasi complete da etichetta di prodotto, del tu al cliente, mai urlato. Le parole che tornano sono ingredienti, materia prima, stagionalità, natura, eccellenza, valorizzare, cremoso, avvolgente. La bandiera è l'ape: prima della gelateria c'erano le api e il miele. Ogni post sui gusti ha lo stesso schema: la coppetta con il logo su un fondo a tinta unita, poi un collage con l'ingrediente, la pianta e il luogo d'origine. Il titolare risponde a ogni recensione con «La ringraziamo» e il rimando ai «prossimi gusti».

## L'identità visiva

Logo: un'ape stilizzata con la corona, il corpo è un nastro ritorto oro `#ECC428` e antracite `#3C3C3C` dentro una goccia a contorno; sotto, «l'ape regina» in corsivo calligrafico. Locale: pareti sabbia e una senape, bancone in legno chiaro, lavagna nera con il logo a gessetto, apertura esagonale «GELATERIA» sulla parete di fondo, pozzetti aperti in acciaio con i cartellini dei gusti scritti a mano; terrazza in pietra con sedie verde menta e luci a festone. Foto buone: 11 da Instagram (1080×1350 e 1440×1920) e 9 da Maps (fino a 2400 px); il logo solo come foto profilo a 1080 px.

## Il giro 1 (23/10/2026): «Prima l'ingrediente»

La direzione l'ha scritta Trevis (Fable) in `direzione/DIREZIONE.md` dopo aver guardato Fiftynine e Snia a 375 px; costruzione su tre operatori in parallelo con un contratto di DOM (`direzione/contratto.md`): «pagina» (Opus) HTML, CSS e testi; «motion» (Opus) i quattro moduli `crema.js`, `apertura.js`, `spina.js`, `scorrimento.js`; «foto» (Sonnet) i ritagli in `assets/img/`. Prima, in parallelo: concorrenti su Sonnet ([[competitor-siti-gelaterie]]), raccolta su Sonnet, scheletro Astro copiato da [[sito-mybalance]], riassunto delle skill in `direzione/skill-digest.md`.

- **Metafora**: il loro modo di lavorare, prima l'ingrediente con il suo luogo e poi il gelato; i cartellini scritti a mano sui pozzetti sono l'oggetto vero del mestiere.
- **Apertura** (1,8 s, a ogni caricamento): lo schermo pieno di «crema», un fragment shader con domain warping preso dalla skill `shader-glsl` (WebGL nudo, 1,4 KB) nei colori avorio, miele e nocciola; «L'Ape Regina» entra con SplitText mentre gli assi SOFT e WONK di Fraunces si rapprendono; poi la crema rallenta e resta sfondo dell'hero.
- **Spina**: il banco (i cartellini scorrono di lato con un pin corto da computer, carosello nativo sul telefono), la stagione (binario dell'anno con il campo di colore che cambia in scrub), dalle api (un esagono in `clip-path` si apre sulla foto dell'interno). Nessun disegno a mano: shader, tipografia variabile, forma esagonale, cartellini.
- **Palette**: avorio `#F6F0E4`, sabbia `#EADFC9`, nocciola `#C9A27C`, miele `#ECC428` (accento unico), antracite `#3C3C3C` una sola volta per le recensioni.
- **Font**: Fraunces (titoli, assi per l'apertura), Hanken Grotesk (testo), Caveat solo sui cartellini.
- **Skill cercate e installate** il 23/10 con `npx skills find` su dieci parole chiave, tenute solo quelle con più di mille installazioni: `awwwards-animations`, `cinematic-scroll-storytelling`, `cinematic-gsap-lenis-motion-system`, `shader-glsl`, `threejs-animation`, `animation-performance`, `animated-component-libraries` ([[design-frontend]]). Per «gelato» e «sito di ristorazione» non esiste nessuna skill.
- **Lasciato fuori**: la figura del carretto dei gelati con `anatomy` (70-85 parti, 1-2 ore), possibile al giro 2.

## Da chiedere nel DM

Prezzi di coppette, vaschette e torte; con quanto anticipo si ordina una torta; nomi dei titolari e se vogliono comparire; quali orari valgono (zaap.bio o Maps) e se chiudono d'inverno; il logo in vettoriale; foto e video del carretto; come funziona la consegna (link, pagamento); la storia delle api (dove sono, quanto miele, se si vende); cosa sono le storie «Natura Km0», «nazionale» e «edizionelimitata»; quali gusti sono gluten free e vegan; permesso per usare le foto di Instagram e di Maps.

## Collegamenti

[[laperegina]] · [[processo-siti]] · [[competitor-siti-gelaterie]] · [[direttive-siti]] · [[design-frontend]] · [[sito-mybalance]]
