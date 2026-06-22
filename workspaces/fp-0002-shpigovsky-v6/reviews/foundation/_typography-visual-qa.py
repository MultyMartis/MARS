"""FP-0002 V6 production typography — SECTION-001 visual capture @ 1398px."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST_HTML = ROOT / "dist" / "index.html"
OUT_PNG = Path(__file__).resolve().parent / "visual" / "FP-0002-V6-PRODUCTION-TYPOGRAPHY-SECTION-001.png"
OUT_JSON = Path(__file__).resolve().parent / "visual" / "_typography-computed-styles.json"
VIEWPORT_W, VIEWPORT_H = 1398, 1000


def ensure_playwright():
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def main() -> int:
    if not DIST_HTML.is_file():
        print(f"MISSING_BUILD: {DIST_HTML}")
        return 2

    ensure_playwright()
    from playwright.sync_api import sync_playwright

    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    url = DIST_HTML.as_uri()

    selectors = {
        "body": "body",
        "header_address": ".site-header__address",
        "header_schedule": ".site-header__schedule",
        "nav_link": ".site-header__nav-link",
        "phone": ".site-header__phone",
        "header_cta": ".site-header__callback",
        "search_button": ".site-header__search",
        "hero_tagline": ".hero__tagline",
        "hero_title": ".hero__title",
        "hero_cta": ".hero__button",
        "global_h2": "h2",
        "global_h3": "h3",
        "header_container": ".site-header__container",
        "hero_root": ".hero",
    }

    props = [
        "fontFamily",
        "fontSize",
        "lineHeight",
        "fontWeight",
        "color",
        "maxWidth",
        "width",
        "height",
    ]

    computed: dict = {}

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": VIEWPORT_W, "height": VIEWPORT_H})
        page.goto(url, wait_until="networkidle")
        page.screenshot(path=str(OUT_PNG), full_page=False)

        for key, sel in selectors.items():
            el = page.query_selector(sel)
            if not el:
                computed[key] = {"missing": True, "selector": sel}
                continue
            computed[key] = page.evaluate(
                """([node, props]) => {
                    const s = getComputedStyle(node);
                    const out = {};
                    for (const p of props) out[p] = s[p];
                    return out;
                }""",
                [el, props],
            )

        browser.close()

    OUT_JSON.write_text(json.dumps(computed, indent=2) + "\n", encoding="utf-8")
    print(f"Screenshot: {OUT_PNG}")
    print(f"Computed: {OUT_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
