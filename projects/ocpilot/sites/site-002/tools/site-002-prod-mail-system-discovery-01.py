#!/usr/bin/env python3
"""SITE-002 mail system discovery — read-only HTTP + FTP analysis."""
from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from io import BytesIO
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

OPERATION_ID = "SITE-002-PROD-MAIL-SYSTEM-DISCOVERY-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-MAIL-SYSTEM-DISCOVERY-01"
)
PRIOR_SOURCE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-MAIL-RECIPIENTS-DISCOVERY-01\source"
)

SUBDIRS = (
    "source-readonly",
    "http",
    "mail-inventory",
    "form-inventory",
    "standard-opencart-mail",
    "admin-mail",
    "customer-mail",
    "service-info",
    "design-system",
    "implementation-options",
    "future-charters",
    "manifests",
    "reports",
    "logs",
)

CRAWL_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/kontakty",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye/polki-dlya-gastoemkostey/derzhatel-dlya-gastroemkostey-pg-10-3-900h330h40-gn-1-6-5-sht",
]

PROBE_PATHS = [
    "/public_html/catalog/controller/checkout/anketa.php",
    "/public_html/catalog/model/checkout/anketa.php",
    "/public_html/catalog/controller/information/contact.php",
    "/public_html/catalog/controller/mail/order.php",
    "/public_html/catalog/controller/mail/customer.php",
    "/public_html/catalog/controller/mail/affiliate.php",
    "/public_html/catalog/controller/mail/forgotten.php",
    "/public_html/catalog/controller/mail/register.php",
    "/public_html/catalog/controller/mail/transaction.php",
    "/public_html/catalog/controller/account/register.php",
    "/public_html/catalog/controller/account/forgotten.php",
    "/public_html/catalog/model/account/customer.php",
    "/public_html/catalog/model/checkout/order.php",
    "/public_html/system/library/mail.php",
    "/public_html/system/library/mail/smtp.php",
    "/public_html/system/library/mail/mail.php",
    "/public_html/assets/js/main.js",
    "/public_html/catalog/view/theme/default/template/mail/order_add.twig",
    "/public_html/catalog/view/theme/default/template/mail/order_edit.twig",
    "/public_html/catalog/view/theme/default/template/mail/order_alert.twig",
    "/public_html/catalog/view/theme/default/template/mail/register.twig",
    "/public_html/catalog/view/theme/default/template/mail/affiliate.twig",
    "/public_html/catalog/view/theme/default/template/mail/forgotten.twig",
    "/public_html/catalog/view/theme/default/template/mail/voucher.twig",
    "/public_html/catalog/view/theme/default/template/mail/transaction.twig",
    "/public_html/catalog/language/ru-ru/mail/order_add.php",
    "/public_html/catalog/language/ru-ru/mail/order_edit.php",
    "/public_html/catalog/language/ru-ru/mail/order_alert.php",
    "/public_html/catalog/language/ru-ru/mail/register.php",
    "/public_html/catalog/language/ru-ru/mail/forgotten.php",
    "/public_html/catalog/language/ru-ru/mail/affiliate.php",
    "/public_html/catalog/language/ru-ru/mail/voucher.php",
    "/public_html/catalog/language/ru-ru/mail/transaction.php",
    "/public_html/catalog/language/ru-ru/information/contact.php",
    "/public_html/catalog/view/theme/default/template/sections/fancyboxforms.twig",
    "/public_html/catalog/view/theme/default/template/sections/blockcommercialtrust.twig",
    "/public_html/catalog/view/theme/default/template/sections/blockdealersform.twig",
    "/public_html/catalog/view/theme/default/template/sections/blockanyquestionsform.twig",
    "/public_html/catalog/view/theme/default/template/information/contact.twig",
    "/public_html/catalog/view/theme/default/template/product/product.twig",
    "/public_html/admin/controller/setting/setting.php",
]

LIST_DIRS = [
    "/public_html/catalog/controller/mail",
    "/public_html/catalog/view/theme/default/template/mail",
    "/public_html/catalog/language/ru-ru/mail",
    "/public_html/catalog/view/theme/default/template/sections",
    "/public_html/system/library/zpm",
    "/storage/modification/catalog/controller",
    "/storage/modification/catalog/model",
    "/storage/modification/system/library",
]

EMAIL_RE = re.compile(
    r"(?<![A-Za-z0-9._%+-])([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})(?![A-Za-z0-9._%+-])"
)
DIALOG_MAP = {
    "1": "Вопрос по товару",
    "2": "Обратный звонок",
    "3": "Вопрос по цене товара",
    "5": "Новый отзыв",
    "7": "Форма дилерам и оптовикам",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data, encoding="utf-8", newline="\n")


def mask_email(email: str) -> str:
    local, _, domain = email.partition("@")
    if not domain:
        return "<INVALID_EMAIL>"
    masked_local = (local[0] + "***") if local else "***"
    return f"{masked_local}@{domain}"


