# Il Word che leggono al telefono

Giulia, Gabriele ed Edoardo non hanno il vault: leggono i `.docx` in
`02-Sales/script/`. Questi file li generano.

```bash
cd .claude/skills/script-vendita/word
npm install docx          # solo la prima volta, su una macchina nuova
node build.js             # riscrive i quattro .docx in 02-Sales/script/
```

- `build-lib.js` — impaginazione: Arial, grigi, riquadri delle battute,
  tabelle, piè di pagina. Non contiene testo di vendita
- `content-[a|b|c|d].js` — il testo dei quattro script, uno per prodotto

⚠️ **La verità sta nella nota, non qui.** `script-*.md` è il file che si
corregge dopo le chiamate; questi `content-*.js` sono la sua versione
impaginata. **Chi cambia lo script cambia tutti e due e rigenera il Word**,
altrimenti si telefona con la versione vecchia — che è esattamente il
problema che questi file dovrebbero evitare.
