---
riga: Detto da Patrick il 31 agosto 2026 - *«il sito di Castiglione, come tutti i siti bozza, viene messo su Netlify per farlo vedere»*.
type: risorsa
updated: 2026-09-17
source: denkicode
tags: [strumenti, hosting, bozze, siti-vetrina]
---

# Netlify — dove vive una bozza prima di essere venduta

Detto da **Patrick il 31 agosto 2026**: *«il sito di Castiglione, come tutti i
siti bozza, viene messo su Netlify per farlo vedere»*.

Non è un dettaglio tecnico: è **il pezzo di catena commerciale che mancava
scritto**. L'esca di DenkiCode è la bozza ([[flusso-vendita]], flusso A), e una
bozza che sta sul Desktop di Nicola non è un'esca — è un file. Su Netlify
diventa un link che si incolla in WhatsApp, in una mail o in un DM.

## Cosa cambia, in pratica

| Prima della bozza pubblicata | Dopo |
|---|---|
| «gliela preparo e gliela mando» | «guardi, è già qui: [link]» |
| Screenshot in chat | Il sito vero, che scrolla sul suo telefono |
| Il cliente immagina | Il cliente vede |

Agisce su tre dei quattro termini dell'equazione del valore
([[core-crescita-finanze]]): alza la **probabilità percepita**, azzera il
**tempo di attesa**, azzera lo **sforzo** del cliente. È la leva più forte che
abbiamo, ed è anche l'unica su cui il [[core-crescita-finanze]] diceva che
eravamo forti «più di quanto la stiamo usando».

## La regola

**Una bozza esiste quando è online.** Finché è in locale è lavoro fatto e non
consegnato: non si annuncia, non si promette, non si conta.

Vale per tutti i canali:
- **Telefono** — «le mandiamo la bozza» → il link parte su WhatsApp
  ([[script-siti-vetrina]]).
- **DM Instagram** — il link **non va nel primo messaggio** (è il segnale di
  spam più forte che ci sia): entra nel secondo, quando ha risposto
  → [[dm-instagram-vetrina]].
- **Blitz e meeting** — si apre dal telefono di Patrick, non si racconta.

## Le bozze pubblicate

