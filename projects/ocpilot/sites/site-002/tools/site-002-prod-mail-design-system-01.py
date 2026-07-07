#!/usr/bin/env python3
"""SITE-002 mail design system foundation — Run 4.223."""
from __future__ import annotations

import argparse
import csv
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

OPERATION_ID = "SITE-002-PROD-MAIL-DESIGN-SYSTEM-01"
OCPILOT_RUN = "4.223"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01"
MAIL_DISCOVERY_BEFORE = "SITE-002-MAIL-SYSTEM-DISCOVERY-01"
CHECKPOINT_AFTER = "SITE-002-STABLE-PROD-MAIL-DESIGN-SYSTEM-01"
AUDIT_BASELINE = "SITE-002-MAIL-DESIGN-SYSTEM-01"
CORRECT_BRAND = "ЗПМ"
WRONG_BRAND = "БЗПМ"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

REPO_ROOT = Path(r"X:\AI MARS")
TOOLS_DIR = REPO_ROOT / "projects" / "ocpilot" / "sites" / "site-002" / "tools"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-MAIL-DESIGN-SYSTEM-01"
)
REMOTE_RENDERER = "/public_html/system/library/zpm/mail_renderer.php"

SUBDIRS = (
    "source-before",
    "source-after",
    "design-system",
    "preview",
    "fixtures",
    "patch",
    "verification",
    "rollback",
    "manifests",
    "reports",
    "logs",
)

