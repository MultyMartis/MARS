#!/usr/bin/env python3
"""SITE-002 — M9.13 About Company redesign restore v2 (polish authority, operator CSS merge)."""
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
WORK_DIR = ROOT / "reports" / "m9.13-work"
POLISH_DIR = ROOT / "reports" / "m9.13-polish-work"
OUT_DIR = ROOT / "reports" / "m9.13-restore-v2-work"
BACKUP_DIR = ROOT / "backups"
QA_DIR = ROOT / "qa"

BACKUP_SUFFIX = "pre-site-002-about-restore-v2.bak"
CSS_MARKER = "M9.13 — About Company page — compact redesign"
LIVE_URL = "https://zpm.new-site.space/about"

AUTHORITY = {
    "twig": WORK_DIR / "about.twig",
    "php": WORK_DIR / "about.php",
    "css_block": WORK_DIR / "m9.13-about-page.css",
    "hero_img": POLISH_DIR / "assets" / "img" / "about-page-img.jpg",
    "logistics_img": POLISH_DIR / "assets" / "img" / "about-logistics.jpg",
    "reports": [
        "SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md",
        "SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md",
    ],
}

DEPLOY_ITEMS = [
    {
        "remote": "catalog/view/theme/default/template/information/about.twig",
        "local": AUTHORITY["twig"],
        "backup": BACKUP_DIR / f"catalog__view__theme__default__template__information__about.twig.{BACKUP_SUFFIX}",
    },
    {
        "remote": "catalog/controller/information/about.php",
        "local": AUTHORITY["php"],
        "backup": BACKUP_DIR / f"catalog__controller__information__about.php.{BACKUP_SUFFIX}",
    },
    {
        "remote": "assets/css/style.css",
        "local": None,
        "backup": BACKUP_DIR / f"style.css.{BACKUP_SUFFIX}",
        "css_merge": True,
    },
]

IMAGE_ITEMS = [
    {
        "remote": "assets/img/about-page-img.jpg",
        "local": AUTHORITY["hero_img"],
        "backup": BACKUP_DIR / f"assets__img__about-page-img.jpg.{BACKUP_SUFFIX}",
    },
    {
        "remote": "assets/img/about-logistics.jpg",
        "local": AUTHORITY["logistics_img"],
        "backup": None,
        "action": "new_or_replace",
    },
]