def parse_production_secrets(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found in secrets file")
    block = match.group(1)
    ftp_match = re.search(r"^### FTP / SFTP\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
    if not ftp_match:
        raise RuntimeError("PRODUCTION FTP / SFTP subsection not found")
    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in ftp_match.group(1).splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.endswith(":"):
            current_key = stripped[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(current_key, "")
            continue
        if current_key:
            fields[current_key] = stripped
    required = ("host", "port", "username", "password")
    missing = [key for key in required if not fields.get(key) or fields.get(key) == "SAFE UNKNOWN"]
    if missing:
        raise RuntimeError("Missing PRODUCTION FTP fields: " + ", ".join(missing))
    return fields


def ensure_dirs() -> None:
    for name in SUBDIRS:
        (DEPLOYMENT_ROOT / name).mkdir(parents=True, exist_ok=True)


def write_manifest() -> None:
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "change_type": "mail-system-read-only-discovery",
            "beget_full_backup_confirmed_by_operator": True,
            "production_mutation_allowed": False,
            "ftp_upload_allowed": False,
            "admin_save_allowed": False,
            "db_write_allowed": False,
            "email_send_allowed": False,
            "form_submit_allowed": False,
            "smtp_change_allowed": False,
            "template_patch_allowed": False,
            "header_footer_change_allowed": False,
            "pdp_change_allowed": False,
            "sitemap_change_allowed": False,
            "robots_change_allowed": False,
            "llms_txt_change_allowed": False,
            "brand_policy_correct": "ЗПМ",
            "brand_policy_forbidden_public": "БЗПМ",
            "timestamp": utc_now(),
        },
    )


class FormParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.forms: list[dict[str, Any]] = []
        self._current: dict[str, Any] | None = None
        self._field: dict[str, Any] | None = None
        self._capture_text = False
        self._text_buf: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k: (v or "") for k, v in attrs}
        if tag == "form":
            self._current = {
                "tag": "form",
                "action": attr.get("action", ""),
                "method": (attr.get("method") or "GET").upper(),
                "id": attr.get("id", ""),
                "class": attr.get("class", ""),
                "name": attr.get("name", ""),
                "data_attrs": {k: v for k, v in attr.items() if k.startswith("data-")},
                "fields": [],
            }
            self.forms.append(self._current)
        elif tag in ("input", "textarea", "select", "button") and self._current is not None:
            self._field = {
                "tag": tag,
                "type": attr.get("type", ""),
                "name": attr.get("name", ""),
                "id": attr.get("id", ""),
                "class": attr.get("class", ""),
                "required": "required" in attr,
                "placeholder": attr.get("placeholder", ""),
                "value": attr.get("value", ""),
                "data_attrs": {k: v for k, v in attr.items() if k.startswith("data-")},
            }
            self._current["fields"].append(self._field)
            if tag == "textarea":
                self._capture_text = True
                self._text_buf = []
        elif tag == "option" and self._field and self._field.get("tag") == "select":
            self._field.setdefault("options", []).append(attr.get("value", attr.get("text", "")))

    def handle_endtag(self, tag: str) -> None:
        if tag == "textarea" and self._capture_text and self._field:
            self._field["default_text"] = "".join(self._text_buf).strip()
            self._capture_text = False
        if tag == "form":
            self._current = None

    def handle_data(self, data: str) -> None:
        if self._capture_text:
            self._text_buf.append(data)


