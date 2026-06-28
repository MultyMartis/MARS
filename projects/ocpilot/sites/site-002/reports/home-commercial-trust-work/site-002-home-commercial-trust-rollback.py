#!/usr/bin/env python3
"""Rollback SITE-002 home commercial trust replacement."""
from __future__ import annotations

import ftplib
import io
import json
import sys
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002")
BACKUP = ROOT / "backups"
SUFFIX = "pre-home-commercial-trust-01.bak"


def ftp_connect() -> ftplib.FTP:
    ftp = ftplib.FTP(FTP_HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_upload(remote_path: str, data: bytes) -> None:
    ftp = ftp_connect()
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def ftp_delete(remote_path: str) -> None:
    ftp = ftp_connect()
    try:
        ftp.delete(remote_path)
    except ftplib.error_perm:
        pass
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


def main() -> int:
    restores = [
        (
            "catalog/view/theme/default/template/sections/blockdealersform.twig",
            BACKUP / f"catalog__view__theme__default__template__sections__blockdealersform.twig.{SUFFIX}",
        ),
        (
            "catalog/controller/common/home.php",
            BACKUP / f"catalog__controller__common__home.php.{SUFFIX}",
        ),
    ]
    for remote, local in restores:
        ftp_upload(remote, local.read_bytes())
    ftp_delete("catalog/view/theme/default/template/sections/blockcommercialtrust_home.twig")
    clear_twig_cache()
    print(json.dumps({"rollback": "complete", "restored": [r for r, _ in restores]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
