#!/usr/bin/env python3
"""M9.8.9-03 — live FTP capture (read-only)."""
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
WORK_DIR = ROOT / "reports" / "m9.8.9-03-work"
CAPTURE_DIR = WORK_DIR / "live-capture"

REMOTE_FILES = {
    "certificates.twig": "catalog/view/theme/default/template/sections/certificates.twig",
    "blockdealersform.twig": "catalog/view/theme/default/template/sections/blockdealersform.twig",
    "category.twig": "catalog/view/theme/default/template/product/category.twig",
    "category.php": "catalog/controller/product/category.php",
    "style.css": "assets/css/style.css",
    "main.js": "assets/js/main.js",
}


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


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)

    manifest: dict = {
        "task": "M9.8.9-03",
        "authority": "SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01",
        "phase": "pre-deploy-capture",
        "stamp": stamp,
        "files": [],
    }

    for local_name, remote in REMOTE_FILES.items():
        raw = ftp_download(remote)
        path = CAPTURE_DIR / local_name
        path.write_bytes(raw)
        manifest["files"].append(
            {
                "remote_path": remote,
                "local": str(path),
                "sha256": sha256_hex(raw),
                "size": len(raw),
            }
        )
        print(f"OK {remote} ({len(raw)} bytes)")

    manifest_path = WORK_DIR / f"manifest-capture-{stamp}.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
