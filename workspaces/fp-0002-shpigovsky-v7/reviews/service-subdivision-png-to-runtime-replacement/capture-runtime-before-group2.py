"""Capture GROUP 2 runtime before crops aligned to DOM sections."""
from pathlib import Path
import json

from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174"
review = Path(__file__).parent
out_before = review / "runtime-crops-before" / "group-2"
out_d = out_before / "desktop"
out_m = out_before / "mobile"
out_d.mkdir(parents=True, exist_ok=True)
out_m.mkdir(parents=True, exist_ok=True)

BLOCKS = [
    ("05-CTA-01", "#service-subdivision-start"),
    ("06-PROGRAM-HEADER", "#service-subdivision-program .services-program-v2__head, #service-subdivision-program .services-program-v2__lead, #service-subdivision-program .services-program-v2__intro"),
    ("07-PROGRAM-CARDS", "#service-subdivision-program .services-program-v2__grid"),
    ("08-CTA-02", "#service-subdivision-second-cta, #service-subdivision-program .services-program-v2__cta-band"),
]

meta = {"desktop": {}, "mobile": {}}

with sync_playwright() as p:
    browser = p.chromium.launch()
    for label, width, out_dir in [("desktop", 1437, out_d), ("mobile", 380, out_m)]:
        page = browser.new_page(viewport={"width": width, "height": 900})
        page.goto(f"{base_url}/usluga-podrazdel-v1.html", wait_until="networkidle")
        prefix = "D" if label == "desktop" else "M"
        meta[label]["page_height"] = page.evaluate("document.body.scrollHeight")
        for block_id, selector in BLOCKS:
            loc = page.locator(selector)
            count = loc.count()
            file_name = f"RUNTIME-BEFORE-{prefix}-{block_id}.png"
            if count == 0:
                meta[label][block_id] = {"present": False}
                continue
            if "," in selector:
                page.locator(selector.split(",")[0].strip()).first.screenshot(path=str(out_dir / file_name))
            else:
                loc.first.screenshot(path=str(out_dir / file_name))
            box = loc.first.bounding_box()
            meta[label][block_id] = {"present": True, "selector": selector, "box": box}
        page.close()
    browser.close()

(out_before / "capture-meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
print("done", json.dumps(meta, ensure_ascii=False, indent=2))