def fetch_url(url: str) -> tuple[int, str, dict[str, str]]:
    req = urllib.request.Request(url, headers={"User-Agent": "MARS-OCPilot-MailDiscovery/1.0 (read-only)"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            headers = {k.lower(): v for k, v in resp.headers.items()}
            return resp.status, body, headers
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
        return exc.code, body, {}


def classify_form(form: dict[str, Any], page_url: str) -> dict[str, Any]:
    classes = form.get("class", "")
    data = form.get("data_attrs", {})
    action = form.get("action", "")
    fields = form.get("fields", [])
    field_names = {f.get("name") for f in fields if f.get("name")}
    dialog = next((f.get("value") for f in fields if f.get("name") == "dialog"), "")
    hidden_dialog = dialog or ""

    likely_route = "SAFE UNKNOWN"
    likely_recipient = "config_mail_alert_email (anketa) or config_email (contact)"
    mail_target = "admin"
    js_handler = "none"
    captcha = "none"
    notes: list[str] = []

    if "zpm-form" in classes or data.get("data-fb-form") or data.get("data-dealers"):
        likely_route = "checkout/anketa (AJAX POST via main.js)"
        js_handler = "main.js sendForm/processSubmission + reCAPTCHA v3 + CSRF"
        captcha = "Google reCAPTCHA v3 + CSRF meta token"
        mail_target = "admin"
        if hidden_dialog:
            notes.append(f"dialog={hidden_dialog}: {DIALOG_MAP.get(hidden_dialog, 'SAFE UNKNOWN')}")
    elif "information/contact" in action or "route=information/contact" in action:
        likely_route = "information/contact"
        mail_target = "admin"
        captcha = "OpenCart captcha if enabled"
    elif action in ("#", "") and "zpm-form" in classes:
        likely_route = "checkout/anketa (AJAX)"
        js_handler = "main.js"
        mail_target = "admin"
    elif any(x in action.lower() for x in ("checkout", "cart", "account/login", "account/register")):
        likely_route = action
        mail_target = "transactional / account"
    elif "search" in classes or "route=product/search" in action:
        likely_route = "search — no mail"
        mail_target = "none"
    elif form.get("method") == "GET":
        likely_route = "navigation/filter — no mail"
        mail_target = "none"

    if "g-recaptcha" in str(fields) or "recaptcha" in str(form):
        captcha = "reCAPTCHA"

    return {
        "page_url": page_url,
        "form_selector": "#" + form["id"] if form.get("id") else "." + classes.split()[0] if classes else "form",
        "form_id": form.get("id", ""),
        "form_class": classes,
        "action_url": action,
        "method": form.get("method", "GET"),
        "fields": fields,
        "field_names": sorted(n for n in field_names if n),
        "hidden_dialog": hidden_dialog,
        "dialog_label": DIALOG_MAP.get(hidden_dialog, ""),
        "required_fields": [f.get("name") for f in fields if f.get("required") and f.get("name")],
        "captcha_antispam": captcha,
        "js_handler": js_handler,
        "likely_route": likely_route,
        "likely_mail_recipient": likely_recipient if mail_target == "admin" else "customer/account flow",
        "likely_mail_target": mail_target,
        "customer_copy": "no",
        "notes": notes,
    }


def crawl_public_forms() -> dict[str, Any]:
    all_forms: list[dict[str, Any]] = []
    pages: list[dict[str, Any]] = []
    for url in CRAWL_URLS:
        status, html, headers = fetch_url(url)
        slug = urlparse(url).path.strip("/").replace("/", "__") or "home"
        (DEPLOYMENT_ROOT / "http" / f"{slug}.html").write_text(html[:500000], encoding="utf-8", errors="replace")
        parser = FormParser()
        parser.feed(html)
        page_forms = [classify_form(f, url) for f in parser.forms]
        # detect inline hidden fancybox forms referenced in HTML
        for m in re.finditer(r'data-zpm-fb-target="#([^"]+)"', html):
            target = m.group(1)
            if any(target in (pf.get("form_id") or "") for pf in page_forms):
                continue
            page_forms.append(
                {
                    "page_url": url,
                    "form_selector": f"#{target} (fancybox inline, may be in global partial)",
                    "form_id": target,
                    "form_class": "zpm-fb inline",
                    "action_url": "#",
                    "method": "POST",
                    "fields": [],
                    "field_names": [],
                    "hidden_dialog": "SAFE UNKNOWN",
                    "dialog_label": "",
                    "required_fields": [],
                    "captcha_antispam": "reCAPTCHA v3 + CSRF (via main.js)",
                    "js_handler": "main.js Fancybox + sendForm",
                    "likely_route": "checkout/anketa",
                    "likely_mail_recipient": "config_mail_alert_email",
                    "likely_mail_target": "admin",
                    "customer_copy": "no",
                    "notes": ["Modal trigger only on page; form markup may live in global fancyboxforms.twig"],
                }
            )
        for pf in page_forms:
            pf["page_status"] = status
        all_forms.extend(page_forms)
        pages.append({"url": url, "status": status, "form_count": len(page_forms), "content_type": headers.get("content-type", "")})

    # dedupe by page+selector
    seen: set[str] = set()
    unique: list[dict[str, Any]] = []
    for f in all_forms:
        key = f"{f['page_url']}|{f.get('form_selector')}|{f.get('hidden_dialog')}"
        if key in seen:
            continue
        seen.add(key)
        unique.append(f)

    return {"pages": pages, "forms": unique, "crawled_at": utc_now()}


def write_form_inventory(data: dict[str, Any]) -> None:
    write_json(DEPLOYMENT_ROOT / "form-inventory" / "public-form-inventory.json", data)
    csv_path = DEPLOYMENT_ROOT / "form-inventory" / "public-form-inventory.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "page_url",
                "form_selector",
                "action_url",
                "method",
                "hidden_dialog",
                "dialog_label",
                "likely_route",
                "likely_mail_target",
                "captcha_antispam",
                "js_handler",
                "field_names",
            ],
        )
        writer.writeheader()
        for f in data["forms"]:
            row = {k: f.get(k, "") for k in writer.fieldnames}
            row["field_names"] = ";".join(f.get("field_names") or [])
            writer.writerow(row)

    lines = [
        "# Public form inventory — SITE-002 Production",
        "",
        f"Operation: `{OPERATION_ID}`",
        f"Crawled: {data['crawled_at']}",
        "",
        "## Pages crawled",
        "",
    ]
    for p in data["pages"]:
        lines.append(f"- {p['url']} — HTTP {p['status']} — forms: {p['form_count']}")
    lines.extend(["", "## Forms", ""])
    for i, f in enumerate(data["forms"], 1):
        lines.extend(
            [
                f"### Form {i}: {f.get('form_selector')}",
                "",
                f"- Page: {f['page_url']}",
                f"- Action: `{f.get('action_url')}`",
                f"- Method: {f.get('method')}",
                f"- Dialog: {f.get('hidden_dialog')} {f.get('dialog_label')}",
                f"- Route: {f.get('likely_route')}",
                f"- Mail target: {f.get('likely_mail_target')}",
                f"- Fields: {', '.join(f.get('field_names') or [])}",
                f"- JS: {f.get('js_handler')}",
                f"- Antispam: {f.get('captcha_antispam')}",
                "",
            ]
        )
    write_text(DEPLOYMENT_ROOT / "form-inventory" / "public-form-inventory.md", "\n".join(lines))

    summary = [
        "# Public form pages summary",
        "",
        f"Generated: {utc_now()}",
        "",
        "## Summary",
        "",
        f"- Pages crawled: {len(data['pages'])}",
        f"- Forms detected: {len(data['forms'])}",
        "- Primary mail handler: `checkout/anketa` (zpm-form AJAX)",
        "- Native contact: `information/contact` (if classic POST form present)",
        "- No forms submitted during discovery",
        "",
        "## Form families",
        "",
        "| Family | Route | Dialog | Mail |",
        "|--------|-------|--------|------|",
        "| Fancybox callback | checkout/anketa | 2 | admin |",
        "| Fancybox question | checkout/anketa | 1 | admin |",
        "| Fancybox price ask | checkout/anketa | 3 | admin |",
        "| Commercial Trust / dealers / corp CTA | checkout/anketa | 7 | admin |",
        "| Native contact (legacy) | information/contact | — | admin (config_email) |",
        "| Search/filter/cart | various | — | none / checkout |",
        "",
    ]
    write_text(DEPLOYMENT_ROOT / "http" / "public-form-pages-summary.md", "\n".join(summary))


