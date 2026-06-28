#!/usr/bin/env python3
"""SITE-002 M9.18 Custom Manufacturing — preflight, backup, seo_url, deploy, QA."""
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
WORK_DIR = ROOT / "reports" / "m9.18-work"
BACKUP_DIR = ROOT / "backups"
QA_DIR = ROOT / "qa" / "m9.18-custom-screenshots"

CSS_MARKER = "M9.18 — Custom Manufacturing page — manufacturer capability"
JS_MARKER = "M9.14 — Corp FAQ accordion"
LIVE_URL = "https://zpm.new-site.space/custom-equipment"

DEPLOY_FILES = [
    {
        "remote": "catalog/controller/information/custom_equipment.php",
        "local": WORK_DIR / "custom_equipment.php",
        "backup": BACKUP_DIR / "custom_equipment.php.pre-m9.18-custom.bak",
        "is_new": True,
    },
    {
        "remote": "catalog/view/theme/default/template/information/custom_equipment.twig",
        "local": WORK_DIR / "custom_equipment.twig",
        "backup": BACKUP_DIR / "custom_equipment.twig.pre-m9.18-custom.bak",
        "is_new": True,
    },
    {
        "remote": "assets/css/style.css",
        "local": None,
        "backup": BACKUP_DIR / "style.css.pre-m9.18-custom.bak",
        "css_append": WORK_DIR / "m9.18-custom-page.css",
    },
    {
        "remote": "assets/js/main.js",
        "local": None,
        "backup": BACKUP_DIR / "main.js.pre-m9.18-custom.bak",
        "js_append": WORK_DIR / "m9.18-corp-accordion.js",
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


def capture_live_baseline() -> None:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        LIVE_URL,
        headers={"Cookie": "beget=begetok", "User-Agent": "MARS-M9.18-preflight"},
    )
    html = urllib.request.urlopen(req, context=ctx, timeout=60).read().decode("utf-8", "replace")
    (WORK_DIR / "custom-equipment-live.html").write_text(html, encoding="utf-8")


def update_seo_url_via_http(manifest: dict) -> dict:
    patch_name = "m918-seo-custom-patch.php"
    patch_body = """<?php
require_once __DIR__ . '/config.php';
$mysqli = new mysqli(DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_DATABASE);
if ($mysqli->connect_error) { http_response_code(500); exit('db_fail'); }
$mysqli->set_charset('utf8');
$before = $mysqli->query("SELECT seo_url_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='custom-equipment' LIMIT 1");
$row = $before ? $before->fetch_assoc() : null;
header('Content-Type: application/json; charset=utf-8');
if (!$row) {
  $mysqli->query("INSERT INTO " . DB_PREFIX . "seo_url SET store_id=0, language_id=1, query='information/custom_equipment', keyword='custom-equipment'");
  $after = $mysqli->query("SELECT seo_url_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='custom-equipment' LIMIT 1");
  echo json_encode(['ok'=>true,'action'=>'insert','after'=>$after?$after->fetch_assoc():null]);
  exit;
}
$old = $row['query'];
if ($old !== 'information/custom_equipment') {
  $mysqli->query("UPDATE " . DB_PREFIX . "seo_url SET query='information/custom_equipment' WHERE keyword='custom-equipment'");
}
$after = $mysqli->query("SELECT seo_url_id, query, keyword FROM " . DB_PREFIX . "seo_url WHERE keyword='custom-equipment' LIMIT 1");
echo json_encode(['ok'=>true,'before'=>$row,'after'=>$after?$after->fetch_assoc():null]);
"""
    ftp_upload(patch_name, patch_body.encode("utf-8"))
    ctx = ssl.create_default_context()
    patch_url = "https://zpm.new-site.space/" + patch_name
    try:
        req = urllib.request.Request(
            patch_url,
            headers={"Cookie": "beget=begetok", "User-Agent": "MARS-M9.18-SEO"},
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


def clear_opencart_cache_via_http(manifest: dict) -> dict:
    patch_name = "m918-custom-cache-clear.php"
    patch_body = """<?php
require_once __DIR__ . '/config.php';
header('Content-Type: application/json; charset=utf-8');
$cleared = 0;
$cacheDir = DIR_STORAGE . 'cache/';
foreach (glob($cacheDir . '*') as $f) {
  if (is_file($f)) { @unlink($f); $cleared++; }
}
echo json_encode(['ok'=>true,'cache_files_cleared'=>$cleared]);
"""
    ftp_upload(patch_name, patch_body.encode("utf-8"))
    ctx = ssl.create_default_context()
    try:
        req = urllib.request.Request(
            "https://zpm.new-site.space/" + patch_name,
            headers={"Cookie": "beget=begetok", "User-Agent": "MARS-M9.18-cache"},
        )
        raw = urllib.request.urlopen(req, context=ctx, timeout=60).read().decode("utf-8", "replace")
        manifest["opencart_cache_clear"] = json.loads(raw)
    except Exception as exc:
        manifest["opencart_cache_clear"] = {"ok": False, "error": str(exc)}
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
        headers={"Cookie": "beget=begetok", "User-Agent": "MARS-M9.18-Custom"},
    )
    html = urllib.request.urlopen(req, context=ctx, timeout=60).read().decode("utf-8", "replace")
    qa_path = WORK_DIR / "qa-custom-equipment.html"
    qa_path.write_text(html, encoding="utf-8")

    main_html = html.split("zpm-custom-page")[1].split("</main>")[0] if "zpm-custom-page" in html else ""

    checks = {
        "http_ok": True,
        "has_zpm_custom_page": "zpm-custom-page" in html,
        "has_page_intro_lead": "page-intro__description" in html,
        "has_triggers": "zpm-custom-triggers" in html,
        "triggers_5_bullets": main_html.count("<li>") >= 5 if "zpm-custom-triggers" in main_html else False,
        "has_tasks_matrix": "zpm-custom-tasks" in html,
        "tasks_7_rows": main_html.count("zpm-custom-tasks__table") > 0,
        "has_scope": "zpm-custom-scope" in html,
        "has_oem": "zpm-custom-oem" in html,
        "oem_5_h3": main_html.count("zpm-custom-oem__title") >= 5,
        "has_process": "zpm-custom-process" in html,
        "timeline_8_steps": html.count("zpm-corp-timeline__step") >= 8,
        "approval_badge": "Согласование до производства" in html,
        "has_requirements": "zpm-custom-requirements" in html,
        "checklist_9_rows": main_html.count("zpm-custom-requirements__table") > 0,
        "has_materials": "zpm-custom-materials" in html,
        "no_grade_table_hero": "AISI" not in main_html.split("zpm-custom-materials")[1].split("zpm-custom-outcomes")[0] if "zpm-custom-materials" in main_html else True,
        "has_outcomes": "zpm-custom-outcomes" in html,
        "outcomes_5_rows": main_html.count("zpm-custom-outcomes__table") > 0,
        "has_faq": "zpm-custom-faq" in html,
        "faq_8_items": html.count('id="custom-faq-btn-') >= 8,
        "data_custom_faq": "data-custom-faq" in html,
        "has_cta_title": "Получить расчёт изделия под ваш объект" in html,
        "has_form_title": "Заявка на расчёт" in html or "Заявка на&nbsp;расчёт" in html,
        "company_required": 'name="company"' in html and "required" in html.split('name="company"')[1][:200],
        "contact_required": 'name="contact"' in html and "required" in html.split('name="contact"')[1][:200],
        "project_description_required": 'name="project_description"' in html and "required" in html.split('name="project_description"')[1][:200],
        "phone_mask": 'data-mask="phone"' in html,
        "email_validate": 'data-validate="email"' in html,
        "drawings_optional": 'name="drawings"' in html,
        "notes_optional": 'name="notes"' in html,
        "no_file_upload": 'type="file"' not in html,
        "no_calculator": "calculator" not in html.lower() or "zpm-custom" in html,
        "dialog_7": 'name="dialog" value="7"' in html,
        "meta_title": "Оборудование на заказ" in html,
        "payment_link_step5": 'href="/payment-methods"' in html,
        "delivery_link_step8": 'href="/delivery"' in html,
        "guarantee_link": 'href="/guarantee"' in html,
        "about_link": 'href="/about"' in html,
        "privacy_link": 'href="/privacy-policy"' in html,
        "commercial_trust_card": "zpm-commercial-trust__card" in html,
        "zpm_form": "zpm-form" in html,
        "breadcrumb": "Оборудование на заказ" in html,
        "phone_cta": "72-18-90" in html,
        "email_cta": "info@bzpm.ru" in html,
        "dealers_pointer": 'href="/dealers"' in html,
        "no_zpm_seo_body": 'class="zpm-seo"' not in main_html,
    }
    checks["all_pass"] = all(v for k, v in checks.items() if k != "all_pass")
    return checks


def main() -> None:
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    QA_DIR.mkdir(parents=True, exist_ok=True)

    capture_live_baseline()

    manifest: dict = {
        "pass": "m9.18-custom-implementation",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "branch": "mars/canonical-post-recovery",
        "expected_head_note": "26e09732 or descendant — verify at git checkpoint",
        "live_url": LIVE_URL,
        "route": "information/custom_equipment",
        "seo_keyword": "custom-equipment",
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

    manifest = clear_opencart_cache_via_http(manifest)

    qa = qa_capture()
    manifest["qa"] = qa

    out = WORK_DIR / "deploy-manifest.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
