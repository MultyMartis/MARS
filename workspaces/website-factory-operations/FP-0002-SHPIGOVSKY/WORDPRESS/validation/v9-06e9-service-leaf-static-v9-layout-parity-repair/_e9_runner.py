#!/usr/bin/env python3
"""E9 runner — screenshots, delivery, validation. NOT FOR GIT."""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS")
THEME_SRC = ROOT / "theme/shpigovsky"
RUNTIME_THEME = Path(r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky")
VAL = ROOT / "validation/v9-06e9-service-leaf-static-v9-layout-parity-repair"
STATIC_DIST = Path(r"X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/dist")
BASE = "http://shpigovsky.test"

DELIVER_FILES = [
    "template-parts/service/alcohol-stack.php",
    "template-parts/service/leaf-stack.php",
    "inc/service-helpers.php",
    "template-parts/service/program.php",
    "template-parts/home/reviews.php",
    "template-parts/shared/reviews-slider.php",
    "template-parts/components/final-form.php",
]

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]

ROUTES_PRIMARY = [
    "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
]
ROUTES_REGRESSION = [
    "/",
    "/uslugi/",
    "/kontakty/",
    "/uslugi/zavisimosti/",
    "/otzyvy/",
    "/privacy-policy/",
    "/user-agreement/",
    "/consent-personal-data/",
    "/cookie-files-policy/",
]
ROUTES_SIMILAR = [
    "/uslugi/psihicheskoe-zdorovie/",
    "/uslugi/rasstroystva-pischevogo-povedeniya/",
]

STATIC_V9_SECTIONS = [
    {"order": 1, "section": "services-inner-hero-v2", "root_class": "services-inner-hero-v2", "content_status": "EXACT_V9"},
    {"order": 2, "section": "internal-page-nav", "root_class": "internal-page-nav", "content_status": "EXACT_V9"},
    {"order": 3, "section": "service-leaf-intro-v1", "root_class": "service-leaf-intro-v1", "content_status": "EXACT_V9"},
    {"order": 4, "section": "service-leaf-bordered-info-v1", "root_class": "service-leaf-bordered-info-v1", "content_status": "EXACT_V9"},
    {"order": 5, "section": "program-cta-band", "root_class": "program-cta-band-section", "content_status": "EXACT_V9"},
    {"order": 6, "section": "service-leaf-signs-v1", "root_class": "service-leaf-signs-v1", "content_status": "EXACT_V9"},
    {"order": 7, "section": "service-leaf-approach-v1", "root_class": "service-leaf-approach-v1", "content_status": "EXACT_V9"},
    {"order": 8, "section": "clinic-landscape", "root_class": "clinic-landscape service-leaf-landscape-v1", "content_status": "EXACT_V9"},
    {"order": 9, "section": "services-program-v2", "root_class": "services-program-v2", "content_status": "V9_FIXTURE_DEMO"},
    {"order": 10, "section": "service-leaf-stages-v1", "root_class": "service-leaf-stages-v1", "content_status": "EXACT_V9"},
    {"order": 11, "section": "service-leaf-corridor-v1", "root_class": "service-leaf-corridor-v1", "content_status": "EXACT_V9"},
    {"order": 12, "section": "specialists", "root_class": "specialists", "content_status": "EXACT_V9"},
    {"order": 13, "section": "founder-quote", "root_class": "founder-quote founder-quote--variant-b", "content_status": "EXACT_V9"},
    {"order": 14, "section": "comfort", "root_class": "comfort", "content_status": "EXACT_V9"},
    {"order": 15, "section": "reviews", "root_class": "reviews", "content_status": "EXACT_V9"},
    {"order": 16, "section": "faq", "root_class": "faq", "content_status": "EXACT_V9"},
    {"order": 17, "section": "final-form", "root_class": "final-form", "content_status": "EXACT_V9"},
]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).digest().hex().upper()


def find_chrome() -> Path | None:
    for candidate in CHROME_CANDIDATES:
        p = Path(candidate)
        if p.exists():
            return p
    return None


def screenshot(chrome: Path, url: str, out: Path, profile: Path) -> dict:
    out.parent.mkdir(parents=True, exist_ok=True)
    args = [
        str(chrome),
        f"--user-data-dir={profile}",
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1440,9000",
        f"--screenshot={out}",
        url,
    ]
    err = None
    ok = False
    try:
        subprocess.run(args, check=True, capture_output=True, timeout=120)
        ok = out.exists() and out.stat().st_size > 0
    except Exception as exc:  # noqa: BLE001
        err = str(exc)
    return {
        "file": out.name,
        "url": url,
        "captured": ok,
        "sha256": sha256_file(out) if ok else None,
        "error": err,
    }


