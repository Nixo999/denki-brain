#!/usr/bin/env python3
"""Il piano del giorno per /banco: quali settori, in quali luoghi, quante righe.

Esiste perche' la sessione sceglieva a mano da un elenco in prosa: ripeteva
settori gia' bocciati e apriva settori che su Instagram non esistono. Regola di
Nicola, 1/10/2026: ricircolo di settori e luoghi, priorita' a lead ad alta
conversione, tenendo conto del metodo di contatto. Qui le scelte sono numeri.

    python3 prossimo-giro.py [--lista siti|ricerca] [--n N] [--oggi YYYY-MM-DD]
    python3 prossimo-giro.py --autotest

Sola lettura: settori.csv, rotazione.csv, lista-corrente.csv, risposte-dm.csv.
Priorita' di una cella (luogo, settore) = resa_settore x resa_luogo x freschezza
x vicinanza a Seveso. Le celle esaurite tornano in gioco 30 giorni dopo.
"""
import argparse, collections, csv, datetime, re, sys
from pathlib import Path

SALES = Path(__file__).resolve().parent.parent
ORDINE = {"siti": "MB CO MI LC VA BG NO LO PV VB VC PC SO BS BI CR AL AT TO PR GE MN AO VR".split(),
          "ricerca": "MB CO MI LC VA BG LO PV SO BS CR MN".split()}
RIGHE = {"siti": 100, "ricerca": 60}
CELLE = {"siti": 4, "ricerca": 3}
POSITIVI = {"caldo", "CHIEDE", "tiepido", "rimanda", "ricerca", "siti"}
RIAPRE, MEDIA_COSTR, PER_LUOGO, RISERVE = 30, 0.14, 2, 3


def leggi(p):
    return list(csv.DictReader((SALES / p).open(encoding="utf-8-sig", newline="")))


def giorno(s):
    try:
        return datetime.date.fromisoformat((s or "").strip())
    except ValueError:
        return None


def resa(pos, inv):
    # ponytail: (positivi+1)/(inviati+60) = media di partenza 1,7%: un settore mai
    # misurato parte dalla media. Rivedere quando un settore supera ~100 inviati
    # letti: li' il +60 pesa poco e il dato vince da solo.
    return (pos + 1) / (inv + 60)


def carica():
    sett, rot = leggi("liste/settori.csv"), leggi("liste/rotazione.csv")
    banco, risp = leggi("strumenti/lista-corrente.csv"), leggi("liste/risposte-dm.csv")
    pos = {r["Account IG"].lower().lstrip("@") for r in risp if r["Tipo"] in POSITIVI}
    h = lambda r: r["Account IG"].lower().lstrip("@")
    # Il taglio e' l'ultimo giorno d'invio che ha avuto almeno una risposta scritta:
    # i DM mandati dopo non sono ancora stati letti, contarli abbasserebbe il tasso.
    con_risposta = {x["Account IG"].lower().lstrip("@") for x in risp}
    taglio = max(d for r in banco if h(r) in con_risposta and (d := giorno(r["DM inviato (data)"])))
    rx = {l: [(s["Settore"], re.compile(s["Parole"], re.I)) for s in sett if s["Lista"] == l] for l in ORDINE}
    evitare = {(s["Lista"], s["Settore"]) for s in sett if s["Stato"] == "evitare"}
    per_s, per_l, mai = (collections.defaultdict(lambda: [0, 0]) for _ in range(3))
    for r in banco:
        d, p = giorno(r["DM inviato (data)"]), r["Prodotto"]
        if not d:  # stessa condizione di stato-banco.py: mai mandata e non SCARTATO
            if not re.match(r"scartat", (r["Esito DM"] or "").strip(), re.I):
                mai[p][1] += 1
            continue
        if d > taglio:
            continue
        m = re.search(r"\((\w\w)\)\s*$", r["Comune (prov)"] or "")
        # le liste di settembre hanno Prodotto vuoto: il settore si cerca in tutte e due
        s = min(((x.start(), i, l, n) for l in ([p] if p else ORDINE) for i, (n, q) in enumerate(rx.get(l, ()))
                 if (x := q.search(r["Segmento"] or ""))), default=None)
        if s:
            per_s[s[2:]][0] += h(r) in pos
            per_s[s[2:]][1] += 1
        # la resa di un luogo non conta i settori da evitare: Varese e Como erano
        # piene di ristorazione, che al DM non risponde mai
        if m and not (s and s[2:] in evitare):
            per_l[m[1].upper()][0] += h(r) in pos
            per_l[m[1].upper()][1] += 1
    return dict(sett=sett, rot=rot, per_s=per_s, per_l=per_l, mai=mai)


def costruzione(nota):
    m = re.search(r"(\d+) profili, (\d+) rig", nota or "")
    return (int(m[2]), int(m[1])) if m else None


