#!/usr/bin/env bash
# Hook SessionStart — dice se ~/.claude/ e' indietro rispetto al vault.
#
# Sta a livello di account e trova il vault da solo: vale anche quando la
# sessione parte in un repo di un sito o sul Desktop. Non scrive niente.
# Se python3 non c'e' tace: una rete che esplode e' peggio di nessuna rete.

set -u
V=$("$(dirname "$0")/trova-vault.sh" 2>/dev/null) || exit 0
command -v python3 >/dev/null 2>&1 || exit 0
[ -f "$V/01-Coding/strumenti/installa-macchina.py" ] || exit 0

if ! uscita=$(cd "$V" && python3 01-Coding/strumenti/installa-macchina.py --check 2>&1); then
  printf '%s\n\n' "$uscita"
  printf '%s\n' "Su questa macchina ~/.claude/ e' indietro rispetto al vault. Prima di lavorare: python3 $V/01-Coding/strumenti/installa-macchina.py"
fi
exit 0
