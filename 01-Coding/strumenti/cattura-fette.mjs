// Cattura a fette di viewport con Brave headless via CDP (node 22, zero dipendenze),
// piu' cinque posizioni dentro ogni pin di ScrollTrigger. Il pannello del browser
// non fotografa in modo attendibile dopo lo scroll: questo si'.
// uso: node 01-Coding/strumenti/cattura-fette.mjs <url> <larghezza> <altezza> <mobile 0|1> <cartella> <prefisso>
//   es. node cattura-fette.mjs http://localhost:8791/ 1440 900 0 /tmp/catture d
//       node cattura-fette.mjs http://localhost:8791/ 375 812 1 /tmp/catture m
// Poi si guardano i PNG (sips -Z 720 per ridurli). Nato su sito-hairstylebrescia, 16/09/2026.
import { spawn } from 'node:child_process'
import { existsSync, writeFileSync, mkdirSync, rmSync } from 'node:fs'
const [url, W, H, MOB, cartella, prefisso] = process.argv.slice(2)
const PORTA = 9334, profilo = cartella + '/profilo-brave'
rmSync(profilo, { recursive: true, force: true }); mkdirSync(cartella, { recursive: true })
// Brave se c'e', se no Chrome: su alcune macchine di casa Brave non e' installato.
const CANDIDATI = [process.env.BROWSER_CATTURE,
  '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'].filter(Boolean)
const eseguibile = CANDIDATI.find(p => existsSync(p))
if (!eseguibile) throw new Error('nessun browser headless trovato: ' + CANDIDATI.join(' · '))
const brave = spawn(eseguibile, [
  '--headless=new', '--disable-gpu', '--hide-scrollbars', `--remote-debugging-port=${PORTA}`,
  `--user-data-dir=${profilo}`, '--no-first-run', '--no-default-browser-check', 'about:blank'], { stdio: 'ignore' })
const attesa = ms => new Promise(r => setTimeout(r, ms))
let pagine
for (let i = 0; i < 60; i++) { try { pagine = await (await fetch(`http://127.0.0.1:${PORTA}/json`)).json(); if (pagine.length) break } catch {} await attesa(250) }
if (!pagine) { brave.kill(); throw new Error('il browser headless non risponde') }
const ws = new WebSocket(pagine.find(p => p.type === 'page').webSocketDebuggerUrl)
await new Promise(r => ws.onopen = r)
let n = 0; const coda = new Map(); const eventi = []
const cdp = (method, params = {}) => new Promise((res, rej) => { coda.set(++n, { res, rej }); ws.send(JSON.stringify({ id: n, method, params })) })
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && coda.has(m.id)) { const { res, rej } = coda.get(m.id); coda.delete(m.id); m.error ? rej(new Error(JSON.stringify(m.error))) : res(m.result) } else eventi.push(m.method) }
const js = async (expr) => (await cdp('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true })).result.value
await cdp('Page.enable'); await cdp('Network.enable'); await cdp('Network.setCacheDisabled', { cacheDisabled: true })
await cdp('Emulation.setDeviceMetricsOverride', { width: +W, height: +H, deviceScaleFactor: 1, mobile: MOB === '1' })
await cdp('Page.navigate', { url })
for (let i = 0; i < 80 && !eventi.includes('Page.loadEventFired'); i++) await attesa(100)
await attesa(3800) // apertura
await js(`Promise.all([...document.images].map(i=>{i.loading='eager';return i.decode().catch(()=>{})})).then(()=>1)`)
const info = await js(`JSON.stringify({h:document.documentElement.scrollHeight, w:document.documentElement.scrollWidth, st:(window.ScrollTrigger?ScrollTrigger.getAll().map(t=>[t.start,t.end,!!t.pin]):[])})`)
const { h, w, st } = JSON.parse(info); console.log('documento', h, 'x', w, 'trigger', JSON.stringify(st))
const posizioni = []
for (let y = 0; y < h; y += +H) posizioni.push(['fetta', y])
for (const [s, e, pin] of st) if (pin) for (const p of [0.1, 0.4, 0.7, 0.85, 0.98]) posizioni.push(['pin' + Math.round(p * 100), Math.round(s + (e - s) * p)])
let k = 0
for (const [nome, y] of posizioni) {
  await js(`window.scrollTo({top:${y},behavior:'instant'});1`); await attesa(1100)
  const reale = await js(`Math.round(scrollY)`)
  const { data } = await cdp('Page.captureScreenshot', { format: 'png' })
  const f = `${cartella}/${prefisso}-${String(k++).padStart(2, '0')}-${nome}-y${reale}.png`
  writeFileSync(f, Buffer.from(data, 'base64')); console.log(f.split('/').pop())
}
ws.close(); brave.kill()
