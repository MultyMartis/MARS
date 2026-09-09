#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISEO-SU-SITE-OPS-FORM-CONTRACT-REGRESSION-01: POST/UI validate after contract patch."""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SITE = "https://i-seo.su"
TOKEN_URL = f"{SITE}/iseo-form-token.php"
HANDLER = f"{SITE}/page__FORM.php"
HOME = f"{SITE}/"
WEBINAR = f"{SITE}/webinar-seo-podryadchik.html"
RESTAURANT = f"{SITE}/services/seo/prodvizhenie-sajta-restorana.html"
BLOG = f"{SITE}/blog.html"
ADV = f"{SITE}/services/adv/google-adwords.html"
SERM = f"{SITE}/services/serm/smm.html"
DEVELOP = f"{SITE}/services/development/sozdanie-sajta.html"
SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
DOC = "/home/n/nikel0rv/i-seo.su/public_html"
CFG_REMOTE = f"{DOC}/iseo-form-config.php"
EVENTS_LOG = f"{DOC}/.iseo-form-runtime/events.log"
EVIDENCE = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-contract-regression-01")
OUT = EVIDENCE / "_validate.json"
UA = "ISEO-SU-FORM-CONTRACT-REGRESSION-01/1.0"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_secrets(path: Path) -> dict:
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([a-z0-9_]+):\s*(.*)$", line.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def sftp_connect():
    secrets = parse_secrets(SECRETS)
    transport = paramiko.Transport(
        (secrets["ftp_or_sftp_host"], int(secrets.get("ftp_or_sftp_port") or 22))
    )
    transport.connect(
        username=secrets["ftp_or_sftp_username"], password=secrets["ftp_or_sftp_password"]
    )
    return paramiko.SFTPClient.from_transport(transport), transport


def read_remote_bytes(sftp, path: str) -> bytes:
    with sftp.open(path, "r") as f:
        return f.read()


def write_remote_bytes(sftp, path: str, data: bytes) -> None:
    with sftp.open(path, "w") as f:
        f.write(data)


def http_get(url: str) -> tuple[int, str, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=45) as resp:
        body = resp.read()
        return resp.status, resp.headers.get("Content-Type", ""), body


def http_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def post_handler(fields: dict, page_link: str) -> dict:
    tok = http_json(TOKEN_URL)
    time.sleep(3.3)
    data = {
        "contact_company_url": "",
        "iseo_ft": tok["t"],
        "iseo_fs": tok["s"],
        "iseo_fid": tok["id"],
        "pf_page_title": "FORM CONTRACT REGRESSION TEST",
        "pf_page_link": page_link,
    }
    data.update(fields)
    body = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(
        HANDLER,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": UA,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return {
                "http_status": resp.status,
                "content_type": resp.headers.get("Content-Type", ""),
                "body": resp.read().decode("utf-8", "replace").strip(),
                "posted_keys": sorted(data.keys()),
            }
    except urllib.error.HTTPError as e:
        return {
            "http_status": e.code,
            "content_type": e.headers.get("Content-Type", "") if e.headers else "",
            "body": e.read().decode("utf-8", "replace").strip(),
            "posted_keys": sorted(data.keys()),
        }


def tail_events(sftp, n: int = 8) -> list[str]:
    try:
        raw = read_remote_bytes(sftp, EVENTS_LOG).decode("utf-8", "replace")
    except Exception as exc:  # noqa: BLE001
        return [f"UNREAD:{exc}"]
    lines = [ln for ln in raw.splitlines() if ln.strip()]
    return lines[-n:]


def last_event_class(lines: list[str]) -> str:
    if not lines:
        return "MISSING"
    last = lines[-1]
    try:
        obj = json.loads(last)
        return str(obj.get("class") or last)
    except Exception:
        return last


def set_test_mode(sftp, enabled: bool) -> str:
    text = read_remote_bytes(sftp, CFG_REMOTE).decode("utf-8", "replace")
    new_val = "true" if enabled else "false"
    new_text, n = re.subn(
        r'("test_mode"\s*=>\s*)(true|false)',
        rf"\1{new_val}",
        text,
        count=1,
    )
    if n != 1:
        raise SystemExit(f"test_mode replace failed n={n}")
    write_remote_bytes(sftp, CFG_REMOTE, new_text.encode("utf-8"))
    verify = read_remote_bytes(sftp, CFG_REMOTE).decode("utf-8", "replace")
    m = re.search(r'"test_mode"\s*=>\s*(true|false)', verify)
    return m.group(1) if m else "MISSING"


