---
type: progetto
riga: Bozza di sito vetrina per Ohana Special Dog, toelettatura di Daniela Esposito a Levate (BG). Costruita il 16/10 in un'ora.
updated: 2026-10-16
source: claude
verificato: 2026-10-16
status: attivo
client: ohana-special-dog
stack: HTML statico, GSAP, Netlify
started: 2026-10-16
deadline: TODO
---

# Sito Ohana Special Dog

Bozza di sito vetrina per [[ohana-special-dog]]. Il 16/10/2026 Nicola l'ha
chiesta in un'ora, con il metodo di [[sito-ngbarber]], [[sito-fiftynine]] e
[[sito-barbershop-snia]] e la struttura di [[sito-giulia-pregnolato]], perché
la apriranno quasi tutti dal telefono.

**Cartella**: `~/lavoro/ohana-site`
**Online**: <https://ohanaspecialdog.netlify.app> (sito Netlify `bf3e4ae9-04a1-4dc0-8463-a4280e3dfaba`, team di Nicola), si pubblica con `./pubblica.sh`

## La direzione

L'ha scritta un agente Fable in `DIREZIONE.md` del repo. Il sito prende i
colori veri del negozio: il verde acceso delle pareti della sala come campo, il
rosso dell'ibisco del logo come accento, il verde scuro e il rosa delle due
carte da parati. Il racconto allo scroll è la seduta di toelettatura in sei
tappe, dall'arrivo al ritorno a casa. La sezione su Daniela parte dalla sua
frase «Ohana vuol dire famiglia».

## Il materiale

Il materiale completo sta in `RACCOLTA.md` e `CONCORRENTI.md` del repo. Le
foto utilizzabili sono cinque: il ritratto di Daniela, tre pastori tedeschi e
la vetrina con l'insegna. Instagram non era collegato nel browser dell'app,
quindi si vedevano solo i primi 12 post. Le foto della scheda Google con il
barboncino, i cani piccoli, il murale e i gatti sono a 600x800 pixel e non
bastano.

## Storia

- 16/10: raccolta e concorrenti su Sonnet, direzione su Fable, costruzione su Opus in tre passaggi. Online il giro 2 (`2a42cf4`): dieci sezioni, font Lilita One, Nunito e Pacifico scelti con le prove a 375 (gli altri due titoli sbordavano), bottone principale «Chiama Daniela» sul cellulare, servizi a schede colorate, la seduta in sei tappe con il binario sotto la barra sul telefono, recensioni vere. Controlli 8/8, 0 e 0. Il nastro di parole che scorre, chiesto per errore nel brief, è stato tolto prima della pubblicazione. Motion mai vista a velocità vera (il pannello dell'app girava a 2 fotogrammi al secondo), iPhone mai. Due frasi sulla tecnica sono generiche e non confermate da Daniela.
- 16/10, dopo il verdetto di Nicola («il verde all'inizio non mi piace, … troppa roba scritta»): giro 3 con la palette semplice di Fable (crema `#FAF6EF`, sabbia `#F0E8DB`, rosso `#B73A34`, inchiostro `#2B2A26`) e il testo tagliato da 807 a 373 parole; tolta la sezione «La prima volta». Poi Patrick ha detto che dal telefono lagga: tolte la sfocatura della barra, lo scrub sul telefono, le misure durante lo scroll, le maschere sulle foto, e ignorato il resize della barra degli indirizzi di iPhone (`df12fbd`). Con la CPU rallentata 4 volte i fotogrammi lenti sono passati da 1 a 0 e il peggiore da 250 a 17 ms; su un iPhone vero non è ancora riprovato.
- 16/10, pomeriggio, dopo «troppo semplice e vuoto, le sottolineature toglile»: giro 4 «vita nella stessa famiglia», direzione scritta dal direttore su Fable, costruita su Opus (`4d65c8f`, `13edb67`). Via le righe sotto le parole e i link sottolineati; due tinte in più della stessa famiglia (sabbia scura `#E4D9C6`, rosa cipria `#F3E3DF`); una parola rossa in ogni titolo, ombre ferme sulle schede, il cartellino appiccicato di sbieco sulla foto, le foto della galleria inclinate che si raddrizzano entrando, la tappa accesa che si alza, il 10 che conta. Contrasto rosso su rosa cipria 4,6:1. Con la CPU rallentata 4 volte: 0 fotogrammi lenti, il peggiore 17 ms. iPhone vero ancora da riprovare.
