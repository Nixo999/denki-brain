---
type: progetto
riga: Bozza sito Emozioni di casa (Elisabetta Ramondini, fotografa di famiglia a Casale Monferrato): «Dalla porta di casa ai campi», Astro e GSAP, colline dai dati SRTM; giro 1 del 27/10/2026.
status: attivo
client: emozionidicasa
stack: [astro, gsap, netlify]
started: 2026-10-27
deadline: TODO
updated: 2026-10-28
source: claude
tags: [sito, fotografa, casale-monferrato, alessandria, astro, gsap]
---

# Sito Emozioni di casa — giro 1 «Dalla porta di casa ai campi»

Bozza di sito vetrina per [[emozionidicasa]], Elisabetta Ramondini, fotografa di gravidanza, neonati e famiglia a
Casale Monferrato e Alessandria. Nicola il 27/10/2026: «nuovo sito da fare per questo instagram, stesse istruzioni degli
ultimi, deve andare bene soprattutto per telefono ma anche da pc, studio dei competitor, animazioni fatte pulite, non
deve laggare, cerca le skill più adeguate al sito per farlo nello stile e personalità della cliente».

**Cartella**: `~/lavoro/emozionidicasa-site`, ramo `main`, nessun remoto per ora.
**Online**: sito Netlify `emozionidicasa` (id `22b8d6bc-16fb-4ee4-84d7-93506e78c0aa`, team denkicode, badge spento),
indirizzo <https://emozionidicasa.netlify.app>. Si ripubblica con `npm run build && npx netlify-cli deploy --prod --dir dist
--site 22b8d6bc-16fb-4ee4-84d7-93506e78c0aa` (sempre con `--site`: la cartella non è collegata).
**Memoria tecnica nel repo**: `PRODUCT.md` (verità di prodotto), `direzione/DIREZIONE.md` (il mondo),
`direzione/contratto.md` (il DOM fra gli operatori), `direzione/{skill-digest,colline,pagina,motion}.md` (i rapporti),
`raccolta/` (Instagram con 106 foto a 1080+, il sito Pixieset verbatim, Google, concorrenti del 27/10),
`riferimenti/foto.md` (catalogo di 95 foto vere e 33 grafiche con i provini a fianco), `riferimenti/foto-usate.md`.

## Il mondo

Betta non fotografa in un posto solo: le famiglie le aprono la porta di casa («le famiglie che mi hanno aperto la porta
di casa»), poi si esce nei campi del Monferrato, e dal 2026 c'è lo studio di Casale. **La pagina è una sua giornata di
lavoro**: la mattina a casa vostra (campo crema con la luce della finestra), il pomeriggio nei campi all'ora d'oro
(campo oro), la sera in studio con le luci del Natale 2026 (campo verde-notte con le luci). La spina è la sezione «La
giornata»: da computer una scena sticky con la foto che cambia in cross-fade e il campo che cambia a livelli di
opacità; sul telefono tre blocchi con uno schema di foto ciascuno, niente scrub.

- **Le colline del Monferrato** sono generate da uno script dai dati di quota SRTM (Open Topo Data, tre linee: Alessandria–
  Casale, Acqui–Alessandria, Vignale–Valenza): sono l'orizzonte dell'hero e la cucitura fra i campi di colore, con la
  riga che si disegna allo scroll. Nessun tratto a mano (regola di Nicola del 12/10, 20/10, 23/10).
- **Apertura «Le stampe sul tavolo»**: quattro sue foto cadono come stampe su un tavolo crema, il nome sale per righe,
  poi stampe e nome vanno al loro posto nell'hero con Flip; ≤ 1,7 s, un gesto solo.
- **Le sei schede** (gravidanza, neonati e famiglia a casa, famiglia all'aperto, Compleanno Raccontato, battesimi, nonni
  e nipoti) con le sue frasi verbatim; **Il vostro Natale 2026** con le tre proposte e i prezzi veri (79, 169, 239 €);
  «Come funziona» in quattro passi suoi; lo studio con l'indirizzo; «Ciao, sono Betta»; le quattro recensioni del suo
  sito; contatti su notte.
- **Palette**: crema `#F7F0E3`, lino, oro `#E9CE98`, notte `#17241D`, un accento solo: la terracotta delle sue grafiche
  `#B5563E`. **Font**: scelti su specimen fra Young Serif, Bricolage Grotesque e Gloock (display), Ephesis, Allison e
  Corinthia (script), Nunito Sans e Hanken Grotesk (corpo): la scelta sta in `direzione/pagina.md`.
- **Metodo**: Fable dirige e non costruisce. Cinque Sonnet in parallelo per la raccolta (Instagram dal browser dell'app,
  sito Pixieset e Google, concorrenti al volo, digest delle skill con `npx skills find`, scheletro Astro dal modello di
  Marta Cesena), poi un Sonnet per le colline dai dati, uno per Pixieset e Maps dal browser (Cloudflare blocca `curl`),
  uno per i provini e il catalogo; pagina e motion su due Opus con un contratto di DOM, le foto su un Sonnet.

## Stato

**Giro 1 online dalla notte del 27/10/2026** su <https://emozionidicasa.netlify.app> (deploy `6ae129c3`, commit `5e329e6`),
con i tre sbarramenti, i 404 sui file di lavoro, `og:image` e la firma verificati con `curl` sul permalink. Misurato:
`controlla-sito` 8/8, `controlla-slop` 0 blocchi (3 avvisi: «davvero» e «passione» stanno nelle sue frasi, i gruppi di tre
sono «gravidanza, neonati e famiglia» e gli indirizzi), `controlla-testo` 0/0; overflow 0 da 320 a 1440; nessun
`will-change` nel CSS; apertura 1,79 s e p95 18 ms allo scroll in Brave headless (operatore motion); i tre campi della
giornata messi in uno schermo sticky alto una finestra prima del deploy (la lezione del giro 2 di Marta Cesena);
la pila di stampe a 375 era sopra il titolo e ora sta sotto i bottoni (giro 1b, stesso deploy). Guardato dal direttore
nel pannello a 375 (hero, la mattina) e a 1440 (hero): tre catture in tutto. **Misura nel Brave vero di Nicola:
MISURA_VIVO.** iPhone e Safari veri mai.
**Deboli**: nessuna foto di lei (il ritratto dentro la grafica non regge: 470×627 col nastro adesivo); le quattro foto
Pixieset sono a 1000 px e stanno al massimo a 500 px CSS; quasi tutte le foto mostrano visi di bambini e le liberatorie
non sono note; il Flip dell'apertura verso la pila sotto il titolo (telefono) non è stato visto girare; il primo
tentativo di misura `--vivo` si è bloccato perché lo script ha lanciato il Brave appena aggiornato (156) mentre quello
aperto era il 155.
**Verdetto di Nicola sul giro 1: `TODO`.**

## Da chiedere a lei (via Patrick)

Elenco in `PRODUCT.md`: listino fuori dal Natale; durata, foto consegnate e tempi; orari dello studio; email; matrimoni;
logo vettoriale; foto originali e **liberatorie delle famiglie**; permesso per le quattro recensioni; dominio.

## Collegamenti

[[emozionidicasa]] · [[processo-siti]] · [[direttive-siti]] · [[sito-whitelilium]] · [[sito-martacesena]] · [[sito-groavel]]
