# Website Factory — Wave 1 operational entity map

**Status:** **documented** — compact operator vocabulary for Lane B frontend work.  
**Not:** runtime schema, registry engine, or new governance philosophy.

**Wave:** Website Factory Operational Wave 1 (2026-05-20).  
**Topology:** [wave1-operational-topology-v1.md](wave1-operational-topology-v1.md).

---

## How to use

Read this map when a term is ambiguous. **One sentence per entity** — open linked docs only when the task needs depth.

---

## Systems and roles

| Entity | Definition | Relationship |
|--------|------------|--------------|
| **Website Factory** | MARS **operational system** (`mars-website-factory`): methodology, contracts, registries, handoffs, QA semantics for commercial static sites. | **Contains** agent packs, workflows, reference cases; **does not** execute Gulp in-repo. |
| **Forge** | **Overlay** on `gulp_frontend_agent` — phased pipeline, freeze discipline, overlay QA. **Not** parallel SoT. | **Extends** foundation; if silent, foundation wins. Modes: [forge-operational-modes-v1.md](../../agents/mars-forge/forge-operational-modes-v1.md). |
| **frontend-gulp-agent** | **Canonical foundation** SoT for Gulp/include/SCSS/JS production rules (`agents/frontend-gulp-agent/`). | **Parent** of Forge; **pairs** with Factory contracts. |
| **governance layer** | Factory **methodology docs** (`*-governance.md`, drift taxonomies) — human-supervised intent, **not** automated policy. | **Tier 3** on demand; **not** default session read post–Cycle 8. |
| **execution surface** | Where work runs: **operator machine** + **Cursor session** + **external workspace** (`workspaces/*`). | **Not** MARS runtime; chat is **not** SoT. |

---

## Execution locus

| Entity | Definition | Relationship |
|--------|------------|--------------|
| **workspace** | **Lane A** project tree with real `src/`, `gulpfile`, build output — opened by operator outside governance SoT. | Factory/Forge define **how**; workspace is **where**. |
| **foundation** | Combined **gulp pack + Factory production rules + handoff** — default law for implementation. | Forge **inherits**; does not replace. |
| **overlay** | Forge-only **additions** (phases, freeze, specialist checklists). | **Thin** layer on foundation. |
| **legacy** | Web-GPT imports, old briefs, archived design versions — **context only**. | **Never** SoT for new work. |
| **planned systems** | Future runtime, WPilot bridge, automated validators — **documented direction only**. | **No** implementation claim without repo evidence. |

---

## Contracts and artifacts

| Entity | Definition | Relationship |
|--------|------------|--------------|
| **contract** | Named **fielded obligation** between stages (handoff, blueprint, design pack). Markdown-first; **not** enforced API. | **Binds** scope; violations → REPORT + HITL. |
| **registry** | Stable **ID tables** (`block_id`, `site_type_id`) for planning and blueprints. | **Informs** composition; **not** component library code. |
| **block** | Registry **row** — reusable section **role** with SEO/conversion/UX semantics. | Maps to **section** in implementation; may be one partial. |
| **section** | **Page slice** under implementation — DOM + SCSS partial + optional JS; **freeze unit** for Forge. | **Instance** of `block_id` (or ad hoc with gap noted). |
| **partial** | Gulp **include fragment** (HTML/SCSS) — composes pages. | **Owned** by section scope when section-scoped. |
| **component** | **Reusable UI unit** (markup + styles + behavior hooks) inside or across sections. | Prefer **data-* hooks**; avoid global pollution. |
| **implementation pack** | Versioned **design law** (`semantics/` + `implementation-pack/`) for faithful build. | **Canonical** for active `vN` only. |
| **operational pack** | Bounded doc set for one concern (agent pack, checklist cluster). | **Read selectively** — not full catalog per session. |
| **blueprint** | **Page orchestration** artifact — blocks, order, constraints for a route. | **Upstream** of handoff. |
| **handoff** | **Frontend Handoff Contract** instance — files, breakpoints, `block_id`, freeze target. | **Downstream** of blueprint/design. |
| **reference case** | **Documented example run** (e.g. Triumph doc simulation) — lessons, **not** production proof. | **Informs** mode selection; **not** live site SoT. |
| **execution case** | **Registered client delivery** under Factory lane (e.g. `isbd-care-landing`) — live workspace + freeze. | SoT: [execution-cases-registry-v1.md](execution-cases-registry-v1.md); **not** default `project_id`. |
| **checklist** | Human **verification list** (foundation QA, Forge overlay, page QA). | **Mode-dependent** mandatory set — see Forge modes. |
| **runbook** | **Ordered operator steps** for a recurring task (first run, workflow). | **Core Run** entry for process. |

---

## Process nouns

| Entity | Definition | Relationship |
|--------|------------|--------------|
| **methodology** | Factory **preferred ways** (cadence, tokens, commercial density, interaction intent). | **Guides** implementation; Tier 3 depth optional. |
| **implementation** | **src-first** HTML/SCSS/JS in workspace — build to `dist/`, no hand-edits. | **Subject** of freeze and [section-replacement-contract-v1.md](section-replacement-contract-v1.md). |
| **freeze / unfreeze** | **Section lock** after QA — edits need recorded reason. | See section contract + Forge `AGENT.md`. |
| **REPORT** | Session **artifact** with scope, evidence, findings, freeze state — **committed** truth over chat. | [reporting-standard-v0.md](reporting-standard-v0.md). |

---

## Quick SoT matrix

| Question | SoT |
|----------|-----|
| How to build (includes, dist rule)? | `frontend-gulp-agent` + [frontend-production-rules-v0.md](frontend-production-rules-v0.md) |
| What to build (scope, block)? | Handoff instance + active design `vN` |
| Phases / freeze / overlay QA? | Forge `AGENT.md` + [forge-operational-modes-v1.md](../../agents/mars-forge/forge-operational-modes-v1.md) |
| Where files live? | **Workspace** (operator opens) — **SAFE UNKNOWN** until path stated |
| Session memory? | **Not** SoT — REPORT + repo docs |

---

*Wave 1 — entity normalization only; no new registry rows.*
