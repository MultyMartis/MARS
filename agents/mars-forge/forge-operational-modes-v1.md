# MARS Forge — operational modes (Wave 1)

**Status:** **documented** — **three** operator modes; **Lite is default**.  
**Not:** runtime mode engine; **not** new checklists.

**Parent:** [operational-modes-model.md](../../projects/mars-website-factory/operational-modes-model.md) (full Factory vocabulary — use only when escalated).  
**Foundation map:** [frontend-legacy-and-foundation-map-v0.md](../../governance/frontend-legacy-and-foundation-map-v0.md).

---

## Default rule

**Start in Lite.** Escalate to **Standard** or **Critical** only when triggers below match. **De-escalate** when risk drops — record in REPORT.

---

## Mode matrix

| Mode | When | Mandatory | Optional (open if task needs) |
|------|------|-----------|--------------------------------|
| **Lite** *(default)* | Local edit, one selector/partial, reversible, stable source, narrow blast radius, no freeze/delivery impact. | Foundation: [workflow.md](../frontend-gulp-agent/workflow.md) steps in scope · [frontend-production-rules-v0.md](../../projects/mars-website-factory/frontend-production-rules-v0.md) · Forge [qa-checklist.md](qa-checklist.md) **core slice** (structure, scope, build honesty) · [foundation-lite-checklist.md](foundation-lite-checklist.md) when `data-module` / `foundations/` touched · Compact REPORT | Specialist Forge checklists — **none** unless finding class appears |
| **Standard** | Normal **section slice**: handoff-driven build, responsive + styling + interaction, ordinary production risk. | Lite set + Forge [AGENT.md](AGENT.md) **7 phases** + [workflow.md](workflow.md) + [qa-checklist.md](qa-checklist.md) full overlay pass + foundation [qa-checklist.md](../frontend-gulp-agent/qa-checklist.md) before freeze | **Pick ≤3** specialist checklists tied to handoff (e.g. responsive-intent, design-token, implementation-reliability, cadence) — **not** full catalog |
| **Critical** | Freeze, unfreeze, delivery positioning, source authority dispute, cross-section/global blast, accessibility trust, recovery, or battle-test charter. | Standard set + [semantic-source-lock.md](semantic-source-lock.md) + relevant specialist checks for cited risk + explicit HITL boundary in REPORT | Meta/governance/economics/memory checklists — **only** if charter or REPORT cites them |

---

## Lite — operator expectations

- **Timebox:** one concern per prompt; name `page_slug`, `block_id`, files.
- **Evidence:** build command run **or** SAFE UNKNOWN; no fake PASS.
- **Freeze:** usually **not** in Lite — if freeze touched, **escalate to Standard minimum**.
- **Forbidden in Lite:** reading Forge README checklist table end-to-end; running meta-governance / trust-calibration / organizational-memory checklists “for safety.”

---

## Standard — operator expectations

- **Unit of work:** one **section** (or explicit batch in handoff).
- **Phases:** Structure → Layout → Styling → Responsive → Interaction → QA → Freeze — no silent skips.
- **Findings:** use standard FINDINGS headers from [qa-checklist.md](qa-checklist.md); defer Tier 3 governance prose unless implicated.
- **Freeze:** allowed when QA pass/partial with evidence; record `frozen: true` + file list in REPORT.

---

## Critical — operator expectations

- **Trigger examples:** V3 battle-test charter, production readiness gate, unfreeze of frozen section, global SCSS/token change, contradictory sources, rollback.
- **Evidence:** full relevant proof boundaries; risk weighting stated; HITL for authority conflicts.
- **Checklist cap:** still **targeted** — Critical ≠ “all 30+ checklists.” Use risk-linked lists only.
- **Mode map:** aligns with Factory **freeze-validation**, **recovery/emergency**, **audit/reconstruction** in [operational-modes-model.md](../../projects/mars-website-factory/operational-modes-model.md) — cite which sub-mode in REPORT.

---

## Mandatory vs optional (Forge pack)

| Always (Standard+) | Lite only if applicable | Optional (risk-linked) |
|--------------------|-------------------------|-------------------------|
| foundation workflow + production rules | scoped build check | design-token, cadence, rhythm |
| Forge workflow phases | | responsive-intent, interaction-intent |
| qa-checklist.md overlay | | accessibility-intent, state-consistency |
| foundation qa-checklist.md pre-freeze | | source-interpretation, reconstruction-fidelity |
| semantic-source-lock (Critical) | | human-escalation, qa-confidence |
| REPORT per [reporting-standard-v0.md](../../projects/mars-website-factory/reporting-standard-v0.md) | | production-readiness, temporal-evolution |
| | | meta-governance, trust-calibration, governance-economics, organizational-memory |

---

## Escalation shortcuts

| Signal | Go to |
|--------|-------|
| Touching frozen section | **Standard** minimum; often **Critical** |
| Global variables / shared partial | **Standard** |
| Source PDF vs charter conflict | **Critical** + semantic-source-lock |
| “Quick CSS fix” on landing hero | **Standard** (commercial/first-screen checks) |
| Typo in one local class | **Lite** |

---

## De-escalation

After Critical/Standard work narrows to a local fix with stable evidence → return to **Lite**; note remaining freeze constraints in REPORT.

---

*Wave 1 Forge simplification — checklist fatigue reduction; does not delete existing checklists.*
