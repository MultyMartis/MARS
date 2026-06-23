"""FP-0002 V6 — services foundation + home regression screenshots."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST_HOME = ROOT / "dist" / "index.html"
DIST_SERVICES = ROOT / "dist" / "uslugi.html"
OUT = ROOT / "reviews" / "services-page" / "foundation"
WIDTHS = [320, 375, 390, 430, 768, 1024, 1025, 1398]


def ensure_deps() -> None:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def overflow_metrics(page) -> dict:
    return page.evaluate(
        """() => {
            const doc = document.documentElement;
            const body = document.body;
            return {
                docScrollWidth: doc.scrollWidth,
                docClientWidth: doc.clientWidth,
                bodyScrollWidth: body.scrollWidth,
                bodyClientWidth: body.clientWidth,
                horizontalOverflow: Math.max(0, doc.scrollWidth - doc.clientWidth, body.scrollWidth - body.clientWidth)
            };
        }"""
    )


def main() -> int:
    if not DIST_HOME.is_file() or not DIST_SERVICES.is_file():
        print("MISSING_BUILD")
        return 2

    ensure_deps()
    from playwright.sync_api import sync_playwright

    OUT.mkdir(parents=True, exist_ok=True)
    metrics: dict = {"overflow": {}, "files": []}

    with sync_playwright() as p:
        browser = p.chromium.launch()

        def capture(page_path: Path, label: str, width: int, height: int, name: str, full_page: bool = True) -> None:
            page = browser.new_page(viewport={"width": width, "height": height})
            page.goto(page_path.as_uri(), wait_until="networkidle")
            target = OUT / name
            page.screenshot(path=str(target), full_page=full_page)
            metrics["files"].append(name)
            key = f"{label}-{width}"
            metrics["overflow"].setdefault(key, overflow_metrics(page))
            page.close()

        capture(DIST_SERVICES, "services", 1398, 1200, "SERVICES-FOUNDATION-DESKTOP-1398.png")
        capture(DIST_SERVICES, "services", 390, 844, "SERVICES-FOUNDATION-MOBILE-390.png")
        capture(DIST_HOME, "home", 1398, 1200, "HOME-REGRESSION-DESKTOP.png")
        capture(DIST_HOME, "home", 390, 844, "HOME-REGRESSION-MOBILE-390.png")

        page = browser.new_page(viewport={"width": 1398, "height": 900})
        page.goto(DIST_SERVICES.as_uri(), wait_until="networkidle")
        page.locator('.site-header__nav-link--active').hover()
        page.wait_for_timeout(200)
        page.screenshot(path=str(OUT / "SERVICES-HEADER-ACTIVE-HOVER.png"), full_page=False)
        metrics["files"].append("SERVICES-HEADER-ACTIVE-HOVER.png")

        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(DIST_SERVICES.as_uri(), wait_until="networkidle")
        page.locator("[data-offcanvas-open]").click()
        page.wait_for_selector('[data-offcanvas-state="open"]', timeout=5000)
        page.screenshot(path=str(OUT / "SERVICES-MOBILE-MENU.png"), full_page=False)
        metrics["files"].append("SERVICES-MOBILE-MENU.png")

        page.set_viewport_size({"width": 1398, "height": 900})
        page.goto(DIST_SERVICES.as_uri(), wait_until="networkidle")
        page.locator('.site-footer__nav-link[href="/uslugi/zavisimosti/"]').hover()
        page.wait_for_timeout(200)
        page.screenshot(path=str(OUT / "SERVICES-FOOTER-LINK-STATES.png"), full_page=False)
        metrics["files"].append("SERVICES-FOOTER-LINK-STATES.png")

        page.goto(DIST_SERVICES.as_uri(), wait_until="networkidle")
        page.locator('[data-modal-source="services-founder"]').click()
        page.wait_for_selector('[data-modal-state="open"]', timeout=5000)
        page.screenshot(path=str(OUT / "SERVICES-MODAL-OPEN.png"), full_page=False)
        metrics["files"].append("SERVICES-MODAL-OPEN.png")
        page.close()

        for width in WIDTHS:
            height = 844 if width <= 1024 else 1200
            for page_path, label in ((DIST_HOME, "home"), (DIST_SERVICES, "services")):
                page = browser.new_page(viewport={"width": width, "height": height})
                page.goto(page_path.as_uri(), wait_until="networkidle")
                metrics["overflow"][f"{label}-{width}"] = overflow_metrics(page)
                page.close()

        browser.close()

    (OUT / "SERVICES-FOUNDATION-CAPTURE-METRICS.json").write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(metrics["overflow"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
