#!/usr/bin/env python3
"""SITE-002 — Operator Manual Polish Canonical Checkpoint — read-only FTP capture + diff vs Pass 1.2."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
import ssl
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002")
WORK = ROOT / "reports" / "site-002-operator-manual-polish-01-work"
CAPTURE = WORK / "live-capture"
BACKUP = ROOT / "backups"
BACKUP_SUFFIX = "pre-site-002-operator-manual-polish-01.bak"

PASS12_SHA = {
    "assets/css/style.css": "243d6d5e2a1ad00c06c450f4b90dc72adb1671b64a681f266675abdbd9330252",
}

REMOTE_FILES = [
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
    "catalog/view/theme/default/template/product/producthero.twig",
    "catalog/view/theme/default/template/sections/blockcommercialtrust.twig",
    "catalog/view/theme/default/template/sections/filterssidebar.twig",
    "catalog/controller/product/category.php",
    "catalog/model/catalog/product.php",
]

PAGE_URLS = [
    ("home", "https://zpm.new-site.space/"),
    ("about", "https://zpm.new-site.space/about"),
    ("delivery", "https://zpm.new-site.space/delivery"),
    ("payment", "https://zpm.new-site.space/payment-methods"),
    ("guarantee", "https://zpm.new-site.space/guarantee"),
    ("dealers", "https://zpm.new-site.space/dealers"),
    ("custom_equipment", "https://zpm.new-site.space/custom-equipment"),
    ("catalog", "https://zpm.new-site.space/katalog/"),
    ("pdp", "https://zpm.new-site.space/index.php?route=product/product&product_id=50"),
]


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def local_capture_name(remote_path: str) -> str:
    return remote_path.replace("/", "__")


def backup_name(remote_path: str) -> str:
    base = local_capture_name(remote_path)
    return f"{base}.{BACKUP_SUFFIX}"


def ftp_connect() -> ftplib.FTP:
    return ftplib.FTP(FTP_HOST, timeout=180)


def ftp_download(remote_path: str) -> bytes | None:
    ftp = ftp_connect()
    ftp.login(FTP_USER, FTP_PASS)
    bio = io.BytesIO()
    try:
        ftp.retrbinary("RETR " + remote_path, bio.write)
        ftp.quit()
        return bio.getvalue()
    except ftplib.error_perm:
        ftp.quit()
        return None


def http_check(url: str) -> dict:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "SITE-002-checkpoint/1.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            return {"url": url, "http_status": resp.status, "ok": resp.status == 200}
    except urllib.error.HTTPError as exc:
        return {"url": url, "http_status": exc.code, "ok": False}
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "http_status": None, "ok": False, "error": str(exc)}


def main() -> None:
    CAPTURE.mkdir(parents=True, exist_ok=True)
    BACKUP.mkdir(parents=True, exist_ok=True)
    captured_at = datetime.now(timezone.utc).isoformat()
    entries: list[dict] = []

    print("Downloading live TEST files (read-only)...")
    for remote_path in REMOTE_FILES:
        data = ftp_download(remote_path)
        if data is None:
            entries.append(
                {
                    "remote": remote_path,
                    "status": "missing_on_ftp",
                    "sha256": None,
                    "bytes": 0,
                }
            )
            print(f"  MISSING {remote_path}")
            continue

        digest = sha256_hex(data)
        capture_path = CAPTURE / local_capture_name(remote_path)
        capture_path.write_bytes(data)
        backup_path = BACKUP / backup_name(remote_path)
        backup_path.write_bytes(data)

        pass12_sha = PASS12_SHA.get(remote_path)
        changed_vs_pass12 = pass12_sha is not None and digest != pass12_sha

        entry = {
            "remote": remote_path,
            "status": "ok",
            "sha256": digest,
            "bytes": len(data),
            "capture_local": str(capture_path),
            "backup_local": str(backup_path),
            "pass12_sha256": pass12_sha,
            "changed_vs_pass12": changed_vs_pass12 if pass12_sha else None,
        }
        entries.append(entry)
        flag = " CHANGED vs Pass1.2" if changed_vs_pass12 else ""
        print(f"  OK {remote_path} ({len(data)} bytes) sha256={digest[:16]}...{flag}")

    print("\nHTTP page checks...")
    qa_urls: dict[str, dict] = {}
    for name, url in PAGE_URLS:
        result = http_check(url)
        qa_urls[name] = result
        status = result.get("http_status")
        ok = result.get("ok")
        print(f"  {name}: {status} {'PASS' if ok else 'FAIL'}")

    manifest = {
        "checkpoint": "SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01",
        "pass": "site-002-operator-manual-polish-01",
        "mode": "read-only-capture",
        "environment": "https://zpm.new-site.space/",
        "captured_at": captured_at,
        "operator_beget_backup": "CONFIRMED",
        "prior_checkpoint": "SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2",
        "files": entries,
        "qa_urls": qa_urls,
        "changed_vs_pass12": [
            e["remote"] for e in entries if e.get("changed_vs_pass12") is True
        ],
    }

    manifest_path = WORK / "capture-manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nManifest: {manifest_path}")
    print(f"Changed vs Pass 1.2: {manifest['changed_vs_pass12'] or '(none with Pass 1.2 baseline hash)'}")


if __name__ == "__main__":
    main()
