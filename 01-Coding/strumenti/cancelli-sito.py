#!/usr/bin/env python3
"""I cancelli di un sito vetrina: un comando solo, prima di mostrarlo a Nicola.

    python3 01-Coding/strumenti/cancelli-sito.py ~/lavoro/<nome>-site
    python3 01-Coding/strumenti/cancelli-sito.py ~/lavoro/<nome>-site --url https://<nome>.netlify.app
    python3 01-Coding/strumenti/cancelli-sito.py ~/lavoro/<nome>-site --consegnato

--consegnato vale per un sito gia' passato al cliente, che non ha piu' i tre sbarramenti di proposito.

Lancia in fila:
1. controlla-sito.py   il livello minimo misurato su NG Barber e Fiftynine, sbarramenti e firma;
2. controlla-slop.py   i segni che fanno sembrare il sito fatto con l'AI;
3. controlla-testo.py  didascalie, micro-titoli, frasi lunghe, leggibilita';
4. cancelli-telefono.mjs  a 375x812 con CPU rallentata 4 volte: lag e le bocciature ricorrenti di
   01-Coding/stack/direttive-siti.md che si vedono sulla pagina.

Senza --url serve la cartella (o la sua dist/, se e' un sito Astro) su 127.0.0.1 per il tempo della misura.
Esce 1 se un cancello blocca. Gli avvisi non bloccano: si guardano.

CONTRADDIZIONE APERTA (31/10/2026): controlla-sito.py chiede almeno 3 <svg> inline o un racconto
tipografico («grafica inventata»), mentre Nicola ha scritto piu' volte di non disegnare niente noi
(direttive-siti, 12/10 e 23/10). Finche' Nicola non decide, quei due controlli si stampano come
CONTRADDIZIONE e non bloccano. Nato il 31/10/2026 dalla pipeline dei siti.
"""
import functools
import http.server
import json
import socket
import subprocess
import sys
import threading
from pathlib import Path

QUI = Path(__file__).resolve().parent
# i controlli di controlla-sito.py che spingono a disegnare: vedi CONTRADDIZIONE APERTA
SPINGONO_A_DISEGNARE = ("grafica inventata", "foto, oppure grafica che le sostituisca")
SBARRAMENTI = ("sbarramento meta", "sbarramento header", "sbarramento robots")


def servi(radice):
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    porta = s.getsockname()[1]
    s.close()
    class Muto(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    gestore = functools.partial(Muto, directory=str(radice))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", porta), gestore)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{porta}/"


def lancia(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).rstrip()


def controlla_sito(cartella, consegnato=False):
    """controlla-sito.py, con i due controlli che spingono a disegnare separati dagli altri."""
    sys.path.insert(0, str(QUI))
    import importlib.util
    spec = importlib.util.spec_from_file_location("controlla_sito", QUI / "controlla-sito.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    r = mod.controlla(cartella)
    if r is None:
        return True, ["  (nessun index.html: controlla-sito non si applica)"]
    righe, ok = [], True
    for nome, passa, msg in r["esiti"]:
        if passa or (consegnato and nome in SBARRAMENTI):
            continue
        if nome in SPINGONO_A_DISEGNARE:
            righe.append(f"  CONTRADDIZIONE  {nome}: {msg}")
        else:
            ok = False
            righe.append(f"  BLOCCA  {nome}: {msg}")
    righe += [f"  avvisa  {a}" for a in r["avvisi"]]
    return ok, righe or ["  tutto a posto"]


def main(argv):
    if not argv or argv[0].startswith("-"):
        sys.exit(__doc__)
    cartella = Path(argv[0]).expanduser().resolve()
    url = argv[argv.index("--url") + 1] if "--url" in argv else None
    cpu = argv[argv.index("--cpu") + 1] if "--cpu" in argv else "4"
    radice = cartella / "dist" if (cartella / "dist" / "index.html").exists() else cartella
    file_da_leggere = cartella if (cartella / "index.html").exists() else radice

    esiti = []
    ok, righe = controlla_sito(file_da_leggere, "--consegnato" in argv)
    esiti.append(("livello minimo (controlla-sito)", ok, "\n".join(righe)))
    for nome, script in (("segni da AI (controlla-slop)", "controlla-slop.py"),
                         ("testo (controlla-testo)", "controlla-testo.py")):
        codice, out = lancia([sys.executable, str(QUI / script), str(file_da_leggere)])
        esiti.append((nome, codice == 0, out))

    srv = None
    if not url:
        srv, url = servi(radice)
    try:
        codice, out = lancia(["node", str(QUI / "cancelli-telefono.mjs"), url, "--cpu", cpu, "--json"])
    finally:
        if srv:
            srv.shutdown()
    try:
        t = json.loads(out.splitlines()[-1])
        righe = [f"  {'ok     ' if c['ok'] else 'BLOCCA ' if c['blocca'] else 'avvisa '} {c['id']}: {c['msg']}"
                 for c in t["controlli"]]
        esiti.append((f"telefono 375x812, CPU {cpu}x (cancelli-telefono)", codice == 0, "\n".join(righe)))
    except (ValueError, IndexError, KeyError):
        esiti.append(("telefono (cancelli-telefono)", False, "  la misura non e' partita:\n" + out))

    print(f"Cancelli di {cartella.name} · {url}\n")
    for nome, passa, out in esiti:
        print(f"{'PASSA' if passa else 'NON PASSA'} — {nome}")
        print(out)
        print()
    fermi = [n for n, p, _ in esiti if not p]
    print("ESITO: " + ("passa tutti i cancelli. Gli avvisi restano da guardare." if not fermi
                       else "fermo a " + ", ".join(fermi) + "."))
    sys.exit(1 if fermi else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
