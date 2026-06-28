#!/usr/bin/env python3
"""Rollback SITE-002 About restore v2 — restore pre-restore-v2 FTP backups."""
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
BACKUP_DIR = ROOT / "backups"
OUT_DIR = ROOT / "reports" / "m9.13-restore-v2-work"
SUFFIX = "pre-site-002-about-restore-v2.bak"

ROLLBACK_MAP = [
    (
        "catalog/view/theme/default/template/information/about.twig",
        BACKUP_DIR / f"catalog__view__theme__default__template__information__about.twig.{SUFFIX}",
    ),
    (
        "catalog/controller/information/about.php",
        BACKUP_DIR / f"catalog__controller__information__about.php.{SUFFIX}",
    ),
    (
        "assets/css/style.css",
        BACKUP_DIR / f"style.css.{SUFFIX}",
    ),
    (
        "assets/img/about-page-img.jpg",
        BACKUP_DIR / f"assets__img__about-page-img.jpg.{SUFFIX}",
    ),
]


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ftp_connect() -> ftplib.FTP:
    ftp = ftplib.FTP(FTP_HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_upload(remote_path: str, data: bytes) -> None:
    ftp = ftp_connect()
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def clear_twig_cache() -> list[str]:
    cleared: list[str] = []
    try:
        ftp = ftp_connect()
        try:
            ftp.cwd("system/storage/cache/template")
            for name in ftp.nlst():
                if name in (".", ".."):
                    continue
                try:
                    ftp.delete(name)
                    cleared.append(name)
                except ftplib.error_perm:
                    pass
        except ftplib.error_perm:
            pass
        ftp.quit()
    except Exception:
        pass
    return cleared


def main() -> None:
    manifest: dict = {
        "action": "rollback-restore-v2",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "files": {},
    }
    for remote, backup in ROLLBACK_MAP:
        if not backup.is_file():
            raise SystemExit(f"Missing backup: {backup}")
        data = backup.read_bytes()
        ftp_upload(remote, data)
        manifest["files"][remote] = {
            "backup": str(backup),
            "sha256": sha256_hex(data),
            "bytes": len(data),
        }
    manifest["twig_cache_cleared"] = clear_twig_cache()
    manifest["note"] = (
        "about-logistics.jpg may remain orphaned on server after rollback; "
        "harmless if pre-restore About did not reference it"
    )
    out = OUT_DIR / "rollback-restore-v2-manifest.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
