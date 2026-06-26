"""Capture GROUP 3 runtime before crops aligned to DOM sections."""
from pathlib import Path
import json

from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174"
review = Path(__file__).parent
out_before = review / "runtime-crops-before" / "group-3"
out_d = out_before / "desktop"
out_m = out_before / "mobile"
out_d.mkdir(parents=True, exist_ok=True)
out_m.mkdir(parents=True, exist_ok=True)

BLOCKS = [
    ("G3-01-REHABILITATION-HEADER", "#service-subdivision-stages-heading, #service-subdivision-stages .service-subdivision-stages-v1__lead"),
    ("G3-02-REHABILITATION-STAGES", "#service-subdivision-stages .service-subdivision-stages-v1__steps"),
    ("G3-03-CTA", "#service-subdivision-stages .service-subdivision-stages-v1__cta"),
    ("G3-04-SUPPORT-BLOCK", "#service-subdivision-stages .service-subdivision-stages-v1__support"),
    ("G3-05-TRANSITION", "#service-subdivision-stages, #service-subdivision-team-stats"),
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
                meta[label][block_id] = {"present": False, "selector": selector}
                continue
            target = loc.first if block_id != "G3-05-TRANSITION" else page.locator("#service-subdivision-stages")
            if block_id == "G3-05-TRANSITION":
                stages = page.locator("#service-subdivision-stages")
                team = page.locator("#service-subdivision-team-stats")
                if stages.count() and team.count():
                    sb = stages.first.bounding_box()
                    tb = team.first.bounding_box()
                    clip = {
                        "x": 0,
                        "y": max(0, sb["y"] + sb["height"] - 80),
                        "width": width,
                        "height": min(tb["y"] - sb["y"] - sb["height"] + 160, 400),
                    }
                    page.screenshot(path=str(out_dir / file_name), clip=clip)
                    meta[label][block_id] = {"present": True, "clip": clip}
                else:
                    meta[label][block_id] = {"present": False}
                continue
            if "," in selector:
                target = page.locator(selector.split(",")[0].strip()).first
            target.screenshot(path=str(out_dir / file_name))
            box = target.bounding_box()
            meta[label][block_id] = {"present": True, "selector": selector, "box": box}
        page.close()
    browser.close()

(out_before / "capture-meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
print("done", json.dumps(meta, ensure_ascii=False, indent=2))
