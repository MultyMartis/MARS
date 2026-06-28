#!/usr/bin/env python3
"""SITE-002 — Home page zpm-dealers → zpm-commercial-trust replacement."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
import re
import ssl
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002")
WORK_DIR = ROOT / "reports" / "home-commercial-trust-work"
BACKUP_DIR = ROOT / "backups"
BACKUP_SUFFIX = "pre-home-commercial-trust-01.bak"
LIVE_BASE = "https://zpm.new-site.space"

REMOTE_TWIG = "catalog/view/theme/default/template/sections/blockdealersform.twig"
REMOTE_HOME_PHP = "catalog/controller/common/home.php"
REMOTE_KATALOG_PHP = "catalog/controller/product/katalog.php"

LOCAL_TWIG = WORK_DIR / "blockdealersform.twig"


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
    except Exception as exc:  # noqa: BLE001
        print(f"cache clear warning: {exc}")
    return cleared


def git_preflight() -> dict:
    repo = Path(r"C:\MARS Phenix\AI MARS")
    branch = subprocess.check_output(
        ["git", "branch", "--show-current"], cwd=repo, text=True
    ).strip()
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
    return {"branch": branch, "head": head}


def http_probe(url: str) -> dict:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "SITE-002-home-commercial-trust/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            html = resp.read().decode("utf-8", errors="replace")
            return {
                "url": url,
                "status": resp.status,
                "ok": resp.status == 200,
                "has_commercial_trust": "zpm-commercial-trust" in html and "data-commercial-trust" in html,
                "has_old_dealers_layout": bool(re.search(r'<section class="zpm-dealers"', html)),
                "has_dealers_grid": "zpm-dealers__grid" in html,
                "has_form_dialog7": 'name="dialog" value="7"' in html,
                "has_data_dealers": "data-dealers" in html,
            }
    except urllib.error.HTTPError as exc:
        return {"url": url, "status": exc.code, "ok": False, "error": str(exc)}
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "status": None, "ok": False, "error": str(exc)}


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else "deploy"
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

    git_info = git_preflight()
    print(json.dumps({"git_preflight": git_info}, ensure_ascii=False, indent=2))

    if git_info["branch"] != "mars/canonical-post-recovery":
        print("ERROR: wrong branch", git_info["branch"])
        return 2

    capture_items = [
        {
            "remote": REMOTE_TWIG,
            "backup": BACKUP_DIR / f"catalog__view__theme__default__template__sections__blockdealersform.twig.{BACKUP_SUFFIX}",
            "capture": WORK_DIR / "live-capture" / "blockdealersform.twig.before",
        },
        {
            "remote": REMOTE_HOME_PHP,
            "backup": BACKUP_DIR / f"catalog__controller__common__home.php.{BACKUP_SUFFIX}",
            "capture": WORK_DIR / "live-capture" / "home.php.before",
        },
        {
            "remote": REMOTE_KATALOG_PHP,
            "backup": BACKUP_DIR / f"catalog__controller__product__katalog.php.{BACKUP_SUFFIX}",
            "capture": WORK_DIR / "live-capture" / "katalog.php.before",
        },
    ]

    WORK_DIR.mkdir(parents=True, exist_ok=True)
    (WORK_DIR / "live-capture").mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    manifest: dict = {
        "task": "SITE-002-HOME-COMMERCIAL-TRUST-01",
        "timestamp_utc": ts,
        "git": git_info,
        "backup_suffix": BACKUP_SUFFIX,
        "files": [],
        "katalog_uses_blockdealersform": None,
    }

    for item in capture_items:
        remote = item["remote"]
        data = ftp_download(remote)
        item["backup"].write_bytes(data)
        item["capture"].write_bytes(data)
        manifest["files"].append(
            {
                "remote": remote,
                "action": "backup",
                "sha256_before": sha256_hex(data),
                "bytes_before": len(data),
                "backup_local": str(item["backup"]),
            }
        )

    katalog_src = capture_items[2]["capture"].read_text(encoding="utf-8", errors="replace")
    manifest["katalog_uses_blockdealersform"] = "blockdealersform" in katalog_src

    if mode == "rollback":
        for entry in manifest["files"]:
            backup_path = Path(entry["backup_local"])
            if not backup_path.exists():
                print("missing backup", backup_path)
                return 3
            ftp_upload(entry["remote"], backup_path.read_bytes())
        cleared = clear_twig_cache()
        manifest["rollback"] = {"cleared_cache_files": len(cleared)}
        out = WORK_DIR / f"rollback-manifest-{ts}.json"
        out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        print("rollback complete", out)
        return 0

    if mode != "deploy":
        print("usage: deploy|rollback")
        return 1

    new_twig = LOCAL_TWIG.read_bytes()
    ftp_upload(REMOTE_TWIG, new_twig)
    cleared = clear_twig_cache()

    for entry in manifest["files"]:
        if entry["remote"] == REMOTE_TWIG:
            entry["action"] = "replaced"
            entry["sha256_after"] = sha256_hex(new_twig)
            entry["bytes_after"] = len(new_twig)

    qa = {
        "home": http_probe(f"{LIVE_BASE}/"),
        "katalog": http_probe(f"{LIVE_BASE}/katalog") if manifest["katalog_uses_blockdealersform"] else {"skipped": True},
    }
    manifest["qa"] = qa
    manifest["twig_cache_cleared"] = len(cleared)

    out = WORK_DIR / f"deploy-manifest-{ts}.json"
    sha_out = WORK_DIR / f"deploy-sha256-{ts}.json"
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    sha_out.write_text(
        json.dumps(
            {
                "deployed": {
                    "remote": REMOTE_TWIG,
                    "sha256": sha256_hex(new_twig),
                    "bytes": len(new_twig),
                },
                "backups": [
                    {
                        "remote": f["remote"],
                        "sha256_before": f["sha256_before"],
                        "backup_local": f["backup_local"],
                    }
                    for f in manifest["files"]
                ],
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(json.dumps({"manifest": str(out), "sha256": str(sha_out), "qa": qa}, ensure_ascii=False, indent=2))
    if not qa["home"].get("ok") or not qa["home"].get("has_commercial_trust"):
        return 4
    if qa["home"].get("has_old_dealers_layout"):
        return 5
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
