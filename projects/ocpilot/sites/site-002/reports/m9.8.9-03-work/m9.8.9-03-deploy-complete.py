#!/usr/bin/env python3
"""M9.8.9-03 — complete partial deploy (category.twig + style.css)."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
WORK_DIR = ROOT / "reports" / "m9.8.9-03-work"
CSS_PATCH = (WORK_DIR / "m9.8.9-03-commercial-trust.css").read_text(encoding="utf-8")


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


def clear_twig_cache() -> int:
    cleared = 0
    try:
        ftp = ftp_connect()
        ftp.cwd("system/storage/cache/template")
        for name in ftp.nlst():
            if name in (".", ".."):
                continue
            try:
                ftp.delete(name)
                cleared += 1
            except ftplib.error_perm:
                pass
        ftp.quit()
    except Exception:
        pass
    return cleared


def patch_category_twig(content: str) -> str:
    patched, count = re.subn(
        r"\{\{\s*seotext\s*\}\}\s*\{\{\s*certificates\s*\}\}\s*\{\{\s*blockdealersform\s*\}\}",
        "{{ seotext }}\n{{ blockcommercialtrust }}",
        content,
        count=1,
    )
    if count != 1:
        raise RuntimeError("category.twig patch failed")
    return patched


def patch_style_css(content: str) -> str:
    if "M9.8.9-03 — PLP commercial trust" in content:
        raise RuntimeError("style.css already patched")
    anchor = "/* ==========================================================================\n   DEALERS + FORM"
    idx = content.find(anchor)
    if idx == -1:
        raise RuntimeError("style.css anchor not found")
    return content[:idx] + CSS_PATCH + "\n" + content[idx:]


def deploy_one(remote: str, patch_fn) -> dict:
    live_raw = ftp_download(remote)
    patched = patch_fn(live_raw.decode("utf-8")).encode("utf-8")
    patched_sha = sha256_hex(patched)
    ftp_upload(remote, patched)
    verify_sha = sha256_hex(ftp_download(remote))
    return {
        "remote_path": remote,
        "sha256_patched": patched_sha,
        "verify_sha256": verify_sha,
        "deploy_ok": verify_sha == patched_sha,
    }


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    results = [
        deploy_one(
            "catalog/view/theme/default/template/product/category.twig",
            patch_category_twig,
        ),
        deploy_one("assets/css/style.css", patch_style_css),
    ]
    cache = clear_twig_cache()
    manifest = {
        "task": "M9.8.9-03-complete",
        "stamp": stamp,
        "files": results,
        "twig_cache_cleared_count": cache,
        "all_deploy_ok": all(r["deploy_ok"] for r in results),
    }
    path = WORK_DIR / f"manifest-complete-{stamp}.json"
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    if not manifest["all_deploy_ok"]:
        raise SystemExit("Deploy verification failed")


if __name__ == "__main__":
    main()
