#!/usr/bin/env python3
"""SITE-002 MARS 1C import wrapper TXT reports — download, enhance, deploy, verify."""
from __future__ import annotations

import argparse
import difflib
import ftplib
import hashlib
import io
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-CRON-RUN-REPORTS-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CRON-WRAPPER-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CRON-RUN-REPORTS-01"
)
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

WRAPPER_REMOTE = "/storage/mars-tools/cron/mars_1c_import_wrapper.php"
REPORTS_REMOTE_DIR = "/storage/mars-tools/cron/reports/"
REPORTS_INDEX_REMOTE = "/storage/mars-tools/cron/reports/index.html"

LOCAL_SOURCE = DEPLOYMENT_ROOT / "source" / "mars_1c_import_wrapper.php"
LOCAL_BACKUP = DEPLOYMENT_ROOT / "backup" / "mars_1c_import_wrapper.php.pre-txt-reports.bak"
LOCAL_ROLLBACK = DEPLOYMENT_ROOT / "rollback" / "mars_1c_import_wrapper.php"
LOCAL_PREPARED = DEPLOYMENT_ROOT / "prepared" / "mars_1c_import_wrapper.php"
LOCAL_INDEX = DEPLOYMENT_ROOT / "prepared" / "index.html"

INDEX_HTML = b"<!DOCTYPE html><html><head><title>403</title></head><body></body></html>\n"


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


def normalize_remote(path: str) -> str:
    path = path.strip()
    if not path.startswith("/"):
        path = "/" + path
    return path


def ftp_download(ftp: ftplib.FTP, remote_path: str) -> bytes | None:
    bio = io.BytesIO()
    try:
        ftp.retrbinary("RETR " + normalize_remote(remote_path), bio.write)
        return bio.getvalue()
    except ftplib.error_perm:
        return None


def ftp_mkdirs(ftp: ftplib.FTP, remote_dir: str) -> None:
    parts = [p for p in normalize_remote(remote_dir).split("/") if p]
    current = ""
    for part in parts:
        current += "/" + part
        try:
            ftp.mkd(current)
        except ftplib.error_perm as exc:
            if "550" not in str(exc):
                raise


def ftp_upload(ftp: ftplib.FTP, remote_path: str, data: bytes) -> None:
    remote_path = normalize_remote(remote_path)
    parent = "/".join(remote_path.split("/")[:-1])
    if parent:
        ftp_mkdirs(ftp, parent)
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + remote_path, bio)


def ftp_exists(ftp: ftplib.FTP, remote_path: str) -> bool:
    remote_path = normalize_remote(remote_path)
    try:
        ftp.size(remote_path)
        return True
    except ftplib.error_perm:
        pass
    try:
        ftp.cwd(remote_path)
        ftp.cwd("/")
        return True
    except ftplib.error_perm:
        return False


def list_dir_names(ftp: ftplib.FTP, path: str) -> list[str]:
    names: list[str] = []
    try:
        for name, _facts in ftp.mlsd(normalize_remote(path)):
            if name not in (".", ".."):
                names.append(name)
        return names
    except ftplib.error_perm:
        pass
    lines: list[str] = []
    try:
        ftp.retrlines("LIST " + normalize_remote(path), lines.append)
    except ftplib.error_perm:
        return names
    for line in lines:
        parts = line.split(maxsplit=8)
        if len(parts) >= 9:
            names.append(parts[8])
    return names


def resolve_roots(ftp: ftplib.FTP) -> dict[str, str]:
    pwd = ftp.pwd() or "/"
    login_root = normalize_remote(pwd if pwd.startswith("/") else "/" + pwd)
    public_root = normalize_remote(login_root + "public_html").rstrip("/") + "/"
    storage_root = normalize_remote(login_root + "storage").rstrip("/") + "/"
    try:
        names = {n.lower() for n in list_dir_names(ftp, login_root)}
        if "public_html" in names:
            public_root = normalize_remote(login_root + "public_html").rstrip("/") + "/"
        if "storage" in names:
            storage_root = normalize_remote(login_root + "storage").rstrip("/") + "/"
    except Exception:
        pass
    return {"login_root": login_root, "public_root": public_root, "storage_root": storage_root}


def wrapper_remote(roots: dict[str, str]) -> str:
    return roots["storage_root"] + "mars-tools/cron/mars_1c_import_wrapper.php"


def reports_remote_dir(roots: dict[str, str]) -> str:
    return roots["storage_root"] + "mars-tools/cron/reports/"


