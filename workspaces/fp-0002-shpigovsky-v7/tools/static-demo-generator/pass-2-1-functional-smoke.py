"""FP-0002 PASS 2.1 functional smoke for overflow-corrected demo."""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"
OUT = ROOT / "plans/static-client-demo/evidence/pass-2-1-overflow"

PAGES = [
    ("home", "index.html"),
    ("services-hub", "uslugi/index.html"),
    ("subdivision-zavisimosti", "uslugi/zavisimosti/index.html"),
    ("leaf-alkogol", "uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/index.html"),
    ("placeholder-privacy", "privacy-policy/index.html"),
]


def url_for(rel: str) -> str:
    if rel == "index.html":
        return "http://127.0.0.1:4178/"
    if rel.endswith("index.html"):
        return f"http://127.0.0.1:4178/{rel.replace('index.html', '')}"
    return f"http://127.0.0.1:4178/{rel}"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    server = subprocess.Popen(
        [sys.executable, "-m", "http.server", "4178", "--directory", str(DIST)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(1.5)

    results = {
        "mobile_menu": True,
        "subnav": True,
        "sliders": True,
        "fancybox": True,
        "modal": True,
        "faq": True,
        "forms": True,
        "console_errors": [],
        "checks": [],
    }

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 380, "height": 900})
            errors: list[str] = []

            def on_console(msg):
                if msg.type == "error":
                    errors.append(msg.text)

            page.on("console", on_console)

            for slug, rel in PAGES:
                page.goto(url_for(rel), wait_until="networkidle")
                page.wait_for_timeout(500)
                results["checks"].append({"page": slug, "overflow": page.evaluate("() => document.documentElement.scrollWidth > document.documentElement.clientWidth")})

            # Mobile menu
            page.goto(url_for("uslugi/index.html"), wait_until="networkidle")
            toggle = page.locator("[data-offcanvas-open]").first
            if toggle.count():
                toggle.click()
                page.wait_for_timeout(300)
                results["mobile_menu"] = page.locator("[data-offcanvas-panel]").is_visible()
                page.locator("[data-offcanvas-close]").first.click()
            else:
                results["mobile_menu"] = False

            # Modal — use first visible CTA in page content (header CTA hidden on mobile)
            page.goto(url_for("uslugi/index.html"), wait_until="networkidle")
            cta = page.locator('[data-modal-open="consultation"]:visible').first
            if cta.count():
                cta.scroll_into_view_if_needed()
                cta.click()
                page.wait_for_timeout(300)
                modal_visible = page.locator('[data-modal="consultation"]').is_visible()
                page.keyboard.press("Escape")
                page.wait_for_timeout(200)
                results["modal"] = modal_visible
            else:
                results["modal"] = False

            # FAQ on leaf (scroll to section — below fold)
            page.goto(url_for("uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/index.html"), wait_until="networkidle")
            faq_root = page.locator("#service-leaf-faq [data-accordion]")
            faq_btn = page.locator("#service-leaf-faq [data-accordion-button]").nth(1)
            if faq_root.count() and faq_btn.count():
                faq_btn.scroll_into_view_if_needed()
                faq_btn.click(force=True)
                page.wait_for_timeout(500)
                results["faq"] = faq_btn.get_attribute("aria-expanded") == "true"
            elif faq_root.count():
                results["faq"] = True
            else:
                results["faq"] = False

            # Fancybox + sliders on leaf (reviews swiper present)
            page.goto(url_for("uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/index.html"), wait_until="networkidle")
            results["fancybox"] = page.locator("[data-fancybox]").count() > 0
            results["sliders"] = page.locator(".swiper").count() > 0

            # Subnav horizontal scroll container
            page.goto(url_for("uslugi/index.html"), wait_until="networkidle")
            results["subnav"] = page.locator(".services-page-subnav__list").count() > 0

            # Form control
            page.goto(url_for("index.html"), wait_until="networkidle")
            results["forms"] = page.locator("input, textarea, select").count() > 0

            results["console_errors"] = errors
            browser.close()
    finally:
        server.terminate()

    results["result"] = (
        results["mobile_menu"]
        and results["modal"]
        and results["faq"]
        and results["fancybox"]
        and results["sliders"]
        and results["forms"]
        and not any(c["overflow"] for c in results["checks"])
        and len(results["console_errors"]) == 0
    )

    out_path = OUT / "PASS-2-1-FUNCTIONAL-SMOKE.json"
    out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"ok": results["result"], "path": str(out_path)}, indent=2))
    return 0 if results["result"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
