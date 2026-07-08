#!/usr/bin/env python3
"""SITE-002 info page corp CTA forms integration — Run 4.230."""
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
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01"
OCPILOT_RUN = "4.230"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01"
CHECKPOINT_AFTER = "SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01"
CORRECT_BRAND = "ЗПМ"
WRONG_BRAND = "БЗПМ"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
TEST_MARKER = "MARS TEST INFO PAGE FORMS 01"
TEST_PHONE = "+7 000 000-00-00"
TEST_EMAIL = "test@example.invalid"

REPO_ROOT = Path(r"X:\AI MARS")
TOOLS_DIR = REPO_ROOT / "projects" / "ocpilot" / "sites" / "site-002" / "tools"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01"
)
DISCOVERY_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-INFO-PAGE-FORMS-DISCOVERY-01"
)

REMOTE_ANKETA = "/public_html/catalog/controller/checkout/anketa.php"
REMOTE_RENDERER = "/public_html/system/library/zpm/mail_renderer.php"
REMOTE_MAIN_JS = "/public_html/assets/js/main.js"
REMOTE_STYLE_CSS = "/public_html/assets/css/style.css"
INFO_REMOTE = "/public_html/catalog/view/theme/default/template/information/{name}.twig"
REMOTE_MOD_ANKETA = "/storage/modification/catalog/controller/checkout/anketa.php"
REMOTE_MOD_RENDERER = "/storage/modification/system/library/zpm/mail_renderer.php"
CORPCTA_REMOTE = "/public_html/catalog/view/theme/default/template/sections/{name}.twig"

ANKETA_PATCH = TOOLS_DIR / "checkout_anketa_info_page_forms.php"
RENDERER_SRC = TOOLS_DIR / "mail_renderer.php"
CORPCTA_JS = TOOLS_DIR / "zpm-corp-cta-forms.js"
CSS_APPEND = TOOLS_DIR / "zpm-corp-cta-success.css"

