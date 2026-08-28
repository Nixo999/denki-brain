---
type: area
updated: 2026-08-28
source: claude
---

# Mettere in piedi una macchina nuova

Scritto per il **MacBook Air di Patrick**, ma vale per qualunque macchina nuova.
Al termine, da quella macchina si può: aprire il second brain, lavorare sui
progetti, pushare su GitHub e applicare le migrazioni su Supabase.

⏱️ Circa un'ora, quasi tutta di attesa sui download.

---

## 0. Chi lavora su quella macchina

**Deciso il 28 agosto 2026: Patrick usa il proprio account.** Ha un account
GitHub suo, già collegato ai repository come collaboratore.

| | Valore |
|---|---|
| Utente GitHub | `patricksappa26` |
| Email dei commit | `patricksappa26@gmail.com` |

Questo semplifica tutto e toglie il problema più grosso: **le credenziali di
Nicola non finiscono su una macchina che non è la sua.** Ognuno pusha col
proprio nome, e nella storia di git si vede chi ha fatto cosa.

### Cosa serve a Patrick, e cosa no

| | Serve? | Perché |
|---|---|---|
| Il **second brain** | ✅ Sì | È la sua metà del vault: clienti, soldi, strategia |
| **Claude Code** | ✅ Sì | Per interrogare il brain e farsi scrivere script e liste |
| **Obsidian** | ✅ Sì | Per leggere il vault senza il terminale |
| I repo **`smooth-duty`** e **`opero-sito`** | ⚪ Solo se serve | Patrick non scrive codice. Si clonano il giorno in cui gli servono davvero — **e quel giorno è arrivato**, vedi 7-ter |
| Le chiavi **Supabase** e i file `.env` | ⚠️ Una alla volta | Ognuna si aggiunge quando serve, per un progetto alla volta, mai in blocco. Vedi [[2026-08-28-supabase-denkishift-sul-mac]] |

> [!note] Analisi di Claude — 2026-08-28
> **Non installare a Patrick quello che non gli serve** non è pigrizia: la
> `service_role` di OperO vede i dati di tutte le aziende del cliente, causali
> di malattia comprese. Una copia in meno in giro è una copia in meno da
> rigenerare il giorno in cui un portatile sparisce.
>
> Se un domani Patrick dovrà davvero far girare i progetti, si aggiunge allora —
> i passaggi 4, 5 e 6 restano scritti qui apposta.

⚠️ Da fare comunque, su qualunque macchina che porta in giro dati di clienti:
**FileVault acceso** (*Impostazioni → Privacy e sicurezza → FileVault*). Senza,
chi ha il portatile in mano legge il disco.

## 1. Gli strumenti di base

Terminale, uno alla volta.

**Command Line Tools di Xcode** — porta `git`:
```bash
xcode-select --install
```

**Homebrew**, se non c'è già:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
A fine installazione stampa due righe da incollare per aggiungere `brew` al
`PATH` sui Mac Apple Silicon. **Vanno incollate**, o il comando successivo non
viene trovato.

**Il resto in un colpo solo:**
```bash
brew install node@22 gh supabase/tap/supabase
brew install --cask temurin@21
```

| Cosa | A cosa serve |
|---|---|
| `node@22` | Far girare i progetti. Next 16 e React 19 vogliono Node 20+ |
| `gh` | Autenticarsi su GitHub senza smanettare con le chiavi SSH |
| `supabase` | Applicare le migrazioni — **solo su OperO**, vedi punto 5 |
| `temurin@21` | JDK per compilare l'APK Android di DenkiShift |

Verifica:
```bash
node -v && gh --version && supabase --version && java -version
```

---

## 2. GitHub

```bash
gh auth login
```

Rispondere: **GitHub.com** → **HTTPS** → **sì**, autentica git con le
credenziali → **Login with a web browser**. Si incolla il codice nel browser e
si conferma.

Poi:
```bash
gh auth setup-git
```

Da qui in avanti `git push` funziona su tutti i repository senza chiedere nulla.

Verifica:
```bash
gh auth status
```

### 2-bis. L'identità dei commit — passaggio separato, e si dimentica

`gh auth login` autentica il **push**; non dice a git **chi firma** il commit.
Sono due cose distinte, e senza la seconda il primo `git commit` si ferma con
*«Please tell me who you are»*.

```bash
git config --global user.name "patricksappa26"
git config --global user.email "patricksappa26@gmail.com"
```

Verifica — deve stampare il nome giusto:
```bash
git var GIT_AUTHOR_IDENT
```

