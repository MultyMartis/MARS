"""Capture full-page and group crops for SERVICE LEAF remaining pass."""
from pathlib import Path
import json
import sys

from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174/usluga-konechnaya-v1.html"
review = Path(__file__).parent
shots_dir = review / "screenshots"
shots_dir.mkdir(parents=True, exist_ok=True)


def capture():
    meta = {"url": base_url, "shots": {}}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for label, width, height, prefix in [
            ("desktop", 1437, 12000, "SERVICE-LEAF"),
            ("mobile", 380, 14000, "SERVICE-LEAF"),
        ]:
            page = browser.new_page(viewport={"width": width, "height": height})
            page.goto(base_url, wait_until="networkidle")
            page.wait_for_timeout(500)

            if label == "desktop":
                full_name = "SERVICE-LEAF-FULL-DESKTOP-1437.png"
            else:
                full_name = "SERVICE-LEAF-FULL-MOBILE-380.png"

            page.screenshot(path=str(shots_dir / full_name), full_page=True)
            meta["shots"][full_name] = {"width": width, "full_page": True}

            crops = [
                ("G3", "#service-leaf-approach"),
                ("G4", "#service-leaf-program"),
                ("G5", "#service-leaf-start"),
                ("G6", "#service-leaf-specialists"),
            ]
            for g, sel in crops:
                loc = page.locator(sel)
                file_name = f"SERVICE-LEAF-{g}-AFTER-{'DESKTOP' if label == 'desktop' else 'MOBILE'}.png"
                if loc.count():
                    loc.first.scroll_into_view_if_needed()
                    page.wait_for_timeout(200)
                    loc.first.screenshot(path=str(shots_dir / file_name))
                    meta["shots"][file_name] = {"selector": sel, "present": True}
                else:
                    meta["shots"][file_name] = {"selector": sel, "present": False}

            page.close()
        browser.close()

    (shots_dir / "capture-meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("screenshots done", len(meta["shots"]))


if __name__ == "__main__":
    capture()
