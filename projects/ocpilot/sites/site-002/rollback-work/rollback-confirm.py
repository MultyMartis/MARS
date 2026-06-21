#!/usr/bin/env python3
"""Confirm live FTP files match rollback backups."""
import ftplib
import hashlib
import io
import os

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

REMOTE = {
    "producthero": "catalog/view/theme/default/template/product/producthero.twig",
    "producttabs": "catalog/view/theme/default/template/product/producttabs.twig",
    "style": "assets/css/style.css",
}

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002\backups"
LOCAL = {
    "producthero": os.path.join(BASE, "producthero.twig.pre-w1a.bak"),
    "producttabs": os.path.join(BASE, "producttabs.twig.pre-w1b.bak"),
    "style": os.path.join(BASE, "style.css.pre-w1a.bak"),
}


def md5(data):
    return hashlib.md5(data).hexdigest()


def ftp_download(remote_path):
    ftp = ftplib.FTP(HOST, timeout=120)
    ftp.login(FTP_USER, FTP_PASS)
    bio = io.BytesIO()
    ftp.retrbinary("RETR " + remote_path, bio.write)
    ftp.quit()
    return bio.getvalue()


def main():
    for key in REMOTE:
        live = ftp_download(REMOTE[key])
        with open(LOCAL[key], "rb") as f:
            local = f.read()
        match = live == local
        print(
            key,
            "MATCH" if match else "DIFF",
            f"live={len(live)} local={len(local)}",
            f"md5_live={md5(live)} md5_local={md5(local)}",
        )


if __name__ == "__main__":
    main()
