#!/usr/bin/env python3
"""M9.8.9-10 — remove page-intro__description from neutral hub: capture, backup, patch, deploy."""
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
WORK_DIR = ROOT / "reports" / "m9.8.9-10-work"
CAPTURE_DIR = WORK_DIR / "live-capture"

REMOTE = "catalog/controller/product/category.php"
LOCAL = "catalog__controller__product__category.php"
BACKUP = ROOT / "backups" / "category.php.pre-m9.8.9-10-page-intro-description.bak"
PATCHED = "catalog__controller__product__category.php.patched"

PHP_OLD = """\t\t\t$pageintro = new Pageintro();
\t\t\t$pageintro->title = $data['heading_title'];
\t\t\tif ($is_hub) {
\t\t\t\t$pageintro->description = 'Выберите тип нейтрального оборудования: столы, моечные ванны, подтоварники, зонты или сервировочные тележки. В каждом разделе — свой каталог с подходящими фильтрами.';
\t\t\t} else {
\t\t\t\t$pageintro->description = '';
\t\t\t}
\t\t\t$this->document->setPageintro($pageintro->render());"""

PHP_NEW = """\t\t\t$pageintro = new Pageintro();
\t\t\t$pageintro->title = $data['heading_title'];
\t\t\t$pageintro->description = '';
\t\t\t$this->document->setPageintro($pageintro->render());"""


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


def patch_category_php(content: str) -> str:
    marker = "$pageintro->description = '';"
    if PHP_OLD not in content:
        if (
            marker in content
            and "Выберите тип нейтрального оборудования" not in content
        ):
            raise RuntimeError("category.php patch already applied (hub intro text absent)")
        raise RuntimeError("pageintro hub description block not found in category.php")

    return content.replace(PHP_OLD, PHP_NEW, 1)


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
    ROOT.joinpath("backups").mkdir(parents=True, exist_ok=True)

    capture_path = CAPTURE_DIR / LOCAL
    patched_path = WORK_DIR / PATCHED

    live_raw = ftp_download(REMOTE)
    live_sha = sha256_hex(live_raw)
    capture_path.write_bytes(live_raw)
    BACKUP.write_bytes(live_raw)

    live_text = live_raw.decode("utf-8")
    patched_text = patch_category_php(live_text)
    patched_raw = patched_text.encode("utf-8")
    patched_sha = sha256_hex(patched_raw)
    patched_path.write_bytes(patched_raw)

    file_entry = {
        "remote_path": REMOTE,
        "capture": str(capture_path),
        "backup": str(BACKUP),
        "patched_local": str(patched_path),
        "sha256_pre": live_sha,
        "sha256_patched": patched_sha,
        "size_pre": len(live_raw),
        "size_patched": len(patched_raw),
    }

    manifest_pre = {
        "task": "M9.8.9-10",
        "authority": "SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01",
        "stamp": stamp,
        "phase": "pre-deploy",
        "files": [file_entry],
    }

    ftp_upload(REMOTE, patched_raw)

    verify_raw = ftp_download(REMOTE)
    verify_sha = sha256_hex(verify_raw)
    file_entry["verify_sha256"] = verify_sha
    file_entry["deploy_ok"] = verify_sha == patched_sha

    cache_cleared = clear_twig_cache()

    manifest_post = {
        **manifest_pre,
        "phase": "post-deploy",
        "twig_cache_cleared": cache_cleared,
        "all_deploy_ok": file_entry["deploy_ok"],
    }

    manifest_pre_path = WORK_DIR / f"manifest-pre-{stamp}.json"
    manifest_post_path = WORK_DIR / f"manifest-post-{stamp}.json"
    manifest_pre_path.write_text(
        json.dumps(manifest_pre, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    manifest_post_path.write_text(
        json.dumps(manifest_post, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(json.dumps(manifest_post, indent=2, ensure_ascii=False))
    if not manifest_post["all_deploy_ok"]:
        raise SystemExit("Deploy verification failed")


if __name__ == "__main__":
    main()
