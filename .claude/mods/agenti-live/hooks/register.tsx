import type { EngineInterface, Register, SessionMessage } from 'claude-code'

import type { Stima } from '../types'

const MAIN = 'agenti'
const DETTAGLIO = 'agente:'
const TICK = { plugin: 'agenti-live', key: 'tick' } as const
const STIME = { plugin: 'agenti-live', key: 'stime' } as const

// ---------------------------------------------------------------------------
// Testi e numeri

const STATO: Record<string, string> = {
  running: 'lavora',
  pending: 'in coda',
  completed: 'finito',
  failed: 'fallito',
  killed: 'fermato',
}
const PALLINO: Record<string, string> = { running: '●', pending: '◌', completed: '✓', failed: '✕', killed: '■' }
const COLORE: Record<string, string> = { running: 'green', pending: 'yellow', completed: 'gray', failed: 'red', killed: 'gray' }
/** Il colore della barra di avanzamento, per stato. */
const TINTA: Record<string, string> = { running: '#3e8ef7', pending: '#f5a623', completed: '#30a46c', failed: '#e5484d', killed: '#8a8a8a' }

const FINESTRA: Record<string, string> = {
  five_hour: '5 ore',
  seven_day: '7 giorni',
  seven_day_opus: '7 giorni · Opus',
  seven_day_sonnet: '7 giorni · Sonnet',
  spend_limit: 'Spesa',
}

const due = (n: number): string => String(n).padStart(2, '0')
const GIORNI = ['dom', 'lun', 'mar', 'mer', 'gio', 'ven', 'sab']

function azzera(iso?: string): string {
  if (!iso) return ''
  const d = new Date(iso)
  if (Number.isNaN(d.getTime())) return ''
  const ora = `${due(d.getHours())}:${due(d.getMinutes())}`
  const oggi = new Date()
  return d.toDateString() === oggi.toDateString()
    ? `si azzera alle ${ora}`
    : `si azzera ${GIORNI[d.getDay()]} ${d.getDate()} alle ${ora}`
}

/** La riga che dice su cosa lavora uno strumento: il comando, il file, la ricerca. */
function bersaglio(input: unknown): string {
  if (!input || typeof input !== 'object') return ''
  const i = input as Record<string, unknown>
  for (const key of ['description', 'command', 'file_path', 'pattern', 'query', 'url', 'skill', 'path', 'prompt']) {
    const v = i[key]
    if (typeof v === 'string' && v.trim()) return v.replace(/\s+/g, ' ').slice(0, 160)
  }
  return JSON.stringify(i).slice(0, 160)
}

function primaRiga(v: unknown): string {
  const t = typeof v === 'string' ? v : v == null ? '' : JSON.stringify(v)
  return (t.split('\n').find(r => r.trim()) ?? '').trim().slice(0, 200)
}

const quanto = (pct: number): string => `${Math.round(pct)}%`

function fa(quando: number): string {
  const min = Math.round((Date.now() - quando) / 60000)
  return min < 1 ? 'adesso' : `${min} min fa`
}

// ---------------------------------------------------------------------------
// La lancetta: un contachilometri da 240°. Per i limiti verde, ambra, rosso;
// per l'avanzamento blu che diventa verde a lavoro finito.

