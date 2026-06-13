# Website Factory — frontend operator quickstart (Wave 1)

**Status:** **documented** — **one** entry for Lane B frontend work.  
**Not:** full pack index; **not** governance catalog.

**Replaces for onboarding:** breadth-first README Pack index + scattered Forge README reads.

---

## Open first (≤5 minutes)

| Order | Open | Why |
|-------|------|-----|
| 1 | [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Tier 2 — pick **one** Core Run row |
| 2 | This file | SoT, workspace, Forge default, flow |
| 3 | [wave1-operational-entity-map-v1.md](wave1-operational-entity-map-v1.md) | Term confusion only |
| 4 | [agents/frontend-gulp-agent/README.md](../../agents/frontend-gulp-agent/README.md) | Foundation SoT |
| 5 | Handoff for your page | Scope truth |

**Do not** open: full `*-governance.md` list, Forge README checklist table, `web-gpt-sources/` for new work.

---

## What is SoT

**Authority order (read first for conflicts):** [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) — (1) Project Production Standards → (2) Approved Operator Laws → (3) Factory Governance → (4) Layout Pattern Library → (5) Industry Best Practice → (6) Agent Preference.

| Topic | Source of truth |
|-------|-----------------|
| **Decision hierarchy** | [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) |
| Build rules (src, dist, includes) | [frontend-production-rules-v0.md](frontend-production-rules-v0.md) + [agents/frontend-gulp-agent/](../frontend-gulp-agent/) |
| Operator Laws (spacing, layout, type) | [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) §3 (OL-01–OL-07); detail in [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) |
| Page scope | Frontend handoff instance + active design `vN` |
| Phases / freeze | [agents/mars-forge/AGENT.md](../../agents/mars-forge/AGENT.md) + [forge-operational-modes-v1.md](../../agents/mars-forge/forge-operational-modes-v1.md) |
| Session outcome | **REPORT** in repo — not chat |
| Physical files | **Workspace** path operator states — **SAFE UNKNOWN** until confirmed |

---

## Where implementation lives

- **Documentation (Lane B):** `projects/mars-website-factory/`, `agents/frontend-gulp-agent/`, `agents/mars-forge/`
- **Real code (Lane A):** `workspaces/<project>/` (or external gulp-starter) — operator opens in IDE
- **MARS repo:** **no** claim that `gulp build` runs here without evidence in that workspace

---

## When to use Forge

| Use Forge | Skip Forge (foundation only) |
|-----------|------------------------------|
| Section build through freeze | Trivial one-line fix in Lite |
| Overlay QA and phase discipline | Docs-only task |
| Commercial landing slice | Pure planning / blueprint authoring |
| Battle test or charter-driven rebuild | |

**Default Forge mode:** **Lite** — see [forge-operational-modes-v1.md](../../agents/mars-forge/forge-operational-modes-v1.md).

---

## Minimal operational flow

0. **Greenfield site** — Production Standards Draft → Mapping QA → Approval → Shell → Visual Foundation → Design Calibration → Foundation QA before Home ([production-standards-governance-v1.md](production-standards-governance-v1.md) · [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) · [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md)). **Layout law:** [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) · [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md). **Precision law:** [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md).
1. **Charter** — state `page_slug`, `block_id`, workspace path, active design version.
2. **Mode** — Lite (default) → Standard (section) → Critical (freeze/source/delivery).
3. **Read** — handoff + foundation workflow step for current phase only.
4. **Implement** — `src/` only; scoped partials; no silent structure invention.
5. **Validate** — build or SAFE UNKNOWN; mode-appropriate checklists. **Page Production PASS:** Design Completeness → Frontend Design QA Matrix → Pixel Fidelity → [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §6.
6. **Report** — `# REPORT — …` per [reporting-standard-v0.md](reporting-standard-v0.md): scope, files, findings, freeze state.
7. **Freeze** — Standard+ when PASS; unfreeze needs reason — [section-replacement-contract-v1.md](section-replacement-contract-v1.md).

---

## REPORT expectations

- Heading: `# REPORT — <task>`
- Scope: page, block, files touched, mode (Lite/Standard/Critical)
- Evidence: commands run or SAFE UNKNOWN
- Findings: use Forge/foundation FINDINGS headers when applicable
- Freeze: `frozen: true|false` + unfreeze reason if changed
- **No** runtime/orchestration claims

---

## Workspace execution reality

- You edit **external** `src/`; MARS docs do not auto-sync to disk.
- **`dist/`** is generated — **never** hand-edit for delivery fix.
- PowerShell/UTF-8: follow [terminal-survivability-governance.md](terminal-survivability-governance.md) when shell issues appear.
- Chat memory **is not** SoT — re-read handoff after long sessions.

---

## Forbidden paths

| Forbidden | Why |
|-----------|-----|
| `dist/` manual patches | Breaks reproducibility |
| Archived design `v*` as active authority | Version drift |
| `web-gpt-sources` as SoT for new frontend | Legacy import |
| Full Forge checklist catalog per session | Fatigue / drift |
| Claiming MARS runtime executed the build | No orchestration in repo |
| Governance expansion without charter | Post–Cycle 8 maintenance mode |

---

## Next depth (on demand)

| Task | Doc |
|------|-----|
| Greenfield foundation sequence | [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) · [production-standards-governance-v1.md](production-standards-governance-v1.md) · [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) · [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) · [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) · [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) · [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) |
| WF-GRID / WF-LAYOUT layout law | [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) · [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) · [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md) |
| Design Completeness + Production PASS | [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) · [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) · [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) |
| Replace / swap section | [section-replacement-contract-v1.md](section-replacement-contract-v1.md) |
| Topology | [wave1-operational-topology-v1.md](wave1-operational-topology-v1.md) |
| Shared tokens/forms/modals/JS | [foundation-systems/README.md](foundation-systems/README.md) (Wave 2) |
| Reference implementation | [workspaces/website-factory-reference-v1/](../../workspaces/website-factory-reference-v1/) (Wave 3–4) |
| Wave 4 onboarding path | [onboarding-flow-v1.md](onboarding-flow-v1.md) |
| Adoption / REPORT examples | [foundation-adoption-charter-v1.md](foundation-adoption-charter-v1.md) · [operational-examples/golden-report-examples-v1.md](operational-examples/golden-report-examples-v1.md) |
| Blueprint roadmap | [frontend-foundation-blueprint-v1.md](frontend-foundation-blueprint-v1.md) |
| First formal run | [first-operational-runbook-v0.md](first-operational-runbook-v0.md) |

---

*Wave 1 — operator entry simplification.*
