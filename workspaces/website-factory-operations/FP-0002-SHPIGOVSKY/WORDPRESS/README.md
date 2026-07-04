# FP-0002 Canonical WordPress Source Surface

**Project:** FP-0002 — Шпиговский  
**Surface:** `WORDPRESS/`  
**Status:** V9-06D.6 TEMPLATE INTEGRATION PLANNING COMPLETE (PASS — planning/docs only; V9 integration NOT_STARTED)
**Classification:** CONTENT MODEL RUNTIME DELIVERED — OBJECT SKELETON COMPLETE — MINIMAL VISUAL CONTENT SEEDED — DEPTH-2 REWRITE REPAIRED — VISUAL ROUTE BASELINE READY — V9 TEMPLATE INTEGRATION PLAN COMPLETE — NEXT D7-A GLOBAL SHELL/ASSETS

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
| Runtime changes | **AUTHORIZED FILE DELIVERY (V9-06D.1 rerun) + AUTHORIZED OBJECT SKELETON (V9-06D.2)** |
| WordPress source implementation | **CONTENT MODEL COMPLETE** |
| WordPress runtime implementation | **CONTENT MODEL ACTIVATED — 15 SERVICE OBJECTS CREATED / PAGE TEMPLATES RECONCILED** |
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
| Shpigovsky Core | V9-06D.2 CONTENT MODEL RUNTIME DELIVERED — OBJECT SKELETON COMPLETE |
| ACF JSON | V9-06D.1 DELIVERED — 13 LOCAL JSON FILES; V9-06D.2 object meta only |

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
- `reports/FP-0002-V9-06D1-RERUN-RUNTIME-DELIVERY-CONTENT-MODEL-ACTIVATION-REPORT-v1.md` — V9-06D.1 rerun PASS; runtime code/model activation complete


## V9-06D.1 rerun runtime delivery (2026-07-04)

V9-06D.1 rerun delivered `theme/shpigovsky`, `plugins/shpigovsky-core`, and 13 `acf-json` files into the local runtime under checkpoint control. Service CPT, ACF local field groups, Options Page, admin hooks, validation hooks, and runtime health are verified. WordPress object creation, content migration, redirects, rewrite flush, plugin updates/install/deletes, and V9 integration remain not started.


## V9-06D.2 WordPress object skeleton (2026-07-04)

V9-06D.2 created the controlled WordPress object skeleton in the local FP-0002 runtime: 15 `service` CPT objects with registry metadata and hierarchy, 0 new Pages, 13 existing Page template assignments, 0 Posts, 0 menu changes, 0 option changes, 0 redirects, and no rewrite flush. Content migration and V9 integration remain not started.

Report: `reports/FP-0002-V9-06D2-WORDPRESS-OBJECT-SKELETON-REPORT-v1.md`.


## V9-06D.3 content migration planning (2026-07-04)

Planning-only phase complete: route/object matrices, ACF fill strategy, and minimal visual content seed plan. Runtime content writes: 0.

Report: `reports/FP-0002-V9-06D3-CONTENT-MIGRATION-PLANNING-REPORT-v1.md`.


## V9-06D.4 RERUN minimal content seed for visual route QA (2026-07-04)

Authorized minimal ACF/meta seed applied to Pages 4/5/20 and Services 73/74/77/84 under DB checkpoint control. Full content migration, V9 HTML/CSS/JS integration, menus, redirects, and Options Page values were not performed.

### REWRITE-FLUSH-MICRO-GATE (2026-07-04)

Soft rewrite flush performed under DB checkpoint (`wp rewrite flush`, no `--hard`, `.htaccess` unchanged). Options changed: `rewrite_rules` only. Service 74 generated permalink still matches expected path but HTTP remains **404** — classification `FLUSH_NOT_SUFFICIENT`. Report: [reports/FP-0002-REWRITE-FLUSH-MICRO-GATE-REPORT-v1.md](reports/FP-0002-REWRITE-FLUSH-MICRO-GATE-REPORT-v1.md).

