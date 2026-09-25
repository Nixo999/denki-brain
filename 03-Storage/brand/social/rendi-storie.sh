#!/bin/bash
# Rende una serie di storie in PNG 1080x1920 con Chrome headless, poi esporta i JPEG.
# Le immagini non stanno nel vault: finiscono sul Desktop di Patrick.
#   rendi-storie.sh                    l'ultima serie in storie/
#   rendi-storie.sh 2026-09-16         quella serie
#   rendi-storie.sh 2026-09-16 <dir>   quella serie, in un'altra cartella
set -e
QUI="$(cd "$(dirname "$0")" && pwd)"
SERIE="${1:-$(ls "$QUI/storie" | sort | tail -1)}"
FUORI="${2:-$HOME/Desktop/denki-storie-instagram-$SERIE}"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[ -d "$QUI/storie/$SERIE" ] || { echo "serie $SERIE sconosciuta"; exit 1; }

mkdir -p "$FUORI/png"
# via i render del giro prima: la serie si rinumera quando una storia esce
rm -f "$FUORI"/storia-*.jpg "$FUORI/png"/storia-*.png
for f in "$QUI"/storie/"$SERIE"/storia-*.html; do
  n="$(basename "$f" .html)"
  "$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
    --force-device-scale-factor=1 --window-size=1080,1920 \
    --default-background-color=ff07070a \
    --screenshot="$FUORI/png/$n.png" "file://$f" >/dev/null 2>&1
  sips -s format jpeg -s formatOptions 92 "$FUORI/png/$n.png" \
    --out "$FUORI/$n.jpg" >/dev/null
  printf '%s  ' "$n"
done
echo
echo "$FUORI"