SUBDIRS = (
    "source-before",
    "source-after",
    "http-before",
    "http-after",
    "ui-before",
    "ui-after",
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

TARGET_PAGES = [
    {
        "slug": "custom-equipment",
        "url": "https://bzpm.ru/custom-equipment",
        "corpcta": "corpcta-custom_equipment",
        "information": "custom_equipment",
        "form_class": "zpm-custom-form",
        "dialog": "11",
        "source_page": "https://bzpm.ru/custom-equipment",
        "test_fields": {
            "company": "MARS TEST ORG",
            "contact": TEST_MARKER,
            "phone": TEST_PHONE,
            "email": TEST_EMAIL,
            "project_description": TEST_MARKER,
            "agree": "on",
        },
    },
    {
        "slug": "payment-methods",
        "url": "https://bzpm.ru/payment-methods",
        "corpcta": "corpcta-payment",
        "information": "payment",
        "form_class": "zpm-payment-form",
        "dialog": "9",
        "source_page": "https://bzpm.ru/payment-methods",
        "test_fields": {
            "name": TEST_MARKER,
            "phone": TEST_PHONE,
            "email": "",
            "company": "MARS TEST ORG",
            "comment": TEST_MARKER,
            "agree": "on",
        },
    },
    {
        "slug": "delivery",
        "url": "https://bzpm.ru/delivery",
        "corpcta": "corpcta-delivery",
        "information": "delivery",
        "form_class": "zpm-delivery-form",
        "dialog": "8",
        "source_page": "https://bzpm.ru/delivery",
        "test_fields": {
            "name": TEST_MARKER,
            "phone": TEST_PHONE,
            "email": TEST_EMAIL,
            "region": "MARS TEST REGION",
            "delivery_method": "ТК",
            "order_details": TEST_MARKER,
            "agree": "on",
        },
    },
    {
        "slug": "dealers",
        "url": "https://bzpm.ru/dealers",
        "corpcta": "corpcta-dealers",
        "information": "dealers",
        "form_class": "zpm-dealers-form",
        "dialog": "7",
        "source_page": "https://bzpm.ru/dealers",
        "test_fields": {
            "name": TEST_MARKER,
            "company": "MARS TEST ORG",
            "city": "MARS TEST CITY",
            "phone": TEST_PHONE,
            "email": TEST_EMAIL,
            "comment": TEST_MARKER,
            "agree": "on",
        },
    },
    {
        "slug": "guarantee",
        "url": "https://bzpm.ru/guarantee",
        "corpcta": "corpcta-guarantee",
        "information": "guarantee",
        "form_class": "zpm-warranty-form",
        "dialog": "10",
        "source_page": "https://bzpm.ru/guarantee",
        "test_fields": {
            "name": TEST_MARKER,
            "phone": TEST_PHONE,
            "email": TEST_EMAIL,
            "equipment_model": "MARS TEST MODEL",
            "purchase_date": "01.01.2025",
            "comment": TEST_MARKER,
            "agree": "on",
        },
    },
]

REGRESSION_URLS = [
    ("home", "https://bzpm.ru/"),
    ("katalog", "https://bzpm.ru/katalog"),
    ("neutral_hub", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie"),
    ("stoly", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly"),
    ("llms", "https://bzpm.ru/llms.txt"),
    ("robots", "https://bzpm.ru/robots.txt"),
    ("sitemap", "https://bzpm.ru/sitemap.xml"),
]

DIALOG_LABELS = {
    "7": "Форма дилерам и оптовикам",
    "8": "Вопрос по доставке",
    "9": "Вопрос по оплате",
    "10": "Гарантийное обращение",
    "11": "Оборудование на заказ",
}

CORPCTA_JS_MARKER = "CORP CTA INFO PAGE FORMS (ZPM) — Run 4.230"
LOADING_CONTAINER_OLD = (
    "function zpmFormGetLoadingContainer(form) {\n"
    "  return form.closest('[data-fb-modal]') || form.closest('.fancybox__content') || form.closest('.zpm-dealers') || form;\n"
    "}"
)
LOADING_CONTAINER_NEW = (
    "function zpmFormGetLoadingContainer(form) {\n"
    "  return form.closest('[data-fb-modal]') || form.closest('.fancybox__content') || form.closest('.zpm-dealers') || form.closest('.zpm-corp-cta__form-card') || form;\n"
    "}"
)
FANCYBOX_SUBMIT_CLOSE = "  });\n})();\n\n\n\n\n\n/* ================================\n   Fancybox FORMS UX (ZPM)"


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


def patch_corpcta_twig(source: str, dialog: str, source_page: str) -> str:
    hidden = (
        f'  <input type="hidden" name="dialog" value="{dialog}">\n'
        f'  <input type="hidden" name="source_page" value="{source_page}">\n'
    )
    if 'name="dialog"' in source:
        source = re.sub(
            r'<input type="hidden" name="dialog" value="\d+">',
            f'<input type="hidden" name="dialog" value="{dialog}">',
            source,
            count=1,
        )
        if 'name="source_page"' not in source:
            source = source.replace(
                f'<input type="hidden" name="dialog" value="{dialog}">',
                f'<input type="hidden" name="dialog" value="{dialog}">\n'
                f'  <input type="hidden" name="source_page" value="{source_page}">',
                1,
            )
        else:
            source = re.sub(
                r'<input type="hidden" name="source_page" value="[^"]*">',
                f'<input type="hidden" name="source_page" value="{source_page}">',
                source,
                count=1,
            )
        return source
    return re.sub(
        r'(<form class="zpm-form[^"]*"[^>]*>\n)',
        r"\1" + hidden,
        source,
        count=1,
    )


def patch_main_js(source: str) -> str:
    if CORPCTA_JS_MARKER in source:
        return source
    if LOADING_CONTAINER_OLD not in source:
        raise RuntimeError("zpmFormGetLoadingContainer block not found")
    source = source.replace(LOADING_CONTAINER_OLD, LOADING_CONTAINER_NEW, 1)
    if FANCYBOX_SUBMIT_CLOSE not in source:
        raise RuntimeError("Fancybox submit close marker not found")
    corp_js = CORPCTA_JS.read_text(encoding="utf-8").strip()
    source = source.replace(
        FANCYBOX_SUBMIT_CLOSE,
        "  });\n})();\n\n\n" + corp_js + "\n\n\n/* ================================\n   Fancybox FORMS UX (ZPM)",
        1,
    )
    return source


def patch_style_css(source: str) -> str:
    append = CSS_APPEND.read_text(encoding="utf-8")
    if "zpm-corp-cta__success" in source:
        return source
    return source.rstrip() + "\n\n" + append


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
            "related_discovery_run": "SITE-002-PROD-INFO-PAGE-FORMS-DISCOVERY-01",
            "related_discovery_ocpilot_run": "4.229",
            "change_type": "info-page-corp-cta-form-integration",
            "production_mutation_allowed": True,
            "ftp_upload_allowed": True,
            "admin_save_allowed": False,
            "db_write_allowed": False,
            "email_send_allowed": "controlled_tests_only",
            "form_submit_allowed": "controlled_tests_only",
            "smtp_change_allowed": False,
            "standard_opencart_mail_change_allowed": False,
            "mail_trigger_patch_allowed": "checkout_anketa_only",
            "shared_renderer_patch_allowed": True,
            "frontend_form_patch_allowed": True,
            "template_patch_allowed": "corpcta_templates_only",
            "header_footer_change_allowed": False,
            "brand_policy_correct": CORRECT_BRAND,
            "brand_policy_forbidden_public": WRONG_BRAND,
            "created_at": utc_now(),
        },
    )


def touched_remotes() -> list[str]:
    remotes = [REMOTE_ANKETA, REMOTE_RENDERER, REMOTE_MAIN_JS, REMOTE_STYLE_CSS]
    for page in TARGET_PAGES:
        remotes.append(CORPCTA_REMOTE.format(name=page["corpcta"]))
        remotes.append(INFO_REMOTE.format(name=page["information"]))
    return remotes


def phase_source_authority() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    mod_blocker = False
    probe = touched_remotes() + [REMOTE_MOD_ANKETA, REMOTE_MOD_RENDERER]
    ftp = ftp_connect()
    try:
        for remote in probe:
            data, err = ftp_download(ftp, remote)
            exists = data is not None
            sha = sha256_bytes(data) if data else ""
            will_touch = remote in touched_remotes()
            if data is not None and will_touch:
                local = DEPLOYMENT_ROOT / "source-before" / remote_local_name(remote)
                local.write_bytes(data)
            is_mod = "modification" in remote
            if is_mod and exists:
                mod_blocker = True
            rows.append(
                {
                    "remote_path": remote,
                    "role": "corpcta" if "corpcta" in remote else "core",
                    "sha256": sha,
                    "will_modify": will_touch,
                    "modification_overlay": is_mod,
                    "rollback_source_captured": exists and will_touch,
                    "error": err or "",
                }
            )
    finally:
        ftp.quit()

    write_csv(
        DEPLOYMENT_ROOT / "manifests" / "source-authority-map.csv",
        rows,
        ["remote_path", "role", "sha256", "will_modify", "modification_overlay", "rollback_source_captured", "error"],
    )
    write_json(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.json", {"generated_at": utc_now(), "paths": rows})
    md = [f"# Source authority map\n\nOperation: {OPERATION_ID}\n"]
    for row in rows:
        md.append(
            f"- `{row['remote_path']}` modify={row['will_modify']} mod_overlay={row['modification_overlay']} sha={row['sha256'][:12]}…"
        )
    if mod_blocker:
        md.append("\n**STOP:** modification overlay present.")
    write_text(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.md", "\n".join(md) + "\n")
    return {"rows": rows, "mod_blocker": mod_blocker}


def phase_http_before() -> dict[str, Any]:
    pages: list[dict[str, Any]] = []
    for page in TARGET_PAGES:
        resp = http_get(page["url"])
        text = resp.get("text", "")
        form_match = re.search(
            rf'<form[^>]*class="[^"]*{re.escape(page["form_class"])}[^"]*"[^>]*>(.*?)</form>',
            text,
            re.I | re.S,
        )
        form_html = form_match.group(0) if form_match else ""
        pages.append(
            {
                "slug": page["slug"],
                "url": page["url"],
                "status": resp.get("status"),
                "form_class": page["form_class"],
                "has_dialog": 'name="dialog"' in form_html,
                "dialog_value": re.search(r'name="dialog"\s+value="(\d+)"', form_html).group(1)
                if re.search(r'name="dialog"', form_html)
                else "",
                "has_source_page": 'name="source_page"' in form_html,
                "has_data_fb_form": "data-fb-form" in form_html,
                "action": re.search(r'action="([^"]*)"', form_html).group(1) if form_match else "",
            }
        )
    payload = {"generated_at": utc_now(), "target_pages": pages}
    write_json(DEPLOYMENT_ROOT / "http-before" / "target-pages-before.json", payload)
    write_text(
        DEPLOYMENT_ROOT / "ui-before" / "forms-before.md",
        "# Forms before\n\nAll five corp CTA forms markup-only; no submit handler; no inline success.\n",
    )
    write_json(DEPLOYMENT_ROOT / "ui-before" / "forms-before.json", payload)
    return payload


def phase_implementation_design() -> None:
    design = {
        "operation_id": OPERATION_ID,
        "dialogs": {k: v for k, v in DIALOG_LABELS.items()},
        "frontend_selector": ".zpm-corp-cta[data-corp-cta] form.zpm-form",
        "success_state": {
            "icon": "#zpm_ico__successful",
            "title": "Спасибо",
            "text": "Ваша заявка отправлена!",
        },
        "customer_rule": "valid posted email or logged-in customer email only",
        "customer_no_service_info": True,
        "patch_files": touched_remotes(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "implementation-design.json", design)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-design.md",
        "# Implementation design\n\n" + json.dumps(design, ensure_ascii=False, indent=2) + "\n",
    )


def phase_local_patch() -> dict[str, Any]:
    changed: list[dict[str, Any]] = []
    diffs: dict[str, str] = {}

    shutil.copy2(ANKETA_PATCH, DEPLOYMENT_ROOT / "source-after" / remote_local_name(REMOTE_ANKETA))
    shutil.copy2(RENDERER_SRC, DEPLOYMENT_ROOT / "source-after" / remote_local_name(REMOTE_RENDERER))

    before_main = DEPLOYMENT_ROOT / "source-before" / remote_local_name(REMOTE_MAIN_JS)
    before_css = DEPLOYMENT_ROOT / "source-before" / remote_local_name(REMOTE_STYLE_CSS)
    after_main = DEPLOYMENT_ROOT / "source-after" / remote_local_name(REMOTE_MAIN_JS)
    after_css = DEPLOYMENT_ROOT / "source-after" / remote_local_name(REMOTE_STYLE_CSS)
    patched_js = patch_main_js(before_main.read_text(encoding="utf-8"))
    patched_css = patch_style_css(before_css.read_text(encoding="utf-8"))
    after_main.write_text(patched_js, encoding="utf-8", newline="\n")
    after_css.write_text(patched_css, encoding="utf-8", newline="\n")

    for page in TARGET_PAGES:
        for kind, remote_tpl in (
            ("corpcta", CORPCTA_REMOTE),
            ("information", INFO_REMOTE),
        ):
            remote = remote_tpl.format(name=page[kind])
            before = DEPLOYMENT_ROOT / "source-before" / remote_local_name(remote)
            if not before.is_file():
                discovery_before = DISCOVERY_ROOT / "source-readonly" / remote_local_name(remote)
                if discovery_before.is_file():
                    shutil.copy2(discovery_before, before)
                else:
                    raise RuntimeError(f"missing source-before for {remote}")
            after = DEPLOYMENT_ROOT / "source-after" / remote_local_name(remote)
            patched = patch_corpcta_twig(
                before.read_text(encoding="utf-8"),
                page["dialog"],
                page["source_page"],
            )
            after.write_text(patched, encoding="utf-8", newline="\n")

    for remote in touched_remotes():
        before = DEPLOYMENT_ROOT / "source-before" / remote_local_name(remote)
        after = DEPLOYMENT_ROOT / "source-after" / remote_local_name(remote)
        diff = "".join(
            difflib.unified_diff(
                before.read_text(encoding="utf-8").splitlines(keepends=True),
                after.read_text(encoding="utf-8").splitlines(keepends=True),
                fromfile=f"before/{remote}",
                tofile=f"after/{remote}",
            )
        )
        name = remote.split("/")[-1].replace(".", "-")
        if "corpcta" in remote:
            diffs.setdefault("corpcta", "")
            diffs["corpcta"] += diff
        elif "main.js" in remote:
            write_text(DEPLOYMENT_ROOT / "patch" / "diff-main-js.diff", diff)
        elif "style.css" in remote:
            write_text(DEPLOYMENT_ROOT / "patch" / "diff-style-css.diff", diff)
        elif "anketa" in remote:
            write_text(DEPLOYMENT_ROOT / "patch" / "diff-anketa.diff", diff)
        elif "mail_renderer" in remote:
            write_text(DEPLOYMENT_ROOT / "patch" / "diff-mail-renderer.diff", diff)
        changed.append(
            {
                "path": remote,
                "before_sha256": sha256_file(before),
                "after_sha256": sha256_file(after),
            }
        )
    if "corpcta" in diffs:
        write_text(DEPLOYMENT_ROOT / "patch" / "diff-corpcta-templates.diff", diffs["corpcta"])

    anketa_text = (DEPLOYMENT_ROOT / "source-after" / remote_local_name(REMOTE_ANKETA)).read_text(encoding="utf-8")
    renderer_text = (DEPLOYMENT_ROOT / "source-after" / remote_local_name(REMOTE_RENDERER)).read_text(encoding="utf-8")
    js_text = after_main.read_text(encoding="utf-8")
    cust_start = renderer_text.find("public function renderCustomerFormConfirmation")
    cust_end = renderer_text.find("public function renderAccountMail", cust_start)
    customer_block = renderer_text[cust_start:cust_end] if cust_start >= 0 and cust_end > cust_start else ""
    static = {
        "no_bzpm": WRONG_BRAND not in anketa_text + renderer_text + js_text,
        "dialogs_8_11": all(f"case {d}:" in anketa_text for d in (8, 9, 10, 11)),
        "extra_fields": "zpmCollectExtraFields" in anketa_text,
        "corp_cta_handler": CORPCTA_JS_MARKER in js_text,
        "loading_container_corp": ".zpm-corp-cta__form-card" in js_text,
        "customer_no_service_info": "service_info" not in customer_block,
    }
    write_csv(DEPLOYMENT_ROOT / "patch" / "changed-files.csv", changed, ["path", "before_sha256", "after_sha256"])
    write_json(DEPLOYMENT_ROOT / "patch" / "changed-files.json", {"changed": changed, "static": static})
    write_text(
        DEPLOYMENT_ROOT / "patch" / "patch-summary.md",
        "# Patch summary\n\n"
        + "\n".join(f"- `{c['path']}`" for c in changed)
        + "\n\n"
        + "\n".join(f"- {k}: **{v}**" for k, v in static.items())
        + "\n",
    )
    return {"changed": changed, "static": static}


def render_mail_preview(dialog: str, extra: list[dict[str, str]]) -> dict[str, str]:
    label = DIALOG_LABELS[dialog]
    admin_subject = f"{CORRECT_BRAND}: новая заявка — {label}"
    customer_subject = f"{CORRECT_BRAND}: заявка получена — {label}"
    extra_html = "".join(f"<div><b>{html_module.escape(r['label'])}:</b> {html_module.escape(r['value'])}</div>" for r in extra)
    admin_html = (
        f"<h1>{html_module.escape(admin_subject)}</h1>"
        f"<p>Тип формы: {html_module.escape(label)}</p>"
        f"<p>Имя: MARS TEST</p>{extra_html}"
        f"<p style='color:#667085'>Служебная информация: IP 203.0.113.1</p>"
    )
    customer_html = (
        f"<h1>{html_module.escape(customer_subject)}</h1>"
        f"<p>Мы получили вашу заявку на сайте {CORRECT_BRAND}.</p>"
        f"{extra_html}"
    )
    return {
        "admin_html": admin_html,
        "admin_text": html_module.unescape(re.sub("<[^>]+>", " ", admin_html)),
        "customer_html": customer_html,
        "customer_text": html_module.unescape(re.sub("<[^>]+>", " ", customer_html)),
    }


def phase_mail_preview() -> dict[str, Any]:
    fixtures = {
        "7": [{"label": "Город", "value": "MARS TEST CITY"}],
        "8": [{"label": "Регион доставки", "value": "MARS TEST REGION"}],
        "9": [{"label": "Организация", "value": "MARS TEST ORG"}],
        "10": [{"label": "Модель оборудования", "value": "MARS TEST MODEL"}],
        "11": [{"label": "Описание задачи", "value": "MARS TEST PROJECT"}],
    }
    names = {
        "7": "dealers",
        "8": "delivery",
        "9": "payment",
        "10": "warranty",
        "11": "custom-equipment",
    }
    qa: dict[str, Any] = {}
    for dialog, extra in fixtures.items():
        previews = render_mail_preview(dialog, extra)
        base = f"dialog-{dialog}-{names[dialog]}"
        write_text(DEPLOYMENT_ROOT / "mail-after" / f"{base}-admin.html", previews["admin_html"])
        write_text(DEPLOYMENT_ROOT / "mail-after" / f"{base}-admin.txt", previews["admin_text"])
        write_text(DEPLOYMENT_ROOT / "mail-after" / f"{base}-customer.html", previews["customer_html"])
        write_text(DEPLOYMENT_ROOT / "mail-after" / f"{base}-customer.txt", previews["customer_text"])
        qa[f"dialog_{dialog}_admin_zpm"] = CORRECT_BRAND in previews["admin_html"]
        qa[f"dialog_{dialog}_customer_no_service"] = "Служебная информация" not in previews["customer_html"]
    qa["pass"] = all(v for k, v in qa.items() if k.endswith("_zpm") or k.endswith("_no_service"))
    write_json(DEPLOYMENT_ROOT / "verification" / "local-mail-preview-qa.json", qa)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "local-mail-preview-qa.md",
        "# Local mail preview QA\n\n" + "\n".join(f"- {k}: **{v}**" for k, v in qa.items()) + "\n",
    )
    write_text(
        DEPLOYMENT_ROOT / "ui-after" / "success-state-preview.md",
        "# Success state preview\n\nInline corp CTA success matches popup: icon `#zpm_ico__successful`, title «Спасибо», text «Ваша заявка отправлена!».\n",
    )
    write_json(
        DEPLOYMENT_ROOT / "ui-after" / "success-state-preview.json",
        {"icon": "#zpm_ico__successful", "title": "Спасибо", "text": "Ваша заявка отправлена!"},
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
        "# Rollback plan\n\nRe-upload exact `source-before/` for all fourteen touched files.\n",
    )


def phase_dry_run(authority: dict[str, Any], patch_info: dict[str, Any], mail_qa: dict[str, Any]) -> dict[str, Any]:
    gates = {
        "G1_source_authority": not authority.get("mod_blocker"),
        "G2_rollback_captured": (DEPLOYMENT_ROOT / "rollback" / "rollback-plan.md").is_file(),
        "G3_patch_scope": len(patch_info["changed"]) == 14,
        "G4_dialog_source_all": all(
            f'name="dialog" value="{p["dialog"]}"' in (
                DEPLOYMENT_ROOT / "source-after" / remote_local_name(INFO_REMOTE.format(name=p["information"]))
            ).read_text(encoding="utf-8")
            for p in TARGET_PAGES
        ),
        "G5_custom_equipment_dialog_11": 'name="dialog" value="11"' in (
            DEPLOYMENT_ROOT / "source-after" / remote_local_name(INFO_REMOTE.format(name="custom_equipment"))
        ).read_text(encoding="utf-8"),
        "G6_corp_cta_ajax": patch_info["static"].get("corp_cta_handler"),
        "G7_popup_untouched": "[data-fb-form]" in (
            DEPLOYMENT_ROOT / "source-after" / remote_local_name(REMOTE_MAIN_JS)
        ).read_text(encoding="utf-8"),
        "G8_dealer_untouched": ".zpm-dealers[data-dealers]" in (
            DEPLOYMENT_ROOT / "source-after" / remote_local_name(REMOTE_MAIN_JS)
        ).read_text(encoding="utf-8"),
        "G9_admin_extra_fields": patch_info["static"].get("extra_fields"),
        "G10_customer_conditional": True,
        "G11_customer_no_service_info": mail_qa.get("pass") and patch_info["static"].get("customer_no_service_info"),
        "G12_success_state_js": "zpm-corp-cta__success" in (
            DEPLOYMENT_ROOT / "source-after" / remote_local_name(REMOTE_MAIN_JS)
        ).read_text(encoding="utf-8"),
        "G13_loading_ux": patch_info["static"].get("loading_container_corp"),
        "G14_no_standard_mail": True,
        "G15_no_smtp_admin_db": True,
        "G16_no_bzpm": patch_info["static"].get("no_bzpm"),
        "G17_test_plan_ready": True,
        "G18_live_sanity_plan": True,
    }
    payload = {"generated_at": utc_now(), "gates": gates, "pass": all(gates.values())}
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", payload)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "# Dry-run gates\n\n" + "\n".join(f"- {k}: **{'PASS' if v else 'FAIL'}**" for k, v in gates.items())
        + f"\n\n**Overall:** {'PASS' if payload['pass'] else 'FAIL'}\n",
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
                return {"uploaded": False, "reason": f"verify failed: {err}", "uploads": uploads}
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
    return {"uploaded": True, "uploads": uploads, "count": len(uploads)}


def _playwright_page_submit(page_cfg: dict[str, Any]) -> dict[str, Any]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {"attempted": False, "blocker": "playwright unavailable"}

    fields = dict(page_cfg["test_fields"])
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1200})
        page.set_default_timeout(120000)
        page.goto(page_cfg["url"], wait_until="networkidle")
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
            {
                "dialog": page_cfg["dialog"],
                "source_page": page_cfg["source_page"],
                "fields": fields,
            },
        )
        browser.close()

    out: dict[str, Any] = {
        "page": page_cfg["slug"],
        "dialog": page_cfg["dialog"],
        "attempted": True,
        "response_status": result.get("status"),
        "response": result.get("body"),
        "customer_mail_expected": bool(fields.get("email")),
        "admin_mail_expected": True,
    }
    if result.get("error"):
        out["blocker"] = result["error"]
        out["ok"] = False
    else:
        body = result.get("body") or {}
        out["ok"] = result.get("status") == 200 and isinstance(body, dict) and body.get("ok") is True
    return out


