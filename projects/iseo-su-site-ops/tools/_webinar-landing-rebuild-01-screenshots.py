#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISEO-SU-SITE-OPS-WEBINAR-LANDING-REBUILD-01 — viewport QA + screenshots."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

URL = "https://i-seo.su/webinar-seo-podryadchik.html"
SOURCE_URL = "https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html"
EVIDENCE = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\webinar-landing-rebuild-01")
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

VIEWPORTS = [
    ("desktop-1920x1080", 1920, 1080),
    ("desktop-1440x900", 1440, 900),
    ("desktop-1366x768", 1366, 768),
    ("desktop-1280x720", 1280, 720),
    ("desktop-1440x600", 1440, 600),
    ("mobile-390x844", 390, 844),
    ("mobile-360x800", 360, 800),
]


def measure(page) -> dict:
    return page.evaluate(
        """() => {
          const hero = document.querySelector('.page_scene_inner, .page_scene');
          const h1 = document.querySelector('h1');
          const img = document.querySelector('img[src*="iSEO_Boss"]');
          const cta = document.querySelector('a[href="#webinar-register"]');
          const form = document.querySelector('#webinar-register, #page__FORM_seo');
          const consent = document.querySelector('[name="personal_data_consent"]');
          const header = document.querySelector('.page_header, header');
          const footer = document.querySelector('.page_footer, footer');
          const bodyOk = document.body.classList.contains('webinar-seo-podryadchik')
            && document.body.classList.contains('new-seo-landing-flex-first-screen');
          const scrollW = document.documentElement.scrollWidth;
          const clientW = document.documentElement.clientWidth;
          let overlap = false;
          if (h1 && img) {
            const a = h1.getBoundingClientRect();
            const b = img.getBoundingClientRect();
            const ix = Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left));
            const iy = Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top));
            if (ix > 24 && iy > 24 && window.innerWidth >= 1025) overlap = true;
          }
          const vis = (el) => {
            if (!el) return false;
            const r = el.getBoundingClientRect();
            const st = window.getComputedStyle(el);
            return r.width > 0 && r.height > 0 && st.visibility !== 'hidden' && st.display !== 'none';
          };
          const imgRect = img ? img.getBoundingClientRect() : null;
          const consoleErrors = (window.__iseo_console_errors || []).slice();
          return {
            ok: true,
            body_ok: bodyOk,
            h1_text: h1 ? (h1.textContent || '').trim() : '',
            h1_visible: vis(h1),
            cta_visible: vis(cta),
            img_visible: vis(img),
            img_width: imgRect ? Math.round(imgRect.width) : 0,
            img_height: imgRect ? Math.round(imgRect.height) : 0,
            form_present: !!form,
            consent_present: !!consent,
            header_present: !!header,
            footer_present: !!footer,
            horizontal_scroll: scrollW > clientW + 2,
            overlap: overlap,
            scroll_width: scrollW,
            client_width: clientW,
            console_errors: consoleErrors,
          };
        }"""
    )


def main() -> int:
    from playwright.sync_api import sync_playwright

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = EVIDENCE / "screenshots" / ts
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    errors = []
    broken = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(user_agent=UA)
        page = context.new_page()
        page.on(
            "pageerror",
            lambda exc: errors.append(str(exc)),
        )
        page.on(
            "console",
            lambda msg: errors.append(f"console:{msg.type}:{msg.text}")
            if msg.type == "error"
            else None,
        )
        page.on(
            "response",
            lambda resp: broken.append(resp.url)
            if resp.status >= 400
            and any(x in resp.url for x in ("/img/", "/css/", "/js/", "webinar"))
            else None,
        )

        # Source first screen
        page.set_viewport_size({"width": 1440, "height": 900})
        page.goto(SOURCE_URL, wait_until="networkidle", timeout=60000)
        page.screenshot(path=str(out / "01-source-first-screen.png"), full_page=False)

        # Rebuilt webinar first + full
        page.goto(URL, wait_until="networkidle", timeout=60000)
        page.evaluate(
            """() => { window.__iseo_console_errors = []; }"""
        )
        page.screenshot(path=str(out / "02-webinar-first-screen.png"), full_page=False)
        page.screenshot(path=str(out / "03-webinar-full-page.png"), full_page=True)

        # Mobile hero + form/footer
        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(URL, wait_until="networkidle", timeout=60000)
        page.screenshot(path=str(out / "04-mobile-hero.png"), full_page=False)
        form = page.query_selector("#webinar-register")
        if form:
            form.scroll_into_view_if_needed()
            page.wait_for_timeout(300)
        page.screenshot(path=str(out / "05-mobile-form-footer.png"), full_page=False)

        for name, w, h in VIEWPORTS:
            page.set_viewport_size({"width": w, "height": h})
            page.goto(URL, wait_until="networkidle", timeout=60000)
            page.wait_for_timeout(400)
            m = measure(page)
            shot = out / f"viewport-{name}.png"
            page.screenshot(path=str(shot), full_page=False)
            rows.append(
                {
                    "viewport": name,
                    "w": w,
                    "h": h,
                    "shot": str(shot),
                    **m,
                    "pass": bool(
                        m.get("body_ok")
                        and m.get("h1_visible")
                        and m.get("cta_visible")
                        and m.get("img_visible")
                        and m.get("form_present")
                        and m.get("consent_present")
                        and m.get("header_present")
                        and m.get("footer_present")
                        and not m.get("horizontal_scroll")
                        and not m.get("overlap")
                        and (m.get("img_width") or 0) >= (180 if w < 1025 else 280)
                    ),
                }
            )

        browser.close()

    report = {
        "task": "WEBINAR-LANDING-REBUILD-01",
        "ts": ts,
        "url": URL,
        "source_url": SOURCE_URL,
        "out_dir": str(out),
        "viewports": rows,
        "js_errors": errors,
        "broken_assets": sorted(set(broken)),
        "all_viewports_pass": all(r["pass"] for r in rows),
        "layout_overlap": sum(1 for r in rows if r.get("overlap")),
        "js_error_count": len(errors),
        "broken_asset_count": len(set(broken)),
    }
    (EVIDENCE / "viewport-qa.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (out / "viewport-qa.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["all_viewports_pass"] and not errors and not broken else 1


if __name__ == "__main__":
    raise SystemExit(main())
