#!/bin/sh
# Banco DM — doppio click e si apre con la lista del giorno gia' dentro.
# Il file si puo' copiare sul Desktop: il vault se lo cerca da solo.
#
# Il server e' banco-server.py: serve i CSV (da file:// il browser lo vieta) e
# scrive in liste/contattati.csv ogni DM segnato, poi committa e pusha il vault.

PORTA=8770

for p in "$HOME/lavoro/denki-brain" "$HOME/Desktop/denkicode volt" "$HOME/Documents/denkicode volt" "$HOME/denkicode volt" "$HOME/Desktop/denki-brain"; do
  if [ -d "$p/02-Sales/strumenti" ]; then V="$p"; break; fi
done

if [ -z "$V" ]; then
  echo "Non trovo il vault (cerco «denkicode volt» sul Desktop o in Documenti)."
  echo "Premi invio per chiudere."
  read _
  exit 1
fi

cd "$V/02-Sales" || exit 1

# se e' gia' aperto da un'altra volta, non ne apro un secondo
if ! curl -s -o /dev/null "http://localhost:$PORTA/strumenti/banco-dm.html"; then
  python3 strumenti/banco-server.py $PORTA &
  SERVER=$!
  sleep 1
fi

open "http://localhost:$PORTA/strumenti/banco-dm.html"

echo "Banco DM aperto nel browser."
echo "Lascia stare questa finestra mentre mandi i messaggi: chiudendola si spegne."
[ -n "$SERVER" ] && wait $SERVER
