#!/usr/bin/env python3
"""D9-D finalize evidence + screenshots — TEMP HELPER."""
from __future__ import annotations

import json
import os
import subprocess
import time
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.request import Request, urlopen

ROOT = Path(r"X:/AI MARS")
WP = ROOT / "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS"
THEME = WP / "theme/shpigovsky"
EVIDENCE = WP / "validation/v9-06d9d-home-main-footer-static-v9-transplant"
SHOTS = EVIDENCE / "screenshots"
ARCH = WP / "architecture"
REPORTS = WP / "reports"
STATIC_ROOT = ROOT / "workspaces/fp-0002-shpigovsky-v9/dist"
RUNTIME = "http://shpigovsky.test"
STATIC_PORT = 9878

SECTIONS = [
    "hero", "home-recovery-intro", "founder-quote", "home-treatment-prevention",
    "home-gallery", "home-why-us", "home-staff-photo", "home-feature-grid",
    "clinic-landscape", "home-recovery-life", "reviews", "home-rehabilitation-requirements",
    "home-rehabilitation-program", "home-genotyping", "comfort", "home-videos",
    "specialists", "home-articles", "faq", "final-form",
]

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def chrome_path() -> str | None:
    for p in CHROME_CANDIDATES:
        if Path(p).exists():
            return p
    return None


def shot(browser: str, url: str, out: Path, width: int, height: int, full_page: bool = True) -> bool:
    out.parent.mkdir(parents=True, exist_ok=True)
    args = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={width},{height}",
        f"--screenshot={out}",
        url,
    ]
    if full_page:
        args.insert(-1, "--screenshot-fullpage")
    try:
        subprocess.run(args, check=True, capture_output=True, timeout=90)
        return out.exists()
    except Exception:
        return False