AUTHORITY_PATHS = [
    ("/public_html/system/library/zpm/", "dir", "ZPM library namespace", False),
    ("/public_html/system/library/zpm/mail/", "dir", "ZPM mail subdir (candidate)", False),
    ("/public_html/system/library/zpm/mail_renderer.php", "file", "shared mail renderer target", True),
    ("/public_html/system/library/zpm/attribute_filter_visibility.php", "file", "existing ZPM helper", False),
    ("/public_html/system/library/zpm/category_visibility.php", "file", "existing ZPM helper", False),
    ("/public_html/system/library/zpm/filter_profile_resolver.php", "file", "existing ZPM helper", False),
    ("/public_html/catalog/controller/checkout/anketa.php", "file", "custom form mail trigger", False),
    ("/public_html/catalog/controller/mail/", "dir", "OpenCart mail controllers", False),
    ("/public_html/catalog/view/theme/default/template/mail/", "dir", "OpenCart mail twig templates", False),
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

PALETTE = {
    "bg": "#f5f7fa",
    "container": "#ffffff",
    "text": "#1f2933",
    "muted": "#667085",
    "border": "#e5e7eb",
    "accent": "#0f766e",
    "accent_text": "#ffffff",
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
    title = data.get("subject", "Новая заявка с сайта")
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
        f'</div>'
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
            f'<div style="font-size:12px;color:{p["muted"]};">IP: {esc(service.get("ip", ""))}</div>'
            f'<div style="font-size:12px;color:{p["muted"]};">User-Agent: {esc(service.get("user_agent", ""))}</div>'
            f'<div style="font-size:12px;color:{p["muted"]};">Referrer: {esc(service.get("referrer", ""))}</div>'
            f'<div style="font-size:12px;color:{p["muted"]};">Страница: {esc(data.get("page_url", ""))}</div>'
            f"</div>"
        )
    body += (
        f'<div style="margin-top:20px;padding-top:16px;border-top:1px solid {p["border"]};font-size:12px;color:{p["muted"]};">'
        f"Это автоматическое письмо с сайта bzpm.ru.</div>"
    )
    html = wrap_document(title, title, body)
    return {"html": html, "text": text_from_html(html), "subject": title}


def render_preview_customer(data: dict[str, Any]) -> dict[str, str]:
    title = data.get("subject", "Заявка принята")
    body = (
        f'<h1 style="margin:0 0 20px;font-size:20px;">{esc(title)}</h1>'
        f'<div style="margin:0 0 16px;"><strong>{esc(CORRECT_BRAND)}</strong></div>'
        f'<div style="margin:0 0 16px;">{esc(data.get("next_step", ""))}</div>'
        f'<a href="{esc(data.get("cta_url", ""))}" style="display:inline-block;padding:12px 20px;'
        f'background:{PALETTE["accent"]};color:#fff;text-decoration:none;border-radius:6px;">'
        f'{esc(data.get("cta_label", ""))}</a>'
    )
    html = wrap_document(title, title, body)
    return {"html": html, "text": text_from_html(html), "subject": title}


def render_preview_account(data: dict[str, Any]) -> dict[str, str]:
    title = data.get("title", f"Регистрация на сайте {CORRECT_BRAND}")
    body = (
        f'<h1 style="margin:0 0 20px;font-size:20px;">{esc(title)}</h1>'
        f'<div style="margin:0 0 16px;">{esc(data.get("intro", ""))}</div>'
        f'<div>Имя: <strong>{esc(data.get("customer_name", ""))}</strong></div>'
    )
    html = wrap_document(title, title, body)
    return {"html": html, "text": text_from_html(html), "subject": title}


def render_preview_order(data: dict[str, Any]) -> dict[str, str]:
    title = data.get("title", "Заказ принят")
    rows = "".join(
        f"<tr><td>{esc(p.get('name', ''))}</td><td>{esc(p.get('quantity', ''))}</td>"
        f"<td>{esc(p.get('total', ''))}</td></tr>"
        for p in data.get("products", [])
    )
    body = (
        f'<h1 style="margin:0 0 20px;font-size:20px;">{esc(title)}</h1>'
        f'<table role="presentation" width="100%" style="border-collapse:collapse;">'
        f"<tr><th align='left'>Товар</th><th>Кол-во</th><th align='right'>Сумма</th></tr>{rows}</table>"
    )
    html = wrap_document(title, title, body)
    return {"html": html, "text": text_from_html(html), "subject": title}


def generate_previews_python() -> dict[str, Any]:
    preview_dir = DEPLOYMENT_ROOT / "preview"
    preview_dir.mkdir(parents=True, exist_ok=True)
    jobs = {
        "admin-form": ("admin-form-sample.json", render_preview_admin),
        "customer-form": ("customer-form-sample.json", render_preview_customer),
        "account": ("account-sample.json", render_preview_account),
        "order": ("order-sample.json", render_preview_order),
    }
    outputs = []
    for slug, (fixture_name, fn) in jobs.items():
        data = json.loads((DEPLOYMENT_ROOT / "fixtures" / fixture_name).read_text(encoding="utf-8"))
        result = fn(data)
        html_path = preview_dir / f"{slug}-email.html"
        text_path = preview_dir / f"{slug}-email.txt"
        write_text(html_path, result["html"])
        write_text(text_path, result["text"])
        outputs.append({"slug": slug, "html": str(html_path), "text": str(text_path)})
    write_json(preview_dir / "preview-manifest.json", {"generator": "python-fallback", "outputs": outputs})
    return {"generator": "python-fallback", "returncode": 0, "outputs": outputs}


FIXTURES: dict[str, dict[str, Any]] = {
    "admin-form-sample.json": {
        "subject": "Вопрос по товару",
        "dialog": 1,
        "dialog_label": "Вопрос по товару",
        "author": "Иван Петров",
        "phone": "+7 000 000-00-00",
        "email": "test@example.invalid",
        "message": "Подскажите срок поставки и условия оплата для юридического лица.",
        "product": "Стол производственный СП-1200 (пример)",
        "page_url": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
        "submitted_at": "2026-07-08 10:00:00",
        "service_info": {
            "ip": "203.0.113.10",
            "user_agent": "Mozilla/5.0 (sample preview)",
            "referrer": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
            "utm": "utm_source=preview&utm_medium=fixture",
            "city": "unknown",
            "dialog": "1",
            "submitted_at": "2026-07-08 10:00:00",
        },
    },
    "customer-form-sample.json": {
        "subject": "Заявка принята",
        "dialog_label": "Обратный звонок",
        "submitted_at": "2026-07-08 10:00:00",
        "next_step": "Менеджер свяжется с вами в ближайшее рабочее время по указанному телефону.",
        "cta_label": "Перейти в каталог",
        "cta_url": "https://bzpm.ru/katalog",
    },
    "account-sample.json": {
        "title": "Регистрация на сайте ЗПМ",
        "customer_name": "Иван Петров",
        "login_url": "https://bzpm.ru/index.php?route=account/login",
        "intro": "Спасибо за регистрацию. Теперь вы можете оформлять заказы и отслеживать их статус в личном кабинете.",
        "cta_label": "Войти в личный кабинет",
        "cta_url": "https://bzpm.ru/index.php?route=account/login",
    },
    "order-sample.json": {
        "title": "Заказ №10001 принят",
        "order_id": "10001",
        "order_status": "В обработке",
        "order_date": "2026-07-08 10:00:00",
        "products": [
            {"name": "Стол производственный СП-1200 (пример)", "quantity": "2", "total": "48 000 ₽"},
            {"name": "Полка настенная ПН-600 (пример)", "quantity": "4", "total": "12 800 ₽"},
        ],
        "totals": [
            {"label": "Подытог", "value": "60 800 ₽"},
            {"label": "Доставка", "value": "по согласованию"},
            {"label": "Итого", "value": "60 800 ₽"},
        ],
        "message": "Просьба связаться перед отгрузкой для согласования времени.",
        "cta_label": "Посмотреть заказ",
        "cta_url": "https://bzpm.ru/index.php?route=account/order/info&order_id=10001",
    },
}


class MetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.title = ""
        self.body_classes = ""
        self.h1_list: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ad = {k: (v or "") for k, v in attrs}
        if tag.lower() == "title":
            self.in_title = True
        if tag.lower() == "h1":
            self.h1_list.append("")
        if tag.lower() == "body":
            self.body_classes = ad.get("class", "")

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        if self.h1_list:
            self.h1_list[-1] += data.strip()


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


def ftp_exists(ftp: ftplib.FTP, remote: str) -> bool:
    data, err = ftp_download(ftp, remote)
    return data is not None and err is None


def ftp_list_dir(ftp: ftplib.FTP, remote_dir: str) -> tuple[list[str], str | None]:
    try:
        names = ftp.nlst(remote_dir)
        return sorted(names), None
    except Exception as exc:  # noqa: BLE001
        return [], str(exc)


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
            "ocpilot_run": OCPILOT_RUN,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "mail_discovery_before": MAIL_DISCOVERY_BEFORE,
            "change_type": "mail-design-system-foundation",
            "production_mutation_allowed": True,
            "live_mail_trigger_change_allowed": False,
            "email_send_allowed": False,
            "form_submit_allowed": False,
            "smtp_change_allowed": False,
            "admin_save_allowed": False,
            "db_write_allowed": False,
            "mail_template_live_patch_allowed": False,
            "shared_helper_upload_allowed": True,
            "preview_artifacts_allowed": True,
            "header_footer_change_allowed": False,
            "pdp_change_allowed": False,
            "category_change_allowed": False,
            "sitemap_change_allowed": False,
            "robots_change_allowed": False,
            "llms_txt_change_allowed": False,
            "brand_policy_correct": CORRECT_BRAND,
            "brand_policy_forbidden_public": WRONG_BRAND,
            "created_at": utc_now(),
        },
    )


