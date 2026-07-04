# FP-0002 WordPress Source Authority

**Version:** v1  
**Date:** 2026-07-03  
**Task:** FW-07C-2C

---

## Canonical source decision

| Surface | Origin | Runtime match | Canonical source | Classification |
|---------|--------|---------------|------------------|----------------|
| Theme `shpigovsky` | V6 `theme-source/shpigovsky` + runtime deltas | DELIVERED TO LOCAL RUNTIME in V9-06D.1 rerun | `WORDPRESS/theme/shpigovsky/` | CANONICAL_CURRENT — ADOPTED — RUNTIME DELIVERED |
| Plugin `shpigovsky-core` | V6 `functionality-plugin/shpigovsky-core` + runtime deltas | DELIVERED TO LOCAL RUNTIME in V9-06D.1 rerun | `WORDPRESS/plugins/shpigovsky-core/` | CANONICAL_CURRENT — ADOPTED — CONTENT MODEL ACTIVE |
| ACF JSON | V6 empty state + V9-06C source generation | 13 JSON files delivered to local runtime in V9-06D.1 rerun | `WORDPRESS/acf-json/` | REGISTERED — RUNTIME DELIVERED |

## Historical surfaces

| Path | Classification |
|------|----------------|
| `workspaces/fp-0002-shpigovsky-v6/WORDPRESS/` | FOUNDATION_ORIGIN / HISTORICAL |
| Runtime `wp-content/themes/shpigovsky/` | RUNTIME_ONLY (deployment target) |
| Runtime `wp-content/plugins/shpigovsky-core/` | RUNTIME_ONLY (deployment target) |

Runtime was **not** silently treated as canonical. Foundation captured from runtime after hash comparison and provenance review (V9-05A adoption). V6 remains historical reference; drift documented.

## Source/runtime boundary

```text
Git source (editable)     →  Package (manifested ZIP)  →  Runtime (deploy only)
WORDPRESS/theme/...          shpigovsky-theme-foundation-*     wp-content/themes/shpigovsky/
WORDPRESS/plugins/...        shpigovsky-core-foundation-*      wp-content/plugins/shpigovsky-core/
WORDPRESS/acf-json/          fp-0002-acf-json-foundation-*     wp-content/acf-json/
```

## Excluded from source

- WordPress core
- WPilot plugin
- MU-plugins
- Uploads
- wp-config.php secrets
- Generated caches/logs
- V9 `src/` and `dist/` (separate authority)

## Secret audit

Foundation baseline scanned at capture; no secrets detected in theme/plugin source files.

## V9 implementation

V9 frontend HTML/CSS/JS integration is **NOT INCLUDED** in V9-06C. V9 frontend remains under `workspaces/fp-0002-shpigovsky-v9/`.

V9-06C adds WordPress content model source only: Shpigovsky Core CPT/permalink/ACF/admin/validation source and canonical ACF JSON under `WORDPRESS/acf-json/`. V9-06C.1 resolves the Shpigovsky Core source activation gate with `SHPIGOVSKY_CORE_MODE=content_model`. V9-06D.1 rerun delivered this source into local runtime and verified content model activation. Object skeleton is **COMPLETE** in the local FP-0002 runtime as V9-06D.2; content migration, redirects, rewrite flush, and V9 integration remain **NOT STARTED**.

## Operator-managed external plugin boundary

V9-06B.2 admits ACF PRO as an operator-managed external dependency. The installed plugin files under runtime wp-content/plugins/advanced-custom-fields-pro/ are **not** canonical source, are **not** copied into Git, and are **not** delivered by Forge filesystem packages.

ACF Extended PRO is also operator-managed, active, and classified separately, but not approved for FP-0002 use by default. ACF Free is inactive fallback only.

Forbidden for these dependencies: automatic update, replacement, deletion, package delivery, license handling, license bypass repair, source mirroring, and unattended remediation. See architecture/FP-0002-OPERATOR-MANAGED-EXTERNAL-PLUGINS-v1.md.



## V9-06C.1 activation gate

Delivery of the previous V9-06D.1 package was blocked by the old skeleton gate and is now superseded by V9-06C.1 source repair. The current canonical source is activation-ready for a separate V9-06D.1 rerun. V9-06C.1 did not change runtime files, database state, external plugins, or WordPress objects.


## V9-06D.1 rerun runtime delivery

Runtime delivery is complete for the local FP-0002 runtime only. The runtime remains a deployment target, not canonical editable source. External plugins remain operator-managed and were not delivered, updated, replaced, or modified.


## V9-06D.2 object skeleton

