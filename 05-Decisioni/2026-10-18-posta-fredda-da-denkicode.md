---
riga: Nicola, 18/10 - la posta a freddo per i gestionali parte dalle tre caselle di denkicode.com per non pagare niente. Riapre il «mai da denkicode.com» del 2/09.
type: decisione
data: 2026-10-18
progetto: azienda
source: denkicode
stato: presa
updated: 2026-10-18
tags: [email, outreach, gestionali, deliverability]
---

# La posta a freddo per i gestionali parte dalle caselle di denkicode.com, per ora

## Il contesto

Il 18 ottobre Nicola ha chiesto un sistema che trovi aziende B2B fra 1 e 15
milioni di fatturato e le contatti via mail per i gestionali su misura, da
solo e ogni giorno, con più mail possibile.

La decisione del 2 settembre ([[2026-09-02-cold-email-gestionali]]) diceva di
non mandare mai la posta a freddo da `denkicode.com` e di usare domini
secondari con caselle a pagamento. Trevis ha presentato i costi: circa 4 € al
mese con un dominio secondario e tre caselle Zoho, circa 25 € con Google
Workspace.

## La decisione

Nicola: «voglio fare con le mail di denkicode intanto per non pagare niente».

1. **Si manda dalle tre caselle di `denkicode.com`.** La casella personale di
   Patrick resta fuori: se Google la chiude, Patrick perde la sua posta.
2. **Il rischio è accettato apposta.** Se le aziende segnano le mail come spam,
   Gmail e Outlook si fidano meno di `denkicode.com`, e nello spam finiscono
   anche le mail a Seba, i preventivi e le risposte ai lead.
3. **«Intanto»**: quando il canale porta il primo incasso, o al primo segnale
   di spam, si passa a un dominio secondario.

## Com'era il dominio il 18/10

Controllato da Trevis con `host` sul DNS pubblico:

| Cosa | Stato |
|---|---|
| Server di posta (MX) | `mail.register.it` |
| SPF | c'è: `v=spf1 include:spf.webapps.net ~all` |
| DMARC | c'è, `p=none`, ma i rapporti vanno a `dmarcreports@lovable.dev` e non a noi |
| Firma DKIM | non trovata sui nomi più comuni; si controlla nell'intestazione di una mail vera |

## Le contromisure, visto che il dominio è quello vero

- **Volume basso e in salita**: 10 mail al giorno per casella la prima
  settimana, 20 la seconda, 30 dalla terza. Il tetto è circa 90 al giorno.
- **Due mail per azienda al massimo**: la prima e un solo seguito.
- **Solo persone giuridiche con casella generica** (Srl, SpA, cooperative;
  `info@`, `commerciale@`), mai le PEC e mai le caselle con un nome di
  persona. È il perimetro difendibile della decisione del 2 settembre.
- **In ogni mail**: da dove viene l'indirizzo e come non riceverne più.
  Chi risponde di no entra nell'elenco dei disiscritti, e a quell'azienda non
  si scrive più.
- **Freno automatico**: se i rimbalzi di un giorno superano il 5%, o arriva un
  rifiuto per spam, l'invio si ferma da solo e lo segnala.

## Cosa si è scartato

- **Gmail gratuite**: Google può chiuderle, vanno aperte a mano con un
  telefono ciascuna, e una software house che scrive da `@gmail.com` non è
  credibile per un gestionale.
- **Smartlead o Instantly**: circa 90 € al mese per l'API, senza alzare il
  tetto, che dipende dal numero di caselle.

## Collegamenti

[[2026-09-02-cold-email-gestionali]] · [[generazione-lead]] ·
[[2026-09-17-brianza-gestionali-1m]] · [[core-commerciale]]
