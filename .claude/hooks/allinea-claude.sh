#!/usr/bin/env bash
# Hook SessionStart del vault denki-brain.
#
# ~/.claude/ (protocollo, agente operatore, comandi, skill nostre) e' locale
# alla macchina e sta fuori da git: un `git pull` porta le copie canoniche nel
# vault ma NON le installa. Finche' era un passaggio a mano restava indietro —
# il 10/09/2026 cinque comandi erano vecchi di mezza giornata sul Mac di Nicola.
#
# Questo hook non scrive niente: dice solo se e' indietro, a inizio sessione.
# Se python3 non c'e' (PC Windows), tace: una rete di sicurezza che esplode e'
# peggio di nessuna rete. Stessa lezione di jq in ricorda-push.sh.

set -u

cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
command -v python3 >/dev/null 2>&1 || exit 0
[ -f 01-Coding/strumenti/installa-macchina.py ] || exit 0

if ! uscita=$(python3 01-Coding/strumenti/installa-macchina.py --check 2>&1); then
  printf '%s\n\n' "$uscita"
  printf '%s\n' "Su questa macchina ~/.claude/ e' indietro rispetto al vault. Prima di lavorare, lancia: python3 01-Coding/strumenti/installa-macchina.py"
fi

exit 0
