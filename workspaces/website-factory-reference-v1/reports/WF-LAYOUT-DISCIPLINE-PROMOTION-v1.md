# WF Layout Discipline — Foundation Promotion Report v1

**Версия:** v1  
**Дата:** 2026-06-13  
**Тип:** Anti-regression promotion — documentation only  
**Status:** **MANDATORY** — promoted to Website Factory Foundation

**Rule artefact:** [frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md](../frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md)

**Complements:** [frontend-rules/WF-GRID-DISCIPLINE-v1.md](../frontend-rules/WF-GRID-DISCIPLINE-v1.md) (Container Layer — already promoted)

---

## Origin

| Field | Value |
|-------|-------|
| **Project** | SITE-001 — Автосалон СИБКАР |
| **Context** | WF-V3 prototype development — Layout Authority Review |
| **Discovery phase** | HITL layout audit after Container Layer PASS |
| **Scope** | Not SITE-001-specific; systemic Factory defect |
| **Source review** | [SITE-001-WFV3-LAYOUT-AUTHORITY-REVIEW-v1.md](../../../projects/ocpilot/sites/site-001/reports/SITE-001-WFV3-LAYOUT-AUTHORITY-REVIEW-v1.md) |

### Lesson sources (evidence)

| Source | Path | Role |
|--------|------|------|
| **SITE-001** | `projects/ocpilot/sites/site-001/` | Origin project; layout drift discovery |
| **WF-V3 PDP** | `workspaces/site-001-wf-v3-pdp-prototype/` | PDP hero `65% / 35%` + gap defect; credit `5fr / 7fr` stable |
| **WF-V3 Homepage** | `workspaces/site-001-wf-v3-homepage-prototype/` | Homepage hero `1fr / 42%` — inconsistent with PDP |

---

## Observed failure mode

**Container Layer = PASS** (WF-GRID-DISCIPLINE).  
**Layout Layer = NOT READY** — mixed inner-zone models without Factory authority.

| Zone | Observed model | Drift class |
|------|----------------|-------------|
| PDP Hero | `65%` / `35%` + `40px` gap | **Defective** — % + gap overflow |
| Homepage Hero | `1fr` / `42%` + `40px` gap | **Inconsistent** — ≠ PDP grammar |
| Credit Block | `5fr` / `7fr` | **Stable** — reference L4 |
| Featured Inventory | `repeat(4, 1fr)` | **Stable** — reference L3 |
| Trust Row | flex `flex: 1` | **Acceptable** — normalize to L5 grid |

**Root cause class:** WF-GRID governs section/container/padding; **does not** govern hero split, trust split, finance split, card grid authority, responsive collapse, or zone composition.

**Anti-regression label:** `layout-discipline-failure`

---

## Lesson

### Layout discipline failure

| Symptom | Cause |
|---------|-------|
| Same container, different hero math on PDP vs homepage | No inner-zone authority — per-agent split improvisation |
| `65% / 35%` vs `60% / 40%` vs `1fr 42%` vs `3fr 2fr` across projects | Percentage and hybrid models as default |
| Gallery/offer widths drift when container max or gap changes | `%` tracks + gap arithmetic conflict |
| Credit uses `fr`, hero uses `%`, trust uses flex | No unified Layout Layer grammar |
| Production freeze attempted with desktop-only layout | Missing responsive collapse authority |

**Complement to container lesson:** [WF-GRID-DISCIPLINE-PROMOTION-v1.md](WF-GRID-DISCIPLINE-PROMOTION-v1.md) — outer grid fixed; inner zones remained ad-hoc.

---

## Promotion

| Field | Value |
|-------|-------|
| **Promoted artefact** | `WF-LAYOUT-DISCIPLINE-v1.md` |
| **Location** | `workspaces/website-factory-reference-v1/frontend-rules/` |
| **Authority level** | **Foundation** — default mandatory for all future Website Factory projects |
| **Rule IDs** | WF-LAYOUT-001 … WF-LAYOUT-008 |
| **Promotion type** | Factory-wide foundation rule (anti-regression) |
| **Runtime impact** | **None** — documentation and human-operated QA gates only |

### Why Foundation (not project-local)

Inner-zone drift recurs across page types and stacks:

- PDP hero vs homepage hero
- Card grids vs catalog auto-fill
- Trust strips vs finance modules
- Gulp / OpenCart / WordPress theme work
- Frontend QA / production freeze gates

Project-local fix in SITE-001 alone would not prevent recurrence on SITE-002+ without Factory authority.

---

## Status

