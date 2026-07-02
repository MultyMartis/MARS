# FP-0002 Canonical WordPress Source Surface

**Project:** FP-0002 — Шпиговский  
**Surface:** `WORDPRESS/`  
**Status:** V9-06B SKELETON COMPLETE  
**Classification:** FOUNDATION BASELINE — ARCHITECTURE APPROVED — NO V9 IMPLEMENTATION

---

## Purpose

Git-tracked canonical source for WordPress theme, project plugin, and ACF JSON delivery to the local FP-0002 runtime.

## Authority

| Role | Path |
|------|------|
| **Canonical WordPress source** | `X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS\` |
| **Runtime deployment target** | `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\` |
| **V9 frontend source (separate)** | `X:\AI MARS\workspaces\fp-0002-shpigovsky-v9\src\` |
| **V9 static output (separate)** | `X:\AI MARS\workspaces\fp-0002-shpigovsky-v9\dist\` |

The runtime is **not** the canonical editable source. Delivery flows: Git source → manifested package → bounded runtime apply.

## V9-06A / V9-06A.1 architecture (2026-07-03)

| Surface | Status |
|---------|--------|
| V9-06A | COMPLETE |
| V9-06A.1 | COMPLETE — reconciliation |
| WordPress architecture | **APPROVED** |
| Route classification | RECONCILED |
| Service entity registry | 15 VERIFIED |
| Service permalink contract | DEFINED |
| ACF Pro | **REQUIRED** (OD-001) |
| BoundedMeta primary path | REJECTED |
| V9-06B | **COMPLETE** — theme + core skeleton |
| V9-06C | READY FOR OPERATOR AUTHORIZATION |
| Runtime changes | 0 |
| WordPress implementation | SKELETON ONLY (V9-06B) |
| FW-07C-2D | SUPERSEDED BY ARCHITECTURE-FIRST SEQUENCE (V9-06D) |

Authority: [architecture/FP-0002-WORDPRESS-ARCHITECTURE-v1.md](architecture/FP-0002-WORDPRESS-ARCHITECTURE-v1.md)

## Structure

```text
WORDPRESS/
  README.md
  SOURCE-AUTHORITY.md
  architecture/       # V9-06A design pack
  manifests/          # source and package manifests
  packages/           # built ZIP packages
  theme/shpigovsky/   # V9-06B skeleton theme
  plugins/shpigovsky-core/  # V9-06B skeleton plugin
  validation/         # V9-06B static validation
  reports/            # implementation reports
```

## Foundation classification

| Surface | Classification |
|---------|----------------|
| Theme | V9-06B SKELETON — NO V9 VISUAL INTEGRATION |
| Shpigovsky Core | V9-06B SKELETON — MODULES INERT |
| ACF JSON | EMPTY FOUNDATION STATE |

## Provenance

- **FOUNDATION_ORIGIN:** `workspaces/fp-0002-shpigovsky-v6/WORDPRESS/` (historical V6 surface)
- **CANONICAL_CURRENT:** this surface (adopted from prepared runtime foundation, FW-07C-2C)
- Runtime foundation preserved per V9-05A adoption register

## Delivery policy (FW-07C-2C)

- Mode: `ADDITIVE_ONLY` (proven)
- Overwrite: NOT AUTHORIZED
- Delete: NOT AUTHORIZED (except exact owned proof cleanup)
- Unknown files: FAIL CLOSED

See [SOURCE-AUTHORITY.md](SOURCE-AUTHORITY.md) and Forge delivery contract.
