---
type: decisione
data: 2026-08-30
progetto: azienda
source: denkicode
tags: [liste, siti, verifica, metodo]
---

# «Non ha il sito» si verifica su Google e sul dominio, non su Pagine Gialle

Deciso da **Patrick il 30 agosto 2026**, dopo aver preso in mano la lista di
Giulia e trovato l'errore alla prima riga: *«se dici che il sito non c'è, il
sito non ci deve essere; se dici che c'è ed è vecchio o fatto male, deve essere
vero»*.

## Cosa non funzionava

La lista del 28 agosto usava come segnale **«la scheda Pagine Gialle non linka
un sito»**. Pagine Gialle mostra il sito solo a chi ha comprato la scheda a
pagamento: **assenza dalla scheda ≠ assenza del sito**. Su 50 righe, 30 avevano
la nota falsa → [[2026-08-30-verifica-siti-giulia]].

## Il metodo, dal 30 agosto 2026

Una riga entra in lista siti solo dopo **tutti e tre** i passaggi:

1. **Ricerca su Google** con nome + comune. Si guardano i risultati che **non**
   sono directory (Pagine Gialle/Bianche, TripAdvisor, Facebook, Sluurpy,
   TheFork, JustEat, Virgilio, Treatwell, Fresha…): quelli non sono un sito.
2. **Prova del dominio**: si apre. `https://dominio` e `https://www.dominio`,
   seguendo i redirect.
3. **Lettura di cosa risponde**, perché «risponde» non basta.

## I sei esiti, e cosa si scrive in nota

| Esito | Come si riconosce | In lista? |
|---|---|---|
| **Nessun sito** | Google non dà nulla fuori dalle directory | ✅ sì — «nessun sito, verificato» |
| **Dominio morto** | Non risponde, ma le schede lo citano | ✅ **lead migliore** — «il vostro sito non si apre» |
| **Parcheggiato** | Risponde con poche centinaia di byte, senza contenuto | ✅ sì — «il dominio c'è, il sito no» |
| **Dirottato** | Risponde ma è un'altra cosa (è successo: un **casinò online**) | ✅ **il più forte** |
| **Su piattaforma** | `*.wixsite.com`, `*.eatbu.com`, `*.xmenu.it`, microsito JustEat | ✅ sì — «non è un dominio vostro» |
| **Vivo e curato** | Contenuto vero, copyright recente | ❌ **fuori** |

**Vivo ma vecchio** è un caso a parte: entra come **restyling**, e in nota si
scrive *cosa* lo rende vecchio (copyright fermo, nessun `viewport`, contenuti
che non citano servizi attivi da anni). Mai «il vostro sito è brutto».

## Le due trappole viste sul campo

1. **Il dominio omonimo.** `naifparrucchieri.it` esiste ma è di **Bologna**;
   `aldragone.it` è di **Vieste**. Un dominio che risponde va aperto e
   confrontato con comune e telefono, o si conta un sito che non è suo.
2. **Il segmento conta più del comune.** Parrucchieri ed estetiste: 12 su 14
   senza sito. Mobilifici: 6 su 6 con sito. **La lista siti si costruisce sul
   wellness**; per i negozi la domanda giusta non è «ha un sito» ma **«vende
   online»**.

## Cosa costa

Circa **un minuto a riga** invece di dieci secondi. Su 50 righe è un'ora in
più, una volta a settimana. È il prezzo per non bruciare una chiamata su due
nei primi cinque secondi — e per non far dire a Giulia, Gabriele o Edoardo una
cosa falsa a un titolare che sa benissimo di avere un sito.

## Collegamenti

[[metodo-liste]] · [[2026-08-30-verifica-siti-giulia]] · [[ciclo-settimanale]] ·
[[2026-08-28-liste-31-agosto]] · [[core-commerciale]] · [[pattern-interrupt]]