> [!warning] Se su una macchina resta l'account di un altro
> `gh auth status` dice a nome di **chi parte il push**. Se su un Mac di
> Patrick risponde `Nixo999`, l'autenticazione è ancora quella di Nicola: il
> commit risulterà di Patrick ma il push di Nicola, e la separazione decisa
> sopra salta a metà. Si sistema con `gh auth login` sull'account giusto
> (`gh auth switch` se sono entrambi presenti).

---

## 3. Clonare i tre repository

```bash
mkdir -p ~/denkicode && cd ~/denkicode
git clone https://github.com/Nixo999/denki-brain.git
git clone https://github.com/Nixo999/smooth-duty.git
git clone https://github.com/Nixo999/opero-sito.git
```

⚠️ `opero-sito` è **privato**: senza il passaggio 2 questo comando fallisce.

Poi le dipendenze, che sono un paio di minuti a testa:
```bash
cd ~/denkicode/smooth-duty && npm install
cd ~/denkicode/opero-sito && npm install
```

---

## 4. I file `.env` — l'unica cosa che git non porta

Sono fuori dal versionamento apposta, e vanno ricreati a mano.

**DenkiShift** (`~/denkicode/smooth-duty`) — i modelli sono già nel repo:
```bash
cp .env.local.example .env.local
cp .env.db.example .env.db
```
Poi si riempiono. I valori stanno nel pannello Supabase del progetto
`rytuurzafjxzlrpgforj` (*Project Settings → API*), oppure si copiano dal PC
Windows di Nicola.

**OperO** (`~/denkicode/opero-sito`) — qui il modello non c'è, si crea:
```bash
cat > .env.local <<'FINE'
VITE_SUPABASE_URL=https://oyoltwisdwujitsryzax.supabase.co
VITE_SUPABASE_ANON_KEY=<la chiave anon del progetto di sviluppo>
FINE
```
⚠️ **Il progetto di sviluppo è `oyoltwisdwujitsryzax`.** Quello di produzione
del cliente, `avsuihlxecpbmddhnyvo`, **non si tocca mai** — è l'app che Seba usa
davvero presso l'impresa del padre.

### Come si trasferiscono i valori

**Mai su WhatsApp, mai per email.** Una chiave incollata in chat resta nella
cronologia di due telefoni e in un backup cloud, per sempre.

Le due strade sane: **rileggerli dal pannello Supabase** direttamente sul Mac
(è la più semplice — sono lì), oppure copiarli con una chiavetta o AirDrop dal
PC di Nicola.

---

## 5. Supabase — «pushare» vuol dire due cose diverse

> [!warning] I due progetti non si aggiornano allo stesso modo
> **OperO** usa la CLI di Supabase: `npx supabase db push`.
>
> **DenkiShift non ha `db push`** — le sue migrazioni non stanno in
> `supabase/migrations/` e non c'è un `config.toml`, quindi la CLI non le vede.
> Ha **un comando suo**, `esegui-sql.mjs`, ed è quello l'equivalente del push.
> Cercare `db push` su DenkiShift è il modo più rapido di perdere mezz'ora.

> [!note] Correzione del 28 agosto 2026
> Fino a oggi qui c'era scritto che le migrazioni di DenkiShift **si incollano a
> mano nel SQL Editor**. È superato: `docs/06-ambiente.md` del repo dice
> testualmente che «si possono eseguire da qui, senza passare dal SQL Editor».
> Sul tecnico ha ragione il repo, e questa nota è stata riallineata.

**Per OperO:**
```bash
supabase login
cd ~/Desktop/opero-sito          # su altre macchine: ~/denkicode/opero-sito
supabase link --project-ref oyoltwisdwujitsryzax
```
`link` chiede la password del database e ricrea `supabase/.temp/`, che non sta
in git. Da qui:
```bash
npx supabase db push                                                  # migrazioni
npx supabase gen types typescript --linked > src/lib/database.types.ts  # tipi
```

### Per DenkiShift — il push si chiama `esegui-sql.mjs`

Due comandi, sempre in quest'ordine. Il primo **dice cosa manca**, il secondo
**lo applica**:

```bash
cd ~/Desktop/smoothduty          # su Windows: C:\Users\User\Desktop\turni

# 1. cosa manca al database rispetto al codice — dopo OGNI git pull
node --env-file=.env.local --env-file=.env.db scripts/verifica-schema.mjs

# 2. applica la migrazione che il comando sopra ha nominato
node --env-file=.env.local --env-file=.env.db scripts/esegui-sql.mjs supabase/17-turno-spostato.sql
```

