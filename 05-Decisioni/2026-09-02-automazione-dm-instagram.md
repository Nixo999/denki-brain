---
type: decisione
data: 2026-09-02
progetto: azienda
source: claude
tags: [instagram, dm, outreach, automazione]
---

# I DM di Instagram non si mandano da soli: si automatizza tutto tranne l'invio

**Chiesto da Nicola per Patrick**, il 2 settembre 2026: rendere automatico e più
veloce il contatto dei possibili clienti dai messaggi diretti di Instagram.
Ricerca fatta lo stesso giorno.

## Il verdetto

**Non esiste un modo lecito di mandare un DM a freddo in automatico.** Le tre
strade, e cosa costano:

1. **API ufficiale (Instagram Messaging API).** La documentazione Meta è
   esplicita: *la conversazione dev'essere iniziata dalla persona*. Si risponde
   entro **24 ore** a chi ha scritto, commentato o risposto a una storia; il tag
   *Human Agent* allunga a **7 giorni**. Nessun tag e nessuna eccezione
   permettono di scrivere per primi. **Per il cold outreach è inutilizzabile.**
2. **Bot che pilotano browser o app** (Selenium, Playwright, o i servizi che li
   rivendono). È l'unica via che fa quello che Patrick chiede, ed è quella che
   brucia l'account: automazione fuori dall'API = violazione diretta delle
   Platform Terms. I numeri riportati per il 2025-26: **blocco delle azioni a
   15-25 DM al giorno su account nuovi**, 25-35 su account maturi.
   L'automazione non fa mandare di più, fa **perdere l'account prima** — e
   l'account è quello personale di Patrick, che secondo
   [[dm-instagram-vetrina]] è metà del messaggio.
3. **Click-to-Instagram-DM ads.** L'unico modo legittimo di far partire
   conversazioni da freddo: si paga l'annuncio, il prospect tocca «Invia
   messaggio», la finestra di 24 ore si apre da sola e **da lì l'automazione è
   permessa**. Sposta il costo da tempo a budget. Non provata.

## Il vincolo che pesa più del ban

L'**art. 130 del Codice privacy** impone l'opt-in per le comunicazioni
commerciali inviate con **sistemi automatizzati**. Un DM scritto a mano a un
profilo business è la zona grigia in cui si muovono tutti; **un invio massivo
automatizzato è esattamente la fattispecie sanzionata**, e il Garante su questo
è restrittivo. Vale insieme a [[vincoli-fiscali]]: sono i due limiti che non si
aggirano per comodità.

## Dove sta davvero il tempo

Guardando [[2026-09-02-instagram-tattoo-wedding]]: **47 profili invece dei 70
chiesti**, e la colonna che è costata il giro è «Esito verifica sito». Il collo
di bottiglia **non è premere invio, è trovare e qualificare**. Quella metà è
automatizzabile per intero senza violare niente.

## La decisione

**Si automatizza tutto fino al testo pronto; l'invio resta un gesto umano.**

Fatto oggi: [banco-dm.html](../02-Sales/strumenti/banco-dm.html) — un file
solo, nessuna dipendenza, doppio click. Carica il CSV della lista, scrive la
**versione B** del messaggio col gancio della colonna, copia negli appunti e
apre la conversazione con `ig.me/m/<utente>` (deep link ufficiale Meta). Segna
la data, riconosce i recuperi dopo **4 giorni lavorativi**, si ferma a **30
messaggi al giorno** e restituisce il CSV aggiornato.

Dove il gancio ha un buco — dominio, piattaforma, anno — **il tasto resta
spento finché non è compilato**: è la protezione contro il «il dominio [X] non
si apre» mandato davvero.

**Non ancora fatto**: la raccolta e la verifica automatica dei profili (Apify
più il controllo del dominio in bio), che è il pezzo dove sta il tempo vero.

## Collegamenti

[[dm-instagram-vetrina]] · [[metodo-instagram]] ·
[[2026-08-31-canale-dm-instagram]] · [[core-commerciale]] · [[vincoli-fiscali]]
