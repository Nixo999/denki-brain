#!/usr/bin/env python3
"""Installa in ~/.claude/ i file che git non porta, dalle copie canoniche del vault.

    python3 01-Coding/strumenti/installa-macchina.py           # scrive
    python3 01-Coding/strumenti/installa-macchina.py --check   # dice e basta, esce 1 se serve

`~/.claude/` e' locale alla macchina e fuori da git: protocollo, agenti, comandi,
skill nostre e **hook** vivono li'. Le copie canoniche stanno nel vault e ci arrivano col
push, ma qualcuno deve portarle dentro. Finche' era un passaggio a mano restava
indietro, come la firma nel footer. Adesso e' un comando.

Non tocca niente di terze parti: plugin, skill di design e le altre voci di
settings.json restano come sono. Degli hook registra solo i nostri due, e li
riconosce dal nome dello script.

Gli hook stanno a livello di account e non di progetto dall'11/09/2026: legati
alla cartella del vault non sarebbero mai scattati per Patrick, che apre Claude
dove capita e poi lancia /patrick. Trovano il vault da soli e toccano solo lui.
"""
import filecmp, shutil, sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
CLAUDE = Path.home() / ".claude"
MARK = "<!-- INIZIO FILE LOCALE"

# copia canonica nel vault -> dove va sulla macchina
CANONICHE = {
    "03-Storage/sistemi/claude-md-globale.md": "CLAUDE.md",
    "03-Storage/sistemi/agente-operatore.md": "agents/operatore.md",
}
# cartelle del vault ricopiate pari pari
CARTELLE = ["commands", "skills", "hooks"]

# Gli hook stanno a livello di ACCOUNT, non di progetto: Patrick apre Claude
# dove capita, e un hook legato alla cartella del vault non scatterebbe mai.
# Trovano il vault da soli (trova-vault.sh) e toccano solo lui.
HOOK = {
    "SessionStart": ("allinea-claude.sh", 15, "Controllo che ~/.claude/ sia allineato al vault"),
    "Stop": ("pusha-da-solo.sh", 60, "Chiudo e pusho il vault"),
}
FIRMA = "denki-brain"      # marcatore: cosi' non si tocca quello che c'era gia'


def corpo(p):
    """Il file vero: quello che sta sotto il marcatore, senza l'involucro del vault."""
    t = p.read_text(encoding="utf-8")
    i = t.find(MARK)
    if i < 0:
        sys.exit(f"{p}: manca il marcatore «{MARK}...»")
    return t[t.index("\n", i) + 1:].lstrip("\n")


def scrivi(dest, testo, check, fatti):
    vecchio = dest.read_text(encoding="utf-8") if dest.exists() else None
    if vecchio == testo:
        return
    fatti.append(("aggiorna" if vecchio else "crea", dest))
    if not check:
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(testo, encoding="utf-8")


def registra_hook(check, fatti):
    """Aggiunge i nostri hook a ~/.claude/settings.json senza toccare gli altri."""
    import json
    s = CLAUDE / "settings.json"
    dati = json.loads(s.read_text(encoding="utf-8")) if s.exists() else {}
    hooks = dati.setdefault("hooks", {})
    cambiato = False
    for evento, (script, timeout, messaggio) in HOOK.items():
        comando = f'"$HOME/.claude/hooks/{script}"'
        voce = {"type": "command", "command": comando,
                "timeout": timeout, "statusMessage": messaggio}
        gruppi = hooks.setdefault(evento, [])
        # i nostri si riconoscono dal nome dello script: gli altri restano dove sono
        nostri = [g for g in gruppi
                  if any(FIRMA in h.get("command", "") or script in h.get("command", "")
                         for h in g.get("hooks", []))]
        if nostri and nostri[0]["hooks"] == [voce]:
            continue
        for g in nostri:
            gruppi.remove(g)
        gruppi.append({"hooks": [voce]})
        cambiato = True
        fatti.append(("registra hook", CLAUDE / f"settings.json ({evento})"))
    if cambiato and not check:
        s.write_text(json.dumps(dati, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main(check):
    fatti = []
    for sorgente, destinazione in CANONICHE.items():
        scrivi(CLAUDE / destinazione, corpo(VAULT / sorgente), check, fatti)

    for cartella in CARTELLE:
        radice = VAULT / ".claude" / cartella
        if not radice.is_dir():
            continue
        # gli hook sono script, non note: servono anche il bit di esecuzione
        modelli = ("*.sh",) if cartella == "hooks" else ("*.md",)
        for modello in modelli:
            for q in radice.rglob(modello):
                dest = CLAUDE / cartella / q.relative_to(radice)
                scrivi(dest, q.read_text(encoding="utf-8"), check, fatti)
                if modello == "*.sh" and dest.exists() and not check:
                    dest.chmod(0o755)

    registra_hook(check, fatti)

    for azione, dest in fatti:
        print(f"{azione}: ~/{dest.relative_to(Path.home())}")
    if not fatti:
        print("~/.claude/ e' gia' allineato al vault")
        return 0
    print(f"\n{len(fatti)} file {'da aggiornare' if check else 'scritti'}")
    return 1 if check else 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