| Bozza | Per chi | Stato |
|---|---|---|
| [[castiglione-furniture]] | Castiglione Falegnameria Sartoriale, Bronte (CT) | `TODO` da pubblicare — il repo è in locale e senza remote ([[2026-08-30-sito-castiglione]]) |
| [[sito-da-caterina]] | Da Caterina Toelettatura Professionale, Olgiate Olona (VA) — Instagram `@dacaterinatoelettatura` | ✅ **online su <https://dacaterina.netlify.app>** dal 9 settembre 2026, sito `dacaterina` sul team `denkicode` (slug API `nicola-la-rezza`), deploy dal CLI non collegato al repo `Nixo999/caterina-site`; tre sbarramenti attivi |
| [[sito-mikuma-dogs]] | Martina Carneli, istruttrice cinofila, Como — Instagram `@mikuma.dogs`, ha già chiesto la bozza | ✅ **online su <https://mikumadogs.netlify.app>** dall'11 settembre 2026, sito `mikumadogs` sul team `denkicode` (slug `nicola-la-rezza`), deploy dal CLI, repo `Nixo999/mikuma-site` privata; tre sbarramenti verificati con `curl` |
| [[sito-pinkploy]] | Nails Art by Pinkploy, onicotecnica, Brescia centro — Instagram `@nails_art_by_pinkploy`, ha già chiesto la bozza | ✅ online su <https://pinkploy.netlify.app> dal 14 settembre 2026, sito `pinkploy` sul team `denkicode` (slug `nicola-la-rezza`), deploy dal CLI, repo `Nixo999/pinkploy-site` privata; tre sbarramenti verificati con `curl` |
| [[sito-laurafranzoni]] | Laura Franzoni, lash maker, Brescia — Instagram `@laurafranzoni_lashmaker`, il DM non è ancora partito | ✅ online su <https://laurafranzoni.netlify.app> dal 14 settembre 2026, sito `laurafranzoni` sul team `denkicode` (slug `nicola-la-rezza`), deploy dal CLI non collegato al repo `Nixo999/laurafranzoni-site` privata; tre sbarramenti verificati con `curl`. ⚠️ **online c'è il giro 2**: il giro 3 (`93081ec`) alle 09:12 del 14/09 è fermo in locale e non ripubblicato |
| [[sito-nails-robyy]] | Roberta, nail artist e educator, Brescia e provincia — Instagram `@nails.robyy`, ha risposto «Ciao ok vediamo» al DM | ✅ online su <https://nailsrobyy.netlify.app> dal 14 settembre 2026, sito `nailsrobyy` sul team `denkicode` (slug `nicola-la-rezza`), deploy dal CLI con `npx --no-install netlify`, repo `Nixo999/nailsrobyy-site` privata; **tre sbarramenti verificati con `curl` il 14/09** (`x-robots-tag`, `robots.txt` con `Disallow: /`, il `meta robots` in pagina), HTTP 200. Online c'è il giro di finitura delle due regressioni (`673d6c6`) |
| [[sito-hairstylebrescia]] | Hair Style Parrucchieri, salone, Brescia — Instagram `@hairstyle_brescia`, gancio sposa, il DM non è ancora partito | ✅ online su <https://hairstylebrescia.netlify.app> dal 16 settembre 2026, sito `hairstylebrescia` sul team `denkicode` (slug `nicola-la-rezza`), deploy dal CLI (binario 27.5.2 nella cache di npx, `--prod --no-build`), non collegato al repo `Nixo999/hairstylebrescia-site` privata; **sbarramenti verificati nei file** (`controlla-sito.py` 8/8), **non con `curl`**: il classificatore dell'auto mode ha bloccato la verifica sul sito vivo, la fa Nicola |
| [[sito-newfantasy]] | New Fantasy Parrucchieri, Lurate Caccivio (CO) — Instagram `@newfantasy_parrucchieri`, DM con autorisposta, il secondo contatto è WhatsApp | ✅ online su <https://newfantasy-parrucchieri.netlify.app> dal 16 settembre 2026, sito `newfantasy-parrucchieri` sul team `nicola-la-rezza`, deploy dal CLI in cache (`~/.npm/_npx/da5c1b6ea715e8b4/node_modules/.bin/netlify`, `npx --no-install` non lo trova), repo `Nixo999/newfantasy-site` privata; tre sbarramenti verificati con `curl`. Prenotazioni e gestionale su `localStorage`: la demo vale su un dispositivo solo |
| [[sito-custombeautynails]] | Custom Beauty Nails, onicotecnica, Treviglio (BG) — Instagram `@custombeautynailstreviglio`, il DM non e' ancora partito | ✅ online su <https://custombeautynails.netlify.app> dal 16 settembre 2026, progetto `custombeautynails` sul team `travis`, deploy dal CLI; **repo solo locale, nessun remote git**. Tre sbarramenti verificati con `curl` sul sito vivo, piu' i file di lavoro sbarrati con `force = true`. ⬜ badge «Powered by Netlify» ancora acceso. ⚠️ **Non e' vero che si spegne solo dal pannello**: si spegne dal CLI, vedi la riga di Barbershop |
| [[sito-shaddai]] | Shaddai Extension Lash, lash artist a domicilio, Bergamo — Instagram `@shaddai_extensionlash`, il DM non e' ancora partito | ✅ **online su <https://shaddailash.netlify.app>** dal 17 settembre 2026, progetto `shaddailash` sul team `travis` (slug API **`patricksappa26`**: `--account-slug travis` risponde 404), deploy dal CLI `--prod --no-build`; **repo solo locale**, `gh repo create` bloccato dal classificatore dell'auto mode, lo lancia Nicola. Tre sbarramenti verificati con `curl` sul vivo, piu' `BRIEF.md`, `MONDO.md`, `PRODUCT.md`, `.impeccable/` e `.claude/` sbarrati con `force = true` — **al primo deploy erano serviti a 200** |
| [[sito-barbershop-snia]] | Barbershop di Andrea, barbiere, Cesano Maderno (MB) — Instagram `@barbershop_snia`, portato da Morgan come presidio volantini | ✅ **online su <https://barbershop-snia.netlify.app>** dal 17 settembre 2026, progetto `barbershop-snia` sul team **slug `patricksappa26`** (che si chiama «travis»: il nome non è lo slug, e `--account-slug travis` risponde 404), deploy dal CLI di Homebrew `/opt/homebrew/bin/netlify`, repo **`Nixo999/barbershop-snia-site` privata**. **Tre sbarramenti verificati con `curl` sul sito vivo** (`x-robots-tag`, `robots.txt` con `Disallow: /`, il `meta robots` in pagina), HTTP 200. ⬜ Badge «Powered by Netlify» **spento dall'API**, non dal pannello |
| [[sito-designcapelli]] | Design Capelli, parrucchiere di Daniela Cantello, Nichelino (TO) — Instagram `@designcapelli`, ha risposto «Buonasera qui grazie» e aspetta la bozza nel DM | ✅ **online su <https://designcapelli.netlify.app>** dal 21 settembre 2026, progetto `designcapelli` sul team `nicola-la-rezza`, deploy dal CLI `--prod --no-build`, repo `Nixo999/designcapelli-site` privata; **tre sbarramenti verificati con `curl` sul deploy pubblicato**, i quattro file di lavoro rispondono 404, badge «Powered by Netlify» spento dall'API |
| sito NG Barber | NG Barber Studio, Como + Erba + Mendrisio (CH) — riga 2 dell'[[2026-09-01-instagram-anello-1-b\|anello 1-b]] | ⬜ **pronto, non pubblicato**: `netlify.toml` scritto. il codice è su **`patricksappa26/ng-barber`** (pubblica, `main`, allineata). Resta indietro `Nixo999/ngbarber-site` (privata, primo tentativo). **Manca solo il login Netlify**, che è di Nicola — in alternativa, essendo la repo pubblica, **GitHub Pages** la pubblica senza altri accessi |

