#!/usr/bin/env python3
"""SITE-002 MARS 1C cron reports cleanup — exact redundant TXT removal only."""
from __future__ import annotations

import argparse
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

OPERATION_ID = "SITE-002-PROD-CRON-REPORTS-CLEANUP-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CRON-BEGET-ACTIVE-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CRON-REPORTS-CLEANUP-01"
)
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

KEEP_FILES = frozenset(
    {
        "index.html",
        "mars_1c_import_2026-07-05_205934.txt",
        "mars_1c_import_status_2026-07-05_212740.txt",
    }
)

DELETE_CANDIDATES = frozenset(
    {
        "mars_1c_import_dry_run_2026-07-05_203642.txt",
        "mars_1c_import_dry_run_2026-07-05_205005.txt",
        "mars_1c_import_dry_run_2026-07-05_205007.txt",
        "mars_1c_import_dry_run_2026-07-05_205117.txt",
        "mars_1c_import_dry_run_2026-07-05_205118.txt",
        "mars_1c_import_dry_run_2026-07-05_205915.txt",
        "mars_1c_import_dry_run_2026-07-05_210515.txt",
        "mars_1c_import_dry_run_2026-07-05_210556.txt",
        "mars_1c_import_dry_run_2026-07-05_212703.txt",
        "mars_1c_import_dry_run_2026-07-05_212704.txt",
        "mars_1c_import_dry_run_2026-07-05_212739.txt",
        "mars_1c_import_status_2026-07-05_203642.txt",
        "mars_1c_import_status_2026-07-05_205005.txt",
        "mars_1c_import_status_2026-07-05_205117.txt",
        "mars_1c_import_status_2026-07-05_205915.txt",
        "mars_1c_import_status_2026-07-05_210515.txt",
        "mars_1c_import_status_2026-07-05_210557.txt",
        "mars_1c_import_status_2026-07-05_212704.txt",
        "mars_1c_import_status_2026-07-05_212705.txt",
    }
)

SUBDIRS = ("source-listing", "backup-deleted-reports", "verification", "manifests")


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


def list_dir_names(ftp: ftplib.FTP, path: str) -> list[str]:
    names: list[str] = []
    try:
        for name, _facts in ftp.mlsd(normalize_remote(path)):
            if name not in (".", ".."):
                names.append(name)
        return sorted(names)
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
    return sorted(names)


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


def reports_remote_dir(roots: dict[str, str]) -> str:
    return roots["storage_root"] + "mars-tools/cron/reports/"


def ftp_download(ftp: ftplib.FTP, remote_path: str) -> bytes | None:
    bio = io.BytesIO()
    try:
        ftp.retrbinary("RETR " + normalize_remote(remote_path), bio.write)
        return bio.getvalue()
    except ftplib.error_perm:
        return None


def ftp_delete(ftp: ftplib.FTP, remote_path: str) -> None:
    ftp.delete(normalize_remote(remote_path))


def http_get(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = resp.read(65536)
            return {
                "url": url,
                "status_code": resp.status,
                "body_preview_len": len(body),
                "timestamp": utc_now(),
            }
    except urllib.error.HTTPError as exc:
        return {"url": url, "status_code": exc.code, "timestamp": utc_now()}
    except Exception as exc:
        return {"url": url, "status_code": None, "error": str(exc), "timestamp": utc_now()}


def init_operation() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "environment": ENVIRONMENT,
        "production_url": PRODUCTION_URL,
        "baseline_before": BASELINE_BEFORE,
        "change_type": "reports-cleanup",
        "reports_path": "/storage/mars-tools/cron/reports/",
        "delete_scope": "exact redundant TXT files for 2026-07-05",
        "import_execution_allowed": False,
        "cron_change_allowed": False,
        "created_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation.json", manifest)


