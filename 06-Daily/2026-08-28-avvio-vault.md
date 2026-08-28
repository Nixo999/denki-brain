---
type: daily
data: 2026-08-28
updated: 2026-08-28
source: claude
progetti: []
---

# 2026-08-28 — Avvio del second brain

Prima nota del vault. Scritta da Claude a fine costruzione, per lasciare un
punto di partenza invece di una cartella muta.

## Fatto

- Intervista a Nicola su azienda, stack, comunicazione, progetti, clienti,
  business e vendita — 5 blocchi
- Analisi diretta dei repo `smooth-duty` ([[denkishift]]) e `opero-sito`
  ([[opero]]), inclusi `CLAUDE.md` e tutti i `docs/`
- Censimento dei repo pubblici su `github.com/Nixo999` e verifica di
  `albybike.com`
- Costruita la struttura PARA completa: 3 progetti attivi, 2 clienti, 3 archivi,
  4 decisioni, 8 note di area e risorsa, 4 template, 5 slash command

## Deciso

- [[2026-08-28-domini-a-scadenza]] — confermata la strategia dell'1 €, il
  rischio resta scritto
- [[2026-08-28-stack-non-uniforme]] — aperta, da chiudere

## Secondo giro — i sette `TODO`, chiusi in sei

Nicola ha risposto in serata. Cosa è cambiato:

1. ✅ **Il cliente di OperO è Sebastian Torres, "Seba"** — e non è un'azienda di
   traslochi: è **un privato che sta aprendo la sua attività, e l'attività è
   OperO**. Noi siamo i suoi sviluppatori; lui rivende l'app alle aziende. Il
   suo primo cliente è **suo padre**, il secondo è in attesa. Riscritta
   [[sebastian-torres]], rinominato il file, propagato ovunque, riscritta
   l'apertura di [[opero]] e aggiunta la regola 6 in `CLAUDE.md`.
2. ✅ **Le ricevute si emettono su Patrick.** Conto del tetto aggiornato in
   [[vincoli-fiscali]]: a OperO saldato gli restano ~2.600 €.
3. ✅ **Prodotto B**: da 500 € + canone 30-100 €/mese + **1% sulle vendite**.
   Giulia prende il **25% sull'incasso iniziale**, niente su mensilità e 1%.
   → [[prodotti-e-listino]]. **La provvigione su DenkiShift resta TBD**: era
   nella stessa domanda ed è l'unico pezzo rimasto scoperto.
4. ✅ **Niente è escluso per principio**: si può proporre qualunque strumento,
   purché la proposta dica cosa migliora e cosa costa mantenerlo → [[stack]].
5. ✅ **cococat non ha detto no: non ha risposto.** Cambia l'esito da "rifiutata"
   a "nessun riscontro" — è un lead **ancora vivo**, con una bozza già pronta.
6. ✅ **DROP OUT** sono gli eventi universitari di Patrick e di un gruppo di
   ragazzi, in un locale in Bicocca. Guadagno bassissimo, estraneo a DenkiCode:
   il sito è stato fatto **per riempire la galleria** → [[sito-dropout]].
7. ⬜ Numeri di [[metriche]] — ancora da compilare.

## Terzo giro — le ultime risposte

- ✅ **La galleria sta su denkicode.com.** Creata la scheda [[sito-denkicode]]:
  è un progetto attivo, perché è lo strumento di vendita più usato che avete.
  Rilevati due punti: un commento `TODO` del template rimasto nel sorgente
  pubblico, e il fatto che in galleria ci siano *lavori* ma non *clienti*
- ✅ **Provvigione su DenkiShift**: 20% sul totale, come i gestionali a
  pacchetto. Interpretazione da confermare con Patrick, segnata nella nota
- ✅ **Secondo cliente di Seba**: si saprà nella settimana del 31 agosto
- ✅ Riscritta [[metriche]] perché non era chiara: adesso dice esattamente quali
  due numeri servono, dove si prendono e come si scrivono

## Quarto giro — provvigioni definitive e la questione ricevute

**Schema provvigioni dettato da Patrick.** Sostituisce tutto quello che avevo
scritto prima — le mie versioni precedenti (20% su A, 20% su D) erano sbagliate:

| Prodotto | Giulia prende |
|---|---|
| A — Vetrina | **25% sull'anticipo**, 0% sui canoni |
| B — E-commerce | **25% sull'anticipo**, 0% sui canoni, **0% sulle royalty** |
| C — DenkiShift | **TBD**, e non è bloccante |
| D — Custom | **25% del totale venduto** — una tantum o annuale |

Il principio: **prende su quello che il cliente paga per *avere* la cosa, mai su
quello che paga per *tenerla*.** Aggiornati [[ruoli-e-responsabilita]],
[[prodotti-e-listino]], [[flusso-vendita]], [[denkishift]].

Due cose emerse di contorno: le royalty degli e-commerce sono **1-2%**, non 1%
fisso; e i gestionali custom si possono vendere **anche ad abbonamento
annuale**, non solo una tantum.

**I 400 € di OperO non hanno ricevuta**: accordo fra privati. Non consumano il
tetto di nessuno, ma non sono nemmeno un'entrata dimostrabile. Aggiornato il
conto in [[vincoli-fiscali]]: a Patrick, incassati i 2.000 €, restano ~3.000 €.

## Quinto giro — si attacca il collo di bottiglia

Priorità decisa: **DenkiShift**, senza chiudere gli altri prodotti. Zona:
**Brianza**, scelta da Claude perché è dove biglietto e telefonata si sommano.

Scritti due documenti, tutti e due `source: claude` e **da provare su 40
chiamate** prima di considerarli buoni:

