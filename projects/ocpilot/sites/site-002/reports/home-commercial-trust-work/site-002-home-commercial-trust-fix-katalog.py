#!/usr/bin/env python3
"""Restore katalog blockdealersform; deploy home-only commercial trust partial."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
import re
import ssl
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002")
WORK = ROOT / "reports" / "home-commercial-trust-work"
BACKUP = ROOT / "backups"
LIVE = "https://zpm.new-site.space"


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ftp_connect() -> ftplib.FTP:
    ftp = ftplib.FTP(FTP_HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_upload(remote_path: str, data: bytes) -> None:
    ftp = ftp_connect()
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def clear_twig_cache() -> None:
    try:
        ftp = ftp_connect()
        try:
            ftp.cwd("system/storage/cache/template")
            for name in ftp.nlst():
                if name in (".", ".."):
                    continue
                try:
                    ftp.delete(name)
                except ftplib.error_perm:
                    pass
        except ftplib.error_perm:
            pass
        ftp.quit()
    except Exception:
        pass


def probe(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "SITE-002-home-commercial-trust-fix/1.0"})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
        html = resp.read().decode("utf-8", errors="replace")
    return {
        "url": url,
        "status": resp.status,
        "ok": resp.status == 200,
        "has_commercial_trust": "zpm-commercial-trust" in html,
        "has_old_dealers_grid": "zpm-dealers__grid" in html,
        "has_legacy_dealers_section": bool(re.search(r'<section class="zpm-dealers"', html)),
    }


def main() -> int:
    deploy_items = [
        (
            "catalog/view/theme/default/template/sections/blockdealersform.twig",
            BACKUP
            / "catalog__view__theme__default__template__sections__blockdealersform.twig.pre-home-commercial-trust-01.bak",
        ),
        (
            "catalog/view/theme/default/template/sections/blockcommercialtrust_home.twig",
            WORK / "blockcommercialtrust_home.twig",
        ),
        ("catalog/controller/common/home.php", WORK / "home.php"),
    ]

    manifest = {
        "fix": "katalog-isolation",
        "timestamp_utc": datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S"),
        "files": [],
    }

    for remote, local in deploy_items:
        data = local.read_bytes()
        ftp_upload(remote, data)
        manifest["files"].append(
            {
                "remote": remote,
                "local": str(local),
                "sha256": sha256_hex(data),
                "bytes": len(data),
            }
        )

    clear_twig_cache()
    manifest["qa"] = {
        "home": probe(f"{LIVE}/"),
        "katalog": probe(f"{LIVE}/katalog"),
    }

    out = WORK / f"fix-manifest-{manifest['timestamp_utc']}.json"
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))

    home_ok = manifest["qa"]["home"]["ok"] and manifest["qa"]["home"]["has_commercial_trust"]
    katalog_ok = manifest["qa"]["katalog"]["ok"] and manifest["qa"]["katalog"]["has_legacy_dealers_section"]
    katalog_no_trust = not manifest["qa"]["katalog"]["has_commercial_trust"]
    return 0 if home_ok and katalog_ok and katalog_no_trust else 1


if __name__ == "__main__":
    raise SystemExit(main())
