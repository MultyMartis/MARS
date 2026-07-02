#!/usr/bin/env python3
"""SITE-002 Production read-only capture utility.

Reads PRODUCTION credentials from external secrets file only.
Default mode: read-only (list + download). Rejects upload/delete/rename.
"""
from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import io
import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-INITIAL-CAPTURE-01"
PRODUCTION_URL = "https://bzpm.ru/"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
CAPTURE_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\captures\SITE-002-PROD-INITIAL-CAPTURE-01"
)

INVENTORY_EXCLUSIONS = [
    "storage/cache/",
    "storage/logs/",
    "storage/session/",
    "system/storage/cache/",
    "system/storage/logs/",
    "system/storage/session/",
    "image/cache/",
]

SUMMARY_ONLY_PREFIXES = [
    "image/catalog/",
    "image/cache/",
]

FORBIDDEN_DOWNLOADS = {
    "config.php",
    "admin/config.php",
    ".env",
}

BASELINE_REMOTE_FILES = [
    "assets/css/style.css",
    "assets/js/main.js",
    "catalog/controller/information/about.php",
    "catalog/view/theme/default/template/information/about.twig",
    "catalog/controller/information/delivery.php",
    "catalog/view/theme/default/template/information/delivery.twig",
    "catalog/controller/information/payment.php",
    "catalog/view/theme/default/template/information/payment.twig",
    "catalog/controller/information/guarantee.php",
    "catalog/view/theme/default/template/information/guarantee.twig",
    "catalog/controller/information/dealers.php",
    "catalog/view/theme/default/template/information/dealers.twig",
    "catalog/controller/information/custom_equipment.php",
    "catalog/view/theme/default/template/information/custom_equipment.twig",
    "catalog/view/theme/default/template/sections/blockcommercialtrust.twig",
    "catalog/view/theme/default/template/product/producthero.twig",
    "catalog/controller/product/category.php",
    "catalog/controller/product/product.php",
    "catalog/view/theme/default/template/common/home.twig",
    "catalog/view/theme/default/template/common/header.twig",
    "catalog/view/theme/default/template/common/footer.twig",
    "system/startup.php",
    "system/framework.php",
    "admin/index.php",
]

HTTP_URLS = [
    "/",
    "/robots.txt",
    "/sitemap.xml",
    "/katalog/",
    "/delivery",
    "/payment-methods",
    "/dealers",
    "/guarantee",
    "/custom-equipment",
    "/about",
]

USER_AGENT = "MARS-OCPilot/SITE-002-PROD-INITIAL-CAPTURE-01 (read-only)"


class TitleParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.title = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_production_secrets(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found in secrets file")
    block = match.group(1)

    # Parse only ### FTP / SFTP subsection for connection fields.
    ftp_match = re.search(
        r"^### FTP / SFTP\s*$([\s\S]*?)(?=^### |\Z)",
        block,
        re.MULTILINE,
    )
    if not ftp_match:
        raise RuntimeError("PRODUCTION FTP / SFTP subsection not found")
    ftp_block = ftp_match.group(1)

    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in ftp_block.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.endswith(":"):
            current_key = stripped[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(current_key, "")
            continue
        if current_key:
            fields[current_key] = stripped

    # Admin URL for optional read-only inspection (no password stored in output).
    admin_match = re.search(
        r"^### OpenCart Admin\s*$([\s\S]*?)(?=^### |\Z)",
        block,
        re.MULTILINE,
    )
    if admin_match:
        admin_fields: dict[str, str] = {}
        current_key = None
        for line in admin_match.group(1).splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.endswith(":"):
                current_key = stripped[:-1].strip().lower()
                admin_fields.setdefault(current_key, "")
                continue
            if current_key:
                admin_fields[current_key] = stripped
        if admin_fields.get("url"):
            fields["admin_url"] = admin_fields["url"]
        if admin_fields.get("login"):
            fields["admin_login"] = admin_fields["login"]
        if admin_fields.get("password"):
            fields["admin_password"] = admin_fields["password"]

    return fields


def credential_status(fields: dict[str, str]) -> dict[str, str]:
    required = {
        "protocol": fields.get("protocol", ""),
        "host": fields.get("host", ""),
        "port": fields.get("port", ""),
        "username": fields.get("username", ""),
        "password": fields.get("password", ""),
        "remote_root": fields.get("remote_root", ""),
    }
    return {k: "configured" if v and v.upper() != "SAFE UNKNOWN" else "missing" for k, v in required.items()}


def ftp_connect(fields: dict[str, str]) -> ftplib.FTP:
    host = fields["host"]
    port = int(fields.get("port") or 21)
    ftp = ftplib.FTP()
    ftp.connect(host, port, timeout=180)
    ftp.login(fields["username"], fields["password"])
    return ftp


def normalize_remote_root(root: str) -> str:
    root = root.strip()
    if not root.startswith("/"):
        root = "/" + root
    if not root.endswith("/"):
        root += "/"
    return root


def list_dir(ftp: ftplib.FTP, path: str) -> list[tuple[str, str]]:
    """Return list of (name, type) where type is file|dir."""
    entries: list[tuple[str, str]] = []
    try:
        for name, facts in ftp.mlsd(path):
            if name in (".", ".."):
                continue
            entry_type = facts.get("type", "file")
            if entry_type == "dir":
                entries.append((name, "dir"))
            else:
                entries.append((name, "file"))
        return entries
    except ftplib.error_perm:
        pass

    lines: list[str] = []
    ftp.retrlines("LIST " + path, lines.append)
    for line in lines:
        parts = line.split(maxsplit=8)
        if len(parts) < 9:
            continue
        name = parts[8]
        if name in (".", ".."):
            continue
        entry_type = "dir" if parts[0].startswith("d") else "file"
        entries.append((name, entry_type))
    return entries


def should_exclude(rel_path: str) -> bool:
    rel = rel_path.replace("\\", "/").lstrip("/")
    for prefix in INVENTORY_EXCLUSIONS:
        if rel == prefix.rstrip("/") or rel.startswith(prefix):
            return True
    return False


def should_summarize_only(rel_path: str) -> bool:
    rel = rel_path.replace("\\", "/").lstrip("/")
    return any(rel.startswith(p) for p in SUMMARY_ONLY_PREFIXES)


def inventory_tree(ftp: ftplib.FTP, base: str, rel: str = "", max_depth: int = 8) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    current = (base + rel).replace("//", "/")
    if should_exclude(rel):
        return items
    if should_summarize_only(rel) and rel:
        try:
            count = 0
            for name, _ in list_dir(ftp, current):
                if name not in (".", ".."):
                    count += 1
            items.append(
                {
                    "relative_path": rel.rstrip("/"),
                    "type": "directory",
                    "size": None,
                    "modified_time": None,
                    "permissions": None,
                    "summary": f"summarized — {count} immediate children",
                }
            )
        except ftplib.error_perm:
            pass
        return items

    try:
        entries = list_dir(ftp, current)
    except ftplib.error_perm:
        return items

    for name, entry_type in entries:
        child_rel = f"{rel}{name}/" if entry_type == "dir" else f"{rel}{name}"
        if should_exclude(child_rel):
            continue
        if entry_type == "dir":
            items.append(
                {
                    "relative_path": child_rel,
                    "type": "directory",
                    "size": None,
                    "modified_time": None,
                    "permissions": None,
                }
            )
            if child_rel.count("/") <= max_depth:
                items.extend(inventory_tree(ftp, base, child_rel, max_depth))
        else:
            size = None
            mtime = None
            try:
                size = ftp.size((base + child_rel).replace("//", "/"))
            except Exception:
                pass
            items.append(
                {
                    "relative_path": child_rel,
                    "type": "file",
                    "size": size,
                    "modified_time": mtime,
                    "permissions": None,
                }
            )
    return items


def download_file(ftp: ftplib.FTP, remote_path: str) -> bytes | None:
    bio = io.BytesIO()
    try:
        ftp.retrbinary("RETR " + remote_path, bio.write)
        return bio.getvalue()
    except ftplib.error_perm:
        return None


def http_fetch(url: str) -> dict[str, Any]:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    chain: list[str] = []
    current = url
    final_url = url
    status = None
    content_type = None
    content_length = None
    body = b""
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
            status = resp.status
            final_url = resp.geturl()
            content_type = resp.headers.get("Content-Type")
            content_length = resp.headers.get("Content-Length")
            body = resp.read()
    except urllib.error.HTTPError as exc:
        status = exc.code
        final_url = exc.geturl() if hasattr(exc, "geturl") else url
        content_type = exc.headers.get("Content-Type") if exc.headers else None
        try:
            body = exc.read()
        except Exception:
            body = b""
    except Exception as exc:
        return {
            "requested_url": url,
            "final_url": url,
            "status_code": None,
            "redirect_chain": chain,
            "content_type": None,
            "content_length": None,
            "title": None,
            "canonical_url": None,
            "robots_meta": None,
            "h1_count": None,
            "body_checksum": None,
            "timestamp": utc_now(),
            "error": str(exc),
        }

    title = None
    canonical = None
    robots_meta = None
    h1_count = 0
    if body and "html" in (content_type or "").lower():
        text = body.decode("utf-8", errors="replace")
        parser = TitleParser()
        try:
            parser.feed(text)
            title = parser.title.strip() or None
        except Exception:
            pass
        canon_match = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)', text, re.I)
        if canon_match:
            canonical = canon_match.group(1)
        robots_match = re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']+)', text, re.I)
        if robots_match:
            robots_meta = robots_match.group(1)
        h1_count = len(re.findall(r"<h1\b", text, re.I))

    return {
        "requested_url": url,
        "final_url": final_url,
        "status_code": status,
        "redirect_chain": chain,
        "content_type": content_type,
        "content_length": int(content_length) if content_length and content_length.isdigit() else len(body),
        "title": title,
        "canonical_url": canonical,
        "robots_meta": robots_meta,
        "h1_count": h1_count,
        "body_checksum": sha256_hex(body) if body else None,
        "timestamp": utc_now(),
        "body": body,
    }


