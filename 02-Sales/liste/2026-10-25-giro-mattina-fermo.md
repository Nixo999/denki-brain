---
riga: Giro del 25/10 - zero righe nuove: Instagram e Brave non leggibili senza una persona, motori in captcha; banco a 60 righe di ricerca
type: area
updated: 2026-10-25
source: claude
verificato: 2026-10-25
prodotto: [siti-vetrina]
canale: instagram
stato: bozza
---

# 25 ottobre: il giro automatico non ha trovato righe

Giro di [[giro-mattina]], ruolo `primo`, dal Mac di Nicola, partito alle 13:07.
Sul banco ci sono 60 righe mai mandate, tutte di ricerca. Il piano chiedeva
110 righe di siti in quattro celle: GE toelettature (29), BG sartorie (27),
VC pasticcerie (27) e VC fioristi (27). Non ne è entrata nessuna.

## Perché

- **Brave**: la prima apertura di `instagram.com/direct/inbox/` con Claude in
  Chrome ha chiesto un'approvazione. Nessuno l'ha data entro 5 minuti, quindi
  la posta non è stata letta e i profili non si potevano aprire da lì.
- **Il browser dell'app** non è collegato a Instagram: la ricerca risponde 404
  e `web_profile_info` risponde 401 con `require_login`.
- **I motori con curl**: DuckDuckGo html risponde con la pagina «anomaly»,
  Yahoo rimanda a un'altra pagina (307), Startpage non restituisce link.

Il complimento di ogni messaggio si scrive aprendo il profilo, quindi senza
lettura dei profili non si costruiscono righe.

## Cosa serve

Il giro si ripete con qualcuno davanti, che approvi Brave alla prima richiesta.
Le celle del piano restano le stesse e `rotazione.csv` non cambia.

[[metodo-liste]] · [[banco-dm]]
