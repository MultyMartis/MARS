#!/usr/bin/env python3
"""Upload one-shot cache flush helper and invoke it on TEST."""
import ftplib
import io
import json
import urllib.request
import ssl

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"
REMOTE = "m8.3-wave1-cache-flush.php"
LOCAL = r"C:\AI MARS\projects\ocpilot\sites\site-002\m8.3-wave1-cleanup-work\m8.3-wave1-cache-flush.php"
URL = "https://zpm.new-site.space/m8.3-wave1-cache-flush.php?token=m8.3-wave1-cache-flush-20260615"


def main():
    data = open(LOCAL, "rb").read()
    ftp = ftplib.FTP(HOST, timeout=120)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.storbinary("STOR " + REMOTE, io.BytesIO(data))
    ftp.quit()

    ctx = ssl.create_default_context()
    resp = urllib.request.urlopen(
        urllib.request.Request(URL, headers={"User-Agent": "BZPM-M8.3"}),
        timeout=60,
        context=ctx,
    )
    body = resp.read().decode("utf-8", "replace")
    print(body)


if __name__ == "__main__":
    main()
