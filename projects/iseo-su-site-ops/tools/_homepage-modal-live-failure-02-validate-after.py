#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISEO-SU-HOMEPAGE-MODAL-LIVE-FAILURE-02 — browser retest + smoke (test_mode ON)."""
from __future__ import annotations

import importlib.util
import json
import time
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

_VALIDATE = Path(__file__).resolve().parent / "_form-contract-regression-01-validate.py"
_spec = importlib.util.spec_from_file_location("form_contract_validate", _VALIDATE)
_v = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_v)

EVIDENCE = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\homepage-modal-live-failure-02")
OUT = EVIDENCE / "_validation-after.json"
UA = "ISEO-SU-HOMEPAGE-MODAL-LIVE-FAILURE-02-AFTER/1.0"
HOME = "https://i-seo.su/"
WEBINAR = "https://i-seo.su/webinar-seo-podryadchik.html"
RESTAURANT = "https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html"
CITY = "https://i-seo.su/services/seo/prodvizhenie-v-novosibirske.html"
NICHE = "https://i-seo.su/services/seo/prodvizhenie-internet-magazina-kosmetiki.html"
SUFFIX = datetime.now(timezone.utc).strftime("%H%M%S")


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def capture(page, bag: list, needles: tuple[str, ...]) -> None:
    def on_request(req):
        if req.method == "POST" and any(x in req.url for x in needles):
            bag.append({"phase": "req", "url": req.url, "method": req.method, "post": req.post_data})

    def on_response(resp):
        if resp.request.method == "POST" and any(x in resp.url for x in needles):
            try:
                body = resp.text().strip()
            except Exception as exc:  # noqa: BLE001
                body = f"READ_FAIL:{exc}"
            bag.append(
                {
                    "phase": "resp",
                    "url": resp.url,
                    "status": resp.status,
                    "ct": resp.headers.get("content-type"),
                    "body": body,
                }
            )

    page.on("request", on_request)
    page.on("response", on_response)


def ui_state(page) -> dict:
    return page.evaluate(
        """() => {
          const txt = document.body.innerText || '';
          return {
            success: /Успешно! Сообщение отправлено/i.test(txt),
            generic_error: /Не удалось отправить заявку/i.test(txt),
            preventDefault_audit: (function(){
              try {
                const $ = jQuery;
                const btn = document.getElementById('audit__FORM_send');
                const clicks = (btn && $ && ($._data(btn,'events')||{}).click) || [];
                return clicks.some(h => String(h.handler).includes('preventDefault'));
              } catch(e) { return null; }
            })()
          };
        }"""
    )


