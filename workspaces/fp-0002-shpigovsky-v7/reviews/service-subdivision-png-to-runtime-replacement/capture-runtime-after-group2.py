"""Capture GROUP 2 runtime after crops aligned to DOM sections."""
from pathlib import Path
import json

from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174"
review = Path(__file__).parent
out_d = review / "runtime-crops-after" / "group-2" / "desktop"
out_m = review / "runtime-crops-after" / "group-2" / "mobile"
out_d.mkdir(parents=True, exist_ok=True)
out_m.mkdir(parents=True, exist_ok=True)

BLOCKS = [
    ("05-CTA-01", "#service-subdivision-start"),
    ("06-PROGRAM-HEADER", "#service-subdivision-program .services-program-v2__head"),
    ("07-PROGRAM-CARDS", "#service-subdivision-program .services-program-v2__grid"),
    ("08-CTA-02", "#service-subdivision-program .services-program-v2__foot-link"),
]

meta = {"desktop": {}, "mobile": {}}

with sync_playwright() as p:
    browser = p.chromium.launch()
    for label, width, out_dir, prefix in [
        ("desktop", 1437, out_d, "D"),
        ("mobile", 380, out_m, "M"),
    ]:
        page = browser.new_page(viewport={"width": width, "height": 900})
        page.goto(f"{base_url}/usluga-podrazdel-v1.html", wait_until="networkidle")
        meta[label]["page_height"] = page.evaluate("document.body.scrollHeight")
        for block_id, selector in BLOCKS:
            loc = page.locator(selector)
            file_name = f"RUNTIME-AFTER-{prefix}-{block_id}.png"
            if loc.count() == 0:
                meta[label][block_id] = {"present": False}
                continue
            target = loc.first
            if block_id == "06-PROGRAM-HEADER":
                page.locator(
                    "#service-subdivision-program .services-program-v2__head, "
                    "#service-subdivision-program .services-program-v2__lead, "
                    "#service-subdivision-program .services-program-v2__intro, "
                    "#service-subdivision-program .services-program-v2__intro--continued"
                ).first.evaluate(
                    """els => {
                        const nodes = Array.from(document.querySelectorAll(
                          '#service-subdivision-program .services-program-v2__head, #service-subdivision-program .services-program-v2__lead, #service-subdivision-program .services-program-v2__intro, #service-subdivision-program .services-program-v2__intro--continued'
                        ));
                        if (!nodes.length) return;
                        const top = Math.min(...nodes.map(n => n.getBoundingClientRect().top));
                        const bottom = Math.max(...nodes.map(n => n.getBoundingClientRect().bottom));
                        window.scrollTo(0, window.scrollY + top - 16);
                    }"""
                )
                box = page.locator("#service-subdivision-program").evaluate(
                    """() => {
                        const nodes = Array.from(document.querySelectorAll(
                          '.service-subdivision-program-v1 .services-program-v2__head, .service-subdivision-program-v1 .services-program-v2__lead, .service-subdivision-program-v1 .services-program-v2__intro, .service-subdivision-program-v1 .services-program-v2__intro--continued'
                        ));
                        const rects = nodes.map(n => n.getBoundingClientRect());
                        const top = Math.min(...rects.map(r => r.top));
                        const bottom = Math.max(...rects.map(r => r.bottom));
                        const left = Math.min(...rects.map(r => r.left));
                        const right = Math.max(...rects.map(r => r.right));
                        return {x:left, y:top, width:right-left, height:bottom-top};
                    }"""
                )
                page.screenshot(path=str(out_dir / file_name), clip=box)
            elif block_id == "08-CTA-02" and label == "desktop":
                meta[label][block_id] = {"present": False, "note": "design has no desktop dark CTA-02 after program"}
                continue
            else:
                target.screenshot(path=str(out_dir / file_name))
            meta[label][block_id] = {"present": True, "selector": selector}
        page.close()
    browser.close()

(out_d.parent / "capture-meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
print("done")
