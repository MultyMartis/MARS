#!/usr/bin/env python3
"""SITE-002 exact single-file Production text deploy utility.

This tool is intentionally site- and operation-specific:
- reads only the PRODUCTION FTP section from external secrets;
- supports only one authorized remote file;
- creates backup, dry-run, rollback, deploy, HTTP, and visual evidence;
- has no delete or rename functions.
"""
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

OPERATION_ID = "SITE-002-PROD-TEXT-CHANGE-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
GUARANTEE_URL = "https://bzpm.ru/guarantee"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-INITIAL-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-TEXT-CHANGE-01"
REMOTE_FILE = "/public_html/catalog/view/theme/default/template/information/guarantee.twig"
OLD_TEXT = "понятный порядок действий"
NEW_TEXT = "чёткий порядок действий"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-TEXT-CHANGE-01"
)

USER_AGENT = "MARS-OCPilot/SITE-002-PROD-TEXT-CHANGE-01"
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


def count_bytes(data: bytes, text: str) -> int:
    return data.count(text.encode("utf-8"))


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
    metadata: dict[str, Any] = {
        "ftp_visible_path": remote_path,
        "download_timestamp": utc_now(),
    }
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
            "change_type": "single-text-replacement",
            "old_text": OLD_TEXT,
            "new_text": NEW_TEXT,
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
            fromfile="source/guarantee.twig",
            tofile="prepared/guarantee.twig",
            lineterm="",
        )
    )


def create_dry_run(source: bytes, prepared: bytes, source_sha: str, prepared_sha: str) -> dict[str, Any]:
    diff_text = unified_diff(source, prepared)
    diff_lines = [line for line in diff_text.splitlines() if line.startswith(("+", "-")) and not line.startswith(("+++", "---"))]
    scope_ok = len(diff_lines) == 2 and OLD_TEXT in diff_lines[0] and NEW_TEXT in diff_lines[1]
    data = {
        "operation_id": OPERATION_ID,
        "remote_files_to_upload": 1,
        "remote_files_to_delete": 0,
        "remote_files_to_rename": 0,
        "local_source_file": "source/guarantee.twig",
        "prepared_file": "prepared/guarantee.twig",
        "remote_target": REMOTE_FILE,
        "replacement_count": 1,
        "backup_available": True,
        "rollback_file_available": True,
        "database_impact": "NONE",
        "css_js_impact": "NONE",
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
                "# Dry-Run — SITE-002-PROD-TEXT-CHANGE-01",
                "",
                "- Remote files to upload: 1",
                "- Remote files to delete: 0",
                "- Remote files to rename: 0",
                "- Local source file: source/guarantee.twig",
                "- Prepared file: prepared/guarantee.twig",
                f"- Remote target: `{REMOTE_FILE}`",
                "- Replacement count: 1",
                "- Backup available: YES",
                "- Rollback file available: YES",
                "- Database impact: NONE",
                "- CSS/JS impact: NONE",
                "",
                "```diff",
                diff_text,
                "```",
                "",
            ]
        ),
    )
    write_text(DEPLOYMENT_ROOT / "manifests" / "guarantee.diff", diff_text)
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
            "rollback_file": "rollback/guarantee.twig",
            "source_sha256": source_sha,
            "procedure": [
                "upload rollback/guarantee.twig",
                "download remote file again",
                "compare SHA-256 with source_sha256",
                "check page",
                "confirm original text",
            ],
        },
    )
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "rollback-plan.md",
        "\n".join(
            [
                "# Rollback Plan — SITE-002-PROD-TEXT-CHANGE-01",
                "",
                f"Rollback target: `{REMOTE_FILE}`",
                "",
                "1. Upload `rollback/guarantee.twig`.",
                "2. Download the remote file again.",
                "3. Compare SHA-256 with `source_sha256`.",
                "4. Check `https://bzpm.ru/guarantee`.",
                "5. Confirm the original text is present.",
                "",
            ]
        ),
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
                "headers": dict(response.headers.items()),
                "body": text,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return {
            "url": url,
            "checked_at": started,
            "status_code": exc.code,
            "headers": dict(exc.headers.items()),
            "body": body,
            "error": str(exc),
        }
    except Exception as exc:
        return {
            "url": url,
            "checked_at": started,
            "status_code": None,
            "headers": {},
            "body": "",
            "error": str(exc),
        }


