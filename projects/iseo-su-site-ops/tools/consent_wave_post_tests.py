#!/usr/bin/env python3
"""WAVE 1 consent: negative direct-POST + bounded positive via temporary test_mode."""
from __future__ import annotations

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
TOKEN_URL = f"{SITE}/iseo-form-token.php"
SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
OUT = Path(r"X:\AI MARS\projects\iseo-su-site-ops\tools\_consent_post_tests.json")
CFG_REMOTE = "/home/n/nikel0rv/i-seo.su/public_html/iseo-form-config.php"
HANDLERS = [
    "callback__FORM.php",
    "page__FORM.php",
    "audit__FORM.php",
    "calc__FORM.php",
    "tariff_1__FORM.php",
    "tariff_2__FORM.php",
    "tariff_3__FORM.php",
    "tariff_4__FORM.php",
    "bonus__FORM.php",
    "career__FORM.php",
    "partners__FORM.php",
    "review__FORM.php",
]


def parse_secrets(path: Path) -> dict:
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([a-z0-9_]+):\s*(.*)$", line.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def http_json(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def post_handler(handler_url: str, fields: dict) -> tuple[int, str]:
    tok = http_json(TOKEN_URL)
    time.sleep(3.2)
    data = {
        "contact_company_url": "",
        "iseo_ft": tok["t"],
        "iseo_fs": tok["s"],
        "iseo_fid": tok["id"],
    }
    data.update(fields)
    body = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(
        handler_url,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "ISEO-SU-FORM-CONSENT-WAVE-01/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return resp.status, resp.read().decode("utf-8", "replace").strip()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace").strip()


def sftp_connect():
    secrets = parse_secrets(SECRETS)
    transport = paramiko.Transport((secrets["ftp_or_sftp_host"], int(secrets.get("ftp_or_sftp_port") or 22)))
    transport.connect(username=secrets["ftp_or_sftp_username"], password=secrets["ftp_or_sftp_password"])
    sftp = paramiko.SFTPClient.from_transport(transport)
    return sftp, transport


def read_remote(sftp, path: str) -> str:
    with sftp.open(path, "r") as f:
        return f.read().decode("utf-8", "replace")


def write_remote(sftp, path: str, text: str) -> None:
    data = text.encode("utf-8")
    with sftp.open(path, "w") as f:
        f.write(data)


def set_test_mode(sftp, enabled: bool) -> str:
    text = read_remote(sftp, CFG_REMOTE)
    new_val = "true" if enabled else "false"
    new_text, n = re.subn(
        r'("test_mode"\s*=>\s*)(true|false)',
        rf"\1{new_val}",
        text,
        count=1,
    )
    if n != 1:
        raise SystemExit(f"test_mode replace failed n={n}")
    write_remote(sftp, CFG_REMOTE, new_text)
    verify = read_remote(sftp, CFG_REMOTE)
    m = re.search(r'"test_mode"\s*=>\s*(true|false)', verify)
    return m.group(1) if m else "MISSING"


def page_payload(extra: dict | None = None) -> dict:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    base = {
        "pf_name": "Consent Wave Test",
        "pf_contact": "Telegram",
        "pf_phone": f"@consent_wave_{stamp}",
        "pf_site": "https://example.com",
        "pf_comment": f"ISEO-SU-FORM-CONSENT-WAVE-01 positive {stamp}",
        "pf_page_title": "Consent Wave 01",
        "pf_page_link": "https://i-seo.su/",
        "personal_data_consent": "1",
    }
    if extra:
        base.update(extra)
    return base


def main() -> int:
    results = {"stamp": datetime.now(timezone.utc).isoformat(), "negative": [], "positive": {}, "handlers": []}

    # Consent fails inside iseo_form_guard_request BEFORE business-field checks.
    # Use distinct handlers to avoid shared rate-limit buckets.
    negatives = [
        ("missing", f"{SITE}/page__FORM.php", {}),
        ("zero", f"{SITE}/callback__FORM.php", {"personal_data_consent": "0"}),
        ("false", f"{SITE}/audit__FORM.php", {"personal_data_consent": "false"}),
        ("malformed", f"{SITE}/calc__FORM.php", {"personal_data_consent": "random"}),
    ]
    for name, url, fields in negatives:
        status, body = post_handler(url, fields)
        ok = status == 200 and body == "false"
        results["negative"].append(
            {"case": name, "handler": url, "status": status, "body": body, "rejected": ok}
        )
        print(f"NEG {name}: status={status} body={body!r} rejected={ok}")

    sftp, transport = sftp_connect()
    try:
        for h in HANDLERS:
            path = f"/home/n/nikel0rv/i-seo.su/public_html/{h}"
            try:
                text = read_remote(sftp, path)
            except OSError as e:
                results["handlers"].append({"handler": h, "ok": False, "error": str(e)})
                print("HANDLER_FAIL", h, e)
                continue
            guarded = "iseo_form_guard_request" in text
            results["handlers"].append({"handler": h, "ok": guarded, "guard": guarded, "bytes": len(text)})
            print(f"HANDLER {h}: guard={guarded}")

        sec = read_remote(sftp, "/home/n/nikel0rv/i-seo.su/public_html/iseo-form-security.php")
        results["security_consent"] = {
            "reject_call": 'iseo_form_reject($form_id, "consent")' in sec,
            "field": "personal_data_consent" in sec,
            "exact_1": '!== "1"' in sec,
        }

        print("ENABLING test_mode...")
        tm = set_test_mode(sftp, True)
        print("test_mode now", tm)
        try:
            status, body = post_handler(f"{SITE}/page__FORM.php", page_payload())
            pos_ok = status == 200 and body == "true"
            if not pos_ok:
                status, body = post_handler(f"{SITE}/page__FORM.php", page_payload())
                pos_ok = status == 200 and body == "true"
            results["positive"] = {
                "status": status,
                "body": body,
                "pass": pos_ok,
                "recipient_expected": "im.work@mail.ru",
                "note": "Accept-path under test_mode; mailbox not polled by this script",
            }
            print(f"POS: status={status} body={body!r} pass={pos_ok}")
        finally:
            after = set_test_mode(sftp, False)
            print("RESTORED test_mode", after)
            cfg = read_remote(sftp, CFG_REMOTE)
            tm_m = re.search(r'"test_mode"\s*=>\s*(true|false)', cfg)
            results["post_restore"] = {
                "test_mode": tm_m.group(1) if tm_m else "MISSING",
                "prod_recipient_literal": "nikel007i33@yandex.ru" in cfg,
                "nail_typo": "im.work@nail.ru" in cfg,
            }
            assert results["post_restore"]["test_mode"] == "false"
    finally:
        sftp.close()
        transport.close()

    neg_all = all(x["rejected"] for x in results["negative"])
    handlers_all = all(x.get("ok") for x in results["handlers"]) and len(results["handlers"]) == 12
    results["summary"] = {
        "negative_all_rejected": neg_all,
        "positive_pass": results["positive"].get("pass"),
        "handlers_all_guarded": handlers_all,
        "handler_count": len(results["handlers"]),
        "test_mode_restored_off": results.get("post_restore", {}).get("test_mode") == "false",
        "security_consent_ok": all(results.get("security_consent", {}).values()),
    }
    OUT.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(results["summary"], indent=2))
    if not all(
        [
            neg_all,
            results["positive"].get("pass"),
            handlers_all,
            results["summary"]["test_mode_restored_off"],
            results["summary"]["security_consent_ok"],
        ]
    ):
        return 2
    print("POST_TESTS_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
