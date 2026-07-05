#!/usr/bin/env python3
"""SITE-002 parallel 1C import cron wrapper — legacy map, prepare, upload, verify."""
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

OPERATION_ID = "SITE-002-PROD-CRON-WRAPPER-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-SORT-MENU-ORDER-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CRON-WRAPPER-01"
)
SUBDIRS = ("source", "prepared", "backup", "verification", "rollback", "manifests", "logs", "legacy-map")
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

LEGACY_REMOTE_FILES = [
    "catalog/controller/common/cronjob.php",
    "catalog/model/catalog/cronjob.php",
    "catalog/controller/common/import_1C.php",
    "catalog/controller/common/import_1C_offers.php",
    "catalog/controller/common/import_1C_process.php",
    "reindex_prices.php",
]

FORBIDDEN_DOWNLOADS = {"config.php", "admin/config.php", ".env"}

WRAPPER_STORAGE_REMOTE = "/storage/mars-tools/cron/mars_1c_import_wrapper.php"
WRAPPER_PUBLIC_REMOTE = "/public_html/mars-tools/cron/mars_1c_import_wrapper.php"
WRAPPER_PUBLIC_GATEWAY_REMOTE = "/public_html/mars-tools/cron/mars_1c_http_gateway.php"
INDEX_HTML_REMOTES = [
    "/storage/mars-tools/index.html",
    "/storage/mars-tools/cron/index.html",
    "/public_html/mars-tools/index.html",
    "/public_html/mars-tools/cron/index.html",
]

LOCAL_WRAPPER = DEPLOYMENT_ROOT / "prepared" / "mars_1c_import_wrapper.php"
LOCAL_GATEWAY = DEPLOYMENT_ROOT / "prepared" / "mars_1c_http_gateway.php"
LOCAL_INDEX = DEPLOYMENT_ROOT / "prepared" / "index.html"


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


def list_dir_names(ftp: ftplib.FTP, path: str) -> list[str]:
    names: list[str] = []
    try:
        for name, facts in ftp.mlsd(normalize_remote(path)):
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


def http_get(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read(65536)
            return {
                "url": url,
                "status_code": resp.status,
                "body_preview": body[:4000].decode("utf-8", errors="replace"),
                "body_sha256": sha256_bytes(body),
                "timestamp": utc_now(),
            }
    except urllib.error.HTTPError as exc:
        body = exc.read(65536) if exc.fp else b""
        return {
            "url": url,
            "status_code": exc.code,
            "body_preview": body[:4000].decode("utf-8", errors="replace"),
            "body_sha256": sha256_bytes(body) if body else None,
            "timestamp": utc_now(),
        }
    except Exception as exc:
        return {"url": url, "status_code": None, "error": str(exc), "timestamp": utc_now()}


def init_operation_tree() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "environment": ENVIRONMENT,
        "production_url": PRODUCTION_URL,
        "baseline_before": BASELINE_BEFORE,
        "change_type": "parallel-1c-cron-wrapper",
        "legacy_import_policy": "preserve-sergey-version",
        "real_import_execution": "forbidden",
        "db_mutation": "forbidden",
        "beget_cron_activation": "forbidden",
        "authorized_remote_changes": "new wrapper files only",
        "created_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation.json", manifest)


def phase_legacy_map(ftp: ftplib.FTP, roots: dict[str, str]) -> dict[str, Any]:
    public = roots["public_root"]
    legacy_dir = DEPLOYMENT_ROOT / "source" / "legacy"
    legacy_dir.mkdir(parents=True, exist_ok=True)
    files_meta: list[dict[str, Any]] = []

    for rel in LEGACY_REMOTE_FILES:
        remote = public + rel
        data = ftp_download(ftp, remote)
        entry: dict[str, Any] = {
            "remote_relative": rel,
            "remote_full": remote,
            "classification": "LEGACY SERGEY — READ ONLY",
            "status": "missing" if data is None else "downloaded",
        }
        if data is not None:
            local_name = rel.replace("/", "__")
            local_path = legacy_dir / local_name
            local_path.write_bytes(data)
            entry["sha256"] = sha256_bytes(data)
            entry["size"] = len(data)
            entry["local_path"] = str(local_path)
        files_meta.append(entry)

    xml_dir = public + "1c_incoming/webdata/"
    xml_listing: dict[str, Any] = {"path": xml_dir, "classification": "LEGACY SERGEY — READ ONLY"}
    try:
        names = list_dir_names(ftp, xml_dir)
        xml_listing["status"] = "listed"
        xml_listing["entry_count"] = len(names)
        xml_listing["sample_names"] = sorted(names)[:20]
        xml_listing["import0_glob_matches"] = [n for n in names if n.startswith("import0_") and n.endswith(".xml")]
        xml_listing["offers0_glob_matches"] = [n for n in names if n.startswith("offers0_") and n.endswith(".xml")]
    except Exception as exc:
        xml_listing["status"] = "error"
        xml_listing["error"] = str(exc)

    target_checks = {
        "storage_wrapper": roots["storage_root"] + "mars-tools/cron/mars_1c_import_wrapper.php",
        "public_wrapper": roots["public_root"] + "mars-tools/cron/mars_1c_import_wrapper.php",
        "public_gateway": roots["public_root"] + "mars-tools/cron/mars_1c_http_gateway.php",
    }
    exists_map = {k: ftp_exists(ftp, v) for k, v in target_checks.items()}

    result = {
        "timestamp": utc_now(),
        "legacy_files": files_meta,
        "xml_directory": xml_listing,
        "wrapper_target_exists": exists_map,
        "upload_blocked": any(exists_map.values()),
    }
    write_json(DEPLOYMENT_ROOT / "legacy-map" / "sergey-legacy-import-files.json", result)
    return result


