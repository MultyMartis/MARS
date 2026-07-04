# Forge WordPress — FP-0002 Project Lane

**Project ID:** FP-0002 — Шпиговский  
**Stage:** REWRITE-RULE-REPAIR COMPLETE (PASS — Service 74 HTTP 200; V9-06D.5 unblocked)

| Document | Purpose |
|----------|---------|
| [FP-0002-V9-06A1-ARCHITECTURE-RECONCILIATION-REPORT-v1.md](../../../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/architecture/FP-0002-V9-06A1-ARCHITECTURE-RECONCILIATION-REPORT-v1.md) | **V9-06A.1** — reconciliation PASS |
| [FP-0002-WORDPRESS-ARCHITECTURE-v1.md](../../../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/architecture/FP-0002-WORDPRESS-ARCHITECTURE-v1.md) | **V9-06A** — WordPress IA, content model, template system |
| [FP-0002-V9-06B-SKELETON-IMPLEMENTATION-REPORT-v1.md](../../../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/reports/FP-0002-V9-06B-SKELETON-IMPLEMENTATION-REPORT-v1.md) | **V9-06B** — theme + core skeleton PASS |
| [FP-0002-V9-06C-CONTENT-MODEL-SOURCE-IMPLEMENTATION-REPORT-v1.md](../../../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/reports/FP-0002-V9-06C-CONTENT-MODEL-SOURCE-IMPLEMENTATION-REPORT-v1.md) | **V9-06C** — content model source implementation PASS |
| [FP-0002-V9-06C1-SOURCE-ACTIVATION-GATE-RESOLUTION-REPORT-v1.md](../../../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/reports/FP-0002-V9-06C1-SOURCE-ACTIVATION-GATE-RESOLUTION-REPORT-v1.md) | **V9-06C.1** — source activation gate resolution PASS |
| [FP-0002-V9-06D1-RERUN-RUNTIME-DELIVERY-CONTENT-MODEL-ACTIVATION-REPORT-v1.md](../../../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/reports/FP-0002-V9-06D1-RERUN-RUNTIME-DELIVERY-CONTENT-MODEL-ACTIVATION-REPORT-v1.md) | **V9-06D.1 rerun** — runtime delivery + content model activation PASS |
| [FP-0002-OD-002-ROUTE-AUTHORITY-v1.md](../../../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/architecture/FP-0002-OD-002-ROUTE-AUTHORITY-v1.md) | OD-002 final route authority |
| [FP-0002-FW-07C-2C-FILESYSTEM-DELIVERY-PROOF-RECEIPT-v1.md](FP-0002-FW-07C-2C-FILESYSTEM-DELIVERY-PROOF-RECEIPT-v1.md) | **FW-07C-2C PASS** — bounded filesystem delivery + rollback proof |
| [FP-0002-FW-07C-2B-WPILOT-LOCAL-WRITE-PROOF-RECEIPT-v1.md](FP-0002-FW-07C-2B-WPILOT-LOCAL-WRITE-PROOF-RECEIPT-v1.md) | **FW-07C-2B PASS** — local WPilot write lifecycle proof |
| [FP-0002-FW-07C-2-MUTATION-CHARTER-v1.md](FP-0002-FW-07C-2-MUTATION-CHARTER-v1.md) | **BOUNDED — FW-07C-2C PROVEN** — controlled mutation programme |
| [FP-0002-V9-05B-PRE-IMPLEMENTATION-CHECKPOINT-SUMMARY-v1.md](FP-0002-V9-05B-PRE-IMPLEMENTATION-CHECKPOINT-SUMMARY-v1.md) | **Current** — V9 pre-implementation runtime checkpoint |
| [FP-0002-V9-05A-FOUNDATION-ADOPTION-SUMMARY-v1.md](FP-0002-V9-05A-FOUNDATION-ADOPTION-SUMMARY-v1.md) | V9 intake + foundation adoption |
| [FP-0002-WORDPRESS-FOUNDATION-REPORT-v1.md](FP-0002-WORDPRESS-FOUNDATION-REPORT-v1.md) | Foundation matrix + FW-06A evidence |
| [FP-0002-WORDPRESS-FOUNDATION-PREFLIGHT-v1.md](FP-0002-WORDPRESS-FOUNDATION-PREFLIGHT-v1.md) | Preflight + authority |
| [FP-0002-FW-06B-APPROVED-FRONTEND-INTAKE-INPUT-v1.md](FP-0002-FW-06B-APPROVED-FRONTEND-INTAKE-INPUT-v1.md) | Historical FW-06B input (superseded by V9-05A) |

