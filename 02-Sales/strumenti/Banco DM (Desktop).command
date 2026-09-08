#!/bin/sh
# Copia da tenere sul Desktop. Non contiene il banco: trova il vault, lo
# aggiorna, e lancia il lanciatore VERO che sta nel vault. Cosi' quando il
# banco cambia, cambia anche qui senza ricopiare niente.
for p in "$HOME/Desktop/denki-brain" "$HOME/lavoro/denki-brain" "$HOME/Desktop/denkicode volt" "$HOME/Documents/denkicode volt" "$HOME/denkicode volt"; do
  if [ -d "$p/02-Sales/strumenti" ]; then V="$p"; break; fi
done
if [ -z "$V" ]; then
  echo "Non trovo il vault (denki-brain sul Desktop). Premi invio per chiudere."; read _; exit 1
fi
cd "$V" && git pull --rebase --autostash -q 2>&1 | tail -1
exec sh "$V/02-Sales/strumenti/Banco DM.command"
