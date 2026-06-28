#!/usr/bin/env python3
"""SITE-002 M9.14 Delivery — preflight, backup, seo_url, deploy, QA."""
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
import http.cookiejar
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DB_USER = "polygonws_zpm"
DB_PASS = "VBCDry2bJ5P"

ROOT = Path(r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002")
WORK_DIR = ROOT / "reports" / "m9.14-work"
BACKUP_DIR = ROOT / "backups"
QA_DIR = ROOT / "qa" / "m9.14-delivery-screenshots"

CSS_MARKER = "M9.14 — Delivery page — corporate logistics"
JS_MARKER = "M9.14 — Corp FAQ accordion"
LIVE_URL = "https://zpm.new-site.space/delivery"

DEPLOY_FILES = [
    {
        "remote": "catalog/controller/information/delivery.php",
        "local": WORK_DIR / "delivery.php",
        "backup": BACKUP_DIR / "delivery.php.pre-m9.14-delivery.bak",
        "is_new": True,
    },
    {
        "remote": "catalog/view/theme/default/template/information/delivery.twig",
        "local": WORK_DIR / "delivery.twig",
        "backup": BACKUP_DIR / "delivery.twig.pre-m9.14-delivery.bak",
        "is_new": True,
    },
    {
        "remote": "assets/css/style.css",
        "local": None,
        "backup": BACKUP_DIR / "style.css.pre-m9.14-delivery.bak",
        "css_append": WORK_DIR / "m9.14-delivery-page.css",
    },
    {
        "remote": "assets/js/main.js",
        "local": None,
        "backup": BACKUP_DIR / "main.js.pre-m9.14-delivery.bak",
        "js_append": WORK_DIR / "m9.14-corp-accordion.js",
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


def patch_style_css(live_text: str, append_path: Path) -> str:
    append_block = append_path.read_text(encoding="utf-8")
    marker_line = f"/* ==========================================================================\n   {CSS_MARKER}"
    if CSS_MARKER in live_text:
        before, _sep, _after = live_text.partition(marker_line)
        return before.rstrip() + "\n\n" + append_block.strip() + "\n"
    return live_text.rstrip() + "\n\n" + append_block.strip() + "\n"


def patch_main_js(live_text: str, append_path: Path) -> str:
    append_block = append_path.read_text(encoding="utf-8")
    if JS_MARKER in live_text:
        before, _sep, _after = live_text.partition(f"/* ==========================================================================\n   {JS_MARKER}")
        return before.rstrip() + "\n" + append_block.strip() + "\n"
    return live_text.rstrip() + "\n" + append_block.strip() + "\n"


def pma_login():
    ctx = ssl.create_default_context()
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cj),
        urllib.request.HTTPSHandler(context=ctx),
    )
    lp = op.open(PMA + "/", timeout=60).read().decode("utf-8", "replace")
    token = re.search(r'name="token"\s+value="([^"]+)"', lp).group(1)
    op.open(
        urllib.request.Request(
            PMA + "/index.php",
            data=urllib.parse.urlencode(
                {
                    "pma_username": DB_USER,
                    "pma_password": DB_PASS,
                    "server": "1",
                    "target": "index.php",
                    "token": token,
                }
            ).encode(),
            method="POST",
        ),
        timeout=60,
    )
    db_page = op.open(
        PMA + "/db_structure.php?db=" + urllib.parse.quote(DB), timeout=60
    ).read().decode("utf-8", "replace")
    csrf = re.search(r'name="token"\s+value="([^"]+)"', db_page)
    return op, csrf.group(1) if csrf else token


def pma_sql(op, csrf, query: str) -> list[dict]:
    qdata = urllib.parse.urlencode(
        {"db": DB, "sql_query": query, "token": csrf, "sql_delimiter": ";"}
    ).encode()
    html = op.open(
        urllib.request.Request(PMA + "/sql.php", data=qdata, method="POST"),
        timeout=180,
    ).read().decode("utf-8", "replace")
    if "error" in html.lower() and "MySQL" in html:
        return [{"_error": html[:500]}]
    for tbl in re.findall(r"<table[^>]*>(.*?)</table>", html, re.S | re.I):
        trs = re.findall(r"<tr[^>]*>(.*?)</tr>", tbl, re.S | re.I)
        if len(trs) < 2:
            continue
        parsed = []
        for tr in trs:
            cells = [
                unescape(re.sub(r"<[^>]+>", " ", c).strip())
                for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S | re.I)
            ]
            cells = [re.sub(r"\s+", " ", c) for c in cells if c.strip()]
            if cells:
                parsed.append(cells)
        if len(parsed) >= 2 and len(parsed[0]) >= 2:
            hdr = parsed[0]
            if hdr[0].lower() in ("seo_url_id", "query", "keyword"):
                return [dict(zip(hdr, r)) for r in parsed[1:] if len(r) == len(hdr)]
    return []


