#!/usr/bin/env python3
import ftplib
import os
import re
import pathlib
import urllib.request

HOST = os.environ.get("SITE002_FTP_HOST", "polygonws.beget.tech")
U = os.environ.get("SITE002_FTP_USER", "")
P = os.environ.get("SITE002_FTP_PASS", "")

css = pathlib.Path(
    r"C:\AI MARS\shared\assets\icon-libraries\Font Awesome Pro 5.15.4\css\all.min.css"
).read_text(encoding="utf-8", errors="replace")
refs = [r.split("/")[-1].strip("\"'") for r in re.findall(r"url\(([^)]+\.woff2)\)", css)]

ftp = ftplib.FTP(HOST, timeout=60)
ftp.login(U, P)
ftp.cwd("assets/vendor/fontawesome-pro-5.15.4/webfonts")
remote = set()
ftp.retrlines("NLST", remote.add)
ftp.quit()

missing = [r for r in refs if r not in remote]
print("css_refs", len(refs))
print("remote_files", len(remote))
print("missing_from_css_refs", len(missing))
if missing:
    print("sample_missing", missing[:8])

base = "https://zpm.new-site.space"
for path in [
    "/assets/vendor/fontawesome-pro-5.15.4/css/all.min.css",
    "/assets/vendor/fontawesome-pro-5.15.4/webfonts/fa-solid-900.woff2",
    "/assets/vendor/fontawesome-pro-5.15.4/webfonts/pro-fa-light-300-5.15.4.woff2",
]:
    req = urllib.request.Request(base + path, method="HEAD", headers={"Cookie": "beget=begetok"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            print(path, r.status)
    except Exception as e:
        print(path, "ERR", e)
