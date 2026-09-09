#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SEO smoke: check ALL .required-checkbox (legacy cf_agree* + consent)."""
from __future__ import annotations

import importlib.util
import json
import time
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

_VALIDATE = Path(__file__).resolve().parent / "_form-contract-regression-01-validate.py"
_spec = importlib.util.spec_from_file_location("v", _VALIDATE)
_v = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_v)

EVIDENCE = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\homepage-modal-live-failure-02")
OUT = EVIDENCE / "_validation-seo-smoke.json"
SUFFIX = datetime.now(timezone.utc).strftime("%H%M%S")
PAGES = [
    ("restaurant", "https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html", "9116011101"),
    ("city", "https://i-seo.su/services/seo/prodvizhenie-v-novosibirske.html", "9116022202"),
    ("niche", "https://i-seo.su/services/seo/prodvizhenie-internet-magazina-kosmetiki.html", "9116033303"),
]


def main() -> None:
    report: dict = {"started": datetime.now(timezone.utc).isoformat(), "suffix": SUFFIX, "cases": []}
    sftp, transport = _v.sftp_connect()
    try:
        report["test_mode_on"] = _v.set_test_mode(sftp, True)
        time.sleep(1)
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            for i, (label, url, digits) in enumerate(PAGES):
                posts: list = []
                navs: list = []
                page = browser.new_page(viewport={"width": 1440, "height": 900})
                page.on(
                    "framenavigated",
                    lambda f, n=navs, pg=page: n.append(f.url) if f == pg.main_frame else None,
                )

                def on_req(r, bag=posts):
                    if r.method == "POST" and "page__FORM.php" in r.url:
                        bag.append({"phase": "req", "url": r.url, "post": r.post_data})

                def on_resp(r, bag=posts):
                    if r.request.method == "POST" and "page__FORM.php" in r.url:
                        try:
                            body = r.text().strip()
                        except Exception:
                            body = "ERR"
                        bag.append({"phase": "resp", "status": r.status, "body": body})

                page.on("request", on_req)
                page.on("response", on_resp)
                page.goto(url, wait_until="domcontentloaded", timeout=60000)
                page.wait_for_timeout(7000)
                f = page.locator("#page__FORM_seo")
                f.scroll_into_view_if_needed()
                f.locator("input[name='pf_name']").fill(f"{label} {SUFFIX}")
                ph = f.locator("input[name='pf_phone']")
                ph.click()
                ph.fill("")
                ph.type(digits, delay=30)
                page.wait_for_timeout(300)
                for cb in f.locator(".required-checkbox").all():
                    cb.check(force=True)
                blocked = page.evaluate("() => checkEmptyFields(jQuery('#page__FORM_seo'))")
                page.locator("#page__FORM_send_seo").click(force=True)
                try:
                    page.wait_for_function(
                        "() => /Успешно! Сообщение отправлено/i.test(document.body.innerText || '')",
                        timeout=4000,
                    )
                    success = True
                except Exception:
                    success = False
                body = next((x.get("body") for x in posts if x.get("phase") == "resp"), None)
                err = page.evaluate(
                    "() => /Не удалось отправить заявку/i.test(document.body.innerText || '')"
                )
                case = {
                    "case": label,
                    "checkEmptyFields": blocked,
                    "request_url": next((x.get("url") for x in posts if x.get("phase") == "req"), None),
                    "http": next((x.get("status") for x in posts if x.get("phase") == "resp"), None),
                    "body": body,
                    "success_ui": success,
                    "generic_error": err,
                    "page_reload": len(navs) > 1,
                    "pass": body == "true" and len(navs) <= 1 and not err,
                }
                report["cases"].append(case)
                print(json.dumps(case, ensure_ascii=False))
                page.close()
                if i == 0:
                    time.sleep(320)
                else:
                    time.sleep(12)
            browser.close()
        report["events"] = _v.tail_events(sftp, 12)
        report["test_mode_off"] = _v.set_test_mode(sftp, False)
        report["cfg_final"] = _v.cfg_snapshot(sftp)
    except Exception:
        try:
            report["test_mode_off_on_error"] = _v.set_test_mode(sftp, False)
        except Exception as exc:  # noqa: BLE001
            report["restore_err"] = str(exc)
        raise
    finally:
        sftp.close()
        transport.close()
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print("WROTE", OUT)
    print("SUMMARY", {c["case"]: c["pass"] for c in report["cases"]})


if __name__ == "__main__":
    main()
