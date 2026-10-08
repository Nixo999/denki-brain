---
riga: Bozza sito Claudia, educatrice cinofila e dog sitter ad Azzano San Paolo (BG). Giro 1 «Una giornata da Claudia» dell'08/10, una testa sola su Fable.
type: progetto
status: attivo
client: claudia-dogsitter
stack: [html, css, gsap, netlify]
started: 2026-10-08
deadline: TODO
updated: 2026-10-08
source: claude
valore: 0
incassato: 0
---

# Sito Claudia, dog sitter Bergamo

Bozza vetrina per [[claudia-dogsitter]], educatrice cinofila e dog sitter ad Azzano San Paolo (BG). Lei ha risposto
al DM l'08/10 («se vuoi mandarmela qui»): la bozza è la risposta.

**Repo**: `~/lavoro/claudia-dogsitter-site`, **solo locale** (nessun remoto, come Luiza e White Lilium).
**Online**: TODO, il deploy lo lancia Nicola (il classificatore di Claude Code nega a Trevis la creazione di un sito Netlify). Sito da creare: `claudiadogsitter`, team `denkicode`.
**Memoria tecnica**: `DIREZIONE.md`, `raccolta/RACCOLTA.md`, `raccolta/CONCORRENTI.md`, `prove/` nel repo.

## Il metodo (08/10, stesso di White Lilium: un'ora, pochi agenti, Fable solo sul design)
Raccolta Instagram e concorrenti su **Sonnet in parallelo** → `DIREZIONE.md` scritto da **Fable** senza agente →
**una testa sola su Fable** costruisce. Due cose andate storte, da non ripetere: la raccolta si è fermata 10 minuti
senza scrivere su disco (riavviata con l'ordine «salva prima, poi continua»); lo studio concorrenti ha letto 14 siti
e 9 profili in 43 minuti e 200k token, e Nicola l'ha fermato: da allora vale la direttiva dell'08/10 in
[[direttive-siti]] (lettura al volo, 3-4 siti, solo informazioni e ordine delle sezioni).

## Cosa sappiamo e cosa manca (`raccolta/RACCOLTA.md`)
- 12 foto a 1440 (WebP) dai 12 post visibili sloggati su 72: sette ospiti di agosto sul prato (Ettore, Funny, Charlie,
  Leo, Olly, Winston, Iago), tre matrimoni, il volantino del post fissato. Nessuna orizzontale.
- Le sue parole: «Educatrice cinofila in continua formazione», giardino «ampio spazio esterno» (il volantino dice più
  di 1000 mq), «piscinetta» d'estate, «foto e video durante le attività», taxi dog, «Presentazione degli ospiti di agosto».
- Telefono 346 822 9692 (solo nel post fissato). Zona: Azzano San Paolo.
- Non ci sono: cognome, indirizzo, prezzi, orari, formazione e corsi, assicurazione, numero di cani insieme, primo
  incontro, comuni serviti, recensioni vere. Le storie in evidenza (Asilo, Formazione, Wedding, Dogsitter, Lezioni)
  vogliono il login: è lì che stanno probabilmente prezzi e lezioni.
- Concorrenti (`raccolta/CONCORRENTI.md`): nel Bergamasco quasi nessun sito mette i prezzi; passeggiata 8-15 €,
  pensione casalinga 20-40 € a notte sulle piattaforme. Nessuno racconta cosa fa il cane durante il giorno.

## Giro 1 «Una giornata da Claudia» (08/10)
Direzione in `DIREZIONE.md`: la pagina è la giornata del cane da lei (arrivo → giochi e attività olfattive → riposo e
piscina → passeggiata → ritorno con le foto), pista di impronte SVG che si disegna allo scroll con la pallina gialla
che segna «adesso», sole che sale e cala; apertura «il cancello» (due ante salmone che scorrono); palette dal suo
volantino (crema, salmone, bruno, giallo del cuore, prato solo per le tacche); tre terne di font da provare a 375
(Fredoka+Nunito+Caveat, Lilita One+Figtree+Borel, Baloo 2+Mulish+Shantell Sans); h1 «CLAUDIA», foto piccola di Charlie.
Esito (commit `a161ceb`): terna **B, Lilita One + Figtree + Borel** scelta su `prove/font-375.png` (Lilita regge «CLAUDIA» a 12vw ed è il
tono del suo volantino; Caveat sfuma a 26 px, Baloo somiglia a Fredoka). Apertura «il cancello» in CSS: nove impronte una a una, ante
che scorrono a .3 s, titolo e resto in sequenza sovrapposta, rete a 2,6 s. Pin da 900 (`+=1600`) con cinque tappe orarie e le foto
winston→ettore→funny→olly→charlie, freccia «scorri»; sotto 900 colonna testo/foto. Sei servizi senza prezzi («te lo scrivo in chat»),
wedding senza nomi delle coppie, «Prima di venire» in quattro blocchi, sette ospiti con le sue righe, chi sono, Scrivimi gigante.
Misurato: overflow 0 a 375 e 1440, console vuota, controlla-sito **8/8**, slop 0 bloccanti (4 avvisi: gruppi di tre, numeri 01-06),
testo 0/0. Guardato da Trevis dal vivo a 1440 (pin) e 375 (apertura, hero, colonna, servizi). Tempi: raccolta 7+7 min (si era fermata
senza scrivere), concorrenti 43 (troppo: fermati da Nicola), direzione 8, costruzione 46 (32 di sola lettura della catena prima
dell'ordine di scrivere), controllo 8: **circa 1h50**, non un'ora.
Deboli (costruttore e direttore d'accordo): la catena skill è stata tagliata per tempo (craft-floor, high-end, scrittura-sito, polish
e finish review **non fatti**); contrasti AA non misurati (giallo-testo su salmone); didascalie dalle sue righe, non guardando le foto;
i JPEG 800 pesano 140-350 KB (sips senza qualità); i blocchi di 02 e 04 sono card con pallino, il più vicino a template; pista in hero
stretta a 375; pagina lunga 11.500 px a 375; nel pin le righe mischiano tappa e cane («Fuori dal cancello… Olly, una labrador…»).
Non visto: iPhone e Safari veri, pagina senza JS. Verdetto di Nicola: TODO.

## Da chiedere a lei (via Patrick)
Cognome da mettere o no; prezzi o «da»; i comuni dove va a domicilio; quanti cani tiene insieme; primo incontro;
formazione e corsi; assicurazione; WhatsApp sul 346; ok sulle foto dei matrimoni (ci sono gli sposi); logo se esiste;
foto originali (Instagram dà 1440 al massimo).
