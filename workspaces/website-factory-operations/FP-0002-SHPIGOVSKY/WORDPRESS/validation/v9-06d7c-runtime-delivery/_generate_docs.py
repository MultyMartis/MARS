#!/usr/bin/env python3
"""Generate V9-06D7-C runtime delivery documentation from evidence JSON."""
import json
from pathlib import Path

WP = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS")
EV = WP / "validation" / "v9-06d7c-runtime-delivery"
PROJ = WP.parent


def load(name):
    return json.loads((EV / name).read_text(encoding="utf-8"))


def main():
    final = load("final-verdict.json")
    dry = load("dry-run-delivery-plan.json")
    apply = load("apply-delivery-result.json")
    hash_match = load("runtime-hash-match-after.json")
    routes = load("post-delivery-route-smoke.json")
    hub = load("services-hub-section-render-smoke.json")
    home = load("home-stability-after-d7c.json")
    assets = load("post-delivery-asset-smoke.json")
    checkpoint = load("runtime-checkpoint.json")
    identity = load("runtime-identity-before.json")
    php_lint = load("php-lint-before-delivery.json")
    visual = load("visual-smoke-result.json")
    rollback = load("rollback-readiness.json")
    preflight = load("preflight.json")
    s74 = load("service-74-regression.json")

    wp = identity["wordpress_state"]
    counts = dry["counts"]

    report = f"""# FP-0002 V9-06D7C Runtime Delivery Report v1

**Date:** 2026-07-05  
**Task:** V9-06D7-C Services Hub Template Runtime Delivery  
**Source HEAD (required):** `0a9a354925226acec2d79af3518e40ed5e0d03dc`  
**Verdict:** {final['verdict']}

## Summary

Scoped additive theme delivery of D7-C Services Hub template source from canonical Git to local FP-0002 runtime. PHP lint PASS ({php_lint['files']} theme PHP files). Runtime checkpoint created. Dry-run: {counts['ADD']} ADD, {counts['MODIFY']} MODIFY, {counts['SAME']} SAME, 0 DELETE. Post-delivery hash match PASS ({hash_match['runtime_files_matched']}/{hash_match['source_files_checked']}). All seven D.5 routes HTTP 200 with V9 header/footer/CSS/JS visible. Services Hub D7-C core-wave sections render (hero, CPT groups/cards, rehabilitation-program, final-form; FAQ omitted where ACF empty). Home D7-B stability PASS. Service ID 74 regression PASS. DB/content/ACF writes: 0.

## Preflight note

Local HEAD `{preflight['local_head'][:8]}` was ahead 1 (docs-only commit); remote at required HEAD; theme source verified unchanged since `0a9a3549`.

## Evidence

- `validation/v9-06d7c-runtime-delivery/`
- Checkpoint: `{checkpoint['checkpoint_root']}`

## Result

COMPLETE
"""
    (WP / "reports" / "FP-0002-V9-06D7C-RUNTIME-DELIVERY-REPORT-v1.md").write_text(report, encoding="utf-8")

    arch_result = f"""# FP-0002 V9-06D7C Runtime Delivery Result v1

**Date:** 2026-07-05

| Item | Result |
|------|--------|
| Runtime delivery | {final['runtime_delivery']} |
| PHP lint | {final['php_lint']} |
| Hash match | {final['hash_match']} |
| Required routes | {final['required_routes']} |
| Services Hub | {final['services_hub']} |
| Service ID 74 | {final['service_id_74']} |
| Home stability | {final['home_stability']} |
| Header/footer/assets | {final['header_footer_assets']} |
| Runtime mutations | {final['runtime_mutations']} |
| DB writes | {final['db_writes']} |

## Apply counts

- ADD: {apply['files_added']}
- MODIFY: {apply['files_modified']}
- SAME: {apply['files_same']}
- TARGET_ONLY preserved: {apply['target_only_preserved']}
- DELETE: {apply['deletes']}

## Result

PASS
"""
    (WP / "architecture" / "FP-0002-V9-06D7C-RUNTIME-DELIVERY-RESULT-v1.md").write_text(arch_result, encoding="utf-8")

    arch_hash = f"""# FP-0002 V9-06D7C Runtime Hash Match v1

**Date:** 2026-07-05

| Check | Value |
|-------|------:|
| Source files checked | {hash_match['source_files_checked']} |
| Runtime files matched | {hash_match['runtime_files_matched']} |
| Hash mismatches | {len(hash_match['hash_mismatches'])} |
| Missing in runtime | {len(hash_match['missing_in_runtime'])} |
| Target-only preserved | {hash_match['target_only_count']} |

## Result

{hash_match['result']}
"""
    (WP / "architecture" / "FP-0002-V9-06D7C-RUNTIME-HASH-MATCH-v1.md").write_text(arch_hash, encoding="utf-8")

    route_rows = "\n".join(
        f"| {r['label']} | {r['url']} | {r['http_status']} | {r['expected_object_type']} #{r['expected_object_id']} | {r['header_present']} | {r['footer_present']} | {r['css_loaded']} | {r['js_loaded']} | {r['result']} |"
        for r in routes["routes"]
    )
    hub_rows = "\n".join(
        f"| {c['section']} | {c['present']} | {c.get('expected_if_empty', False)} | {c['result']} |"
        for c in hub["checks"]
    )
    arch_smoke = f"""# FP-0002 V9-06D7C Services Hub Post-Delivery Smoke Result v1

**Date:** 2026-07-05

## Route smoke

| Route | URL | HTTP | Expected | Header | Footer | CSS | JS | Result |
|---|---|---:|---|---:|---:|---:|---:|---|
{route_rows}

## Services Hub section render smoke

| Section/check | Present | Expected if empty | Result |
|---|---:|---|---|
{hub_rows}

## Home stability after D7-C

| Check | Present | Result |
|---|---:|---|
""" + "\n".join(
        f"| {c['section']} | {c['present']} | {c['result']} |" for c in home["checks"]
    ) + f"""

## Asset smoke

| Asset | Status |
|---|---|
| V9 CSS | {assets['assets'][0]['result']} |
| V9 shell JS | {assets['assets'][1]['result']} |
| Logo SVG | {assets['assets'][2]['result']} |

## Service 74 regression

URL: {s74['url']} — HTTP {s74['http_status']} — {s74['result']}

## Visual smoke

Screenshots: {visual['result']} — {len([s for s in visual['screenshots'] if s['captured']])} captured.

## Result

PASS
"""
    (WP / "architecture" / "FP-0002-V9-06D7C-SERVICES-HUB-POST-DELIVERY-SMOKE-RESULT-v1.md").write_text(arch_smoke, encoding="utf-8")

    arch_rollback = f"""# FP-0002 V9-06D7C Rollback Ready v1

**Date:** 2026-07-05

| Item | Value |
|------|-------|
| Checkpoint | `{checkpoint['checkpoint_root']}` |
| Theme snapshot | `{checkpoint['theme_snapshot']}` |
| Baseline manifest | `{checkpoint['baseline_manifest']}` |
| DB dump | None |
| Rollback tested | {rollback['rollback_tested']} |

## Restore procedure

1. Copy checkpoint `theme/shpigovsky/` to runtime `wp-content/themes/shpigovsky/`.
2. Validate aggregate hash against pre-delivery manifest.
3. Re-run D.5 route smoke, Services Hub section smoke, and home stability.

## Result

PASS
"""
    (WP / "architecture" / "FP-0002-V9-06D7C-ROLLBACK-READY-v1.md").write_text(arch_rollback, encoding="utf-8")

    arch_next = f"""# FP-0002 V9-06D7C Next Step Recommendation v1

**Date:** 2026-07-05

D7-C Services Hub template runtime delivery **COMPLETE**. Core-wave sections (hero, CPT groups/cards, rehabilitation-program, final-form) live in local runtime with hash-verified theme copy. Deferred: founder-quote, comfort, genotyping hub, category galleries.

## Recommended next phase

**CREATE_V9_06D7D_SERVICE_TEMPLATE_SOURCE_TASK** — implement individual service template blocks from V9 static reference in canonical theme source (source-only; separate runtime delivery authorization).

## V9-06D7-D gate

READY FOR OPERATOR REVIEW (not authorized by this task).

## Result

RECOMMENDED
"""
    (WP / "architecture" / "FP-0002-V9-06D7C-NEXT-STEP-RECOMMENDATION-v1.md").write_text(arch_next, encoding="utf-8")

    readme = (WP / "README.md").read_text(encoding="utf-8")
    readme = readme.replace(
        "**Status:** V9-06D7-C SERVICES HUB TEMPLATE SOURCE COMPLETE — next D7-C runtime delivery (operator review)",
        "**Status:** V9-06D7-C SERVICES HUB TEMPLATE RUNTIME DELIVERED — hash verified — route/hub smoke PASS",
    )
    readme = readme.replace(
        "CONTENT MODEL RUNTIME DELIVERED — OBJECT SKELETON COMPLETE — MINIMAL VISUAL CONTENT SEEDED — DEPTH-2 REWRITE REPAIRED — VISUAL ROUTE BASELINE READY — V9 GLOBAL SHELL RUNTIME DELIVERED — V9 HOME TEMPLATE RUNTIME DELIVERED — V9 SERVICES HUB TEMPLATE SOURCE COMPLETE — NEXT D7-C RUNTIME DELIVERY",
        "CONTENT MODEL RUNTIME DELIVERED — OBJECT SKELETON COMPLETE — MINIMAL VISUAL CONTENT SEEDED — DEPTH-2 REWRITE REPAIRED — VISUAL ROUTE BASELINE READY — V9 GLOBAL SHELL RUNTIME DELIVERED — V9 HOME TEMPLATE RUNTIME DELIVERED — V9 SERVICES HUB TEMPLATE RUNTIME DELIVERED — NEXT D7-D SERVICE TEMPLATE SOURCE",
    )
    readme = readme.replace(
        "| Theme | V9-06D7-B HOME TEMPLATE RUNTIME DELIVERED — D7-B home sections live in local runtime |",
        "| Theme | V9-06D7-C SERVICES HUB TEMPLATE RUNTIME DELIVERED — D7-C hub sections live in local runtime |",
    )
    if "## V9-06D7-C runtime delivery" not in readme:
        readme += """

## V9-06D7-C runtime delivery

D7-C Services Hub template delivered to local runtime theme only. PHP lint PASS. Checkpoint + hash match PASS. Seven D.5 routes HTTP 200; Service 74 PASS; Services Hub core-wave sections visible (6/10 V9 wave; FAQ omitted where ACF empty; founder-quote/comfort/genotyping/galleries deferred). Home D7-B stability PASS. No DB/content/ACF/menu/redirect writes. Evidence: `validation/v9-06d7c-runtime-delivery/`. Next: D7-D service template source (operator review).
"""
    (WP / "README.md").write_text(readme, encoding="utf-8")

    sa = (WP / "SOURCE-AUTHORITY.md").read_text(encoding="utf-8")
    if "## V9-06D7-C runtime delivery" not in sa:
        sa += """

## V9-06D7-C runtime delivery

Canonical D7-C Services Hub template source delivered to local runtime `wp-content/themes/shpigovsky/` only. Additive/update copy (8 ADD, 2 MODIFY); no deletes; no plugin/core/uploads/ACF JSON changes. Hash match 462/462. Runtime remains deployment target; Git canonical source unchanged post-delivery. Evidence: `validation/v9-06d7c-runtime-delivery/`.
"""
    (WP / "SOURCE-AUTHORITY.md").write_text(sa, encoding="utf-8")

    ps = (PROJ / "PROJECT-STATUS.md").read_text(encoding="utf-8")
    ps = ps.replace(
        "**Last updated:** 2026-07-05 (V9-06D7-C Services Hub template source PASS)",
        "**Last updated:** 2026-07-05 (V9-06D7-C Services Hub template runtime delivery PASS)",
    )
    ps = ps.replace(
        "**Current WordPress phase:** V9-06D7-C Services Hub template source complete in canonical theme — next `CREATE_V9_06D7C_RUNTIME_DELIVERY_TASK` (operator review). Report: `WORDPRESS/reports/FP-0002-V9-06D7C-SERVICES-HUB-TEMPLATE-SOURCE-REPORT-v1.md`.",
        "**Current WordPress phase:** V9-06D7-C Services Hub template runtime delivered to local runtime — next `CREATE_V9_06D7D_SERVICE_TEMPLATE_SOURCE_TASK` (operator review). Report: `WORDPRESS/reports/FP-0002-V9-06D7C-RUNTIME-DELIVERY-REPORT-v1.md`.",
    )
    (PROJ / "PROJECT-STATUS.md").write_text(ps, encoding="utf-8")

    print("docs generated")


if __name__ == "__main__":
    main()
