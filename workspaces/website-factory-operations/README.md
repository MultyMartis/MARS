# Website Factory — Authorized Records Zone (LOC-ZONE)

**Class:** LOC-ZONE  
**Path:** `workspaces/website-factory-operations/`  
**Authority:** RT-G04 Physical Artifact Specification v1 (DF-03)  
**Created:** 2026-06-07  
**Wave:** 1 complete — Wave 2 complete (C4 + C5 scaffold)  

---

## Purpose

Bounded Factory Source-of-Truth filesystem root. All Factory structured records for Website Factory operations **live in this zone** — not scattered across the MARS monorepo.

**Doctrine remains outside this zone:** `workspaces/website-factory-reference-v1/`

---

## Portfolio catalog (C4)

**START HERE for registry:** [POC-02-registry-facet/ROC-01-catalog-aggregate.md](POC-02-registry-facet/ROC-01-catalog-aggregate.md)

| Registry ID | Factory Project | LOC-HOME | Discoverability | MOC-01 |
|-------------|-----------------|----------|-----------------|--------|
| REG-0001 | FP-0001 — Triumph Manipulator Landing | [projects/FP-0001-triumph-manipulator-landing/](projects/FP-0001-triumph-manipulator-landing/) | discoverable | [MOC-01](projects/FP-0001-triumph-manipulator-landing/manifest/MOC-01-entry-anchor.md) |

---

## Operator path (Registry → Manifest → Surface)

```text
  README (this file) → ROC-01 → ROC-05 → MOC-01 → SOC-01 → SOC-02…08
```

---

## Wave inventory

| Wave | Scope | Status |
|------|-------|--------|
| Wave 1 | RT-G04 substrate + RT-G10 manifest (FP-0001) | **complete** — C2, C3 |
| Wave 2 | RT-G05 registry + RT-G04 index scaffold + RT-G12 surface | **complete** — C4, C5 scaffold |
| Wave 3 | Playbook 04/05 population, POC-06/07/08/10 | **not started** — C6, C7 |

**Deferred (Wave 3+):** POC-06, POC-07, POC-08, POC-10 population; Playbook 04/05 acts.

---

*Human-operated Factory records. No runtime. No automation.*
