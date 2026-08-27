---
type: decisione
data: 2026-08-11
progetto: opero
source: repo
---

# La regola "stessa app, codice migliore" non è più assoluta

## Il contesto

[[opero]] nasce come **ricostruzione pulita** di `sebapp-bolanos`, l'app che il
cliente usa già in produzione. La regola fondante era netta:

> Stessa app, codice migliore. Nessuna funzione in più, nessuna in meno.

Serviva a due cose: rendere il lavoro stimabile (la specifica esiste già,
funzionante) e impedire che il progetto crescesse senza fine.

## Cosa è successo

L'**11 agosto 2026** il committente ha chiesto funzioni che nella vecchia app
non esistono: sospensione utenti, ruoli personalizzati, preferiti, liste del
super admin, notifiche con immagini, creazione account.

## La decisione

La regola decade come vincolo assoluto, ma restano vere due cose:

1. **Quando una funzione esiste anche nella vecchia app, si copia da lì.**
   L'originale è più preciso di qualunque riassunto — e la verifica è doppia:
   il componente dev'essere *renderizzato* da qualche parte raggiungibile (non
   solo importato) e la tabella dev'essere *interrogata*. Copiare codice morto è
   il modo più silenzioso di sprecare settimane: ha già scartato tre voci.
2. **Ogni aggiunta va detta al committente come aggiunta**, perché sposta piano
   e data.

## Conseguenza aperta

⚠️ Il punto 2 è quello che nella pratica sta scivolando. Il progetto è oltre la
data promessa (21 agosto), lo scope ha continuato a muoversi, e le 2.000 € di
credito dipendono dalla chiusura.

Vedi anche [[2026-08-22-xml-sdi-da-quotare]], che è lo stesso problema in forma
più costosa.

## Collegamenti

[[opero]] · [[cliente-opero]] · [[stile-comunicazione]]
