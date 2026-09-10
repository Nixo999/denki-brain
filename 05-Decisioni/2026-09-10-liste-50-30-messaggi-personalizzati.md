---
type: decisione
data: 2026-09-10
progetto: azienda
source: denkicode
tags: [dm-instagram, generazione-lead, liste, denkishift, siti-vetrina, script]
---

# Ogni lista DM è 50 siti più 30 DenkiShift, con un messaggio scritto per ognuno

**Detto da Patrick il 10 settembre 2026**, dopo la lista animali da 17 righe:

> «Abbiamo da migliorare tantissimo lo strumento perché ha potenziale ma non
> lo stiamo sfruttando al massimo, soprattutto tu non lo stai sfruttando al
> massimo. […] Non mi importa quanto ci metti, basta che il lavoro sia fatto
> bene.»

## Le quattro regole, da oggi

1. **Tutti i controlli, ogni volta.** Per ogni profilo si verifica se il sito
   c'è e, se c'è, com'è fatto. Si scrive solo a chi **non ce l'ha**, o ce l'ha
   **davvero vecchio o fatto male**, con un fatto verificabile in mano
   (`esamina-sito.py`: niente https, non si adatta al telefono, anno fermo in
   fondo, titolo di default, costruttore di un'altra era). Un sito vivo e
   decente è uno SCARTATO, anche se il profilo era perfetto.
2. **Un messaggio per ogni attività**, scritto su quel profilo e su quel
   motivo. Non un modello con un buco: quello che ho visto io nelle sue foto,
   il fatto preciso che manca, la cosa che gli propongo. Costruito sui
   framework di [[core-commerciale]] e [[core-crescita-finanze]], passato da
   `voce-denkicode`, e **più umano possibile**: frasi corte e irregolari,
   niente ritmo da macchina. Il banco usa la colonna `Messaggio` così com'è.
3. **Ogni richiesta di lista = due liste**: **50 contatti per i siti** e
   **30 per DenkiShift**, in due file separati e in due sezioni del banco.
   Chi ha già il sito non è perso: se ha una squadra a turni è un candidato
   DenkiShift, e la lista DenkiShift si costruisce anche con gli scartati
   della lista siti.
4. **Si sondano i settori.** Ogni lista dichiara perché ha scelto quei
   settori e riporta quanto hanno reso (quanti profili aperti, quanti col
   sito, quanti tenuti). Il settore che rende poco si abbandona, quello che
   rende si rifà sui comuni accanto.

## Cosa cambia nel vault

- [[metodo-instagram]]: i passi 2, 3 e 4 riscritti; il tetto giornaliero
  delle liste è 50+30.
- [[dm-instagram-vetrina]]: la **versione D**, scritta a mano per ogni
  riga, sostituisce la C. La promessa «la bozza è già pronta» finisce, come
  chiedeva [[2026-09-08-test-dm-chiuso]]: si promette una **prima schermata**
  con le sue foto, e la si fa dopo il sì.
- [[dm-instagram-denkishift]]: il DM per i turni, che prima non esisteva.
  Voss in apertura, una domanda SPIN sola, Challenger per dire cosa fa,
  Blount per chiedere dieci minuti. Nessuna data, prezzo come totale annuo.
- Strumenti: `esamina-sito.py` (nuovo), `verifica-sito.py` (DNS via
  Cloudflare, il locale non rispondeva), `banco-dm.html` (due sezioni per
  giorno), `controlla-lista.py` (le liste DenkiShift portano
  `[verifica-turni]`), `allinea-contattati.py` (le date degli invii tornano
  nel CSV).

## Il prezzo di questa decisione

Ottanta righe verificate una per una e scritte una per una sono **una
giornata intera di lavoro del modello per ogni lista**, e circa 150-200
profili aperti. Patrick lo sa e lo ha chiesto così. Il tetto d'invio del
banco resta 65 al giorno: due liste da 80 righe coprono un giorno e mezzo di
invii.

## Collegamenti

[[metodo-instagram]] · [[dm-instagram-vetrina]] · [[dm-instagram-denkishift]] ·
[[core-commerciale]] · [[core-crescita-finanze]] · [[2026-09-08-test-dm-chiuso]] ·
[[2026-09-10-animali-va-co-lc-bg-ti]] · [[generazione-lead]]
