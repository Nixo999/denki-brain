#!/bin/bash
# Rende le storie in PNG 1080x1920 con Chrome headless, poi esporta i JPEG.
# Le immagini non stanno nel vault: finiscono sul Desktop di Patrick.
set -e
QUI="$(cd "$(dirname "$0")" && pwd)"
OGGI="$(date +%Y-%m-%d)"
FUORI="${1:-$HOME/Desktop/denki-storie-instagram-$OGGI}"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

mkdir -p "$FUORI/png"
# via i render del giro prima: la serie si rinumera quando una storia esce
rm -f "$FUORI"/storia-*.jpg "$FUORI/png"/storia-*.png
for f in "$QUI"/storie/storia-*.html; do
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
