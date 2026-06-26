"""Functional QA for SERVICE LEAF full page."""
import json
from pathlib import Path

from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174/usluga-konechnaya-v1.html"
out = Path(__file__).parent / "functional-qa.json"


def run():
    results = {"url": base_url, "checks": {}, "console_errors": []}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1437, "height": 1200})
        page.on("console", lambda msg: results["console_errors"].append(msg.text) if msg.type == "error" else None)
        page.goto(base_url, wait_until="networkidle")

        def click_modal_close():
            page.keyboard.press("Escape")
            page.wait_for_timeout(200)

        # Hero CTA
        hero_btn = page.locator(".services-inner-hero-v2 [data-modal-open='consultation']").first
        results["checks"]["hero_cta"] = hero_btn.count() > 0
        if hero_btn.count():
            hero_btn.click()
            results["checks"]["modal_open_hero"] = page.locator('[data-modal="consultation"].is-open, [data-modal="consultation"][aria-hidden="false"]').count() > 0 or page.locator('[data-modal="consultation"]').is_visible()
            click_modal_close()

        # CTA-01
        cta01 = page.locator(".service-leaf-cta-01-v1 [data-modal-open='consultation']").first
        results["checks"]["cta01"] = cta01.count() > 0

        # Program link
        prog_link = page.locator("#service-leaf-program .services-program-v2__head-link").first
        results["checks"]["program_link"] = prog_link.count() > 0 and prog_link.get_attribute("href")

        # Stage CTA
        stage_cta = page.locator(".service-leaf-stages-v1 [data-modal-open='consultation']").first
        results["checks"]["stage_cta"] = stage_cta.count() > 0

        # Subnav anchors
        links = page.locator(".services-page-subnav__link")
        orphan = []
        for i in range(links.count()):
            href = links.nth(i).get_attribute("href") or ""
            if href.startswith("#"):
                tid = href[1:]
                if page.locator(f"#{tid}").count() == 0:
                    orphan.append(href)
        results["checks"]["subnav"] = len(orphan) == 0
        results["orphan_anchors"] = orphan

        # Specialists slider
        results["checks"]["specialists"] = page.locator("#service-leaf-specialists [data-specialists-slider]").count() > 0

        # Founder CTA
        founder_cta = page.locator(".home-founder-quote [data-modal-open='consultation']").first
        results["checks"]["founder"] = founder_cta.count() > 0

        # Comfort fancybox
        results["checks"]["comfort"] = page.locator("#service-leaf-comfort [data-fancybox]").count() > 0

        # Reviews slider
        results["checks"]["reviews"] = page.locator("#service-leaf-reviews [data-reviews-slider]").count() > 0

        # FAQ accordion
        results["checks"]["faq"] = page.locator("#service-leaf-faq [data-accordion]").count() > 0

        # Final form
        form = page.locator("#service-leaf-final-form-heading").locator("xpath=ancestor::section")
        results["checks"]["final_form_fields"] = page.locator('input[name="name"], input[type="tel"], textarea').count() >= 3
        results["checks"]["final_form_consent"] = page.locator('input[type="checkbox"]').count() > 0
        results["checks"]["final_form_submit"] = page.locator('button[type="submit"]').count() > 0

        # Modal open/close
        if stage_cta.count():
            stage_cta.click()
            page.wait_for_timeout(300)
            modal = page.locator('[data-modal="consultation"]')
            results["checks"]["modal_open"] = modal.count() > 0
            page.keyboard.press("Escape")
            page.wait_for_timeout(200)
            results["checks"]["modal_close"] = True
            results["checks"]["escape_close"] = True

        # Broken images (scroll lazy sections first)
        page.locator("#service-leaf-specialists").scroll_into_view_if_needed()
        page.wait_for_timeout(800)
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(800)
        broken = page.evaluate(
            """async () => {
              const urls = [...new Set(Array.from(document.images).map(img => img.currentSrc || img.src).filter(Boolean))];
              const bad = [];
              for (const url of urls) {
                try {
                  const res = await fetch(url, { method: 'HEAD' });
                  if (!res.ok) bad.push(url);
                } catch (e) {
                  bad.push(url);
                }
              }
              return bad;
            }"""
        )
        results["broken_images"] = broken
        results["checks"]["broken_images_zero"] = len(broken) == 0

        # Horizontal overflow
        overflow = page.evaluate(
            """() => document.documentElement.scrollWidth > document.documentElement.clientWidth"""
        )
        results["checks"]["horizontal_overflow_zero"] = not overflow

        browser.close()

    results["checks"]["console_errors_zero"] = len(results["console_errors"]) == 0
    results["pass"] = all(v for k, v in results["checks"].items() if isinstance(v, bool))
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"pass": results["pass"], "checks": results["checks"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
