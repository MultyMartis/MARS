from pathlib import Path
import json
from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174"
out_dir = Path(__file__).parent / "screenshots"
out_dir.mkdir(parents=True, exist_ok=True)

shots = [
    {"file": "SERVICES-V2-MOCKUP-COPY-FULL-1398.png", "width": 1398, "full": True},
    {"file": "SERVICES-V2-MOCKUP-COPY-FULL-390.png", "width": 390, "height": 844, "full": True},
    {"file": "SERVICES-V2-MOCKUP-COPY-CATEGORY-02-1398.png", "width": 1398, "selector": "#services-category-mental-health"},
    {"file": "SERVICES-V2-MOCKUP-COPY-CATEGORY-02-390.png", "width": 390, "selector": "#services-category-mental-health"},
    {"file": "SERVICES-V2-MOCKUP-COPY-CATEGORY-03-1398.png", "width": 1398, "selector": "#services-category-eating-disorders"},
    {"file": "SERVICES-V2-MOCKUP-COPY-CATEGORY-03-390.png", "width": 390, "selector": "#services-category-eating-disorders"},
    {"file": "SERVICES-V2-MOCKUP-COPY-CATEGORY-04-1398.png", "width": 1398, "selector": "#services-category-genotyping"},
    {"file": "SERVICES-V2-MOCKUP-COPY-CATEGORY-04-390.png", "width": 390, "selector": "#services-category-genotyping"},
    {"file": "SERVICES-V2-MOCKUP-COPY-TRANSITIONS-1398.png", "width": 1398, "selector": "#services-category-eating-disorders", "pad_top": 120},
    {"file": "SERVICES-V2-MOCKUP-COPY-TRANSITIONS-390.png", "width": 390, "selector": "#services-category-eating-disorders", "pad_top": 80},
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1398, "height": 900})
    page.goto(f"{base_url}/uslugi-v2.html", wait_until="networkidle")
    compiled = page.evaluate(
        """() => {
      const sections = ['services-category-mental-health','services-category-eating-disorders','services-category-genotyping'];
      return sections.map((id) => {
        const root = document.getElementById(id);
        if (!root) return { id, missing: true };
        return {
          id,
          intro: root.querySelector('.services-category-section-v2__intro')?.textContent?.trim() || '',
          lead: root.querySelector('.services-category-section-v2__lead')?.textContent?.trim() || '',
          body: root.querySelector('.services-category-section-v2__body')?.textContent?.trim() || '',
          serviceTextCount: root.querySelectorAll('.services-category-section-v2__service-text').length,
          loremServiceTextCount: [...root.querySelectorAll('.services-category-section-v2__service-text')].filter(el => el.textContent.includes('Lorem ipsum')).length,
        };
      });
    }"""
    )
    page.close()

    for shot in shots:
        vp = {"width": shot["width"], "height": shot.get("height", 900)}
        page = browser.new_page(viewport=vp)
        page.goto(f"{base_url}/uslugi-v2.html", wait_until="networkidle")
        if shot.get("full"):
            page.screenshot(path=str(out_dir / shot["file"]), full_page=True)
        else:
            loc = page.locator(shot["selector"])
            loc.screenshot(path=str(out_dir / shot["file"]))
        page.close()

    browser.close()

(out_dir / "compiled-content-probe.json").write_text(json.dumps(compiled, ensure_ascii=False, indent=2), encoding="utf-8")
print("capture complete", out_dir)