def phase_upload(ftp: ftplib.FTP, roots: dict[str, str], replace_operation: bool = False) -> dict[str, Any]:
    if not LOCAL_WRAPPER.exists():
        return {"status": "skipped", "reason": "local wrapper missing"}

    targets = [
        ("storage_wrapper", roots["storage_root"] + "mars-tools/cron/mars_1c_import_wrapper.php", LOCAL_WRAPPER),
        ("public_gateway", roots["public_root"] + "mars-tools/cron/mars_1c_http_gateway.php", LOCAL_GATEWAY),
    ]
    existence = {name: ftp_exists(ftp, remote) for name, remote, _ in targets}
    if any(existence.values()) and not replace_operation:
        return {"status": "blocked", "reason": "STOP — WRAPPER TARGET EXISTS", "existence": existence}

    uploads: list[dict[str, Any]] = []
    for name, remote, local in targets:
        data = local.read_bytes()
        ftp_upload(ftp, remote, data)
        remote_data = ftp_download(ftp, remote)
        uploads.append(
            {
                "name": name,
                "remote": remote,
                "local_sha256": sha256_bytes(data),
                "remote_sha256": sha256_bytes(remote_data) if remote_data else None,
                "match": remote_data == data if remote_data else False,
            }
        )

    for remote in [
        roots["storage_root"] + "mars-tools/index.html",
        roots["storage_root"] + "mars-tools/cron/index.html",
        roots["public_root"] + "mars-tools/index.html",
        roots["public_root"] + "mars-tools/cron/index.html",
    ]:
        if not ftp_exists(ftp, remote):
            ftp_upload(ftp, remote, LOCAL_INDEX.read_bytes())

    write_json(DEPLOYMENT_ROOT / "manifests" / "upload-result.json", uploads)
    return {"status": "uploaded", "uploads": uploads}


def phase_verify_http() -> dict[str, Any]:
    base = PRODUCTION_URL.rstrip("/") + "/mars-tools/cron/mars_1c_http_gateway.php"
    checks = {
        "dry_run": http_get(base + "?mode=dry-run"),
        "status": http_get(base + "?mode=status"),
        "run_without_token": http_get(base + "?mode=run"),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "http-checks.json", checks)
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument(
        "--phase",
        choices=["init", "legacy-map", "upload", "verify-http", "all"],
        default="all",
    )
    parser.add_argument(
        "--replace-operation-files",
        action="store_true",
        help="Replace wrapper files uploaded in this operation only (same SHA manifest)",
    )
    args = parser.parse_args()

    init_operation_tree()
    log: list[str] = []

    if args.phase in ("init",):
        print("Operation tree initialized.")
        return 0

    if not SECRETS_PATH.exists():
        print("STOP — secrets file missing")
        return 1

    fields = parse_production_secrets(SECRETS_PATH)
    ftp = ftp_connect(fields)
    roots = resolve_roots(ftp)
    write_json(DEPLOYMENT_ROOT / "manifests" / "ftp-roots.json", roots)
    log.append(f"FTP roots: {roots}")

    legacy_result: dict[str, Any] = {}
    upload_result: dict[str, Any] = {}
    http_result: dict[str, Any] = {}

    if args.phase in ("legacy-map", "all"):
        legacy_result = phase_legacy_map(ftp, roots)
        log.append(f"Legacy map: {len(legacy_result.get('legacy_files', []))} files")

    if args.phase in ("upload", "all"):
        if legacy_result.get("upload_blocked") and args.phase == "all":
            upload_result = {"status": "blocked", "reason": "precheck exists map", "detail": legacy_result.get("wrapper_target_exists")}
        else:
            upload_result = phase_upload(ftp, roots, replace_operation=args.replace_operation_files)
        log.append(f"Upload: {upload_result.get('status')}")

    ftp.quit()

    if args.phase in ("verify-http", "all") and upload_result.get("status") == "uploaded":
        http_result = phase_verify_http()
        log.append("HTTP verify complete")

    write_text(DEPLOYMENT_ROOT / "logs" / "run.log", "\n".join(log))
    summary = {"legacy": legacy_result, "upload": upload_result, "http": http_result, "timestamp": utc_now()}
    write_json(DEPLOYMENT_ROOT / "manifests" / "run-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
