"""FP-0002 V6 — Section 02 Figma portrait fix visual capture."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DIST_HTML = ROOT / "dist" / "index.html"
MOCKUP = (
    ROOT.parent
    / "website-factory-operations"
    / "FP-0002-SHPIGOVSKY"
    / "INCOMING"
    / "01_DESIGN"
    / "HOME-PAGE-FULL-MOCKUP.jpg"
)
META = ROOT / "reviews" / "main-content" / "section-02-audit" / "FP-0002-V6-SECTION-02-BOUNDARY-META.json"
OUT_DIR = ROOT / "reviews" / "main-content" / "section-02-portrait-fix"


def ensure_deps() -> None:
    try:
        from PIL import Image  # noqa: F401
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def main() -> int:
    if not DIST_HTML.is_file():
        print(f"MISSING_BUILD: {DIST_HTML}")
        return 2

    ensure_deps()
    from PIL import Image
    from playwright.sync_api import sync_playwright

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    meta = json.loads(META.read_text(encoding="utf-8"))
    b = meta["boundaries"]
    y0 = b["section_02_start_y"] - 24
    y1 = b["section_02_end_y"] + 24

    mockup = Image.open(MOCKUP).convert("RGB")
    mockup.crop((0, y0, mockup.width, y1)).save(OUT_DIR / "FP-0002-V6-SECTION-02-FIGMA-PORTRAIT-CONTEXT.png")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1398, "height": 3200})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        page.locator(".home-founder-quote").screenshot(
            path=str(OUT_DIR / "FP-0002-V6-SECTION-02-FIGMA-PORTRAIT-DESKTOP.png")
        )
        page.set_viewport_size({"width": 390, "height": 2400})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        page.locator(".home-founder-quote").screenshot(
            path=str(OUT_DIR / "FP-0002-V6-SECTION-02-FIGMA-PORTRAIT-MOBILE.png")
        )
        browser.close()

    render = Image.open(OUT_DIR / "FP-0002-V6-SECTION-02-FIGMA-PORTRAIT-DESKTOP.png").convert("RGB")
    reference = Image.open(OUT_DIR / "FP-0002-V6-SECTION-02-FIGMA-PORTRAIT-CONTEXT.png").convert("RGB")
    target_h = max(render.height, reference.height)
    canvas = Image.new("RGB", (render.width + reference.width + 20, target_h), (240, 244, 248))
    canvas.paste(reference, (0, 0))
    canvas.paste(render, (reference.width + 20, 0))
    canvas.save(OUT_DIR / "FP-0002-V6-SECTION-02-FIGMA-PORTRAIT-COMPARISON.png")
    print(f"CAPTURED in {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