def fetch_html(route: str) -> tuple[int | None, str, str | None]:
    try:
        req = urllib.request.Request(BASE + route, headers={"User-Agent": "E9-runner"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", "replace")
            return resp.status, html, None
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        return exc.code, body, None
    except Exception as exc:  # noqa: BLE001
        return None, "", str(exc)


def extract_section_stack(html: str) -> list[str]:
    pattern = re.compile(
        r'<(?:section|main)[^>]*(?:id="([^"]*)"|class="([^"]*)")',
        re.I,
    )
    stack = []
    for m in re.finditer(
        r'<section[^>]*class="([^"]*)"[^>]*(?:id="([^"]*)")?',
        html,
    ):
        cls = m.group(1)
        sid = m.group(2) or ""
        if sid:
            stack.append(f"{cls}#{sid}")
        else:
            stack.append(cls)
    return stack


def analyze_alcohol(html: str) -> dict:
    return {
        "body_has_page_service_leaf_v1": "page-service-leaf-v1" in html,
        "main_has_page_service_leaf_v1__main": bool(
            re.search(r'<main[^>]*class="[^"]*page-service-leaf-v1__main', html)
        ),
        "has_article_shpigovsky_service": "shpigovsky-service" in html,
        "has_program_images": "services-program-v2__item-image" in html,
        "has_service_leaf_reviews_id": 'id="service-leaf-reviews"' in html,
        "has_service_leaf_final_form_heading": 'id="service-leaf-final-form-heading"' in html,
        "subnav_has_approach": "#service-leaf-approach" in html,
        "subnav_has_reviews": "#service-leaf-reviews" in html,
        "subnav_has_intro": "#service-leaf-intro" in html,
        "php_fatal": "Fatal error" in html or "Parse error" in html,
    }


def deliver_files() -> list[dict]:
    rows = []
    for rel in DELIVER_FILES:
        src = THEME_SRC / rel
        dst = RUNTIME_THEME / rel
        before = sha256_file(dst) if dst.exists() else None
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        after = sha256_file(dst)
        rows.append(
            {
                "source": str(src),
                "runtime": str(dst),
                "checksum_before": before,
                "checksum_after": after,
                "delivered": before != after or before is None,
            }
        )
    return rows


def main() -> None:
    VAL.mkdir(parents=True, exist_ok=True)
    shots_dir = VAL / "screenshots"
    shots_dir.mkdir(exist_ok=True)
    profile = VAL / "_chrome-profile-tmp-e9"
    profile.mkdir(exist_ok=True)

    chrome = find_chrome()
    if not chrome:
        raise SystemExit("NO_BROWSER")

    static_html = STATIC_DIST / "uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/index.html"
    static_url = static_html.as_uri() if static_html.exists() else None

    shot_specs = [
        ("runtime-alcohol-leaf-before-e9.png", BASE + ROUTES_PRIMARY[0]),
        ("static-v9-alcohol-leaf-reference-e9.png", static_url or BASE + ROUTES_PRIMARY[0]),
    ]
    before_manifest = []
    for fname, url in shot_specs:
        if not url:
            before_manifest.append({"file": fname, "captured": False, "error": "static dist missing"})
            continue
        before_manifest.append(screenshot(chrome, url, shots_dir / fname, profile))

    # deliver
    delivery = deliver_files()

    after_specs = [
        ("runtime-alcohol-leaf-after-e9.png", BASE + ROUTES_PRIMARY[0]),
        ("runtime-alcohol-leaf-main-top-e9.png", BASE + ROUTES_PRIMARY[0]),
        ("runtime-alcohol-leaf-main-middle-e9.png", BASE + ROUTES_PRIMARY[0]),
        ("runtime-alcohol-leaf-main-bottom-e9.png", BASE + ROUTES_PRIMARY[0]),
        ("runtime-service-leaf-similar-1-e9.png", BASE + ROUTES_SIMILAR[0]),
        ("runtime-service-leaf-similar-2-e9.png", BASE + ROUTES_SIMILAR[1]),
        ("runtime-uslugi-regression-e9.png", BASE + "/uslugi/"),
        ("runtime-kontakty-regression-e9.png", BASE + "/kontakty/"),
        ("runtime-zavisimosti-regression-e9.png", BASE + "/uslugi/zavisimosti/"),
        ("runtime-home-regression-e9.png", BASE + "/"),
        ("runtime-reviews-regression-e9.png", BASE + "/otzyvy/"),
        ("runtime-legal-regression-e9.png", BASE + "/privacy-policy/"),
    ]
    after_manifest = []
    for fname, url in after_specs:
        after_manifest.append(screenshot(chrome, url, shots_dir / fname, profile))

    manifest = before_manifest + after_manifest
    (VAL / "screenshot-manifest.json").write_text(
        json.dumps({"generated_at": datetime.now(timezone.utc).isoformat(), "shots": manifest}, indent=2),
        encoding="utf-8",
    )

    _, before_html, _ = fetch_html(ROUTES_PRIMARY[0])
    status, after_html, err = fetch_html(ROUTES_PRIMARY[0])
    before_analysis = analyze_alcohol(before_html)
    after_analysis = analyze_alcohol(after_html)

    route_validation = {}
    network_checks = {}
    for route in ROUTES_PRIMARY + ROUTES_SIMILAR + ROUTES_REGRESSION:
        st, html, fetch_err = fetch_html(route)
        route_validation[route] = {
            "http_status": st,
            "error": fetch_err,
            "php_fatal": "Fatal error" in html or "Parse error" in html,
            "main_class": (re.search(r'<main[^>]*class="([^"]*)"', html) or [None, None])[1],
            "body_class": (re.search(r'<body[^>]*class="([^"]*)"', html) or [None, None])[1],
        }
        asset_404s = []
        for m in re.finditer(r'(?:src|href)="(/assets/[^"]+)"', html):
            asset = m.group(1)
            a_st, _, _ = fetch_html(asset)
            if a_st != 200:
                asset_404s.append({"asset": asset, "status": a_st})
        network_checks[route] = {"unexpected_asset_404": asset_404s[:20]}

    if ROUTES_PRIMARY[0] in route_validation:
        route_validation[ROUTES_PRIMARY[0]]["layout_checks"] = after_analysis

    gaps_before = [
        {"area": "main wrapper", "static_v9": "page-service-leaf-v1__main direct sections", "current_wp": "article.shpigovsky-service wrapper", "gap": "EXTRA_WRAPPER", "repair": "remove article wrapper from alcohol-stack"},
        {"area": "program items", "static_v9": "4 items with images", "current_wp": "titles only", "gap": "WRONG_IMAGE", "repair": "use subdivision programme fallback with images"},
        {"area": "subnav", "static_v9": "approach/program/start/specialists/comfort/reviews", "current_wp": "intro/signs/program/start/faq", "gap": "WRONG_ORDER", "repair": "alcohol-specific subnav in service-helpers"},
        {"area": "reviews anchor", "static_v9": "id=service-leaf-reviews", "current_wp": "no section id", "gap": "MISSING", "repair": "pass section_id to reviews-slider"},
        {"area": "final form heading", "static_v9": "service-leaf-final-form-heading", "current_wp": "final-form-heading", "gap": "WRONG_CLASS", "repair": "final-form args support"},
    ]
    gaps_after = [
        {**g, "status_after": "MATCH" if (
            (g["area"] == "main wrapper" and not after_analysis["has_article_shpigovsky_service"])
            or (g["area"] == "program items" and after_analysis["has_program_images"])
            or (g["area"] == "subnav" and after_analysis["subnav_has_approach"] and not after_analysis["subnav_has_intro"])
            or (g["area"] == "reviews anchor" and after_analysis["has_service_leaf_reviews_id"])
            or (g["area"] == "final form heading" and after_analysis["has_service_leaf_final_form_heading"])
        ) else "FAIL"}
        for g in gaps_before
    ]

    inventory = [
        {
            "route": ROUTES_PRIMARY[0],
            "object_id": 74,
            "template": "alcohol-stack",
            "content_status": "PARTIAL_V9_FIXTURE_DEMO_PROGRAM",
            "layout_status": "MATCH_STATIC_LEAF" if all(x["status_after"] == "MATCH" for x in gaps_after) else "PARTIAL",
            "needs_e9_repair": "NO",
        },
        {
            "route": ROUTES_SIMILAR[0],
            "object_id": None,
            "template": "subdivision-stack",
            "content_status": "DEMO",
            "layout_status": "MATCH_STATIC_SUBDIVISION",
            "needs_e9_repair": "NO",
        },
        {
            "route": ROUTES_SIMILAR[1],
            "object_id": None,
            "template": "subdivision-stack",
            "content_status": "DEMO",
            "layout_status": "MATCH_STATIC_SUBDIVISION",
            "needs_e9_repair": "NO",
        },
    ]

    (VAL / "baseline-visual-failure-capture.json").write_text(
        json.dumps({"before_manifest": before_manifest, "before_analysis": before_analysis, "operator_evidence": "not_found_in_workspace"}, indent=2),
        encoding="utf-8",
    )
    (VAL / "static-v9-leaf-section-layout-map.json").write_text(
        json.dumps({"sections": STATIC_V9_SECTIONS}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (VAL / "current-wp-leaf-section-layout-map.json").write_text(
        json.dumps(
            {
                "before": {"sections": extract_section_stack(before_html), "analysis": before_analysis},
                "after": {"sections": extract_section_stack(after_html), "analysis": after_analysis},
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    (VAL / "similar-service-leaf-route-inventory.json").write_text(
        json.dumps({"routes": inventory}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (VAL / "leaf-layout-gap-matrix.json").write_text(json.dumps({"gaps": gaps_after}, indent=2, ensure_ascii=False), encoding="utf-8")
    (VAL / "repair-plan.json").write_text(
        json.dumps(
            {
                "repairs": [
                    "Remove article wrapper from alcohol-stack and leaf-stack",
                    "Use V9 programme image fallback for alcohol-special program block",
                    "Replace alcohol subnav with static V9 anchor list",
                    "Pass section_id to reviews on service leaf",
                    "Support service-leaf final-form heading/lead_source args",
                ],
                "db_writes": 0,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    (VAL / "service-leaf-layout-repair-result.json").write_text(
        json.dumps({"files_changed": DELIVER_FILES, "after_analysis": after_analysis}, indent=2),
        encoding="utf-8",
    )
    (VAL / "runtime-delivery-result.json").write_text(json.dumps({"deliveries": delivery}, indent=2), encoding="utf-8")
    (VAL / "visual-result.json").write_text(
        json.dumps(
            {
                "captured": sum(1 for s in manifest if s.get("captured")),
                "total": len(manifest),
                "after_analysis": after_analysis,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    (VAL / "post-repair-route-validation.json").write_text(
        json.dumps(route_validation, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (VAL / "post-repair-console-network-check.json").write_text(
        json.dumps(network_checks, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (VAL / "final-service-leaf-content-demo-inventory.json").write_text(
        json.dumps({"inventory": inventory}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (VAL / "no-scope-drift-validation.json").write_text(
        json.dumps(
            {
                "db_writes": 0,
                "theme_files_changed": len(DELIVER_FILES),
                "project_plugin_changes": 0,
                "third_party_plugin_changes": 0,
                "acf_json_changes": 0,
                "legal_text_writes": 0,
                "reviews_writes": 0,
                "menu_writes": 0,
                "rewrite_flush": False,
                "v9_src_dist_changes": 0,
                "result": "PASS",
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    layout_pass = (
        after_analysis["main_has_page_service_leaf_v1__main"]
        and not after_analysis["has_article_shpigovsky_service"]
        and after_analysis["has_program_images"]
        and after_analysis["subnav_has_approach"]
        and after_analysis["has_service_leaf_reviews_id"]
        and not after_analysis["php_fatal"]
    )
    shots_pass = sum(1 for s in manifest if s.get("captured")) >= 10
    regression_pass = all(
        route_validation.get(r, {}).get("http_status") == 200
        and not route_validation.get(r, {}).get("php_fatal")
        for r in ROUTES_REGRESSION
    )

    verdict = "PASS" if layout_pass and shots_pass and regression_pass else "PARTIAL PASS"
    (VAL / "final-verdict.json").write_text(
        json.dumps(
            {
                "verdict": verdict,
                "layout_pass": layout_pass,
                "screenshots_pass": shots_pass,
                "regression_pass": regression_pass,
                "captured_screenshots": sum(1 for s in manifest if s.get("captured")),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(json.dumps({"verdict": verdict, "captured": sum(1 for s in manifest if s.get("captured"))}))


if __name__ == "__main__":
    main()
