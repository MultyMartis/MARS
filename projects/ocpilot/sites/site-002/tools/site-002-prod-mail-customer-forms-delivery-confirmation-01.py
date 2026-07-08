#!/usr/bin/env python3
"""SITE-002 customer form email delivery confirmation — Run 4.231."""
from __future__ import annotations

import json
import re
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-MAIL-CUSTOMER-FORMS-DELIVERY-CONFIRMATION-01"
OCPILOT_RUN = "4.231"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
TEST_MARKER = "MARS TEST CUSTOMER DELIVERY CONFIRMATION 01"
TEST_PHONE = "+7 000 000-00-00"
TEST_PAGE_URL = "https://bzpm.ru/custom-equipment"
TEST_DIALOG = "11"
TEST_SOURCE_PAGE = "https://bzpm.ru/custom-equipment"
WRONG_BRAND = "БЗПМ"

SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOY_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-MAIL-CUSTOMER-FORMS-DELIVERY-CONFIRMATION-01"
)

BEFORE_URLS = [
    "https://bzpm.ru/custom-equipment",
    "https://bzpm.ru/delivery",
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/llms.txt",
    "https://bzpm.ru/robots.txt",
]
AFTER_URLS = [
    "https://bzpm.ru/custom-equipment",
    "https://bzpm.ru/delivery",
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/llms.txt",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/sitemap.xml",
]

