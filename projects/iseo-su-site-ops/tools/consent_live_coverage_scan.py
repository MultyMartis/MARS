#!/usr/bin/env python3
"""Production live coverage + server consent + false-positive static analysis."""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
FIELD = "personal_data_consent"
RECEIPT = Path(r"X:\AI MARS\local\sites\iseo-su-production\_form-consent-wave-01\deploy-receipt.json")

URLS = [
    "https://i-seo.su/",
    "https://i-seo.su/services.html",
    "https://i-seo.su/services/seo/b-regionakh.html",
    "https://i-seo.su/services/seo/zarubezhnye.html",
    "https://i-seo.su/blog/",
    "https://i-seo.su/glossary/",
    "https://i-seo.su/tariff-calc",
    "https://i-seo.su/about.html",
    "https://i-seo.su/career.html",
    "https://i-seo.su/bonuses.html",
    "https://i-seo.su/services/audit.html",
    "https://i-seo.su/services/seo.html",
    "https://i-seo.su/services/ai-optimization/chatgpt.html",
    "https://i-seo.su/privacy-policy.html",
]


def parse_secrets(path: Path) -> dict:
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([a-z0-9_]+):\s*(.*)$", line.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def fetch(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"Cache-Control": "no-cache", "Pragma": "no-cache"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.status, resp.read().decode("utf-8", "replace")


def analyze_html(html: str) -> dict:
    forms = re.findall(r"<form\b[^>]*>.*?</form>", html, flags=re.I | re.S)
    contact_forms = []
    for f in forms:
        low = f.lower()
        if any(
            x in low
            for x in (
                "__form",
                "cf_phone",
                "cf_name",
                'type="tel"',
                "calc_phone",
                "callback__",
            )
        ):
            contact_forms.append(f)
    missing = []
    for i, f in enumerate(contact_forms):
        if not re.search(rf'name=["\']{FIELD}["\']', f, re.I):
            idm = re.search(r'\bid=["\']([^"\']+)', f, re.I)
            missing.append(idm.group(1) if idm else f"form_{i}")
        else:
            # prechecked?
            m = re.search(rf'<input\b[^>]*name=["\']{FIELD}["\'][^>]*>', f, re.I)
            if m and re.search(r"\bchecked\b", m.group(0), re.I):
                missing.append("PRECHECKED:" + (re.search(r'\bid=["\']([^"\']+)', f, re.I).group(1) if re.search(r'\bid=["\']([^"\']+)', f, re.I) else "?"))
    return {
        "forms_total": len(forms),
        "contact_forms": len(contact_forms),
        "consent_fields": len(re.findall(rf'name=["\']{FIELD}["\']', html, re.I)),
        "missing_or_bad": missing,
        "privacy_link": "/privacy-policy.html" in html,
    }


def main() -> int:
    print("=== LIVE URL SCAN ===")
    live_uncovered = []
    results = {}
    for url in URLS:
        try:
            status, html = fetch(url)
        except Exception as e:
            print("FAIL", url, e)
            live_uncovered.append(url)
            continue
        info = analyze_html(html)
        results[url] = {"status": status, **info}
        flag = "OK"
        if info["contact_forms"] and info["missing_or_bad"]:
            flag = "UNCOVERED"
            live_uncovered.append(url)
        elif info["contact_forms"] == 0 and url != "https://i-seo.su/privacy-policy.html":
            # glossary/blog may still have footer forms
            flag = "NO_CONTACT_FORMS"
        print(
            f"{flag} {status} contact={info['contact_forms']} consent={info['consent_fields']} "
            f"missing={info['missing_or_bad']} {url}"
        )

    # False-positive analysis of receipt uncovered_final
    print("=== STATIC FALSE POSITIVE CHECK ===")
    secrets = parse_secrets(SECRETS)
    transport = paramiko.Transport((secrets["ftp_or_sftp_host"], int(secrets.get("ftp_or_sftp_port") or 22)))
    transport.connect(username=secrets["ftp_or_sftp_username"], password=secrets["ftp_or_sftp_password"])
    sftp = paramiko.SFTPClient.from_transport(transport)
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    uncovered = (receipt.get("static_stats") or {}).get("uncovered_final") or []
    real_static_gaps = []
    marker_only = []
    for remote in uncovered:
        try:
            with sftp.open(remote, "r") as f:
                text = f.read().decode("utf-8", "replace")
        except OSError as e:
            print("READ_FAIL", remote, e)
            continue
        has_form = bool(re.search(r"<form\b", text, re.I))
        has_consent = bool(re.search(rf'name=["\']{FIELD}["\']', text, re.I))
        if has_form and not has_consent:
            real_static_gaps.append(remote)
        else:
            marker_only.append(remote)
    print("receipt_uncovered", len(uncovered))
    print("marker_only_no_form_or_already_ok", len(marker_only))
    print("real_static_form_gaps", len(real_static_gaps))
    for g in real_static_gaps[:30]:
        print(" REAL_GAP", g)

    # Server security snippet checks
    with sftp.open("/home/n/nikel0rv/i-seo.su/public_html/iseo-form-security.php", "r") as f:
        sec = f.read().decode("utf-8", "replace")
    with sftp.open("/home/n/nikel0rv/i-seo.su/public_html/iseo-form-config.php", "r") as f:
        cfg = f.read().decode("utf-8", "replace")
    print("=== SERVER ===")
    print("consent_reject", 'iseo_form_reject($form_id, "consent")' in sec)
    print("exact_1", 'personal_data_consent' in sec and '!== "1"' in sec)
    print("test_mode_line", re.search(r"test_mode[^\n]+", cfg))
    print("recipient", re.findall(r"[\w.+-]+@[\w.-]+", cfg))

    sftp.close()
    transport.close()

    out = {
        "live_results": results,
        "live_uncovered": live_uncovered,
        "real_static_form_gaps": real_static_gaps,
        "marker_only_count": len(marker_only),
    }
    Path(r"X:\AI MARS\projects\iseo-su-site-ops\tools\_consent_live_scan.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("LIVE_UNCOVERED", len(live_uncovered))
    print("REAL_STATIC_GAPS", len(real_static_form_gaps))
    return 0 if not live_uncovered and not real_static_form_gaps else 1


if __name__ == "__main__":
    raise SystemExit(main())
