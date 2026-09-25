# Coordinate dei comuni via Nominatim (1 richiesta al secondo, in cache), distanza da Seveso in linea d'aria.
import json, os, time, math, urllib.request, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(HERE, 'coord_comuni.json')
C = json.load(open(F)) if os.path.exists(F) else {}
PROV = {'MB': 'Monza e della Brianza', 'MI': 'Milano', 'CO': 'Como', 'VA': 'Varese', 'LC': 'Lecco', 'BG': 'Bergamo',
        'NO': 'Novara', 'PV': 'Pavia', 'LO': 'Lodi', 'CR': 'Cremona', 'BS': 'Brescia', 'SO': 'Sondrio', 'VB': 'Verbano-Cusio-Ossola',
        'MN': 'Mantova', 'TO': 'Torino', 'VC': 'Vercelli', 'BI': 'Biella', 'AT': 'Asti', 'AL': 'Alessandria', 'CN': 'Cuneo',
        'GE': 'Genova', 'SV': 'Savona', 'SP': 'La Spezia', 'IM': 'Imperia', 'PC': 'Piacenza', 'PR': 'Parma', 'RE': "Reggio nell'Emilia",
        'MO': 'Modena', 'BO': 'Bologna', 'FE': 'Ferrara', 'VR': 'Verona', 'VI': 'Vicenza', 'PD': 'Padova', 'RO': 'Rovigo', 'TN': 'Trento', 'AO': 'Valle d\'Aosta',
        'FI': 'Firenze', 'PO': 'Prato', 'PT': 'Pistoia', 'LU': 'Lucca', 'PI': 'Pisa', 'LI': 'Livorno', 'MS': 'Massa-Carrara',
        'VE': 'Venezia', 'TV': 'Treviso', 'BL': 'Belluno', 'RA': 'Ravenna', 'FC': 'Forlì-Cesena', 'RN': 'Rimini', 'BZ': 'Bolzano',
        'UD': 'Udine', 'PN': 'Pordenone', 'AR': 'Arezzo', 'SI': 'Siena'}
SEVESO = (45.6434655, 9.1373787)
def coord(comune, prov):
    k = f'{comune}|{prov}'
    if k in C: return C[k]
    q = urllib.parse.urlencode({'city': comune, 'county': PROV.get(prov, ''), 'country': 'Italy', 'format': 'json', 'limit': 1})
    r = json.load(urllib.request.urlopen(urllib.request.Request('https://nominatim.openstreetmap.org/search?' + q, headers={'User-Agent': 'DenkiCode-liste/1.0'}), timeout=30))
    if not r:
        q = urllib.parse.urlencode({'q': f'{comune}, {PROV.get(prov, "")}, Italia', 'format': 'json', 'limit': 1})
        r = json.load(urllib.request.urlopen(urllib.request.Request('https://nominatim.openstreetmap.org/search?' + q, headers={'User-Agent': 'DenkiCode-liste/1.0'}), timeout=30))
    C[k] = [float(r[0]['lat']), float(r[0]['lon'])] if r else None
    json.dump(C, open(F, 'w'), ensure_ascii=False)
    time.sleep(1.1)
    return C[k]
def km(a, b=SEVESO):
    la1, lo1, la2, lo2 = map(math.radians, [a[0], a[1], b[0], b[1]])
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))
