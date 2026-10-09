---
riga: Bozza sito ICAARUS ASD, centro cinofilo a Brembate-Grignano (BG). Giro 1 «Il percorso» del 09/10, direzione Trevis, costruzione Opus.
type: progetto
status: attivo
client: TODO
stack: [html, css, gsap, netlify]
started: 2026-10-09
deadline: TODO
updated: 2026-10-09
source: claude
valore: 0
incassato: 0
---

# Sito ICAARUS — centro cinofilo ASD, Brembate (BG)

Lead dal banco del 6/10 (`02-Sales/liste/2026-10-05-instagram-siti-bg-toelettature.csv`), primo DM di Patrick il 7/10.
Il 9/10 ha risposto su Instagram «Buongiorno, chiamami pure»: la bozza serve per la telefonata e la vedranno dal telefono.

**Repo**: `~/lavoro/icaarus-site`, **solo locale**.
**Online**: <https://icaarus.netlify.app> dal 9/10 (Nicola: «mettilo su netlify vai»), sbarramenti verificati. Riga in [[netlify]].
**Memoria tecnica**: `DIREZIONE.md`, `raccolta/RACCOLTA.md`, `raccolta/CONCORRENTI.md`, `prove/` nel repo.

## Il metodo (09/10)
Raccolta Instagram/Facebook/Maps e concorrenti su **Sonnet in parallelo** (4 e 3 minuti, entrambi salvati su disco
subito) → `DIREZIONE.md` scritto dal direttore senza agente → **una testa sola su Opus** costruisce, con lista di
lettura in tre file (DIREZIONE, craft-floor, scrittura-sito) e scaletta a orario.

## Il mondo: «Il percorso»
Il loro sport è il Rally-O (percorso a cartelli numerati), la loro parola «Relazione», la loro formula «DOG in …».
La pagina è il percorso che fai con loro: consulenza → educazione → riabilitazione se serve → Rally-O e ricerca → insieme.
Grafica solo geometrica e tipografica: cartelli Rally-O, planimetria del campo con tratteggio allo scroll, l'acronimo
che si apre, anelli olfattivi sul bottone finale. Palette dalla locandina di settembre (blu #0b47a8, arancio #ff7a1a).

## Cosa sappiamo e cosa manca
- Via S. Fermo, 24041 Brembate, frazione Grignano; campo recintato. WhatsApp 328 633 7427, icaarusasd@gmail.com.
- Google Maps 4,9 su 13 recensioni; Renza citata per nome. Orari Maps lun-ven 18-20, sab-dom 8-20 (da confermare).
- Foto: il feed è locandine e Reel a 360 px. Due foto vere da Maps (spaniel sul campo, maltese). Il sito non dipende
  dalle foto: **le foto buone si chiedono**.
- ICAARUS = «Interventi Cinofili Assistiti Ausilio Ricerca Utilità Soccorso» (Facebook, «In breve»): da confermare.
- Non ci sono: prezzi, cognomi, titoli FISC delle istruttrici, anno di nascita, civico, tessera e assicurazione.
- Il post Facebook su Rumba è un lutto: fuori dal sito.

## Giro 1 (09/10)
Commit `84d9c68` (8 commit). Design rivisto da **Fable** su richiesta di Nicola («usa fable però per la direttiva del
design»): via l'acronimo dal sito, campo a griglia hairline con tracciato continuo (il tratteggio era la pista di
Claudia), nastro arancio che taglia il sipario + «START →», «4,9» piccolo. Terna **Big Shoulders Display + Hanken Grotesk
+ Bungee** (prova in `prove/font-375.png`). 1-bis dopo la cattura a 375: ICAARUS a 89% della larghezza con griglia e
tracciato che finisce sul bottone «Prenota la consulenza»; «DOG in» a parole che riempiono la riga, 45svh; la riga sotto
ogni parola si accende con la parola. Misurato: controlla-sito 8/8, slop 0 (3 avvisi), testo 0/0, overflow 0 a 375 e
1440, console vuota, pagina completa senza JS. Tempi: raccolta 4 min, concorrenti 3, Fable 3, costruzione 17 + 1-bis 5:
**circa 35 minuti**. Deboli: sipario blu vuoto ~300 ms finché GSAP arriva dalla CDN; font da Google; animazione del
tracciato in hero non campionata; firma DenkiCode poco leggibile sul blu notte; recensioni con nome (Marinella,
Vincenzo) senza consenso; «GIOCO» e «GARA» come «DOG in» sono nostri, loro usano RELAZIONE, RICERCA, NATURA.
Non visto: iPhone e Safari veri. Verdetto di Nicola: TODO.

## Da chiedere (via Patrick, in telefonata)
Foto vere del campo e dei cani al lavoro; chi sono (nomi, titoli); conferma dell'acronimo; orari; prezzi o «da»;
ok a citare le recensioni Google; logo in alta risoluzione.