SUBDIRS = (
    "test-submit",
    "mailbox-confirmation",
    "verification",
    "reports",
    "manifests",
    "logs",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def mask_email(email: str) -> str:
    if "@" not in email:
        return "[redacted]"
    local, domain = email.split("@", 1)
    if not local:
        return f"***@{domain}"
    return f"{local[0]}***@{domain}"


def read_operator_test_email() -> tuple[str, str]:
    text = SECRETS_PATH.read_text(encoding="utf-8")
    in_prod = False
    for line in text.splitlines():
        if line.strip() == "## PRODUCTION":
            in_prod = True
            continue
        if in_prod and line.startswith("## ") and line.strip() != "## PRODUCTION":
            break
        if in_prod:
            m = re.match(r"^\s*operator_test_email:\s*(\S+)\s*$", line)
            if m:
                email = m.group(1).strip()
                return email, mask_email(email)
    raise RuntimeError("operator_test_email not found in secrets PRODUCTION section")


def http_get(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read()
            try:
                text = body.decode("utf-8")
            except UnicodeDecodeError:
                text = body.decode("utf-8", errors="replace")
            return {
                "url": url,
                "status": resp.status,
                "length": len(body),
                "has_bzpm": WRONG_BRAND in text,
                "has_zpm_form": "zpm-form" in text,
                "has_corp_cta": "data-corp-cta" in text,
                "has_load_more": "load-more" in text.lower() or "Load More" in text or "загрузить ещё" in text.lower(),
            }
    except urllib.error.HTTPError as e:
        return {"url": url, "status": e.code, "error": str(e)}
    except Exception as e:  # noqa: BLE001
        return {"url": url, "status": "ERROR", "error": str(e)}


def sitemap_count(url: str) -> int | None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            root = ET.fromstring(resp.read())
            ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            locs = root.findall(".//sm:loc", ns)
            if locs:
                return len(locs)
            return len(root.findall(".//loc"))
    except Exception:  # noqa: BLE001
        return None


def controlled_submit(test_email: str, masked: str) -> dict[str, Any]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {"attempted": False, "blocker": "playwright unavailable"}

    fields = {
        "company": "MARS TEST ORG",
        "contact": TEST_MARKER,
        "phone": TEST_PHONE,
        "email": test_email,
        "project_description": (
            "Тестовое сообщение MARS TEST CUSTOMER DELIVERY CONFIRMATION 01. "
            "Проверка клиентского письма-подтверждения. Это тест, не заявка клиента."
        ),
        "agree": "on",
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1200})
        page.set_default_timeout(120000)
        page.goto(TEST_PAGE_URL, wait_until="networkidle")
        page.wait_for_timeout(3000)
        result = page.evaluate(
            """async (cfg) => {
                const csrf = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');
                if (!csrf) return { error: 'csrf_missing' };
                const recaptchaScript = document.querySelector('script[src*="google.com/recaptcha"]');
                const siteKey = recaptchaScript ? recaptchaScript.getAttribute('data-sitekey') : null;
                let captchaToken = null;
                if (window.grecaptcha && siteKey) {
                    await new Promise((resolve) => window.grecaptcha.ready(resolve));
                    captchaToken = await window.grecaptcha.execute(siteKey, { action: 'submit' });
                }
                if (!captchaToken) return { error: 'recaptcha_token_missing' };
                const formData = new FormData();
                formData.append('dialog', String(cfg.dialog));
                formData.append('source_page', cfg.source_page);
                for (const [k, v] of Object.entries(cfg.fields)) {
                    if (v !== '' && v != null) formData.append(k, v);
                }
                formData.append('csrf_token', csrf);
                formData.append('g-recaptcha-response', captchaToken);
                const response = await fetch('/index.php?route=checkout/anketa', {
                    method: 'POST',
                    body: formData,
                    credentials: 'same-origin',
                });
                let body;
                try { body = await response.json(); } catch (e) { body = { raw: await response.text() }; }
                return { status: response.status, body };
            }""",
            {"dialog": TEST_DIALOG, "source_page": TEST_SOURCE_PAGE, "fields": fields},
        )
        browser.close()

    out: dict[str, Any] = {
        "operation_id": OPERATION_ID,
        "page": "custom-equipment",
        "dialog": TEST_DIALOG,
        "marker": TEST_MARKER,
        "attempted": True,
        "response_status": result.get("status"),
        "response": result.get("body"),
        "admin_mail_expected": True,
        "customer_mail_expected": True,
        "inline_success_observed": None,
    }
    if result.get("error"):
        out["blocker"] = result["error"]
        out["ok"] = False
    else:
        body = result.get("body") or {}
        out["ok"] = result.get("status") == 200 and isinstance(body, dict) and body.get("ok") is True

    redacted_request = {
        "page": TEST_PAGE_URL,
        "dialog": TEST_DIALOG,
        "source_page": TEST_SOURCE_PAGE,
        "fields": {
            "company": "MARS TEST ORG",
            "contact": TEST_MARKER,
            "phone": TEST_PHONE,
            "email": masked,
            "project_description": "[test marker text]",
            "agree": "on",
        },
    }
    write_json(DEPLOY_ROOT / "test-submit" / "request-redacted.json", redacted_request)
    write_json(DEPLOY_ROOT / "test-submit" / "response.json", {
        "status": out.get("response_status"),
        "body": out.get("response"),
        "ok": out.get("ok"),
        "blocker": out.get("blocker"),
    })
    summary = [
        "# Controlled test submit",
        "",
        f"- Operation: `{OPERATION_ID}`",
        f"- Page: `{TEST_PAGE_URL}`",
        f"- Dialog: **{TEST_DIALOG}** (Оборудование на заказ)",
        f"- Marker: `{TEST_MARKER}`",
        f"- Email: `{masked}`",
        f"- HTTP status: {out.get('response_status')}",
        f"- JSON ok: {out.get('ok')}",
        f"- Admin mail expected: yes",
        f"- Customer mail expected: yes",
        f"- Blocker: {out.get('blocker', 'none')}",
        "",
    ]
    write_text(DEPLOY_ROOT / "test-submit" / "summary.md", "\n".join(summary))
    return out


def main() -> int:
    for sub in SUBDIRS:
        (DEPLOY_ROOT / sub).mkdir(parents=True, exist_ok=True)

    test_email, masked = read_operator_test_email()

    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": "SITE-002",
        "environment": "PRODUCTION_VERIFICATION",
        "production_url": PRODUCTION_URL,
        "baseline_before": BASELINE_BEFORE,
        "related_customer_forms_run": "SITE-002-PROD-MAIL-CUSTOMER-FORMS-01",
        "related_customer_forms_ocpilot_run": "4.226",
        "change_type": "customer-mailbox-delivery-confirmation",
        "production_mutation_allowed": False,
        "code_change_allowed": False,
        "ftp_upload_allowed": False,
        "admin_save_allowed": False,
        "db_write_allowed": False,
        "email_send_allowed": "one_controlled_customer_test",
        "form_submit_allowed": "one_controlled_customer_test",
        "smtp_change_allowed": False,
        "standard_opencart_mail_change_allowed": False,
        "customer_service_info_allowed": False,
        "brand_policy_correct": "ЗПМ",
        "brand_policy_forbidden_public": "БЗПМ",
        "created_at": utc_now(),
    }
    write_json(DEPLOY_ROOT / "manifests" / "operation.json", manifest)

    write_json(
        DEPLOY_ROOT / "verification" / "test-email-resolution.json",
        {
            "source": "secrets.md PRODUCTION operator_test_email",
            "email_masked": masked,
            "usable_for_controlled_test": True,
            "resolved_at": utc_now(),
        },
    )
    write_text(
        DEPLOY_ROOT / "verification" / "test-email-resolution.md",
        "\n".join(
            [
                "# Test email resolution",
                "",
                "- Source: `secrets.md` → `## PRODUCTION` → `operator_test_email`",
                f"- Masked: `{masked}`",
                "- Usable for one controlled customer delivery test: **yes**",
                "",
            ]
        ),
    )

    before = [http_get(u) for u in BEFORE_URLS]
    write_json(DEPLOY_ROOT / "verification" / "before-sanity.json", {"checked_at": utc_now(), "results": before})
    before_lines = ["# Before sanity", "", f"Checked: {utc_now()}", ""]
    for r in before:
        before_lines.append(
            f"- {r['url']}: status={r.get('status')} bzpm={r.get('has_bzpm', 'n/a')} form={r.get('has_zpm_form', r.get('has_corp_cta', 'n/a'))}"
        )
    write_text(DEPLOY_ROOT / "verification" / "before-sanity.md", "\n".join(before_lines) + "\n")

    submit = controlled_submit(test_email, masked)

    mailbox = {
        "delivery_confirmed": False,
        "confirmation_source": "pending_operator_mailbox_check",
        "subject_expected_pattern": "ЗПМ: заявка получена — Оборудование на заказ",
        "subject_observed": None,
        "marker_found": None,
        "zpm_branding": None,
        "design_approved": None,
        "service_info_absent": None,
        "ip_absent": None,
        "user_agent_absent": None,
        "referrer_absent": None,
        "issues": ["Agent has no safe mailbox access; operator must confirm delivery in mailbox"],
        "submit_ok": submit.get("ok"),
        "checked_at": utc_now(),
    }
    write_json(DEPLOY_ROOT / "mailbox-confirmation" / "customer-delivery-confirmation.json", mailbox)
    write_text(
        DEPLOY_ROOT / "mailbox-confirmation" / "customer-delivery-confirmation.md",
        "\n".join(
            [
                "# Customer delivery confirmation",
                "",
                "- Delivery confirmed: **no** (pending operator mailbox check)",
                f"- Submit ok: {submit.get('ok')}",
                "- Expected subject pattern: `ЗПМ: заявка получена — Оборудование на заказ`",
                "- Agent mailbox inspection: **not available**",
                "",
            ]
        ),
    )

    after = [http_get(u) for u in AFTER_URLS]
    sm_count = sitemap_count("https://bzpm.ru/sitemap.xml")
    write_json(
        DEPLOY_ROOT / "verification" / "after-sanity.json",
        {"checked_at": utc_now(), "results": after, "sitemap_url_count": sm_count},
    )
    after_lines = ["# After sanity", "", f"Checked: {utc_now()}", f"Sitemap URL count: {sm_count}", ""]
    for r in after:
        after_lines.append(
            f"- {r['url']}: status={r.get('status')} bzpm={r.get('has_bzpm', 'n/a')} load_more={r.get('has_load_more', 'n/a')}"
        )
    write_text(DEPLOY_ROOT / "verification" / "after-sanity.md", "\n".join(after_lines) + "\n")

    write_json(
        DEPLOY_ROOT / "logs" / "run-summary.json",
        {
            "operation_id": OPERATION_ID,
            "ocpilot_run": OCPILOT_RUN,
            "submit_ok": submit.get("ok"),
            "email_masked": masked,
            "mailbox_pending": True,
            "finished_at": utc_now(),
        },
    )
    print(json.dumps({"submit_ok": submit.get("ok"), "email_masked": masked, "blocker": submit.get("blocker")}))
    return 0 if submit.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