- [[metodo-liste]] — chi è davvero il cliente (8-50 dipendenti, turni variabili,
  non catene), i nove segmenti in ordine di dolore, il **segnale osservabile**
  (orario H24 / 7 su 7 / annuncio di lavoro attivo), le colonne del foglio e la
  regola «una lista = un segmento + un comune»
- [[script-giulia-denkishift]] — apertura pattern interrupt, la domanda che apre
  il dolore, sei obiezioni col looping, cosa Giulia deve portare a Patrick, i
  due messaggi WhatsApp, e la tabella di quello che non si dice mai

Il rilievo che conta: **il segmento ovvio è quello sbagliato.** "Negozi" viene
in mente per primo ed è il più debole. Il dolore vero sta in RSA, imprese di
pulizie e vigilanza — H24, sostituzioni continue, e nessuno li chiama.

## Sesto giro — repository online e prima lista

- ✅ **Push eseguito** su `github.com/Nixo999/denki-brain` (privato). Sette
  commit. Aggiunto `.gitattributes` per normalizzare i fine riga fra Windows e
  Mac, altrimenti ogni pull sarebbe un conflitto su note mai toccate
- ✅ **Capacità di Giulia**: un'ora al giorno, ~5 a settimana, numero personale
  con WhatsApp. Il conto in [[metriche]] dice che 50 chiamate ne occupano due:
  il limite non è lei, è quanto ha da chiamare. Lista ridimensionata a 70-80
- ✅ **Prima lista vera**: [[2026-08-28-brianza-turni]], **51 contatti** —
  25 RSA, 7 cooperative, 19 imprese di pulizie. Nessuna lista in mano a Giulia
  prima di questa

## Settimo giro — correzione, team e pattern interrupt

⚠️ **Correzione di un mio errore.** "50 chiamate" significa **50 risposte
vere**, non 50 numeri composti. Avevo dedotto che a Giulia avanzasse tempo: è
il contrario. Per 50 conversazioni servono ~130 numeri, che fanno **quasi
quattro ore** delle cinque che ha. Il target la porta all'80% della capacità.
Rifatto il conto in [[metriche]] e ridimensionata la lista a **130-150 contatti
a settimana**: le 51 righe di [[2026-08-28-brianza-turni]] coprono due giorni,
non una settimana.

- ✅ **[[team-e-vincoli]]** — profili, orari, università e hardware. Tutti e tre
  lavorano ~25h a MediaWorld o come cameriera e studiano a Bicocca: DenkiCode è
  il terzo impegno. Aggiunta la regola 6 in `CLAUDE.md`
- ✅ **[[pattern-interrupt]]** — quattro aperture con meccanismi diversi
  (disarmo, franchezza, no anticipato, prossimità) e un piano di test a
  eliminazione, due per volta

Tre cose emerse leggendo i profili: **la Bicocca è un asset**, non
un'informazione anagrafica — ci sono tutti e tre più giorni a settimana, e per
i siti vetrina è territorio a costo zero. **I picchi di MediaWorld cadono a
novembre e dicembre**, cioè nei due mesi in cui l'obiettivo P.IVA dovrebbe
chiudersi. E **l'Osmo Action di Patrick è l'unico strumento in casa
completamente inutilizzato**: una demo filmata di DenkiShift si manda su
WhatsApp prima della chiamata e scalda il lead senza consumare ore.

## Ottavo giro — il Mac di Patrick

Scritta [[setup-macchina-nuova]]: procedura completa per rendere il MacBook di
Patrick una macchina di lavoro a tutti gli effetti — brain, repo, push su
GitHub e migrazioni.

Due cose emerse preparandola:

- ⚠️ **«Push su Supabase» esiste solo su [[opero]].** Su [[denkishift]] le
  migrazioni si incollano a mano nel SQL Editor: cercare un comando che non
  c'è è mezz'ora persa
- ✅ Controllato `.env.production` di OperO, che è **tracciato da git**: contiene
  solo URL e chiave *anon*, committati apposta perché Netlify compila dal
  repository e quei valori finiscono comunque nel bundle. La `service_role` non
  è lì dentro. Entrambi i `.gitignore` coprono correttamente i file veri

## Aperto adesso

- ⬜ **Decidere chi si autentica sul Mac** — Nicola o Patrick →
  [[setup-macchina-nuova]]
- ⬜ **Chiamare la lista**, cominciando dalle RSA
- ⬜ **Estendere la lista a 130-150 contatti** — le 51 attuali bastano 2 giorni
- ⬜ `TODO` — Nicola lavora dal MacBook di Patrick? → [[team-e-vincoli]]
- ⬜ **Provare lo script su 40 chiamate** di un solo segmento
- ⬜ **Come si trattano le royalty 1-2%** senza P.IVA → [[vincoli-fiscali]]
- ⬜ **Cosa c'è in galleria oggi**, e aggiungerci [[albybike]] con una
  testimonianza → [[sito-denkicode]]
- ⬜ Numeri della settimana in [[metriche]]
- ⬜ Secondo cliente di Seba, appena si sa

## Prossimi passi

- [ ] Nicola: installare Obsidian e aprire questa cartella (vedi `README.md`)
- [ ] Creare il repo privato su GitHub e fare il primo push
- [ ] Riempire i sette `TODO` qui sopra — bastano dieci minuti in due
- [ ] Primo lavoro vero: attaccare [[generazione-lead]]

## Non verificato

- Il repo del sito [[sito-albybike]] non è stato trovato: potrebbe essere
  privato o non esistere
- I numeri di [[opero]] (~60%, stato aree) vengono dai `docs/` del repo,
  aggiornati al 21-27 agosto: non li ho verificati eseguendo l'app
- `sebapp-bolanos`, l'app vecchia del cliente, non è stata aperta

## Collegamenti

[[stato-azienda]] · [[generazione-lead]] · [[opero]] · [[denkishift]]
