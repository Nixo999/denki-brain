---
type: progetto
status: attivo
client: interno
stack: [vite, react, netlify, cloudflare]
started: TODO
deadline: TODO
updated: 2026-08-29
source: denkicode
valore: 0
incassato: 0
---

# denkicode.com — il nostro sito e la galleria

Sito di DenkiCode. **È qui che sta la galleria dei lavori**: il posto dove si
mostra a un cliente cosa abbiamo già fatto.

**Online**: `https://denkicode.com`
**Hosting**: Netlify, dietro Cloudflare
**Stack rilevato**: SPA React buildata con Vite
**Tagline**: *High-Voltage Sites, Low-Voltage Prices*
**Repo**: `github.com/Nixo999/pixel-perfect-rebuild`, ramo `main`
**Sul PC di Nicola**: `C:\Users\User\Desktop\denkicode-site` (clonato il 29
agosto 2026). ⚠️ In `Documents/GitHub/my-github-link-466158a8` c'è una **copia
vecchia dell'era WeBolt**, senza `.git` e due generazioni indietro: non è il
sito, e modificarla significa ripubblicare marzo.

## Perché è un progetto e non una risorsa

Non porta soldi da solo, ma è **lo strumento commerciale più usato che avete**:
è la risposta a *"voi cosa avete fatto finora"*, che è l'obiezione standard di
un'azienda che non vi conosce. [[sito-dropout]] e in parte [[cococat]] sono
stati fatti apposta per riempirlo.

## Com'è fatto oggi, dopo il 29 agosto 2026

Il sito è **diviso in due metà**, separate da una fascia (`SectionBand`) e
raggiungibili dai due bottoni dell'hero. La barra in alto ha quattro voci:
`CHI SIAMO · SITI WEB · GESTIONALI · CONTATTI`.

| Metà | Cosa contiene |
|---|---|
| **01 — Siti web** | Offerta (vetrina, e-commerce), i servizi, la galleria dei siti |
| **02 — Gestionali** | DenkiShift, i gestionali su misura, la galleria dei gestionali |

**Galleria dei siti**: Groavel, [[albybike]], Bellastoria, [[sito-dropout]].
**Galleria dei gestionali**: [[denkishift]] e [[opero]] — quest'ultimo
dichiarato come **collaborazione**, perché è il prodotto di
[[sebastian-torres]] e non nostro.

⚠️ Le due card dei gestionali **non hanno uno screenshot**: mostrano una
copertina tipografica col monogramma, perché mettere una foto di repertorio al
posto di un prodotto vero sarebbe una bugia. Servono due immagini reali.

## Cosa dice sui prezzi, e perché

Il listino a schermo non coincide più con [[prodotti-e-listino]], ed è voluto:

- **Sito vetrina**: da «600 sbarrato, 300, −50%» a **«circa 300»**. La cifra
  esatta esce dal preventivo, e sbandierarla toglie margine in trattativa.
- **Blog**: tolto. Non si vende più.
- **E-commerce**: invariato, 1000 sbarrato → 500, −50%.
- **Abbonamenti**: resta il prezzo del solo **Base, 15-40 €**. Silver e Gold
  vanno «su preventivo». La tariffa oraria di 20 €/h resta scritta.
- **DenkiShift**: nessuna cifra a schermo, ma **quota annuale calcolata sui
  dipendenti**. È la forma che regge il vincolo della ricevuta
  ([[vincoli-fiscali]]), e non promette una data che non abbiamo.
- **Gestionali su misura**: «una tantum oppure abbonamento annuale», costo
  definito sul lavoro. Nessun numero.

## Rilievi tecnici

> [!note] Analisi di Claude — 2026-08-29
> - ⚠️ **`index.css` ha un blocco `@media (max-width: 767px)` che disattiva
>   tutte le animazioni e azzera ogni `transform` inline**, commento `DEBUG:`
>   compreso. Il cassetto del menu su telefono sopravvive per via della
>   `visibility`, non perché la sua `translateX` funzioni. È un mucchio di
>   toppe in produzione, e va sciolto con calma su un telefono vero.
> - **Le icone social nella barra e nel cassetto puntano a `href="#"`**: tre
>   link morti, sei volte in pagina. O esistono i profili, o si tolgono.
> - **Il sito è una SPA React.** Per un sito che deve essere trovato su Google
>   statico sarebbe più veloce e più indicizzabile. Qui pesa meno, perché
>   nessuno vi cerca per parola chiave: il link lo manda Patrick.
> - **Manca ancora il pezzo che converte**: una riga di testimonianza da
>   [[albybike]] cambia il registro più di dieci progetti in più.

## Aperto

- [x] Trovare il repo del sito → `Nixo999/pixel-perfect-rebuild`
- [x] Togliere il commento `TODO` dal sorgente
- [x] Elencare qui cosa c'è in galleria
- [ ] Due screenshot veri per le card di DenkiShift e OperO
- [ ] Sciogliere il blocco `DEBUG:` di `index.css` su un telefono vero
- [ ] Decidere i tre link social, o toglierli
- [ ] Aggiungere `albybike.com` alla galleria, con una testimonianza
- [ ] Decidere chi aggiorna la galleria quando esce un lavoro nuovo

## Collegamenti

[[sito-dropout]] · [[cococat]] · [[sito-albybike]] · [[albybike]] ·
[[denkishift]] · [[opero]] · [[prodotti-e-listino]] ·
[[flusso-vendita]] · [[generazione-lead]] · [[stack]]