> [!note] Analisi di Claude — 2026-09-01
> **Il punto 3 qui sotto ha già una risposta tecnica, e va usata sempre.**
> Una bozza pubblica porta il marchio di un'azienda che non è nostra cliente:
> se Google la indicizza, il titolare si ritrova **un secondo sito col suo
> nome** nei risultati, e il danno lo facciamo noi prima ancora di vendergli
> qualcosa. Da NG Barber in poi ogni bozza esce con tre sbarramenti —
> `<meta name="robots" content="noindex, nofollow">`, `X-Robots-Tag` negli
> header del `netlify.toml`, `robots.txt` che vieta tutto — che **si tolgono
> il giorno in cui il sito diventa suo**. Non sostituisce la scadenza: un
> lead perso con la bozza ancora online resta materiale che gira.

## Quello che manca ancora scritto

`TODO` **Patrick o Nicola**, tre righe e questa nota è completa:

1. **Quale account** pubblica — GitHub `Nixo999`, o un account Netlify a sé?
   Le credenziali restano fuori dal vault ([[credenziali]]): qui serve solo
   sapere *chi* ce l'ha.
2. **Che indirizzo prende una bozza** — un `*.netlify.app` col nome del
   cliente, o un sottodominio di `denkicode.com`? Cambia come suona quando lo
   si manda: un sottodominio nostro dice «software house», un indirizzo
   generico dice «ho smanettato».
3. **Quanto resta online una bozza rifiutata.** Un lead perso con la bozza
   ancora pubblica è materiale di un altro che gira col nostro lavoro sotto.
   Serve una scadenza, anche solo «si toglie dopo 60 giorni».

## Collegamenti

[[strumenti]] · [[flusso-vendita]] · [[prodotti-e-listino]] ·
[[dm-instagram-vetrina]] · [[metodo-instagram]] · [[core-crescita-finanze]] ·
[[castiglione-furniture]] · [[credenziali]] · [[sito-denkicode]]

## Due cose che fanno perdere tempo ogni volta

**Lo slug del team non e' il suo nome.** Il team si chiama «travis» ma lo slug e
`patricksappa26`, e `netlify sites:create --account-slug travis` risponde
`404: Not Found` senza dire perche'. Lo slug vero:

```bash
netlify api listAccountsForUser --data '{}'
```

**Il badge «Powered by Netlify» si spegne dal CLI.** Sul piano gratuito compare
in basso a destra su ogni `*.netlify.app`, e su una bozza da mostrare a un
cliente non ci puo' stare. Non serve il pannello:

```bash
netlify api updateSite --data '{"site_id":"<id>","body":{"built_with_badge_enabled":false}}'
```

Ha effetto subito, senza ripubblicare. Verificato il 17/09/2026 su
[[sito-barbershop-snia]], dove dopo la chiamata `curl` non trova piu' la stringa.

**E se `curl` dice che il sito e' giu', probabilmente non lo e'.** Il risolutore
di questa sandbox non conosce i sottodomini `netlify.app` appena creati: `curl`
esce con codice 6 mentre `host` li risolve senza problemi. Gli sbarramenti si
verificano sul permalink del deploy pubblicato, che e' quello che la produzione
serve davvero:

```bash
netlify api getSite --data '{"site_id":"<id>"}'   # published_deploy.id
curl -sI https://<deploy-id>--<sito>.netlify.app/ | grep -i x-robots-tag
```

## ⚠️ 18/09/2026: Netlify blocca i deploy, il credito e' finito

```
JSONHTTPError: Forbidden
"error": "Account credit usage exceeded - new deploys are blocked until credits are added"
```

Il team **`patricksappa26`** (che si chiama «travis», piano Free) ha esaurito il
credito e **non accetta piu' pubblicazioni**. I siti gia' online restano online:
si blocca solo il deploy nuovo.

**Verificato il 18/09/2026 dal Mac di Nicola**: il CLI lì è loggato come Nicola
(team `nicola-la-rezza`, 25 siti, deploy accettati: `operotest` pubblicato il
18/09). `barbershop-snia` in quell'elenco **non c'è**: sta sul team di Patrick,
quindi `netlify link --name barbershop-snia` dall'account di Nicola non lo trova.
**Fatto il 18/09**: Nicola ha creato `barber-shop-snia` sul suo team, ed è quello il link buono.
O si pubblica dall'account di Patrick quando torna il credito, o si crea un sito
nuovo sul team di Nicola con un altro nome (e un altro link).

Cosa vuol dire in pratica: **una bozza corretta oggi resta in locale**, e quello
che il cliente vede e' il giro prima. Prima di dire a Patrick che una correzione
e' online, si controlla quale deploy sta servendo la produzione:

```bash
netlify api getSite --data '{"site_id":"<id>"}'   # published_deploy.id e published_at
```

Da decidere: aggiungere credito, oppure spostare le bozze su un altro hosting
(GitHub Pages regge, le repo dei siti sono su `Nixo999`).
