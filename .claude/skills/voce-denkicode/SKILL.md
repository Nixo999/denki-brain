---
name: voce-denkicode
description: Impone la voce DenkiCode su ogni testo diretto a un cliente o lead — messaggi WhatsApp, DM Instagram, email, copy di siti vetrina. Da usare ogni volta che si scrive un testo che un cliente leggerà, prima di mostrarlo: elimina i tell da AI (em dash, elenchi da tre, connettivi logici da saggio, frasi-cuscinetto, ritmo troppo regolare) che fanno riconoscere il testo come generato da un LLM invece che scritto da chi vende. Non riguarda come Trevis parla a Nicola o Patrick — per quello vale registro-trevis.
---

# Voce DenkiCode — perché esiste

Nata il 6 settembre 2026: un lead (angolorelax_nembro) ha risposto a un
messaggio scritto da Claude per Patrick dicendo, testuale: *"è un banale copy
poco professionale per chatGPT... leva le em dashes che ti fanno sgamare
all'istante"*. Aveva ragione su due cose distinte: il tono e il carattere
tipografico. Trattativa persa sulla forma, non sul prezzo.

**Prima versione insufficiente.** Tolto l'em dash dai template il 6 settembre,
il primo messaggio di prova per un lead-barbiere è stato bocciato di nuovo:
«ancora non ci siamo». L'em dash era il tell più visibile, non l'unico. Sotto
c'è tutta una cadenza — elenchi di tre, connettivi da tema scolastico, frasi
tutte della stessa lunghezza — che un umano che scrive di fretta non produce
mai, e che nessuna blacklist di singole parole cattura da sola. Le regole qui
sotto vengono da una ricerca su cosa distingue davvero un testo AI da uno
umano, non solo dall'esempio di Nembro. Fonti in fondo al file.

## Prima di scrivere

1. `02-Sales/processo/stile-comunicazione.md` — tono DenkiCode: diretto,
   giovane, problem-solving, no fuffa; voce di **Patrick**, non di Nicola;
   Lei/Tu per fase.
2. Lessico obbligatorio (vincolo fiscale, non stilistico): ricevuta non
   fattura, collaborazione occasionale non fornitura, quota annuale non
   canone.

Questa skill non sostituisce quel file: aggiunge la parte che oggi manca, la
blacklist dei pattern che tradiscono un testo generato.

## La blacklist — motivo per motivo

| Vietato | Perché tradisce | Al suo posto |
|---|---|---|
| Em dash (—) | Il tell più riconoscibile: il lead di Nembro l'ha nominato per primo | Punto, virgola, a capo |
| **Qualunque elenco di tre**, non solo aggettivi — tre verbi, tre frasi, tre bisogni ("non deve scrivere testi, non deve mandarmi materiale, non deve decidere niente") | È il formato di risposta più tipico dei chatbot: tre voci, ritmo da diapositiva. Vale anche quando le tre voci sono vere | Due voci, o una frase sola che dice la stessa cosa senza contarle |
| Connettivi logici da tema ("quindi", "perciò", "dunque", "inoltre", "di conseguenza") | Un testo umano non annuncia la propria logica: la applica e basta | Si taglia il connettivo, le due frasi restano vicine o diventano una |
| Aggettivi ombrello usati come riempitivo ("soluzioni", "innovativo", "su misura", "professionale") | Non dicono niente: toglili e il messaggio non perde senso | Il fatto specifico che l'aggettivo voleva riassumere |
| Apertura a domanda retorica ("Hai mai pensato a...", "Sai che...") | Struttura da copy pubblicitario, riconoscibile a colpo d'occhio | Si parte dal fatto o dall'offerta |
| Frasi-cuscinetto ("Capisco perfettamente", "Fantastica domanda", "Sono qui per aiutarti") | Riempiono senza informare, un venditore vero non le scrive | Si taglia, si passa al punto |
| Frasi tutte della stessa lunghezza e cadenza | I modelli scrivono a soggetto-verbo-oggetto con ritmo costante: è la firma più difficile da vedere perché nessuna singola frase è sbagliata | Alternare una frase lunga a una cortissima, anche di due parole |
| Frasi lunghe tenute insieme da "e" ripetuti, invece che spezzate | L'AI usa meno punti, virgole e parentesi di un umano e allunga con "e": un umano che scrive in fretta va a capo prima | Punto. Frase nuova |
| `**grassetto**` o markdown nel testo che parte davvero | Instagram e WhatsApp non lo interpretano: arrivano gli asterischi veri, ed è un segnale tecnico oltre che stilistico | Il grassetto resta solo nelle note interne (i placeholder `[GANCIO]`), mai nel testo copiato per l'invio |

