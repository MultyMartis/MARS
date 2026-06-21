# SITE-001 — Website Factory Decision v1

**Type:** Design authorization decision — Website Factory  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`

**Inputs:**

- [SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md](SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md)
- [SITE-001-WEBSITE-FACTORY-IMPLEMENTATION-BRIEF-v1.md](SITE-001-WEBSITE-FACTORY-IMPLEMENTATION-BRIEF-v1.md)
- OCPilot reports W2–W3ATMOSPHERE (see design direction §Evidence)
- Operator feedback (task brief 2026-06-09)

---

## Decision

# **READY FOR OCPILOT IMPLEMENTATION**

Website Factory provides **concrete CSS direction**, **selector map**, **token set**, **acceptance checklist (10 criteria, 7/10 pass threshold)**, and **W3WF-01 execution sequence**. OCPilot may proceed to charter + CR + backup + implementation on TEST.

---

## Rationale

### Why READY

| Gate | Status | Evidence |
|------|--------|----------|
| Single visual direction (not 3 options) | **PASS** | «Graphite Salon» — Part 2 of design direction |
| Palette + graphite + red rules defined | **PASS** | `--wf-*` token table + usage rules |
| Surface / depth / card language specified | **PASS** | L1/L2/L2-alt levels + shadow stack |
| CSS-only scope with forbidden properties listed | **PASS** | Implementation brief §5–6 |
| Preserve rules explicit | **PASS** | W3UX-C1, Phase 1, PDP, structure |
| Avoid list from failed waves | **PASS** | W3-C, W3VIS, weak tokens documented |
| Acceptance checklist for operator | **PASS** | 10 criteria, 7/10 threshold |
| OCPilot execution sequence defined | **PASS** | W3WF-01 steps 1–9 |
| Relationship to live W3ATMOSPHERE clarified | **PASS** | W3WF-01 consolidates/refines — not new experiment |

### Why not NOT READY

- Token namespace, selectors, and phases are **executable without interpretation**.
- OCPilot does not need to invent design — brief maps to existing CSS selectors from W3COLOR/W3ATMOSPHERE discovery.

### Why not NEEDS OPERATOR DESIGN REVIEW (blocking)

- Direction **aligns** with operator language (раскраска, тональность, дороже, современнее, красный+тёмный из логотипа).
- W3ATMOSPHERE-01A preview already described same zones — operator intent captured.
- **Non-blocking:** operator may preview charter before sign-off; does not block OCPilot **documentation** readiness.

---

## Authorization matrix

| Action | Status | Owner |
|--------|--------|-------|
| Website Factory design direction | **DONE** | Website Factory |
| Website Factory implementation brief | **DONE** | Website Factory |
| W3WF-01 write charter | **NOT AUTHORIZED** — OCPilot to create | OCPilot |
| W3WF-01 execution on TEST | **NOT AUTHORIZED** — pending charter + CR + backup | OCPilot |
| Operator design sign-off (post-execution) | **PENDING** | Operator |
| Production | **FORBIDDEN** | — |
| Git commit / push | **NOT AUTHORIZED** | — |

---

## Recommended next OCPilot wave

**W3WF-01 — Website Factory Visual Direction Implementation**

1. Charter referencing this decision + implementation brief.
2. CR `CR-SITE-001-W3WF-01-2026-06-09`.
3. Rollback plan T1 (2 CSS files).
4. Backup current `css/main.css` + `css/media.css` (includes W3ATMOSPHERE layer if active).
5. Implement `--wf-*` block per implementation brief.
6. Verify URLs + screenshots.
7. Operator 10-point acceptance checklist.

**Alternative if operator rejects current TEST visuals:**

- T1 rollback to `pre-w3atmosphere-01-20260609-1156` (or latest pre-W3WF backup), then W3WF-01 clean implement.

---

## Risks

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R-WF-01 | W3WF-01 duplicates W3ATMOSPHERE with minimal delta | Low | Brief requires consolidation + Phase H purge; operator checklist detects invisible improvement |
| R-WF-02 | Legacy literals survive override | Medium | Documented in W3ATMOSPHERE N-01; acceptable if visual checklist passes |
| R-WF-03 | Operator expects full rebrand | Medium | Preview sets ~6–7/10 transformation expectation |
| R-WF-04 | W3UX-C1 accidental touch | High | Charter exclusion + verification on `/cars/` |
| R-WF-05 | OCPilot scope creep to PDP hero | High | Brief §6 forbidden + W3VIS rollback reference |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Operator formal sign-off on W3ATMOSPHERE-01 live TEST | **PENDING** — does not block READY FOR IMPLEMENTATION |
| PDP sample URLs on TEST (sparse inventory) | **SAFE UNKNOWN** — category shells suffice per prior waves |
| QA screenshots in git | **LOCAL ONLY** — may be gitignored |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — Decision **READY FOR OCPILOT IMPLEMENTATION** |

*SITE-001 Website Factory Decision v1 — documentation only.*
