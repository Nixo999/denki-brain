#!/usr/bin/env python3
"""Hook PreToolUse: approva da solo gli strumenti di una sessione avviata da un
task pianificato dell'app, cioe' il giro del mattino del banco DM.

Perche' esiste (13/10/2026): la sessione del task parte in modalita' permessi
`default`, non `auto`, e il task non ha un campo per cambiarla. Il 12/10 e il
13/10 il giro si e' fermato alle 8 sul primo comando, aspettando una conferma
che nessuno poteva dare. Le regole di permissions.allow non bastano: il modello
cambia la coda dei comandi a ogni giro e gli operatori lanciano script nella
scratchpad. Il dettaglio sta in trappole.md, sezione «Liste e banco DM».

Riconosce la sessione dal tag `<scheduled-task name="...">` nel primo messaggio
della trascrizione; per gli operatori, che stanno in <sessione>/subagents/,
risale a quella madre. Fuori da una sessione di task non decide niente e
valgono i permessi normali. Nel giro resta vietato quello che e' vietato
ovunque: push forzato, reset --hard, sudo, rm -rf fuori dalla scratchpad. Le
regole di deny di settings.json vincono comunque sull'hook (documentazione
degli hook, 13/10/2026).

Stdlib sola, niente jq: sul PC Windows c'e' solo python3.

    python3 permessi-giro.py --autotest
"""
import json
import re
import sys
import tempfile
from pathlib import Path

TAG = re.compile(r'<scheduled-task name="([^"]+)"')
TASK_NOSTRI = {"banco-mattina"}   # ponytail: lista fissa, si allunga quando nasce un altro task
VIETATO = re.compile(r"git\s+push\b[^|;&]*(--force|\s-f\b)|git\s+reset\s+--hard|\bsudo\b")
RM = re.compile(r"\brm\s+((?:-\S+\s+)+)(\S+)")   # (opzioni, bersaglio): un rm ricorsivo fuori dalla scratchpad non passa
MCP_AMMESSI = ("mcp__Claude_Browser__", "mcp__remote-devices__Claude_Browser__")
SCRATCH = ("/tmp/", "/private/tmp/", "/var/folders/", tempfile.gettempdir().rstrip("/") + "/")


def trascrizioni(e):
    """Dove puo' stare il tag: la trascrizione data, quella madre di un
    operatore, quella ricavata da sessione e cartella."""
    tp = e.get("transcript_path") or ""
    out = [tp]
    if "/subagents/" in tp:
        out.append(tp.split("/subagents/")[0] + ".jsonl")
    sid, cwd = e.get("session_id"), e.get("cwd")
    if sid and cwd:
        out.append(str(Path.home() / ".claude" / "projects" / re.sub(r"[^A-Za-z0-9]", "-", cwd) / f"{sid}.jsonl"))
    return [p for p in out if p]


def nome_task(e):
    """Il nome del task nel primo messaggio scritto dell'utente, o None.
    Solo il primo: un risultato di strumento che cita il tag non conta."""
    for p in trascrizioni(e):
        try:
            with open(p, encoding="utf-8") as f:
                for _ in range(80):
                    riga = f.readline()
                    if not riga:
                        break
                    if '"type":"user"' not in riga.replace(" ", ""):
                        continue
                    try:
                        c = json.loads(riga).get("message", {}).get("content")
                    except ValueError:
                        continue
                    if isinstance(c, list):
                        c = " ".join(x.get("text", "") for x in c if isinstance(x, dict) and x.get("type") == "text")
                    if not isinstance(c, str) or not c.strip():
                        continue
                    m = TAG.search(c)
                    if m:
                        return m.group(1)
                    break   # primo messaggio senza tag: non e' qui, si prova la trascrizione madre
        except OSError:
            continue
    return None


def decidi(e):
    nome = nome_task(e)
    if nome not in TASK_NOSTRI:
        return None
    strumento, ing = e.get("tool_name", ""), e.get("tool_input") or {}
    if strumento == "Bash":
        cmd = ing.get("command", "")
        if VIETATO.search(cmd):
            return None
        for opzioni, bersaglio in RM.findall(cmd):
            bersaglio = bersaglio.strip("'\"")
            if "r" in opzioni.lower() and bersaglio.startswith(("/", "~")) and not bersaglio.startswith(SCRATCH):
                return None
    if strumento in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        f = ing.get("file_path") or ing.get("notebook_path") or ""
        dentro = (e.get("cwd") or "\0").rstrip("/") + "/"
        if not (f.startswith(dentro) or f.startswith(SCRATCH)):
            return None
    if strumento.startswith("mcp__") and not strumento.startswith(MCP_AMMESSI):
        return None
    return {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "allow",
                                   "permissionDecisionReason": f"sessione del task {nome}: approvato da permessi-giro"}}


