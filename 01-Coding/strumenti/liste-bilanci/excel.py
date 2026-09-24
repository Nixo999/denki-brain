# Il file per Seba: come si usa, 100 da chiamare, riserva, com'e' fatta. Piu' i CSV per il vault.
import json, os, sys, csv, re, statistics, collections
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
DEST = sys.argv[1]
BASE = sys.argv[2]
N = 100
ESITI = ['Non risponde', 'Richiamare', "Non è il decisore", 'No', 'Troppo piccoli', 'Fissato incontro']
GANCIO = {
    'Facchinaggio': "Squadre su più commesse ogni giorno. Chi va dove e quante ore ha fatto, senza il giro di telefonate la sera prima.",
    'Allestimento': "Montaggi e smontaggi su più cantieri nella stessa settimana. La squadra e le ore da fatturare al cliente stanno in un posto solo.",
}
SCURO = PatternFill('solid', fgColor='FF0F2A2E')
TEAL = PatternFill('solid', fgColor='FFD9EFEE')
GIALLO = PatternFill('solid', fgColor='FFFFF2B3')
BIANCO = Font(bold=True, color='FFFFFFFF')
FILO = Border(bottom=Side(style='thin', color='FFD0D7D8'))

d = json.load(open(os.path.join(HERE, 'finale.json')))
tenute, scarti = d['tenute'], d['scarti']
chiamare = tenute[:N]
# le aziende del settore, in fascia ed entro 30 km, per cui il numero pubblico non e' risultato
_SET = {'52.24.4': 'Facchinaggio', '52.24': 'Facchinaggio', '77.39.94': 'Allestimento', '90.02.01': 'Allestimento'}
_ok = {r['piva'] for r in tenute}
senza = sorted([x for x in json.load(open(os.path.join(HERE, 'trovate.json'))).values()
                if not x['scartata'] and not x['esito'] and x['ateco_lista'] in _SET and x['km'] is not None and x['km'] <= 30
                and x['piva'] not in _ok and (x.get('personale') is None or x['personale'] >= 60000)
                and 250000 <= (x['fatturato'] or 0) <= 10000000 and 'LIQUIDAZ' not in x['nome'].upper()],
               key=lambda x: (x['km'], -x['fatturato']))
for x in senza:
    x['settore'] = _SET[x['ateco_lista']]
riserva = senza


def fonte(r):
    adr = r['pg']['adr']
    if r['livello'] == 'altra-sede':
        return f"Pagine Gialle: stessa ragione sociale, sede operativa a {r['comune']}"
    if r['livello'] == 'via':
        return 'Pagine Gialle: nome in parte diverso, stessa via della sede legale'
    if r['livello'] == 'senza-titolare':
        return 'Pagine Gialle: stesso nome senza il titolare, stesso comune'
    return 'Pagine Gialle: stessa ragione sociale, stesso comune'


def via(adr):
    return adr.split(' - ')[0].strip()


COLONNE = [('#', 5), ('Comune', 16), ('km', 6), ('Azienda', 36), ('Settore', 14), ('Cosa fanno', 34), ('Fatturato', 13),
           ('Anno', 6), ('Costo del personale', 13), ('Dipendenti', 13), ('Indirizzo', 30), ('Telefono', 15),
           ('Altri numeri', 22), ('Gancio', 58), ('Referente (da chiedere)', 22), ('Esito', 18), ('Data richiamo', 13),
           ('Note', 30), ('Fonte del numero', 44)]


def valori(i, r):
    tel = r['pg']['tel']
    return [i, r['comune'], r['km'], r['nome'].title() if r['nome'].isupper() else r['nome'], r['settore'], r['pg']['cat'],
            r['fatturato'], r['anno'], r['personale'], r['dipendenti'] or 'n.d.', via(r['pg']['adr']), tel[0],
            ' · '.join(tel[1:]) or None, GANCIO[r['settore']], None, None, None, None, fonte(r)]