| Attribute | Value |
|-----------|-------|
| **Effective** | 2026-06-13 |
| **Mandatory** | Yes — all future Website Factory frontend work |
| **Override** | Operator charter + `WF-LAYOUT-EXCEPTION` marker (WF-LAYOUT-007) only |
| **Automated enforcement** | **NOT IMPLEMENTED** |
| **Frozen layer impact** | None — no modification to Legal Pack, Registry, Blueprint, or Block Registry canon |

---

## Cross-reference updates (this promotion)

| Document | Update |
|----------|--------|
| [DESIGN-SYSTEM-RULES-v1.md](../design-system/DESIGN-SYSTEM-RULES-v1.md) | Pre-Frontend layout discipline pointer |
| [BLUEPRINT-IMPLEMENTATION-RULES-v1.md](../blueprints/BLUEPRINT-IMPLEMENTATION-RULES-v1.md) | Frontend implementation cross-ref |
| [PAGE-IMPLEMENTATION-RULES-v1.md](../page-architecture/PAGE-IMPLEMENTATION-RULES-v1.md) | Layout authority cross-ref |
| [PRODUCTION-QA-CHECKLIST-v1.md](../production-qa/PRODUCTION-QA-CHECKLIST-v1.md) | Handoff / Frontend QA layout gate pointer |
| [PRODUCTION-QA-SYSTEM-v1.md](../production-qa/PRODUCTION-QA-SYSTEM-v1.md) | Handoff readiness + related docs |
| [projects/mars-website-factory/frontend-production-rules-v0.md](../../../projects/mars-website-factory/frontend-production-rules-v0.md) | Consolidated authority pointer |
| [projects/mars-website-factory/frontend-production-invariants-v1.md](../../../projects/mars-website-factory/frontend-production-invariants-v1.md) | Layout discipline cross-ref |
| [agents/frontend-gulp-agent/qa-checklist.md](../../../agents/frontend-gulp-agent/qa-checklist.md) | Inner-zone layout QA rows |

---

## Enforcement surfaces (current)

| Surface | Enforcement mode |
|---------|------------------|
| Gulp Frontend Agent prompts | Human — cite WF-LAYOUT in task / REPORT |
| Frontend QA checklist | Human — layout zone checks + REPORT line |
| Layout authority review | Human — WF-LAYOUT-008 before freeze |
| Production QA handoff | Human — architecture checklist references implementation obligation |
| CI / layout linter | **FUTURE** — not implemented |
| Runtime validator | **NOT IN SCOPE** |

---

## Systems affected

| System | Impact |
|--------|--------|
| Website Factory Foundation | New mandatory frontend authority layer |
| WF-GRID-DISCIPLINE | Unchanged — Container Layer; WF-LAYOUT complements |
| SITE-001 WF-V3 | First candidate reference implementation after chartered iteration |
| Production QA / Frontend QA | New REPORT line and handoff checks |
| Blueprint / Page / Design rules | Cross-reference pointers only |

---

## Future enforcement surfaces

| Surface | Status |
|---------|--------|
| Automated hero `%` track detection | VALIDATION-ROADMAP candidate — not scheduled |
| Inner-zone token lint in Gulp build | **FUTURE** |
| Layout authority review template in Factory | **FUTURE** — WF-LAYOUT-008 manual today |
| Snapshot copies under `snapshots/` | Not updated by default — live canon only |

---

## Remaining gaps

| Gap | Severity | Notes |
|-----|----------|-------|
| SITE-001 prototypes still use pre-authority `%` hero | **Expected** — iteration under charter, not in this promotion |
| Responsive collapse undefined in WF-V3 prototypes | HIGH — WF-LAYOUT-006 blocks production freeze |
| OpenCart / WordPress layout token mapping guide | Low — semantics mandatory; exact names per project |
| WF-LAYOUT in PAGE-BLOCK-VALIDATION layer | Low — structural rule lives in Frontend Foundation |

---

## SITE-001 follow-up (documentation only)

| Question | Answer |
|----------|--------|
| May SITE-001 be corrected under new authority? | **YES** — chartered prototype iteration only |
| Role after correction | **First reference implementation** of WF-LAYOUT-DISCIPLINE |
| Allowed in this promotion pass | Documentation + cross-refs only — **no prototype/CSS changes** |

---

## Promotion sign-off template

```text
promotion_id:   wf-layout-discipline-promotion-v1
origin:         SITE-001 WF-V3 Layout Authority Review
sources:        SITE-001 · WF-V3 PDP · WF-V3 Homepage
rule_ref:       frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md
complements:    frontend-rules/WF-GRID-DISCIPLINE-v1.md
status:         MANDATORY
effective_date: 2026-06-13
runtime_changed: NO
operator:       _______________
```

---

*WF Layout Discipline Promotion v1 — SITE-001 layout lesson promoted to Factory Foundation. Documentation only.*
