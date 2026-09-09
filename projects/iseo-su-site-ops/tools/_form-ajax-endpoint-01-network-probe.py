#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISEO-SU-SITE-OPS-FORM-AJAX-ENDPOINT-01: live URL-resolution + honeypot POST capture.

Honeypot is filled so the handler REJECTS and does not send production mail.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

EVIDENCE = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-ajax-endpoint-01")
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else EVIDENCE / "_network-probe.json"
UA = "ISEO-SU-FORM-AJAX-ENDPOINT-01/1.0"

PAGES = [
    {
        "name": "HOME",
        "url": "https://i-seo.su/",
        "form_id": "page__FORM",
        "button_id": "page__FORM_send",
        "family": "homepage #page__FORM",
        "phone_selector": "#page__FORM #pf_phone",
        "has_contact_select": True,
        "has_cf_agree": False,
        "has_site": True,
    },
    {
        "name": "WEBINAR",
        "url": "https://i-seo.su/webinar-seo-podryadchik.html",
        "form_id": "page__FORM_seo",
        "button_id": "page__FORM_send_seo",
        "family": "seo #page__FORM_seo",
        "phone_selector": "#page__FORM_seo input[name='pf_phone']",
        "has_contact_select": False,
        "has_cf_agree": False,
        "has_site": False,
    },
    {
        "name": "RESTAURANT",
        "url": "https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html",
        "form_id": "page__FORM_seo",
        "button_id": "page__FORM_send_seo",
        "family": "seo #page__FORM_seo",
        "phone_selector": "#page__FORM_seo input[name='pf_phone']",
        "has_contact_select": False,
        "has_cf_agree": True,
        "has_site": True,
    },
    {
        "name": "CITY",
        "url": "https://i-seo.su/services/seo/prodvizhenie-v-novosibirske.html",
        "form_id": "page__FORM_seo",
        "button_id": "page__FORM_send_seo",
        "family": "seo #page__FORM_seo",
        "phone_selector": "#page__FORM_seo input[name='pf_phone']",
        "has_contact_select": False,
        "has_cf_agree": True,
        "has_site": True,
    },
    {
        "name": "NICHE",
        "url": "https://i-seo.su/services/seo/prodvizhenie-internet-magazina-kosmetiki.html",
        "form_id": "page__FORM_seo",
        "button_id": "page__FORM_send_seo",
        "family": "seo #page__FORM_seo",
        "phone_selector": "#page__FORM_seo input[name='pf_phone']",
        "has_contact_select": False,
        "has_cf_agree": True,
        "has_site": True,
    },
    {
        "name": "USA",
        "url": "https://i-seo.su/services/seo/prodvizhenie-v-ssha.html",
        "form_id": "page__FORM_seo",
        "button_id": "page__FORM_send_seo",
        "family": "seo #page__FORM_seo",
        "phone_selector": "#page__FORM_seo input[name='pf_phone']",
        "has_contact_select": False,
        "has_cf_agree": True,
        "has_site": True,
    },
    {
        "name": "UAE",
        "url": "https://i-seo.su/services/seo/prodvizhenie-v-oae.html",
        "form_id": "page__FORM_seo",
        "button_id": "page__FORM_send_seo",
        "family": "seo #page__FORM_seo",
        "phone_selector": "#page__FORM_seo input[name='pf_phone']",
        "has_contact_select": False,
        "has_cf_agree": True,
        "has_site": True,
    },
]


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def probe_page(page, spec: dict) -> dict:
    posted: dict = {}
    console = []
    page.on("console", lambda msg: console.append({"type": msg.type, "text": msg.text}))

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
    page.goto(spec["url"], wait_until="domcontentloaded", timeout=45000)
    page.wait_for_timeout(1500)

    pre = page.evaluate(
        """() => {
            const scripts = Array.from(document.scripts)
              .map(s => s.src)
              .filter(src => src.includes('common.js'));
            const form = document.getElementById(%r);
            return {
              location_href: location.href,
              base_uri: document.baseURI,
              base_href: document.querySelector('base') ? document.querySelector('base').href : null,
              common_js: scripts,
              form_present: !!form,
              form_action: form ? form.getAttribute('action') : null,
              resolved_relative: new URL('page__FORM.php', location.href).href,
              resolved_root_relative: new URL('/page__FORM.php', location.href).href
            };
        }"""
        % spec["form_id"]
    )

    form = page.locator("#" + spec["form_id"])
    form.scroll_into_view_if_needed()
    form.locator("#pf_name").fill("AJAX ENDPOINT AUDIT HONEYPOT")
    if spec["has_contact_select"] and form.locator("select[name='pf_contact']").count():
        form.locator("select[name='pf_contact']").select_option("WhatsApp")
    page.locator(spec["phone_selector"]).fill("+7 (988) 111-22-33")
    if spec["has_site"] and form.locator("input[name='pf_site']").count():
        site_el = form.locator("input[name='pf_site']")
        if site_el.get_attribute("type") != "hidden":
            site_el.fill("https://example-ajax-endpoint-audit.test")
    if form.locator("#pf_comment").count():
        form.locator("#pf_comment").fill("SYNTHETIC HONEYPOT — do not mail")
    if spec["has_cf_agree"] and form.locator("#cf_agree21").count():
        form.locator("#cf_agree21").check(force=True)
    consent = form.locator("input[name='personal_data_consent']")
    if consent.count():
        consent.first.check(force=True)
    hp = form.locator("input[name='contact_company_url']")
    if hp.count():
        hp.fill("https://honeypot.invalid")
        posted["honeypot_filled"] = True
    else:
        posted["honeypot_filled"] = False

    page.wait_for_timeout(3500)
    try:
        with page.expect_response(lambda r: "page__FORM.php" in r.url, timeout=20000):
            page.click("#" + spec["button_id"])
        page.wait_for_timeout(1500)
    except Exception as exc:  # noqa: BLE001
        posted["wait_error"] = str(exc)
        page.wait_for_timeout(4000)

    return {
        "page_name": spec["name"],
        "page_url": spec["url"],
        "form_family": spec["family"],
        "js_file": pre.get("common_js"),
        "endpoint_string_in_source": (
            "seo handler uses /page__FORM.php after fix; other families remain relative"
        ),
        "browser_pre_submit": pre,
        "network": {
            "url": posted.get("url"),
            "method": posted.get("method"),
            "status": posted.get("status"),
            "body": posted.get("body"),
            "honeypot_filled": posted.get("honeypot_filled"),
            "honeypot_posted": "contact_company_url=https%3A%2F%2Fhoneypot.invalid"
            in (posted.get("post_data") or "")
            or "contact_company_url=https://honeypot.invalid" in (posted.get("post_data") or ""),
            "wait_error": posted.get("wait_error"),
        },
        "console_errors": [c for c in console if c["type"] == "error"],
    }


def main() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for spec in PAGES:
            page = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
            try:
                results.append(probe_page(page, spec))
            except Exception as exc:  # noqa: BLE001
                results.append({"page_name": spec["name"], "page_url": spec["url"], "error": str(exc)})
            finally:
                page.close()
        browser.close()
    payload = {"started": utc_now(), "results": results, "ended": utc_now()}
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
