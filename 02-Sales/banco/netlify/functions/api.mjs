// Le API del banco DM online. Lo stato sta in Netlify Blobs, store «banco»:
//   contattati.csv, gia-col-sito.csv   stesso formato di 02-Sales/liste/
//   messaggi.json                      {account: {handle: testo}}, i testi corretti a mano
//   utenti.json                        {nome: {sale, impronta}}, impronte scrypt
//
// POST /api/login {utente, password}   POST /api/logout
// GET  /api/stato                      POST /api/segna {file, azione, riga}
// POST /api/messaggio {account, handle, testo}
// GET  /api/esporta?file=contattati|gia-col-sito   con sessione o Bearer BANCO_TOKEN
//
// /api/segna fa quello che faceva segna() di banco-server.py: stessa chiave
// (Data, Da, Account IG minuscolo), niente doppioni, «togli» toglie e basta,
// righe ordinate. Due telefoni che scrivono insieme non si pestano: lettura,
// modifica e scrittura condizionata sull'ETag, e se qualcuno ha scritto in
// mezzo si rilegge e si riprova.
import { getStore } from '@netlify/blobs';
import { createHash, scryptSync, timingSafeEqual } from 'node:crypto';
import { chi, cookie, USCITA } from '../sessione.mjs';

export const CAMPI = ['Data', 'Da', 'Account IG', 'Nome', 'Comune', 'Segmento', 'Tipo', 'Lista'];
const FILE = { contattati: 'contattati.csv', 'gia-col-sito': 'gia-col-sito.csv' };
const ACCOUNT = ['patrick', 'denkicode'];

const archivio = () => getStore({ name: 'banco', consistency: 'strong' });
const pausa = (ms) => new Promise((r) => setTimeout(r, ms));
const risposta = (stato, corpo, altri = {}) => new Response(JSON.stringify(corpo), {
  status: stato,
  headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store', ...altri },
});

export const impronta = (parola, sale) => scryptSync(String(parola), Buffer.from(sale, 'hex'), 32);
const sha = (s) => createHash('sha256').update(String(s)).digest();

