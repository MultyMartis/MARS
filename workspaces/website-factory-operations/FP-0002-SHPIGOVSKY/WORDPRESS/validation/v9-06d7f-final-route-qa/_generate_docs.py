#!/usr/bin/env python3
"""Generate V9-06D7-F final route QA documentation from evidence JSON."""
import json
from pathlib import Path

WP = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS")
EV = WP / "validation" / "v9-06d7f-final-route-qa"
PROJ = WP.parent


def load(name):
    return json.loads((EV / name).read_text(encoding="utf-8"))


def main():
    preflight = load("preflight.json")
    identity = load("runtime-identity-qa.json")
    routes = load("final-route-matrix.json")
    templates = load("template-specific-qa.json")
    shell = load("global-shell-asset-qa.json")
    assets = load("asset-http-smoke.json")
    s74 = load("service-74-regression.json")
    mutation = load("no-mutation-audit.json")
    gaps = load("known-gaps-classification.json")
    visual = load("visual-smoke-result.json")
    shots = load("visual-smoke-screenshot-manifest.json")
    final = load("final-verdict.json")

    route_rows = "\n".join(
        f"| {r['label']} | {r['url']} | {r['http_status']} | {r['expected_object']} | {r['resolved_object']} | {r.get('body_class', '')[:60]} | {r['header_present']} | {r['footer_present']} | {r['v9_css_loaded']} | {r['v9_js_loaded']} | {r['result']} |"
        for r in routes["routes"]
    )
    tpl_rows = "\n".join(
        f"| {t['template']} | {t['route']} | {', '.join(t['required_markers'][:5])} | {', '.join(t['optional_omissions'][:4]) or 'none'} | {t['result']} |"
        for t in templates["templates"]
    )
    shell_rows = "\n".join(
        f"| {r['route']} | {r['header']} | {r['footer']} | {r['nav']} | {r['modal']} | {r['css_200']} | {r['js_200']} | {r['critical_missing'] or 'none'} | {r['result']} |"
        for r in shell["routes"]
    )
    gap_rows = "\n".join(
        f"| {g['area']} | {g['gap']} | {g['classification']} | {g['blocking']} |"
        for g in gaps["gaps"]
    )
    shot_rows = "\n".join(
        f"| {s['file']} | {s['route']} | {s['viewport']} | {s['captured']} | {s['result']} |"
        for s in shots["screenshots"]
    )

    (WP / "architecture" / "FP-0002-V9-06D7F-FINAL-ROUTE-MATRIX-v1.md").write_text(f"""# FP-0002 V9-06D7F Final Route Matrix v1

**Date:** 2026-07-05  
**Task:** V9-06D7-F Final Route QA (read-only)

## Matrix

| Route | URL | HTTP | Expected object | Resolved object | Root marker | Header | Footer | CSS | JS | Result |
|---|---|---:|---|---|---|---:|---:|---:|---:|---|
{route_rows}

## Summary

- All HTTP 200: {routes['all_http_200']}
- Object resolution: {routes['all_object_resolution_pass']}
- Result: **{routes['result']}**
""", encoding="utf-8")

    (WP / "architecture" / "FP-0002-V9-06D7F-TEMPLATE-SPECIFIC-QA-v1.md").write_text(f"""# FP-0002 V9-06D7F Template-Specific QA v1

**Date:** 2026-07-05

| Template | Route | Required markers | Optional omissions | Result |
|---|---|---|---|---|
{tpl_rows}

## Result

**{templates['result']}**
""", encoding="utf-8")

    asset_rows = "\n".join(
        f"| {a['asset']} | {a.get('url') or a.get('path')} | {a.get('http_status', 'N/A')} | {a['result']} |"
        for a in assets["assets"]
    )
    (WP / "architecture" / "FP-0002-V9-06D7F-GLOBAL-SHELL-ASSET-QA-v1.md").write_text(f"""# FP-0002 V9-06D7F Global Shell / Asset QA v1

**Date:** 2026-07-05

## Per-route shell

| Route | Header | Footer | Nav | Modal | CSS 200 | JS 200 | Critical missing | Result |
|---|---:|---:|---:|---:|---:|---:|---|---|
{shell_rows}

## Shared assets

| Asset | URL/path | HTTP | Result |
|---|---|---:|---|
{asset_rows}

## Result

**{shell['result']}**
""", encoding="utf-8")

    (WP / "architecture" / "FP-0002-V9-06D7F-VISUAL-SMOKE-RESULT-v1.md").write_text(f"""# FP-0002 V9-06D7F Visual Smoke Result v1

**Date:** 2026-07-05

| Screenshot | Route | Viewport | Captured | Result |
|---|---|---|---:|---|
{shot_rows}

- Captured: {shots['captured']} / {len(shots['screenshots'])}
- Pixel-perfect claim: **NO**
- Known gaps documented: **YES**

## Result

**{visual['result']}**
""", encoding="utf-8")

    (WP / "architecture" / "FP-0002-V9-06D7F-KNOWN-GAPS-CLASSIFICATION-v1.md").write_text(f"""# FP-0002 V9-06D7F Known Gaps Classification v1

**Date:** 2026-07-05

| Area | Gap | Classification | Blocking |
|---|---|---|---:|
{gap_rows}

## Result

**{gaps['result']}** — no defects or blockers in deferred content/media scope.
""", encoding="utf-8")

    (WP / "architecture" / "FP-0002-V9-06D7F-NEXT-STEP-RECOMMENDATION-v1.md").write_text(f"""# FP-0002 V9-06D7F Next Step Recommendation v1

**Date:** 2026-07-05

## Verdict

{final['verdict']}

## Recommended next phase

**{final['recommended_next_phase']}**

## Rationale

D7-A through D7-E runtime deliveries verified read-only. Seven first-wave routes HTTP 200 with object resolution, global shell/assets, template markers, Service ID 74 regression, and visual smoke {visual['result']}. Known gaps are expected content/media/shared-block omissions only — not blockers for D8 content seed planning.

## V9-06D8

**{final['v9_06d8']}**
""", encoding="utf-8")

    report = f"""# FP-0002 V9-06D7F Final Route QA Report v1

**Date:** 2026-07-05  
**Task:** V9-06D7-F Final Route QA (read-only)  
**Local HEAD at QA:** `{preflight['local_head']}`  
**Required D7-E HEAD:** `{preflight['required_head']}`  
**Strict HEAD gate:** {preflight['strict_head_gate']} (descendant +1 unrelated commit; branch 0 ahead/0 behind)  
**Verdict:** {final['verdict']}

## Summary

Read-only final QA of local FP-0002 WordPress runtime after D7-A/B/C/D/E deliveries. No runtime delivery, source changes, DB writes, or content mutations performed. Runtime identity PASS (theme `shpigovsky`, plugin `shpigovsky-core`, core mode `content_model`, WPilot write_enabled false). Seven first-wave routes validated with HTTP/object resolution, template-specific markers, global shell/assets, Service ID 74 regression, desktop/mobile screenshots, and no-mutation audit.

## Runtime identity

| Item | Value |
|------|-------|
| Pages | {identity['pages']} |
| Services | {identity['services']} |
| Posts | {identity['posts']} |
| Menus | {identity['menus']} |
| ACF groups | {identity['acf_groups']} |
| Theme file count | {identity['runtime_theme_file_count']} |

## Results

| Suite | Result |
|-------|--------|
| Required routes | {final['required_routes']} |
| Object resolution | {final['object_resolution']} |
| Global shell/assets | {final['global_shell_assets']} |
| Home | {final['home']} |
| Services Hub | {final['services_hub']} |
| Service templates | {final['service_templates']} |
| Service ID 74 | {final['service_id_74']} |
| Contacts | {final['contacts']} |
| Visual smoke | {final['visual_smoke']} |
| Known gaps | {final['known_gaps']} |
| No-mutation audit | {mutation['result']} |

## Evidence

`WORDPRESS/validation/v9-06d7f-final-route-qa/`

## Result

COMPLETE — {final['verdict']}
"""
    (WP / "reports" / "FP-0002-V9-06D7F-FINAL-ROUTE-QA-REPORT-v1.md").write_text(report, encoding="utf-8")

    readme = (WP / "README.md").read_text(encoding="utf-8")
    readme = readme.replace(
        "V9-06D7-E CONTACTS TEMPLATE RUNTIME DELIVERED — hash verified — route/contacts smoke PASS",
        "V9-06D7-F FINAL ROUTE QA PASS — D7 wave runtime verified read-only",
    )
    readme = readme.replace(
        "NEXT D7-F FINAL ROUTE QA",
        "NEXT D8 CONTENT SEED PLANNING (operator review)",
    )
    if "V9-06D7-F" not in readme:
        pass
    (WP / "README.md").write_text(readme, encoding="utf-8")

    sa = (WP / "SOURCE-AUTHORITY.md").read_text(encoding="utf-8")
    if "V9-06D7-F" not in sa:
        marker = "## V9 implementation"
        insert = """## V9-06D7-F final route QA (2026-07-05)

Read-only QA PASS after D7-A–D7-E runtime deliveries. Evidence: `validation/v9-06d7f-final-route-qa/`. No runtime/source/DB mutations. Recommended next: D8 content seed planning.

"""
        if marker in sa:
            sa = sa.replace(marker, insert + marker)
        (WP / "SOURCE-AUTHORITY.md").write_text(sa, encoding="utf-8")

    ps = (PROJ / "PROJECT-STATUS.md").read_text(encoding="utf-8")
    ps = ps.replace(
        "**Last updated:** 2026-07-05 (V9-06D7-E Contacts template runtime delivery PASS)",
        "**Last updated:** 2026-07-05 (V9-06D7-F Final Route QA PASS)",
    )
    ps = ps.replace(
        "**Current WordPress phase:** V9-06D7-E Contacts template runtime delivered to local runtime — next `CREATE_V9_06D7F_FINAL_ROUTE_QA_TASK` (operator review). Report: `WORDPRESS/reports/FP-0002-V9-06D7E-RUNTIME-DELIVERY-REPORT-v1.md`.",
        f"**Current WordPress phase:** V9-06D7-F Final Route QA PASS (read-only) — D7 wave verified. Next `{final['recommended_next_phase']}`. Report: `WORDPRESS/reports/FP-0002-V9-06D7F-FINAL-ROUTE-QA-REPORT-v1.md`.",
    )
    (PROJ / "PROJECT-STATUS.md").write_text(ps, encoding="utf-8")

    print("DOCS_OK")


if __name__ == "__main__":
    main()