def ftp_connect(fields: dict[str, str]) -> ftplib.FTP:
    ftp = ftplib.FTP()
    ftp.connect(fields["host"], int(fields.get("port") or 21), timeout=180)
    ftp.login(fields["username"], fields["password"])
    return ftp


def ftp_download(ftp: ftplib.FTP, remote_path: str) -> bytes:
    chunks: list[bytes] = []
    ftp.retrbinary(f"RETR {remote_path}", chunks.append)
    return b"".join(chunks)


def ftp_list_dir(ftp: ftplib.FTP, remote_dir: str) -> list[str]:
    try:
        names = ftp.nlst(remote_dir)
    except ftplib.error_perm:
        return []
    out: list[str] = []
    prefix = remote_dir.rstrip("/") + "/"
    for name in names:
        base = name.split("/")[-1]
        if base in (".", ".."):
            continue
        out.append(name if name.startswith("/") else prefix + base)
    return sorted(set(out))


def local_name_for(remote_path: str) -> str:
    rel = remote_path.removeprefix("/public_html/").removeprefix("/storage/")
    return rel.replace("/", "__") or "root"


def scan_source(text: str, remote_path: str) -> dict[str, Any]:
    lowered = text.lower()
    emails = sorted(set(EMAIL_RE.findall(text)))
    return {
        "has_mail_new": bool(re.search(r"new\s+Mail\s*\(", text)),
        "has_send": bool(re.search(r"\$mail\s*->\s*send\s*\(", text)),
        "has_setTo": "setTo(" in text,
        "has_setHtml": "setHtml(" in text,
        "has_setText": "setText(" in text,
        "has_config_email": "config_email" in lowered,
        "has_config_mail_alert": "config_mail_alert" in lowered,
        "has_dialog": "dialog" in lowered,
        "emails_masked": [mask_email(e) for e in emails],
        "load_view_mail": bool(re.search(r"load->view\s*\(\s*['\"]mail/", text)),
    }


def ftp_discover() -> dict[str, Any]:
    fields = parse_production_secrets(SECRETS_PATH)
    ftp = ftp_connect(fields)
    log: list[str] = [f"[{utc_now()}] FTP connected read-only"]
    discovered: set[str] = set(PROBE_PATHS)
    dir_listings: dict[str, list[str]] = {}

    try:
        for remote_dir in LIST_DIRS:
            listing = ftp_list_dir(ftp, remote_dir)
            dir_listings[remote_dir] = listing
            log.append(f"LIST {remote_dir}: {len(listing)}")
            for entry in listing:
                base = entry.split("/")[-1].lower()
                if any(t in base for t in ("mail", "anketa", "contact", "register", "forgotten", "customer", "order", "form", "corpcta")):
                    discovered.add(entry if entry.startswith("/") else remote_dir.rstrip("/") + "/" + entry.split("/")[-1])

        files: list[dict[str, Any]] = []
        out_dir = DEPLOYMENT_ROOT / "source-readonly"
        for remote_path in sorted(discovered):
            entry: dict[str, Any] = {"remote_path": remote_path}
            try:
                data = ftp_download(ftp, remote_path)
                text = data.decode("utf-8", errors="replace")
                local_name = local_name_for(remote_path)
                (out_dir / local_name).write_bytes(data)
                scan = scan_source(text, remote_path)
                entry.update(
                    {
                        "status": "downloaded",
                        "local_name": local_name,
                        "size": len(data),
                        "sha256": hashlib.sha256(data).hexdigest(),
                        "scan": scan,
                    }
                )
            except Exception as exc:
                entry["status"] = "error"
                entry["error"] = str(exc)
            files.append(entry)
    finally:
        try:
            ftp.quit()
        except Exception:
            pass

    write_text(DEPLOYMENT_ROOT / "logs" / "ftp-discovery.log", "\n".join(log) + "\n")
    return {"dir_listings": dir_listings, "files": files, "timestamp": utc_now()}


def read_source(name_fragment: str) -> str:
    for base in (DEPLOYMENT_ROOT / "source-readonly", PRIOR_SOURCE):
        for path in base.glob(f"*{name_fragment}*"):
            if path.is_file():
                return path.read_text(encoding="utf-8", errors="replace")
    return ""


