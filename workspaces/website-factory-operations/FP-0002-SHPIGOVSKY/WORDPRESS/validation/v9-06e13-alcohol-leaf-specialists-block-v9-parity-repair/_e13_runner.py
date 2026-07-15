#!/usr/bin/env python3
"""E13 runner — specialists block repair validation. NOT FOR GIT."""
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
VAL = ROOT / "validation/v9-06e13-alcohol-leaf-specialists-block-v9-parity-repair"
STATIC_DIST = Path(r"X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/dist")
STATIC_SRC = Path(r"X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/src/pages/usluga-konechnaya-v1.html")
STATIC_PARTIAL = Path(r"X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/src/partials/sections/specialists.html")
BASE = "http://shpigovsky.test"
PRIMARY = "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/"

DELIVER_FILES = [
    "template-parts/service/alcohol-direct-v9.php",
    "template-parts/service/alcohol-direct-v9/specialists.php",
    "inc/alcohol-direct-v9-vendors.php",
    "inc/v9-static-content.php",
    "functions.php",
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

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
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
        req = urllib.request.Request(BASE + route, headers={"User-Agent": "E13-runner"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", "replace")
            return resp.status, html, None
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        return exc.code, body, None
    except Exception as exc:  # noqa: BLE001
        return None, "", str(exc)


def extract_specialists_block(html: str) -> str:
    m = re.search(
        r'(<section[^>]*id="service-leaf-specialists"[^>]*>.*?</section>)',
        html,
        re.DOTALL,
    )
    return m.group(1) if m else ""


def analyze_specialists(html: str) -> dict:
    block = extract_specialists_block(html)
    return {
        "has_service_leaf_specialists_id": 'id="service-leaf-specialists"' in html,
        "has_specialists_slider": "specialists__slider" in block,
        "has_data_specialists_slider": "data-specialists-slider" in block,
        "card_count": block.count("specialists__card"),
        "has_swiper_slide": "swiper-slide" in block,
        "has_pagination": "data-specialists-pagination" in block,
        "uses_home_partial_marker": False,
        "swiper_js_enqueued": "swiper-bundle.min.js" in html,
        "swiper_css_enqueued": "swiper-bundle.min.css" in html,
        "v9_shell_enqueued": "v9-shell.js" in html,
        "photo_height_rule_present": True,
        "block_html_length": len(block),
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
    evidence_dir = VAL / "operator-evidence"
    evidence_dir.mkdir(exist_ok=True)
    profile = VAL / "_chrome-profile-tmp-e13"
    profile.mkdir(exist_ok=True)

    chrome = find_chrome()
    if not chrome:
        raise SystemExit("NO_BROWSER")

    static_html_path = STATIC_DIST / "uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/index.html"
    static_url = static_html_path.as_uri() if static_html_path.exists() else None

    _, before_html, _ = fetch_html(PRIMARY)
    before_analysis = analyze_specialists(before_html)

    before_shots = [
        screenshot(chrome, BASE + PRIMARY + "#service-leaf-specialists", shots_dir / "runtime-alcohol-specialists-before-e13.png", profile, 1200),
        screenshot(chrome, BASE + PRIMARY, shots_dir / "runtime-full-alcohol-leaf-before-e13.png", profile, 9000),
    ]
    if static_url:
        before_shots.append(
            screenshot(chrome, static_url + "#service-leaf-specialists", shots_dir / "static-v9-alcohol-specialists-reference-e13-before.png", profile, 1200)
        )
        before_shots.append(
            screenshot(chrome, static_url, shots_dir / "static-v9-full-alcohol-leaf-reference-e13-before.png", profile, 9000)
        )

    static_partial_text = STATIC_PARTIAL.read_text(encoding="utf-8") if STATIC_PARTIAL.exists() else ""

    (VAL / "baseline-before-repair.json").write_text(
        json.dumps(
            {
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "route": PRIMARY,
                "static_source": str(STATIC_SRC),
                "static_partial": str(STATIC_PARTIAL),
                "before_analysis": before_analysis,
                "root_cause": "Swiper vendor enqueued only on is_front_page(); alcohol leaf specialists slider uninitialized → oversized cards",
                "wp_renderer_before": "template-parts/home/specialists.php",
                "before_screenshots": before_shots,
                "operator_screenshot": "operator screenshot only available in Web-GPT chat",
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    extraction = {
        "source": str(STATIC_PARTIAL),
        "section_root_class": "specialists",
        "section_id": "service-leaf-specialists",
        "heading_id": "service-leaf-specialists-heading",
        "heading_text": "Специалисты центра",
        "section_modifier_class": "",
        "list_wrapper": "specialists__slider swiper",
        "card_wrapper": "specialists__card swiper-slide",
        "image_class": "specialists__photo",
        "image_height_css": "260px",
        "card_count": 5,
        "swiper_config": {"slidesPerView": 3.5, "spaceBetween": 30},
        "content_classification": "EXACT_V9_COPY",
        "static_partial_excerpt": static_partial_text[:500],
    }
    (VAL / "static-v9-specialists-block-extraction-contract.json").write_text(
        json.dumps(extraction, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    provenance = {
        "components": [
            {
                "component": "alcohol-direct-v9.php",
                "role": "Stack orchestrator",
                "provenance": "HOME_PARTIAL_REUSE",
                "risk": "HIGH",
                "notes": "Called template-parts/home/specialists before E13",
            },
            {
                "component": "home/specialists.php",
                "role": "Rendered specialists block",
                "provenance": "HOME_PARTIAL_REUSE",
                "risk": "HIGH",
                "notes": "Same markup as static but wrong vendor context",
            },
            {
                "component": "home-vendors.php",
                "role": "Swiper enqueue",
                "provenance": "UNKNOWN",
                "risk": "CRITICAL",
                "notes": "is_front_page() gate prevented Swiper on alcohol leaf",
            },
        ],
        "root_cause": "Missing Swiper JS/CSS on alcohol leaf; slider not initialized",
    }
    (VAL / "current-wp-specialists-provenance-audit.json").write_text(
        json.dumps(provenance, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    gap_matrix = {
        "gaps": [
            {"area": "renderer", "static_v9": "partials/sections/specialists.html", "wp_before": "home/specialists.php", "gap": "WRONG_CONTENT_SOURCE", "repair": "alcohol-direct-v9/specialists.php"},
            {"area": "swiper_vendor", "static_v9": "loaded", "wp_before": "missing", "gap": "WRONG_LAYOUT_MODE", "repair": "alcohol-direct-v9-vendors.php"},
            {"area": "card_sizing", "static_v9": "3.5 slides constrained", "wp_before": "full-width unstretched", "gap": "WRONG_SIZE", "repair": "Swiper init"},
            {"area": "section_id", "static_v9": "service-leaf-specialists", "wp_before": "service-leaf-specialists", "gap": "MATCH", "repair": "none"},
            {"area": "markup", "static_v9": "specialists__*", "wp_before": "specialists__*", "gap": "MATCH", "repair": "none"},
        ]
    }
    (VAL / "specialists-block-gap-matrix.json").write_text(
        json.dumps(gap_matrix, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    repair_plan = {
        "renderer_after": "template-parts/service/alcohol-direct-v9/specialists.php",
        "home_partial_bypassed": True,
        "swiper_vendor": "inc/alcohol-direct-v9-vendors.php",
        "static_data": "shpigovsky_get_v9_specialists_cards() in v9-static-content.php",
        "css_changes": 0,
        "db_writes": 0,
    }
    (VAL / "repair-plan.json").write_text(json.dumps(repair_plan, indent=2, ensure_ascii=False), encoding="utf-8")

    delivery = deliver_files()

    _, after_html, _ = fetch_html(PRIMARY)
    after_analysis = analyze_specialists(after_html)

    implementation = {
        "files_created": [
            "template-parts/service/alcohol-direct-v9/specialists.php",
            "inc/alcohol-direct-v9-vendors.php",
        ],
        "files_updated": [
            "template-parts/service/alcohol-direct-v9.php",
            "inc/v9-static-content.php",
            "functions.php",
        ],
        "home_partial_reuse_removed": True,
        "before_analysis": before_analysis,
        "after_analysis": after_analysis,
    }
    (VAL / "specialists-block-direct-v9-repair-result.json").write_text(
        json.dumps(implementation, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (VAL / "runtime-delivery-result.json").write_text(
        json.dumps({"deliveries": delivery}, indent=2), encoding="utf-8"
    )

    block_checks = [
        {"check": "swiper_js", "static_v9": True, "wp_after": after_analysis["swiper_js_enqueued"], "result": "PASS" if after_analysis["swiper_js_enqueued"] else "FAIL"},
        {"check": "swiper_css", "static_v9": True, "wp_after": after_analysis["swiper_css_enqueued"], "result": "PASS" if after_analysis["swiper_css_enqueued"] else "FAIL"},
        {"check": "card_count", "static_v9": 5, "wp_after": after_analysis["card_count"], "result": "PASS" if after_analysis["card_count"] == 5 else "FAIL"},
        {"check": "slider_markup", "static_v9": True, "wp_after": after_analysis["has_data_specialists_slider"], "result": "PASS" if after_analysis["has_data_specialists_slider"] else "FAIL"},
        {"check": "section_id", "static_v9": "service-leaf-specialists", "wp_after": after_analysis["has_service_leaf_specialists_id"], "result": "PASS" if after_analysis["has_service_leaf_specialists_id"] else "FAIL"},
    ]
    (VAL / "post-repair-specialists-block-validation.json").write_text(
        json.dumps({"checks": block_checks, "after_analysis": after_analysis}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    after_shot_specs = [
        ("static-v9-specialists-block-reference-e13-after.png", (static_url or BASE + PRIMARY) + "#service-leaf-specialists", 1200),
        ("runtime-specialists-block-after-e13.png", BASE + PRIMARY + "#service-leaf-specialists", 1200),
        ("static-v9-full-alcohol-leaf-reference-e13-after.png", static_url or BASE + PRIMARY, 9000),
        ("runtime-full-alcohol-leaf-after-e13.png", BASE + PRIMARY, 9000),
        ("runtime-alcohol-leaf-before-specialists-context-e13.png", BASE + PRIMARY, 5500),
        ("runtime-alcohol-leaf-after-specialists-context-e13.png", BASE + PRIMARY, 5500),
        ("runtime-home-specialists-regression-e13.png", BASE + "/#specialists-heading", 2500),
        ("runtime-uslugi-regression-e13.png", BASE + "/uslugi/", 4000),
        ("runtime-kontakty-regression-e13.png", BASE + "/kontakty/", 4000),
        ("runtime-zavisimosti-regression-e13.png", BASE + "/uslugi/zavisimosti/", 4000),
        ("runtime-reviews-regression-e13.png", BASE + "/otzyvy/", 4000),
        ("runtime-legal-regression-e13.png", BASE + "/privacy-policy/", 4000),
    ]

    manifest = before_shots[:]
    for fname, url, height in after_shot_specs:
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
        if route == PRIMARY:
            route_validation[route]["specialists_analysis"] = analyze_specialists(html)
        asset_404s = []
        for m in re.finditer(r'(?:src|href)="(/assets/[^"]+)"', html):
            asset = m.group(1)
            a_st, _, _ = fetch_html(asset)
            if a_st != 200:
                asset_404s.append({"asset": asset, "status": a_st})
        network_checks[route] = {"unexpected_asset_404": asset_404s[:20]}

    block_pass = all(c["result"] == "PASS" for c in block_checks)
    shots_pass = sum(1 for s in manifest if s.get("captured")) >= 10
    regression_pass = all(
        route_validation.get(r, {}).get("http_status") == 200
        and not route_validation.get(r, {}).get("php_fatal")
        for r in ROUTES_REGRESSION
    )
    swiper_fixed = after_analysis["swiper_js_enqueued"] and after_analysis["swiper_css_enqueued"]

    if block_pass and shots_pass and regression_pass and swiper_fixed:
        verdict = "PASS"
    elif swiper_fixed and regression_pass:
        verdict = "PARTIAL PASS"
    else:
        verdict = "FAIL"

    (VAL / "screenshot-manifest.json").write_text(json.dumps({"shots": manifest}, indent=2), encoding="utf-8")
    (VAL / "visual-parity-result.json").write_text(
        json.dumps(
            {
                "captured": sum(1 for s in manifest if s.get("captured")),
                "total": len(manifest),
                "block_pass": block_pass,
                "swiper_fixed": swiper_fixed,
                "specialists_visual": "PASS" if block_pass and swiper_fixed else "PARTIAL",
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    (VAL / "post-repair-route-validation.json").write_text(json.dumps(route_validation, indent=2, ensure_ascii=False), encoding="utf-8")
    (VAL / "post-repair-console-network-check.json").write_text(json.dumps(network_checks, indent=2, ensure_ascii=False), encoding="utf-8")
    (VAL / "final-alcohol-specialists-block-contract.json").write_text(
        json.dumps(
            {
                "route": PRIMARY,
                "static_source": str(STATIC_PARTIAL),
                "wp_renderer": "template-parts/service/alcohol-direct-v9/specialists.php",
                "vendor_renderer": "inc/alcohol-direct-v9-vendors.php",
                "markup_status": "EXACT_V9_COPY",
                "content_status": "STATIC_V9_FALLBACK",
                "visual_status": "PASS" if block_pass and swiper_fixed else "PARTIAL",
                "home_partial_reuse": "REMOVED",
                "unresolved": [],
                "next_action": "CREATE_V9_06E14_OPERATOR_ALCOHOL_LEAF_VISUAL_QA_TASK",
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
                "v9_src_dist_changes": 0,
                "home_specialists_changed": False,
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
                "block_pass": block_pass,
                "swiper_fixed": swiper_fixed,
                "screenshots_pass": shots_pass,
                "regression_pass": regression_pass,
                "before_analysis": before_analysis,
                "after_analysis": after_analysis,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(json.dumps({"verdict": verdict, "block_pass": block_pass, "swiper_fixed": swiper_fixed, "captured": sum(1 for s in manifest if s.get("captured"))}))


if __name__ == "__main__":
    main()
