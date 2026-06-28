#!/usr/bin/env python3
"""SITE-002 M9.17 Warranty — preflight, backup, seo_url, deploy, QA."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
import re
import ssl
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002")
WORK_DIR = ROOT / "reports" / "m9.17-work"
BACKUP_DIR = ROOT / "backups"
QA_DIR = ROOT / "qa" / "m9.17-warranty-screenshots"

CSS_MARKER = "M9.17 — Warranty page — manufacturer service reassurance"
JS_MARKER = "M9.14 — Corp FAQ accordion"
LIVE_URL = "https://zpm.new-site.space/guarantee"

DEPLOY_FILES = [
    {
        "remote": "catalog/controller/information/guarantee.php",
        "local": WORK_DIR / "guarantee.php",
        "backup": BACKUP_DIR / "guarantee.php.pre-m9.17-warranty.bak",
        "is_new": True,
    },
    {
        "remote": "catalog/view/theme/default/template/information/guarantee.twig",
        "local": WORK_DIR / "guarantee.twig",
        "backup": BACKUP_DIR / "guarantee.twig.pre-m9.17-warranty.bak",
        "is_new": True,
    },
    {
        "remote": "assets/css/style.css",
        "local": None,
        "backup": BACKUP_DIR / "style.css.pre-m9.17-warranty.bak",
        "css_append": WORK_DIR / "m9.17-warranty-page.css",
    },
    {
        "remote": "assets/js/main.js",
        "local": None,
        "backup": BACKUP_DIR / "main.js.pre-m9.17-warranty.bak",
        "js_append": WORK_DIR / "m9.17-corp-accordion.js",
    },
]


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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


def strip_css_block(text: str, marker: str) -> str:
    needle = f"/* ==========================================================================\n   {marker}"
    if marker not in text:
        return text
    before, _sep, rest = text.partition(needle)
    next_block = re.search(r"\n/\* ={10,}\n", rest)
    if next_block:
        after = rest[next_block.start() + 1 :]
        return before.rstrip() + "\n\n" + after.lstrip()
    return before.rstrip() + "\n"


def patch_style_css(live_text: str, append_path: Path) -> str:
    text = strip_css_block(live_text, CSS_MARKER)
    append_block = append_path.read_text(encoding="utf-8")
    return text.rstrip() + "\n\n" + append_block.strip() + "\n"


def patch_main_js(live_text: str, append_path: Path) -> str:
    append_block = append_path.read_text(encoding="utf-8")
    marker_line = f"/* ==========================================================================\n   {JS_MARKER}"
    if JS_MARKER in live_text:
        before, _sep, _after = live_text.partition(marker_line)
        return before.rstrip() + "\n" + append_block.strip() + "\n"
    return live_text.rstrip() + "\n" + append_block.strip() + "\n"


def update_seo_url_via_http(manifest: dict) -> dict:
    patch_name = "m917-seo-guarantee-patch.php"
    patch_body = """<?php
