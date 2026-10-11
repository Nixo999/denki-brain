// La build del banco: copia le due liste che /banco pubblica nel vault dentro
// public/dati/, dove la pagina le legge (dietro la edge function del login).
// Nient'altro: la pagina e' statica, lo stato sta in Netlify Blobs.
import { copyFileSync, mkdirSync } from 'node:fs';

const qui = new URL('.', import.meta.url);
mkdirSync(new URL('public/dati/', qui), { recursive: true });
for (const f of ['lista-corrente.csv', 'lista-denkicode.csv']) {
  copyFileSync(new URL('../strumenti/' + f, qui), new URL('public/dati/' + f, qui));
}
console.log('banco: liste copiate in public/dati/');