def reports_index_remote(roots: dict[str, str]) -> str:
    return roots["storage_root"] + "mars-tools/cron/reports/index.html"


def http_get(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = resp.read(65536)
            return {
                "url": url,
                "status_code": resp.status,
                "body_preview": body[:8000].decode("utf-8", errors="replace"),
                "body_sha256": sha256_bytes(body),
                "timestamp": utc_now(),
            }
    except urllib.error.HTTPError as exc:
        body = exc.read(65536) if exc.fp else b""
        return {
            "url": url,
            "status_code": exc.code,
            "body_preview": body[:8000].decode("utf-8", errors="replace"),
            "body_sha256": sha256_bytes(body) if body else None,
            "timestamp": utc_now(),
        }
    except Exception as exc:
        return {"url": url, "status_code": None, "error": str(exc), "timestamp": utc_now()}


def init_manifests() -> None:
    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "environment": ENVIRONMENT,
        "production_url": PRODUCTION_URL,
        "baseline_before": BASELINE_BEFORE,
        "change_type": "mars-1c-wrapper-txt-reports",
        "legacy_import_policy": "preserve-sergey-version",
        "real_import_execution": "forbidden",
        "db_mutation": "forbidden",
        "beget_cron_activation": "forbidden",
        "authorized_remote_changes": [
            "update existing MARS wrapper only",
            "create reports directory",
            "create reports index guard if needed",
        ],
        "created_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation.json", manifest)


def phase_download(ftp: ftplib.FTP, roots: dict[str, str]) -> dict[str, Any]:
    remote = wrapper_remote(roots)
    data = ftp_download(ftp, remote)
    if data is None:
        return {"status": "failed", "reason": "wrapper not found on production", "remote": remote}

    for path in (LOCAL_SOURCE, LOCAL_BACKUP, LOCAL_ROLLBACK):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    digest = sha256_bytes(data)
    meta = {
        "status": "downloaded",
        "remote": remote,
        "size": len(data),
        "download_timestamp": utc_now(),
        "source_sha256": digest,
        "backup_sha256": digest,
        "rollback_sha256": digest,
        "hashes_match": True,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "file-hashes.json", meta)
    return meta


def phase_dry_run_manifest() -> dict[str, Any]:
    if not LOCAL_SOURCE.exists() or not LOCAL_PREPARED.exists():
        return {"status": "blocked", "reason": "source or prepared missing"}

    source_lines = LOCAL_SOURCE.read_text(encoding="utf-8").splitlines(keepends=True)
    prepared_lines = LOCAL_PREPARED.read_text(encoding="utf-8").splitlines(keepends=True)
    diff = list(
        difflib.unified_diff(source_lines, prepared_lines, fromfile="source", tofile="prepared", lineterm="")
    )
    diff_text = "\n".join(diff)
    write_text(DEPLOYMENT_ROOT / "manifests" / "wrapper.diff", diff_text)

    source_text = LOCAL_SOURCE.read_text(encoding="utf-8")
    prepared_text = LOCAL_PREPARED.read_text(encoding="utf-8")
    forbidden_new_patterns = [
        r"ftp.*password\s*=",
        r"run_token\s*=\s*['\"][^'\"]{8,}['\"]",
        r"password\s*=\s*['\"][^'\"]+['\"]",
    ]
    violations = [
        p
        for p in forbidden_new_patterns
        if re.search(p, prepared_text, re.I) and not re.search(p, source_text, re.I)
    ]
    added_lines = [line for line in diff if line.startswith("+") and not line.startswith("+++")]
    legacy_flow_markers = ["import_1C.php", "cronjob.php"]
    if any("mars_mode_run" in line and "mutation" in line for line in added_lines):
        pass  # run mode instrumentation allowed
    if any(re.search(r"unlink\s*\(.*legacy", line, re.I) for line in added_lines):
        violations.append("legacy file deletion in diff")

    dry_run = {
        "remote_files_to_upload": 1,
        "remote_index_guard": "optional",
        "remote_legacy_edits": 0,
        "database_impact": "NONE",
        "import_execution": "NONE",
        "beget_cron_impact": "NONE",
        "reports_directory": REPORTS_REMOTE_DIR,
        "txt_report_creation": "dry-run/status/run hooks",
        "diff_line_count": len(diff),
        "scope_violations": violations,
        "prepared_sha256": sha256_file(LOCAL_PREPARED),
        "source_sha256": sha256_file(LOCAL_SOURCE),
        "timestamp": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", dry_run)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "\n".join(
            [
                "# Dry-run manifest",
                "",
                f"- Remote uploads: **{dry_run['remote_files_to_upload']}** wrapper (+ optional index guard)",
                "- Remote legacy edits: **0**",
                "- Database impact: **NONE**",
                "- Import execution: **NONE**",
                f"- Scope violations: **{len(violations)}**",
                "",
            ]
        ),
    )
    return dry_run


