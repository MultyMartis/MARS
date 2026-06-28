#!/usr/bin/env python3
"""SITE-002 Corporate Pages Visual Polish Pass 1 — rollback style.css on TEST."""
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

ROOT = Path(r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002")
WORK = ROOT / "reports" / "site-002-visual-polish-pass1-work"
BACKUPS = ROOT / "backups"

PRE_PASS1 = BACKUPS / "style.css.pre-site-002-corp-visual-polish-pass1.bak"
REJECTED_BACKUP = BACKUPS / "style.css.rejected-site-002-corp-visual-polish-pass1.bak"
REMOTE = "assets/css/style.css"

CORP_URLS = [
    "https://zpm.new-site.space/",
    "https://zpm.new-site.space/delivery",
    "https://zpm.new-site.space/payment-methods",
    "https://zpm.new-site.space/guarantee",
    "https://zpm.new-site.space/dealers",
    "https://zpm.new-site.space/custom-equipment",
]


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ftp_connect() -> ftplib.FTP:
    return ftplib.FTP(FTP_HOST, timeout=180)


def ftp_download(remote_path: str) -> bytes:
    ftp = ftp_connect()
    ftp.login(FTP_USER, FTP_PASS)
    bio = io.BytesIO()
    ftp.retrbinary("RETR " + remote_path, bio.write)
    ftp.quit()
    return bio.getvalue()


def ftp_upload(remote_path: str, data: bytes) -> None:
    ftp = ftp_connect()
    ftp.login(FTP_USER, FTP_PASS)
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def http_get(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "SITE-002-polish-pass1-rollback/1.0"})
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return resp.status, body
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def main() -> None:
    if not PRE_PASS1.is_file():
        raise SystemExit(f"Missing rollback source: {PRE_PASS1}")

    current_live = ftp_download(REMOTE)
    REJECTED_BACKUP.write_bytes(current_live)
    rejected_sha = sha256_hex(current_live)

    pre_sha = sha256_hex(PRE_PASS1.read_bytes())
    rollback_css = PRE_PASS1.read_bytes()
    rollback_sha = sha256_hex(rollback_css)

    ftp_upload(REMOTE, rollback_css)

    qa: dict = {"urls": {}, "css_marker_absent": False}
    for url in CORP_URLS:
        status, _ = http_get(url)
        qa["urls"][url] = {"http_status": status, "ok": status == 200}

    _, css_live = http_get("https://zpm.new-site.space/assets/css/style.css")
    qa["css_marker_absent"] = "Corporate Pages Visual Polish Pass 1" not in css_live
    qa["live_css_sha256"] = sha256_hex(css_live.encode("utf-8"))
    qa["all_http_ok"] = all(v["ok"] for v in qa["urls"].values())
    qa["rollback_matches_pre_pass1"] = qa["live_css_sha256"] == rollback_sha == pre_sha

    manifest = {
        "pass": "site-002-corp-visual-polish-pass1-rollback",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "branch": "mars/canonical-post-recovery",
        "operator_decision": "REJECTED BY OPERATOR",
        "rollback_reason": "Global padding-top: 0 reset on corporate sections removed vertical rhythm",
        "files": {
            "assets/css/style.css": {
                "rejected_backup": str(REJECTED_BACKUP),
                "rejected_sha256": rejected_sha,
                "rejected_bytes": len(current_live),
                "pre_pass1_backup": str(PRE_PASS1),
                "pre_pass1_sha256": pre_sha,
                "pre_pass1_bytes": PRE_PASS1.stat().st_size,
                "post_rollback_sha256": rollback_sha,
                "post_rollback_bytes": len(rollback_css),
            }
        },
        "deploy": {"remote": REMOTE, "qa": qa},
    }
    out = WORK / "rollback-manifest.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
