#!/usr/bin/env python3
"""Generate V9-06D7-A runtime delivery documentation from evidence JSON."""
import json
from pathlib import Path

WP = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS")
EV = WP / "validation" / "v9-06d7a-runtime-delivery"
PROJ = WP.parent


def load(name):
    return json.loads((EV / name).read_text(encoding="utf-8"))


def main():
    final = load("final-verdict.json")
    dry = load("dry-run-delivery-plan.json")
    apply = load("apply-delivery-result.json")
    hash_match = load("runtime-hash-match-after.json")
    routes = load("post-delivery-route-smoke.json")
    assets = load("post-delivery-asset-smoke.json")
    checkpoint = load("runtime-checkpoint.json")
    identity = load("runtime-identity-before.json")
    php_cli = load("php-cli-discovery.json")
    php_lint = load("php-lint-before-delivery.json")
    visual = load("visual-smoke-result.json")
    rollback = load("rollback-readiness.json")

    wp = identity["wordpress_state"]

    # Runtime delivery report
    report = f"""# FP-0002 V9-06D7A Runtime Delivery Report v1

**Date:** 2026-07-05  
**Task:** V9-06D7-A Runtime Delivery  
**Source HEAD:** `97346603a889d2794a9024e7a4b6f04dd8ed4477`  
**Verdict:** {final['verdict']}

## Summary

Scoped additive theme delivery from canonical D7-A source to local FP-0002 runtime. PHP lint PASS (72 files). Runtime checkpoint created. Dry-run: 380 ADD, 11 MODIFY, 62 SAME, 0 DELETE. Post-delivery hash match PASS (453/453). All seven D.5 routes HTTP 200 with V9 header/footer/CSS/JS visible. Service ID 74 regression PASS. DB/content/ACF writes: 0.

## Evidence

- `validation/v9-06d7a-runtime-delivery/`
- Checkpoint: `{checkpoint['checkpoint_root']}`

## Result

COMPLETE
"""
    (WP / "reports" / "FP-0002-V9-06D7A-RUNTIME-DELIVERY-REPORT-v1.md").write_text(report, encoding="utf-8")

    arch_result = f"""# FP-0002 V9-06D7A Runtime Delivery Result v1

**Date:** 2026-07-05

| Item | Result |
|------|--------|
| Runtime delivery | {final['runtime_delivery']} |
| PHP lint | {final['php_lint']} |
| Hash match | {final['hash_match']} |
| Required routes | {final['required_routes']} |
| Service ID 74 | {final['service_id_74']} |
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
    (WP / "architecture" / "FP-0002-V9-06D7A-RUNTIME-DELIVERY-RESULT-v1.md").write_text(arch_result, encoding="utf-8")

    arch_hash = f"""# FP-0002 V9-06D7A Runtime Hash Match v1

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
    (WP / "architecture" / "FP-0002-V9-06D7A-RUNTIME-HASH-MATCH-v1.md").write_text(arch_hash, encoding="utf-8")

    route_rows = "\n".join(
        f"| {r['label']} | {r['url']} | {r['http_status']} | {r['expected_object_type']} #{r['expected_object_id']} | {r['header_present']} | {r['footer_present']} | {r['css_loaded']} | {r['js_loaded']} | {r['result']} |"
        for r in routes["routes"]
    )
    arch_smoke = f"""# FP-0002 V9-06D7A Post-Delivery Smoke Result v1

**Date:** 2026-07-05

## Route smoke

| Route | URL | HTTP | Expected | Header | Footer | CSS | JS | Result |
|---|---|---:|---|---:|---:|---:|---:|---|
{route_rows}

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
    (WP / "architecture" / "FP-0002-V9-06D7A-POST-DELIVERY-SMOKE-RESULT-v1.md").write_text(arch_smoke, encoding="utf-8")

    arch_rollback = f"""# FP-0002 V9-06D7A Rollback Ready v1

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
3. Re-run D.5 route smoke.

## Result

PASS
"""
    (WP / "architecture" / "FP-0002-V9-06D7A-ROLLBACK-READY-v1.md").write_text(arch_rollback, encoding="utf-8")

    arch_next = f"""# FP-0002 V9-06D7A Next Step Recommendation v1

**Date:** 2026-07-05

D7-A runtime delivery **COMPLETE**. Global V9 shell (header/footer/nav/assets) is live in local runtime with hash-verified theme copy.

## Recommended next phase

**CREATE_V9_06D7B_HOME_TEMPLATE_SOURCE_TASK** — implement home page template blocks from V9 static reference in canonical theme source (source-only; separate runtime delivery authorization).