def _block(text: str, key: str) -> str:
    m = re.search(rf'"{key}"\s*=>\s*array\s*\((.*?)\)\s*,', text, re.S)
    if m:
        return m.group(1)
    m = re.search(rf'"{key}"\s*=>\s*\[(.*?)\]', text, re.S)
    return m.group(1) if m else ""


def cfg_snapshot(sftp) -> dict:
    text = read_remote_bytes(sftp, CFG_REMOTE).decode("utf-8", "replace")
    tm = re.search(r'"test_mode"\s*=>\s*(true|false)', text)
    prod_raw = _block(text, "production_recipients")
    test_raw = _block(text, "test_recipients")
    return {
        "test_mode": tm.group(1) if tm else None,
        "prod_has_nikel": "nikel007i33@yandex.ru" in prod_raw,
        "prod_has_im_work": "im.work@mail.ru" in prod_raw,
        "test_has_im_work": "im.work@mail.ru" in test_raw,
        "nail_typo": "im.work@nail.ru" in text,
        "hmac_secret_null": '"hmac_secret" => null' in text or '"hmac_secret"=>null' in text,
        "honeypot_field": "contact_company_url" in text,
        "min_fill_seconds": "min_fill_seconds" in text,
        "rate_limit_burst_max": "rate_limit_burst_max" in text,
        "duplicate_window": "duplicate_window" in text,
        "consent_guard_hint": "personal_data_consent" in text,
    }


def restaurant_base(stamp: str, extra: dict | None = None) -> dict:
    fields = {
        "pf_name": f"FORM CONTRACT REGRESSION {stamp}",
        "pf_contact": "WhatsApp",
        "pf_phone": f"+7999{stamp[-7:]}",
        "pf_site": "https://example-regression.test",
        "pf_comment": "SYNTHETIC FORM CONTRACT REGRESSION TEST — ignore",
        "personal_data_consent": "1",
    }
    if extra:
        fields.update(extra)
    return fields


def html_form_contract(html: str) -> dict:
    tel_named = re.search(r'<input type="tel"[^>]*name="pf_contact"', html) is not None
    return {
        "has_pf_phone": 'name="pf_phone"' in html,
        "has_hidden_whatsapp": 'name="pf_contact" value="WhatsApp"' in html,
        "tel_still_named_contact": tel_named,
        "consent_checkbox": 'name="personal_data_consent"' in html,
        "select_pf_contact": "<select" in html and 'name="pf_contact"' in html,
    }


