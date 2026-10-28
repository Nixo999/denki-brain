// Misura i fotogrammi lunghi di una pagina con Brave via CDP (node 22, zero dipendenze).
//
// uso:
//   node 01-Coding/strumenti/misura-fotogrammi.mjs <url> [larghezza] [altezza] [durata] [distanza] [--ridotta]
//   node 01-Coding/strumenti/misura-fotogrammi.mjs <url> --vivo [--mobile] [--traccia] [larghezza] [altezza] [distanza] [--ridotta]
//
// Due modi, che non si mescolano:
//
// 1. Senza --vivo: Brave HEADLESS e SENZA GPU. Scorre con requestAnimationFrame per `durata` ms (9000) fino a
//    `distanza` px (tutta la pagina) e riporta, per fascia di 1000 px, quanti fotogrammi superano 32 ms, piu' i
//    dieci peggiori con la posizione. I numeri assoluti sono peggiori di un Mac vero: regge il CONFRONTO fra
//    sezioni e fra prima e dopo. Larghezza 1440, altezza 900 se non passate.
//    Lo scroll programmato e' 'instant' e forza scroll-behavior:auto: con html{scroll-behavior:smooth} (lo mette lo
//    starter) ogni scrollTo a ogni fotogramma farebbe ripartire uno scroll animato, e la pagina arrivava a ~1100 px
//    su 11.000. Le misure headless fatte dal 20/10/2026 su siti con smooth scroll valgono quindi solo per il primo
//    schermo: vanno rifatte. In --vivo la rotella vera non ne risente. --ridotta emula
//    prefers-reduced-motion: la differenza fra le due corse e' il costo della motion.
//
// 2. Con --vivo: il browser VERO del Mac, Brave con interfaccia e GPU (niente --headless, niente --disable-gpu).
//    Apre una finestra visibile e la tiene per circa mezzo minuto (piu' con --traccia): non toccare mouse e
//    tastiera nel frattempo e non coprirla, altrimenti il browser rallenta i fotogrammi. Misura due cose:
//    - APERTURA: i 2,2 s dopo l'evento load. Fotogrammi (media, p95, massimo, quanti oltre 20, 33 e 50 ms,
//      i peggiori con l'istante) e le long animation frame (LoAF) con durata, tempo di blocco e script attribuiti.
//    - SCROLL A ROTELLA: eventi `mouseWheel` veri (Input.dispatchMouseEvent, 50 px ogni 20 ms) fino in fondo.
//      Fotogrammi come sopra, i peggiori con la posizione in px, e il lavoro del thread principale da
//      Performance.getMetrics (layout, stile, script, in ms e in numero di passate).
//    --mobile  emula un telefono (mobile:true, touch) dentro la stessa finestra: 400x781 o la larghezza e
//              l'altezza passate. Senza --mobile la pagina usa la finestra vera (1440x900, la misura reale
//              viene stampata nell'intestazione).
//    --traccia registra anche la traccia di DevTools (Tracing) e stampa, per apertura e per scroll, il riassunto
//              per nome di evento (totale ms, numero, massimo) e gli eventi singoli piu' lunghi col nodo DOM
//              che li ha causati. La traccia pesa: i fotogrammi di quella corsa escono un po' peggiori.
//    In --vivo `durata` non conta (la rotella ha un suo passo) e `distanza` limita lo scroll.
//
// La regola: direttive-siti.md, 26/10/2026 («lagga tantissimo», «lagga, l'animazione iniziale va a scatti
// decisamente»): un sito non si mostra a Nicola finche' apertura e scroll non sono misurati nel suo Brave, a
// larghezza computer e a larghezza telefono. Quello e' --vivo, e --vivo --mobile.
// Browser: BROWSER_CATTURE, poi Brave, poi Chrome. Nato su sito-mybalance, 20/10/2026 («lagga un pochettino»).
// Dal 28/10/2026 in --vivo lo script porta la propria finestra davanti con System Events: un browser lanciato da un
// processo di sfondo resta dietro l'app, la pagina si vede nascosta (document.hidden) e i fotogrammi non valgono.
import { spawn, execFileSync } from 'node:child_process'
import { existsSync, mkdtempSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'

const argv = process.argv.slice(2)
const ha = f => argv.includes('--' + f)
const ridotta = ha('ridotta'), vivo = ha('vivo'), mobile = ha('mobile'), traccia = ha('traccia')
const pos = argv.filter(a => !a.startsWith('--'))
const [url, Wa, Ha, durata = 9000, distanza = 0] = pos
if (!url) { console.error('uso: node misura-fotogrammi.mjs <url> [larghezza] [altezza] [durata] [distanza] [--ridotta]\n     node misura-fotogrammi.mjs <url> --vivo [--mobile] [--traccia] [larghezza] [altezza] [distanza]'); process.exit(1) }
if (!vivo && (mobile || traccia)) { console.error('--mobile e --traccia valgono solo insieme a --vivo'); process.exit(1) }
// in --vivo il terzo numero dopo l'altezza e' la distanza (la durata non esiste)
const distanzaScelta = vivo ? +(pos[3] ?? 0) : +distanza
const W = +(Wa ?? (vivo && mobile ? 400 : 1440)), H = +(Ha ?? (vivo && mobile ? 781 : 900))
const attesa = ms => new Promise(r => setTimeout(r, ms))

// ---------- impalcatura CDP, una sola per tutte le modalita' ----------
async function avvia({ headless, finestra }) {
  const CANDIDATI = [process.env.BROWSER_CATTURE, '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'].filter(Boolean)
  const eseguibile = CANDIDATI.find(p => existsSync(p)); if (!eseguibile) throw new Error('nessun browser trovato (BROWSER_CATTURE, Brave, Chrome)')
  const porta = 9340 + Math.floor(Math.random() * 400), profilo = mkdtempSync(tmpdir() + '/misura-')
  const modo = headless ? ['--headless=new', '--disable-gpu'] : [`--window-size=${finestra}`, '--window-position=0,0', '--disable-session-crashed-bubble']
  const brave = spawn(eseguibile, [...modo, '--hide-scrollbars', `--remote-debugging-port=${porta}`, `--user-data-dir=${profilo}`, '--no-first-run', '--no-default-browser-check', 'about:blank'], { stdio: 'ignore' })
  const uscito = new Promise(r => brave.on('exit', r))
  const s = { eventi: [], tracce: [], coda: new Map(), n: 0, ws: null }
  let chiuso = false
  s.chiudi = async () => {
    if (chiuso) return; chiuso = true
    try { s.ws?.close() } catch {}
    brave.kill(); await Promise.race([uscito, attesa(4000)])
    try { rmSync(profilo, { recursive: true, force: true, maxRetries: 3, retryDelay: 300 }) } catch (e) { console.error('profilo temporaneo non cancellato (' + profilo + '): ' + e.code) }
  }
  try {
    let pagine
    for (let i = 0; i < 80; i++) { try { pagine = await (await fetch(`http://127.0.0.1:${porta}/json`)).json(); if (pagine.some(p => p.type === 'page')) break } catch {} await attesa(250) }
    const pagina = pagine?.find(p => p.type === 'page'); if (!pagina) throw new Error('Brave non ha aperto una pagina sulla porta ' + porta)
    s.ws = new WebSocket(pagina.webSocketDebuggerUrl); await new Promise((res, rej) => { s.ws.onopen = res; s.ws.onerror = rej })
    s.ws.onmessage = e => {
      const m = JSON.parse(e.data)
      if (m.id && s.coda.has(m.id)) { const { res, rej } = s.coda.get(m.id); s.coda.delete(m.id); m.error ? rej(new Error(m.error.message ?? JSON.stringify(m.error))) : res(m.result) }
      else if (m.method === 'Tracing.dataCollected') s.tracce.push(...m.params.value)
      else s.eventi.push(m.method)
    }
    s.cdp = (method, params = {}) => new Promise((res, rej) => { s.coda.set(++s.n, { res, rej }); s.ws.send(JSON.stringify({ id: s.n, method, params })) })
    // valuta un'espressione; per eseguire una funzione di questo file nella pagina: js(`(${fn})(arg)`). Mai `let` al livello globale.
    s.js = async expr => { const r = await s.cdp('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true }); if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description ?? r.exceptionDetails.text); return r.result.value }
    s.apri = async u => { s.eventi.length = 0; await s.cdp('Page.navigate', { url: u }); for (let i = 0; i < 100 && !s.eventi.includes('Page.loadEventFired'); i++) await attesa(100) }
    s.metriche = async () => Object.fromEntries((await s.cdp('Performance.getMetrics')).metrics.map(m => [m.name, m.value]))
    await s.cdp('Page.enable'); await s.cdp('Performance.enable')
    if (!headless) { try { await s.cdp('Page.bringToFront') } catch {} }
    if (!headless && process.platform === 'darwin') { try { execFileSync('osascript', ['-e', `tell application "System Events" to set frontmost of (first process whose unix id is ${brave.pid}) to true`], { stdio: 'ignore', timeout: 5000 }); await attesa(400) } catch {} }
    if (ridotta) await s.cdp('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] })
    return s
  } catch (e) { await s.chiudi(); throw e }
}
// differenza di due letture di Performance.getMetrics, in ms per le durate
const delta = (prima, dopo, k) => (dopo[k] - prima[k]) * (k.endsWith('Duration') ? 1000 : 1)
const lavoroMain = (prima, dopo) => ({ layout: Math.round(delta(prima, dopo, 'LayoutDuration')), layoutN: delta(prima, dopo, 'LayoutCount'), stile: Math.round(delta(prima, dopo, 'RecalcStyleDuration')), stileN: delta(prima, dopo, 'RecalcStyleCount'), script: Math.round(delta(prima, dopo, 'ScriptDuration')), compiti: Math.round(delta(prima, dopo, 'TaskDuration')), nodi: dopo.Nodes })

// ---------- modo 1: headless, scroll con requestAnimationFrame ----------
async function misuraHeadless() {
  const s = await avvia({ headless: true })
  try {
    await s.cdp('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: 2, mobile: false })
    await s.apri(url); await attesa(3800)
    const prima = await s.metriche()
    const esito = await s.js(`(async()=>{window.scrollTo(0,0);await new Promise(r=>setTimeout(r,600));
document.documentElement.style.scrollBehavior='auto';const frames=[];let last=performance.now();let run=true;(function tick(){const t=performance.now();frames.push({dt:t-last,y:scrollY});last=t;if(run)requestAnimationFrame(tick)})();
const dist=${distanzaScelta}||document.documentElement.scrollHeight-innerHeight,dur=${+durata},start=performance.now();
await new Promise(res=>{(function step(){const p=Math.min(1,(performance.now()-start)/dur);window.scrollTo({top:p*dist,behavior:'instant'});if(p<1)requestAnimationFrame(step);else res()})()});
run=false;await new Promise(r=>setTimeout(r,80));
const f=frames.slice(2);const dts=f.map(x=>x.dt).sort((a,b)=>a-b);const fasce={};
for(const x of f){const k=Math.floor(x.y/1000)*1000;fasce[k]??={n:0,lunghi:0,max:0};fasce[k].n++;if(x.dt>32)fasce[k].lunghi++;fasce[k].max=Math.max(fasce[k].max,Math.round(x.dt))}
const peggiori=[...f].sort((a,b)=>b.dt-a.dt).slice(0,10).map(x=>Math.round(x.dt)+'ms@'+Math.round(x.y));
return JSON.stringify({fotogrammi:f.length,dist:Math.round(dist),media:+(dts.reduce((a,b)=>a+b,0)/dts.length).toFixed(1),p50:+dts[Math.floor(dts.length*.5)].toFixed(1),p95:+dts[Math.floor(dts.length*.95)].toFixed(1),max:Math.round(dts.at(-1)),oltre32:dts.filter(d=>d>32).length,oltre50:dts.filter(d=>d>50).length,fasce,peggiori})})()`)
    const r = JSON.parse(esito), l = lavoroMain(prima, await s.metriche())
    console.log(`${ridotta ? 'MOTION RIDOTTA' : 'MOTION VIVA'} · ${W}x${H} · headless senza GPU · ${r.fotogrammi} fotogrammi su ${r.dist} px in ${durata} ms`)
    console.log(`media ${r.media} ms · p50 ${r.p50} · p95 ${r.p95} · max ${r.max} · oltre 32 ms: ${r.oltre32} · oltre 50 ms: ${r.oltre50}`)
    for (const [k, v] of Object.entries(r.fasce)) console.log(`  ${String(k).padStart(5)}-${String(+k + 999).padStart(5)} px: ${String(v.n).padStart(3)} fotogrammi, ${String(v.lunghi).padStart(2)} lunghi, max ${v.max} ms`)
    console.log('peggiori:', r.peggiori.join(' '))
    console.log(`lavoro del thread principale durante lo scroll: layout ${l.layout} ms in ${l.layoutN} passate · stile ${l.stile} ms in ${l.stileN} passate · script ${l.script} ms · nodi DOM ${l.nodi}`)
  } finally { await s.chiudi() }
}

// ---------- modo 2: --vivo, Brave con GPU, rotella vera ----------
// Funzioni eseguite NELLA pagina (serializzate con String): niente variabili di questo file dentro.
function campioneAvvia(buffered) {
  if (window.__po) window.__po.disconnect()
  const m = window.__m = { d: [], y: [], t: [], loaf: [], on: true, loafOk: false }
  const registra = lista => { for (const e of lista) m.loaf.push({ t: Math.round(e.startTime), d: Math.round(e.duration), blk: Math.round(e.blockingDuration), s: (e.scripts || []).slice(0, 3).map(x => ((x.sourceURL || '').split('/').pop().slice(0, 24) || '(inline)') + '|' + (x.invoker || '').slice(0, 30) + '|' + Math.round(x.duration)) }) }
  try { m.loafOk = PerformanceObserver.supportedEntryTypes.includes('long-animation-frame'); window.__po = new PerformanceObserver(l => registra(l.getEntries())); window.__po.observe({ type: 'long-animation-frame', buffered }); window.__registra = registra } catch (e) {}
  const t0 = performance.now(); let ultimo = t0
  requestAnimationFrame(function tick(t) { m.d.push(t - ultimo); m.y.push(Math.round(scrollY)); m.t.push(Math.round(t - t0)); ultimo = t; if (m.on) requestAnimationFrame(tick) })
  return 'ok'
}
function campioneFerma() {
  const m = window.__m; m.on = false
  try { window.__registra(window.__po.takeRecords()); window.__po.disconnect() } catch (e) {}
  const d = m.d.slice(2), ys = m.y.slice(2), ts = m.t.slice(2)
  const base = { w: innerWidth, h: innerHeight, dpr: devicePixelRatio, nascosta: document.hidden, loafOk: m.loafOk, loaf: m.loaf, yFine: Math.max(0, ...m.y), alto: document.documentElement.scrollHeight }
  if (!d.length) return { ...base, fotogrammi: 0 }
  const o = [...d].sort((a, b) => a - b), somma = d.reduce((a, b) => a + b, 0)
  const peggiori = d.map((x, i) => ({ ms: Math.round(x), y: ys[i], t: ts[i] })).sort((a, b) => b.ms - a.ms).slice(0, 8)
  return { ...base, fotogrammi: d.length, ms: Math.round(somma), media: +(somma / d.length).toFixed(1), p95: Math.round(o[Math.floor(o.length * .95)]), max: Math.round(o.at(-1)), oltre20: d.filter(x => x > 20).length, oltre33: d.filter(x => x > 33).length, oltre50: d.filter(x => x > 50).length, peggiori }
}
const CATEGORIE = ['-*', 'devtools.timeline', 'disabled-by-default-devtools.timeline', 'disabled-by-default-devtools.timeline.frame', 'blink.user_timing', 'disabled-by-default-devtools.timeline.stack']
// registra la traccia mentre gira fn. L'array degli eventi si svuota SEMPRE prima di Tracing.start e prima di
// Tracing.end, altrimenti l'attesa di tracingComplete legge quello della corsa precedente e la seconda traccia esce vuota.
async function conTraccia(s, fn) {
  if (!traccia) return { r: await fn(), ev: [] }
  s.tracce.length = 0
  await s.cdp('Tracing.start', { traceConfig: { includedCategories: CATEGORIE }, transferMode: 'ReportEvents' })
  const r = await fn()
  s.eventi.length = 0; await s.cdp('Tracing.end')
  for (let i = 0; i < 200 && !s.eventi.includes('Tracing.tracingComplete'); i++) await attesa(100)
  if (!s.eventi.includes('Tracing.tracingComplete')) console.log('  (avviso: la traccia non si e\' chiusa in tempo, il riassunto puo\' essere parziale)')
  return { r, ev: s.tracce.splice(0) }
}
async function riassuntoTraccia(s, titolo, tracce) {
  const ev = tracce.filter(e => e.ph === 'X' && e.dur > 0), per = {}
  for (const e of ev) { const p = per[e.name] ??= { tot: 0, n: 0, max: 0 }; p.tot += e.dur; p.n++; p.max = Math.max(p.max, e.dur) }
  const top = Object.entries(per).sort((a, b) => b[1].tot - a[1].tot).slice(0, 16).map(([k, v]) => `${k} ${Math.round(v.tot / 1000)}ms/${v.n} (max ${Math.round(v.max / 1000)})`)
  const lunghi = ev.filter(e => /^(Paint|Layout|UpdateLayoutTree|PrePaint|Layerize|FunctionCall|EvaluateScript|ParseHTML|HitTest|ImageDecodeTask|RasterTask|DecodeImage|TimerFire|EventDispatch|UpdateLayer|CompositeLayers|ScrollLayer|Commit|Animation)$/.test(e.name)).sort((a, b) => b.dur - a.dur).slice(0, 12)
  const ids = [...new Set(lunghi.map(e => e.args?.data?.nodeId).filter(Boolean))].slice(0, 10), nomi = {}
  if (ids.length) {
    try {
      await s.cdp('DOM.enable'); await s.cdp('DOM.getDocument', { depth: 0 })
      const { nodeIds } = await s.cdp('DOM.pushNodesByBackendIdsToFrontend', { backendNodeIds: ids })
      for (let i = 0; i < ids.length; i++) {
        try { const { node } = await s.cdp('DOM.describeNode', { nodeId: nodeIds[i] }); const a = node.attributes || []; const cls = a[a.indexOf('class') + 1]; nomi[ids[i]] = `${node.nodeName.toLowerCase()}${a.includes('class') ? '.' + String(cls).split(' ').slice(0, 2).join('.') : ''}${a.includes('id') ? '#' + a[a.indexOf('id') + 1] : ''}` } catch { nomi[ids[i]] = '?' }
      }
    } catch {}
  }
  const dett = lunghi.map(e => { const d = e.args?.data || {}; const extra = [d.nodeId ? nomi[d.nodeId] || ('nodo ' + d.nodeId) : '', d.layerId ? 'livello ' + d.layerId : '', d.clip ? 'clip ' + Math.round(d.clip[2] - d.clip[0]) + 'x' + Math.round(d.clip[5] - d.clip[1]) : '', d.functionName || '', d.url ? String(d.url).split('/').pop().slice(0, 22) : '', d.dirtyObjects ? 'sporchi ' + d.dirtyObjects : '', d.elementCount ? 'elementi ' + d.elementCount : '', d.type || ''].filter(Boolean).join(' '); return `${e.name} ${Math.round(e.dur / 1000)}ms ${extra}`.trim() })
  console.log(`  traccia ${titolo} — per nome (totale ms / numero, max):\n    ` + (top.join('\n    ') || '(vuota)') + '\n  eventi singoli piu\' lunghi:\n    ' + (dett.join('\n    ') || '(nessuno)'))
}
function stampaFotogrammi(r, conPosizione) {
  if (!r.fotogrammi) return console.log('  nessun fotogramma campionato')
  console.log(`  fotogrammi ${r.fotogrammi} in ${r.ms} ms · media ${r.media} ms · p95 ${r.p95} · max ${r.max} · oltre 20 ms: ${r.oltre20} · oltre 33 ms: ${r.oltre33} · oltre 50 ms: ${r.oltre50}`)
  console.log('  peggiori: ' + r.peggiori.map(p => conPosizione ? `${p.ms}ms@${p.y}px` : `${p.ms}ms@${p.t}ms`).join(' '))
}
async function misuraVivo() {
  const finestra = mobile ? `${Math.max(W, 1440)},${Math.max(H, 900)}` : `${W},${H}`
  const s = await avvia({ headless: false, finestra })
  try {
    if (mobile) {
      await s.cdp('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: 2, mobile: true, screenWidth: W, screenHeight: H })
      await s.cdp('Emulation.setTouchEmulationEnabled', { enabled: true, maxTouchPoints: 5 })
    }
    const etichetta = `${mobile ? 'telefono emulato' : 'finestra vera'}${ridotta ? ', motion ridotta' : ''}${traccia ? ', con traccia' : ''}`
    // 1) apertura
    const ap = await conTraccia(s, async () => {
      await s.apri(url)
      await s.js(`(${campioneAvvia})(true)`); await attesa(2200)
      return await s.js(`(${campioneFerma})()`)
    })
    const a = ap.r
    console.log(`VIVO · ${etichetta} · viewport ${a.w}x${a.h} @${a.dpr}x · Brave con GPU · ${url}`)
    if (a.nascosta) console.log('  AVVISO: la finestra risulta nascosta (document.hidden), i fotogrammi non sono affidabili')
    console.log('APERTURA (2,2 s dopo load, fotogrammi dopo il load; le LoAF coprono anche il caricamento)')
    stampaFotogrammi(a, false)
    const lo = [...a.loaf].sort((x, y) => y.d - x.d)
    if (!a.loafOk) console.log('  LoAF: non supportate da questo browser')
    else console.log(`  LoAF: ${lo.length}, durata totale ${lo.reduce((t, x) => t + x.d, 0)} ms, blocco totale ${lo.reduce((t, x) => t + x.blk, 0)} ms` + (lo.length > 8 ? ' (le 8 piu\' lunghe)' : ''))
    for (const x of lo.slice(0, 8)) console.log(`    t=${x.t}ms durata ${x.d}ms blocco ${x.blk}ms script: ${x.s.join(' ; ') || '(nessuno attribuito)'}`)
    if (traccia) await riassuntoTraccia(s, 'apertura (dalla navigazione a 2,2 s dopo load)', ap.ev)
    // 2) scroll a rotella
    await attesa(800); await s.js('scrollTo(0,0)'); await attesa(600)
    if (await s.js('document.hidden')) console.log('  AVVISO: la finestra risulta nascosta anche prima dello scroll, i fotogrammi non sono affidabili')
    const altezza = await s.js('document.documentElement.scrollHeight-innerHeight')
    const tot = distanzaScelta > 0 ? Math.min(distanzaScelta, altezza) : altezza, passi = Math.ceil(tot / 50) + 6
    const [cx, cy] = await s.js('[Math.round(innerWidth/2),Math.round(innerHeight/2)]')
    const prima = await s.metriche()
    const sc = await conTraccia(s, async () => {
      await s.js(`(${campioneAvvia})(false)`)
      for (let i = 0; i < passi; i++) { await s.cdp('Input.dispatchMouseEvent', { type: 'mouseWheel', x: cx, y: cy, deltaX: 0, deltaY: 50 }); await attesa(20) }
      await attesa(300)
      return await s.js(`(${campioneFerma})()`)
    })
    const dopo = await s.metriche(), r = sc.r, l = lavoroMain(prima, dopo)
    console.log(`SCROLL A ROTELLA (${passi} colpi da 50 px, uno ogni 20 ms; arrivato a ${r.yFine} px su ${altezza} scorribili)`)
    stampaFotogrammi(r, true)
    console.log(`  lavoro del thread principale: layout ${l.layout} ms in ${l.layoutN} passate · stile ${l.stile} ms in ${l.stileN} passate · script ${l.script} ms · compiti totali ${l.compiti} ms · nodi DOM ${l.nodi}`)
    if (traccia) await riassuntoTraccia(s, 'scroll', sc.ev)
  } finally { await s.chiudi() }
}

process.on('SIGINT', () => process.exit(130))
await (vivo ? misuraVivo() : misuraHeadless())
