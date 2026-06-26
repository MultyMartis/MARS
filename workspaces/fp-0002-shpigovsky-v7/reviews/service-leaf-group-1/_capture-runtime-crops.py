"""Capture SERVICE LEAF GROUP 1 runtime crops."""
from pathlib import Path
import json

from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174/usluga-konechnaya-v1.html"
review = Path(__file__).parent

BLOCKS = [
    ("G1-01-HEADER-HERO", "header, .services-inner-hero-v2"),
    ("G1-02-NAV", ".page-service-leaf-v1__upper-nav"),
    ("G1-03-INTRO", ".service-leaf-intro-v1"),
    ("G1-04-BORDERED-INFO", ".service-leaf-bordered-info-v1"),
    ("G1-05-CTA", ".service-leaf-cta-01-v1"),
]

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
            page = browser.new_page(viewport={"width": width, "height": 1200})
            page.goto(base_url, wait_until="networkidle")
            prefix = f"SERVICE-LEAF-RUNTIME-{phase.upper()}-{'D' if label == 'desktop' else 'M'}"
            for block_id, selector in BLOCKS:
                loc = page.locator(selector)
                file_name = f"{prefix}-{block_id}.png"
                if loc.count() == 0:
                    meta[label][block_id] = {"present": False, "selector": selector}
                    continue
                loc.first.screenshot(path=str(out_dir / file_name))
                meta[label][block_id] = {
                    "present": True,
                    "selector": selector,
                    "box": loc.first.bounding_box(),
                }
            full_name = f"{prefix}-G1-FULL.png"
            page.screenshot(path=str(out_dir / full_name), full_page=True)
            meta[label]["FULL"] = {"file": full_name}
            page.close()
        browser.close()

    (review / f"runtime-crops-{phase}" / "capture-meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(phase, "done")

if __name__ == "__main__":
    capture("before")
    capture("after")
