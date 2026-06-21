#!/usr/bin/env python3
"""M9.8.9-04A — filter scroll offset tuning: reduce to ~15px gap."""
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
REMOTE_PATH = "assets/js/main.js"

ROOT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
WORK_DIR = ROOT / "reports" / "m9.8.9-04a-work"
CAPTURE_DIR = WORK_DIR / "live-capture"
CAPTURE_PATH = CAPTURE_DIR / "assets__js__main.js"
BACKUP_PATH = ROOT / "backups" / "main.js.pre-m9.8.9-04a-filter-scroll-offset-tuning.bak"
PATCHED_PATH = WORK_DIR / "assets__js__main.js.patched"

OLD_OFFSET_LINE = "    var offset = getPageScrollOffset();"
NEW_OFFSET_LINE = "    var offset = 15;"

SCROLL_OFFSET_PATTERN = re.compile(
    r"(function scrollToCategorySection\(\) \{[\s\S]*?)"
    r"var offset = getPageScrollOffset\(\);"
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


def apply_patch(content: str) -> str:
    if "function scrollToCategorySection()" not in content:
        raise RuntimeError("scrollToCategorySection() not found — M9.8.9-04 prerequisite missing")
    if NEW_OFFSET_LINE in content:
        raise RuntimeError("Patch already applied (offset = 15 present)")
    if OLD_OFFSET_LINE not in content:
        raise RuntimeError("Expected offset line not found in scrollToCategorySection()")
    return content.replace(OLD_OFFSET_LINE, NEW_OFFSET_LINE, 1)


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
        "task": "M9.8.9-04A",
        "authority": "SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01",
        "stamp": stamp,
        "remote_path": REMOTE_PATH,
        "phase": "pre-deploy",
        "capture": str(CAPTURE_PATH),
        "backup": str(BACKUP_PATH),
        "sha256": live_sha,
        "size": len(live_raw),
        "patch": {
            "type": "js-scroll-offset-tuning",
            "file": "main.js",
            "change": "scrollToCategorySection: offset getPageScrollOffset() -> 15px",
            "previous_offset": "getPageScrollOffset() (~131 desktop / ~90 mobile)",
            "new_offset": "15px fixed",
        },
    }
    manifest_pre_path = WORK_DIR / f"manifest-pre-{stamp}.json"
    manifest_pre_path.write_text(
        json.dumps(manifest_pre, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    ftp_upload(REMOTE_PATH, patched_raw)

    verify_raw = ftp_download(REMOTE_PATH)
    verify_sha = sha256_hex(verify_raw)

    manifest_post = {
        **manifest_pre,
        "phase": "post-deploy",
        "patched_local": str(PATCHED_PATH),
        "patched_sha256": patched_sha,
        "verify_sha256": verify_sha,
        "deploy_ok": verify_sha == patched_sha,
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
