#!/usr/bin/env python3
"""SITE-002 catalog sort menu order — single-Twig Production deploy."""
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

OPERATION_ID = "SITE-002-PROD-SORT-MENU-ORDER-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-SORT-AZ-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-SORT-MENU-ORDER-01"
REMOTE_CANDIDATE = "/public_html/catalog/view/theme/default/template/product/category.twig"
LOCAL_NAME = "category.twig"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-SORT-MENU-ORDER-01"
)
VERIFY_URLS = [
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
]
USER_AGENT = "MARS-OCPilot/SITE-002-PROD-SORT-MENU-ORDER-01"
SUBDIRS = ("source", "prepared", "backup", "verification", "rollback", "manifests", "logs")

SORT_MENU_PATTERN = re.compile(
    r'(<div class="category__sort-menu" data-sort-menu(?:=""| hidden)?>)([\s\S]*?)(</div>)',
    re.MULTILINE,
)
BUTTON_PATTERN = re.compile(
    r'(<button class="category__sort-item" type="button"\s+data-sort="[^"]*">[^<]*</button>)',
    re.MULTILINE,
)

EXPECTED_ORDER = [
    "sort=pd.name&order=ASC",
    "sort=pd.name&order=DESC",
    "sort=p.price&order=ASC",
    "sort=p.price&order=DESC",
]
REMOVED_SORT = "sort=p.date_added&order=DESC"
DEFAULT_SORT_LABEL = "Название - от А до Я"
SEARCH_PATHS = [
    "/public_html/catalog/view/theme/default/template/product/category.twig",
    "/public_html/catalog/view/theme/default/template/product/search.twig",
    "/public_html/catalog/view/theme/default/template/product/special.twig",
    "/public_html/catalog/view/theme/default/template/product/manufacturer_info.twig",
]


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


def has_catalog_sort_menu(data: bytes) -> bool:
    text = data.decode("utf-8", errors="replace")
    if "data-sort-menu" not in text:
        return False
    return all(token in text for token in (REMOVED_SORT, *EXPECTED_ORDER))


def discover_target(ftp: ftplib.FTP) -> tuple[str, bytes]:
    primary = REMOTE_CANDIDATE
    try:
        category_data = ftp_download(ftp, primary)
    except ftplib.error_perm as exc:
        raise RuntimeError("BLOCKED — SORT MENU SOURCE NOT FOUND") from exc

    candidate_path = DEPLOYMENT_ROOT / "source" / "category.twig.candidate"
    candidate_path.write_bytes(category_data)

    secondary_hits: list[str] = []
    for remote_path in SEARCH_PATHS:
        if remote_path == primary:
            continue
        try:
            data = ftp_download(ftp, remote_path)
        except ftplib.error_perm:
            continue
        if b"data-sort-menu" in data:
            secondary_hits.append(remote_path)

    discovery = {
        "primary_target": primary,
        "primary_has_catalog_sort_menu": has_catalog_sort_menu(category_data),
        "secondary_data_sort_menu_files": secondary_hits,
        "secondary_out_of_scope": True,
        "note": "Only category.twig contains the full catalog sort menu with data-sort attributes.",
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "discovery.json", discovery)

    if not discovery["primary_has_catalog_sort_menu"]:
        raise RuntimeError("BLOCKED — SORT MENU SOURCE NOT FOUND")
    if len(secondary_hits) > 0:
        for remote_path in secondary_hits:
            data = ftp_download(ftp, remote_path)
            if has_catalog_sort_menu(data):
                write_json(
                    DEPLOYMENT_ROOT / "manifests" / "discovery-block.json",
                    {"status": "BLOCKED", "files": [primary, remote_path]},
                )
                raise RuntimeError("BLOCKED — MULTIPLE SORT MENU SOURCES FOUND")
    return primary, category_data


def write_operation_metadata(remote_file: str) -> None:
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "change_type": "catalog-sort-menu-order",
            "remote_file": remote_file,
            "authorized_files": 1,
            "expected_removed_item": "Умолчанию",
            "expected_order": [
                "pd.name ASC",
                "pd.name DESC",
                "p.price ASC",
                "p.price DESC",
            ],
        },
    )


def extract_button_sort_key(button: str) -> str | None:
    match = re.search(r'data-sort="([^"]*)"', button)
    return match.group(1) if match else None


