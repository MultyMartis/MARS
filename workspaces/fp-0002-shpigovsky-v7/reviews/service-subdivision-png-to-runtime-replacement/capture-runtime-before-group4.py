"""Capture GROUP 4 runtime before crops aligned to DOM sections."""
from pathlib import Path
import json

from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174"
review = Path(__file__).parent
out_before = review / "runtime-crops-before" / "group-4"
out_d = out_before / "desktop"
out_m = out_before / "mobile"
out_d.mkdir(parents=True, exist_ok=True)
out_m.mkdir(parents=True, exist_ok=True)

BLOCKS = [
    ("G4-01-TRANSITION", "#service-subdivision-stages .service-subdivision-stages-v1__support, #service-subdivision-team-stats"),
    ("G4-02-CORRIDOR", ".service-subdivision-team-stats-v1__photo-bleed"),
    ("G4-03-STATS", ".service-subdivision-team-stats-v1__stats"),
    ("G4-04-TEAM", ".service-subdivision-team-stats-v1__staff-bleed"),
    ("G4-05-END", "#service-subdivision-team-stats, #service-subdivision-approach"),
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
            file_name = f"RUNTIME-BEFORE-{prefix}-{block_id}.png"
            if block_id == "G4-01-TRANSITION":
                support = page.locator("#service-subdivision-stages .service-subdivision-stages-v1__support")
                team = page.locator("#service-subdivision-team-stats")
                if support.count() and team.count():
                    support.first.scroll_into_view_if_needed()
                    team.first.scroll_into_view_if_needed()
                    sb = support.first.bounding_box()
                    tb = team.first.bounding_box()
                    gap_h = max(120, tb["y"] - (sb["y"] + sb["height"]) + 80)
                    clip = {
                        "x": 0,
                        "y": max(0, sb["y"] + sb["height"] - 20),
                        "width": width,
                        "height": min(gap_h, 700),
                    }
                    if clip["height"] > 0:
                        page.screenshot(path=str(out_dir / file_name), clip=clip)
                        meta[label][block_id] = {"present": True, "clip": clip}
                    else:
                        meta[label][block_id] = {"present": False, "reason": "empty_clip"}
                else:
                    meta[label][block_id] = {"present": False}
                continue
            if block_id == "G4-05-END":
                team = page.locator("#service-subdivision-team-stats")
                approach = page.locator("#service-subdivision-approach")
                if team.count() and approach.count():
                    team.first.scroll_into_view_if_needed()
                    approach.first.scroll_into_view_if_needed()
                    tb = team.first.bounding_box()
                    ab = approach.first.bounding_box()
                    gap_h = max(120, ab["y"] - (tb["y"] + tb["height"]) + 80)
                    clip = {
                        "x": 0,
                        "y": max(0, tb["y"] + tb["height"] - 20),
                        "width": width,
                        "height": min(gap_h, 700),
                    }
                    if clip["height"] > 0:
                        page.screenshot(path=str(out_dir / file_name), clip=clip)
                        meta[label][block_id] = {"present": True, "clip": clip}
                    else:
                        meta[label][block_id] = {"present": False, "reason": "empty_clip"}
                else:
                    meta[label][block_id] = {"present": False}
                continue
            loc = page.locator(selector)
            if loc.count() == 0:
                meta[label][block_id] = {"present": False, "selector": selector}
                continue
            loc.first.scroll_into_view_if_needed()
            loc.first.screenshot(path=str(out_dir / file_name))
            meta[label][block_id] = {"present": True, "selector": selector, "box": loc.first.bounding_box()}
        page.close()
    browser.close()

(out_before / "capture-meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
print("done")
