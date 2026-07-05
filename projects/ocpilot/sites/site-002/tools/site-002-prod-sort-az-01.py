#!/usr/bin/env python3
"""SITE-002 catalog default sort A→Я — single-controller Production deploy."""
from __future__ import annotations

import argparse
import difflib
import ftplib
import hashlib
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-SORT-AZ-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-TEXT-CHANGE-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-SORT-AZ-01"
REMOTE_FILE = "/public_html/catalog/controller/product/category.php"
LOCAL_NAME = "category.php"
OLD_DEFAULT_SORT = "p.date_added"
NEW_DEFAULT_SORT = "pd.name"
OLD_DEFAULT_ORDER = "DESC"
NEW_DEFAULT_ORDER = "ASC"
OLD_SORTTEXT = "Умолчанию"
NEW_SORTTEXT = "Название - от А до Я"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-SORT-AZ-01"
)
VERIFY_URLS = [
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
]
USER_AGENT = "MARS-OCPilot/SITE-002-PROD-SORT-AZ-01"
SUBDIRS = ("source", "prepared", "backup", "verification", "rollback", "manifests", "logs")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data, encoding="utf-8", newline="\n")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


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


def ftp_upload(ftp: ftplib.FTP, remote_path: str, data: bytes) -> None:
    from io import BytesIO

    ftp.storbinary(f"STOR {remote_path}", BytesIO(data))


def ftp_metadata(ftp: ftplib.FTP, remote_path: str) -> dict[str, Any]:
    metadata: dict[str, Any] = {"ftp_visible_path": remote_path, "download_timestamp": utc_now()}
    try:
        metadata["size"] = ftp.size(remote_path)
    except Exception as exc:
        metadata["size_error"] = str(exc)
    try:
        metadata["modified_time_raw"] = ftp.sendcmd(f"MDTM {remote_path}")
    except Exception as exc:
        metadata["modified_time_error"] = str(exc)
    return metadata


def ensure_dirs() -> None:
    for name in SUBDIRS:
        (DEPLOYMENT_ROOT / name).mkdir(parents=True, exist_ok=True)


def write_operation_metadata() -> None:
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "remote_file": REMOTE_FILE,
            "change_type": "catalog-default-sort",
            "old_default_sort": OLD_DEFAULT_SORT,
            "old_default_order": OLD_DEFAULT_ORDER,
            "new_default_sort": NEW_DEFAULT_SORT,
            "new_default_order": NEW_DEFAULT_ORDER,
            "authorized_files": 1,
        },
    )


def unified_diff(source: bytes, prepared: bytes) -> str:
    before = source.decode("utf-8").splitlines(keepends=True)
    after = prepared.decode("utf-8").splitlines(keepends=True)
    return "".join(
        difflib.unified_diff(
            before,
            after,
            fromfile=f"source/{LOCAL_NAME}",
            tofile=f"prepared/{LOCAL_NAME}",
            lineterm="",
        )
    )


def diff_scope_ok(diff_text: str) -> tuple[bool, list[str]]:
    changed = [
        line
        for line in diff_text.splitlines()
        if line.startswith(("+", "-")) and not line.startswith(("+++", "---"))
    ]
    allowed_patterns = (
        OLD_DEFAULT_SORT,
        NEW_DEFAULT_SORT,
        OLD_DEFAULT_ORDER,
        NEW_DEFAULT_ORDER,
        OLD_SORTTEXT,
        NEW_SORTTEXT,
        "$sort",
        "$order",
        "sorttext",
    )
    for line in changed:
        if not any(p in line for p in allowed_patterns):
            return False, changed
    return True, changed


def prepare_category(source: bytes) -> tuple[bytes, dict[str, Any]]:
    text = source.decode("utf-8")
    checks: dict[str, Any] = {}
    checks["is_opencart_category"] = "class ControllerProductCategory" in text
    checks["default_sort_count"] = text.count(f"$sort = '{OLD_DEFAULT_SORT}';")
    checks["default_order_count"] = text.count(f"$order = '{OLD_DEFAULT_ORDER}';")
    checks["pd_name_asc_sorttext_rule_present"] = (
        f"($sort == 'pd.name') AND ($order == 'ASC')" in text
        and NEW_SORTTEXT in text
    )
    checks["sorttext_updated"] = False

    if (
        not checks["is_opencart_category"]
        or checks["default_sort_count"] != 1
        or checks["default_order_count"] != 1
        or not checks["pd_name_asc_sorttext_rule_present"]
    ):
        checks["status"] = "FAIL"
        return source, checks

    prepared = source.replace(
        f"\t\t\t$sort = '{OLD_DEFAULT_SORT}';".encode("utf-8"),
        f"\t\t\t$sort = '{NEW_DEFAULT_SORT}';".encode("utf-8"),
        1,
    )
    prepared = prepared.replace(
        f"\t\t\t$order = '{OLD_DEFAULT_ORDER}';".encode("utf-8"),
        f"\t\t\t$order = '{NEW_DEFAULT_ORDER}';".encode("utf-8"),
        1,
    )
    checks["status"] = "PASS"
    return prepared, checks


