"""Capture runtime crops aligned to DOM sections."""
from pathlib import Path
import json

from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174"
review = Path(__file__).parent
out_before = review / "runtime-crops-before"
out_before.mkdir(parents=True, exist_ok=True)

BLOCKS = [
    ("01-HEADER-HERO", "header, .services-inner-hero-v2"),
    ("02-UPPER-CONTENT", ".page-service-subdivision-v1__upper-nav"),
    ("03-INTRO", "#service-subdivision-intro"),
    ("04-PROCEDURE", "#service-subdivision-procedure"),
    ("05-DEPENDENCIES", "#service-subdivision-dependencies"),
    ("06-NATURE", "#service-subdivision-nature"),
    ("07-CTA-01", "#service-subdivision-first-cta"),
    ("08-PROGRAM", "#service-subdivision-program"),
    ("09-TEAM-STATS", "#service-subdivision-team-stats"),
    ("10-STAGES", "#service-subdivision-stages"),
    ("11-CTA-02", "#service-subdivision-second-cta"),
    ("12-APPROACH", "#service-subdivision-approach"),
    ("13-SPECIALISTS", "#service-subdivision-specialists"),
    ("14-FOUNDER", ".home-founder-quote"),
    ("15-COMFORT", "#service-subdivision-comfort"),
    ("16-REVIEWS", ".home-reviews"),
    ("17-FAQ", "#service-subdivision-faq"),
    ("18-FINAL-FORM", ".home-final-form"),
    ("19-FOOTER", "footer"),
]

meta = {"desktop": {}, "mobile": {}}

with sync_playwright() as p:
    browser = p.chromium.launch()
    for label, width in [("desktop", 1437), ("mobile", 380)]:
        page = browser.new_page(viewport={"width": width, "height": 900})
        page.goto(f"{base_url}/usluga-podrazdel-v1.html", wait_until="networkidle")
        full_path = out_before / f"RUNTIME-{label.upper()}-FULL.png"
        page.screenshot(path=str(full_path), full_page=True)
        meta[label]["full"] = str(full_path.name)
        meta[label]["page_height"] = page.evaluate("document.body.scrollHeight")
        for block_id, selector in BLOCKS:
            loc = page.locator(selector)
            count = loc.count()
            file_name = f"RUNTIME-{label[0].upper()}-{block_id}.png"
            if count == 0:
                meta[label][block_id] = {"present": False}
                continue
            loc.first.screenshot(path=str(out_before / file_name))
            box = loc.first.bounding_box()
            meta[label][block_id] = {"present": True, "selector": selector, "box": box}
        page.close()
    browser.close()

(out_before / "capture-meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
print("done", json.dumps(meta, ensure_ascii=False, indent=2))
