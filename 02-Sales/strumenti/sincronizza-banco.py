#!/usr/bin/env python3
"""Riporta nel vault quello che il banco online ha segnato.

    BANCO_URL=https://... BANCO_TOKEN=... python3 02-Sales/strumenti/sincronizza-banco.py [--prova]
    python3 02-Sales/strumenti/sincronizza-banco.py --autotest

Dall'11/10/2026 il banco DM sta su Netlify e i gesti di Patrick finiscono in
Netlify Blobs, non piu' nel vault. Questo script scarica `contattati.csv` e
`gia-col-sito.csv` da `/api/esporta`, li UNISCE a quelli di `02-Sales/liste/`
(chiave Data, Da, handle) e riordina come faceva banco-server.py. Non toglie
mai una riga dal vault: un invio segnato dal banco vecchio resta. Un «Annulla»
fatto online dopo che la riga e' gia' arrivata qui, quindi, qui non si vede.
Poi lancia allinea-contattati.py, che porta le date dentro le liste.

Lo lancia .github/workflows/banco-sync.yml ogni mezz'ora. Solo libreria standard.
--prova scarica e conta, non scrive niente.
"""
import csv, io, os, subprocess, sys, urllib.request
from pathlib import Path

QUI = Path(__file__).resolve().parent
LISTE = QUI.parent / "liste"
FILE = {"contattati": LISTE / "contattati.csv", "gia-col-sito": LISTE / "gia-col-sito.csv"}
CAMPI = ["Data", "Da", "Account IG", "Nome", "Comune", "Segmento", "Tipo", "Lista"]


def righe(testo):
    return [{k: (r.get(k) or "") for k in CAMPI} for r in csv.DictReader(io.StringIO(testo))]


def chiave(r):
    return (r["Data"].strip(), r["Da"].strip(), r["Account IG"].strip().lstrip("@").lower())


def unisci(vault, online):
    """Le righe del vault, piu' quelle online che il vault non ha. Ordinate come il server."""
    viste = {chiave(r) for r in vault}
    nuove = [r for r in online if chiave(r) not in viste and not viste.add(chiave(r))]
    tutte = vault + nuove
    tutte.sort(key=lambda r: (r["Data"], r["Da"], r["Account IG"].lower()))
    return tutte, len(nuove)


def scarica(url, token, nome):
    req = urllib.request.Request(f"{url.rstrip('/')}/api/esporta?file={nome}",
                                 headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req, timeout=60) as r:
        testo = r.read().decode("utf-8")
    if testo.splitlines()[:1] != [",".join(CAMPI)]:
        sys.exit(f"{nome}: l'intestazione online non e' quella attesa, non scrivo niente")
    return testo


def autotest():
    v = righe("Data,Da,Account IG,Nome,Comune,Segmento,Tipo,Lista\n"
              "2026-10-02,Patrick Sappa,@Bravo,B,,,primo,l\n"
              "2026-10-01,Patrick Sappa,@alfa,A,,,primo,l\n")
    o = righe("Data,Da,Account IG,Nome,Comune,Segmento,Tipo,Lista\n"
              "2026-10-02,Patrick Sappa,@bravo,B,,,primo,l\n"       # gia' nel vault (maiuscole a parte)
              "2026-10-03,Patrick Sappa,@alfa,A,,,recupero,l\n"     # nuova
              "2026-10-03,Patrick Sappa,@alfa,A,,,recupero,l\n"     # doppia online: entra una volta
              "2026-09-30,DenkiCode,@zeta,Z,,,primo,l\n")           # nuova, va in cima
    tutte, n = unisci(v, o)
    assert n == 2, n
    assert [(r["Data"], r["Account IG"]) for r in tutte] == [
        ("2026-09-30", "@zeta"), ("2026-10-01", "@alfa"), ("2026-10-02", "@Bravo"), ("2026-10-03", "@alfa")], tutte
    assert unisci(v, [])[1] == 0 and len(unisci(v, [])[0]) == 2   # online vuoto: il vault resta com'e'
    assert unisci([], o)[1] == 3
    print("autotest: a posto")


def main():
    prova = "--prova" in sys.argv
    url, token = os.environ.get("BANCO_URL"), os.environ.get("BANCO_TOKEN")
    if not url or not token:
        sys.exit("servono BANCO_URL e BANCO_TOKEN nell'ambiente")
    for nome, p in FILE.items():
        vault = righe(p.read_text(encoding="utf-8")) if p.exists() else []
        online = righe(scarica(url, token, nome))
        tutte, n = unisci(vault, online)
        print(f"{nome}: vault {len(vault)}, online {len(online)}, nuove {n}")
        if n and not prova:
            with p.open("w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=CAMPI, lineterminator="\n")
                w.writeheader()
                w.writerows(tutte)
    subprocess.run([sys.executable, str(QUI / "allinea-contattati.py")] + (["--prova"] if prova else []), check=True)


if __name__ == "__main__":
    autotest() if "--autotest" in sys.argv else main()
