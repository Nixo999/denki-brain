---
type: progetto
riga: Bozza sito Minerva Esposito, MUA ad Alessandria. Online il giro 2 (bocciato); giro 3 «Il velo» pronto in locale, deploy da lanciare.
status: attivo
client: minniminerva
stack: html-css-js
started: 2026-10-04
deadline:
updated: 2026-10-05
source: claude
verificato: 2026-10-05
tags: [sito, bozza, make-up, sposa, alessandria, instagram]
---

# Sito Minerva Esposito — bozza, Alessandria

Cartella `~/lavoro/minniminerva-site`, dallo starter. **Repo solo locale**, 24
commit, nessun remote. Netlify: <https://minervaesposito.netlify.app> (progetto
`minervaesposito`, id `b65feb44-f910-459f-a359-89fec5fcd600`, team
`denkicode`). **Online c'è il giro 2, quello bocciato**; il giro 3 (`38dadd6`)
è in locale. Il deploy lo lancia Nicola: a Trevis lo blocca il classificatore
dell'auto mode. La cliente sta in [[minniminerva]].

Metodo: raccolta del direttore (Fable), concorrenti su Sonnet
(`COMPETITOR.md`), direzione e costruzione su operatori Opus.

## I giri

- **Giro 1-2, «Due occhi»** (04/10): due tondi con macro di occhi, grigio
  `#EEF0EF`, Jost. **Bocciato da Nicola il 05/10**: «questo sito fa cagare, non
  è per niente nello stile della sposa della cliente. dagli più personalità, e
  cambia completamente l'animazione all'avvio». Idea concettuale e fredda.
- **La falla era nella raccolta**: le otto copertine delle sue storie in
  evidenza sono tutte bianco su bianco (seta, rose, petali in rilievo,
  brillantini, calligrafia) e nessuno le aveva guardate. Ora stanno in
  `RACCOLTA.md` e in `sorgenti/_copertine-evidenza.jpg`. Regola in
  [[direttive-siti]]: il mondo nasce dallo stile della cliente.
- **Giro 3, «Il velo»** (05/10, `MONDO.md`): seta e tulle. Apertura in 2,95 s:
  seta a tutto schermo (shader su una foto vera, Susan Wilkinson su Unsplash),
  il velo si solleva dal basso, la sposa di `p11-4` passa dallo sfocato al
  nitido, il nome si scrive in Parisienne, le perline scintillano. Innesti:
  recensioni come bigliettini col nome a mano, richiesta come partecipazione
  con gli spazi, la sua frase «Ognuno merita di brillare» grande sulla seta, un
  solo capitolo nero «Al lavoro». Nome a 158 px da computer, 68 sul telefono.

## Cosa fa di utile, cioè cosa Instagram non fa

- **La richiesta che compone il messaggio** (servizio, data, ora, luogo,
  persone, prova, stile, note): «Copia e apri Instagram» lo copia e apre la
  chat. WhatsApp è cablato e nascosto: il numero va nella costante `WHATSAPP`
  in testa a `assets/sito.js`.
- Sei percorsi, sette domande con risposta, il triangolo Torino–Milano–Genova.
- `<title>` e JSON-LD per «truccatrice sposa Alessandria», dove su Google non
  c'è il sito di nessuna truccatrice. Anteprima del link (`og.jpg`) rifatta.

## Verificato il 05/10 (giro 3, in locale)

- `controlla-sito.py` 8/8, `controlla-slop.py` 0 blocca e 3 avvisi,
  `controlla-testo.py` 0/0, rilanciati dal direttore su `38dadd6`.
- Apertura guardata dal direttore battuta per battuta a 375 e a 1440
  (`catture/g5/apertura-*.jpg`), fette a 375 e 1440, testa ritoccata in `g6`.
- **Non verificato**: telefono vero e Safari; copia negli appunti e apertura di
  Instagram su un telefono; niente del giro 3 è online.

## Tela di design (05/10)

`/design` di Nicola: pagina intera a telefono e computer più l'apertura in
quattro battute, su <https://claude.ai/artifact/5ymszHnC9vsu58Ya7sFDCW>
(privata). Scritta da un agente Opus, **mai guardata a schermo**. Lì il nome è
in maiuscolo sottile (Jost) e il corsivo sta solo nelle firme: nel codice il
nome è in corsivo. Sono due letture dello stesso mondo.

## Come si pubblica

Solo i file pubblici: `catture/` pesa centinaia di MB e il CLI caricherebbe tutto.

```bash
cd ~/lavoro/minniminerva-site && rm -rf /tmp/pubblica-minerva && mkdir /tmp/pubblica-minerva && rsync -a --exclude '*.json' index.html robots.txt netlify.toml assets /tmp/pubblica-minerva/ && cd /tmp/pubblica-minerva && netlify deploy --prod --no-build --dir . --site b65feb44-f910-459f-a359-89fec5fcd600
```

Dopo ogni deploy: tre sbarramenti con `curl`. Prima del DM: link da un iPhone.

## Da chiederle

Elenco intero in `MONDO.md`. I primi: file del logo, numero WhatsApp, un prezzo
di partenza, quando si fa la prova, se lavora a domicilio (oggi è in pagina),
consenso su recensioni e foto delle clienti.