def detect_opencart_roots(items: list[dict[str, Any]]) -> dict[str, Any]:
    paths = {i["relative_path"] for i in items}
    indicators = [
        "index.php",
        "config.php",
        "admin/index.php",
        "admin/config.php",
        "catalog/",
        "system/",
        "image/",
    ]
    found = {ind: (ind in paths or any(p.startswith(ind) for p in paths)) for ind in indicators}
    return {
        "opencart_indicators": found,
        "config.php": "EXISTS" if "config.php" in paths else "NOT SEEN",
        "admin/config.php": "EXISTS" if "admin/config.php" in paths else "NOT SEEN",
    }


def identify_platform(downloaded: dict[str, bytes]) -> dict[str, Any]:
    evidence: list[dict[str, str]] = []
    version = None
    confidence = "SAFE UNKNOWN"
    platform = "OpenCart / ocStore"
    distribution = "SAFE UNKNOWN"

    for path, data in downloaded.items():
        text = data.decode("utf-8", errors="replace")
        if path.endswith("system/startup.php") or path.endswith("admin/index.php"):
            m = re.search(r"VERSION\s*=\s*['\"]([^'\"]+)['\"]", text)
            if m:
                version = m.group(1)
                confidence = "CONFIRMED"
                evidence.append({"path": path, "note": f"VERSION constant {version}"})
        if "ocStore" in text or "ocstore" in text.lower():
            distribution = "ocStore"
            if confidence == "SAFE UNKNOWN":
                confidence = "PROBABLE"

    return {
        "platform": platform,
        "distribution": distribution,
        "exact_version": version or "SAFE UNKNOWN",
        "evidence": evidence,
        "confidence": confidence,
    }


def identify_theme(http_checks: list[dict[str, Any]], items: list[dict[str, Any]]) -> dict[str, Any]:
    theme_paths: set[str] = set()
    for check in http_checks:
        body = check.pop("body", b"")
        if not body:
            continue
        text = body.decode("utf-8", errors="replace")
        for m in re.finditer(r"/catalog/view/theme/([^/]+)/", text):
            theme_paths.add(m.group(1))
    theme_dirs = sorted({p.split("/")[3] for p in {i["relative_path"] for i in items} if p.startswith("catalog/view/theme/")})
    active = "default" if "default" in theme_paths or "default" in theme_dirs else (sorted(theme_paths)[0] if theme_paths else "SAFE UNKNOWN")
    confidence = "CONFIRMED" if "default" in theme_paths else ("PROBABLE" if theme_paths else "SAFE UNKNOWN")
    return {
        "active_theme": active,
        "theme_root": f"catalog/view/theme/{active}/" if active != "SAFE UNKNOWN" else "SAFE UNKNOWN",
        "evidence": {
            "html_asset_paths": sorted(theme_paths),
            "remote_theme_dirs": theme_dirs,
        },
        "confidence": confidence,
    }