### ROUTE-OWNERSHIP-INVESTIGATION (2026-07-04)

Read-only diagnostics complete. Primary cause: **POST_TYPE_LINK_REWRITE_MISMATCH** — depth-2 rewrite maps `service=$matches[2]` (leaf only) while hierarchical CPT lookup requires `parent/child`. Page ID 6 / Service ID 73 shared path **CONFIRMED** as secondary ownership debt, not the direct Service 74 404 mechanism. Recommended next: rewrite rule repair micro-task. V9-06D.5: **BLOCKED**. Runtime mutations: 0.

### REWRITE-RULE-REPAIR (2026-07-04)

Depth-2 rewrite query repaired to `service=$matches[1]/$matches[2]` in `ServicePermalinks.php`; delivered to local runtime; soft flush under checkpoint. Service 74 HTTP **200** (resolved ID 74). Controls all 200. Content/ACF/menus/redirects unchanged. V9-06D.5: **UNBLOCKED**. Report: [reports/FP-0002-REWRITE-RULE-REPAIR-REPORT-v1.md](reports/FP-0002-REWRITE-RULE-REPAIR-REPORT-v1.md).

### V9-06D.5 visual route QA (2026-07-04)

Read-only visual route QA after rewrite repair: all seven required routes HTTP **200**; Service 74 regression **PASS**; header/footer/main present; desktop/mobile screenshots captured; theme remains V9-06B skeleton (no V9 integration). Runtime mutations: **0**. Verdict: **PARTIAL PASS**. Report: [reports/FP-0002-V9-06D5-VISUAL-ROUTE-QA-REPORT-v1.md](reports/FP-0002-V9-06D5-VISUAL-ROUTE-QA-REPORT-v1.md).

### V9-06D.6 template integration planning (2026-07-04)

Planning-only rerun after Cursor crash recovery (`D6_RECOVERABLE_RESUME_READY`). Static→WP matrix, ACF binding, component/asset plan, integration waves D7-A…F, runtime delivery/rollback plan, and risk register complete. V9 integration and theme/plugin source changes: **NOT STARTED**. Next: `CREATE_V9_06D7_GLOBAL_SHELL_ASSET_INTEGRATION_SOURCE_TASK` (operator review). Report: [reports/FP-0002-V9-06D6-TEMPLATE-INTEGRATION-PLANNING-REPORT-v1.md](reports/FP-0002-V9-06D6-TEMPLATE-INTEGRATION-PLANNING-REPORT-v1.md). Crash recovery: [reports/FP-0002-V9-06D6-CURSOR-CRASH-RECOVERY-AUDIT-REPORT-v1.md](reports/FP-0002-V9-06D6-CURSOR-CRASH-RECOVERY-AUDIT-REPORT-v1.md).

Reports:

- `reports/FP-0002-V9-06D6-TEMPLATE-INTEGRATION-PLANNING-REPORT-v1.md` — D.6 planning PASS
- `reports/FP-0002-V9-06D6-CURSOR-CRASH-RECOVERY-AUDIT-REPORT-v1.md` — crash recovery PASS
- `reports/FP-0002-V9-06D5-VISUAL-ROUTE-QA-REPORT-v1.md` — D.5 visual route QA PARTIAL PASS
- `reports/FP-0002-REWRITE-RULE-REPAIR-REPORT-v1.md` — repair PASS
- `reports/FP-0002-ROUTE-OWNERSHIP-INVESTIGATION-REPORT-v1.md` — investigation PASS
- `reports/FP-0002-V9-06D4-RERUN-MINIMAL-CONTENT-SEED-FOR-VISUAL-ROUTE-QA-REPORT-v1.md` — rerun PASS/PARTIAL
- `reports/FP-0002-V9-06D4-MINIMAL-CONTENT-SEED-FOR-VISUAL-ROUTE-QA-REPORT-v1.md` — previous blocked attempt (HEAD mismatch), preserved
- `reports/FP-0002-REWRITE-FLUSH-MICRO-GATE-REPORT-v1.md` — flush micro-gate PARTIAL PASS
