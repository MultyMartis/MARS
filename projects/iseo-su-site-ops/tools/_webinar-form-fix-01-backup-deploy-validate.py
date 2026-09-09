#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISEO-SU-SITE-OPS-WEBINAR-FORM-FIX-01: backup, surgical HTML deploy, POST/UI validate."""
from __future__ import annotations

import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SITE = "https://i-seo.su"
URL = f"{SITE}/webinar-seo-podryadchik.html"
TOKEN_URL = f"{SITE}/iseo-form-token.php"
HANDLER = f"{SITE}/page__FORM.php"
HOME = f"{SITE}/"
RESTAURANT = f"{SITE}/services/seo/prodvizhenie-sajta-restorana.html"
SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
DOC = "/home/n/nikel0rv/i-seo.su/public_html"
REMOTE_HTML = f"{DOC}/webinar-seo-podryadchik.html"
CFG_REMOTE = f"{DOC}/iseo-form-config.php"
EVENTS_LOG = f"{DOC}/.iseo-form-runtime/events.log"
SRC_HTML = Path(
    r"X:\AI MARS\projects\iseo-su-site-ops\production-source\static-html\webinar-seo-podryadchik.html"
)
BAK_ROOT = Path(r"X:\AI MARS\local\sites\iseo-su-production\_webinar-form-fix-01")
EVIDENCE = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\webinar-form-fix-01")
OUT = BAK_ROOT / "_deploy_validate.json"
UA = "ISEO-SU-WEBINAR-FORM-FIX-01/1.0"

OLD_CORE = (
    '<input type="tel" id="pf_contact" name="pf_contact" placeholder="WhatsApp / Telegram" required>'
)
OLD_CORE_B = OLD_CORE.encode("ascii")
DATE10_B = "10 сентября 2026".encode("utf-8")
DATE3_B = "3 сентября 2026".encode("utf-8")


def apply_core_patch_bytes(raw: bytes) -> tuple[bytes, str]:
    if b'name="pf_phone"' in raw and b'value="WhatsApp"' in raw:
        return raw, "already_patched"
    if OLD_CORE_B not in raw:
        raise SystemExit("live HTML tel/name=pf_contact core not found; refuse broad rewrite")
    nl = b"\r\n" if b"\r\n" in raw else b"\n"
    replacement = (
        b'<input type="hidden" name="pf_contact" value="WhatsApp">'
        + nl
        + b"\t\t\t\t\t\t\t\t\t"
        + b'<input type="tel" id="pf_contact" name="pf_phone" placeholder="WhatsApp / Telegram" required>'
    )
    after = raw.replace(OLD_CORE_B, replacement, 1)
    if raw.count(DATE10_B) != after.count(DATE10_B):
        raise SystemExit("date 10 сентября drift during patch")
    if DATE3_B not in raw and DATE3_B in after:
        raise SystemExit("date 3 сентября introduced")
    if b'name="pf_phone"' not in after:
        raise SystemExit("patch did not introduce pf_phone")
    return after, "patched"

KEEP_MARKERS = [
    "10 сентября 2026",
    "19:00 МСК",
    "Как выбрать подрядчика в SEO и не ошибиться?",
    "WEBINAR SEO CONTRACTOR 2026-09",
    'name="personal_data_consent"',
    'id="page__FORM_seo"',
    'id="page__FORM_send_seo"',
    'name="pf_phone"',
    'name="pf_contact"',
]


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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


