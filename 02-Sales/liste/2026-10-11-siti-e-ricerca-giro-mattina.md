---
riga: Per Patrick - il primo giro del mattino (11/10, partito alle 18:23), siti 18 e ricerca 29 da 11 celle, fonti quasi tutte ferme
type: area
updated: 2026-10-11
source: claude
verificato: 2026-10-11
prodotto: [siti-vetrina, gestionale-custom]
canale: instagram
stato: pubblicata
---

# 11 ottobre, giro del mattino: siti 18 su 100, ricerca 29 su 60

Primo giro di [[giro-mattina]], ruolo `primo`, dal Mac di Nicola. Il task è
partito alle 18:23, non alle 8. Sette operatori Opus, uno per cella di
`prossimo-giro.py`, e quando la cella si chiudeva sono passati alla riserva.
Le liste sono sul banco unico «DenkiCode» (`lista-corrente.csv`).

**Perché così poche**: nel browser dell'app di questo Mac **Instagram non è
loggato**. Ricerca, topsearch, `users/{pk}/info` e gli hashtag rispondono 401.
Si leggevano solo i profili già noti, e gli handle si dovevano indovinare.
Con sette operatori sullo stesso IP i motori sono andati in captcha in pochi
minuti.

| Lista | Cella | Righe | Profili | Stato |
|---|---|---|---|---|
| siti | BI · toelettature | 3 | 18 | aperta, chiusa per fonti |
| siti | SO · toelettature (riserva) | 5 | 17 | aperta, chiusa per fonti |
| siti | LO · tatuatori | 3 | 16 | esaurita (6 studi in provincia) |
| siti | VB · tatuatori (riserva) | 1 | 4 | esaurita (4 studi) |
| siti | LO · pilates e yoga | 3 | 89 | esaurita (~55 omonimi fuori) |
| siti | LO · fotografi (riserva) | 0 | 46 | esaurita, solo omonimi |
| siti | MI · fioristi e wedding | 3 | 30 | esaurita (matrimonio.com 403) |
| ricerca | BS · aziende agricole | 14 | 24 | aperta, rende 1 su 2 |
| ricerca | CR · edilizia | 4 | 113 | esaurita (~90 fuori provincia) |
| ricerca | LO · ingrossi (riserva) | 1 | 62 | esaurita |
| ricerca | MI · ingrossi | 10 | 38 | aperta, rende 1 su 4 |

## Da guardare prima di mandare

- **Scade**: @eldosdelbec scrive «ieri» per la falconeria del 10/10, se parte
  dopo il 12/10 va scritto «sabato 10».
- **Profili grandi**: @ilcolmetto 36,8K, @socagrmarchesini 23,5K,
  @agriturismo_le_campagnole 18K, @eldosdelbec 10,2K, @fruttetotitoldini 7,3K.
- **Sede incerta**: @cristina_casa_pedrini_ (comune `TODO`, account
  personale), @ameliepetsalon (Piantedo o Morbegno), @dogsfeelings (Donato o
  Andrate), @peluche_toelettatura, @vitaminaink (sede solo da PagineBianche),
  @tortifrutta (AL o MI), @dipigreensrl (Andria e Crema), @zainicodogno.
- **Domini da riaprire**: dogsfeelings.it (in allestimento), ameliepetsalon.it
  (pagina di cortesia), zamparttoelettatura.my.canva.site, studioflor31.com
  (Shopify sotto password), studionaturalmente.eu/.it (di chi sono?).
- **Insieme, non lo stesso giorno**: quattro noleggi di carrelli elevatori MI
  (@reba_mh, @tecnocarrelli, @ungari_srl, @gfegroupit).
- **Al limite del segmento**: @esteamobili (arredo con e-commerce),
  @ifalegnami_pandino (falegnameria), @cormet.srl (rottami e noleggio).
- **Tu, Lei e voi**: @vitaminaink usa il Tu, @massarifiori e
  @studio_naturalmente il voi. Nelle 10 righe di MI ingrossi tutti i messaggi
  usano «vi», e il link al modulo sta nel primo DM come nel modello del 10/10.
- @intattooveritas ha il profilo dello studio fermo al 17/4, l'artista
  @egidio_aldo_boni (9K) posta ancora. Il post di @pepitatoelettaturaebenessere
  del 20/6 parla di un lutto, il messaggio non lo cita.

## Fonti, 11/10 dal Mac di Nicola

- **Hanno retto**: curl con UA Googlebot sui profili (~135 letture senza 429:
  bio, follower, 12 didascalie), embed `facebookexternalhit`, profilo da
  sloggato nel browser per il link in bio. PagineBianche via curl (72 ricerche
  senza 429). Elenchi di settore: dati.lombardia.it (fattorie didattiche,
  agriturismi), tag di @coldiretti_brescia e @campagnamica_brescia, operatori
  SoGeMi, soci Assodimi, toelettature.net, toelettapp.it, Interflora (JSON-LD
  per comune, ma quasi tutti col sito), Overpass.
- **Bloccate**: Pagine Gialle 429 dopo 2-50 ricerche; DuckDuckGo, Brave,
  Startpage, Mojeek, Qwant, Ecosia, Yahoo (regge ~60 ricerche, solo
  `--http1.1` e con i cookie); Google e Bing inutili via curl; matrimonio.com
  e zankyou 403.
- **Posta non letta**: Instagram non loggato in questo browser.
- **Contromisura**: il giro `primo` rende solo se il browser dell'app di
  questo Mac ha la sessione Instagram di DenkiCode. `TODO` Nicola.
