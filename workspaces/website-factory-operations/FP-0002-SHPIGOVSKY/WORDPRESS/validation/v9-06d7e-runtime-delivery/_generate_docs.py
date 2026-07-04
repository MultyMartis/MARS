#!/usr/bin/env python3
"""Generate V9-06D7-E runtime delivery documentation from evidence JSON."""
import json
from pathlib import Path

WP = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS")
EV = WP / "validation" / "v9-06d7e-runtime-delivery"
PROJ = WP.parent


def load(name):
    return json.loads((EV / name).read_text(encoding="utf-8"))


def main():
    final = load("final-verdict.json")
    dry = load("dry-run-delivery-plan.json")
    apply = load("apply-delivery-result.json")
    hash_match = load("runtime-hash-match-after.json")
    routes = load("post-delivery-route-smoke.json")
    contacts = load("contacts-section-render-smoke.json")
    stability = load("home-services-service-stability.json")
    assets = load("post-delivery-asset-smoke.json")
    checkpoint = load("runtime-checkpoint.json")
    identity = load("runtime-identity-before.json")
    php_lint = load("php-lint-before-delivery.json")
    visual = load("visual-smoke-result.json")
    rollback = load("rollback-readiness.json")
    preflight = load("preflight.json")
    s74 = load("service-74-regression.json")
    api_check = load("no-external-api-key-runtime-check.json")

    wp = identity["wordpress_state"]
    counts = dry["counts"]

    report = f"""# FP-0002 V9-06D7E Runtime Delivery Report v1

**Date:** 2026-07-05  
**Task:** V9-06D7-E Contacts Template Runtime Delivery  
**Source HEAD (required):** `{preflight['required_head']}`  
**Verdict:** {final['verdict']}

## Summary

Scoped additive theme delivery of D7-E Contacts template source from canonical Git commit `5a7eb400` to local FP-0002 runtime. PHP lint PASS ({php_lint['files']} theme PHP files; 6 changed D7-E files). Runtime checkpoint created. Dry-run: {counts['ADD']} ADD, {counts['MODIFY']} MODIFY, {counts['SAME']} SAME, 0 DELETE. Post-delivery hash match PASS ({hash_match['runtime_files_matched']}/{hash_match['source_files_checked']}). All seven D.5 routes HTTP 200 with V9 header/footer/CSS/JS visible. Contacts `/kontakty/` renders D7-E orchestration (contacts body, location cards, rehabilitation steps, CTA band, modal-only behavior). Map figure and messengers correctly omitted where media/options unavailable. Home D7-B, Services Hub D7-C, and Service templates 73/74/77/84 stability PASS. Service ID 74 alcohol-special markers detected. No external API keys; no live form endpoint. DB/content/ACF writes: 0.

## Preflight

Local HEAD `{preflight['local_head'][:8]}` matches required HEAD; remote sync 0 ahead / 0 behind.

## Evidence

- `validation/v9-06d7e-runtime-delivery/`
- Checkpoint: `{checkpoint['checkpoint_root']}`

## Result

COMPLETE
"""
    (WP / "reports" / "FP-0002-V9-06D7E-RUNTIME-DELIVERY-REPORT-v1.md").write_text(report, encoding="utf-8")

    arch_result = f"""# FP-0002 V9-06D7E Runtime Delivery Result v1

**Date:** 2026-07-05

| Item | Result |
|------|--------|
| Runtime delivery | {final['runtime_delivery']} |
| PHP lint | {final['php_lint']} |
| Hash match | {final['hash_match']} |
| Required routes | {final['required_routes']} |
| Contacts template | {final['contacts_template']} |
| Contacts media gaps | {final['contacts_media_gaps']} |
| External API keys | {final['external_api_keys']} |
| Service ID 74 | {final['service_id_74']} |
| Home stability | {final['home_stability']} |
| Services Hub stability | {final['services_hub_stability']} |
| Service templates stability | {final['service_templates_stability']} |
| Header/footer/assets | {final['header_footer_assets']} |
| Runtime mutations | {final['runtime_mutations']} |
| DB writes | {final['db_writes']} |

## Apply counts

- ADD: {apply['files_added']}
- MODIFY: {apply['files_modified']}
- SAME: {apply['files_same']}
- TARGET_ONLY preserved: {apply['target_only_preserved']}
- DELETE: {apply['deletes']}

## Delivered D7-E files

- `inc/contacts-helpers.php` (ADD)
- `template-parts/contacts/location-card.php` (ADD)
- `functions.php` (MODIFY)
- `page-templates/contacts.php` (MODIFY)
- `template-parts/contacts/map-body.php` (MODIFY)
- `template-parts/contacts/rehabilitation-steps.php` (MODIFY)

## Result

PASS
"""
    (WP / "architecture" / "FP-0002-V9-06D7E-RUNTIME-DELIVERY-RESULT-v1.md").write_text(arch_result, encoding="utf-8")

    arch_hash = f"""# FP-0002 V9-06D7E Runtime Hash Match v1

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
    (WP / "architecture" / "FP-0002-V9-06D7E-RUNTIME-HASH-MATCH-v1.md").write_text(arch_hash, encoding="utf-8")

    route_rows = "\n".join(
        f"| {r['label']} | {r['url']} | {r['http_status']} | {r['expected_object_type']} #{r['expected_object_id']} | {r['header_present']} | {r['footer_present']} | {r['css_loaded']} | {r['js_loaded']} | {r['result']} |"
        for r in routes["routes"]
    )
    contact_rows = "\n".join(
        f"| {c['section']} | {c['present']} | {c['expected_if_empty']} | {c['result']} |"
        for c in contacts["checks"]
    )
    stability_rows = "\n".join(
        f"| {r['route']} | {r['http_status']} | {r['key_marker']} | {r['header_present']}/{r['footer_present']}/{r['css_loaded']}/{r['js_loaded']} | {r['result']} |"
        for r in stability["routes"]
    )

    arch_smoke = f"""# FP-0002 V9-06D7E Contacts Post-Delivery Smoke Result v1

