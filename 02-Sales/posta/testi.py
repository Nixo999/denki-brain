"""I testi delle mail: lo scheletro fisso, i pezzi per settore, il seguito.

Chi li cambia cambia questo file, e solo questo. Claude scrive una riga sola
per azienda, quella personale (`riga`), presa dal sito dell'azienda: il resto
è fisso e l'ha riletto una persona.

Da dove vengono le scelte, dal core commerciale (02-Sales/processo/core-commerciale.md)
e dallo script di Patrick sui gestionali (02-Sales/script/script-gestionali-brianza.md):

- Gitomer, «fai i compiti a casa»: la riga personale dice una cosa vera del
  loro lavoro, letta sul loro sito. Il fatturato non si nomina mai.
- Challenger: il problema del settore detto come un fatto che succede a tutti,
  non come una domanda su di loro.
- SPIN, implicazione: la domanda che fa fare il conto a chi legge.
- Klaff, il premio sei tu: «se state già bene così, ve lo dico e vi saluto».
- Voss: la richiesta è formulata per un «no» («sarebbe un problema se...»), e
  il seguito lascia la via d'uscita («o vi lascio stare?»).
- Script di Patrick: Patrick è «del commerciale», l'obiettivo è mezz'ora, e a
  una casella generica si chiede solo il nome della persona giusta.

Registro: «voi» dall'inizio alla fine, perché scrive a info@, cioè all'azienda.
Lingua: le regole di 03-Storage/azienda/italiano-chiaro.md e la blacklist di
voce-denkicode. La riga in fondo (da dove viene l'indirizzo, come non ricevere
altro) non è una traccia del processo: la chiede la legge, decisione del 2/09.
"""

SETTORI = {
    'Officine e carpenterie': dict(
        oggetto='Una domanda sulle vostre commesse',
        problema=('Nelle officine che lavorano su commessa succede spesso una cosa. Un cliente chiama per '
                  'sapere a che punto è il suo ordine, e qualcuno deve andare in reparto a chiederlo.'),
        domanda=('Se quella risposta la vedeste dal telefono, già aggiornata, quanti giri in reparto vi '
                 'risparmiereste in una settimana?'),
        chi_segue='la programmazione della produzione',
        tema='sapere a che punto è una commessa senza andare in reparto',
    ),
    'Manifattura': dict(
        oggetto='Una domanda sui vostri ordini',
        problema=('Nelle aziende di produzione lo stesso ordine viene ricopiato a mano più volte, '
                  "dall'ufficio al reparto fino alla spedizione."),
        domanda=('Quando qualcuno sbaglia a ricopiarlo, ve ne accorgete prima che la merce parta o '
                 'quando chiama il cliente?'),
        chi_segue='gli ordini e la produzione',
        tema="non ricopiare più a mano gli ordini, dall'ufficio alla spedizione",
    ),
    'Impiantistica': dict(
        oggetto='Una domanda sui rapportini delle squadre',
        problema=('Nelle imprese di impianti i rapportini con ore e materiali arrivano spesso su carta, '
                  'la sera. Poi in ufficio qualcuno li deve ribattere.'),
        domanda=('A fine commessa, quando fate il conto delle ore, torna sempre o qualcosa si perde per '
                 'strada?'),
        chi_segue='i rapportini e le commesse',
        tema="ricevere i rapportini di ore e materiali dal telefono, senza ribatterli in ufficio",
    ),
    'Costruzioni': dict(
        oggetto='Una domanda sui vostri cantieri',
        problema=('Nelle imprese edili, per sapere quanto è fatto di un cantiere, spesso bisogna '
                  'chiamare il capocantiere.'),
        domanda=('Se lo stato di ogni cantiere fosse aggiornato ogni sera, quanto prima riuscireste a '
                 'preparare gli stati di avanzamento?'),
        chi_segue='la contabilità dei cantieri',
        tema='vedere lo stato di ogni cantiere aggiornato ogni sera, senza chiamare il capocantiere',
    ),
    'Ingrosso': dict(
        oggetto='Una domanda sul vostro magazzino',
        problema=('Nella distribuzione capita spesso che il gestionale dica che un articolo c\'è, e in '
                  'magazzino non ci sia.'),
        domanda=('Quando succede con un cliente al telefono, cosa fate: rimandate la spedizione o lo '
                 'richiamate dopo aver controllato?'),
        chi_segue='gli ordini e il magazzino',
        tema='avere una giacenza vera, la stessa a gestionale e sugli scaffali',
    ),
    'Trasporti': dict(
        oggetto='Una domanda sui giri degli autisti',
        problema=('Nelle aziende di trasporto i giri e i turni degli autisti si decidono spesso la sera '
                  'prima, al telefono e su un foglio in ufficio.'),
        domanda=('Quando un autista si ammala alle sei del mattino, quanto ci mettete a riorganizzare '
                 'i giri?'),
        chi_segue='i giri e i turni degli autisti',
        tema='assegnare giri e turni degli autisti dal telefono, senza il foglio in ufficio',
    ),
    'Magazzinaggio e logistica': dict(
        oggetto='Una domanda sulle vostre consegne',
        problema=('Nella logistica conto terzi i clienti chiamano spesso per sapere dov\'è il loro '
                  'carico. E qualcuno deve chiederlo al magazzino.'),
        domanda=('Se lo stato di ogni carico lo vedesse direttamente il cliente, quante di quelle '
                 'telefonate sparirebbero?'),
        chi_segue='le spedizioni e il magazzino',
        tema='far vedere ai clienti lo stato dei carichi, senza telefonate al magazzino',
    ),
    'Pulizie e servizi': dict(
        oggetto='Una domanda sulle vostre squadre',
        problema=('Nelle imprese di pulizie con molti cantieri, chi va dove domani si decide spesso su '
                  'fogli e messaggi.'),
        domanda=("Quando manca qualcuno all'ultimo momento, quanto tempo vi porta via trovare il "
                 'sostituto e avvisare il cliente?'),
        chi_segue='i turni e le squadre',
        tema='avere turni e ore delle squadre in un posto solo',
    ),
}

