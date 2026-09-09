#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resilient Playwright smoke after full_page screenshot failures."""
from __future__ import annotations

import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

_VALIDATE = Path(__file__).resolve().parent / "_form-contract-regression-01-validate.py"
_spec = importlib.util.spec_from_file_location("form_contract_validate", _VALIDATE)
_v = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_v)

ADV = _v.ADV
DEVELOP = _v.DEVELOP
EVIDENCE = _v.EVIDENCE
HOME = _v.HOME
OUT = _v.OUT
RESTAURANT = _v.RESTAURANT
SERM = _v.SERM
UA = _v.UA
cfg_snapshot = _v.cfg_snapshot
set_test_mode = _v.set_test_mode
sftp_connect = _v.sftp_connect
tail_events = _v.tail_events
utc_now = _v.utc_now

SHOTS = EVIDENCE / "screenshots"


def _shot(page, path: Path) -> str:
    try:
        page.screenshot(
            path=str(path),
            full_page=False,
            animations="disabled",
            timeout=12000,
        )
        return str(path)
    except Exception as exc:  # noqa: BLE001
        return f"SCREENSHOT_FAIL:{exc}"


def _form_metrics(page, form_id: str) -> dict:
    form = page.locator(f"#{form_id}")
    return {
        "form_present": form.count() > 0,
        "pf_phone": page.locator(f"#{form_id} input[name='pf_phone']").count() > 0
        if form.count()
        else page.locator('input[name="pf_phone"]').count() > 0,
        "hidden_pf_contact": page.locator(
            f"#{form_id} input[type='hidden'][name='pf_contact']"
        ).count()
        > 0,
        "select_pf_contact": page.locator(f"#{form_id} select[name='pf_contact']").count() > 0,
        "tel_named_contact": page.locator(
            f"#{form_id} input[type='tel'][name='pf_contact']"
        ).count()
        > 0,
    }


def fields_page(url: str, form_id: str, name: str, stamp: str) -> dict:
    shots = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for label, vp in (
            ("desktop-1440x900", {"width": 1440, "height": 900}),
            ("mobile-390x844", {"width": 390, "height": 844}),
        ):
            page = browser.new_page(viewport=vp, user_agent=UA)
            console = []
            page.on("console", lambda msg: console.append({"type": msg.type, "text": msg.text}))
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(1200)
            metrics = _form_metrics(page, form_id)
            path = SHOTS / f"{name}-{label}-{stamp}.png"
            metrics["screenshot"] = _shot(page, path)
            metrics["console_errors"] = [c for c in console if c["type"] == "error"]
            shots[label] = metrics
            page.close()
        browser.close()
    return {"available": True, "url": url, "viewports": shots}


