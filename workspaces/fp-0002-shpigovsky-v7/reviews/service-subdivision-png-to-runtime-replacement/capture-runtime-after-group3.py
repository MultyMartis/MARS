"""Capture GROUP 3 runtime after crops aligned to DOM sections."""
from pathlib import Path
import json

from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174"
review = Path(__file__).parent
out_after = review / "runtime-crops-after" / "group-3"
out_d = out_after / "desktop"
out_m = out_after / "mobile"
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
            file_name = f"RUNTIME-AFTER-{prefix}-{block_id}.png"
            if block_id == "G3-05-TRANSITION":
                stages = page.locator("#service-subdivision-stages")
                team = page.locator("#service-subdivision-team-stats")
                if stages.count() and team.count():
                    sb = stages.first.bounding_box()
                    tb = team.first.bounding_box()
                    gap = tb["y"] - (sb["y"] + sb["height"])
                    if gap > 40:
                        clip = {
                            "x": 0,
                            "y": sb["y"] + sb["height"] - 20,
                            "width": width,
                            "height": min(gap + 40, 300),
                        }
                        page.screenshot(path=str(out_dir / file_name), clip=clip)
                        meta[label][block_id] = {"present": True, "clip": clip}
                    else:
                        team.first.screenshot(path=str(out_dir / file_name))
                        meta[label][block_id] = {"present": True, "fallback": "team-top"}
                else:
                    meta[label][block_id] = {"present": False}
                continue
            loc = page.locator(selector.split(",")[0].strip() if "," in selector else selector)
            if loc.count() == 0:
                meta[label][block_id] = {"present": False, "selector": selector}
                continue
            loc.first.screenshot(path=str(out_dir / file_name))
            meta[label][block_id] = {"present": True, "selector": selector, "box": loc.first.bounding_box()}
        page.close()
    browser.close()

(out_after / "capture-meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
print("done", json.dumps(meta, ensure_ascii=False, indent=2))