def phase_pre_upload_check(ftp: ftplib.FTP, roots: dict[str, str], source_sha256: str) -> dict[str, Any]:
    remote = wrapper_remote(roots)
    data = ftp_download(ftp, remote)
    check_path = DEPLOYMENT_ROOT / "verification" / "remote-pre-upload-check.mars_1c_import_wrapper.php"
    if data is None:
        return {"status": "failed", "reason": "remote wrapper missing"}
    check_path.write_bytes(data)
    remote_sha = sha256_bytes(data)
    result = {
        "remote_pre_upload_sha256": remote_sha,
        "source_sha256": source_sha256,
        "match": remote_sha == source_sha256,
        "timestamp": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "pre-upload-check.json", result)
    return result


def phase_deploy(ftp: ftplib.FTP, roots: dict[str, str]) -> dict[str, Any]:
    if not LOCAL_PREPARED.exists():
        return {"status": "failed", "reason": "prepared wrapper missing"}

    prepared_data = LOCAL_PREPARED.read_bytes()
    prepared_sha = sha256_bytes(prepared_data)
    remote_wrapper = wrapper_remote(roots)
    remote_reports = reports_remote_dir(roots)
    remote_index = reports_index_remote(roots)

    ftp_mkdirs(ftp, remote_reports)
    ftp_upload(ftp, remote_wrapper, prepared_data)

    index_uploaded = False
    if not ftp_exists(ftp, remote_index):
        ftp_upload(ftp, remote_index, INDEX_HTML)
        index_uploaded = True

    after_data = ftp_download(ftp, remote_wrapper)
    after_path = DEPLOYMENT_ROOT / "verification" / "remote-after-upload.mars_1c_import_wrapper.php"
    if after_data:
        after_path.write_bytes(after_data)

    after_sha = sha256_bytes(after_data) if after_data else None
    deploy = {
        "status": "uploaded" if after_sha == prepared_sha else "hash_mismatch",
        "remote_wrapper": remote_wrapper,
        "remote_reports_dir": remote_reports,
        "index_guard_uploaded": index_uploaded,
        "prepared_sha256": prepared_sha,
        "remote_after_sha256": after_sha,
        "hash_match": after_sha == prepared_sha,
        "timestamp": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "deploy-manifest.json", deploy)
    return deploy


def phase_rollback(ftp: ftplib.FTP, roots: dict[str, str]) -> dict[str, Any]:
    if not LOCAL_ROLLBACK.exists():
        return {"status": "failed", "reason": "rollback file missing"}
    data = LOCAL_ROLLBACK.read_bytes()
    remote = wrapper_remote(roots)
    ftp_upload(ftp, remote, data)
    after = ftp_download(ftp, remote)
    result = {
        "status": "rolled_back" if after == data else "rollback_hash_mismatch",
        "remote": remote,
        "rollback_sha256": sha256_bytes(data),
        "remote_after_sha256": sha256_bytes(after) if after else None,
        "timestamp": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "rollback-result.json", result)
    return result


def phase_verify_http() -> dict[str, Any]:
    base = PRODUCTION_URL.rstrip("/") + "/mars-tools/cron/mars_1c_http_gateway.php"
    checks = {
        "dry_run": http_get(base + "?mode=dry-run"),
        "status": http_get(base + "?mode=status"),
        "run_without_token": http_get(base + "?mode=run"),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "runtime-verification.json", checks)
    return checks


