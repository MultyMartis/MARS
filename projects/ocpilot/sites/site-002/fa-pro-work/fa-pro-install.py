#!/usr/bin/env python3
"""SITE-002 — install Font Awesome Pro 5.15.4 (FTP upload + header link)."""
import ftplib
import io
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HOST = os.environ.get("SITE002_FTP_HOST", "")
FTP_USER = os.environ.get("SITE002_FTP_USER", "")
FTP_PASS = os.environ.get("SITE002_FTP_PASS", "")

BASE = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
BACKUP_DIR = BASE / "backups"
WORK = BASE / "fa-pro-work"
QA_DIR = BASE / "qa" / "fa-pro-install"

FA_SRC = Path(
    r"C:\AI MARS\shared\assets\icon-libraries\Font Awesome Pro 5.15.4"
)
FA_CSS_LOCAL = FA_SRC / "css" / "all.min.css"
FA_WEBFONTS_LOCAL = FA_SRC / "webfonts"

REMOTE_CSS = "assets/vendor/fontawesome-pro-5.15.4/css/all.min.css"
REMOTE_WEBFONTS_DIR = "assets/vendor/fontawesome-pro-5.15.4/webfonts"
REMOTE_HEADER = "catalog/view/theme/default/template/common/header.twig"

BACKUP_HEADER = BACKUP_DIR / "header.twig.pre-fa-pro-install.bak"
WORK_HEADER = WORK / "header.twig"

FA_LINK = (
    '<link rel="stylesheet" '
    'href="/assets/vendor/fontawesome-pro-5.15.4/css/all.min.css">'
)

TEST_BASE = "https://zpm.new-site.space"
URLS = {
    "home": f"{TEST_BASE}/",
    "catalog": f"{TEST_BASE}/katalog/",
    "category": (
        f"{TEST_BASE}/katalog/nejtralnoe-oborudovanie/stoly/"
        "stoly-serii-premium/stoly-premium-600/"
    ),
    "pdp": (
        f"{TEST_BASE}/katalog/nejtralnoe-oborudovanie/stoly/"
        "stoly-serii-premium/stoly-premium-600/"
        "stol-proizvodstvennyy-sp-p-18-6-1800h600h850"
    ),
}


def require_creds():
    if not all((HOST, FTP_USER, FTP_PASS)):
        print("Missing SITE002_FTP_HOST / SITE002_FTP_USER / SITE002_FTP_PASS", file=sys.stderr)
        sys.exit(1)