GENERICO = dict(
    oggetto='Una domanda sul vostro lavoro',
    problema=('In molte aziende della vostra dimensione le informazioni di tutti i giorni stanno su '
              'fogli Excel e nella testa di due o tre persone.'),
    domanda='Se una di quelle persone si assenta per una settimana, il lavoro va avanti uguale?',
    chi_segue="l'organizzazione del lavoro",
    tema='avere le informazioni di tutti i giorni in un programma solo',
)

PIEDE = ('Ho trovato questo indirizzo nella pagina contatti del vostro sito. Se non volete ricevere '
         'altre mail da noi, rispondete a questa e non vi scrivo più.')


def pezzi(settore):
    return SETTORI.get(settore or '', GENERICO)


def firma(telefono=''):
    righe = ['Patrick Sappa', 'DenkiCode, Seveso (MB)']
    if telefono:
        righe.append(telefono)
    return '\n'.join(righe)


def primo(settore, riga='', telefono=''):
    """Oggetto e corpo della prima mail. `riga` è la frase personale scritta da Claude."""
    p = pezzi(settore)
    blocchi = [
        'Buongiorno,',
        ('sono Patrick, del commerciale di DenkiCode. Siamo a Seveso e scriviamo gestionali costruiti '
         'sul modo in cui lavora ogni azienda, non programmi standard da adattare.'),
    ]
    if riga.strip():
        blocchi.append(riga.strip())
    blocchi += [
        p['problema'],
        p['domanda'],
        ("Sarebbe un problema se ci sentissimo mezz'ora, da voi o in videochiamata? Guardo come "
         "lavorate adesso e alla fine vi dico se c'è qualcosa da automatizzare oppure no. Se state già "
         'bene così, ve lo dico e vi saluto.'),
        f"Se non siete voi a seguire {p['chi_segue']}, mi basta il nome della persona giusta.",
        firma(telefono),
        PIEDE,
    ]
    return p['oggetto'], '\n\n'.join(blocchi)


def seguito(settore, oggetto_primo, telefono=''):
    """Il seguito: parte una volta sola, nello stesso filo, se al primo non ha risposto nessuno."""
    p = pezzi(settore)
    corpo = '\n\n'.join([
        'Buongiorno,',
        'riprendo la mail della settimana scorsa, nel caso sia finita sotto le altre.',
        f"Mi basta una riga: vi interessa {p['tema']}, oppure vi lascio stare?",
        firma(telefono),
        PIEDE,
    ])
    return 'Re: ' + oggetto_primo, corpo