Le migrazioni stanno in `supabase/`, numerate da `01-` in su, e si eseguono
**in ordine**. Sono ri-eseguibili (`if not exists`, `drop ... if exists`) e
nessuna cancella turni: nel dubbio si rilanciano. Senza il passo 1, un
tabellone vuoto sembra un tabellone cancellato — è già successo il 25 agosto,
con 429 turni spariti alla vista che invece c'erano tutti.

⚠️ **`pg` non è dichiarato nel `package.json` del repo**, ma `scripts/lib-db.mjs`
lo importa: su una macchina appena installata i due comandi qui sopra si
fermano con `Cannot find package 'pg'`. Si rimedia senza sporcare il repo:
```bash
npm install pg --no-save --no-package-lock
```
È una cosa da segnalare a Nicola, non da sistemare per conto proprio: la
correzione vera è una riga nel `package.json`, e sta nel suo repo.

⚠️ **Il database di produzione è un altro progetto.** `denkishift.it` gira su
un progetto Supabase separato da quello di sviluppo, e lì le migrazioni **non
partono col deploy**: prima la migrazione sul database, poi il deploy. Toccare
la produzione è una cosa che si decide, non che si fa di passaggio.

---

## 6. Android — solo se serve compilare l'APK

Il percorso del JDK dentro `android/gradle.properties` è quello di Windows, e
**non va tolto**: serve a rimettere in piedi la build sull'altra macchina. Si
sovrascrive dove Gradle guarda per primo:

```bash
mkdir -p ~/.gradle
echo 'org.gradle.java.home=/Library/Java/JavaVirtualMachines/temurin-21.jdk/Contents/Home' >> ~/.gradle/gradle.properties
```

---

## 7. Il second brain su Obsidian

Scaricare Obsidian da `obsidian.md`, poi **Open folder as vault** → la
cartella del vault. Sul Mac di Patrick **non** sta in `~/denkicode/`: sta in
`~/Desktop/denki-brain`. Funziona identico, ma i comandi qui sotto vanno letti
con quel percorso.

Plugin e impostazioni arrivano già col repository. Da installare a parte solo
**Obsidian Git**, con *Pull updates on startup* acceso — vedi la sezione 7 del
`README.md`.

---

## 7-bis. Il percorso di Patrick — con o senza terminale

Claude Code esiste **anche come applicazione desktop** per Mac e Windows, oltre
che da terminale, dal web (`claude.ai/code`) e come estensione per gli editor.
Stesso motore, stesso vault, stesso `CLAUDE.md`, stessi slash command: cambia
solo l'involucro.

⚠️ **Sul Mac di Patrick la versione da terminale è già installata e funziona**
(vedi 7-ter). Quanto segue non è da rifare: serve a decidere se passare
all'app, e a impostare la prossima macchina.

### Quale conviene a chi

| | Desktop | Terminale |
|---|---|---|
| **Patrick** | ✅ Non scrive codice e non ha nulla da guadagnare dal terminale. Vede le modifiche ai file in modo leggibile invece che come testo che scorre | Funziona, ed è quello che ha oggi |
| **Nicola** | Va bene per il vault | ✅ Per i progetti: `npm run dev`, gli script, il pannello browser |

### Il percorso senza terminale, per una macchina nuova

| # | Cosa | Dove |
|---|---|---|
| 1 | **GitHub Desktop** | `desktop.github.com` |
| 2 | **Claude Code**, versione desktop | dal sito di Claude Code |
| 3 | **Obsidian** | `obsidian.md` |
| 4 | Nel vault, il plugin **Obsidian Git** | dentro Obsidian |

**1 — GitHub Desktop.** Si accede col proprio account, poi *Clone a repository*
→ `Nixo999/denki-brain`. Porta con sé anche `git`, che serve al plugin di
Obsidian. Da qui in avanti «scaricare le novità» e «mandare le modifiche» sono
due bottoni, e il `pull --rebase` del punto 8 lo gestisce lui.

⚠️ GitHub Desktop autentica il push **e** imposta l'identità dei commit: sostituisce
sia il punto 2 sia il 2-bis. È il motivo principale per preferirlo su una
macchina non tecnica.

**2 — Claude Code desktop.** Si accede col proprio account Claude e si apre la
cartella del vault. Legge il `CLAUDE.md` da solo.

**3 e 4 — Obsidian** con *Open folder as vault* sulla stessa cartella, più il
plugin **Obsidian Git** con *Pull updates on startup* acceso: il vault si
allinea da sé all'apertura.

⚠️ Se nell'app desktop non compaiono `/chiudi-sessione`, `/settimana` e gli
altri, dirlo: stanno in `.claude/commands/` dentro il vault e dovrebbero essere
letti allo stesso modo, ma va verificato una volta invece che dato per scontato.
Da terminale, sul Mac di Patrick, si vedono tutti e cinque.

