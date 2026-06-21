#!/usr/bin/env python3
import ftplib

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ftp = ftplib.FTP(HOST, timeout=120)
ftp.login(FTP_USER, FTP_PASS)
for d in [
    "system/storage/cache",
    "system/storage/cache/template",
    "storage/cache",
    "storage/cache/template",
]:
    try:
        ftp.cwd("/" + d if not d.startswith("/") else d)
        lines = []
        ftp.retrlines("LIST", lines.append)
        files = [l.split(None, 8)[-1] for l in lines if len(l.split(None, 8)) >= 9 and not l.startswith("d")]
        print(d, "files", len(files), "sample", files[:5])
    except Exception as e:
        print(d, "ERR", e)
ftp.quit()