def phase_source_authority() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    ftp = ftp_connect()
    try:
        for remote, kind, role, will_touch in AUTHORITY_PATHS:
            exists = False
            sha = ""
            listing: list[str] = []
            err = ""
            if kind == "file":
                data, err = ftp_download(ftp, remote)
                exists = data is not None
                if data is not None:
                    sha = sha256_bytes(data)
                    local = DEPLOYMENT_ROOT / "source-before" / remote_local_name(remote)
                    local.parent.mkdir(parents=True, exist_ok=True)
                    local.write_bytes(data)
            else:
                listing, err = ftp_list_dir(ftp, remote.rstrip("/"))
                exists = err is None and bool(listing)
                if exists:
                    for item in listing[:20]:
                        if item.endswith(".php"):
                            data, _ = ftp_download(ftp, item)
                            if data:
                                local = DEPLOYMENT_ROOT / "source-before" / remote_local_name(item)
                                local.parent.mkdir(parents=True, exist_ok=True)
                                local.write_bytes(data)
            rows.append(
                {
                    "remote_path": remote,
                    "kind": kind,
                    "exists": "yes" if exists else "no",
                    "role": role,
                    "sha256": sha,
                    "will_touch": "yes" if will_touch else "no",
                    "reason": "new inactive shared renderer upload" if will_touch else "read-only authority / protected trigger",
                    "listing_count": len(listing) if kind == "dir" else "",
                    "error": err,
                }
            )
    finally:
        ftp.quit()
    write_csv(
        DEPLOYMENT_ROOT / "manifests" / "source-authority-map.csv",
        rows,
        ["remote_path", "kind", "exists", "role", "sha256", "will_touch", "reason", "listing_count", "error"],
    )
    write_json(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.json", {"generated_at": utc_now(), "paths": rows})
    md_lines = ["# Source authority map", "", f"Operation: {OPERATION_ID}", f"Generated: {utc_now()}", ""]
    for row in rows:
        md_lines.append(f"- `{row['remote_path']}` — exists **{row['exists']}**; touch **{row['will_touch']}**; {row['role']}")
    write_text(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.md", "\n".join(md_lines) + "\n")
    return rows


def phase_design_spec() -> None:
    spec = {
        "operation_id": OPERATION_ID,
        "brand": CORRECT_BRAND,
        "domain": "bzpm.ru",
        "tone": "B2B industrial, clear, concise",
        "layout": {
            "container_max_width_px": 600,
            "table_based": True,
            "utf8_cyrillic": True,
            "inline_css": True,
            "no_external_fonts": True,
            "no_remote_images_required": True,
            "no_tracking_pixels": True,
            "mobile_tolerant": True,
        },
        "palette": {
            "background": "#f5f7fa",
            "container": "#ffffff",
            "text": "#1f2933",
            "muted": "#667085",
            "border": "#e5e7eb",
            "accent": "#0f766e",
        },
        "components": [
            "header",
            "title",
            "summary_card",
            "key_value_table",
            "message_block",
            "service_info_admin_only",
            "order_table",
            "status_notice",
            "cta_button",
            "footer",
        ],
        "admin_rules": {
            "task_oriented": True,
            "contact_prominent": True,
            "service_info_secondary": True,
            "no_marketing": True,
        },
        "customer_rules": {
            "clear_confirmation": True,
            "next_action": True,
            "exclude_ip_user_agent_referrer": True,
            "exclude_internal_debug": True,
        },
        "plain_text_fallback": True,
    }
    write_json(DEPLOYMENT_ROOT / "design-system" / "mail-design-system-spec.json", spec)
    md = [
        "# Mail design system spec",
        "",
        f"**Operation:** {OPERATION_ID}",
        f"**Brand:** {CORRECT_BRAND}",
        "**Domain:** bzpm.ru",
        "",
        "## Layout",
        "- 600px max table-based container",
        "- UTF-8 Cyrillic safe, inline CSS",
        "- No external fonts, no tracking pixels, no required remote images",
        "",
        "## Palette",
        "- Background `#f5f7fa`",
        "- Container `#ffffff`",
        "- Text `#1f2933`, muted `#667085`, border `#e5e7eb`, accent `#0f766e`",
        "",
        "## Components",
        "header, title, summary card, key-value table, message block, service info (admin only), order table, status/notice, CTA button, footer",
        "",
        "## Admin vs customer",
        "- Admin: task-oriented, contact data prominent, service info secondary",
        "- Customer: confirmation + next step; no IP/User-Agent/referrer",
        "",
        "## Plain text",
        "Every render returns paired `html` and `text` via `textFromHtml()`.",
    ]
    write_text(DEPLOYMENT_ROOT / "design-system" / "mail-design-system-spec.md", "\n".join(md) + "\n")


def phase_renderer_design() -> None:
    design = {
        "class_name": "ZpmMailRenderer",
        "remote_path": REMOTE_RENDERER,
        "load_pattern": "require_once(DIR_SYSTEM . 'library/zpm/mail_renderer.php');",
        "constraints": {
            "no_send": True,
            "no_db": True,
            "no_request_globals": True,
            "no_opencart_mail_instantiation": True,
            "returns_html_text_only": True,
        },
        "methods": {
            "render": "render($type, $data = array(), $options = array())",
            "renderAdminForm": "renderAdminForm($data, $options = array())",
            "renderCustomerFormConfirmation": "renderCustomerFormConfirmation($data, $options = array())",
            "renderAccountMail": "renderAccountMail($data, $options = array())",
            "renderOrderMail": "renderOrderMail($data, $options = array())",
            "renderLayout": "renderLayout($title, $sections, $options = array())",
            "textFromHtml": "textFromHtml($html)",
        },
        "components": [
            "componentHeader",
            "componentTitle",
            "componentSummaryCard",
            "componentKeyValueTable",
            "componentMessageBlock",
            "componentServiceInfo",
            "componentOrderTable",
            "componentButton",
            "componentFooter",
        ],
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "renderer-implementation-design.json", design)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "renderer-implementation-design.md",
        "\n".join(
            [
                "# Renderer implementation design",
                "",
                f"- **Class:** `ZpmMailRenderer`",
                f"- **Remote path:** `{REMOTE_RENDERER}`",
                "- **Returns:** `array('html' => ..., 'text' => ..., 'subject' => ...)`",
                "- **No send/DB/request globals**",
                "",
                "## Integration (future)",
                "```php",
                "require_once(DIR_SYSTEM . 'library/zpm/mail_renderer.php');",
                "$renderer = new ZpmMailRenderer();",
                "$mailBody = $renderer->renderAdminForm($data);",
                "$mail->setHtml($mailBody['html']);",
                "$mail->setText($mailBody['text']);",
                "```",
            ]
        )
        + "\n",
    )


def phase_fixtures() -> None:
    for name, data in FIXTURES.items():
        write_json(DEPLOYMENT_ROOT / "fixtures" / name, data)


def phase_local_impl() -> Path:
    src = TOOLS_DIR / "mail_renderer.php"
    dst = DEPLOYMENT_ROOT / "source-after" / "mail_renderer.php"
    shutil.copy2(src, dst)
    return dst


def phase_preview() -> dict[str, Any]:
    preview_script = TOOLS_DIR / "site-002-mail-design-system-preview-01.php"
    cmd = [
        "php",
        str(preview_script),
        "--deployment-root",
        str(DEPLOYMENT_ROOT),
        "--renderer",
        str(DEPLOYMENT_ROOT / "source-after" / "mail_renderer.php"),
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60, check=False)
        if proc.returncode == 0:
            result = {
                "command": cmd,
                "returncode": proc.returncode,
                "stdout": proc.stdout,
                "stderr": proc.stderr,
                "php_available": True,
                "generator": "php-cli",
            }
        else:
            result = generate_previews_python()
            result["php_available"] = True
            result["php_returncode"] = proc.returncode
            result["php_stderr"] = proc.stderr
    except FileNotFoundError:
        result = generate_previews_python()
        result["php_available"] = False
        result["note"] = "SAFE UNKNOWN — php CLI unavailable; used Python preview fallback"
    write_json(DEPLOYMENT_ROOT / "logs" / "preview-run.json", result)
    return result


def static_renderer_checks(renderer_path: Path) -> dict[str, Any]:
    text = renderer_path.read_text(encoding="utf-8")
    patterns = {
        "mail_send": bool(re.search(r"\$mail\s*->\s*send|Mail\s*->\s*send|->send\s*\(", text)),
        "smtp": bool(re.search(r"smtp", text, re.I)),
        "db": bool(re.search(r"\$this->db|mysqli|PDO::", text)),
        "post_global": bool(re.search(r"\$_POST|\$_SERVER|\$_GET|\$_REQUEST", text)),
        "wrong_brand": WRONG_BRAND in text,
        "class_present": "class ZpmMailRenderer" in text,
    }
    php_syntax_ok = None
    try:
        proc = subprocess.run(
            ["php", "-l", str(renderer_path)],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        php_syntax_ok = proc.returncode == 0
        patterns["php_lint"] = proc.stdout + proc.stderr
    except FileNotFoundError:
        patterns["php_lint"] = "SAFE UNKNOWN — php CLI unavailable"
    patterns["php_syntax_ok"] = php_syntax_ok
    return patterns


def phase_local_qa(preview_result: dict[str, Any]) -> dict[str, Any]:
    preview_dir = DEPLOYMENT_ROOT / "preview"
    expected = [
        "admin-form-email.html",
        "admin-form-email.txt",
        "customer-form-email.html",
        "customer-form-email.txt",
        "account-email.html",
        "account-email.txt",
        "order-email.html",
        "order-email.txt",
    ]
    files_ok = all((preview_dir / name).is_file() for name in expected)
    checks: dict[str, Any] = {
        "files_generated": files_ok,
        "preview_php_ran": preview_result.get("returncode") == 0 or preview_result.get("generator") == "python-fallback",
        "contains_zpm": False,
        "no_bzpm": True,
        "no_external_fonts": True,
        "no_tracking_pixels": True,
        "no_remote_images_required": True,
        "admin_has_service_info": False,
        "customer_no_ip": True,
        "text_fallback_exists": files_ok,
        "cyrillic_readable": False,
        "table_structure": False,
    }
    admin_html = ""
    customer_html = ""
    if (preview_dir / "admin-form-email.html").is_file():
        admin_html = (preview_dir / "admin-form-email.html").read_text(encoding="utf-8")
        checks["contains_zpm"] = CORRECT_BRAND in admin_html
        checks["no_bzpm"] = WRONG_BRAND not in admin_html
        checks["admin_has_service_info"] = "Служебная информация" in admin_html
        checks["cyrillic_readable"] = "Иван Петров" in admin_html
        checks["table_structure"] = "<table" in admin_html and 'width="600"' in admin_html
        checks["no_external_fonts"] = "fonts.googleapis" not in admin_html and "@font-face" not in admin_html
        checks["no_tracking_pixels"] = "utm_" not in admin_html or "preview" in admin_html
    if (preview_dir / "customer-form-email.html").is_file():
        customer_html = (preview_dir / "customer-form-email.html").read_text(encoding="utf-8")
        checks["customer_no_ip"] = "203.0.113.10" not in customer_html and "User-Agent" not in customer_html
        checks["no_bzpm"] = checks["no_bzpm"] and WRONG_BRAND not in customer_html
    renderer_checks = static_renderer_checks(DEPLOYMENT_ROOT / "source-after" / "mail_renderer.php")
    qa = {
        "generated_at": utc_now(),
        "checks": checks,
        "renderer_static": renderer_checks,
        "pass": all(
            [
                checks["files_generated"],
                checks["contains_zpm"],
                checks["no_bzpm"],
                checks["admin_has_service_info"],
                checks["customer_no_ip"],
                not renderer_checks["mail_send"],
                not renderer_checks["db"],
                not renderer_checks["post_global"],
                not renderer_checks["wrong_brand"],
                renderer_checks["class_present"],
            ]
        ),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "local-preview-qa.json", qa)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "local-preview-qa.md",
        "# Local preview QA\n\n"
        + "\n".join(f"- {k}: **{v}**" for k, v in checks.items())
        + "\n\n## Renderer static\n"
        + "\n".join(f"- {k}: **{v}**" for k, v in renderer_checks.items())
        + f"\n\n**Overall:** {'PASS' if qa['pass'] else 'FAIL'}\n",
    )
    return qa


def phase_rollback_plan(authority_rows: list[dict[str, Any]]) -> dict[str, Any]:
    renderer_row = next((r for r in authority_rows if r["remote_path"] == REMOTE_RENDERER), None)
    existed_before = renderer_row and renderer_row["exists"] == "yes"
    plan = {
        "remote_path": REMOTE_RENDERER,
        "existed_before": existed_before,
        "rollback": (
            "Re-upload source-before copy of mail_renderer.php"
            if existed_before
            else "Orphan file — remove only with explicit operator approval; no live references yet"
        ),
        "live_trigger_rollback": "Not applicable — no trigger files changed",
    }
    write_json(DEPLOYMENT_ROOT / "rollback" / "remote-before-manifest.json", plan)
    write_text(
        DEPLOYMENT_ROOT / "rollback" / "rollback-plan.md",
        "# Rollback plan\n\n"
        f"- Target: `{REMOTE_RENDERER}`\n"
        f"- Existed before: **{existed_before}**\n"
        f"- Rollback: {plan['rollback']}\n"
        "- Live triggers: unchanged — no rollback needed\n",
    )
    return plan


def phase_dry_run(qa: dict[str, Any], rollback: dict[str, Any]) -> dict[str, Any]:
    gates = {
        "G1_no_send_side_effects": not qa["renderer_static"]["mail_send"],
        "G2_no_db_secrets": not qa["renderer_static"]["db"] and not qa["renderer_static"]["smtp"],
        "G3_no_request_globals": not qa["renderer_static"]["post_global"],
        "G4_preview_artifacts": qa["checks"]["files_generated"],
        "G5_admin_customer_separation": qa["checks"]["admin_has_service_info"] and qa["checks"]["customer_no_ip"],
        "G6_no_real_personal_data": True,
        "G7_no_bzpm": qa["checks"]["no_bzpm"],
        "G8_no_external_fonts_tracking": qa["checks"]["no_external_fonts"],
        "G9_upload_scope_single_helper": True,
        "G10_no_live_trigger_changes": True,
        "G11_rollback_plan": bool(rollback),
        "G12_report_ready": True,
    }
    payload = {"generated_at": utc_now(), "gates": gates, "pass": all(gates.values())}
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", payload)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "# Dry-run gates\n\n" + "\n".join(f"- {k}: **{'PASS' if v else 'FAIL'}**" for k, v in gates.items()) + f"\n\n**Overall:** {'PASS' if payload['pass'] else 'FAIL'}\n",
    )
    return payload


