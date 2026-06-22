# Website Factory — Authorized Records Zone (LOC-ZONE)

**Class:** LOC-ZONE  
**Path:** `workspaces/website-factory-operations/`  
**Authority:** RT-G04 Physical Artifact Specification v1 (DF-03)  
**Created:** 2026-06-07  
**Wave:** 1 complete — Wave 2 complete — Wave 3 complete (C2–C7 proven on FP-0001)  

---

## Purpose

Bounded Factory Source-of-Truth filesystem root. All Factory structured records for Website Factory operations **live in this zone** — not scattered across the MARS monorepo.

**Doctrine remains outside this zone:** `workspaces/website-factory-reference-v1/`

**Production mode (passport SoT):** [FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md](FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md) · charter [website-factory-production-modes-charter-v1.md](../../projects/mars-website-factory/website-factory-production-modes-charter-v1.md) · validation [website-factory-validation-architecture-charter-v1.md](../../projects/mars-website-factory/website-factory-validation-architecture-charter-v1.md)

---

## Portfolio catalog (C4)

**START HERE for registry:** [POC-02-registry-facet/ROC-01-catalog-aggregate.md](POC-02-registry-facet/ROC-01-catalog-aggregate.md)

| Registry ID | Factory Project | LOC-HOME | Discoverability | MOC-01 |
|-------------|-----------------|----------|-----------------|--------|
| REG-0001 | FP-0001 — Triumph Manipulator Landing | [projects/FP-0001-triumph-manipulator-landing/](projects/FP-0001-triumph-manipulator-landing/) | discoverable | [MOC-01](projects/FP-0001-triumph-manipulator-landing/manifest/MOC-01-entry-anchor.md) |

### Visibility-only (not ROC-01 enrolled)

| Factory Project ID | Name | Path | Status |
|--------------------|------|------|--------|
| **FP-0002** | Shpigovsky.ru | [FP-0002-SHPIGOVSKY/](FP-0002-SHPIGOVSKY/) | Foundation material active; **not** catalog-enrolled — operator decision pending (Awareness Alignment 2026-06) |

### Internal agent seeds (not `agents/registry.md` rows)

| Seed ID | Role | Path |
|---------|------|------|
| **AG-WP-001** | Forge WordPress — internal seed (not registered agent); canonical subsystem: [subsystems/forge-wordpress/](../../projects/mars-website-factory/subsystems/forge-wordpress/) | [internal-agent-seeds/AG-WP-001-forge-wordpress/](internal-agent-seeds/AG-WP-001-forge-wordpress/) |

---

## Operator path (Registry → Manifest → Surface)

```text
  README (this file) → ROC-01 → ROC-05 → MOC-01 → SOC-01 → SOC-02…08
```

---

## Wave inventory

| Wave | Scope | Status | Execution record |
|------|-------|--------|------------------|
| Wave 1 | RT-G04 substrate + RT-G10 manifest (FP-0001) | **complete** — C2, C3 | [WAVE-1-PHYSICAL-ARTIFACT-CREATION-EXECUTION-v1.md](WAVE-1-PHYSICAL-ARTIFACT-CREATION-EXECUTION-v1.md) |
| Wave 2 | RT-G05 registry + RT-G04 index scaffold + RT-G12 surface | **complete** — C4, C5 scaffold | [WAVE-2-PHYSICAL-ARTIFACT-CREATION-EXECUTION-v1.md](WAVE-2-PHYSICAL-ARTIFACT-CREATION-EXECUTION-v1.md) |
| Wave 3 | Playbook 03↔04→05 population, POC-06/07/08/10 | **complete** — C6, C7 | [WAVE-3-PHYSICAL-ARTIFACT-CREATION-EXECUTION-v1.md](WAVE-3-PHYSICAL-ARTIFACT-CREATION-EXECUTION-v1.md) |

**Pilot closure:** FP-0001 — **FACTORY_TRACK_CLOSED_PARTIAL** (D-W3-01). See [WAVE-3-PHYSICAL-ARTIFACT-CREATION-EXECUTION-v1.md](WAVE-3-PHYSICAL-ARTIFACT-CREATION-EXECUTION-v1.md).

---

*Human-operated Factory records. No runtime. No automation.*
