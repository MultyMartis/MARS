#!/usr/bin/env python3
"""SITE-002 M9.13 About Company redesign — backup, deploy, verify, QA capture."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
import re
import ssl
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
WORK_DIR = ROOT / "reports" / "m9.13-work"
BACKUP_DIR = ROOT / "backups"
QA_DIR = ROOT / "qa"

CSS_MARKER = "M9.13 — About Company page — compact redesign"
LIVE_URL = "https://zpm.new-site.space/about"

DEPLOY_FILES = [
    {
        "remote": "catalog/view/theme/default/template/information/about.twig",
        "local": WORK_DIR / "about.twig",
        "backup": BACKUP_DIR / "about.twig.pre-m9.13-about-redesign.bak",
    },
    {
        "remote": "catalog/controller/information/about.php",
        "local": WORK_DIR / "about.php",
        "backup": BACKUP_DIR / "about.php.pre-m9.13-about-redesign.bak",
    },
    {
        "remote": "assets/css/style.css",
        "local": None,
        "backup": BACKUP_DIR / "style.css.pre-m9.13-about-redesign.bak",
        "css_append": WORK_DIR / "m9.13-about-page.css",
    },
]


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ftp_connect() -> ftplib.FTP:
    ftp = ftplib.FTP(FTP_HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_download(remote_path: str) -> bytes:
    ftp = ftp_connect()
    bio = io.BytesIO()
    ftp.retrbinary("RETR " + remote_path, bio.write)
    ftp.quit()
    return bio.getvalue()


def ftp_upload(remote_path: str, data: bytes) -> None:
    ftp = ftp_connect()
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def clear_twig_cache() -> list[str]:
    cleared: list[str] = []
    try:
        ftp = ftp_connect()
        try:
            ftp.cwd("system/storage/cache/template")
            for name in ftp.nlst():
                if name in (".", ".."):
                    continue
                try:
                    ftp.delete(name)
                    cleared.append(name)
                except ftplib.error_perm:
                    pass
        except ftplib.error_perm:
            pass
        ftp.quit()
    except Exception:
        pass
    return cleared


def patch_style_css(live_text: str, append_path: Path) -> str:
    append_block = append_path.read_text(encoding="utf-8")
    marker_line = f"/* ==========================================================================\n   {CSS_MARKER}"
    if CSS_MARKER in live_text:
        before, _sep, _after = live_text.partition(marker_line)
        return before.rstrip() + "\n\n" + append_block.strip() + "\n"
    return live_text.rstrip() + "\n\n" + append_block.strip() + "\n"


def qa_capture() -> dict:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        LIVE_URL,
        headers={"Cookie": "beget=begetok", "User-Agent": "MARS-M9.13"},
    )
    html = urllib.request.urlopen(req, context=ctx, timeout=60).read().decode("utf-8", "replace")
    qa_path = WORK_DIR / "qa-about-redesign.html"
    qa_path.write_text(html, encoding="utf-8")
    QA_DIR.mkdir(parents=True, exist_ok=True)
    (QA_DIR / "m9.13-about-desktop.html").write_text(html, encoding="utf-8")

    checks = {
        "http_ok": True,
        "has_zpm_about_page": "zpm-about-page" in html,
        "has_hero": "zpm-about-hero" in html,
        "has_proof_cards": "zpm-about-proof-card" in html,
        "has_advantages": "zpm-about-advantages" in html,
        "has_certs_podium": "zpm-about-certs" in html and "sert-base.jpg" in html,
        "has_fancybox_cert": 'data-fancybox="certificates-about"' in html,
        "has_geo": "zpm-about-geo" in html,
        "has_cta": "zpm-about-cta" in html,
        "has_2010": "2010" in html,
        "no_5x_metric": "5&times;" not in html and "5×" not in html,
        "no_dealer_block": "zpm-dealers" not in html and "Дилерам" not in html,
        "no_video_block": "about-page-video" not in html,
        "no_cert_slider": "js-certificates-slider" not in html,
        "cert_link": 'href="/our-certification"' in html,
        "delivery_link": 'href="/delivery"' in html,
        "form_dialog_7": 'name="dialog" value="7"' in html,
        "proof_production": "Собственное производство" in html,
        "proof_docs": "Документы для" in html and "закупки" in html,
        "proof_made_in_russia": "Сделано в" in html and "России" in html,
    }
    checks["all_pass"] = all(checks.values())
    return checks


def main() -> None:
    manifest: dict = {
        "pass": "m9.13-about-redesign",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "files": {},
    }

    for item in DEPLOY_FILES:
        remote = item["remote"]
        live = ftp_download(remote)
        item["backup"].write_bytes(live)
        manifest["files"][remote] = {
            "pre_sha256": sha256_hex(live),
            "pre_bytes": len(live),
            "backup": str(item["backup"]),
        }

        if item.get("local"):
            upload_data = item["local"].read_bytes()
        elif item.get("css_append"):
            live_text = live.decode("utf-8", errors="replace")
            patched = patch_style_css(live_text, item["css_append"])
            upload_data = patched.encode("utf-8")
        else:
            upload_data = live

        ftp_upload(remote, upload_data)
        manifest["files"][remote]["post_sha256"] = sha256_hex(upload_data)
        manifest["files"][remote]["post_bytes"] = len(upload_data)

    cleared = clear_twig_cache()
    manifest["twig_cache_cleared"] = cleared

    qa = qa_capture()
    manifest["qa"] = qa

    out = WORK_DIR / "deploy-manifest.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
