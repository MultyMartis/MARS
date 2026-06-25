#!/usr/bin/env python3
"""SITE-002 M9.13 About Company — restore to pre-redesign via point rollback backups."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
import ssl
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
BACKUP_DIR = ROOT / "backups"
WORK_DIR = ROOT / "reports" / "m9.13-restore-work"
CAPTURE_DIR = WORK_DIR / "pre-restore-capture"
LIVE_URL = "https://zpm.new-site.space/about"

M913_SECTIONS = (
    "zpm-about-hero",
    "zpm-about-company",
    "zpm-about-advantages",
    "zpm-about-certs",
    "zpm-about-geo",
    "zpm-about-cta",
)

RESTORE_ITEMS = [
    {
        "remote": "catalog/view/theme/default/template/information/about.twig",
        "backup": BACKUP_DIR / "about.twig.pre-m9.13-about-redesign.bak",
        "capture_name": "about.twig",
    },
    {
        "remote": "catalog/controller/information/about.php",
        "backup": BACKUP_DIR / "about.php.pre-m9.13-about-redesign.bak",
        "capture_name": "about.php",
    },
    {
        "remote": "assets/css/style.css",
        "backup": BACKUP_DIR / "style.css.pre-m9.13-about-redesign.bak",
        "capture_name": "style.css",
    },
    {
        "remote": "assets/img/about-page-img.jpg",
        "backup": BACKUP_DIR / "about-page-img.jpg.pre-m9.13-about-polish-v1.bak",
        "capture_name": "about-page-img.jpg",
        "note": "No pre-m9.13-about-redesign.bak for image; redesign did not replace file — polish backup equals pre-redesign bytes.",
    },
]

REMOVE_REMOTE = "assets/img/about-logistics.jpg"


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


def ftp_delete(remote_path: str) -> bool:
    ftp = ftp_connect()
    try:
        ftp.delete(remote_path)
        ftp.quit()
        return True
    except ftplib.error_perm:
        ftp.quit()
        return False


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


def verify_backups() -> dict:
    out: dict = {"ok": True, "files": {}}
    for item in RESTORE_ITEMS:
        bak = item["backup"]
        entry = {"path": str(bak), "exists": bak.is_file()}
        if entry["exists"]:
            data = bak.read_bytes()
            entry["sha256"] = sha256_hex(data)
            entry["bytes"] = len(data)
        else:
            out["ok"] = False
        if item.get("note"):
            entry["note"] = item["note"]
        out["files"][item["remote"]] = entry
    return out


def capture_live() -> dict:
    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
    captures: dict = {"files": {}, "images": {}}

    for item in RESTORE_ITEMS:
        remote = item["remote"]
        name = item["capture_name"]
        try:
            live = ftp_download(remote)
            path = CAPTURE_DIR / name
            path.write_bytes(live)
            captures["files" if name.endswith((".twig", ".php", ".css")) else "images"][remote] = {
                "local": str(path),
                "sha256": sha256_hex(live),
                "bytes": len(live),
            }
        except ftplib.error_perm as exc:
            captures.setdefault("errors", {})[remote] = str(exc)

    for extra in ("about-logistics.jpg",):
        remote = f"assets/img/{extra}"
        try:
            live = ftp_download(remote)
            path = CAPTURE_DIR / extra
            path.write_bytes(live)
            captures["images"][remote] = {
                "local": str(path),
                "sha256": sha256_hex(live),
                "bytes": len(live),
            }
        except ftplib.error_perm:
            captures.setdefault("missing", []).append(remote)

    return captures


def restore_files() -> dict:
    restored: dict = {"files": {}}
    for item in RESTORE_ITEMS:
        remote = item["remote"]
        backup = item["backup"]
        data = backup.read_bytes()
        ftp_upload(remote, data)
        restored["files"][remote] = {
            "backup": str(backup),
            "sha256": sha256_hex(data),
            "bytes": len(data),
        }
    return restored


def qa_check() -> dict:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        LIVE_URL,
        headers={"Cookie": "beget=begetok", "User-Agent": "MARS-M9.13-restore"},
    )
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
            html = resp.read().decode("utf-8", "replace")
            http_status = resp.status
    except urllib.error.HTTPError as exc:
        html = exc.read().decode("utf-8", "replace") if exc.fp else ""
        http_status = exc.code

    qa_path = WORK_DIR / "qa-about-restored.html"
    qa_path.write_text(html, encoding="utf-8")

    checks = {
        "http_200": http_status == 200,
        "http_status": http_status,
        "old_main_wrap": "about-page--main-wrap" in html,
        "old_video_block": "about-page-video" in html,
        "old_geo_image": "geo-web.png" in html,
        "old_dealer_block": "blockdealersform" in html or "zpm-dealers" in html,
        "old_cert_slider": "js-certificates-slider" in html or "aboutcertificates" in html,
    }
    for sec in M913_SECTIONS:
        checks[f"no_{sec}"] = sec not in html
    checks["no_m913_sections"] = all(not sec in html for sec in M913_SECTIONS)
    checks["no_about_logistics_img"] = "about-logistics.jpg" not in html
    checks["all_pass"] = all(
        v
        for k, v in checks.items()
        if k not in ("http_status",) and isinstance(v, bool)
    )
    return checks


def main() -> None:
    manifest: dict = {
        "pass": "m9.13-about-restore-to-pre-redesign",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "live_url": LIVE_URL,
    }

    manifest["backup_verification"] = verify_backups()
    if not manifest["backup_verification"]["ok"]:
        raise SystemExit("Missing required backup files")

    manifest["pre_restore_capture"] = capture_live()
    manifest["restored"] = restore_files()

    removed = False
    try:
        ftp_download(REMOVE_REMOTE)
        removed = ftp_delete(REMOVE_REMOTE)
    except ftplib.error_perm:
        removed = False
    manifest["removed"] = {
        "remote": REMOVE_REMOTE,
        "deleted": removed,
        "reason": "Introduced by M9.13 polish only; not in pre-redesign page",
    }

    manifest["twig_cache_cleared"] = clear_twig_cache()
    manifest["qa"] = qa_check()

    out = WORK_DIR / "restore-manifest.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
