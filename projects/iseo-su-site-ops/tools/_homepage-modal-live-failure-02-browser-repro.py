#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISEO-SU-SITE-OPS-HOMEPAGE-MODAL-LIVE-FAILURE-02 — real-browser repro (pre-fix)."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

OUT = Path(
    r"X:\AI MARS\projects\iseo-su-site-ops\evidence\homepage-modal-live-failure-02\_browser-repro-before.json"
)
HOME = "https://i-seo.su/"
UA = "ISEO-SU-HOMEPAGE-MODAL-LIVE-FAILURE-02/1.0"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def inventory(page) -> dict:
    return page.evaluate(
        """() => {
      const popup = document.getElementById('audit__FORM_popup');
      const form = document.getElementById('audit__FORM');
      const title = popup ? (popup.querySelector('.callback_form__title') || {}).textContent : null;
      const fields = form
        ? [...form.querySelectorAll('input,select,textarea,button')].map(el => ({
            tag: el.tagName.toLowerCase(),
            name: el.getAttribute('name'),
            id: el.id || null,
            type: el.getAttribute('type'),
            required: el.hasAttribute('required'),
            placeholder: el.getAttribute('placeholder')
          }))
        : null;
      let audit_handler = null;
      try {
        const $ = window.jQuery;
        const btn = document.getElementById('audit__FORM_send');
        const ev = btn && $ ? ($._data(btn, 'events') || {}) : {};
        const clicks = ev.click || [];
        audit_handler = {
          click_count: clicks.length,
          has_preventDefault: clicks.some(h => String(h.handler).includes('preventDefault')),
          has_return_false: clicks.some(h => String(h.handler).includes('return false')),
          src_preview: clicks.map(h => String(h.handler).slice(0, 280))
        };
      } catch (e) {
        audit_handler = { error: String(e) };
      }
      const site = form ? form.querySelector('input[name="af_site"]') : null;
      return {
        modal_title: title ? title.trim() : null,
        form_id: form ? form.id : null,
        form_action: form ? form.getAttribute('action') : null,
        form_method: form ? form.getAttribute('method') : null,
        submit_id: document.getElementById('audit__FORM_send')
          ? 'audit__FORM_send'
          : null,
        fields,
        site_required_attr: site ? site.hasAttribute('required') : null,
        site_required_prop: site ? !!site.required : null,
        audit_handler,
        common_js_src: [...document.scripts]
          .map(s => s.src)
          .filter(s => /common\\.js/i.test(s))
      };
    }"""
    )


def run_case(
    browser,
    *,
    label: str,
    phone: str,
    site_filled: bool,
    message: str,
) -> dict:
    console: list = []
    posts: list = []
    navs: list = []
    page = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
    page.on("console", lambda m: console.append({"type": m.type, "text": m.text}))
    page.on(
        "request",
        lambda r: posts.append(
            {"phase": "req", "url": r.url, "method": r.method, "post": r.post_data}
        )
        if r.method == "POST" and "FORM.php" in r.url
        else None,
    )

    def on_response(resp):
        if resp.request.method == "POST" and "FORM.php" in resp.url:
            try:
                body = resp.text().strip()
            except Exception as exc:  # noqa: BLE001
                body = f"READ_FAIL:{exc}"
            posts.append(
                {
                    "phase": "resp",
                    "url": resp.url,
                    "status": resp.status,
                    "ct": resp.headers.get("content-type"),
                    "body": body,
                }
            )

    page.on("response", on_response)
    page.on("framenavigated", lambda f: navs.append(f.url) if f == page.main_frame else None)

    page.goto(HOME, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(4000)
    inv = inventory(page)

    opened = page.evaluate(
        """() => {
          const a = document.querySelector('a[href="#audit__FORM_popup"]');
          if (a) { a.click(); return a.getAttribute('href'); }
          return null;
        }"""
    )
    page.wait_for_timeout(1500)

    form = page.locator("#audit__FORM")
    form.locator("#af_name").fill("TEST MARS")
    form.locator("select[name='af_contact']").select_option("WhatsApp")
    form.locator("#af_phone").fill(phone)
    if site_filled:
        form.locator("#af_site").fill("https://example-mars-modal-live-failure-02.test")
    else:
        form.locator("#af_site").fill("")
    if form.locator("#af_comment").count():
        form.locator("#af_comment").fill(message)
    form.locator("input[name='personal_data_consent']").first.check(force=True)

    js_probe = page.evaluate(
        """() => {
          const f = jQuery('#audit__FORM');
          const before = checkEmptyFields(f);
          const site = f.find('input[name="af_site"]');
          return {
            checkEmptyFields: before,
            site_error: site.hasClass('error'),
            site_required: !!site.prop('required'),
            data_errors: f.attr('data-errors')
          };
        }"""
    )

    url_before = page.url
    nav_before = len(navs)
    page.locator("#audit__FORM_send").click(force=True)
    page.wait_for_timeout(4500)

    success_ui = page.evaluate(
        """() => {
          const wrap = document.querySelector('#audit__FORM_popup, .fancybox-inner, .fancybox-content') || document.body;
          const txt = wrap.innerText || '';
          return {
            success: /Успешно|Сообщение отправлено/i.test(txt),
            generic_error: /Не удалось отправить заявку/i.test(txt),
            busy_or_error_html: !!document.querySelector('.iseo-form-error, #audit__FORM_popup em, .fancybox-inner em'),
            visible_snippet: txt.slice(0, 400)
          };
        }"""
    )

    form_posts = [p for p in posts if "audit__FORM.php" in p.get("url", "")]
    resp = next((p for p in form_posts if p.get("phase") == "resp"), None)
    req = next((p for p in form_posts if p.get("phase") == "req"), None)

    page.close()
    return {
        "label": label,
        "opened_href": opened,
        "inventory": inv,
        "js_probe": js_probe,
        "phone": phone,
        "site_filled": site_filled,
        "request_sent": req is not None,
        "request_url": req.get("url") if req else None,
        "method": req.get("method") if req else None,
        "post_payload": req.get("post") if req else None,
        "http_status": resp.get("status") if resp else None,
        "response_body": resp.get("body") if resp else None,
        "page_reload": (len(navs) - nav_before) > 1,
        "nav_count": len(navs) - nav_before,
        "url_before": url_before,
        "success_ui": success_ui,
        "console": [c for c in console if c["type"] in ("error", "warning")][:20],
        "all_form_posts": form_posts,
    }


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    report: dict = {"started": utc_now(), "cases": []}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # A: blank site + structurally valid phone (operator path)
        report["cases"].append(
            run_case(
                browser,
                label="blank_site_valid_phone",
                phone="+7 (999) 123-45-67",
                site_filled=False,
                message="TEST HOMEPAGE MODAL — DO NOT PROCESS",
            )
        )
        # B: filled site + operator-style repeated phone
        report["cases"].append(
            run_case(
                browser,
                label="filled_site_operator_phone",
                phone="+7 (111) 111-11-11",
                site_filled=True,
                message="TEST HOMEPAGE MODAL PHONE B — DO NOT PROCESS",
            )
        )
        browser.close()
    report["ended"] = utc_now()
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"out": str(OUT), "n": len(report["cases"])}, ensure_ascii=False))
    for c in report["cases"]:
        print(
            c["label"],
            "sent=",
            c["request_sent"],
            "url=",
            c["request_url"],
            "http=",
            c["http_status"],
            "body=",
            c["response_body"],
            "err=",
            (c["success_ui"] or {}).get("generic_error"),
            "ok=",
            (c["success_ui"] or {}).get("success"),
        )


if __name__ == "__main__":
    main()