def phase_list(ftp: ftplib.FTP, roots: dict[str, str], label: str) -> dict[str, Any]:
    reports_dir = reports_remote_dir(roots)
    names = list_dir_names(ftp, reports_dir)
    listing = {
        "operation_id": OPERATION_ID,
        "reports_dir": reports_dir,
        "reports_dir_canonical": "/storage/mars-tools/cron/reports/",
        "file_count": len(names),
        "files": names,
        "timestamp": utc_now(),
    }
    sub = "source-listing" if label == "before" else "verification"
    write_json(DEPLOYMENT_ROOT / sub / f"reports-{label}.json", listing)
    write_text(
        DEPLOYMENT_ROOT / sub / f"reports-{label}.txt",
        "\n".join(names) + ("\n" if names else ""),
    )
    return listing


def classify(listing: dict[str, Any]) -> dict[str, Any]:
    remote_files = set(listing["files"])
    missing_keep = sorted(KEEP_FILES - remote_files)
    keep_present = sorted(KEEP_FILES & remote_files)
    delete_intersection = sorted(DELETE_CANDIDATES & remote_files)
    delete_not_remote = sorted(DELETE_CANDIDATES - remote_files)
    other_dates = sorted(
        f
        for f in remote_files
        if f not in KEEP_FILES
        and f not in DELETE_CANDIDATES
        and f.endswith(".txt")
    )
    other_non_txt = sorted(f for f in remote_files if f not in KEEP_FILES and not f.endswith(".txt"))
    redundant_20260705 = sorted(
        f
        for f in remote_files
        if f.endswith(".txt")
        and "2026-07-05" in f
        and f not in KEEP_FILES
        and f not in DELETE_CANDIDATES
    )
    return {
        "missing_keep": missing_keep,
        "keep_present": keep_present,
        "delete_intersection": delete_intersection,
        "delete_not_remote": delete_not_remote,
        "other_dates": other_dates,
        "other_non_txt": other_non_txt,
        "redundant_20260705_unlisted": redundant_20260705,
        "blocked": bool(missing_keep),
    }


def phase_backup(ftp: ftplib.FTP, roots: dict[str, str], filenames: list[str]) -> dict[str, Any]:
    reports_dir = reports_remote_dir(roots)
    backup_dir = DEPLOYMENT_ROOT / "backup-deleted-reports"
    hashes: dict[str, Any] = {}
    failures: list[str] = []
    for name in filenames:
        remote = reports_dir.rstrip("/") + "/" + name
        data = ftp_download(ftp, remote)
        if data is None:
            failures.append(name)
            continue
        local = backup_dir / name
        local.write_bytes(data)
        hashes[name] = {
            "remote": remote,
            "local": str(local),
            "size": len(data),
            "sha256": sha256_bytes(data),
        }
    result = {
        "backed_up_count": len(hashes),
        "failures": failures,
        "hashes": hashes,
        "timestamp": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "delete-candidates.json", {"candidates": filenames, "remote_present": list(hashes.keys())})
    write_json(DEPLOYMENT_ROOT / "manifests" / "delete-backup-hashes.json", result)
    return result


def phase_delete_plan(roots: dict[str, str], filenames: list[str]) -> dict[str, Any]:
    reports_dir = reports_remote_dir(roots)
    paths = [reports_dir.rstrip("/") + "/" + name for name in filenames]
    for path in paths:
        basename = path.rsplit("/", 1)[-1]
        if basename in KEEP_FILES:
            raise RuntimeError("STOP — DELETE PLAN INCLUDES KEEP FILE: " + basename)
        if basename not in DELETE_CANDIDATES:
            raise RuntimeError("STOP — DELETE PLAN INCLUDES NON-CANDIDATE: " + basename)
        allowed_prefixes = (
            "/storage/mars-tools/cron/reports/mars_1c_import_dry_run_2026-07-05_",
            "/storage/mars-tools/cron/reports/mars_1c_import_status_2026-07-05_",
        )
        canonical = "/storage/mars-tools/cron/reports/" + basename
        if not any(canonical.startswith(p) for p in allowed_prefixes):
            raise RuntimeError("STOP — DELETE PATH OUT OF SCOPE: " + canonical)
        if canonical == "/storage/mars-tools/cron/reports/mars_1c_import_status_2026-07-05_212740.txt":
            raise RuntimeError("STOP — DELETE PLAN INCLUDES KEEP STATUS FILE")

    plan = {
        "operation_id": OPERATION_ID,
        "delete_count": len(paths),
        "remote_paths": paths,
        "filenames": filenames,
        "timestamp": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "delete-plan.json", plan)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "delete-plan.txt",
        "\n".join(paths) + ("\n" if paths else ""),
    )
    return plan


