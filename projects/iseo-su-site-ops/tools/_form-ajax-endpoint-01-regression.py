#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISEO-SU-SITE-OPS-FORM-AJAX-ENDPOINT-01: bounded functional + security regression.

Honeypot/consent negatives first. Isolated test_mode for valid UI submits.
Always restores test_mode OFF.
"""
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

EVIDENCE = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-ajax-endpoint-01")
OUT = EVIDENCE / "_regression.json"
UA = "ISEO-SU-FORM-AJAX-ENDPOINT-01/1.0"
HOME = "https://i-seo.su/"
WEBINAR = "https://i-seo.su/webinar-seo-podryadchik.html"
RESTAURANT = "https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html"
CITY = "https://i-seo.su/services/seo/prodvizhenie-v-novosibirske.html"
NICHE = "https://i-seo.su/services/seo/prodvizhenie-internet-magazina-kosmetiki.html"
SEO_HUB = "https://i-seo.su/services/seo.html"
EXPECTED_POST = "https://i-seo.su/page__FORM.php"

cfg_snapshot = _v.cfg_snapshot
set_test_mode = _v.set_test_mode
sftp_connect = _v.sftp_connect
tail_events = _v.tail_events
page_contract_get = _v.page_contract_get
post_handler = _v.post_handler
restaurant_base = _v.restaurant_base


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _attach_post_capture(page, posted: dict) -> None:
    def on_request(req):
        if "page__FORM.php" in req.url and req.method == "POST":
            posted["url"] = req.url
            posted["method"] = req.method
            posted["post_data"] = req.post_data or ""

    def on_response(resp):
        if "page__FORM.php" in resp.url and resp.request.method == "POST":
            posted["status"] = resp.status
            try:
                posted["body"] = resp.text().strip()
            except Exception as exc:  # noqa: BLE001
                posted["body"] = f"READ_FAIL:{exc}"

    page.on("request", on_request)
    page.on("response", on_response)


def _fill_seo(form, page, name: str, phone: str, *, consent: bool, honeypot: str | None) -> None:
    form.scroll_into_view_if_needed()
    form.locator("#pf_name").fill(name)
    phone_el = form.locator("input[name='pf_phone']")
    if phone_el.count():
        phone_el.fill(phone)
    elif form.locator("#pf_contact").count():
        form.locator("#pf_contact").fill(phone)
    if form.locator("input[name='pf_site']").count():
        site_el = form.locator("input[name='pf_site']")
        if site_el.get_attribute("type") != "hidden":
            site_el.fill("https://example-ajax-endpoint-01.test")
    if form.locator("#pf_comment").count():
        form.locator("#pf_comment").fill("SYNTHETIC AJAX ENDPOINT 01 — ignore")
    if form.locator("#cf_agree21").count():
        form.locator("#cf_agree21").check(force=True)
    consent_box = form.locator("input[name='personal_data_consent']")
    if consent and consent_box.count():
        consent_box.first.check(force=True)
    hp = form.locator("input[name='contact_company_url']")
    if hp.count() and honeypot:
        hp.fill(honeypot)


def _fill_home(form, name: str, phone: str, *, consent: bool, honeypot: str | None) -> None:
    form.scroll_into_view_if_needed()
    form.locator("#pf_name").fill(name)
    if form.locator("select[name='pf_contact']").count():
        form.locator("select[name='pf_contact']").select_option("WhatsApp")
    form.locator("#pf_phone").fill(phone)
    if form.locator("input[name='pf_site']").count():
        form.locator("input[name='pf_site']").fill("https://example-ajax-endpoint-01.test")
    if form.locator("#pf_comment").count():
        form.locator("#pf_comment").fill("SYNTHETIC AJAX ENDPOINT 01 — ignore")
    consent_box = form.locator("input[name='personal_data_consent']")
    if consent and consent_box.count():
        consent_box.first.check(force=True)
    hp = form.locator("input[name='contact_company_url']")
    if hp.count() and honeypot:
        hp.fill(honeypot)


def submit_case(spec: dict) -> dict:
    posted: dict = {}
    console = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
        page.on("console", lambda msg: console.append({"type": msg.type, "text": msg.text}))
        _attach_post_capture(page, posted)
        page.goto(spec["url"], wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(3500)
        form = page.locator("#" + spec["form_id"])
        if spec["form_id"] == "page__FORM":
            _fill_home(
                form,
                spec["name"],
                spec["phone"],
                consent=spec["consent"],
                honeypot=spec.get("honeypot"),
            )
        else:
            _fill_seo(
                form,
                page,
                spec["name"],
                spec["phone"],
                consent=spec["consent"],
                honeypot=spec.get("honeypot"),
            )
        page.wait_for_timeout(3500)
        try:
            with page.expect_response(lambda r: "page__FORM.php" in r.url, timeout=20000):
                page.click("#" + spec["button_id"])
            page.wait_for_timeout(2000)
        except Exception as exc:  # noqa: BLE001
            posted["wait_error"] = str(exc)
            page.wait_for_timeout(4000)
        success = page.locator("text=Успешно! Сообщение отправлено").count() > 0
        fail = page.locator("text=Не удалось отправить заявку").count() > 0
        browser.close()
    return {
        "case": spec["case"],
        "page_url": spec["url"],
        "post_url": posted.get("url"),
        "canonical_post": posted.get("url") == EXPECTED_POST,
        "status": posted.get("status"),
        "body": posted.get("body"),
        "success_ui": success,
        "fail_ui": fail,
        "wait_error": posted.get("wait_error"),
        "console_errors": [c for c in console if c["type"] == "error"],
        "consent_posted": "personal_data_consent=1" in (posted.get("post_data") or ""),
        "honeypot_posted": "contact_company_url=https%3A%2F%2Fhoneypot.invalid"
        in (posted.get("post_data") or "")
        or "contact_company_url=https://honeypot.invalid" in (posted.get("post_data") or ""),
    }


def load_console(url: str) -> dict:
    console = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
        page.on("console", lambda msg: console.append({"type": msg.type, "text": msg.text}))
        page.goto(url, wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(1500)
        form_ok = page.locator("#page__FORM, #page__FORM_seo").count() > 0
        browser.close()
    return {
        "url": url,
        "form_present": form_ok,
        "console_errors": [c for c in console if c["type"] == "error"],
    }


def main() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    report: dict = {
        "task": "ISEO-SU-SITE-OPS-FORM-AJAX-ENDPOINT-01",
        "started": utc_now(),
        "stamp": stamp,
    }
    sftp, transport = sftp_connect()
    test_mode_touched = False
    try:
        report["cfg_before"] = cfg_snapshot(sftp)
        report["seo_gets"] = {
            "home": page_contract_get(HOME),
            "webinar": page_contract_get(WEBINAR),
            "restaurant": page_contract_get(RESTAURANT),
            "city": page_contract_get(CITY),
            "niche": page_contract_get(NICHE),
            "seo_hub": page_contract_get(SEO_HUB),
        }

        report["neg_honeypot"] = submit_case(
            {
                "case": "honeypot",
                "url": RESTAURANT,
                "form_id": "page__FORM_seo",
                "button_id": "page__FORM_send_seo",
                "name": f"AJAX EP HP {stamp}",
                "phone": f"+7988{stamp[-7:]}",
                "consent": True,
                "honeypot": "https://honeypot.invalid",
            }
        )

        report["neg_consent"] = submit_case(
            {
                "case": "consent_missing",
                "url": RESTAURANT,
                "form_id": "page__FORM_seo",
                "button_id": "page__FORM_send_seo",
                "name": f"AJAX EP NC {stamp}",
                "phone": f"+7987{stamp[-7:]}",
                "consent": False,
                "honeypot": None,
            }
        )
        report["events_after_negatives"] = tail_events(sftp, 6)
        missing_consent = restaurant_base(stamp)
        del missing_consent["personal_data_consent"]
        report["neg_consent_server"] = post_handler(missing_consent, RESTAURANT)

        test_mode_touched = True
        report["test_mode_on"] = set_test_mode(sftp, True)

        valids = []
        wave1 = [
            {
                "case": "valid_webinar",
                "url": WEBINAR,
                "form_id": "page__FORM_seo",
                "button_id": "page__FORM_send_seo",
                "name": f"AJAX EP WB {stamp}",
                "phone": f"+7981{stamp[-7:]}",
                "consent": True,
                "honeypot": None,
            },
            {
                "case": "valid_restaurant",
                "url": RESTAURANT,
                "form_id": "page__FORM_seo",
                "button_id": "page__FORM_send_seo",
                "name": f"AJAX EP RS {stamp}",
                "phone": f"+7982{stamp[-7:]}",
                "consent": True,
                "honeypot": None,
            },
        ]
        for spec in wave1:
            valids.append(submit_case(spec))
            report["valid_submits"] = valids
            OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
            time.sleep(2)

        report["rate_limit_pause_seconds"] = 310
        report["pause_started"] = utc_now()
        time.sleep(310)
        report["pause_ended"] = utc_now()

        wave2 = [
            {
                "case": "valid_city",
                "url": CITY,
                "form_id": "page__FORM_seo",
                "button_id": "page__FORM_send_seo",
                "name": f"AJAX EP CY {stamp}",
                "phone": f"+7983{stamp[-7:]}",
                "consent": True,
                "honeypot": None,
            },
            {
                "case": "valid_niche",
                "url": NICHE,
                "form_id": "page__FORM_seo",
                "button_id": "page__FORM_send_seo",
                "name": f"AJAX EP NI {stamp}",
                "phone": f"+7984{stamp[-7:]}",
                "consent": True,
                "honeypot": None,
            },
            {
                "case": "valid_home",
                "url": HOME,
                "form_id": "page__FORM",
                "button_id": "page__FORM_send",
                "name": f"AJAX EP HM {stamp}",
                "phone": f"+7985{stamp[-7:]}",
                "consent": True,
                "honeypot": None,
            },
        ]
        for spec in wave2:
            valids.append(submit_case(spec))
            report["valid_submits"] = valids
            OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
            time.sleep(2)
        report["valid_submits"] = valids
        report["events_after_valids"] = tail_events(sftp, 10)

        report["shared_js_console"] = [
            load_console(HOME),
            load_console(SEO_HUB),
            load_console(RESTAURANT),
            load_console(WEBINAR),
        ]

        report["test_mode_off"] = set_test_mode(sftp, False)
        test_mode_touched = False
        report["cfg_final"] = cfg_snapshot(sftp)
        report["ended"] = utc_now()
        OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        summary = {
            "out": str(OUT),
            "honeypot_body": report["neg_honeypot"].get("body"),
            "consent_body": report["neg_consent"].get("body"),
            "valid_bodies": [v.get("body") for v in valids],
            "valid_urls": [v.get("post_url") for v in valids],
            "cfg_final": report["cfg_final"],
        }
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0
    except Exception:
        if test_mode_touched:
            try:
                report["test_mode_off_on_error"] = set_test_mode(sftp, False)
            except Exception as restore_exc:  # noqa: BLE001
                report["test_mode_restore_error"] = str(restore_exc)
        report["ended"] = utc_now()
        OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        raise
    finally:
        sftp.close()
        transport.close()


if __name__ == "__main__":
    raise SystemExit(main())
