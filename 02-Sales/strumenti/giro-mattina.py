#!/usr/bin/env python3
"""Chi costruisce la lista del giorno: il Mac di Nicola alle 8, quello di Patrick
solo se il primo non è partito. Lo lancia il task pianificato dell'app Claude.

    python3 02-Sales/strumenti/giro-mattina.py --ruolo primo     # Mac di Nicola, 08:00
    python3 02-Sales/strumenti/giro-mattina.py --ruolo riserva   # Mac di Patrick, 08:30
    python3 02-Sales/strumenti/giro-mattina.py --fine            # a giro finito
    python3 02-Sales/strumenti/giro-mattina.py --installato      # c'è il task su questa macchina?
    python3 02-Sales/strumenti/giro-mattina.py --autotest

Nicola, 11/10/2026 (metodo-liste.md): il suo Mac manda prima una conferma nel
vault che dice che parte; quello di Patrick, dopo una certa ora, la cerca e
parte lui solo se non c'è. La conferma è una riga in liste/giri-mattina.csv,
committata e pushata prima di cominciare. Se due Mac pushano insieme, il
secondo push viene rifiutato: quello toglie la sua riga, riprende il vault e
trova la riga dell'altro.

Esce 0 se tocca a questa macchina, 1 se no (e stampa perché).
"""
import csv, datetime, socket, subprocess, sys
from pathlib import Path

QUI = Path(__file__).resolve().parent
VAULT = QUI.parent.parent
FILE = QUI.parent / "liste" / "giri-mattina.csv"
CAMPI = ["Data", "Ora", "Macchina", "Ruolo", "Stato"]
TASK = Path.home() / ".claude" / "scheduled-tasks" / "banco-mattina" / "SKILL.md"


def git(*a):
    return subprocess.run(["git", "-C", str(VAULT), *a], capture_output=True, text=True)


def macchina():
    r = subprocess.run(["scutil", "--get", "ComputerName"], capture_output=True, text=True)
    return (r.stdout.strip() if r.returncode == 0 else "") or socket.gethostname()


def righe():
    return list(csv.DictReader(FILE.open(encoding="utf-8"))) if FILE.exists() else []


def chi_ce(tutte, oggi, liste_di_oggi):
    """Perché questa macchina NON deve partire, o "" se tocca a lei."""
    for r in tutte:
        if r["Data"] == oggi and r["Stato"] == "partito":
            return f"il giro di oggi è già partito da {r['Macchina']} alle {r['Ora']}"
    if liste_di_oggi:
        return "le liste di oggi ci sono già: " + ", ".join(liste_di_oggi)
    return ""


def scrivi(riga, messaggio):
    nuovo = not FILE.exists()
    with FILE.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPI, lineterminator="\n")
        if nuovo:
            w.writeheader()
        w.writerow(riga)
    rel = str(FILE.relative_to(VAULT))
    git("add", rel)
    git("commit", "-qm", messaggio, "--", rel)
    return git("push", "-q").returncode == 0, rel


def prenota(ruolo):
    oggi = datetime.date.today().isoformat()
    for tentativo in range(2):
        git("pull", "--rebase", "--autostash", "-q")
        liste = sorted(p.name for p in (QUI.parent / "liste").glob(oggi + "-*.csv"))
        perche = chi_ce(righe(), oggi, liste)
        if perche:
            print(f"Non parto: {perche}.")
            return 1
        ora = datetime.datetime.now().strftime("%H:%M")
        ok, rel = scrivi({"Data": oggi, "Ora": ora, "Macchina": macchina(), "Ruolo": ruolo, "Stato": "partito"},
                         f"Giro del mattino: parte da {macchina()} ({ruolo}), {oggi} {ora}")
        if ok:
            print(f"Parto io: conferma nel vault, {macchina()} ({ruolo}) alle {ora}.")
            return 0
        # push rifiutato: qualcuno ha pushato nel frattempo. Si toglie solo la
        # propria riga (il resto del lavoro locale non si tocca) e si riguarda.
        git("reset", "--soft", "HEAD~1")
        git("restore", "--staged", "--worktree", "--", rel)
    print("Non parto: il push della conferma non passa, il vault non è raggiungibile.")
    return 1


def fine():
    oggi = datetime.date.today().isoformat()
    git("pull", "--rebase", "--autostash", "-q")
    ok, _ = scrivi({"Data": oggi, "Ora": datetime.datetime.now().strftime("%H:%M"), "Macchina": macchina(),
                    "Ruolo": "", "Stato": "finito"}, f"Giro del mattino: finito su {macchina()}, {oggi}")
    print("Fine giro scritta nel vault." if ok else "Fine giro scritta, push non passato.")
    return 0


def autotest():
    r = [{"Data": "2026-10-12", "Ora": "08:03", "Macchina": "Mac di Nicola", "Ruolo": "primo", "Stato": "partito"}]
    assert chi_ce([], "2026-10-12", []) == ""
    assert "Mac di Nicola" in chi_ce(r, "2026-10-12", [])
    assert chi_ce(r, "2026-10-13", []) == ""                       # ieri non conta
    assert "ci sono già" in chi_ce([], "2026-10-12", ["2026-10-12-instagram-siti-mi.csv"])
    print("autotest ok")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--autotest" in a:
        sys.exit(autotest())
    if "--installato" in a:
        print("installato" if TASK.exists() else "manca")
        sys.exit(0 if TASK.exists() else 1)
    if "--fine" in a:
        sys.exit(fine())
    if "--ruolo" in a and a.index("--ruolo") + 1 < len(a) and a[a.index("--ruolo") + 1] in ("primo", "riserva"):
        sys.exit(prenota(a[a.index("--ruolo") + 1]))
    sys.exit(__doc__)