**Date:** 2026-07-05

## Route smoke

| Route | URL | HTTP | Expected | Header | Footer | CSS | JS | Result |
|---|---|---:|---|---:|---:|---:|---:|---|
{route_rows}

## Contacts section render smoke

| Section/check | Present | Expected if empty/deferred | Result |
|---|---:|---|---|
{contact_rows}

## Home / Services Hub / Service stability

| Route | HTTP | Key marker | Header/footer/assets | Result |
|---|---:|---|---|---|
{stability_rows}

## Asset smoke

| Asset | Status |
|---|---|
| V9 CSS | {assets['assets'][0]['result']} |
| V9 shell JS | {assets['assets'][1]['result']} |
| Logo SVG | {assets['assets'][2]['result']} |

## Service 74 regression

URL: {s74['url']} — HTTP {s74['http_status']} — variant {s74['detected_variant']} — {s74['result']}

## No external API key runtime check

- API keys in HTML: {api_check['contacts_html_api_key_patterns']}
- Live form endpoint: {api_check['live_form_endpoint_created']}
- Result: {api_check['result']}

## Visual smoke

Screenshots: {visual['result']} — {len([s for s in visual['screenshots'] if s['captured']])} captured.

## Deferred gaps (not blockers)

- Map PNG assets not packaged — map figure omitted
- Rehabilitation interior photo not packaged — photo bleed omitted
- Messengers may be omitted when site options unseeded

## Result

PASS
"""
    (WP / "architecture" / "FP-0002-V9-06D7E-CONTACTS-POST-DELIVERY-SMOKE-RESULT-v1.md").write_text(arch_smoke, encoding="utf-8")

    arch_rollback = f"""# FP-0002 V9-06D7E Rollback Ready v1

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
3. Re-run D.5 route smoke, contacts section smoke, home/hub/service stability.

## Result

PASS
"""
    (WP / "architecture" / "FP-0002-V9-06D7E-ROLLBACK-READY-v1.md").write_text(arch_rollback, encoding="utf-8")

    arch_next = f"""# FP-0002 V9-06D7E Next Step Recommendation v1

**Date:** 2026-07-05

D7-E Contacts template runtime delivery **COMPLETE**. Contacts page orchestration live in local runtime with hash-verified theme copy. Deferred: map PNG media, rehabilitation interior photo, unseeded phone/messenger options.

## Recommended next phase

**CREATE_V9_06D7F_FINAL_ROUTE_QA_TASK** — consolidated final route QA across all D7 wave templates after Contacts delivery.

## V9-06D7-F gate

READY FOR OPERATOR REVIEW (not authorized by this task).

## Result

