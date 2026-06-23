"""FP-0002 V6 — services hub unique blocks implementation screenshots."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST_HOME = ROOT / "dist" / "index.html"
DIST_SERVICES = ROOT / "dist" / "uslugi.html"
OUT = ROOT / "reviews" / "services-page" / "unique-blocks" / "implementation"
MOCK_DESKTOP = ROOT / "reviews" / "services-page" / "unique-blocks" / "SERVICES-HUB-DESKTOP-FULL-CONTEXT.png"


def ensure_deps() -> None:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
        from PIL import Image  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "pillow", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def overflow_metrics(page) -> dict:
    return page.evaluate(
        """() => {
            const doc = document.documentElement;
            const body = document.body;
            return {
                horizontalOverflow: Math.max(0, doc.scrollWidth - doc.clientWidth, body.scrollWidth - body.clientWidth)
            };
        }"""
    )


def capture_section(page, selector: str, path: Path, width: int) -> None:
    page.set_viewport_size({"width": width, "height": 900})
    page.goto(DIST_SERVICES.as_uri(), wait_until="networkidle")
    locator = page.locator(selector).first
    locator.scroll_into_view_if_needed()
    page.wait_for_timeout(150)
    locator.screenshot(path=str(path))


def side_by_side(mock_path: Path, render_path: Path, out_path: Path) -> None:
    from PIL import Image

    mock = Image.open(mock_path).convert("RGB")
    render = Image.open(render_path).convert("RGB")
    target_h = min(mock.height, render.height, 4000)
    mock_ratio = target_h / mock.height
    render_ratio = target_h / render.height
    mock_resized = mock.resize((int(mock.width * mock_ratio), target_h))
    render_resized = render.resize((int(render.width * render_ratio), target_h))
    canvas = Image.new("RGB", (mock_resized.width + render_resized.width + 20, target_h), (240, 244, 248))
    canvas.paste(mock_resized, (0, 0))
    canvas.paste(render_resized, (mock_resized.width + 20, 0))
    canvas.save(out_path)


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

        def capture_full(page_path: Path, label: str, width: int, name: str) -> None:
            page = browser.new_page(viewport={"width": width, "height": 900})
            page.goto(page_path.as_uri(), wait_until="networkidle")
            page.screenshot(path=str(OUT / name), full_page=True)
            metrics["files"].append(name)
            metrics["overflow"][f"{label}-{width}"] = overflow_metrics(page)
            page.close()

        capture_full(DIST_SERVICES, "services", 1398, "SERVICES-HUB-FULL-DESKTOP-1398.png")
        capture_full(DIST_SERVICES, "services", 390, "SERVICES-HUB-FULL-MOBILE-390.png")
        capture_full(DIST_HOME, "home", 1398, "HOME-REGRESSION-DESKTOP.png")
        capture_full(DIST_HOME, "home", 390, "HOME-REGRESSION-MOBILE-390.png")

        page = browser.new_page()
        for selector, desktop_name, mobile_name in [
            (".services-hero", "SERVICES-HERO-DESKTOP.png", "SERVICES-HERO-MOBILE-390.png"),
            (".services-addictions", "SERVICES-ADDICTIONS-DESKTOP.png", "SERVICES-ADDICTIONS-MOBILE-390.png"),
            (".services-mental-health", "SERVICES-MENTAL-HEALTH-DESKTOP.png", "SERVICES-MENTAL-HEALTH-MOBILE-390.png"),
            (".services-eating-disorders", "SERVICES-EATING-DISORDERS-DESKTOP.png", "SERVICES-EATING-DISORDERS-MOBILE-390.png"),
        ]:
            capture_section(page, selector, OUT / desktop_name, 1398)
            capture_section(page, selector, OUT / mobile_name, 390)
            metrics["files"].extend([desktop_name, mobile_name])

        page.close()
        browser.close()

    if MOCK_DESKTOP.is_file():
        side_by_side(
            MOCK_DESKTOP,
            OUT / "SERVICES-HUB-FULL-DESKTOP-1398.png",
            OUT / "SERVICES-DESKTOP-COMPARISON.png",
        )
        side_by_side(
            ROOT / "reviews/services-page/unique-blocks/SERVICES-HUB-MOBILE-FULL-CONTEXT.png",
            OUT / "SERVICES-HUB-FULL-MOBILE-390.png",
            OUT / "SERVICES-MOBILE-COMPARISON.png",
        )
        metrics["files"].extend(["SERVICES-DESKTOP-COMPARISON.png", "SERVICES-MOBILE-COMPARISON.png"])

    (OUT / "SERVICES-UNIQUE-CAPTURE-METRICS.json").write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(metrics["overflow"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
