from pathlib import Path
import json
from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174"
out_dir = Path(__file__).parent / "screenshots"
out_dir.mkdir(parents=True, exist_ok=True)

shots = [
    {"file": "SERVICES-V2-CORRECTIONS-FULL-1398.png", "width": 1398, "full": True},
    {"file": "SERVICES-V2-CORRECTIONS-FULL-390.png", "width": 390, "height": 844, "full": True},
    {"file": "SERVICES-V2-HERO-CORRECTED-1398.png", "width": 1398, "selector": ".services-inner-hero-v2"},
    {"file": "SERVICES-V2-HERO-CORRECTED-390.png", "width": 390, "selector": ".services-inner-hero-v2"},
    {"file": "SERVICES-V2-GALLERIES-EQUAL-1398.png", "width": 1398, "selector": "#services-category-addictions .services-category-section-v2__gallery"},
    {"file": "SERVICES-V2-GALLERIES-EQUAL-390.png", "width": 390, "selector": "#services-category-addictions .services-category-section-v2__gallery"},
    {"file": "SERVICES-V2-PROGRAM-CORRECTED-1398.png", "width": 1398, "selector": "#services-program"},
    {"file": "SERVICES-V2-PROGRAM-CORRECTED-390.png", "width": 390, "selector": "#services-program"},
    {"file": "SERVICES-V2-FOUNDER-1398.png", "width": 1398, "selector": "#services-founder"},
    {"file": "SERVICES-V2-FOUNDER-390.png", "width": 390, "selector": "#services-founder"},
    {"file": "SERVICES-V2-COMFORT-1398.png", "width": 1398, "selector": "#services-comfort"},
    {"file": "SERVICES-V2-COMFORT-390.png", "width": 390, "selector": "#services-comfort"},
    {"file": "SERVICES-V2-MID-CTA-1398.png", "width": 1398, "selector": "#services-mid-cta"},
    {"file": "SERVICES-V2-MID-CTA-390.png", "width": 390, "selector": "#services-mid-cta"},
    {"file": "SERVICES-V2-PROGRAM-TO-FOUNDER-1398.png", "width": 1398, "selector": "#services-program", "pad_bottom": 200},
    {"file": "SERVICES-V2-COMFORT-TO-CTA-1398.png", "width": 1398, "selector": "#services-comfort", "pad_bottom": 200},
    {"file": "HOME-SMOKE-AFTER-SERVICES-LOWER-PASS-1398.png", "width": 1398, "url": "/index.html", "full": True},
    {"file": "HOME-SMOKE-AFTER-SERVICES-LOWER-PASS-390.png", "width": 390, "url": "/index.html", "height": 844, "full": True},
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    probe_page = browser.new_page(viewport={"width": 1398, "height": 900})
    probe_page.goto(f"{base_url}/uslugi-v2.html", wait_until="networkidle")
    compiled = probe_page.evaluate(
        """() => {
      const hero = document.querySelector('.services-inner-hero-v2');
      const program = document.getElementById('services-program');
      const founder = document.getElementById('services-founder');
      const comfort = document.getElementById('services-comfort');
      const mid = document.getElementById('services-mid-cta');
      const gallery = document.querySelector('#services-category-addictions .services-category-section-v2__gallery');
      const imgs = gallery ? [...gallery.querySelectorAll('.services-category-section-v2__gallery-image')] : [];
      const heights = imgs.map(img => Math.round(img.getBoundingClientRect().height));
      const items = program ? [...program.querySelectorAll('.services-program-v2__item')] : [];
      const domOrderOk = items.every(el => {
        const body = el.querySelector('.services-program-v2__item-body');
        const media = el.querySelector('.services-program-v2__item-media');
        return body && media && body.compareDocumentPosition(media) & Node.DOCUMENT_POSITION_FOLLOWING;
      });
      return {
        heroScene: !!hero?.querySelector('.services-inner-hero-v2__scene'),
        heroEyebrow: hero?.querySelector('.services-inner-hero-v2__eyebrow')?.textContent?.trim() || '',
        heroTitle: hero?.querySelector('.services-inner-hero-v2__title')?.textContent?.trim() || '',
        galleryImageHeights: heights,
        galleryHeightsEqual: heights.length > 1 && heights.every(h => h === heights[0]),
        programDomOrderOk: domOrderOk,
        founder: !!founder,
        comfort: !!comfort,
        midCta: !!mid,
        loremFounder: founder?.textContent?.includes('Lorem ipsum') || false,
        comfortHeading: comfort?.querySelector('.services-comfort-v2__heading')?.textContent?.trim() || '',
        midLabel: mid?.querySelector('.services-mid-cta-v2__important-label')?.textContent?.trim() || '',
        modalHooks: document.querySelectorAll('[data-modal-open]').length,
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
            page.locator(shot["selector"]).screenshot(path=str(out_dir / shot["file"]))
        page.close()

    browser.close()

(out_dir / "compiled-content-probe.json").write_text(json.dumps(compiled, ensure_ascii=False, indent=2), encoding="utf-8")
print("capture complete", out_dir)