### Il percorso da terminale

```bash
curl -fsSL https://claude.ai/install.sh | bash
cd ~/Desktop/denki-brain   # su altre macchine: ~/denkicode/denki-brain
claude
```
Se risponde `command not found`:
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc
```

⚠️ **Claude Code richiede un abbonamento Claude a testa**, non è condivisibile
fra due persone. È un costo ricorrente da mettere accanto a quelli di
[[vincoli-fiscali]].

### La prima cosa da scrivere

Il vault ha il suo `CLAUDE.md`: alla prima riga di conversazione Claude sa già
chi siamo, cosa stiamo facendo e quanto ci devono. A Patrick basta:

> «Sono Patrick. Leggi il CLAUDE.md e dimmi a che punto siamo.»

## 7-ter. Dov'è arrivato il MacBook di Patrick

Verificato da quella macchina il **28 agosto 2026**. Si aggiorna quando cambia:
serve a sapere cosa manca ancora senza rifare il giro dei comandi.

| Pezzo | Stato |
|---|---|
| Vault `denki-brain` | ✅ In `~/Desktop/denki-brain`, `main` allineato a `origin`, 47 note |
| Claude Code | ✅ v2.1.248, legge il vault e i cinque slash command |
| `git`, `node`, `gh`, Homebrew | ✅ Installati |
| Identità dei commit | ✅ `patricksappa26` — impostata il 28/08, prima mancava del tutto |
| **Push verso `origin`** | ✅ **Funziona** — verificato il 28/08 con un push reale dal Mac |
| `gh auth` | ⚠️ Autenticato come **`Nixo999`**: il push parte ancora a nome di Nicola |
| Obsidian | ❌ Non installato — il vault si legge solo dal terminale |
| Claude Code desktop | ⚪ Non installato: c'è la versione da terminale, che basta |
| Repo di codice | ✅ **Presenti**, sul Desktop e non in `~/denkicode/`: `smoothduty`, `opero-sito`, `opero-core`, `capacitor` |
| Chiavi di **OperO** | ⚠️ `opero-sito/.env.local` è già su questa macchina |
| Chiavi di **DenkiShift** | 🟡 File `.env.local` e `.env.db` predisposti il 28/08, **da riempire**: mancano anon key, service_role e password del database |
| Migrazioni DenkiShift da qui | 🟡 Catena provata fino al database — l'host `aws-1-eu-west-1.pooler.supabase.com` risponde, si ferma solo sulla password |

> [!note] Analisi di Claude — 2026-08-28
> Le righe non verdi non bloccano il lavoro: da qui si scrive nel vault, si
> committa e si pusha — il push è stato provato davvero, non dedotto. Ma finché
> `gh` resta su `Nixo999`, metà della decisione del 28 agosto non è applicata:
> l'autore del commit dice Patrick, il push dice Nicola, e su GitHub i commit
> risultano *pushati da* Nicola. `patricksappa26` è già collaboratore del repo
> con permesso di scrittura (verificato il 28/08), quindi il cambio non toglie
> l'accesso a nulla: è un `gh auth login` da fare a mano, dal browser. Nessuno
> può farlo al posto suo — nel terminale di Claude Code si scrive
> `! gh auth login` e si segue la procedura del punto 2.

## 8. Il rituale, da qui in avanti

Vale su tutte le macchine, ed è la stessa regola che sta nei repo di codice:

1. **`git pull` prima di cominciare**, e di nuovo prima di ogni push
2. Su DenkiShift, dopo il pull: `verifica-schema.mjs`
3. **Commit piccoli, push subito.** Sul vault non è più un consiglio ma la
   regola: *ogni* modifica si pusha, anche una riga, salvo che non venga detto
   il contrario — vedi [[2026-08-28-push-automatico]]. Il lavoro tenuto in
   locale mezza giornata è il lavoro che poi non entra
4. **Il push non passa? Non forzare.** `git pull --rebase` e si guarda

Sul vault il punto 3 è anche automatico: `.claude/settings.json` monta un hook
che a fine turno controlla se è rimasto qualcosa da pushare e lo segnala. Sta
nel repo, quindi arriva su ogni macchina col `git clone`: non c'è niente da
installare a mano.

I fine riga sono già normalizzati dal `.gitattributes` del vault: Windows e Mac
non si contenderanno le note.

## Collegamenti

[[team-e-vincoli]] · [[convenzioni]] · [[opero]] · [[denkishift]] ·
[[sebastian-torres]] · [[stack]]
