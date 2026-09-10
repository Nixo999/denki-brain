---
type: risorsa
riga: Come si usa lo starter dei siti - cosa porta dentro (le trappole gia' pagate) e cosa non porta mai (il gusto).
updated: 2026-09-10
verificato: 2026-09-10
source: denkicode
tags: [siti, starter, strumenti]
---

# Starter sito — quello che è già stato pagato, e niente altro

```bash
python3 01-Coding/strumenti/nuovo-sito.py <nome-cliente>
```

Crea `~/lavoro/<nome-cliente>-site` con dentro questa cartella, il repo git
inizializzato e il primo commit. Poi si progetta.

## Cosa porta dentro

| File | Cosa risolve |
|---|---|
| `assets/base.css` | Il reset con dodici trappole già dentro: `img{height:auto}`, `[hidden]` con `!important`, `--vh` per le catture headless, `.cattura` che spegne tutto, le rivelazioni col fallback solo a scheda nascosta |
| `index.html` | I tre sbarramenti, il boot della motion, il `?cattura`, la firma DenkiCode nel footer |
| `netlify.toml` | `X-Robots-Tag`, e la cache che rivalida CSS e JS invece di tenerli una settimana sul telefono del cliente |
| `robots.txt` | Sbarramento 3 di 3 |
| `assets/logo-simbolo*.svg` | 4,5 KB. **Mai `logo-lockup.svg`**: 151 KB |

## Cosa NON porta dentro, di proposito

**Nessun colore, nessun font, nessuna spaziatura, nessuna sezione, nessun
componente.** Quelli nascono dall'essenza del cliente ogni volta, e sono il
motivo per cui il sito non sembra un template. Se ti viene voglia di mettere
qui una palette o una griglia «tanto serve sempre», stai costruendo la cosa
che ci farà uscire dodici siti uguali.

Il gusto sta in [[essenza-e-motion]] e in [[processo-siti]]. Qui c'è
l'idraulica.

## Le tre cose da fare subito dopo la copia

1. **Il titolo e la descrizione** — nome, città, cosa fa. Sono `TODO` apposta:
   restano visibili finché non li scrivi.
2. **`assets/stile.css`** — non esiste, lo crei tu. È dove vive il sito.
3. **Le foto in `assets/img/`** — gli URL Instagram scadono in giorni: si
   scaricano nella stessa sessione in cui si guarda il profilo.

## Quando il sito diventa suo

Si tolgono i tre sbarramenti insieme, mai uno solo: `meta robots` in
`index.html`, `X-Robots-Tag` in `netlify.toml`, `robots.txt`. La firma
DenkiCode invece resta.
