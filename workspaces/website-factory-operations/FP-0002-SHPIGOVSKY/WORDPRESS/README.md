# FP-0002 Canonical WordPress Source Surface

**Project:** FP-0002 — Шпиговский  
**Surface:** `WORDPRESS/`  
**Status:** ARCHITECTURE DESIGNED (V9-06A)  
**Classification:** FOUNDATION BASELINE — ARCHITECTURE DESIGN COMPLETE — NO V9 IMPLEMENTATION

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

## V9-06A architecture (2026-07-03)

| Surface | Status |
|---------|--------|
| V9-06A | ARCHITECTURE DESIGN COMPLETE |
| WordPress entity model | DESIGNED |
| Template system | DESIGNED |
| Admin UX | DESIGNED |
| ACF decision | MIXED (Free + BoundedMeta; Pro optional) |
| Runtime changes | 0 |
| WordPress implementation | NOT STARTED |
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
  theme/shpigovsky/   # adopted foundation theme
  plugins/shpigovsky-core/
  acf-json/           # empty foundation state
  delivery/           # delivery fixtures and proof harness
  validation/         # validation evidence
  reports/            # human-readable reports
```

## Foundation classification

| Surface | Classification |
|---------|----------------|
| Theme | ADOPTED — NO V9 IMPLEMENTATION |
| Shpigovsky Core | ADOPTED — NO NEW CAPABILITIES |
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
