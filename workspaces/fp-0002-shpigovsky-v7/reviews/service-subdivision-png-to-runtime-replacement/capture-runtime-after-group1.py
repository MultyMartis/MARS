"""Capture GROUP 1 runtime-after crops."""
from pathlib import Path
import json

from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174"
review = Path(__file__).parent
out_d = review / "runtime-crops-after" / "group-1" / "desktop"
out_m = review / "runtime-crops-after" / "group-1" / "mobile"
out_d.mkdir(parents=True, exist_ok=True)
out_m.mkdir(parents=True, exist_ok=True)

BLOCKS = [
    ("01-HEADER-HERO", "header, .services-inner-hero-v2"),
    ("02-UPPER-NAV", ".page-service-subdivision-v1__upper-nav"),
    ("03-DEPENDENCIES", "#service-subdivision-dependencies"),
    ("04-NATURE", "#service-subdivision-nature"),
]

meta = {"desktop": {}, "mobile": {}}

with sync_playwright() as p:
    browser = p.chromium.launch()
    for label, width, out_dir in [
        ("desktop", 1437, out_d),
        ("mobile", 380, out_m),
    ]:
        page = browser.new_page(viewport={"width": width, "height": 900})
        page.goto(f"{base_url}/usluga-podrazdel-v1.html", wait_until="networkidle")
        prefix = "RUNTIME-AFTER-D" if label == "desktop" else "RUNTIME-AFTER-M"
        for block_id, selector in BLOCKS:
            loc = page.locator(selector)
            file_name = f"{prefix}-{block_id}.png"
            if loc.count() == 0:
                meta[label][block_id] = {"present": False}
                continue
            loc.first.screenshot(path=str(out_dir / file_name))
            meta[label][block_id] = {
                "present": True,
                "selector": selector,
                "box": loc.first.bounding_box(),
            }
        page.close()
    browser.close()

(out_d.parent / "capture-meta.json").write_text(
    json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
)
print("done", json.dumps(meta, ensure_ascii=False, indent=2))
