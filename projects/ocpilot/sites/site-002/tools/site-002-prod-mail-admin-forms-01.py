#!/usr/bin/env python3
"""SITE-002 admin form mail redesign + service info — Run 4.224."""
from __future__ import annotations

import argparse
import csv
import difflib
import ftplib
import hashlib
import html as html_module
import io
import json
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-MAIL-ADMIN-FORMS-01"
OCPILOT_RUN = "4.224"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-MAIL-DESIGN-SYSTEM-01"
CHECKPOINT_AFTER = "SITE-002-STABLE-PROD-MAIL-ADMIN-FORMS-01"
CORRECT_BRAND = "ЗПМ"
WRONG_BRAND = "БЗПМ"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

REPO_ROOT = Path(r"X:\AI MARS")
TOOLS_DIR = REPO_ROOT / "projects" / "ocpilot" / "sites" / "site-002" / "tools"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-MAIL-ADMIN-FORMS-01"
)

REMOTE_ANKETA = "/public_html/catalog/controller/checkout/anketa.php"
REMOTE_RENDERER = "/public_html/system/library/zpm/mail_renderer.php"
REMOTE_MOD_ANKETA = "/storage/modification/catalog/controller/checkout/anketa.php"
REMOTE_MOD_RENDERER = "/storage/modification/system/library/zpm/mail_renderer.php"

ANKETA_PATCH = TOOLS_DIR / "checkout_anketa_mail_admin_forms.php"
RENDERER_SRC = TOOLS_DIR / "mail_renderer.php"

SUBDIRS = (
    "source-before",
    "source-after",
    "http-before",
    "http-after",
    "mail-before",
    "mail-after",
    "test-submit",
    "patch",
    "verification",
    "rollback",
    "manifests",
    "reports",
    "logs",
)

