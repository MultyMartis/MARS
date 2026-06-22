# Forge WordPress — Phase 1 Architecture Input v1

**Document type:** Next-stage input package (not architecture)  
**Version:** v1  
**Date:** 2026-06-22  
**Authorized use:** Input to **Forge WordPress Phase 1 Architecture Design** only

---

## Confirmed inputs

| Input | Source / note |
|-------|----------------|
| MARS pre-architecture audit | REPORT — WP FORGE PRE-ARCHITECTURE ECOSYSTEM INTELLIGENCE AUDIT (internal repo audit — see [research register](../FORGE-WORDPRESS-RESEARCH-REGISTER-v1.md) Entry 1) |
| Global research | [AG-WP-001-GLOBAL-WORDPRESS-DEVELOPMENT-RESEARCH-v1.md](../../../../../workspaces/website-factory-operations/internal-agent-seeds/AG-WP-001-forge-wordpress/research/AG-WP-001-GLOBAL-WORDPRESS-DEVELOPMENT-RESEARCH-v1.md) |
| Website Factory boundaries | [FORGE-WORDPRESS-SCOPE-AND-BOUNDARIES-v1.md](../FORGE-WORDPRESS-SCOPE-AND-BOUNDARIES-v1.md); Factory [OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md) |
| WPilot boundaries | [projects/wpilot/OPERATIONAL-INDEX.md](../../../../../projects/wpilot/OPERATIONAL-INDEX.md); seed [AG-WP-001-WPILOT-CONNECTION.md](../../../../../workspaces/website-factory-operations/internal-agent-seeds/AG-WP-001-forge-wordpress/AG-WP-001-WPILOT-CONNECTION.md) |
| AG-WP-001 seed | [internal-agent-seeds/AG-WP-001-forge-wordpress/](../../../../../workspaces/website-factory-operations/internal-agent-seeds/AG-WP-001-forge-wordpress/) |
| FP-0002 probable pilot | LOC-ZONE [FP-0002-SHPIGOVSKY/](../../../../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/) — **not started** |
| Human-supervised model | MARS execution model; research + audit consensus |
| Sandbox-first | Research Base v1 + WPilot DEV-only operational precedent |
| Version-controlled implementation | Research + enterprise practice alignment — **design target**, not evidenced subsystem tooling |
| QA-gated handoff | Factory validation architecture (VL0–VL6) upstream; WPilot backup-first operations downstream |

---

## Decisions required in Phase 1 (FW-01)

Phase 1 **must** produce human-approved answers — **not** decided in FW-00:

| # | Decision area |
|---|----------------|
| 1 | Exact subsystem architecture (layers, artifacts, descent order) |
| 2 | Agent vs skill family (whether `AG-WP-001` promotes to registered agent or remains doc/skill pack) |
| 3 | Classic / hybrid / block implementation modes (per site or per section policy) |
| 4 | ACF policy (mandatory vs optional, Local JSON, blocks strategy) |
| 5 | Theme vs functionality plugin policy |
| 6 | Source repo model (mono-repo, theme+plugin split, deployment packaging) |
| 7 | Dev environment (Playground, wp-env, local stack — evidence-based choice) |
| 8 | Validation stack (PHPCS, PHPUnit, visual regression, preview surfaces) |
| 9 | WPilot handoff contract (frozen zones, editable regions, operational limits) |
| 10 | FP-0002 eligibility (pilot charter, frontend readiness gate, WordPress stack) |

---

## Still prohibited in Phase 1 unless separately chartered

| Prohibited | Notes |
|------------|-------|
| Implementation code | Theme, plugin, ACF JSON, CPT registration code |
| Production access | Live site credentials, unrestricted admin |
| Autonomous deploy | CI/CD to production without human gates |
| Agent registration | `agents/registry.md` row requires promotion charter |
| `project_id` registration | Subsystem remains under `mars-website-factory` unless operator reclassifies |

---

## Output expectations (indicative — not executed here)

Phase 1 architecture design should yield **documentation artifacts** such as:

- Architecture overview charter (v1)
- Methodology descent order
- Handoff contract draft (Factory frontend → Forge WordPress → WPilot)
- Tooling and validation design (documentation)
- Pilot intake criteria

**No outputs from this list are created by FW-00.**

---

## Related

- [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) — next authorized stage
- [roadmap.md](../roadmap.md) — FW-01 **NEXT**

---

*Phase 1 input v1 — decisions deferred. Not architecture approval.*
