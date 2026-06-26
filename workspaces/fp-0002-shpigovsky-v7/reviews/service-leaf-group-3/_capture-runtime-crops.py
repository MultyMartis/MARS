"""Capture SERVICE LEAF GROUP 3 runtime crops."""
from pathlib import Path
import json
import sys

from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174/usluga-konechnaya-v1.html"
review = Path(__file__).parent


def capture(phase: str):
    out_d = review / f"runtime-crops-{phase}" / "desktop"
    out_m = review / f"runtime-crops-{phase}" / "mobile"
    out_d.mkdir(parents=True, exist_ok=True)
    out_m.mkdir(parents=True, exist_ok=True)
    meta = {"desktop": {}, "mobile": {}, "url": base_url, "phase": phase}
    prefix_tag = "BEFORE" if phase == "before" else "AFTER"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for label, width, out_dir in [
            ("desktop", 1437, out_d),
            ("mobile", 380, out_m),
        ]:
            page = browser.new_page(viewport={"width": width, "height": 1400})
            page.goto(base_url, wait_until="networkidle")
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(400)
            prefix = f"SERVICE-LEAF-RUNTIME-{prefix_tag}-{'D' if label == 'desktop' else 'M'}-G3"

            def shot(file_suffix, selector):
                loc = page.locator(selector)
                file_name = f"{prefix}-{file_suffix}.png"
                if loc.count() == 0:
                    meta[label][file_suffix] = {"present": False, "selector": selector}
                    return
                loc.first.scroll_into_view_if_needed()
                page.wait_for_timeout(150)
                loc.first.screenshot(path=str(out_dir / file_name))
                meta[label][file_suffix] = {
                    "present": True,
                    "selector": selector,
                    "box": loc.first.bounding_box(),
                }

            if phase == "before":
                shot("START", ".service-leaf-signs-v1")
                shot("END", "footer")
            else:
                shot("01-BOUNDARY-START", ".service-leaf-signs-v1")
                shot("02-APPROACH-HEADING-INTRO", ".service-leaf-approach-v1__head")
                shot("03-TEAM-PHOTO", ".service-leaf-approach-v1__staff-image")
                shot("04-APPROACH-CARDS", ".service-leaf-approach-v1__approach-cards")
                shot("05-CLINIC-LANDSCAPE", ".service-leaf-landscape-v1 .home-clinic-landscape__image")
                shot("06-BOUNDARY-END", ".service-leaf-landscape-v1")
                approach = page.locator(".service-leaf-approach-v1")
                landscape = page.locator(".service-leaf-landscape-v1")
                if approach.count() and landscape.count():
                    approach.first.scroll_into_view_if_needed()
                    b1 = approach.first.bounding_box()
                    landscape.first.scroll_into_view_if_needed()
                    b2 = landscape.first.bounding_box()
                    if b1 and b2:
                        page.screenshot(
                            path=str(out_dir / f"{prefix}-FULL.png"),
                            clip={
                                "x": 0,
                                "y": max(0, b1["y"] - 20),
                                "width": width,
                                "height": min(1400, b2["y"] + b2["height"] - b1["y"] + 40),
                            },
                        )

            page.close()
        browser.close()

    (review / f"runtime-crops-{phase}" / "capture-meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(phase, "done")


if __name__ == "__main__":
    capture(sys.argv[1] if len(sys.argv) > 1 else "after")
