#!/usr/bin/env python3
"""SITE-002 M9.15 Payment — preflight, backup, seo_url, deploy, QA."""
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
WORK_DIR = ROOT / "reports" / "m9.15-work"
BACKUP_DIR = ROOT / "backups"
QA_DIR = ROOT / "qa" / "m9.15-payment-screenshots"

CSS_MARKER_NEW = "M9.15 — Payment page — corporate settlement"
CSS_MARKER_OLD = "M9.15 — Payment page — process-first redesign"
JS_MARKER = "M9.14 — Corp FAQ accordion"
LIVE_URL = "https://zpm.new-site.space/payment-methods"

DEPLOY_FILES = [
    {
        "remote": "catalog/controller/information/payment.php",
        "local": WORK_DIR / "payment.php",
        "backup": BACKUP_DIR / "payment.php.pre-m9.15-payment.bak",
        "is_new": True,
    },
    {
        "remote": "catalog/view/theme/default/template/information/payment.twig",
        "local": WORK_DIR / "payment.twig",
        "backup": BACKUP_DIR / "payment.twig.pre-m9.15-payment.bak",
        "is_new": True,
    },
    {
        "remote": "assets/css/style.css",
        "local": None,
        "backup": BACKUP_DIR / "style.css.pre-m9.15-payment.bak",
        "css_append": WORK_DIR / "m9.15-payment-page.css",
    },
    {
        "remote": "assets/js/main.js",
        "local": None,
        "backup": BACKUP_DIR / "main.js.pre-m9.15-payment.bak",
        "js_append": WORK_DIR / "m9.15-corp-accordion.js",
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
    text = strip_css_block(live_text, CSS_MARKER_OLD)
    text = strip_css_block(text, CSS_MARKER_NEW)
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
    patch_name = "m915-seo-payment-patch.php"
    patch_body = """<?php
require_once __DIR__ . '/config.php';
$mysqli = new mysqli(DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_DATABASE);
if ($mysqli->connect_error) { http_response_code(500); exit('db_fail'); }
$mysqli->set_charset('utf8');
$before = $mysqli->query("SELECT seo_url_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='payment-methods' LIMIT 1");
$row = $before ? $before->fetch_assoc() : null;
header('Content-Type: application/json; charset=utf-8');
if (!$row) {
  $mysqli->query("INSERT INTO " . DB_PREFIX . "seo_url SET store_id=0, language_id=1, query='information/payment', keyword='payment-methods'");
  $after = $mysqli->query("SELECT seo_url_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='payment-methods' LIMIT 1");
  echo json_encode(['ok'=>true,'action'=>'insert','after'=>$after?$after->fetch_assoc():null]);
  exit;
}
$old = $row['query'];
if ($old !== 'information/payment') {
  $mysqli->query("UPDATE " . DB_PREFIX . "seo_url SET query='information/payment' WHERE keyword='payment-methods'");
}
$after = $mysqli->query("SELECT seo_url_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='payment-methods' LIMIT 1");
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
            headers={"Cookie": "beget=begetok", "User-Agent": "MARS-M9.15-SEO"},
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
        headers={"Cookie": "beget=begetok", "User-Agent": "MARS-M9.15-Payment"},
    )
    html = urllib.request.urlopen(req, context=ctx, timeout=60).read().decode("utf-8", "replace")
    qa_path = WORK_DIR / "qa-payment.html"
    qa_path.write_text(html, encoding="utf-8")

    checks = {
        "http_ok": True,
        "has_zpm_payment_page": "zpm-payment-page" in html,
        "has_page_intro_lead": "page-intro__description" in html,
        "has_timeline": "zpm-payment-timeline" in html,
        "timeline_6_steps": html.count("zpm-corp-timeline__step") >= 6,
        "step6_preparation": "Подготовка к&nbsp;отгрузке" in html or "Подготовка к отгрузке" in html,
        "has_methods": "zpm-payment-methods" in html,
        "has_documents": "zpm-payment-documents" in html,
        "has_proof_cards": html.count("zpm-payment-proof-card") >= 5,
        "has_legal": "zpm-payment-legal" in html,
        "has_faq": "zpm-payment-faq" in html,
        "faq_8_items": html.count('id="payment-faq-btn-') >= 8,
        "has_cta_title": "Получить счёт или уточнить условия оплаты" in html,
        "has_form_title": "Запрос счёта или консультации" in html,
        "company_required": 'id="paymentCompany"' in html and "required" in html.split('id="paymentCompany"')[1][:200],
        "meta_title": "Оплата оборудования — ЗПМ" in html,
        "meta_description": "безналичный расчёт по счёту" in html,
        "delivery_link": 'href="/delivery"' in html,
        "no_bank_widgets": "visa" not in html.lower() and "mastercard" not in html.lower(),
        "no_qr": "qr-код" not in html.lower() and "qr code" not in html.lower(),
        "no_moscow_warehouse": "zpm-payment-page" in html and "Никольское" not in html.split("zpm-payment-page")[1].split("</main>")[0],
        "no_logistics_tk": "Деловые Линии" not in html and "zpm-delivery-carriers" not in html,
        "commercial_trust_card": "zpm-commercial-trust__card" in html,
        "zpm_form": "zpm-form" in html,
        "breadcrumb": "Оплата" in html,
        "h1_oplata": "page-intro__title" in html and "Оплата" in html,
    }
    checks["all_pass"] = all(checks.values())
    return checks


def main() -> None:
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    QA_DIR.mkdir(parents=True, exist_ok=True)

    manifest: dict = {
        "pass": "m9.15-payment-implementation",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "branch": "mars/canonical-post-recovery",
        "live_url": LIVE_URL,
        "route": "information/payment",
        "seo_keyword": "payment-methods",
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
            if not item.get("is_new"):
                raise RuntimeError(f"Expected existing remote file missing: {remote}")

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