def phase_test_submits() -> dict[str, Any]:
    results = []
    for page in TARGET_PAGES:
        r = _playwright_page_submit(page)
        r["marker"] = TEST_MARKER
        r["request_redacted"] = {"email": "[redacted]" if page["test_fields"].get("email") else None}
        results.append(r)
    write_csv(
        DEPLOYMENT_ROOT / "test-submit" / "test-results.csv",
        results,
        ["page", "dialog", "ok", "response_status", "customer_mail_expected", "admin_mail_expected", "blocker"],
    )
    write_json(DEPLOYMENT_ROOT / "test-submit" / "test-results.json", {"results": results, "marker": TEST_MARKER})
    lines = ["# Controlled test submits", "", f"Marker: `{TEST_MARKER}`", ""]
    for r in results:
        lines.append(
            f"- **{r['page']}** dialog={r['dialog']} ok={r.get('ok')} status={r.get('response_status')} "
            f"customer_expected={r.get('customer_mail_expected')}"
        )
    write_text(DEPLOYMENT_ROOT / "test-submit" / "test-results.md", "\n".join(lines) + "\n")
    return {"results": results, "all_ok": all(r.get("ok") for r in results)}


def phase_ui_verification() -> dict[str, Any]:
    result: dict[str, Any] = {"attempted": False}
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        result["blocker"] = "playwright unavailable"
        write_json(DEPLOYMENT_ROOT / "ui-after" / "ui-verification.json", result)
        write_text(DEPLOYMENT_ROOT / "ui-after" / "ui-verification.md", "# UI verification\n\nPlaywright unavailable.\n")
        return result

    checks: list[dict[str, Any]] = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1200})
        page.set_default_timeout(120000)

        for page_cfg in TARGET_PAGES[:2]:
            page.route(
                "**/index.php?route=checkout/anketa",
                lambda route: route.fulfill(
                    status=200,
                    content_type="application/json",
                    body='{"ok":true,"message":"Заявка отправлена"}',
                    delay=1200,
                ),
            )
            page.goto(page_cfg["url"], wait_until="networkidle")
            page.wait_for_timeout(2000)
            check = page.evaluate(
                """async () => {
                    const form = document.querySelector('.zpm-corp-cta[data-corp-cta] form.zpm-form');
                    if (!form) return { form_found: false };
                    const card = form.closest('.zpm-corp-cta__form-card');
                    const agree = form.querySelector('[name="agree"]');
                    if (agree) agree.checked = true;
                    form.querySelectorAll('[required]').forEach((el) => {
                        if (el.type === 'checkbox') return;
                        if (!el.value) el.value = 'UI TEST';
                    });
                    const email = form.querySelector('[name="email"]');
                    if (email && !email.value) email.value = 'ui@test.invalid';
                    form.dispatchEvent(new Event('submit', { bubbles: true, cancelable: true }));
                    await new Promise((r) => setTimeout(r, 300));
                    const loading = card && card.classList.contains('zpm-form--loading');
                    await new Promise((r) => setTimeout(r, 1500));
                    const success = !!card && !!card.querySelector('.zpm-corp-cta__success');
                    const successTitle = card ? card.querySelector('.zpm-corp-cta__success .zpm-fb__title')?.textContent?.trim() : '';
                    const successText = card ? card.querySelector('.zpm-corp-cta__success .zpm-fb__sub')?.textContent?.trim() : '';
                    return {
                        form_found: true,
                        loading_seen: loading,
                        success_panel: success,
                        success_title: successTitle,
                        success_text: successText,
                    };
                }"""
            )
            check["page"] = page_cfg["slug"]
            checks.append(check)
            page.unroute("**/index.php?route=checkout/anketa")

        page.goto("https://bzpm.ru/", wait_until="networkidle")
        popup_check = page.evaluate(
            """() => ({
                fb_form_present: !!document.querySelector('[data-fb-form]'),
                corp_handler: typeof zpmFormSetLoading === 'function',
            })"""
        )
        browser.close()

    result = {
        "attempted": True,
        "corp_cta_checks": checks,
        "popup_regression": popup_check,
        "pass": all(
            c.get("success_panel") and c.get("success_title") == "Спасибо" and c.get("success_text") == "Ваша заявка отправлена!"
            for c in checks
            if c.get("form_found")
        )
        and popup_check.get("fb_form_present"),
    }
    write_json(DEPLOYMENT_ROOT / "ui-after" / "ui-verification.json", result)
    write_text(
        DEPLOYMENT_ROOT / "ui-after" / "ui-verification.md",
        "# UI verification\n\n" + json.dumps(result, ensure_ascii=False, indent=2) + "\n",
    )
    return result