**V9 intake authority:** `workspaces/fp-0002-shpigovsky-v9/forge-intake/`

Runtime manifest: [MLI-WP-FP0002-LOCAL-RUNTIME-MANIFEST-v1.md](../../../../mars-localhost-infrastructure/manifests/MLI-WP-FP0002-LOCAL-RUNTIME-MANIFEST-v1.md)

## V9-06B.2 ACF dependency admission

| Document | Purpose |
|----------|---------|
| [FP-0002-V9-06B2-ACF-OPERATOR-DEPENDENCY-ADMISSION-REPORT-v1.md](../../../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/reports/FP-0002-V9-06B2-ACF-OPERATOR-DEPENDENCY-ADMISSION-REPORT-v1.md) | **V9-06B.2** — operator-managed ACF PRO admission PASS |
| [FP-0002-OPERATOR-MANAGED-EXTERNAL-PLUGINS-v1.md](../../../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/architecture/FP-0002-OPERATOR-MANAGED-EXTERNAL-PLUGINS-v1.md) | ACF PRO / ACF Extended PRO update-ignore and delivery-deny registry |

## V9-06C source implementation

| Surface | Status |
|---|---|
| WordPress source implementation | CONTENT MODEL COMPLETE |
| Service CPT source | IMPLEMENTED |
| Service permalink source | IMPLEMENTED |
| ACF Pro field groups | SOURCE IMPLEMENTED |
| ACF JSON | SOURCE CREATED |
| Options Page | SOURCE IMPLEMENTED |
| Admin UX | SOURCE IMPLEMENTED |
| Validation hooks | SOURCE IMPLEMENTED |
| Source activation gate | RESOLVED — CONTENT_MODEL |
| Runtime delivery | COMPLETE — V9-06D.1 rerun |
| WordPress objects | SKELETON COMPLETE (15 Services) — CONTENT NOT MIGRATED |

## V9-06C.1 source activation gate

| Surface | Status |
|---|---|
| Shpigovsky Core mode | CONTENT_MODEL |
| Legacy skeleton flag | FALSE_OR_COMPAT_DERIVED |
| Content model modules | ENABLED_IN_SOURCE |
| Migrations | DISABLED |
| Forms | DISABLED |
| Runtime delivery | NOT PERFORMED |
| V9-06D.1 rerun | COMPLETE — PASS |


## V9-06D.1 rerun runtime delivery

Runtime code/model activation is complete in local runtime: theme, Shpigovsky Core, and ACF JSON delivered; service CPT, 13 ACF groups, and Options Page verified. WordPress object skeleton complete (V9-06D.2); content migration planned (V9-06D.3); minimal visual content seed applied for Pages 4/5/20 and Services 73/74/77/84 (V9-06D.4 RERUN). Soft rewrite flush performed (REWRITE-FLUSH-MICRO-GATE); route ownership investigation identified `POST_TYPE_LINK_REWRITE_MISMATCH`. Rewrite rule repair **PASS**: depth-2 query `service=$matches[1]/$matches[2]`; Service 74 HTTP 200. Page 6 / Service 73 collision remains secondary debt. Full content migration and V9 integration remain not performed. Next: V9-06D.5 visual route QA.