def update_seo_url_via_http(manifest: dict) -> dict:
    patch_name = "m914-seo-delivery-patch.php"
    patch_local = WORK_DIR / patch_name
    patch_body = """<?php
require_once __DIR__ . '/config.php';
$mysqli = new mysqli(DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_DATABASE);
if ($mysqli->connect_error) { http_response_code(500); exit('db_fail'); }
$mysqli->set_charset('utf8');
$before = $mysqli->query("SELECT seo_url_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='delivery' LIMIT 1");
$row = $before ? $before->fetch_assoc() : null;
header('Content-Type: application/json; charset=utf-8');
if (!$row) { echo json_encode(['ok'=>false,'error'=>'no_row']); exit; }
$old = $row['query'];
if ($old !== 'information/delivery') {
  $mysqli->query("UPDATE " . DB_PREFIX . "seo_url SET query='information/delivery' WHERE keyword='delivery'");
}
$after = $mysqli->query("SELECT seo_url_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='delivery' LIMIT 1");
echo json_encode(['ok'=>true,'before'=>$row,'after'=>$after?$after->fetch_assoc():null]);
"""
    patch_local.write_text(patch_body, encoding="utf-8")
    ftp_upload(patch_name, patch_body.encode("utf-8"))
    ctx = ssl.create_default_context()
    patch_url = "https://zpm.new-site.space/" + patch_name
    try:
        req = urllib.request.Request(
            patch_url,
            headers={"Cookie": "beget=begetok", "User-Agent": "MARS-M9.14-SEO"},
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


def update_seo_url(manifest: dict) -> dict:
    try:
        return update_seo_url_via_http(manifest)
    except Exception as exc:
        manifest["seo_url_updated"] = False
        manifest["seo_url_error"] = str(exc)
        return manifest


def qa_capture() -> dict:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        LIVE_URL,
        headers={"Cookie": "beget=begetok", "User-Agent": "MARS-M9.14-Delivery"},
    )
    html = urllib.request.urlopen(req, context=ctx, timeout=60).read().decode("utf-8", "replace")
    qa_path = WORK_DIR / "qa-delivery.html"
    qa_path.write_text(html, encoding="utf-8")

    checks = {
        "http_ok": True,
        "has_zpm_delivery_page": "zpm-delivery-page" in html,
        "has_page_intro_lead": "page-intro__description" in html,
        "has_shipment_points": "zpm-delivery-points" in html,
        "has_timeline": "zpm-delivery-timeline" in html,
        "timeline_7_steps": html.count("zpm-corp-timeline__step") >= 7,
        "has_faq": "zpm-delivery-faq" in html,
        "faq_8_items": html.count("data-accordion-button") >= 8,
        "has_cta_title": "Уточнить условия поставки для вашего региона" in html,
        "has_form_title": "Запрос по доставке" in html,
        "region_required": 'id="deliveryRegion"' in html and "required" in html.split('id="deliveryRegion"')[1][:200],
        "meta_title": "Доставка оборудования — ЗПМ" in html,
        "meta_description": "отгрузка из Барнаула" in html,
        "payment_link": 'href="/payment-methods"' in html,
        "no_basovskaya": "Басовская" not in html,
        "no_map": "ymaps" not in html.lower() and 'class="yandex-map' not in html,
        "no_calculator": "калькулятор" not in html.lower(),
        "nikolskoye_address": "Никольское" in html and "204" in html,
        "commercial_trust_card": "zpm-commercial-trust__card" in html,
        "zpm_form": "zpm-form" in html,
        "breadcrumb": "Доставка" in html,
    }
    checks["all_pass"] = all(checks.values())
    return checks


def main() -> None:
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    manifest: dict = {
        "pass": "m9.14-delivery-implementation",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "branch": "mars/canonical-post-recovery",
        "live_url": LIVE_URL,
        "route": "information/delivery",
        "files": {},
    }

    # Preflight capture for existing files
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

    # Deploy files
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

    # SEO URL migration (after controller exists)
    manifest = update_seo_url(manifest)

    cleared = clear_twig_cache()
    manifest["twig_cache_cleared"] = cleared

    qa = qa_capture()
    manifest["qa"] = qa

    out = WORK_DIR / "deploy-manifest.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
