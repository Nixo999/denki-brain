// Campiona l'apertura: un fotogramma ogni N ms dal load. Stesso meccanismo di
// cattura-fette.mjs (Brave/Chrome headless via CDP), ma senza scroll.
// uso: node apertura.mjs <url> <cartella> <ms1,ms2,...>
import { spawn } from 'node:child_process'
import { existsSync, writeFileSync, mkdirSync, rmSync } from 'node:fs'
const [url, cartella, tempi] = process.argv.slice(2)
const MS = tempi.split(',').map(Number)
const PORTA = 9336, profilo = cartella + '/profilo'
rmSync(profilo, { recursive: true, force: true }); mkdirSync(cartella, { recursive: true })
const CANDIDATI = ['/Applications/Brave Browser.app/Contents/MacOS/Brave Browser',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome']
const eseguibile = CANDIDATI.find(p => existsSync(p))
if (!eseguibile) throw new Error('nessun browser headless')
const br = spawn(eseguibile, ['--headless=new', '--disable-gpu', '--hide-scrollbars',
  `--remote-debugging-port=${PORTA}`, `--user-data-dir=${profilo}`, '--no-first-run',
  '--no-default-browser-check', 'about:blank'], { stdio: 'ignore' })
const attesa = ms => new Promise(r => setTimeout(r, ms))
let pagine
for (let i = 0; i < 60; i++) { try { pagine = await (await fetch(`http://127.0.0.1:${PORTA}/json`)).json(); if (pagine.length) break } catch {} await attesa(250) }
const ws = new WebSocket(pagine.find(p => p.type === 'page').webSocketDebuggerUrl)
await new Promise(r => ws.onopen = r)
let n = 0; const coda = new Map()
const cdp = (method, params = {}) => new Promise((res, rej) => { coda.set(++n, { res, rej }); ws.send(JSON.stringify({ id: n, method, params })) })
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && coda.has(m.id)) { const { res, rej } = coda.get(m.id); coda.delete(m.id); m.error ? rej(new Error(JSON.stringify(m.error))) : res(m.result) } }
await cdp('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false })
await cdp('Page.enable')
cdp('Page.navigate', { url })   // non si attende: si campiona da adesso
const t0 = Date.now()
for (const ms of MS) {
  const resta = ms - (Date.now() - t0); if (resta > 0) await attesa(resta)
  const { data } = await cdp('Page.captureScreenshot', { format: 'png' })
  const nome = `${cartella}/a-${String(ms).padStart(4, '0')}.png`
  writeFileSync(nome, Buffer.from(data, 'base64')); console.log(nome)
}
ws.close(); br.kill()
