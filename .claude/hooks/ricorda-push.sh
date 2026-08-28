#!/usr/bin/env bash
# Hook Stop del vault denki-brain.
#
# Regola del 28/08/2026: ogni modifica al vault, anche minima, va committata e
# pushata, da qualsiasi macchina, salvo indicazione contraria dell'utente.
# Questo hook e' la rete di sicurezza: a fine turno controlla se e' rimasto
# lavoro non pushato e, se si', lo dice a Claude una volta sola per sessione.
#
# Una volta sola: se l'utente ha chiesto di NON pushare, il secondo Stop passa.

set -u

cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
git rev-parse --git-dir >/dev/null 2>&1 || exit 0

# L'input dell'hook arriva su stdin come JSON: serve solo l'id di sessione.
sid=$(jq -r '.session_id // "nosid"' 2>/dev/null) || sid="nosid"
marcatore="${TMPDIR:-/tmp}/denki-brain-push-${sid}"
[ -f "$marcatore" ] && exit 0

sporco=$(git status --porcelain 2>/dev/null)
avanti=$(git rev-list --count '@{u}..HEAD' 2>/dev/null || echo 0)

if [ -n "$sporco" ] || [ "$avanti" != "0" ]; then
  : > "$marcatore"
  motivo=$(cat <<'MSG'
Nel vault e' rimasto lavoro non pushato: modifiche non committate, oppure commit locali non ancora inviati a origin.

La regola del 28/08/2026: ogni modifica al vault, anche minima, si committa e si pusha subito, da qualsiasi macchina. Fai `git pull --rebase`, poi commit con un messaggio nello stile del vault e `git push`.

Se invece l'utente ha chiesto esplicitamente di non pushare, dillo e fermati pure: questo promemoria non si ripete nella stessa sessione.
MSG
)
  jq -n --arg r "$motivo" '{decision: "block", reason: $r}'
fi

exit 0
