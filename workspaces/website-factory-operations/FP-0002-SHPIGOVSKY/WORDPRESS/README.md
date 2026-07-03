# FP-0002 Canonical WordPress Source Surface

**Project:** FP-0002 — Шпиговский  
**Surface:** `WORDPRESS/`  
**Status:** V9-06C.1 SOURCE ACTIVATION GATE RESOLVED
**Classification:** SOURCE ACTIVATION READY — NOT DELIVERED — RUNTIME NOT STARTED

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
| ACF Pro | **ADMITTED** as operator-managed external dependency (OD-001 / V9-06B.2) |
| BoundedMeta primary path | REJECTED |
| V9-06B | **COMPLETE** — theme + core skeleton |
| V9-06C | **COMPLETE — CONTENT MODEL SOURCE IMPLEMENTED** |
| V9-06C.1 | **COMPLETE — SOURCE ACTIVATION GATE RESOLVED** |
| Runtime changes | 0 |
| WordPress source implementation | **CONTENT MODEL COMPLETE** |
| WordPress runtime implementation | **NOT STARTED** |
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
| Shpigovsky Core | V9-06C.1 CONTENT MODEL SOURCE ACTIVATION READY — NOT DELIVERED |
| ACF JSON | V9-06C SOURCE CREATED — NOT DELIVERED |

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

## V9-06B.2 ACF dependency admission

ACF PRO advanced-custom-fields-pro/acf.php v6.8.5 is admitted as an **operator-managed external dependency**. MARS may use its public APIs after admission but must not source, install, update, replace, delete, distribute, package, or manage licensing for it.

ACF Extended PRO acf-extended-pro/acf-extended.php v0.9.2.3 is classified separately as operator-managed and **not approved for FP-0002 use by default**. ACF Free remains installed but inactive and is not used while PRO is active.

Registry: architecture/FP-0002-OPERATOR-MANAGED-EXTERNAL-PLUGINS-v1.md.

## V9-06C content model source implementation

V9-06C implements the canonical WordPress content model in source only:

- `service` CPT source and `/uslugi/{service-path}/` permalink source are implemented in `plugins/shpigovsky-core/`.
- 13 ACF Pro field group definitions are implemented in source and canonical JSON is generated under `acf-json/`.
- Options Page, admin UX helpers, ACF dependency guards, and validation hooks are source implemented.
- Runtime delivery, WordPress object creation, database writes, rewrite flushing, ACF runtime DB registration, V9 HTML/CSS/JS integration, and runtime ACF JSON writes were not performed.

Report: `reports/FP-0002-V9-06C-CONTENT-MODEL-SOURCE-IMPLEMENTATION-REPORT-v1.md`.


## V9-06C.1 source activation gate resolution (2026-07-04)

V9-06D.1 runtime delivery was blocked before apply by the old `SHPIGOVSKY_CORE_SKELETON=true` source gate. V9-06C.1 resolves that source blocker with `SHPIGOVSKY_CORE_MODE=content_model` and an explicit module activation registry. Runtime writes: 0. WordPress object writes: 0.

Reports:

- `reports/FP-0002-V9-06C1-SOURCE-ACTIVATION-GATE-RESOLUTION-REPORT-v1.md`
- `reports/FP-0002-V9-06D1-RUNTIME-DELIVERY-CONTENT-MODEL-ACTIVATION-REPORT-v1.md` — historical blocked attempt, superseded by V9-06C.1 source fix

