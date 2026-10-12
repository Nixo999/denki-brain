#!/usr/bin/env bash
# Hook SessionStart e SubagentStart — mette in contesto la guida all'italiano
# chiaro, a Trevis e a ogni operatore, prima che scrivano qualcosa.
# Nicola, 12/10/2026: «prima di iniziare a scrivere o comunicarci qualcosa
# legga degli esempi». La guida sta in 03-Storage/azienda/italiano-chiaro.md.
#
# Sta a livello di account e trova il vault da solo. Se manca qualcosa tace.

set -u
V=$("$(dirname "$0")/trova-vault.sh" 2>/dev/null) || exit 0
G="$V/03-Storage/azienda/italiano-chiaro.md"
[ -f "$G" ] || exit 0
command -v python3 >/dev/null 2>&1 || exit 0

python3 -c '
import json, sys
try:
    evento = json.load(sys.stdin).get("hook_event_name") or "SessionStart"
except Exception:
    evento = "SessionStart"
testo = open(sys.argv[1], encoding="utf-8").read()
if testo.startswith("---"):
    testo = testo.split("---", 2)[2]
print(json.dumps({"hookSpecificOutput": {"hookEventName": evento,
                  "additionalContext": testo.strip()}}, ensure_ascii=False))
' "$G"
exit 0
