---
riga: Bozza sito White Lilium Photography, fotografa maternity/newborn/famiglia, Trezzano sul Naviglio. Giro 1 «Il controluce» del 07/10, una testa sola su Fable.
type: progetto
status: attivo
client: whitelilium
stack: [html, css, gsap, netlify]
started: 2026-10-07
deadline: TODO
updated: 2026-10-07
source: claude
valore: 0
incassato: 0
---

# Sito White Lilium Photography

Bozza vetrina per [[whitelilium]], fotografa di famiglia, gravidanza e newborn a Trezzano sul Naviglio (MI). Esca del
flusso A: lei ha risposto al DM di Patrick il 07/10 («Stavo già pensando di fare un sito»), la bozza è la risposta.

**Repo**: `~/lavoro/whitelilium-site`, **solo locale** (nessun remoto, come Luiza).
**Online**: whiteliliumphotography.netlify.app (dal 07/10 sera; Netlify site `e96a0b8a`, team `nicola-la-rezza`). Tre sbarramenti + 404 su `PRODUCT.md`, `DIREZIONE.md`, `raccolta/*`, `prove/*`.
**Memoria tecnica**: `PRODUCT.md`, `DIREZIONE.md`, `raccolta/` nel repo.

## Il metodo (07/10, richiesta di Nicola: un'ora, pochi agenti, poco Fable)
Raccolta e concorrenti su **Sonnet in parallelo** (raccolta 7 min, concorrenti 4) → direzione scritta da **Fable** senza
agente (`DIREZIONE.md`, 95 righe: mondo, palette, tre coppie di font da provare a 375, apertura, spina, sezioni, mappa dei
file) → **una testa sola su Fable** costruisce tutto (la direttiva del 07/10 vuole il design su Fable; «il meno possibile»
è stato letto come: zero costruttori in parallelo, Sonnet dove non serve giudizio).

## Cosa sappiamo e cosa manca (dalla raccolta, `raccolta/RACCOLTA.md`)
- 18 foto a 1440 dal singolo post Instagram sloggato (la griglia dà 640, il post 1440). Nessuna orizzontale.
- Facebook: email pubblica, sito `whiteliliumphotography.it` dichiarato ma **morto** (NXDOMAIN 07/10), 6 recensioni tutte
  positive, una leggibile (2020). mondozampa.com è dirottato: non è una fonte.
- Il nome della fotografa non è scritto da nessuna parte: l'email lo suggerisce, **non si scrive** finché non lo dice lei.
- Non ci sono: prezzi, durata, foto consegnate, tempi, telefono, orari, studio, logo. Nel sito: «scrivimi e lo decidiamo».
- Concorrenti: 2 siti letti su 8 (Moxedano Milano, Nico Bologna), il resto schede di portale; sintesi «da confermare».
  Nessuna fotografa vera mette i prezzi in home.

## Giro 1 «Il controluce» (07/10)
La pagina è una famiglia che cresce in controluce: pancione → primi giorni → primo anno → anni dopo (sue parole: «rivedere
le "mie famiglie" a distanza di anni, più numerosi»). Palette latte/avorio/bruno/miele dalle sue foto, nessun disegno di
soggetti: la grafica è luce e linee (sole che scorre, binario del tempo, orizzonte). Apertura «il telo» in CSS.
Font: **Fraunces** (opsz 144, SOFT 50) + **Figtree** + **Pinyon Script**, scelti su `prove/font-375.png` contro Instrument Serif+Albert Sans+Corinthia
e Gloock+Nunito Sans+Birthstone (Pinyon è l'unico script che tiene «fotografa di famiglia e gravidanza» su una riga a 375).
Spina: sole fisso che attraversa la pagina, binario del tempo in nav e hero, da 900 px **un pin** (`+=1600`) con f01→f14→f10→f06
e le sue frasi; sotto 900 colonna. Apertura «il telo»: due teli avorio con alone miele in `multiply`, 1,05 s, righe h1 .35/.47 s, tutto
in un fiato, rete a 2,6 s. Misurato: controlla-sito **8/8**, slop 0 bloccanti (5 avvisi su frasi sue verbatim), testo 0/0, overflow 0 a
375 e 1440, console vuota. Catture `prove/giro1-375.png` e `giro1-1440.png`, guardate da Trevis. Tempi: raccolta 7 min, concorrenti 4,
direzione 6, costruzione 24, controllo e deploy 10: **circa 55 minuti**.
Deboli (costruttore e direttore d'accordo): a 1440 la hero ha molto latte vuoto a destra del testo; «Come si svolge» è quattro righe senza
un fatto (non ci sono fatti: durata, foto, tempi mancano); «Cosa fotografo» ripete lo stesso ritmo in tre blocchi; Newborn usa f11 (bimba,
non neonata). Non visto: iPhone e Safari veri, pagina con JS disattivato. Verdetto di Nicola: TODO.
Trappola nuova scritta in [[trappole]]: `controlla-sito.py` conta le `-800.jpg` in `assets/img/` come foto piccole; le versioni mobile
stanno in `assets/img/800/`.

## Da chiedere a lei (via Patrick)
Nome da mettere sul sito; prezzi o «da»; durata e numero di foto; quando prenotare maternity e newborn; studio (dove);
WhatsApp; logo se esiste; il dominio `.it` è suo e scaduto?; via libera sulle foto dei clienti usate.
