---
riga: Il prodotto che Sebastian rivende, non un gestionale nostro. Chi tocca il Super Admin tocca il suo conto economico.
type: progetto
status: attivo
client: sebastian-torres
stack: [react-19, typescript, vite-8, tailwind-3, react-router-7, tanstack-query, supabase, capacitor-6]
started: 2026-07-20
deadline: TODO
updated: 2026-09-11
source: repo
valore: 2400
incassato: 400
---

# OperO — gestionale cantieri e fatturazione

⚠️ **OperO non è il gestionale di un nostro cliente: è il prodotto che il
nostro cliente sta lanciando.** Committente: **[[sebastian-torres]]**, un
privato che sta aprendo la sua attività, e la sua attività è questa app. Noi
siamo i suoi sviluppatori; lui la rivende alle aziende.

```
DenkiCode ──sviluppa──▶ OperO ──venduto da Seba a──▶ aziende
                                                      └─ 1ª: l'impresa del padre
                                                      └─ 2ª: in attesa
```

Cosa fa il software: gestionale **multi-azienda** per imprese di
**facchinaggio, allestimenti e traslochi**. La segreteria gestisce clienti,
cantieri, squadre, conti dei lavoratori e la fatturazione.

Il "multi-azienda" e l'area Super Admin con il cruscotto di **quanto ogni
workspace paga a OperO** (`lib/pianoWorkspace.ts`, listino datato in
`workspace_plans`) non sono funzioni di comodo: **sono il modello di ricavo di
Seba**. Chi le tocca sta toccando il suo conto economico.

**Repo**: `github.com/Nixo999/opero-sito` (npm: `opero-core`)
**OperO 1**: `github.com/SebastianOperO/sebapp-bolanos`, clonato in
`~/lavoro/sebapp-bolanos`. **Sola lettura**: è la specifica, e il suo `types.ts`
è l'unico posto dove lo schema di produzione è scritto
**Memoria tecnica**: `CLAUDE.md` + `docs/handoff.md` nel repo — 4.400 righe di
storico. Leggerli prima di toccare qualsiasi cosa.

## Cos'è davvero

Non è un'app nuova: è la **ricostruzione pulita** di `sebapp-bolanos`, costruita
con **Lovable**, che è **in produzione oggi presso l'impresa del padre di
Seba** — la sua prima installazione reale, non un prototipo. La regola fondante
era *stessa app, codice migliore* — nessuna funzione in più, nessuna in meno, e
l'app vecchia resta la specifica di riferimento.

⚠️ **Dall'11 agosto 2026 quella regola non regge più**: il committente ha
iniziato a chiedere funzioni che nella vecchia app non esistono (sospensione
utenti, ruoli personalizzati, preferiti, liste super admin, notifiche con
immagini, creazione account). Vedi [[2026-08-11-opero-scope-allargato]].

## Soldi

| | |
|---|---|
| Prezzo pattuito | **2.400 €** |
| Incassato al 2026-08-28 | **400 €** |
| **Da incassare** | **2.000 €** |
| I 400 € già presi | **Senza ricevuta** — accordo fra privati |
| I 2.000 € futuri | Ricevuta per prestazione occasionale intestata a **Patrick** → [[vincoli-fiscali]] |

⚠️ I 2.000 € futuri si mangiano il **40%** del tetto annuo di Patrick in un
colpo solo. I 400 € già presi non lo toccano, perché non è stata emessa nessuna
ricevuta.

⚠️ **Il credito dipende dall'impresa di Seba, non da un budget IT.** Lui ha un
cliente pagante (suo padre) e un secondo in attesa. Se quel secondo non firma,
i 2.000 € non hanno una fonte evidente. Non è un giudizio su di lui: è la
ragione per cui vale la pena sapere a che punto è quella trattativa. Vedi
[[sebastian-torres]].

## A che punto siamo

**~60%** (rilevazione del 21 agosto 2026, dal repo). Quattro aree vive sul
database:

| Area | Cosa fa |
|---|---|
| **Segreteria** | Clienti, tariffe, cantieri, conti, fatture PDF/Excel |
| **Lavoratore** | Turni, chiusura chiamata, ore, calendario, rubrica ufficio |
| **Visualizer** | Lavori, conti, disponibilità — sola lettura |
| **Admin** | Utenti, tipo lavoratore, Plus, aziende, cruscotto workspace |

**Non iniziati**: lavoratori provvisori, app native compilate. La **migrazione
dello storico** ha il piano e la mappatura, non ha l'accesso ai dati.