function lancetta(pct: number, titolo: string, sotto: string, avanzamento = false): string {
  const cx = 120
  const cy = 112
  const r = 92
  const p = Math.min(1, Math.max(0, pct / 100))
  const ang = (x: number) => ((150 + 240 * x) * Math.PI) / 180
  const pt = (x: number, rr: number) => [cx + rr * Math.cos(ang(x)), cy + rr * Math.sin(ang(x))].map(n => n.toFixed(1))
  const arco = (a: number, b: number, rr: number) => {
    const [x0, y0] = pt(a, rr)
    const [x1, y1] = pt(b, rr)
    return `M${x0} ${y0} A${rr} ${rr} 0 ${(b - a) * 240 > 180 ? 1 : 0} 1 ${x1} ${y1}`
  }
  const tacche: string[] = []
  for (let i = 0; i <= 50; i++) {
    const lunga = i % 5 === 0
    const [x0, y0] = pt(i / 50, r - 12)
    const [x1, y1] = pt(i / 50, r - (lunga ? 24 : 18))
    tacche.push(`<line x1="${x0}" y1="${y0}" x2="${x1}" y2="${y1}" stroke="#8a8a8a" stroke-width="${lunga ? 2 : 1}"/>`)
    if (i % 10 === 0) {
      const [tx, ty] = pt(i / 50, r - 36)
      tacche.push(`<text x="${tx}" y="${ty}" font-size="11" fill="#8a8a8a" text-anchor="middle" dominant-baseline="middle">${i * 2}</text>`)
    }
  }
  const colore = avanzamento
    ? pct >= 100 ? '#30a46c' : '#3e8ef7'
    : pct >= 80 ? '#e5484d' : pct >= 60 ? '#f5a623' : '#30a46c'
  const fasce = avanzamento
    ? ''
    : `<path d="${arco(0, 0.6, r)}" fill="none" stroke="#30a46c" stroke-opacity=".55" stroke-width="6"/>
  <path d="${arco(0.6, 0.8, r)}" fill="none" stroke="#f5a623" stroke-opacity=".7" stroke-width="6"/>
  <path d="${arco(0.8, 1, r)}" fill="none" stroke="#e5484d" stroke-opacity=".85" stroke-width="6"/>`
  const [tx, ty] = pt(p, r - 16)
  const [bx1, by1] = pt(p + 0.25, 6)
  const [bx2, by2] = pt(p - 0.25, 6)
  const [cx2, cy2] = pt(p + 0.5, 16)
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 200" width="240" height="200" font-family="-apple-system,system-ui,sans-serif">
  <path d="${arco(0, 1, r)}" fill="none" stroke="#8a8a8a" stroke-opacity=".18" stroke-width="10" stroke-linecap="round"/>
  ${fasce}
  ${p > 0 ? `<path d="${arco(0, p, r)}" fill="none" stroke="${colore}" stroke-width="10" stroke-linecap="round"/>` : ''}
  ${tacche.join('')}
  <polygon points="${tx},${ty} ${bx1},${by1} ${cx2},${cy2} ${bx2},${by2}" fill="#ff6a3d"/>
  <circle cx="${cx}" cy="${cy}" r="8" fill="#2b2b2b" stroke="#ff6a3d" stroke-width="2"/>
  <text x="${cx}" y="${cy + 44}" font-size="26" font-weight="700" fill="${colore}" text-anchor="middle">${pct.toFixed(pct % 1 ? 1 : 0)}%</text>
  <text x="${cx}" y="${cy + 64}" font-size="12" font-weight="600" fill="#8a8a8a" text-anchor="middle">${titolo}</text>
  <text x="${cx}" y="${cy + 80}" font-size="10.5" fill="#8a8a8a" text-anchor="middle">${sotto}</text>
</svg>`
}

/** Il contachilometri: il costo della sessione a listino API, a rulli. */
function rulli(usd: number): string {
  const testo = usd.toFixed(2).padStart(7, '0')
  const celle = testo
    .split('')
    .map((c, i) => {
      const x = 4 + i * 20
      const centesimi = i >= testo.length - 2
      if (c === '.') return `<text x="${x + 9}" y="25" font-size="20" font-weight="700" fill="#f2f2f2" text-anchor="middle">.</text>`
      return `<rect x="${x}" y="4" width="18" height="26" rx="3" fill="${centesimi ? '#b3261e' : '#1f1f1f'}"/>
      <text x="${x + 9}" y="23" font-size="17" font-weight="700" fill="#f2f2f2" text-anchor="middle" font-family="ui-monospace,Menlo,monospace">${c}</text>`
    })
    .join('')
  const w = 8 + testo.length * 20
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} 50" width="${w}" height="50">
  <rect x="0" y="0" width="${w}" height="34" rx="5" fill="#0d0d0d"/>${celle}
  <text x="${w / 2}" y="46" font-size="10" fill="#8a8a8a" text-anchor="middle" font-family="-apple-system,system-ui,sans-serif">$ della sessione, a listino API</text>
</svg>`
}

const barra = (pct: number, w = 20): string => {
  const pieni = Math.round((Math.min(100, Math.max(0, pct)) / 100) * w)
  return '█'.repeat(pieni) + '░'.repeat(w - pieni)
}

