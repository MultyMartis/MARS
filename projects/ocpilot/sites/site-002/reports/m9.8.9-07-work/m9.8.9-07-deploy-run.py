#!/usr/bin/env python3
"""M9.8.9-07 — hide Subcategories filter group (UI only): capture, backup, patch, deploy."""
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
REMOTE_PATH = "catalog/view/theme/default/template/sections/filterssidebar.twig"

ROOT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
WORK_DIR = ROOT / "reports" / "m9.8.9-07-work"
CAPTURE_DIR = WORK_DIR / "live-capture"
CAPTURE_PATH = CAPTURE_DIR / "catalog__view__theme__default__template__sections__filterssidebar.twig"
BACKUP_PATH = ROOT / "backups" / "filterssidebar.twig.pre-m9.8.9-07-hide-subcategories.bak"
PATCHED_PATH = WORK_DIR / "catalog__view__theme__default__template__sections__filterssidebar.twig.patched"

OLD_IF = "    <!-- SUBCATEGORIES -->\n     {% if filter_subcategories %}"
NEW_IF = (
    "    {# M9.8.9-07: Subcategories filter group hidden (UI only). "
    "Restore: replace `false and filter_subcategories` with `filter_subcategories`. #}\n"
    "    <!-- SUBCATEGORIES -->\n"
    "     {% if false and filter_subcategories %}"
)


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


def apply_patch(content: str) -> str:
    if OLD_IF not in content:
        raise RuntimeError("Expected SUBCATEGORIES `{% if filter_subcategories %}` anchor not found")
    if "false and filter_subcategories" in content:
        raise RuntimeError("Patch already applied (false and filter_subcategories present)")
    return content.replace(OLD_IF, NEW_IF, 1)


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
    ROOT.joinpath("backups").mkdir(parents=True, exist_ok=True)

    live_raw = ftp_download(REMOTE_PATH)
    live_sha = sha256_hex(live_raw)
    CAPTURE_PATH.write_bytes(live_raw)
    BACKUP_PATH.write_bytes(live_raw)

    live_text = live_raw.decode("utf-8")
    patched_text = apply_patch(live_text)
    patched_raw = patched_text.encode("utf-8")
    patched_sha = sha256_hex(patched_raw)
    PATCHED_PATH.write_bytes(patched_raw)

    manifest_pre = {
        "task": "M9.8.9-07",
        "authority": "SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01",
        "stamp": stamp,
        "remote_path": REMOTE_PATH,
        "phase": "pre-deploy",
        "capture": str(CAPTURE_PATH),
        "backup": str(BACKUP_PATH),
        "sha256": live_sha,
        "size": len(live_raw),
        "patch": {
            "type": "ui-removal",
            "file": "filterssidebar.twig",
            "change": "SUBCATEGORIES group: `{% if filter_subcategories %}` → `{% if false and filter_subcategories %}`",
        },
    }
    manifest_pre_path = WORK_DIR / f"manifest-pre-{stamp}.json"
    manifest_pre_path.write_text(
        json.dumps(manifest_pre, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    ftp_upload(REMOTE_PATH, patched_raw)
    cache_cleared = clear_twig_cache()

    verify_raw = ftp_download(REMOTE_PATH)
    verify_sha = sha256_hex(verify_raw)

    manifest_post = {
        **manifest_pre,
        "phase": "post-deploy",
        "patched_local": str(PATCHED_PATH),
        "patched_sha256": patched_sha,
        "verify_sha256": verify_sha,
        "deploy_ok": verify_sha == patched_sha,
        "twig_cache_cleared": cache_cleared,
    }
    manifest_post_path = WORK_DIR / f"manifest-post-{stamp}.json"
    manifest_post_path.write_text(
        json.dumps(manifest_post, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(json.dumps(manifest_post, indent=2, ensure_ascii=False))
    if not manifest_post["deploy_ok"]:
        raise SystemExit("Deploy verification failed: live SHA != patched SHA")


if __name__ == "__main__":
    main()