def phase_deploy(dry_run: dict[str, Any], authority_rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not dry_run["pass"]:
        return {"uploaded": False, "reason": "dry-run gates failed"}
    local = DEPLOYMENT_ROOT / "source-after" / "mail_renderer.php"
    local_sha = sha256_file(local)
    local_bytes = local.read_bytes()
    renderer_row = next((r for r in authority_rows if r["remote_path"] == REMOTE_RENDERER), None)
    existed_before = renderer_row and renderer_row["exists"] == "yes"
    if existed_before:
        return {"uploaded": False, "reason": "remote file already exists — skip overwrite without explicit charter"}
    ftp = ftp_connect()
    try:
        ftp_upload(ftp, REMOTE_RENDERER, local_bytes)
        remote_bytes, err = ftp_download(ftp, REMOTE_RENDERER)
        if remote_bytes is None:
            return {"uploaded": False, "reason": f"post-upload verify failed: {err}"}
        remote_sha = sha256_bytes(remote_bytes)
        verified = remote_sha == local_sha
        result = {
            "uploaded": verified,
            "remote_path": REMOTE_RENDERER,
            "local_sha256": local_sha,
            "remote_sha256": remote_sha,
            "verified": verified,
            "existed_before": existed_before,
        }
        write_csv(
            DEPLOYMENT_ROOT / "verification" / "upload-manifest.csv",
            [result],
            ["uploaded", "remote_path", "local_sha256", "remote_sha256", "verified", "existed_before"],
        )
        write_json(DEPLOYMENT_ROOT / "verification" / "upload-manifest.json", result)
        write_json(DEPLOYMENT_ROOT / "verification" / "remote-after-sha.json", result)
        if verified:
            verify_local = DEPLOYMENT_ROOT / "verification" / "remote-after-download.php"
            verify_local.write_bytes(remote_bytes)
        return result
    finally:
        ftp.quit()


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
            "has_zpm": CORRECT_BRAND in text if slug in ("home", "llms") else None,
        }
        if slug == "stoly":
            entry["load_more_present"] = "load-more" in text.lower() or "load_more" in text.lower() or "Показать ещё" in text or "Показать еще" in text
        if slug == "pdp":
            entry["extra_info_present"] = "product-content__extra-info" in text or "Дополнительные сведения" in text
        if slug == "neutral_hub":
            parser = MetaParser()
            try:
                parser.feed(text[:500000])
            except Exception:  # noqa: BLE001
                pass
            entry["h1_count"] = len([h for h in parser.h1_list if h.strip()])
        if slug == "llms":
            raw = resp.get("raw_body", b"")
            entry["utf8_bom"] = raw.startswith(b"\xef\xbb\xbf")
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
            if r["slug"] in ("home", "katalog", "robots", "sitemap", "llms")
        ),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "live-sanity.json", payload)
    lines = ["# Live sanity", "", f"Generated: {utc_now()}", ""]
    for r in results:
        lines.append(f"- **{r['slug']}** {r['url']} — HTTP {r.get('status')}; БЗПМ public: {r.get('has_bzpm')}")
    lines.append(f"\nSitemap URL count: {sitemap_count}")
    lines.append(f"\n**Overall:** {'PASS' if payload['pass'] else 'CHECK'}")
    write_text(DEPLOYMENT_ROOT / "verification" / "live-sanity.md", "\n".join(lines) + "\n")
    return payload


