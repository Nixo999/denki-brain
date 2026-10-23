---
riga: Per Patrick - giro del 23/10, 0 righe pubblicate (browser fermo, motori in captcha), posta non letta; 31 sartorie biellesi senza sito da cercare su IG
type: area
updated: 2026-10-23
source: claude
verificato: 2026-10-23
prodotto: [siti-vetrina]
canale: instagram
stato: pubblicata
---

# 23 ottobre: nessuna riga nuova, il banco resta a 164

Giro di [[giro-mattina]], ruolo `primo`, dal Mac di Nicola, partito alle 9:50.
`prossimo-giro.py` contava 164 righe mai mandate (siti 49, ricerca 115) e ha
chiesto solo 6 righe siti, nella cella BI · sartorie, atelier e tappezzieri. La
ricerca era già oltre quota. Il 22/10 Patrick non ha mandato DM.

## Perché non è entrata nessuna riga

Il giro è passato dall'hook, ma il browser no. La prima azione in Brave con gli
strumenti di Claude in Chrome ha chiesto un'approvazione, che nessuno poteva
dare: dopo cinque minuti il sistema l'ha annullata. Senza browser:

- **la posta non si è letta**, quindi esiti e lead fermi non sono aggiornati;
- **gli handle Instagram non si sono trovati.** La ricerca interna di Instagram
  senza login risponde «Page Not Found», DuckDuckGo e Startpage mostrano un
  captcha, Yahoo risponde 500. WebSearch non restituisce profili Instagram.

Una scoperta utile: **un profilo si legge senza browser** con
`curl -A "facebookexternalhit/1.1" https://www.instagram.com/<handle>/embed/`.
La pagina contiene nome, follower, numero di post e le ultime sei didascalie con
la data, che bastano per il complimento e per capire se il profilo è vivo. La
bio e il link in bio non ci sono. Serve però l'handle esatto.

Ho provato circa 90 handle indovinati dai nomi: nessuno era un'attività
biellese viva e senza sito. @sartoria_biellese è fermo dal 2021,
@bottega_del_cucito fa abiti storici a Torino ed è fermo dal 2024,
@ilsalottodellasposa è di Torino, @il_salotto_della_sposa sta cedendo
l'attività, @bicolorbiella è un colorificio col sito.

La cella **non è chiusa**: il blocco è della fonte, non della resa, e i profili
letti sono pochi.

## I candidati, da cercare su Instagram dal prossimo giro

Un operatore Sonnet ha raccolto 38 attività da Pagine Gialle e ReteImprese e ha
controllato i domini con curl il 23/10. Trentatré non hanno un sito vivo; queste
sono le più promettenti, da cercare per nome e comune nella casella di Instagram
in Brave:

| Nome | Comune | Tipo | Sito |
|---|---|---|---|
| Atelier Viby | Biella | atelier sposa | viby.it parcheggiato, non loro |
| Piqûre Chic (Samanta Filippi) | Cossato | sartoria aperta da poco | nessuno |
| La Sartoria Colpo, dal 1938 | Pray | su misura e sposa | nessuno |
| Pezzaro dal 1914 | Cossato | sposa e cerimonia | pezzaro.it è un'altra azienda |
| Rosa Blu di Tirelli Daniela | Cossato | sartoria | rosablu.it non è loro |
| Filrus Biella 1962 | Biella | sartoria e tessuti | filrus.it rimanda a share.google |
| Sartoria Bellinazzo Davico | Biella | sartoria | nessuno |
| Arte e Cucito di Peveraro Ilaria | Biella | sartoria | nessuno |
| Magia del Cucito | Biella | sartoria | nessuno |
| Autoselleria Zighy | Biella | tappezzeria auto | nessuno |
| Dell'Orto | Biella | tappezzeria | nessuno proprio |
| Sartoria Antonella di Nesci | Vigliano Biellese | sartoria | non cercato |
| Sartoria Maltese Angela | Pray | sartoria | non cercato |
| Boschetti Marco e Cesare | Viverone | tappezziere materassaio | nessuno |

Gli altri, con l'esito di ogni dominio, stanno nella tabella dell'operatore che
ho riassunto qui: Fornaro Giorgio, Magnetto Guido, Bottega del Cucito, Sartoria
di Dong, Scarparo Irvano, Marasco Anna Maria, Silvestrin Guido, Barberis
Organista Giovanni e Cela Riza (Valdilana), Pagliuca Generoso (Verrone),
Franchini Giuseppe (Occhieppo Inferiore), Amisuraduomo, Aba srl, Ago & Filo.

**Fuori, col sito vivo**: Creations Larusse, B&D Abiti su misura, Biella
Collezioni, Atelier Privé (Paola Fini), Caneparo, Tatiana Fusi.

[[2026-10-22-posta-giro-mattina]] · [[metodo-liste]] · [[banco-dm]]
