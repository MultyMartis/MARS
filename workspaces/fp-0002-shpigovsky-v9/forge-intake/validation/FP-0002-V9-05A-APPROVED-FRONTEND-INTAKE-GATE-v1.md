# FP-0002 V9-05A — Approved Frontend Intake Gate v1

**Project:** FP-0002 Shpigovsky.ru  
**Phase:** V9-05A — Approved Frontend Intake and WordPress Foundation Adoption  
**Date:** 2026-07-02  
**Status:** `FP0002_V9_APPROVED_FRONTEND_INTAKE_APPROVED`

---

## Gate decision

```text
FP-0002 V9 APPROVED FRONTEND INTAKE:
APPROVED

Prepared WordPress foundation:
ADOPTED

Implementation base:
PREPARED FOUNDATION + CONTROLLED V9 INTEGRATION
```

This gate **closes** the Approved Frontend Intake boundary for FP-0002. It **does not** authorize WordPress implementation writes, Shpigovsky admission, or FW-07C-2.

---

## Operator decision (recorded)

The operator confirms the existing Shpigovsky WordPress runtime, theme, plugin, database, page skeleton, menus, ACF wiring, and local infrastructure were **intentionally prepared** for FP-0002. They are **not** disposable legacy artefacts. They are the **approved WordPress foundation** for the next implementation stage.

```text
Implementation-base decision:
REUSE PREPARED WORDPRESS FOUNDATION WITH CONTROLLED V9 INTEGRATION
```

Clean rebuild and foundation discard are **not** reopened by this gate.

---

## Authority order (effective)

| Priority | Authority |
|----------|-----------|
| 1 | Explicit operator decision (this gate) |
| 2 | V9 stable frontend tag `fp-0002-v9-operator-approved-static-frontend-stable-01` |
| 3 | V9 Forge Intake Pack tag `fp-0002-v9-forge-wordpress-intake-pack-01` |
| 4 | V9 `dist/` — rendered visual reference |
| 5 | V9 `src/` — editable frontend source |
| 6 | Prepared WordPress foundation (`MLI-WP-FP0002-LOCAL`) |
| 7 | Current Forge contracts |
| 8 | Current MLI authority |
| 9 | Earlier FP-0002 materials where non-conflicting |
| 10 | Historical evidence |

---

## Frontend authority

| Surface | Role | Canonical path |
|---------|------|----------------|
| V9 `src/` | Canonical editable frontend source | `workspaces/fp-0002-shpigovsky-v9/src/` |
| V9 `dist/` | Canonical rendered visual reference | `workspaces/fp-0002-shpigovsky-v9/dist/` |
| Stable baseline commit | Frozen operator-approved frontend | `a51376872fbfefb7d5f68a58b440c726d6cf3de3` |
| Stable baseline tag | Operator freeze marker | `fp-0002-v9-operator-approved-static-frontend-stable-01` |

V7/V8 frontends are **historical reference only** — not implementation authority.

---

## WordPress foundation authority

| Surface | Role | Canonical path |
|---------|------|----------------|
| WordPress installation | Approved implementation foundation | `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\` |
| Domain | Local runtime identity | `http://shpigovsky.test/` |
| Database | Reconciliation base | `mars_wp_fp0002` |
| Theme | Approved foundation theme | `wp-content/themes/shpigovsky/` |
| Functionality plugin | Approved foundation plugin | `wp-content/plugins/shpigovsky-core/` |
| MLI manifest | Runtime contract | `projects/mars-localhost-infrastructure/manifests/MLI-WP-FP0002-LOCAL-RUNTIME-MANIFEST-v1.md` |

Historical origin under V6-era tracked paths does **not** invalidate foundation status.

---

## Intake pack authority

| Field | Value |
|-------|-------|
| Master document | `forge-intake/FP-0002-V9-FORGE-WORDPRESS-INTAKE-PACK-v1.md` |
| Intake commit | `de1169cfc4d58eb879bac4387d514cd1a540a1eb` |
| Intake tag | `fp-0002-v9-forge-wordpress-intake-pack-01` |
| Routes | 31 / 31 |
| Unmapped | 0 |
| Validator | `npm run validate:forge-intake` |

---

## Integration disposition

```text
Preserve foundation.
Integrate V9 into it.
Reconcile conflicting route/content assumptions.
Do not rebuild WordPress from zero.
Do not create an unrelated replacement scaffold.
```

### Classification model

| Class | Meaning |
|-------|---------|
| **FOUNDATION — PRESERVE** | Infrastructure and bootstrap intentionally created for FP-0002 |
| **V9 INTEGRATION REQUIRED** | Elements not yet implemented in theme/plugin/content |
| **SUPERSEDED ASSUMPTIONS** | Old route/content assumptions that conflict with V9 only |

The whole theme, plugin, or WordPress foundation is **not** superseded.

---

## Linked registers

| Register | Path |
|----------|------|
| Foundation adoption | [FP-0002-V9-05A-WORDPRESS-FOUNDATION-ADOPTION-REGISTER-v1.md](../registers/FP-0002-V9-05A-WORDPRESS-FOUNDATION-ADOPTION-REGISTER-v1.md) |
| Route conflicts | [FP-0002-V9-05A-ROUTE-CONFLICT-REGISTER-v1.md](../registers/FP-0002-V9-05A-ROUTE-CONFLICT-REGISTER-v1.md) |
| Pre-implementation sequence | [FP-0002-V9-05A-PRE-IMPLEMENTATION-GATE-SEQUENCE-v1.md](./FP-0002-V9-05A-PRE-IMPLEMENTATION-GATE-SEQUENCE-v1.md) |

---

## Hard boundaries (this gate)

| Action | Authorized |
|--------|------------|
| Documentation under approved roots | **YES** |
| WordPress / DB / runtime mutation | **NO** |
| V9 `src/` or `dist/` edits | **NO** |
| Shpigovsky project admission | **NO** |
| FW-07C-2 write charter | **NO** |
| Implementation (templates, ACF, assets) | **NO** |
| Fresh pre-implementation checkpoint | **NO** (deferred to V9-05B) |

---

## Evidence reconciliation (V9-05 audit)

| Check | Result |
|-------|--------|
| V9 authority | **VERIFIED** |
| Intake Pack | **31 / 31 routes, 0 unmapped — PASS** |
| Local runtime | **AVAILABLE** |
| Theme | **prepared foundation** |
| Plugin | **prepared foundation** |
| Reuse decision | **REUSE PREPARED FOUNDATION WITH CONTROLLED V9 INTEGRATION** |
| Shpigovsky admission | **NO** |
| FW-07C-2 | **NOT AUTHORIZED** |
| Implementation | **NOT STARTED** |

---

## Next authorized stage

**V9-05B — Pre-Implementation Runtime Checkpoint** — see [pre-implementation gate sequence](./FP-0002-V9-05A-PRE-IMPLEMENTATION-GATE-SEQUENCE-v1.md).

---

*Formal intake gate — documentation only. Closes V9-05A; does not open implementation.*