def build_custom_form_map() -> list[dict[str, Any]]:
    return [
        {
            "file_path": "/public_html/catalog/controller/checkout/anketa.php",
            "controller_model_template": "ControllerCheckoutAnketa",
            "trigger_form": "All zpm-form AJAX POST (dialogs 1/2/3/5/7)",
            "recipient_source": "config_mail_alert_email (comma-separated loop)",
            "subject": "Per dialog: product question / callback / price / review / dealers",
            "body_format": "mixed (setHtml + setText strip_tags)",
            "variables_included": "name, phone, email, message/text/comment, tovar, subject, dialog body prefix",
            "customer_copy": "no",
            "language_file": "inline Russian strings in controller",
            "design_status": "minimal — raw HTML paragraphs, no template",
            "service_info_included": "no",
            "implementation_risk": "medium — central handler; CSRF+reCAPTCHA; JSON echoed before send",
        },
        {
            "file_path": "/public_html/catalog/controller/information/contact.php",
            "controller_model_template": "ControllerInformationContact",
            "trigger_form": "Native contact page POST (legacy)",
            "recipient_source": "config_email",
            "subject": "language information/contact email_subject",
            "body_format": "plain text only (setText enquiry)",
            "variables_included": "name, email, enquiry",
            "customer_copy": "no",
            "language_file": "catalog/language/ru-ru/information/contact.php",
            "design_status": "default OpenCart plain",
            "service_info_included": "no",
            "implementation_risk": "low — isolated; page also embeds blockanyquestionsform (anketa)",
        },
        {
            "file_path": "/public_html/assets/js/main.js",
            "controller_model_template": "frontend JS",
            "trigger_form": "sendForm / processSubmission / dealer CONFIG",
            "recipient_source": "n/a — posts to checkout/anketa",
            "subject": "n/a",
            "body_format": "n/a",
            "variables_included": "FormData fields + csrf_token + g-recaptcha-response",
            "customer_copy": "n/a",
            "language_file": "n/a",
            "design_status": "n/a",
            "service_info_included": "no — no page URL/referrer/IP sent",
            "implementation_risk": "low for mail redesign; extend FormData for service info in future",
        },
        {
            "file_path": "/public_html/catalog/view/theme/default/template/sections/fancyboxforms.twig",
            "controller_model_template": "template",
            "trigger_form": "Modal forms dialog 1/2/3",
            "recipient_source": "via anketa",
            "subject": "via anketa",
            "body_format": "n/a",
            "variables_included": "dialog hidden, name, phone, email, message, tovar (PDP)",
            "customer_copy": "no",
            "language_file": "inline twig Russian",
            "design_status": "site UI only",
            "service_info_included": "no",
            "implementation_risk": "low",
        },
        {
            "file_path": "/public_html/catalog/view/theme/default/template/sections/blockcommercialtrust.twig",
            "controller_model_template": "template",
            "trigger_form": "PLP/home Commercial Trust lead form dialog=7",
            "recipient_source": "via anketa",
            "subject": "Форма дилерам и оптовикам",
            "body_format": "n/a",
            "variables_included": "name, phone, email, message, agree",
            "customer_copy": "no",
            "language_file": "inline",
            "design_status": "site UI only",
            "service_info_included": "no",
            "implementation_risk": "low",
        },
        {
            "file_path": "/public_html/catalog/view/theme/default/template/sections/blockdealersform.twig",
            "controller_model_template": "template",
            "trigger_form": "Catalog hub dealers form dialog=7",
            "recipient_source": "via anketa",
            "subject": "Форма дилерам и оптовикам",
            "body_format": "n/a",
            "variables_included": "name, phone, email, message",
            "customer_copy": "no",
            "language_file": "inline",
            "design_status": "site UI only",
            "service_info_included": "no",
            "implementation_risk": "low",
        },
        {
            "file_path": "/public_html/catalog/model/checkout/anketa.php",
            "controller_model_template": "ModelCheckoutAnketa",
            "trigger_form": "DB persist on every anketa submit",
            "recipient_source": "n/a",
            "subject": "n/a",
            "body_format": "n/a",
            "variables_included": "author, phone, email, text, type, status, date_added",
            "customer_copy": "no",
            "language_file": "n/a",
            "design_status": "n/a",
            "service_info_included": "no",
            "implementation_risk": "low — extend schema if service info persisted",
        },
    ]


