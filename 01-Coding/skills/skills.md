---
type: area
updated: 2026-08-28
source: claude
---

# Skill e comandi

Quale strumento di Claude si usa per quale lavoro. Serve a non riscrivere a
mano cose che una skill fa già meglio.

| Quando | Cosa si usa |
|---|---|
| inizio sessione | `/stato` — pull, ultima nota di giornata, otto righe |
| lavoro tecnico | `/nicola` |
| lavoro commerciale | `/patrick` |
| telefonate e liste | `/giulia` |
| un preventivo, una proposta | skill `proposta-commerciale` |
| uno script di vendita, un'apertura | skill `script-vendita` |
| fine giornata | `/chiudi-sessione` |

Le skill del vault stanno in `.claude/skills/`, i comandi in
`.claude/commands/`: sono **versionati**, quindi valgono su ogni macchina.

`TODO` — le skill di frontend installate a livello di account (design,
interfacce) non sono ancora state provate su un progetto vero.