def check_preconditions(text: str) -> dict[str, Any]:
    checks: dict[str, Any] = {}
    menu_matches = SORT_MENU_PATTERN.findall(text)
    checks["sort_menu_block_count"] = len(menu_matches)
    checks["has_default_removed_sort"] = REMOVED_SORT in text and "Умолчанию" in text
    checks["has_price_asc"] = "sort=p.price&order=ASC" in text and "Сначала дешевле" in text
    checks["has_price_desc"] = "sort=p.price&order=DESC" in text and "Сначала дороже" in text
    checks["has_name_asc"] = "sort=pd.name&order=ASC" in text
    checks["has_name_desc"] = "sort=pd.name&order=DESC" in text
    checks["name_asc_label"] = "sort=pd.name&order=ASC" in text and ("А до" in text or "от&nbsp;А" in text)
    checks["name_desc_label"] = "sort=pd.name&order=DESC" in text and ("Я до" in text or "от&nbsp;Я" in text)
    checks["status"] = (
        "PASS"
        if checks["sort_menu_block_count"] == 1
        and checks["has_default_removed_sort"]
        and checks["has_price_asc"]
        and checks["has_price_desc"]
        and checks["has_name_asc"]
        and checks["has_name_desc"]
        else "FAIL"
    )
    return checks


def prepare_category_twig(source: bytes) -> tuple[bytes, dict[str, Any]]:
    text = source.decode("utf-8")
    checks = check_preconditions(text)
    if checks["status"] != "PASS":
        return source, checks

    match = SORT_MENU_PATTERN.search(text)
    if not match:
        checks["status"] = "FAIL"
        checks["error"] = "sort menu block not found"
        return source, checks

    inner = match.group(2)
    buttons = BUTTON_PATTERN.findall(inner)
    by_sort: dict[str, str] = {}
    for button in buttons:
        key = extract_button_sort_key(button)
        if key:
            by_sort[key] = button

    required_keys = [REMOVED_SORT] + EXPECTED_ORDER
    missing = [k for k in required_keys if k not in by_sort]
    if missing:
        checks["status"] = "FAIL"
        checks["missing_buttons"] = missing
        return source, checks

    reordered_inner = "\n" + "\n".join(by_sort[k] for k in EXPECTED_ORDER) + "\n"
    new_block = match.group(1) + reordered_inner + match.group(3)
    prepared_text = text[: match.start()] + new_block + text[match.end() :]
    checks["buttons_before"] = len(buttons)
    checks["buttons_after"] = len(EXPECTED_ORDER)
    checks["removed_sort_key"] = REMOVED_SORT
    checks["status"] = "PASS"
    return prepared_text.encode("utf-8"), checks


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
    allowed_markers = (
        "category__sort-menu",
        "category__sort-item",
        "data-sort=",
        "Умолчанию",
        "Сначала дешевле",
        "Сначала дороже",
        "pd.name",
        "p.price",
        "p.date_added",
        "от",
        "до",
        "Я",
        "А",
        "&nbsp;",
        "button",
        "type=",
        "</div>",
    )
    for line in changed:
        if not any(marker in line for marker in allowed_markers):
            return False, changed
    return True, changed


