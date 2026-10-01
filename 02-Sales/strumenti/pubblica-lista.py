#!/usr/bin/env python3
"""Appende una lista del giorno al banco DM. Lo lancia /banco, e basta.

    python3 02-Sales/strumenti/pubblica-lista.py 02-Sales/liste/<lista>.csv [--banco denkicode] [--prova]

Esiste perche` ogni sessione improvvisava un add.py nella scratchpad: due
operatori se lo sono sovrascritto, e aprire lista-corrente.csv (2,1 MB, campi
multilinea) brucia il contesto. Qui il banco non si apre mai a mano.

Passi: controlla-lista.py (se non esce 0 ci si ferma, non c'e` modo di
saltarlo) -> righe rimappate sulle colonne del banco -> via chi e` gia` su uno
dei due banchi -> append in coda, senza riscrivere le righe esistenti ->
allinea-contattati.py e stato-banco.py. --prova fa tutto tranne scrivere e
tranne gli ultimi due.
"""
import csv, io, subprocess, sys, tempfile
from pathlib import Path

QUI = Path(__file__).resolve().parent
BANCHI = {"patrick": QUI / "lista-corrente.csv", "denkicode": QUI / "lista-denkicode.csv"}


def handle(s):
    return (s or "").strip().lstrip("@").lower()


def leggi(p):
    with p.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def prepara(lista, nome, banco, righe, visti):
    """Righe nuove con le colonne del banco, e quante ne ha saltate."""
    campi = banco
    extra = [c for c in lista if c not in campi]
    if extra:
        sys.exit(f"colonne della lista che il banco non ha: {', '.join(extra)}")
    nuove, saltate = [], 0
    for r in righe:
        h = handle(r.get("Account IG"))
        if h in visti:
            saltate += 1
            continue
        visti.add(h)                       # doppioni dentro la stessa lista compresi
        o = {c: r.get(c, "") for c in campi}
        if "Lista" in o and not o["Lista"].strip():
            o["Lista"] = nome
        if "Prodotto" in lista and o["Prodotto"] not in ("siti", "ricerca"):
            sys.exit(f"{r.get('Account IG')}: Prodotto «{o['Prodotto']}», deve essere siti o ricerca")
        nuove.append(o)
    return nuove, saltate


def pubblica(csv_lista, banco_path, altro_path, prova=False):
    campi_b, righe_b = leggi(banco_path)
    campi_l, righe_l = leggi(csv_lista)
    if "Prodotto" not in campi_l:
        sys.exit("manca la colonna Prodotto (siti o ricerca)")
    visti = {handle(r.get("Account IG")) for r in righe_b}
    if altro_path.exists():
        visti |= {handle(r.get("Account IG")) for r in leggi(altro_path)[1]}
    nuove, saltate = prepara(campi_l, csv_lista.stem, campi_b, righe_l, visti)
    if nuove and not prova:
        # append puro: se manca il newline finale lo aggiungo, il resto non si tocca
        with banco_path.open("rb") as f:
            f.seek(-1, 2)
            manca_nl = f.read(1) != b"\n"
        with banco_path.open("a", encoding="utf-8", newline="") as f:
            if manca_nl:
                f.write("\n")
            w = csv.DictWriter(f, fieldnames=campi_b, lineterminator="\n")
            w.writerows(nuove)
    return len(nuove), saltate


def main():
    a = sys.argv[1:]
    prova = "--prova" in a
    nome_banco = a[a.index("--banco") + 1] if "--banco" in a else "patrick"
    lista = [x for x in a if x.endswith(".csv")]
    if len(lista) != 1 or nome_banco not in BANCHI:
        sys.exit(__doc__)
    lista = Path(lista[0])
    c = subprocess.run([sys.executable, str(QUI / "controlla-lista.py"), str(lista)], capture_output=True, text=True)
    if c.returncode != 0:
        print(c.stdout + c.stderr)
        sys.exit(1)
    banco = BANCHI[nome_banco]
    altro = next(p for n, p in BANCHI.items() if n != nome_banco)
    n, m = pubblica(lista, banco, altro, prova)
    if not prova:
        for s in ("allinea-contattati.py", "stato-banco.py"):
            print(subprocess.run([sys.executable, str(QUI / s)], capture_output=True, text=True).stdout)
    print(f"pubblicate {n} righe su {nome_banco} (saltate {m} già presenti)" + (" [prova, niente scritto]" if prova else ""))


def demo():
    d = Path(tempfile.mkdtemp())
    testa = ["Account IG", "Nome attivita", "Messaggio", "Lista", "Prodotto"]

    def scrivi(p, righe, campi=testa):
        with p.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=campi, lineterminator="\n")
            w.writeheader()
            w.writerows(righe)
    banco, altro, lista = d / "banco.csv", d / "altro.csv", d / "2026-10-01-instagram-siti-x.csv"
    scrivi(banco, [dict(zip(testa, ["@a", "A", "riga uno\nsu due righe, con virgola", "old", "siti"])),
                   dict(zip(testa, ["@b", "B", "m", "old", "ricerca"]))])
    scrivi(altro, [])
    scrivi(lista, [dict(zip(testa, ["@C", "C", "m", "", "siti"])),
                   dict(zip(testa, ["@b", "B", "m", "", "siti"])),      # doppione, gia` sul banco
                   dict(zip(testa, ["@d", "D", "m", "", "ricerca"]))],
           ["Account IG", "Nome attivita", "Messaggio", "Lista", "Prodotto"])
    prima = banco.read_bytes()
    assert pubblica(lista, banco, altro) == (2, 1)
    assert banco.read_bytes().startswith(prima)            # le righe esistenti, byte per byte
    righe = leggi(banco)[1]
    assert len(righe) == 4 and righe[0]["Messaggio"].count("\n") == 1
    assert righe[2]["Lista"] == lista.stem
    assert pubblica(lista, banco, altro) == (0, 3)         # rilanciata: niente doppioni
    print("autotest ok:", banco)


if __name__ == "__main__":
    demo() if "--autotest" in sys.argv else main()
