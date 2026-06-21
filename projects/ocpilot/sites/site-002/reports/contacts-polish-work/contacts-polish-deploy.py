#!/usr/bin/env python3
"""SITE-002 contacts page polish v1 — backup, deploy, verify, QA capture."""
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
WORK_DIR = ROOT / "reports" / "contacts-polish-work"
BACKUP_DIR = ROOT / "backups"

CSS_MARKER = "Contacts page — polish v1"
LIVE_URL = "https://zpm.new-site.space/contact/"

DEPLOY_FILES = [
    {
        "remote": "catalog/view/theme/default/template/information/contact.twig",
        "local": WORK_DIR / "contact.twig",
        "backup": BACKUP_DIR / "contact.twig.pre-contact-polish-v1.bak",
    },
    {
        "remote": "catalog/view/theme/default/template/sections/blockanyquestionsform.twig",
        "local": None,
        "backup": BACKUP_DIR / "blockanyquestionsform.twig.pre-contact-polish-v1.bak",
    },
    {
        "remote": "assets/css/style.css",
        "local": None,
        "backup": BACKUP_DIR / "style.css.pre-contact-polish-v1.bak",
        "css_append": WORK_DIR / "contacts-polish.css",
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
        headers={"Cookie": "beget=begetok", "User-Agent": "MARS"},
    )
    html = urllib.request.urlopen(req, context=ctx, timeout=60).read().decode("utf-8", "replace")
    qa_path = WORK_DIR / "qa-contact-polish.html"
    qa_path.write_text(html, encoding="utf-8")

    checks = {
        "http_ok": True,
        "has_contact_cards": "zpm-contact-cards" in html,
        "has_messengers": "zpm-contact-cards--messengers" in html,
        "has_requisites_ogrn": "ОГРН" in html and "1172225049787" in html,
        "has_legal_address": "Юридический адрес" in html,
        "has_actual_address": "Фактический адрес" in html,
        "duotone_map": "fad fa-map-marked-alt" in html,
        "duotone_phone": "fad fa-phone-alt" in html,
        "duotone_email": "fad fa-envelope-open-text" in html,
        "duotone_clock": "fad fa-clock" in html,
        "duotone_industry": "fad fa-industry-alt" in html,
        "duotone_certificate": "fad fa-file-certificate" in html,
        "duotone_badge": "fad fa-badge-check" in html,
        "duotone_truck": "fad fa-truck" in html,
        "duotone_bus": "fad fa-bus-alt" in html,
        "duotone_dolly": "fad fa-dolly-flatbed" in html,
        "fab_telegram": "fab fa-telegram-plane" in html,
        "fab_whatsapp": "fab fa-whatsapp" in html,
        "max_icon": "fad fa-comments-alt" in html,
        "no_fal_contact_icons": not re.search(
            r"zpm-contact-(card|directions)__icon[^>]*>\s*<i class=\"fal ",
            html,
        ),
        "legacy_blocks_absent": "contacts-blocks" not in html,
    }
    checks["all_pass"] = all(checks.values())
    checks["capture_path"] = str(qa_path)
    checks["capture_bytes"] = len(html.encode("utf-8"))
    return checks


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    manifest_files: list[dict] = []

    for item in DEPLOY_FILES:
        remote = item["remote"]
        live_raw = ftp_download(remote)
        live_sha = sha256_hex(live_raw)
        item["backup"].write_bytes(live_raw)

        if item.get("css_append"):
            live_text = live_raw.decode("utf-8")
            patched_text = patch_style_css(live_text, item["css_append"])
            deploy_raw = patched_text.encode("utf-8")
            patched_path = WORK_DIR / "style.css.patched"
            patched_path.write_bytes(deploy_raw)
        elif item.get("local"):
            deploy_raw = item["local"].read_bytes()
            patched_path = item["local"]
        else:
            deploy_raw = live_raw
            patched_path = item["backup"]

        deploy_sha = sha256_hex(deploy_raw)
        entry: dict = {
            "remote": remote,
            "backup_local": str(item["backup"]),
            "patched_local": str(patched_path),
            "sha256_pre": live_sha,
            "sha256_deploy": deploy_sha,
            "size_pre": len(live_raw),
            "size_deploy": len(deploy_raw),
        }

        ftp_upload(remote, deploy_raw)

        verify_raw = ftp_download(remote)
        verify_sha = sha256_hex(verify_raw)
        entry["verify_sha256"] = verify_sha
        entry["deploy_ok"] = verify_sha == deploy_sha
        manifest_files.append(entry)
        print(f"{'OK' if entry['deploy_ok'] else 'FAIL'}: {remote}")

    cache_cleared = clear_twig_cache()
    qa = qa_capture()

    manifest = {
        "task": "SITE-002-CONTACTS-PAGE-POLISH-V1",
        "authority": "SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01",
        "stamp": stamp,
        "files": manifest_files,
        "twig_cache_cleared": cache_cleared,
        "all_deploy_ok": all(f["deploy_ok"] for f in manifest_files),
        "qa": qa,
    }

    manifest_path = WORK_DIR / f"manifest-post-{stamp}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))

    if not manifest["all_deploy_ok"]:
        raise SystemExit("Deploy verification failed")
    if not qa["all_pass"]:
        raise SystemExit("QA checks failed")


if __name__ == "__main__":
    main()
