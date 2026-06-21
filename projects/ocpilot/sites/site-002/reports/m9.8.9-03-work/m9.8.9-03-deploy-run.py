#!/usr/bin/env python3
"""M9.8.9-03 — certificates + dealers merge (Variant B): capture, backup, deploy."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
WORK_DIR = ROOT / "reports" / "m9.8.9-03-work"
CAPTURE_DIR = WORK_DIR / "live-capture"
BACKUP_DIR = ROOT / "backups"
CSS_PATCH = (WORK_DIR / "m9.8.9-03-commercial-trust.css").read_text(encoding="utf-8")
NEW_TWIG = (WORK_DIR / "blockcommercialtrust.twig").read_text(encoding="utf-8")

REMOTE_NEW_TWIG = "catalog/view/theme/default/template/sections/blockcommercialtrust.twig"

FILES = [
    {
        "remote": REMOTE_NEW_TWIG,
        "local": "blockcommercialtrust.twig",
        "backup": None,
        "is_new": True,
    },
    {
        "remote": "catalog/controller/product/category.php",
        "local": "category.php",
        "backup": BACKUP_DIR / "category.php.pre-m9.8.9-03-commercial-trust.bak",
        "patch_fn": "patch_category_php",
    },
    {
        "remote": "catalog/view/theme/default/template/product/category.twig",
        "local": "category.twig",
        "backup": BACKUP_DIR / "category.twig.pre-m9.8.9-03-commercial-trust.bak",
        "patch_fn": "patch_category_twig",
    },
    {
        "remote": "assets/css/style.css",
        "local": "style.css",
        "backup": BACKUP_DIR / "style.css.pre-m9.8.9-03-commercial-trust.bak",
        "patch_fn": "patch_style_css",
    },
]


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


def ftp_exists(remote_path: str) -> bool:
    ftp = ftp_connect()
    try:
        ftp.size(remote_path)
        ftp.quit()
        return True
    except ftplib.error_perm:
        ftp.quit()
        return False


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


def patch_category_php(content: str) -> str:
    if "blockcommercialtrust" in content:
        raise RuntimeError("category.php patch already applied")

    old = """\t\t\t$data['certificates'] = $this->load->view('sections/certificates');
\t\t\t$data['aboutteaser'] = $this->load->view('sections/aboutteaser');
\t\t\t$data['blockadvantagestop'] = $this->load->view('sections/blockadvantagestop');
\t\t\t$data['blockdealersform'] = $this->load->view('sections/blockdealersform');"""

    new = """\t\t\t$data['blockcommercialtrust'] = $this->load->view('sections/blockcommercialtrust');
\t\t\t$data['aboutteaser'] = $this->load->view('sections/aboutteaser');
\t\t\t$data['blockadvantagestop'] = $this->load->view('sections/blockadvantagestop');"""

    if old not in content:
        raise RuntimeError("category.php expected block not found")

    return content.replace(old, new, 1)


def patch_category_twig(content: str) -> str:
    if "blockcommercialtrust" in content and "certificates" not in content:
        raise RuntimeError("category.twig patch already applied")

    import re

    patched, count = re.subn(
        r"\{\{\s*seotext\s*\}\}\s*\{\{\s*certificates\s*\}\}\s*\{\{\s*blockdealersform\s*\}\}",
        "{{ seotext }}\n{{ blockcommercialtrust }}",
        content,
        count=1,
    )
    if count != 1:
        raise RuntimeError("category.twig expected block not found")

    return patched


def patch_style_css(content: str) -> str:
    marker = "M9.8.9-03 — PLP commercial trust"
    if marker in content:
        raise RuntimeError("style.css patch already applied")

    anchor = "/* ==========================================================================\n   DEALERS + FORM"
    idx = content.find(anchor)
    if idx == -1:
        raise RuntimeError("style.css DEALERS anchor not found")

    return content[:idx] + CSS_PATCH + "\n" + content[idx:]


PATCH_FNS = {
    "patch_category_php": patch_category_php,
    "patch_category_twig": patch_category_twig,
    "patch_style_css": patch_style_css,
}


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    manifest: dict = {
        "task": "M9.8.9-03",
        "variant": "B — Trust strip + split",
        "authority": "SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01",
        "stamp": stamp,
        "phase": "pre-deploy",
        "files": [],
    }

    deploy_results: list[dict] = []

    for spec in FILES:
        remote = spec["remote"]
        patch_fn_name = spec.get("patch_fn")
        file_entry: dict = {"remote_path": remote}

        if spec.get("is_new") and ftp_exists(remote):
            file_entry["skipped"] = "already deployed"
            file_entry["deploy_ok"] = True
            deploy_results.append(file_entry)
            manifest["files"].append(file_entry)
            continue

        if spec.get("is_new"):
            pre_exists = ftp_exists(remote)
            file_entry["pre_exists"] = pre_exists
            patched_text = NEW_TWIG
            patched_path = WORK_DIR / "blockcommercialtrust.twig.deploy"
            patched_path.write_text(patched_text, encoding="utf-8")
            file_entry["patched_local"] = str(patched_path)
            file_entry["sha256_patched"] = sha256_hex(patched_text.encode("utf-8"))
            file_entry["size_patched"] = len(patched_text.encode("utf-8"))
        else:
            live_raw = ftp_download(remote)
            live_sha = sha256_hex(live_raw)
            capture_path = CAPTURE_DIR / spec["local"]
            capture_path.write_bytes(live_raw)
            if spec["backup"]:
                spec["backup"].write_bytes(live_raw)

            live_text = live_raw.decode("utf-8")
            patch_fn = PATCH_FNS[patch_fn_name]
            patched_text = patch_fn(live_text)
            patched_raw = patched_text.encode("utf-8")
            patched_sha = sha256_hex(patched_raw)
            patched_path = WORK_DIR / f"{spec['local']}.patched"
            patched_path.write_bytes(patched_raw)

            file_entry.update(
                {
                    "capture": str(capture_path),
                    "backup": str(spec["backup"]) if spec["backup"] else None,
                    "patched_local": str(patched_path),
                    "sha256_pre": live_sha,
                    "sha256_patched": patched_sha,
                    "size_pre": len(live_raw),
                    "size_patched": len(patched_raw),
                }
            )

        ftp_upload(remote, patched_text.encode("utf-8"))

        verify_raw = ftp_download(remote)
        verify_sha = sha256_hex(verify_raw)
        file_entry["verify_sha256"] = verify_sha
        file_entry["deploy_ok"] = verify_sha == file_entry["sha256_patched"]
        deploy_results.append(file_entry)
        manifest["files"].append(file_entry)

    cache_cleared = clear_twig_cache()

    manifest_post = {
        **manifest,
        "phase": "post-deploy",
        "twig_cache_cleared_count": len(cache_cleared),
        "all_deploy_ok": all(f["deploy_ok"] for f in deploy_results),
    }

    manifest_pre_path = WORK_DIR / f"manifest-pre-{stamp}.json"
    manifest_post_path = WORK_DIR / f"manifest-post-{stamp}.json"
    manifest_pre_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    manifest_post_path.write_text(
        json.dumps(manifest_post, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(json.dumps(manifest_post, indent=2, ensure_ascii=False))
    if not manifest_post["all_deploy_ok"]:
        raise SystemExit("Deploy verification failed for one or more files")


if __name__ == "__main__":
    main()
