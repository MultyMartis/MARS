# Forge WordPress — Ecosystem Position v1

**Document type:** Ecosystem relationship map  
**Version:** v1  
**Date:** 2026-06-22  
**Lifecycle:** FOUNDATION

---

## Proven pipeline boundary

```text
Website Factory
    → approved frontend package
Forge WordPress
    → WordPress implementation package
WPilot
    → controlled WordPress operations
```

Human is final authority at each transition. Autonomous handoff and production deployment are **excluded**.

---

## Relationship matrix

### Website Factory

| Aspect | Status |
|--------|--------|
| **Actual relationship** | **Parent program pack** (`mars-website-factory`). Forge WordPress is a **subsystem**, not a separate `project_id`. |
| **Upstream artifact** | Approved frontend package from Factory production/validation chain (VL0–VL6, production modes, QA gates — Factory docs). |
| **Non-relationship** | Forge WordPress does **not** own intake, strategy, IA, design creation, or static frontend implementation. |

**SoT:** [projects/mars-website-factory/OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md)

---

### Gulp Frontend Agent

| Aspect | Status |
|--------|--------|
| **Actual relationship** | **Upstream implementation lane** within Website Factory. Produces static HTML/SCSS/JS deliverables Forge WordPress may later consume. |
| **Non-relationship** | Gulp Frontend Agent is **not** part of Forge WordPress; no WordPress implementation role. |

**SoT:** [agents/frontend-gulp-agent/README.md](../../../../agents/frontend-gulp-agent/README.md)

---

### MARS Forge (frontend overlay)

| Aspect | Status |
|--------|--------|
| **Actual relationship** | **None** — different entity, different domain. |
| **Non-relationship** | MARS Forge is a **thin overlay** on Gulp foundation for frontend discipline. **Not** Forge WordPress. **Not** WordPress implementation. |
| **Naming risk** | Operator alias **WP Forge** must not be conflated with **MARS Forge**. |

**SoT:** [agents/mars-forge/README.md](../../../../agents/mars-forge/README.md) · [governance/frontend-legacy-and-foundation-map-v0.md](../../../../governance/frontend-legacy-and-foundation-map-v0.md)

---

### WPilot

| Aspect | Status |
|--------|--------|
| **Actual relationship** | **Downstream operations** — controlled WordPress administration on existing sites; reference CMS Pilot runtime (RC5 proven on DEV). |
| **Handoff direction** | Forge WordPress → implementation package → WPilot for **controlled operations** (not development). |
| **Non-relationship** | WPilot does **not** replace theme/plugin development, ACF architecture, or frontend-to-WordPress transformation. |
| **Strategic note** | WPilot docs describe **Factory-native WordPress** as preferred long-term target — alignment **planned**, handoff contract **SAFE UNKNOWN** until Phase 1. |

**SoT:** [projects/wpilot/OPERATIONAL-INDEX.md](../../../wpilot/OPERATIONAL-INDEX.md) · seed [AG-WP-001-WPILOT-CONNECTION.md](../../../../workspaces/website-factory-operations/internal-agent-seeds/AG-WP-001-forge-wordpress/AG-WP-001-WPILOT-CONNECTION.md)

---

### OCPilot

| Aspect | Status |
|--------|--------|
| **Actual relationship** | **Sibling CMS Pilot** (OpenCart/ocStore) — External Systems lane. |
| **Non-relationship** | No shared implementation scope. Forge WordPress does **not** own ecommerce CMS operations covered by OCPilot. |

**SoT:** [projects/ocpilot/README.md](../../../ocpilot/README.md)

---

### ATLAS

| Aspect | Status |
|--------|--------|
| **Actual relationship** | **SAFE UNKNOWN** for direct consumption — ATLAS is Business Reality Registry (documentation population). Factory LOC-ZONE pilots may bind ATLAS ids where attested (e.g. FP-0001/FP-0002). |
| **Non-relationship** | Forge WordPress does **not** own canonical business identity. |
| **Future** | May reference attested org/project/website records for pilot context — **not** defined at FOUNDATION. |

**SoT:** [projects/atlas/foundation/ATLAS-REALITY-MODEL-v1.md](../../../atlas/foundation/ATLAS-REALITY-MODEL-v1.md)

---

### OPS

| Aspect | Status |
|--------|--------|
| **Actual relationship** | **No direct relationship** at FOUNDATION. |
| **Non-relationship** | OPS is Business Operations Domain — reporting, approvals, deadlines. Not WordPress implementation. |
| **Future** | **SAFE UNKNOWN** — operational workflows may surface Factory delivery status; not chartered here. |

**SoT:** [projects/ops/README.md](../../../ops/README.md)

---

### GitGuard

| Aspect | Status |
|--------|--------|
| **Actual relationship** | **Cross-cutting survivability patterns** — checkpoint, freeze, rollback visibility may apply to future WordPress implementation repos. |
| **Non-relationship** | GitGuard is **not** a WordPress subsystem; no autonomous enforcement. |

**SoT:** [projects/mars-survivability/registries/gitguard-system-entry-v1.md](../../../mars-survivability/registries/gitguard-system-entry-v1.md)

---

### LOC-ZONE (`website-factory-operations/`)

| Aspect | Status |
|--------|--------|
| **Actual relationship** | **Physical records plane** for Factory operations. Hosts **AG-WP-001** internal seed and pilot folders (FP-0001, FP-0002). |
| **Non-relationship** | LOC-ZONE is **not** the canonical methodology home — subsystem docs live under `projects/mars-website-factory/subsystems/forge-wordpress/`. |

**SoT:** [workspaces/website-factory-operations/README.md](../../../../workspaces/website-factory-operations/README.md)

---

### FP-0002 — Shpigovsky.ru

| Aspect | Status |
|--------|--------|
| **Actual relationship** | **First probable pilot** and learning context referenced by AG-WP-001 seed. Foundation material active in LOC-ZONE. |
| **Non-relationship** | WordPress implementation **NOT STARTED**. Frontend work in Factory lane is **separate** — Forge WordPress must not modify FP-0002 frontend in FW-00. |
| **Status** | Visibility-only in ROC-01; catalog enrollment **operator decision pending**. |

**SoT:** [workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/](../../../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/)

---

## Anti-confusion rules

1. **MARS Forge ≠ Forge WordPress** — frontend overlay vs WordPress implementation subsystem.
2. **Forge WordPress ≠ WPilot** — build implementation vs operate site.
3. **WordPress development ≠ WordPress operations** — separate charters, separate evidence, separate runtime claims.

---

*Ecosystem position v1 — relationship documentation only.*
