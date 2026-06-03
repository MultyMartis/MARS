# GitGuard Registration v1

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 2B  
**Upstream:** [gitguard-deep-review-v2.md](../discoveries/gitguard-deep-review-v2.md), Wave 2A [gitguard-crosslink-alignment-v1.md](gitguard-crosslink-alignment-v1.md)  
**Architect decision:** GitGuard = **KEEP** + **REGISTER** (Repository Survivability Layer)

---

## Registration posture

| Field | Value |
|-------|-------|
| **Entity** | GitGuard |
| **Classification** | **REGISTERED** cross-cutting survivability concept |
| **Role** | **Repository Survivability Layer** |
| **Implementation home** | `projects/mars-survivability/` (human-operated advisory + CLI helpers) |
| **`project_id` row** | **No** — avoids `project_id` inflation |
| **`projects/gitguard/` pack** | **No** — not evidenced; not created |

---

## Responsibilities (documented only)

| Responsibility | Reality in repo |
|----------------|-----------------|
| Checkpoint visibility | GIT CHECKPOINT signals ([system-signals-dictionary.md](../../governance/system-signals-dictionary.md)); snapshot manifests; program freeze folders |
| Freeze visibility | ORCA/Factory freeze discipline; protected zones registry |
| Rollback visibility | Rollback map schema, `logs/rollback-history/`, drill reports |
| Baseline visibility | Release evidence (`logs/releases/`); baseline exclusions in stable baseline pack |
| Backup intelligence | Snapshot helper, manifest conventions — **human-invoked** |
| Release traceability | Cross-links to lifecycle + release trails; observability linters |

**Not:** autonomous backup service, Cursor hooks (G3+ **planned**), or runtime enforcement engine.

---

## Actions taken

| Surface | Change |
|---------|--------|
| `registry/project-registry.md` | GitGuard **REGISTERED** cross-cutting note (replaces SAFE UNKNOWN deferral) |
| `governance/ecosystem-topology-index.md` | GitGuard § — registered role; MARS Survivability § — GitGuard implemented via pack |
| `governance/mars-reality-index-v0.md` | GitGuard § — registered survivability layer |
| `governance/external-systems-relationship-map-v0.md` | GitGuard row — mars-survivability ownership |
| `governance/canonical-terminology-registry.md` | GitGuard term entry |
| `projects/mars-survivability/registries/gitguard-system-entry-v1.md` | Wave 2B registration banner |
| `projects/mars-survivability/README.md` | GitGuard registration cross-link |

**Not done:** G-01 separate `project_id`; G-03 hooks pilot; G-04 `projects/gitguard/rollback-map.json`.

---

## Files changed

- `registry/project-registry.md`
- `governance/ecosystem-topology-index.md`
- `governance/mars-reality-index-v0.md`
- `governance/external-systems-relationship-map-v0.md`
- `governance/canonical-terminology-registry.md`
- `projects/mars-survivability/registries/gitguard-system-entry-v1.md`
- `projects/mars-survivability/README.md`

---

*GitGuard registration v1 — Wave 2B evidence. Documentation only; no runtime.*
