#!/bin/bash
# Rende un carosello in PNG 1080x1350 con Brave headless, poi esporta i JPEG.
# Le immagini non stanno nel vault: finiscono sul Desktop, e da li' in
# ~/lavoro/denkicode-social/media/ quando il carosello va in coda.
#   rendi-carosello.sh                          l'ultimo carosello in caroselli/
#   rendi-carosello.sh 2026-10-08-ore-whatsapp   quello
#   rendi-carosello.sh <nome> <dir>              quello, in un'altra cartella
set -e
QUI="$(cd "$(dirname "$0")" && pwd)"
NOME="${1:-$(ls "$QUI/caroselli" | sort | tail -1)}"
FUORI="${2:-$HOME/Desktop/denki-carosello-instagram-$NOME}"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# sul Mac di Nicola Chrome non c'e': Brave rende uguale (come rendi-storie.sh)
[ -x "$CHROME" ] || CHROME="/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
[ -d "$QUI/caroselli/$NOME" ] || { echo "carosello $NOME sconosciuto"; exit 1; }

mkdir -p "$FUORI/png"
# via i render del giro prima: il carosello si rinumera quando una slide esce
rm -f "$FUORI"/slide-*.jpg "$FUORI/png"/slide-*.png
for f in "$QUI"/caroselli/"$NOME"/slide-*.html; do
  n="$(basename "$f" .html)"
  "$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
    --force-device-scale-factor=1 --window-size=1080,1350 \
    --default-background-color=ff07070a \
    --screenshot="$FUORI/png/$n.png" "file://$f" >/dev/null 2>&1
  # Instagram ritaglia il carosello sul rapporto della prima: tutte 1080x1350
  [ "$(sips -g pixelHeight "$FUORI/png/$n.png" | awk '/pixelHeight/{print $2}')" = 1350 ] \
    || { echo "$n non e' alta 1350"; exit 1; }
  sips -s format jpeg -s formatOptions 92 "$FUORI/png/$n.png" \
    --out "$FUORI/$n.jpg" >/dev/null
  printf '%s  ' "$n"
done
echo
echo "$FUORI"