def post_handler(fields: dict) -> dict:
    tok = http_json(TOKEN_URL)
    time.sleep(3.3)
    data = {
        "contact_company_url": "",
        "iseo_ft": tok["t"],
        "iseo_fs": tok["s"],
        "iseo_fid": tok["id"],
        "pf_page_title": "WEBINAR FORM TEST",
        "pf_page_link": URL,
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


def cfg_snapshot(sftp) -> dict:
    text = read_remote_bytes(sftp, CFG_REMOTE).decode("utf-8", "replace")
    tm = re.search(r'"test_mode"\s*=>\s*(true|false)', text)
    prod = re.search(r'"production_recipients"\s*=>\s*\[(.*?)\]', text, re.S)
    test = re.search(r'"test_recipients"\s*=>\s*\[(.*?)\]', text, re.S)
    prod_raw = prod.group(1) if prod else ""
    test_raw = test.group(1) if test else ""
    return {
        "test_mode": tm.group(1) if tm else None,
        "production_recipients_raw": prod_raw.strip(),
        "test_recipients_raw": test_raw.strip(),
        "prod_has_nikel": "nikel007i33@yandex.ru" in prod_raw,
        "prod_has_im_work": "im.work@mail.ru" in prod_raw,
        "test_has_im_work": "im.work@mail.ru" in test_raw,
        "nail_typo": "im.work@nail.ru" in text,
        "hmac_secret_null": '"hmac_secret" => null' in text or '"hmac_secret"=>null' in text,
        "honeypot_field": "contact_company_url" in text,
        "min_fill_seconds": "min_fill_seconds" in text and "3" in text,
        "rate_limit_burst_max": "rate_limit_burst_max" in text,
        "duplicate_window": "duplicate_window" in text,
    }


def webinar_base(stamp: str, extra: dict | None = None) -> dict:
    fields = {
        "pf_name": f"WEBINAR FORM TEST {stamp}",
        "pf_contact": "WhatsApp",
        "pf_phone": f"+7999{stamp[-7:]}",
        "pf_site": "WEBINAR SEO CONTRACTOR 2026-09",
        "pf_comment": "SYNTHETIC WEBINAR FORM TEST — ignore",
        "personal_data_consent": "1",
    }
    if extra:
        fields.update(extra)
    return fields


def html_form_contract(html: str) -> dict:
    return {
        "has_pf_phone": 'name="pf_phone"' in html,
        "has_hidden_whatsapp": 'name="pf_contact" value="WhatsApp"' in html,
        "tel_still_named_contact": re.search(
            r'<input type="tel"[^>]*name="pf_contact"', html
        )
        is not None,
        "consent_1": 'name="personal_data_consent"' in html and 'value="1"' in html,
        "pf_site": "WEBINAR SEO CONTRACTOR 2026-09" in html,
        "date_10": "10 сентября 2026" in html,
        "date_3": "3 сентября 2026" in html,
        "time_1900": "19:00 МСК" in html,
        "h1": "Как выбрать подрядчика в SEO и не ошибиться?" in html,
    }


def playwright_ui(stamp: str) -> dict:
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:  # noqa: BLE001
        return {"available": False, "error": str(exc)}

    out = EVIDENCE / "screenshots"
    out.mkdir(parents=True, exist_ok=True)
    result = {"available": True, "viewports": []}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Desktop submit + screenshot
        page = browser.new_page(viewport={"width": 1440, "height": 900}, user_agent=UA)
        console = []
        page.on("console", lambda msg: console.append({"type": msg.type, "text": msg.text}))
        page.goto(URL, wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(3500)
        page.fill("#pf_name", f"WEBINAR UI TEST {stamp}")
        page.fill("#pf_contact", f"+7988{stamp[-7:]}")
        page.fill("#pf_comment", "SYNTHETIC WEBINAR UI TEST — ignore")
        page.check("input[name='personal_data_consent']")
        posted = {}

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
            with page.expect_response(
                lambda r: "page__FORM.php" in r.url, timeout=20000
            ):
                page.click("#page__FORM_send_seo")
            page.wait_for_timeout(2500)
        except Exception as exc:  # noqa: BLE001
            posted["wait_error"] = str(exc)
            page.wait_for_timeout(8000)
        success = page.locator("text=Успешно! Сообщение отправлено").count() > 0
        fail = page.locator("text=Не удалось отправить заявку").count() > 0
        shot = out / f"desktop-1440x900-after-submit-{stamp}.png"
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
            },
            "screenshot": str(shot),
        }
        page.close()

        page2 = browser.new_page(viewport={"width": 390, "height": 844}, user_agent=UA)
        page2.goto(URL, wait_until="domcontentloaded", timeout=45000)
        page2.wait_for_timeout(1500)
        mobile_shot = out / f"mobile-390x844-{stamp}.png"
        page2.screenshot(path=str(mobile_shot), full_page=True)
        form_ok = page2.locator("#page__FORM_seo").count() > 0
        result["mobile"] = {
            "form_present": form_ok,
            "screenshot": str(mobile_shot),
            "h1": page2.locator("h1").inner_text().strip() if page2.locator("h1").count() else "",
        }
        browser.close()
    return result


