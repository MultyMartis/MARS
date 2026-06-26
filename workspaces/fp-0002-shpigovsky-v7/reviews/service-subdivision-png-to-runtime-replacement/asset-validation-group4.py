"""Browser image load validation for GROUP 4 assets."""
from pathlib import Path
import json

from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174/usluga-podrazdel-v1.html"
review = Path(__file__).parent

checks = {}

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1437, "height": 900})
    page.goto(base_url, wait_until="networkidle")
    for key, selector in {
        "corridor": ".service-subdivision-team-stats-v1__corridor-image",
        "team": ".service-subdivision-team-stats-v1__staff-image",
    }.items():
        img = page.locator(selector)
        img.first.scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        checks[key] = page.evaluate(
            """(sel) => {
              const el = document.querySelector(sel);
              if (!el) return { present: false };
              const r = el.getBoundingClientRect();
              return {
                present: true,
                src: el.currentSrc || el.src,
                naturalWidth: el.naturalWidth,
                naturalHeight: el.naturalHeight,
                renderedWidth: r.width,
                renderedHeight: r.height,
                complete: el.complete,
              };
            }""",
            selector,
        )
    browser.close()

(review / "asset-validation-group4-result.json").write_text(
    json.dumps(checks, ensure_ascii=False, indent=2), encoding="utf-8"
)
print(json.dumps(checks, ensure_ascii=False, indent=2))
