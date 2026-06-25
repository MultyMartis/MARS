#!/usr/bin/env python3
"""SITE-002 M9.13 About Company polish pass v1 — backup, deploy images + twig + css, QA."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
import ssl
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
WORK_DIR = ROOT / "reports" / "m9.13-work"
POLISH_DIR = ROOT / "reports" / "m9.13-polish-work"
BACKUP_DIR = ROOT / "backups"
QA_DIR = ROOT / "qa"

CSS_MARKER = "M9.13 — About Company page — compact redesign"
LIVE_URL = "https://zpm.new-site.space/about"

DEPLOY_FILES = [
    {
        "remote": "catalog/view/theme/default/template/information/about.twig",
        "local": WORK_DIR / "about.twig",
        "backup": BACKUP_DIR / "about.twig.pre-m9.13-about-polish-v1.bak",
    },
    {
        "remote": "assets/css/style.css",
        "local": None,
        "backup": BACKUP_DIR / "style.css.pre-m9.13-about-polish-v1.bak",
        "css_append": WORK_DIR / "m9.13-about-page.css",
    },
]

IMAGE_FILES = [
    {
        "remote": "assets/img/about-page-img.jpg",
        "local": POLISH_DIR / "assets" / "img" / "about-page-img.jpg",
        "backup": BACKUP_DIR / "about-page-img.jpg.pre-m9.13-about-polish-v1.bak",
        "action": "replace",
    },
    {
        "remote": "assets/img/about-logistics.jpg",
        "local": POLISH_DIR / "assets" / "img" / "about-logistics.jpg",
        "backup": None,
        "action": "new",
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
        headers={"Cookie": "beget=begetok", "User-Agent": "MARS-M9.13-polish-v1"},
    )
    html = urllib.request.urlopen(req, context=ctx, timeout=60).read().decode("utf-8", "replace")
    qa_path = POLISH_DIR / "qa-about-polish.html"
    qa_path.write_text(html, encoding="utf-8")
    QA_DIR.mkdir(parents=True, exist_ok=True)
    (QA_DIR / "m9.13-about-polish-desktop.html").write_text(html, encoding="utf-8")

    checks = {
        "http_ok": True,
        "has_trust_row": "zpm-about-hero__trust" in html,
        "trust_production": "Собственное производство в" in html and "Барнауле" in html,
        "trust_certified": "Сертифицированная продукция" in html,
        "trust_custom": "Изготовление по" in html and "размерам заказчика" in html,
        "has_fad_icons": "fad fa-industry-alt" in html and "fad fa-badge-check" in html,
        "logistics_photo": 'src="/assets/img/about-logistics.jpg"' in html,
        "hero_photo": 'src="/assets/img/about-page-img.jpg"' in html,
        "has_fancybox_cert": 'data-fancybox="certificates-about"' in html,
        "has_cta": "zpm-about-cta" in html,
        "form_dialog_7": 'name="dialog" value="7"' in html,
        "no_adv_trans_geo": 'zpm-about-geo' in html and 'advant/adv-trans-company.png' not in html.split("zpm-about-geo")[1].split("</section>")[0],
    }
    checks["all_pass"] = all(checks.values())
    return checks


def main() -> None:
    manifest: dict = {
        "pass": "m9.13-about-polish-v1",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "files": {},
        "images": {},
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

    for item in IMAGE_FILES:
        remote = item["remote"]
        upload_data = item["local"].read_bytes()
        entry: dict = {
            "action": item["action"],
            "local": str(item["local"]),
            "post_sha256": sha256_hex(upload_data),
            "post_bytes": len(upload_data),
        }
        if item.get("backup"):
            try:
                live = ftp_download(remote)
                item["backup"].write_bytes(live)
                entry["pre_sha256"] = sha256_hex(live)
                entry["pre_bytes"] = len(live)
                entry["backup"] = str(item["backup"])
            except ftplib.error_perm:
                entry["pre_exists"] = False
        ftp_upload(remote, upload_data)
        manifest["images"][remote] = entry

    cleared = clear_twig_cache()
    manifest["twig_cache_cleared"] = cleared

    qa = qa_capture()
    manifest["qa"] = qa

    out = POLISH_DIR / "deploy-manifest.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
