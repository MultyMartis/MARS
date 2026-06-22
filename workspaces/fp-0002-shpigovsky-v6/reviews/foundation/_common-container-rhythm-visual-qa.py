"""FP-0002 V6 common container + section rhythm visual capture @ 1398px."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST_HTML = ROOT / "dist" / "index.html"
OUT_DIR = Path(__file__).resolve().parent / "visual"
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

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    url = DIST_HTML.as_uri()

    shots = {
        "FP-0002-V6-COMMON-CONTAINER-AND-RHYTHM-HEADER.png": {"full_page": False, "clip": {"x": 0, "y": 0, "width": VIEWPORT_W, "height": 220}},
        "FP-0002-V6-COMMON-CONTAINER-AND-RHYTHM-FOOTER.png": {"full_page": False, "clip": None, "footer": True},
        "FP-0002-V6-COMMON-CONTAINER-AND-RHYTHM-FULL.png": {"full_page": True, "clip": None},
    }

    selectors = {
        "header_container": ".site-header .container",
        "footer_container": ".site-footer .container",
        "hero_root": ".hero",
    }

    props = ["maxWidth", "width", "paddingTop", "paddingBottom", "paddingInline", "marginInline"]

    computed: dict = {}

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": VIEWPORT_W, "height": VIEWPORT_H})
        page.goto(url, wait_until="networkidle")

        for name, opts in shots.items():
            path = OUT_DIR / name
            if opts.get("footer"):
                footer = page.query_selector(".site-footer")
                if footer:
                    box = footer.bounding_box()
                    if box:
                        page.screenshot(path=str(path), clip=box)
                    else:
                        page.screenshot(path=str(path), full_page=False)
                else:
                    page.screenshot(path=str(path), full_page=False)
            elif opts.get("clip"):
                page.screenshot(path=str(path), clip=opts["clip"])
            else:
                page.screenshot(path=str(path), full_page=opts["full_page"])

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

    out_json = OUT_DIR / "_common-container-rhythm-computed.json"
    out_json.write_text(json.dumps(computed, indent=2), encoding="utf-8")
    print(f"WROTE {len(shots)} screenshots to {OUT_DIR}")
    print(f"WROTE {out_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