> [!warning] La migrazione dello storico è il rischio numero uno
> Il piano la dava chiusa a fine settimana 1. È l'unico pezzo che al go-live non
> si può rimandare. **Piano e mappatura esistono dall'11 settembre 2026**, in
> `docs/migrazione-storico.md` del repo: 44 tabelle di OperO 1 contro 38 di
> OperO 2, 25 in comune, nove copiabili così come sono.
>
> Due correzioni a quello che si diceva qui: **non ci sono «dati di anni»** (le
> migrazioni di OperO 1 partono dal 16 aprile 2026, quindi al massimo cinque
> mesi), e **Seba vuole solo da settembre in poi** (11/09/2026), prima di quella
> data non gli interessa.
>
> ⛔ **Il blocco non è più tecnico, è l'accesso.** Il progetto Supabase di
> produzione è ancora agganciato a **Lovable** e nessuno di noi ha mai avuto la
> password: senza una via d'accesso ai dati non esiste nessun import. Le due
> strade, e il prezzo della seconda (tutto l'ufficio resetta la password), stanno
> nel §2 di quel documento.

## Il piano consegnato vs la realtà

Il PDF *"Piano di Sviluppo e Migrazione Software (V2)"* consegnato al cliente
dichiara: **inizio 20 luglio 2026, fine indicativa 21 agosto 2026**.

Siamo oltre quella data. Secondo Nicola (28 agosto) **la scadenza non è più
stringente**: il lavoro attuale è correzione su segnalazione, non sviluppo.

⚠️ **Il documento consegnato al cliente non è mai stato corretto** e promette
ancora Chat, Disponibilità, XML FatturaPA e area Direzione. Chat e Direzione
sono fuori scope per decisione del committente stesso; Disponibilità è
rientrata il 20 agosto. Al go-live quelle voci risulteranno **mancanti anziché
rinunciate**, e la differenza la nota il cliente, non noi.

## Lo scope si muove — cronologia

| Data | Cosa è successo |
|---|---|
| 2026-08-04 | Committente toglie Chat e Disponibilità |
| 2026-08-05 | Committente toglie XML FatturaPA e area Direzione |
| 2026-08-11 | Chiede funzioni **nuove**, non presenti nella vecchia app |
| 2026-08-20 | Disponibilità **rientra**, sviluppata in giornata |
| 2026-08-22 | **XML SDI richiesto di nuovo** → [[2026-08-22-xml-sdi-da-quotare]] |
| 2026-08-25/27 | Tre liste di segnalazioni in tre giorni |
| 2026-08-29 | **OperO Choice**: messaggio a schermo pieno scelto dal Super Admin. Chiesto a voce, non esiste in OperO 1 → **lavoro nuovo da quotare**, come l'XML SDI |

## Il ritmo attuale, e cosa dice

Dal 25 al 27 agosto sono arrivate **tre liste di segnalazioni** dal
committente. Nella seconda, **tre punti su nove erano regressioni** introdotte
dal lavoro consegnato poche ore prima. Nella terza, **cinque punti su dieci**
nascevano da un'unica regola mancante ("l'autista esterno guida e basta").

> [!note] Analisi di Claude — 2026-08-28
> Il pattern è consegna rapida → il cliente prova → segnala anche quello che
> abbiamo appena rotto. Non è cattiva volontà del cliente: è che consegniamo
> senza un giro di verifica nostro, e il collaudo lo sta facendo lui. Costa
> credibilità in un progetto già oltre la data. Il repo lo dice esplicitamente:
> *"Non erano difetti vecchi scoperti da lui — li ha trovati perché avevamo
> consegnato."*

## Ambienti

| Ambiente | Progetto Supabase | Nota |
|---|---|---|
| Produzione cliente | `avsuihlxecpbmddhnyvo` | Usata da `sebapp-bolanos`. **Mai toccare** |
| Sviluppo | `oyoltwisdwujitsryzax` | Collegato al repo, è anche il sito di prova |

**Nessun test automatico** in questo progetto: la verifica è nel browser,
misurando con `getComputedStyle` / `getBoundingClientRect`. Vedi [[convenzioni]].

## Aperto

- [ ] Incassare i **2.000 €** residui — ricevuta su Patrick
- [ ] **Quotare l'XML SDI** come lavoro nuovo, non regalarlo
- [ ] **Correggere il PDF consegnato** al cliente sulle funzioni rinunciate
- [ ] **Migrazione dello storico: chiedere a Seba l'accesso al database.** È l'unica cosa che blocca, piano e mappatura sono scritti
- [ ] Lavoratori provvisori (4 tabelle + edge function)
- [ ] Applicare la migrazione `20260826110000` (trigger finestra)
- [ ] Decidere una data di go-live e dirla al cliente

## Collegamenti

[[sebastian-torres]] · [[stack]] · [[convenzioni]] · [[vincoli-fiscali]] ·
[[2026-08-11-opero-scope-allargato]] · [[2026-08-22-xml-sdi-da-quotare]]
