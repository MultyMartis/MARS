# Forge WordPress — Command and Operation Model v1

**Document type:** Typed operation specification  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03

**Honesty:** Operation **specifications** only — not implemented runtime or agent API.

---

## 1. Risk classes

| Class | Definition | Forge allowed |
|-------|------------|---------------|
| **R0 READ-ONLY** | Inspect, list, diff — no mutation | **Yes** |
| **R1 LOCAL REVERSIBLE** | Local file/build changes; Git-committable | **Yes** with policy |
| **R2 DEV MUTATION** | Local WP DB/options/plugins | **Yes** — local only |
| **R3 RELEASE PREPARATION** | Package, manifest, handoff bundle | **Yes** — human gate |
| **R4 PRODUCTION** | Live site mutation | **FORBIDDEN** |

---

## 2. Operation registry

### inspect_frontend_package

| Field | Value |
|-------|-------|
| **Purpose** | Verify handoff manifest, `src`/`dist`, build reproducibility |
| **Inputs** | Frontend path, expected SHA, manifest |
| **Outputs** | `WV0-INPUT-COMPLETENESS-REPORT` section |
| **Environment** | Local filesystem |
| **Risk** | R0 |
| **Approval** | Auto |
| **Rollback** | N/A |
| **Forbidden targets** | Production hosts |
| **Report** | `inspect-frontend-package.json` |

### inspect_wordpress_project

| Field | Value |
|-------|-------|
| **Purpose** | Validate WORDPRESS workspace structure vs standards |
| **Inputs** | Project path, WAD |
| **Outputs** | Structure checklist |
| **Risk** | R0 |
| **Approval** | Auto |
| **Report** | `inspect-wordpress-project.json` |

### inspect_theme

| Field | Value |
|-------|-------|
| **Purpose** | Template map, enqueue, hierarchy compliance |
| **Inputs** | Theme path |
| **Outputs** | WV3 pre-check |
| **Risk** | R0 |

### inspect_plugins

| Field | Value |
|-------|-------|
| **Purpose** | Plugin register vs installed set (local) |
| **Inputs** | Plugin register, local `wp plugin list` |
| **Risk** | R0 |

### inspect_acf_schema

| Field | Value |
|-------|-------|
| **Purpose** | ACF JSON sync state |
| **Inputs** | `acf-json/` paths |
| **Risk** | R0 |

### inspect_content_model

| Field | Value |
|-------|-------|
| **Purpose** | CPT/taxonomy vs content model doc |
| **Risk** | R0 |

### create_local_environment

| Field | Value |
|-------|-------|
| **Purpose** | Provision Local site per project slug |
| **Inputs** | Project passport, PHP version |
| **Outputs** | Local site URL, path record in `local/` |
| **Risk** | R2 |
| **Approval** | Operator |
| **Rollback** | Delete Local site |
| **Forbidden** | Production |

### reset_local_environment

| Field | Value |
|-------|-------|
| **Purpose** | Fresh DB / reinstall WP on local |
| **Risk** | R2 |
| **Approval** | Operator |
| **Rollback** | Restore from STORAGE dump if exists |

### build_frontend_assets

| Field | Value |
|-------|-------|
| **Purpose** | `npm run build` + sync to theme assets |
| **Inputs** | FRONTEND path, theme assets path |
| **Outputs** | Built CSS/JS/img; build log |
| **Risk** | R1 |
| **Approval** | Auto in dev; operator for release |
| **Rollback** | Git restore |

### run_phpcs

| Field | Value |
|-------|-------|
| **Purpose** | WPCS compliance (WV2) |
| **Outputs** | `WV2-CODE-QUALITY-REPORT` |
| **Risk** | R0 |
| **Approval** | Auto |

### run_static_analysis

| Field | Value |
|-------|-------|
| **Purpose** | Optional PHPStan/Psalm |
| **Risk** | R0 |
| **Approval** | Auto |

### run_php_tests

| Field | Value |
|-------|-------|
| **Purpose** | PHPUnit for custom logic |
| **Risk** | R0–R1 |
| **Approval** | Auto |

### run_js_tests

| Field | Value |
|-------|-------|
| **Purpose** | Frontend unit tests if present |
| **Risk** | R0 |

### run_e2e_tests

| Field | Value |
|-------|-------|
| **Purpose** | Playwright smoke paths (WV5) |
| **Risk** | R0 |
| **Approval** | Auto |

### capture_reference_screenshots

| Field | Value |
|-------|-------|
| **Purpose** | Static `dist/` or approved HTML reference |
| **Outputs** | STORAGE baselines |
| **Risk** | R1 |
| **Approval** | Operator (PIXEL_PERFECT) |

### capture_wordpress_screenshots

| Field | Value |
|-------|-------|
| **Purpose** | Local WP URLs at canonical viewports |
| **Risk** | R0 |

### compare_visual_output

| Field | Value |
|-------|-------|
| **Purpose** | Diff reference vs WP (WV6) |
| **Outputs** | Diff images, metrics |
| **Risk** | R0 |
| **Approval** | Human sign-off required for PIXEL_PERFECT |

### run_accessibility_checks

| Field | Value |
|-------|-------|
| **Purpose** | axe-playwright / manual checklist (WV8) |
| **Risk** | R0 |

### run_performance_checks

| Field | Value |
|-------|-------|
| **Purpose** | Lighthouse CLI or Playwright trace (WV8) |
| **Risk** | R0 |

### run_security_checks

| Field | Value |
|-------|-------|
| **Purpose** | PHPCS security sniffs, secret scan, dependency audit (WV4) |
| **Risk** | R0 |
| **Approval** | Security reviewer for waivers |

### package_theme

| Field | Value |
|-------|-------|
| **Purpose** | Theme ZIP excluding dev files |
| **Outputs** | `theme-{slug}-{version}.zip` |
| **Risk** | R3 |
| **Approval** | Operator |

### package_functionality_plugin

| Field | Value |
|-------|-------|
| **Purpose** | Custom plugin ZIP |
| **Risk** | R3 |
| **Approval** | Operator |

### build_release_manifest

| Field | Value |
|-------|-------|
| **Purpose** | RELEASE-MANIFEST per FW-T-12 |
| **Risk** | R3 |
| **Approval** | Operator + validator |

### prepare_wpilot_handoff

| Field | Value |
|-------|-------|
| **Purpose** | Assemble WPILOT-HANDOFF package per FW-C-03 |
| **Outputs** | Package + evidence bundle |
| **Risk** | R3 |
| **Approval** | **BLOCKING** — G10 |
| **Forbidden** | Direct production deploy |

---

## 3. Excluded from normal surface

| Excluded | Reason |
|----------|--------|
| Arbitrary SQL | Use WP-CLI scoped commands only |
| Unrestricted shell | Safe command policy |
| Production mutation | R4 |
| `wp search-replace` on remote | WPilot domain |

---

## Related

- [FORGE-WORDPRESS-SAFE-COMMAND-POLICY-v1.md](FORGE-WORDPRESS-SAFE-COMMAND-POLICY-v1.md)
- [FORGE-WORDPRESS-VALIDATION-RUNNER-ARCHITECTURE-v1.md](FORGE-WORDPRESS-VALIDATION-RUNNER-ARCHITECTURE-v1.md)

---

*Command model v1 — typed operations; not runtime.*
