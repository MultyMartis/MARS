#!/usr/bin/env python3
"""Read-only FTP fetch — category twig templates for audit."""
import ftplib
import os

HOST = "polygonws.beget.tech"
USER = "polygonws_zpm"
PWD = "RT4uK7VKr&c"
OUT = r"C:\AI MARS\projects\ocpilot\sites\site-002\category-audit-v1-work\templates"
FILES = [
    "catalog/view/theme/default/template/product/category.twig",
    "catalog/view/theme/default/template/sections/filterssidebar.twig",
    "catalog/view/theme/default/template/sections/categorylayout.twig",
    "catalog/view/theme/default/template/common/product_card.twig",
    "catalog/view/theme/default/template/product/thumb.twig",
]


def main():
    os.makedirs(OUT, exist_ok=True)
    ftp = ftplib.FTP(HOST, timeout=120)
    ftp.login(USER, PWD)
    for remote in FILES:
        local_name = remote.replace("/", "__")
        local = os.path.join(OUT, local_name)
        try:
            with open(local, "wb") as f:
                ftp.retrbinary("RETR " + remote, f.write)
            print("OK", remote, os.path.getsize(local))
        except Exception as e:
            print("FAIL", remote, e)
    ftp.quit()


if __name__ == "__main__":
    main()
