#!/usr/bin/env bash
# Dice dove sta il vault, da qualunque cartella parta la sessione.
# Lo usano gli hook, che a livello di account non hanno CLAUDE_PROJECT_DIR
# puntato al vault: Patrick apre Claude dove capita.
for p in "${DENKI_VAULT:-}" "${CLAUDE_PROJECT_DIR:-}" "$PWD" \
         "$HOME/lavoro/denki-brain" "$HOME/Desktop/denki-brain" \
         "$HOME/Desktop/denkicode volt" "$HOME/Documents/denkicode volt" \
         "$HOME/denkicode volt" "$HOME/denki-brain"; do
  [ -n "$p" ] && [ -f "$p/CLAUDE.md" ] && [ -d "$p/01-Coding" ] && { printf '%s' "$p"; exit 0; }
done
exit 1
