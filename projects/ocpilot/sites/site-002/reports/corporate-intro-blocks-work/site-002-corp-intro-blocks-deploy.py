#!/usr/bin/env python3
"""SITE-002 — corporate intro image blocks: backup, deploy, QA."""
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
WORK = ROOT / "reports" / "corporate-intro-blocks-work"
ASSETS_LOCAL = WORK / "assets" / "img" / "corporate"
BACKUP = ROOT / "backups"
BACKUP_SUFFIX = "pre-site-002-corp-intro-blocks-01.bak"
CSS_MARKER = "SITE-002 — Corporate intro image blocks (zpm-corp-intro)"
BASE = "https://zpm.new-site.space"

PAGES = {
    "catalog/view/theme/default/template/information/about.twig": {
        "local": WORK / "about.twig",
        "url": f"{BASE}/about",
        "image": "/assets/img/corporate/about-intro.jpg",
    },
    "catalog/view/theme/default/template/information/delivery.twig": {
        "local": WORK / "delivery.twig",
        "url": f"{BASE}/delivery",
        "image": "/assets/img/corporate/delivery-intro.jpg",
    },
    "catalog/view/theme/default/template/information/payment.twig": {
        "local": WORK / "payment.twig",
        "url": f"{BASE}/payment-methods",
        "image": "/assets/img/corporate/payment-intro.jpg",
    },
    "catalog/view/theme/default/template/information/guarantee.twig": {
        "local": WORK / "guarantee.twig",
        "url": f"{BASE}/guarantee",
        "image": "/assets/img/corporate/warranty-intro.jpg",
    },
    "catalog/view/theme/default/template/information/dealers.twig": {
        "local": WORK / "dealers.twig",
        "url": f"{BASE}/dealers",
        "image": "/assets/img/corporate/dealers-intro.jpg",
    },
    "catalog/view/theme/default/template/information/custom_equipment.twig": {
        "local": WORK / "custom_equipment.twig",
        "url": f"{BASE}/custom-equipment",
        "image": "/assets/img/corporate/custom-intro.jpg",
    },
}

ASSET_FILES = [
    "assets/img/corporate/about-intro.jpg",
    "assets/img/corporate/delivery-intro.jpg",
    "assets/img/corporate/payment-intro.jpg",
    "assets/img/corporate/warranty-intro.jpg",
    "assets/img/corporate/dealers-intro.jpg",
    "assets/img/corporate/custom-intro.jpg",
]

REMOTE_TOUCHED = list(PAGES.keys()) + ["assets/css/style.css"]


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


def ftp_ensure_dir(remote_dir: str) -> None:
    ftp = ftp_connect()
    ftp.cwd("/")
    parts = remote_dir.strip("/").split("/")
    for part in parts:
        try:
            ftp.cwd(part)
        except ftplib.error_perm:
            try:
                ftp.mkd(part)
            except ftplib.error_perm:
                pass
            ftp.cwd(part)
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
    append_block = (WORK / "zpm-corp-intro.css").read_text(encoding="utf-8")
    marker_line = f"/* ==========================================================================\n   {CSS_MARKER}"
    if CSS_MARKER in live_text:
        before, _sep, _after = live_text.partition(marker_line)
        return before.rstrip() + "\n\n" + append_block.strip() + "\n"
    return live_text.rstrip() + "\n\n" + append_block.strip() + "\n"


def http_get(url: str) -> tuple[int, str]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "SITE-002-corp-intro-blocks/1.0", "Cookie": "beget=begetok"},
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", errors="replace")


def qa_page(url: str, image_path: str) -> dict:
    status, html = http_get(url)
    checks = {
        "http_ok": status == 200,
        "has_zpm_corp_intro": "zpm-corp-intro" in html,
        "has_intro_aria": 'aria-label="Вводная информация"' in html,
        "has_intro_image": image_path in html,
        "hero_not_using_about_intro": True,
        "oem_not_using_custom_intro": True,
    }
    if "/about" in url:
        checks["hero_restored"] = "/assets/img/about-page-img.jpg" in html
        if "zpm-about-hero" in html and "zpm-corp-intro" in html:
            hero_html = html.split("zpm-about-hero", 1)[1].split("zpm-corp-intro", 1)[0]
            checks["hero_not_using_about_intro"] = "/assets/img/corporate/about-intro.jpg" not in hero_html
        checks["intro_image_in_block"] = "zpm-corp-intro" in html and "/assets/img/corporate/about-intro.jpg" in html
    if "custom-equipment" in url:
        oem_chunk = html.split("zpm-custom-oem__media", 1)
        if len(oem_chunk) > 1:
            checks["oem_not_using_custom_intro"] = "/assets/img/corporate/custom-intro.jpg" not in oem_chunk[1].split(
                "zpm-corp-intro", 1
            )[0]
        checks["oem_restored"] = "/assets/img/about-page-img.jpg" in html
    checks["all_pass"] = all(checks.values())
    return {"url": url, "status": status, "checks": checks}


