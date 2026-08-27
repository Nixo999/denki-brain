---
type: progetto
status: attivo
client: interno
stack: [next-16, react-19, typescript, tailwind-4, supabase, capacitor-8, zod]
started: TODO
deadline: TODO
updated: 2026-08-28
source: repo
prezzo: 2 €/dipendente/mese
clienti-paganti: 0
---

# DenkiShift — gestione turni

Pianificazione turni per aziende con squadre a orario variabile: negozi,
magazzini, ristorazione. Il responsabile costruisce la settimana, ogni
dipendente vede la sua. **Prodotto di punta**, nostro, non di un cliente.

**Repo**: `github.com/Nixo999/smooth-duty` (npm: `turni`, ramo `main`)
**Nome**: il repo si chiama ancora `smooth-duty`, il prodotto è **DenkiShift**.
Da rinominare. Dominio **`denkishift.it`** già configurato su Supabase.
**Memoria tecnica**: `CLAUDE.md` + `docs/` (8 file) nel repo.

## Lo stato vero

> [!warning] "Già pronto" è ottimismo commerciale
> Il materiale di vendita dice che il software è pronto. **Non è installabile
> in produzione presso un cliente.** Gira in locale e su un APK di debug
> puntato alla rete di casa di Nicola. È dimostrabile in demo, non consegnabile.
> Chi vende deve saperlo, o promette una data che non esiste.

Quello che **c'è ed è solido**: tutti i motori di calcolo, scritti come
funzioni pure e coperti da **132 controlli automatici** (`npm run prove`), che
girano senza browser e senza database. Copertura, prospetto, importazione
Excel/CSV, trascinamento, generazione, pubblicazione.

## Cosa manca per vendere

| Blocco | Perché blocca |
|---|---|
| **SMTP proprio** | Senza, poche mail all'ora e i modelli non si possono modificare. Il recupero password funziona **solo nello stesso browser** da cui è partita la richiesta — inutilizzabile per una squadra vera |
| **UI della generazione turni** | Il motore c'è e funziona, ma non lo chiama nessuno: manca il bottone, l'anteprima e la Server Action |
| **Notifiche fuori dall'app** | Né mail né push. Un turno pubblicato non avvisa nessuno |
| **Pubblicazione su indirizzo pubblico** | L'app non è ancora online |
| **App sugli store** | Guscio Capacitor Android + APK di debug. iOS mai impostato |
| **Storico e archiviazione** | Non c'è modo di chiudere un anno |

⚠️ **Otto schermate sono state scritte sul Mac e mai viste a schermo** (niente
`.env.local` su quella macchina). Passano build, lint e i 132 controlli — che
non è la stessa cosa. L'elenco ordinato sta in `docs/08-aperto.md`.

## Come si vende, oggi

Prodotto **C** del listino ([[prodotti-e-listino]]). Giulia fa leva
sull'ottimizzazione del personale (ferie, malattie, coperture) e spinge per una
demo dal vivo o in call, gestita da Patrick. Supporto: i **200 biglietti da
visita** dedicati ([[materiale-offline]]).

Prezzo: **~2 €/mese per dipendente**, pagato dal datore di lavoro.
Provvigione Giulia: **TBD**, e non è bloccante ([[ruoli-e-responsabilita]]).

**Clienti paganti al 2026-08-28: zero.** Obiettivo a 6 mesi: **20**
([[obiettivi-6-mesi]]).

> [!note] Analisi di Claude — 2026-08-28
> A 2 €/dipendente, 20 clienti da 15 dipendenti fanno **600 €/mese** ricorrenti.
> È il ricavo più interessante che avete a listino, ed è anche l'unico che non
> richiede di rivendere nulla il mese dopo. Ma un cliente installato che poi non
> riceve la mail di recupero password è un cliente che chiama Patrick ogni
> settimana: **l'SMTP è un blocco commerciale, non tecnico**.

## Sicurezza — cosa c'è già

Fatto il 26 agosto 2026: tetto ai tentativi di accesso (10/15 min per
indirizzo, 50/15 min per rete), password minimo 10 caratteri, errori generici
che non rivelano chi lavora in azienda, security headers (`X-Frame-Options`,
`Referrer-Policy`, `Permissions-Policy`), `X-Powered-By` rimosso.

Dichiarato assente: CSP completa, secondo fattore.

L'app protegge **causali di malattia e legge 104**: è un dato sensibile, e in
una trattativa è un argomento a favore, non un dettaglio.

## Aperto

- [ ] Configurare **SMTP proprio** su Supabase → sblocca il recupero password
- [ ] Rinominare repo e progetto npm in `denkishift`
- [ ] Provare nel browser le 8 schermate mai viste
- [ ] Interfaccia della generazione automatica
- [ ] Pubblicare su `denkishift.it`
- [ ] Definire la provvigione di Giulia sul prodotto turni — non bloccante
- [ ] Primo cliente pilota — anche gratis, per avere un caso reale

## Collegamenti

[[prodotti-e-listino]] · [[stack]] · [[convenzioni]] · [[obiettivi-6-mesi]] ·
[[flusso-vendita]] · [[materiale-offline]]