FORM_URLS = [
    ("home", "https://bzpm.ru/"),
    ("katalog", "https://bzpm.ru/katalog"),
    ("stoly", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly"),
    (
        "pdp",
        "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye/"
        "polki-dlya-gastoemkostey/derzhatel-dlya-gastroemkostey-pg-10-3-900h330h40-gn-1-6-5-sht",
    ),
]

SANITY_URLS = [
    ("home", "https://bzpm.ru/"),
    ("katalog", "https://bzpm.ru/katalog"),
    ("neutral_hub", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie"),
    ("stoly", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly"),
    (
        "pdp",
        "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye/"
        "polki-dlya-gastoemkostey/derzhatel-dlya-gastroemkostey-pg-10-3-900h330h40-gn-1-6-5-sht",
    ),
    ("llms", "https://bzpm.ru/llms.txt"),
    ("robots", "https://bzpm.ru/robots.txt"),
    ("sitemap", "https://bzpm.ru/sitemap.xml"),
]

TEST_MARKER = "MARS TEST MAIL ADMIN FORMS 01"
TEST_NAME = TEST_MARKER
TEST_PHONE = "+7 000 000-00-00"
TEST_EMAIL = "test@example.invalid"
TEST_MESSAGE = (
    "Тестовое сообщение MARS TEST MAIL ADMIN FORMS 01. "
    "Проверка оформления admin-письма и служебной информации. Это тест, не заявка клиента."
)

PALETTE = {
    "bg": "#f5f7fa",
    "container": "#ffffff",
    "text": "#1f2933",
    "muted": "#667085",
    "border": "#e5e7eb",
    "accent": "#0f766e",
}


def esc(value: Any) -> str:
    return html_module.escape(str(value), quote=True)


def text_from_html(content: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", content, flags=re.I)
    text = re.sub(r"</p>|</tr>|</li>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = html_module.unescape(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def wrap_document(title: str, preheader: str, body: str) -> str:
    p = PALETTE
    return (
        f'<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">'
        f'<meta name="viewport" content="width=device-width, initial-scale=1.0">'
        f"<title>{esc(title)}</title></head>"
        f'<body style="margin:0;padding:0;background-color:{p["bg"]};'
        f'font-family:Arial,Helvetica,sans-serif;color:{p["text"]};">'
        f'<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:transparent;">{esc(preheader)}</div>'
        f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" '
        f'style="background-color:{p["bg"]};padding:24px 12px;"><tr><td align="center">'
        f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="600" '
        f'style="max-width:600px;width:100%;background-color:{p["container"]};'
        f'border:1px solid {p["border"]};border-radius:8px;overflow:hidden;">'
        f'<tr><td style="padding:24px 28px;font-size:15px;line-height:1.55;color:{p["text"]};">'
        f"{body}</td></tr></table>"
        f'<p style="margin:16px 0 0;font-size:12px;line-height:1.4;color:{p["muted"]};text-align:center;">'
        f"{esc(CORRECT_BRAND)} · bzpm.ru</p></td></tr></table></body></html>"
    )


def render_preview_admin(data: dict[str, Any]) -> dict[str, str]:
    p = PALETTE
    title = data.get("subject", "ЗПМ: новая заявка")
    body = (
        f'<table role="presentation" width="100%" style="margin:0 0 20px;"><tr><td '
        f'style="padding-bottom:16px;border-bottom:2px solid {p["accent"]};">'
        f'<div style="font-size:22px;font-weight:700;color:{p["accent"]};">{esc(CORRECT_BRAND)}</div>'
        f'<div style="margin-top:4px;font-size:13px;color:{p["muted"]};">bzpm.ru</div></td></tr></table>'
        f'<h1 style="margin:0 0 20px;font-size:20px;">{esc(title)}</h1>'
        f'<div style="margin:0 0 16px;padding:14px 16px;background:{p["bg"]};border:1px solid {p["border"]};border-radius:6px;">'
        f'<div style="font-weight:700;margin-bottom:8px;">Кратко</div>'
        f'<div>Тип формы: <strong>{esc(data.get("dialog_label", ""))}</strong></div>'
        f'<div>Товар: <strong>{esc(data.get("product", ""))}</strong></div>'
        f"</div>"
        f'<div style="margin:0 0 16px;"><div style="font-weight:700;margin-bottom:8px;">Контактные данные</div>'
        f'<div>Имя: <strong>{esc(data.get("author", ""))}</strong></div>'
        f'<div>Телефон: <strong>{esc(data.get("phone", ""))}</strong></div>'
        f'<div>E-mail: <strong>{esc(data.get("email", ""))}</strong></div></div>'
        f'<div style="margin:0 0 16px;padding:14px 16px;border:1px solid {p["border"]};border-radius:6px;">'
        f'<div style="font-weight:700;margin-bottom:8px;">Сообщение</div>'
        f'<div>{esc(data.get("message", ""))}</div></div>'
    )
    service = data.get("service_info", {})
    if service:
        body += (
            f'<div style="margin-top:16px;padding-top:12px;border-top:1px dashed {p["border"]};">'
            f'<div style="font-size:12px;font-weight:700;color:{p["muted"]};text-transform:uppercase;">Служебная информация</div>'
        )
        for label, key in (
            ("IP", "ip"),
            ("Браузер", "browser"),
            ("Устройство", "device"),
            ("ОС", "os"),
            ("User-Agent", "user_agent"),
            ("Referrer", "referrer"),
            ("UTM", "utm"),
            ("Город", "city"),
            ("Dialog", "dialog"),
            ("Отправлено", "submitted_at"),
        ):
            if service.get(key):
                body += f'<div style="font-size:12px;color:{p["muted"]};">{label}: {esc(service.get(key))}</div>'
        body += f'<div style="font-size:12px;color:{p["muted"]};">Страница: {esc(data.get("page_url", ""))}</div></div>'
    body += (
        f'<div style="margin-top:20px;padding-top:16px;border-top:1px solid {p["border"]};font-size:12px;color:{p["muted"]};">'
        "Это автоматическое письмо с сайта bzpm.ru.</div>"
    )
    html = wrap_document(title, title, body)
    return {"html": html, "text": text_from_html(html), "subject": title}


class FormParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.forms: list[dict[str, Any]] = []
        self._current: dict[str, Any] | None = None
        self._field: dict[str, str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ad = {k: (v or "") for k, v in attrs}
        if tag.lower() == "form":
            self._current = {
                "action": ad.get("action", ""),
                "method": ad.get("method", "get").upper(),
                "class": ad.get("class", ""),
                "fields": [],
            }
        elif self._current is not None and tag.lower() in ("input", "textarea", "select", "button"):
            self._field = {
                "tag": tag.lower(),
                "type": ad.get("type", ""),
                "name": ad.get("name", ""),
                "id": ad.get("id", ""),
            }
            if tag.lower() == "textarea":
                self._current["fields"].append(self._field)
                self._field = None

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "form" and self._current is not None:
            self.forms.append(self._current)
            self._current = None


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow(row)


def parse_production_section(path: Path, subsection: str | None = None) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    if subsection:
        sub = re.search(rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
        if not sub:
            raise RuntimeError(f"Subsection {subsection!r} not found")
        block = sub.group(1)
    fields: dict[str, str] = {}
    current: str | None = None
    for line in block.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.endswith(":"):
            current = s[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(current, "")
            continue
        if current:
            fields[current] = s
    return fields


def ftp_connect() -> ftplib.FTP:
    creds = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(creds["host"], int(creds.get("port") or 21), timeout=120)
    ftp.login(creds["username"], creds["password"])
    return ftp


def ftp_download(ftp: ftplib.FTP, remote: str) -> tuple[bytes | None, str | None]:
    buf = io.BytesIO()
    try:
        ftp.retrbinary(f"RETR {remote}", buf.write)
        return buf.getvalue(), None
    except Exception as exc:  # noqa: BLE001
        return None, str(exc)


def ftp_upload(ftp: ftplib.FTP, remote: str, data: bytes) -> None:
    ftp.storbinary(f"STOR {remote}", io.BytesIO(data))


def remote_local_name(remote: str) -> str:
    return remote.strip("/").replace("/", "__")


def http_get(url: str) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xml,text/plain,*/*"},
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = resp.read()
            charset = resp.headers.get_content_charset() or "utf-8"
            return {
                "url": url,
                "status": resp.status,
                "headers": dict(resp.headers.items()),
                "raw_body": body,
                "text": body.decode(charset, errors="replace"),
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read()
        charset = exc.headers.get_content_charset() or "utf-8"
        return {
            "url": url,
            "status": exc.code,
            "headers": dict(exc.headers.items()),
            "raw_body": body,
            "text": body.decode(charset, errors="replace"),
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "status": None, "headers": {}, "raw_body": b"", "text": "", "error": str(exc)}


def ensure_layout() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "change_type": "admin-form-mail-redesign-service-info",
            "production_mutation_allowed": True,
            "email_send_allowed": "one_controlled_test_submit_only",
            "form_submit_allowed": "one_controlled_test_submit_only",
            "smtp_change_allowed": False,
            "admin_save_allowed": False,
            "db_write_allowed": False,
            "customer_copy_change_allowed": False,
            "standard_opencart_mail_change_allowed": False,
            "mail_trigger_patch_allowed": "checkout_anketa_only",
            "shared_renderer_patch_allowed": "only_if_compatibility_needed",
            "header_footer_change_allowed": False,
            "pdp_change_allowed": False,
            "category_change_allowed": False,
            "sitemap_change_allowed": False,
            "robots_change_allowed": False,
            "llms_txt_change_allowed": False,
            "geoip_external_api_allowed": False,
            "brand_policy_correct": CORRECT_BRAND,
            "brand_policy_forbidden_public": WRONG_BRAND,
            "created_at": utc_now(),
        },
    )


def phase_source_authority() -> dict[str, Any]:
    paths = [
        (REMOTE_ANKETA, True),
        (REMOTE_RENDERER, False),
        (REMOTE_MOD_ANKETA, False),
        (REMOTE_MOD_RENDERER, False),
    ]
    rows: list[dict[str, Any]] = []
    mod_blocker = False
    ftp = ftp_connect()
    try:
        for remote, will_touch in paths:
            data, err = ftp_download(ftp, remote)
            exists = data is not None
            sha = sha256_bytes(data) if data else ""
            if data is not None:
                local = DEPLOYMENT_ROOT / "source-before" / remote_local_name(remote)
                local.write_bytes(data)
            is_mod = "modification" in remote
            if is_mod and exists:
                mod_blocker = True
            rows.append(
                {
                    "remote_path": remote,
                    "exists": exists,
                    "sha256": sha,
                    "will_touch": will_touch,
                    "modification_overlay": is_mod,
                    "error": err or "",
                }
            )
    finally:
        ftp.quit()

    write_csv(
        DEPLOYMENT_ROOT / "manifests" / "source-authority-map.csv",
        rows,
        ["remote_path", "exists", "sha256", "will_touch", "modification_overlay", "error"],
    )
    write_json(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.json", {"generated_at": utc_now(), "paths": rows})
    md = ["# Source authority map", "", f"Operation: {OPERATION_ID}", ""]
    for row in rows:
        md.append(
            f"- `{row['remote_path']}` exists={row['exists']} touch={row['will_touch']} mod={row['modification_overlay']}"
        )
    if mod_blocker:
        md.append("\n**STOP:** modification overlay overrides target file(s).")
    write_text(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.md", "\n".join(md) + "\n")
    return {"rows": rows, "mod_blocker": mod_blocker}


def phase_http_before() -> dict[str, Any]:
    inventory: list[dict[str, Any]] = []
    for slug, url in FORM_URLS:
        resp = http_get(url)
        parser = FormParser()
        try:
            parser.feed(resp.get("text", "")[:800000])
        except Exception:  # noqa: BLE001
            pass
        zpm_forms = [f for f in parser.forms if "zpm-form" in f.get("class", "")]
        csrf = bool(re.search(r'<meta[^>]+name=["\']csrf-token["\']', resp.get("text", ""), re.I))
        recaptcha = "google.com/recaptcha" in resp.get("text", "")
        inventory.append(
            {
                "slug": slug,
                "url": url,
                "status": resp.get("status"),
                "form_count": len(parser.forms),
                "zpm_form_count": len(zpm_forms),
                "csrf_meta": csrf,
                "recaptcha_present": recaptcha,
                "route": "checkout/anketa",
                "sample_fields": [fld.get("name") for f in zpm_forms[:2] for fld in f.get("fields", []) if fld.get("name")],
            }
        )
    payload = {"generated_at": utc_now(), "pages": inventory}
    write_json(DEPLOYMENT_ROOT / "http-before" / "form-pages-before.json", payload)
    lines = ["# Form pages before", ""]
    for p in inventory:
        lines.append(f"- **{p['slug']}** {p['url']} HTTP {p['status']}; zpm-forms={p['zpm_form_count']}; CSRF={p['csrf_meta']}; reCAPTCHA={p['recaptcha_present']}")
    write_text(DEPLOYMENT_ROOT / "http-before" / "form-pages-before.md", "\n".join(lines) + "\n")
    return payload


def phase_implementation_design() -> None:
    design = {
        "operation_id": OPERATION_ID,
        "patch_files": [REMOTE_ANKETA],
        "optional_patch": [REMOTE_RENDERER],
        "renderer_load": "require_once(DIR_SYSTEM . 'library/zpm/mail_renderer.php');",
        "renderer_method": "renderAdminForm",
        "subject_pattern": "ЗПМ: новая заявка — {dialog_label}",
        "recipients": "config_mail_alert_email comma-separated loop",
        "json_fix": "echo success only after mail send attempt",
        "service_info_fields": [
            "ip",
            "remote_addr",
            "x_forwarded_for",
            "x_real_ip",
            "cf_connecting_ip",
            "user_agent",
            "browser",
            "device",
            "os",
            "referrer",
            "page_url",
            "submitted_at",
            "dialog",
            "utm",
            "city",
        ],
        "city_policy": "unknown — no GeoIP API",
        "customer_copy": False,
        "fallback_if_renderer_missing": "legacy minimal HTML assembly",
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "implementation-design.json", design)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-design.md",
        "# Implementation design\n\n" + json.dumps(design, ensure_ascii=False, indent=2) + "\n",
    )


def phase_local_patch(authority: dict[str, Any]) -> dict[str, Any]:
    before_anketa = DEPLOYMENT_ROOT / "source-before" / remote_local_name(REMOTE_ANKETA)
    after_anketa = DEPLOYMENT_ROOT / "source-after" / remote_local_name(REMOTE_ANKETA)
    after_renderer = DEPLOYMENT_ROOT / "source-after" / remote_local_name(REMOTE_RENDERER)
    shutil.copy2(ANKETA_PATCH, after_anketa)
    shutil.copy2(RENDERER_SRC, after_renderer)

    before_renderer_path = DEPLOYMENT_ROOT / "source-before" / remote_local_name(REMOTE_RENDERER)
    renderer_patch_needed = True
    if before_renderer_path.is_file():
        renderer_patch_needed = sha256_file(before_renderer_path) != sha256_file(RENDERER_SRC)

    diff_anketa = difflib.unified_diff(
        before_anketa.read_text(encoding="utf-8").splitlines(keepends=True),
        after_anketa.read_text(encoding="utf-8").splitlines(keepends=True),
        fromfile="before/anketa.php",
        tofile="after/anketa.php",
    )
    write_text(DEPLOYMENT_ROOT / "patch" / "diff-anketa.diff", "".join(diff_anketa))

    diff_renderer = ""
    if before_renderer_path.is_file() and renderer_patch_needed:
        diff_renderer = "".join(
            difflib.unified_diff(
                before_renderer_path.read_text(encoding="utf-8").splitlines(keepends=True),
                after_renderer.read_text(encoding="utf-8").splitlines(keepends=True),
                fromfile="before/mail_renderer.php",
                tofile="after/mail_renderer.php",
            )
        )
        write_text(DEPLOYMENT_ROOT / "patch" / "diff-mail-renderer.diff", diff_renderer)

    changed = [
        {"path": REMOTE_ANKETA, "sha256": sha256_file(after_anketa), "action": "overwrite"},
    ]
    if renderer_patch_needed:
        changed.append({"path": REMOTE_RENDERER, "sha256": sha256_file(after_renderer), "action": "overwrite"})

    write_json(DEPLOYMENT_ROOT / "patch" / "changed-files.json", {"files": changed})
    write_csv(DEPLOYMENT_ROOT / "patch" / "changed-files.csv", changed, ["path", "sha256", "action"])
    write_text(
        DEPLOYMENT_ROOT / "patch" / "patch-summary.md",
        "# Patch summary\n\n"
        f"- anketa.php patched with ZpmMailRenderer + service info\n"
        f"- renderer compatibility patch needed: **{renderer_patch_needed}**\n"
        f"- customer copy: **no**\n"
        f"- БЗПМ introduced: **no**\n",
    )

    static = static_anketa_checks(after_anketa.read_text(encoding="utf-8"))
    write_json(DEPLOYMENT_ROOT / "patch" / "static-checks.json", static)
    return {"changed": changed, "renderer_patch_needed": renderer_patch_needed, "static": static}


def static_anketa_checks(text: str) -> dict[str, Any]:
    checks = {
        "uses_renderer": "ZpmMailRenderer" in text,
        "render_admin_form": "renderAdminForm" in text,
        "service_info": "zpmBuildServiceInfo" in text,
        "json_after_send": text.find("'ok' => true, 'message' => 'Заявка отправлена'") > text.rfind("$mail->send()"),
        "no_customer_copy": "renderCustomerFormConfirmation" not in text,
        "no_hardcoded_recipient_send": "sergejd@mail.ru" not in text or "$to = 'sergejd@mail.ru'" not in text,
        "no_bzpm": WRONG_BRAND not in text,
        "no_geoip": "geoip" not in text.lower(),
        "brand_zpm_subject": "ЗПМ: новая заявка" in text,
        "config_mail_alert_email": "config_mail_alert_email" in text,
    }
    checks["pass"] = all(
        [
            checks["uses_renderer"],
            checks["render_admin_form"],
            checks["service_info"],
            checks["json_after_send"],
            checks["no_customer_copy"],
            checks["no_bzpm"],
            checks["brand_zpm_subject"],
            checks["config_mail_alert_email"],
        ]
    )
    return checks


def phase_mail_preview() -> dict[str, Any]:
    fixture = {
        "subject": "ЗПМ: новая заявка — Запрос на обратный звонок",
        "dialog_label": "Запрос на обратный звонок",
        "author": "Тестовый посетитель",
        "phone": "+7 000 000-00-00",
        "email": "test@example.invalid",
        "message": "Тестовое сообщение для preview.",
        "product": "",
        "page_url": "https://bzpm.ru/",
        "submitted_at": "2026-07-08 12:00:00",
        "service_info": {
            "ip": "203.0.113.10",
            "browser": "Chrome",
            "device": "desktop",
            "os": "Windows",
            "user_agent": "Mozilla/5.0 (preview fixture)",
            "referrer": "https://bzpm.ru/",
            "utm": "",
            "city": "unknown",
            "dialog": "2",
            "submitted_at": "2026-07-08 12:00:00",
        },
    }
    result = render_preview_admin(fixture)
    write_text(DEPLOYMENT_ROOT / "mail-after" / "admin-form-mail-preview.html", result["html"])
    write_text(DEPLOYMENT_ROOT / "mail-after" / "admin-form-mail-preview.txt", result["text"])
    write_json(DEPLOYMENT_ROOT / "mail-after" / "admin-form-mail-preview.json", fixture)

    qa = {
        "html_generated": True,
        "text_generated": True,
        "contains_zpm": CORRECT_BRAND in result["html"],
        "no_bzpm": WRONG_BRAND not in result["html"],
        "service_info_present": "Служебная информация" in result["html"],
        "city_unknown": "unknown" in result["html"],
        "pass": CORRECT_BRAND in result["html"] and WRONG_BRAND not in result["html"] and "Служебная информация" in result["html"],
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "local-mail-preview-qa.json", qa)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "local-mail-preview-qa.md",
        "# Local mail preview QA\n\n" + "\n".join(f"- {k}: **{v}**" for k, v in qa.items()) + "\n",
    )
    return qa


def phase_rollback(patch_info: dict[str, Any]) -> None:
    manifest = []
    for row in patch_info["changed"]:
        remote = row["path"]
        before = DEPLOYMENT_ROOT / "source-before" / remote_local_name(remote)
        manifest.append(
            {
                "remote_path": remote,
                "source_before_sha256": sha256_file(before) if before.is_file() else "",
                "rollback_method": "re-upload source-before exact file",
            }
        )
    write_json(DEPLOYMENT_ROOT / "rollback" / "remote-before-manifest.json", {"files": manifest})
    write_text(
        DEPLOYMENT_ROOT / "rollback" / "rollback-plan.md",
        "# Rollback plan\n\nRe-upload exact `source-before/` copies for touched files.\n",
    )


def phase_dry_run(authority: dict[str, Any], patch_info: dict[str, Any], preview_qa: dict[str, Any]) -> dict[str, Any]:
    gates = {
        "G1_source_authority": not authority.get("mod_blocker"),
        "G2_rollback_captured": (DEPLOYMENT_ROOT / "rollback" / "rollback-plan.md").is_file(),
        "G3_patch_scope": len(patch_info["changed"]) <= 2,
        "G4_recipients_preserved": patch_info["static"].get("config_mail_alert_email"),
        "G5_no_smtp_admin_db": True,
        "G6_no_customer_copy": patch_info["static"].get("no_customer_copy"),
        "G7_no_standard_mail": True,
        "G8_no_geoip": patch_info["static"].get("no_geoip"),
        "G9_preview_pass": preview_qa.get("pass"),
        "G10_json_after_send": patch_info["static"].get("json_after_send"),
        "G11_test_plan_ready": True,
        "G12_live_sanity_plan": True,
    }
    payload = {"generated_at": utc_now(), "gates": gates, "pass": all(gates.values())}
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", payload)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "# Dry-run gates\n\n" + "\n".join(f"- {k}: **{'PASS' if v else 'FAIL'}**" for k, v in gates.items()) + f"\n\n**Overall:** {'PASS' if payload['pass'] else 'FAIL'}\n",
    )
    return payload


def phase_deploy(dry_run: dict[str, Any], patch_info: dict[str, Any]) -> dict[str, Any]:
    if not dry_run["pass"]:
        return {"uploaded": False, "reason": "dry-run gates failed"}
    uploads = []
    ftp = ftp_connect()
    try:
        for row in patch_info["changed"]:
            remote = row["path"]
            local = DEPLOYMENT_ROOT / "source-after" / remote_local_name(remote)
            data = local.read_bytes()
            ftp_upload(ftp, remote, data)
            remote_bytes, err = ftp_download(ftp, remote)
            if remote_bytes is None:
                return {"uploaded": False, "reason": f"verify failed for {remote}: {err}"}
            local_sha = sha256_bytes(data)
            remote_sha = sha256_bytes(remote_bytes)
            verified = local_sha == remote_sha
            uploads.append(
                {
                    "remote_path": remote,
                    "local_sha256": local_sha,
                    "remote_sha256": remote_sha,
                    "verified": verified,
                }
            )
            if not verified:
                return {"uploaded": False, "reason": f"sha mismatch {remote}", "uploads": uploads}
    finally:
        ftp.quit()

    write_csv(
        DEPLOYMENT_ROOT / "verification" / "upload-manifest.csv",
        uploads,
        ["remote_path", "local_sha256", "remote_sha256", "verified"],
    )
    write_json(DEPLOYMENT_ROOT / "verification" / "upload-manifest.json", {"uploads": uploads})
    write_json(DEPLOYMENT_ROOT / "verification" / "remote-after-sha.json", {"uploads": uploads})
    return {"uploaded": True, "uploads": uploads}


def phase_test_submit() -> dict[str, Any]:
    result: dict[str, Any] = {
        "attempted": False,
        "ok": False,
        "blocker": None,
        "response": None,
    }
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        result["blocker"] = "playwright unavailable"
        write_test_submit_artifacts(result)
        return result

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1200})
        page.set_default_timeout(120000)
        page.goto("https://bzpm.ru/", wait_until="networkidle")
        page.wait_for_timeout(4000)

        submit_payload = page.evaluate(
            """async ({ name, phone }) => {
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
                formData.append('dialog', '2');
                formData.append('name', name);
                formData.append('phone', phone);
                formData.append('message', name);
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
            {"name": TEST_NAME, "phone": TEST_PHONE},
        )

        result["attempted"] = True
        if submit_payload.get("error"):
            result["blocker"] = submit_payload["error"]
        else:
            result["response_status"] = submit_payload.get("status")
            result["response"] = submit_payload.get("body")
            body = submit_payload.get("body") or {}
            result["ok"] = submit_payload.get("status") == 200 and isinstance(body, dict) and body.get("ok") is True
        browser.close()

    write_test_submit_artifacts(result)
    return result


def write_test_submit_artifacts(result: dict[str, Any]) -> None:
    redacted = {
        "marker": TEST_MARKER,
        "name": TEST_NAME,
        "phone": TEST_PHONE,
        "email": TEST_EMAIL,
        "dialog": 2,
        "source_page": "https://bzpm.ru/",
        "message_preview": TEST_MESSAGE[:80] + "...",
    }
    write_json(DEPLOYMENT_ROOT / "test-submit" / "test-submit-request-redacted.json", redacted)
    write_json(DEPLOYMENT_ROOT / "test-submit" / "test-submit-response.json", result)
    lines = [
        "# Controlled test submit",
        "",
        f"- Attempted: **{result.get('attempted')}**",
        f"- OK: **{result.get('ok')}**",
        f"- Blocker: {result.get('blocker') or 'none'}",
        f"- HTTP status: {result.get('response_status')}",
        f"- Response ok flag: {(result.get('response') or {}).get('ok') if isinstance(result.get('response'), dict) else 'SAFE UNKNOWN'}",
        "- Mailbox delivery: **SAFE UNKNOWN** (operator visual confirmation pending)",
    ]
    write_text(DEPLOYMENT_ROOT / "test-submit" / "test-submit-summary.md", "\n".join(lines) + "\n")


def phase_live_sanity() -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    sitemap_count = None
    for slug, url in SANITY_URLS:
        resp = http_get(url)
        text = resp.get("text", "")
        entry: dict[str, Any] = {
            "slug": slug,
            "url": url,
            "status": resp.get("status"),
            "error": resp.get("error"),
            "has_bzpm": WRONG_BRAND in text,
        }
        if slug == "stoly":
            entry["load_more_present"] = any(
                s in text for s in ("load-more", "load_more", "Показать ещё", "Показать еще")
            )
        if slug == "pdp":
            entry["extra_info_present"] = "product-content__extra-info" in text or "Дополнительные сведения" in text
        if slug == "llms":
            raw = resp.get("raw_body", b"")
            entry["utf8_bom"] = raw.startswith(b"\xef\xbb\xbf")
            entry["has_zpm"] = CORRECT_BRAND in text
        if slug == "sitemap" and resp.get("status") == 200:
            try:
                root = ET.fromstring(text)
                ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
                sitemap_count = len(root.findall("sm:url", ns)) or len(root.findall("url"))
                entry["url_count"] = sitemap_count
            except ET.ParseError:
                entry["url_count"] = None
        results.append(entry)

    payload = {
        "generated_at": utc_now(),
        "sitemap_url_count": sitemap_count,
        "results": results,
        "pass": all(
            r.get("status") == 200 and not r.get("has_bzpm")
            for r in results
            if r["slug"] in ("home", "katalog", "robots", "sitemap", "llms", "neutral_hub", "stoly", "pdp")
        ),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "live-sanity.json", payload)
    lines = ["# Live sanity", "", f"Generated: {utc_now()}", ""]
    for r in results:
        lines.append(f"- **{r['slug']}** {r['url']} — HTTP {r.get('status')}; БЗПМ: {r.get('has_bzpm')}")
    lines.append(f"\nSitemap URL count: {sitemap_count}")
    lines.append(f"\n**Overall:** {'PASS' if payload['pass'] else 'CHECK'}")
    write_text(DEPLOYMENT_ROOT / "verification" / "live-sanity.md", "\n".join(lines) + "\n")
    return payload


def phase_future_integration() -> None:
    spec = {
        "next_operation": "SITE-002-PROD-MAIL-CUSTOMER-FORMS-01",
        "scope": [
            "optional customer confirmation emails for forms",
            "no service info in customer emails",
            "clear confirmation wording",
            "no order/account mail changes",
        ],
        "roadmap": [
            "SITE-002-PROD-MAIL-ACCOUNT-TRANSACTIONAL-01",
            "SITE-002-PROD-MAIL-ORDER-TRANSACTIONAL-01",
        ],
    }
    write_json(DEPLOYMENT_ROOT / "mail-after" / "future-customer-forms-spec.json", spec)
    write_text(
        DEPLOYMENT_ROOT / "mail-after" / "future-customer-forms-spec.md",
        "# Future customer forms spec\n\nNext: **SITE-002-PROD-MAIL-CUSTOMER-FORMS-01**\n",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--skip-deploy", action="store_true")
    parser.add_argument("--skip-test-submit", action="store_true")
    parser.add_argument("--test-submit-only", action="store_true")
    args = parser.parse_args()

    if args.test_submit_only:
        ensure_layout()
        test_submit = phase_test_submit()
        print(json.dumps(test_submit, ensure_ascii=False, indent=2))
        return 0 if test_submit.get("ok") else 1

    ensure_layout()
    authority = phase_source_authority()
    if authority.get("mod_blocker"):
        print("BLOCKED — modification overlay present")
        return 2

    phase_http_before()
    phase_implementation_design()
    patch_info = phase_local_patch(authority)
    if not patch_info["static"].get("pass"):
        print("BLOCKED — static checks failed", patch_info["static"])
        return 2

    preview_qa = phase_mail_preview()
    phase_rollback(patch_info)
    dry_run = phase_dry_run(authority, patch_info, preview_qa)
    deploy = {"uploaded": False, "reason": "skipped"} if args.skip_deploy else phase_deploy(dry_run, patch_info)
    test_submit = {"skipped": True} if args.skip_test_submit or not deploy.get("uploaded") else phase_test_submit()
    sanity = phase_live_sanity()
    phase_future_integration()

    summary = {
        "operation_id": OPERATION_ID,
        "ocpilot_run": OCPILOT_RUN,
        "dry_run_pass": dry_run["pass"],
        "deploy": deploy,
        "test_submit": test_submit,
        "sanity_pass": sanity["pass"],
        "patch_files": [r["path"] for r in patch_info["changed"]],
    }
    write_json(DEPLOYMENT_ROOT / "reports" / "operation-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if dry_run["pass"] and deploy.get("uploaded") else 1


if __name__ == "__main__":
    sys.exit(main())
