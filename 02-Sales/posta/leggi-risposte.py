#!/usr/bin/env python3
"""Legge le caselle e riconosce cosa è tornato indietro dalle mail mandate.

    python3 02-Sales/posta/leggi-risposte.py

Non segna niente come letto: la posta resta da leggere per Patrick. Si ricorda
cosa ha già visto con l'UID IMAP (tabella `eventi`, colonna `uid`).

Quattro casi, e solo per le mail che riguardano la campagna:
- **rimbalzo**: avviso del server (mailer-daemon, rapporto di consegna). Un
  errore permanente (5.x.x) segna l'azienda `rimbalzata`. Un rifiuto per spam
  (5.7.x, «spam», «blocked») mette il freno.
- **automatica**: fuori sede, risposta automatica. Non ferma il seguito.
- **disiscrizione**: risposta che chiede di non scrivere più. Il dominio entra
  nei disiscritti, per sempre.
- **risposta**: tutto il resto. L'azienda passa a `risposta`, il seguito non
  parte più, e la conversazione è di Patrick.

Una risposta si riconosce dal filo (In-Reply-To e References contengono il
Message-ID della nostra mail) oppure dal dominio del mittente, perché spesso
risponde un'altra persona dell'azienda dal suo indirizzo.

Alla fine controlla il freno dei rimbalzi: sopra il 5% delle mail di oggi, e
con almeno tre rimbalzi, l'invio si ferma.
"""
import email
import imaplib
import os
import re
import sys
from datetime import date, timedelta
from email.header import decode_header, make_header
from email.utils import getaddresses, parseaddr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config  # noqa: E402
import db      # noqa: E402
import manda   # noqa: E402

AUTOMATICA = re.compile(r'(risposta automatica|fuori sede|fuori ufficio|out of (the )?office|auto(matic)? ?reply|'
                        r'^auto:|assente|in ferie|vacation|abwesend)', re.I)
# Solo frasi chiare: «ci toglierebbe un sacco di lavoro» è un sì, non una disiscrizione.
# Quello che sfugge lo rilegge Claude nel giro del mattino (risposte.md).
DISISCRIZIONE = re.compile(r'(non (ci |mi )?(scriv|contatt|invi|mand)|cancellate(ci|mi)|cancellarci|rimuovete|'
                           r'rimuoverci|togliete(ci|mi)|toglierci|non (siamo|sono) interessat|'
                           r'non (ci |mi )?interessa|non interessat|no,? grazie|unsubscribe|disiscriv)', re.I)
SPAM = re.compile(r'(5\.7\.\d|spam|blocked|blacklist|block list|reputation|rejected for policy)', re.I)


def testo_di(msg):
    """Il testo in chiaro del messaggio, senza la parte citata."""
    parti = []
    for p in msg.walk():
        if p.get_content_type() == 'text/plain' and not p.get_filename():
            try:
                parti.append(p.get_payload(decode=True).decode(p.get_content_charset() or 'utf-8', 'ignore'))
            except Exception:
                pass
    if not parti:
        for p in msg.walk():
            if p.get_content_type() == 'text/html':
                h = p.get_payload(decode=True).decode(p.get_content_charset() or 'utf-8', 'ignore')
                parti.append(re.sub(r'<[^>]+>', ' ', h))
    t = '\n'.join(parti)
    tagli = [m.start() for m in re.finditer(r'(\n>|\nIl .{5,80} ha scritto:|\nOn .{5,80} wrote:|\n-----Original|'
                                           r'\nDa: |\nFrom: )', t)]
    return (t[:min(tagli)] if tagli else t).strip()


def intestazione(msg, nome):
    try:
        return str(make_header(decode_header(msg.get(nome, ''))))
    except Exception:
        return msg.get(nome, '') or ''


def destinatario_rimbalzato(msg):
    """Indirizzo e codice di un rapporto di mancata consegna."""
    for p in msg.walk():
        if p.get_content_type() == 'message/delivery-status':
            corpo = p.as_string()
            r = re.search(r'Final-Recipient:\s*rfc822;\s*<?([^\s>]+)', corpo, re.I)
            s = re.search(r'Status:\s*([245]\.\d+\.\d+)', corpo, re.I)
            if r:
                return r.group(1).lower(), (s.group(1) if s else '5.0.0'), corpo
    x = msg.get('X-Failed-Recipients')
    t = testo_di(msg)
    s = re.search(r'\b([45]\.\d\.\d+)\b', t)
    if x:
        return x.strip().lower(), (s.group(1) if s else '5.0.0'), t
    return None, None, t


def trova_azienda(c, msg, mittente):
    rif = ' '.join([msg.get('In-Reply-To', ''), msg.get('References', '')])
    for mid in re.findall(r'<[^>]+>', rif):
        r = c.execute('SELECT piva FROM messaggi WHERE message_id=?', (mid,)).fetchone()
        if r:
            return r['piva']
    dom = db.dominio(mittente)
    if dom:
        r = c.execute("SELECT piva FROM aziende WHERE email LIKE ? AND fase IN ('inviata','seguita','risposta')",
                      ('%@' + dom,)).fetchone()
        if r:
            return r['piva']
    return None


