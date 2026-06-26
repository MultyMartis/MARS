from pathlib import Path
import json
from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174"
out_dir = Path(__file__).parent / "screenshots"
out_dir.mkdir(parents=True, exist_ok=True)

shots = [
    {"file": "SERVICES-V2-PROGRAM-FULL-1398.png", "width": 1398, "full": True},
    {"file": "SERVICES-V2-PROGRAM-FULL-390.png", "width": 390, "height": 844, "full": True},
    {"file": "SERVICES-V2-PROGRAM-BLOCK-1398.png", "width": 1398, "selector": "#services-program"},
    {"file": "SERVICES-V2-PROGRAM-BLOCK-390.png", "width": 390, "selector": "#services-program"},
    {"file": "SERVICES-V2-PROGRAM-HEADER-1398.png", "width": 1398, "selector": ".services-program-v2__head"},
    {"file": "SERVICES-V2-PROGRAM-HEADER-390.png", "width": 390, "selector": ".services-program-v2__head"},
    {"file": "SERVICES-V2-PROGRAM-ITEMS-1398.png", "width": 1398, "selector": ".services-program-v2__grid"},
    {"file": "SERVICES-V2-PROGRAM-ITEMS-390.png", "width": 390, "selector": ".services-program-v2__grid"},
    {"file": "SERVICES-V2-PROGRAM-CTA-1398.png", "width": 1398, "selector": ".services-program-v2__cta-band"},
    {"file": "SERVICES-V2-PROGRAM-CTA-390.png", "width": 390, "selector": ".services-program-v2__cta-band"},
    {"file": "SERVICES-V2-CATEGORY4-TO-PROGRAM-1398.png", "width": 1398, "selector": "#services-category-genotyping", "pad_bottom": 200},
    {"file": "SERVICES-V2-CATEGORY4-TO-PROGRAM-390.png", "width": 390, "selector": "#services-category-genotyping", "pad_bottom": 120},
    {"file": "HOME-SMOKE-AFTER-SERVICES-PROGRAM-1398.png", "width": 1398, "url": "/index.html", "full": True},
    {"file": "HOME-SMOKE-AFTER-SERVICES-PROGRAM-390.png", "width": 390, "url": "/index.html", "height": 844, "full": True},
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    probe_page = browser.new_page(viewport={"width": 1398, "height": 900})
    probe_page.goto(f"{base_url}/uslugi-v2.html", wait_until="networkidle")
    compiled = probe_page.evaluate(
        """() => {
      const root = document.getElementById('services-program');
      if (!root) return { missing: true };
      const items = [...root.querySelectorAll('.services-program-v2__item')];
      return {
        root: true,
        heading: root.querySelector('.services-program-v2__heading')?.textContent?.trim() || '',
        lead: root.querySelector('.services-program-v2__lead')?.textContent?.trim() || '',
        intro: root.querySelector('.services-program-v2__intro')?.textContent?.trim() || '',
        itemCount: items.length,
        itemTitles: items.map(el => el.querySelector('.services-program-v2__item-title')?.textContent?.trim() || ''),
        loremCount: [...root.querySelectorAll('.services-program-v2__item-text')].filter(el => el.textContent.includes('Lorem ipsum')).length,
        ctaTitle: root.querySelector('.services-program-v2__cta-title')?.textContent?.trim() || '',
        ctaSubtitle: root.querySelector('.services-program-v2__cta-subtitle')?.textContent?.trim() || '',
        ctaPhone: root.querySelector('.services-program-v2__cta-phone')?.textContent?.trim() || '',
        hasModalHook: !!root.querySelector('[data-modal-open]'),
        overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth,
      };
    }"""
    )
    probe_page.close()

    for shot in shots:
        vp = {"width": shot["width"], "height": shot.get("height", 900)}
        page = browser.new_page(viewport=vp)
        page.goto(f"{base_url}{shot.get('url', '/uslugi-v2.html')}", wait_until="networkidle")
        if shot.get("full"):
            page.screenshot(path=str(out_dir / shot["file"]), full_page=True)
        else:
            loc = page.locator(shot["selector"])
            loc.screenshot(path=str(out_dir / shot["file"]))
        page.close()

    browser.close()

(out_dir / "compiled-content-probe.json").write_text(json.dumps(compiled, ensure_ascii=False, indent=2), encoding="utf-8")
print("capture complete", out_dir)
