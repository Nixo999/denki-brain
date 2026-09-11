#!/usr/bin/env bash
# Hook Stop — chiude la sessione pushando il vault, da qualunque cartella.
#
# Regola del 28/08/2026: ogni modifica al vault si committa e si pusha subito.
# Fino all'11/09 questo hook ricordava di farlo, e funzionava solo se
# dall'altra parte c'era qualcuno che sa cos'e' un commit. Patrick non lo sa.
#
# Sta a livello di account, non di progetto: se fosse legato alla cartella,
# Patrick che apre Claude sul Desktop e lancia /patrick non avrebbe nessun
# push automatico. Tocca **solo** il vault, mai il repo in cui stai lavorando.
#
# NIENTE jq: sul PC Windows non c'e', e un hook che muore non e' una rete.

set -u
V=$("$(dirname "$0")/trova-vault.sh" 2>/dev/null) || exit 0
cd "$V" 2>/dev/null || exit 0
git rev-parse --git-dir >/dev/null 2>&1 || exit 0

g=$(git rev-parse --git-dir)
[ -d "$g/rebase-merge" ] || [ -d "$g/rebase-apply" ] || [ -f "$g/MERGE_HEAD" ] && exit 0

entrata=$(cat 2>/dev/null || true)
sid=$(printf '%s' "$entrata" | sed -n 's/.*"session_id"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)
[ -z "$sid" ] && sid="nosid"
marcatore="${TMPDIR:-/tmp}/denki-brain-push-${sid}"

sporco=$(git status --porcelain 2>/dev/null)
avanti=$(git rev-list --count '@{u}..HEAD' 2>/dev/null || echo 0)
[ -z "$sporco" ] && [ "$avanti" = "0" ] && exit 0
[ -f "$marcatore" ] && exit 0

dillo() { : > "$marcatore"; printf '{"decision":"block","reason":"%s"}\n' "$1"; exit 0; }

git pull --rebase --autostash -q >/dev/null 2>&1 || {
  git rebase --abort >/dev/null 2>&1
  dillo "Il pull --rebase del vault non e passato e ho annullato il rebase. Guarda git status nel vault, risolvi a mano e pusha. Non ho committato niente."
}

if [ -n "$sporco" ]; then
  git add -A >/dev/null 2>&1
  cartelle=$(git diff --cached --name-only | cut -d/ -f1 | sort -u | tr '\n' ' ')
  n=$(git diff --cached --name-only | wc -l | tr -d ' ')
  git commit -q -m "Chiusura automatica: $n file in $cartelle" \
    -m "Committato dall'hook di fine sessione, non da una persona: il perche' di
ogni modifica sta nei commit scritti durante la sessione. Se questo commit e'
l'unico, quel lavoro e' rimasto senza spiegazione." >/dev/null 2>&1 || true
fi

git push -q >/dev/null 2>&1 || dillo "Il push del vault non e passato. Non ho forzato. Fai git pull --rebase nel vault, guarda il risultato e riprova."
exit 0
