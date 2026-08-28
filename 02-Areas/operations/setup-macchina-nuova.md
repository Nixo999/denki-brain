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

Questo semplifica tutto e toglie il problema più grosso: **le credenziali di
Nicola non finiscono su una macchina che non è la sua.** Ognuno pusha col
proprio nome, e nella storia di git si vede chi ha fatto cosa.

### Cosa serve a Patrick, e cosa no

| | Serve? | Perché |
|---|---|---|
| Il **second brain** | ✅ Sì | È la sua metà del vault: clienti, soldi, strategia |
| **Claude Code** | ✅ Sì | Per interrogare il brain e farsi scrivere script e liste |
| **Obsidian** | ✅ Sì | Per leggere il vault senza il terminale |
| I repo **`smooth-duty`** e **`opero-sito`** | ⚪ Solo se serve | Patrick non scrive codice. Si clonano il giorno in cui gli servono davvero |
| Le chiavi **Supabase** e i file `.env` | ❌ No | Non gli servono, e ogni copia in più di una chiave è un rischio in più |

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

## 5. Supabase — attenzione, «push» esiste solo su OperO

> [!warning] I due progetti si comportano in modo diverso
> **OperO** usa la CLI: `npx supabase db push` applica le migrazioni.
>
> **DenkiShift no.** Le sue migrazioni **si incollano a mano nel SQL Editor**,
> in ordine numerico, e non esiste una tabella che registri cosa è già stato
> eseguito (`docs/08-aperto.md`). Cercare un comando che non c'è è il modo più
> rapido di perdere mezz'ora.

**Per OperO:**
```bash
supabase login
cd ~/denkicode/opero-sito
supabase link --project-ref oyoltwisdwujitsryzax
```
`link` chiede la password del database e ricrea `supabase/.temp/`, che non sta
in git. Da qui:
```bash
npx supabase db push                                                  # migrazioni
npx supabase gen types typescript --linked > src/lib/database.types.ts  # tipi
```

**Per DenkiShift**, il comando da lanciare dopo ogni `git pull` è un altro — e
va lanciato sempre:
```bash
cd ~/denkicode/smooth-duty
node --env-file=.env.local --env-file=.env.db scripts/verifica-schema.mjs
```
Dice se il database è allineato al codice. Senza, un tabellone vuoto sembra un
tabellone cancellato.

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

Scaricare Obsidian da `obsidian.md`, poi **Open folder as vault** →
`~/denkicode/denki-brain`.

Plugin e impostazioni arrivano già col repository. Da installare a parte solo
**Obsidian Git**, con *Pull updates on startup* acceso — vedi la sezione 7 del
`README.md`.

---

## 7-bis. Il percorso breve per Patrick

Se serve solo il brain — che è il caso di Patrick — bastano questi passaggi:
**1** (solo `xcode-select` e Homebrew), **2**, **3** (solo `denki-brain`), il
blocco Claude Code qui sotto e **7**. Gli altri si saltano.

### Installare Claude Code

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Non richiede Node: si installa da sé. Se al comando successivo il terminale
risponde `command not found`, il percorso non è ancora nel `PATH`:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc
```

Poi, **dentro la cartella del brain**:

```bash
cd ~/denkicode/denki-brain
claude
```

Al primo avvio chiede di accedere — si apre il browser — e se ci si fida della
cartella: **sì**, l'abbiamo scritta noi.

⚠️ **Claude Code richiede un abbonamento Claude a testa.** Non è condivisibile
fra due persone, quindi è un costo ricorrente in più da mettere in conto
insieme a quelli di [[vincoli-fiscali]].

### La prima cosa da scrivere

Il vault ha il suo `CLAUDE.md`: alla prima riga di conversazione Claude sa già
chi siamo, cosa stiamo facendo e quanto ci devono. A Patrick basta scrivere:

> «Sono Patrick. Leggi il CLAUDE.md e dimmi a che punto siamo.»

## 8. Il rituale, da qui in avanti

Vale su tutte le macchine, ed è la stessa regola che sta nei repo di codice:

1. **`git pull` prima di cominciare**, e di nuovo prima di ogni push
2. Su DenkiShift, dopo il pull: `verifica-schema.mjs`
3. **Commit piccoli, push subito.** Il lavoro tenuto in locale mezza giornata è
   il lavoro che poi non entra
4. **Il push non passa? Non forzare.** `git pull --rebase` e si guarda

I fine riga sono già normalizzati dal `.gitattributes` del vault: Windows e Mac
non si contenderanno le note.

## Collegamenti

[[team-e-vincoli]] · [[convenzioni]] · [[opero]] · [[denkishift]] ·
[[sebastian-torres]] · [[stack]]