def phase_verify_reports(ftp: ftplib.FTP, roots: dict[str, str]) -> dict[str, Any]:
    reports_dir = reports_remote_dir(roots)
    names = list_dir_names(ftp, reports_dir)
    txt_files = sorted([n for n in names if n.endswith(".txt")], reverse=True)
    report_meta: dict[str, Any] = {
        "reports_dir": reports_dir,
        "directory_exists": ftp_exists(ftp, reports_dir),
        "txt_file_count": len(txt_files),
        "txt_files": txt_files[:10],
        "latest_report": None,
        "contains_secrets": False,
        "contains_expected_headings": False,
        "timestamp": utc_now(),
    }

    if txt_files:
        latest_remote = reports_dir.rstrip("/") + "/" + txt_files[0]
        content_bytes = ftp_download(ftp, latest_remote)
        if content_bytes:
            content = content_bytes.decode("utf-8", errors="replace")
            local_report = DEPLOYMENT_ROOT / "verification" / txt_files[0]
            local_report.write_bytes(content_bytes)
            secret_markers = ["password", "DB_PASSWORD", "DB_USERNAME", "run_token=", "token="]
            report_meta["latest_report"] = {
                "filename": txt_files[0],
                "remote": latest_remote,
                "size": len(content_bytes),
                "sha256": sha256_bytes(content_bytes),
            }
            lower = content.lower()
            report_meta["contains_secrets"] = any(m.lower() in lower for m in secret_markers if m != "token=")
            if "token=" in lower and "run_token_configured" not in lower:
                report_meta["contains_secrets"] = True
            expected = [
                "SITE-002 MARS 1C IMPORT REPORT",
                "Run ID:",
                "Mode:",
                "Final status:",
            ]
            report_meta["contains_expected_headings"] = all(h in content for h in expected)

    write_json(DEPLOYMENT_ROOT / "manifests" / "report-verification.json", report_meta)
    return report_meta


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument(
        "--phase",
        choices=[
            "init",
            "download",
            "dry-run",
            "pre-upload-check",
            "deploy",
            "verify-http",
            "verify-reports",
            "rollback",
            "all",
        ],
        default="all",
    )
    args = parser.parse_args()

    init_manifests()

    if args.phase == "init":
        print("Operation tree initialized.")
        return 0

    if not SECRETS_PATH.exists():
        print("STOP — secrets file missing")
        return 1

    if args.phase in ("dry-run",) and not LOCAL_PREPARED.exists():
        print("STOP — prepared wrapper missing; run local preparation first")
        return 1

    fields = parse_production_secrets(SECRETS_PATH)
    ftp = ftp_connect(fields)
    roots = resolve_roots(ftp)
    write_json(DEPLOYMENT_ROOT / "manifests" / "ftp-roots.json", roots)

    summary: dict[str, Any] = {"timestamp": utc_now()}

    if args.phase in ("download", "all"):
        dl = phase_download(ftp, roots)
        summary["download"] = dl
        if dl.get("status") != "downloaded":
            ftp.quit()
            print(json.dumps(summary, ensure_ascii=False, indent=2))
            return 1

    if args.phase in ("dry-run", "all"):
        dr = phase_dry_run_manifest()
        summary["dry_run"] = dr
        if dr.get("scope_violations"):
            ftp.quit()
            print("STOP — DRY-RUN SCOPE VIOLATION")
            print(json.dumps(summary, ensure_ascii=False, indent=2))
            return 1

    source_sha = sha256_file(LOCAL_SOURCE) if LOCAL_SOURCE.exists() else ""

    if args.phase in ("pre-upload-check", "all"):
        if not source_sha:
            ftp.quit()
            print("STOP — source missing for pre-upload check")
            return 1
        pre = phase_pre_upload_check(ftp, roots, source_sha)
        summary["pre_upload_check"] = pre
        if not pre.get("match"):
            ftp.quit()
            print("STOP — REMOTE WRAPPER CHANGED SINCE BACKUP")
            print(json.dumps(summary, ensure_ascii=False, indent=2))
            return 1

    if args.phase in ("deploy", "all"):
        if not LOCAL_PREPARED.exists():
            ftp.quit()
            print("STOP — prepared wrapper missing")
            return 1
        deploy = phase_deploy(ftp, roots)
        summary["deploy"] = deploy
        if not deploy.get("hash_match"):
            ftp.quit()
            print("STOP — post-upload hash mismatch")
            return 1

    if args.phase in ("verify-reports", "all"):
        summary["report_verification"] = phase_verify_reports(ftp, roots)

    ftp.quit()

    if args.phase in ("verify-http", "all"):
        summary["http_verification"] = phase_verify_http()

    rollback_plan = {
        "rollback_file": str(LOCAL_ROLLBACK),
        "rollback_sha256": sha256_file(LOCAL_ROLLBACK) if LOCAL_ROLLBACK.exists() else None,
        "remote_target": WRAPPER_REMOTE,
        "command": f"python {__file__} --phase rollback",
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "rollback-plan.json", rollback_plan)

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
