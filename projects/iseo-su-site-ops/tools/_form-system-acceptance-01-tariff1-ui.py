#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tariff_1 modal UI only. Isolated test_mode. Unique phone."""
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
OUT = EVIDENCE / "_tariff1-ui.json"
SITE = acc.SITE


def main() -> None:
    report = {"started_utc": acc.utc_now()}
    sftp, transport = acc._v.sftp_connect()
    test_mode_on = False
    try:
        report["cfg_before"] = acc._v.cfg_snapshot(sftp)
        acc._v.set_test_mode(sftp, True)
        test_mode_on = True
        acc.PHONE = f"+7999{datetime.now(timezone.utc).strftime('%H%M%S')}1"
        acc.STAMP = datetime.now(timezone.utc).strftime("%H%M%S")
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            report["browser"] = acc.browser_submit(
                browser,
                label="nested_tariff1_modal",
                url=f"{SITE}/services/seo/prodvizhenie-sajta-restorana.html",
                form_sel="#tariff_1__FORM_seo",
                btn_sel="#tariff_1__FORM_send_seo",
                open_sel='a.modalbox[href="#tariff_1__FORM_popup"]',
                needles=("tariff_1__FORM.php",),
            )
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
    print(json.dumps({
        "label": report.get("browser", {}).get("label") if isinstance(report.get("browser"), dict) else None,
        "body": report.get("browser", {}).get("body") if isinstance(report.get("browser"), dict) else None,
        "pass": report.get("browser", {}).get("pass") if isinstance(report.get("browser"), dict) else None,
        "success_ui": report.get("browser", {}).get("success_ui") if isinstance(report.get("browser"), dict) else None,
        "request_url": report.get("browser", {}).get("request_url") if isinstance(report.get("browser"), dict) else None,
        "error": report.get("browser", {}).get("error") if isinstance(report.get("browser"), dict) else None,
        "crash": report.get("crash"),
        "test_mode_final": report.get("cfg_final", {}).get("test_mode"),
        "prod_has_im_work": report.get("cfg_final", {}).get("prod_has_im_work"),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