def piano(lista, D, oggi, righe):
    """(celle del piano, celle di riserva), ciascuna un dict."""
    ordine = ORDINE[lista]
    rot = {(r["Luogo"], r["Settore"]): r for r in D["rot"] if r["Lista"] == lista}
    attivi = [s["Settore"] for s in D["sett"] if s["Lista"] == lista and s["Stato"] == "attivo" and s["Canale"] == "dm"]
    ultime = collections.defaultdict(list)  # settore -> date delle sue celle
    medie = collections.defaultdict(lambda: [0, 0])  # settore -> righe, profili
    for (l, s), r in rot.items():
        if giorno(r["Ultima lista"]):
            ultime[s].append(giorno(r["Ultima lista"]))
        if costruzione(r["Nota"]):
            medie[s][0] += costruzione(r["Nota"])[0]
            medie[s][1] += costruzione(r["Nota"])[1]
    celle = []
    for s in attivi:
        for i, l in enumerate(ordine):
            r, riaperta, u = rot.get((l, s)), False, None
            if r:
                u = giorno(r["Ultima lista"])
                if r["Stato"] == "esaurito":
                    if not u or (oggi - u).days < RIAPRE:
                        continue  # senza data resta fuori
                    riaperta = True
            fresco = (0.5 if any((oggi - d).days <= 2 for d in ultime[s]) else 1) * \
                     (0.5 if u and (oggi - u).days <= 7 else 1)
            c = costruzione(r["Nota"]) if r else None
            stimata = c is None
            c = c or (medie[s] if medie[s][1] else (MEDIA_COSTR, 1))
            ps, ns = D["per_s"][(lista, s)]
            pl, nl = D["per_l"][l]
            celle.append(dict(luogo=l, settore=s, riaperta=riaperta, ultima=u, pos=ps, inv=ns, stimata=stimata,
                              costr=c[0] / c[1], pri=resa(ps, ns) * resa(pl, nl) * fresco / (1 + 0.1 * i), i=i))
    celle.sort(key=lambda c: (-c["pri"], -c["costr"], c["i"], c["settore"]))

    def scegli(k, fuori=()):  # golosa: un settore una volta, al massimo 2 celle per luogo
        out, usati, luoghi = [], set(), collections.Counter()
        for c in celle:
            if c in fuori or c["settore"] in usati or luoghi[c["luogo"]] >= PER_LUOGO:
                continue
            out.append(c), usati.add(c["settore"]), luoghi.update([c["luogo"]])
            if len(out) == k:
                break
        return out
    p = scegli(CELLE[lista])
    return p, scegli(RISERVE, p)


def data_it(d):
    return f"{d.day}/{d.month:02d}"


def testo(oggi, liste, n, D):
    mai = D["mai"]
    elide = "dell'" if oggi.day in (1, 8, 11, 18) else "del "
    out = [f"Giro {elide}{oggi.day}/{oggi.month}/{oggi.year} — sul banco {sum(v[1] for v in mai.values())} righe mai "
           f"mandate (siti {mai['siti'][1]} · ricerca {mai['ricerca'][1]})"]
    for lista in liste:
        tot = n or RIGHE[lista]
        p, riserva = piano(lista, D, oggi, tot)
        base, resto = divmod(tot, len(p))
        out.append(f"\n{lista.upper()} — {tot} righe")
        for k, c in enumerate(p, 1):
            costr = f"{'~' if c['stimata'] else ''}{c['costr'] * 100:.1f}%".replace(".", ",")
            extra = ("riaperta" if c["riaperta"] else f"ultima {data_it(c['ultima'])}" if c["ultima"] else "mai aperta")
            out.append(f"  {k}. {c['luogo']} · {c['settore']} · {base + (resto if k == 1 else 0)} righe   "
                       f"[DM {c['pos']}/{c['inv']} · costruzione {costr} · {extra}]")
        out.append("  riserva (se una cella rende meno di 1 riga su 5 profili dopo i primi 30): " +
                   " | ".join(f"{c['luogo']} · {c['settore']}" + (" (riaperta)" if c["riaperta"] else "") for c in riserva))
        tel = [f"{s['Settore']} ({s['Nota']})" for s in D["sett"]
               if s["Lista"] == lista and s["Stato"] == "evitare" and s["Canale"] == "telefono"]
        if tel:
            out.append("  al telefono, non in DM: " + " · ".join(tel))
        pausa = [s["Settore"] for s in D["sett"] if s["Lista"] == lista and s["Stato"] == "pausa"]
        if pausa:
            out.append("  in pausa: " + ", ".join(pausa))
    return "\n".join(out)


def autotest():
    D, oggi = carica(), datetime.date.today()
    stato = {(s["Lista"], s["Settore"]): (s["Stato"], s["Canale"]) for s in D["sett"]}
    rot = {(r["Lista"], r["Luogo"], r["Settore"]): r for r in D["rot"]}
    for (l, _, s) in rot:  # i nomi devono essere identici a rotazione.csv
        assert s == "altro" or (l, s) in stato, f"settore fuori da settori.csv: {l}/{s}"
    riaperte = 0
    for data_, tot in ((oggi, 0), (datetime.date(2026, 11, 15), 1)):
        for lista in ORDINE:
            p, r = piano(lista, D, data_, RIGHE[lista])
            assert len(p) == CELLE[lista] and len({c["settore"] for c in p}) == len(p), "settore doppio nel piano"
            for c in p + r:
                assert stato[(lista, c["settore"])] == ("attivo", "dm"), f"settore non attivo: {c['settore']}"
                x = rot.get((lista, c["luogo"], c["settore"]))
                if x and x["Stato"] == "esaurito":
                    assert (data_ - giorno(x["Ultima lista"])).days >= RIAPRE and c["riaperta"], "esaurita troppo presto"
                riaperte += tot * c["riaperta"]
    assert riaperte, "il 15/11 nessuna cella riaperta"
    assert testo(oggi, list(ORDINE), 0, D) == testo(oggi, list(ORDINE), 0, D), "non deterministico"
    print(f"autotest ok (celle riaperte al 15/11 fra piano e riserva: {riaperte})")


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--lista", choices=list(ORDINE)), a.add_argument("--n", type=int)
    a.add_argument("--oggi", type=datetime.date.fromisoformat, default=datetime.date.today())
    a.add_argument("--autotest", action="store_true")
    o = a.parse_args()
    autotest() if o.autotest else print(testo(o.oggi, [o.lista] if o.lista else list(ORDINE), o.n, carica()))