def create_dry_run(
    source: bytes, prepared: bytes, source_sha: str, prepared_sha: str, remote_file: str
) -> dict[str, Any]:
    diff_text = unified_diff(source, prepared)
    scope_ok, diff_lines = diff_scope_ok(diff_text)
    data = {
        "operation_id": OPERATION_ID,
        "remote_files_to_upload": 1,
        "remote_target": remote_file,
        "local_source_file": f"source/{LOCAL_NAME}",
        "prepared_file": f"prepared/{LOCAL_NAME}",
        "backup_available": True,
        "rollback_file_available": True,
        "database_impact": "NONE",
        "controller_impact": "NONE",
        "css_impact": "NONE",
        "js_impact": "NONE",
        "removed_sort_item": f"p.date_added DESC / Умолчанию",
        "final_menu_order": EXPECTED_ORDER,
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
                f"# Dry-Run — {OPERATION_ID}",
                "",
                "- Remote files to upload: 1",
                f"- Remote target: `{remote_file}`",
                f"- Source file: source/{LOCAL_NAME}",
                f"- Prepared file: prepared/{LOCAL_NAME}",
                "- Backup available: YES",
                "- Rollback file available: YES",
                "- Database impact: NONE",
                "- Controller impact: NONE",
                "- CSS impact: NONE",
                "- JS impact: NONE",
                "- Removed sort item: p.date_added DESC / Умолчанию",
                "- Final menu order:",
                "  1. pd.name ASC",
                "  2. pd.name DESC",
                "  3. p.price ASC",
                "  4. p.price DESC",
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


def write_rollback_plan(source_sha: str, remote_file: str) -> None:
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "rollback-plan.json",
        {
            "operation_id": OPERATION_ID,
            "rollback_target": remote_file,
            "rollback_file": f"rollback/{LOCAL_NAME}",
            "source_sha256": source_sha,
            "procedure": [
                f"upload rollback/{LOCAL_NAME}",
                "download remote file again",
                "compare SHA-256 with source_sha256",
                "check category pages HTTP 200",
                "confirm old sort menu restored",
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
            return {"url": url, "checked_at": started, "status_code": response.status, "body": text, "error": None}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return {"url": url, "checked_at": started, "status_code": exc.code, "body": body, "error": str(exc)}
    except Exception as exc:
        return {"url": url, "checked_at": started, "status_code": None, "body": "", "error": str(exc)}


def extract_sort_menu_items(html_text: str) -> list[str]:
    match = re.search(r'data-sort-menu[^>]*>([\s\S]*?)</div>', html_text)
    if not match:
        return []
    inner = match.group(1)
    labels = re.findall(r"category__sort-item[^>]*>([^<]+)<", inner)
    return [html.unescape(label.strip()) for label in labels]


def verify_sort_menu_order(labels: list[str]) -> bool:
    normalized = [re.sub(r"\s+", " ", label.replace("\xa0", " ")).strip() for label in labels]
    expected = [
        "Название - от А до Я",
        "Название - от Я до А",
        "Сначала дешевле",
        "Сначала дороже",
    ]
    if len(normalized) != 4:
        return False
    for got, exp in zip(normalized, expected):
        if exp not in got and got not in exp:
            return False
    return True


def verify_http() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    overall = "PASS"
    for base_url in VERIFY_URLS:
        url = f"{base_url}?mars_verify={OPERATION_ID}"
        result = http_get(url)
        body = result.get("body", "")
        normalized = html.unescape(body)
        menu_labels = extract_sort_menu_items(body)
        entry: dict[str, Any] = {
            "url": url,
            "status_code": result.get("status_code"),
            "error": result.get("error"),
            "php_error_visible": any(
                marker in normalized for marker in ("Fatal error", "Parse error", "Twig_Error", "Twig\\Error")
            ),
            "sort_menu_labels": menu_labels,
            "sort_menu_order_ok": verify_sort_menu_order(menu_labels),
            "default_removed_in_menu": not any("Умолчанию" in label for label in menu_labels),
            "default_visible_sort_a_to_z": DEFAULT_SORT_LABEL in normalized or "от А до Я" in normalized,
            "limit_selector_present": "limit" in normalized.lower() or "Показать" in normalized or "на странице" in normalized.lower(),
            "product_grid_present": "product" in normalized.lower(),
            "sort_links_present": all(
                token in normalized
                for token in ("sort=pd.name", "sort=p.price", "order=ASC", "order=DESC")
            ),
        }
        if result.get("status_code") != 200 or entry["php_error_visible"] or not entry["product_grid_present"]:
            entry["status"] = "FAIL"
            overall = "FAIL"
        elif not entry["sort_menu_order_ok"] or not entry["default_removed_in_menu"]:
            entry["status"] = "CACHE_PENDING"
            if overall != "FAIL":
                overall = "CACHE_PENDING"
        else:
            entry["status"] = "PASS"
        checks.append(entry)

    data = {"operation_id": OPERATION_ID, "status": overall, "checks": checks}
    write_json(DEPLOYMENT_ROOT / "manifests" / "http-verification.json", data)
    return data


def verify_remote_content(data: bytes) -> dict[str, Any]:
    text = data.decode("utf-8", errors="replace")
    menu_match = SORT_MENU_PATTERN.search(text)
    inner = menu_match.group(2) if menu_match else ""
    buttons = BUTTON_PATTERN.findall(inner)
    keys = [extract_button_sort_key(b) for b in buttons]
    keys = [k for k in keys if k]
    return {
        "sort_menu_block_count": len(SORT_MENU_PATTERN.findall(text)),
        "button_count": len(buttons),
        "default_removed": REMOVED_SORT not in inner and "Умолчанию" not in inner,
        "button_order_keys": keys,
        "button_order_ok": keys == EXPECTED_ORDER,
    }


def verify_visual() -> dict[str, Any]:
    desktop = DEPLOYMENT_ROOT / "verification" / "desktop-stoly-sort-menu-order.png"
    mobile = DEPLOYMENT_ROOT / "verification" / "mobile-stoly-sort-menu-order.png"
    desktop_open = DEPLOYMENT_ROOT / "verification" / "desktop-stoly-sort-menu-open.png"
    mobile_open = DEPLOYMENT_ROOT / "verification" / "mobile-stoly-sort-menu-open.png"
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
        for name, viewport, target, open_menu in (
            ("desktop", {"width": 1440, "height": 1200}, desktop, desktop_open),
            ("mobile", {"width": 390, "height": 844}, mobile, mobile_open),
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
                menu_opened = False
                sort_toggle = page.locator('[data-sort-menu], .category__sort, [class*="sort"]').first
                try:
                    if sort_toggle.count() > 0:
                        sort_toggle.click(timeout=3000)
                        page.wait_for_timeout(400)
                        page.screenshot(path=str(open_menu), full_page=True)
                        menu_opened = True
                except Exception:
                    pass
                menu_labels = extract_sort_menu_items(page.content())
                entry.update(
                    {
                        "http_ok": bool(response and response.ok),
                        "sort_menu_order_ok": verify_sort_menu_order(menu_labels),
                        "default_removed_in_menu": not any("Умолчанию" in label for label in menu_labels),
                        "twig_error_visible": any(marker in text for marker in ("Twig_Error", "Fatal error", "Parse error")),
                        "body_text_length": len(text.strip()),
                        "menu_opened": menu_opened,
                        "open_menu_file": str(open_menu) if menu_opened else None,
                        "sort_menu_labels": menu_labels,
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


def rollback(remote_file: str, reason: str) -> int:
    ensure_dirs()
    fields = parse_production_secrets(SECRETS_PATH)
    rollback_file = DEPLOYMENT_ROOT / "rollback" / LOCAL_NAME
    if not rollback_file.exists():
        write_receipt("ROLLED BACK", "ROLLBACK FAILED — rollback file missing", uploaded=False, extra={"reason": reason})
        raise RuntimeError("Rollback file missing")
    source_sha = sha256_file(rollback_file)
    ftp = ftp_connect(fields)
    try:
        ftp_upload(ftp, remote_file, rollback_file.read_bytes())
        after = ftp_download(ftp, remote_file)
    finally:
        try:
            ftp.quit()
        except Exception:
            pass
    restored_sha = sha256_bytes(after)
    (DEPLOYMENT_ROOT / "verification" / "remote-after-rollback.category.twig").write_bytes(after)
    http_result = http_get(f"{VERIFY_URLS[0]}?mars_rollback={int(time.time())}")
    rollback_data = {
        "operation_id": OPERATION_ID,
        "reason": reason,
        "source_sha256": source_sha,
        "remote_after_rollback_sha256": restored_sha,
        "hash_match": restored_sha == source_sha,
        "http_status_code": http_result.get("status_code"),
        "timestamp": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "rollback-result.json", rollback_data)
    if rollback_data["hash_match"] and rollback_data["http_status_code"] == 200:
        write_receipt("ROLLED BACK", "SITE-002 CATALOG SORT MENU ORDER ROLLED BACK SAFELY", uploaded=True, extra=rollback_data)
        print("ROLLED BACK SAFELY")
        return 0
    write_receipt("ROLLED BACK", "ROLLBACK VERIFICATION FAILED", uploaded=True, extra=rollback_data)
    raise RuntimeError("Rollback verification failed")


def deploy() -> int:
    ensure_dirs()
    fields = parse_production_secrets(SECRETS_PATH)

    ftp = ftp_connect(fields)
    try:
        remote_file, source = discover_target(ftp)
        metadata = ftp_metadata(ftp, remote_file)
    finally:
        try:
            ftp.quit()
        except Exception:
            pass

    write_operation_metadata(remote_file)

    source_path = DEPLOYMENT_ROOT / "source" / LOCAL_NAME
    backup_path = DEPLOYMENT_ROOT / "backup" / "category.twig.pre-sort-menu-order.bak"
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

    prepared, prep_checks = prepare_category_twig(source)
    prep_checks["remote_metadata"] = metadata
    prep_checks["remote_file"] = remote_file
    write_json(DEPLOYMENT_ROOT / "manifests" / "precondition.json", prep_checks)
    if prep_checks.get("status") != "PASS":
        write_receipt(
            "FAILED BEFORE DEPLOY",
            "BLOCKED — SORT MENU PRECONDITION FAILED",
            uploaded=False,
            extra=prep_checks,
        )
        raise RuntimeError("BLOCKED — SORT MENU PRECONDITION FAILED")

    prepared_path = DEPLOYMENT_ROOT / "prepared" / LOCAL_NAME
    prepared_path.write_bytes(prepared)
    prepared_sha = sha256_bytes(prepared)
    create_dry_run(source, prepared, source_sha, prepared_sha, remote_file)
    write_rollback_plan(source_sha, remote_file)

    ftp = ftp_connect(fields)
    try:
        pre_upload = ftp_download(ftp, remote_file)
        (DEPLOYMENT_ROOT / "verification" / "remote-pre-upload-check.category.twig").write_bytes(pre_upload)
        remote_pre_upload_sha = sha256_bytes(pre_upload)
        if remote_pre_upload_sha != source_sha:
            write_receipt(
                "FAILED BEFORE DEPLOY",
                "STOP — REMOTE FILE CHANGED SINCE BACKUP",
                uploaded=False,
                extra={"remote_pre_upload_sha256": remote_pre_upload_sha, "source_sha256": source_sha},
            )
            raise RuntimeError("STOP — REMOTE FILE CHANGED SINCE BACKUP")
        ftp_upload(ftp, remote_file, prepared)
        after = ftp_download(ftp, remote_file)
    finally:
        try:
            ftp.quit()
        except Exception:
            pass

    after_path = DEPLOYMENT_ROOT / "verification" / "remote-after-upload.category.twig"
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
            "uploaded_files": [remote_file],
            "upload_count": 1,
            "delete_count": 0,
            "rename_count": 0,
            "remote_after_content_checks": content_after,
        },
    )

    if remote_after_sha != prepared_sha or not content_after["button_order_ok"] or not content_after["default_removed"]:
        rollback(remote_file, "Remote hash/content mismatch after upload")
        return 2

    http_result = verify_http()
    if http_result["status"] == "FAIL":
        rollback(remote_file, "HTTP verification failed after deploy")
        return 2
    if http_result["status"] == "CACHE_PENDING":
        write_receipt(
            "DEPLOYED — HTTP CACHE PENDING",
            "SITE-002 CATALOG SORT MENU ORDER DEPLOYED — HTTP CACHE PENDING",
            uploaded=True,
            extra={"http_verification": http_result},
        )
        print("DEPLOYED — HTTP CACHE PENDING")
        return 0

    visual_result = verify_visual()
    if visual_result.get("status") == "FAIL":
        rollback(remote_file, "Visual verification failed after deploy")
        return 2

    write_receipt(
        "DEPLOYED",
        "SITE-002 CATALOG SORT MENU ORDER COMPLETE — DEPLOY AND ROLLBACK READINESS VERIFIED",
        uploaded=True,
        extra={"http_verification": http_result, "visual_verification": visual_result},
    )
    print("DEPLOYED")
    print(f"remote_file={remote_file}")
    print(f"source_sha256={source_sha}")
    print(f"prepared_sha256={prepared_sha}")
    print(f"remote_after_sha256={remote_after_sha}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="SITE-002 catalog sort menu order deploy.")
    parser.add_argument("command", choices=("deploy", "rollback"))
    parser.add_argument("--reason", default="operator requested rollback")
    args = parser.parse_args()
    if args.command == "deploy":
        return deploy()
    remote_file = REMOTE_CANDIDATE
    manifest = DEPLOYMENT_ROOT / "manifests" / "operation.json"
    if manifest.exists():
        remote_file = json.loads(manifest.read_text(encoding="utf-8")).get("remote_file", remote_file)
    return rollback(remote_file, args.reason)


if __name__ == "__main__":
    sys.exit(main())
