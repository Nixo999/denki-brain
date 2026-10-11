// La sessione del banco: un cookie firmato HMAC-SHA256 con BANCO_SEGRETO,
// valido 180 giorni. Lo usano la edge function (Deno) e la funzione (Node):
// solo Web Crypto, che c'e' in tutti e due.
//
// Formato: <utente>.<scadenza in secondi>.<firma base64url>. Niente archivio da
// leggere a ogni richiesta. Per buttare fuori tutti si cambia BANCO_SEGRETO.

const NOME = 'banco';
const DURATA = 180 * 24 * 3600;
const testo = new TextEncoder();

const segreto = () => globalThis.Netlify?.env?.get('BANCO_SEGRETO') ?? globalThis.process?.env?.BANCO_SEGRETO;
const a64 = (b) => btoa(String.fromCharCode(...new Uint8Array(b))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const da64 = (s) => Uint8Array.from(atob(s.replace(/-/g, '+').replace(/_/g, '/')), (c) => c.charCodeAt(0));
const chiave = (s, uso) => crypto.subtle.importKey('raw', testo.encode(s), { name: 'HMAC', hash: 'SHA-256' }, false, [uso]);

const attributi = '; Path=/; HttpOnly; Secure; SameSite=Lax';
export const USCITA = NOME + '=' + attributi + '; Max-Age=0';

// Il valore di Set-Cookie per chi ha appena dato nome e password giusti.
export async function cookie(utente) {
  const s = segreto();
  if (!s) throw new Error('BANCO_SEGRETO mancante');
  const corpo = utente + '.' + (Math.floor(Date.now() / 1000) + DURATA);
  const firma = a64(await crypto.subtle.sign('HMAC', await chiave(s, 'sign'), testo.encode(corpo)));
  return NOME + '=' + corpo + '.' + firma + attributi + '; Max-Age=' + DURATA;
}

// Il nome dell'utente se il cookie e' buono, altrimenti null. Mai un'eccezione.
export async function chi(req) {
  const s = segreto();
  const m = /(?:^|;\s*)banco=([a-z0-9_-]{1,40})\.(\d{1,12})\.([A-Za-z0-9_-]{43})(?:;|$)/.exec(req.headers.get('cookie') || '');
  if (!s || !m || Number(m[2]) < Date.now() / 1000) return null;
  try {
    const ok = await crypto.subtle.verify('HMAC', await chiave(s, 'verify'), da64(m[3]), testo.encode(m[1] + '.' + m[2]));
    return ok ? m[1] : null;
  } catch {
    return null;
  }
}