def phase_delete(ftp: ftplib.FTP, plan: dict[str, Any]) -> dict[str, Any]:
    deleted: list[str] = []
    failed: list[dict[str, str]] = []
    for path in plan["remote_paths"]:
        try:
            ftp_delete(ftp, path)
            deleted.append(path)
        except Exception as exc:
            failed.append({"path": path, "error": str(exc)})
            break
    result = {
        "deleted_count": len(deleted),
        "deleted_paths": deleted,
        "failed": failed,
        "partial": bool(failed),
        "timestamp": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "delete-execution.json", result)
    return result


def phase_http_health() -> dict[str, Any]:
    checks = {
        "home": http_get(PRODUCTION_URL),
        "catalog_stoly": http_get(PRODUCTION_URL.rstrip("/") + "/katalog/nejtralnoe-oborudovanie/stoly"),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "http-health.json", checks)
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument(
        "--phase",
        choices=["init", "list-before", "backup", "plan", "delete", "list-after", "http-health", "all"],
        default="all",
    )
    args = parser.parse_args()

    init_operation()

    if args.phase == "init":
        print("Operation tree initialized.")
        return 0

    if not SECRETS_PATH.exists():
        print("STOP — secrets file missing")
        return 1

    fields = parse_production_secrets(SECRETS_PATH)
    ftp = ftp_connect(fields)
    roots = resolve_roots(ftp)
    write_json(DEPLOYMENT_ROOT / "manifests" / "ftp-roots.json", roots)

    summary: dict[str, Any] = {"operation_id": OPERATION_ID, "timestamp": utc_now()}

    if args.phase in ("list-before", "all"):
        listing = phase_list(ftp, roots, "before")
        classification = classify(listing)
        write_json(DEPLOYMENT_ROOT / "manifests" / "classification-before.json", classification)
        summary["listing_before"] = listing
        summary["classification"] = classification
        if classification["blocked"]:
            ftp.quit()
            print("STOP — KEEP FILE MISSING ON REMOTE")
            print(json.dumps(summary, ensure_ascii=False, indent=2))
            return 1

    classification_path = DEPLOYMENT_ROOT / "manifests" / "classification-before.json"
    if classification_path.exists():
        classification = json.loads(classification_path.read_text(encoding="utf-8"))
    else:
        classification = classify(phase_list(ftp, roots, "before"))

    delete_files = classification["delete_intersection"]

    if args.phase in ("backup", "all"):
        backup = phase_backup(ftp, roots, delete_files)
        summary["backup"] = backup
        if backup["failures"]:
            ftp.quit()
            print("STOP BEFORE DELETE — BACKUP FAILED")
            print(json.dumps(summary, ensure_ascii=False, indent=2))
            return 1

    if args.phase in ("plan", "all"):
        plan = phase_delete_plan(roots, delete_files)
        summary["delete_plan"] = plan

    if args.phase in ("delete", "all"):
        plan_path = DEPLOYMENT_ROOT / "manifests" / "delete-plan.json"
        plan = json.loads(plan_path.read_text(encoding="utf-8")) if plan_path.exists() else phase_delete_plan(roots, delete_files)
        execution = phase_delete(ftp, plan)
        summary["delete_execution"] = execution
        if execution["partial"]:
            ftp.quit()
            print("PARTIAL DELETE — STOPPED AFTER FAILURE")
            print(json.dumps(summary, ensure_ascii=False, indent=2))
            return 1

    if args.phase in ("list-after", "all"):
        listing_after = phase_list(ftp, roots, "after")
        after_class = classify(listing_after)
        write_json(DEPLOYMENT_ROOT / "manifests" / "classification-after.json", after_class)
        summary["listing_after"] = listing_after
        summary["classification_after"] = after_class

    ftp.quit()

    if args.phase in ("http-health", "all"):
        summary["http_health"] = phase_http_health()

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
