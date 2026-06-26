"""Visual QA + functional checks + dependency border computed styles."""
import json
from pathlib import Path

from playwright.sync_api import sync_playwright

base_url = "http://127.0.0.1:4174"
review = Path(__file__).parent
shots = review / "screenshots"
shots.mkdir(parents=True, exist_ok=True)

results = {"screenshots": [], "functional": {}, "borders": {}, "overflow": {}}

with sync_playwright() as p:
    browser = p.chromium.launch()
    for label, width in [("1398", 1398), ("390", 390)]:
        page = browser.new_page(viewport={"width": width, "height": 900})
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(f"{base_url}/usluga-podrazdel-v1.html", wait_until="networkidle")

        # full page
        page.evaluate("window.scrollTo(0, 0)")
        full = shots / f"SERVICE-SUBDIVISION-FINAL-CORRECTIONS-FULL-{label}.png"
        page.screenshot(path=str(full), full_page=True)
        results["screenshots"].append(full.name)

        # program block
        prog = page.locator("#service-subdivision-program")
        prog.first.scroll_into_view_if_needed()
        pb = prog.first.bounding_box()
        page.screenshot(
            path=str(shots / f"SERVICE-SUBDIVISION-PROGRAM-NO-TEMPLATE-GARBAGE-{label}.png"),
            clip={"x": 0, "y": max(0, pb["y"] - 20), "width": width, "height": min(900, pb["height"] + 120)},
        )
        results["screenshots"].append(f"SERVICE-SUBDIVISION-PROGRAM-NO-TEMPLATE-GARBAGE-{label}.png")

        # dependencies
        dep = page.locator("#service-subdivision-dependencies")
        dep.first.scroll_into_view_if_needed()
        db = dep.first.bounding_box()
        page.screenshot(
            path=str(shots / f"SERVICE-SUBDIVISION-DEPENDENCIES-NO-DIVIDERS-{label}.png"),
            clip={"x": 0, "y": max(0, db["y"] - 10), "width": width, "height": min(1100, db["height"] + 40)},
        )
        results["screenshots"].append(f"SERVICE-SUBDIVISION-DEPENDENCIES-NO-DIVIDERS-{label}.png")

        # clinic landscape
        land = page.locator("section.home-clinic-landscape")
        land.first.scroll_into_view_if_needed()
        lb = land.first.bounding_box()
        page.screenshot(
            path=str(shots / f"SERVICE-SUBDIVISION-CLINIC-LANDSCAPE-{label}.png"),
            clip={"x": 0, "y": max(0, lb["y"] - 20), "width": width, "height": min(900, lb["height"] + 60)},
        )
        results["screenshots"].append(f"SERVICE-SUBDIVISION-CLINIC-LANDSCAPE-{label}.png")

        if label == "1398":
            # borders on dependency rows
            rows = page.locator(
                ".service-subdivision-dependencies-v1 .services-category-section-v2__service"
            )
            borders = []
            for i in range(rows.count()):
                style = rows.nth(i).evaluate(
                    """el => {
                    const cs = getComputedStyle(el);
                    return {
                      borderBottomWidth: cs.borderBottomWidth,
                      borderBottomStyle: cs.borderBottomStyle,
                    };
                }"""
                )
                borders.append(style)
            results["borders"]["desktop"] = borders

            # horizontal overflow
            overflow = page.evaluate(
                """() => {
                const w = document.documentElement.clientWidth;
                let bad = 0;
                document.querySelectorAll('*').forEach(el => {
                  const r = el.getBoundingClientRect();
                  if (r.width > 0 && r.right > w + 1) bad++;
                });
                return bad;
            }"""
            )
            results["overflow"]["desktop"] = overflow

            # functional smoke
            fn = {}
            fn["subnav_links"] = page.locator(".services-page-subnav__link").count()
            fn["cta_modal_open"] = page.locator("[data-modal-open]").count() > 0
            fn["program_link"] = page.locator("#service-subdivision-program .services-program-v2__head-link").count()
            fn["specialists_slider"] = page.locator("#service-subdivision-specialists .swiper").count()
            fn["founder_cta"] = page.locator(".home-founder-quote [data-modal-open]").count()
            fn["comfort_fancybox"] = page.locator("#service-subdivision-comfort [data-fancybox]").count()
            fn["reviews_slider"] = page.locator(".home-reviews .swiper").count()
            fn["faq_accordion"] = page.locator("#service-subdivision-faq [data-accordion]").count()
            fn["final_form"] = page.locator("#service-subdivision-final-form-heading").count()
            fn["modal"] = page.locator("[data-modal]").count()
            fn["clinic_landscape_sections"] = page.locator("section.home-clinic-landscape").count()
            fn["visible_else_text"] = "else {" in page.content()
            results["functional"] = fn
            results["console_errors"] = errors

    browser.close()

out = review / "qa-results.json"
out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(results, ensure_ascii=False, indent=2))
