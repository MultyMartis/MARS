#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Isolated browser + mail acceptance for FORM-SYSTEM-ACCEPTANCE-01.

Never sends to nikel007i33@yandex.ru. test_mode ON only during this run, OFF in finally.
"""
from __future__ import annotations

import importlib.util
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

_VALIDATE = Path(__file__).resolve().parent / "_form-contract-regression-01-validate.py"
_spec = importlib.util.spec_from_file_location("form_contract_validate", _VALIDATE)
_v = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_v)

EVIDENCE = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-system-acceptance-01")
OUT = EVIDENCE / "_accept.json"
SHOT = EVIDENCE / "screenshots"
UA = "ISEO-SU-FORM-SYSTEM-ACCEPTANCE-01-ACCEPT/1.0"
SITE = "https://i-seo.su"
TOKEN_URL = f"{SITE}/iseo-form-token.php"
STAMP = datetime.now(timezone.utc).strftime("%H%M%S")
PHONE = f"+7999{STAMP[-7:]}"

HANDLERS = {
    "page": {
        "url": f"{SITE}/page__FORM.php",
        "fields": {
            "pf_name": f"FSA PAGE {STAMP}",
            "pf_contact": "WhatsApp",
            "pf_phone": PHONE,
            "pf_site": "",
            "pf_comment": "FSA isolated mail — ignore",
            "personal_data_consent": "1",
        },
    },
    "callback": {
        "url": f"{SITE}/callback__FORM.php",
        "fields": {
            "cf_name": f"FSA CB {STAMP}",
            "cf_contact": "Телефон",
            "cf_phone": PHONE,
            "cf_site": "не указан",
            "personal_data_consent": "1",
        },
    },
    "audit": {
        "url": f"{SITE}/audit__FORM.php",
        "fields": {
            "af_name": f"FSA AUDIT {STAMP}",
            "af_contact": "WhatsApp",
            "af_phone": PHONE,
            "af_site": "",
            "af_comment": "FSA isolated — ignore",
            "af_email": "",
            "af_coast": "",
            "personal_data_consent": "1",
        },
    },
    "calc": {
        "url": f"{SITE}/calc__FORM.php",
        "fields": {
            "radio_st_01": "a",
            "radio_st_02": "a",
            "radio_st_03": "a",
            "radio_st_04": "a",
            "radio_st_05": "a",
            "calc_name": f"FSA CALC {STAMP}",
            "calc_contact": "Телефон",
            "calc_phone": PHONE,
            "calc_site": "",
            "personal_data_consent": "1",
        },
    },
    "bonus": {
        "url": f"{SITE}/bonus__FORM.php",
        "fields": {
            "bf_name": f"FSA BONUS {STAMP}",
            "bf_contact": "WhatsApp",
            "bf_phone": PHONE,
            "bf_comment": "FSA isolated — ignore",
            "personal_data_consent": "1",
        },
    },
    "career": {
        "url": f"{SITE}/career__FORM.php",
        "fields": {
            "cf_name": f"FSA CAREER {STAMP}",
            "cf_contact": "Телефон",
            "cf_phone": PHONE,
            "cf_file": "",
            "personal_data_consent": "1",
        },
    },
    "partners": {
        "url": f"{SITE}/partners__FORM.php",
        "fields": {
            "pf_name": f"FSA PARTNERS {STAMP}",
            "pf_site": "https://example-fsa.test",
            "pt_contact": "WhatsApp",
            "pt_phone": PHONE,
            "pf_comment": "FSA isolated — ignore",
            "personal_data_consent": "1",
        },
    },
    "review": {
        "url": f"{SITE}/review__FORM.php",
        "fields": {
            "rf_name": f"FSA REVIEW {STAMP}",
            "rf_contact": "Телефон",
            "rf_phone": PHONE,
            "rf_comment": "FSA isolated — ignore",
            "personal_data_consent": "1",
        },
    },
}

LABEL_TO_HANDLER = {
    "homepage_main": "page",
    "homepage_audit_modal": "audit",
    "homepage_calc": "calc",
    "seo_calculator": "callback",
    "tariff_calculator": "callback",
    "nested_seo_page": "page",
    "blog_html": "page",
    "blog_wp_footer_callback": "callback",
    "career": "career",
    "partners": "partners",
    "reviews": "review",
    "bonuses": "bonus",
    "nested_tariff1_modal": "tariff_1",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def post_handler(handler_url: str, fields: dict, page_link: str) -> dict:
    tok = json.loads(
        urllib.request.urlopen(
            urllib.request.Request(TOKEN_URL, headers={"User-Agent": UA}), timeout=30
        ).read().decode("utf-8")
    )
    time.sleep(3.3)
    data = {
        "contact_company_url": "",
        "iseo_ft": tok["t"],
        "iseo_fs": tok["s"],
        "iseo_fid": tok["id"],
        "pf_page_title": f"FSA MAIL {STAMP}",
        "pf_page_link": page_link,
    }
    data.update(fields)
    body = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(
        handler_url,
        data=body,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded", "User-Agent": UA},
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return {
                "http_status": resp.status,
                "body": resp.read().decode("utf-8", "replace").strip(),
            }
    except urllib.error.HTTPError as e:
        return {
            "http_status": e.code,
            "body": e.read().decode("utf-8", "replace").strip(),
        }


def capture(page, bag, needles):
    def on_request(req):
        if req.method == "POST" and any(x in req.url for x in needles):
            bag.append({"phase": "req", "url": req.url, "post": req.post_data})

    def on_response(resp):
        if resp.request.method == "POST" and any(x in resp.url for x in needles):
            try:
                body = resp.text().strip()
            except Exception as exc:  # noqa: BLE001
                body = f"READ_FAIL:{exc}"
            bag.append({"phase": "resp", "url": resp.url, "status": resp.status, "body": body})

    page.on("request", on_request)
    page.on("response", on_response)


def ui_success(page) -> bool:
    # textContent keeps success copy after fancybox closes (innerText hides display:none).
    return page.evaluate(
        "() => /Успешно! Сообщение отправлено/i.test(document.body.textContent||'')"
    )


def fill_common(form, *, name: str, phone: str, method: str | None = "Телефон"):
    for sel in [
        "input[name='pf_name']",
        "input[name='cf_name']",
        "input[name='af_name']",
        "input[name='bf_name']",
        "input[name='rf_name']",
        "input[name='calc_name']",
    ]:
        loc = form.locator(sel)
        if loc.count():
            loc.first.fill(name, force=True)
            break
    for sel in [
        "select[name='pf_contact']",
        "select[name='cf_contact']",
        "select[name='cf_ontact']",
        "select[name='af_contact']",
        "select[name='af_ontact']",
        "select[name='calc_contact']",
        "select[name='bf_contact']",
        "select[name='rf_contact']",
        "select[name='rf_ontact']",
        "select[name='pt_contact']",
    ]:
        loc = form.locator(sel)
        if loc.count() and method:
            try:
                loc.first.select_option(method)
            except Exception:
                try:
                    loc.first.select_option("WhatsApp")
                except Exception:
                    try:
                        loc.first.select_option(index=1)
                    except Exception:
                        pass
            break
    else:
        text_method = form.locator("input[name='cf_contact'][type='text'], input[name='bf_contact']")
        if text_method.count() and method:
            text_method.first.fill(method, force=True)
    for sel in [
        "input[name='pf_phone']",
        "input[name='cf_phone']",
        "input[name='af_phone']",
        "input[name='bf_phone']",
        "input[name='rf_phone']",
        "input[name='pt_phone']",
        "input[name='calc_phone']",
    ]:
        loc = form.locator(sel)
        if loc.count():
            loc.first.fill(phone, force=True)
            break
    comment = form.locator("textarea[name='pf_comment'], textarea[name='af_comment'], textarea[name='bf_comment'], textarea[name='rf_comment']")
    if comment.count():
        comment.first.fill(f"FSA UI {STAMP} — ignore", force=True)
    form.evaluate(
        """el => {
          el.querySelectorAll('input[name="personal_data_consent"], input.required-checkbox').forEach(i => {
            i.checked = true;
            i.dispatchEvent(new Event('change', {bubbles: true}));
          });
        }"""
    )


def browser_submit(browser, *, label, url, form_sel, btn_sel, open_sel=None, needles=None, extra=None, viewport=None):
    needles = needles or ("__FORM.php",)
    posts, navs, console = [], [], []
    page = browser.new_page(
        viewport=viewport or {"width": 1440, "height": 900},
        user_agent=UA,
    )
    page.on("console", lambda m: console.append({"type": m.type, "text": m.text}) if m.type == "error" else None)
    page.on("framenavigated", lambda f: navs.append(f.url) if f == page.main_frame else None)
    capture(page, posts, needles)
    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(6500)
    if extra:
        extra(page)
    if open_sel:
        page.evaluate(
            """(sel) => {
              const a = document.querySelector(sel);
              if (!a) return false;
              if (window.jQuery) { window.jQuery(a).trigger('click'); return true; }
              a.click();
              return true;
            }""",
            open_sel,
        )
        page.wait_for_timeout(1800)
    f = page.locator(form_sel)
    if f.count():
        try:
            f.first.scroll_into_view_if_needed()
        except Exception:
            pass
        try:
            fill_common(f.first, name=f"FSA {label} {STAMP}", phone=PHONE)
        except Exception as exc:  # noqa: BLE001
            page.close()
            return {"label": label, "url": url, "pass": False, "error": f"fill:{exc}"}
    if page.locator(btn_sel).count():
        clicked = page.evaluate(
            """(sel) => {
              const b = document.querySelector(sel);
              if (!b) return false;
              b.click();
              return true;
            }""",
            btn_sel.split(",")[0].strip(),
        )
        if not clicked:
            try:
                page.locator(btn_sel).first.click(force=True)
            except Exception as exc:  # noqa: BLE001
                page.close()
                return {"label": label, "url": url, "pass": False, "error": f"click:{exc}"}
    page.wait_for_timeout(5500)
    resp = next((p for p in posts if p.get("phase") == "resp"), None)
    req = next((p for p in posts if p.get("phase") == "req"), None)
    shot = SHOT / f"accept-{label}.png"
    try:
        page.screenshot(path=str(shot), full_page=False)
    except Exception:
        shot = None
    out = {
        "label": label,
        "url": url,
        "request_url": req.get("url") if req else None,
        "http": resp.get("status") if resp else None,
        "body": resp.get("body") if resp else None,
        "success_ui": ui_success(page),
        "page_reload": len(navs) > 1,
        "nav_count": len(navs),
        "console_errors": console[:8],
        "wrong_endpoint": bool(req and "/services/" in (req.get("url") or "") and "__FORM.php" in (req.get("url") or "")),
        "screenshot": str(shot) if shot else None,
    }
    out["pass"] = (
        out["body"] == "true"
        and out["success_ui"]
        and not out["page_reload"]
        and not out["wrong_endpoint"]
    )
    page.close()
    return out


def run_calculator(browser, *, label, url):
    posts, navs, console = [], [], []
    page = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
    page.on("console", lambda m: console.append({"type": m.type, "text": m.text}) if m.type == "error" else None)
    page.on("framenavigated", lambda f: navs.append(f.url) if f == page.main_frame else None)
    capture(page, posts, ("callback__FORM.php",))
    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(5000)
    if page.locator(".tariff-calc-submit").count():
        page.locator(".tariff-calc-submit").first.click()
        page.wait_for_timeout(2000)
    after = page.evaluate(
        """() => {
          const res = document.querySelector('.tariff-calc-result');
          const form = document.querySelector('#callback__FORM_tariff_calc');
          const req = document.querySelector('.tariff-calc-request');
          return {
            result_text: res ? (res.innerText||'').slice(0,180) : '',
            result_display: res ? getComputedStyle(res).display : null,
            form: !!form,
            consent: !!(form && form.querySelector('input[name="personal_data_consent"]')),
            request_display: req ? getComputedStyle(req).display : null
          };
        }"""
    )
    f = page.locator("#callback__FORM_tariff_calc")
    fill_common(f, name=f"FSA {label} {STAMP}", phone=PHONE)
    page.locator("#callback__FORM_tariff_calc_send").click(force=True)
    page.wait_for_timeout(5500)
    resp = next((p for p in posts if p.get("phase") == "resp"), None)
    req = next((p for p in posts if p.get("phase") == "req"), None)
    # recalculate
    if page.locator(".tariff-calc-submit").count():
        page.locator(".tariff-calc-submit").first.click()
        page.wait_for_timeout(800)
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
    shot = SHOT / f"accept-{label}.png"
    page.screenshot(path=str(shot), full_page=False)
    out = {
        "label": label,
        "url": url,
        "calculation": after,
        "request_url": req.get("url") if req else None,
        "http": resp.get("status") if resp else None,
        "body": resp.get("body") if resp else None,
        "success_ui": ui_success(page),
        "page_reload": len(navs) > 1,
        "console_errors": console[:8],
        "dup_click_handlers_on_button": dup_handler,
        "screenshot": str(shot),
    }
    out["pass"] = (
        after.get("form")
        and after.get("consent")
        and out["body"] == "true"
        and out["success_ui"]
        and not out["page_reload"]
        and (out["request_url"] or "").endswith("/callback__FORM.php")
    )
    page.close()
    return out


def run_homepage_calc(browser):
    posts, navs, console = [], [], []
    page = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
    page.on("console", lambda m: console.append({"type": m.type, "text": m.text}) if m.type == "error" else None)
    page.on("framenavigated", lambda f: navs.append(f.url) if f == page.main_frame else None)
    capture(page, posts, ("calc__FORM.php",))
    page.goto(f"{SITE}/", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(6500)
    page.evaluate(
        """() => {
          const $ = window.jQuery;
          if (!$) return;
          for (let i = 1; i <= 5; i++) {
            const name = 'radio_st_0' + i;
            const inp = document.querySelector('input[name="'+name+'"]');
            if (inp) inp.checked = true;
          }
          if (typeof handleCalcStage === 'function') handleCalcStage(5);
        }"""
    )
    page.wait_for_timeout(500)
    f = page.locator("#calculator__FORM, [id^='calculator__FORM']").first
    fill_common(f, name=f"FSA HOMECALC {STAMP}", phone=PHONE)
    if page.locator(".calculator_stage__btns .submit").count():
        page.locator(".calculator_stage__btns .submit").first.click(force=True)
    page.wait_for_timeout(5500)
    resp = next((p for p in posts if p.get("phase") == "resp"), None)
    req = next((p for p in posts if p.get("phase") == "req"), None)
    out = {
        "label": "homepage_calc",
        "request_url": req.get("url") if req else None,
        "http": resp.get("status") if resp else None,
        "body": resp.get("body") if resp else None,
        "success_ui": ui_success(page),
        "page_reload": len(navs) > 1,
        "console_errors": console[:8],
    }
    out["pass"] = out["body"] == "true" and out["success_ui"] and not out["page_reload"]
    page.close()
    return out


def main() -> None:
    SHOT.mkdir(parents=True, exist_ok=True)
    report: dict = {"started_utc": utc_now(), "stamp": STAMP, "browser": [], "mail": [], "negative": []}
    sftp, transport = _v.sftp_connect()
    test_mode_on = False
    try:
        report["cfg_before"] = _v.cfg_snapshot(sftp)
        report["test_mode_on"] = _v.set_test_mode(sftp, True)
        test_mode_on = True
        report["cfg_during"] = _v.cfg_snapshot(sftp)

        # Browser first. Burst is 3/5min per form_id — do not pre-burn with synthetic POSTs.

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            report["browser"].append(
                browser_submit(
                    browser,
                    label="homepage_main",
                    url=f"{SITE}/",
                    form_sel="#page__FORM",
                    btn_sel="#page__FORM_send",
                    needles=("page__FORM.php",),
                )
            )
            report["browser"].append(
                browser_submit(
                    browser,
                    label="homepage_audit_modal",
                    url=f"{SITE}/",
                    form_sel="#audit__FORM",
                    btn_sel="#audit__FORM_send",
                    open_sel='a[href="#audit__FORM_popup"]',
                    needles=("audit__FORM.php",),
                )
            )
            report["browser"].append(run_homepage_calc(browser))
            report["browser"].append(run_calculator(browser, label="seo_calculator", url=f"{SITE}/services/seo.html"))
            report["browser"].append(run_calculator(browser, label="tariff_calculator", url=f"{SITE}/tariff-calc"))
            # page burst slot 2: nested SEO proves root-relative endpoint
            report["browser"].append(
                browser_submit(
                    browser,
                    label="nested_seo_page",
                    url=f"{SITE}/services/seo/prodvizhenie-sajta-restorana.html",
                    form_sel="#page__FORM_seo",
                    btn_sel="#page__FORM_send_seo",
                    needles=("page__FORM.php",),
                )
            )
            # Nested callback: inspect root-relative URL without a 4th callback accept.
            nest = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
            nest.goto(
                f"{SITE}/services/seo/prodvizhenie-sajta-restorana.html",
                wait_until="domcontentloaded",
                timeout=60000,
            )
            nest.wait_for_timeout(2500)
            report["nested_callback_js_url"] = nest.evaluate(
                """() => {
                  try {
                    const $ = jQuery;
                    const btn = document.getElementById('callback__FORM_send_seo');
                    const clicks = (btn && $ && ($._data(btn,'events')||{}).click) || [];
                    return clicks.map(h => {
                      const s = String(h.handler);
                      const m = s.match(/url:\\s*['\"]([^'\"]+__FORM\\.php)['\"]/);
                      return {has_prevent: s.indexOf('preventDefault')>=0, url: m && m[1]};
                    });
                  } catch(e) { return String(e); }
                }"""
            )
            nest.close()
            report["family_inspect"] = []
            for lab, href in [
                ("city", f"{SITE}/services/seo/prodvizhenie-v-sankt-peterburge.html"),
                ("usa", f"{SITE}/services/seo/prodvizhenie-v-ssha.html"),
                ("webinar", f"{SITE}/webinar-seo-podryadchik.html"),
                ("cases", f"{SITE}/cases.html"),
            ]:
                pg = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
                pg.goto(href, wait_until="domcontentloaded", timeout=60000)
                pg.wait_for_timeout(2000)
                report["family_inspect"].append(
                    {
                        "label": lab,
                        "url": href,
                        "has_page_form": pg.evaluate(
                            "() => !!(document.querySelector('#page__FORM_seo, #page__FORM, #page__FORM_cases'))"
                        ),
                        "consent": pg.evaluate(
                            "() => !!document.querySelector('form input[name=personal_data_consent]')"
                        ),
                        "send_seo": pg.evaluate(
                            "() => !!(document.getElementById('page__FORM_send_seo') || document.getElementById('page__FORM_send') || document.getElementById('page__FORM_send_cases'))"
                        ),
                        "cf_contact_latin": pg.evaluate(
                            "() => !!(document.querySelector('[name=cf_contact]') && !document.getElementById('сf_contact'))"
                        ),
                    }
                )
                pg.close()
            # page burst slot 3: blog.html consent repair
            report["browser"].append(
                browser_submit(
                    browser,
                    label="blog_html",
                    url=f"{SITE}/blog.html",
                    form_sel="#page__FORM_info",
                    btn_sel="#page__FORM_send_info",
                    needles=("page__FORM.php",),
                )
            )
            report["browser"].append(
                browser_submit(
                    browser,
                    label="blog_wp_footer_callback",
                    url=f"{SITE}/blog/",
                    form_sel="#callback__FORM_info",
                    btn_sel="#callback__FORM_send_info",
                    open_sel='a[href="#callback__FORM_popup"]',
                    needles=("callback__FORM.php",),
                )
            )
            report["browser"].append(
                browser_submit(
                    browser,
                    label="career",
                    url=f"{SITE}/career.html",
                    form_sel="#career__FORM_info",
                    btn_sel="#career__FORM_send_info",
                    open_sel='a[href="#career__FORM_popup"]',
                    needles=("career__FORM.php",),
                )
            )
            report["browser"].append(
                browser_submit(
                    browser,
                    label="partners",
                    url=f"{SITE}/partners.html",
                    form_sel="#partners_page__FORM_info",
                    btn_sel="#partners_page__FORM_send_info",
                    needles=("partners__FORM.php",),
                )
            )
            report["browser"].append(
                browser_submit(
                    browser,
                    label="reviews",
                    url=f"{SITE}/reviews.html",
                    form_sel="#review_page__FORM_info",
                    btn_sel="#review_page__FORM_send_info",
                    needles=("review__FORM.php",),
                )
            )
            report["browser"].append(
                browser_submit(
                    browser,
                    label="bonuses",
                    url=f"{SITE}/bonuses.html",
                    form_sel="#bonus__FORM",
                    btn_sel="#bonus__FORM_send",
                    open_sel='a[href="#bonus__FORM_popup"]',
                    needles=("bonus__FORM.php",),
                )
            )
            report["browser"].append(
                browser_submit(
                    browser,
                    label="nested_tariff1_modal",
                    url=f"{SITE}/services/seo.html",
                    form_sel="#tariff_1__FORM_seo",
                    btn_sel="#tariff_1__FORM_send_seo",
                    open_sel='a[href="#tariff_1__FORM_popup"], a[href="#tariff_1__FORM_seo_popup"]',
                    needles=("tariff_1__FORM.php",),
                )
            )
            # responsive snapshots of key UIs (no extra mail)
            for label, href, w, h in [
                ("home_390", f"{SITE}/", 390, 844),
                ("seo_390", f"{SITE}/services/seo.html", 390, 844),
                ("webinar_390", f"{SITE}/webinar-seo-podryadchik.html", 390, 844),
            ]:
                pg = browser.new_page(viewport={"width": w, "height": h}, user_agent=UA)
                pg.goto(href, wait_until="domcontentloaded", timeout=60000)
                pg.wait_for_timeout(2500)
                pg.screenshot(path=str(SHOT / f"responsive-{label}.png"), full_page=False)
                pg.close()
            browser.close()

        for b in report["browser"]:
            if b.get("body") == "true":
                hid = LABEL_TO_HANDLER.get(b.get("label"), b.get("label"))
                report["mail"].append(
                    {
                        "handler": hid,
                        "source": "browser",
                        "label": b.get("label"),
                        "http_status": b.get("http"),
                        "body": "true",
                        "recipient": "im.work@mail.ru",
                    }
                )
        covered = {m["handler"] for m in report["mail"]}
        for hid, spec in HANDLERS.items():
            if hid in covered:
                continue
            row = post_handler(spec["url"], spec["fields"], f"{SITE}/?fsa={hid}")
            row["handler"] = hid
            row["source"] = "synthetic_uncovered"
            row["recipient"] = "im.work@mail.ru"
            report["mail"].append(row)
            time.sleep(0.4)
        for n in (1, 2, 3, 4):
            hid = f"tariff_{n}"
            if hid in covered:
                continue
            fields = {
                "cf_name": f"FSA T{n} {STAMP}",
                "cf_contact": "Телефон",
                "cf_phone": PHONE,
                "cf_site": "",
                "cf_site_no": "",
                "personal_data_consent": "1",
            }
            row = post_handler(f"{SITE}/tariff_{n}__FORM.php", fields, f"{SITE}/?fsa=t{n}")
            row["handler"] = hid
            row["source"] = "synthetic_uncovered"
            row["recipient"] = "im.work@mail.ru"
            report["mail"].append(row)
            covered.add(hid)
            time.sleep(0.4)
        report["events_after_mail"] = _v.tail_events(sftp, 20)

        # page burst was used by 3 browser accepts; wait for window before consent-reject matrix
        report["negative_wait_sec"] = 310
        time.sleep(310)

        # Negative matrix on page handler (after positives)
        tok = json.loads(
            urllib.request.urlopen(
                urllib.request.Request(TOKEN_URL, headers={"User-Agent": UA}), timeout=30
            ).read().decode("utf-8")
        )
        time.sleep(3.3)
        base = {
            "contact_company_url": "",
            "iseo_ft": tok["t"],
            "iseo_fs": tok["s"],
            "iseo_fid": tok["id"],
            "pf_page_title": f"FSA NEG {STAMP}",
            "pf_page_link": f"{SITE}/",
            "pf_name": f"FSA NEG {STAMP}",
            "pf_contact": "WhatsApp",
            "pf_phone": PHONE,
            "pf_site": "",
            "pf_comment": "neg",
        }
        for case, extra in [
            ("missing_consent", {}),
            ("consent_0", {"personal_data_consent": "0"}),
            ("consent_bad", {"personal_data_consent": "yes"}),
            ("honeypot", {"personal_data_consent": "1", "contact_company_url": "http://spam.test"}),
        ]:
            data = dict(base)
            data.update(extra)
            body = urllib.parse.urlencode(data).encode("utf-8")
            req = urllib.request.Request(
                f"{SITE}/page__FORM.php",
                data=body,
                method="POST",
                headers={"Content-Type": "application/x-www-form-urlencoded", "User-Agent": UA},
            )
            try:
                with urllib.request.urlopen(req, timeout=45) as resp:
                    report["negative"].append(
                        {"case": case, "http": resp.status, "body": resp.read().decode("utf-8", "replace").strip()}
                    )
            except urllib.error.HTTPError as e:
                report["negative"].append(
                    {"case": case, "http": e.code, "body": e.read().decode("utf-8", "replace").strip()}
                )
            time.sleep(0.3)
        # too_fast: reuse fresh token immediately
        tok2 = json.loads(
            urllib.request.urlopen(
                urllib.request.Request(TOKEN_URL, headers={"User-Agent": UA}), timeout=30
            ).read().decode("utf-8")
        )
        data = dict(base)
        data.update(
            {
                "personal_data_consent": "1",
                "iseo_ft": tok2["t"],
                "iseo_fs": tok2["s"],
                "iseo_fid": tok2["id"],
            }
        )
        body = urllib.parse.urlencode(data).encode("utf-8")
        req = urllib.request.Request(
            f"{SITE}/page__FORM.php",
            data=body,
            method="POST",
            headers={"Content-Type": "application/x-www-form-urlencoded", "User-Agent": UA},
        )
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                report["negative"].append(
                    {"case": "too_fast", "http": resp.status, "body": resp.read().decode("utf-8", "replace").strip()}
                )
        except urllib.error.HTTPError as e:
            report["negative"].append(
                {"case": "too_fast", "http": e.code, "body": e.read().decode("utf-8", "replace").strip()}
            )

        report["events_final_during"] = _v.tail_events(sftp, 12)
    except Exception as exc:  # noqa: BLE001
        report["crash"] = str(exc)
    finally:
        if test_mode_on:
            report["test_mode_off"] = _v.set_test_mode(sftp, False)
        report["cfg_final"] = _v.cfg_snapshot(sftp)
        sftp.close()
        transport.close()
        report["finished_utc"] = utc_now()
        mail_true = sum(1 for m in report["mail"] if m.get("body") == "true")
        browser_pass = sum(1 for b in report["browser"] if b.get("pass"))
        report["summary"] = {
            "mail_true": mail_true,
            "mail_total": len(report["mail"]),
            "browser_pass": browser_pass,
            "browser_total": len(report["browser"]),
            "test_mode_final": report.get("cfg_final", {}).get("test_mode"),
            "prod_has_nikel": report.get("cfg_final", {}).get("prod_has_nikel"),
            "prod_has_im_work": report.get("cfg_final", {}).get("prod_has_im_work"),
            "crash": report.get("crash"),
        }
        OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    print("browser", [(b.get("label"), b.get("body"), b.get("pass"), b.get("request_url")) for b in report["browser"]])
    print("mail", [(m.get("handler"), m.get("body"), m.get("source")) for m in report["mail"]])
    print("negative", report["negative"])
    print("cfg_final", report.get("cfg_final"))
    if report.get("crash"):
        raise SystemExit(f"CRASH: {report['crash']}")


if __name__ == "__main__":
    main()
