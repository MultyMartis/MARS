#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Closeout: SEO recalc+resubmit, tariff_2-4 CTAs, responsive inspect, blog consent. Isolated mail only."""
from __future__ import annotations

import importlib.util
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ACCEPT = Path(__file__).resolve().parent / "_form-system-acceptance-01-accept.py"
_spec = importlib.util.spec_from_file_location("fsa_accept", ACCEPT)
acc = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(acc)

EVIDENCE = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-system-acceptance-01")
OUT = EVIDENCE / "_closeout-ui.json"
SITE = acc.SITE
NEST = f"{SITE}/services/seo/prodvizhenie-sajta-restorana.html"


def stamp_phone(suffix: str) -> str:
    base = datetime.now(timezone.utc).strftime("%H%M%S")
    return f"+7999{base[-6:]}{suffix}"[:16]


def blog_consent_live() -> dict:
    req = urllib.request.Request(
        f"{SITE}/blog.html",
        headers={"User-Agent": acc.UA},
    )
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    return {
        "url": f"{SITE}/blog.html",
        "consent_checkbox": 'name="personal_data_consent"' in html,
        "privacy_link": "privacy-policy.html" in html,
        "page_form": 'id="page__FORM"' in html or 'id="page__FORM_info"' in html or 'id="page__FORM_blog"' in html,
    }


