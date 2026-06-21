#!/usr/bin/env python3
"""SITE-002 contacts page main redesign — capture, backup, deploy, verify."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
WORK_DIR = ROOT / "reports" / "contacts-redesign-work"
CAPTURE_DIR = WORK_DIR / "live-capture"
BACKUP_DIR = ROOT / "backups"

CSS_MARKER = "Contacts page — main content redesign"

DEPLOY_FILES = [
    {
        "remote": "catalog/view/theme/default/template/information/contact.twig",
        "local": WORK_DIR / "contact.twig",
        "backup": BACKUP_DIR / "contact.twig.pre-contact-redesign.bak",
        "capture_name": "catalog__view__theme__default__template__information__contact.twig",
    },
    {
        "remote": "catalog/view/theme/default/template/sections/blockanyquestionsform.twig",
        "local": WORK_DIR / "blockanyquestionsform.twig",
        "backup": BACKUP_DIR / "blockanyquestionsform.twig.pre-contact-redesign.bak",
        "capture_name": "catalog__view__theme__default__template__sections__blockanyquestionsform.twig",
    },
    {
        "remote": "assets/css/style.css",
        "local": None,
        "backup": BACKUP_DIR / "style.css.pre-contact-redesign.bak",
        "capture_name": "assets__css__style.css",
        "css_append": WORK_DIR / "contacts-redesign.css",
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
    if CSS_MARKER in live_text:
        before, _sep, _after = live_text.partition(f"/* ==========================================================================\n   {CSS_MARKER}")
        return before.rstrip() + "\n\n" + append_block.strip() + "\n"
    return live_text.rstrip() + "\n\n" + append_block.strip() + "\n"


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    manifest_files: list[dict] = []

    for item in DEPLOY_FILES:
        remote = item["remote"]
        live_raw = ftp_download(remote)
        live_sha = sha256_hex(live_raw)
        capture_path = CAPTURE_DIR / item["capture_name"]
        capture_path.write_bytes(live_raw)
        item["backup"].write_bytes(live_raw)

        if item.get("css_append"):
            live_text = live_raw.decode("utf-8")
            patched_text = patch_style_css(live_text, item["css_append"])
            deploy_raw = patched_text.encode("utf-8")
            patched_path = WORK_DIR / "style.css.patched"
            patched_path.write_bytes(deploy_raw)
        else:
            deploy_raw = item["local"].read_bytes()
            patched_path = item["local"]

        deploy_sha = sha256_hex(deploy_raw)
        entry: dict = {
            "remote": remote,
            "capture_local": str(capture_path),
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

    manifest = {
        "task": "SITE-002-CONTACTS-PAGE-MAIN-REDESIGN",
        "authority": "SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01",
        "stamp": stamp,
        "files": manifest_files,
        "twig_cache_cleared": cache_cleared,
        "all_deploy_ok": all(f["deploy_ok"] for f in manifest_files),
    }

    manifest_path = WORK_DIR / f"manifest-post-{stamp}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))

    if not manifest["all_deploy_ok"]:
        raise SystemExit("Deploy verification failed")


if __name__ == "__main__":
    main()
