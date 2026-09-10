---
riga: Decisione. Nicola, 8 settembre 2026. Ogni cosa che esce da qui — siti vetrina, e-commerce, gestionali — porta nel piè di pagina la scritta P...
type: decisione
data: 2026-09-08
progetto: azienda
source: claude
---

# Ogni progetto porta la firma nel piè di pagina

**Decisione.** Nicola, 8 settembre 2026. Ogni cosa che esce da qui — siti
vetrina, e-commerce, gestionali — porta nel piè di pagina la scritta **Powered
by DenkiCode**, il **simbolo** e il **link a `denkicode.com`**. Vale sui
progetti già consegnati, non solo sui prossimi: quelli online si ripassano.

**Perché.** Il collo di bottiglia è la generazione lead, non il closing
(`CLAUDE.md`, regola 6). Un sito pubblicato è l'unico canale che lavora mentre
noi facciamo altro: sta davanti ai clienti *del cliente*, cioè esattamente le
PMI locali che chiamiamo a freddo, e costa zero ore al mese. In più ogni firma
è un link verso `denkicode.com`, che oggi è la [[sito-denkicode|galleria dei
lavori]] e vive di prova sociale. Nove siti pubblicati con la firma valgono più
di nove righe in una lista.

## Cosa si scrive, esattamente

```html
<a class="firma" href="https://denkicode.com" target="_blank" rel="noopener">
  <img src="/logo-denkicode.svg" alt="" width="18" height="18">
  <span>Powered by <strong>DenkiCode</strong></span>
</a>
```

- **La scritta è «Powered by DenkiCode»**, in inglese, con `DenkiCode` in
  CamelCase e in `<strong>`. Non «Realizzato da», non «Sito a cura di».
- **Il simbolo sta a sinistra del testo**, 18-24 px di lato, `alt=""` perché il
  nome è già nel testo accanto: ripeterlo fa dire due volte «DenkiCode» a chi
  usa uno screen reader.
- **Riga sua in fondo al footer**, sotto il copyright del cliente. Non è un
  elemento del suo brand e non si mescola ai suoi contatti.
- **Il link apre in scheda nuova** e ha `rel="noopener"`: da un sito di un
  cliente non si porta via il visitatore, gli si apre una finestra.
- **Discreta, non nascosta**: colore secondario del tema, mai `display:none`,
  mai un contrasto sotto 4.5:1. Una firma che non si legge non porta lead e ci
  fa sembrare furbi.

## Gli asset — due file nuovi, tagliati non ridisegnati

In `03-Storage/brand/logo/`:

| File | Per fondi | Peso |
|---|---|---|
| `logo-simbolo.svg` | chiari (bianco, grigio chiaro) | 4,5 KB |
| `logo-simbolo-scuro.svg` | scuri (nero, grigio medio) | 4,5 KB |

Sono **il solo simbolo** — l'anello con 気, `viewBox` quadrato 89×89 — senza
marchio testuale e senza payoff: la parola «DenkiCode» la dice già la scritta
accanto.

⚠️ **`logo-lockup.svg` nel footer non ci va.** Pesa **151 KB** e contiene 346
tracciati: sono le quattro versioni su quattro fondi, tutte dentro il file, e il
`viewBox` ristretto le **nasconde soltanto**. Servirle a ogni visita di ogni
pagina di ogni sito, per un segno da 20 px, è un errore che si paga su tutti i
progetti insieme. I due file nuovi sono ritagliati da quello — stessi tracciati,
nessun ridisegno, tre gruppi su quattro rimossi davvero.

**Verificato l'8 settembre** nel pannello browser: i due simboli caricano
(`naturalWidth` 150, quadrati), resi a 22 px e a 110 px su fondo bianco, nero e
grigio `#706F6F`, tutti e tre leggibili. **La sera stessa** sono dentro dieci
siti, misurati a 1440 e 375: contrasto fra 5,56 e 14,97, resi 18×18 ovunque.

## Dove va applicata — il ripasso

Fatto la sera stessa dal Mac di Nicola, dove i repo stanno in `~/lavoro`: sul
Desktop di Patrick c'è solo `smoothduty`. Il resoconto con le misure è nel
[[registro-interventi]].

- [x] [[sito-albybike]] — online su `albybike.com` (`334ea4f` su `vibrant-web-foundation`; ✅ online tre minuti dopo il push: Netlify pubblica da quel repo)
- [x] **Bellastoria** — `bellastoria_sito`, `bellastoria.netlify.app` (`4f5f1e8`, ✅ online)
- [ ] **Groavel** — `groavel.com` è **Squarespace**, niente repo: la firma si mette dal pannello Squarespace, da chi ha l'accesso (non io: [[credenziali]])
- [x] [[sito-denkicode]] — il nostro, firma compresa (`64397fc`, sera dell'8/9)
- [x] [[sito-fiftynine]] — in `bartabaccheria59` (`c5cae57`, **non ancora pushato**: il push scrive su tutti e due i remoti)
- [x] [[sito-atelier-selva]] · [[sito-dsi-advertising]] ·
      [[sito-salone-di-andrea]] · [[sito-nails-mania]] — bozze in trattativa
- [ ] [[sito-castiglione]] — ferma, repo sul PC di Nicola · [x] [[sito-ngbarber]] (`648187b`)
- [x] [[denkishift]] — nell'app, minima e solo da computer, come l'ha voluta Nicola (`c95a968`); ⬜ da guardare in produzione dopo il login
- [x] **V-BAG** — sito di Giulia, online su Netlify (`f1f8567`, due simboli in `<picture>`)
- [x] [[cococat]] (`a60c226`) · [[sito-dropout]] (`b20baf4`) — non erano in lista, ma sono siti nostri

Su una bozza la firma entra **subito**, non alla pubblicazione: è quello che il
lead vede quando gli mandiamo il link, ed è lì che spiega chi l'ha fatto.

## I due punti che la regola non chiude da sola

1. **Va detta nell'offerta, non scoperta dopo.** Un cliente che se la trova in
   pagina dopo aver pagato ha ragione a chiederne conto. Una riga nel preventivo
   («il sito porta in fondo la firma di chi l'ha realizzato») la trasforma da
   sorpresa in prassi, e chi vuole toglierla la paga. Va in
   [[proposta-commerciale]] e [[prodotti-e-listino]] — `TODO`.
2. **`TODO` — [[opero]] è un caso diverso, e non l'ho toccato.** Non è il
   gestionale di un cliente: è **il prodotto che [[sebastian-torres]] rivende
   alle aziende**. Una nostra firma dentro l'app la vedono i *suoi* clienti, e
   tocca il suo conto economico (`CLAUDE.md`, regola 9). È una decisione
   commerciale, non tecnica: la prende Nicola con Sebastian, non io in un
   footer.

## Collegamenti

[[identita-visiva]] · [[convenzioni]] · [[processo-siti]] · [[sito-denkicode]] ·
[[generazione-lead]] · [[prodotti-e-listino]] · [[registro-interventi]]
