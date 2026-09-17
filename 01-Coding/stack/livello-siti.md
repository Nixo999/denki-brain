---
type: risorsa
riga: Le costanti visive dei siti premiati del settore, lette nei loro sorgenti il 17/09/2026 - rapporti, misure, palette. Il metro con cui si giudica un sito nuovo.
updated: 2026-09-17
source: claude
verificato: 2026-09-17
tags: [siti, design, tipografia, ricerca]
---

# Il livello, in numeri

Nicola, 17/09/2026: «voglio che crei il sito più bello, significativo e unico
che riesci a fare. fai una ricerca dei competitor di settore e prendi spunto dai
migliori siti». Sono stati aperti **27 siti** e letti **i sorgenti veri** — HTML
e fogli di stile, non le schermate: famiglie di font, misure, tracking, hex,
librerie e conteggi vengono da lì. Restano fuori due cose che dal sorgente non
si vedono: se una foto è in bianco e nero (si legge solo un `grayscale` imposto
in CSS) e il movimento vero, ricavato da librerie e `@keyframes`.

Premiati letti: [Hagi's](https://hagisbarbering.com) (Awwwards SOTD),
[Rendezvous](https://www.myrendezvous.ca), [Monolith
Studio](https://monolithstudio.com) (SOTD + FWA + CSSDA),
[Pankhurst](https://pankhurstlondon.com), [Blind
Barber](https://www.blindbarber.com), [Barber Surgeons
Guild](https://barbersurgeonsguild.com), [Antica Barbieria
Colla](https://www.anticabarbieriacolla.com). Fuori settore, dove il livello è
più alto: [Rexhep Rexhepi](https://www.rexheprexhepi.com),
[Voutilainen](https://www.voutilainen.ch), [Anderson &
Sheppard](https://www.anderson-sheppard.co.uk),
[NOMOS](https://nomos-glashuette.com/en), [Ardbeg](https://www.ardbeg.com/en-gb),
[Liverano](https://liverano.com), [Coltellerie Berti](https://coltellerieberti.it).

## Le otto costanti

1. **Rapporto titolo grande / corpo ≥ 8:1.** Pankhurst 72-120 px su 12 (10:1),
   Hagi's 150 su 11 (13:1), Rendezvous 340 su 16 (21:1). I mediocri stanno a
   1,5-3,7:1 — Fellow Barber 24/16, No.95 42/16, Antica Colla 60/16.
2. **Titoli in `vw` o `clamp`, interlinea ≤ 1.** `clamp(4.5rem,12vw,7.5rem)`,
   10,42vw, interlinea 80%, fino a 0,7. I mediocri: px fissi e interlinea 1,2-1,4.
3. **Tracking negativo sui grandi, positivo sui piccoli.** -0,02/-0,05em sui
   titoli; le etichette 11-14 px maiuscole con +0,03 fino a +0,2em. Mai tracking
   su un titolo minuscolo da 40 px.
4. **Una o due famiglie; se una, tre tagli.** Monument Grotesk Regular/Medium/
   Semi-Mono, Gotham + Narrow + Tabular, SK Modernist + Mono. I mediocri ne
   caricano 5-7 e ne usano due a caso.
5. **Due neutri caldi e un accento, l'accento sotto il 5% della pagina.**
   #151515/#fffded, #010101/#f1f1f1/#e0e0e0, #111/#f1f1ef. **Nessuno usa il
   bianco puro come fondo**, se non i negozi. L'accento sta su un elemento solo.
6. **Poche foto, rapporto fisso, una sola sopra la piega.** Hagi's 14 tutte a
   3:4, Voutilainen 1, Anderson & Sheppard 5. I mediocri 45-83 in tagli casuali.
7. **Sei-dieci blocchi, titoli nominali di una o due parole, un dato per
   blocco.** «Artists», «Locations», «Ateliers», «Dove siamo», «DAL 1895».
8. **I numeri sono titoli.** «Est 1906», «FIRENZE 1948», «over 70 hours»,
   «1 Hour 30 Minutes £65», gli orari a 7rem, l'ora locale in testata. Un anno,
   un prezzo o una durata reggono una sezione da soli.

**Sul movimento**: nei premiati ci sono **1-3 `@keyframes` in tutto** e un solo
effetto proprietario. I temi mediocri ne portano 30-80 senza deciderne nessuno.

## Le cinque cose che fanno tutti i mediocri

1. **Hero uguale slider** (3-4 slide, «Précédent 0/0 Suivant», «skip carousel»),
   o titolo con due bottoni sotto.
2. **Servizi uguale tre o quattro card con icona.** Nessuno dei premiati ha
   un'icona.
3. **Font e colori lasciati dal tema** — il blu di default usato 57 volte, sei
   famiglie caricate e due usate.
4. **Rosso, nero, bianco più la fascia promozionale.**
5. **Testo al posto della pagina**: parole chiave in fila, feed Instagram con
   didascalie da 400 caratteri, sei articoli generati in home.

## Tre strutture che quasi nessuno usa

- **La home a due porte, senza hero.** Anderson & Sheppard («Bespoke Tailoring /
  Haberdashery»), Voutilainen, Barber Surgeons Guild («Barbershop / Hair
  Restoration»). Risolve due mestieri sotto un nome senza mescolarli. È quella
  scelta per [[sito-barbershop-snia]].
- **L'orario come pezzo grafico**, quando l'orario è raro.
- **La pagina che finisce con un solo link enorme**, al posto del footer a
  quattro colonne.

## Collegamenti

[[anti-slop-siti]] · [[direttive-siti]] · [[processo-siti]] · [[sito-barbershop-snia]]