def sync_assets_from_ftp() -> dict:
    ASSETS_LOCAL.mkdir(parents=True, exist_ok=True)
    report: dict = {}
    for remote in ASSET_FILES:
        local = ASSETS_LOCAL / Path(remote).name
        data = ftp_download(remote)
        if data is None:
            report[remote] = {"local": str(local), "exists": False, "bytes": 0}
            continue
        local.write_bytes(data)
        report[remote] = {
            "local": str(local),
            "exists": True,
            "bytes": len(data),
            "sha256": sha256_hex(data),
        }
    return report


def upload_assets(manifest_assets: dict) -> dict:
    uploaded: dict = {}
    ftp_ensure_dir("assets/img/corporate")
    for remote in ASSET_FILES:
        local = ASSETS_LOCAL / Path(remote).name
        entry = manifest_assets.get(remote, {})
        if not local.is_file():
            uploaded[remote] = {"uploaded": False, "reason": "missing_local"}
            continue
        data = local.read_bytes()
        ftp_upload(remote, data)
        uploaded[remote] = {
            "uploaded": True,
            "bytes": len(data),
            "sha256": sha256_hex(data),
            "source": str(local),
        }
    return uploaded


def main() -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    BACKUP.mkdir(parents=True, exist_ok=True)

    subprocess.run(["python", str(WORK / "apply-corp-intro-twig.py")], check=True)

    manifest: dict = {
        "pass": "site-002-corporate-intro-blocks-01",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "branch": "mars/canonical-post-recovery",
        "checkpoint_pre": "c658d560",
        "files": {},
        "sha256": {},
        "assets_local": {},
        "assets_upload": {},
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
        backup = backup_name(remote)
        backup.write_bytes(live)

    manifest["assets_local"] = sync_assets_from_ftp()
    manifest["assets_upload"] = upload_assets(manifest["assets_local"])

    for remote, meta in PAGES.items():
        payload = meta["local"].read_bytes()
        live = backup_name(remote).read_bytes()
        ftp_upload(remote, payload)
        entry = {
            "backup": str(backup_name(remote)),
            "pre_sha256": sha256_hex(live),
            "post_sha256": sha256_hex(payload),
            "pre_bytes": len(live),
            "post_bytes": len(payload),
            "expect_image": meta["image"],
        }
        manifest["files"][remote] = entry
        manifest["sha256"][remote] = {"pre": entry["pre_sha256"], "post": entry["post_sha256"]}

    css_remote = "assets/css/style.css"
    css_live = backup_name(css_remote).read_bytes()
    css_text = css_live.decode("utf-8", errors="replace")
    css_patched = patch_style_css(css_text)
    css_upload = css_patched.encode("utf-8")
    ftp_upload(css_remote, css_upload)
    manifest["files"][css_remote] = {
        "backup": str(backup_name(css_remote)),
        "pre_sha256": sha256_hex(css_live),
        "post_sha256": sha256_hex(css_upload),
        "pre_bytes": len(css_live),
        "post_bytes": len(css_upload),
    }
    manifest["sha256"][css_remote] = {
        "pre": sha256_hex(css_live),
        "post": sha256_hex(css_upload),
    }

    manifest["twig_cache_cleared"] = clear_twig_cache()

    qa_results = {}
    for remote, meta in PAGES.items():
        qa_results[remote] = qa_page(meta["url"], meta["image"])

    manifest["qa"] = qa_results
    manifest["qa"]["assets_http"] = {}
    for asset in ASSET_FILES:
        url = f"{BASE}/{asset.lstrip('/')}"
        try:
            code = urllib.request.urlopen(url, timeout=60).getcode()
            manifest["qa"]["assets_http"][asset] = code
        except urllib.error.HTTPError as exc:
            manifest["qa"]["assets_http"][asset] = exc.code

    manifest["qa_all_pass"] = all(
        r.get("checks", {}).get("all_pass", False) for r in qa_results.values()
    ) and all(code == 200 for code in manifest["qa"]["assets_http"].values())

    (WORK / "deploy-sha256.json").write_text(
        json.dumps(manifest["sha256"], indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (WORK / "deploy-manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