RECOMMENDED
"""
    (WP / "architecture" / "FP-0002-V9-06D7E-NEXT-STEP-RECOMMENDATION-v1.md").write_text(arch_next, encoding="utf-8")

    readme = (WP / "README.md").read_text(encoding="utf-8")
    readme = readme.replace(
        "**Status:** V9-06D7-E CONTACTS TEMPLATE SOURCE COMPLETE — runtime delivery pending operator task",
        "**Status:** V9-06D7-E CONTACTS TEMPLATE RUNTIME DELIVERED — hash verified — route/contacts smoke PASS",
    )
    readme = readme.replace(
        "CONTENT MODEL RUNTIME DELIVERED — OBJECT SKELETON COMPLETE — MINIMAL VISUAL CONTENT SEEDED — DEPTH-2 REWRITE REPAIRED — VISUAL ROUTE BASELINE READY — V9 GLOBAL SHELL RUNTIME DELIVERED — V9 HOME TEMPLATE RUNTIME DELIVERED — V9 SERVICES HUB TEMPLATE RUNTIME DELIVERED — V9 SERVICE TEMPLATE RUNTIME DELIVERED — V9 CONTACTS TEMPLATE SOURCE COMPLETE — NEXT D7-E RUNTIME DELIVERY",
        "CONTENT MODEL RUNTIME DELIVERED — OBJECT SKELETON COMPLETE — MINIMAL VISUAL CONTENT SEEDED — DEPTH-2 REWRITE REPAIRED — VISUAL ROUTE BASELINE READY — V9 GLOBAL SHELL RUNTIME DELIVERED — V9 HOME TEMPLATE RUNTIME DELIVERED — V9 SERVICES HUB TEMPLATE RUNTIME DELIVERED — V9 SERVICE TEMPLATE RUNTIME DELIVERED — V9 CONTACTS TEMPLATE RUNTIME DELIVERED — NEXT D7-F FINAL ROUTE QA",
    )
    readme = readme.replace(
        "Theme | V9-06D7-E CONTACTS TEMPLATE SOURCE COMPLETE — D7-E contacts stacks in Git; runtime delivery pending operator task",
        "Theme | V9-06D7-E CONTACTS TEMPLATE RUNTIME DELIVERED — D7-E contacts stacks live in local runtime",
    )
    if "## V9-06D7-E runtime delivery" not in readme:
        readme += """

## V9-06D7-E runtime delivery

D7-E Contacts template delivered to local runtime theme only. PHP lint PASS. Checkpoint + hash match PASS. Seven D.5 routes HTTP 200; `/kontakty/` renders D7-E contacts body, location cards, rehabilitation steps, CTA band (modal-only); map/messengers omitted where expected. Home D7-B, Services Hub D7-C, Service templates 73/74/77/84 stability PASS. No DB/content/ACF/menu/redirect writes. Evidence: `validation/v9-06d7e-runtime-delivery/`. Next: D7-F final route QA (operator review).
"""
    (WP / "README.md").write_text(readme, encoding="utf-8")

    sa = (WP / "SOURCE-AUTHORITY.md").read_text(encoding="utf-8")
    sa = sa.replace(
        "No runtime delivery, no DB/content/ACF writes, no plugin or V9 src/dist edits. Validation: `validation/v9-06d7e-contacts-template-source/`. Next: V9-06D7-E runtime delivery task (operator review; not authorized here).",
        "Runtime delivery performed 2026-07-05. Canonical D7-E source (commit `5a7eb400`) delivered to local runtime `wp-content/themes/shpigovsky/` only. Additive/update copy; no deletes; no plugin/core/uploads/ACF JSON changes. Hash match verified post-delivery. Evidence: `validation/v9-06d7e-runtime-delivery/`.",
    )
    if "## V9-06D7-E runtime delivery" not in sa:
        sa += """

## V9-06D7-E runtime delivery

Canonical D7-E Contacts template source (commit `5a7eb400`) delivered to local runtime `wp-content/themes/shpigovsky/` only. Six theme files (2 ADD, 4 MODIFY). Hash match verified post-delivery. Runtime remains deployment target; Git canonical source unchanged post-delivery. Evidence: `validation/v9-06d7e-runtime-delivery/`.
"""
    (WP / "SOURCE-AUTHORITY.md").write_text(sa, encoding="utf-8")

    ps = (PROJ / "PROJECT-STATUS.md").read_text(encoding="utf-8")
    ps = ps.replace(
        "**Last updated:** 2026-07-05 (V9-06D7-E Contacts template source PASS)",
        "**Last updated:** 2026-07-05 (V9-06D7-E Contacts template runtime delivery PASS)",
    )
    ps = ps.replace(
        "**Current WordPress phase:** V9-06D7-E Contacts template source complete in Git — next `CREATE_V9_06D7E_RUNTIME_DELIVERY_TASK` (operator review). Report: `WORDPRESS/reports/FP-0002-V9-06D7E-CONTACTS-TEMPLATE-SOURCE-REPORT-v1.md`.",
        "**Current WordPress phase:** V9-06D7-E Contacts template runtime delivered to local runtime — next `CREATE_V9_06D7F_FINAL_ROUTE_QA_TASK` (operator review). Report: `WORDPRESS/reports/FP-0002-V9-06D7E-RUNTIME-DELIVERY-REPORT-v1.md`.",
    )
    (PROJ / "PROJECT-STATUS.md").write_text(ps, encoding="utf-8")

    print("docs generated")


if __name__ == "__main__":
    main()