def foglio_righe(ws, righe):
    ws.append([c for c, _ in COLONNE])
    for j, (c, w) in enumerate(COLONNE, 1):
        cell = ws.cell(1, j)
        cell.font, cell.fill = BIANCO, SCURO
        cell.alignment = Alignment(vertical='center', wrap_text=True)
        ws.column_dimensions[get_column_letter(j)].width = w
    ws.row_dimensions[1].height = 30
    for i, r in enumerate(righe, 1):
        ws.append(valori(i, r))
        for j in range(1, len(COLONNE) + 1):
            c = ws.cell(i + 1, j)
            c.alignment = Alignment(vertical='top', wrap_text=j in (4, 6, 14, 19))
            c.border = FILO
        ws.cell(i + 1, 7).number_format = '#,##0 €'
        ws.cell(i + 1, 9).number_format = '#,##0 €'
        ws.cell(i + 1, 3).number_format = '0.0'
        if (r['personale'] or 0) >= 500000:
            ws.cell(i + 1, 9).fill = GIALLO
    last = len(righe) + 1
    ws.freeze_panes = 'E2'
    ws.auto_filter.ref = f'A1:{get_column_letter(len(COLONNE))}{last}'
    dv = DataValidation(type='list', formula1='"' + ','.join(ESITI) + '"', allow_blank=True,
                        error='Usa uno dei sei valori del menu: il conto degli esiti gira su quelle parole.', showErrorMessage=True)
    ws.add_data_validation(dv)
    dv.add(f'P2:P{last}')
    dvd = DataValidation(type='date', allow_blank=True)
    ws.add_data_validation(dvd)
    dvd.add(f'Q2:Q{last}')
    for rr in range(2, last + 1):
        ws.cell(rr, 17).number_format = 'DD/MM/YYYY'


wb = Workbook()
ws = wb.active
ws.title = 'Come si usa'
cnt = collections.Counter(r['settore'] for r in chiamare)
kmax = max(r['km'] for r in chiamare)
testo = [
    ('LISTA CHIAMATE OPERO: FACCHINAGGIO E ALLESTIMENTO', None),
    ('Preparata da DenkiCode il 25 settembre 2026', None),
    (None, None),
    ("Cosa c'è dentro", f"{N} aziende da chiamare, {cnt['Facchinaggio']} di facchinaggio e {cnt['Allestimento']} di allestimento. "
                        f"Si parte da Seveso e ci si allontana: la prima è a {str(chiamare[0]['km']).replace('.', ',')} km, l'ultima a {str(kmax).replace('.', ',')} km. "
                        f"Nel foglio Senza numero ce ne sono altre {len(senza)} entro 30 km, stessi criteri: il numero pubblico non è risultato e va cercato sul loro sito."),
    ('Il criterio', "Fatturato tra 250.000 € e 10 milioni, azienda attiva al registro imprese, nessuna in liquidazione. "
                    "Un numero di telefono compare una volta sola: le società dello stesso gruppo sullo stesso centralino sono una riga."),
    ('Il fatturato', "È quello dell'ultimo bilancio depositato. L'anno sta nella colonna accanto e cambia da azienda ad azienda: "
                     "un bilancio vecchio vale come ordine di grandezza, non come numero di oggi."),
    ('Il costo del personale', "Dice quanta gente lavora davvero, meglio della fascia dipendenti. Nelle cooperative la fascia spesso manca. "
                               "La cella è gialla da 500.000 € in su, cioè una squadra vera."),
    ('Cosa fanno', "La categoria con cui l'azienda si presenta su Pagine Gialle. Serve a capire prima di chiamare se montano stand, "
                   "noleggiano strutture o fanno service tecnico."),
    ('Il telefono', "È il numero pubblico dell'azienda, con la stessa ragione sociale del bilancio. "
                    "Nessuno l'ha ancora chiamato: il primo squillo è anche la verifica. La colonna Fonte del numero dice come è stato abbinato."),
    ('Il referente', "Non c'è, per nessuna. Si chiede al centralino chi organizza le squadre e i turni, e si scrive il nome nella colonna."),
    ('La distanza', "In linea d'aria da Seveso all'indirizzo, non in strada."),
    (None, None),
    ('La colonna Esito', "Ha un menu a tendina con sei valori: " + ' · '.join(ESITI) + ". "
                         "Scrivere altro non si può, così a fine settimana il conto torna."),
    ('Le chiamate che contano', "Quelle con un esito diverso da «Non risponde». Sono le conversazioni vere."),
    ('Quando chiamare', "Facchinaggio a metà mattina, fra le 9:30 e le 11:30, quando le squadre sono già uscite. "
                        "Allestimento lontano dalle date delle fiere: in settimana di montaggio non risponde nessuno."),
]
for a, b in testo:
    ws.append([a, b])
ws.column_dimensions['A'].width = 26
ws.column_dimensions['B'].width = 100
ws['A1'].font = Font(bold=True, size=14, color='FF0F2A2E')
ws['A2'].font = Font(italic=True, color='FF5B6B6D')
for row in ws.iter_rows(min_row=4):
    row[0].font = Font(bold=True, color='FF0F2A2E')
    row[0].alignment = Alignment(vertical='top')
    row[1].alignment = Alignment(wrap_text=True, vertical='top')

foglio_righe(wb.create_sheet('Da chiamare'), chiamare)
ws = wb.create_sheet('Senza numero')
COL2 = [('#', 5), ('Comune', 18), ('km', 6), ('Azienda', 40), ('Settore', 14), ('Attività (ATECO)', 44), ('Fatturato', 13),
        ('Anno', 6), ('Costo del personale', 13), ('Dipendenti', 13), ('Indirizzo della sede', 32), ('Telefono trovato', 16), ('Note', 30)]
