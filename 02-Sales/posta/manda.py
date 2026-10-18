#!/usr/bin/env python3
"""Manda le mail già scritte, una alla volta, dalle caselle di denkicode.com.

    python3 02-Sales/posta/manda.py              un giro: al massimo una mail per casella
    python3 02-Sales/posta/manda.py --prova ID   manda il messaggio ID a PROVA_A, senza toccare lo stato
    python3 02-Sales/posta/manda.py --togli-freno

Lo lancia launchd ogni cinque minuti (`giro.py`). A ogni giro ogni casella
manda al massimo una mail, e solo se:
- è un giorno lavorativo fra le 9 e le 17:30;
- la casella non ha finito la quota del giorno (la rampa sta in config.py);
- è passato abbastanza tempo dall'ultima mail di quella casella: la quota si
  spalma sulla giornata, con un intervallo che varia del 40% in più o in meno;
- non c'è il freno (`dati/FRENO`), che mette leggi-risposte.py quando i
  rimbalzi superano il 5% o arriva un rifiuto per spam.

Prima i seguiti scaduti, poi le prime mail. Il seguito parte dalla stessa
casella della prima mail, nello stesso filo. Con ATTIVO=0 nel file delle
caselle non parte niente: il giro scrive solo cosa avrebbe mandato.
"""
import imaplib
import json
import os
import random
import smtplib
import ssl
import sys
import time as _time
from datetime import date, datetime, timedelta
from email.message import EmailMessage
from email.utils import formataddr, formatdate, make_msgid
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config  # noqa: E402
import db      # noqa: E402
import testi   # noqa: E402

FRENO = os.path.join(db.DATI, 'FRENO')
PROSSIMO = os.path.join(db.DATI, 'prossimo-invio.json')
LOG = os.path.join(db.DATI, 'manda.log')


def log(*a):
    riga = datetime.now().strftime('%Y-%m-%d %H:%M:%S ') + ' '.join(str(x) for x in a)
    print(riga)
    os.makedirs(db.DATI, exist_ok=True)
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(riga + '\n')


def metti_freno(motivo):
    os.makedirs(db.DATI, exist_ok=True)
    with open(FRENO, 'w', encoding='utf-8') as f:
        f.write(f'{db.adesso()} {motivo}\n')
    with db.connessione() as c:
        c.execute('INSERT INTO eventi(quando, tipo, testo) VALUES (?,?,?)', (db.adesso(), 'freno', motivo))
    log('FRENO:', motivo)


# --- composizione ----------------------------------------------------------

def componi(m, casella, a=None):
    msg = EmailMessage()
    msg['From'] = formataddr(('Patrick Sappa', casella))
    msg['To'] = a or m['a']
    msg['Subject'] = m['oggetto']
    msg['Date'] = formatdate(localtime=True)
    msg['Message-ID'] = m['message_id'] or make_msgid(domain=db.dominio(casella))
    if m['in_risposta']:
        msg['In-Reply-To'] = m['in_risposta']
        msg['References'] = m['in_risposta']
    msg['List-Unsubscribe'] = '<mailto:%s?subject=%s>' % (casella, quote('Non scriveteci più'))
    msg.set_content(m['corpo'], charset='utf-8')
    return msg


def smtp(cfg, casella, password):
    host, porta = cfg.get('SMTP_HOST', ''), int(cfg.get('SMTP_PORT', '465'))
    # SMTP_SICUREZZA=nessuna serve solo alle prove con un server finto su localhost
    sicurezza = cfg.get('SMTP_SICUREZZA') or ('ssl' if porta == 465 else 'starttls')
    ctx = ssl.create_default_context()
    if sicurezza == 'ssl':
        s = smtplib.SMTP_SSL(host, porta, context=ctx, timeout=60)
    else:
        s = smtplib.SMTP(host, porta, timeout=60)
        if sicurezza == 'starttls':
            s.starttls(context=ctx)
    if sicurezza != 'nessuna':
        s.login(casella, password)
    return s


def copia_in_inviata(cfg, casella, password, msg):
    """Mette la mail nella cartella della posta inviata, così Patrick la vede nella casella.
    Se non ci riesce lo scrive nel log e va avanti: la mail è già partita."""
    try:
        im = imaplib.IMAP4_SSL(cfg.get('IMAP_HOST', ''), int(cfg.get('IMAP_PORT', '993')), timeout=60)
        im.login(casella, password)
        _, cartelle = im.list()
        nome = None
        for r in cartelle or []:
            riga = r.decode(errors='ignore')
            if '\\Sent' in riga or any(x in riga.lower() for x in ('"sent"', 'inviat', 'sent items', '.sent"')):
                nome = riga.rsplit(' ', 1)[-1].strip()
                break
        im.append(nome or 'Sent', '\\Seen', imaplib.Time2Internaldate(_time.time()), msg.as_bytes())
        im.logout()
    except Exception as e:
        log('copia in inviata non riuscita', casella, e)


