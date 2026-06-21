#!/usr/bin/env python3
import ftplib, io, re

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

paths = [
    "system/storage/modification/catalog/controller/product/product.php",
    "storage/modification/catalog/controller/product/product.php",
    "../storage/modification/catalog/controller/product/product.php",
]

ftp = ftplib.FTP(HOST, timeout=120)
ftp.login(FTP_USER, FTP_PASS)
for p in paths:
    try:
        b = io.BytesIO()
        ftp.retrbinary("RETR " + p, b.write)
        t = b.getvalue().decode("utf-8", "replace")
        print(p, "EXISTS", len(t), "SUPER_ATTS" in t)
        if "super_atts" in t:
            m = re.search(r"super_atts[\s\S]{0,400}", t)
            print(m.group(0)[:400] if m else "")
    except Exception as e:
        print(p, "MISSING", e)
ftp.quit()