**Eccezione dichiarata: il contrasto-ancora non è un elenco di tre.** «Poche
centinaia di euro, non di migliaia, più una quota annuale» è tre pezzi ma è
una tecnica di prezzo (Hormozi/Michalowicz, [[core-crescita-finanze]]), non
un ritmo decorativo: resta. La differenza è se le tre voci **fanno un
lavoro** — un contrasto, un numero — o se **contano cose** solo per
completezza, come i tre «non deve».

## Un fatto prima dell'aggettivo

Non "un sito professionale e moderno", ma "un sito che carica in 2 secondi e
si aggiorna da telefono". Il numero o il fatto viene prima, il giudizio dopo
o non c'è.

## Come scrive davvero chi vende da telefono

Un DM o un WhatsApp vero è scritto in fretta: frasi corte, qualche minuscola
dopo un punto, punteggiatura imperfetta. Non è sciatteria voluta: è l'opposto
della forma pulita che un LLM produce di default. Non vale per le email
formali o il PDF dei gestionali, dove il registro resta pulito — lì il tell
non è lo stile informale, resta comunque la blacklist sopra.

## Dove si applica

- Ogni messaggio diretto: WhatsApp, DM Instagram, email — insieme a
  `proposta-commerciale` quando il testo è un preventivo.
- Il copy testuale dei siti vetrina (titoli, sezioni, CTA) — dentro
  `processo-siti`, passaggio "Finish review": quel detector guarda il layout,
  non le parole. Le parole le controlla questa skill.

## Self-check, prima di mostrare il testo

Non si consegna un testo cliente senza questa scansione, riga per riga:

- [ ] Zero em dash
- [ ] Zero elenchi di tre che contano invece di lavorare (i contrasti-ancora sui prezzi restano)
- [ ] Zero connettivi da tema ("quindi", "perciò", "dunque", "inoltre")
- [ ] Zero apertura a domanda
- [ ] Zero frasi-cuscinetto
- [ ] Le frasi non hanno tutte la stessa lunghezza: c'è almeno una frase molto
      corta
- [ ] Nessuna frase tenuta insieme da due o più "e": si può spezzare in due?
- [ ] Zero asterischi o markdown nel testo pronto per l'invio
- [ ] Il primo elemento di ogni paragrafo è un fatto, non un aggettivo
- [ ] Riletto ad alta voce: suona come parlerebbe Patrick, o come
      risponderebbe un assistente?

Se anche un solo punto fallisce, si riscrive prima di mostrarlo. Non basta
guardare le parole vietate una per una: il tell più difficile da vedere è il
ritmo — quando è tutto troppo bilanciato, è sbagliato anche se ogni singola
frase è pulita.

## Sempre

- Voce di Patrick, mai di Nicola, salvo il caso tecnico previsto da
  `stile-comunicazione.md`
- Non tocca `registro-trevis`: quello resta il modo in cui si parla a Nicola
  e Patrick, non ai clienti
- Il testo generato resta `source: claude` finché una persona non lo rilegge

## Fonti — ricerca del 6 settembre 2026

Le voci nuove della blacklist (elenchi di tre, connettivi da tema, ritmo
troppo regolare, frasi tenute insieme da "e") vengono da qui, non da un solo
esempio:

- [Come scrive l'AI? I "tic linguistici" che svelano i bot](https://blog.register.it/come-scrive-lai-i-tic-linguistici-che-svelano-i-bot/) — elenchi da tre voci, connettivi logici in eccesso, meno virgole e più "e" rispetto a un umano
- [Come riconoscere un testo scritto con ChatGPT](https://www.studiocataldi.it/articoli/48141-come-riconoscere-un-testo-scritto-con-chatgpt.asp)
- [Si può riconoscere un testo scritto dall'intelligenza artificiale? (Il Post)](https://www.ilpost.it/2026/03/30/scoprire-chi-scrive-con-chatgpt/)
- [Em dash: il più grande omaggio alla scrittura AI è cambiato (Dataconomy)](https://it.dataconomy.com/2026/08/04/em-dash-il-piu-grande-omaggio-alla-scrittura-tramite-intelligenza-artificiale-e-cambiato/) — anche i modelli più recenti stanno riducendo i trattini: è un tell in via di scadenza, la cadenza sotto non lo è
- [25 Instagram DM examples (Jotform)](https://www.jotform.com/ai/instagram-dm-template/) e [Instagram cold DM outreach guide (Fuel Your Digital)](https://fuelyourdigital.com/post/instagram-cold-dm-outreach-guide-free-template-step-by-step-guide/) — messaggi brevi, 2-3 paragrafi corti, niente vendita diretta al primo rigo
