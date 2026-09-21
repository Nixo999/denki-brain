---
type: risorsa
riga: Regole verificabili per il testo dei siti: didascalie, leggibilità Gulpease, punteggiatura, SEO locale, microcopy, tutte con fonte.
updated: 2026-09-21
source: claude
tags: [copy, scrittura, web, ricerca]
---

# Testo dei siti: regole controllabili

Ricerca per la skill che chi scrive i siti vetrina applica a ogni pagina: regole con un numero o un criterio verificabile, non consigli generici. Nasce dal numero misurato sui 16 siti DenkiCode, 35 didascalie su 97 ripetono il testo alternativo dell'immagine (36%), e dalla bocciatura di Nicola del 21/09/2026: «sotto le foto hai scritto delle cose completamente inutili a uno spettatore del sito, tipo descrizioni della foto o titoletti completamente inutili» (dettaglio in [[direttive-siti]]).

## 1. Didascalie e testo attorno alle immagini

**Alt e figcaption hanno due pubblici diversi e non si scrivono uguali.** L'`alt` sostituisce l'immagine per chi non la vede, uno screen reader o un caricamento fallito: non è mai a video. La `figcaption` è contenuto visibile, letto da chi la foto la vede già, e dà all'elemento `figure` un nome accessibile: non sostituisce l'alt, gli convive accanto ([MDN, elemento figcaption](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption)). Scrivere la stessa frase in tutti e due i posti significa dire la stessa cosa a due pubblici diversi e sprecare uno dei due.

