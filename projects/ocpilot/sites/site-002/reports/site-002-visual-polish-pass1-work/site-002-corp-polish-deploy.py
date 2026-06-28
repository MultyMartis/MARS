#!/usr/bin/env python3
"""SITE-002 Corporate Pages Visual Polish Pass 1 — deploy style.css to TEST."""
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
STYLE_LOCAL = WORK / "style.css"
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


def ftp_upload(remote_path: str, data: bytes) -> None:
    ftp = ftp_connect()
    ftp.login(FTP_USER, FTP_PASS)
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def http_get(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "SITE-002-polish-pass1/1.0"})
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return resp.status, body
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def main() -> None:
    css = STYLE_LOCAL.read_bytes()
    post_hash = sha256_hex(css)
    ftp_upload(REMOTE, css)

    qa: dict = {"urls": {}, "css_marker": False}
    for url in CORP_URLS:
        status, body = http_get(url)
        qa["urls"][url] = {"http_status": status, "ok": status == 200}

    _, css_live = http_get("https://zpm.new-site.space/assets/css/style.css")
    qa["css_marker"] = "Corporate Pages Visual Polish Pass 1" in css_live
    qa["live_css_has_polish"] = qa["css_marker"]
    qa["all_http_ok"] = all(v["ok"] for v in qa["urls"].values())

    manifest_path = WORK / "preflight-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["timestamp"] = datetime.now(timezone.utc).isoformat()
    manifest["files"]["assets/css/style.css"]["post_sha256"] = post_hash
    manifest["files"]["assets/css/style.css"]["post_bytes"] = len(css)
    manifest["deploy"] = {"remote": REMOTE, "qa": qa}
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    deploy_manifest = {
        "pass": "site-002-corp-visual-polish-pass1",
        "timestamp": manifest["timestamp"],
        "remote": REMOTE,
        "post_sha256": post_hash,
        "post_bytes": len(css),
        "qa": qa,
    }
    (WORK / "deploy-manifest.json").write_text(
        json.dumps(deploy_manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(deploy_manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
