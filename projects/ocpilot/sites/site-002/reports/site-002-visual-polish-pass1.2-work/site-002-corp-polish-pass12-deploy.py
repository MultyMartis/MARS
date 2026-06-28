#!/usr/bin/env python3
"""SITE-002 Corporate Pages Visual Polish Pass 1.2 — backup, deploy, QA."""
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

ROOT = Path(r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002")
WORK = ROOT / "reports" / "site-002-visual-polish-pass1.2-work"
BACKUP = ROOT / "backups"

CSS_MARKER = "Corporate Pages Visual Polish Pass 1.2"
BACKUP_SUFFIX = "pre-site-002-corp-visual-polish-pass1.2.bak"

CORP_URLS = [
    "https://zpm.new-site.space/",
    "https://zpm.new-site.space/delivery",
    "https://zpm.new-site.space/payment-methods",
    "https://zpm.new-site.space/guarantee",
    "https://zpm.new-site.space/dealers",
    "https://zpm.new-site.space/custom-equipment",
]

DEPLOY_FILES = [
    {
        "remote": "assets/css/style.css",
        "local": WORK / "style.css",
        "backup": BACKUP / f"style.css.{BACKUP_SUFFIX}",
    },
]


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ftp_connect() -> ftplib.FTP:
    return ftplib.FTP(FTP_HOST, timeout=180)


def ftp_download(remote_path: str) -> bytes | None:
    ftp = ftp_connect()
    ftp.login(FTP_USER, FTP_PASS)
    bio = io.BytesIO()
    try:
        ftp.retrbinary("RETR " + remote_path, bio.write)
        ftp.quit()
        return bio.getvalue()
    except ftplib.error_perm:
        ftp.quit()
        return None


def ftp_upload(remote_path: str, data: bytes) -> None:
    ftp = ftp_connect()
    ftp.login(FTP_USER, FTP_PASS)
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def clear_twig_cache() -> list[str]:
    cleared: list[str] = []
    try:
        ftp = ftp_connect()
        ftp.login(FTP_USER, FTP_PASS)
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


def http_get(url: str) -> tuple[int, str]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "SITE-002-polish-pass1.2/1.0", "Cookie": "beget=begetok"},
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def main() -> None:
    ts = datetime.now(timezone.utc).isoformat()
    manifest: dict = {
        "pass": "site-002-corp-visual-polish-pass1.2",
        "timestamp": ts,
        "operator_beget_backup": "CONFIRMED",
        "checkpoint_commit": "a838210f",
        "files": {},
    }

    for item in DEPLOY_FILES:
        remote = item["remote"]
        local_path: Path = item["local"]
        backup_path: Path = item["backup"]
        live = ftp_download(remote)
        entry = {"remote": remote, "pre_exists": live is not None}
        if live is not None:
            backup_path.write_bytes(live)
            entry["pre_sha256"] = sha256_hex(live)
            entry["pre_bytes"] = len(live)
        else:
            entry["pre_sha256"] = None
            entry["pre_bytes"] = 0
            entry["is_new_remote"] = True

        post = local_path.read_bytes()
        ftp_upload(remote, post)
        entry["post_sha256"] = sha256_hex(post)
        entry["post_bytes"] = len(post)
        manifest["files"][remote] = entry

    cache_cleared = clear_twig_cache()
    manifest["twig_cache_cleared"] = cache_cleared

    qa: dict = {"urls": {}, "css_marker": False, "page_intro_description_removed": {}}
    corp_paths = {
        "/delivery": "delivery",
        "/payment-methods": "payment",
        "/guarantee": "guarantee",
        "/dealers": "dealers",
        "/custom-equipment": "custom",
    }
    for url in CORP_URLS:
        status, body = http_get(url)
        qa["urls"][url] = {"http_status": status, "ok": status == 200}
        for path, key in corp_paths.items():
            if path in url:
                qa["page_intro_description_removed"][key] = "page-intro__description" not in body
                qa[f"has_corp_page_lead_{key}"] = "zpm-corp-page-lead" in body

    _, css_live = http_get("https://zpm.new-site.space/assets/css/style.css")
    qa["css_marker"] = CSS_MARKER in css_live
    qa["pass11_marker_still_present"] = "Corporate Pages Visual Polish Pass 1.1" in css_live
    qa["all_http_ok"] = all(v["ok"] for v in qa["urls"].values())
    qa["all_no_page_intro_description"] = all(qa["page_intro_description_removed"].values())

    manifest["deploy"] = {"qa": qa}
    (WORK / "preflight-manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (WORK / "deploy-manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
