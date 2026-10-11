// Prova del banco online, in locale e col protocollo vero: l'archivio e'
// BlobsServer (quello che Netlify usa in locale), funzione ed edge function
// sono quelle che vanno online. `npm install` prima.
//
//   node prova.mjs                 controlli a assert su login, porta, segna, concorrenza, esporta
//   node prova.mjs serve           il banco su http://localhost:8790, archivio in .netlify/blobs-prova
//                                  (al primo giro ci copia i due CSV del vault). Utente di prova:
//                                  BANCO_PROVA_PAROLA=... nell'ambiente lo crea o lo aggiorna
//   node prova.mjs utente          legge una password da stdin e stampa {sale, impronta} per utenti.json
//   node prova.mjs online <url>    25 scritture insieme sul sito vero (BANCO_SEGRETO e BANCO_TOKEN nell'ambiente)
import { createServer } from 'node:http';
import { existsSync, mkdirSync, mkdtempSync, readFileSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, extname, normalize } from 'node:path';
import { execFileSync } from 'node:child_process';
import { randomBytes } from 'node:crypto';
import assert from 'node:assert/strict';

process.chdir(new URL('.', import.meta.url).pathname);
const modo = process.argv[2] || 'controlli';

if (modo === 'utente') {
  const { impronta } = await import('./netlify/functions/api.mjs');
  const parola = readFileSync(0, 'utf8').trim();
  assert.ok(parola.length >= 8, 'password troppo corta');
  const sale = randomBytes(16).toString('hex');
  console.log(JSON.stringify({ sale, impronta: impronta(parola, sale).toString('hex') }));
  process.exit(0);
}

// Online: la scrittura condizionata vera di Netlify Blobs. Venticinque righe
// finte (Data 1999-01-01, Da «prova-concorrenza») scritte tutte insieme, poi
// tolte tutte insieme: alla fine contattati.csv e' com'era. Serve un cookie,
// e lo si firma qui con BANCO_SEGRETO: nessuna password passa in rete.
if (modo === 'online') {
  const base = process.argv[3];
  assert.ok(base && process.env.BANCO_SEGRETO && process.env.BANCO_TOKEN, 'serve: node prova.mjs online <url>, con BANCO_SEGRETO e BANCO_TOKEN');
  const { cookie } = await import('./netlify/sessione.mjs');
  const biscotto = (await cookie('concorrenza')).split(';')[0];
  const { leggiCSV } = await import('./netlify/functions/api.mjs');
  const esporta = async () => leggiCSV(await (await fetch(base + '/api/esporta?file=contattati', { headers: { authorization: 'Bearer ' + process.env.BANCO_TOKEN } })).text());
  const finte = (righe) => righe.filter((r) => r[1] === 'prova-concorrenza').length;
  const prima = (await esporta()).length;
  const tutte = (azione) => Promise.all(Array.from({ length: 25 }, (_, i) => fetch(base + '/api/segna', {
    method: 'POST', headers: { 'content-type': 'application/json', cookie: biscotto },
    body: JSON.stringify({ file: 'contattati', azione, riga: { Data: '1999-01-01', Da: 'prova-concorrenza', 'Account IG': '@finto' + i, Tipo: 'primo' } }),
  }).then((r) => r.status)));
  console.log('aggiungi:', await tutte('aggiungi'));
  const dentro = finte(await esporta());
  console.log('righe finte dopo 25 scritture insieme:', dentro);
  console.log('togli:', await tutte('togli'));
  const dopo = await esporta();
  console.log('righe finte rimaste:', finte(dopo), '· righe prima', prima, 'dopo', dopo.length);
  assert.equal(dentro, 25); assert.equal(finte(dopo), 0); assert.equal(dopo.length, prima);
  console.log('scrittura condizionata online: a posto');
  process.exit(0);
}

const { BlobsServer } = await import('@netlify/blobs/server');
const { getStore } = await import('@netlify/blobs');
const cartella = modo === 'serve' ? '.netlify/blobs-prova' : mkdtempSync(join(tmpdir(), 'banco-prova-'));
mkdirSync(cartella, { recursive: true });
const fileSegreto = join(cartella, '.segreto-locale');
if (!existsSync(fileSegreto)) writeFileSync(fileSegreto, randomBytes(32).toString('hex'));
process.env.BANCO_SEGRETO = readFileSync(fileSegreto, 'utf8');
process.env.BANCO_TOKEN = 'token-' + randomBytes(8).toString('hex');
const server = new BlobsServer({ directory: cartella, token: 'locale' });
const { port } = await server.start();
process.env.NETLIFY_BLOBS_CONTEXT = Buffer.from(JSON.stringify({
  edgeURL: 'http://localhost:' + port, uncachedEdgeURL: 'http://localhost:' + port, siteID: 'banco-prova', token: 'locale',
})).toString('base64');