def page_contract_get(url: str) -> dict:
    status, ctype, raw = http_get(url)
    html = raw.decode("utf-8", "replace")
    title_m = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
    h1_m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S)
    can_m = re.search(r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', html, re.I)
    return {
        "url": url,
        "http": status,
        "content_type": ctype,
        "title": title_m.group(1).strip() if title_m else "",
        "h1": re.sub(r"<[^>]+>", "", h1_m.group(1)).strip() if h1_m else "",
        "canonical": can_m.group(1) if can_m else "",
        "contract": html_form_contract(html),
    }


def playwright_restaurant(stamp: str) -> dict:
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:  # noqa: BLE001
        return {"available": False, "error": str(exc)}

    out = EVIDENCE / "screenshots"
    out.mkdir(parents=True, exist_ok=True)
    result: dict = {"available": True}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
        console = []
        page.on("console", lambda msg: console.append({"type": msg.type, "text": msg.text}))
        page.goto(RESTAURANT, wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(3500)
        form = page.locator("#page__FORM_seo")
        form.locator("#pf_name").fill(f"FORM CONTRACT UI {stamp}")
        form.locator("#pf_contact").fill(f"+7988{stamp[-7:]}")
        if form.locator("#pf_site").count():
            form.locator("#pf_site").fill("https://example-regression.test")
        form.locator("#pf_comment").fill("SYNTHETIC FORM CONTRACT UI TEST — ignore")
        if form.locator("#cf_agree21").count():
            page.locator("label[for='cf_agree21']").first.click()
        page.locator("label[for='personal_data_consent_page__FORM_seo']").first.click()
        posted: dict = {}

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
        try:
            with page.expect_response(lambda r: "page__FORM.php" in r.url, timeout=20000):
                page.click("#page__FORM_send_seo")
            page.wait_for_timeout(2500)
        except Exception as exc:  # noqa: BLE001
            posted["wait_error"] = str(exc)
            page.wait_for_timeout(8000)
        success = page.locator("text=Успешно! Сообщение отправлено").count() > 0
        fail = page.locator("text=Не удалось отправить заявку").count() > 0
        shot = out / f"restaurant-desktop-1440x900-after-submit-{stamp}.png"
        page.screenshot(path=str(shot), full_page=True)
        result["desktop"] = {
            "success_ui": success,
            "generic_fail_ui": fail,
            "console_errors": [c for c in console if c["type"] == "error"],
            "network": {
                "url": posted.get("url"),
                "method": posted.get("method"),
                "status": posted.get("status"),
                "body": posted.get("body"),
                "has_pf_phone": "pf_phone=" in (posted.get("post_data") or ""),
                "consent_1": "personal_data_consent=1" in (posted.get("post_data") or ""),
                "honeypot_empty": "contact_company_url=" in (posted.get("post_data") or "")
                and "contact_company_url=http" not in (posted.get("post_data") or ""),
                "relative_ajax_note": posted.get("url"),
            },
            "screenshot": str(shot),
        }
        page.close()

        page2 = browser.new_page(viewport={"width": 390, "height": 844}, user_agent=UA)
        page2.goto(RESTAURANT, wait_until="domcontentloaded", timeout=45000)
        page2.wait_for_timeout(1500)
        mobile_shot = out / f"restaurant-mobile-390x844-{stamp}.png"
        page2.screenshot(path=str(mobile_shot), full_page=True)
        result["mobile"] = {
            "form_present": page2.locator("#page__FORM_seo").count() > 0,
            "pf_phone": page2.locator('input[name="pf_phone"]').count() > 0,
            "tel_named_contact": page2.locator('input[type="tel"][name="pf_contact"]').count() > 0,
            "screenshot": str(mobile_shot),
        }
        browser.close()
    return result


def playwright_fields_only(url: str, form_id: str, stamp: str, name: str) -> dict:
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:  # noqa: BLE001
        return {"available": False, "error": str(exc), "url": url}

    out = EVIDENCE / "screenshots"
    out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        shots = {}
        for label, vp in (("desktop-1440x900", {"width": 1440, "height": 900}), ("mobile-390x844", {"width": 390, "height": 844})):
            page = browser.new_page(viewport=vp, user_agent=UA)
            console = []
            page.on("console", lambda msg: console.append({"type": msg.type, "text": msg.text}))
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(1500)
            shot = out / f"{name}-{label}-{stamp}.png"
            page.screenshot(path=str(shot), full_page=True)
            shots[label] = {
                "form_present": page.locator(f"#{form_id}").count() > 0 if form_id else True,
                "pf_phone": page.locator('input[name="pf_phone"]').count() > 0,
                "hidden_pf_contact": page.locator('input[type="hidden"][name="pf_contact"]').count() > 0,
                "select_pf_contact": page.locator('select[name="pf_contact"]').count() > 0,
                "tel_named_contact": page.locator('input[type="tel"][name="pf_contact"]').count() > 0,
                "console_errors": [c for c in console if c["type"] == "error"],
                "screenshot": str(shot),
            }
            page.close()
        browser.close()
    return {"available": True, "url": url, "viewports": shots}


def _write_report(report: dict) -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    report["ended"] = utc_now()
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    ui_only = "--ui-only" in sys.argv
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    report: dict = {
        "task": "ISEO-SU-SITE-OPS-FORM-CONTRACT-REGRESSION-01",
        "started": utc_now(),
        "mode": "ui-only" if ui_only else "full",
    }
    sftp, transport = sftp_connect()
    test_mode_touched = False
    pos = {"skipped": True}
    try:
        report["cfg_before"] = cfg_snapshot(sftp)
        report["gets"] = {
            "restaurant": page_contract_get(RESTAURANT),
            "blog": page_contract_get(BLOG),
            "adv": page_contract_get(ADV),
            "serm": page_contract_get(SERM),
            "develop": page_contract_get(DEVELOP),
            "home": page_contract_get(HOME),
            "webinar": page_contract_get(WEBINAR),
        }
        stamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        report["events_salvage"] = tail_events(sftp, 30)

        if not ui_only:
            report["rate_limit_pause_seconds"] = 310

            test_mode_touched = True
            report["test_mode_on"] = set_test_mode(sftp, True)

            missing_fields = restaurant_base(stamp + "1")
            del missing_fields["personal_data_consent"]
            missing = post_handler(missing_fields, RESTAURANT)
            missing["event_class"] = last_event_class(tail_events(sftp))
            report["neg_missing_consent"] = missing

            zero = post_handler(restaurant_base(stamp + "2", {"personal_data_consent": "0"}), RESTAURANT)
            zero["event_class"] = last_event_class(tail_events(sftp))
            report["neg_consent_0"] = zero

            malformed = post_handler(
                restaurant_base(stamp + "3", {"personal_data_consent": "yes"}), RESTAURANT
            )
            malformed["event_class"] = last_event_class(tail_events(sftp))
            report["neg_malformed_consent"] = malformed

            report["pause_started"] = utc_now()
            time.sleep(310)
            report["pause_ended"] = utc_now()

            tok = http_json(TOKEN_URL)
            time.sleep(3.3)
            hp_fields = restaurant_base(stamp + "4")
            hp_data = {
                "contact_company_url": "http://spam.example",
                "iseo_ft": tok["t"],
                "iseo_fs": tok["s"],
                "iseo_fid": tok["id"],
                "pf_page_title": "FORM CONTRACT REGRESSION TEST",
                "pf_page_link": RESTAURANT,
            }
            hp_data.update(hp_fields)
            body = urllib.parse.urlencode(hp_data).encode("utf-8")
            req = urllib.request.Request(
                HANDLER,
                data=body,
                method="POST",
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": UA,
                },
            )
            with urllib.request.urlopen(req, timeout=45) as resp:
                hp_res = {
                    "http_status": resp.status,
                    "body": resp.read().decode("utf-8", "replace").strip(),
                }
            hp_res["event_class"] = last_event_class(tail_events(sftp))
            report["neg_honeypot"] = hp_res

            pos = post_handler(restaurant_base(stamp + "5"), RESTAURANT)
            pos["event_class"] = last_event_class(tail_events(sftp))
            report["pos_isolated_mail"] = pos
        else:
            test_mode_touched = True
            report["test_mode_on"] = set_test_mode(sftp, True)
            report["post_wave_note"] = (
                "HTTP POST negatives + isolated accept already executed in the first "
                "full validate wave; this run is UI-only. events_salvage holds the log."
            )

        try:
            report["ui_restaurant"] = playwright_restaurant(stamp + "6")
        except Exception as exc:  # noqa: BLE001
            report["ui_restaurant"] = {"available": False, "error": str(exc)}

        for key, url, form_id, name in (
            ("ui_blog_fields_only", BLOG, "page__FORM_info", "blog"),
            ("ui_adv_fields_only", ADV, "page__FORM_adv", "adv-adwords"),
            ("ui_serm_fields_only", SERM, "page__FORM_serm", "serm-smm"),
            ("ui_develop_fields_only", DEVELOP, "page__FORM_develop", "develop-sozdanie"),
            ("ui_home_unaffected", HOME, "page__FORM", "home-unaffected"),
            ("ui_webinar_unaffected", WEBINAR, "page__FORM_seo", "webinar-unaffected"),
        ):
            try:
                report[key] = playwright_fields_only(url, form_id, stamp, name)
            except Exception as exc:  # noqa: BLE001
                report[key] = {"available": False, "error": str(exc), "url": url}

        report["test_mode_off"] = set_test_mode(sftp, False)
        test_mode_touched = False
        report["cfg_final"] = cfg_snapshot(sftp)
        _write_report(report)
        print(
            json.dumps(
                {
                    "out": str(OUT),
                    "mode": report.get("mode"),
                    "pos": pos,
                    "cfg": report["cfg_final"],
                    "restaurant_contract": report["gets"]["restaurant"]["contract"],
                    "home_contract": report["gets"]["home"]["contract"],
                    "webinar_contract": report["gets"]["webinar"]["contract"],
                    "ui_restaurant_ok": not report.get("ui_restaurant", {}).get("error"),
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
        try:
            report["cfg_final"] = cfg_snapshot(sftp)
        except Exception as cfg_exc:  # noqa: BLE001
            report["cfg_final_error"] = str(cfg_exc)
        _write_report(report)
        raise
    finally:
        sftp.close()
        transport.close()


if __name__ == "__main__":
    raise SystemExit(main())