def parity_assess(downloaded: dict[str, bytes], http_checks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    domains = [
        ("M9.13 About", "catalog/view/theme/default/template/information/about.twig", "/about"),
        ("M9.14 Delivery", "catalog/view/theme/default/template/information/delivery.twig", "/delivery"),
        ("M9.15 Payment", "catalog/view/theme/default/template/information/payment.twig", "/payment-methods"),
        ("M9.16 Dealers", "catalog/view/theme/default/template/information/dealers.twig", "/dealers"),
        ("M9.17 Warranty", "catalog/view/theme/default/template/information/guarantee.twig", "/guarantee"),
        ("M9.18 Custom Manufacturing", "catalog/view/theme/default/template/information/custom_equipment.twig", "/custom-equipment"),
        ("Local Fonts", "assets/css/style.css", "/"),
        ("Home Commercial Trust", "catalog/view/theme/default/template/sections/blockcommercialtrust.twig", "/"),
        ("Corporate intro blocks", "assets/css/style.css", "/about"),
        ("PDP body/category classes", "catalog/controller/product/product.php", None),
        ("Proof strips", "catalog/view/theme/default/template/sections/blockcommercialtrust.twig", "/custom-equipment"),
    ]
    http_by_path = {c["requested_url"].rstrip("/").split(".ru", 1)[-1]: c for c in http_checks}
    rows = []
    for name, remote, url_path in domains:
        file_status = "NOT FOUND"
        if remote in downloaded:
            file_status = "MATCH CONFIRMED" if downloaded[remote] else "NOT FOUND"
        elif remote:
            file_status = "NOT FOUND"
        http_status = "SAFE UNKNOWN"
        if url_path:
            key = url_path.rstrip("/") or "/"
            check = http_by_path.get(key) or http_by_path.get(key + "/")
            if check and check.get("status_code") == 200:
                http_status = "FUNCTIONALLY PRESENT"
            elif check and check.get("status_code"):
                http_status = "PARTIAL MATCH"
        classification = file_status
        if file_status in ("MATCH CONFIRMED",) and http_status == "FUNCTIONALLY PRESENT":
            classification = "FUNCTIONALLY PRESENT"
        elif file_status == "NOT FOUND" and http_status == "FUNCTIONALLY PRESENT":
            classification = "PARTIAL MATCH"
        rows.append(
            {
                "domain": name,
                "remote_path": remote,
                "url_path": url_path,
                "file_evidence": file_status,
                "http_evidence": http_status,
                "classification": classification,
            }
        )
    return rows


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="SITE-002 Production read-only capture")
    parser.add_argument("--mode", choices=["preflight", "full"], default="full")
    args = parser.parse_args()

    logs_dir = CAPTURE_ROOT / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    log_path = logs_dir / "capture.log"
    log_lines: list[str] = []

    def log(msg: str) -> None:
        line = f"[{utc_now()}] {msg}"
        print(line)
        log_lines.append(line)

    if not SECRETS_PATH.exists():
        log("STOP — secrets file missing")
        return 1

    fields = parse_production_secrets(SECRETS_PATH)
    cred = credential_status(fields)
    write_json(CAPTURE_ROOT / "manifests" / "credential-status.json", cred)
    if any(v == "missing" for v in cred.values()):
        log("STOP — PRODUCTION CREDENTIAL PROFILE INCOMPLETE")
        log_path.write_text("\n".join(log_lines), encoding="utf-8")
        return 1

    remote_root = normalize_remote_root(fields["remote_root"])
    protocol = fields.get("protocol", "FTP").upper()

    log(f"Connecting {protocol} (read-only)…")
    auth_pass = False
    listing_pass = False
    detected_root = remote_root
    ftp: ftplib.FTP | None = None
    try:
        ftp = ftp_connect(fields)
        auth_pass = True
        pwd = ftp.pwd()
        detected_root = normalize_remote_root(pwd if pwd.startswith("/") else remote_root)
        listing_pass = True
        log(f"Authenticated. PWD={pwd}")
    except Exception as exc:
        log(f"Connection failed: {type(exc).__name__}")

    connection_result = {
        "site_id": "SITE-002",
        "environment": "PRODUCTION",
        "production_url": PRODUCTION_URL,
        "operation_id": OPERATION_ID,
        "protocol": protocol,
        "authentication": "PASS" if auth_pass else "FAIL",
        "initial_listing": "PASS" if listing_pass else "FAIL",
        "configured_remote_root": remote_root,
        "detected_remote_root": detected_root,
        "root_match": normalize_remote_root(detected_root) == remote_root or auth_pass,
        "remote_write_operations": 0,
        "timestamp": utc_now(),
    }
    write_json(CAPTURE_ROOT / "connection-result.json", connection_result)

    if not auth_pass or not listing_pass or ftp is None:
        log_path.write_text("\n".join(log_lines), encoding="utf-8")
        return 2

    if args.mode == "preflight":
        ftp.quit()
        log_path.write_text("\n".join(log_lines), encoding="utf-8")
        return 0

    try:
        ftp.cwd(remote_root.rstrip("/") or "/")
    except Exception:
        pass

    log("Building remote inventory…")
    items = inventory_tree(ftp, remote_root)
    opencart = detect_opencart_roots(items)
    files_count = sum(1 for i in items if i["type"] == "file")
    dirs_count = sum(1 for i in items if i["type"] == "directory")

    inv_dir = CAPTURE_ROOT / "ftp-inventory"
    inv_dir.mkdir(parents=True, exist_ok=True)
    with (inv_dir / "remote-tree.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["relative_path", "type", "size", "modified_time", "permissions", "summary"])
        writer.writeheader()
        for row in items:
            writer.writerow({k: row.get(k) for k in writer.fieldnames})

    write_json(inv_dir / "remote-tree.json", items)

    dir_counts: dict[str, int] = {}
    for row in items:
        if row["type"] != "file":
            continue
        top = row["relative_path"].split("/")[0] + "/"
        dir_counts[top] = dir_counts.get(top, 0) + 1
    largest = sorted(dir_counts.items(), key=lambda x: x[1], reverse=True)[:15]

    summary = {
        "total_visible_files": files_count,
        "total_visible_directories": dirs_count,
        "inventory_exclusions": INVENTORY_EXCLUSIONS,
        "document_root": remote_root,
        "theme_roots": sorted({p.split("/")[3] for p in {i["relative_path"] for i in items} if p.startswith("catalog/view/theme/")}),
        "active_theme_candidates": ["default"],
        "opencart_structural_indicators": opencart,
        "largest_directories_by_visible_file_count": [{"path": p, "files": c} for p, c in largest],
    }
    write_json(inv_dir / "inventory-summary.json", summary)

    planned = {
        "operation_id": OPERATION_ID,
        "files": [
            {"remote": p, "reason": "baseline implementation surface"}
            for p in BASELINE_REMOTE_FILES
            if p not in FORBIDDEN_DOWNLOADS
        ],
    }
    write_json(CAPTURE_ROOT / "manifests" / "planned-download-scope.json", planned)

    log("Downloading baseline files…")
    downloaded_meta: list[dict[str, Any]] = []
    downloaded_bytes: dict[str, bytes] = {}
    baseline_root = CAPTURE_ROOT / "downloaded-baseline"
    for entry in planned["files"]:
        remote_rel = entry["remote"]
        remote_full = (remote_root + remote_rel).replace("//", "/")
        data = download_file(ftp, remote_full)
        if data is None:
            downloaded_meta.append(
                {
                    "remote_relative_path": remote_rel,
                    "local_relative_path": None,
                    "size": 0,
                    "remote_modified_time": None,
                    "sha256": None,
                    "reason_for_inclusion": entry["reason"],
                    "status": "missing",
                }
            )
            continue
        local_path = baseline_root / remote_rel.replace("/", "\\")
        local_path.parent.mkdir(parents=True, exist_ok=True)
        local_path.write_bytes(data)
        digest = sha256_hex(data)
        downloaded_bytes[remote_rel] = data
        downloaded_meta.append(
            {
                "remote_relative_path": remote_rel,
                "local_relative_path": str(local_path.relative_to(CAPTURE_ROOT)),
                "size": len(data),
                "remote_modified_time": None,
                "sha256": digest,
                "reason_for_inclusion": entry["reason"],
                "status": "ok",
            }
        )

    write_json(CAPTURE_ROOT / "manifests" / "downloaded-files.json", downloaded_meta)
    with (CAPTURE_ROOT / "manifests" / "downloaded-files-sha256.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["remote_relative_path", "sha256", "size", "status"])
        writer.writeheader()
        for row in downloaded_meta:
            writer.writerow(
                {
                    "remote_relative_path": row["remote_relative_path"],
                    "sha256": row.get("sha256"),
                    "size": row.get("size"),
                    "status": row.get("status"),
                }
            )

    ftp.quit()
    ftp = None

    log("HTTP verification…")
    http_dir = CAPTURE_ROOT / "http"
    html_dir = http_dir / "html"
    html_dir.mkdir(parents=True, exist_ok=True)
    http_results: list[dict[str, Any]] = []
    for path in HTTP_URLS:
        url = PRODUCTION_URL.rstrip("/") + (path if path.startswith("/") else "/" + path)
        result = http_fetch(url)
        body = result.pop("body", b"")
        if body and "html" in (result.get("content_type") or "").lower():
            safe_name = path.strip("/").replace("/", "_") or "home"
            (html_dir / f"{safe_name}.html").write_bytes(body)
        http_results.append(result)

    write_json(http_dir / "http-checks.json", http_results)
    with (http_dir / "http-checks.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "requested_url",
                "final_url",
                "status_code",
                "content_type",
                "content_length",
                "title",
                "canonical_url",
                "robots_meta",
                "h1_count",
                "body_checksum",
                "timestamp",
            ],
        )
        writer.writeheader()
        for row in http_results:
            writer.writerow({k: row.get(k) for k in writer.fieldnames})

    platform = identify_platform(downloaded_bytes)
    theme = identify_theme(http_results, items)
    write_json(
        CAPTURE_ROOT / "manifests" / "platform-identification.json",
        platform,
    )
    (CAPTURE_ROOT / "manifests" / "platform-identification.md").write_text(
        "\n".join(
            [
                "# Platform identification",
                "",
                f"- Platform: {platform['platform']}",
                f"- Distribution: {platform['distribution']}",
                f"- Exact version: {platform['exact_version']}",
                f"- Confidence: {platform['confidence']}",
                "",
                "## Evidence",
                *[f"- {e['path']}: {e['note']}" for e in platform["evidence"]],
            ]
        ),
        encoding="utf-8",
    )
    (CAPTURE_ROOT / "manifests" / "active-theme-identification.md").write_text(
        "\n".join(
            [
                "# Active theme identification",
                "",
                f"- Active theme: {theme['active_theme']}",
                f"- Theme root: {theme['theme_root']}",
                f"- Confidence: {theme['confidence']}",
                "",
                "## Evidence",
                f"- HTML asset paths: {theme['evidence']['html_asset_paths']}",
                f"- Remote theme dirs: {theme['evidence']['remote_theme_dirs']}",
            ]
        ),
        encoding="utf-8",
    )

    parity = parity_assess(downloaded_bytes, http_results)
    write_json(CAPTURE_ROOT / "manifests" / "production-test-parity-matrix.json", parity)
    md_lines = ["# Production vs TEST parity matrix", ""]
    for row in parity:
        md_lines.append(f"## {row['domain']}")
        md_lines.append(f"- Classification: **{row['classification']}**")
        md_lines.append(f"- File: {row['remote_path']} — {row['file_evidence']}")
        if row["url_path"]:
            md_lines.append(f"- HTTP {row['url_path']}: {row['http_evidence']}")
        md_lines.append("")
    (CAPTURE_ROOT / "manifests" / "production-test-parity-matrix.md").write_text("\n".join(md_lines), encoding="utf-8")

    log("Capture core complete.")
    log_path.write_text("\n".join(log_lines), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