def run_audit(browser, *, site_filled: bool, phone: str, name: str, msg: str) -> dict:
    posts: list = []
    navs: list = []
    console: list = []
    page = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
    page.on("console", lambda m: console.append({"type": m.type, "text": m.text}) if m.type == "error" else None)
    page.on("framenavigated", lambda f: navs.append(f.url) if f == page.main_frame else None)
    capture(page, posts, ("audit__FORM.php",))
    page.goto(HOME, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(6500)
    page.evaluate("""() => { const a=document.querySelector('a[href="#audit__FORM_popup"]'); if(a) a.click(); }""")
    page.wait_for_timeout(1200)
    f = page.locator("#audit__FORM")
    f.locator("#af_name").fill(name)
    f.locator("select[name='af_contact']").select_option("WhatsApp")
    f.locator("#af_phone").fill(phone)
    if site_filled:
        f.locator("#af_site").fill(f"https://example-modal-{SUFFIX}.test")
    else:
        f.locator("#af_site").fill("")
    f.locator("#af_comment").fill(msg)
    f.locator("input[name='personal_data_consent']").first.check(force=True)
    page.locator("#audit__FORM_send").click(force=True)
    page.wait_for_timeout(5000)
    body = next((p.get("body") for p in posts if p.get("phase") == "resp"), None)
    req = next((p for p in posts if p.get("phase") == "req"), None)
    ui = ui_state(page)
    out = {
        "case": "audit_modal",
        "site_filled": site_filled,
        "phone": phone,
        "request_url": req.get("url") if req else None,
        "http": next((p.get("status") for p in posts if p.get("phase") == "resp"), None),
        "body": body,
        "page_reload": len(navs) > 1,
        "nav_count": len(navs),
        "success_ui": ui["success"],
        "generic_error": ui["generic_error"],
        "preventDefault_audit": ui["preventDefault_audit"],
        "console_errors": console[:10],
        "posts": posts,
        "pass": body == "true" and ui["success"] and not ui["generic_error"] and len(navs) <= 1,
    }
    page.close()
    return out


def run_page_form(browser, *, url: str, label: str, phone: str, name: str, form_selector: str, button: str, open_modal: str | None = None) -> dict:
    posts: list = []
    navs: list = []
    console: list = []
    page = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
    page.on("console", lambda m: console.append({"type": m.type, "text": m.text}) if m.type == "error" else None)
    page.on("framenavigated", lambda f: navs.append(f.url) if f == page.main_frame else None)
    capture(page, posts, ("page__FORM.php", "callback__FORM.php", "audit__FORM.php"))
    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(6500)
    if open_modal:
        page.evaluate(f"() => {{ const a=document.querySelector('{open_modal}'); if(a) a.click(); }}")
        page.wait_for_timeout(1000)
    f = page.locator(form_selector)
    f.scroll_into_view_if_needed()
    # field mapping
    if form_selector == "#page__FORM":
        f.locator("#pf_name").fill(name)
        f.locator("select[name='pf_contact']").select_option("Telegram")
        f.locator("#pf_phone").fill(phone)
        f.locator("input[name='pf_site']").fill("")
        if f.locator("#pf_comment").count():
            f.locator("#pf_comment").fill(f"SMOKE {label} {SUFFIX} — DO NOT PROCESS")
    elif form_selector.endswith("_seo") or "page__FORM_seo" in form_selector:
        # SEO shared form: pf_name / hidden pf_contact / pf_phone
        # Do NOT clear hidden pf_site (often prefilled and not visible/editable).
        if f.locator("input[name='pf_name']").count():
            f.locator("input[name='pf_name']").fill(name)
        if f.locator("input[name='pf_phone']").count():
            f.locator("input[name='pf_phone']").fill(phone)
        if f.locator("textarea[name='pf_comment']").count():
            f.locator("textarea[name='pf_comment']").fill(f"SMOKE {label} {SUFFIX}")
    else:
        # generic try
        if f.locator("input[name='pf_name']").count():
            f.locator("input[name='pf_name']").fill(name)
        if f.locator("input[name='pf_phone']").count():
            f.locator("input[name='pf_phone']").fill(phone)
    consent = f.locator("input[name='personal_data_consent']")
    if consent.count():
        consent.first.check(force=True)
    page.locator(button).click(force=True)
    page.wait_for_timeout(5000)
    resp = next((p for p in posts if p.get("phase") == "resp"), None)
    req = next((p for p in posts if p.get("phase") == "req"), None)
    ui = ui_state(page)
    out = {
        "case": label,
        "url": url,
        "request_url": req.get("url") if req else None,
        "http": resp.get("status") if resp else None,
        "body": resp.get("body") if resp else None,
        "page_reload": len(navs) > 1,
        "success_ui": ui["success"],
        "generic_error": ui["generic_error"],
        "console_errors": console[:8],
        "posts": posts,
        "pass": (resp or {}).get("body") == "true" and len(navs) <= 1 and not ui["generic_error"],
    }
    page.close()
    return out


def run_consent_negative(browser) -> dict:
    posts: list = []
    page = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
    capture(page, posts, ("audit__FORM.php",))
    page.goto(HOME, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(4000)
    page.evaluate("""() => { const a=document.querySelector('a[href="#audit__FORM_popup"]'); if(a) a.click(); }""")
    page.wait_for_timeout(1000)
    f = page.locator("#audit__FORM")
    f.locator("#af_name").fill(f"ConsentNeg {SUFFIX}")
    f.locator("select[name='af_contact']").select_option("WhatsApp")
    f.locator("#af_phone").fill(f"+7909{SUFFIX[-6:]}")
    f.locator("#af_site").fill("")
    # leave consent unchecked
    blocked = page.evaluate(
        """() => {
          const form = jQuery('#audit__FORM');
          return checkEmptyFields(form);
        }"""
    )
    page.locator("#audit__FORM_send").click(force=True)
    page.wait_for_timeout(2000)
    out = {
        "case": "consent_negative",
        "checkEmptyFields": blocked,
        "request_sent": any(p.get("phase") == "req" for p in posts),
        "pass": blocked == "1" and not any(p.get("phase") == "req" for p in posts),
        "posts": posts,
    }
    page.close()
    return out


def main() -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    report: dict = {"started": utc_now(), "suffix": SUFFIX}
    sftp, transport = _v.sftp_connect()
    try:
        report["cfg_before"] = _v.cfg_snapshot(sftp)
        report["test_mode_on"] = _v.set_test_mode(sftp, True)
        time.sleep(1)
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            cases = []
            # Primary: audit blank + filled
            cases.append(
                run_audit(
                    browser,
                    site_filled=False,
                    phone=f"+7901{SUFFIX[-6:]}",
                    name=f"TEST MARS blank {SUFFIX}",
                    msg=f"TEST HOMEPAGE MODAL BLANK {SUFFIX} — DO NOT PROCESS",
                )
            )
            time.sleep(8)
            cases.append(
                run_audit(
                    browser,
                    site_filled=True,
                    phone=f"+7902{SUFFIX[-6:]}",
                    name=f"TEST MARS filled {SUFFIX}",
                    msg=f"TEST HOMEPAGE MODAL FILLED {SUFFIX} — DO NOT PROCESS",
                )
            )
            time.sleep(8)
            # Main homepage form
            cases.append(
                run_page_form(
                    browser,
                    url=HOME,
                    label="main_homepage",
                    phone=f"+7903{SUFFIX[-6:]}",
                    name=f"MainHome {SUFFIX}",
                    form_selector="#page__FORM",
                    button="#page__FORM_send",
                )
            )
            time.sleep(8)
            # Webinar (page form family)
            cases.append(
                run_page_form(
                    browser,
                    url=WEBINAR,
                    label="webinar",
                    phone=f"+7904{SUFFIX[-6:]}",
                    name=f"Webinar {SUFFIX}",
                    form_selector="#page__FORM_seo, #page__FORM",
                    button="#page__FORM_send_seo, #page__FORM_send",
                )
            )
            # page-family burst almost full — wait before more page accepts
            report["rate_wait_sec"] = 310
            time.sleep(310)
            cases.append(
                run_page_form(
                    browser,
                    url=RESTAURANT,
                    label="restaurant",
                    phone=f"+7905{SUFFIX[-6:]}",
                    name=f"Rest {SUFFIX}",
                    form_selector="#page__FORM_seo",
                    button="#page__FORM_send_seo",
                )
            )
            time.sleep(8)
            cases.append(
                run_page_form(
                    browser,
                    url=CITY,
                    label="city",
                    phone=f"+7906{SUFFIX[-6:]}",
                    name=f"City {SUFFIX}",
                    form_selector="#page__FORM_seo",
                    button="#page__FORM_send_seo",
                )
            )
            time.sleep(8)
            cases.append(
                run_page_form(
                    browser,
                    url=NICHE,
                    label="niche",
                    phone=f"+7907{SUFFIX[-6:]}",
                    name=f"Niche {SUFFIX}",
                    form_selector="#page__FORM_seo",
                    button="#page__FORM_send_seo",
                )
            )
            cases.append(run_consent_negative(browser))
            browser.close()
        report["cases"] = cases
        report["events_tail"] = _v.tail_events(sftp, 20)
        report["test_mode_off"] = _v.set_test_mode(sftp, False)
        report["cfg_final"] = _v.cfg_snapshot(sftp)
        report["ended"] = utc_now()
        report["summary"] = {c["case"] if "case" in c else c.get("label"): c.get("pass") for c in cases}
    except Exception:
        try:
            report["test_mode_off_on_error"] = _v.set_test_mode(sftp, False)
            report["cfg_final"] = _v.cfg_snapshot(sftp)
        except Exception as exc:  # noqa: BLE001
            report["test_mode_restore_error"] = str(exc)
        raise
    finally:
        sftp.close()
        transport.close()
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"out": str(OUT), "summary": report.get("summary"), "cfg_final": report.get("cfg_final")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
