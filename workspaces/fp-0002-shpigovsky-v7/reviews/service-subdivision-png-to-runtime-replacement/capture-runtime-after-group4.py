"""Capture GROUP 4 runtime after crops aligned to DOM sections."""
from pathlib import Path
import json

from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174"
review = Path(__file__).parent
out_after = review / "runtime-crops-after" / "group-4"
out_d = out_after / "desktop"
out_m = out_after / "mobile"
out_d.mkdir(parents=True, exist_ok=True)
out_m.mkdir(parents=True, exist_ok=True)

BLOCKS = [
    ("G4-01-TRANSITION", "#service-subdivision-stages .service-subdivision-stages-v1__support, #service-subdivision-approach"),
    ("G4-02-CORRIDOR", ".service-subdivision-team-stats-v1__corridor-bleed"),
    ("G4-03-APPROACH-HEAD", ".service-subdivision-team-stats-v1__head, .service-subdivision-team-stats-v1__highlight"),
    ("G4-04-TEAM", ".service-subdivision-team-stats-v1__staff-bleed"),
    ("G4-05-CARDS", ".service-subdivision-team-stats-v1__approach-cards"),
    ("G4-06-END", ".service-subdivision-team-stats-v1__approach-cards, .service-subdivision-approach-v1--gallery-only"),
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
            if block_id == "G4-01-TRANSITION":
                support = page.locator("#service-subdivision-stages .service-subdivision-stages-v1__support")
                section = page.locator("#service-subdivision-approach")
                if support.count() and section.count():
                    support.first.scroll_into_view_if_needed()
                    section.first.scroll_into_view_if_needed()
                    sb = support.first.bounding_box()
                    tb = section.first.bounding_box()
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
            if block_id == "G4-06-END":
                cards = page.locator(".service-subdivision-team-stats-v1__approach-cards")
                gallery = page.locator(".service-subdivision-approach-v1--gallery-only")
                if cards.count() and gallery.count():
                    cards.first.scroll_into_view_if_needed()
                    gallery.first.scroll_into_view_if_needed()
                    cb = cards.first.bounding_box()
                    gb = gallery.first.bounding_box()
                    gap_h = max(120, gb["y"] - (cb["y"] + cb["height"]) + 80)
                    clip = {
                        "x": 0,
                        "y": max(0, cb["y"] + cb["height"] - 20),
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
            if block_id == "G4-03-APPROACH-HEAD" and "," in selector:
                head = page.locator(".service-subdivision-team-stats-v1__head")
                highlight = page.locator(".service-subdivision-team-stats-v1__highlight")
                intro = page.locator(".service-subdivision-team-stats-v1__intro")
                if head.count():
                    head.first.scroll_into_view_if_needed()
                    hb = head.first.bounding_box()
                    ib = intro.first.bounding_box() if intro.count() else hb
                    clip = {
                        "x": 0,
                        "y": max(0, hb["y"] - 10),
                        "width": width,
                        "height": min((ib["y"] + ib["height"]) - hb["y"] + 20, 700),
                    }
                    page.screenshot(path=str(out_dir / file_name), clip=clip)
                    meta[label][block_id] = {"present": True, "clip": clip}
                else:
                    meta[label][block_id] = {"present": False}
                continue
            loc = page.locator(selector.split(",")[0].strip())
            if loc.count() == 0:
                meta[label][block_id] = {"present": False, "selector": selector}
                continue
            loc.first.scroll_into_view_if_needed()
            loc.first.screenshot(path=str(out_dir / file_name))
            meta[label][block_id] = {"present": True, "selector": selector, "box": loc.first.bounding_box()}
        page.close()
    browser.close()

(out_after / "capture-meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
print("done")
