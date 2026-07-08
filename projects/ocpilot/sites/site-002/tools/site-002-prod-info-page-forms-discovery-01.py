#!/usr/bin/env python3
"""SITE-002 info page footer/corp CTA forms — read-only discovery (Run 4.229)."""
from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import json
import re
import shutil
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-INFO-PAGE-FORMS-DISCOVERY-01"
OCPILOT_RUN = "4.229"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION_READ_ONLY"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

REPO_ROOT = Path(r"X:\AI MARS")
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-INFO-PAGE-FORMS-DISCOVERY-01"
)
PRIOR_MAIL_DISCOVERY = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-MAIL-SYSTEM-DISCOVERY-01\source-readonly"
)
PRIOR_MAIL_CUSTOMER = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-MAIL-CUSTOMER-FORMS-01\source-after"
)

SUBDIRS = (
    "source-readonly",
    "http",
    "forms",
    "success-state",
    "mail",
    "implementation-plan",
    "verification",
    "reports",
    "manifests",
    "logs",
)

TARGET_PAGES = [
    {
        "name": "Оборудование на заказ",
        "url": "https://bzpm.ru/custom-equipment",
        "slug": "custom-equipment",
        "route": "information/custom_equipment",
        "form_class": "zpm-custom-form",
        "corpcta": "corpcta-custom_equipment",
        "dialog_current": "7",
        "dialog_recommended": "11",
        "dialog_label": "Оборудование на заказ",
    },
    {
        "name": "Оплата",
        "url": "https://bzpm.ru/payment-methods",
        "slug": "payment-methods",
        "route": "information/payment",
        "form_class": "zpm-payment-form",
        "corpcta": "corpcta-payment",
        "dialog_current": "",
        "dialog_recommended": "9",
        "dialog_label": "Вопрос по оплате",
    },
    {
        "name": "Доставка",
        "url": "https://bzpm.ru/delivery",
        "slug": "delivery",
        "route": "information/delivery",
        "form_class": "zpm-delivery-form",
        "corpcta": "corpcta-delivery",
        "dialog_current": "",
        "dialog_recommended": "8",
        "dialog_label": "Вопрос по доставке",
    },
    {
        "name": "Дилерам",
        "url": "https://bzpm.ru/dealers",
        "slug": "dealers",
        "route": "information/dealers",
        "form_class": "zpm-dealers-form",
        "corpcta": "corpcta-dealers",
        "dialog_current": "7",
        "dialog_recommended": "7",
        "dialog_label": "Форма дилерам и оптовикам",
    },
    {
        "name": "Гарантия",
        "url": "https://bzpm.ru/guarantee",
        "slug": "guarantee",
        "route": "information/guarantee",
        "form_class": "zpm-warranty-form",
        "corpcta": "corpcta-guarantee",
        "dialog_current": "",
        "dialog_recommended": "10",
        "dialog_label": "Гарантийное обращение",
    },
]

REGRESSION_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/llms.txt",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/sitemap.xml",
]

FTP_PROBE_PATHS = [
    "/public_html/catalog/controller/checkout/anketa.php",
    "/public_html/system/library/zpm/mail_renderer.php",
    "/public_html/assets/js/main.js",
    "/public_html/assets/css/style.css",
    "/public_html/catalog/view/theme/default/template/sections/fancyboxforms.twig",
    "/public_html/catalog/view/theme/default/template/sections/corpcta-guarantee.twig",
    "/public_html/catalog/view/theme/default/template/sections/corpcta-delivery.twig",
    "/public_html/catalog/view/theme/default/template/sections/corpcta-payment.twig",
    "/public_html/catalog/view/theme/default/template/sections/corpcta-dealers.twig",
    "/public_html/catalog/view/theme/default/template/sections/corpcta-custom_equipment.twig",
    "/public_html/catalog/view/theme/default/template/sections/corpcta-form-guarantee.twig",
    "/public_html/catalog/view/theme/default/template/sections/corpcta-form-delivery.twig",
    "/public_html/catalog/view/theme/default/template/sections/corpcta-form-payment.twig",
    "/public_html/catalog/view/theme/default/template/sections/corpcta-form-dealers.twig",
    "/public_html/catalog/view/theme/default/template/sections/corpcta-form-custom_equipment.twig",
    "/public_html/catalog/view/theme/default/template/information/guarantee.twig",
    "/public_html/catalog/view/theme/default/template/information/delivery.twig",
    "/public_html/catalog/view/theme/default/template/information/payment.twig",
    "/public_html/catalog/view/theme/default/template/information/dealers.twig",
    "/public_html/catalog/view/theme/default/template/information/custom_equipment.twig",
    "/public_html/catalog/controller/information/guarantee.php",
    "/public_html/catalog/controller/information/delivery.php",
    "/public_html/catalog/controller/information/payment.php",
    "/public_html/catalog/controller/information/dealers.php",
    "/public_html/catalog/controller/information/custom_equipment.php",
    "/storage/modification/catalog/controller/checkout/anketa.php",
    "/storage/modification/catalog/view/theme/default/template/information/guarantee.twig",
]

