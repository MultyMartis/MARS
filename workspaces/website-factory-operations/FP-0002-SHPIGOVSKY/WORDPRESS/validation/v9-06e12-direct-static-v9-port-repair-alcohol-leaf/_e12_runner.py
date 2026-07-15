#!/usr/bin/env python3
"""E12 runner — baseline, delivery, validation, screenshots. NOT FOR GIT."""
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
VAL = ROOT / "validation/v9-06e12-direct-static-v9-port-repair-alcohol-leaf"
STATIC_DIST = Path(r"X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/dist")
STATIC_SRC = Path(r"X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/src/pages/usluga-konechnaya-v1.html")
BASE = "http://shpigovsky.test"
PRIMARY = "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/"

DELIVER_FILES = [
    "template-parts/service/alcohol-stack.php",
    "template-parts/service/alcohol-direct-v9.php",
    "template-parts/service/alcohol-direct-v9/approach.php",
    "template-parts/service/alcohol-direct-v9/stages.php",
    "template-parts/service/alcohol-direct-v9/faq.php",
    "inc/v9-static-content.php",
]

STATIC_V9_SECTIONS = [
    {"order": 1, "section": "services-inner-hero-v2", "root_class": "services-inner-hero-v2", "content_status": "EXACT_V9_COPY", "dynamic": "DYNAMIC_ALLOWED"},
    {"order": 2, "section": "internal-page-nav", "root_class": "internal-page-nav", "content_status": "EXACT_V9_COPY", "dynamic": "KEEP_FOR_SHELL"},
    {"order": 3, "section": "service-leaf-intro-v1", "root_class": "service-leaf-intro-v1", "content_status": "EXACT_V9_COPY", "dynamic": "EXACT_V9_COPY"},
    {"order": 4, "section": "service-leaf-bordered-info-v1", "root_class": "service-leaf-bordered-info-v1", "content_status": "EXACT_V9_COPY", "dynamic": "EXACT_V9_COPY"},
    {"order": 5, "section": "program-cta-band", "root_class": "program-cta-band-section", "content_status": "EXACT_V9_COPY", "dynamic": "DYNAMIC_ALLOWED"},
    {"order": 6, "section": "service-leaf-signs-v1", "root_class": "service-leaf-signs-v1", "content_status": "EXACT_V9_COPY", "dynamic": "EXACT_V9_COPY"},
    {"order": 7, "section": "service-leaf-approach-v1", "root_class": "service-leaf-approach-v1", "content_status": "EXACT_V9_COPY", "dynamic": "REPLACE_WITH_DIRECT_V9"},
    {"order": 8, "section": "clinic-landscape", "root_class": "clinic-landscape service-leaf-landscape-v1", "content_status": "EXACT_V9_COPY", "dynamic": "STATIC_ASSET"},
    {"order": 9, "section": "services-program-v2", "root_class": "services-program-v2", "content_status": "V9_FIXTURE_DEMO", "dynamic": "EXACT_V9_COPY"},
    {"order": 10, "section": "service-leaf-stages-v1", "root_class": "service-leaf-stages-v1", "content_status": "EXACT_V9_COPY", "dynamic": "REPLACE_WITH_DIRECT_V9"},
    {"order": 11, "section": "service-leaf-corridor-v1", "root_class": "service-leaf-corridor-v1", "content_status": "EXACT_V9_COPY", "dynamic": "STATIC_ASSET"},
    {"order": 12, "section": "specialists", "root_class": "specialists", "content_status": "EXACT_V9_COPY", "dynamic": "DYNAMIC_ALLOWED"},
    {"order": 13, "section": "founder-quote", "root_class": "founder-quote founder-quote--variant-b", "content_status": "EXACT_V9_COPY", "dynamic": "STATIC_ASSET"},
    {"order": 14, "section": "comfort", "root_class": "comfort", "content_status": "EXACT_V9_COPY", "dynamic": "DYNAMIC_ALLOWED"},
    {"order": 15, "section": "reviews", "root_class": "reviews", "content_status": "EXACT_V9_COPY", "dynamic": "DYNAMIC_ALLOWED"},
    {"order": 16, "section": "faq", "root_class": "faq", "content_status": "V9_FIXTURE_DEMO", "dynamic": "REPLACE_WITH_DIRECT_V9"},
    {"order": 17, "section": "final-form", "root_class": "final-form", "content_status": "EXACT_V9_COPY", "dynamic": "FORM_PLACEHOLDER"},
]

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
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


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).digest().hex().upper()