const api = await import('./netlify/functions/api.mjs');
const porta = (await import('./netlify/edge-functions/porta.mjs')).default;
const archivio = () => getStore({ name: 'banco', consistency: 'strong' });
const SITO = 'https://banco.prova';
const pausa = (ms) => new Promise((r) => setTimeout(r, ms));

if (modo === 'serve') {
  await import('./build.mjs');
  const a = archivio();
  for (const f of ['contattati.csv', 'gia-col-sito.csv']) {
    if (!(await a.get(f))) await a.set(f, readFileSync('../liste/' + f, 'utf8'));
  }
  if (process.env.BANCO_PROVA_PAROLA) {
    const sale = randomBytes(16).toString('hex');
    const utenti = (await a.get('utenti.json', { type: 'json' })) || {};
    utenti.prova = { sale, impronta: api.impronta(process.env.BANCO_PROVA_PAROLA, sale).toString('hex') };
    await a.setJSON('utenti.json', utenti);
  }
  const TIPI = { '.html': 'text/html; charset=utf-8', '.csv': 'text/csv; charset=utf-8', '.webmanifest': 'application/manifest+json', '.png': 'image/png' };
  // come Netlify: / → index.html, /login → login.html
  const statico = (percorso) => {
    let f = percorso === '/' ? '/index.html' : percorso;
    if (!extname(f)) f += '.html';
    f = normalize('public' + decodeURIComponent(f));
    if (!f.startsWith('public/') || !existsSync(f)) return new Response('non trovato', { status: 404 });
    return new Response(readFileSync(f), { headers: { 'content-type': TIPI[extname(f)] || 'application/octet-stream', 'cache-control': 'no-cache' } });
  };
  createServer(async (req, res) => {
    const url = new URL(req.url, SITO);
    const corpo = req.method === 'POST' ? await new Promise((ok) => { const b = []; req.on('data', (c) => b.push(c)); req.on('end', () => ok(Buffer.concat(b))); }) : undefined;
    const richiesta = new Request(SITO + url.pathname + url.search, { method: req.method, headers: req.headers, body: corpo });
    let r;
    if (url.pathname.startsWith('/api/')) r = await api.default(richiesta);
    else if (/^\/(login|icone\/|manifest\.webmanifest)/.test(url.pathname)) r = statico(url.pathname);
    else r = (await porta(richiesta)) || statico(url.pathname);
    const intestazioni = Object.fromEntries([...r.headers].filter(([k]) => k !== 'set-cookie'));
    const biscotti = r.headers.getSetCookie();
    res.writeHead(r.status, biscotti.length ? { ...intestazioni, 'set-cookie': biscotti } : intestazioni);
    res.end(Buffer.from(await r.arrayBuffer()));
  }).listen(Number(process.env.PORT) || 8790, () => console.log('banco in locale: http://localhost:' + (Number(process.env.PORT) || 8790)));
} else {
  const a = archivio();
  const PAROLA = 'prova-' + randomBytes(6).toString('hex');
  const sale = randomBytes(16).toString('hex');
  await a.setJSON('utenti.json', { prova: { sale, impronta: api.impronta(PAROLA, sale).toString('hex') } });
  const chiama = (percorso, { corpo, biscotto, intestazioni = {} } = {}) => api.default(new Request(SITO + percorso, {
    method: corpo === undefined ? 'GET' : 'POST',
    headers: { 'content-type': 'application/json', ...(biscotto ? { cookie: biscotto } : {}), ...intestazioni },
    body: corpo === undefined ? undefined : JSON.stringify(corpo),
  }));

  // 1. login: sbagliato → 401 dopo mezzo secondo, mai 500; giusto → cookie
  let t = Date.now();
  let r = await chiama('/api/login', { corpo: { utente: 'prova', password: 'sbagliata' } });
  assert.equal(r.status, 401); assert.ok(Date.now() - t >= 450, 'il 401 deve arrivare dopo ~500 ms');
  assert.equal((await chiama('/api/login', { corpo: { utente: 'nessuno', password: PAROLA } })).status, 401);
  assert.equal((await chiama('/api/login', { corpo: 'non un oggetto' })).status, 401);
  r = await chiama('/api/login', { corpo: { utente: '  PROVA ', password: PAROLA } });
  assert.equal(r.status, 200, 'il nome non distingue maiuscole');
  const sc = r.headers.get('set-cookie');
  assert.match(sc, /HttpOnly/); assert.match(sc, /Secure/); assert.match(sc, /SameSite=Lax/); assert.match(sc, /Max-Age=15552000/);
  const biscotto = sc.split(';')[0];
  console.log('✓ login');

  // 2. la porta: senza sessione la pagina va al login, le liste 401
  const bordo = (p, c) => porta(new Request(SITO + p, { headers: c ? { cookie: c } : {} }));
  assert.equal((await bordo('/')).headers.get('location'), '/login');
  assert.equal((await bordo('/dati/lista-corrente.csv')).status, 401);
  assert.equal((await bordo('/DATI/lista-corrente.csv')).status, 401);
  assert.equal(await bordo('/', biscotto), undefined);
  const [u, s, f] = biscotto.split('=')[1].split('.');
  assert.equal((await bordo('/', 'banco=nicola.' + s + '.' + f)).status, 302, 'firma di un altro utente');
  assert.equal((await bordo('/', 'banco=' + u + '.' + (Number(s) + 1) + '.' + f)).status, 302, 'scadenza allungata');
  assert.equal((await chiama('/api/stato')).status, 401);
  assert.equal((await chiama('/api/stato', { biscotto: 'banco=x' })).status, 401);
  assert.match((await chiama('/api/logout', { corpo: {} })).headers.get('set-cookie'), /Max-Age=0/);
  console.log('✓ porta e sessione');

  // 3. segna: identico a segna() di banco-server.py, operazione per operazione
  const riga = (Data, h, Tipo = 'primo', Da = 'Patrick Sappa') => ({ Data, Da, 'Account IG': h, Nome: 'N, "virgolette"', Comune: 'C (MB)', Segmento: 'a\nb', Tipo, Lista: 'l' });
  const ops = [
    { file: 'contattati', azione: 'aggiungi', riga: riga('2026-10-02', '@Bravo') },
    { file: 'contattati', azione: 'aggiungi', riga: riga('2026-10-01', '@zeta') },
    { file: 'contattati', azione: 'aggiungi', riga: riga('2026-10-01', '@alfa') },
    { file: 'contattati', azione: 'aggiungi', riga: riga('2026-10-02', '@bravo', 'recupero') },
    { file: 'contattati', azione: 'aggiungi', riga: riga('2026-10-03', '@alfa', 'primo', 'DenkiCode') },
    { file: 'contattati', azione: 'togli', riga: riga('2026-10-01', '@ZETA') },
    { file: 'gia-col-sito', azione: 'aggiungi', riga: riga('2026-10-04', '@sito', 'scartato dal banco') },
  ];
  const partenza = readFileSync('../liste/gia-col-sito.csv', 'utf8'); // righe vecchie piu' corte dell'intestazione
  const py = mkdtempSync(join(tmpdir(), 'banco-py-'));
  writeFileSync(join(py, 'gia-col-sito.csv'), partenza);
  writeFileSync(join(py, 'ops.json'), JSON.stringify(ops));
  execFileSync('python3', ['-c', `
import importlib.util, json, sys
from pathlib import Path
spec = importlib.util.spec_from_file_location("bs", "../strumenti/banco-server.py")
bs = importlib.util.module_from_spec(spec); spec.loader.exec_module(bs)
d = Path(sys.argv[1])
bs.FILE = {"contattati": d / "contattati.csv", "gia-col-sito": d / "gia-col-sito.csv"}
for op in json.load(open(d / "ops.json")): bs.segna(op)
`, py]);
  let testo = { contattati: '', 'gia-col-sito': partenza };
  for (const op of ops) testo[op.file] = api.segna(testo[op.file], op);
  for (const f of ['contattati', 'gia-col-sito']) {
    assert.equal(testo[f], readFileSync(join(py, f + '.csv'), 'utf8'), f + ': JS e Python devono dare lo stesso file al byte');
  }
  console.log('✓ segna uguale a banco-server.py al byte (contattati e gia-col-sito)');

  // 4. venticinque gesti insieme da due telefoni: nessuno si perde. Il
  // BlobsServer locale non manda l'ETag in lettura, quindi qui si prova su un
  // archivio finto che, come quello vero sotto carico, a volte accetta un ETag
  // vecchio: il controllo dopo la scrittura deve ritrovare tutti i gesti.
  // Quello vero di Netlify si prova con `node prova.mjs online <url>`.
  let finto = null, versione = 0;
  const archivioFinto = {
    async getWithMetadata() { await pausa(Math.random() * 5); return finto && { ...finto }; },
    async get() { await pausa(Math.random() * 5); return finto && finto.data; },
    async set(_, data, o) {
      await pausa(Math.random() * 5);
      const vecchio = o.onlyIfNew ? finto !== null : finto?.etag !== o.onlyIfMatch;
      if (vecchio && Math.random() < 0.7) return { modified: false }; // il 30% passa lo stesso, come online
      finto = { data, etag: String(++versione) };
      return { modified: true, etag: finto.etag };
    },
  };
  await Promise.all(Array.from({ length: 25 }, (_, i) =>
    api.cambia(archivioFinto, 'x', (t) => api.segna(t, { file: 'contattati', riga: riga('2026-10-05', '@h' + i) }),
      (t) => (t || '').includes('@h' + i + ','), 5)));
  assert.equal(api.leggiCSV(finto.data).length - 1, 25, 'scritture concorrenti');
  for (let i = 0; i < 25; i++) {
    await chiama('/api/segna', { biscotto, corpo: { file: 'contattati', azione: 'aggiungi', riga: riga('2026-10-05', '@h' + i) } });
  }
  const stato = await (await chiama('/api/stato', { biscotto })).json();
  assert.equal(api.leggiCSV(stato.contattati).length - 1, 25);
  assert.equal((await chiama('/api/segna', { biscotto, corpo: { file: 'altro', riga: riga('2026-10-05', '@x') } })).status, 400);
  assert.equal((await chiama('/api/segna', { biscotto, corpo: { file: 'contattati', riga: riga('ieri', '@x') } })).status, 400);
  // il file del vault riletto e riscritto resta identico al byte
  const vault = readFileSync('../liste/contattati.csv', 'utf8');
  const giro = api.segna(vault, { azione: 'togli', riga: riga('1999-01-01', '@nessuno') });
  assert.equal(giro, vault, 'contattati.csv del vault, riletto e riscritto');
  console.log('✓ 25 scritture concorrenti (archivio finto), contattati.csv del vault identico dopo il giro');

  // 5. testi corretti a mano (in fila: vedi sopra per la concorrenza)
  for (const h of ['a', 'b', 'c']) await chiama('/api/messaggio', { biscotto, corpo: { account: 'patrick', handle: '@' + h, testo: 'ciao ' + h } });
  await chiama('/api/messaggio', { biscotto, corpo: { account: 'denkicode', handle: 'a', testo: '' } });
  const m = (await (await chiama('/api/stato', { biscotto })).json()).messaggi;
  assert.deepEqual(m, { patrick: { a: 'ciao a', b: 'ciao b', c: 'ciao c' }, denkicode: { a: '' } });
  assert.equal((await chiama('/api/messaggio', { biscotto, corpo: { account: 'altro', handle: 'a', testo: 'x' } })).status, 400);
  console.log('✓ messaggi');

  // 6. esporta: col token o con la sessione, mai senza
  r = await chiama('/api/esporta?file=contattati', { intestazioni: { authorization: 'Bearer ' + process.env.BANCO_TOKEN } });
  assert.equal(r.status, 200); assert.match(r.headers.get('content-type'), /text\/csv/);
  assert.ok((await r.text()).startsWith(api.CAMPI.join(',') + '\n'));
  assert.equal((await chiama('/api/esporta?file=contattati', { intestazioni: { authorization: 'Bearer sbagliato' } })).status, 401);
  assert.equal((await chiama('/api/esporta?file=gia-col-sito', { biscotto })).status, 200);
  assert.equal((await chiama('/api/esporta?file=../x', { biscotto })).status, 400);
  console.log('✓ esporta');

  await server.stop();
  console.log('tutto a posto');
}