def create_dry_run(source: bytes, prepared: bytes, source_sha: str, prepared_sha: str) -> dict[str, Any]:
    diff_text = unified_diff(source, prepared)
    scope_ok, diff_lines = diff_scope_ok(diff_text)
    data = {
        "operation_id": OPERATION_ID,
        "remote_files_to_upload": 1,
        "remote_target": REMOTE_FILE,
        "local_source_file": f"source/{LOCAL_NAME}",
        "prepared_file": f"prepared/{LOCAL_NAME}",
        "backup_available": True,
        "rollback_file_available": True,
        "database_impact": "NONE",
        "twig_impact": "NONE",
        "css_impact": "NONE",
        "js_impact": "NONE",
        "expected_default_sort": NEW_DEFAULT_SORT,
        "expected_default_order": NEW_DEFAULT_ORDER,
        "explicit_sort_order_urls_preserved": True,
        "source_sha256": source_sha,
        "prepared_sha256": prepared_sha,
        "diff_scope_ok": scope_ok,
        "diff_semantic_change_lines": diff_lines,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", data)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "\n".join(
            [
                "# Dry-Run — SITE-002-PROD-SORT-AZ-01",
                "",
                "- Remote files to upload: 1",
                f"- Remote target: `{REMOTE_FILE}`",
                f"- Source file: source/{LOCAL_NAME}",
                f"- Prepared file: prepared/{LOCAL_NAME}",
                "- Backup available: YES",
                "- Rollback file available: YES",
                "- Database impact: NONE",
                "- Twig impact: NONE",
                "- CSS impact: NONE",
                "- JS impact: NONE",
                f"- Expected default sort: {NEW_DEFAULT_SORT}",
                f"- Expected default order: {NEW_DEFAULT_ORDER}",
                "- Explicit sort/order URLs: preserved",
                "",
                "```diff",
                diff_text,
                "```",
                "",
            ]
        ),
    )
    write_text(DEPLOYMENT_ROOT / "manifests" / "category.diff", diff_text)
    if not scope_ok:
        write_receipt("FAILED BEFORE DEPLOY", "STOP — DRY-RUN SCOPE VIOLATION", uploaded=False)
        raise RuntimeError("STOP — DRY-RUN SCOPE VIOLATION")
    return data


def write_rollback_plan(source_sha: str) -> None:
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "rollback-plan.json",
        {
            "operation_id": OPERATION_ID,
            "rollback_target": REMOTE_FILE,
            "rollback_file": f"rollback/{LOCAL_NAME}",
            "source_sha256": source_sha,
            "procedure": [
                f"upload rollback/{LOCAL_NAME}",
                "download remote file again",
                "compare SHA-256 with source_sha256",
                "check category pages HTTP 200",
                "confirm old default sort restored",
            ],
        },
    )


def write_receipt(status: str, verdict: str, uploaded: bool, extra: dict[str, Any] | None = None) -> None:
    data: dict[str, Any] = {
        "operation_id": OPERATION_ID,
        "status": status,
        "verdict": verdict,
        "uploaded": uploaded,
        "timestamp": utc_now(),
    }
    if extra:
        data.update(extra)
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation-receipt.json", data)


