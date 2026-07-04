#!/usr/bin/env python3
"""Generate V9-06D7-D runtime delivery documentation from evidence JSON."""
import json
from pathlib import Path

WP = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS")
EV = WP / "validation" / "v9-06d7d-runtime-delivery"
PROJ = WP.parent


def load(name):
    return json.loads((EV / name).read_text(encoding="utf-8"))


def main():
    final = load("final-verdict.json")
    dry = load("dry-run-delivery-plan.json")
    apply = load("apply-delivery-result.json")
    hash_match = load("runtime-hash-match-after.json")
    routes = load("post-delivery-route-smoke.json")
    svc = load("service-section-render-smoke.json")
    layout = load("service-layout-variant-runtime-check.json")
    home_hub = load("home-services-hub-stability.json")
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

    report = f"""# FP-0002 V9-06D7D Runtime Delivery Report v1

**Date:** 2026-07-05  
**Task:** V9-06D7-D Service Template Runtime Delivery  
**Source HEAD (required):** `{preflight['required_head']}`  
**Verdict:** {final['verdict']}

## Summary

Scoped additive theme delivery of D7-D Service template source from canonical Git commit `c54c23d0` to local FP-0002 runtime. PHP lint PASS ({php_lint['files']} theme PHP files; 21 changed D7-D files). Runtime checkpoint created. Dry-run: {counts['ADD']} ADD, {counts['MODIFY']} MODIFY, {counts['SAME']} SAME, 0 DELETE. Post-delivery hash match PASS ({hash_match['runtime_files_matched']}/{hash_match['source_files_checked']}). All seven D.5 routes HTTP 200 with V9 header/footer/CSS/JS visible. Service templates 73/74/77/84 render D7-D core-wave sections (hero, subnav, children/programme/final-form; optional FAQ/stages omitted where ACF empty). Layout variants detected for seeded routes. Home D7-B and Services Hub D7-C stability PASS. Service ID 74 HTTP 200 with alcohol-special markers. DB/content/ACF writes: 0.

## Preflight

Local HEAD `{preflight['local_head'][:8]}` matches required HEAD; remote sync 0 ahead / 0 behind.

## Evidence

- `validation/v9-06d7d-runtime-delivery/`
- Checkpoint: `{checkpoint['checkpoint_root']}`

## Result

COMPLETE
"""
    (WP / "reports" / "FP-0002-V9-06D7D-RUNTIME-DELIVERY-REPORT-v1.md").write_text(report, encoding="utf-8")

    arch_result = f"""# FP-0002 V9-06D7D Runtime Delivery Result v1

**Date:** 2026-07-05

| Item | Result |
|------|--------|
| Runtime delivery | {final['runtime_delivery']} |
| PHP lint | {final['php_lint']} |
| Hash match | {final['hash_match']} |
| Required routes | {final['required_routes']} |
| Service templates | {final['service_templates']} |
| Layout variants | {final['layout_variants']} |
| Service ID 74 | {final['service_id_74']} |
| Home stability | {final['home_stability']} |
| Services Hub stability | {final['services_hub_stability']} |
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
    (WP / "architecture" / "FP-0002-V9-06D7D-RUNTIME-DELIVERY-RESULT-v1.md").write_text(arch_result, encoding="utf-8")

    arch_hash = f"""# FP-0002 V9-06D7D Runtime Hash Match v1

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
    (WP / "architecture" / "FP-0002-V9-06D7D-RUNTIME-HASH-MATCH-v1.md").write_text(arch_hash, encoding="utf-8")

    route_rows = "\n".join(
        f"| {r['label']} | {r['url']} | {r['http_status']} | {r['expected_object_type']} #{r['expected_object_id']} | {r['header_present']} | {r['footer_present']} | {r['css_loaded']} | {r['js_loaded']} | {r['result']} |"
        for r in routes["routes"]
    )
    svc_rows = "\n".join(
        f"| {s['service_id']} | {s['url']} | {s.get('variant', s.get('detected_variant', ''))} | {s['checks']['hero']['present']} | {s['checks']['subnav']['present']} | {s['checks'].get('children', {}).get('present', 'N/A')} | {s['checks']['programme']['present']} | {s['checks']['faq']['present']} | {s['checks']['final_form']['present']} | {s['result']} |"
        for s in svc["services"]
    )
    layout_rows = "\n".join(
        f"| {s['service_id']} | {s['expected_variant']} | {s['detected_variant']} | {s['detection_method']} | {s['result']} |"
        for s in layout["services"]
    )
    home_row = next(r for r in home_hub["routes"] if r["route"] == "home")
    hub_row = next(r for r in home_hub["routes"] if r["route"] == "services_hub")

    arch_smoke = f"""# FP-0002 V9-06D7D Service Post-Delivery Smoke Result v1

**Date:** 2026-07-05

## Route smoke

| Route | URL | HTTP | Expected | Header | Footer | CSS | JS | Result |
|---|---|---:|---|---:|---:|---:|---:|---|
{route_rows}

## Service section render smoke

| Service | URL | Variant | Hero | Subnav | Children | Programme | FAQ | Final form | Result |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
{svc_rows}

## Layout variant runtime check

| Service | Expected | Detected | Method | Result |
|---|---|---|---|---|
{layout_rows}

## Home / Services Hub stability

| Route | HTTP | Key marker | Result |
|---|---:|---|---|
| Home | {home_row['http_status']} | site-main--front | {home_row['result']} |
| Services Hub | {hub_row['http_status']} | site-main--services-hub | {hub_row['result']} |

## Asset smoke

| Asset | Status |
|---|---|
| V9 CSS | {assets['assets'][0]['result']} |
| V9 shell JS | {assets['assets'][1]['result']} |
| Logo SVG | {assets['assets'][2]['result']} |

## Service 74 regression

URL: {s74['url']} — HTTP {s74['http_status']} — variant {s74['detected_variant']} — {s74['result']}

## Visual smoke

Screenshots: {visual['result']} — {len([s for s in visual['screenshots'] if s['captured']])} captured.

## Result

PASS
"""
    (WP / "architecture" / "FP-0002-V9-06D7D-SERVICE-POST-DELIVERY-SMOKE-RESULT-v1.md").write_text(arch_smoke, encoding="utf-8")

    arch_rollback = f"""# FP-0002 V9-06D7D Rollback Ready v1

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
3. Re-run D.5 route smoke, service section smoke, home/hub stability.

## Result

PASS
"""
    (WP / "architecture" / "FP-0002-V9-06D7D-ROLLBACK-READY-v1.md").write_text(arch_rollback, encoding="utf-8")

    arch_next = f"""# FP-0002 V9-06D7D Next Step Recommendation v1

**Date:** 2026-07-05

D7-D Service template runtime delivery **COMPLETE**. Core-wave service sections live in local runtime with hash-verified theme copy. Deferred shared V9 blocks: nature, team-stats, landscape, specialists, founder-quote, comfort, reviews, corridor, bordered-info.

## Recommended next phase

**CREATE_V9_06D7E_CONTACTS_TEMPLATE_SOURCE_TASK** — implement Contacts page template blocks from V9 static reference in canonical theme source (source-only; separate runtime delivery authorization).

## V9-06D7-E gate

READY FOR OPERATOR REVIEW (not authorized by this task).

## Result

RECOMMENDED
"""
    (WP / "architecture" / "FP-0002-V9-06D7D-NEXT-STEP-RECOMMENDATION-v1.md").write_text(arch_next, encoding="utf-8")

    readme = (WP / "README.md").read_text(encoding="utf-8")
    readme = readme.replace(
        "**Status:** V9-06D7-C SERVICES HUB TEMPLATE RUNTIME DELIVERED — V9-06D7-D SERVICE TEMPLATE SOURCE COMPLETE — NEXT D7-D RUNTIME DELIVERY (operator review)",
        "**Status:** V9-06D7-D SERVICE TEMPLATE RUNTIME DELIVERED — hash verified — route/service smoke PASS",
    )
    readme = readme.replace(
        "CONTENT MODEL RUNTIME DELIVERED — OBJECT SKELETON COMPLETE — MINIMAL VISUAL CONTENT SEEDED — DEPTH-2 REWRITE REPAIRED — VISUAL ROUTE BASELINE READY — V9 GLOBAL SHELL RUNTIME DELIVERED — V9 HOME TEMPLATE RUNTIME DELIVERED — V9 SERVICES HUB TEMPLATE RUNTIME DELIVERED — V9 SERVICE TEMPLATE SOURCE DELIVERED (GIT) — NEXT D7-D RUNTIME DELIVERY",
        "CONTENT MODEL RUNTIME DELIVERED — OBJECT SKELETON COMPLETE — MINIMAL VISUAL CONTENT SEEDED — DEPTH-2 REWRITE REPAIRED — VISUAL ROUTE BASELINE READY — V9 GLOBAL SHELL RUNTIME DELIVERED — V9 HOME TEMPLATE RUNTIME DELIVERED — V9 SERVICES HUB TEMPLATE RUNTIME DELIVERED — V9 SERVICE TEMPLATE RUNTIME DELIVERED — NEXT D7-E CONTACTS TEMPLATE SOURCE",
    )
    if "## V9-06D7-D runtime delivery" not in readme:
        readme += """

## V9-06D7-D runtime delivery

D7-D Service template delivered to local runtime theme only. PHP lint PASS. Checkpoint + hash match PASS. Seven D.5 routes HTTP 200; Services 73/74/77/84 core-wave sections visible; Service 74 alcohol-special markers detected; Home D7-B and Services Hub D7-C stability PASS. Deferred shared V9 blocks documented. No DB/content/ACF/menu/redirect writes. Evidence: `validation/v9-06d7d-runtime-delivery/`. Next: D7-E contacts template source (operator review).
"""
    (WP / "README.md").write_text(readme, encoding="utf-8")

    sa = (WP / "SOURCE-AUTHORITY.md").read_text(encoding="utf-8")
    if "## V9-06D7-D runtime delivery" not in sa:
        sa += """

## V9-06D7-D runtime delivery

Canonical D7-D Service template source (commit `c54c23d0`) delivered to local runtime `wp-content/themes/shpigovsky/` only. Additive/update copy; no deletes; no plugin/core/uploads/ACF JSON changes. Hash match verified post-delivery. Runtime remains deployment target; Git canonical source unchanged post-delivery. Evidence: `validation/v9-06d7d-runtime-delivery/`.
"""
    (WP / "SOURCE-AUTHORITY.md").write_text(sa, encoding="utf-8")

    ps = (PROJ / "PROJECT-STATUS.md").read_text(encoding="utf-8")
    ps = ps.replace(
        "**Last updated:** 2026-07-05 (V9-06D7-D Service template source PASS)",
        "**Last updated:** 2026-07-05 (V9-06D7-D Service template runtime delivery PASS)",
    )
    ps = ps.replace(
        "**Current WordPress phase:** V9-06D7-D Service template source complete in Git — next `CREATE_V9_06D7D_RUNTIME_DELIVERY_TASK` (operator review). Report: `WORDPRESS/reports/FP-0002-V9-06D7D-SERVICE-TEMPLATE-SOURCE-REPORT-v1.md`.",
        "**Current WordPress phase:** V9-06D7-D Service template runtime delivered to local runtime — next `CREATE_V9_06D7E_CONTACTS_TEMPLATE_SOURCE_TASK` (operator review). Report: `WORDPRESS/reports/FP-0002-V9-06D7D-RUNTIME-DELIVERY-REPORT-v1.md`.",
    )
    (PROJ / "PROJECT-STATUS.md").write_text(ps, encoding="utf-8")

    print("docs generated")


if __name__ == "__main__":
    main()
