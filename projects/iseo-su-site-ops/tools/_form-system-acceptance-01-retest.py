#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Retest remaining UI authorities after fill/popup/success-UI harness fixes.

Does not send to nikel007i33@yandex.ru. test_mode ON only during run.
Unique phones avoid duplicate-window false rejects.
"""
from __future__ import annotations

import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ACCEPT = Path(__file__).resolve().parent / "_form-system-acceptance-01-accept.py"
_spec = importlib.util.spec_from_file_location("fsa_accept", ACCEPT)
acc = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(acc)

EVIDENCE = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-system-acceptance-01")
OUT = EVIDENCE / "_retest.json"
SITE = acc.SITE


def phone_for(label: str) -> str:
    stamp = datetime.now(timezone.utc).strftime("%H%M%S")
    tail = abs(hash(label + stamp)) % 10_000_000
    return f"+7999{tail:07d}"


def main() -> None:
    report = {"started_utc": acc.utc_now(), "browser": []}
    sftp, transport = acc._v.sftp_connect()
    test_mode_on = False
    try:
        report["cfg_before"] = acc._v.cfg_snapshot(sftp)
        acc._v.set_test_mode(sftp, True)
        test_mode_on = True
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            cases = [
                dict(
                    label="nested_seo_page",
                    url=f"{SITE}/services/seo/prodvizhenie-sajta-restorana.html",
                    form_sel="#page__FORM_seo",
                    btn_sel="#page__FORM_send_seo",
                    needles=("page__FORM.php",),
                ),
                dict(
                    label="webinar",
                    url=f"{SITE}/webinar-seo-podryadchik.html",
                    form_sel="#page__FORM_seo, #page__FORM",
                    btn_sel="#page__FORM_send_seo, #page__FORM_send",
                    needles=("page__FORM.php",),
                ),
                dict(
                    label="career",
                    url=f"{SITE}/career.html",
                    form_sel="#career__FORM_info",
                    btn_sel="#career__FORM_send_info",
                    open_sel='a[href="#career__FORM_popup"]',
                    needles=("career__FORM.php",),
                ),
                dict(
                    label="reviews",
                    url=f"{SITE}/reviews.html",
                    form_sel="#review_page__FORM_info",
                    btn_sel="#review_page__FORM_send_info",
                    needles=("review__FORM.php",),
                ),
                dict(
                    label="nested_tariff1_modal",
                    url=f"{SITE}/services/seo.html",
                    form_sel="#tariff_1__FORM_seo",
                    btn_sel="#tariff_1__FORM_send_seo",
                    open_sel='a[href="#tariff_1__FORM_popup"]',
                    needles=("tariff_1__FORM.php",),
                ),
                dict(
                    label="blog_html",
                    url=f"{SITE}/blog.html",
                    form_sel="#page__FORM_info",
                    btn_sel="#page__FORM_send_info",
                    needles=("page__FORM.php",),
                ),
            ]
            for spec in cases:
                acc.PHONE = phone_for(spec["label"])
                acc.STAMP = datetime.now(timezone.utc).strftime("%H%M%S")
                report["browser"].append(acc.browser_submit(browser, **spec))
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
    report["summary"] = {
        "pass": [(b.get("label"), b.get("body"), b.get("pass"), b.get("success_ui"), b.get("request_url")) for b in report["browser"]],
        "test_mode_final": report.get("cfg_final", {}).get("test_mode"),
        "prod_has_nikel": report.get("cfg_final", {}).get("prod_has_nikel"),
        "prod_has_im_work": report.get("cfg_final", {}).get("prod_has_im_work"),
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