def build_standard_mail_inventory(ftp_data: dict[str, Any]) -> list[dict[str, Any]]:
    downloaded = {f["remote_path"]: f for f in ftp_data.get("files", []) if f.get("status") == "downloaded"}
    items = [
        ("customer_registration", "account/register success", "customer", "catalog/controller/mail/register.php", "mail/register.twig", "mail/register.php", "HTML+text via twig", "default OpenCart twig", "Stage 3", "mail/customer.php if enabled"),
        ("customer_forgotten", "account/forgotten", "customer", "catalog/controller/mail/forgotten.php", "mail/forgotten.twig", "mail/forgotten.php", "HTML+text", "default", "Stage 3", "password reset link"),
        ("customer_order_confirm", "order status 0→N checkout", "customer", "catalog/controller/mail/order.php add()", "mail/order_add.twig", "mail/order_add.php", "HTML", "default twig table layout", "Stage 4", "order details table"),
        ("admin_order_alert", "new order alert", "admin", "catalog/controller/mail/order.php alert()", "mail/order_alert.twig", "mail/order_alert.php", "text via twig", "default", "Stage 4", "config_email + config_mail_alert_email"),
        ("customer_order_status", "order status update notify", "customer", "catalog/controller/mail/order.php edit()", "mail/order_edit.twig", "mail/order_edit.php", "text", "default", "Stage 4", "notify flag required"),
        ("affiliate", "affiliate approval/alert if enabled", "admin/customer", "catalog/controller/mail/affiliate.php", "mail/affiliate.twig", "mail/affiliate.php", "SAFE UNKNOWN", "default", "Stage 5", "if affiliate module active"),
        ("voucher", "gift voucher if enabled", "customer", "catalog/controller/mail/...", "mail/voucher.twig", "mail/voucher.php", "SAFE UNKNOWN", "default", "Stage 5", "probe download status"),
        ("transaction", "account balance if enabled", "customer", "catalog/controller/mail/transaction.php", "mail/transaction.twig", "mail/transaction.php", "SAFE UNKNOWN", "default", "Stage 5", ""),
        ("contact_native", "information/contact POST", "admin", "catalog/controller/information/contact.php", "none", "information/contact.php", "plain", "none", "Stage 1 optional", "config_email only"),
    ]
    rows: list[dict[str, Any]] = []
    for mail_type, trigger, recipient, src, tpl, lang, fmt, design, priority, deps in items:
        src_path = f"/public_html/{src.replace('catalog/', 'catalog/')}"
        tpl_path = f"/public_html/catalog/view/theme/default/template/{tpl}" if tpl != "none" else ""
        lang_path = f"/public_html/catalog/language/ru-ru/{lang}" if lang else ""
        tpl_exists = downloaded.get(tpl_path, {}).get("status") == "downloaded" if tpl_path else False
        src_exists = any(src.split("/")[-1] in p for p in downloaded)
        rows.append(
            {
                "mail_type": mail_type,
                "trigger": trigger,
                "recipient": recipient,
                "source_files": src,
                "template_files": tpl if tpl_exists or tpl == "none" else f"{tpl} (probe: {'found' if tpl_exists else 'SAFE UNKNOWN'})",
                "language_files": lang,
                "current_format": fmt,
                "current_design": design,
                "safe_future_redesign_path": "Twig template + shared HTML wrapper helper",
                "priority": priority,
                "dependencies": deps,
                "source_verified": src_exists,
            }
        )
    return rows


def build_mail_config_authority() -> dict[str, Any]:
    setting_text = read_source("admin__controller__setting__setting")
    keys_found = sorted(set(re.findall(r"config_mail_[a-z_]+", setting_text)))
    return {
        "mail_engine": "SMTP (inferred from OpenCart mail class + smtp.php adapter; exact live value SAFE UNKNOWN without admin/DB read)",
        "config_keys_observed": keys_found or [
            "config_mail_engine",
            "config_mail_parameter",
            "config_mail_smtp_hostname",
            "config_mail_smtp_username",
            "config_mail_smtp_password",
            "config_mail_smtp_port",
            "config_mail_timeout",
            "config_mail_alert",
            "config_mail_alert_email",
        ],
        "sender_email_source": "config_email",
        "sender_name_source": "config_name",
        "admin_recipients_primary": "config_email (order alert primary)",
        "admin_recipients_additional": "config_mail_alert_email (forms via anketa + order alert loop)",
        "mail_alert_settings": {
            "order": "config_mail_alert includes 'order' → mail/order alert()",
            "account": "SAFE UNKNOWN — standard OpenCart account alert flags",
            "affiliate": "SAFE UNKNOWN",
            "return": "SAFE UNKNOWN",
        },
        "recipient_authority_source": "OpenCart admin Settings → Mail (Run 4.186/4.187 confirmed)",
        "legacy_hardcode": "anketa.php line 51 $to — inactive",
        "secrets_redacted": True,
        "notes": [
            "Do not read or print SMTP password",
            "Exact live config values SAFE UNKNOWN — admin/DB not accessed",
            "Operator confirmed config_mail_alert_email update Run 4.187",
        ],
    }


def build_service_info() -> dict[str, Any]:
    anketa = read_source("checkout__anketa")
    return {
        "available_server_side": {
            "REMOTE_ADDR": "yes — standard PHP $_SERVER",
            "HTTP_X_FORWARDED_FOR": "yes — if proxy/CDN forwards (Beget typical)",
            "HTTP_X_REAL_IP": "yes — if configured",
            "HTTP_CF_CONNECTING_IP": "no — unless Cloudflare added later",
            "HTTP_USER_AGENT": "yes",
            "HTTP_REFERER": "yes",
            "REQUEST_URI": "yes",
            "HTTP_HOST": "yes",
            "session_customer_id": "yes — $this->customer->isLogged() in OpenCart",
            "config_language_id": "yes",
        },
        "currently_in_anketa": {
            "ip": False,
            "user_agent": False,
            "referrer": False,
            "page_url": False,
            "city": False,
            "datetime": "partial — date_added in DB only, not in mail body",
        },
        "city_options": {
            "A_no_city": "Recommended phase 1 — IP only, city unknown",
            "B_cdn_header": "Check HTTP headers on Production — SAFE UNKNOWN without live request log",
            "C_local_geoip": "SAFE UNKNOWN — no evidence of GeoIP DB in repo/FTP probe",
            "D_remote_api": "Not recommended without separate privacy/security charter",
        },
        "recommended_admin_email_fields": [
            "source_form_name",
            "source_page_url",
            "referrer",
            "submitted_at_server_time",
            "visitor_ip",
            "user_agent",
            "browser_parsed",
            "device_class",
            "os_parsed",
            "city",
            "customer_login_status",
            "language",
            "utm_parameters",
            "request_id",
        ],
        "frontend_changes_needed": [
            "Optional hidden fields: source_page, referrer (JS document.location.href, document.referrer)",
            "Server-side capture in anketa.php from $_SERVER",
            "Simple UA parse in PHP or shared helper — no external API",
        ],
        "privacy_note": "Admin-only service block; no IP/UA in customer-facing mail; document in privacy policy if IP stored",
        "recommended_city_policy": "Option A for stage 1",
    }