def run_recalc_resubmit(browser) -> dict:
    posts, navs, console = [], [], []
    page = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=acc.UA)
    page.on("console", lambda m: console.append({"type": m.type, "text": m.text}) if m.type == "error" else None)
    page.on("framenavigated", lambda f: navs.append(f.url) if f == page.main_frame else None)
    acc.capture(page, posts, ("callback__FORM.php",))
    page.goto(f"{SITE}/services/seo.html", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(5000)
    page.locator(".tariff-calc-submit").first.click()
    page.wait_for_timeout(2000)
    first_result = page.locator(".tariff-calc-final-cost").first.inner_text()
    acc.PHONE = stamp_phone("1")
    acc.STAMP = datetime.now(timezone.utc).strftime("%H%M%S")
    f = page.locator("#callback__FORM_tariff_calc")
    acc.fill_common(f, name=f"FSA recalc1 {acc.STAMP}", phone=acc.PHONE)
    page.evaluate("() => document.getElementById('callback__FORM_tariff_calc_send').click()")
    page.wait_for_timeout(5500)
    first_body = next((p.get("body") for p in reversed(posts) if p.get("phase") == "resp"), None)
    first_success = acc.ui_success(page)
    page.locator("#traffic").first.fill("4500")
    page.locator(".tariff-calc-submit").first.click()
    page.wait_for_timeout(2000)
    second_result = page.locator(".tariff-calc-final-cost").first.inner_text()
    form_count = page.locator("#callback__FORM_tariff_calc").count()
    acc.PHONE = stamp_phone("2")
    acc.STAMP = datetime.now(timezone.utc).strftime("%H%M%S")
    f2 = page.locator("#callback__FORM_tariff_calc")
    acc.fill_common(f2, name=f"FSA recalc2 {acc.STAMP}", phone=acc.PHONE)
    page.evaluate("() => document.getElementById('callback__FORM_tariff_calc_send').click()")
    page.wait_for_timeout(5500)
    resp_bodies = [p.get("body") for p in posts if p.get("phase") == "resp"]
    dup_handler = page.evaluate(
        """() => {
          try {
            const $ = jQuery;
            const btn = document.getElementById('callback__FORM_tariff_calc_send');
            const clicks = (btn && $ && ($._data(btn,'events')||{}).click) || [];
            return clicks.length;
          } catch(e) { return null; }
        }"""
    )
    shot = acc.SHOT / "accept-seo_calculator_recalc.png"
    page.screenshot(path=str(shot), full_page=False)
    out = {
        "label": "seo_calculator_recalc_resubmit",
        "url": f"{SITE}/services/seo.html",
        "first_result_cost": first_result,
        "second_result_cost": second_result,
        "result_changed": first_result != second_result,
        "form_count_after_recalc": form_count,
        "first_body": first_body,
        "resp_bodies": resp_bodies,
        "second_body": resp_bodies[-1] if resp_bodies else None,
        "submit_count": len(resp_bodies),
        "first_success_ui": first_success,
        "final_success_ui": acc.ui_success(page),
        "page_reload": len(navs) > 1,
        "dup_click_handlers_on_button": dup_handler,
        "console_errors": console[:8],
        "screenshot": str(shot),
    }
    out["pass"] = (
        form_count == 1
        and out["submit_count"] == 2
        and all(b == "true" for b in resp_bodies)
        and out["final_success_ui"]
        and not out["page_reload"]
        and (dup_handler in (0, 1, None) or (isinstance(dup_handler, int) and dup_handler <= 1))
    )
    page.close()
    return out


def responsive_inspect(browser) -> dict:
    pages = [
        ("homepage", f"{SITE}/", "#page__FORM", "#page__FORM_send"),
        ("homepage_modal_trigger", f"{SITE}/", 'a[href="#audit__FORM_popup"]', "#audit__FORM_send"),
        ("seo_calc", f"{SITE}/services/seo.html", "#callback__FORM_tariff_calc", "#callback__FORM_tariff_calc_send"),
        ("tariff_calc", f"{SITE}/tariff-calc", "#callback__FORM_tariff_calc", "#callback__FORM_tariff_calc_send"),
        ("webinar", f"{SITE}/webinar-seo-podryadchik.html", "#page__FORM, #page__FORM_seo", "[id*='FORM_send']"),
    ]
    viewports = [(1440, 900), (390, 844)]
    rows = []
    for w, h in viewports:
        page = browser.new_page(viewport={"width": w, "height": h}, user_agent=acc.UA)
        for label, url, form_sel, btn_sel in pages:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(2500)
            if "seo" in label or "tariff_calc" == label:
                if page.locator(".tariff-calc-submit").count():
                    page.locator(".tariff-calc-submit").first.click()
                    page.wait_for_timeout(1200)
            if "modal" in label:
                page.evaluate(
                    """() => {
                      const a = document.querySelector('a[href="#audit__FORM_popup"]');
                      if (a && window.jQuery) window.jQuery(a).trigger('click');
                    }"""
                )
                page.wait_for_timeout(900)
            info = page.evaluate(
                """({formSel, btnSel}) => {
                  const form = document.querySelector(formSel.split(',')[0].trim());
                  const consent = form && form.querySelector('input[name="personal_data_consent"]');
                  const btn = document.querySelector(btnSel.split(',')[0].trim());
                  const box = (el) => {
                    if (!el) return null;
                    const r = el.getBoundingClientRect();
                    return {w: Math.round(r.width), h: Math.round(r.height), t: Math.round(r.top), vis: r.width>8 && r.height>8};
                  };
                  return {
                    form: box(form),
                    consent: box(consent),
                    button: box(btn),
                    vw: window.innerWidth,
                    vh: window.innerHeight
                  };
                }""",
                {"formSel": form_sel, "btnSel": btn_sel},
            )
            rows.append({"viewport": f"{w}x{h}", "label": label, **info})
        page.close()
    return {"rows": rows}


def main() -> None:
    acc.SHOT.mkdir(parents=True, exist_ok=True)
    report = {"started_utc": acc.utc_now(), "browser": []}
    report["blog_consent_live"] = blog_consent_live()
    sftp, transport = acc._v.sftp_connect()
    test_mode_on = False
    try:
        report["cfg_before"] = acc._v.cfg_snapshot(sftp)
        acc._v.set_test_mode(sftp, True)
        test_mode_on = True
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            report["seo_recalc"] = run_recalc_resubmit(browser)
            for n in (2, 3, 4):
                acc.PHONE = stamp_phone(str(n))
                acc.STAMP = datetime.now(timezone.utc).strftime("%H%M%S")
                report["browser"].append(
                    acc.browser_submit(
                        browser,
                        label=f"nested_tariff{n}_modal",
                        url=NEST,
                        form_sel=f"#tariff_{n}__FORM_seo",
                        btn_sel=f"#tariff_{n}__FORM_send_seo",
                        open_sel=f'a.modalbox[href="#tariff_{n}__FORM_popup"]',
                        needles=(f"tariff_{n}__FORM.php",),
                    )
                )
            report["responsive"] = responsive_inspect(browser)
            browser.close()
    except Exception as exc:  # noqa: BLE001
        report["crash"] = str(exc)
    finally:
        if test_mode_on:
            acc._v.set_test_mode(sftp, False)
        report["cfg_final"] = acc._v.cfg_snapshot(sftp)
        sftp.close()
        transport.close()
    report["finished_utc"] = acc.utc_now()
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "blog_consent": report.get("blog_consent_live"),
                "seo_recalc_pass": (report.get("seo_recalc") or {}).get("pass"),
                "seo_recalc": {
                    k: (report.get("seo_recalc") or {}).get(k)
                    for k in (
                        "first_body",
                        "second_body",
                        "submit_count",
                        "form_count_after_recalc",
                        "result_changed",
                        "dup_click_handlers_on_button",
                        "pass",
                    )
                },
                "tariff_modals": [
                    {
                        "label": b.get("label"),
                        "pass": b.get("pass"),
                        "body": b.get("body"),
                        "request_url": b.get("request_url"),
                    }
                    for b in report.get("browser") or []
                ],
                "crash": report.get("crash"),
                "test_mode_final": (report.get("cfg_final") or {}).get("test_mode"),
                "prod_has_im_work": (report.get("cfg_final") or {}).get("prod_has_im_work"),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
