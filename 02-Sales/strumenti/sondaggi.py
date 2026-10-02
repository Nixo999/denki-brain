#!/usr/bin/env python3
"""I sondaggi delle storie li pubblica Patrick a mano: questo dice quando, cosa, e gli lascia la foto.

    python3 02-Sales/strumenti/sondaggi.py

L'API di Instagram non mette gli sticker (sondaggi, link). Le storie escono da sole
dal repo denkicode-social, ma il frame col sondaggio lo appoggia Patrick dall'app,
sopra l'immagine base. Nicola, 3/10/2026: «ricorda a patrick ogni volta che fa
/patrick di creare dei sondaggi, come farlo, a che ora e quando, ricordaglielo fin
dalle 5 ore precedenti e dagli una foto base del sondaggio».

Legge coda.json dal repo pubblico: le voci con il campo `sondaggio`
({"domanda", "opzioni", "file"}) sono quelle da fare a mano. Finestra: da 5 ore
prima dell'orario fino a sera (una storia dura 24 ore). L'immagine base la
scarica sul Desktop, una volta sola. Solo libreria standard.
"""
import json
import pathlib
import sys
import urllib.request
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

REPO = "https://raw.githubusercontent.com/Nixo999/denkicode-social/main/"
ROMA = ZoneInfo("Europe/Rome")
PRIMA, DOPO = timedelta(hours=5), timedelta(hours=16)
GIORNI = ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]

COME = """Come si fa, dall'app Instagram con @denkicode (tre minuti):
  1. passa l'immagine base sul telefono (AirDrop dal Desktop)
  2. la tua storia → scegli l'immagine → sticker → Sondaggio
  3. scrivi la domanda e le due risposte qui sopra, appoggia lo sticker nella fascia vuota al centro
  4. pubblica. Le altre storie della sequenza escono da sole dall'API."""


def main():
    try:
        with urllib.request.urlopen(REPO + "coda.json", timeout=8) as r:
            coda = json.load(r)
    except Exception as e:
        print(f"sondaggi: coda non raggiungibile ({e.__class__.__name__}), si riprova alla prossima sessione")
        return 0
    ora = datetime.now(ROMA)
    oggi, prossimi = [], []
    for it in coda:
        s = it.get("sondaggio")
        if not s:
            continue
        q = datetime.fromisoformat(it["quando"]).replace(tzinfo=ROMA)
        if q - PRIMA <= ora <= q + DOPO:
            oggi.append((q, it, s))
        elif q > ora:
            prossimi.append((q, it, s))
    if not oggi:
        if prossimi:
            q, it, s = min(prossimi)
            print(f"Prossimo sondaggio da fare a mano: {GIORNI[q.weekday()]} {q:%-d/%-m alle %H:%M} · «{s['domanda']}»")
        else:
            print("Nessun sondaggio in coda.")
        return 0
    for q, it, s in sorted(oggi):
        stato = "ADESSO" if ora >= q else f"fra {int((q - ora).total_seconds() // 3600)} ore"
        dest = pathlib.Path.home() / "Desktop" / f"sondaggio-{q:%Y-%m-%d}.jpg"
        if not dest.exists():
            try:
                urllib.request.urlretrieve(REPO + "media/" + s["file"], dest)
            except Exception as e:
                dest = f"(immagine non scaricata: {e.__class__.__name__}; sta in {REPO}media/{s['file']})"
        print(f"SONDAGGIO DA PUBBLICARE A MANO · {GIORNI[q.weekday()]} {q:%-d/%-m alle %H:%M} · {stato}")
        print(f"  Domanda: {s['domanda']}")
        print("  Risposte: " + " / ".join(s["opzioni"]))
        print(f"  Immagine base: {dest}")
    print(COME)
    return 0


if __name__ == "__main__":
    sys.exit(main())
