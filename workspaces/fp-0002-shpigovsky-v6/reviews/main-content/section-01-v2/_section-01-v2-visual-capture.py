"""FP-0002 V6 — Section 01 V2 desktop validation screenshots."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "reviews" / "main-content" / "section-01-v2"


def ensure_playwright() -> None:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def main() -> int:
    ensure_playwright()
    from playwright.sync_api import sync_playwright

    dist = ROOT / "dist" / "index.html"
    if not dist.is_file():
        print(f"MISSING_BUILD: {dist}")
        return 2

    OUT.mkdir(parents=True, exist_ok=True)
    url = dist.resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1398, "height": 900})
        page.goto(url, wait_until="networkidle")
        page.screenshot(path=str(OUT / "FP-0002-V6-SECTION-01-V2-DESKTOP.png"), full_page=False)

        page.set_viewport_size({"width": 1398, "height": 1600})
        page.goto(url, wait_until="networkidle")
        el = page.locator(".home-recovery-intro")
        box = el.bounding_box()
        if box:
            page.screenshot(
                path=str(OUT / "FP-0002-V6-SECTION-01-V2-HERO-CONTEXT.png"),
                clip={"x": 0, "y": max(0, box["y"] - 120), "width": 1398, "height": min(1600, box["height"] + 200)},
            )
        page.screenshot(path=str(OUT / "FP-0002-V6-SECTION-01-V2-FULL-CONTEXT.png"), full_page=True)

        mobile = browser.new_page(viewport={"width": 390, "height": 844})
        mobile.goto(url, wait_until="networkidle")
        overflow = mobile.evaluate(
            "() => ({sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth})"
        )
        mobile.close()
        browser.close()

    print({"overflow_mobile": overflow, "outputs": str(OUT)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
