// Legge una pagina Instagram aperta nel browser dell'app, SENZA login, e restituisce JSON.
// Si incolla intero in javascript_tool (mcp__Claude_Browser__javascript_tool), con la scheda in primo piano.
//
// Sulla pagina del profilo (instagram.com/<utente>/) restituisce bio, numeri, link, titoli delle storie in
// evidenza, l'URL della foto profilo e l'elenco dei post della griglia (codice, tipo p|reel, data dall'alt).
// Sulla pagina di un post (instagram.com/<utente>/p/<codice>/) restituisce la didascalia intera e gli URL delle
// foto a taglia piena, letti da performance.getEntriesByType('resource'): solo `regular_photo`, mai i fotogrammi
// dei Reel (CLIPS, video_first_frame). Gli URL sono firmati e scadono: si passano subito a raccogli-instagram.py.
//
// Perche' il browser dell'app e non curl: dal 31/10/2026 l'API pubblica risponde 401 require_login, e la pagina
// del profilo da curl e' il guscio di login. Nel browser dell'app sloggato griglia e post si leggono ancora.
// Le trappole di questa strada stanno in 01-Coding/trappole.md (cerca «Instagram sloggato»).
await (async () => {
  await new Promise(r => setTimeout(r, 2500))   // dopo il modale di login le foto arrivano in ritardo
  const meta = s => document.querySelector(s)?.content ?? ''
  const tag = u => { try { return atob(decodeURIComponent(new URL(u).searchParams.get('efg') ?? '')) } catch { return '' } }
  const m = location.pathname.match(/^\/([^/]+)\/(p|reel)\/([^/]+)/) ?? location.pathname.match(/^\/(p|reel)\/([^/]+)/)
  if (m) {
    const codice = m.at(-1)
    // la didascalia sta in meta description dopo i due punti, fra virgolette
    const d = meta('meta[name=description]'), q = d.indexOf(': "')
    const visti = new Set(), immagini = []
    for (const u of performance.getEntriesByType('resource').map(e => e.name)) {
      if (!/fbcdn\.net|cdninstagram\.com/.test(u) || !/regular_photo/.test(tag(u))) continue
      const chiave = new URL(u).pathname.split('/').pop()
      if (!visti.has(chiave)) { visti.add(chiave); immagini.push(u) }
    }
    return JSON.stringify({ pagina: 'post', codice, tipo: m.at(-2), data: (d.match(/su ([A-Z][a-z]+ \d{1,2}, \d{4})/) ?? [])[1] ?? '',
      didascalia: q > 0 ? d.slice(q + 3).replace(/"\.?$/, '') : '', immagini,
      avviso: immagini.length ? '' : 'nessuna foto a taglia piena: scheda in primo piano? carosello? riprova dopo 3 s' })
  }
  const desc = meta('meta[name=description]')
  const num = re => (desc.match(re) ?? [])[1] ?? ''
  const utente = location.pathname.split('/')[1]
  const post = [...new Map([...document.querySelectorAll('a[href*="/p/"],a[href*="/reel/"]')].map(a => {
    const h = a.getAttribute('href'), p = h.match(/\/(p|reel)\/([^/]+)/), alt = a.querySelector('img')?.alt ?? ''
    return [p[2], { codice: p[2], tipo: p[1], di: h.split('/')[1] === utente || h.startsWith('/p/') || h.startsWith('/reel/') ? utente : h.split('/')[1],
      data: (alt.match(/on ([A-Z][a-z]+ \d{1,2}, \d{4})/) ?? [])[1] ?? '', alt: alt.replace(/^.*?\d{4}\.\s*/, '').slice(0, 200) }]
  })).values()]
  const evidenza = [...document.querySelectorAll('img[alt*="storia in evidenza"], img[alt*="highlight"]')]
    .map(i => i.closest('li')?.innerText?.trim()).filter(Boolean)
  const foto = document.querySelector('img[alt*="profilo"], img[alt*="profile picture"]')
  const link = [...document.querySelectorAll('a[href*="l.instagram.com"], a[rel*="nofollow"]')].map(a => a.innerText.trim() || a.href).filter(Boolean)
  return JSON.stringify({ pagina: 'profilo', utente, titolo: document.title.replace(/ • Foto e video.*$/, ''),
    follower: num(/^([\d.,]+[KkMm]?) follower/), post_totali: num(/([\d.,]+) post/),
    bio: (desc.match(/su Instagram: "([\s\S]*)"$/) ?? desc.match(/on Instagram: "([\s\S]*)"$/) ?? [])[1] ?? '',
    link: [...new Set(link)], evidenza: [...new Set(evidenza)], foto_profilo: foto?.currentSrc || foto?.src || '',
    post, loggato: !document.querySelector('a[href*="/accounts/login"]') })
})()
