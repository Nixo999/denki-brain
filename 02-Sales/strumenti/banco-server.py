#!/usr/bin/env python3
"""Server del banco DM. Al posto di `python3 -m http.server`.

Serve `02-Sales/` come prima, e in piu` accetta `POST /segna`: per ogni DM che
Patrick segna come mandato scrive una riga in `liste/contattati.csv` (o in
`liste/gia-col-sito.csv` quando scarta un profilo che il sito ce l'ha gia`),
poi committa e pusha il vault due minuti dopo l'ultimo gesto. Cosi` l'elenco
dei contattati vive nel brain e non solo nel localStorage del suo browser.

Niente librerie: parte su qualunque Mac o PC con python3.
"""
import csv, json, subprocess, sys, threading, signal
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

SALES = Path(__file__).resolve().parent.parent
VAULT = SALES.parent
FILE = {"contattati": SALES / "liste" / "contattati.csv",
        "gia-col-sito": SALES / "liste" / "gia-col-sito.csv"}
CAMPI = ["Data", "Da", "Account IG", "Nome", "Comune", "Segmento", "Tipo", "Lista"]
ATTESA_COMMIT = 120          # secondi dopo l'ultimo gesto

lock = threading.Lock()
timer = None
toccati = set()


def leggi(p):
    if not p.exists():
        return []
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def salva(p, righe):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPI, lineterminator="\n")
        w.writeheader()
        w.writerows(righe)


def segna(op):
    p = FILE[op["file"]]
    riga = {k: str(op.get("riga", {}).get(k, "")).strip() for k in CAMPI}
    chiave = lambda r: (r["Data"], r["Da"], r["Account IG"].lower())
    with lock:
        righe = leggi(p)
        righe = [r for r in righe if chiave(r) != chiave(riga)]   # niente doppioni, e "togli" e` solo questo
        if op.get("azione", "aggiungi") == "aggiungi":
            righe.append(riga)
        righe.sort(key=lambda r: (r["Data"], r["Da"], r["Account IG"].lower()))
        salva(p, righe)
        toccati.add(p)
    return len(righe)


def commit():
    global timer
    with lock:
        timer = None
        file = sorted(str(p.relative_to(VAULT)) for p in toccati)
        toccati.clear()
    if not file:
        return
    git = lambda *a: subprocess.run(["git", "-C", str(VAULT), *a], capture_output=True, text=True)
    git("add", "--", *file)
    if git("diff", "--cached", "--quiet").returncode == 0:
        return
    n = sum(len(leggi(p)) for p in FILE.values())
    git("commit", "-qm", f"Banco DM: {n} righe fra contattati e gia' col sito\n\nScritte dal server del banco, non a mano.")
    # --autostash: sul Mac di Patrick il vault ha spesso .obsidian modificato e
    # senza questo il pull si rifiuta e il push non parte (visto l'8 settembre)
    for passo in (("pull", "--rebase", "--autostash", "-q"), ("push", "-q")):
        r = git(*passo)
        if r.returncode:
            print("git", passo[0], "fallito:", r.stderr.strip(), file=sys.stderr)
            return
    print("vault aggiornato:", ", ".join(file))


def programma_commit():
    global timer
    with lock:
        if timer:
            timer.cancel()
        timer = threading.Timer(ATTESA_COMMIT, commit)
        timer.daemon = True
        timer.start()


class Banco(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(SALES), **k)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_POST(self):
        if self.path != "/segna":
            return self.send_error(404)
        try:
            op = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
            if op["file"] not in FILE:
                raise ValueError("file sconosciuto")
            n = segna(op)
        except Exception as e:
            return self.send_error(400, str(e))
        programma_commit()
        corpo = json.dumps({"righe": n}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def log_message(self, *a):
        pass


def chiudi(*_):
    commit()          # quello che non e` ancora partito parte adesso
    sys.exit(0)


if __name__ == "__main__":
    porta = int(sys.argv[1]) if len(sys.argv) > 1 else 8770
    for s in (signal.SIGINT, signal.SIGTERM) + ((signal.SIGHUP,) if hasattr(signal, "SIGHUP") else ()):
        signal.signal(s, chiudi)
    print(f"Banco DM su http://localhost:{porta}/strumenti/banco-dm.html")
    ThreadingHTTPServer(("127.0.0.1", porta), Banco).serve_forever()
