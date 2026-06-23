from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist" / "index.html"
IMPL = ROOT / "reviews" / "main-content" / "lower-home-implementation"
AUDIT = ROOT / "reviews" / "main-content" / "lower-home-audit"
URL = DIST.resolve().as_uri()

SECTIONS = [
    ("rehabilitation-requirements", ".home-rehabilitation-requirements"),
    ("rehabilitation-program", ".home-rehabilitation-program"),
    ("genotyping", ".home-genotyping"),
    ("comfort", ".home-comfort"),
    ("videos", ".home-videos"),
    ("specialists", ".home-specialists"),
    ("articles", ".home-articles"),
    ("faq", ".home-faq"),
    ("final-form", ".home-final-form"),
]


def shot(page, path, width, height=1400):
    page.set_viewport_size({"width": width, "height": height})
    page.goto(URL)
    page.wait_for_timeout(700)
    page.screenshot(path=str(path), full_page=width >= 1024)


def main():
    IMPL.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        shot(page, IMPL / "FP-0002-V6-REVIEWS-TO-FOOTER-DESKTOP.png", 1398, 16343)
        shot(page, IMPL / "FP-0002-V6-FULL-HOME-DESKTOP.png", 1398, 16343)

        page.set_viewport_size({"width": 390, "height": 2000})
        page.goto(URL)
        page.wait_for_timeout(700)
        page.locator(".home-reviews").scroll_into_view_if_needed()
        page.screenshot(path=str(IMPL / "FP-0002-V6-REVIEWS-TO-FOOTER-MOBILE-390.png"), full_page=True)

        for name, selector in SECTIONS:
            folder = AUDIT / name
            folder.mkdir(parents=True, exist_ok=True)
            page.set_viewport_size({"width": 1398, "height": 2000})
            page.goto(URL)
            page.wait_for_timeout(500)
            loc = page.locator(selector)
            loc.scroll_into_view_if_needed()
            page.wait_for_timeout(300)
            loc.screenshot(path=str(folder / "IMPLEMENTATION-DESKTOP.png"))

            page.set_viewport_size({"width": 390, "height": 1200})
            page.goto(URL)
            page.wait_for_timeout(500)
            loc = page.locator(selector)
            loc.scroll_into_view_if_needed()
            page.wait_for_timeout(300)
            loc.screenshot(path=str(folder / "IMPLEMENTATION-MOBILE-390.png"))

        browser.close()


if __name__ == "__main__":
    main()
