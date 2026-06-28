#!/usr/bin/env python3
"""SITE-002 — Local fonts migration deploy (TEST only)."""
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
WORK = ROOT / "reports" / "local-fonts-work"
BACKUP = ROOT / "backups"
BACKUP_SUFFIX = "pre-site-002-local-fonts-01.bak"

FONT_FACE_BLOCK = """@font-face {
  font-family: "Inter";
  src: url("../fonts/Inter-Regular.woff2") format("woff2"), url("../fonts/Inter-Regular.woff") format("woff");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: "Inter";
  src: url("../fonts/Inter-Medium.woff2") format("woff2"), url("../fonts/Inter-Medium.woff") format("woff");
  font-weight: 500;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: "Inter";
  src: url("../fonts/Inter-SemiBold.woff2") format("woff2"), url("../fonts/Inter-SemiBold.woff") format("woff");
  font-weight: 600;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: "Inter";
  src: url("../fonts/Inter-Bold.woff2") format("woff2");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: "Inter";
  src: url("../fonts/Inter-ExtraBold.woff2") format("woff2");
  font-weight: 800;
  font-style: normal;
  font-display: swap;
}"""

PRELOAD_BLOCK = """    <!-- Local Inter — critical weights (SITE-002 local fonts migration) -->
    <link rel="preload" href="/assets/fonts/Inter-Regular.woff2" as="font" type="font/woff2" crossorigin />
    <link rel="preload" href="/assets/fonts/Inter-Medium.woff2" as="font" type="font/woff2" crossorigin />
"""

QA_URLS = [
    "https://zpm.new-site.space/",
    "https://zpm.new-site.space/about",
    "https://zpm.new-site.space/katalog/",
]

DEPLOY_FILES = [
    {
        "remote": "assets/css/style.css",
        "local": WORK / "style.css",
        "backup": BACKUP / f"style.css.{BACKUP_SUFFIX}",
    },
    {
        "remote": "assets/css/style.min.css",
        "local": WORK / "style.min.css",
        "backup": BACKUP / f"style.min.css.{BACKUP_SUFFIX}",
    },
    {
        "remote": "catalog/view/theme/default/template/common/header.twig",
        "local": WORK / "header.twig",
        "backup": BACKUP / f"catalog__view__theme__default__template__common__header.twig.{BACKUP_SUFFIX}",
    },
]