def leggi_casella(cfg, casella, password, dal):
    im = imaplib.IMAP4_SSL(cfg.get('IMAP_HOST', ''), int(cfg.get('IMAP_PORT', '993')), timeout=60)
    im.login(casella, password)
    im.select('INBOX', readonly=True)
    _, uv = im.status('INBOX', '(UIDVALIDITY)')
    uidvalidity = re.search(rb'UIDVALIDITY (\d+)', uv[0]).group(1).decode()
    _, dati = im.uid('search', None, 'SINCE', dal.strftime('%d-%b-%Y'))
    nuovi = 0
    with db.connessione() as c:
        for uid in (dati[0] or b'').split():
            chiave = f'{casella}:{uidvalidity}:{uid.decode()}'
            if c.execute('SELECT 1 FROM eventi WHERE uid=?', (chiave,)).fetchone():
                continue
            _, d = im.uid('fetch', uid, '(BODY.PEEK[])')
            if not d or not d[0]:
                continue
            msg = email.message_from_bytes(d[0][1])
            mittente = parseaddr(msg.get('From', ''))[1].lower()
            oggetto = intestazione(msg, 'Subject')
            evento = classifica(c, msg, mittente, oggetto)
            if not evento:
                # posta che non c'entra con la campagna: si ricorda l'UID e basta
                c.execute('INSERT INTO eventi(quando, casella, tipo, da, oggetto, uid) VALUES (?,?,?,?,?,?)',
                          (db.adesso(), casella, 'altro', mittente, oggetto[:200], chiave))
                continue
            tipo, piva, testo = evento
            c.execute('INSERT INTO eventi(quando, piva, casella, tipo, da, oggetto, testo, uid) VALUES (?,?,?,?,?,?,?,?)',
                      (db.adesso(), piva, casella, tipo, mittente, oggetto[:300], testo[:4000], chiave))
            nuovi += 1
            manda.log('letto', casella, tipo, mittente, '|', oggetto[:80])
    im.logout()
    return nuovi


def classifica(c, msg, mittente, oggetto):
    tipo_cont = msg.get_content_type()
    da_server = re.match(r'(mailer-daemon|postmaster|mail delivery)', mittente + ' ' + msg.get('From', ''), re.I)
    if da_server or tipo_cont == 'multipart/report':
        a, stato, testo = destinatario_rimbalzato(msg)
        if not a:
            return None
        r = c.execute('SELECT piva FROM messaggi WHERE lower(a)=? AND inviato IS NOT NULL', (a,)).fetchone()
        if not r:
            return None
        if stato.startswith('5'):
            db.metti_fase(c, r['piva'], 'rimbalzata', f'rimbalzo {stato}')
            if SPAM.search(testo or '') and stato.startswith('5.7'):
                manda.metti_freno(f'rimbalzo per spam su {a}: {stato}')
        return 'rimbalzo', r['piva'], f'{a} {stato}\n{(testo or "")[:1500]}'

    piva = trova_azienda(c, msg, mittente)
    if not piva:
        return None
    testo = testo_di(msg)
    auto = msg.get('Auto-Submitted', 'no').lower() != 'no' or msg.get('X-Autoreply') or msg.get('X-Autorespond')
    if auto or AUTOMATICA.search(oggetto) or AUTOMATICA.search(testo[:300]):
        return 'automatica', piva, testo
    if DISISCRIZIONE.search(testo[:600]) or DISISCRIZIONE.search(oggetto):
        dom = db.dominio(mittente)
        c.execute('INSERT OR IGNORE INTO disiscritti(dominio, quando, motivo) VALUES (?,?,?)',
                  (dom, db.adesso(), testo[:200]))
        db.metti_fase(c, piva, 'disiscritta', 'ha chiesto di non ricevere altro')
        return 'disiscrizione', piva, testo
    db.metti_fase(c, piva, 'risposta')
    return 'risposta', piva, testo


def controlla_freno():
    oggi = date.today().isoformat()
    with db.connessione() as c:
        mandate = c.execute("SELECT COUNT(*) FROM messaggi WHERE substr(inviato,1,10)=?", (oggi,)).fetchone()[0]
        rimbalzi = c.execute("SELECT COUNT(*) FROM eventi WHERE tipo='rimbalzo' AND substr(quando,1,10)=?", (oggi,)).fetchone()[0]
    if rimbalzi >= 3 and mandate and rimbalzi / mandate > config.FRENO_RIMBALZI:
        manda.metti_freno(f'rimbalzi oggi {rimbalzi} su {mandate} mandate, sopra il {config.FRENO_RIMBALZI:.0%}')


def main():
    cfg = config.leggi()
    if not cfg['caselle']:
        sys.exit('nessuna casella configurata in ' + config.FILE)
    with db.connessione() as c:
        primo = c.execute('SELECT MIN(inviato) FROM messaggi WHERE inviato IS NOT NULL').fetchone()[0]
    dal = (date.fromisoformat(primo[:10]) if primo else date.today()) - timedelta(days=1)
    for casella, password in cfg['caselle']:
        try:
            n = leggi_casella(cfg, casella, password, dal)
            print(casella, 'nuovi eventi:', n)
        except Exception as e:
            manda.log('lettura non riuscita', casella, e)
    controlla_freno()


if __name__ == '__main__':
    main()