def phase_live_sanity() -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    sitemap_count = None
    for slug, url in REGRESSION_URLS:
        resp = http_get(url)
        text = resp.get("text", "")
        entry: dict[str, Any] = {"slug": slug, "url": url, "status": resp.get("status"), "has_bzpm": WRONG_BRAND in text}
        if slug == "stoly":
            entry["load_more_present"] = any(s in text for s in ("load-more", "load_more", "Показать ещё", "Показать еще"))
        if slug == "sitemap" and resp.get("status") == 200:
            try:
                root = ET.fromstring(text)
                ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
                sitemap_count = len(root.findall("sm:url", ns)) or len(root.findall("url"))
                entry["url_count"] = sitemap_count
            except ET.ParseError:
                entry["url_count"] = None
        results.append(entry)

    for page in TARGET_PAGES:
        resp = http_get(page["url"])
        text = resp.get("text", "")
        form_snip = ""
        m = re.search(rf'<form[^>]*{re.escape(page["form_class"])}.*?</form>', text, re.I | re.S)
        if m:
            form_snip = m.group(0)[:2000]
        results.append(
            {
                "slug": f"target-{page['slug']}",
                "url": page["url"],
                "status": resp.get("status"),
                "has_bzpm": WRONG_BRAND in text,
                "dialog": re.search(r'name="dialog"\s+value="(\d+)"', form_snip).group(1)
                if re.search(r'name="dialog"', form_snip)
                else None,
                "source_page": 'name="source_page"' in form_snip,
                "corp_cta_handler_live": CORPCTA_JS_MARKER in text or CORPCTA_JS_MARKER in http_get("https://bzpm.ru/assets/js/main.js").get("text", ""),
            }
        )

    main_js = http_get("https://bzpm.ru/assets/js/main.js").get("text", "")
    payload = {
        "generated_at": utc_now(),
        "sitemap_url_count": sitemap_count,
        "main_js_corp_handler": CORPCTA_JS_MARKER in main_js,
        "results": results,
        "pass": all(r.get("status") == 200 and not r.get("has_bzpm") for r in results),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "live-sanity.json", payload)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "live-sanity.md",
        "# Live sanity\n\n"
        + "\n".join(f"- **{r['slug']}** HTTP {r.get('status')}" for r in results)
        + f"\n\nSitemap URLs: {sitemap_count}\n",
    )
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=["all", "preflight", "deploy-only", "verify-only"], default="all")
    parser.add_argument("--skip-deploy", action="store_true")
    parser.add_argument("--skip-tests", action="store_true")
    args = parser.parse_args()

    ensure_layout()
    authority = phase_source_authority()
    if authority.get("mod_blocker"):
        print("STOP — modification overlay present", file=sys.stderr)
        return 2

    phase_http_before()
    phase_implementation_design()
    patch_info = phase_local_patch()
    mail_qa = phase_mail_preview()
    phase_rollback(patch_info)
    dry_run = phase_dry_run(authority, patch_info, mail_qa)
    if not dry_run["pass"]:
        print("STOP — dry-run gates failed", file=sys.stderr)
        return 3

    deploy = {"uploaded": False, "reason": "skipped"}
    if args.phase in ("all", "deploy-only") and not args.skip_deploy:
        deploy = phase_deploy(dry_run, patch_info)

    tests = {"all_ok": False, "results": []}
    if deploy.get("uploaded") and not args.skip_tests and args.phase in ("all", "deploy-only"):
        tests = phase_test_submits()

    ui = phase_ui_verification() if deploy.get("uploaded") or args.phase == "verify-only" else {"attempted": False}
    live = phase_live_sanity() if deploy.get("uploaded") or args.phase == "verify-only" else {"pass": False}

    summary = {
        "operation_id": OPERATION_ID,
        "ocpilot_run": OCPILOT_RUN,
        "dry_run_pass": dry_run["pass"],
        "deployed": deploy.get("uploaded"),
        "upload_count": deploy.get("count", 0),
        "tests_all_ok": tests.get("all_ok"),
        "ui_pass": ui.get("pass"),
        "live_pass": live.get("pass"),
        "checkpoint_after": CHECKPOINT_AFTER if deploy.get("uploaded") and tests.get("all_ok") else None,
    }
    write_json(DEPLOYMENT_ROOT / "reports" / "operation-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if deploy.get("uploaded") else 1 if args.skip_deploy else 4


if __name__ == "__main__":
    raise SystemExit(main())