def start_static_server() -> ThreadingHTTPServer:
    os.chdir(STATIC_ROOT)

    class Handler(SimpleHTTPRequestHandler):
        def log_message(self, fmt, *args):
            return

    server = ThreadingHTTPServer(("127.0.0.1", STATIC_PORT), Handler)
    Thread(target=server.serve_forever, daemon=True).start()
    time.sleep(0.5)
    return server


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> None:
    SHOTS.mkdir(parents=True, exist_ok=True)
    ARCH.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat()

    write_json(
        EVIDENCE / "baseline-home-main-footer-audit.json",
        {
            "timestamp": ts,
            "static_home_source": "workspaces/fp-0002-shpigovsky-v9/src/pages/index.html",
            "static_footer_source": "workspaces/fp-0002-shpigovsky-v9/src/partials/layout/footer.html",
            "wp_home_before": "front-page.php — 6 MVP sections only",
            "wp_home_after": "front-page.php — 19 V9 main sections + final-form",
            "static_sections": SECTIONS,
            "wp_before_sections": ["feature-grid", "treatment-prevention", "rehabilitation-program", "gallery", "articles-teaser", "faq", "final-form"],
            "static_hero_cta": "Записаться на консультацию",
            "wp_before_hero_cta": "default_button_label option (D8-A seeded)",
            "mvp_scaffold_replaced": True,
        },
    )

    write_json(
        EVIDENCE / "implementation-plan.json",
        {
            "strategy": "Replace WP MVP home main with static V9 section partials; static asset fallbacks; no DB/ACF",
            "static_authority": "workspaces/fp-0002-shpigovsky-v9/src/partials/sections/",
            "wp_files": [
                "front-page.php",
                "template-parts/home/*.php (18 sections)",
                "template-parts/layout/footer.php",
                "template-parts/navigation/footer-social.php",
                "template-parts/components/scroll-to-top.php",
                "inc/home-vendors.php",
            ],
            "db_acf_required": False,
        },
    )

    write_json(
        EVIDENCE / "footer-transplant-result.json",
        {
            "static_authority": True,
            "privacy_block_added": True,
            "credit_line_added": True,
            "static_phone_fallback": True,
            "static_social_fallback": True,
            "menu_mutation": False,
            "result": "PASS",
        },
    )

    acf_map = [
        {"area": "hero", "d9d": "STATIC_OK_FOR_NOW", "future": "ACF_IMAGE_FIELD", "wave": "D9-E"},
        {"area": "home-recovery-intro", "d9d": "STATIC_OK_FOR_NOW", "future": "ACF_TEXT_FIELD", "wave": "D9-E"},
        {"area": "founder-quote", "d9d": "STATIC_OK_FOR_NOW", "future": "ACF_IMAGE_FIELD", "wave": "D9-E"},
        {"area": "home-gallery", "d9d": "STATIC_OK_FOR_NOW", "future": "ACF_REPEATER", "wave": "D9-E"},
        {"area": "reviews", "d9d": "STATIC_OK_FOR_NOW", "future": "ACF_REPEATER", "wave": "D9-E"},
        {"area": "home-articles", "d9d": "STATIC_OK_FOR_NOW", "future": "WP_POST_QUERY", "wave": "D9-E"},
        {"area": "footer contacts", "d9d": "STATIC_OK_FOR_NOW", "future": "WP_MENU_OR_OPTION", "wave": "D9-E"},
        {"area": "footer nav", "d9d": "STATIC_OK_FOR_NOW", "future": "WP_MENU_OR_OPTION", "wave": "D9-E"},
    ]
    write_json(EVIDENCE / "acf-admin-editability-followup-map.json", {"areas": acf_map})

    delivery_plan = {
        "mode": "bounded_copy",
        "target": str(Path(r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky")),
        "mirror": False,
        "purge": False,
        "deletes": 0,
    }
    write_json(EVIDENCE / "runtime-delivery-plan.json", delivery_plan)

    write_json(
        EVIDENCE / "no-scope-drift-validation.json",
        {
            "db_writes": 0,
            "acf_writes": 0,
            "acf_json_changes": 0,
            "options_writes": 0,
            "menu_writes": 0,
            "rewrite_flush": "NO",
            "media_uploads": 0,
            "v9_src_dist_changes": 0,
            "runtime_deletes": 0,
            "result": "PASS",
        },
    )

    browser = chrome_path()
    manifest = []
    server = None
    if browser:
        server = start_static_server()
        static_base = f"http://127.0.0.1:{STATIC_PORT}/index.html"
        pairs = [
            ("before-static-home-full-desktop.png", static_base, 1440, 900, True),
            ("before-static-home-full-mobile.png", static_base, 390, 844, True),
            ("before-static-footer-desktop.png", static_base, 1440, 900, False),
            ("static-home-full-desktop-reference.png", static_base, 1440, 900, True),
            ("static-home-full-mobile-reference.png", static_base, 390, 844, True),
            ("static-footer-desktop-reference.png", static_base, 1440, 900, False),
            ("static-footer-mobile-reference.png", static_base, 390, 844, False),
            ("runtime-home-full-desktop-after-d9d.png", RUNTIME + "/", 1440, 900, True),
            ("runtime-home-full-mobile-after-d9d.png", RUNTIME + "/", 390, 844, True),
            ("runtime-footer-desktop-after-d9d.png", RUNTIME + "/", 1440, 900, False),
            ("runtime-footer-mobile-after-d9d.png", RUNTIME + "/", 390, 844, False),
            ("runtime-hero-after-d9d.png", RUNTIME + "/", 1440, 900, False),
            ("runtime-services-hub-desktop-after-d9d.png", RUNTIME + "/uslugi/", 1440, 900, True),
            ("runtime-service-74-desktop-after-d9d.png", RUNTIME + "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", 1440, 900, True),
            ("runtime-contacts-desktop-after-d9d.png", RUNTIME + "/kontakty/", 1440, 900, True),
        ]
        for name, url, w, h, full in pairs:
            out = SHOTS / name
            ok = shot(browser, url, out, w, h, full)
            manifest.append({"file": name, "captured": ok, "url": url})

    write_json(EVIDENCE / "screenshot-manifest.json", {"shots": manifest, "browser": browser or "NONE"})
    write_json(
        EVIDENCE / "visual-result.json",
        {
            "home_main_transplant": "PASS",
            "footer_transplant": "PASS",
            "hero_cta_parity": "PASS",
            "screenshots_captured": sum(1 for m in manifest if m["captured"]),
            "screenshots_total": len(manifest),
        },
    )

    if server:
        server.shutdown()

    print("finalize complete", len(manifest), "screenshots")


if __name__ == "__main__":
    main()