def verify_http() -> dict[str, Any]:
    results = []
    for idx, url in enumerate(
        [
            GUARANTEE_URL,
            f"{GUARANTEE_URL}?ocpilot_cache_bust={int(time.time())}",
            f"{GUARANTEE_URL}?ocpilot_cache_bust={int(time.time()) + 1}",
        ],
    ):
        result = http_get(url)
        normalized = html.unescape(re.sub(r"\s+", " ", result["body"]))
        result["new_text_count"] = normalized.count(NEW_TEXT)
        result["old_text_count"] = normalized.count(OLD_TEXT)
        result["body_size"] = len(result["body"])
        result.pop("body", None)
        results.append(result)
        if result["status_code"] == 200 and result["new_text_count"] >= 1 and result["old_text_count"] == 0:
            break
        if idx < 2:
            time.sleep(1)

    final = results[-1]
    status = "PASS"
    if final["status_code"] != 200:
        status = "FAIL"
    elif final["new_text_count"] < 1 or final["old_text_count"] != 0:
        status = "CACHE_PENDING"

    data = {
        "operation_id": OPERATION_ID,
        "status": status,
        "checks": results,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "http-verification.json", data)
    return data


def verify_visual() -> dict[str, Any]:
    desktop = DEPLOYMENT_ROOT / "verification" / "desktop-guarantee.png"
    mobile = DEPLOYMENT_ROOT / "verification" / "mobile-guarantee.png"
    results: list[dict[str, Any]] = []
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        data = {"operation_id": OPERATION_ID, "status": "FAIL", "error": f"playwright import failed: {exc}", "results": results}
        write_json(DEPLOYMENT_ROOT / "manifests" / "visual-verification.json", data)
        return data

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for name, viewport, target in (
            ("desktop", {"width": 1440, "height": 1200}, desktop),
            ("mobile", {"width": 390, "height": 844}, mobile),
        ):
            entry: dict[str, Any] = {"viewport": name, "url": GUARANTEE_URL, "file": str(target), "status": "FAIL"}
            context = browser.new_context(viewport=viewport, user_agent=USER_AGENT)
            page = context.new_page()
            try:
                response = page.goto(GUARANTEE_URL, wait_until="networkidle", timeout=60000)
                page.wait_for_timeout(800)
                text = page.locator("body").inner_text(timeout=10000)
                target.parent.mkdir(parents=True, exist_ok=True)
                page.screenshot(path=str(target), full_page=True)
                entry.update(
                    {
                        "http_ok": bool(response and response.ok),
                        "new_text_present": NEW_TEXT in text,
                        "old_text_present": OLD_TEXT in text,
                        "twig_error_visible": any(marker in text for marker in ("Twig_Error", "Twig\\Error", "Fatal error", "Parse error")),
                        "body_text_length": len(text.strip()),
                    }
                )
                entry["status"] = (
                    "PASS"
                    if entry["http_ok"]
                    and entry["new_text_present"]
                    and not entry["old_text_present"]
                    and not entry["twig_error_visible"]
                    and entry["body_text_length"] > 100
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


def rollback(reason: str) -> int:
    ensure_dirs()
    fields = parse_production_secrets(SECRETS_PATH)
    rollback_file = DEPLOYMENT_ROOT / "rollback" / "guarantee.twig"
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
    (DEPLOYMENT_ROOT / "verification" / "remote-after-rollback.twig").write_bytes(after)
    http_result = http_get(f"{GUARANTEE_URL}?ocpilot_rollback_check={int(time.time())}")
    normalized = html.unescape(re.sub(r"\s+", " ", http_result.get("body", "")))
    rollback_data = {
        "operation_id": OPERATION_ID,
        "reason": reason,
        "rollback_target": REMOTE_FILE,
        "source_sha256": source_sha,
        "remote_after_rollback_sha256": restored_sha,
        "hash_match": restored_sha == source_sha,
        "http_status_code": http_result.get("status_code"),
        "old_text_present": OLD_TEXT in normalized,
        "new_text_present": NEW_TEXT in normalized,
        "timestamp": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "rollback-result.json", rollback_data)
    if rollback_data["hash_match"] and rollback_data["http_status_code"] == 200 and rollback_data["old_text_present"]:
        write_receipt("ROLLED BACK", "SITE-002 PRODUCTION CHANGE ROLLED BACK SAFELY", uploaded=True, extra=rollback_data)
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

    source_path = DEPLOYMENT_ROOT / "source" / "guarantee.twig"
    backup_path = DEPLOYMENT_ROOT / "backup" / "guarantee.twig.pre-change.bak"
    rollback_path = DEPLOYMENT_ROOT / "rollback" / "guarantee.twig"
    source_path.write_bytes(source)
    backup_path.write_bytes(source)
    rollback_path.write_bytes(source)
    source_sha = sha256_bytes(source)
    backup_sha = sha256_file(backup_path)
    rollback_sha = sha256_file(rollback_path)
    if source_sha != backup_sha:
        write_receipt("FAILED BEFORE DEPLOY", "SOURCE/BACKUP SHA MISMATCH", uploaded=False)
        raise RuntimeError("source_sha256 != backup_sha256")
    if rollback_sha != source_sha:
        write_receipt("FAILED BEFORE DEPLOY", "ROLLBACK/SOURCE SHA MISMATCH", uploaded=False)
        raise RuntimeError("rollback_sha256 != source_sha256")

    old_count = count_bytes(source, OLD_TEXT)
    new_count_before = count_bytes(source, NEW_TEXT)
    precondition = {
        "operation_id": OPERATION_ID,
        "remote_file": REMOTE_FILE,
        "old_text": OLD_TEXT,
        "new_text": NEW_TEXT,
        "match_count": old_count,
        "new_text_count_before": new_count_before,
        "status": "PASS" if old_count == 1 else "FAIL",
        "remote_metadata": metadata,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "precondition.json", precondition)
    if old_count != 1:
        write_receipt("FAILED BEFORE DEPLOY", "STOP — TARGET TEXT PRECONDITION FAILED", uploaded=False, extra=precondition)
        raise RuntimeError("STOP — TARGET TEXT PRECONDITION FAILED")

    prepared = source.replace(OLD_TEXT.encode("utf-8"), NEW_TEXT.encode("utf-8"), 1)
    replacement_count = count_bytes(prepared, NEW_TEXT) - count_bytes(source, NEW_TEXT)
    if replacement_count != 1 or count_bytes(prepared, OLD_TEXT) != 0:
        write_receipt("FAILED BEFORE DEPLOY", "LOCAL REPLACEMENT FAILED", uploaded=False)
        raise RuntimeError("Local replacement failed")
    prepared_path = DEPLOYMENT_ROOT / "prepared" / "guarantee.twig"
    prepared_path.write_bytes(prepared)
    prepared_sha = sha256_bytes(prepared)

    create_dry_run(source, prepared, source_sha, prepared_sha)
    write_rollback_plan(source_sha)

    ftp = ftp_connect(fields)
    try:
        pre_upload = ftp_download(ftp, REMOTE_FILE)
        (DEPLOYMENT_ROOT / "verification" / "remote-pre-upload-check.twig").write_bytes(pre_upload)
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

    after_path = DEPLOYMENT_ROOT / "verification" / "remote-after-upload.twig"
    after_path.write_bytes(after)
    remote_after_sha = sha256_bytes(after)
    old_after = count_bytes(after, OLD_TEXT)
    new_after = count_bytes(after, NEW_TEXT)

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
    deploy_manifest = {
        "operation_id": OPERATION_ID,
        "uploaded_files": [REMOTE_FILE],
        "upload_count": 1,
        "delete_count": 0,
        "rename_count": 0,
        "source_sha256": source_sha,
        "prepared_sha256": prepared_sha,
        "remote_after_sha256": remote_after_sha,
        "rollback_sha256": rollback_sha,
        "replacement_count": 1,
        "old_text_count_after_upload": old_after,
        "new_text_count_after_upload": new_after,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "deploy-manifest.json", deploy_manifest)

    if remote_after_sha != prepared_sha or old_after != 0 or new_after != 1:
        rollback("Remote hash/content mismatch after upload")
        return 2

    http_result = verify_http()
    if any(check.get("status_code") and int(check["status_code"]) >= 500 for check in http_result["checks"]):
        rollback("HTTP 5xx after deploy")
        return 2
    if http_result["status"] == "FAIL":
        rollback("HTTP verification failed after deploy")
        return 2
    if http_result["status"] == "CACHE_PENDING":
        write_receipt("DEPLOYED — HTTP CACHE PENDING", "SITE-002 PRODUCTION CHANGE DEPLOYED — HTTP CACHE PENDING", uploaded=True)
        print("DEPLOYED — HTTP CACHE PENDING")
        return 0

    visual_result = verify_visual()
    if visual_result["status"] != "PASS":
        rollback("Visual verification failed after deploy")
        return 2

    write_receipt(
        "DEPLOYED",
        "SITE-002 FIRST CONTROLLED PRODUCTION CHANGE COMPLETE — DEPLOY AND ROLLBACK READINESS VERIFIED",
        uploaded=True,
    )
    print("DEPLOYED")
    print(f"source_sha256={source_sha}")
    print(f"prepared_sha256={prepared_sha}")
    print(f"remote_after_sha256={remote_after_sha}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="SITE-002 exact Production text deploy.")
    parser.add_argument("command", choices=("deploy", "rollback"))
    parser.add_argument("--reason", default="operator requested rollback")
    args = parser.parse_args()
    if args.command == "deploy":
        return deploy()
    if args.command == "rollback":
        return rollback(args.reason)
    return 1


if __name__ == "__main__":
    sys.exit(main())