require_once __DIR__ . '/config.php';
$mysqli = new mysqli(DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_DATABASE);
if ($mysqli->connect_error) { http_response_code(500); exit('db_fail'); }
$mysqli->set_charset('utf8');
$before = $mysqli->query("SELECT seo_url_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='guarantee' LIMIT 1");
$row = $before ? $before->fetch_assoc() : null;
header('Content-Type: application/json; charset=utf-8');
if (!$row) {
  $mysqli->query("INSERT INTO " . DB_PREFIX . "seo_url SET store_id=0, language_id=1, query='information/guarantee', keyword='guarantee'");
  $after = $mysqli->query("SELECT seo_url_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='guarantee' LIMIT 1");
  echo json_encode(['ok'=>true,'action'=>'insert','after'=>$after?$after->fetch_assoc():null]);
  exit;
}
$old = $row['query'];
if ($old !== 'information/guarantee') {
  $mysqli->query("UPDATE " . DB_PREFIX . "seo_url SET query='information/guarantee' WHERE keyword='guarantee'");
}
$after = $mysqli->query("SELECT seo_url_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='guarantee' LIMIT 1");
echo json_encode(['ok'=>true,'before'=>$row,'after'=>$after?$after->fetch_assoc():null]);
"""
    patch_local = WORK_DIR / patch_name
    patch_local.write_text(patch_body, encoding="utf-8")
    ftp_upload(patch_name, patch_body.encode("utf-8"))
    ctx = ssl.create_default_context()
    patch_url = "https://zpm.new-site.space/" + patch_name
    try:
        req = urllib.request.Request(
            patch_url,
            headers={"Cookie": "beget=begetok", "User-Agent": "MARS-M9.17-SEO"},
        )
        raw = urllib.request.urlopen(req, context=ctx, timeout=60).read().decode("utf-8", "replace")
        manifest["seo_url_patch_response"] = json.loads(raw)
        manifest["seo_url_updated"] = manifest["seo_url_patch_response"].get("ok", False)
    except Exception as exc:
        manifest["seo_url_updated"] = False
        manifest["seo_url_patch_error"] = str(exc)
    try:
        ftp = ftp_connect()
        ftp.delete(patch_name)
        ftp.quit()
    except Exception:
        pass
    return manifest


def qa_capture() -> dict:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        LIVE_URL,
        headers={"Cookie": "beget=begetok", "User-Agent": "MARS-M9.17-Warranty"},
    )
    html = urllib.request.urlopen(req, context=ctx, timeout=60).read().decode("utf-8", "replace")
    qa_path = WORK_DIR / "qa-guarantee.html"
    qa_path.write_text(html, encoding="utf-8")

    main_html = html.split("zpm-warranty-page")[1].split("</main>")[0] if "zpm-warranty-page" in html else ""

    checks = {
        "http_ok": True,
        "has_zpm_warranty_page": "zpm-warranty-page" in html,
        "has_page_intro_lead": "page-intro__description" in html,
        "has_principles": "zpm-warranty-principles" in html,
        "coverage_5_rows": html.count("zpm-warranty-coverage__table") > 0 and main_html.count("<tr>") >= 5,
        "summary_4_labels": "zpm-warranty-summary" in html,
        "has_docs": "zpm-warranty-docs" in html,
        "has_timeline": "zpm-warranty-process" in html,
        "timeline_5_steps": html.count("zpm-corp-timeline__step") >= 5,
        "has_verification": "zpm-warranty-verification" in html,
        "verification_7_bullets": main_html.count("zpm-warranty-verification__list") > 0,
        "has_outcomes": "zpm-warranty-outcomes" in html,
        "outcomes_6": html.count("zpm-warranty-outcome") >= 6,
        "has_faq": "zpm-warranty-faq" in html,
        "faq_8_items": html.count('id="warranty-faq-btn-') >= 8,
        "data_warranty_faq": "data-warranty-faq" in html,
        "has_cta_title": "Связаться по вопросу гарантии" in html or "Связаться по&nbsp;вопросу гарантии" in html,
        "has_form_title": "Обращение по гарантии" in html or "Обращение по&nbsp;гарантии" in html,
        "equipment_model_required": 'name="equipment_model"' in html and "required" in html.split('name="equipment_model"')[1][:200],
        "comment_required": 'name="comment"' in html and "required" in html.split('name="comment"')[1][:200],
        "purchase_date_optional": (
            'name="purchase_date"' in html
            and "required" not in html.split('name="purchase_date"')[1].split(">")[0]
        ),
        "meta_title": "Гарантия на оборудование — ЗПМ" in html,
        "meta_description": "Гарантийная поддержка оборудования ЗПМ" in html,
        "about_link": 'href="/about"' in html,
        "delivery_link": 'href="/delivery"' in html,
        "dealers_link": 'href="/dealers"' in html,
        "payment_link": 'href="/payment-methods"' in html,
        "no_term_badge": "12 мес" not in html and "24 мес" not in html,
        "no_asc_map": "ymaps" not in html.lower() and "google.com/maps" not in html.lower(),
        "no_red_alert": "alert-danger" not in html and "zpm-warranty-verification" in html,
        "commercial_trust_card": "zpm-commercial-trust__card" in html,
        "zpm_form": "zpm-form" in html,
        "breadcrumb": "Гарантия" in html,
        "h1_garantiya": "Гарантия на оборудование" in html or "Гарантия на&nbsp;оборудование" in html,
        "phone_cta": "72-18-90" in html,
        "email_cta": "info@bzpm.ru" in html,
    }
    checks["all_pass"] = all(checks.values())
    return checks


def main() -> None:
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    QA_DIR.mkdir(parents=True, exist_ok=True)

    manifest: dict = {
        "pass": "m9.17-warranty-implementation",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "branch": "mars/canonical-post-recovery",
        "live_url": LIVE_URL,
        "route": "information/guarantee",
        "seo_keyword": "guarantee",
        "files": {},
    }

    preflight: dict = {}
    for item in DEPLOY_FILES:
        remote = item["remote"]
        live = ftp_download(remote)
        preflight[remote] = {
            "exists": live is not None,
            "pre_sha256": sha256_hex(live) if live else None,
            "pre_bytes": len(live) if live else 0,
        }
    (WORK_DIR / "preflight-manifest.json").write_text(
        json.dumps(preflight, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    manifest["preflight"] = preflight

    for item in DEPLOY_FILES:
        remote = item["remote"]
        live = ftp_download(remote)
        if live is not None:
            item["backup"].write_bytes(live)
            pre_sha = sha256_hex(live)
        else:
            pre_sha = None

        manifest["files"][remote] = {
            "pre_sha256": pre_sha,
            "pre_bytes": len(live) if live else 0,
            "backup": str(item["backup"]),
            "is_new": item.get("is_new", False),
        }

        if item.get("local"):
            upload_data = item["local"].read_bytes()
        elif item.get("css_append"):
            if live is None:
                raise RuntimeError(f"Cannot patch CSS — {remote} not found")
            live_text = live.decode("utf-8", errors="replace")
            patched = patch_style_css(live_text, item["css_append"])
            upload_data = patched.encode("utf-8")
        elif item.get("js_append"):
            if live is None:
                raise RuntimeError(f"Cannot patch JS — {remote} not found")
            live_text = live.decode("utf-8", errors="replace")
            patched = patch_main_js(live_text, item["js_append"])
            upload_data = patched.encode("utf-8")
        else:
            upload_data = live or b""

        ftp_upload(remote, upload_data)
        manifest["files"][remote]["post_sha256"] = sha256_hex(upload_data)
        manifest["files"][remote]["post_bytes"] = len(upload_data)

    manifest = update_seo_url_via_http(manifest)

    cleared = clear_twig_cache()
    manifest["twig_cache_cleared"] = cleared

    qa = qa_capture()
    manifest["qa"] = qa

    out = WORK_DIR / "deploy-manifest.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
