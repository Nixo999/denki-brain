"""La base dati della posta a freddo: una sola, locale, sul Mac che manda.

Sta in `02-Sales/posta/dati/posta.db`, fuori da git: cambia a ogni invio e un
binario nel vault gonfierebbe la storia. Quello che deve restare nel vault lo
scrive `registro.py` in CSV leggibili (inviate, risposte, disiscritti).

Il ciclo di vita di un'azienda, colonna `fase`:

    nuova        trovata su companyreports, scheda letta, dentro i filtri
    senza_sito   cercato il sito e non trovato (la prova sta in `sito_prova`)
    senza_mail   sito trovato, nessuna casella generica sul sito
    pronta       sito e casella generica trovati: si può scrivere
    scritta      Claude ha scritto la prima mail (tabella `messaggi`)
    inviata      la prima mail è partita
    seguita      è partito anche il seguito: non si scrive più
    risposta     ha risposto: la conversazione passa a Patrick
    rimbalzata   l'indirizzo non esiste
    disiscritta  ha chiesto di non ricevere altro
    scartata     fuori perimetro (motivo in `note`)
"""
import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime

QUI = os.path.dirname(os.path.abspath(__file__))
DB = os.environ.get('POSTA_DB', os.path.join(QUI, 'dati', 'posta.db'))
DATI = os.path.dirname(DB)        # log, freno e file di lavoro stanno accanto alla base dati

SCHEMA = """
CREATE TABLE IF NOT EXISTS aziende (
    piva         TEXT PRIMARY KEY,
    nome         TEXT NOT NULL,
    slug         TEXT,              -- scheda companyreports.it/<slug>
    fatturato    INTEGER,
    anno         INTEGER,           -- anno del bilancio del fatturato
    ateco        TEXT,
    attivita     TEXT,
    forma        TEXT,              -- forma giuridica dalla scheda
    stato        TEXT,              -- «Attiva» o altro, dalla scheda
    dipendenti   TEXT,              -- banda dichiarata, es. «da 20 a 49»
    indirizzo    TEXT,
    comune       TEXT,
    prov         TEXT,
    settore      TEXT,              -- la nostra etichetta, decide il gancio
    sito         TEXT,
    sito_prova   TEXT,              -- come è stato trovato o perché no
    email        TEXT,
    email_prova  TEXT,              -- pagina esatta dove sta l'indirizzo
    estratto     TEXT,              -- testo del sito (max ~1500 caratteri) per la riga personale
    fase         TEXT NOT NULL DEFAULT 'nuova',
    note         TEXT,
    creata       TEXT NOT NULL,
    aggiornata   TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS aziende_fase ON aziende(fase);
CREATE UNIQUE INDEX IF NOT EXISTS aziende_email ON aziende(email) WHERE email IS NOT NULL;

CREATE TABLE IF NOT EXISTS messaggi (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    piva         TEXT NOT NULL REFERENCES aziende(piva),
    tipo         TEXT NOT NULL,     -- primo | seguito
    casella      TEXT,              -- da quale casella parte (deciso all'invio)
    a            TEXT NOT NULL,     -- destinatario
    oggetto      TEXT NOT NULL,
    corpo        TEXT NOT NULL,
    message_id   TEXT,              -- Message-ID, per riconoscere le risposte
    in_risposta  TEXT,              -- Message-ID del primo, per il seguito
    scritto      TEXT NOT NULL,
    da_mandare   TEXT,              -- il seguito non parte prima di questa data
    inviato      TEXT,
    esito        TEXT               -- ok | errore: ...
);
CREATE INDEX IF NOT EXISTS messaggi_coda ON messaggi(inviato, da_mandare);

CREATE TABLE IF NOT EXISTS eventi (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    quando       TEXT NOT NULL,
    piva         TEXT,
    casella      TEXT,
    tipo         TEXT NOT NULL,     -- risposta | rimbalzo | disiscrizione | freno | errore
    da           TEXT,
    oggetto      TEXT,
    testo        TEXT,
    uid          TEXT UNIQUE        -- casella + UID IMAP, per non leggere due volte
);

-- Chi ha detto no. Per dominio, non per indirizzo: se info@ dice no,
-- commerciale@ della stessa azienda non si scrive.
CREATE TABLE IF NOT EXISTS disiscritti (
    dominio      TEXT PRIMARY KEY,
    quando       TEXT NOT NULL,
    motivo       TEXT
);
"""


def adesso():
    return datetime.now().isoformat(timespec='seconds')


def apri():
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    c = sqlite3.connect(DB, timeout=30)
    c.row_factory = sqlite3.Row
    c.execute('PRAGMA journal_mode=WAL')
    c.execute('PRAGMA foreign_keys=ON')
    c.executescript(SCHEMA)
    # 19/10: la frase personale e il nome breve si tengono, così le mail ancora in coda
    # si ricompongono quando cambiano i testi fissi (`scrivi.py ricomponi`)
    colonne = {r[1] for r in c.execute('PRAGMA table_info(messaggi)')}
    for col in ('riga', 'nome'):
        if col not in colonne:
            c.execute(f'ALTER TABLE messaggi ADD COLUMN {col} TEXT')
    return c


@contextmanager
def connessione():
    c = apri()
    try:
        yield c
        c.commit()
    finally:
        c.close()


def dominio(email):
    return (email or '').rsplit('@', 1)[-1].lower().strip()


def disiscritto(c, email):
    return c.execute('SELECT 1 FROM disiscritti WHERE dominio=?', (dominio(email),)).fetchone() is not None


def metti_fase(c, piva, fase, note=None):
    if note is None:
        c.execute('UPDATE aziende SET fase=?, aggiornata=? WHERE piva=?', (fase, adesso(), piva))
    else:
        c.execute('UPDATE aziende SET fase=?, note=?, aggiornata=? WHERE piva=?', (fase, note, adesso(), piva))
