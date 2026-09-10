---
type: decisione
riga: Da adesso i siti si fanno con starter, essenza del cliente e metafora sola, e il direttore non scrive codice - lo scrive l'operatore su Opus.
data: 2026-09-10
progetto: azienda
source: denkicode
stato: presa
updated: 2026-09-10
verificato: 2026-09-10
---

# I siti si fanno con lo starter, una metafora sola e l'operatore su Opus

## Il contesto

Sedici repo di siti, ognuno partito da zero. Misurato: `netlify.toml` in 12 su
12, il reset `img{height:auto}` in 8 su 12, la firma **Powered by DenkiCode**
assente su Da Caterina e Osteria Tarilli, cioe' i due costruiti subito dopo la
decisione dell'8 settembre che la rendeva obbligatoria. La regola scritta e'
caduta sui primi due siti che l'hanno incontrata.

Costo per sito: ~17.500 parole di skill di design caricate prima della prima
riga di HTML, di cui 12.853 di `design-taste-frontend` da sola.

Nicola: «voglio siti originali, sempre un'animazione all'avvio, tante animazioni
particolari per far sembrare il sito vero, e voglio essere sorpreso come su NG
Barber e Fiftynine. E voglio il metodo direttore/operatore in automatico, con
Fable che dirige e non scrive codice, per sprecare meno Fable possibile».

## La decisione

1. **Lo starter**, `01-Coding/strumenti/starter-sito/`, copiato da
   `nuovo-sito.py`. Porta reset, `--vh`, `.cattura`, rivelazioni col fallback
   giusto, tre sbarramenti, cache che rivalida, firma nel footer. **Non porta
   gusto**: nessun colore, nessun font, nessuna sezione, o fra dodici siti ne
   escono dodici uguali.
2. **L'essenza del cliente si cava da Instagram e si scrive** prima di aprire
   una skill. Da li' esce **una metafora sola**, e se si potrebbe spostare su un
   altro cliente non e' quella giusta. Metodo e casi in [[essenza-e-motion]].
3. **L'apertura animata e' obbligatoria** su ogni sito, ed e' la metafora che
   entra in scena. Piu' quattro tipi di motion: una cosa che risponde a un dato
   vero, un ambiente lento in loop, **un solo** momento autoriale, le
   rivelazioni sfalsate.
4. **Il direttore non scrive codice.** Decide, scrive un brief da 40 righe,
   giudica, pubblica. L'agente `operatore` (Opus, `effort: high`) carica le
   skill di design nel **suo** contesto e riferisce in dieci righe. Il direttore
   puo' girare su Fable senza pagarne la catena.
5. **La classe della firma e' `firma-denkicode`**, non `firma`: quel nome era
   gia' preso su Atelier Selva. Corretto in [[convenzioni]].

## Cosa si e' scartato

Mettere una palette o una griglia di partenza nello starter: e' la scorciatoia
che produce il template. Riscrivere `design-taste-frontend`: e' di terze parti,
si sposta di contesto invece che di contenuto.

## Conseguenze aperte

Firma aggiunta e misurata su Da Caterina e Osteria Tarilli, **commit locale, non
ripubblicati**: il deploy e' una decisione del direttore. Gli altri quattordici
repo non sono stati verificati uno per uno. `processo-siti` e' anche in
`.claude/skills/` del vault, quindi versionata: prima era solo locale e
`source: claude`.

## Collegamenti

[[processo-siti]] · [[essenza-e-motion]] · [[convenzioni]] · [[trappole]]
