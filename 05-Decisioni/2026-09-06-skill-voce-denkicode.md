---
type: decisione
data: 2026-09-06
progetto: azienda
source: claude
---

# Nasce la skill voce-denkicode

**Il fatto.** Un lead, angolorelax_nembro, ha risposto a un DM Instagram
scritto da Claude per conto di Patrick dicendo, testuale: *"è un banale copy
poco professionale per chatGPT... leva le em dashes che ti fanno sgamare
all'istante"*. Screenshot mostrato da Nicola il 6 settembre 2026. Lead perso
sulla forma del messaggio, non sul prezzo o sull'offerta.

**La causa.** `stile-comunicazione.md` dice il tono ("diretto, giovane, no
fuffa") ma non elenca i pattern concreti che tradiscono un testo generato da
LLM: em dash, triadi retoriche, aperture a domanda, frasi-cuscinetto. Senza
una blacklist esplicita, ogni testo generato rischiava lo stesso tell.

**La decisione.** Creata `voce-denkicode` come skill a parte (non una
modifica a `stile-comunicazione.md`, che resta la fonte del tono):
`.claude/skills/voce-denkicode/SKILL.md` nel vault, copiata in
`~/.claude/skills/` su questo Mac perché sia caricabile. Si applica a:

- ogni messaggio diretto al cliente (WhatsApp, DM, email), insieme a
  [[proposta-commerciale]]
- il copy testuale dei siti vetrina, agganciata dentro `processo-siti` prima
  della finish review — vedi `~/.claude/skills/processo-siti/SKILL.md`, passo
  7bis

**Cosa resta aperto.** La skill non ha ancora un caso di verifica: la prossima
bozza di copy o il prossimo messaggio a un lead è il primo test reale. Se
sgama di nuovo, il problema non è la blacklist ma il fatto che nessuno la
rilegge prima di mandare — a quel punto serve un passaggio umano dichiarato,
non una skill più lunga.

## Addendum, stesso giorno — il testo che parte davvero era altrove

Un secondo giro ha bocciato la prima versione (solo em dash): la cadenza
sotto — elenchi di tre, connettivi da tema, ritmo troppo regolare — non è
catturata da una blacklist di parole singole. Aggiunta alla skill dopo una
ricerca su cosa distingue davvero un testo umano da uno AI, non da un solo
esempio (fonti in `voce-denkicode/SKILL.md`).

Il gancio più concreto: `02-Sales/strumenti/banco-dm.html`, il tool che
Patrick apre davvero per generare i DM, aveva lo **stesso testo prima della
correzione**, in un template JS separato dalla documentazione. Corretto
anche lì, e marcato nel file come sorgente canonica: chi lo cambia da qui in
avanti aggiorna anche `dm-instagram-vetrina.md` e `voce-denkicode`, i tre non
si sincronizzano da soli.

**Come arriva a Patrick.** Non serve installare niente: `banco-dm.html` è un
file del vault, gli arriva con `git pull` come tutto il resto. La skill
`voce-denkicode` invece serve solo se qualcuno chiede a Claude di scrivere un
testo a mano (un preventivo, una risposta fuori schema): si attiva da sola
quando la sessione lavora dentro il vault clonato, senza installazione
separata — a differenza delle skill di design di `processo-siti`, che vivono
fuori dal vault e vanno reinstallate macchina per macchina.

**Se Patrick vuole cambiare una frase.** Sul singolo lead: la textarea del
banco già salva la modifica nella colonna `Messaggio` del CSV, e resta lì
anche se il file si riesporta — non serve altro, esisteva già. Se vuole
cambiare il testo di default per tutti i lead futuri, la modifica va nel
`messaggio()` di `banco-dm.html` (quello che generano tutti quando la riga
non ha già un `Messaggio` scritto a mano): non è una cosa che si fa da sola
dal banco, va chiesta a chi tocca il codice.

## Collegamenti

[[stile-comunicazione]] · [[registro-trevis]] · [[proposta-commerciale]]
