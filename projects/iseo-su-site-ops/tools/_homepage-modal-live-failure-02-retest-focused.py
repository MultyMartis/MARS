#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Focused live retest after partial validation failures (UI timing + SEO smoke)."""
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
OUT = EVIDENCE / "_validation-focused-retest.json"
UA = "ISEO-SU-HOMEPAGE-MODAL-LIVE-FAILURE-02-FOCUSED/1.0"
HOME = "https://i-seo.su/"
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
                    "body": body,
                }
            )

    page.on("request", on_request)
    page.on("response", on_response)


def wait_success(page, timeout_ms: int = 2500) -> bool:
    try:
        page.wait_for_function(
            """() => /Успешно! Сообщение отправлено/i.test(document.body.innerText || '')""",
            timeout=timeout_ms,
        )
        return True
    except Exception:
        return False


def ui_flags(page) -> dict:
    return page.evaluate(
        """() => {
          const txt = document.body.innerText || '';
          return {
            success: /Успешно! Сообщение отправлено/i.test(txt),
            generic_error: /Не удалось отправить заявку/i.test(txt),
            form_hidden: (() => {
              const f = document.querySelector('#audit__FORM');
              if (!f) return null;
              const s = getComputedStyle(f);
              return s.display === 'none' || s.visibility === 'hidden' || f.offsetParent === null;
            })()
          };
        }"""
    )


def run_audit(browser, *, site_filled: bool, phone: str) -> dict:
    posts: list = []
    navs: list = []
    page = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
    page.on("framenavigated", lambda f: navs.append(f.url) if f == page.main_frame else None)
    capture(page, posts, ("audit__FORM.php",))
    page.goto(HOME, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(7000)
    page.evaluate("""() => { const a=document.querySelector('a[href=\"#audit__FORM_popup\"]'); if(a) a.click(); }""")
    page.wait_for_timeout(1200)
    f = page.locator("#audit__FORM")
    f.locator("#af_name").fill(f"TEST MARS {SUFFIX}")
    f.locator("select[name='af_contact']").select_option("WhatsApp")
    f.locator("#af_phone").fill(phone)
    f.locator("#af_site").fill(f"https://example-{SUFFIX}.test" if site_filled else "")
    f.locator("#af_comment").fill(f"FOCUSED RETEST site={'Y' if site_filled else 'N'} {SUFFIX} — DO NOT PROCESS")
    f.locator("input[name='personal_data_consent']").first.check(force=True)
    page.locator("#audit__FORM_send").click(force=True)
    success_seen = wait_success(page, 2500)
    page.wait_for_timeout(500)
    ui = ui_flags(page)
    body = next((p.get("body") for p in posts if p.get("phase") == "resp"), None)
    out = {
        "case": f"audit_blank" if not site_filled else "audit_filled",
        "site_filled": site_filled,
        "request_url": next((p.get("url") for p in posts if p.get("phase") == "req"), None),
        "http": next((p.get("status") for p in posts if p.get("phase") == "resp"), None),
        "body": body,
        "page_reload": len(navs) > 1,
        "success_ui_early": success_seen,
        "success_ui_late": ui["success"],
        "form_hidden": ui["form_hidden"],
        "generic_error": ui["generic_error"],
        "posts": posts,
        "pass": body == "true" and len(navs) <= 1 and not ui["generic_error"] and (success_seen or ui["form_hidden"]),
    }
    page.close()
    return out


def run_seo(browser, url: str, label: str, phone: str) -> dict:
    posts: list = []
    navs: list = []
    page = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
    page.on("framenavigated", lambda f: navs.append(f.url) if f == page.main_frame else None)
    capture(page, posts, ("page__FORM.php",))
    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(7500)
    f = page.locator("#page__FORM_seo")
    f.scroll_into_view_if_needed()
    f.locator("input[name='pf_name']").fill(f"{label} {SUFFIX}")
    f.locator("input[name='pf_phone']").fill(phone)
    if f.locator("input[name='pf_site']").count():
        # visible optional site — leave blank for smoke (optional)
        site = f.locator("input[name='pf_site']")
        if site.is_visible():
            site.fill("")
        else:
            pass
    if f.locator("textarea[name='pf_comment']").count():
        f.locator("textarea[name='pf_comment']").fill(f"SMOKE {label} {SUFFIX}")
    f.locator("input[name='personal_data_consent']").first.check(force=True)
    blocked = page.evaluate(
        """() => {
          try { return checkEmptyFields(jQuery('#page__FORM_seo')); }
          catch (e) { return 'ERR:' + e; }
        }"""
    )
    page.locator("#page__FORM_send_seo").click(force=True)
    success_seen = wait_success(page, 4000)
    ui = ui_flags(page)
    body = next((p.get("body") for p in posts if p.get("phase") == "resp"), None)
    out = {
        "case": label,
        "url": url,
        "checkEmptyFields": blocked,
        "request_url": next((p.get("url") for p in posts if p.get("phase") == "req"), None),
        "http": next((p.get("status") for p in posts if p.get("phase") == "resp"), None),
        "body": body,
        "page_reload": len(navs) > 1,
        "success_ui": success_seen or ui["success"],
        "generic_error": ui["generic_error"],
        "posts": posts,
        "pass": body == "true" and len(navs) <= 1 and not ui["generic_error"],
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
            # unique phone digits avoid inputmask collision
            cases.append(run_audit(browser, site_filled=False, phone="+7 (911) 501-11-01"))
            time.sleep(12)
            cases.append(run_audit(browser, site_filled=True, phone="+7 (911) 502-22-02"))
            time.sleep(12)
            cases.append(run_seo(browser, RESTAURANT, "restaurant", "+7 (911) 503-33-03"))
            time.sleep(320)  # page form rate window
            cases.append(run_seo(browser, CITY, "city", "+7 (911) 504-44-04"))
            time.sleep(12)
            cases.append(run_seo(browser, NICHE, "niche", "+7 (911) 505-55-05"))
            browser.close()
        report["cases"] = cases
        report["events_tail"] = _v.tail_events(sftp, 25)
        report["test_mode_off"] = _v.set_test_mode(sftp, False)
        report["cfg_final"] = _v.cfg_snapshot(sftp)
        report["ended"] = utc_now()
        report["summary"] = {c["case"]: c.get("pass") for c in cases}
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
