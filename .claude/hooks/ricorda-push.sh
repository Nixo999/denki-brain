#!/usr/bin/env bash
# Hook Stop del vault denki-brain.
#
# Regola del 28/08/2026: ogni modifica al vault, anche minima, va committata e
# pushata, da qualsiasi macchina, salvo indicazione contraria dell'utente.
# Questo hook e' la rete di sicurezza: a fine turno controlla se e' rimasto
# lavoro non pushato e, se si', lo dice a Claude una volta sola per sessione.
#
# Una volta sola: se l'utente ha chiesto di NON pushare, il secondo Stop passa.
#
# NIENTE jq. La prima versione lo usava, e sul PC Windows di Nicola jq non c'e':
# lo script moriva con "command not found" senza stampare niente, quindi la rete
# di sicurezza non c'era proprio sulla macchina dove si lavora di piu'.
# Verificato il 28/08/2026, vedi 05-Decisioni/2026-08-28-push-automatico.md.

set -u

cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
git rev-parse --git-dir >/dev/null 2>&1 || exit 0

# L'input dell'hook arriva su stdin come JSON: serve solo l'id di sessione.
# Estratto con sed perche' deve funzionare ovunque ci sia bash, jq o meno.
entrata=$(cat 2>/dev/null || true)
sid=$(printf '%s' "$entrata" | sed -n 's/.*"session_id"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)
[ -z "$sid" ] && sid="nosid"

marcatore="${TMPDIR:-/tmp}/denki-brain-push-${sid}"
[ -f "$marcatore" ] && exit 0

sporco=$(git status --porcelain 2>/dev/null)
avanti=$(git rev-list --count '@{u}..HEAD' 2>/dev/null || echo 0)

if [ -n "$sporco" ] || [ "$avanti" != "0" ]; then
  : > "$marcatore"
  # JSON scritto a mano: il messaggio non contiene virgolette ne' backslash,
  # quindi non serve nessuna escape oltre agli a-capo gia' resi come \n.
  printf '%s' '{"decision":"block","reason":"Nel vault e rimasto lavoro non pushato: modifiche non committate, oppure commit locali non ancora inviati a origin.\n\nLa regola del 28/08/2026: ogni modifica al vault, anche minima, si committa e si pusha subito, da qualsiasi macchina. Fai git pull --rebase, poi commit con un messaggio nello stile del vault e git push.\n\nSe invece lutente ha chiesto esplicitamente di non pushare, dillo e fermati pure: questo promemoria non si ripete nella stessa sessione."}'
  printf '\n'
fi

exit 0
