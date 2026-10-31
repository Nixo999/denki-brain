// Il sito visto da un telefono lento: lag e bocciature ricorrenti, misurati in Brave o Chrome headless (node 22, zero dipendenze).
//
// uso:
//   node 01-Coding/strumenti/cancelli-telefono.mjs <url> [--cpu 4] [--json]
//
// Viewport 375x812, mobile e touch, CPU rallentata di --cpu volte (4 se non passato: un telefono di fascia media).
// Misura:
// - APERTURA: i fotogrammi dei primi 2,5 s dalla navigazione (lo script si inietta prima che la pagina parta).
// - SCROLL: dall'alto in fondo in 9 s con requestAnimationFrame, come misura-fotogrammi.mjs headless.
// - LE BOCCIATURE RICORRENTI di 01-Coding/stack/direttive-siti.md che si vedono sulla pagina a 375 px:
//   pagina piu' larga del telefono (testo tagliato), apertura con sola scritta, numerazione delle sezioni,
//   muro di foto, disegni inline fatti da noi, sottolineature, cambi di sfondo netti fra sezioni, barra
//   appiccicata al titolo. Ogni controllo porta la data della direttiva da cui viene.
// LIMITE MISURATO il 31/10/2026: in headless il lag che Nicola sente nel suo Brave non si vede. Su quattro siti
// approvati (NG Barber, Fiftynine, Mikuma, Davide Milan) e cinque bocciati per il lag lo scroll da' a tutti un p95
// di 17-18 ms, con o senza GPU, e il lavoro del thread principale non li separa. Le soglie di SOGLIE fermano
// solo il lag grossolano; il segnale che separava i due gruppi e' il numero di elementi (controllo «peso»).
// Esce 1 se qualcosa BLOCCA. Con --json stampa solo l'esito, per cancelli-sito.py. Nato il 31/10/2026.
import { spawn } from 'node:child_process'
import { existsSync, mkdtempSync, rmSync } from 'node:fs'
import { tmpdir } from 'node:os'

// fermano solo il lag grossolano: vedi LIMITE MISURATO in testa
const SOGLIE = { scrollP95: 50, scrollOltre50: 25, aperturaMax: 400, aperturaOltre50: 12 }
const argv = process.argv.slice(2)
const url = argv.find(a => !a.startsWith('--') && !/^\d+$/.test(a))
const cpu = argv.includes('--cpu') ? +argv[argv.indexOf('--cpu') + 1] : 4
const comeJson = argv.includes('--json')
if (!url) { console.error('uso: node cancelli-telefono.mjs <url> [--cpu 4] [--json]'); process.exit(2) }
const W = 375, H = 812
const attesa = ms => new Promise(r => setTimeout(r, ms))