def ftp_connect():
    ftp = ftplib.FTP(HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_cwd_mkd(ftp, remote_dir):
    ftp.cwd("/")
    for part in remote_dir.replace("\\", "/").split("/"):
        if not part:
            continue
        try:
            ftp.cwd(part)
        except ftplib.error_perm:
            ftp.mkd(part)
            ftp.cwd(part)


def ftp_upload_bytes(remote_path, data_bytes, ftp=None):
    remote_path = remote_path.replace("\\", "/")
    dirname = os.path.dirname(remote_path)
    filename = os.path.basename(remote_path)
    own = ftp is None
    if own:
        ftp = ftp_connect()
    ftp_cwd_mkd(ftp, dirname)
    bio = io.BytesIO(data_bytes)
    ftp.storbinary("STOR " + filename, bio)
    if own:
        ftp.quit()


def ftp_upload_file(local_path, remote_path, ftp=None):
    with open(local_path, "rb") as f:
        ftp_upload_bytes(remote_path, f.read(), ftp=ftp)


def ftp_upload_many(pairs):
    ftp = ftp_connect()
    try:
        for local_path, remote_path in pairs:
            ftp_upload_file(local_path, remote_path, ftp=ftp)
    finally:
        ftp.quit()


def ftp_download(remote_path):
    ftp = ftp_connect()
    bio = io.BytesIO()
    ftp.cwd("/")
    ftp.retrbinary("RETR " + remote_path.replace("\\", "/"), bio.write)
    ftp.quit()
    return bio.getvalue()


def clear_cache():
    cleared = []
    errors = []
    for cache_dir in ("system/storage/cache", "system/storage/cache/template"):
        ftp = ftp_connect()
        try:
            ftp.cwd(cache_dir)
            entries = []
            ftp.retrlines("LIST", entries.append)
            for line in entries:
                parts = line.split(None, 8)
                if len(parts) < 9:
                    continue
                name = parts[8]
                if name in (".", "..", "index.html"):
                    continue
                if line.startswith("d"):
                    continue
                try:
                    ftp.delete(name)
                    cleared.append(f"{cache_dir}/{name}")
                except ftplib.error_perm as e:
                    errors.append(f"{name}: {e}")
        except Exception as e:
            errors.append(f"{cache_dir}: {e}")
        finally:
            ftp.quit()
    return cleared, errors


def patch_header(content):
    if FA_LINK in content:
        return content, "already_present"
    m = re.search(r"<link[^>]+href=[\"']/assets/css/style\.css[\"'][^>]*>", content, re.I)
    if m:
        insert_at = m.start()
        return content[:insert_at] + FA_LINK + "\n" + content[insert_at:], "before_style_css"
    m = re.search(r"</head>", content, re.I)
    if m:
        return content[: m.start()] + FA_LINK + "\n" + content[m.start() :], "before_head_close"
    raise RuntimeError("Cannot find insertion point in header.twig")


def http_head(url):
    req = urllib.request.Request(url, method="HEAD", headers={"Cookie": "beget=begetok"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.status, dict(resp.headers)
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers)


def http_get(url):
    req = urllib.request.Request(url, headers={"Cookie": "beget=begetok"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.status, resp.read().decode("utf-8", "replace")


def extract_font_urls(css_text):
    return sorted(set(re.findall(r"url\(([^)]+\.woff2[^)]*)\)", css_text, re.I)))


def main():
    require_creds()
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    WORK.mkdir(parents=True, exist_ok=True)
    QA_DIR.mkdir(parents=True, exist_ok=True)

    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "backup_path": str(BACKUP_HEADER),
        "source_folder": str(FA_SRC),
        "uploaded_remote_paths": [],
        "header_changed": REMOTE_HEADER,
        "qa": {},
        "errors": [],
    }

    # TASK 1 — verify source files
    required = [
        FA_CSS_LOCAL,
        FA_WEBFONTS_LOCAL / "fa-solid-900.woff2",
        FA_WEBFONTS_LOCAL / "fa-regular-400.woff2",
        FA_WEBFONTS_LOCAL / "fa-brands-400.woff2",
    ]
    for p in required:
        if not p.exists():
            result["errors"].append(f"Missing source: {p}")
    light_candidates = list(FA_WEBFONTS_LOCAL.glob("fa-light-300.woff2")) + list(
        FA_WEBFONTS_LOCAL.glob("pro-fa-light-300*.woff2")
    )
    result["source_light_fonts"] = [str(p.name) for p in light_candidates[:5]]
    if result["errors"]:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        sys.exit(1)

    # BACKUP — download live header
    header_bytes = ftp_download(REMOTE_HEADER)
    BACKUP_HEADER.write_bytes(header_bytes)
    WORK_HEADER.write_bytes(header_bytes)
    result["backup_bytes"] = len(header_bytes)

    # TASK 2 — upload CSS + full webfonts (single FTP session)
    upload_pairs = [(FA_CSS_LOCAL, REMOTE_CSS)]
    webfont_files = sorted(p for p in FA_WEBFONTS_LOCAL.iterdir() if p.is_file())
    for wf in webfont_files:
        upload_pairs.append((wf, f"{REMOTE_WEBFONTS_DIR}/{wf.name}"))
    ftp_upload_many(upload_pairs)
    result["uploaded_remote_paths"] = [remote for _, remote in upload_pairs]
    result["webfonts_uploaded_count"] = len(webfont_files)

    # TASK 3 — patch and upload header
    header_text = WORK_HEADER.read_text(encoding="utf-8")
    patched, how = patch_header(header_text)
    WORK_HEADER.write_text(patched, encoding="utf-8")
    ftp_upload_bytes(REMOTE_HEADER, patched.encode("utf-8"))
    result["header_insertion"] = how

    cleared, cache_errors = clear_cache()
    result["cache_cleared"] = len(cleared)
    result["cache_errors"] = cache_errors

    # QA
    css_status, _ = http_head(f"{TEST_BASE}/{REMOTE_CSS}")
    result["qa"]["css_status"] = css_status

    css_body_status, css_text = http_get(f"{TEST_BASE}/{REMOTE_CSS}")
    result["qa"]["css_get_status"] = css_body_status
    font_urls = extract_font_urls(css_text)
    result["qa"]["css_font_refs_sample"] = font_urls[:8]
    result["qa"]["css_font_refs_total"] = len(font_urls)

    font_checks = []
    font_404 = []
    for ref in font_urls[:12]:
        ref_clean = ref.strip("\"'")
        if ref_clean.startswith("../webfonts/"):
            url = f"{TEST_BASE}/assets/vendor/fontawesome-pro-5.15.4/webfonts/{ref_clean.split('/')[-1]}"
        elif ref_clean.startswith("/"):
            url = f"{TEST_BASE}{ref_clean}"
        else:
            url = f"{TEST_BASE}/assets/vendor/fontawesome-pro-5.15.4/css/{ref_clean}"
        st, _ = http_head(url)
        font_checks.append({"ref": ref_clean, "url": url, "status": st})
        if st != 200:
            font_404.append(url)
    result["qa"]["font_head_checks"] = font_checks
    result["qa"]["font_404"] = font_404

    for name, url in URLS.items():
        st, html = http_get(url)
        has_link = FA_LINK.split("href=")[1].rstrip(">") in html or REMOTE_CSS in html
        result["qa"][f"page_{name}"] = {
            "url": url,
            "status": st,
            "fa_link_in_html": has_link,
        }

    key_fonts = [
        "fa-solid-900.woff2",
        "fa-regular-400.woff2",
        "fa-brands-400.woff2",
    ]
    for fname in key_fonts:
        url = f"{TEST_BASE}/assets/vendor/fontawesome-pro-5.15.4/webfonts/{fname}"
        st, _ = http_head(url)
        result["qa"][f"key_font_{fname}"] = st

    out = WORK / "fa-pro-install-result.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if css_status == 200 and not font_404 else 2


if __name__ == "__main__":
    sys.exit(main())
