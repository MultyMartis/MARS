#!/usr/bin/env python3
"""SITE-002 — custom OEM proof strip restyle: backup, deploy, QA."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
import re
import ssl
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002")
WORK = ROOT / "reports" / "custom-proof-strip-work"
BACKUP = ROOT / "backups"
BACKUP_SUFFIX = "pre-site-002-custom-proof-strip-01.bak"
CSS_MARKER = "SITE-002 — Custom OEM proof strip → commercial trust services reuse"
BASE = "https://zpm.new-site.space"

REMOTE_TWIG = "catalog/view/theme/default/template/information/custom_equipment.twig"
REMOTE_CSS = "assets/css/style.css"
REMOTE_TOUCHED = [REMOTE_TWIG, REMOTE_CSS]
PAGE_URL = f"{BASE}/custom-equipment"


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def backup_name(remote: str) -> Path:
    safe = remote.replace("/", "__")
    return BACKUP / f"{safe}.{BACKUP_SUFFIX}"


def ftp_connect() -> ftplib.FTP:
    ftp = ftplib.FTP(FTP_HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_download(remote_path: str) -> bytes | None:
    ftp = ftp_connect()
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


def patch_style_css(live_text: str) -> str:
    append_block = (WORK / "zpm-custom-proof-strip.css").read_text(encoding="utf-8")
    marker_line = f"/* ==========================================================================\n   {CSS_MARKER}"
    if CSS_MARKER in live_text:
        before, _sep, _after = live_text.partition(marker_line)
        return before.rstrip() + "\n\n" + append_block.strip() + "\n"
    return live_text.rstrip() + "\n\n" + append_block.strip() + "\n"


def http_get(url: str) -> tuple[int, str]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "SITE-002-custom-proof-strip/1.0", "Cookie": "beget=begetok"},
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", errors="replace")


def qa_page(url: str) -> dict:
    status, html = http_get(url)
    checks = {
        "http_ok": status == 200,
        "has_proof_strip_wrapper": "zpm-custom-oem__proof-strip" in html,
        "has_commercial_trust_services": "zpm-commercial-trust__services" in html,
        "has_service_cards": html.count("zpm-commercial-trust__service") >= 3,
        "has_service_icons": "zpm-commercial-trust__service-icon" in html,
        "no_legacy_proof_item": "zpm-custom-oem__proof-item" not in html,
        "has_production_icon": "fad fa-industry" in html,
        "has_cert_icon": "fad fa-file-certificate" in html,
        "has_catalog_icon": "fad fa-th-large" in html,
        "content_production": "Собственная площадка" in html,
        "content_cert": "Сделано в" in html or "Сделано&nbsp;в" in html,
        "content_catalog": "Серийные модели" in html,
    }
    checks["all_pass"] = all(checks.values())
    return {"url": url, "status": status, "checks": checks}


def main() -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    BACKUP.mkdir(parents=True, exist_ok=True)

    manifest: dict = {
        "pass": "site-002-custom-proof-strip-01",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "branch": "mars/canonical-post-recovery",
        "checkpoint_pre": "ba196a379fd6aa7dc755a774cc10994597e34849",
        "files": {},
        "sha256": {},
    }

    preflight: dict = {}
    for remote in REMOTE_TOUCHED:
        live = ftp_download(remote)
        preflight[remote] = {
            "exists": live is not None,
            "pre_sha256": sha256_hex(live) if live else None,
            "pre_bytes": len(live) if live else 0,
        }
    (WORK / "preflight-manifest.json").write_text(
        json.dumps(preflight, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    manifest["preflight"] = preflight

    for remote in REMOTE_TOUCHED:
        live = ftp_download(remote)
        if live is None:
            raise RuntimeError(f"Missing remote: {remote}")
        backup_name(remote).write_bytes(live)

    twig_local = WORK / "catalog__view__theme__default__template__information__custom_equipment.twig"
    twig_payload = twig_local.read_bytes()
    twig_live = backup_name(REMOTE_TWIG).read_bytes()
    ftp_upload(REMOTE_TWIG, twig_payload)
    manifest["files"][REMOTE_TWIG] = {
        "backup": str(backup_name(REMOTE_TWIG)),
        "pre_sha256": sha256_hex(twig_live),
        "post_sha256": sha256_hex(twig_payload),
        "pre_bytes": len(twig_live),
        "post_bytes": len(twig_payload),
    }
    manifest["sha256"][REMOTE_TWIG] = {
        "pre": manifest["files"][REMOTE_TWIG]["pre_sha256"],
        "post": manifest["files"][REMOTE_TWIG]["post_sha256"],
    }

    css_live = backup_name(REMOTE_CSS).read_bytes()
    css_text = css_live.decode("utf-8", errors="replace")
    css_patched = patch_style_css(css_text)
    css_upload = css_patched.encode("utf-8")
    ftp_upload(REMOTE_CSS, css_upload)
    manifest["files"][REMOTE_CSS] = {
        "backup": str(backup_name(REMOTE_CSS)),
        "pre_sha256": sha256_hex(css_live),
        "post_sha256": sha256_hex(css_upload),
        "pre_bytes": len(css_live),
        "post_bytes": len(css_upload),
    }
    manifest["sha256"][REMOTE_CSS] = {
        "pre": sha256_hex(css_live),
        "post": sha256_hex(css_upload),
    }

    manifest["twig_cache_cleared"] = clear_twig_cache()
    manifest["qa"] = qa_page(PAGE_URL)
    manifest["qa_all_pass"] = manifest["qa"].get("checks", {}).get("all_pass", False)

    (WORK / "deploy-sha256.json").write_text(
        json.dumps(manifest["sha256"], indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (WORK / "deploy-manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
