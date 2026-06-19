# WPilot Maintenance Policy v1

**Classification:** Maintenance policy — post-RC5 reference implementation.  
**Version:** v1  
**Date:** 2026-06-19  
**Lifecycle state:** Reference Implementation  
**Authority:** `WPILOT-RC5-PROVEN-CONNECTION-RUNTIME-2026-06-19`  
**Scope:** Documentation policy. Does not auto-authorize code changes.

---

## Purpose

Define what changes are allowed on WPilot after RC5 finalization without treating WPilot as an active MVP development target. WPilot is the **first proven CMS Pilot runtime reference implementation** in MARS — maintenance preserves the proven baseline; expansion requires explicit charter.

**Related:** [WPILOT-FINAL-STATE-RC5.md](WPILOT-FINAL-STATE-RC5.md) · [WPILOT-LIFECYCLE-STATE.md](WPILOT-LIFECYCLE-STATE.md) · [WPILOT-STATE-FREEZE-2026-06-19-v1.md](WPILOT-STATE-FREEZE-2026-06-19-v1.md)

---

## Default posture

| Field | Value |
|-------|-------|
| **Development focus** | **Shifted away** from WPilot |
| **Freeze** | **ACTIVE** |
| **Sprint 3** | **HOLD** |
| **Future work** | Explicit HITL charter only |

---

## Allowed without charter

The following may proceed under normal human-operated discipline:

| Category | Examples |
|----------|----------|
| **Bug fixes** | Correct incorrect behavior on proven REST paths; connection tracker fixes; admin UI defects |
| **Security fixes** | Token handling hardening; auth validation; secret exposure remediation |
| **Documentation updates** | Evidence register updates after new proof; cross-links; operator runbooks; lifecycle docs |
| **Compatibility updates** | WordPress/PHP version compatibility on existing proven surface; dependency bumps that do not expand API |

**Constraints:**

- Preserve proven safety loop semantics.
- Update [WPILOT-PROVEN-CAPABILITIES-v1.md](WPILOT-PROVEN-CAPABILITIES-v1.md) only after new completed DEV work + evidence.
- No token values in repo.
- Document changes in reports when material.

---

## Requires explicit charter

The following **must not** proceed without explicit HITL charter:

| Category | Examples |
|----------|----------|
| **New runtime capabilities** | Autonomous execution; batch operations; new mutation primitives |
| **New endpoint families** | Menu, widget, CSS, footer, theme, media REST routes |
| **New write targets** | Targets beyond `page.post_content` scoped-replace |
| **Sprint 3** | Any Sprint 3 scope, roadmap activation, or feature sprint |
| **Production expansion** | Production deploy; multisite; live customer sites |
| **Core Model expansion** | New policy layers; architecture passes beyond v1 stable stack |
| **Unfreezing RC5** | Lifting endpoint freeze; removing Sprint 3 HOLD |

Charter should name: scope, environment, evidence standard, rollback plan, and explicit exclusions.

---

## Change classification

| Class | Description | Approval | Examples |
|-------|-------------|----------|----------|
| **M0 — Documentation only** | Markdown, reports, registry/governance cross-links; no plugin/runtime change | Operator / doc maintainer | Finalization docs; OPERATIONAL-INDEX update; proven capabilities evidence addendum |
| **M1 — Maintenance fix** | Corrective change on proven surface; no new capabilities | HITL review; minimal diff | Connection tracker bugfix; auth edge case; admin label fix |
| **M2 — Security fix** | Addresses vulnerability or secret exposure risk | HITL review; priority path | Token leak remediation; REST auth hardening |
| **M3 — Compatibility** | Keeps proven surface working on supported WP/PHP versions | HITL review | WordPress core compatibility patch on existing routes |
| **C1 — Chartered expansion** | New capability within existing family pattern | **Explicit charter required** | Additional read endpoints; expanded inspect surface |
| **C2 — Chartered write expansion** | New write targets or endpoint families | **Explicit charter required** | Menu/widget/CSS plugin writes; Sprint 3 |
| **C3 — Chartered environment expansion** | Production, multisite, or new site baselines | **Explicit charter required** | Production deploy; second DEV site proof |
| **X — Forbidden without re-charter** | Violates RC5 freeze or mission boundaries | Blocked | Autonomous admin; MARS orchestration claims; token in git |

**Default for ambiguous changes:** treat as **C1 or higher** — require charter.

---

## Evidence discipline after changes

| Change class | Proven Capabilities update | New milestone |
|--------------|---------------------------|---------------|
| M0 | Only if documenting new proof | No |
| M1–M3 | Only if behavior proof changed | Optional report |
| C1–C3 | **Required** after DEV proof | Charter may require new milestone |

---

## Explicit exclusions (normative)

| Excluded | Reason |
|----------|--------|
| MARS orchestration runtime | WPilot is External Systems lane |
| Autonomous CMS administration | Human-supervised only |
| Shadow registries | Use [registry/project-registry.md](../../registry/project-registry.md) |
| Sprint 3 by default | HOLD until charter |

---

## Related documents

| Document | Role |
|----------|------|
| [WPILOT-FINAL-STATE-RC5.md](WPILOT-FINAL-STATE-RC5.md) | Final state |
| [WPILOT-AUTHORITY-STATE-RC5.md](WPILOT-AUTHORITY-STATE-RC5.md) | Authority baseline |
| [metacode-wpilot-plugin-mvp-roadmap.md](metacode-wpilot-plugin-mvp-roadmap.md) | Planned roadmap — **not** auto-activated |

---

*WPilot Maintenance Policy v1 · Reference Implementation · 2026-06-19.*