NEW_FONTS = [
    {
        "remote": "assets/fonts/Inter-Bold.woff2",
        "local": WORK / "fonts-pack" / "Inter-Bold.woff2",
        "backup": BACKUP / f"assets__fonts__Inter-Bold.woff2.{BACKUP_SUFFIX}",
    },
    {
        "remote": "assets/fonts/Inter-ExtraBold.woff2",
        "local": WORK / "fonts-pack" / "Inter-ExtraBold.woff2",
        "backup": BACKUP / f"assets__fonts__Inter-ExtraBold.woff2.{BACKUP_SUFFIX}",
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


def patch_style_css(text: str) -> str:
    return re.sub(
        r"@font-face\s*\{[^}]+\}\s*@font-face\s*\{[^}]+\}\s*@font-face\s*\{[^}]+\}",
        FONT_FACE_BLOCK,
        text,
        count=1,
        flags=re.S,
    )


def patch_style_min_css(text: str) -> str:
    replacement = (
        '@font-face{font-display:swap;font-family:Inter;font-style:normal;font-weight:400;'
        'src:url(../fonts/Inter-Regular.woff2) format("woff2"),url(../fonts/Inter-Regular.woff) format("woff")}'
        '@font-face{font-display:swap;font-family:Inter;font-style:normal;font-weight:500;'
        'src:url(../fonts/Inter-Medium.woff2) format("woff2"),url(../fonts/Inter-Medium.woff) format("woff")}'
        '@font-face{font-display:swap;font-family:Inter;font-style:normal;font-weight:600;'
        'src:url(../fonts/Inter-SemiBold.woff2) format("woff2"),url(../fonts/Inter-SemiBold.woff) format("woff")}'
        '@font-face{font-display:swap;font-family:Inter;font-style:normal;font-weight:700;'
        'src:url(../fonts/Inter-Bold.woff2) format("woff2")}'
        '@font-face{font-display:swap;font-family:Inter;font-style:normal;font-weight:800;'
        'src:url(../fonts/Inter-ExtraBold.woff2) format("woff2")}'
    )
    return re.sub(
        r"@font-face\{font-display:swap;font-family:Inter;font-style:normal;font-weight:400;[^}]+\}"
        r"@font-face\{font-display:swap;font-family:Inter;font-style:normal;font-weight:500;[^}]+\}"
        r"@font-face\{font-display:swap;font-family:Inter;font-style:normal;font-weight:600;[^}]+\}",
        replacement,
        text,
        count=1,
    )


def patch_header_twig(text: str) -> str:
    if 'href="/assets/fonts/Inter-Regular.woff2"' in text:
        return text
    marker = '    <link rel="apple-touch-icon" sizes="180x180" href="/assets/favicon/apple-touch-icon.png" />'
    if marker not in text:
        raise RuntimeError("header.twig favicon marker not found")
    text = text.replace(marker, marker + "\n\n" + PRELOAD_BLOCK.rstrip())
    text = text.replace(
        '<link rel="stylesheet" href="/assets/css/style.css?22062026-mca" />',
        '<link rel="stylesheet" href="/assets/css/style.css" />',
    )
    return text


def http_get(url: str) -> tuple[int, str]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "SITE-002-local-fonts/1.0", "Cache-Control": "no-cache"},
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def qa_scan(html: str) -> dict:
    head = html.split("</head>")[0] if "</head>" in html else html[:5000]
    return {
        "googleapis": "fonts.googleapis.com" in head.lower(),
        "gstatic": "fonts.gstatic.com" in head.lower(),
        "preload_regular": 'rel="preload"' in head and "Inter-Regular.woff2" in head,
        "style_min_active": 'href="/assets/css/style.min.css"' in head and "<!--" not in head.split('style.min.css')[0][-30:],
    }


def prepare_work_files() -> None:
    css_live = (WORK / "style.css.live").read_text(encoding="utf-8")
    (WORK / "style.css").write_text(patch_style_css(css_live), encoding="utf-8")

    min_live = ftp_download("assets/css/style.min.css")
    if not min_live:
        raise RuntimeError("style.min.css download failed")
    (WORK / "style.min.css").write_bytes(min_live)
    patched_min = patch_style_min_css(min_live.decode("utf-8", errors="replace"))
    (WORK / "style.min.css").write_text(patched_min, encoding="utf-8")

    header = (WORK / "header.twig").read_text(encoding="utf-8")
    (WORK / "header.twig").write_text(patch_header_twig(header), encoding="utf-8")


def main() -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest: dict = {"timestamp": ts, "checkpoint": "SITE-002-STABLE-LIVE-LOCAL-FONTS-01", "backups": [], "deploy": [], "qa": []}

    prepare_work_files()

    for item in DEPLOY_FILES + NEW_FONTS:
        remote = item["remote"]
        live = ftp_download(remote)
        if live is not None:
            item["backup"].write_bytes(live)
            manifest["backups"].append({"remote": remote, "backup": str(item["backup"]), "sha256": sha256_hex(live)})
        elif item in NEW_FONTS:
            manifest["backups"].append({"remote": remote, "backup": None, "note": "new file — no prior remote"})

    for item in DEPLOY_FILES + NEW_FONTS:
        data = item["local"].read_bytes()
        ftp_upload(item["remote"], data)
        manifest["deploy"].append({"remote": item["remote"], "sha256": sha256_hex(data), "bytes": len(data)})

    manifest["twig_cache_cleared"] = clear_twig_cache()

    for url in QA_URLS:
        status, html = http_get(url)
        scan = qa_scan(html)
        manifest["qa"].append({"url": url, "status": status, **scan})

    for font in ["Inter-Regular.woff2", "Inter-Medium.woff2", "Inter-SemiBold.woff2", "Inter-Bold.woff2", "Inter-ExtraBold.woff2"]:
        req = urllib.request.Request(f"https://zpm.new-site.space/assets/fonts/{font}", method="HEAD")
        ctx = ssl.create_default_context()
        try:
            with urllib.request.urlopen(req, timeout=20, context=ctx) as resp:
                manifest.setdefault("font_http", []).append({"file": font, "status": resp.status})
        except urllib.error.HTTPError as e:
            manifest.setdefault("font_http", []).append({"file": font, "status": e.code})

    out = WORK / "deploy-manifest.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
