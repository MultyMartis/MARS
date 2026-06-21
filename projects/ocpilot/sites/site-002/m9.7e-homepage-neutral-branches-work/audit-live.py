#!/usr/bin/env python3
"""Live TEST audit — homepage category section (pre-fix)."""
import ftplib
import hashlib
import io
import re
import urllib.request
from pathlib import Path

BASE = "https://zpm.new-site.space"
HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"
WORK = Path(__file__).resolve().parent
BACKUP = WORK / "backups"
BACKUP.mkdir(exist_ok=True)

REMOTE_FILES = [
    "catalog/controller/common/home.php",
    "system/library/zpm/category_visibility.php",
]


def fetch(path: str) -> str:
    req = urllib.request.Request(BASE + path, headers={"User-Agent": "M9.7E-audit"})
    return urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")


def homepage_cat_cards(html: str) -> list:
    m = re.search(r'<section class="zpm-cat-sections"[^>]*>.*?</section>', html, re.S)
    block = m.group(0) if m else ""
    cards = []
    for card in re.findall(r'<a class="zpm-cat-card".*?</a>', block, re.S):
        title_m = re.search(r'zpm-cat-card__title">([^<]+)</div>', card)
        img_m = re.search(r'<img[^>]+src="([^"]+)"', card)
        href_m = re.search(r'href="([^"]+)"', card)
        if title_m:
            cards.append(
                {
                    "name": title_m.group(1).strip(),
                    "img": img_m.group(1) if img_m else None,
                    "href": href_m.group(1) if href_m else None,
                }
            )
    return cards


def ftp_download(remote: str) -> bytes:
    ftp = ftplib.FTP(HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    buf = io.BytesIO()
    ftp.retrbinary("RETR " + remote, buf.write)
    ftp.quit()
    return buf.getvalue()


def main():
    home = fetch("/")
    cards = homepage_cat_cards(home)
    print("=== HOMEPAGE CAT SECTION (BEFORE) ===")
    print("card_count:", len(cards))
    for c in cards:
        print(c)
    print("PHP errors:", bool(re.search(r"(Notice:|Warning:|Fatal error:)", home)))

    print("\n=== LIVE FTP CAPTURE ===")
    for remote in REMOTE_FILES:
        data = ftp_download(remote)
        sha = hashlib.sha256(data).hexdigest()
        safe = remote.replace("/", "__")
        out = BACKUP / f"pre-m9.7e-live__{safe}"
        out.write_bytes(data)
        print(f"{remote}: {len(data)} bytes sha256={sha[:16]}... -> {out.name}")


if __name__ == "__main__":
    main()
