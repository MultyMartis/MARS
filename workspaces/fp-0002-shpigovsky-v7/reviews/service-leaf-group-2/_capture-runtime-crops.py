"""Capture SERVICE LEAF GROUP 2 runtime crops."""
from pathlib import Path
import json

from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174/usluga-konechnaya-v1.html"
review = Path(__file__).parent


def capture(phase: str):
    out_d = review / f"runtime-crops-{phase}" / "desktop"
    out_m = review / f"runtime-crops-{phase}" / "mobile"
    out_d.mkdir(parents=True, exist_ok=True)
    out_m.mkdir(parents=True, exist_ok=True)
    meta = {"desktop": {}, "mobile": {}, "url": base_url, "phase": phase}

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for label, width, out_dir in [
            ("desktop", 1437, out_d),
            ("mobile", 380, out_m),
        ]:
            page = browser.new_page(viewport={"width": width, "height": 1400})
            page.goto(base_url, wait_until="networkidle")
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(300)
            prefix = f"SERVICE-LEAF-RUNTIME-{phase.upper()}-{'D' if label == 'desktop' else 'M'}"

            def shot(block_id, selector):
                loc = page.locator(selector)
                file_name = f"{prefix}-{block_id}.png"
                if loc.count() == 0:
                    meta[label][block_id] = {"present": False, "selector": selector}
                    return
                loc.first.scroll_into_view_if_needed()
                loc.first.screenshot(path=str(out_dir / file_name))
                meta[label][block_id] = {
                    "present": True,
                    "selector": selector,
                    "box": loc.first.bounding_box(),
                }

            shot("G2-01-BOUNDARY-START", ".service-leaf-cta-01-v1")
            shot("G2-02-HEADING-INTRO", ".service-leaf-signs-v1__container")
            shot("G2-03-UPPER", ".service-leaf-signs-v1__list-item:nth-child(1)")
            shot("G2-04-MIDDLE", ".service-leaf-signs-v1__list-item:nth-child(4)")
            shot("G2-05-LOWER", ".service-leaf-signs-v1__list-item:nth-child(7)")
            shot("G2-06-LINKS-ACCENTS", ".service-leaf-signs-v1__editorial")
            shot("G2-07-BOUNDARY-END", ".service-leaf-signs-v1")

            g2 = page.locator(".service-leaf-signs-v1")
            if g2.count():
                g2.first.scroll_into_view_if_needed()
                g2.first.screenshot(path=str(out_dir / f"{prefix}-G2-FULL.png"))

            cta = page.locator(".service-leaf-cta-01-v1")
            if cta.count() and g2.count():
                cta.first.scroll_into_view_if_needed()
                b1 = cta.first.bounding_box()
                b2 = g2.first.bounding_box()
                if b1 and b2:
                    page.screenshot(
                        path=str(out_dir / f"{prefix}-G1-G2-FULL.png"),
                        clip={
                            "x": 0,
                            "y": max(0, b1["y"] - 20),
                            "width": width,
                            "height": min(1400, b2["y"] + b2["height"] - b1["y"] + 40),
                        },
                    )

            if phase == "before":
                shot("G2-START", ".service-leaf-cta-01-v1")
                shot("G2-BOUNDARY", "main")

            page.close()
        browser.close()

    (review / f"runtime-crops-{phase}" / "capture-meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(phase, "done")


if __name__ == "__main__":
    import sys
    capture(sys.argv[1] if len(sys.argv) > 1 else "after")