def restaurant_submit(stamp: str) -> dict:
    posted: dict = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
        console = []
        page.on("console", lambda msg: console.append({"type": msg.type, "text": msg.text}))

        def on_request(req):
            if "page__FORM.php" in req.url and req.method == "POST":
                posted["url"] = req.url
                posted["method"] = req.method
                posted["post_data"] = req.post_data or ""

        def on_response(resp):
            if "page__FORM.php" in resp.url:
                posted["status"] = resp.status
                try:
                    posted["body"] = resp.text().strip()
                except Exception:
                    posted["body"] = ""

        page.on("request", on_request)
        page.on("response", on_response)
        page.goto(RESTAURANT, wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(2500)
        form = page.locator("#page__FORM_seo")
        form.scroll_into_view_if_needed()
        form.locator("#pf_name").fill(f"FORM CONTRACT UI {stamp}")
        form.locator("#pf_contact").fill(f"+7988{stamp[-7:]}")
        if form.locator("#pf_site").count():
            form.locator("#pf_site").fill("https://example-regression.test")
        form.locator("#pf_comment").fill("SYNTHETIC FORM CONTRACT UI TEST — ignore")
        if form.locator("#cf_agree21").count():
            form.locator("#cf_agree21").check(force=True)
        page.locator("#personal_data_consent_page__FORM_seo").check(force=True)
        before = SHOTS / f"restaurant-desktop-1440x900-before-submit-{stamp}.png"
        before_path = _shot(page, before)
        try:
            with page.expect_response(lambda r: "page__FORM.php" in r.url, timeout=20000):
                page.click("#page__FORM_send_seo")
            page.wait_for_timeout(2500)
        except Exception as exc:  # noqa: BLE001
            posted["wait_error"] = str(exc)
            page.wait_for_timeout(6000)
        success = page.locator("text=Успешно! Сообщение отправлено").count() > 0
        fail = page.locator("text=Не удалось отправить заявку").count() > 0
        after = SHOTS / f"restaurant-desktop-1440x900-after-submit-{stamp}.png"
        after_path = _shot(page, after)
        desktop = {
            "success_ui": success,
            "generic_fail_ui": fail,
            "console_errors": [c for c in console if c["type"] == "error"],
            "screenshot_before": before_path,
            "screenshot_after": after_path,
            "network": {
                "url": posted.get("url"),
                "method": posted.get("method"),
                "status": posted.get("status"),
                "body": posted.get("body"),
                "has_pf_phone": "pf_phone=" in (posted.get("post_data") or ""),
                "consent_1": "personal_data_consent=1" in (posted.get("post_data") or ""),
                "wait_error": posted.get("wait_error"),
            },
        }
        page.close()
        page2 = browser.new_page(viewport={"width": 390, "height": 844}, user_agent=UA)
        page2.goto(RESTAURANT, wait_until="domcontentloaded", timeout=45000)
        page2.wait_for_timeout(1200)
        mobile_metrics = _form_metrics(page2, "page__FORM_seo")
        mobile_path = SHOTS / f"restaurant-mobile-390x844-{stamp}.png"
        mobile_metrics["screenshot"] = _shot(page2, mobile_path)
        browser.close()
    return {"available": True, "desktop": desktop, "mobile": mobile_metrics}


def main() -> int:
    SHOTS.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    report = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    report["ui_smoke_retry_started"] = utc_now()
    sftp, transport = sftp_connect()
    test_mode_touched = False
    try:
        report["cfg_before_ui_retry"] = cfg_snapshot(sftp)
        test_mode_touched = True
        report["test_mode_on_ui_retry"] = set_test_mode(sftp, True)
        try:
            report["ui_restaurant_retry"] = restaurant_submit(stamp)
        except Exception as exc:  # noqa: BLE001
            report["ui_restaurant_retry"] = {"available": False, "error": str(exc)}
        report["events_after_ui_retry"] = tail_events(sftp, 8)
        report["test_mode_off_ui_retry"] = set_test_mode(sftp, False)
        test_mode_touched = False
        for key, url, form_id, name in (
            ("ui_adv_retry", ADV, "page__FORM_adv", "adv-adwords"),
            ("ui_serm_retry", SERM, "page__FORM_serm", "serm-smm"),
            ("ui_develop_retry", DEVELOP, "page__FORM_develop", "develop-sozdanie"),
            ("ui_home_retry", HOME, "page__FORM", "home-unaffected"),
        ):
            try:
                report[key] = fields_page(url, form_id, name, stamp)
            except Exception as exc:  # noqa: BLE001
                report[key] = {"available": False, "error": str(exc), "url": url}
        report["cfg_final_ui_retry"] = cfg_snapshot(sftp)
        report["ui_smoke_retry_ended"] = utc_now()
        OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        ui = report.get("ui_restaurant_retry", {})
        desk = ui.get("desktop", {}) if isinstance(ui, dict) else {}
        print(
            json.dumps(
                {
                    "out": str(OUT),
                    "restaurant_success_ui": desk.get("success_ui"),
                    "restaurant_fail_ui": desk.get("generic_fail_ui"),
                    "network": desk.get("network"),
                    "cfg_final": report["cfg_final_ui_retry"],
                    "adv_ok": report.get("ui_adv_retry", {}).get("available"),
                    "home_ok": report.get("ui_home_retry", {}).get("available"),
                },
                ensure_ascii=False,
            )
        )
        return 0
    except Exception:
        if test_mode_touched:
            try:
                report["test_mode_off_on_error"] = set_test_mode(sftp, False)
            except Exception as restore_exc:  # noqa: BLE001
                report["test_mode_restore_error"] = str(restore_exc)
        report["ui_smoke_retry_ended"] = utc_now()
        OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        raise
    finally:
        sftp.close()
        transport.close()


if __name__ == "__main__":
    raise SystemExit(main())