// ── CSV ── lo stesso lettore della pagina; in scrittura le virgolette solo
// dove servono, come il modulo csv di Python.
export function leggiCSV(t) {
  const righe = [];
  let campo = '', riga = [], dentro = false;
  t = t.replace(/^﻿/, '').replace(/\r\n/g, '\n');
  for (let i = 0; i < t.length; i++) {
    const c = t[i];
    if (dentro) {
      if (c === '"' && t[i + 1] === '"') { campo += '"'; i++; }
      else if (c === '"') dentro = false;
      else campo += c;
    } else if (c === '"') dentro = true;
    else if (c === ',') { riga.push(campo); campo = ''; }
    else if (c === '\n') { riga.push(campo); righe.push(riga); riga = []; campo = ''; }
    else campo += c;
  }
  if (campo || riga.length) { riga.push(campo); righe.push(riga); }
  return righe.filter((r) => r.some((c) => c !== ''));
}
const rigaDa = (riga) => CAMPI.map((k) => String(riga?.[k] ?? '').trim());
const scriviCSV = (righe) => righe.map((r) => r.map((c) =>
  /[",\r\n]/.test(c) ? '"' + c.replace(/"/g, '""') + '"' : c).join(',')).join('\n') + '\n';

// segna() di banco-server.py, sul testo del file. Le righe si leggono per
// posizione: gia-col-sito.csv ha righe vecchie piu' corte dell'intestazione, e
// Python le completa con campi vuoti allo stesso modo.
export function segna(testo, op) {
  const righe = leggiCSV(testo || '').slice(1).map((r) => CAMPI.map((_, i) => r[i] ?? ''));
  const riga = rigaDa(op.riga);
  const chiave = (r) => r[0] + '\u0000' + r[1] + '\u0000' + r[2].toLowerCase();
  const nuove = righe.filter((r) => chiave(r) !== chiave(riga));
  if ((op.azione ?? 'aggiungi') === 'aggiungi') nuove.push(riga);
  const per = (a, b) => (a < b ? -1 : a > b ? 1 : 0);
  nuove.sort((a, b) => per(a[0], b[0]) || per(a[1], b[1]) || per(a[2].toLowerCase(), b[2].toLowerCase()));
  return scriviCSV([CAMPI, ...nuove]);
}

// Lettura, modifica, scrittura solo se nessuno ha scritto nel frattempo; poi
// si rilegge e si controlla che il gesto ci sia davvero. Il controllo dopo
// serve: provato online l'11/10/2026, con 3-5 scritture in parallelo la
// scrittura condizionata di Netlify Blobs ne lasciava passare due sullo stesso
// ETag e 2-7 righe su 40 sparivano (tutte con risposta 200). Chi non ritrova
// il suo gesto lo riscrive.
export async function cambia(a, nome, modifica, fatto, attesa = 400) {
  for (let giro = 0; giro < 12; giro++) {
    const ora = await a.getWithMetadata(nome, { type: 'text' });
    if (ora && fatto(ora.data) && giro > 0) return;
    const scritto = await a.set(nome, modifica(ora ? ora.data : null), ora ? { onlyIfMatch: ora.etag } : { onlyIfNew: true });
    await pausa(scritto.modified ? attesa : 30 + Math.random() * 120 * (giro + 1));
    if (!scritto.modified) continue;
    const dopo = await a.get(nome, { type: 'text' });
    if (dopo !== null && fatto(dopo)) return;
  }
  throw new Error('troppe scritture insieme su ' + nome);
}

async function login(a, req) {
  let c = null;
  try { c = await req.json(); } catch {}
  const nome = String(c?.utente ?? '').trim().toLowerCase();
  const parola = String(c?.password ?? '');
  const utenti = (await a.get('utenti.json', { type: 'json' })) || {};
  const u = Object.hasOwn(utenti, nome) ? utenti[nome] : null;
  // lo scrypt si fa anche per un nome che non esiste: il tempo non dice chi c'e'
  const giusta = timingSafeEqual(
    impronta(parola.slice(0, 200), u?.sale ?? '00'.repeat(16)),
    Buffer.from(u?.impronta ?? '00'.repeat(32), 'hex'));
  if (!u || !giusta || parola.length > 200) {
    await pausa(500); // rallenta chi prova a indovinare
    return risposta(401, { errore: 'parola' });
  }
  return risposta(200, { ok: true }, { 'set-cookie': await cookie(nome) });
}

function conToken(req) {
  const atteso = globalThis.Netlify?.env?.get('BANCO_TOKEN') ?? process.env.BANCO_TOKEN;
  const m = /^Bearer\s+(\S{1,200})$/i.exec(req.headers.get('authorization') || '');
  return !!(atteso && m && timingSafeEqual(sha(m[1]), sha(atteso)));
}

async function corpo(req) {
  try { return await req.json(); } catch { return null; }
}

export default async (req) => {
  const via = new URL(req.url);
  const p = via.pathname.replace(/^\/api\//, '');
  try {
    const a = archivio();
    if (p === 'login' && req.method === 'POST') return await login(a, req);
    if (p === 'logout' && req.method === 'POST') return risposta(200, { ok: true }, { 'set-cookie': USCITA });

    if (p === 'esporta' && req.method === 'GET') {
      if (!conToken(req) && !(await chi(req))) return risposta(401, { errore: 'sessione' });
      const f = via.searchParams.get('file');
      if (!Object.hasOwn(FILE, f)) return risposta(400, { errore: 'file' });
      const t = (await a.get(FILE[f], { type: 'text' })) || CAMPI.join(',') + '\n';
      return new Response(t, { headers: {
        'content-type': 'text/csv; charset=utf-8', 'cache-control': 'no-store',
        'content-disposition': 'attachment; filename="' + FILE[f] + '"' } });
    }

    if (!(await chi(req))) return risposta(401, { errore: 'sessione' });

    if (p === 'stato' && req.method === 'GET') {
      const [c, g, m] = await Promise.all([
        a.get(FILE.contattati, { type: 'text' }), a.get(FILE['gia-col-sito'], { type: 'text' }),
        a.get('messaggi.json', { type: 'json' })]);
      return risposta(200, { contattati: c || '', 'gia-col-sito': g || '', messaggi: m || {} });
    }

    if (p === 'segna' && req.method === 'POST') {
      const op = await corpo(req);
      if (!op || !Object.hasOwn(FILE, op.file) || !['aggiungi', 'togli', undefined].includes(op.azione) ||
          !op.riga || typeof op.riga !== 'object' || !/^\d{4}-\d{2}-\d{2}$/.test(String(op.riga.Data ?? '').trim()) ||
          !String(op.riga['Account IG'] ?? '').trim()) return risposta(400, { errore: 'richiesta' });
      let n = 0;
      const chiave = (r) => String(r[0] ?? '').trim() + '\u0000' + String(r[1] ?? '').trim() + '\u0000' + String(r[2] ?? '').trim().toLowerCase();
      const mia = chiave(rigaDa(op.riga));
      const fatto = (t) => leggiCSV(t || '').slice(1).some((r) => chiave(r) === mia) === (op.azione !== 'togli');
      await cambia(a, FILE[op.file], (t) => { const nuovo = segna(t, op); n = leggiCSV(nuovo).length - 1; return nuovo; }, fatto);
      return risposta(200, { righe: n });
    }

    if (p === 'messaggio' && req.method === 'POST') {
      const m = await corpo(req);
      const handle = String(m?.handle ?? '').trim().replace(/^@/, '').toLowerCase();
      if (!m || !ACCOUNT.includes(m.account) || !handle || handle.length > 100 ||
          typeof m.testo !== 'string' || m.testo.length > 5000) return risposta(400, { errore: 'richiesta' });
      await cambia(a, 'messaggi.json', (t) => {
        const tutti = t ? JSON.parse(t) : {};
        (tutti[m.account] ??= {})[handle] = m.testo;
        return JSON.stringify(tutti);
      }, (t) => JSON.parse(t || '{}')[m.account]?.[handle] === m.testo);
      return risposta(200, { ok: true });
    }

    return risposta(404, { errore: 'percorso' });
  } catch (e) {
    console.error(e);
    return risposta(500, { errore: 'interno' });
  }
};

export const config = { path: '/api/*' };
