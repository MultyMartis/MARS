#!/usr/bin/env python3
"""M9.8.9-03C — commercial trust block redesign: capture, backup, deploy, verify."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
WORK_DIR = ROOT / "reports" / "m9.8.9-03c-work"
CAPTURE_DIR = WORK_DIR / "live-capture"
BACKUP_DIR = ROOT / "backups"

CSS_PATCH = (WORK_DIR / "m9.8.9-03c-commercial-trust.css").read_text(encoding="utf-8")
NEW_TWIG = (WORK_DIR / "blockcommercialtrust.twig").read_text(encoding="utf-8")

CSS_MARKER_OLD = "M9.8.9-03 — PLP commercial trust"
CSS_MARKER_NEW = "M9.8.9-03C — PLP commercial trust"
CSS_ANCHOR_AFTER = "/* ==========================================================================\n   DEALERS + FORM"

HEADING_BLOCK = """\t\t\t$commercial_trust_headings = array(
\t\t\t\t'Столы' => 'Нужна помощь с выбором столов?',
\t\t\t\t'Моечные ванны' => 'Нужна помощь с выбором моечных ванн?',
\t\t\t\t'Подтоварники и подставки' => 'Нужна помощь с выбором подтоварников и подставок?',
\t\t\t\t'Тележки сервировочные' => 'Нужна помощь с выбором тележек?',
\t\t\t\t'Зонты вытяжные' => 'Нужна помощь с выбором зонтов?',
\t\t\t);
\t\t\t$commercial_trust_category_name = isset($category_info['name']) ? trim($category_info['name']) : '';
\t\t\t$data['commercial_trust_heading'] = isset($commercial_trust_headings[$commercial_trust_category_name])
\t\t\t\t? $commercial_trust_headings[$commercial_trust_category_name]
\t\t\t\t: 'Подберём оборудование под вашу задачу';
\t\t\t$data['blockcommercialtrust'] = $this->load->view('sections/blockcommercialtrust', $data);"""

FILES = [
    {
        "remote": "catalog/view/theme/default/template/sections/blockcommercialtrust.twig",
        "local": "blockcommercialtrust.twig",
        "backup": BACKUP_DIR / "blockcommercialtrust.twig.pre-m9.8.9-03c.bak",
        "patch_fn": "patch_twig_replace",
    },
    {
        "remote": "catalog/controller/product/category.php",
        "local": "category.php",
        "backup": BACKUP_DIR / "category.php.pre-m9.8.9-03c.bak",
        "patch_fn": "patch_category_php",
    },
    {
        "remote": "assets/css/style.css",
        "local": "style.css",
        "backup": BACKUP_DIR / "style.css.pre-m9.8.9-03c.bak",
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


def patch_twig_replace(_content: str) -> str:
    return NEW_TWIG


def patch_category_php(content: str) -> str:
    if CSS_MARKER_NEW in content or "commercial_trust_headings" in content:
        raise RuntimeError("category.php M9.8.9-03C patch already applied")

    old_simple = "\t\t\t$data['blockcommercialtrust'] = $this->load->view('sections/blockcommercialtrust');"
    old_with_data = "\t\t\t$data['blockcommercialtrust'] = $this->load->view('sections/blockcommercialtrust', $data);"

    if old_simple in content:
        return content.replace(old_simple, HEADING_BLOCK, 1)
    if old_with_data in content:
        return content.replace(old_with_data, HEADING_BLOCK, 1)

    raise RuntimeError("category.php blockcommercialtrust load line not found")


def replace_commercial_trust_css_block(content: str, new_block: str) -> str:
    pattern = re.compile(
        r"/\* =+\s*\n\s*M9\.8\.9-03C? — PLP commercial trust.*?(?=/\* =+\s*\n\s*DEALERS \+ FORM)",
        re.DOTALL,
    )
    match = pattern.search(content)
    if match:
        return content[: match.start()] + new_block + "\n" + content[match.end() :]

    if CSS_MARKER_NEW in content:
        raise RuntimeError("style.css M9.8.9-03C already present but block regex failed")

    anchor_idx = content.find(CSS_ANCHOR_AFTER)
    if anchor_idx == -1:
        raise RuntimeError("style.css DEALERS anchor not found")

    return content[:anchor_idx] + new_block + "\n" + content[anchor_idx:]


def patch_style_css(content: str) -> str:
    if CSS_MARKER_NEW in content and CSS_MARKER_OLD not in content:
        return replace_commercial_trust_css_block(content, CSS_PATCH.strip() + "\n")

    return replace_commercial_trust_css_block(content, CSS_PATCH.strip() + "\n")


PATCH_FNS = {
    "patch_twig_replace": patch_twig_replace,
    "patch_category_php": patch_category_php,
    "patch_style_css": patch_style_css,
}


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    manifest: dict = {
        "task": "M9.8.9-03C",
        "authority": "SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01",
        "stamp": stamp,
        "files": [],
    }

    deploy_results: list[dict] = []

    for spec in FILES:
        remote = spec["remote"]
        patch_fn = PATCH_FNS[spec["patch_fn"]]
        file_entry: dict = {"remote_path": remote}

        live_raw = ftp_download(remote)
        live_sha = sha256_hex(live_raw)
        capture_path = CAPTURE_DIR / spec["local"]
        capture_path.write_bytes(live_raw)
        spec["backup"].write_bytes(live_raw)

        live_text = live_raw.decode("utf-8")
        patched_text = patch_fn(live_text)
        patched_raw = patched_text.encode("utf-8")
        patched_sha = sha256_hex(patched_raw)
        patched_path = WORK_DIR / f"{spec['local']}.patched"
        patched_path.write_bytes(patched_raw)

        file_entry.update(
            {
                "capture": str(capture_path),
                "backup": str(spec["backup"]),
                "patched_local": str(patched_path),
                "sha256_pre": live_sha,
                "sha256_patched": patched_sha,
                "size_pre": len(live_raw),
                "size_patched": len(patched_raw),
            }
        )

        ftp_upload(remote, patched_raw)

        verify_raw = ftp_download(remote)
        verify_sha = sha256_hex(verify_raw)
        file_entry["verify_sha256"] = verify_sha
        file_entry["deploy_ok"] = verify_sha == patched_sha
        deploy_results.append(file_entry)
        manifest["files"].append(file_entry)

    cache_cleared = clear_twig_cache()

    manifest_post = {
        **manifest,
        "phase": "post-deploy",
        "twig_cache_cleared_count": len(cache_cleared),
        "all_deploy_ok": all(f["deploy_ok"] for f in deploy_results),
    }

    manifest_path = WORK_DIR / f"manifest-complete-{stamp}.json"
    manifest_path.write_text(
        json.dumps(manifest_post, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(json.dumps(manifest_post, indent=2, ensure_ascii=False))
    if not manifest_post["all_deploy_ok"]:
        raise SystemExit("Deploy verification failed for one or more files")


if __name__ == "__main__":
    main()
