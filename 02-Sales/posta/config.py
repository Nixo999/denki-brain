"""Le caselle e le regole d'invio. Le password stanno fuori dal vault.

Il file vero è `~/.config/denki-posta/caselle.env` (permessi 600), con lo
stesso formato di `caselle.example.env`, che invece sta nel vault senza segreti.
"""
import os
from datetime import date, datetime, time, timedelta

FILE = os.environ.get('POSTA_CONFIG', os.path.expanduser('~/.config/denki-posta/caselle.env'))

# La rampa: mail al giorno per casella, per settimana dal primo invio di quella
# casella. Il dominio è quello vero (decisione del 18/10), quindi si sale piano.
RAMPA = [10, 20, 30]
FINESTRA = (time(9, 0), time(17, 30))     # orario d'ufficio, lunedì-venerdì
GIORNI_SEGUITO = 4                         # giorni lavorativi fra la prima mail e il seguito
FRENO_RIMBALZI = 0.05                      # sopra il 5% di rimbalzi in un giorno si ferma tutto

# Feste nazionali in cui non si manda niente. Pasquetta va aggiunta ogni anno.
FESTE = {
    date(2026, 11, 1), date(2026, 12, 8), date(2026, 12, 24), date(2026, 12, 25), date(2026, 12, 26),
    date(2026, 12, 31), date(2027, 1, 1), date(2027, 1, 6), date(2027, 3, 29), date(2027, 4, 25),
    date(2027, 5, 1), date(2027, 6, 2), date(2027, 8, 15),
}


def leggi():
    """Restituisce un dizionario con le chiavi del file e la lista `caselle` [(indirizzo, password)]."""
    cfg = {}
    if os.path.exists(FILE):
        for riga in open(FILE, encoding='utf-8'):
            riga = riga.strip()
            if not riga or riga.startswith('#') or '=' not in riga:
                continue
            k, v = riga.split('=', 1)
            cfg[k.strip()] = v.strip().strip('"').strip("'")
    caselle = []
    for i in range(1, 10):
        a, p = cfg.get(f'CASELLA_{i}'), cfg.get(f'PASSWORD_{i}')
        if a and p:
            caselle.append((a.lower(), p))
    cfg['caselle'] = caselle
    cfg['attivo'] = cfg.get('ATTIVO', '0') == '1'
    return cfg


def lavorativo(g):
    return g.weekday() < 5 and g not in FESTE


def in_finestra(t=None):
    if os.environ.get('POSTA_SEMPRE') == '1':   # solo per le prove fuori orario
        return True
    t = t or datetime.now()
    return lavorativo(t.date()) and FINESTRA[0] <= t.time() <= FINESTRA[1]


def piu_lavorativi(d, n):
    """La data `n` giorni lavorativi dopo `d`, alle 9."""
    g = d.date() if isinstance(d, datetime) else d
    while n > 0:
        g += timedelta(days=1)
        if lavorativo(g):
            n -= 1
    return datetime.combine(g, FINESTRA[0])


def quota(primo_invio, oggi=None):
    """Quante mail può mandare oggi una casella che ha cominciato il giorno `primo_invio`."""
    oggi = oggi or date.today()
    if primo_invio is None:
        return RAMPA[0]
    settimana = (oggi - primo_invio).days // 7
    return RAMPA[min(settimana, len(RAMPA) - 1)]