def autotest():
    d = Path(tempfile.mkdtemp())
    sid, cwd = "0000-sessione", str(d / "vault")
    madre = d / "proj" / f"{sid}.jsonl"
    madre.parent.mkdir()
    riga_task = json.dumps({"type": "user", "message": {"role": "user", "content":
                            '<scheduled-task name="banco-mattina" file="x">\nGiro del mattino.'}})
    madre.write_text(json.dumps({"type": "queue-operation"}) + "\n" + riga_task + "\n")
    figlia = d / "proj" / sid / "subagents" / "agent-1.jsonl"
    figlia.parent.mkdir(parents=True)
    figlia.write_text(json.dumps({"type": "user", "message": {"role": "user", "content": "Cella siti VB sartorie"}}) + "\n")
    normale = d / "proj" / "altra.jsonl"
    # una sessione normale che LEGGE una trascrizione di task: il tag sta in un risultato, non nel primo messaggio
    normale.write_text(json.dumps({"type": "user", "message": {"role": "user", "content": "ciao"}}) + "\n"
                       + json.dumps({"type": "user", "message": {"role": "user", "content": [{"type": "tool_result", "content": riga_task}]}}) + "\n")
    base = {"session_id": sid, "cwd": cwd, "transcript_path": str(madre)}
    ok = lambda r: r and r["hookSpecificOutput"]["permissionDecision"] == "allow"
    assert ok(decidi({**base, "tool_name": "Bash", "tool_input": {"command": 'python3 02-Sales/strumenti/giro-mattina.py --ruolo primo; echo "EXIT=$?"'}}))
    assert ok(decidi({**base, "transcript_path": str(figlia), "tool_name": "Bash", "tool_input": {"command": "curl -s https://x"}}))
    assert ok(decidi({**base, "tool_name": "Write", "tool_input": {"file_path": cwd + "/02-Sales/liste/a.csv"}}))
    assert ok(decidi({**base, "tool_name": "Write", "tool_input": {"file_path": "/private/tmp/claude-501/x/s.py"}}))
    assert ok(decidi({**base, "tool_name": "Agent", "tool_input": {"prompt": "x"}}))
    assert ok(decidi({**base, "tool_name": "mcp__Claude_Browser__navigate", "tool_input": {"url": "https://instagram.com"}}))
    assert ok(decidi({**base, "tool_name": "Bash", "tool_input": {"command": "git push -q && rm -rf /private/tmp/claude-501/x"}}))
    assert decidi({**base, "tool_name": "Bash", "tool_input": {"command": "git push --force origin main"}}) is None
    assert decidi({**base, "tool_name": "Bash", "tool_input": {"command": "git reset --hard HEAD~1"}}) is None
    assert decidi({**base, "tool_name": "Bash", "tool_input": {"command": "rm -rf ~/lavoro"}}) is None
    assert decidi({**base, "tool_name": "Write", "tool_input": {"file_path": str(Path.home() / ".claude/settings.json")}}) is None
    assert decidi({**base, "tool_name": "mcp__scheduled-tasks__create_scheduled_task", "tool_input": {}}) is None
    assert decidi({**base, "transcript_path": str(normale), "session_id": "altra", "tool_name": "Bash", "tool_input": {"command": "ls"}}) is None
    assert decidi({**base, "transcript_path": "/nessun/file", "session_id": "x", "cwd": "/y", "tool_name": "Bash", "tool_input": {"command": "ls"}}) is None
    print("autotest ok")


if __name__ == "__main__":
    if "--autotest" in sys.argv:
        autotest()
        sys.exit(0)
    try:
        r = decidi(json.load(sys.stdin))
        if r:
            print(json.dumps(r))
    except Exception:
        pass   # un hook che muore non deve bloccare niente: senza risposta valgono i permessi normali
    sys.exit(0)
