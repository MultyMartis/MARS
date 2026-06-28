#!/usr/bin/env python3
"""Emergency restore corporate pages from corp-cta-v2 backups."""
from __future__ import annotations

import ftplib
import io
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002")
BACKUP = ROOT / "backups"
SUFFIX = "pre-site-002-corp-cta-v2.bak"

RESTORE = [
    "catalog/view/theme/default/template/information/about.twig",
    "catalog/view/theme/default/template/information/delivery.twig",
    "catalog/view/theme/default/template/information/payment.twig",
    "catalog/view/theme/default/template/information/guarantee.twig",
    "catalog/view/theme/default/template/information/dealers.twig",
    "catalog/view/theme/default/template/information/custom_equipment.twig",
]


def ftp_connect() -> ftplib.FTP:
    ftp = ftplib.FTP(FTP_HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_upload(remote_path: str, data: bytes) -> None:
    ftp = ftp_connect()
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def clear_twig_cache() -> None:
    try:
        ftp = ftp_connect()
        try:
            ftp.cwd("system/storage/cache/template")
            for name in ftp.nlst():
                if name in (".", ".."):
                    continue
                try:
                    ftp.delete(name)
                except ftplib.error_perm:
                    pass
        except ftplib.error_perm:
            pass
        ftp.quit()
    except Exception:
        pass


def main() -> None:
    for remote in RESTORE:
        backup = BACKUP / f"{remote.replace('/', '__')}.{SUFFIX.replace('pre-', '')}"
        # backup naming: catalog__view__...pre-site-002-corp-cta-v2.bak
        backup = BACKUP / f"{remote.replace('/', '__')}.pre-site-002-corp-cta-v2.bak"
        if not backup.exists():
            raise FileNotFoundError(backup)
        data = backup.read_bytes()
        ftp_upload(remote, data)
        print(f"restored {remote} ({len(data)} bytes)")
    clear_twig_cache()
    print("twig cache cleared")


if __name__ == "__main__":
    main()