/** La barra di un agente, per il desktop: piena quanto è fatto, l'etichetta a destra. */
function barraSvg(pct: number | null, colore: string, etichetta: string): string {
  const pieno = pct == null ? 0 : Math.round((Math.min(100, Math.max(0, pct)) / 100) * 200)
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 16" width="340" height="16" font-family="-apple-system,system-ui,sans-serif">
  <rect x="0" y="3" width="200" height="10" rx="5" fill="#8a8a8a" fill-opacity=".2"/>
  ${pieno > 0 ? `<rect x="0" y="3" width="${pieno}" height="10" rx="5" fill="${colore}"/>` : ''}
  <text x="210" y="12.5" font-size="11.5" fill="#8a8a8a">${etichetta}</text>
</svg>`
}

type Voce =
  | { tipo: 'testo'; testo: string }
  | { tipo: 'tool'; tool: string; detail: string; esito: string; errore: boolean; finito: boolean }

/** I passi di un agente letti dal suo transcript: solo lettura, niente sul suo percorso. */
function passi(found: readonly SessionMessage[]): Voce[] {
  const voci: Voce[] = []
  for (const m of found) {
    if (m.role !== 'assistant') continue
    if (m.text.trim()) voci.push({ tipo: 'testo', testo: m.text.trim() })
    for (const u of m.toolUses) {
      voci.push({
        tipo: 'tool',
        tool: u.tool,
        detail: bersaglio(u.input),
        esito: primaRiga(u.text ?? u.result),
        errore: u.isError === true,
        finito: u.result !== undefined || u.text !== undefined,
      })
    }
  }
  return voci
}

// ---------------------------------------------------------------------------
// A che punto è. Misurato quando c'è un piano (TodoWrite), stimato da Haiku se no:
// la barra dice sempre quale dei due sta mostrando.

type Avanzamento = { pct: number | null; fonte: string; fase: string }

function piano(found: readonly SessionMessage[]): Avanzamento | null {
  const usi = found.flatMap(m => m.toolUses).filter(u => u.tool === 'TodoWrite')
  const ultimo = usi[usi.length - 1]?.input as { todos?: { status?: string; content?: string; activeForm?: string }[] } | undefined
  const todos = ultimo?.todos
  if (!Array.isArray(todos) || todos.length === 0) return null
  const fatti = todos.filter(t => t.status === 'completed').length
  const ora = todos.find(t => t.status === 'in_progress')
  return { pct: (fatti / todos.length) * 100, fonte: `piano ${fatti}/${todos.length}`, fase: ora?.activeForm ?? ora?.content ?? '' }
}

function avanzamento(stato: string, p: Avanzamento | null, s: Stima | undefined): Avanzamento {
  if (stato === 'completed') return { pct: 100, fonte: 'finito', fase: '' }
  if (p) return p
  if (s) return { pct: s.pct, fonte: `stima, ${fa(s.quando)}`, fase: s.fase }
  return { pct: null, fonte: stato === 'running' ? 'stima in arrivo' : STATO[stato] ?? stato, fase: '' }
}

const storia = (voci: Voce[]): string =>
  voci
    .slice(-15)
    .map(v => (v.tipo === 'testo' ? `(scrive) ${v.testo.slice(0, 300)}` : `[${v.tool}] ${v.detail}${v.esito ? ` → ${v.esito.slice(0, 120)}` : ''}`))
    .join('\n') || '(ancora niente)'

const SOLO_JSON = "Rispondi con un solo oggetto JSON e nient'altro:"

function domandaAgente(compito: string, voci: Voce[]): string {
  return `Un agente di programmazione lavora a questo compito:
<compito>
${compito.slice(0, 2500)}
</compito>

Ha fatto ${voci.length} passi. Gli ultimi:
${storia(voci)}

Stima quanto del compito è fatto, da 0 a 95: conta quello che resta da fare, non i passi già fatti.
${SOLO_JSON} {"pct": <numero>, "fase": "<cosa fa adesso, massimo 8 parole, in italiano>"}`
}

function domandaChat(main: readonly SessionMessage[], agenti: string[]): string {
  const persona = main.filter(m => m.role === 'user' && m.text.trim())
  const scelti = persona.length > 7 ? [...persona.slice(0, 4), ...persona.slice(-3)] : persona
  const assistente = main.filter(m => m.role === 'assistant' && m.text.trim()).slice(-4)
  return `Questa è una chat di lavoro tra una persona e un assistente di programmazione.

Messaggi della persona, in ordine (il compito principale di solito è il primo che chiede un lavoro):
${scelti.map(m => `- ${m.text.trim().slice(0, 700)}`).join('\n')}

Ultime cose scritte dall'assistente:
${assistente.map(m => `- ${m.text.trim().slice(0, 500)}`).join('\n') || '- niente'}

Ultimi passi dell'assistente:
${storia(passi(main))}

Agenti lanciati:
${agenti.join('\n') || '- nessuno'}

${SOLO_JSON} {"obiettivo": "<il compito principale della chat, massimo 12 parole, in italiano>", "pct": <da 0 a 100, quanto del compito principale è fatto; 100 solo se l'assistente l'ha consegnato e non resta niente>, "fase": "<a che punto siamo, massimo 10 parole>"}`
}

async function chiedi($: EngineInterface, prompt: string): Promise<Omit<Stima, 'passi' | 'quando'> | null> {
  const r = await $.model.complete({ model: 'haiku', prompt, maxTokens: 200, effort: 'low', timeoutMs: 30_000 })
  const json = r.isAnswered ? r.text.match(/\{[\s\S]*\}/)?.[0] : undefined
  if (!json) return null
  try {
    const j = JSON.parse(json) as Record<string, unknown>
    const pct = Number(j.pct)
    if (!Number.isFinite(pct)) return null
    return {
      pct: Math.min(100, Math.max(0, pct)),
      fase: String(j.fase ?? '').slice(0, 90),
      obiettivo: typeof j.obiettivo === 'string' ? j.obiettivo.slice(0, 140) : undefined,
    }
  } catch {
    return null
  }
}

// Si stima solo a pannello aperto: chiuso, non si spende niente.
let disegnato = 0
let stimando = false

async function stima($: EngineInterface): Promise<void> {
  if (stimando || Date.now() - disegnato > 30_000) return
  stimando = true
  try {
    const prima: Record<string, Stima> = (await $.state.get(STIME)).value ?? {}
    const ora = Date.now()
    // si rifà quando è cambiato qualcosa, e non più spesso di `ogni`
    const daRifare = (id: string, n: number, ogni: number) => {
      const s = prima[id]
      return !s || (s.passi !== n && ora - s.quando >= ogni)
    }
    const nuove: Record<string, Stima> = {}
    const agenti = await $.agent.list()
    await Promise.all(
      agenti
        .filter(a => a.status === 'running')
        .map(async a => {
          const found = await $.session.messages({ agentId: a.id })
          if ('deny' in found || piano(found)) return
          const voci = passi(found)
          if (!daRifare(a.id, voci.length, 45_000)) return
          const s = await chiedi($, domandaAgente(found.find(m => m.role === 'user')?.text ?? a.description, voci))
          if (s) nuove[a.id] = { ...s, passi: voci.length, quando: ora }
        }),
    )
    const main = await $.session.messages()
    if (main.some(m => m.role === 'user') && daRifare('main', main.length, 60_000)) {
      const righe = agenti.map(a => {
        const s = nuove[a.id] ?? prima[a.id]
        return `- ${a.description}: ${STATO[a.status] ?? a.status}${a.status === 'running' && s ? `, circa ${quanto(s.pct)}` : ''}`
      })
      const s = await chiedi($, domandaChat(main, righe))
      if (s) nuove.main = { ...s, passi: main.length, quando: ora }
    }
    // ponytail: legge e riscrive senza lock, regge perché scrive solo stima() e `stimando` la tiene da sola
    if (Object.keys(nuove).length > 0) await $.state.set(STIME, { ...prima, ...nuove })
  } finally {
    stimando = false
  }
}

// ---------------------------------------------------------------------------
// Solo lettura: nessun hook sul percorso degli agenti (tool.call, turn.step).
// La prima versione ci scriveva lo stato e li ha fermati tutti e quattro.

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'agenti', description: 'Apre il pannello degli agenti al lavoro' })
    $.clock.every(5000, () => void $.clock.now().then(t => $.state.set(TICK, t)))
    $.clock.every(10_000, () => void stima($))
    void $.ui.open({ id: MAIN, title: 'Agenti' })
    return next(e)
  })

  on('command.run', { command: 'agenti' }, async $ => {
    await $.ui.open({ id: MAIN, title: 'Agenti' })
    return { text: 'Pannello degli agenti aperto.' }
  })

  on('ui.render', { component: 'Pane' }, async ($, e, next) => {
    if (e.requestId !== MAIN && !e.requestId.startsWith(DETTAGLIO)) return next(e)
    const ui = $.ui.resolve(e)
    const { Box, Text, Button } = ui
    await $.state.get(TICK)
    disegnato = Date.now()
    // nel terminale Svg c'è ma disegna niente: lì vanno le barre di testo
    const Svg = e.surface !== 'terminal' && 'Svg' in ui ? ui.Svg : null

    // ----- Dettaglio di un agente
    if (e.requestId.startsWith(DETTAGLIO)) {
      const id = e.requestId.slice(DETTAGLIO.length)
      const info = (await $.agent.list()).find(a => a.id === id)
      const found = await $.session.messages({ agentId: id })
      const head = (
        <Box flexDirection="column" marginBottom={1}>
          <Text bold>{info?.description ?? id}</Text>
          <Text dimColor>
            {[info ? `${PALLINO[info.status] ?? '·'} ${STATO[info.status] ?? info.status}` : '', info?.type].filter(Boolean).join(' · ')}
          </Text>
        </Box>
      )
      if ('deny' in found) {
        return (
          <Box flexDirection="column">
            {head}
            <Text color="red">{`Non posso leggere questo agente: ${String(found.deny)}`}</Text>
          </Box>
        )
      }
      const compito = found.find(m => m.role === 'user')?.text ?? ''
      const voci = passi(found)
      const recenti = voci.slice(-40).reverse()
      return (
        <Box flexDirection="column">
          {head}
          <Text bold>Compito</Text>
          <Text dimColor wrap="wrap">{compito.slice(0, 600) + (compito.length > 600 ? '…' : '')}</Text>
          <Box marginTop={1} flexDirection="column">
            <Text bold>{`Cosa fa adesso (${voci.length} passi, i più recenti in alto)`}</Text>
            {recenti.length === 0 && <Text dimColor>Ancora niente.</Text>}
            {recenti.map((v, i) =>
              v.tipo === 'testo' ? (
                <Box marginTop={1} flexDirection="column">
                  <Text italic wrap="wrap">{v.testo.slice(0, 700) + (v.testo.length > 700 ? '…' : '')}</Text>
                </Box>
              ) : (
                <Box flexDirection="column" marginTop={i === 0 ? 1 : 0}>
                  <Text wrap="truncate-end">
                    <Text bold color={v.errore ? 'red' : v.finito ? undefined : 'yellow'}>{`${v.finito ? '▸' : '⟳'} ${v.tool}`}</Text>
                    {`  ${v.detail}`}
                  </Text>
                  {v.esito ? <Text dimColor wrap="truncate-end">{`   → ${v.esito}`}</Text> : null}
                </Box>
              ),
            )}
          </Box>
        </Box>
      )
    }

    // ----- Il pannello principale
    const uso = await $.session.usage()
    const limiti = uso.rateLimits
    const stime: Record<string, Stima> = (await $.state.get(STIME)).value ?? {}
    const agenti = await $.agent.list()
    const lavorano = agenti.filter(a => a.status === 'running').length
    const ordinati = [...agenti].sort((a, b) => Number(b.status === 'running') - Number(a.status === 'running'))
    const righe = await Promise.all(
      ordinati.map(async a => {
        const found = await $.session.messages({ agentId: a.id })
        const voci = 'deny' in found ? [] : passi(found)
        const ultima = [...voci].reverse().find(v => v.tipo === 'tool')
        const av = avanzamento(a.status, 'deny' in found ? null : piano(found), stime[a.id])
        return { a, av, ultima: ultima?.tipo === 'tool' ? ultima : null }
      }),
    )
    const chat = avanzamento('running', piano(await $.session.messages()), stime.main)

    const contatori = Svg ? (
      <Box flexDirection="row" flexWrap="wrap" gap={1} alignItems="flex-end">
        {limiti.map(l => (
          <Svg
            source={lancetta(l.percentUsed, FINESTRA[l.kind] ?? l.kind, azzera(l.resetsAt))}
            alt={`${FINESTRA[l.kind] ?? l.kind}: ${l.percentUsed}% usato`}
            width={200}
          />
        ))}
        {uso.cost && <Svg source={rulli(uso.cost.usd)} alt={`Costo della sessione: $${uso.cost.usd.toFixed(2)}`} />}
      </Box>
    ) : (
      <Box flexDirection="column">
        {limiti.map(l => (
          <Text>{`${(FINESTRA[l.kind] ?? l.kind).padEnd(18)} ${barra(l.percentUsed)} ${l.percentUsed}%  ${azzera(l.resetsAt)}`}</Text>
        ))}
        {uso.cost && <Text dimColor>{`Costo della sessione a listino API: $${uso.cost.usd.toFixed(2)}`}</Text>}
      </Box>
    )

    const etichetta = (av: Avanzamento) => (av.pct == null ? av.fonte : `${quanto(av.pct)} · ${av.fonte}`)

    return (
      <Box flexDirection="column">
        <Text bold>Limiti del tuo account</Text>
        {limiti.length === 0 ? (
          <Text dimColor>Nessuna lettura dei limiti ancora: arriva con la prossima risposta del modello.</Text>
        ) : (
          contatori
        )}

        <Box marginTop={1} flexDirection="column">
          <Text bold>{`Agenti: ${lavorano} al lavoro su ${agenti.length}`}</Text>
          {agenti.length === 0 && <Text dimColor>Nessun agente in questa sessione.</Text>}
          {righe.map(({ a, av, ultima }) => (
            <Box flexDirection="column" borderStyle="round" borderDimColor paddingX={1} marginTop={1}>
              <Box flexDirection="row" justifyContent="space-between">
                <Text bold wrap="truncate-end">
                  <Text color={COLORE[a.status] ?? 'gray'}>{PALLINO[a.status] ?? '·'}</Text>
                  {` ${a.name ?? a.type}`}
                  <Text dimColor>{` · ${STATO[a.status] ?? a.status}`}</Text>
                </Text>
                <Button onPress={() => void $.ui.open({ id: DETTAGLIO + a.id, title: a.description.slice(0, 40) })}>
                  Apri
                </Button>
              </Box>
              <Text wrap="truncate-end">
                <Text dimColor>{'Obiettivo  '}</Text>
                {a.description}
              </Text>
              {Svg ? (
                <Svg source={barraSvg(av.pct, TINTA[a.status] ?? '#8a8a8a', etichetta(av))} alt={`${a.description}: ${etichetta(av)}`} />
              ) : (
                <Text>
                  <Text color={TINTA[a.status] ?? 'gray'}>{barra(av.pct ?? 0, 24)}</Text>
                  {` ${etichetta(av)}`}
                </Text>
              )}
              {av.fase ? <Text dimColor wrap="truncate-end">{av.fase}</Text> : null}
              {a.status === 'running' && ultima && (
                <Text dimColor wrap="truncate-end">{`${ultima.finito ? '↳' : '⟳'} ${ultima.tool} · ${ultima.detail}`}</Text>
              )}
            </Box>
          ))}
        </Box>

        <Box marginTop={1} flexDirection="column">
          <Text bold>Compito della chat</Text>
          <Text wrap="wrap">{stime.main?.obiettivo ?? 'Lo ricavo dai tuoi messaggi entro qualche secondo.'}</Text>
          {chat.pct == null ? (
            <Text dimColor>{chat.fonte}</Text>
          ) : Svg ? (
            <Svg source={lancetta(chat.pct, 'compito principale', chat.fonte, true)} alt={`Compito della chat: ${etichetta(chat)}`} width={260} />
          ) : (
            <Text>
              <Text color="#3e8ef7">{barra(chat.pct, 30)}</Text>
              {` ${etichetta(chat)}`}
            </Text>
          )}
          {chat.fase ? <Text dimColor wrap="wrap">{chat.fase}</Text> : null}
        </Box>
      </Box>
    )
  })
}
