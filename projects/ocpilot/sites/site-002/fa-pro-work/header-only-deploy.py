#!/usr/bin/env python3
import ftplib
import io
import os
import sys
from pathlib import Path

HOST = os.environ.get("SITE002_FTP_HOST", "")
FTP_USER = os.environ.get("SITE002_FTP_USER", "")
FTP_PASS = os.environ.get("SITE002_FTP_PASS", "")

BASE = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
BACKUP = BASE / "backups" / "header.twig.pre-fa-pro-install.bak"
WORK = BASE / "fa-pro-work" / "header.twig"
REMOTE = "catalog/view/theme/default/template/common/header.twig"
FA_LINK = '<link rel="stylesheet" href="/assets/vendor/fontawesome-pro-5.15.4/css/all.min.css">'
STYLE_LINK = '<link rel="stylesheet" href="/assets/css/style.css" />'


def main():
    if not all((HOST, FTP_USER, FTP_PASS)):
        print("Missing FTP env vars", file=sys.stderr)
        return 1

    text = BACKUP.read_text(encoding="utf-8")
    if FA_LINK not in text:
        text = text.replace(
            f"    {STYLE_LINK}",
            f"    {FA_LINK}\n    {STYLE_LINK}",
            1,
        )
    WORK.write_text(text, encoding="utf-8")

    ftp = ftplib.FTP(HOST, timeout=60)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.storbinary("STOR " + REMOTE, io.BytesIO(text.encode("utf-8")))
    ftp.quit()

    for cache_dir in ("system/storage/cache", "system/storage/cache/template"):
        ftp = ftplib.FTP(HOST, timeout=60)
        ftp.login(FTP_USER, FTP_PASS)
        try:
            ftp.cwd(cache_dir)
            entries = []
            ftp.retrlines("LIST", entries.append)
            for line in entries:
                parts = line.split(None, 8)
                if len(parts) < 9:
                    continue
                name = parts[8]
                if name in (".", "..", "index.html") or line.startswith("d"):
                    continue
                try:
                    ftp.delete(name)
                except ftplib.error_perm:
                    pass
        except ftplib.error_perm:
            pass
        finally:
            ftp.quit()

    print("OK header deployed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
