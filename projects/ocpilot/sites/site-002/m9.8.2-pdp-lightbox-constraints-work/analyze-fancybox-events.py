#!/usr/bin/env python3
import ftplib
import io
import re

ftp = ftplib.FTP("polygonws.beget.tech", timeout=60)
ftp.login("polygonws_zpm", "RT4uK7VKr&c")
bio = io.BytesIO()
ftp.retrbinary("RETR assets/js/vendor/fancybox/fancybox.umd.js", bio.write)
t = bio.getvalue().decode("utf-8", "replace")
for pat in ["init:", 'trigger("init"', "trigger('init'", "on.init"]:
    print(pat, t.count(pat))
for m in re.finditer(r'["\'](init[A-Za-z]*)["\']', t):
  print("event:", m.group(1))
