from pathlib import Path
import json
from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174"
out_dir = Path(__file__).parent / "screenshots"
out_dir.mkdir(parents=True, exist_ok=True)

shots = [
    {"file": "SERVICE-SUBDIVISION-PASS-1-FULL-1398.png", "width": 1398, "url": "/usluga-podrazdel-v1.html", "full": True},
    {"file": "SERVICE-SUBDIVISION-PASS-1-FULL-390.png", "width": 390, "url": "/usluga-podrazdel-v1.html", "height": 844, "full": True},
    {"file": "SERVICE-SUBDIVISION-HERO-1398.png", "width": 1398, "url": "/usluga-podrazdel-v1.html", "selector": ".services-inner-hero-v2"},
    {"file": "SERVICE-SUBDIVISION-HERO-390.png", "width": 390, "url": "/usluga-podrazdel-v1.html", "selector": ".services-inner-hero-v2"},
    {"file": "SERVICE-SUBDIVISION-BREADCRUMBS-SUBNAV-1398.png", "width": 1398, "url": "/usluga-podrazdel-v1.html", "selector": ".page-service-subdivision-v1__upper-nav"},
    {"file": "SERVICE-SUBDIVISION-BREADCRUMBS-SUBNAV-390.png", "width": 390, "url": "/usluga-podrazdel-v1.html", "selector": ".page-service-subdivision-v1__upper-nav"},
    {"file": "SERVICE-SUBDIVISION-INTRO-1398.png", "width": 1398, "url": "/usluga-podrazdel-v1.html", "selector": ".service-subdivision-intro-v1"},
    {"file": "SERVICE-SUBDIVISION-INTRO-390.png", "width": 390, "url": "/usluga-podrazdel-v1.html", "selector": ".service-subdivision-intro-v1"},
    {"file": "SERVICE-SUBDIVISION-PRIMARY-SERVICE-1398.png", "width": 1398, "url": "/usluga-podrazdel-v1.html", "selector": "#service-subdivision-primary"},
    {"file": "SERVICE-SUBDIVISION-PRIMARY-SERVICE-390.png", "width": 390, "url": "/usluga-podrazdel-v1.html", "selector": "#service-subdivision-primary"},
    {"file": "SERVICES-V2-REFERENCE-SMOKE-1398.png", "width": 1398, "url": "/uslugi-v2.html", "full": True},
    {"file": "SERVICES-V2-REFERENCE-SMOKE-390.png", "width": 390, "url": "/uslugi-v2.html", "height": 844, "full": True},
    {"file": "HOME-SMOKE-AFTER-SUBDIVISION-PASS-1-1398.png", "width": 1398, "url": "/index.html", "full": True},
    {"file": "HOME-SMOKE-AFTER-SUBDIVISION-PASS-1-390.png", "width": 390, "url": "/index.html", "height": 844, "full": True},
]

widths = [320, 380, 390, 430, 768, 1024, 1025, 1280, 1398, 1440, 1920]

with sync_playwright() as p:
    browser = p.chromium.launch()
    responsive = {}
    for w in widths:
        page = browser.new_page(viewport={"width": w, "height": 900})
        page.goto(f"{base_url}/usluga-podrazdel-v1.html", wait_until="networkidle")
        responsive[str(w)] = page.evaluate(
            "() => document.documentElement.scrollWidth > document.documentElement.clientWidth"
        )
        page.close()

    for shot in shots:
        page = browser.new_page(viewport={"width": shot["width"], "height": shot.get("height", 900)})
        page.goto(f"{base_url}{shot['url']}", wait_until="networkidle")
        target = out_dir / shot["file"]
        if shot.get("full"):
            page.screenshot(path=str(target), full_page=True)
        else:
            page.locator(shot["selector"]).first.screenshot(path=str(target))
        page.close()
    browser.close()

(out_dir / "responsive-probe.json").write_text(
    json.dumps({"horizontalOverflow": responsive}, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
print("capture complete", out_dir)
