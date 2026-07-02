# FP-0002 V9-05A — Pre-Implementation Gate Sequence v1

**Project:** FP-0002 Shpigovsky.ru  
**Phase:** V9-05A  
**Date:** 2026-07-02  
**Gate:** [FP-0002-V9-05A-APPROVED-FRONTEND-INTAKE-GATE-v1.md](./FP-0002-V9-05A-APPROVED-FRONTEND-INTAKE-GATE-v1.md)

Defines the approved phase sequence, checkpoint specification, admission boundary, FW-07C-2 charter scope, and implementation invariants. **Does not execute any of them.**

---

## Approved phase sequence

```text
V9-05A  Approved Frontend Intake and Foundation Adoption     ← THIS GATE (COMPLETE)
   ↓
V9-05B  Pre-Implementation Runtime Checkpoint
   ↓
V9-05C  Shpigovsky Read-Only Admission and Project Binding
   ↓
FW-07C-2  Controlled Additive/Mutation Capability Charter
   ↓
V9-06  WordPress Foundation Reconciliation
   ↓
V9-07+  Template, ACF, Object, Content and Runtime Implementation
   ↓
Visual parity checkpoints against V9 dist
```

Gates **must not** be skipped.

---

## V9-05B — Pre-Implementation Runtime Checkpoint (specified, not executed)

### Identity

```text
foundation-002-v9-pre-implementation
```

### Scope

Protect before first implementation write:

```text
X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\
Database: mars_wp_fp0002
```

### Required components (future task)

| Component | Requirement |
|-----------|-------------|
| Database dump | Complete `mars_wp_fp0002` export |
| Theme snapshot | `wp-content/themes/shpigovsky/` |
| Plugin snapshot | `wp-content/plugins/shpigovsky-core/` |
| ACF JSON snapshot | Theme/plugin acf-json paths |
| Uploads inventory | `wp-content/uploads/` manifest |
| Pages/Posts/menu manifest | WP-CLI or equivalent export |
| Active theme/plugin state | Recorded |
| WordPress version | Recorded |
| Configuration-safe metadata | No secrets in Git |
| SHA-256 manifest | All snapshot artefacts |
| Rollback instructions | X-native paths only |
| Scripts | No stale D/E operational paths |

### Executed in V9-05A

```text
NO
```

---

## V9-05C — Shpigovsky Read-Only Admission (specified, not executed)

| Field | Value |
|-------|-------|
| Target | `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky` |
| Initial mode | **READ-ONLY PROJECT ADMISSION** |
| Writes authorized | **NO** |
| Auto-escalation to writes | **NO** |

### Required proof (future)

- Exact filesystem root
- Site identity (`MLI-WP-FP0002-LOCAL`)
- Domain (`http://shpigovsky.test/`)
- Environment (PHP, MySQL, WP version)
- Active theme and plugin
- Route/object inventory vs V9 manifest
- ACF state (groups present/absent)
- Zero mutations during admission pass
- No reparse escape outside `X:\`
- Fail-closed on boundary violation

---

## FW-07C-2 — Controlled Capability Charter (boundary only)

**Status:** `NOT AUTHORIZED`

Future write capability groups when separately chartered:

### Filesystem capabilities

- Create/update theme files
- Create/update plugin files
- Create/update ACF JSON/PHP
- Build/copy approved assets from V9 frontend
- Create implementation manifests
- Controlled runtime deployment to MLI site root

### WordPress / database capabilities

- Create missing Pages
- Update exact existing Pages
- Assign parents and page templates
- Create Blog fixture post
- Update menus
- Register/import ACF groups
- Update approved ACF values
- Publish legal routes when explicitly approved
- Retire conflicting objects only with exact operator approval
- Flush rewrites only after route changes

### Explicitly excluded until separate decisions

- Form backend / SMTP
- SEO plugin installation
- Analytics integration
- Cookie consent platform
- Production deployment
- Production secrets
- Legal finalization (remove DEMO tokens)
- Arbitrary plugin installation
- Broad object deletion
- Production database operations

---

## Tracked source authority (forward model)

| Role | Path | Status |
|------|------|--------|
| V9 static frontend authority | `workspaces/fp-0002-shpigovsky-v9/src/` + `dist/` | **ACTIVE** |
| Current tracked WP source (lineage) | `workspaces/fp-0002-shpigovsky-v6/WORDPRESS/` | **TRACKED** — foundation bootstrap origin |
| Canonical Factory WP surface (prescribed) | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/` | **NOT YET CREATED** |
| Runtime deployment target | `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\` | **RUNTIME ONLY** — not source of truth |
| Forge project docs | `projects/mars-website-factory/subsystems/forge-wordpress/projects/fp-0002/` | **DOCUMENTATION** — not PHP source |

### Recommended ownership model

Per [FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md](../../../../projects/mars-website-factory/subsystems/forge-wordpress/FORGE-WORDPRESS-REPOSITORY-AND-FILESYSTEM-MODEL-v1.md):

```text
V9 frontend workspace:
  owns static frontend source and visual authority

Canonical Factory operations WORDPRESS surface:
  workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/
  owns theme PHP, plugin PHP, ACF JSON, integration scripts, deployment manifests
  seeded from existing v6/WORDPRESS tracked bootstrap at first implementation pass

X:\MARS-Localhost:
  runtime deployment only — never sole source of truth
```

**Operator decision still required:** physical creation/migration timing of the operations `WORDPRESS/` tree — **before V9-06 implementation writes**, not in V9-05A.

---

## Implementation invariants (mandatory)

| ID | Invariant |
|----|-----------|
| INV-01 | Do not redesign V9 |
| INV-02 | Do not approximate components |
| INV-03 | Do not use a page builder |
| INV-04 | Do not use arbitrary Flexible Content |
| INV-05 | Native WordPress fields first |
| INV-06 | Deterministic templates plus bounded repeaters |
| INV-07 | Do not return the preloader |
| INV-08 | Do not return G6 (O-Centre removed in V9) |
| INV-09 | Do not publish `/uslugi/genotipirovanie/` |
| INV-10 | Preserve modal lifecycle and accepted scroll lock |
| INV-11 | Preserve Scroll-to-Top contract (`scrollY > 500`) |
| INV-12 | Preserve 31-route map |
| INV-13 | Preserve Alcohol Dependence leaf as full-page exception |
| INV-14 | Use V9 `dist/` for visual comparison |
| INV-15 | Operator remains sole visual approval authority |
| INV-16 | No production-ready claim while production blockers remain |

---

## Remaining blockers before first implementation write

1. V9-05B pre-implementation checkpoint **not executed**
2. V9-05C Shpigovsky read-only admission **not executed**
3. FW-07C-2 mutation charter **not authorized**
4. Tracked WordPress source migration to canonical ops surface **not executed**
5. Route reconciliation (14 creates, 4 retire/review) **not started**
6. Production blockers (legal DEMO, placeholders, forms, cookie) **remain**

---

## Recommended next action

```text
CREATE_V9_05B_PRE_IMPLEMENTATION_CHECKPOINT
```

---

*Sequence specification — documentation only.*
