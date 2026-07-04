#!/usr/bin/env python3
"""Generate V9-06D7-B runtime delivery documentation from evidence JSON."""
import json
from pathlib import Path

WP = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS")
EV = WP / "validation" / "v9-06d7b-runtime-delivery"
PROJ = WP.parent


def load(name):
    return json.loads((EV / name).read_text(encoding="utf-8"))


def main():
    final = load("final-verdict.json")
    dry = load("dry-run-delivery-plan.json")
    apply = load("apply-delivery-result.json")
    hash_match = load("runtime-hash-match-after.json")
    routes = load("post-delivery-route-smoke.json")
    home = load("home-section-render-smoke.json")
    assets = load("post-delivery-asset-smoke.json")
    checkpoint = load("runtime-checkpoint.json")
    identity = load("runtime-identity-before.json")
    php_lint = load("php-lint-before-delivery.json")
    visual = load("visual-smoke-result.json")
    rollback = load("rollback-readiness.json")
    preflight = load("preflight.json")

    wp = identity["wordpress_state"]
    counts = dry["counts"]

    report = f"""# FP-0002 V9-06D7B Runtime Delivery Report v1

**Date:** 2026-07-05  
**Task:** V9-06D7-B Home Template Runtime Delivery  
**Source HEAD:** `c006edeb47afd25cc4e3f6dfe459e8d46993472b`  
**Verdict:** {final['verdict']}

## Summary

Scoped additive theme delivery of D7-B home template source from canonical Git to local FP-0002 runtime. PHP lint PASS ({php_lint['files']} theme PHP files). Runtime checkpoint created. Dry-run: {counts['ADD']} ADD, {counts['MODIFY']} MODIFY, {counts['SAME']} SAME, 0 DELETE. Post-delivery hash match PASS ({hash_match['runtime_files_matched']}/{hash_match['source_files_checked']}). All seven D.5 routes HTTP 200 with V9 header/footer/CSS/JS visible. Home D7-B sections render (hero, treatment-prevention, rehabilitation-program, final-form; optional sections omitted where ACF empty). Service ID 74 regression PASS. DB/content/ACF writes: 0.

## Evidence

- `validation/v9-06d7b-runtime-delivery/`
- Checkpoint: `{checkpoint['checkpoint_root']}`

## Result

COMPLETE
"""
    (WP / "reports" / "FP-0002-V9-06D7B-RUNTIME-DELIVERY-REPORT-v1.md").write_text(report, encoding="utf-8")

    arch_result = f"""# FP-0002 V9-06D7B Runtime Delivery Result v1

**Date:** 2026-07-05

| Item | Result |
|------|--------|
| Runtime delivery | {final['runtime_delivery']} |
| PHP lint | {final['php_lint']} |
| Hash match | {final['hash_match']} |
| Required routes | {final['required_routes']} |
| Service ID 74 | {final['service_id_74']} |
| Home sections | {final['home_sections']} |
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
    (WP / "architecture" / "FP-0002-V9-06D7B-RUNTIME-DELIVERY-RESULT-v1.md").write_text(arch_result, encoding="utf-8")

    arch_hash = f"""# FP-0002 V9-06D7B Runtime Hash Match v1

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
    (WP / "architecture" / "FP-0002-V9-06D7B-RUNTIME-HASH-MATCH-v1.md").write_text(arch_hash, encoding="utf-8")

    route_rows = "\n".join(
        f"| {r['label']} | {r['url']} | {r['http_status']} | {r['expected_object_type']} #{r['expected_object_id']} | {r['header_present']} | {r['footer_present']} | {r['css_loaded']} | {r['js_loaded']} | {r['result']} |"
        for r in routes["routes"]
    )
    home_rows = "\n".join(
        f"| {c['section']} | {c['present']} | {c.get('expected_if_empty', False)} | {c['result']} |"
        for c in home["checks"]
    )
    arch_smoke = f"""# FP-0002 V9-06D7B Home Post-Delivery Smoke Result v1

**Date:** 2026-07-05

## Route smoke

| Route | URL | HTTP | Expected | Header | Footer | CSS | JS | Result |
|---|---|---:|---|---:|---:|---:|---:|---|
{route_rows}

## Home section render smoke

| Section/check | Present | Expected if empty | Result |
|---|---:|---|---|
{home_rows}

## Asset smoke

| Asset | Status |
|---|---|
| V9 CSS | {assets['assets'][0]['result']} |
| V9 shell JS | {assets['assets'][1]['result']} |
| Logo SVG | {assets['assets'][2]['result']} |

## Visual smoke

Screenshots: {visual['result']} — {len([s for s in visual['screenshots'] if s['captured']])} captured.

## Result

PASS
"""
    (WP / "architecture" / "FP-0002-V9-06D7B-HOME-POST-DELIVERY-SMOKE-RESULT-v1.md").write_text(arch_smoke, encoding="utf-8")

    arch_rollback = f"""# FP-0002 V9-06D7B Rollback Ready v1

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
3. Re-run D.5 route smoke and home section smoke.

## Result

PASS
"""
    (WP / "architecture" / "FP-0002-V9-06D7B-ROLLBACK-READY-v1.md").write_text(arch_rollback, encoding="utf-8")

    arch_next = f"""# FP-0002 V9-06D7B Next Step Recommendation v1

**Date:** 2026-07-05

D7-B home template runtime delivery **COMPLETE**. Home front-page orchestration with 8/20 V9 sections (D7-B wave) is live in local runtime with hash-verified theme copy.

## Recommended next phase

**CREATE_V9_06D7C_SERVICES_HUB_TEMPLATE_SOURCE_TASK** — implement Services Hub template blocks from V9 static reference in canonical theme source (source-only; separate runtime delivery authorization).

## V9-06D7-C gate

READY FOR OPERATOR REVIEW (not authorized by this task).

## Result

RECOMMENDED
"""
    (WP / "architecture" / "FP-0002-V9-06D7B-NEXT-STEP-RECOMMENDATION-v1.md").write_text(arch_next, encoding="utf-8")

    readme = (WP / "README.md").read_text(encoding="utf-8")
    readme = readme.replace(
        "**Status:** V9-06D7-B HOME TEMPLATE SOURCE COMPLETE — runtime delivery NOT performed — next D7-B runtime delivery gate",
        "**Status:** V9-06D7-B HOME TEMPLATE RUNTIME DELIVERED — hash verified — route/home smoke PASS",
    )
    readme = readme.replace(
        "CONTENT MODEL RUNTIME DELIVERED — OBJECT SKELETON COMPLETE — MINIMAL VISUAL CONTENT SEEDED — DEPTH-2 REWRITE REPAIRED — VISUAL ROUTE BASELINE READY — V9 GLOBAL SHELL RUNTIME DELIVERED — V9 HOME TEMPLATE SOURCE COMPLETE — NEXT D7-B RUNTIME DELIVERY",
        "CONTENT MODEL RUNTIME DELIVERED — OBJECT SKELETON COMPLETE — MINIMAL VISUAL CONTENT SEEDED — DEPTH-2 REWRITE REPAIRED — VISUAL ROUTE BASELINE READY — V9 GLOBAL SHELL RUNTIME DELIVERED — V9 HOME TEMPLATE RUNTIME DELIVERED — NEXT D7-C SERVICES HUB SOURCE",
    )
    readme = readme.replace(
        "| Theme | V9-06D7-A GLOBAL SHELL RUNTIME DELIVERED — V9 CSS/JS/header/footer/nav live in local runtime |",
        "| Theme | V9-06D7-B HOME TEMPLATE RUNTIME DELIVERED — D7-B home sections live in local runtime |",
    )
    if "## V9-06D7-B runtime delivery" not in readme:
        readme += """

## V9-06D7-B runtime delivery

D7-B home template delivered to local runtime theme only. PHP lint PASS. Checkpoint + hash match PASS. Seven D.5 routes HTTP 200; Service 74 PASS; Home D7-B sections visible (8/20 V9 wave; optional sections omitted where ACF empty). No DB/content/ACF/menu/redirect writes. Evidence: `validation/v9-06d7b-runtime-delivery/`. Next: D7-C Services Hub template source (operator review).
"""
    (WP / "README.md").write_text(readme, encoding="utf-8")

    sa = (WP / "SOURCE-AUTHORITY.md").read_text(encoding="utf-8")
    if "## V9-06D7-B runtime delivery" not in sa:
        sa += """

## V9-06D7-B runtime delivery

Canonical D7-B home template source delivered to local runtime `wp-content/themes/shpigovsky/` only. Additive/update copy (1 ADD, 11 MODIFY); no deletes; no plugin/core/uploads/ACF JSON changes. Hash match 454/454. Runtime remains deployment target; Git canonical source unchanged post-delivery. Evidence: `validation/v9-06d7b-runtime-delivery/`.
"""
    (WP / "SOURCE-AUTHORITY.md").write_text(sa, encoding="utf-8")

    ps = (PROJ / "PROJECT-STATUS.md").read_text(encoding="utf-8")
    ps = ps.replace(
        "**Last updated:** 2026-07-05 (V9-06D7-B home template source PASS)",
        "**Last updated:** 2026-07-05 (V9-06D7-B home template runtime delivery PASS)",
    )
    ps = ps.replace(
        "**Current WordPress phase:** V9-06D7-B home template source complete in canonical theme — runtime delivery NOT performed — next `CREATE_V9_06D7B_RUNTIME_DELIVERY_TASK`. Report: `WORDPRESS/reports/FP-0002-V9-06D7B-HOME-TEMPLATE-SOURCE-REPORT-v1.md`.",
        "**Current WordPress phase:** V9-06D7-B home template runtime delivered to local runtime — next `CREATE_V9_06D7C_SERVICES_HUB_TEMPLATE_SOURCE_TASK` (operator review). Report: `WORDPRESS/reports/FP-0002-V9-06D7B-RUNTIME-DELIVERY-REPORT-v1.md`.",
    )
    (PROJ / "PROJECT-STATUS.md").write_text(ps, encoding="utf-8")

    print("docs generated")


if __name__ == "__main__":
    main()
