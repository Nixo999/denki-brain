---
type: risorsa
riga: Prototipo di CO-OPERO (1/10) sul ramo coopero di opero-sito - cosa c'è, cosa manca per mostrarlo, dove va oltre le decisioni del 30/09.
updated: 2026-10-03
source: claude
progetto: opero
tags: [opero, co-opero, prototipo]
---

# CO-OPERO — il prototipo del 1 ottobre 2026

Nicola l'ha chiesto il 1/10 («prova a disegnare e creare una versione di
coopero, intanto sito […] devono già parlarsi, usa lo stesso database di
opero»). Supera il «non mettere mano al codice» del 30/09 solo come **prova**:
niente è pubblicato, niente è su `main`.

- **Dove**: repo `opero-sito`, ramo `coopero`, otto commit in locale. Com'è
  fatto lo dice il repo: `docs/coopero.md` e la voce del 1/10 in
  `docs/handoff.md`. **Sul tecnico ha ragione il repo.**
- **Cosa c'è**: il portale dei clienti (Lavori, Nuovo, Conti) come secondo
  sito, da telefono e da computer, la pagina Richieste in OperO, lo schema.
  Dal verdetto di Nicola sul primo giro (1/10): Lavori è un giorno alla volta
  con il calendario, e il modulo non chiede più il tipo di lavoro. Dal 2/10:
  da computer un margine solo e pannelli a tutta finestra, e le impostazioni
  della persona. Dal 3/10 le impostazioni seguono il profilo di OperO (dati,
  valuta, luoghi preferiti, versione) e «Nuovo lavoro» da computer è a tre
  schede: chi, quando, dove. Gira su un Supabase locale in
  Docker; sul database di sviluppo la migrazione **non è applicata**.
- **Cosa manca per mostrarlo a Patrick e Seba**: guardare il lato segreteria
  con Nicola (vuole un login), applicare la migrazione allo sviluppo,
  pubblicare il portale su un indirizzo suo, provarlo su un telefono vero.
- **Il codice si indovina, il link no**: era il `TODO` di [[co-opero-clienti]].
  Il cliente entra da un link con un segreto lungo; `VERT001` è solo il nome
  che si legge e si detta.
- **Dove il prototipo va oltre le decisioni del 30/09**, per far girare il
  flusso vero letto nella chat di un cliente: il cliente può modificare dopo la
  conferma (torna dall'ufficio come «modificata», col prima e il dopo) e
  annullare; il rifiuto ha un motivo facoltativo; si conferma anche con una
  parte dei nomi. **Sono fra le cose che aspettano Seba**: qui c'è la versione
  più semplice, da confermare o stringere.
- **Cosa la chat dice e il prototipo non fa**: il preventivo prima della
  conferma, la controproposta dell'ufficio, il giorno stesso («è in ritardo»,
  «uno non è arrivato»).

## Collegamenti

[[co-opero-clienti]] · [[2026-10-01-coopero-prototipo]] · [[opero-intermediar-receive]] ·
[[opero]] · [[registro-interventi]]
