---
type: progetto
status: attivo
client: dsi-advertising
stack: [html]
started: 2026-09-02
deadline: TODO
updated: 2026-09-02
source: claude
valore: TODO
incassato: 0
---

# Sito D.S.I. Advertising — rifacimento vetrina

Sito vetrina per **D.S.I. Advertising di Piras Sebastiano**, Merate (LC),
produttore di articoli promozionali HO.RE.CA. dal 1992. Cliente:
[[dsi-advertising]]. **Non commissionato**: nasce come bozza al buio, stesso
schema di [[sito-fiftynine]] e [[2026-08-30-sito-castiglione]].

**Repo**: nessuno — la bozza sta in una cartella locale `dsi-site`, `git init`
senza remote (**deciso da Nicola il 2 settembre: prima locale, il remote dopo**)
**Online**: no
**Stack**: HTML puro, un solo `index.html`, zero build e zero dipendenze.
`netlify.toml` e `robots.txt` già scritti coi tre sbarramenti `noindex`
([[netlify]]), da togliere il giorno in cui il sito è loro.

## La bozza — 2 settembre 2026

Una pagina: apertura, gamma, lavorazione, marchi, contatti.

Il pezzo che la regge è il **banco prova** in apertura: si scrive il proprio
marchio, si sceglie il colore di stampa fra cinque, e il portatovaglioli
disegnato accanto si personalizza mentre si guarda. **Il colore scelto diventa
l'unico colore della pagina.** È il modello di business — stesso oggetto, il
vostro logo sopra — messo in mano al visitatore invece che raccontato: in
trattativa si fa scrivere il suo nome al cliente, dal telefono di Patrick.

**Niente foto**: gli oggetti sono disegni SVG a tratto. Non è un ripiego
grafico, è la conseguenza di non avere immagini utilizzabili — le Instagram
sono a 640px. Il sito sta in piedi senza chiedere niente al titolare, e le foto
vere si aggiungono quando arrivano.

✅ Misurato a 390, 500 e 1440: nessun elemento fuori viewport.
⚠️ Font (Archivo, Public Sans, IBM Plex Mono) mai visti: Google Fonts è
bloccato dal proxy della sessione, gli screenshot sono coi font di sistema.
⚠️ Tutti i testi sono `source: claude`.

## Il sito che hanno già

`www.dsi-advertising.com`, con una **seconda installazione separata per
l'inglese** su `en.dsi-advertising.com`. Due domini per due lingue è l'impianto
di un sito costruito prima che i CMS gestissero le lingue in un posto solo.

⚠️ **Non l'ho aperto.** Il proxy di rete di questa sessione blocca il dominio:
tutto quello che so viene da risultati di ricerca, non dalle pagine. Prima di
scrivere una riga di copy o di dire al cliente cosa non va, il sito va guardato
da un browser vero — struttura, mobile, velocità, quanti click per arrivare a
un prodotto. Finché non è fatto, «è vecchio» resta un'impressione di Nicola,
non un dato del vault.

## Materiale già in mano

| Cosa | Dove | Nota |
|---|---|---|
| Posizionamento: «Progettazione e Produzione di articoli promozionali per il canale HO.RE.CA. — Made in Italy» | bio Instagram | è già il payoff |
| Dal 1992, produzione propria, kit personalizzabili col logo | testi del sito indicizzati | 30+ anni di storia = leva di fiducia |
| Prodotti: portatovaglioli, portabustine, rendiresto, orologi | testi del sito indicizzati | catalogo stretto, si mette tutto in home |
| **13 foto di prodotto sul campo** (Caffè Teti, Giovannini, DaRoma, Giobatta) | `@dsi.advertising` | è la galleria pronta: prodotto reale su tavolo reale |
| Recapiti (via Statale 40, 039 9903118, dsi.advertising@tin.it) | Pagine Gialle | da riverificare col titolare |

Le foto Instagram sono il pezzo che vale: un produttore di oggetti fisici si
vende con gli oggetti fotografati dove vengono usati, non con stock photo. La
galleria è la struttura del sito, non un contorno.

## Nodi aperti

- ⬜ Aprire il sito attuale e **misurare** cosa non va (PageSpeed, mobile,
  struttura), prima di qualunque testo di vendita.
- ⬜ **Bilingue IT/EN**: il sito attuale ce l'ha. Rifarlo su un dominio solo è
  lavoro in più — va deciso prima di stimare, non dopo.
- ⬜ Foto: quelle Instagram sono a bassa risoluzione. Per un sito vero servono
  gli originali dal titolare.
- ⬜ Recensioni: **non ne esistono di pubbliche** (vedi [[dsi-advertising]]).
  Niente sezione testimonianze finché non ce ne sono di vere; al loro posto i
  marchi serviti, se il titolare dà il permesso di nominarli.
- ⬜ Non è ancora una trattativa: nessun contatto preso, nessun prezzo detto.
- ⬜ La bozza **non è pubblicata e non è su GitHub**: finché resta su una macchina sola non è un'esca ([[netlify]]).

## Collegamenti

[[dsi-advertising]] · [[sito-fiftynine]] · [[2026-08-30-sito-castiglione]] ·
[[2026-08-30-verifica-sito-reale]] · [[prodotti-e-listino]]