# --- scelta di cosa mandare -------------------------------------------------

def prossimo_per(c, casella):
    """Il seguito scaduto di questa casella, se c'è; altrimenti la prima mail più vecchia ancora libera."""
    m = c.execute(
        "SELECT m.* FROM messaggi m JOIN aziende a ON a.piva=m.piva "
        "WHERE m.tipo='seguito' AND m.inviato IS NULL AND m.casella=? AND m.da_mandare<=? "
        "AND a.fase='inviata' ORDER BY m.da_mandare LIMIT 1", (casella, db.adesso())).fetchone()
    if m:
        return m
    for m in c.execute(
            "SELECT m.* FROM messaggi m JOIN aziende a ON a.piva=m.piva "
            "WHERE m.tipo='primo' AND m.inviato IS NULL AND m.esito IS NULL AND a.fase='scritta' "
            "ORDER BY m.scritto, m.id LIMIT 50"):
        if db.disiscritto(c, m['a']):
            db.metti_fase(c, m['piva'], 'disiscritta', 'dominio nei disiscritti prima del primo invio')
            c.execute("UPDATE messaggi SET esito='saltato: disiscritto' WHERE id=?", (m['id'],))
            continue
        gia = c.execute("SELECT 1 FROM messaggi WHERE inviato IS NOT NULL AND a LIKE ? LIMIT 1",
                        ('%@' + db.dominio(m['a']),)).fetchone()
        if gia:
            db.metti_fase(c, m['piva'], 'scartata', 'a questo dominio abbiamo già scritto')
            c.execute("UPDATE messaggi SET esito='saltato: dominio già scritto' WHERE id=?", (m['id'],))
            continue
        return m
    return None


def stato_caselle(c, caselle):
    oggi = date.today().isoformat()
    out = {}
    for a, _ in caselle:
        primo = c.execute('SELECT MIN(inviato) FROM messaggi WHERE casella=? AND inviato IS NOT NULL', (a,)).fetchone()[0]
        oggi_n = c.execute("SELECT COUNT(*) FROM messaggi WHERE casella=? AND substr(inviato,1,10)=?", (a, oggi)).fetchone()[0]
        q = config.quota(date.fromisoformat(primo[:10]) if primo else None)
        out[a] = dict(oggi=oggi_n, quota=q)
    return out


def intervallo(quota):
    """Minuti fra due mail della stessa casella: la finestra divisa per la quota, più o meno 40%."""
    inizio, fine = config.FINESTRA
    minuti = (fine.hour * 60 + fine.minute) - (inizio.hour * 60 + inizio.minute)
    return max(4.0, minuti / max(quota, 1) * random.uniform(0.6, 1.4))


def leggi_prossimo():
    try:
        return json.load(open(PROSSIMO))
    except Exception:
        return {}


def scrivi_prossimo(d):
    os.makedirs(db.DATI, exist_ok=True)
    json.dump(d, open(PROSSIMO, 'w'), indent=1)


# --- invio -------------------------------------------------------------------

def registra_invio(c, m, casella, msg):
    ora = datetime.now()
    c.execute("UPDATE messaggi SET casella=?, message_id=?, inviato=?, esito='ok' WHERE id=?",
              (casella, msg['Message-ID'], ora.isoformat(timespec='seconds'), m['id']))
    if m['tipo'] == 'primo':
        a = c.execute('SELECT settore FROM aziende WHERE piva=?', (m['piva'],)).fetchone()
        ogg, corpo = testi.seguito(a['settore'] if a else None, m['oggetto'], config.leggi().get('TELEFONO', ''))
        c.execute("INSERT INTO messaggi(piva, tipo, casella, a, oggetto, corpo, in_risposta, scritto, da_mandare) "
                  "VALUES (?,?,?,?,?,?,?,?,?)",
                  (m['piva'], 'seguito', casella, m['a'], ogg, corpo, msg['Message-ID'], db.adesso(),
                   config.piu_lavorativi(ora, config.GIORNI_SEGUITO).isoformat(timespec='seconds')))
        db.metti_fase(c, m['piva'], 'inviata')
    else:
        db.metti_fase(c, m['piva'], 'seguita')


def codice(err):
    """Il codice SMTP di un rifiuto: 550, 554, 421..."""
    if isinstance(err, smtplib.SMTPRecipientsRefused):
        return next(iter(err.recipients.values()))[0]
    return getattr(err, 'smtp_code', 0)


