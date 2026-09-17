---
type: risorsa
riga: Cosa fa sembrare un sito fatto con l'AI, dalla ricerca del 17/09/2026 - segni visivi e di testo, cosa blocca controlla-slop, cosa va guardato.
updated: 2026-09-17
source: claude
tags: [siti, anti-slop, controlli, copy, design]
---

# Anti-slop sui siti — il metro dei controlli

Nicola, 17/09/2026: «fai una ricerca approfondita su internet di cosa serve per
annullare l'AI slop sui siti, e tutti i metodi per far sembrare che un sito non sia
fatto dall'AI, usa poi quei risultati come base per controllare i siti futuri».
La regola sta in [[direttive-siti]]. Lo strumento è
`python3 01-Coding/strumenti/controlla-slop.py <cartella>`, e sta al passo 5-bis di
[[processo-siti]] accanto a `controlla-sito.py`.

⚠️ Nota `source: claude` senza `verificato:`: le fonti sono quelle raccolte il
17/09 da quattro ricerche, lette dagli agenti e non riaperte una per una.

## Il principio

I modelli scelgono quello che nei dati è più comune: Inter, sfumature viola su
bianco, poca motion. Le liste di divieto creano nuovi default: il prompt di
Anthropic del 2025 consigliava Space Grotesk, Fraunces e Bricolage Grotesque, e
oggi stanno tutti nelle liste dei rilevatori. **Quindi le scelte vengono dal
cliente e dal mestiere, mai da una lista di sostituti.** Fonti:
[Anthropic](https://claude.com/blog/improving-frontend-design-through-skills),
[impeccable](https://github.com/pbakaus/impeccable/blob/main/crates/live/assets/antipatterns.json),
[Krebs](https://github.com/AdrianKrebs/ai-design-checker).

Chi sospetta un testo fatto con l'AI gli toglie fiducia anche quando l'ha
scritto una persona: -48% di fiducia e -14% d'intenzione d'acquisto
([Raptive](https://raptive.com/blog/the-ai-stink-is-real-and-its-costing-brands/)).

## Cosa blocca `controlla-slop.py`

Le fonti concordano e le nostre regole lo vietavano già.

| Segno | Da dove |
|---|---|
| Trattino lungo nel testo, anche uno solo | [[voce-denkicode]]; umani 3,23 ogni mille parole, GPT-4.1 10,62 ([arXiv](https://arxiv.org/abs/2603.27006)) |
| «Non è X, è Y» e «non solo X, ma anche Y» | fino a 6,3 volte la frequenza umana ([arXiv](https://arxiv.org/abs/2510.15061)); firma del copy turistico generato ([Officina Turistica](https://www.officinaturistica.com/2026/05/non-e-un-hotel-e-unesperienza-stop/)). Le citazioni del cliente fra « » non contano |
| Frase che apre con Inoltre, Perciò, Dunque, Quindi, Di conseguenza, Insomma | [[voce-denkicode]], [Il Post](https://www.ilpost.it/2026/03/30/scoprire-chi-scrive-con-chatgpt/) |
| Frasi fatte: «nel cuore di», «a 360 gradi», «soluzioni su misura», «esperienza unica» e altre trenta | ricerca del 17/09, lista A |
| Segnaposto, lorem ipsum, «Your Company», immagini da picsum o unsplash | [taste-skill](https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/SKILL.md), [Slopdar](https://slopdar.com/) |
| Tracce del nostro lavoro in pagina: fonti, «da confermare», «qui trovi» | [[voce-denkicode]], il muro; direttiva del 14/09 |
| Emoji o glifi al posto delle icone | [craft-floor](https://github.com/pbakaus/impeccable/blob/main/.claude/skills/impeccable/reference/craft-floor.md) |
| Testo con sfumatura | craft-floor, Krebs |
| Tailwind dal CDN di prova | [Tailwind](https://tailwindcss.com/docs/installation/play-cdn) |

NG Barber e Fiftynine sono più vecchi della voce DenkiCode: oggi i loro trattini
lunghi bloccano. Il metro resta la loro grafica, non il loro copy.

## Cosa avvisa

Si guarda e si decide: può essere una scelta giusta del cliente.

- **Testo.** Parole da densità («davvero», «passione», «eccellenza», «qualità»,
  «su misura»); superlativi; quattro o più gruppi di tre; ritmo piatto, cioè
  variazione della lunghezza delle frasi sotto 0,40 (testi generati 0,31, umani
  0,47, [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13350967/)); articoli e
  preposizioni con la maiuscola nei titoli; mesi e giorni maiuscoli a metà frase
  ([Treccani](https://www.treccani.it/enciclopedia/maiuscole-prontuario_(Enciclopedia-dell'Italiano)/));
  «**Titolo:** testo» negli elenchi; virgolette miste; sezioni senza un fatto
  verificabile, perché il testo concreto vende di più
  ([JCR](https://academic.oup.com/jcr/article/47/5/787/5873524)).
- **Grafica.** Occhiello sopra il titolo; una parola del titolo in corsivo o di
  un altro colore; font abusati (Inter, Roboto, Geist, Manrope, Syne, Sora,
  Space Grotesk, Fraunces, Bricolage Grotesque e altri) se non vengono dal
  cliente; viola e indaco; crema #F4F1EA con terracotta #D97757; aloni colorati;
  macchie sfocate; vetro sfocato ripetuto; striscia colorata sul lato dei
  blocchi; ombre dure; easing che rimbalza; zoom sulle foto; superfici del
  browser non disegnate.
- **Pagina.** Anno vecchio nel footer, favicon e og:image mancanti, link a `#`.
- **impeccable detect**, 61 regole fisse: severo anche con NG Barber (10
  segnalazioni), quindi solo avviso.

## Cosa si guarda con gli occhi

Nessuno script lo prende bene:
- l'hero centrato con due bottoni, uno pieno e uno vuoto;
- tre card uguali con icona sopra, e le griglie bento;
- l'ordine fisso hero, servizi, testimonianze, prezzi, contatti;
- recensioni inventate, caroselli senza motivo;
- la stessa entrata dal basso su ogni sezione: un momento d'autore, non uno
  effetto ovunque ([Anthropic skill](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md));
- la spaziatura tutta uguale;
- foto di stock o generate: le foto vere del posto, del titolare e del lavoro
  valgono più di tutto. Con la foto del titolare il 46% si fidava, con una foto
  generica il 33% ([BrightLocal](https://www.brightlocal.com/research/images-inspire-trust-local-business-website/)).

## Cosa fa scegliere un'attività locale

Informazioni complete con gli orari 32%, recensioni 30%, prezzi chiari 29%
([BrightLocal](https://www.brightlocal.com/research/consumer-search-behavior-decisions/)).
Il 74% guarda le recensioni degli ultimi tre mesi
([BrightLocal](https://www.brightlocal.com/research/local-consumer-review-survey/)).
Google non penalizza l'AI in sé, ma le pagine fatte in serie senza valore
([Google](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)).

## Collegamenti

[[direttive-siti]] · [[processo-siti]] · [[voce-denkicode]] · [[denki-agents]]