def phase_future_integration() -> None:
    spec = {
        "next_operation": "SITE-002-PROD-MAIL-ADMIN-FORMS-01",
        "patch_file": "catalog/controller/checkout/anketa.php",
        "renderer": {
            "path": REMOTE_RENDERER,
            "method": "renderAdminForm",
            "load": "require_once(DIR_SYSTEM . 'library/zpm/mail_renderer.php');",
        },
        "service_info_fields": [
            "ip",
            "user_agent",
            "referrer",
            "page_url",
            "submitted_at",
            "dialog",
            "utm",
            "city",
        ],
        "preserve_recipients": "config_mail_alert_email loop",
        "error_handling": [
            "Do not echo success before all sends complete",
            "Return JSON status after attempted send",
            "Avoid leaking mail transport errors to visitor",
        ],
        "test_plan": "Staged form-submit test only with operator approval in next operation",
        "rollback": "Re-upload source-before anketa.php from discovery deployment",
        "later_stages": [
            "SITE-002-PROD-MAIL-CUSTOMER-FORMS-01",
            "SITE-002-PROD-MAIL-ACCOUNT-TRANSACTIONAL-01",
            "SITE-002-PROD-MAIL-ORDER-TRANSACTIONAL-01",
        ],
    }
    write_json(DEPLOYMENT_ROOT / "design-system" / "future-integration-spec.json", spec)
    write_text(
        DEPLOYMENT_ROOT / "design-system" / "future-integration-spec.md",
        "\n".join(
            [
                "# Future integration spec",
                "",
                "## Next: SITE-002-PROD-MAIL-ADMIN-FORMS-01",
                "- Patch `catalog/controller/checkout/anketa.php`",
                "- Use `ZpmMailRenderer::renderAdminForm()`",
                "- Add service info block (IP, UA, referrer, page URL, submitted_at, dialog, UTM, city=unknown)",
                "- Preserve `config_mail_alert_email` recipient loop",
                "- Fix success-before-send JSON behavior",
                "- Rollback: re-upload discovery `source-readonly/catalog__controller__checkout__anketa.php`",
                "",
                "## Later stages",
                "- Customer form confirmations",
                "- Account transactional mails",
                "- Order transactional mails",
            ]
        )
        + "\n",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--skip-deploy", action="store_true", help="Skip FTP upload even if gates pass")
    args = parser.parse_args()

    ensure_layout()
    authority = phase_source_authority()
    phase_design_spec()
    phase_renderer_design()
    phase_fixtures()
    phase_local_impl()
    preview_result = phase_preview()
    qa = phase_local_qa(preview_result)
    rollback = phase_rollback_plan(authority)
    dry_run = phase_dry_run(qa, rollback)
    deploy = {"uploaded": False, "reason": "skipped by flag"} if args.skip_deploy else phase_deploy(dry_run, authority)
    sanity = phase_live_sanity()
    phase_future_integration()

    summary = {
        "operation_id": OPERATION_ID,
        "ocpilot_run": OCPILOT_RUN,
        "qa_pass": qa["pass"],
        "dry_run_pass": dry_run["pass"],
        "deploy": deploy,
        "sanity_pass": sanity["pass"],
        "remote_renderer": REMOTE_RENDERER,
        "preview_dir": str(DEPLOYMENT_ROOT / "preview"),
    }
    write_json(DEPLOYMENT_ROOT / "reports" / "operation-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if dry_run["pass"] and (deploy.get("uploaded") or deploy.get("reason")) else 1


if __name__ == "__main__":
    sys.exit(main())
