from pathlib import Path
import json
from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174"
out_dir = Path(__file__).parent / "screenshots"
out_dir.mkdir(parents=True, exist_ok=True)

shots = [
    {"file": "SERVICES-V2-FINAL-ASSEMBLY-FULL-1398.png", "width": 1398, "full": True},
    {"file": "SERVICES-V2-FINAL-ASSEMBLY-FULL-390.png", "width": 390, "height": 844, "full": True},
    {"file": "SERVICES-V2-PROGRAM-WITHOUT-DESC-1398.png", "width": 1398, "selector": "#services-program"},
    {"file": "SERVICES-V2-PROGRAM-WITHOUT-DESC-390.png", "width": 390, "selector": "#services-program"},
    {"file": "SERVICES-V2-HOME-FOUNDER-1398.png", "width": 1398, "selector": ".home-founder-quote"},
    {"file": "SERVICES-V2-HOME-FOUNDER-390.png", "width": 390, "selector": ".home-founder-quote"},
    {"file": "SERVICES-V2-HOME-COMFORT-1398.png", "width": 1398, "selector": ".home-comfort"},
    {"file": "SERVICES-V2-HOME-COMFORT-390.png", "width": 390, "selector": ".home-comfort"},
    {"file": "SERVICES-V2-SECOND-PROGRAM-CTA-1398.png", "width": 1398, "selector": ".home-comfort + .container .services-program-v2__cta-band"},
    {"file": "SERVICES-V2-SECOND-PROGRAM-CTA-390.png", "width": 390, "selector": ".home-comfort + .container .services-program-v2__cta-band"},
    {"file": "SERVICES-V2-HOME-FAQ-1398.png", "width": 1398, "selector": ".home-faq"},
    {"file": "SERVICES-V2-HOME-FAQ-390.png", "width": 390, "selector": ".home-faq"},
    {"file": "SERVICES-V2-HOME-FINAL-FORM-1398.png", "width": 1398, "selector": ".home-final-form"},
    {"file": "SERVICES-V2-HOME-FINAL-FORM-390.png", "width": 390, "selector": ".home-final-form"},
    {"file": "SERVICES-V2-COMFORT-TO-CTA-TO-FAQ-1398.png", "width": 1398, "selector": ".home-comfort", "pad_bottom": 400},
    {"file": "SERVICES-V2-FAQ-TO-FORM-1398.png", "width": 1398, "selector": ".home-faq", "pad_bottom": 300},
    {"file": "HOME-SMOKE-AFTER-SERVICES-FINAL-ASSEMBLY-1398.png", "width": 1398, "url": "/index.html", "full": True},
    {"file": "HOME-SMOKE-AFTER-SERVICES-FINAL-ASSEMBLY-390.png", "width": 390, "url": "/index.html", "height": 844, "full": True},
]

widths = [320, 390, 430, 768, 1024, 1025, 1280, 1398, 1440, 1920]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1398, "height": 900})
    page.goto(f"{base_url}/uslugi-v2.html", wait_until="networkidle")

    compiled = page.evaluate(
        """() => {
      const count = (sel) => document.querySelectorAll(sel).length;
      const ids = [...document.querySelectorAll('[id]')].map(el => el.id);
      const dup = ids.filter((id, i) => ids.indexOf(id) !== i);
      const programItems = [...document.querySelectorAll('.services-program-v2__item')];
      const domOrderOk = programItems.every(el => {
        const body = el.querySelector('.services-program-v2__item-body');
        const media = el.querySelector('.services-program-v2__item-media');
        return body && media && body.compareDocumentPosition(media) & Node.DOCUMENT_POSITION_FOLLOWING;
      });
      const ctaBands = [...document.querySelectorAll('.services-program-v2__cta-band')];
      const faqBtn1 = document.getElementById('home-faq-trigger-1');
      const faqBtn2 = document.getElementById('home-faq-trigger-2');
      return {
        itemDesc: count('.services-program-v2__item-desc'),
        ctaBands: ctaBands.length,
        homeFounder: count('section.home-founder-quote'),
        servicesFounder: count('.services-founder-v2'),
        homeComfort: count('section.home-comfort'),
        servicesComfort: count('.services-comfort-v2'),
        homeFaq: count('section.home-faq'),
        homeFinalForm: count('section.home-final-form'),
        servicesMidCta: count('.services-mid-cta-v2'),
        footer: count('footer'),
        modal: count('.modal-consultation'),
        duplicateIds: [...new Set(dup)],
        programDomOrderOk: domOrderOk,
        ctaSources: ctaBands.map(b => b.querySelector('[data-modal-source]')?.getAttribute('data-modal-source')),
        faq1Expanded: faqBtn1?.getAttribute('aria-expanded'),
        faq2ExpandedBefore: faqBtn2?.getAttribute('aria-expanded'),
      };
    }"""
    )

    # FAQ functional
    page.click("#home-faq-trigger-2")
    page.wait_for_timeout(200)
    faq_after = page.evaluate(
        """() => ({
      faq1Expanded: document.getElementById('home-faq-trigger-1')?.getAttribute('aria-expanded'),
      faq2Expanded: document.getElementById('home-faq-trigger-2')?.getAttribute('aria-expanded'),
      faq2Hidden: document.getElementById('home-faq-panel-2')?.hasAttribute('hidden'),
    })"""
    )
    compiled["faqFunctional"] = faq_after

    # CTA modal hooks
    cta_modal = page.evaluate(
        """() => {
      const bands = [...document.querySelectorAll('.services-program-v2__cta-band [data-modal-open]')];
      return bands.map(b => b.getAttribute('data-modal-source'));
    }"""
    )
    compiled["ctaModalSources"] = cta_modal

  # Responsive overflow probe
    responsive = {}
    for w in widths:
        probe = browser.new_page(viewport={"width": w, "height": 900})
        probe.goto(f"{base_url}/uslugi-v2.html", wait_until="networkidle")
        responsive[str(w)] = probe.evaluate(
            """() => ({
          overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth,
          overlap: false,
        })"""
        )
        probe.close()
    compiled["responsive"] = responsive

    page.close()

    for shot in shots:
        vp = {"width": shot["width"], "height": shot.get("height", 900)}
        sp = browser.new_page(viewport=vp)
        sp.goto(f"{base_url}{shot.get('url', '/uslugi-v2.html')}", wait_until="networkidle")
        if shot.get("full"):
            sp.screenshot(path=str(out_dir / shot["file"]), full_page=True)
        else:
            sp.locator(shot["selector"]).first.screenshot(path=str(out_dir / shot["file"]))
        sp.close()

    browser.close()

(out_dir / "compiled-content-probe.json").write_text(json.dumps(compiled, ensure_ascii=False, indent=2), encoding="utf-8")
(out_dir / "functional-qa.json").write_text(json.dumps(compiled.get("faqFunctional", {}), ensure_ascii=False, indent=2), encoding="utf-8")
print("capture complete", out_dir)
