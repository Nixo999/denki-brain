---
type: risorsa
updated: 2026-08-28
source: repo
---

# Stack — cosa usiamo e perché

Rilevato dai repo il 28 agosto 2026. Se un progetto cambia stack, si aggiorna
qui **e** si apre una decisione in `05-Decisioni/`.

## Il fondo comune

Presente in tutti i progetti veri:

| Tecnologia | Ruolo |
|---|---|
| **React 19** + **TypeScript** | Interfaccia |
| **Tailwind** | Stile — sempre con **token CSS**, mai colori scritti a mano |
| **Supabase** (Postgres + Auth + RLS) | Database, autenticazione, isolamento dati |
| **zod** + react-hook-form | Validazione |
| **lucide-react** | Icone |
| **sonner** | Notifiche a schermo |
| **date-fns** | Date |
| **exceljs** | Import/export Excel |
| **Capacitor** | Guscio mobile |
| **Netlify** | Hosting |
| **Register** | Domini (~1 €/anno) → [[2026-08-28-domini-a-scadenza]] |

## Dove i due gestionali divergono

⚠️ **Non sono lo stesso stack.** Passare dall'uno all'altro senza accorgersene
è il modo più veloce di scrivere codice che non compila.

| | [[opero]] | [[denkishift]] |
|---|---|---|
| Build | **Vite 8** | **Next.js 16.3.1** (App Router) |
| Tailwind | **3** (config JS) | **4** (config nel CSS) |
| Routing | React Router 7 | App Router, file-based |
| Dati lato client | **TanStack Query 5** | Server Components, niente client cache |
| Scritture | hook → Supabase | **Server Action** (`"use server"`) |
| Capacitor | **6** (Android + iOS) | **8** (solo Android) |
| Lint | **oxlint** | eslint + `eslint-config-next` |
| Test | **nessuno** | `npm run prove`, 132 controlli sui motori puri |
| Commenti | inglese (storico), italiano dal 7 ago | **italiano**, sempre |
| Extra | jsPDF, recharts, pdfjs | papaparse, motion, next-themes, Radix |

⚠️ **Next 16 non è il Next che conosci**: il middleware si chiama `proxy.ts`,
`searchParams` è una Promise. La documentazione vera sta in
`node_modules/next/dist/docs/`.

## I siti vetrina — tre approcci diversi

| Sito | Stack | Nota |
|---|---|---|
| [[sito-albybike]] | SPA React + Vite su Netlify | Online |
| [[cococat]] | **HTML puro**, zero build | Bozza rifiutata. `netlify.toml` con publish `.` |
| [[sito-dropout]] | Generato da **Google AI Studio** | Fermo da maggio 2026 |

> [!note] Analisi di Claude — 2026-08-28
> Tre siti vetrina, tre stack. Per un vantaggio di velocità nel breve, ma il
> conto arriva alla manutenzione: 20 clienti a canone ([[obiettivi-6-mesi]])
> sono 20 siti da aggiornare, e se ognuno è un ambiente diverso il canone
> diventa un costo invece che un ricavo.
>
> Per il prodotto A il candidato giusto è **HTML + Tailwind statico**, come
> cococat: un sito vetrina non ha stato, non ha login, e una SPA React lo rende
> più lento da caricare e più difficile da indicizzare. Ma è una scelta da fare
> apposta, non da subire. Vedi [[2026-08-28-stack-non-uniforme]].

## Cosa non usiamo

`TODO` — non è ancora stato dichiarato niente esplicitamente. Da compilare:
framework, servizi o pratiche escluse per scelta, con il motivo. Serve a Claude
per non proporli.

Quello che si **deduce** dai repo (da confermare):

- **Niente ORM** — si parla a Supabase direttamente
- **Niente dati finti / localStorage come database** (regola esplicita in OperO)
- **Niente colori scritti a mano** nei componenti: solo token CSS
- **Niente password nel codice**, nemmeno per gli account di prova

## Collegamenti

[[convenzioni]] · [[opero]] · [[denkishift]] · [[sito-albybike]] ·
[[2026-08-28-stack-non-uniforme]]
