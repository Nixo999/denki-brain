---
type: risorsa
riga: CO-OPERO lato clienti, deciso con Patrick il 30/09 - accesso, pagina Richieste in OperO, stati delle richieste, il mockup letto.
updated: 2026-10-01
source: claude
progetto: opero
tags: [opero, co-opero, richieste, stati, mockup]
---

# CO-OPERO — il flusso dei clienti

Il pezzo da cui si parte (Patrick, 30/09): il cliente chiede da CO-OPERO, la
segreteria risponde dalla pagina Richieste di OperO. **Da imparare, non da
costruire.** Il modello intero, il repo e i buchi → [[opero-intermediar-receive]].

## Il prototipo

Dal 1/10 c'è un prototipo che gira, chiesto da Nicola: ramo `coopero` di
`opero-sito`, in locale, non pubblicato → [[co-opero-prototipo]].

## Flusso 1 — cosa ha deciso Patrick il 30/09

Parole intere in [[opero-intermediar-receive-testo]].

- **Pagine del cliente**: Nuovo lavoro, Lavori (in corso e tutti), Conti. Niente Home.
- **Accesso**: il cliente che oggi scrive su WhatsApp riceve dalla segreteria un link, entra in CO-OPERO col suo codice («come Alus001») e da lì manda le richieste.
- **Richieste è una pagina a sé** in OperO, staccata da Nuovo lavoro, che resta **manuale**: «lo so che è ridondante ma preferisco così».
- **Dove va**: in futuro Nuovo lavoro sparisce, perché «non ci dovranno essere clienti che non usano Coopero». Per ora le pagine sono due.
- **Chi ti serve**: più lavoratori, di tipi diversi, nella stessa richiesta.
- **Stima dei Conti**: arriva da sola quando il lavoro si chiude su OperO, come la chiusura di oggi.
- **Notifica**: sì, la segreteria la riceve quando arriva una richiesta.
- **Aspettano Seba**: accetto con modifica, motivo del rifiuto, modifica e annullamento del cliente, cambio di un lavoratore dopo la conferma.

> [!note] Analisi di Claude — 30/09/2026
> - **Il codice identifica, non protegge.** «Alus001» si indovina: chi prova
>   Alus002 vede nomi e cellulari dei lavoratori e i costi di un altro
>   cliente. Il codice può restare quello che il cliente vede, l'accesso
>   deve passare da qualcosa che non si indovina: il link lungo, un PIN, un
>   codice via SMS. ~~`TODO` Nicola~~ Nel prototipo del 1/10: link lungo → [[co-opero-prototipo]].
> - **Una voce in più sul telefono**: con Richieste l'isola in basso passa da
>   4 a 5 voci, 7 per un admin con Gestione. Scelta di Patrick.
> - **La notifica non esiste ancora**: oggi le push partono solo dalla
>   segreteria verso i lavoratori. Una richiesta del cliente ne vuole una
>   che parta dal server.
> - **La stima può muoversi**: se la segreteria corregge le ore dopo la
>   chiusura, la stima si aggiorna. È una stima, ma il cliente lo vede.

## Gli stati — decisi il 30/09

Patrick: «per la questione pallini, decidi tu [...] io ho pensato ai pallini
perché era comodo a livello visivo». Scelta di Claude (30/09), da far vedere a
Nicola e Seba prima di costruirla.

- **Lo stato è della richiesta, il numero è di chi deve muoversi.** Nella lista delle aziende, in Richieste e in Gruppo, ogni riga ha solo un numero tondo come i messaggi non letti di WhatsApp: quante richieste aspettano **te**. In cima chi ha qualcosa da fare, poi l'ultima attività. Così un cliente con una richiesta nuova e una rifiutata non ha un colore conteso.
- **Dentro l'azienda, ogni richiesta ha un'etichetta con colore e parola**, mai il colore da solo: rosso e verde sono la coppia che un daltonico confonde.

| Stato | Colore | Chi deve muoversi |
|---|---|---|
| Nuova (per chi la manda: «In attesa») | blu | chi la riceve |
| Modificata, la conferma è caduta | giallo, col diff | chi la riceve |
| Confermata | verde | nessuno |
| In corso, il giorno del lavoro, da sola | verde | nessuno |
| Chiusa (completata o incompleta, come in OperO) | grigio, card attenuata | nessuno |
| Rifiutata | rosso | nessuno |
| Annullata da chi l'ha chiesta | grigio | nessuno |

- **Stesse parole ai due capi**: è la stessa richiesta, cambia solo chi ha il numero.

## Il mockup del 30/09 — cosa aggiunge, cosa non torna

Otto schermate di Patrick, «da prendere con le pinze», descritte in
[[opero-intermediar-receive-testo]]. Si legge l'idea, non il disegno.

> [!note] Analisi di Claude — 30/09/2026
> - **Aggiunge**: in OperO, Richieste e Gruppo diventano due voci del menu.
>   Le pagine del cliente le ha poi fissate Patrick: tre, senza Home (sopra).
>   Quelle del fornitore nel mockup sono Home, Richieste, Lavori, Conti. `TODO`
> - **Gruppo voce di menu** contro il 24/09, che voleva Intermediar «un
>   controllo a destra della bottom nav, non una quinta voce». `TODO`
> - **Le parole degli stati cambiano a ogni schermata**: In attesa, Da
>   valutare e Nuova richiesta sono la stessa cosa. Il giallo non c'è ancora.
> - **Nella pagina Richieste lo stato sta sulla riga dell'azienda**: è il caso
>   che il numero tondo risolve. Il numero c'è già nel menu del fornitore.
> - **Manca «Rifiuta»** nel dettaglio: c'è solo «Accetta e crea commessa».
> - **Manca «quanti»**: «Chi ti serve?» è una figura sola, e il dettaglio
>   accetta due nomi. Il caso vero è 8 facchini, o 2 facchini e un autista.
> - **Nomi e cellulari in due liste separate**: in OperO il lavoratore ha già
>   il telefono nel profilo, sceglierlo basta. Un nome aggiunto a mano in un
>   lavoro non entra: serve un account.
> - ~~«Saldo disponibile» e «Accredito»~~: sbagliati, Patrick (30/09). Conti è
>   la stima a lavoro chiuso. Si calcola con quello che c'è già, le tariffe
>   del cliente e `invoiceEngine` sulle ore vere; il cliente vede il totale,
>   non le regole, che oggi legge solo la segreteria.
> - Dopo l'accettazione la richiesta diventa un lavoro, e il cliente la segue
>   fino in fondo: da qui lo stato «In corso» nella tabella sopra.

## Collegamenti

[[opero-intermediar-receive]] · [[opero-intermediar-receive-testo]] · [[opero]]
