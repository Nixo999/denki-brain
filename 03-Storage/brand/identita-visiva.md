---
type: risorsa
updated: 2026-08-30
source: claude
tags: [brand, stampa, materiale]
---

# Identità visiva e file sorgente

I file vettoriali e i sorgenti di stampa di DenkiCode, portati nel vault il
**28 agosto 2026** da `~/Desktop/denki-pubblicità` sul Mac di Patrick, dove
erano l'unica copia esistente. Da qui in poi **questa è la copia buona**: si
modifica il file che sta qui, non quello sul Desktop.

Cosa c'è **scritto** sui materiali sta in [[materiale-offline]]; qui c'è cosa
sono i file, quale si usa quando, e cosa manca.

## Cosa c'è

### `logo/` — il marchio

| File | Cos'è | Quando si usa |
|---|---|---|
| `logo-principale.svg` | Vettoriale, versione principale | **Web, email, social.** È il formato giusto per Nicola |
| `logo-principale.ai` | Sorgente Illustrator | Solo per modificare il marchio |
| `logo-principale.pdf` | Vettoriale per la stampa | Da mandare in tipografia |
| `logo-alternativo.*` | Seconda versione, stessi tre formati | Quando la principale non regge sul fondo |
| `immagine-denkicode.af` | Sorgente Affinity | Documento di lavoro, non un esportabile |
| `logo-denkishift.svg` | **Il marchio di DenkiShift**, vettoriale | Dentro l'app e ovunque serva il logo del prodotto |

Il marchio è del **13 maggio 2026** e non è più stato toccato: è la parte
stabile dell'identità.

### Il marchio di DenkiShift — 30 agosto 2026

Cosa diverso dai due qui sopra: quelli sono il marchio **dell'azienda**, questo
è il marchio **di un prodotto**. Anello spezzato con due saette, metà neutro e
metà sfumato, calendario al centro. Fatto da Patrick in Affinity.

⚠️ **Qui c'è solo l'SVG, e non è il sorgente.** È stato **estratto dai
tracciati** di un PDF che Patrick ha passato il 30 agosto e che dal Desktop è
poi sparito: sono i percorsi veri, non un ridisegno, ma il documento Affinity
da cui nasce **non è nel vault**. Ce l'ha Patrick sul suo Mac. Se il marchio va
modificato, si parte da lì — non da questo SVG.

Due cose sull'SVG, per chi lo riusa:
- la **metà neutra e il calendario usano `currentColor`**, così il logo si
  adatta al fondo su cui sta. Aperto da solo mostra il neutro scuro (`color=`
  sull'elemento radice); su fondo scuro basta sovrascrivere `color`;
- il **gradiente legge `--marchio-1` / `--marchio-2`** con ripiego sui colori
  del sito (`#923adf → #da2f9b`). I colori del PDF originale sono in **CMYK** e
  su schermo darebbero `#626095 → #ab4287`: gli stessi due colori del marchio,
  smorzati dalla conversione per la stampa. Su schermo valgono quelli del sito.

Il PDF originale era in CMYK ed è materiale da stampa: se serve stampare, non
si usa questo SVG ma si riesporta dal sorgente Affinity.

### `stampa/` — volantino e biglietto

| File | Cos'è | Data originale |
|---|---|---|
| `volantino-fronte-v2.pdf` | Il PDF andato in stampa, fronte | 11 giugno 2026 |
| `volantino-retro-v2.pdf` | Il PDF andato in stampa, retro | 11 giugno 2026 |
| `bigliettino-demo-v2.pdf` | Il biglietto da visita, fronte e retro | 11 giugno 2026 |
| `volantino-fronte-v2.af` | **Sorgente** Affinity del fronte | 29 giugno 2026 |
| `bigliettino-demo.af` | **Sorgente** Affinity del biglietto | 29 giugno 2026 |
| `volantino-retro-finito.af~tmp~` | File temporaneo di Affinity | 29 giugno 2026 |

I nomi sono stati portati in `kebab-case` come vuole il vault. Sul Desktop di
Patrick si chiamano ancora `VOLANTINO FRONTE V2.af`, `Presentazione logo.ai` e
compagnia: stesso contenuto, nome diverso.

## Le tre cose che mancano

> [!warning] Analisi di Claude — 2026-08-28
>
> **1. Il retro del volantino non ha un sorgente modificabile.** In cartella
> c'è `volantino-retro-finito.af~tmp~`, che è un file di appoggio di Affinity —
> quello che resta quando il programma si chiude male — e **non c'è nessun
> `volantino-retro-finito.af`**. Del lato che vende davvero esiste solo il PDF
> dell'11 giugno. Finché non si recupera quel temporaneo (aprirlo rinominandolo
> `.af` e vedere se Affinity lo digerisce), **il retro non si può correggere:
> si può solo rifare**. È il file più importante dei sei ed è l'unico senza
> sorgente sicuro.
>
> **2. I sorgenti sono più recenti dei PDF stampati.** I `.af` sono del
> 29 giugno, i PDF dell'11: fra le due date qualcuno ha modificato fronte e
> biglietto senza riesportare. `TODO` — cosa è stato stampato davvero? Se in
> tipografia sono andati i PDF dell'11 giugno, i sorgenti contengono modifiche
> che non stanno sulla carta che Patrick ha in mano.
>
> **3. Dove punta il QR non è verificato.** Sia il volantino (fronte) sia il
> biglietto ne hanno uno, ed è la stessa immagine su tutte e 1.000 le copie.
> Non è decodificabile dai PDF senza scansionarlo. `TODO` — inquadrarlo col
> telefono e scrivere qui l'indirizzo. Se il volantino atterra sulla home
> invece che su una pagina che parla di siti vetrina, chi scansiona si perde.

## Da correggere alla prossima tiratura

Sono difetti dei materiali, non dei file: sulle copie già stampate non si
risolvono, sui prossimi sì. Il dettaglio del perché sta in [[materiale-offline]].

- ⬜ **Il numero di telefono sul volantino.** Oggi ci sono solo
  `info@denkicode.com` e il sito: chi si convince la sera non manda una mail
- ⬜ **Le icone invertite sul biglietto**: la cornetta sta accanto al sito, il
  mappamondo accanto al numero
- ⬜ **Un QR diverso per zona**, se si vuole misurare da dove arrivano le visite

## Regole d'uso

1. **Si esporta, non si manda il sorgente.** In tipografia va il PDF, sul web
   l'SVG. Il `.af` e l'`.ai` non escono da qui.
2. **Chi modifica riesporta subito il PDF** e lo committa insieme al sorgente,
   altrimenti si ricrea il disallineamento del punto 2 qui sopra.
3. **Le versioni si numerano** (`v2`, `v3`) e la vecchia non si cancella: la
   carta stampata resta in giro per mesi e serve sapere a quale versione
   corrisponde.

## Collegamenti

[[materiale-offline]] · [[generazione-lead]] · [[prodotti-e-listino]] ·
[[sito-denkicode]]