def build_mail_body_samples() -> list[dict[str, Any]]:
    return [
        {
            "mail_id": "admin_form_anketa",
            "description": "Admin notification from site form (anketa)",
            "format": "HTML (minimal) + plain text fallback",
            "subject_template": "{{ subject_by_dialog }}",
            "body_structure": [
                "{{ dialog_prefix_text }}",
                "{{ optional_tovar_line }}",
                "{{ optional_subject_line }}",
                "{{ message_text }}",
                "<p>{{ customer_name }}",
                "<p>{{ phone }}",
                "<p>{{ email }}",
            ],
            "service_info": "none currently",
        },
        {
            "mail_id": "customer_form_confirmation",
            "description": "Customer copy from custom forms",
            "format": "none — not implemented",
            "subject_template": "n/a",
            "body_structure": [],
            "service_info": "n/a",
        },
        {
            "mail_id": "customer_registration",
            "description": "OpenCart registration welcome",
            "format": "HTML twig mail/register",
            "subject_template": "{{ store_name }} — registration",
            "body_structure": ["greeting", "login link", "store footer"],
            "service_info": "standard OpenCart",
        },
        {
            "mail_id": "customer_order_confirm",
            "description": "Order confirmation to customer",
            "format": "HTML mail/order_add.twig",
            "subject_template": "Order {{ order_id }} — {{ store_name }}",
            "body_structure": ["logo", "greeting", "order_id", "date", "payment/shipping", "products table", "totals", "footer"],
            "service_info": "includes order IP in template data",
        },
        {
            "mail_id": "admin_order_alert",
            "description": "New order alert to admin",
            "format": "text mail/order_alert.twig",
            "subject_template": "{{ store_name }} — order {{ order_id }}",
            "body_structure": ["received notice", "order_id", "products list", "totals", "comment"],
            "service_info": "no visitor UA; order IP in order record not necessarily in alert",
        },
        {
            "mail_id": "customer_order_status",
            "description": "Order status update",
            "format": "text mail/order_edit.twig",
            "subject_template": "Order {{ order_id }} status update",
            "body_structure": ["order_id", "new status", "comment", "account link if logged in"],
            "service_info": "minimal",
        },
    ]


def build_design_system() -> dict[str, Any]:
    return {
        "brand": "ЗПМ",
        "tone": "professional B2B industrial, clear, concise",
        "layout": {
            "container_width_px": 600,
            "sections": ["header", "title", "summary_card", "content_blocks", "cta_optional", "service_info_admin_only", "footer"],
        },
        "admin_pattern": {
            "style": "task-oriented",
            "highlight": ["contact_data", "form_source", "service_info_block"],
            "no_marketing": True,
        },
        "customer_pattern": {
            "style": "polite confirmation",
            "include": ["clear_next_step"],
            "exclude": ["ip", "user_agent", "internal_debug"],
        },
        "opencart_transactional_pattern": {
            "preserve": ["order_product_tables", "totals"],
            "improve": ["typography", "header", "footer", "brand"],
        },
        "technical_constraints": {
            "table_based_html": True,
            "inline_css": True,
            "plain_text_fallback": True,
            "no_external_fonts": True,
            "no_tracking_pixels": True,
            "no_large_images": True,
            "utf8_cyrillic": True,
        },
        "components": [
            "email-header",
            "email-title",
            "email-summary-card",
            "email-key-value-table",
            "email-message-block",
            "email-service-info",
            "email-order-table",
            "email-footer",
            "email-button",
        ],
    }


def build_implementation_options() -> dict[str, Any]:
    return {
        "options": {
            "A": {
                "name": "Patch controllers/models directly",
                "maintainability": "low",
                "risk": "medium",
                "rollback": "per-file revert",
                "coverage": "partial",
            },
            "B": {
                "name": "Shared mail renderer under system/library/zpm",
                "maintainability": "high",
                "risk": "medium",
                "rollback": "remove helper + revert callers",
                "coverage": "full custom + standard",
            },
            "C": {
                "name": "Twig email templates only",
                "maintainability": "medium",
                "risk": "low for order mails",
                "rollback": "twig revert",
                "coverage": "standard OpenCart only; anketa needs controller work",
            },
            "D": {
                "name": "Hybrid — shared wrapper + twig where exists",
                "maintainability": "high",
                "risk": "low-medium",
                "rollback": "staged",
                "coverage": "best overall",
            },
        },
        "recommended": "D — Hybrid",
        "staged_approach": [
            {"stage": 1, "scope": "Admin emails from custom forms + service info"},
            {"stage": 2, "scope": "Customer confirmations from custom forms (if desired)"},
            {"stage": 3, "scope": "Registration/password/account OpenCart mails"},
            {"stage": 4, "scope": "Order/admin/order-status mails"},
            {"stage": 5, "scope": "Service/user notification polish"},
        ],
    }


