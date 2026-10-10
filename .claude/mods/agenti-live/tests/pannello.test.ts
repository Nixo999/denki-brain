import { expect, test } from 'claude-code/testing'

// Due agenti finti: uno finito, uno con un piano a metà. La chat ha una stima già fatta.
const AGENTI = [
  { id: 'a1', description: 'Rifà il footer', type: 'operatore', status: 'completed' },
  { id: 'a2', description: 'Controlla i prezzi', type: 'operatore', status: 'running' },
]
const todo = (status: string, content: string) => ({ status, content, activeForm: `${content} in corso` })
const MESSAGGI: Record<string, unknown[]> = {
  a1: [{ role: 'user', text: 'rifai il footer', toolUses: [] }],
  a2: [
    { role: 'user', text: 'controlla i prezzi', toolUses: [] },
    {
      role: 'assistant',
      text: '',
      toolUses: [{ tool: 'TodoWrite', input: { todos: [todo('completed', 'Leggo il listino'), todo('in_progress', 'Confronto i prezzi')] }, result: 'ok' }],
    },
  ],
}
const STIME = { main: { pct: 40, fase: 'agenti al lavoro', obiettivo: 'Rifare il pannello degli agenti', passi: 3, quando: Date.now() } }

for (const surface of ['terminal', 'desktop'] as const) {
  test(`pannello agenti su ${surface}`, async ($, on) => {
    on('agent.list', async () => ({ value: AGENTI }) as never)
    on('session.messages', async (_$, e) => ({ value: e.agentId ? MESSAGGI[e.agentId] : MESSAGGI.a1 }) as never)
    on('session.usage', async () => ({ value: { startedAt: 0, context: {}, rateLimits: [] } }) as never)
    on('state.get', async (_$, e) => ({ value: { value: e.key === 'stime' ? STIME : 0, version: 1 } }) as never)

    const ui = await $.ui.mount({ plugin: 'agenti-live', surface, component: 'Pane', props: {}, requestId: 'agenti', viewport: { columns: 120, rows: 60 } } as never)
    const testi = (await ui.findAll({})).map(el => el.text).join('\n')
    const svg = (await ui.findAll({ type: 'Svg' })).map(el => String(el.props.alt)).join('\n')
    const tutto = `${testi}\n${svg}`

    expect(tutto).toContain('Agenti: 1 al lavoro su 2')
    expect(tutto).toContain('Rifà il footer')
    expect(tutto).toContain('100% · finito')
    expect(tutto).toContain('50% · piano 1/2')
    expect(tutto).toContain('Confronto i prezzi in corso')
    expect(tutto).toContain('Rifare il pannello degli agenti')
    expect(tutto).toContain('40% · stima')
  })
}