def main() -> int:
    BAK_ROOT.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    report: dict = {
        "task": "ISEO-SU-SITE-OPS-WEBINAR-FORM-FIX-01",
        "started": utc_now(),
    }
    src_text = SRC_HTML.read_text(encoding="utf-8")
    if 'name="pf_phone"' not in src_text or 'value="WhatsApp"' not in src_text:
        raise SystemExit("canonical source missing patched webinar form contract")
    if OLD_CORE in src_text:
        raise SystemExit("canonical source still has OLD_CORE tel named pf_contact")

    sftp, transport = sftp_connect()
    test_mode_touched = False
    try:
        before = read_remote_bytes(sftp, REMOTE_HTML)
        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        bak_path = BAK_ROOT / f"webinar-seo-podryadchik.html.before.{ts}"
        bak_path.write_bytes(before)
        cfg_before = read_remote_bytes(sftp, CFG_REMOTE)
        cfg_bak = BAK_ROOT / f"iseo-form-config.php.before.{ts}"
        cfg_bak.write_bytes(cfg_before)
        report["backup"] = [
            {
                "absolute_path": str(bak_path),
                "remote": REMOTE_HTML,
                "sha256_before": sha256_bytes(before),
                "timestamp": utc_now(),
                "bytes": len(before),
            },
            {
                "absolute_path": str(cfg_bak),
                "remote": CFG_REMOTE,
                "sha256_before": sha256_bytes(cfg_before),
                "timestamp": utc_now(),
            },
        ]
        before_html = before.decode("utf-8", "replace")
        report["live_before"] = html_form_contract(before_html)
        report["cfg_before"] = cfg_snapshot(sftp)

        patched, deploy_mode = apply_core_patch_bytes(before)
        if deploy_mode == "already_patched":
            report["deploy"] = "already_patched"
        else:
            write_remote_bytes(sftp, REMOTE_HTML, patched)
            verify = read_remote_bytes(sftp, REMOTE_HTML)
            if sha256_bytes(verify) != sha256_bytes(patched):
                raise SystemExit("remote checksum mismatch after write")
            report["deploy"] = {
                "mode": deploy_mode,
                "sha256_after": sha256_bytes(verify),
                "bytes": len(verify),
            }

        status, ctype, live_bytes = http_get(URL)
        live_html = live_bytes.decode("utf-8", "replace")
        report["live_after_http"] = {
            "status": status,
            "content_type": ctype,
            "contract": html_form_contract(live_html),
            "keep_markers": {m: (m in live_html) for m in KEEP_MARKERS},
        }

        stamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        report["rate_limit_pause_seconds"] = 310

        missing_fields = webinar_base(stamp + "1")
        del missing_fields["personal_data_consent"]
        missing = post_handler(missing_fields)
        missing["event_class"] = last_event_class(tail_events(sftp))
        report["neg_missing_consent"] = missing

        zero = post_handler(webinar_base(stamp + "2", {"personal_data_consent": "0"}))
        zero["event_class"] = last_event_class(tail_events(sftp))
        report["neg_consent_0"] = zero

        malformed = post_handler(
            webinar_base(stamp + "3", {"personal_data_consent": "yes"})
        )
        malformed["event_class"] = last_event_class(tail_events(sftp))
        report["neg_malformed_consent"] = malformed

        report["pause_started"] = utc_now()
        time.sleep(310)
        report["pause_ended"] = utc_now()

        hp_fields = webinar_base(stamp + "4")
        hp_fields["contact_company_url"] = "http://spam.example"
        # post_handler always injects empty honeypot then update — extra must win
        tok = http_json(TOKEN_URL)
        time.sleep(3.3)
        hp_data = {
            "contact_company_url": "http://spam.example",
            "iseo_ft": tok["t"],
            "iseo_fs": tok["s"],
            "iseo_fid": tok["id"],
            "pf_page_title": "WEBINAR FORM TEST",
            "pf_page_link": URL,
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

        test_mode_touched = True
        report["test_mode_on"] = set_test_mode(sftp, True)
        pos = post_handler(webinar_base(stamp + "5"))
        pos["event_class"] = last_event_class(tail_events(sftp))
        report["pos_isolated_mail"] = pos

        ui = playwright_ui(stamp + "6")
        report["ui"] = ui

        report["test_mode_off"] = set_test_mode(sftp, False)
        test_mode_touched = False
        report["cfg_final"] = cfg_snapshot(sftp)

        h_status, _, home = http_get(HOME)
        r_status, _, rest = http_get(RESTAURANT)
        home_html = home.decode("utf-8", "replace")
        rest_html = rest.decode("utf-8", "replace")
        report["regression"] = {
            "home_status": h_status,
            "home_has_pf_phone": 'name="pf_phone"' in home_html,
            "home_has_pf_contact_select": 'name="pf_contact"' in home_html,
            "restaurant_status": r_status,
            "restaurant_form_present": 'id="page__FORM_seo"' in rest_html,
        }
        report["source_sha256"] = sha256_bytes(src_text.encode("utf-8"))
        report["ended"] = utc_now()
        OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        (EVIDENCE / "_deploy_validate.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(json.dumps({"out": str(OUT), "pos": pos, "cfg": report["cfg_final"]}, ensure_ascii=False))
        return 0
    except Exception:
        if test_mode_touched:
            try:
                set_test_mode(sftp, False)
            except Exception:
                pass
        raise
    finally:
        sftp.close()
        transport.close()


if __name__ == "__main__":
    raise SystemExit(main())