M913_SECTIONS = (
    "zpm-about-hero",
    "zpm-about-company",
    "zpm-about-advantages",
    "zpm-about-certs",
    "zpm-about-geo",
    "zpm-about-cta",
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


def patch_style_css(live_text: str, append_path: Path) -> str:
    """Merge M9.13 block onto live operator CSS — replace block if marker exists, else append."""
    append_block = append_path.read_text(encoding="utf-8")
    marker_line = f"/* ==========================================================================\n   {CSS_MARKER}"
    if CSS_MARKER in live_text:
        before, _sep, _after = live_text.partition(marker_line)
        return before.rstrip() + "\n\n" + append_block.strip() + "\n"
    return live_text.rstrip() + "\n\n" + append_block.strip() + "\n"


def verify_authority() -> dict:
    out: dict = {"ok": True, "files": {}}
    for key, path in AUTHORITY.items():
        if key == "reports":
            continue
        entry = {"path": str(path), "exists": path.is_file()}
        if entry["exists"]:
            data = path.read_bytes()
            entry["sha256"] = sha256_hex(data)
            entry["bytes"] = len(data)
        else:
            out["ok"] = False
        out["files"][key] = entry
    return out


def qa_check() -> dict:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        LIVE_URL,
        headers={"Cookie": "beget=begetok", "User-Agent": "MARS-M9.13-restore-v2"},
    )
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
            html = resp.read().decode("utf-8", "replace")
            http_status = resp.status
    except urllib.error.HTTPError as exc:
        html = exc.read().decode("utf-8", "replace") if exc.fp else ""
        http_status = exc.code

    qa_path = OUT_DIR / "qa-about-redesign-v2.html"
    qa_path.write_text(html, encoding="utf-8")
    QA_DIR.mkdir(parents=True, exist_ok=True)
    (QA_DIR / "m9.13-about-redesign-v2-desktop.html").write_text(html, encoding="utf-8")

    checks = {
        "http_200": http_status == 200,
        "http_status": http_status,
        "has_zpm_about_page": "zpm-about-page" in html,
        "has_trust_row": "zpm-about-hero__trust" in html,
        "logistics_photo": 'src="/assets/img/about-logistics.jpg"' in html,
        "hero_photo": 'src="/assets/img/about-page-img.jpg"' in html,
        "has_fancybox_cert": 'data-fancybox="certificates-about"' in html,
        "has_cta": "zpm-about-cta" in html,
        "form_dialog_7": 'name="dialog" value="7"' in html,
        "has_breadcrumbs": "breadcrumb" in html.lower() or "breadcrumbs" in html.lower(),
        "no_old_main_wrap": "about-page--main-wrap" not in html,
        "no_old_video_block": "about-page-video" not in html,
        "no_old_dealer_block": "blockdealersform" not in html and "zpm-dealers" not in html,
        "no_old_cert_slider": "js-certificates-slider" not in html,
        "no_adv_trans_in_geo": "zpm-about-geo" in html
        and "advant/adv-trans-company.png" not in html.split("zpm-about-geo")[1].split("</section>")[0],
    }
    for sec in M913_SECTIONS:
        checks[f"has_{sec}"] = sec in html
    checks["all_pass"] = all(v for k, v in checks.items() if k != "http_status" and isinstance(v, bool))
    return checks


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    manifest: dict = {
        "pass": "m9.13-about-redesign-restore-v2",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "live_url": LIVE_URL,
        "authority": {
            "visual_baseline": "SITE-002-STABLE-LIVE-LOCAL-FONTS-01",
            "about_implementation": "M9.13 redesign + polish pass v1 work copies",
            "merge_policy": "Live operator CSS preserved; M9.13 zpm-about block merged",
        },
        "backup_suffix": BACKUP_SUFFIX,
    }

    manifest["authority_verification"] = verify_authority()
    if not manifest["authority_verification"]["ok"]:
        raise SystemExit("Missing required authority work copies")

    manifest["files"] = {}
    for item in DEPLOY_ITEMS:
        remote = item["remote"]
        live = ftp_download(remote)
        item["backup"].write_bytes(live)
        entry = {
            "pre_sha256": sha256_hex(live),
            "pre_bytes": len(live),
            "backup": str(item["backup"]),
        }

        if item.get("css_merge"):
            live_text = live.decode("utf-8", errors="replace")
            upload_data = patch_style_css(live_text, AUTHORITY["css_block"]).encode("utf-8")
            entry["merge"] = "M9.13 block merged onto live operator style.css"
        elif item.get("local"):
            upload_data = item["local"].read_bytes()
            entry["source"] = str(item["local"])
            entry["source_sha256"] = sha256_hex(upload_data)
        else:
            upload_data = live

        ftp_upload(remote, upload_data)
        entry["post_sha256"] = sha256_hex(upload_data)
        entry["post_bytes"] = len(upload_data)
        manifest["files"][remote] = entry

    manifest["images"] = {}
    for item in IMAGE_ITEMS:
        remote = item["remote"]
        upload_data = item["local"].read_bytes()
        entry: dict = {
            "local": str(item["local"]),
            "source_sha256": sha256_hex(upload_data),
            "post_sha256": sha256_hex(upload_data),
            "post_bytes": len(upload_data),
            "action": item.get("action", "replace"),
        }
        try:
            live = ftp_download(remote)
            if item.get("backup"):
                item["backup"].write_bytes(live)
                entry["pre_sha256"] = sha256_hex(live)
                entry["pre_bytes"] = len(live)
                entry["backup"] = str(item["backup"])
        except ftplib.error_perm:
            entry["pre_exists"] = False
        ftp_upload(remote, upload_data)
        manifest["images"][remote] = entry

    manifest["twig_cache_cleared"] = clear_twig_cache()
    manifest["qa"] = qa_check()

    sha256_manifest = {}
    for path in sorted(BACKUP_DIR.glob(f"*.{BACKUP_SUFFIX}")):
        data = path.read_bytes()
        sha256_manifest[path.name] = {"sha256": sha256_hex(data), "bytes": len(data)}
    manifest["backup_sha256"] = sha256_manifest

    out = OUT_DIR / "restore-v2-manifest.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    (OUT_DIR / "restore-v2-sha256.json").write_text(
        json.dumps(sha256_manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
