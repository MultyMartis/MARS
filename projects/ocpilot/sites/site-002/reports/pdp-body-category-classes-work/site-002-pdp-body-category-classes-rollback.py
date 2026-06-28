#!/usr/bin/env python3
"""SITE-002 — rollback PDP body category classes to pre-deploy backup."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002")
BACKUP = ROOT / "backups" / "catalog__controller__product__product.php.pre-pdp-body-category-classes.bak"
REMOTE = "catalog/controller/product/product.php"
WORK = ROOT / "reports" / "pdp-body-category-classes-work"


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ftp_connect() -> ftplib.FTP:
    ftp = ftplib.FTP(FTP_HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def main() -> None:
    if not BACKUP.is_file():
        raise SystemExit(f"Backup missing: {BACKUP}")

    data = BACKUP.read_bytes()
    ftp = ftp_connect()
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + REMOTE, bio)
    ftp.quit()

    result = {
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "action": "rollback",
        "remote": REMOTE,
        "restored_from": str(BACKUP),
        "sha256": sha256_hex(data),
        "bytes": len(data),
    }
    out = WORK / "rollback-result.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