def rifiuto(c, m, casella, err):
    testo, cod = str(err), codice(err)
    c.execute("UPDATE messaggi SET esito=? WHERE id=?", (f'errore {cod}: ' + testo[:300], m['id']))
    c.execute('INSERT INTO eventi(quando, piva, casella, tipo, da, testo) VALUES (?,?,?,?,?,?)',
              (db.adesso(), m['piva'], casella, 'errore', m['a'], f'{cod} {testo[:1000]}'))
    basso = testo.lower()
    if any(k in basso for k in ('5.7.', 'spam', 'blocked', 'blacklist', 'reputation', 'policy')):
        metti_freno(f'rifiuto del server su {m["a"]} da {casella}: {testo[:200]}')
    elif 500 <= cod < 600:
        db.metti_fase(c, m['piva'], 'rimbalzata', f'rifiutato dal server ({cod}): ' + testo[:200])
    else:
        # 4xx: rifiuto temporaneo, il messaggio torna in coda al prossimo giro
        c.execute("UPDATE messaggi SET esito=NULL WHERE id=?", (m['id'],))


def giro():
    cfg = config.leggi()
    if os.path.exists(FRENO):
        log('fermo: c\'è il freno →', open(FRENO).read().strip())
        return
    if not config.in_finestra():
        return
    if not cfg['caselle']:
        log('nessuna casella configurata in', config.FILE)
        return
    prossimo = leggi_prossimo()
    caselle = list(cfg['caselle'])
    random.shuffle(caselle)
    with db.connessione() as c:
        stati = stato_caselle(c, caselle)
        for casella, password in caselle:
            st = stati[casella]
            if st['oggi'] >= st['quota']:
                continue
            if prossimo.get(casella, '') > db.adesso():
                continue
            m = prossimo_per(c, casella)
            if not m:
                continue
            if not cfg['attivo']:
                log('PROVA (ATTIVO=0), non parte:', casella, '→', m['a'], '|', m['tipo'], '|', m['oggetto'])
                prossimo[casella] = (datetime.now() + timedelta(minutes=intervallo(st['quota']))).isoformat(timespec='seconds')
                continue
            msg = componi(m, casella)
            try:
                s = smtp(cfg, casella, password)
                s.send_message(msg)
                s.quit()
            except smtplib.SMTPAuthenticationError as e:
                log('login rifiutato', casella, e)
                c.execute('INSERT INTO eventi(quando, casella, tipo, testo) VALUES (?,?,?,?)',
                          (db.adesso(), casella, 'errore', f'login rifiutato: {e}'))
                continue
            except smtplib.SMTPSenderRefused as e:
                # il server rifiuta noi, non il destinatario: si ferma tutto
                metti_freno(f'il server rifiuta il mittente {casella}: {e}')
                return
            except (smtplib.SMTPRecipientsRefused, smtplib.SMTPDataError) as e:
                rifiuto(c, m, casella, e)
                c.commit()
                continue
            except Exception as e:
                log('errore di rete, si riprova al prossimo giro', casella, e)
                continue
            registra_invio(c, m, casella, msg)
            c.commit()
            copia_in_inviata(cfg, casella, password, msg)
            log('mandata', casella, '→', m['a'], '|', m['tipo'], '|', m['oggetto'])
            prossimo[casella] = (datetime.now() + timedelta(minutes=intervallo(st['quota']))).isoformat(timespec='seconds')
    scrivi_prossimo(prossimo)


def prova(mid):
    cfg = config.leggi()
    a = cfg.get('PROVA_A')
    if not a or not cfg['caselle']:
        sys.exit('servono PROVA_A e almeno una casella in ' + config.FILE)
    casella, password = cfg['caselle'][0]
    with db.connessione() as c:
        m = c.execute('SELECT * FROM messaggi WHERE id=?', (mid,)).fetchone()
        if not m:
            sys.exit(f'messaggio {mid} non trovato')
        msg = componi(dict(m, message_id=None), casella, a=a)
        msg.replace_header('Subject', '[PROVA per ' + m['a'] + '] ' + m['oggetto'])
    s = smtp(cfg, casella, password)
    s.send_message(msg)
    s.quit()
    copia_in_inviata(cfg, casella, password, msg)
    log('prova mandata', casella, '→', a, '| messaggio', mid)


if __name__ == '__main__':
    if '--togli-freno' in sys.argv:
        if os.path.exists(FRENO):
            os.remove(FRENO)
        log('freno tolto a mano')
    elif '--prova' in sys.argv:
        prova(int(sys.argv[sys.argv.index('--prova') + 1]))
    else:
        giro()
