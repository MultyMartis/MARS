#!/usr/bin/env python3
"""Rollback SITE-002 corporate intro blocks from .pre-site-002-corp-intro-blocks-01.bak."""
from __future__ import annotations

import ftplib
import io
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002")
BACKUP = ROOT / "backups"
SUFFIX = "pre-site-002-corp-intro-blocks-01.bak"

FILES = [
    "catalog/view/theme/default/template/information/about.twig",
    "catalog/view/theme/default/template/information/delivery.twig",
    "catalog/view/theme/default/template/information/payment.twig",
    "catalog/view/theme/default/template/information/guarantee.twig",
    "catalog/view/theme/default/template/information/dealers.twig",
    "catalog/view/theme/default/template/information/custom_equipment.twig",
    "assets/css/style.css",
]


def ftp_connect() -> ftplib.FTP:
    ftp = ftplib.FTP(FTP_HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def main() -> None:
    ftp = ftp_connect()
    restored = []
    for remote in FILES:
        backup = BACKUP / f"{remote.replace('/', '__')}.{SUFFIX}"
        if not backup.is_file():
            print(f"SKIP missing backup: {backup}")
            continue
        data = backup.read_bytes()
        ftp.storbinary(f"STOR {remote}", io.BytesIO(data))
        restored.append(remote)
        print(f"RESTORED {remote} ({len(data)} bytes)")
    ftp.quit()
    print("Done:", len(restored), "files")


if __name__ == "__main__":
    main()