WRONG_BRAND = "БЗПМ"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data, encoding="utf-8", newline="\n")


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
                "action": attr.get("action", ""),
                "method": (attr.get("method") or "GET").upper(),
                "id": attr.get("id", ""),
                "class": attr.get("class", ""),
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

    def handle_endtag(self, tag: str) -> None:
        if tag == "textarea" and self._capture_text and self._field:
            self._field["default_text"] = "".join(self._text_buf).strip()
            self._capture_text = False
        if tag == "form":
            self._current = None

    def handle_data(self, data: str) -> None:
        if self._capture_text:
            self._text_buf.append(data)


def fetch_url(url: str) -> tuple[int, str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            final_url = resp.geturl()
            body = resp.read().decode("utf-8", errors="replace")
            return resp.status, final_url, body
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
        return exc.code, url, body


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def remote_to_local_name(remote_path: str) -> str:
    return remote_path.strip("/").replace("/", "__")


def ftp_download_file(ftp: ftplib.FTP, remote_path: str, local_path: Path) -> dict[str, Any]:
    local_path.parent.mkdir(parents=True, exist_ok=True)
    chunks: list[bytes] = []

    def collector(data: bytes) -> None:
        chunks.append(data)

    try:
        ftp.retrbinary(f"RETR {remote_path}", collector)
        content = b"".join(chunks)
        local_path.write_bytes(content)
        return {
            "remote_path": remote_path,
            "local_path": str(local_path),
            "status": "downloaded",
            "bytes": len(content),
            "sha256": hashlib.sha256(content).hexdigest(),
        }
    except ftplib.error_perm as exc:
        return {"remote_path": remote_path, "local_path": str(local_path), "status": "missing", "error": str(exc)}


def copy_prior_source(remote_path: str, dest: Path) -> bool:
    local_name = remote_to_local_name(remote_path.replace("/public_html/", "public_html/"))
    candidates = [
        PRIOR_MAIL_DISCOVERY / local_name,
        PRIOR_MAIL_CUSTOMER / local_name,
    ]
    for src in candidates:
        if src.is_file():
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            return True
    return False


def analyze_target_form(form: dict[str, Any], page: dict[str, str]) -> dict[str, Any]:
    classes = form.get("class", "")
    fields = form.get("fields", [])
    names = [f.get("name") for f in fields if f.get("name")]
    hidden = [f for f in fields if f.get("type") == "hidden" or f.get("tag") == "input" and f.get("type") == "hidden"]
    dialog = next((f.get("value") for f in fields if f.get("name") == "dialog"), "")
    has_email = "email" in names
    has_phone = "phone" in names
    has_zpm_form = "zpm-form" in classes
    has_fb_form = "data-fb-form" in form.get("data_attrs", {})
    posts_anketa = form.get("action") in ("#", "") and has_zpm_form
    reasons = []
    if not has_fb_form and page["form_class"] in classes:
        reasons.append("No data-fb-form — Fancybox submit handler does not bind")
    if page["form_class"] in classes and ".zpm-dealers[data-dealers] .zpm-form" not in classes:
        reasons.append("Outside .zpm-dealers[data-dealers] — isolated dealer handler does not bind")
    if not dialog and page["slug"] not in ("payment-methods", "delivery", "guarantee"):
        reasons.append("Missing dialog hidden field")
    if page["slug"] in ("payment-methods", "delivery", "guarantee") and not dialog:
        reasons.append("Missing dialog hidden field — backend will label as generic «Заявка с сайта»")
    if page["slug"] == "custom-equipment" and dialog == "7":
        reasons.append("dialog=7 reuses dealers label — needs dedicated dialog/source for OEM page")
    if form.get("action") == "#":
        reasons.append("action=# with no bound JS submit — native submit does nothing useful")
    return {
        "page_name": page["name"],
        "page_url": page["url"],
        "form_selector": f"form.{page['form_class']}",
        "section_block": f".zpm-corp-cta[data-corp-cta] / {page['corpcta']}",
        "form_classes": classes,
        "fields": names,
        "hidden_fields": [{"name": f.get("name"), "value": f.get("value")} for f in hidden],
        "action": form.get("action"),
        "method": form.get("method"),
        "submit_button_text": next(
            (re.sub(r"\s+", " ", (f.get("default_text") or f.get("value") or "submit")).strip()
             for f in fields if f.get("tag") == "button" and f.get("type") in ("submit", "")),
            "Отправить",
        ),
        "has_zpm_form_class": has_zpm_form,
        "has_data_fb_form": has_fb_form,
        "posts_to_checkout_anketa_expected": posts_anketa,
        "has_csrf_integration_expected": True,
        "has_recaptcha_integration_expected": True,
        "has_email_input": has_email,
        "has_phone_input": has_phone,
        "dialog_hidden_value": dialog,
        "dialog_recommended": page["dialog_recommended"],
        "dialog_label_recommended": page["dialog_label"],
        "loading_state_container": ".zpm-corp-cta__form-card or form parent via zpmFormGetLoadingContainer",
        "success_container_present": bool(re.search(r'data-fb-state="success"', "")),
        "suspected_reason_submit_inert": "; ".join(reasons) if reasons else "SAFE UNKNOWN",
        "customer_confirmation_eligible": has_email,
    }


def build_source_authority(downloads: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in downloads:
        remote = item["remote_path"]
        role = "supporting"
        renders = "no"
        handles = "no"
        patch = "no"
        reason = ""
        if "corpcta-" in remote and remote.endswith(".twig"):
            role = "corp CTA section template"
            renders = "yes" if "corpcta-form" not in remote else "partial (form partial exists; live pages embed inline form in corpcta-*.twig)"
            patch = "yes"
            reason = "Add dialog/source hidden fields; optional success-state sibling markup"
        elif "/information/" in remote and remote.endswith(".twig"):
            role = "information page template"
            renders = "yes (includes corp CTA section)"
            patch = "maybe"
            reason = "Only if corp CTA include path differs per page"
        elif "/information/" in remote and remote.endswith(".php"):
            role = "information page controller"
            renders = "no (loads twig)"
            patch = "no"
            reason = "Read-only authority; no form logic expected"
        elif remote.endswith("checkout/anketa.php"):
            role = "unified AJAX form handler"
            handles = "yes"
            patch = "yes"
            reason = "Add dialog IDs 8–11 + map page-specific POST fields into mail body"
        elif remote.endswith("mail_renderer.php"):
            role = "admin/customer mail renderer"
            handles = "yes"
            patch = "yes"
            reason = "Render extra_fields table for corp page-specific inputs"
        elif remote.endswith("main.js"):
            role = "frontend form submit + Fancybox success UX"
            handles = "yes (popup/dealer only today)"
            patch = "yes"
            reason = "Add corp CTA form handler + inline success replacement"
        elif remote.endswith("style.css"):
            role = "loading overlay + corp CTA + Fancybox success styles"
            patch = "maybe"
            reason = "Reuse zpm-fb success icon styles for inline corp success panel"
        elif remote.endswith("fancyboxforms.twig"):
            role = "popup form templates + canonical success-state markup"
            renders = "yes (reference)"
            patch = "no"
            reason = "Reuse success-state structure in JS/Twig; do not break popup forms"
        rows.append(
            {
                "path": remote,
                "role": role,
                "renders_target_form": renders,
                "handles_target_form": handles,
                "current_status": item.get("status", "unknown"),
                "future_patch_candidate": patch,
                "reason": reason,
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--skip-ftp", action="store_true", help="Use cached prior deployment sources only")
    args = parser.parse_args()

    for name in SUBDIRS:
        (DEPLOYMENT_ROOT / name).mkdir(parents=True, exist_ok=True)

    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "change_type": "info-page-forms-discovery",
            "production_mutation_allowed": False,
            "ftp_upload_allowed": False,
            "admin_save_allowed": False,
            "db_write_allowed": False,
            "email_send_allowed": False,
            "form_submit_allowed": False,
            "mail_change_allowed": False,
            "frontend_change_allowed": False,
            "template_change_allowed": False,
            "expected_pages": [p["name"] for p in TARGET_PAGES],
            "brand_policy_correct": "ЗПМ",
            "brand_policy_forbidden_public": "БЗПМ",
            "timestamp": utc_now(),
            "ocpilot_run": OCPILOT_RUN,
        },
    )

    # Phase 1 + 2: HTTP pages
    target_rows: list[dict[str, Any]] = []
    inventory_rows: list[dict[str, Any]] = []
    for page in TARGET_PAGES:
        status, final_url, html = fetch_url(page["url"])
        slug = page["slug"]
        extract_path = DEPLOYMENT_ROOT / "http" / f"{slug}.extract.html"
        masked = re.sub(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", "<EMAIL>", html)
        masked = re.sub(r"\+7\s*\([^)]+\)\s*[\d\s-]{6,}", "<PHONE>", masked)
        write_text(extract_path, masked[:250000])

        parser_html = FormParser()
        parser_html.feed(html)
        target_form = next((f for f in parser_html.forms if page["form_class"] in f.get("class", "")), None)
        has_form = target_form is not None
        target_rows.append(
            {
                "title": page["name"],
                "url": page["url"],
                "http_status": status,
                "final_url": final_url,
                "route_type": page["route"],
                "template_inference": f"catalog/view/theme/default/template/information/{page['slug'].replace('-methods', '')}.twig + sections/{page['corpcta']}.twig",
                "has_target_lower_footer_form": "yes" if has_form else "no",
                "notes": "Corp CTA bottom block confirmed" if has_form else "BLOCKER: target form class not found in HTML",
            }
        )
        if target_form:
            inventory_rows.append(analyze_target_form(target_form, page))

    write_json(DEPLOYMENT_ROOT / "forms" / "target-pages.json", target_rows)
    write_json(DEPLOYMENT_ROOT / "forms" / "target-pages.md", "# Target pages\n\n" + "\n".join(
        f"- **{r['title']}** — {r['url']} — HTTP {r['http_status']} — form: {r['has_target_lower_footer_form']}" for r in target_rows
    ))
    with (DEPLOYMENT_ROOT / "forms" / "target-pages.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "title", "url", "http_status", "final_url", "route_type",
                "template_inference", "has_target_lower_footer_form", "notes",
            ],
        )
        writer.writeheader()
        writer.writerows(target_rows)

    write_json(DEPLOYMENT_ROOT / "forms" / "info-page-form-inventory.json", inventory_rows)
    write_json(DEPLOYMENT_ROOT / "forms" / "info-page-form-inventory.md", "# Form inventory\n\n" + json.dumps(inventory_rows, ensure_ascii=False, indent=2))
    with (DEPLOYMENT_ROOT / "forms" / "info-page-form-inventory.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(inventory_rows[0].keys()) if inventory_rows else ["page_name"])
        writer.writeheader()
        for row in inventory_rows:
            flat = dict(row)
            flat["fields"] = "|".join(row.get("fields", []))
            flat["hidden_fields"] = json.dumps(row.get("hidden_fields", []), ensure_ascii=False)
            writer.writerow(flat)

    # Phase 3: source authority
    downloads: list[dict[str, Any]] = []
    if not args.skip_ftp:
        creds = parse_production_secrets(SECRETS_PATH)
        ftp = ftplib.FTP()
        ftp.connect(creds["host"], int(creds["port"]), timeout=60)
        ftp.login(creds["username"], creds["password"])
        ftp.set_pasv(True)
        for remote in FTP_PROBE_PATHS:
            local = DEPLOYMENT_ROOT / "source-readonly" / remote_to_local_name(remote)
            downloads.append(ftp_download_file(ftp, remote, local))
        ftp.quit()
    else:
        for remote in FTP_PROBE_PATHS:
            local = DEPLOYMENT_ROOT / "source-readonly" / remote_to_local_name(remote)
            if copy_prior_source(remote, local):
                text = local.read_text(encoding="utf-8", errors="replace")
                downloads.append(
                    {
                        "remote_path": remote,
                        "local_path": str(local),
                        "status": "copied_from_prior_deployment",
                        "bytes": len(text.encode("utf-8")),
                        "sha256": sha256_text(text),
                    }
                )
            else:
                downloads.append({"remote_path": remote, "local_path": str(local), "status": "missing"})

    authority_rows = build_source_authority(downloads)
    write_json(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.json", authority_rows)
    write_json(DEPLOYMENT_ROOT / "manifests" / "ftp-downloads.json", downloads)
    with (DEPLOYMENT_ROOT / "manifests" / "source-authority-map.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["path", "role", "renders_target_form", "handles_target_form", "current_status", "future_patch_candidate", "reason"],
        )
        writer.writeheader()
        writer.writerows(authority_rows)

    # Phase 4: popup success-state
    success_map = {
        "reference_form": "Задать вопрос (fancyboxforms.twig #zpmFbQuestion)",
        "source_file": "/public_html/catalog/view/theme/default/template/sections/fancyboxforms.twig",
        "js_handler": "main.js Fancybox block — document submit listener on [data-fb-form]; setState(wrap, 'success')",
        "wrap_selector": "[data-fb-modal]",
        "success_selector": '[data-fb-state="success"]',
        "success_html_structure": (
            '<div class="zpm-fb__state" data-fb-state="success">'
            '<svg class="zpm-icon success zpm-icon--lg"><use href="#zpm_ico__successful"></use></svg>'
            '<div><h3 class="zpm-fb__title section-title__like-h3">Спасибо</h3>'
            '<p class="zpm-fb__sub">Ваша заявка отправлена!</p></div></div>'
        ),
        "success_title": "Спасибо",
        "success_text": "Ваша заявка отправлена!",
        "icon_class": "zpm-icon success zpm-icon--lg",
        "icon_sprite": "#zpm_ico__successful",
        "css_dependencies": ["zpm-fb__state", "zpm-fb__title", "zpm-fb__sub", "zpm-icon", "zpm-icon--lg", "zpm-form--loading"],
        "insertion_method": "JS toggles hidden attribute on [data-fb-state] siblings inside [data-fb-modal]",
        "recommended_reuse_for_info_pages": (
            "Inject equivalent markup into .zpm-corp-cta__form-card on success OR pre-render hidden "
            "[data-corp-form-state=\"success\"] sibling and toggle like Fancybox setState()"
        ),
        "auto_close_behavior_popup": "Fancybox closes after MSG_MS (3000ms) — info pages should NOT auto-close; replace form in-place",
    }
    write_json(DEPLOYMENT_ROOT / "success-state" / "popup-success-state-map.json", success_map)
    write_text(
        DEPLOYMENT_ROOT / "success-state" / "popup-success-state-map.md",
        "# Popup success-state map\n\n" + json.dumps(success_map, ensure_ascii=False, indent=2),
    )

    # Phase 5: mail integration
    mail_plan = {
        "handler": "checkout/anketa.php",
        "renderer": "ZpmMailRenderer",
        "existing_dialogs": {"1": "Вопрос по товару", "2": "Запрос на обратный звонок", "3": "Вопрос по цене товара", "5": "Новый отзыв", "7": "Форма дилерам и оптовикам"},
        "recommended_new_dialogs": {
            "8": "Вопрос по доставке",
            "9": "Вопрос по оплате",
            "10": "Гарантийное обращение",
            "11": "Оборудование на заказ",
        },
        "source_page_field": "POST source_page or page_url — anketa zpmResolvePageUrl() already supports",
        "customer_confirmation_rule": "valid posted email OR logged-in customer email; no service info in customer copy",
        "forms": [],
        "backend_changes_required": True,
        "renderer_changes_required": True,
        "notes": [
            "anketa currently maps only name/phone/email/comment/message — page-specific fields (company, region, equipment_model, etc.) are dropped from admin mail",
            "company POST field is not assigned to $data['company'] today",
            "custom-equipment incorrectly posts dialog=7 (dealers) — must change to dialog=11",
            "Unknown dialog 0 still sends mail as «Заявка с сайта» but loses page-specific labeling",
        ],
    }
    field_map = {
        "custom-equipment": ["company", "contact", "phone", "email", "project_description", "drawings", "notes"],
        "payment-methods": ["name", "phone", "email", "company", "comment"],
        "delivery": ["name", "phone", "email", "region", "delivery_method", "order_details"],
        "dealers": ["name", "company", "city", "phone", "email", "comment"],
        "guarantee": ["name", "phone", "email", "equipment_model", "purchase_date", "comment"],
    }
    for page in TARGET_PAGES:
        inv = next((r for r in inventory_rows if r["page_name"] == page["name"]), {})
        mail_plan["forms"].append(
            {
                "page": page["name"],
                "url": page["url"],
                "recommended_dialog": page["dialog_recommended"],
                "admin_subject_label": f"ЗПМ: новая заявка — {page['dialog_label']}",
                "dialog_label": page["dialog_label"],
                "customer_confirmation_eligible": inv.get("customer_confirmation_eligible", True),
                "required_hidden_fields": [
                    {"name": "dialog", "value": page["dialog_recommended"]},
                    {"name": "source_page", "value": page["url"]},
                ],
                "extra_fields_for_mail": field_map.get(page["slug"], []),
                "backend_changes_required": True,
                "renderer_changes_required": True,
            }
        )
    write_json(DEPLOYMENT_ROOT / "mail" / "info-page-mail-integration-plan.json", mail_plan)
    write_text(
        DEPLOYMENT_ROOT / "mail" / "info-page-mail-integration-plan.md",
        "# Mail integration plan\n\n" + json.dumps(mail_plan, ensure_ascii=False, indent=2),
    )

    # Phase 6: frontend integration
    frontend_plan = {
        "current_submit_handlers": [
            {"selector": "[data-fb-form]", "scope": "Fancybox popup forms", "endpoint": "/index.php?route=checkout/anketa", "success": "setState(wrap,'success') inside [data-fb-modal]"},
            {"selector": ".zpm-dealers[data-dealers] .zpm-form", "scope": "Home/katalog commercial trust legacy", "endpoint": "same", "success": "inline .zpm-form__status-msg (not popup icon state)"},
        ],
        "why_info_page_forms_inert": [
            "Corp CTA forms have class zpm-form but lack data-fb-form",
            "They are not under .zpm-dealers[data-dealers]",
            "No submit listener bound — action=# prevents navigation but no AJAX fires",
        ],
        "recommended_selector": ".zpm-corp-cta[data-corp-cta] form.zpm-form",
        "recommended_data_attributes": {
            "form": 'data-corp-form="{warranty|delivery|payment|dealers|custom}"',
            "wrap": 'data-corp-form-wrap on .zpm-corp-cta__form-card',
            "states": 'data-corp-form-state="form|success|error" hidden siblings',
        },
        "submit_pipeline": "Reuse processSubmission()/sendForm() from Fancybox block (CSRF + reCAPTCHA v3 + fetch anketa + zpmFormSetLoading)",
        "success_replacement_strategy": "On ok:true — hide form state, show pre-rendered success panel matching Fancybox icon+text inside .zpm-corp-cta__form-card; do not reset page",
        "loading_abort": "zpmFormGetLoadingContainer should use .zpm-corp-cta__form-card; abort on navigation only (no Fancybox close)",
        "css_changes_needed": "Minor — reuse .zpm-fb__state/.zpm-icon success styles inside corp card; loading overlay already via .zpm-form--loading",
        "js_changes_needed": True,
        "files": ["/public_html/assets/js/main.js", "corpcta-*.twig optional success markup"],
        "rollback": "Restore main.js + touched corpcta twig from SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01 backups",
        "regression_risk": "Must not alter [data-fb-form] handler or .zpm-dealers[data-dealers] selector logic",
    }
    write_json(DEPLOYMENT_ROOT / "forms" / "frontend-integration-plan.json", frontend_plan)
    write_text(
        DEPLOYMENT_ROOT / "forms" / "frontend-integration-plan.md",
        "# Frontend integration plan\n\n" + json.dumps(frontend_plan, ensure_ascii=False, indent=2),
    )

    # Phase 7: implementation charter
    charter = {
        "operation_id": "SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01",
        "scope": [
            "Enable AJAX submit on 5 corp/info page CTA forms",
            "Reuse checkout/anketa.php + ZpmMailRenderer",
            "Add dialog IDs 8–11 and normalize hidden dialog/source_page",
            "Reuse Run 4.226 loading/spinner/abort UX",
            "Inline success-state matching Fancybox «Задать вопрос» icon+text",
            "Map page-specific fields into admin mail; customer copy only when email eligible",
        ],
        "expected_touched_files": [
            "/public_html/catalog/view/theme/default/template/sections/corpcta-guarantee.twig",
            "/public_html/catalog/view/theme/default/template/sections/corpcta-delivery.twig",
            "/public_html/catalog/view/theme/default/template/sections/corpcta-payment.twig",
            "/public_html/catalog/view/theme/default/template/sections/corpcta-dealers.twig",
            "/public_html/catalog/view/theme/default/template/sections/corpcta-custom_equipment.twig",
            "/public_html/assets/js/main.js",
            "/public_html/assets/css/style.css",
            "/public_html/catalog/controller/checkout/anketa.php",
            "/public_html/system/library/zpm/mail_renderer.php",
        ],
        "test_plan": [
            "One controlled submit per distinct form component (or 5 page submits if charter approves)",
            "At least one form with email — verify customer copy",
            "Verify admin mail labels per page",
            "Verify inline success-state replaces form block",
            "Verify loading/abort on corp card",
            "Regression: popup «Задать вопрос» still success-closes",
            "Regression: dealer/home commercial trust form unchanged",
        ],
        "rollback_plan": "Re-upload exact remote-before copies of touched files from integration deployment backup/",
        "forbidden": [
            "standard OpenCart mails", "SMTP/admin/DB", "header/footer/Yandex",
            "product/category/meta", "1C/import/scheduler",
        ],
    }
    write_json(
        DEPLOYMENT_ROOT / "implementation-plan" / "SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01-CHARTER.json",
        charter,
    )
    write_text(
        DEPLOYMENT_ROOT / "implementation-plan" / "SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01-CHARTER.md",
        "# SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01 Charter\n\n"
        + json.dumps(charter, ensure_ascii=False, indent=2),
    )

    # Phase 8: regression sanity
    regression_rows = []
    sitemap_count = None
    for url in REGRESSION_URLS:
        status, final_url, body = fetch_url(url)
        wrong_brand = WRONG_BRAND in body
        if url.endswith("sitemap.xml") and status == 200:
            try:
                root = ET.fromstring(body)
                sitemap_count = len(root.findall(".//{*}loc"))
            except ET.ParseError:
                sitemap_count = None
        regression_rows.append(
            {
                "url": url,
                "http_status": status,
                "final_url": final_url,
                "public_wrong_brand": wrong_brand,
                "notes": "read-only GET",
            }
        )
    regression = {"checked_at": utc_now(), "sitemap_url_count": sitemap_count, "urls": regression_rows}
    write_json(DEPLOYMENT_ROOT / "verification" / "read-only-regression-sanity.json", regression)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "read-only-regression-sanity.md",
        "# Read-only regression sanity\n\n"
        + f"Sitemap URL count: {sitemap_count}\n\n"
        + "\n".join(f"- {r['url']}: HTTP {r['http_status']}, БЗПМ={r['public_wrong_brand']}" for r in regression_rows),
    )

    summary = {
        "operation_id": OPERATION_ID,
        "ocpilot_run": OCPILOT_RUN,
        "target_pages_found": sum(1 for r in target_rows if r["has_target_lower_footer_form"] == "yes"),
        "target_pages_total": len(target_rows),
        "forms_inventoried": len(inventory_rows),
        "ftp_downloads": len([d for d in downloads if d.get("status") in ("downloaded", "copied_from_prior_deployment")]),
        "verdict": (
            "SITE-002 INFO PAGE FORMS DISCOVERY COMPLETE — INTEGRATION CHARTER READY"
            if all(r["has_target_lower_footer_form"] == "yes" for r in target_rows)
            else "SITE-002 INFO PAGE FORMS DISCOVERY PARTIAL — SOURCE SAFE UNKNOWN"
        ),
        "timestamp": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "reports" / "operation-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
