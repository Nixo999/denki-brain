# Scheda companyreports di un'azienda: indirizzo, anno, personale, dipendenti, stato, forma, attivita'.
import re, html, cr_ateco
def campo(s, etichetta, fino):
    m = re.search(re.escape(etichetta) + r'\s*\n(.*?)\n' + re.escape(fino), s, re.S)
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else None
def leggi(x):
    t = cr_ateco.get('https://www.companyreports.it/' + x['slug'])
    t = re.sub(r'<script.*?</script>|<style.*?</style>', '', t, flags=re.S)
    s = html.unescape(re.sub(r'<[^>]+>', '\n', t)); s = re.sub(r'[ \t]*\n\s*', '\n', s)
    x['indirizzo'] = (campo(s, 'Indirizzo', 'Fatturato') or '').split(' - ')[0].strip()
    m = re.search(r'Fatturato\n€ ([\d.]+)\n\((\d{4})\)', s); x['anno'] = int(m.group(2)) if m else None
    m = re.search(r'Costo del personale\n€ (-?[\d.]+)\n\((\d{4})\)', s); x['personale'] = int(m.group(1).replace('.', '')) if m else None
    x['dipendenti'] = campo(s, 'N. Dipendenti', 'Stato Attività')
    x['stato'] = campo(s, 'Stato Attività', 'Condividi')
    x['forma'] = campo(s, 'Forma giuridica', 'Codice Ateco')
    x['ateco'] = campo(s, 'Codice Ateco', 'Attività prevalente')
    x['attivita'] = campo(s, 'Attività prevalente', 'Fondazione')
    x['fondazione'] = campo(s, 'Fondazione', 'CamCom')
    return x