Local runtime object skeleton is complete: 15 Service CPT objects created, required Page templates reconciled, no content migration, no V9 integration, no menu changes, no redirects, and no rewrite flush. Runtime remains deployment target; Git source records documentation and evidence only.


## V9-06D.3 content migration planning

Content migration planning is complete in Git documentation only. No runtime content writes, no V9 integration, no menu/redirect/rewrite changes.


## V9-06D.4 RERUN minimal content seed

Local runtime minimal ACF/meta seed is complete for authorized Pages 4/5/20 and Services 73/74/77/84 only. Full production content migration, V9 integration, menus, redirects, and Options Page values remain not performed. Previous blocked D.4 attempt is preserved as historical evidence.

## REWRITE-FLUSH-MICRO-GATE

Soft rewrite flush performed in local runtime only (`rewrite_rules` option). Hard flush not used; `.htaccess` unchanged. Service 74 remains HTTP 404 with correct generated permalink (`FLUSH_NOT_SUFFICIENT`). No content, menu, redirect, plugin, or V9 source/dist changes. Runtime remains deployment target; Git source records documentation and evidence only.

## ROUTE-OWNERSHIP-INVESTIGATION

Read-only route ownership investigation complete. Root cause: `POST_TYPE_LINK_REWRITE_MISMATCH` (depth-2 rewrite leaf-only `service` query var). Page ID 6 / Service ID 73 path collision confirmed as secondary. No runtime writes, no rewrite flush, no source edits in this phase. Recommended next: rewrite rule repair micro-task. V9-06D.5 blocked until Service 74 resolves.

## REWRITE-RULE-REPAIR

Depth-2 rewrite query mapping repaired in canonical source `ServicePermalinks.php` (`service=$matches[1]/$matches[2]`) and delivered to local runtime. Soft rewrite flush performed under DB/plugin checkpoint. Service 74 HTTP 200. Contract §4.2 updated. Content/ACF/menus/redirects unchanged. Page 6 / Service 73 secondary debt remains. V9-06D.5 unblocked for visual route QA.

## V9-06D.5 visual route QA

Read-only visual route QA complete after rewrite repair. All required D.5 routes HTTP 200; Service 74 regression PASS; skeleton template/render baseline confirmed; screenshots under `validation/v9-06d5-visual-route-qa/screenshots/`. No runtime content/ACF/menu/redirect/source mutations. V9 integration and production content migration remain not started.

## V9-06D.6 template integration planning

Planning-only package complete (rerun after crash recovery). Maps V9 static blocks to theme templates/partials, ACF binding/fallbacks, waves D7-A…F, delivery/rollback, and risks. No theme/plugin/V9 source edits, no runtime delivery, no content/ACF writes. Next: V9-06D.7 global shell/asset integration source task (operator review; not authorized here).

## V9-06D7-A global shell asset source

Source-only global shell integration in `WORDPRESS/theme/shpigovsky/`: V9 CSS/JS/fonts/webfonts/shell images packaged from `workspaces/fp-0002-shpigovsky-v9/dist/`; header/footer/offcanvas/modal/scroll markup; enqueue via `inc/assets.php`. No runtime delivery, no DB/content/ACF/menu writes, no plugin or V9 src/dist edits. Validation: `validation/v9-06d7a-global-shell-asset-source/`. Next: V9-06D7-A runtime delivery task (operator review).


## V9-06D7-A runtime delivery

Canonical D7-A theme source delivered to local runtime `wp-content/themes/shpigovsky/` only. Additive/update copy; no deletes; no plugin/core/uploads/ACF JSON changes. Hash match 453/453. Runtime remains deployment target; Git canonical source unchanged post-delivery. Evidence: `validation/v9-06d7a-runtime-delivery/`.

## V9-06D7-B home template source

Source-only home template integration in `WORDPRESS/theme/shpigovsky/`: V9-compatible home template-parts, `inc/home-helpers.php`, intro-section front-page boundary, ACF read/fallback bindings. Theme version `0.4.0-d7b-home`. No runtime delivery, no DB/content/ACF writes, no plugin or V9 src/dist edits. Validation: `validation/v9-06d7b-home-template-source/`. Next: V9-06D7-B runtime delivery task (operator review; not authorized here).


## V9-06D7-B runtime delivery

Canonical D7-B home template source delivered to local runtime `wp-content/themes/shpigovsky/` only. Additive/update copy (1 ADD, 11 MODIFY); no deletes; no plugin/core/uploads/ACF JSON changes. Hash match 454/454. Runtime remains deployment target; Git canonical source unchanged post-delivery. Evidence: `validation/v9-06d7b-runtime-delivery/`.