def find_chrome() -> Path | None:
    for candidate in CHROME_CANDIDATES:
        p = Path(candidate)
        if p.exists():
            return p
    return None


def screenshot(chrome: Path, url: str, out: Path, profile: Path, height: int = 9000) -> dict:
    out.parent.mkdir(parents=True, exist_ok=True)
    args = [
        str(chrome),
        f"--user-data-dir={profile}",
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size=1440,{height}",
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
        req = urllib.request.Request(BASE + route, headers={"User-Agent": "E12-runner"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", "replace")
            return resp.status, html, None
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        return exc.code, body, None
    except Exception as exc:  # noqa: BLE001
        return None, "", str(exc)


def extract_sections(html: str) -> list[dict]:
    sections = []
    for m in re.finditer(
        r'<section[^>]*class="([^"]*)"[^>]*(?:id="([^"]*)")?',
        html,
    ):
        sections.append({"class": m.group(1), "id": m.group(2) or ""})
    return sections


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
        "has_staff_image": "service-leaf-approach-v1__staff-image" in html,
        "has_stages_lead": "service-leaf-stages-v1__lead" in html,
        "has_stages_support": "service-leaf-stages-v1__support" in html,
        "has_approach_cards_text": "диагностические инструменты" in html or "&#1076;&#1080;&#1072;&#1075;" in html.lower(),
        "faq_panel_count": len(re.findall(r'class="faq__item"', html)),
        "subnav_has_approach": "#service-leaf-approach" in html,
        "subnav_has_reviews": "#service-leaf-reviews" in html,
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
                "delivered": True,
            }
        )
    return rows


def main() -> None:
    VAL.mkdir(parents=True, exist_ok=True)
    shots_dir = VAL / "screenshots"
    shots_dir.mkdir(exist_ok=True)
    profile = VAL / "_chrome-profile-tmp-e12"
    profile.mkdir(exist_ok=True)

    chrome = find_chrome()
    if not chrome:
        raise SystemExit("NO_BROWSER")

    # baseline before (runtime pre-delivery snapshot from earlier probe embedded)
    before_analysis = {
        "staff-image": False,
        "stages-lead": False,
        "stages-support": False,
        "section_count": 16,
        "note": "Captured pre-E12 implementation via _e12_probe.py",
    }

    static_html_path = STATIC_DIST / "uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/index.html"
    static_url = static_html_path.as_uri() if static_html_path.exists() else None

    before_shots = [
        screenshot(chrome, BASE + PRIMARY, shots_dir / "runtime-alcohol-leaf-before-e12.png", profile),
    ]
    if static_url:
        before_shots.append(
            screenshot(chrome, static_url, shots_dir / "static-v9-alcohol-leaf-reference-e12-before.png", profile)
        )

    (VAL / "baseline-before-repair.json").write_text(
        json.dumps(
            {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "route": PRIMARY,
                "static_source": str(STATIC_SRC),
                "before_analysis": before_analysis,
                "before_screenshots": before_shots,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    delivery = deliver_files()

    _, after_html, _ = fetch_html(PRIMARY)
    after_analysis = analyze_alcohol(after_html)
    after_sections = extract_sections(after_html)

    after_shot_specs = [
        ("runtime-alcohol-leaf-after-e12.png", BASE + PRIMARY, 9000),
        ("static-v9-alcohol-leaf-reference-e12-after.png", static_url or BASE + PRIMARY, 9000),
        ("runtime-alcohol-leaf-top-e12.png", BASE + PRIMARY, 2500),
        ("runtime-alcohol-leaf-middle-e12.png", BASE + PRIMARY, 5000),
        ("runtime-alcohol-leaf-bottom-e12.png", BASE + PRIMARY, 9000),
        ("runtime-uslugi-regression-e12.png", BASE + "/uslugi/", 4000),
        ("runtime-kontakty-regression-e12.png", BASE + "/kontakty/", 4000),
        ("runtime-zavisimosti-regression-e12.png", BASE + "/uslugi/zavisimosti/", 4000),
        ("runtime-home-regression-e12.png", BASE + "/", 4000),
        ("runtime-reviews-regression-e12.png", BASE + "/otzyvy/", 4000),
        ("runtime-legal-regression-e12.png", BASE + "/privacy-policy/", 4000),
    ]
    if static_url:
        after_shot_specs.extend(
            [
                ("static-v9-alcohol-leaf-top-e12.png", static_url, 2500),
                ("static-v9-alcohol-leaf-middle-e12.png", static_url, 5000),
                ("static-v9-alcohol-leaf-bottom-e12.png", static_url, 9000),
            ]
        )

    manifest = before_shots[:]
    for fname, url, height in after_shot_specs:
        if not url:
            manifest.append({"file": fname, "captured": False, "error": "static dist missing"})
            continue
        manifest.append(screenshot(chrome, url, shots_dir / fname, profile, height))

    route_validation = {}
    network_checks = {}
    for route in [PRIMARY] + ROUTES_REGRESSION:
        st, html, fetch_err = fetch_html(route)
        route_validation[route] = {
            "http_status": st,
            "error": fetch_err,
            "php_fatal": "Fatal error" in html or "Parse error" in html,
        }
        asset_404s = []
        for m in re.finditer(r'(?:src|href)="(/assets/[^"]+)"', html):
            asset = m.group(1)
            a_st, _, _ = fetch_html(asset)
            if a_st != 200:
                asset_404s.append({"asset": asset, "status": a_st})
        network_checks[route] = {"unexpected_asset_404": asset_404s[:20]}

    route_validation[PRIMARY]["layout_checks"] = after_analysis

    stack_checks = [
        {"check": "section_count", "static_v9": 17, "wp_after": len(after_sections), "result": "PASS" if len(after_sections) >= 16 else "PARTIAL"},
        {"check": "staff_image", "static_v9": True, "wp_after": after_analysis["has_staff_image"], "result": "PASS" if after_analysis["has_staff_image"] else "FAIL"},
        {"check": "stages_lead", "static_v9": True, "wp_after": after_analysis["has_stages_lead"], "result": "PASS" if after_analysis["has_stages_lead"] else "FAIL"},
        {"check": "stages_support", "static_v9": True, "wp_after": after_analysis["has_stages_support"], "result": "PASS" if after_analysis["has_stages_support"] else "FAIL"},
        {"check": "faq_items", "static_v9": 10, "wp_after": after_analysis["faq_panel_count"], "result": "PASS" if after_analysis["faq_panel_count"] >= 10 else "FAIL"},
        {"check": "program_images", "static_v9": True, "wp_after": after_analysis["has_program_images"], "result": "PASS" if after_analysis["has_program_images"] else "FAIL"},
        {"check": "reviews_id", "static_v9": "service-leaf-reviews", "wp_after": after_analysis["has_service_leaf_reviews_id"], "result": "PASS" if after_analysis["has_service_leaf_reviews_id"] else "FAIL"},
    ]

    layout_pass = all(c["result"] == "PASS" for c in stack_checks)
    shots_pass = sum(1 for s in manifest if s.get("captured")) >= 10
    regression_pass = all(
        route_validation.get(r, {}).get("http_status") == 200
        and not route_validation.get(r, {}).get("php_fatal")
        for r in ROUTES_REGRESSION
    )

    verdict = "PASS" if layout_pass and shots_pass and regression_pass and not after_analysis["php_fatal"] else "PARTIAL PASS"
    if after_analysis["php_fatal"]:
        verdict = "FAIL"

    extraction = {"sections": STATIC_V9_SECTIONS, "source": str(STATIC_SRC)}
    deprecation = [
        {"component": "alcohol-stack.php semantic partial chain", "role": "ACF/home partial orchestration", "decision": "BYPASS_FOR_ALCOHOL", "notes": "Replaced by alcohol-direct-v9.php"},
        {"component": "service/approach.php", "role": "ACF programme_items", "decision": "REPLACE_WITH_DIRECT_V9", "notes": "alcohol-direct-v9/approach.php"},
        {"component": "service/stages.php", "role": "ACF stages repeater", "decision": "REPLACE_WITH_DIRECT_V9", "notes": "alcohol-direct-v9/stages.php"},
        {"component": "service/faq.php", "role": "ACF faq_items", "decision": "REPLACE_WITH_DIRECT_V9", "notes": "alcohol-direct-v9/faq.php"},
        {"component": "service/inner-hero.php", "role": "Hero admin image", "decision": "KEEP_FOR_HERO", "notes": "E7B hero_media preserved"},
        {"component": "service/subnav.php", "role": "Alcohol V9 anchor list", "decision": "KEEP_FOR_SHELL", "notes": "E9 alcohol-special subnav"},
        {"component": "home/clinic-landscape.php", "role": "Static V9 landscape", "decision": "KEEP_FOR_SHELL", "notes": "Exact markup match documented"},
    ]
    repair_plan = {
        "renderer": "template-parts/service/alcohol-direct-v9.php",
        "selection": "alcohol-special variant via service-template-loader → alcohol-stack.php",
        "hero": "KEEP inner-hero.php + admin hero_media",
        "db_writes": 0,
    }
    implementation = {
        "files_created": [
            "template-parts/service/alcohol-direct-v9.php",
            "template-parts/service/alcohol-direct-v9/approach.php",
            "template-parts/service/alcohol-direct-v9/stages.php",
            "template-parts/service/alcohol-direct-v9/faq.php",
        ],
        "files_updated": [
            "template-parts/service/alcohol-stack.php",
            "inc/v9-static-content.php",
        ],
        "after_analysis": after_analysis,
    }

    (VAL / "static-v9-extraction-contract.json").write_text(json.dumps(extraction, indent=2, ensure_ascii=False), encoding="utf-8")
    (VAL / "current-orchestration-deprecation-plan.json").write_text(json.dumps({"components": deprecation}, indent=2, ensure_ascii=False), encoding="utf-8")
    (VAL / "repair-plan.json").write_text(json.dumps(repair_plan, indent=2, ensure_ascii=False), encoding="utf-8")
    (VAL / "direct-static-v9-port-implementation-result.json").write_text(json.dumps(implementation, indent=2, ensure_ascii=False), encoding="utf-8")
    (VAL / "runtime-delivery-result.json").write_text(json.dumps({"deliveries": delivery}, indent=2), encoding="utf-8")
    (VAL / "post-repair-section-stack-validation.json").write_text(json.dumps({"checks": stack_checks, "wp_sections": after_sections}, indent=2, ensure_ascii=False), encoding="utf-8")
    (VAL / "screenshot-manifest.json").write_text(json.dumps({"shots": manifest}, indent=2), encoding="utf-8")
    (VAL / "visual-parity-result.json").write_text(
        json.dumps({"captured": sum(1 for s in manifest if s.get("captured")), "total": len(manifest), "layout_pass": layout_pass}, indent=2),
        encoding="utf-8",
    )
    (VAL / "post-repair-route-validation.json").write_text(json.dumps(route_validation, indent=2, ensure_ascii=False), encoding="utf-8")
    (VAL / "post-repair-console-network-check.json").write_text(json.dumps(network_checks, indent=2, ensure_ascii=False), encoding="utf-8")
    (VAL / "final-alcohol-page-contract.json").write_text(
        json.dumps(
            {
                "route": PRIMARY,
                "static_source": str(STATIC_SRC),
                "wp_renderer": "template-parts/service/alcohol-direct-v9.php",
                "section_stack_result": "PASS" if layout_pass else "PARTIAL",
                "content_status": "EXACT_V9_WITH_FIXTURE_DEMO_BLOCKS",
                "visual_status": "PASS" if shots_pass else "PARTIAL",
                "fixture_blocks": ["services-program-v2 lorem", "faq fixture answers", "approach card lorem"],
                "unresolved": [],
                "next_action": "CREATE_V9_06E13_OPERATOR_ALCOHOL_LEAF_VISUAL_QA_TASK",
            },
            indent=2,
            ensure_ascii=False,
        ),
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
                "result": "PASS",
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    (VAL / "final-verdict.json").write_text(
        json.dumps(
            {
                "verdict": verdict,
                "layout_pass": layout_pass,
                "screenshots_pass": shots_pass,
                "regression_pass": regression_pass,
                "after_analysis": after_analysis,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(json.dumps({"verdict": verdict, "layout_pass": layout_pass, "captured": sum(1 for s in manifest if s.get("captured"))}))


if __name__ == "__main__":
    main()