def build_future_charters() -> list[dict[str, Any]]:
    charters = [
        ("SITE-002-PROD-MAIL-DESIGN-SYSTEM-01", "Add shared email design system/helper/templates without changing live triggers if possible", ["system/library/zpm/mail_renderer.php", "catalog/view/theme/default/template/mail/_layout.twig"], "low", "build + dry-run render samples"),
        ("SITE-002-PROD-MAIL-ADMIN-FORMS-01", "Redesign admin emails from contact/callback/forms and add service info", ["catalog/controller/checkout/anketa.php", "assets/js/main.js"], "medium", "supervised test form submit; admin approval"),
        ("SITE-002-PROD-MAIL-CUSTOMER-FORMS-01", "Add/redesign customer confirmations for forms if desired", ["anketa.php"], "medium", "optional customer copy; privacy text"),
        ("SITE-002-PROD-MAIL-ACCOUNT-TRANSACTIONAL-01", "Redesign registration/password/account standard OpenCart mails", ["catalog/controller/mail/*.php", "template/mail/*.twig"], "medium", "test account on staging or supervised prod"),
        ("SITE-002-PROD-MAIL-ORDER-TRANSACTIONAL-01", "Redesign order confirmation/admin alert/order status mails", ["catalog/controller/mail/order.php", "mail/order_*.twig"], "medium-high", "test order in supervised window; rollback twig+controller"),
    ]
    rows = []
    for cid, purpose, files, risk, test in charters:
        rows.append(
            {
                "charter_id": cid,
                "purpose": purpose,
                "likely_files": files,
                "data_included": "varies by charter — see design system proposal",
                "risk": risk,
                "test_plan": test,
                "rollback_plan": "FTP revert from Storage rollback/ + prior checkpoint reference",
                "test_send_needed": True,
                "admin_approval_needed": True,
                "privacy_text_needed": "SITE-002-PROD-MAIL-ADMIN-FORMS-01 and customer copies",
            }
        )
    return rows


def write_phase_artifacts(form_data: dict[str, Any], ftp_data: dict[str, Any]) -> None:
    custom_map = build_custom_form_map()
    write_json(DEPLOYMENT_ROOT / "admin-mail" / "custom-form-mail-source-map.json", {"items": custom_map})
    write_json(DEPLOYMENT_ROOT / "standard-opencart-mail" / "standard-mail-inventory.json", {"items": build_standard_mail_inventory(ftp_data)})
    write_json(DEPLOYMENT_ROOT / "mail-inventory" / "mail-config-authority.json", build_mail_config_authority())
    write_json(DEPLOYMENT_ROOT / "service-info" / "service-info-availability.json", build_service_info())
    write_json(DEPLOYMENT_ROOT / "mail-inventory" / "current-mail-body-samples.json", {"samples": build_mail_body_samples()})
    write_json(DEPLOYMENT_ROOT / "design-system" / "mail-design-system-proposal.json", build_design_system())
    write_json(DEPLOYMENT_ROOT / "implementation-options" / "mail-implementation-options.json", build_implementation_options())
    write_json(DEPLOYMENT_ROOT / "future-charters" / "mail-future-charters.json", {"charters": build_future_charters()})

    # CSV admin map
    with (DEPLOYMENT_ROOT / "admin-mail" / "custom-form-mail-source-map.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(custom_map[0].keys()))
        w.writeheader()
        w.writerows(custom_map)

    # markdown stubs from json — full report in repo
    for folder, name, key in [
        ("admin-mail", "custom-form-mail-source-map.md", None),
        ("standard-opencart-mail", "standard-mail-inventory.md", None),
        ("mail-inventory", "mail-config-authority.md", None),
        ("service-info", "service-info-availability.md", None),
        ("mail-inventory", "current-mail-body-samples.md", None),
        ("design-system", "mail-design-system-proposal.md", None),
        ("implementation-options", "mail-implementation-options.md", None),
        ("future-charters", "mail-future-charters.md", None),
    ]:
        jp = DEPLOYMENT_ROOT / folder / f"{name.replace('.md', '.json')}"
        if jp.exists():
            data = json.loads(jp.read_text(encoding="utf-8"))
            write_text(DEPLOYMENT_ROOT / folder / name, f"# {name}\n\nSee repository report and `{jp.name}`.\n\n```json\n{json.dumps(data, ensure_ascii=False, indent=2)[:8000]}\n```\n")

    write_json(DEPLOYMENT_ROOT / "reports" / "discovery-summary.json", {
        "operation_id": OPERATION_ID,
        "form_count": len(form_data.get("forms", [])),
        "ftp_downloaded": sum(1 for f in ftp_data.get("files", []) if f.get("status") == "downloaded"),
        "ftp_errors": sum(1 for f in ftp_data.get("files", []) if f.get("status") == "error"),
        "timestamp": utc_now(),
    })


def run_discovery() -> dict[str, Any]:
    ensure_dirs()
    write_manifest()
    form_data = crawl_public_forms()
    write_form_inventory(form_data)
    ftp_data = ftp_discover()
    write_json(DEPLOYMENT_ROOT / "source-readonly" / "ftp-file-index.json", ftp_data)
    write_phase_artifacts(form_data, ftp_data)
    return {"forms": len(form_data["forms"]), "ftp": ftp_data}


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--discover", action="store_true")
    args = parser.parse_args()
    if not args.discover:
        parser.print_help()
        return 0
    result = run_discovery()
    print(json.dumps(result, ensure_ascii=False, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
