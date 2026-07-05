#!/usr/bin/env python3
"""SITE-002 mail recipients discovery — read-only Production FTP + analysis."""
from __future__ import annotations

import argparse
import ftplib
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-MAIL-RECIPIENTS-DISCOVERY-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-LOAD-MORE-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-MAIL-RECIPIENTS-DISCOVERY-01"
)
SUBDIRS = ("source", "source-map", "findings", "manifests", "logs")

SEARCH_TERMS = (
    "anketa",
    "mail",
    "Mail",
    "$mail",
    "send",
    "recipient",
    "setTo",
    "setFrom",
    "setSender",
    "config_mail",
    "config_email",
    "mail_alert",
    "order_status",
    "addOrderHistory",
)

PROBE_PATHS = [
    "/public_html/catalog/controller/checkout/anketa.php",
    "/public_html/catalog/controller/checkout/cart.php",
    "/public_html/catalog/controller/checkout/confirm.php",
    "/public_html/catalog/controller/checkout/checkout.php",
    "/public_html/catalog/controller/information/contact.php",
    "/public_html/catalog/controller/mail/order.php",
    "/public_html/catalog/model/checkout/order.php",
    "/public_html/catalog/model/mail/order.php",
    "/public_html/system/library/mail.php",
    "/public_html/system/library/mail/smtp.php",
    "/public_html/assets/js/main.js",
    "/public_html/catalog/view/theme/default/template/sections/blockcommercialtrust.twig",
    "/public_html/catalog/view/theme/default/template/sections/fancyboxforms.twig",
    "/public_html/catalog/view/theme/default/template/sections/blockdealersform.twig",
    "/public_html/catalog/view/theme/default/template/sections/blockanyquestionsform.twig",
    "/public_html/catalog/view/theme/default/template/information/contact.twig",
    "/public_html/catalog/controller/common/header.php",
    "/public_html/catalog/controller/common/footer.php",
    "/public_html/catalog/controller/extension/module/html.php",
    "/public_html/admin/controller/setting/setting.php",
    "/public_html/admin/model/setting/setting.php",
]

LIST_DIRS = [
    "/public_html/catalog/controller/checkout",
    "/public_html/catalog/controller/common",
    "/public_html/catalog/controller/mail",
    "/public_html/catalog/model/mail",
    "/public_html/catalog/controller/extension/module",
]

EMAIL_RE = re.compile(
    r"(?<![A-Za-z0-9._%+-])([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})(?![A-Za-z0-9._%+-])"
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data, encoding="utf-8", newline="\n")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def mask_email(email: str) -> str:
    local, _, domain = email.partition("@")
    if not domain:
        return "<INVALID_EMAIL>"
    if len(local) <= 1:
        masked_local = local + "***"
    else:
        masked_local = local[0] + "***"
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
        if name.startswith("/"):
            out.append(name)
        else:
            out.append(prefix + base)
    return sorted(set(out))


def local_name_for(remote_path: str) -> str:
    rel = remote_path.removeprefix("/public_html/").replace("/", "__")
    return rel or "root"


def scan_text(text: str) -> dict[str, Any]:
    lowered = text.lower()
    matched_terms = [term for term in SEARCH_TERMS if term.lower() in lowered]
    emails = sorted(set(EMAIL_RE.findall(text)))
    return {
        "matched_terms": matched_terms,
        "email_count": len(emails),
        "emails_masked": [mask_email(e) for e in emails],
        "has_setTo": "setTo(" in text,
        "has_mail_new": bool(re.search(r"new\s+Mail\s*\(", text)),
        "has_send": bool(re.search(r"\$mail\s*->\s*send\s*\(", text)),
        "has_config_email": "config_email" in lowered,
        "has_config_mail_alert": "config_mail_alert" in lowered,
        "has_dialog_field": "dialog" in lowered,
        "has_csrf": "csrf" in lowered,
        "has_recaptcha": "recaptcha" in lowered or "g-recaptcha" in lowered,
    }


def extract_functions(text: str) -> list[str]:
    names = re.findall(r"function\s+([A-Za-z0-9_]+)\s*\(", text)
    classes = re.findall(r"class\s+([A-Za-z0-9_]+)", text)
    return sorted(set(names + classes))


def classify_file(remote_path: str, scan: dict[str, Any]) -> str:
    if scan["email_count"] and (scan["has_setTo"] or scan["has_send"]):
        return "MAIL_RECIPIENT_CANDIDATE"
    if scan["has_mail_new"] or scan["has_send"]:
        return "MAIL_SENDER"
    if "anketa" in remote_path.lower():
        return "FORM_HANDLER"
    if scan["has_dialog_field"] or "fancybox" in remote_path.lower() or "form" in remote_path.lower():
        return "FORM_FRONTEND"
    if scan["has_config_email"] or scan["has_config_mail_alert"]:
        return "OC_CONFIG_MAIL"
    if scan["matched_terms"]:
        return "MAIL_RELATED"
    return "CONTEXT"


def ensure_dirs() -> None:
    for name in SUBDIRS:
        (DEPLOYMENT_ROOT / name).mkdir(parents=True, exist_ok=True)


