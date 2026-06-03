# GitGuard Cross-Link Alignment v1

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 2A  
**Upstream:** [gitguard-deep-review-v2.md](../discoveries/gitguard-deep-review-v2.md), Wave 2 Discovery W2-A07  
**Charter:** Navigation only — **no** new architecture, **no** `project_id`, **no** `projects/gitguard/` pack.

---

## Problem

GitGuard appeared in **three conflicting postures**:

| Surface | Prior posture |
|---------|---------------|
| `system-entity-model.md` | Program example (GitGuard named) |
| `mars-reality-index-v0.md` | conceptual + **UNKNOWN** external |
| `ecosystem-topology-index.md` | SAFE UNKNOWN — “no pack” |

Survivability pack (`projects/mars-survivability/`) already documents GitGuard entry, contracts, and human-operated tools — discoverability gap, not missing implementation class.

---

## Actions taken

| File | Change |
|------|--------|
| `governance/system-entity-model.md` | Cross-References → reality index, operational-survivability, `gitguard-system-entry-v1.md` |
| `governance/mars-reality-index-v0.md` | GitGuard section + quick matrix → **operational** via mars-survivability; clarifies not separate `project_id` |
| `governance/ecosystem-topology-index.md` | GitGuard § rewritten — survivability framework, links to entry + reality index |

**Not done:** REGISTER GitGuard as `project_id`; CREATE `projects/gitguard/`; deploy hooks (G3+).

---

## Operator decisions still deferred

| ID | Question |
|----|----------|
| G-01 | Promote GitGuard to own `project_id` row? |
| G-03 | Charter G3+ Cursor hooks pilot |
| G-04 | First `rollback-map.json` under future pack path |

---

## Files changed

- `governance/system-entity-model.md`
- `governance/mars-reality-index-v0.md`
- `governance/ecosystem-topology-index.md`

---

*GitGuard cross-link alignment v1 — Wave 2A evidence.*
