# WF Grid Discipline — Foundation Promotion Report v1

**Версия:** v1  
**Дата:** 2026-06-13  
**Тип:** Anti-regression promotion — documentation only  
**Status:** **MANDATORY** — promoted to Website Factory Foundation

**Rule artefact:** [frontend-rules/WF-GRID-DISCIPLINE-v1.md](../frontend-rules/WF-GRID-DISCIPLINE-v1.md)

---

## Origin

| Field | Value |
|-------|-------|
| **Project** | SITE-001 — Автосалон СИБКАР |
| **Context** | WF-V3 prototype development (Website Factory visual layer) |
| **Discovery phase** | Implementation / visual QA — horizontal rhythm audit |
| **Scope** | Not SITE-001-specific; systemic Factory defect |

### Observed failure mode

Content **sections** and **containers** were conflated in markup:

```html
<!-- BAD — observed pattern -->
<section class="wf-v3-container">
```

```html
<nav class="wf-v3-container">
```

Instead of required separation:

```html
<!-- GOOD -->
<section class="wf-v3-section">
    <div class="wf-v3-container">
        ...
    </div>
</section>
```

---

## Lesson

### Container discipline failure

| Symptom | Cause |
|---------|-------|
| Inconsistent visual widths across sections | Container class applied to section semantic elements |
| Broken horizontal rhythm | No single inner grid wrapper per section |
| Sections wider/narrower than header | Header and body used different width authority models |
| Design quality degradation despite good visual design | Layout structure defect, not token/color defect |

**Root cause class:** structural HTML/CSS role confusion — **section shell vs content container**.

**Anti-regression label:** `container-discipline-failure`

---

## Promotion

| Field | Value |
|-------|-------|
| **Promoted artefact** | `WF-GRID-DISCIPLINE-v1.md` |
| **Location** | `workspaces/website-factory-reference-v1/frontend-rules/` |
| **Authority level** | **Foundation** — default mandatory for all future Website Factory projects |
| **Rule IDs** | WF-GRID-001 … WF-GRID-005 |
| **Promotion type** | Factory-wide foundation rule (anti-regression) |
| **Runtime impact** | **None** — documentation and human-operated QA gates only |

### Why Foundation (not project-local)

The defect recurred across page types and stacks:

- Homepage generation
- PDP generation
- Catalog generation
- Corporate sites
- Landing pages
- WordPress / OpenCart theme work
- Gulp Frontend Agent output
- Frontend QA / Design QA workflows

Project-local fix in SITE-001 alone would not prevent recurrence on SITE-002+.

---

## Status

| Attribute | Value |
|-----------|-------|
| **Effective** | 2026-06-13 |
| **Mandatory** | Yes — all future Website Factory frontend work |
| **Override** | Operator charter + documented exception (WF-GRID-003 marker) only |
| **Automated enforcement** | **NOT IMPLEMENTED** |
| **Frozen layer impact** | None — no modification to Legal Pack, Registry, Blueprint, or Block Registry canon |

---

## Cross-reference updates (this promotion)

| Document | Update |
|----------|--------|
| [DESIGN-SYSTEM-RULES-v1.md](../design-system/DESIGN-SYSTEM-RULES-v1.md) | Pre-Frontend grid discipline pointer |
| [BLUEPRINT-IMPLEMENTATION-RULES-v1.md](../blueprints/BLUEPRINT-IMPLEMENTATION-RULES-v1.md) | Frontend implementation cross-ref |
| [BLOCK-IMPLEMENTATION-RULES-v1.md](../block-registry/BLOCK-IMPLEMENTATION-RULES-v1.md) | Design & Frontend boundaries cross-ref |
| [PRODUCTION-QA-CHECKLIST-v1.md](../production-qa/PRODUCTION-QA-CHECKLIST-v1.md) | Handoff / Frontend QA grid gate pointer |
| [ARCHITECTURE-FOUNDATION-v1.md](../ARCHITECTURE-FOUNDATION-v1.md) | Lessons learned entry |
| [projects/mars-website-factory/frontend-production-rules-v0.md](../../../projects/mars-website-factory/frontend-production-rules-v0.md) | Consolidated authority pointer |
| [projects/mars-website-factory/frontend-production-invariants-v1.md](../../../projects/mars-website-factory/frontend-production-invariants-v1.md) | Container discipline cross-ref |
| [projects/mars-website-factory/foundation-systems/README.md](../../../projects/mars-website-factory/foundation-systems/README.md) | Systems map entry |
| [agents/frontend-gulp-agent/qa-checklist.md](../../../agents/frontend-gulp-agent/qa-checklist.md) | Grid alignment QA rows |
| [README.md](../README.md) | Frontend rules index |

---

## Enforcement surfaces (current)

| Surface | Enforcement mode |
|---------|------------------|
| Gulp Frontend Agent prompts | Human — cite WF-GRID in task / REPORT |
| Frontend QA checklist | Human — WF-GRID-005 alignment checks |
| Design QA / visual approval | Human — grid fail blocks visual PASS |
| Production QA handoff | Human — architecture checklist references implementation obligation |
| CI / DOM linter | **FUTURE** — not implemented |
| Runtime validator | **NOT IN SCOPE** |

---

## Remaining gaps

| Gap | Severity | Notes |
|-----|----------|-------|
| Automated section/container DOM audit | Medium | VALIDATION-ROADMAP candidate — not scheduled |
| Reference workspace `src/` audit against WF-GRID-001 | Low | LANDING golden pattern may predate rule; separate hygiene pass |
| OpenCart / WordPress class name mapping guide | Low | Semantics mandatory; exact BEM → per-project |
| WF-GRID in PAGE-BLOCK-VALIDATION layer | Low | Structural rule lives in Frontend Foundation, not block validation v1 |
| Snapshot copies under `snapshots/` | Low | Not updated by default — live canon only |

---

## Promotion sign-off template

```text
promotion_id:   wf-grid-discipline-promotion-v1
origin:         SITE-001 WF-V3
rule_ref:       frontend-rules/WF-GRID-DISCIPLINE-v1.md
status:         MANDATORY
effective_date: 2026-06-13
runtime_changed: NO
operator:       _______________
```

---

*WF Grid Discipline Promotion v1 — SITE-001 lesson promoted to Factory Foundation. Documentation only.*