def discover() -> dict[str, Any]:
    ensure_dirs()
    fields = parse_production_secrets(SECRETS_PATH)
    ftp = ftp_connect(fields)
    log_lines: list[str] = [f"[{utc_now()}] FTP connected read-only"]

    dir_listings: dict[str, list[str]] = {}
    discovered_paths: set[str] = set(PROBE_PATHS)

    try:
        for remote_dir in LIST_DIRS:
            listing = ftp_list_dir(ftp, remote_dir)
            dir_listings[remote_dir] = listing
            log_lines.append(f"LIST {remote_dir}: {len(listing)} entries")
            for entry in listing:
                base = entry.split("/")[-1].lower()
                if any(term in base for term in ("anketa", "mail", "contact", "callback", "form", "cart", "checkout", "order")):
                    if not entry.startswith("/"):
                        entry = remote_dir.rstrip("/") + "/" + entry.split("/")[-1]
                    discovered_paths.add(entry)

        files: list[dict[str, Any]] = []
        for remote_path in sorted(discovered_paths):
            entry: dict[str, Any] = {"remote_path": remote_path}
            try:
                data = ftp_download(ftp, remote_path)
                text = data.decode("utf-8", errors="replace")
                local_name = local_name_for(remote_path)
                out_path = DEPLOYMENT_ROOT / "source" / local_name
                out_path.write_bytes(data)
                scan = scan_text(text)
                entry.update(
                    {
                        "status": "downloaded",
                        "local_name": local_name,
                        "size": len(data),
                        "sha256": sha256_bytes(data),
                        "scan": scan,
                        "functions_and_classes": extract_functions(text),
                        "classification": classify_file(remote_path, scan),
                        "contains_recipient_hardcode": scan["email_count"] > 0 and scan["has_setTo"],
                        "contains_form_submit_handling": "anketa" in remote_path.lower()
                        or scan["has_dialog_field"]
                        or "submit" in text.lower(),
                        "contains_order_mail_handling": "order" in remote_path.lower()
                        and (scan["has_send"] or scan["has_config_mail_alert"]),
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

    write_text(DEPLOYMENT_ROOT / "logs" / "discovery.log", "\n".join(log_lines) + "\n")
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "change_type": "mail-recipients-discovery",
            "remote_changes_allowed": False,
            "email_send_allowed": False,
            "db_write_allowed": False,
            "admin_save_allowed": False,
            "cron_change_allowed": False,
            "import_execution_allowed": False,
            "timestamp": utc_now(),
        },
    )
    discovery = {
        "operation_id": OPERATION_ID,
        "timestamp": utc_now(),
        "dir_listings": dir_listings,
        "files": files,
        "downloaded_count": sum(1 for f in files if f.get("status") == "downloaded"),
        "error_count": sum(1 for f in files if f.get("status") == "error"),
    }
    write_json(DEPLOYMENT_ROOT / "source-map" / "discovered-mail-files.json", discovery)
    return discovery


def build_source_map_md(discovery: dict[str, Any]) -> str:
    lines = [
        "# Discovered mail files — SITE-002 Production",
        "",
        f"Operation: `{OPERATION_ID}`",
        f"Timestamp: {discovery['timestamp']}",
        "",
        "## Directory listings",
        "",
    ]
    for remote_dir, entries in discovery.get("dir_listings", {}).items():
        lines.append(f"### `{remote_dir}`")
        lines.append("")
        if not entries:
            lines.append("_empty or inaccessible_")
        else:
            for entry in entries:
                lines.append(f"- `{entry}`")
        lines.append("")

    lines.extend(["## Downloaded / probed files", ""])
    for item in discovery.get("files", []):
        lines.append(f"### `{item['remote_path']}`")
        lines.append("")
        lines.append(f"- Status: **{item.get('status', 'unknown')}**")
        if item.get("status") == "downloaded":
            lines.append(f"- Classification: `{item.get('classification')}`")
            lines.append(f"- Recipient hardcode: **{'yes' if item.get('contains_recipient_hardcode') else 'no'}**")
            lines.append(f"- Form submit handling: **{'yes' if item.get('contains_form_submit_handling') else 'no'}**")
            lines.append(f"- Order mail handling: **{'yes' if item.get('contains_order_mail_handling') else 'no'}**")
            scan = item.get("scan", {})
            if scan.get("emails_masked"):
                lines.append(f"- Masked emails found: {', '.join(scan['emails_masked'])}")
            if item.get("functions_and_classes"):
                lines.append(f"- Functions/classes: `{', '.join(item['functions_and_classes'][:20])}`")
        elif item.get("error"):
            lines.append(f"- Error: {item['error']}")
        lines.append("")
    return "\n".join(lines)