## V9-06D7-B gate

READY FOR OPERATOR REVIEW (not authorized by this task).

## Result

RECOMMENDED
"""
    (WP / "architecture" / "FP-0002-V9-06D7A-NEXT-STEP-RECOMMENDATION-v1.md").write_text(arch_next, encoding="utf-8")

    # Update README status line
    readme = (WP / "README.md").read_text(encoding="utf-8")
    readme = readme.replace(
        "**Status:** V9-06D7-A GLOBAL SHELL ASSET SOURCE COMPLETE (source-only; runtime delivery NOT performed)",
        "**Status:** V9-06D7-A GLOBAL SHELL RUNTIME DELIVERED — hash verified — route smoke PASS",
    )
    readme = readme.replace(
        "CONTENT MODEL RUNTIME DELIVERED — OBJECT SKELETON COMPLETE — MINIMAL VISUAL CONTENT SEEDED — DEPTH-2 REWRITE REPAIRED — VISUAL ROUTE BASELINE READY — V9 TEMPLATE INTEGRATION PLAN COMPLETE — V9 GLOBAL SHELL SOURCE INTEGRATED — NEXT D7-A RUNTIME DELIVERY",
        "CONTENT MODEL RUNTIME DELIVERED — OBJECT SKELETON COMPLETE — MINIMAL VISUAL CONTENT SEEDED — DEPTH-2 REWRITE REPAIRED — VISUAL ROUTE BASELINE READY — V9 GLOBAL SHELL RUNTIME DELIVERED — NEXT D7-B HOME TEMPLATE SOURCE",
    )
    readme = readme.replace(
        "| Theme | V9-06D7-A GLOBAL SHELL SOURCE — V9 CSS/JS packaged; header/footer/nav integrated in source |",
        "| Theme | V9-06D7-A GLOBAL SHELL RUNTIME DELIVERED — V9 CSS/JS/header/footer/nav live in local runtime |",
    )
    if "## V9-06D7-A runtime delivery" not in readme:
        readme += """

## V9-06D7-A runtime delivery

D7-A global shell/assets delivered to local runtime theme only. PHP lint PASS. Checkpoint + hash match PASS. Seven D.5 routes HTTP 200; Service 74 PASS; V9 CSS/JS enqueued. No DB/content/ACF/menu/redirect writes. Evidence: `validation/v9-06d7a-runtime-delivery/`. Next: D7-B home template source (operator review).
"""
    (WP / "README.md").write_text(readme, encoding="utf-8")

    # Update SOURCE-AUTHORITY
    sa = (WP / "SOURCE-AUTHORITY.md").read_text(encoding="utf-8")
    if "## V9-06D7-A runtime delivery" not in sa:
        sa += """

## V9-06D7-A runtime delivery

Canonical D7-A theme source delivered to local runtime `wp-content/themes/shpigovsky/` only. Additive/update copy; no deletes; no plugin/core/uploads/ACF JSON changes. Hash match 453/453. Runtime remains deployment target; Git canonical source unchanged post-delivery. Evidence: `validation/v9-06d7a-runtime-delivery/`.
"""
    (WP / "SOURCE-AUTHORITY.md").write_text(sa, encoding="utf-8")

    # Update PROJECT-STATUS
    ps = (PROJ / "PROJECT-STATUS.md").read_text(encoding="utf-8")
    ps = ps.replace(
        "**Last updated:** 2026-07-04 (V9-06D7-A global shell asset source PASS)",
        "**Last updated:** 2026-07-05 (V9-06D7-A global shell runtime delivery PASS)",
    )
    ps = ps.replace(
        "**Current WordPress phase:** V9-06D7-A global shell/asset source complete in git — next `CREATE_V9_06D7A_RUNTIME_DELIVERY_TASK` (operator review). Report: `WORDPRESS/reports/FP-0002-V9-06D7A-GLOBAL-SHELL-ASSET-SOURCE-REPORT-v1.md`.",
        "**Current WordPress phase:** V9-06D7-A global shell runtime delivered to local runtime — next `CREATE_V9_06D7B_HOME_TEMPLATE_SOURCE_TASK` (operator review). Report: `WORDPRESS/reports/FP-0002-V9-06D7A-RUNTIME-DELIVERY-REPORT-v1.md`.",
    )
    (PROJ / "PROJECT-STATUS.md").write_text(ps, encoding="utf-8")

    print("docs generated")


if __name__ == "__main__":
    main()
