---
type: decisione
data: 2026-09-02
progetto: azienda
source: claude
tags: [email, outreach, denkishift, gdpr, deliverability]
---

# La cold email si automatizza tutta, ma in Italia la base giuridica non è il legittimo interesse

**Chiesto da Nicola**, 2 settembre 2026: si può automatizzare del tutto l'invio
di email alle aziende per [[denkishift]] e gli altri gestionali? Ricerca fatta
lo stesso giorno, subito dopo quella sui DM ([[2026-09-02-automazione-dm-instagram]]).

## La differenza con Instagram

Sui DM il blocco era la piattaforma: Meta non permette di scrivere per primi, e
i bot fanno perdere l'account. **Sulla posta quel blocco non esiste**: SMTP è un
protocollo aperto, nessuno vieta di mandare, e l'invio si automatizza al 100% —
sequenze, follow-up, risposte tracciate, tutto.

Il collo di bottiglia diventano altre due cose, e sono più serie.

## 1. La base giuridica — e qui le guide dei venditori mentono

Le guide dei fornitori di software dicono: «cold email B2B legale, base
giuridica il **legittimo interesse**, art. 6.1.f e considerando 47». Il Garante
italiano dice il contrario, e l'ha ridetto da poco.

⚠️ **Provvedimento del 17 aprile 2026 (doc. 10252188), caso Aesir s.r.l.**: email
commerciali a un avvocato, indirizzi presi da **LinkedIn Sales Navigator**. La
società si è difesa prima col legittimo interesse, poi sostenendo che i dati
fossero «già consentiti» dai termini di LinkedIn. Il Garante ha respinto tutto:

- per l'**art. 130** del Codice privacy serve il **consenso esplicito**, e il
  legittimo interesse **non lo sostituisce**;
- il consenso richiede una dichiarazione o un'azione positiva: presumerlo è
  incompatibile col GDPR;
- **un dato pubblico su un social non è un dato consentito**: contano le
  aspettative di chi l'ha pubblicato.

Sanzione mite — **1.000 €** — ma con **ammonimento e pubblicazione sul sito del
Garante**. Il modello sanzionato è esattamente quello che si vorrebbe usare.

**La riga che divide** non è B2B contro B2C, è **persona fisica contro persona
giuridica**:

| Destinatario | Cosa serve |
|---|---|
| `mario.rossi@azienda.it`, professionisti, ditte individuali, SNC | **Consenso.** Sono persone fisiche anche se hanno partita IVA |
| `info@`, `amministrazione@` di una **Srl o SpA** | Area difendibile: il GDPR non si applica ai dati delle persone giuridiche (considerando 14). Serve comunque **origine documentata** (visura, Registro imprese), **informativa raggiungibile** e **opt-out immediato** |

⚠️ Per [[denkishift]] questo morde: bar, ristoranti e negozi con dipendenti da
turnare sono spesso **ditte individuali o società di persone** — cioè persone
fisiche. Il pezzo di mercato aggredibile per posta è più stretto di quello che
sembra, ed è fatto di **Srl con casella generica**.

## 2. La consegna — dal novembre 2025 non conforme = respinta

Non è più «finisci in spam»: **la posta non conforme viene rifiutata**.

- **SPF + DKIM + DMARC allineati** (il dominio autenticato deve combaciare con
  quello del `From:`) — obbligo Google e Yahoo sopra i 5.000 al giorno, e
  Microsoft lo applica su Outlook/Hotmail/Live dal **5 maggio 2025**.
- **Disiscrizione con un click** nell'intestazione (RFC 8058), da evadere entro
  due giorni.
- **Segnalazioni di spam sotto lo 0,10%**, mai oltre lo 0,30%. È una soglia
  bassissima: tre persone su mille che premono «spam» e il dominio è bruciato.

⚠️ **Mai da `denkicode.com`.** Si usano domini secondari simili, 3-4 caselle per
dominio, **scaldati per 3-4 settimane** prima di partire, e si ruotano.

## 3. Il volume vero, che è il numero che smonta l'entusiasmo

**20-30 email al giorno per casella**, tetto pratico 50. Sopra le 100 il tasso
di spam cresce; oltre 150 è documentato un +43%.

Quindi tre caselle su un dominio secondario fanno **~90 email al giorno**, non
diecimila. L'automazione toglie il lavoro manuale, **non alza il tetto**: quello
lo decidono i filtri.

## Cosa ne segue

- L'invio si automatizza del tutto: qui un banco come quello dei DM non serve.
- Il lavoro si sposta **prima dell'invio**: costruire liste di **sole persone
  giuridiche con casella generica**, con l'origine del dato documentata — ed è
  la stessa lacuna dei DM, dove la raccolta è il pezzo non automatizzato.
- E si sposta **sull'infrastruttura**: domini separati, autenticazione, warm-up,
  disiscrizione funzionante. Senza quelli l'automazione manda posta che viene
  respinta.

**Non deciso**: se aprire il canale, con che dominio, e chi tiene la lista delle
disiscrizioni — che va tenuta, ed è un obbligo, non un'opzione.

## Collegamenti

[[2026-09-02-automazione-dm-instagram]] · [[denkishift]] · [[core-commerciale]] ·
[[vincoli-fiscali]] · [[metodo-instagram]]