L'albero decisionale del W3C/WAI per l'alt distingue tre casi soltanto: vuoto se l'immagine è decorativa o il suo contenuto è già testo nelle vicinanze, descrittivo se l'immagine porta un significato che il testo attorno non dà, funzionale se l'immagine è un link o un bottone e l'alt deve dire dove porta ([W3C WAI, An alt Decision Tree](https://www.w3.org/WAI/tutorials/images/decision-tree/)). In nessuno dei tre casi l'alt esiste per raccontare la scena a chi la vede: esiste per sostituirla a chi non la vede.

Chi guarda una foto vede già il taglio, la texture, la posa: una didascalia che descrive quello che l'occhio ha già preso non aggiunge informazione, aggiunge solo rumore, ed è esattamente l'errore bocciato su Design Capelli, dove ogni foto aveva una riga come «Shag corto nero con frangia, dentro il salone», cioè l'alt ripetuto a video.

La differenza si vede in due righe reali: «Taglio scalato con frangia laterale» descrive quello che la foto già mostra, non regge; «Taglio scalato, 45 minuti, 28 euro» dice quello che la foto non può dire, regge. Vale lo stesso per occhielli e titoletti che ripetono il blocco che etichettano: se il titolo sopra dice già tutto quello che il testo sotto ripete, uno dei due si toglie.

Le guide di redazione dicono da prima del web che una didascalia deve andare oltre quello che l'immagine già mostra, non ripeterlo: «Do some reporting. Go beyond the information provided with the image», scrive Poynter, l'istituto di giornalismo americano, e la tiene corta, una o tre frasi, in forma attiva ([Poynter, Writing Effective Photo Captions](https://www.poynter.org/news/writing-effective-photo-captions)). Un'altra guida editoriale aggiunge la regola pratica opposta a quella sbagliata: non scrivere che qualcuno «è mostrato» o «guarda», puntare a un testo informativo, interessante, vivace, non alla parafrasi dell'immagine ([Get It Write, Caption dos and don'ts](https://getitwrite.ca/2016/03/09/caption-dos-and-donts/)).

Vale la pena scriverla bene perché viene letta: nell'eyetracking di NN/g, titoli, sommari e didascalie sono fra i primi elementi su cui cade lo sguardo quando si apre una pagina, il 78% delle prime fissazioni va sul testo contro il 22% sulle immagini ([NN/g, Eyetracking Study of Web Readers](https://www.nngroup.com/articles/eyetracking-study-of-web-readers/)). Una didascalia vuota di informazione non è neutra: occupa la prima attenzione che l'utente dà alla pagina, e non le restituisce niente.

**Quando una didascalia ha diritto di esistere**: solo se porta un dato che l'immagine e l'alt non dicono già, un prezzo, una durata, un nome proprio, una data, un materiale. Se non c'è quel dato, la riga sotto la foto non esiste.

**Regola controllabile da uno script**: una `figcaption` resta in pagina solo se, tolte le parole vuote (articoli, preposizioni, congiunzioni), condivide meno del 50% delle parole piene con l'`alt` della stessa immagine. Sopra quella soglia è una parafrasi e va tolta o riscritta con un'informazione che l'alt non ha.

## 2. Frasi e paragrafi

Un utente medio non legge una pagina, la scansiona: il 79% degli utenti scansiona sempre una pagina nuova, solo il 16% legge parola per parola ([NN/g, How Users Read on the Web](https://www.nngroup.com/articles/how-users-read-on-the-web/)). Sul tempo che passa in pagina, NN/g misura che si legge al massimo il 28% delle parole, più realisticamente il 20%, su una pagina media di 593 parole, e che si legge almeno metà del contenuto solo se la pagina sta sotto le 111 parole ([NN/g, How Little Do Users Read?](https://www.nngroup.com/articles/how-little-do-users-read/)).

Per l'italiano l'indice che misura la leggibilità è il Gulpease, tarato sulla lingua nostra e non sull'inglese come il Flesch: 89 + (300 × frasi - 10 × lettere) / parole, scala 0-100. Sotto 80 il testo è difficile per chi ha la licenza elementare, sotto 60 per chi ha la licenza media, sotto 40 per chi ha un diploma superiore ([Wikipedia, Indice Gulpease](https://it.wikipedia.org/wiki/Indice_Gulpease)): per un testo commerciale che deve leggere chiunque, il punto sotto cui non scendere è 60.

Un paragrafo porta un'idea sola: gli utenti che scansionano leggono la prima frase di un paragrafo e saltano il resto se non trovano lì l'informazione, quindi ogni idea in più nello stesso paragrafo viene ignorata ([NN/g, How Users Read on the Web](https://www.nngroup.com/articles/how-users-read-on-the-web/)). Non esiste, nella stessa fonte, un numero fisso di parole per paragrafo: la regola verificabile è quella, un'idea, non una lunghezza, e non lo si inventa qui.

La struttura che funziona è la piramide rovesciata, conclusione all'inizio e dettagli dopo, perché chi scansiona deve poter fermarsi alla prima riga e avere già il punto ([NN/g, Inverted Pyramid: Writing for Comprehension](https://www.nngroup.com/articles/inverted-pyramid/)), e lo sguardo si muove sulla pagina a F, due bande orizzontali in alto e poi giù sul margine sinistro: quello che conta va nelle prime due righe e a inizio riga, non in fondo al paragrafo ([NN/g, F-Shaped Pattern of Reading Web Content](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/)).

Riscrivere un testo promozionale in stile scannable, conciso e oggettivo non è un dettaglio di stile: nello studio Morkes/Nielsen la versione scannable misura il 47% in più di usabilità, quella concisa il 58% in più, quella oggettiva il 27% in più, le tre insieme il 124% in più ([NN/g, Concise, Scannable, and Objective](https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/)).

## 3. Punteggiatura italiana

La virgola in italiano non ha una sintassi rigida, il suo valore è comunicativo prima che grammaticale: segna una pausa debole fra parole o proposizioni, apre e chiude incisi (apposizioni, vocativi, elementi circostanziali inseriti), separa gli elementi di un elenco ([Treccani, Virgola](https://www.treccani.it/enciclopedia/virgola_%28Enciclopedia-dell%27Italiano%29/)). In un testo commerciale la si tiene per liste e incisi veri, non per spezzare una frase che si può dire intera.

I due punti introducono, non separano: annunciano una spiegazione, un elenco, una citazione, con funzione dichiarativa, presentativa, argomentativa ([Treccani, Due punti](https://www.treccani.it/enciclopedia/due-punti_%28Enciclopedia-dell%27Italiano%29/)). Il punto e virgola è il segno meno usato, resta proprio della scrittura curata e serve a separare, dentro un elenco, elementi già lunghi o già pieni di virgole al loro interno ([Treccani, Punto e virgola](https://www.treccani.it/enciclopedia/punto-e-virgola-uso-del-prontuario_%28Enciclopedia-dell%27Italiano%29/)): in una pagina vetrina, quasi mai necessario.

Trattino e lineetta non sono lo stesso segno: il trattino breve unisce, senza spazi prima e dopo ("macro-obiettivo"), la lineetta separa, con uno spazio prima e dopo, e sostituisce la virgola in un inciso quando la frase ha già troppe virgole ([Treccani, Trattino](https://www.treccani.it/enciclopedia/trattino_%28Enciclopedia-dell%27Italiano%29/)). I puntini di sospensione, sempre tre, segnalano un discorso sospeso per reticenza o allusione, e fuori dalla narrativa il loro uso "brillante" annuncia un gioco di parole ([Treccani, Puntini](https://www.treccani.it/enciclopedia/puntini_%28Enciclopedia-dell%27Italiano%29/)): in un sito vetrina quell'effetto legge come indecisione, non come stile, e si evita.

Il punto esclamativo va usato con moderazione: l'italiano contemporaneo lo considera incompatibile con un tono oggettivo e lo esclude dai testi tecnici e scientifici proprio perché segnala emotività ([Treccani, Punto esclamativo](https://www.treccani.it/enciclopedia/punto-esclamativo_%28Enciclopedia-dell%27Italiano%29/)): su un prezzo, un orario, un dato, non ci va mai.

Nei titoli l'italiano non capitalizza ogni parola come l'inglese: il "title case" è una convenzione americana, rara in italiano fuori da traduzioni pedanti dell'originale, e si maiuscola solo la prima parola e i nomi propri ([Accademia della Crusca, Uso delle maiuscole e minuscole](https://accademiadellacrusca.it/it/consulenza/uso-delle-maiuscole-e-minuscole/58)).

## 4. Parole chiave per un'attività locale

Sul `<title>`, Google Search Central chiede un brand conciso, separato dal resto con un delimitatore (due punti, trattino, pipe), e non fissa un numero di caratteri: il link viene troncato in base alla larghezza dello schermo, non a un conteggio fisso ([Google Search Central, Influencing Title Links](https://developers.google.com/search/docs/appearance/title-link)). Per la meta description vale lo stesso, nessun numero ufficiale, solo "univoca per pagina" e senza liste di parole chiave ([Google Search Central, How to Write Meta Descriptions](https://developers.google.com/search/docs/appearance/snippet)). Chi cita 155 o 160 caratteri lo fa sulla resa a video misurata da terzi, non perché Google lo dichiari: qui quel numero non entra perché la fonte richiesta non lo dà.

Su quante volte nominare il comune, Google Search Central non dà un numero: dà un divieto. Elencare città e regioni per cui una pagina vuole posizionarsi, o ripetere lo stesso termine fuori contesto, rientra nella loro definizione di keyword stuffing ([Google Search Central, Spam Policies](https://developers.google.com/search/docs/essentials/spam-policies)). La regola verificabile è quindi negativa: il nome del comune compare dove serve al senso della frase, nel title, in un H1, nell'indirizzo, non ripetuto a ogni paragrafo.

Su cosa cerca davvero chi cerca un parrucchiere sotto casa, Google Search Central non pubblica dati di query: quella ricerca non esiste in questa fonte, e non si inventa qui.

## 5. Microcopy

Microcopy è ogni testo d'interfaccia sotto le tre frasi, bottoni, etichette, messaggi di stato, e ha tre compiti soltanto: informare, influenzare, aiutare l'interazione ([NN/g, The 3 I's of Microcopy](https://www.nngroup.com/articles/3-is-of-microcopy/)).

"Scopri di più" è debole per lo stesso motivo di "Learn More": non dice cosa c'è dopo il clic, crea incertezza invece di un'aspettativa, e su una pagina con più bottoni uguali diventa ambiguo quale porti dove; per chi usa uno screen reader il link non ha senso isolato dal contesto, e per il motore di ricerca non porta nessuna parola chiave ([NN/g, "Learn More" Links: You Can Do Better](https://www.nngroup.com/articles/learn-more-links/)). È un caso particolare di un problema più generale: un'etichetta generica ha un "information scent" basso, l'utente non sa cosa aspettarsi e quindi esita a cliccare ([NN/g, Information Scent](https://www.nngroup.com/articles/information-scent/)).

Al posto di "Scopri di più" va la parola chiave della destinazione, "I nostri tagli uomo", "Il listino", "Le foto del salone", oppure si trasforma in link il titolo del blocco che lo precede invece di aggiungere un bottone generico sotto. La verifica è semplice: coprire il resto della pagina e leggere solo l'etichetta del bottone, se non dice dove porta, si riscrive.
