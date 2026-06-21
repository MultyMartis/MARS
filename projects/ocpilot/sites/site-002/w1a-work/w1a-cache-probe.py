#!/usr/bin/env python3
import ftplib

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ftp = ftplib.FTP(HOST, timeout=120)
ftp.login(FTP_USER, FTP_PASS)
for d in ["system/storage/cache", "system/storage/cache/template", "system/storage/modification"]:
    try:
        ftp.cwd("/" + d)
        lines = []
        ftp.retrlines("LIST", lines.append)
        print("\n==", d, "==", "entries:", len(lines))
        for line in lines[:15]:
            print(line)
    except Exception as e:
        print(d, "ERR", e)
ftp.quit()