ws.append([c for c, _ in COL2])
for j, (c, w) in enumerate(COL2, 1):
    ws.cell(1, j).font, ws.cell(1, j).fill = BIANCO, SCURO
    ws.cell(1, j).alignment = Alignment(vertical='center', wrap_text=True)
    ws.column_dimensions[get_column_letter(j)].width = w
ws.row_dimensions[1].height = 30
for i, x in enumerate(senza, 1):
    nome = x['nome'].title() if x['nome'].isupper() else x['nome']
    ws.append([i, x['comune_nome'].title(), x['km'], nome, x['settore'], x.get('attivita'), x['fatturato'], x.get('anno'),
               x.get('personale'), x.get('dipendenti') or 'n.d.', x.get('indirizzo'), None, None])
    ws.cell(i + 1, 7).number_format = '#,##0 €'
    ws.cell(i + 1, 9).number_format = '#,##0 €'
    if (x.get('personale') or 0) >= 500000:
        ws.cell(i + 1, 9).fill = GIALLO
    for j in range(1, len(COL2) + 1):
        ws.cell(i + 1, j).border = FILO
        ws.cell(i + 1, j).alignment = Alignment(vertical='top', wrap_text=j in (4, 6))
ws.freeze_panes = 'E2'
ws.auto_filter.ref = f'A1:{get_column_letter(len(COL2))}{len(senza) + 1}'

ws = wb.create_sheet("Com'è fatta")
ws.append(["COM'È FATTA LA LISTA DA CHIAMARE"])
ws['A1'].font = Font(bold=True, size=13, color='FF0F2A2E')
ws.append([])
ws.append(['Settore', 'Righe', 'Fatturato mediano', 'Con costo del personale da 500.000 € in su'])
for c in ws[3]:
    c.font, c.fill = BIANCO, SCURO
for s in ('Facchinaggio', 'Allestimento'):
    rr = [r for r in chiamare if r['settore'] == s]
    if rr:
        ws.append([s, len(rr), statistics.median(r['fatturato'] for r in rr), sum(1 for r in rr if (r['personale'] or 0) >= 500000)])
        ws.cell(ws.max_row, 3).number_format = '#,##0 €'
ws.append([])
ws.append(['Distanza da Seveso', 'Righe'])
for c in ws[ws.max_row]:
    c.font, c.fill = BIANCO, SCURO
fasce = [(0, 10), (10, 20), (20, 30), (30, 50), (50, 999)]
for a, b in fasce:
    n = sum(1 for r in chiamare if a <= r['km'] < b)
    if n:
        ws.append([f'{a}-{b} km' if b < 999 else f'oltre {a} km', n])
ws.append([])
ws.append(['Comuni con più righe', 'Righe'])
for c in ws[ws.max_row]:
    c.font, c.fill = BIANCO, SCURO
for com, n in collections.Counter(r['comune'] for r in chiamare).most_common(10):
    ws.append([com, n])
for col, w in zip('ABCD', (30, 10, 20, 40)):
    ws.column_dimensions[col].width = w

wb.save(os.path.join(DEST, BASE + '.xlsx'))

# CSV per il vault, con la prova completa
campi = ['comune', 'km', 'nome', 'piva', 'settore', 'cat_pg', 'fatturato', 'anno', 'personale', 'dipendenti', 'indirizzo_pg',
         'indirizzo_legale', 'telefono', 'altri', 'fonte', 'livello', 'link_pg', 'ateco', 'attivita']
for nome, righe in ((BASE + '.csv', chiamare),):
    with open(os.path.join(DEST, nome), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(campi)
        for r in righe:
            w.writerow([r['comune'], r['km'], r['nome'], r['piva'], r['settore'], r['pg']['cat'], r['fatturato'], r['anno'],
                        r['personale'], r['dipendenti'], r['pg']['adr'], r['indirizzo_legale'], r['pg']['tel'][0],
                        ' · '.join(r['pg']['tel'][1:]), r['fonte'], r['livello'], r['pg'].get('link'), r['ateco'], r['attivita']])
with open(os.path.join(DEST, BASE + '-senza-numero.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['comune', 'km', 'nome', 'piva', 'settore', 'ateco', 'attivita', 'fatturato', 'anno', 'personale', 'dipendenti', 'indirizzo', 'prova'])
    for x in senza:
        w.writerow([x['comune_nome'], x['km'], x['nome'], x['piva'], x['settore'], x.get('ateco'), x.get('attivita'), x['fatturato'],
                    x.get('anno'), x.get('personale'), x.get('dipendenti'), x.get('indirizzo'), x['prova']])
print('scritto', len(chiamare), len(senza), dict(cnt), 'km max', kmax)
