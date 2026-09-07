---
type: progetto
status: in-pausa
client: ng-barber
stack: [html, gsap, netlify]
started: 2026-09-01
deadline: TODO
updated: 2026-09-07
source: claude
valore: TODO
incassato: 0
---

# Sito NG Barber Studio — demo non commissionata, e già pubblica

Bozza vetrina per [[ng-barber]], riga 2 dell'anello 1-b delle liste Instagram,
gancio 5. Costruita la notte del 1 settembre 2026 con lo schema di
[[sito-castiglione]] ma **senza Apify**: profilo e 12 post presi dall'endpoint
web di Instagram via `curl`, 13 foto scaricate subito.

Nota scritta il 7 settembre 2026: il progetto viveva solo in quattro righe del
[[registro-interventi]], scritte come testo semplice invece che come wikilink,
quindi non lo segnalava nemmeno un link rotto.

## Com'è fatto

Scroll-telling scuro su un `index.html`. Il **globo wireframe del loro logo
rifatto in SVG** fa da filo narrativo: si disegna nel sipario, ruota dietro
l'hero, e nel capitolo delle sedi (l'unico pin della pagina) accende
Como → Erba → Mendrisio allo scrub. Archivo variable esteso come il loro
wordmark, Ephesis per lo script della locandina, ottone preso da lì. Marquee
servizi e un BOOK NOW che punta alla loro app di prenotazione white-label: il
sito dà l'identità, il booking resta loro.

Dal materiale sono uscite tre cose che la lista non aveva: la **terza sede a
Mendrisio (CH)**, il telefono `+39 345 509 3200`, l'esistenza di masterclass.

## Dove sta — e qui c'è un nodo

| Cosa | Dove |
|---|---|
| Cartella | `Desktop/ngbarber-site` (Mac di Patrick) |
| Repo 1 | `Nixo999/ngbarber-site` — **privata**, 1 commit indietro |
| Repo 2 | `patricksappa26/ng-barber` — **pubblica**, è quella pushata |
| Database | nessuno, è statico |
| Hosting | Netlify preparato (`netlify.toml`, `robots.txt`), **login mai fatto** |

⚠️ **Le due repo divergono e non si possono allineare da qui**: la privata è di
Nicola, l'account `gh` attivo su quel Mac è Patrick, e GitHub risponde
`Repository not found`. O si sceglie quale delle due è la buona, o la privata
resta una copia vecchia.

⚠️ `profilo-raw.json`, il dump grezzo dello scraping, è finito nel commit
iniziale di **tutte e due** le repo, una delle quali è pubblica. Controllato:
nessun dato sensibile dentro. Tolto dal tracking e messo in `.gitignore`, ma
**resta nella storia**: toglierlo davvero vuole riscrittura e force push.

## Aperto

- ⬜ Il sito è pubblico come sorgente ma **non pubblicato**: Netlify non ha mai
  visto un login.
- ⬜ Quando si pubblica valgono i tre sbarramenti anti-indicizzazione di
  [[netlify]], che si tolgono solo quando il sito diventa loro.
- ⬜ Mai proposto al lead. Prezzo mai detto. `TODO`.

## Collegamenti

[[ng-barber]] · [[sito-castiglione]] · [[trappole]] · [[netlify]] ·
[[2026-09-01-instagram-anello-1-b]] · [[registro-interventi]] · [[processo-siti]]
