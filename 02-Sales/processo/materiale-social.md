---
riga: I post pubblicati sul profilo Instagram di DenkiCode - cosa e' uscito, con che didascalia, e dove stanno i file.
type: risorsa
updated: 2026-09-14
source: claude
verificato: 2026-09-14
tags: [social, materiale, lead]
---

# Materiale social

Quello che esce dal profilo di DenkiCode, e dove stanno i file. Il materiale
fisico sta in [[materiale-offline]], l'identita' visiva in [[identita-visiva]].

⚠️ **L'handle del profilo non e' scritto da nessuna parte nel vault.** `TODO` -
lo scrive Patrick qui la prima volta che pubblica.

## Perche' esiste questa nota

Il collo di bottiglia e' la [[generazione-lead]]. Un sito pubblicato lavora da
solo grazie alla firma nel pie' di pagina
([[2026-09-08-firma-powered-by-denkicode]]); un post fa lo stesso mestiere
sulla vetrina nostra, e costa il tempo di scriverlo una volta.

La galleria di [[sito-denkicode]] e la serie di post mostrano gli stessi
lavori: **la regola del dominio vale anche qui**. Si posta un sito che sta su
un indirizzo suo, non una bozza.

## Serie del 14 settembre 2026 - i quattro lavori in galleria

Quattro post verticali, uno per lavoro, stessa impaginazione: simbolo e nome
DenkiCode in testa, nome del progetto con una riga che dice cosa fa il sito, lo
screenshot vero dentro una finestra di browser con il dominio nella barra, tre
voci sotto, `denkicode.com` in fondo.

| Post | Sito | Dominio |
|---|---|---|
| `albybike.jpg` | [[sito-albybike]] | `albybike.com` |
| `fiftynine.jpg` | [[sito-fiftynine]] | `bartabacchi59.it` |
| `bellastoria.jpg` | Bellastoria | `bellastoria.netlify.app` |
| `vbag.jpg` | V-BAG | `vbag.it` |

**I file**: `~/Desktop/denki-pubblicita-instagram-2026-09-14/` sul Mac di
Patrick, piu' `didascalie.txt` con i quattro testi da copiare. Non stanno nel
vault: sono PNG da 300-900 KB e il vault e' testo.

**Il formato buono e' JPEG 1080x1350**, verticale 4:5: e' l'inquadratura che
nel feed occupa piu' schermo, e a parita' di scroll si vede il doppio. Le
stesse quattro a 1080x1080 stanno in `quadrati/`, per quando una serve
quadrata.

Si posta il JPEG, non il PNG: Instagram ricomprime tutto in JPEG comunque, e
partire da un PNG da un mega significa fargli fare la conversione a modo suo.
I PNG restano in `png/` come sorgente da cui riesportare, qualita' 92 e
sottocampionamento disattivato, che e' quello che tiene ferme le scritte
piccole in fondo.

Gli screenshot sono presi dai siti online il 14 settembre 2026, non da una
copia locale: banner dei cookie e badge di Netlify tagliati fuori
dall'inquadratura, niente ritocchi sopra la pagina.

## Le tre cose da sapere prima di pubblicare

1. **V-BAG ha il pulsante d'ordine morto.** In `script.js` la costante del
   numero WhatsApp e' vuota: chi compila il modulo si becca un avviso che lo
   rimanda a Instagram, e `dati/borse.json` e' un elenco vuoto. La didascalia
   per questo non nomina l'ordine dal sito. Portare traffico li' prima della
   correzione butta via i clic.
2. **Bellastoria sta su `bellastoria.netlify.app`**, e l'indirizzo si legge
   nella barra del browser dentro l'immagine. E' l'eccezione gia' nota della
   galleria: se l'indirizzo di anteprima da' fastidio in un post pubblico, si
   rifa' l'immagine senza barra.
3. **V-BAG e' il progetto personale di Giulia**, fuori dal listino DenkiCode.
   Sta in galleria per scelta di Nicola del 12 settembre: postarlo e' coerente
   con quella, e non lo trasforma in un lavoro fatturato.

I testi sono passati da [[voce-denkicode]]. Restano `source: claude` finche'
Patrick non li rilegge prima dell'invio.

[[stile-comunicazione]] · [[generazione-lead]] · [[sito-denkicode]]