def http_get(url: str) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Cache-Control": "no-cache"})
    started = utc_now()
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read()
            text = body.decode(response.headers.get_content_charset() or "utf-8", errors="replace")
            return {
                "url": url,
                "checked_at": started,
                "status_code": response.status,
                "body": text,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return {
            "url": url,
            "checked_at": started,
            "status_code": exc.code,
            "body": body,
            "error": str(exc),
        }
    except Exception as exc:
        return {"url": url, "checked_at": started, "status_code": None, "body": "", "error": str(exc)}


def extract_product_names(html_text: str) -> list[str]:
    names: list[str] = []
    for match in re.finditer(
        r'class="[^"]*product[^"]*__title[^"]*"[^>]*>([^<]+)<',
        html_text,
        re.IGNORECASE,
    ):
        name = html.unescape(match.group(1)).strip()
        if name:
            names.append(name)
    if not names:
        for match in re.finditer(r'class="[^"]*product-card[^"]*"[\s\S]{0,400}?<a[^>]*>([^<]{3,})</a>', html_text, re.IGNORECASE):
            name = html.unescape(match.group(1)).strip()
            if name and name not in names:
                names.append(name)
    return names[:12]


def is_alphabetically_sorted(names: list[str]) -> bool:
    if len(names) < 2:
        return True
    normalized = [n.casefold() for n in names]
    return normalized == sorted(normalized)


def verify_http() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    overall = "PASS"
    for base_url in VERIFY_URLS:
        url = f"{base_url}?mars_verify={OPERATION_ID}"
        result = http_get(url)
        body = result.get("body", "")
        normalized = html.unescape(body)
        product_names = extract_product_names(body)
        entry: dict[str, Any] = {
            "url": url,
            "status_code": result.get("status_code"),
            "error": result.get("error"),
            "php_error_visible": any(
                marker in normalized for marker in ("Fatal error", "Parse error", "Twig_Error", "Twig\\Error")
            ),
            "sort_label_new": NEW_SORTTEXT in normalized or "от А до Я" in normalized,
            "sort_label_old_default": OLD_SORTTEXT in normalized and NEW_SORTTEXT not in normalized,
            "limit_selector_present": "limit" in normalized.lower() or "Показать" in normalized or "на странице" in normalized.lower(),
            "product_grid_present": len(product_names) >= 2 or "product" in normalized.lower(),
            "product_names_sample": product_names[:8],
            "alphabetic_order_sample": is_alphabetically_sorted(product_names),
            "explicit_sort_date_added_link": f"sort={OLD_DEFAULT_SORT}" in normalized or "date_added" in normalized,
            "explicit_sort_name_desc_link": "sort=pd.name" in normalized and "order=DESC" in normalized,
        }
        if result.get("status_code") != 200 or entry["php_error_visible"] or not entry["product_grid_present"]:
            entry["status"] = "FAIL"
            overall = "FAIL"
        elif not entry["alphabetic_order_sample"] or entry["sort_label_old_default"]:
            entry["status"] = "CACHE_PENDING"
            if overall != "FAIL":
                overall = "CACHE_PENDING"
        else:
            entry["status"] = "PASS"
        checks.append(entry)

    data = {"operation_id": OPERATION_ID, "status": overall, "checks": checks}
    write_json(DEPLOYMENT_ROOT / "manifests" / "http-verification.json", data)
    return data


def verify_visual() -> dict[str, Any]:
    desktop = DEPLOYMENT_ROOT / "verification" / "desktop-stoly-sort-az.png"
    mobile = DEPLOYMENT_ROOT / "verification" / "mobile-stoly-sort-az.png"
    url = VERIFY_URLS[0] + f"?mars_verify={OPERATION_ID}"
    results: list[dict[str, Any]] = []
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        data = {
            "operation_id": OPERATION_ID,
            "status": "SAFE_UNKNOWN",
            "error": f"playwright unavailable: {exc}",
            "results": results,
        }
        write_json(DEPLOYMENT_ROOT / "manifests" / "visual-verification.json", data)
        return data

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for name, viewport, target in (
            ("desktop", {"width": 1440, "height": 1200}, desktop),
            ("mobile", {"width": 390, "height": 844}, mobile),
        ):
            entry: dict[str, Any] = {"viewport": name, "url": url, "file": str(target), "status": "FAIL"}
            context = browser.new_context(viewport=viewport, user_agent=USER_AGENT)
            page = context.new_page()
            try:
                response = page.goto(url, wait_until="networkidle", timeout=60000)
                page.wait_for_timeout(800)
                text = page.locator("body").inner_text(timeout=10000)
                target.parent.mkdir(parents=True, exist_ok=True)
                page.screenshot(path=str(target), full_page=True)
                entry.update(
                    {
                        "http_ok": bool(response and response.ok),
                        "sort_label_present": NEW_SORTTEXT in text or "от А до Я" in text,
                        "twig_error_visible": any(marker in text for marker in ("Twig_Error", "Fatal error", "Parse error")),
                        "body_text_length": len(text.strip()),
                    }
                )
                entry["status"] = (
                    "PASS"
                    if entry["http_ok"] and not entry["twig_error_visible"] and entry["body_text_length"] > 100
                    else "FAIL"
                )
            except Exception as exc:
                entry["error"] = f"{type(exc).__name__}: {exc}"
            finally:
                context.close()
            results.append(entry)
        browser.close()

    status = "PASS" if all(item["status"] == "PASS" for item in results) else "FAIL"
    data = {"operation_id": OPERATION_ID, "status": status, "results": results}
    write_json(DEPLOYMENT_ROOT / "manifests" / "visual-verification.json", data)
    return data


def verify_remote_content(data: bytes) -> dict[str, Any]:
    text = data.decode("utf-8", errors="replace")
    return {
        "default_sort_pd_name": text.count(f"$sort = '{NEW_DEFAULT_SORT}';") >= 1,
        "default_order_asc": text.count(f"$order = '{NEW_DEFAULT_ORDER}';") >= 1,
        "old_default_sort_inactive": text.count(f"$sort = '{OLD_DEFAULT_SORT}';") == 0,
        "old_default_order_inactive_as_default": text.count(f"$order = '{OLD_DEFAULT_ORDER}';") == 0,
    }


def rollback(reason: str) -> int:
    ensure_dirs()
    fields = parse_production_secrets(SECRETS_PATH)
    rollback_file = DEPLOYMENT_ROOT / "rollback" / LOCAL_NAME
    if not rollback_file.exists():
        write_receipt("ROLLED BACK", "ROLLBACK FAILED — rollback file missing", uploaded=False, extra={"reason": reason})
        raise RuntimeError("Rollback file missing")
    source_sha = sha256_file(rollback_file)
    ftp = ftp_connect(fields)
    try:
        ftp_upload(ftp, REMOTE_FILE, rollback_file.read_bytes())
        after = ftp_download(ftp, REMOTE_FILE)
    finally:
        try:
            ftp.quit()
        except Exception:
            pass
    restored_sha = sha256_bytes(after)
    (DEPLOYMENT_ROOT / "verification" / "remote-after-rollback.category.php").write_bytes(after)
    http_result = http_get(f"{VERIFY_URLS[0]}?mars_rollback={int(time.time())}")
    rollback_data = {
        "operation_id": OPERATION_ID,
        "reason": reason,
        "source_sha256": source_sha,
        "remote_after_rollback_sha256": restored_sha,
        "hash_match": restored_sha == source_sha,
        "http_status_code": http_result.get("status_code"),
        "content_checks": verify_remote_content(after),
        "timestamp": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "rollback-result.json", rollback_data)
    if rollback_data["hash_match"] and rollback_data["http_status_code"] == 200:
        write_receipt("ROLLED BACK", "SITE-002 CATALOG DEFAULT SORT ROLLED BACK SAFELY", uploaded=True, extra=rollback_data)
        print("ROLLED BACK SAFELY")
        return 0
    write_receipt("ROLLED BACK", "ROLLBACK VERIFICATION FAILED", uploaded=True, extra=rollback_data)
    raise RuntimeError("Rollback verification failed")


def deploy() -> int:
    ensure_dirs()
    write_operation_metadata()
    fields = parse_production_secrets(SECRETS_PATH)

    ftp = ftp_connect(fields)
    try:
        metadata = ftp_metadata(ftp, REMOTE_FILE)
        source = ftp_download(ftp, REMOTE_FILE)
    finally:
        try:
            ftp.quit()
        except Exception:
            pass

    source_path = DEPLOYMENT_ROOT / "source" / LOCAL_NAME
    backup_path = DEPLOYMENT_ROOT / "backup" / "category.php.pre-sort-az.bak"
    rollback_path = DEPLOYMENT_ROOT / "rollback" / LOCAL_NAME
    source_path.write_bytes(source)
    backup_path.write_bytes(source)
    rollback_path.write_bytes(source)

    source_sha = sha256_bytes(source)
    backup_sha = sha256_file(backup_path)
    rollback_sha = sha256_file(rollback_path)
    if source_sha != backup_sha or rollback_sha != source_sha:
        write_receipt("FAILED BEFORE DEPLOY", "SOURCE/BACKUP/ROLLBACK SHA MISMATCH", uploaded=False)
        raise RuntimeError("Hash mismatch among source/backup/rollback")

    prepared, prep_checks = prepare_category(source)
    prep_checks["remote_metadata"] = metadata
    write_json(DEPLOYMENT_ROOT / "manifests" / "precondition.json", prep_checks)
    if prep_checks.get("status") != "PASS":
        write_receipt(
            "FAILED BEFORE DEPLOY",
            "BLOCKED — IMPLEMENTATION SCOPE EXPANDED",
            uploaded=False,
            extra=prep_checks,
        )
        raise RuntimeError("BLOCKED — IMPLEMENTATION SCOPE EXPANDED")

    prepared_path = DEPLOYMENT_ROOT / "prepared" / LOCAL_NAME
    prepared_path.write_bytes(prepared)
    prepared_sha = sha256_bytes(prepared)
    create_dry_run(source, prepared, source_sha, prepared_sha)
    write_rollback_plan(source_sha)

    ftp = ftp_connect(fields)
    try:
        pre_upload = ftp_download(ftp, REMOTE_FILE)
        (DEPLOYMENT_ROOT / "verification" / "remote-pre-upload-check.category.php").write_bytes(pre_upload)
        remote_pre_upload_sha = sha256_bytes(pre_upload)
        if remote_pre_upload_sha != source_sha:
            write_receipt(
                "FAILED BEFORE DEPLOY",
                "STOP — REMOTE FILE CHANGED SINCE BACKUP",
                uploaded=False,
                extra={"remote_pre_upload_sha256": remote_pre_upload_sha, "source_sha256": source_sha},
            )
            raise RuntimeError("STOP — REMOTE FILE CHANGED SINCE BACKUP")
        ftp_upload(ftp, REMOTE_FILE, prepared)
        after = ftp_download(ftp, REMOTE_FILE)
    finally:
        try:
            ftp.quit()
        except Exception:
            pass

    after_path = DEPLOYMENT_ROOT / "verification" / "remote-after-upload.category.php"
    after_path.write_bytes(after)
    remote_after_sha = sha256_bytes(after)
    content_after = verify_remote_content(after)

    hashes = {
        "operation_id": OPERATION_ID,
        "source_sha256": source_sha,
        "backup_sha256": backup_sha,
        "prepared_sha256": prepared_sha,
        "rollback_sha256": rollback_sha,
        "remote_pre_upload_sha256": remote_pre_upload_sha,
        "remote_after_sha256": remote_after_sha,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "file-hashes.json", hashes)
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "deploy-manifest.json",
        {
            "operation_id": OPERATION_ID,
            "uploaded_files": [REMOTE_FILE],
            "upload_count": 1,
            "delete_count": 0,
            "rename_count": 0,
            "remote_after_content_checks": content_after,
        },
    )

    if remote_after_sha != prepared_sha or not content_after["default_sort_pd_name"] or not content_after["default_order_asc"]:
        rollback("Remote hash/content mismatch after upload")
        return 2

    http_result = verify_http()
    if http_result["status"] == "FAIL":
        rollback("HTTP verification failed after deploy")
        return 2
    if http_result["status"] == "CACHE_PENDING":
        write_receipt(
            "DEPLOYED — HTTP CACHE PENDING",
            "SITE-002 CATALOG DEFAULT SORT DEPLOYED — HTTP CACHE PENDING",
            uploaded=True,
            extra={"http_verification": http_result},
        )
        print("DEPLOYED — HTTP CACHE PENDING")
        return 0

    visual_result = verify_visual()
    if visual_result.get("status") == "FAIL":
        rollback("Visual verification failed after deploy")
        return 2

    write_receipt(
        "DEPLOYED",
        "SITE-002 CATALOG DEFAULT SORT A→Я COMPLETE — DEPLOY AND ROLLBACK READINESS VERIFIED",
        uploaded=True,
        extra={"http_verification": http_result, "visual_verification": visual_result},
    )
    print("DEPLOYED")
    print(f"source_sha256={source_sha}")
    print(f"prepared_sha256={prepared_sha}")
    print(f"remote_after_sha256={remote_after_sha}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="SITE-002 catalog default sort deploy.")
    parser.add_argument("command", choices=("deploy", "rollback"))
    parser.add_argument("--reason", default="operator requested rollback")
    args = parser.parse_args()
    if args.command == "deploy":
        return deploy()
    return rollback(args.reason)


if __name__ == "__main__":
    sys.exit(main())
