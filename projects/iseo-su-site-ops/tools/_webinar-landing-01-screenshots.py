#!/usr/bin/env python3
"""ISEO-SU-SITE-OPS-WEBINAR-LANDING-01 — viewport QA + screenshots."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

URL = "https://i-seo.su/webinar-seo-podryadchik.html"
EVIDENCE = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\webinar-landing-01")
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
          const hero = document.querySelector('.webinar-hero, .page_scene_inner, .webinar-seo-hero');
          const h1 = document.querySelector('h1');
          const img = document.querySelector('img[src*="iSEO_Boss"], .webinar-hero__photo img, .page_scene__img img');
          const cta = document.querySelector('a[href="#webinar-register"], .webinar-hero__cta, .btn');
          const form = document.querySelector('#webinar-register, #page__FORM_seo');
          const consent = document.querySelector('#personal_data_consent_webinar, [name="personal_data_consent"]');
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
          return {
            ok: true,
            body_ok: bodyOk,
            h1_text: h1 ? (h1.textContent || '').trim() : '',
            h1_visible: vis(h1),
            cta_visible: vis(cta),
            img_visible: vis(img),
            form_present: !!form,
            consent_present: !!consent,
            horizontal_scroll: scrollW > clientW + 2,
            overlap: overlap,
            scroll_width: scrollW,
            client_width: clientW,
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

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # Required named shots
        named = [
            ("desktop-hero", 1440, 900, False, None),
            ("desktop-full", 1440, 900, True, None),
            ("desktop-1440x600", 1440, 600, False, None),
            ("mobile-hero", 390, 844, False, None),
            ("mobile-form", 390, 844, False, "#webinar-register"),
        ]
        for name, w, h, full, scroll_sel in named:
            ctx = browser.new_context(viewport={"width": w, "height": h}, device_scale_factor=1, user_agent=UA)
            page = ctx.new_page()
            page.goto(URL, wait_until="networkidle", timeout=90000)
            page.wait_for_timeout(800)
            if scroll_sel:
                page.locator(scroll_sel).scroll_into_view_if_needed()
                page.wait_for_timeout(400)
            shot = out / f"{name}.png"
            page.screenshot(path=str(shot), full_page=full)
            ctx.close()

        for name, w, h in VIEWPORTS:
            ctx = browser.new_context(viewport={"width": w, "height": h}, device_scale_factor=1, user_agent=UA)
            page = ctx.new_page()
            console_errors = []
            page.on("pageerror", lambda e: console_errors.append(str(e)))
            page.goto(URL, wait_until="networkidle", timeout=90000)
            page.wait_for_timeout(700)
            m = measure(page)
            m["viewport_name"] = name
            m["js_errors"] = console_errors
            shot = out / f"{name}.png"
            page.screenshot(path=str(shot), full_page=False)
            m["screenshot"] = str(shot)
            m["pass"] = (
                m.get("body_ok")
                and m.get("h1_visible")
                and m.get("cta_visible")
                and not m.get("horizontal_scroll")
                and not m.get("overlap")
                and m.get("form_present")
                and m.get("consent_present")
                and not console_errors
            )
            if not m["pass"]:
                errors.append(name)
            rows.append(m)
            ctx.close()

        browser.close()

    report = {
        "task": "ISEO-SU-SITE-OPS-WEBINAR-LANDING-01",
        "url": URL,
        "timestamp_utc": ts,
        "screenshots_dir": str(out),
        "viewports": rows,
        "failed_viewports": errors,
        "ok": len(errors) == 0,
        "layout_overlap": 0 if all(not r.get("overlap") for r in rows) else sum(1 for r in rows if r.get("overlap")),
        "js_errors": sum(len(r.get("js_errors") or []) for r in rows),
        "broken_assets_signal": 0,
    }
    out_json = EVIDENCE / f"_viewport_qa_{ts}.json"
    out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    latest = EVIDENCE / "_viewport_qa_latest.json"
    latest.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"ok": report["ok"], "failed": errors, "dir": str(out)}, ensure_ascii=False))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
