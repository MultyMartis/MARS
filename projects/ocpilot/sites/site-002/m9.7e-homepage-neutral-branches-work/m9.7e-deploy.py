#!/usr/bin/env python3
"""BZPM M9.7E — deploy homepage neutral branch cards (TEST only)."""
import ftplib
import hashlib
import io
import json
from datetime import datetime, timezone
from pathlib import Path

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

BASE = Path(__file__).resolve().parent
PATCH = BASE / "patch"
BACKUP_DIR = BASE / "backups"
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

REMOTE_FILES = [
    "catalog/controller/common/home.php",
    "system/library/zpm/category_visibility.php",
]


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ftp_connect():
    ftp = ftplib.FTP(HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ensure_remote_dirs(ftp, remote_path: str):
    parts = remote_path.split("/")[:-1]
    if not parts:
        return
    ftp.cwd("/")
    for part in parts:
        try:
            ftp.cwd(part)
        except ftplib.error_perm:
            ftp.mkd(part)
            ftp.cwd(part)
    ftp.cwd("/")


def ftp_download(remote_path: str) -> bytes:
    ftp = ftp_connect()
    buf = io.BytesIO()
    ftp.retrbinary("RETR " + remote_path, buf.write)
    ftp.quit()
    return buf.getvalue()


def ftp_upload(remote_path: str, data_bytes: bytes):
    ftp = ftp_connect()
    ensure_remote_dirs(ftp, remote_path)
    bio = io.BytesIO(data_bytes)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def ftp_clear_twig_cache():
    cleared = []
    errors = []
    try:
        ftp = ftp_connect()
        ftp.cwd("/system/storage/cache/template")
        entries = []
        ftp.retrlines("LIST", entries.append)
        for line in entries:
            parts = line.split(None, 8)
            if len(parts) < 9:
                continue
            name = parts[8]
            if name in (".", "..", "index.html"):
                continue
            if line.startswith("d"):
                continue
            try:
                ftp.delete(name)
                cleared.append(name)
            except ftplib.error_perm as e:
                errors.append(f"{name}: {e}")
        ftp.quit()
    except Exception as e:
        errors.append(str(e))
    return cleared, errors


def main():
    pre_backup = []
    deployed = []

    for rel in REMOTE_FILES:
        local = PATCH / rel.replace("/", "\\") if "\\" in str(PATCH) else PATCH / Path(*rel.split("/"))
        local = PATCH / Path(*rel.split("/"))
        if not local.exists():
            raise FileNotFoundError(local)

        live = ftp_download(rel)
        safe = rel.replace("/", "__")
        pre_path = BACKUP_DIR / f"pre-deploy-{STAMP}__{safe}"
        pre_path.write_bytes(live)
        pre_backup.append({"remote": rel, "local_backup": str(pre_path), "sha256": sha256_hex(live), "bytes": len(live)})

        patch_data = local.read_bytes()
        ftp_upload(rel, patch_data)
        deployed.append({"remote": rel, "local": str(local), "sha256": sha256_hex(patch_data), "bytes": len(patch_data)})

    twig_cleared, twig_errors = ftp_clear_twig_cache()

    manifest = {
        "task": "M9.7E homepage neutral branch cards",
        "environment": "TEST",
        "test_url": "https://zpm.new-site.space/",
        "deployed_at_utc": STAMP,
        "pre_backup": pre_backup,
        "files": deployed,
        "twig_cache_cleared": twig_cleared,
        "twig_cache_errors": twig_errors,
    }

    out = BACKUP_DIR / f"m9.7e-deploy-{STAMP}.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    print("Deployed files:", len(deployed))
    print("Twig cache cleared:", len(twig_cleared))
    if twig_errors:
        print("Twig cache errors:", twig_errors)
    print("Manifest:", out)


if __name__ == "__main__":
    main()