def analyze_anketa(source_dir: Path) -> dict[str, Any] | None:
    candidates = list(source_dir.glob("*checkout__anketa.php"))
    if not candidates:
        return None
    text = candidates[0].read_text(encoding="utf-8", errors="replace")
    info: dict[str, Any] = {
        "file": str(candidates[0].name),
        "lines": text.count("\n") + 1,
    }
    for pattern, key in (
        (r"setTo\s*\(\s*['\"]([^'\"]+)['\"]", "setTo_literals"),
        (r"setTo\s*\(\s*\$([A-Za-z0-9_]+)", "setTo_vars"),
        (r"\$([A-Za-z0-9_]*mail[A-Za-z0-9_]*)\s*=\s*['\"]([^'\"@]+@[^'\"]+)['\"]", "mail_var_literals"),
        (r"dialog\s*[=<>!]+\s*['\"]?\d+", "dialog_checks"),
    ):
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        if matches:
            if key == "mail_var_literals":
                info[key] = [mask_email(m[1]) for m in matches]
            elif key == "setTo_literals":
                info[key] = [mask_email(m) if "@" in m else m for m in matches]
            else:
                info[key] = matches
    return info


def build_findings(discovery: dict[str, Any]) -> None:
    source_dir = DEPLOYMENT_ROOT / "source"
    anketa = analyze_anketa(source_dir)

    recipients: list[dict[str, Any]] = []
    for item in discovery.get("files", []):
        if item.get("status") != "downloaded":
            continue
        scan = item.get("scan", {})
        for masked in scan.get("emails_masked", []):
            classification = "SAFE UNKNOWN"
            remote = item["remote_path"].lower()
            if scan.get("has_setTo") and "anketa" in remote:
                classification = "FORM_NOTIFICATION_EMAIL"
            elif scan.get("has_setTo"):
                classification = "FORM_NOTIFICATION_EMAIL"
            elif "info@" in masked or "sales@" in masked or "order@" in masked:
                classification = "POSSIBLE_SITE_OWNER_RECIPIENT"
            elif scan.get("has_config_email"):
                classification = "ORDER_NOTIFICATION_EMAIL"
            elif item["remote_path"].endswith("mail.php"):
                classification = "SYSTEM_FROM_EMAIL"
            recipients.append(
                {
                    "masked_email": masked,
                    "source_file": item["remote_path"],
                    "classification": classification,
                    "hardcoded": scan.get("has_setTo", False),
                    "from_opencart_config": scan.get("has_config_email", False) or scan.get("has_config_mail_alert", False),
                    "multiple_recipients_supported": "SAFE UNKNOWN",
                }
            )

    write_json(DEPLOYMENT_ROOT / "findings" / "recipient-inventory.json", {"recipients": recipients, "anketa_analysis": anketa})
    write_json(
        DEPLOYMENT_ROOT / "findings" / "mail-flow-map.json",
        {
            "flows": [
                {
                    "id": "form_anketa",
                    "name": "Site forms via checkout/anketa",
                    "route": "checkout/anketa",
                    "entry_urls": ["All zpm-form AJAX submits", "Fancybox modal forms", "Commercial Trust dialog=7"],
                    "controller": "/public_html/catalog/controller/checkout/anketa.php",
                    "frontend": "/public_html/assets/js/main.js",
                    "anketa_analysis": anketa,
                },
                {
                    "id": "contact_opencart",
                    "name": "OpenCart native contact",
                    "route": "information/contact",
                    "controller": "/public_html/catalog/controller/information/contact.php",
                },
                {
                    "id": "order_native",
                    "name": "OpenCart order notifications",
                    "route": "checkout confirm / mail order",
                    "controller_candidates": [
                        "/public_html/catalog/model/checkout/order.php",
                        "/public_html/catalog/controller/mail/order.php",
                    ],
                },
            ]
        },
    )

    md_inventory = ["# Recipient inventory", "", f"Generated: {utc_now()}", ""]
    for r in recipients:
        md_inventory.extend(
            [
                f"## {r['masked_email']}",
                f"- Source: `{r['source_file']}`",
                f"- Classification: `{r['classification']}`",
                f"- Hardcoded: {r['hardcoded']}",
                f"- OpenCart config: {r['from_opencart_config']}",
                "",
            ]
        )
    write_text(DEPLOYMENT_ROOT / "findings" / "recipient-inventory.md", "\n".join(md_inventory))

    write_text(
        DEPLOYMENT_ROOT / "findings" / "mail-flow-map.md",
        "# Mail flow map\n\nSee mail-flow-map.json and repository report for full detail.\n",
    )
    write_text(
        DEPLOYMENT_ROOT / "findings" / "current-mail-architecture.md",
        "# Current mail architecture\n\nSee repository report.\n",
    )
    write_text(
        DEPLOYMENT_ROOT / "findings" / "implementation-options.md",
        "# Implementation options\n\nSee repository report.\n",
    )
    write_text(
        DEPLOYMENT_ROOT / "findings" / "recommendation.md",
        "# Recommendation\n\nSee repository report.\n",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--discover", action="store_true", help="Run FTP discovery")
    args = parser.parse_args()
    if not args.discover:
        parser.print_help()
        return 0
    discovery = discover()
    write_text(DEPLOYMENT_ROOT / "source-map" / "discovered-mail-files.md", build_source_map_md(discovery))
    build_findings(discovery)
    print(json.dumps({"downloaded": discovery["downloaded_count"], "errors": discovery["error_count"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
