#!/usr/bin/env python3
"""SITE-002 — delivery summary restyle: backup, deploy, QA."""
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
WORK = ROOT / "reports" / "delivery-summary-work"
BACKUP = ROOT / "backups"
BACKUP_SUFFIX = "pre-site-002-delivery-summary-01.bak"
CSS_MARKER = "SITE-002 — Delivery summary → commercial trust services reuse"
BASE = "https://zpm.new-site.space"

REMOTE_TWIG = "catalog/view/theme/default/template/information/delivery.twig"
REMOTE_CSS = "assets/css/style.css"
REMOTE_TOUCHED = [REMOTE_TWIG, REMOTE_CSS]
PAGE_URL = f"{BASE}/delivery"


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
    append_block = (WORK / "zpm-delivery-summary.css").read_text(encoding="utf-8")
    marker_line = f"/* ==========================================================================\n   {CSS_MARKER}"
    if CSS_MARKER in live_text:
        before, _sep, _after = live_text.partition(marker_line)
        return before.rstrip() + "\n\n" + append_block.strip() + "\n"
    return live_text.rstrip() + "\n\n" + append_block.strip() + "\n"


def http_get(url: str) -> tuple[int, str]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "SITE-002-delivery-summary/1.0", "Cookie": "beget=begetok"},
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
        "has_delivery_summary_wrapper": "zpm-delivery-summary" in html,
        "has_commercial_trust_services": "zpm-commercial-trust__services" in html,
        "has_service_cards": html.count("zpm-commercial-trust__service") >= 4,
        "has_service_icons": "zpm-commercial-trust__service-icon" in html,
        "no_legacy_summary_item": "zpm-delivery-summary__item" not in html,
        "no_legacy_summary_label": "zpm-delivery-summary__label" not in html,
        "has_geography_icon": "fad fa-map-marked-alt" in html,
        "has_warehouse_icon": "fad fa-warehouse" in html,
        "has_shipping_icon": "fad fa-shipping-fast" in html,
        "has_headset_icon": "fad fa-user-headset" in html,
        "content_geography": "Поставки по" in html,
        "content_shipment_points": "Барнаул" in html and "Московской области" in html,
        "content_methods": "Самовывоз" in html and "транспортная компания" in html,
        "content_support": "Менеджер заказа" in html,
    }
    checks["all_pass"] = all(checks.values())
    return {"url": url, "status": status, "checks": checks}


def preflight_only() -> dict:
    WORK.mkdir(parents=True, exist_ok=True)
    BACKUP.mkdir(parents=True, exist_ok=True)
    preflight: dict = {}
    for remote in REMOTE_TOUCHED:
        live = ftp_download(remote)
        preflight[remote] = {
            "exists": live is not None,
            "pre_sha256": sha256_hex(live) if live else None,
            "pre_bytes": len(live) if live else 0,
        }
        if live is not None:
            backup_name(remote).write_bytes(live)
    (WORK / "preflight-manifest.json").write_text(
        json.dumps(preflight, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return preflight


def main() -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    BACKUP.mkdir(parents=True, exist_ok=True)

    manifest: dict = {
        "pass": "site-002-delivery-summary-01",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "branch": "mars/canonical-post-recovery",
        "checkpoint_pre": "f7d984c89c80a81d8e11a3c38e03055a9e02b586",
        "files": {},
        "sha256": {},
    }

    preflight = preflight_only()
    manifest["preflight"] = preflight

    for remote in REMOTE_TOUCHED:
        live = backup_name(remote).read_bytes()
        if not live:
            raise RuntimeError(f"Missing backup for: {remote}")

    twig_local = WORK / "catalog__view__theme__default__template__information__delivery.twig"
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
