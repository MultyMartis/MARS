# Forge WordPress — Scope and Boundaries v1

**Document type:** Preliminary scope and exclusions  
**Version:** v1  
**Date:** 2026-06-22  
**Lifecycle:** FOUNDATION — **not** a full methodology charter

---

## Preliminary in-scope (future architecture subject)

When chartered beyond FOUNDATION, Forge WordPress is expected to own **documentation and human-supervised design** for:

| Area | Description |
|------|-------------|
| Frontend-to-WordPress transformation methodology | How approved Factory frontend maps to WordPress surfaces |
| WordPress implementation architecture | Overall implementation structure and descent order |
| Theme architecture | Presentation layer decisions (templates, parts, patterns — mode TBD in Phase 1) |
| Functionality plugin boundary | Business logic, CPT/taxonomy placement vs theme |
| Content modeling | Editorial model, fields, relationships, REST exposure |
| ACF architecture | Field groups, Local JSON, blocks — policy TBD in Phase 1 |
| CPT and taxonomy architecture | Registration, capabilities, admin UX |
| Template implementation | PHP/block/hybrid template strategy — mode TBD |
| Admin UX | Editor constraints, editable regions, locking |
| Plugin integration planning | Third-party plugin selection and governance gates |
| Local/dev implementation workflow | Sandbox-first, version-controlled implementation |
| QA and visual regression | Implementation fidelity vs approved frontend |
| Implementation handoff to WPilot | Frozen implementation package + operational boundaries |

**This list is preliminary.** It does **not** authorize implementation work at FOUNDATION lifecycle.

---

## Explicitly out-of-scope

| Excluded | Reason |
|----------|--------|
| Website Factory design creation | Upstream Factory layers and Gulp/Forge frontend lane |
| Frontend redesign | Forge WordPress consumes **approved** frontend — does not replace it |
| Autonomous runtime | Human-supervised only; no MARS orchestration product |
| Production operations | WPilot and external hosting lanes |
| WordPress maintenance (live) | Post-handoff operational domain |
| Backups and rollback execution on live sites | WPilot / operator external workflow |
| Live mutation ownership | Operations, not implementation subsystem |
| Unrestricted production credentials | Security boundary |
| WPilot duplication | Operations bridge ≠ development subsystem |
| OCPilot responsibilities | OpenCart/ocStore lane — separate CMS Pilot sibling |
| Ecommerce architecture (unless separately chartered) | Not default FOUNDATION scope |
| Autonomous deployment | Explicit exclusion |
| Agent registration without charter | `AG-WP-001` promotion is separate decision |
| `project_id` registration | Subsystem under Website Factory only |
| WordPress theme/plugin code at FOUNDATION | FW-00 creates docs only |
| FP-0002 WordPress implementation | Requires Phase 1+ charter and pilot approval |

---

## Boundary reminders

- **Preliminary in-scope ≠ approved methodology.** Phase 1 must produce contracts before any pilot implementation.
- **Research Base v1 ≠ architecture.** External research informs design; it does not authorize build.
- **Probable pilot (FP-0002) ≠ started pilot.** Eligibility is a Phase 1 decision.

---

## Related documents

- [FORGE-WORDPRESS-IDENTITY-v1.md](FORGE-WORDPRESS-IDENTITY-v1.md)
- [FORGE-WORDPRESS-ECOSYSTEM-POSITION-v1.md](FORGE-WORDPRESS-ECOSYSTEM-POSITION-v1.md)
- Seed boundaries: [AG-WP-001-BOUNDARIES.md](../../../../workspaces/website-factory-operations/internal-agent-seeds/AG-WP-001-forge-wordpress/AG-WP-001-BOUNDARIES.md)

---

*Scope v1 — preliminary boundaries only. Not implementation authorization.*
