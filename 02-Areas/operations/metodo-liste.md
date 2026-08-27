---
type: area
updated: 2026-08-28
source: claude
prodotto: denkishift
---

# Metodo liste — DenkiShift

> [!note] Nota generata da Claude — 2026-08-28
> Metodo proposto, non ancora provato sul campo. Va testato su 40 chiamate
> prima di considerarlo buono. Vedi [[generazione-lead]].

Serve a produrre **40-50 contatti profilati in mezz'ora**, ripetibile ogni
settimana. Risolve il problema del volume; l'angolo di attacco sta in
[[script-giulia-denkishift]].

## Chi è il cliente di DenkiShift

Non "aziende con dipendenti". Tre filtri, in ordine:

| Filtro | Perché |
|---|---|
| **8-50 dipendenti** | Sotto 8 il dolore è piccolo e il ricavo pure (16 €/mese). Sopra 50 hanno già un gestionale HR imposto |
| **Turni variabili**, non orario fisso | Chi entra tutti i giorni alle 9 non ha un problema di turni. Il prodotto risolve la settimana che cambia |
| **Indipendenti, non catene** | Una filiale non decide niente: il software glielo impone la sede. Chiamare catene brucia tempo |

## I segmenti, in ordine di dolore

⚠️ **Il segmento ovvio è quello sbagliato.** "Negozi" viene in mente per primo
ed è il più debole: pochi dipendenti, orario quasi fisso, poca sostituzione.
Il dolore vero sta dove si lavora **H24 o su fasce spezzate**.

| # | Segmento | Perché fa male | Testa tipica |
|---|---|---|---|
| 1 | **RSA, case di riposo, cooperative socio-assistenziali** | H24, sette giorni, sostituzioni continue, tanti part-time | 20-60 |
| 2 | **Imprese di pulizie** | Personale sparso su più cantieri con orari diversi, ogni giorno diverso | 10-40 |
| 3 | **Vigilanza privata** | H24, turni notturni, reperibilità | 10-30 |
| 4 | **Logistica e magazzini** | Turni su due o tre fasce, picchi stagionali | 15-50 |
| 5 | **Ristorazione con doppio turno** | Pranzo e cena, weekend, personale giovane che cambia spesso | 8-25 |
| 6 | **Panetterie e pasticcerie con laboratorio** | Produzione notturna + vendita diurna: due mondi da incastrare | 8-20 |
| 7 | **Supermercati e alimentari indipendenti** | Orario lungo, sette giorni | 10-30 |
| 8 | **Palestre e centri sportivi** | Reception + istruttori, fasce lunghe | 8-20 |
| 9 | **Poliambulatori e cliniche dentistiche** | Agenda medici + segreteria su turni | 8-25 |

**Si parte dai primi tre.** Sono anche i meno battuti: chi vende software fa i
ristoranti, non le imprese di pulizie.

## Il segnale — cosa si legge senza chiamare

Per i siti vetrina il segnale è "non ha il sito". Per DenkiShift è questo:

| Segnale | Dove si vede | Cosa dice |
|---|---|---|
| **Aperto 24 ore** | Orari su Google Maps | Massimo dolore. Chiamare per primi |
| **Aperto 7 giorni su 7** | Orari su Google Maps | Servono per forza più squadre |
| **Orario spezzato** (chiude e riapre) | Orari su Google Maps | Due turni al giorno da incastrare |
| **Annuncio di lavoro attivo** | Indeed, Subito, Facebook, vetrina | Turnover: chi assume spesso rifà i turni spesso |
| **Recensioni che citano il personale** | Google Maps | Squadra numerosa e visibile |

**Un contatto senza segnale non entra in lista.** Meglio 30 nomi con un motivo
che 100 presi a caso: è esattamente la differenza fra chiamare e "parlare col
vuoto".

## Il procedimento — mezz'ora

1. **Una query per volta** su Google Maps: `<segmento> <comune>`.
   Esempi pronti per la Brianza:
   `RSA Seveso` · `case di riposo Seregno` · `imprese di pulizie Meda` ·
   `cooperative sociali Cesano Maderno` · `istituti di vigilanza Desio` ·
   `magazzini logistica Lissone` · `ristoranti Barlassina`
2. Per ogni risultato prendi: **nome, telefono, comune, orario**.
3. **Scarta** le catene e chi ha meno di 8 dipendenti (se si capisce).
4. **Segna il segnale** — quale delle righe della tabella sopra è vera.
5. Incolla nel foglio. Passa al comune successivo.

**Regola d'oro: una lista = un segmento + un comune.** Se ne mescoli tre, alla
fine della settimana non sai quale ha funzionato. Se chiami 40 RSA e ne fissi
6, sai che il segmento è buono e puoi rifarlo sul comune accanto.

## Le colonne del foglio

Sostituisce quelle attuali e alimenta [[metriche]] senza lavoro in più:

```
Nome | Telefono | Comune | Segmento | Segnale | Prodotto | Prezzo indicativo |
Esito | Data richiamo | Appuntamento (data) | Esito appuntamento | Note
```

Le tre colonne finali sono quelle che oggi mancano: senza `Esito appuntamento`
non si sa se il problema è la lista o la trattativa.

**Valori di `Esito`**, sempre gli stessi o il conteggio non torna:
`Non risponde` · `Richiamare` · `Non è il decisore` · `No` · `Troppo piccoli` ·
`Fissato incontro`

## Scaldare il lead prima di chiamare

Le due cose che trasformano una chiamata a freddo in una tiepida, e che potete
fare già domani:

**1. Il biglietto prima della telefonata.** Patrick passa in zona e lascia il
biglietto da visita dedicato ai gestionali ([[materiale-offline]]). Giulia
chiama **entro 48 ore** e apre con *"le ha lasciato il biglietto un mio collega
l'altro giorno"*. Non è più uno sconosciuto: è un seguito. Avete 200 biglietti
fermi e questo è il modo di usarli.

**2. Il messaggio prima della chiamata.** Per chi ha Instagram o WhatsApp
Business: un messaggio breve il giorno prima, e la chiamata diventa un
richiamo. Costa due minuti a contatto.

## Come me le faccio generare

Le liste le può produrre anche Claude. Basta dire:

> *"Fammi una lista di 40 RSA e cooperative socio-assistenziali fra Seveso,
> Seregno e Desio, con telefono, orari e il segnale."*

Quello che serve nella richiesta: **segmento, comuni, quanti contatti**.
Il resto lo prendo da qui.

## Da provare, e come si capisce se funziona

Il primo test è **40 chiamate su un solo segmento**. Poi si guardano tre numeri
in [[metriche]]:

- Sotto il **5%** di appuntamenti → il segmento o lo script non vanno
- Fra **5% e 10%** → in linea col target di 4 su 50, si continua
- Sopra il **10%** → segmento buono: rifallo sui comuni accanto prima di
  cambiare

## Collegamenti

[[script-giulia-denkishift]] · [[generazione-lead]] · [[denkishift]] ·
[[metriche]] · [[materiale-offline]] · [[flusso-vendita]] ·
[[prodotti-e-listino]]
