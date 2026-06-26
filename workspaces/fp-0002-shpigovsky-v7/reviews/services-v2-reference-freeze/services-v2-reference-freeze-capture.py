from pathlib import Path
import json
from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174"
out_dir = Path(__file__).parent / "screenshots"
out_dir.mkdir(parents=True, exist_ok=True)

shots = [
    {"file": "SERVICES-V2-REFERENCE-FULL-1398.png", "width": 1398, "full": True},
    {"file": "SERVICES-V2-REFERENCE-FULL-390.png", "width": 390, "height": 844, "full": True},
    {"file": "SERVICES-V2-NO-LIFEBUOY-1398.png", "width": 1398, "selector": "#services-category-addictions"},
    {"file": "SERVICES-V2-NO-LIFEBUOY-390.png", "width": 390, "selector": "#services-category-addictions"},
    {"file": "SERVICES-V2-DETAIL-LINKS-1398.png", "width": 1398, "selector": "#services-category-addictions .services-category-section-v2__services"},
    {"file": "SERVICES-V2-DETAIL-LINKS-390.png", "width": 390, "selector": "#services-category-addictions .services-category-section-v2__services"},
    {"file": "HOME-REHABILITATION-LINK-REFERENCE.png", "width": 1398, "url": "/index.html", "selector": ".home-rehabilitation-program__all-link"},
    {"file": "HOME-SMOKE-AFTER-SERVICES-REFERENCE-FREEZE-1398.png", "width": 1398, "url": "/index.html", "full": True},
    {"file": "HOME-SMOKE-AFTER-SERVICES-REFERENCE-FREEZE-390.png", "width": 390, "url": "/index.html", "height": 844, "full": True},
]

widths = [320, 390, 768, 1024, 1398]

with sync_playwright() as p:
    browser = p.chromium.launch()
    probe = browser.new_page(viewport={"width": 1398, "height": 900})
    probe.goto(f"{base_url}/uslugi-v2.html", wait_until="networkidle")
    compiled = probe.evaluate(
        """() => ({
      lifebuoyDecor: document.querySelectorAll('.services-category-section-v2__decor').length,
      lifebuoyImages: document.querySelectorAll('img[src*="services-hub-decor"]').length,
      detailLinks: document.querySelectorAll('.services-category-section-v2__service-link').length,
      homePatternLinks: document.querySelectorAll('.services-category-section-v2__service-link.home-rehabilitation-program__all-link').length,
      faPlayIcons: document.querySelectorAll('.services-category-section-v2__service-link .fa-play').length,
      externalLinkIcons: document.querySelectorAll('.services-category-section-v2__service-link-icon-image').length,
    })"""
    )
    responsive = {}
    for w in widths:
        rp = browser.new_page(viewport={"width": w, "height": 900})
        rp.goto(f"{base_url}/uslugi-v2.html", wait_until="networkidle")
        responsive[str(w)] = rp.evaluate(
            "() => document.documentElement.scrollWidth > document.documentElement.clientWidth"
        )
        rp.close()
    compiled["horizontalOverflow"] = responsive
    probe.close()

    for shot in shots:
        sp = browser.new_page(viewport={"width": shot["width"], "height": shot.get("height", 900)})
        sp.goto(f"{base_url}{shot.get('url', '/uslugi-v2.html')}", wait_until="networkidle")
        if shot.get("full"):
            sp.screenshot(path=str(out_dir / shot["file"]), full_page=True)
        else:
            sp.locator(shot["selector"]).first.screenshot(path=str(out_dir / shot["file"]))
        sp.close()

    browser.close()

(out_dir / "reference-freeze-probe.json").write_text(
    json.dumps(compiled, ensure_ascii=False, indent=2), encoding="utf-8"
)
print("capture complete", out_dir)
