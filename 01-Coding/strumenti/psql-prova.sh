#!/usr/bin/env bash
# psql-prova: psql che parla solo con il database di prova di OperO.
#
# Perche' esiste (20/10/2026): in modalita' auto il controllo dei permessi
# ferma `psql` sul database, perche' non sa distinguere la prova dallo sviluppo
# (operotest, che usa Seba) o dalla produzione. Una regola `Bash(psql:*)` le
# aprirebbe tutte. Questo comando si apre da solo, e in settings.json c'e'
# `Bash(psql-prova:*)`: passa senza chiedere, ma solo verso la prova.
#
# Legge PROVA_DB_URL da .env.prova.local (la cartella corrente, poi
# ~/lavoro/opero-prova-deploy) e si rifiuta se l'indirizzo non e' quello del
# progetto Supabase qjawewmmgxyrguxajvgf. Si rifiuta anche se gli argomenti
# provano a cambiare host, database o utente.
#
#   psql-prova -c "select 1"
#   psql-prova -v ON_ERROR_STOP=1 -f supabase/migrations/<file>.sql
#
# Installato con: ln -sf <vault>/01-Coding/strumenti/psql-prova.sh ~/.local/bin/psql-prova
set -euo pipefail

PROGETTO_PROVA="qjawewmmgxyrguxajvgf"

url=""
for f in "$PWD/.env.prova.local" "$HOME/lavoro/opero-prova-deploy/.env.prova.local"; do
  if [ -f "$f" ]; then
    url="$(grep -E '^PROVA_DB_URL=' "$f" | head -1 | cut -d= -f2-)"
    [ -n "$url" ] && break
  fi
done

if [ -z "$url" ]; then
  echo "psql-prova: PROVA_DB_URL non trovato in .env.prova.local" >&2
  exit 2
fi
case "$url" in
  *"$PROGETTO_PROVA"*) ;;
  *) echo "psql-prova: PROVA_DB_URL non e' il progetto di prova $PROGETTO_PROVA, mi fermo" >&2; exit 2 ;;
esac

for a in "$@"; do
  case "$a" in
    -h|-h*|--host|--host=*|-d|-d*|--dbname|--dbname=*|-p|-p*|--port|--port=*|-U|-U*|--username|--username=*|*://*|*host=*)
      echo "psql-prova: l'argomento '$a' cambierebbe database, non lo passo" >&2
      exit 2 ;;
  esac
done

exec psql "$url" "$@"
