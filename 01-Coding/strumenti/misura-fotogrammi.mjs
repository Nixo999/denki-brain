// Misura i fotogrammi lunghi mentre la pagina scorre, con Brave headless via CDP (node 22, zero dipendenze).
// Scorre con requestAnimationFrame per `durata` ms fino a `distanza` px e riporta, per fascia di 1000 px di
// scroll, quanti fotogrammi hanno superato 32 ms, piu' i dieci peggiori con la loro posizione.
// uso: node 01-Coding/strumenti/misura-fotogrammi.mjs <url> [larghezza=1440] [altezza=900] [durata=9000] [distanza=tutta] [--ridotta]
//   --ridotta emula prefers-reduced-motion: la differenza fra le due corse e' il costo della motion.
// Headless e' senza GPU: i numeri assoluti sono peggiori di un Mac vero, il confronto fra sezioni e fra prima e dopo regge.
// Nato su sito-mybalance, 20/10/2026 («lagga un pochettino»).
import { spawn } from 'node:child_process'
import { existsSync, mkdtempSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'
const argv = process.argv.slice(2); const ridotta = argv.includes('--ridotta')
const [url, W = 1440, H = 900, durata = 9000, distanza = 0] = argv.filter(a => !a.startsWith('--'))
const PORTA = 9338, profilo = mkdtempSync(tmpdir() + '/misura-')
const CANDIDATI = [process.env.BROWSER_CATTURE, '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'].filter(Boolean)
const eseguibile = CANDIDATI.find(p => existsSync(p)); if (!eseguibile) throw new Error('nessun browser headless')
const brave = spawn(eseguibile, ['--headless=new', '--disable-gpu', '--hide-scrollbars', `--remote-debugging-port=${PORTA}`, `--user-data-dir=${profilo}`, '--no-first-run', '--no-default-browser-check', 'about:blank'], { stdio: 'ignore' })
const attesa = ms => new Promise(r => setTimeout(r, ms))
let pagine; for (let i = 0; i < 60; i++) { try { pagine = await (await fetch(`http://127.0.0.1:${PORTA}/json`)).json(); if (pagine.length) break } catch {} await attesa(250) }
const ws = new WebSocket(pagine.find(p => p.type === 'page').webSocketDebuggerUrl); await new Promise(r => ws.onopen = r)
let n = 0; const coda = new Map(); const eventi = []
const cdp = (method, params = {}) => new Promise((res, rej) => { coda.set(++n, { res, rej }); ws.send(JSON.stringify({ id: n, method, params })) })
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && coda.has(m.id)) { const { res, rej } = coda.get(m.id); coda.delete(m.id); m.error ? rej(new Error(JSON.stringify(m.error))) : res(m.result) } else eventi.push(m.method) }
const js = async (expr) => (await cdp('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true })).result.value
await cdp('Page.enable'); await cdp('Emulation.setDeviceMetricsOverride', { width: +W, height: +H, deviceScaleFactor: 2, mobile: false })
if (ridotta) await cdp('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] })
await cdp('Page.navigate', { url }); for (let i = 0; i < 80 && !eventi.includes('Page.loadEventFired'); i++) await attesa(100)
await attesa(3800)
await cdp('Performance.enable')
const leggiMetriche = async () => Object.fromEntries((await cdp('Performance.getMetrics')).metrics.map(m => [m.name, m.value]))
const prima = await leggiMetriche()
const esito = await js(`(async()=>{window.scrollTo(0,0);await new Promise(r=>setTimeout(r,600));
const frames=[];let last=performance.now();let run=true;(function tick(){const t=performance.now();frames.push({dt:t-last,y:scrollY});last=t;if(run)requestAnimationFrame(tick)})();
const dist=${+distanza}||document.documentElement.scrollHeight-innerHeight,dur=${+durata},start=performance.now();
await new Promise(res=>{(function step(){const p=Math.min(1,(performance.now()-start)/dur);window.scrollTo(0,p*dist);if(p<1)requestAnimationFrame(step);else res()})()});
run=false;await new Promise(r=>setTimeout(r,80));
const f=frames.slice(2);const dts=f.map(x=>x.dt).sort((a,b)=>a-b);const fasce={};
for(const x of f){const k=Math.floor(x.y/1000)*1000;fasce[k]??={n:0,lunghi:0,max:0};fasce[k].n++;if(x.dt>32)fasce[k].lunghi++;fasce[k].max=Math.max(fasce[k].max,Math.round(x.dt))}
const peggiori=[...f].sort((a,b)=>b.dt-a.dt).slice(0,10).map(x=>Math.round(x.dt)+'ms@'+Math.round(x.y));
return JSON.stringify({fotogrammi:f.length,dist:Math.round(dist),media:+(dts.reduce((a,b)=>a+b,0)/dts.length).toFixed(1),p50:+dts[Math.floor(dts.length*.5)].toFixed(1),p95:+dts[Math.floor(dts.length*.95)].toFixed(1),max:Math.round(dts.at(-1)),oltre32:dts.filter(d=>d>32).length,oltre50:dts.filter(d=>d>50).length,fasce,peggiori})})()`)
const r = JSON.parse(esito)
const dopo = await leggiMetriche()
const delta = k => ((dopo[k] - prima[k]) * (k.endsWith('Duration') ? 1000 : 1))
r.lavoro = { layout: Math.round(delta('LayoutDuration')), stile: Math.round(delta('RecalcStyleDuration')), script: Math.round(delta('ScriptDuration')), layoutN: delta('LayoutCount'), stileN: delta('RecalcStyleCount'), nodi: dopo.Nodes }
console.log(`${ridotta ? 'MOTION RIDOTTA' : 'MOTION VIVA'} · ${W}x${H} · ${r.fotogrammi} fotogrammi su ${r.dist} px in ${durata} ms`)
console.log(`media ${r.media} ms · p50 ${r.p50} · p95 ${r.p95} · max ${r.max} · oltre 32 ms: ${r.oltre32} · oltre 50 ms: ${r.oltre50}`)
for (const [k, v] of Object.entries(r.fasce)) console.log(`  ${String(k).padStart(5)}-${String(+k + 999).padStart(5)} px: ${String(v.n).padStart(3)} fotogrammi, ${String(v.lunghi).padStart(2)} lunghi, max ${v.max} ms`)
console.log('peggiori:', r.peggiori.join(' '))
console.log(`lavoro del thread principale durante lo scroll: layout ${r.lavoro.layout} ms in ${r.lavoro.layoutN} passate · stile ${r.lavoro.stile} ms in ${r.lavoro.stileN} passate · script ${r.lavoro.script} ms · nodi DOM ${r.lavoro.nodi}`)
ws.close(); brave.kill(); rmSync(profilo, { recursive: true, force: true })
