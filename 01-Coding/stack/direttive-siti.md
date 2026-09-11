---
type: risorsa
riga: Ogni correzione che Nicola ha dato su un sito, diventata regola permanente. Si legge prima di costruire e prima di pubblicare.
updated: 2026-09-11
verificato: 2026-09-11
source: denkicode
tags: [siti, design, direttive, qualita]
---

# Direttive sui siti — quello che è già stato bocciato

**Questo file cresce e non si accorcia.** Ogni volta che una bozza viene
bocciata, la frase esatta entra qui insieme alla regola che ne esce. Un sito
nuovo non può ripetere niente di quello che c'è scritto sotto: è il meccanismo
per cui i siti migliorano invece di oscillare.

Si legge **due volte**: dall'operatore di direzione prima di proporre i mondi, e
dall'operatore di costruzione prima di dire che ha finito. Il controllo
meccanico è `01-Coding/strumenti/controlla-sito.py`, ma quello misura solo ciò
che si può contare. Qui c'è il resto.

⚠️ Le frasi fra virgolette sono di Nicola, verbatim. Non si ammorbidiscono.

## Il metro

**NG Barber e Fiftynine passano, gli altri no.** Sono gli unici due approvati
senza riserve, e li ha fatti un processo che non aveva brief: chi leggeva il
cliente e chi inventava erano la stessa testa. Se una bozza non regge accanto a
quelle due, non è pronta.

## Le direttive, dalla più recente


### 11/09/2026 — «sembra che non usi più le skill nel modo di prima»

Tre operatori su sette non avevano caricato niente. **Nessun giro tocca la UI
senza `impeccable context` e `craft-floor`.** Un giro di sola correzione copy è
l'unica eccezione, e si dichiara.

### 11/09/2026 — «per NG Barber non gli ho detto niente e ha fatto un sito bellissimo»

La direzione non si decide prima di aver letto le skill di design. L'operatore
di direzione torna con due o tre mondi, il direttore sceglie.

### 10-11/09/2026, Mikuma — «fa schifo, sembra fatto da un bambino di due anni»

Bocciati: acqua a righe generata, foto dentro cornici da widget, hero da
template. Ne escono tre regole:

- **Niente materiali finti generati in CSS.** «Sembra finta, non stare a
  generare acqua finta.» Acqua, legno, marmo, fumo: o è una foto vera o è un
  segno grafico dichiaratamente astratto, mai una imitazione.
- **Niente foto in cornicette.** Una foto o riempie il suo spazio o sta in una
  griglia dichiarata. Quattro foto a quattro rapporti e quattro altezze diverse
  leggono come disordine.
- **Niente hero da template.** Parola gigante, sottotitolo, bottone, vuoto: è
  la forma che esce da sola quando non c'è una direzione. Se l'hero si potrebbe
  mettere su un altro cliente cambiando la parola, è quello.

### 11/09/2026, Mikuma — «scrivi come un bambino»

Il copy va in frasi complete, con il verbo. Le didascalie dicono il servizio,
non ripetono il nome del file né le caption dei post. Passa da
`voce-denkicode` prima della review.

### 10/09/2026, Da Caterina v1 — «da telefono è orribile, i ritagli fanno pena, sembra tutto buttato a caso»

**Il mobile si guarda, non si deduce.** E i ritagli automatici dei soggetti
vanno guardati uno per uno: un contorno sbagliato si vede subito e squalifica
la pagina intera.

### 08/09/2026, Tarilli — «un sacco di animazioni», «pizze che si muovono e fluttuano»

Quando Nicola chiede movimento, ne chiede **tanto e visibile**. La dose
prudente è una sua lamentela ricorrente, non una virtù.

### 01-03/09/2026 — Castiglione v1 «il sito più piatto della storia», DSI v1 «sta venendo malissimo»

Le due prime versioni costruite con la sola `design-taste-frontend`. Da lì nasce
la catena: una sola skill non basta, e il passo di carattere
(`bolder`, `delight`, `animate`) non è opzionale.

### Sempre — l'identità del cliente vince sul nostro gusto

La versione notte di DSI era bella e sbagliata: era il gusto Denki, non il
loro. Se il cliente ha logo, colori e voce, quelli comandano.

## Come si aggiunge una direttiva

**Nel momento in cui viene detta**, non a fine sessione:

```bash
python3 01-Coding/strumenti/regola.py siti "la frase esatta" --chi nicola --perche "..."
```

Vale per una bocciatura **e per una preferenza detta a freddo**. Fino all'11
settembre 2026 il meccanismo era agganciato solo alla bocciatura e a
`/chiudi-sessione`: un «da adesso sui siti voglio sempre X» detto a metà
sessione non scattava, e si perdeva con la conversazione.

Non si riscrivono le vecchie: una direttiva superata si marca superata, non si
cancella. Questo file cresce e non si accorcia.

## Collegamenti

[[processo-siti]] · [[essenza-e-motion]] · [[trappole]] · [[convenzioni]]