async function avvia() {
  const CANDIDATI = [process.env.BROWSER_CATTURE, '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'].filter(Boolean)
  const eseguibile = CANDIDATI.find(p => existsSync(p)); if (!eseguibile) throw new Error('nessun browser trovato (BROWSER_CATTURE, Brave, Chrome)')
  const porta = 9740 + Math.floor(Math.random() * 200), profilo = mkdtempSync(tmpdir() + '/cancelli-')
  const b = spawn(eseguibile, ['--headless=new', ...(process.env.CON_GPU ? [] : ['--disable-gpu']), '--hide-scrollbars', `--remote-debugging-port=${porta}`, `--user-data-dir=${profilo}`, '--no-first-run', '--no-default-browser-check', 'about:blank'], { stdio: 'ignore' })
  const uscito = new Promise(r => b.on('exit', r))
  const s = { eventi: [], coda: new Map(), n: 0 }
  s.chiudi = async () => { try { s.ws?.close() } catch {} b.kill(); await Promise.race([uscito, attesa(4000)]); try { rmSync(profilo, { recursive: true, force: true }) } catch {} }
  let pagine
  for (let i = 0; i < 80; i++) { try { pagine = await (await fetch(`http://127.0.0.1:${porta}/json`)).json(); if (pagine.some(p => p.type === 'page')) break } catch {} await attesa(250) }
  const pagina = pagine?.find(p => p.type === 'page'); if (!pagina) { await s.chiudi(); throw new Error('il browser non ha aperto una pagina') }
  s.ws = new WebSocket(pagina.webSocketDebuggerUrl); await new Promise((res, rej) => { s.ws.onopen = res; s.ws.onerror = rej })
  s.ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && s.coda.has(m.id)) { const { res, rej } = s.coda.get(m.id); s.coda.delete(m.id); m.error ? rej(new Error(m.error.message)) : res(m.result) } else s.eventi.push(m.method) }
  s.cdp = (method, params = {}) => new Promise((res, rej) => { s.coda.set(++s.n, { res, rej }); s.ws.send(JSON.stringify({ id: s.n, method, params })) })
  s.js = async expr => { const r = await s.cdp('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true }); if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description ?? r.exceptionDetails.text); return r.result.value }
  return s
}

// eseguita NELLA pagina prima di ogni suo script: campiona i fotogrammi dell'apertura
const CAMPIONE_APERTURA = `(()=>{const d=[];let u=performance.now();const t0=u;function k(t){d.push(t-u);u=t;if(t-t0<2500)requestAnimationFrame(k)}requestAnimationFrame(k);window.__apertura=d})()`

// eseguita NELLA pagina a scroll fermo in cima: le bocciature che si misurano
function bocciature() {
  const vw = innerWidth, vh = innerHeight, out = []
  const visibile = el => { const s = getComputedStyle(el); return s.display !== 'none' && s.visibility !== 'hidden' && +s.opacity > 0.05 }
  const r = el => { const b = el.getBoundingClientRect(); return { top: b.top + scrollY, bottom: b.bottom + scrollY, left: b.left, right: b.right, w: b.width, h: b.height } }
  const nome = el => el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (typeof el.className === 'string' && el.className.trim() ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.') : '')
  const testo = el => (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 50)

  // 1. pagina piu' larga del telefono, testo tagliato (12/10/2026 «la scritta libertà viene tagliata perché troppo grande»)
  const largo = document.documentElement.scrollWidth - vw
  const fuori = [...document.querySelectorAll('h1,h2,h3,p,a,button,img')].filter(e => visibile(e) && e.getBoundingClientRect().right > vw + 2 && e.getBoundingClientRect().width > 0).slice(0, 4).map(nome)
  out.push({ id: 'larghezza', direttiva: '12/10', blocca: largo > 1, ok: largo <= 1 && !fuori.length, msg: largo > 1 ? `la pagina e' larga ${vw + largo} px su ${vw}: scorre di lato` : fuori.length ? `elementi che escono dal bordo destro (forse tagliati da overflow): ${fuori.join(', ')}` : 'niente esce dal telefono' })

  // 2. apertura con la sola scritta (29/10/2026 «linizio con solo la scritta grande non mi pice, metti delle immagini»)
  let area = 0
  for (const e of document.querySelectorAll('img,picture,video,canvas,svg,[style*="background-image"],section,header,div')) {
    if (!visibile(e)) continue
    const b = e.getBoundingClientRect(); if (b.top >= vh || b.bottom <= 0) continue
    const bg = getComputedStyle(e).backgroundImage
    const media = /^(IMG|VIDEO|CANVAS|PICTURE)$/.test(e.tagName) || (bg && bg !== 'none' && /url\(/.test(bg))
    if (!media) continue
    area = Math.max(area, Math.max(0, Math.min(b.bottom, vh) - Math.max(b.top, 0)) * Math.max(0, Math.min(b.right, vw) - Math.max(b.left, 0)))
  }
  const quota = area / (vw * vh)
  out.push({ id: 'apertura', direttiva: '29/10', blocca: false, ok: quota >= 0.15, msg: `la foto o immagine piu' grande del primo schermo ne copre il ${Math.round(quota * 100)}%${quota < 0.15 ? ': apertura di sola scritta' : ''}` })

  // 3. numerazione delle sezioni (07/10/2026 «togli la numerazione dei pezzi mi dà fastidio che il numero sembri il titolo»)
  const numeri = [...document.querySelectorAll('h1,h2,h3,h4,span,small,p,div')].filter(e => e.children.length === 0 && visibile(e) && /^\s*(?:n[°º.]?\s*)?0\d\s*(?:[./—–-]|\/\s*0?\d+)?\s*$/i.test(e.textContent)).map(e => e.textContent.trim())
  out.push({ id: 'numerazione', direttiva: '07/10', blocca: false, ok: numeri.length < 2, msg: numeri.length < 2 ? 'nessuna numerazione di sezioni' : `numeri da sezione: ${[...new Set(numeri)].slice(0, 6).join(' ')}` })

  // 4. muro di foto sul telefono (26/10/2026 «da telefono risulta un po troppo ripetitivo e muro di foto»)
  const grandi = [...document.querySelectorAll('img,picture,video')].filter(e => visibile(e) && e.getBoundingClientRect().width > vw * 0.55 && e.getBoundingClientRect().height > 120).map(r).sort((a, b) => a.top - b.top)
  const testi = [...document.querySelectorAll('h1,h2,h3,p,blockquote')].filter(e => visibile(e) && testo(e).length > 25).map(r)
  let serie = 1, peggiore = 1, dove = 0
  for (let i = 1; i < grandi.length; i++) {
    const a = grandi[i - 1], b = grandi[i]
    const fraMezzo = testi.some(t => t.top >= a.bottom - 4 && t.bottom <= b.top + 4)
    serie = (!fraMezzo && b.top - a.bottom < 80 && b.top >= a.bottom - 8) ? serie + 1 : 1
    if (serie > peggiore) { peggiore = serie; dove = Math.round(b.top) }
  }
  out.push({ id: 'muro-di-foto', direttiva: '26/10', blocca: false, ok: peggiore < 4, msg: peggiore < 4 ? `al massimo ${peggiore} foto grandi di fila senza testo` : `${peggiore} foto grandi di fila senza testo fra loro, fino a ${dove} px` })

  // 5. disegni inline fatti da noi (12/10/2026 «non disegnare niente tu», 23/10/2026 «non disegnare mai tu a meno che non trovi una skills»)
  const disegni = [...document.querySelectorAll('svg')].filter(e => {
    if (!visibile(e) || e.closest('nav,footer,button,a,[class*=logo],[id*=logo],[aria-label*=logo i]')) return false
    const b = e.getBoundingClientRect(); if (b.width < 80 || b.height < 80) return false
    return e.querySelectorAll('path,circle,ellipse,line,polyline,polygon,rect').length >= 3
  }).map(e => `${nome(e)} ${Math.round(e.getBoundingClientRect().width)}x${Math.round(e.getBoundingClientRect().height)}`)
  out.push({ id: 'disegni-nostri', direttiva: '12/10 e 23/10', blocca: false, ok: !disegni.length, msg: disegni.length ? `${disegni.length} disegni inline sopra gli 80 px fuori da logo e icone: ${disegni.slice(0, 4).join(', ')}. Vengono da una skill?` : 'nessun disegno inline' })

  // 6. sottolineature decorative (16/10/2026 «le sottolineature dalle scritte toglile che fanno schifo»)
  const sott = [...document.querySelectorAll('h1,h2,h3,h4,p,span,em,strong')].filter(e => visibile(e) && !e.closest('a') && /underline/.test(getComputedStyle(e).textDecorationLine) && testo(e)).map(testo)
  out.push({ id: 'sottolineature', direttiva: '16/10', blocca: false, ok: !sott.length, msg: sott.length ? `scritte sottolineate fuori dai link: «${sott.slice(0, 3).join('», «')}»` : 'nessuna sottolineatura decorativa' })

  // 7. cambi di sfondo netti fra sezioni (28/10/2026 «le separazioni tra le sezioni fanno schifo, il colore è sempre diverso»)
  const lum = c => { const m = c.match(/[\d.]+/g); if (!m || (m[3] !== undefined && +m[3] < 0.5)) return null; const [R, G, B] = m.slice(0, 3).map(x => { x /= 255; return x <= 0.03928 ? x / 12.92 : ((x + 0.055) / 1.055) ** 2.4 }); return 0.2126 * R + 0.7152 * G + 0.0722 * B }
  const sezioni = [...document.querySelectorAll('main > section, body > section, main > div > section, body > main > *, body > header, body > footer')].filter(e => visibile(e) && e.getBoundingClientRect().height > 200)
  const fondi = sezioni.map(e => { let x = e; while (x && lum(getComputedStyle(x).backgroundColor) === null && getComputedStyle(x).backgroundImage === 'none') x = x.parentElement; return x ? (getComputedStyle(x).backgroundImage !== 'none' ? 'immagine' : lum(getComputedStyle(x).backgroundColor)) : lum('rgb(255,255,255)') })
  let netti = 0
  for (let i = 1; i < fondi.length; i++) if (typeof fondi[i] === 'number' && typeof fondi[i - 1] === 'number') { const [a, b] = [fondi[i], fondi[i - 1]].sort(); if ((b + 0.05) / (a + 0.05) > 3) netti++ }
  out.push({ id: 'separazioni', direttiva: '26/10 e 28/10', blocca: false, ok: netti <= 2, msg: `${netti} passaggi netti di sfondo (contrasto sopra 3:1) fra ${sezioni.length} sezioni${netti > 2 ? ': le sezioni sembrano incollate' : ''}` })

  // 8. barra appiccicata al titolo sul telefono (20/10/2026 «da telefono la navbar non va bene perche è appiccicata al titolo»)
  const barra = [...document.querySelectorAll('header,nav,[class*=nav],[class*=barra]')].find(e => visibile(e) && /fixed|sticky/.test(getComputedStyle(e).position) && e.getBoundingClientRect().top < 10)
  const titolo = document.querySelector('h1')
  let distanza = null
  if (barra && titolo && visibile(titolo)) distanza = Math.round(titolo.getBoundingClientRect().top - barra.getBoundingClientRect().bottom)
  out.push({ id: 'barra', direttiva: '20/10', blocca: false, ok: distanza === null || distanza >= 16, msg: distanza === null ? 'nessuna barra fissa sopra il titolo' : `fra la barra fissa e il titolo ci sono ${distanza} px` })
  // 9. peso della pagina. Il lag che Nicola vede nel suo Brave headless non si riproduce (31/10/2026: approvati e
  // bocciati hanno lo stesso p95 di 17-18 ms). L'unico segnale che li separava: gli elementi del DOM, 181-450 negli
  // approvati, 500-1625 nei bocciati per il lag (mybalance, emozionidicasa, groavel, pilates-district, martacesena).
  const nodi = document.querySelectorAll('*').length
  const infinite = document.getAnimations().filter(a => a.effect?.getComputedTiming?.().iterations === Infinity).length
  out.push({ id: 'peso', direttiva: '26/10 «lagga tantissimo»', blocca: false, ok: nodi <= 480 && infinite <= 4, msg: `${nodi} elementi nella pagina (approvati 181-450, bocciati per il lag 500-1625), ${infinite} animazioni infinite` })
  return out
}

async function scroll(s) {
  return s.js(`(async()=>{window.scrollTo(0,0);await new Promise(r=>setTimeout(r,600));
document.documentElement.style.scrollBehavior='auto';const f=[];let u=performance.now(),on=true;(function k(){const t=performance.now();f.push({dt:t-u,y:scrollY});u=t;if(on)requestAnimationFrame(k)})();
const dist=document.documentElement.scrollHeight-innerHeight,dur=9000,t0=performance.now();
await new Promise(res=>{(function st(){const p=Math.min(1,(performance.now()-t0)/dur);window.scrollTo({top:p*dist,behavior:'instant'});if(p<1)requestAnimationFrame(st);else res()})()});
on=false;const d=f.slice(2).map(x=>x.dt).sort((a,b)=>a-b);const peggiori=f.slice(2).sort((a,b)=>b.dt-a.dt).slice(0,6).map(x=>Math.round(x.dt)+'ms@'+Math.round(x.y)+'px');
return {fotogrammi:d.length,alto:dist+innerHeight,p50:Math.round(d[Math.floor(d.length*.5)]),p95:Math.round(d[Math.floor(d.length*.95)]),max:Math.round(d.at(-1)),oltre50:d.filter(x=>x>50).length,peggiori}})()`)
}

const s = await avvia()
let esito
try {
  await s.cdp('Page.enable')
  await s.cdp('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: 2, mobile: true, screenWidth: W, screenHeight: H })
  await s.cdp('Emulation.setTouchEmulationEnabled', { enabled: true, maxTouchPoints: 5 })
  await s.cdp('Emulation.setCPUThrottlingRate', { rate: cpu })
  await s.cdp('Page.addScriptToEvaluateOnNewDocument', { source: CAMPIONE_APERTURA })
  s.eventi.length = 0
  await s.cdp('Page.navigate', { url })
  for (let i = 0; i < 300 && !s.eventi.includes('Page.loadEventFired'); i++) await attesa(100)
  await attesa(3000)
  const ap = await s.js(`(()=>{const d=(window.__apertura||[]).slice(1);const o=[...d].sort((a,b)=>a-b);return {fotogrammi:d.length,max:Math.round(o.at(-1)||0),oltre50:d.filter(x=>x>50).length}})()`)
  await s.cdp('Performance.enable')
  const m0 = Object.fromEntries((await s.cdp('Performance.getMetrics')).metrics.map(m => [m.name, m.value]))
  const sc = await scroll(s)
  const m1 = Object.fromEntries((await s.cdp('Performance.getMetrics')).metrics.map(m => [m.name, m.value]))
  const ms = k => Math.round((m1[k] - m0[k]) * 1000)
  sc.lavoro = { compiti: ms('TaskDuration'), script: ms('ScriptDuration'), layout: ms('LayoutDuration'), stile: ms('RecalcStyleDuration'), layoutN: m1.LayoutCount - m0.LayoutCount, stileN: m1.RecalcStyleCount - m0.RecalcStyleCount }
  await s.js('window.scrollTo(0,0)'); await attesa(800)
  const bo = await s.js(`(${bocciature})()`)
  const lag = [
    { id: 'apertura-lag', blocca: true, ok: ap.max <= SOGLIE.aperturaMax && ap.oltre50 <= SOGLIE.aperturaOltre50, msg: `apertura: ${ap.fotogrammi} fotogrammi in 2,5 s, il piu' lungo ${ap.max} ms, ${ap.oltre50} oltre 50 ms (soglie ${SOGLIE.aperturaMax} e ${SOGLIE.aperturaOltre50})` },
    { id: 'scroll-lag', blocca: true, ok: sc.p95 <= SOGLIE.scrollP95 && sc.oltre50 <= SOGLIE.scrollOltre50, msg: `scroll su ${sc.alto} px: p95 ${sc.p95} ms, ${sc.oltre50} fotogrammi oltre 50 ms (soglie ${SOGLIE.scrollP95} e ${SOGLIE.scrollOltre50}); peggiori ${sc.peggiori.join(' ')}` },
  ]
  esito = { url, cpu, viewport: `${W}x${H}`, apertura: ap, scroll: sc, controlli: [...lag, ...bo] }
} finally { await s.chiudi() }

const blocca = esito.controlli.some(c => c.blocca && !c.ok)
if (comeJson) console.log(JSON.stringify(esito))
else {
  console.log(`telefono ${esito.viewport}, CPU rallentata ${cpu}x, headless senza GPU · ${url}`)
  console.log('  lavoro durante lo scroll: ' + JSON.stringify(esito.scroll.lavoro))
  for (const c of esito.controlli) console.log(`${c.ok ? '  ok    ' : c.blocca ? 'BLOCCA  ' : 'avvisa  '}${c.id.padEnd(15)}${c.msg}`)
}
process.exit(blocca ? 1 : 0)
