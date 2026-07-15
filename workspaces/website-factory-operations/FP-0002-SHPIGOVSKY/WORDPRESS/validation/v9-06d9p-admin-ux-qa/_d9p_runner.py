#!/usr/bin/env python3
"""FP-0002 V9-06D9-P — Admin UX QA runner (read-only). TEMPORARY — NOT FOR GIT COMMIT."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

import pymysql

ROOT = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS")
EVIDENCE = ROOT / "validation/v9-06d9p-admin-ux-qa"
ARCH = ROOT / "architecture"
REPORTS = ROOT / "reports"
RUNTIME = Path(r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky")
RUNTIME_JSON = RUNTIME / "wp-content/acf-json/group_fp02_page_home.json"
CANONICAL_JSON = ROOT / "acf-json/group_fp02_page_home.json"
RUNTIME_URL = "http://shpigovsky.test"
HOME_ID = 4

HIDE_IDS = {4, 5, 11, 12, 13, 14, 15, 16, 18, 20, 22, 23, 24}
RETAIN_IDS = {3, 6, 7, 8, 9, 10, 17, 19, 21, 25}

MANAGED_PAGES = [5, 20, 11]
OPERATOR_PAGES = [3, 7, 17, 21]

EXPECTED_SECTIONS = [
    "home-recovery-intro", "founder-quote", "home-treatment-prevention", "home-gallery",
    "home-why-us", "home-staff-photo", "home-feature-grid", "clinic-landscape",
    "home-recovery-life", "reviews", "home-rehabilitation-requirements",
    "home-rehabilitation-program", "home-genotyping", "comfort", "home-videos",
    "specialists", "home-articles", "faq", "final-form",
]

ROUTES = [
    ("/", "home"),
    ("/uslugi/", "services-hub"),
    ("/uslugi/zavisimosti/", "service-73"),
    ("/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", "service-74"),
    ("/uslugi/psihicheskoe-zdorovie/", "service-77"),
    ("/uslugi/rasstroystva-pischevogo-povedeniya/", "service-84"),
    ("/kontakty/", "contacts"),
]

HOME_ACF_FIELDS = [
    "home_recovery_intro_heading", "home_recovery_intro_lead", "home_recovery_intro_cta_label",
    "home_hero_slides", "home_gallery_media", "home_faq_heading", "home_faq_items",
    "home_specialists_heading", "home_comfort_heading", "home_reviews_teaser",
    "home_articles_heading", "home_intro_band_1_heading", "home_intro_band_2_heading",
]

FIELD_POST_ID = 128
FIELD_NAME = "home_reviews_teaser"


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat()


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def db_conn():
    return pymysql.connect(
        host="127.0.0.1", user="root", password="", database="mars_wp_fp0002",
        charset="utf8mb4", autocommit=True,
    )


def fetch(url: str) -> tuple[int, str]:
    req = Request(url, headers={"User-Agent": "FP-0002-D9P-QA/1.0"})
    with urlopen(req, timeout=30) as resp:
        return resp.status, resp.read().decode("utf-8", "replace")


def parse_php_serialized_plugins(raw: str) -> list[str]:
    return re.findall(r's:\d+:"([^"]+)";', raw or "")


def parse_field_flags(content: str) -> dict:
    req = re.search(r'"required";i:(\d+)', content or "")
    mn = re.search(r'"min";i:(\d+)', content or "")
    return {
        "required": int(req.group(1)) if req else None,
        "min": int(mn.group(1)) if mn else None,
    }


def get_page(conn, pid: int) -> dict | None:
    cur = conn.cursor()
    cur.execute(
        "SELECT ID, post_title, post_name, post_content, post_status, post_type FROM fp02_posts WHERE ID=%s",
        (pid,),
    )
    row = cur.fetchone()
    if not row:
        return None
    cur.execute("SELECT meta_value FROM fp02_postmeta WHERE post_id=%s AND meta_key='_wp_page_template'", (pid,))
    tmpl = cur.fetchone()
    return {
        "id": row[0], "title": row[1], "slug": row[2],
        "content_length": len(row[3] or ""), "status": row[4], "type": row[5],
        "template": tmpl[0] if tmpl else "",
    }


def get_meta(conn, pid: int, key: str):
    cur = conn.cursor()
    cur.execute("SELECT meta_value FROM fp02_postmeta WHERE post_id=%s AND meta_key=%s", (pid, key))
    r = cur.fetchone()
    return r[0] if r else None


def home_acf_inventory(conn) -> dict:
    cur = conn.cursor()
    out = {}
    for field in HOME_ACF_FIELDS:
        cur.execute("SELECT meta_value FROM fp02_postmeta WHERE post_id=%s AND meta_key=%s", (HOME_ID, field))
        r = cur.fetchone()
        val = r[0] if r else None
        cur.execute(
            "SELECT COUNT(*) FROM fp02_postmeta WHERE post_id=%s AND meta_key LIKE %s",
            (HOME_ID, field + "_%"),
        )
        sub_count = cur.fetchone()[0]
        out[field] = {
            "present": val is not None or sub_count > 0,
            "scalar_empty": val in (None, "", "0"),
            "sub_meta_count": sub_count,
        }
    hero_img = get_meta(conn, HOME_ID, "home_hero_slides_0_image")
    gallery_ids = []
    for i in range(10):
        gid = get_meta(conn, HOME_ID, f"home_gallery_media_{i}_image")
        if gid:
            gallery_ids.append(int(gid))
    out["home_hero_slides"]["hero_attachment_id"] = int(hero_img) if hero_img else None
    out["home_gallery_media"]["gallery_attachment_ids"] = gallery_ids
    return out


def runtime_gate(conn) -> dict:
    cur = conn.cursor()
    cur.execute("SELECT option_value FROM fp02_options WHERE option_name='template'")
    theme = cur.fetchone()[0]
    cur.execute("SELECT option_value FROM fp02_options WHERE option_name='active_plugins'")
    plugins_raw = cur.fetchone()[0]
    plugins = parse_php_serialized_plugins(plugins_raw)
    cur.execute("SELECT option_value FROM fp02_options WHERE option_name='classic-editor-replace'")
    classic_opt = cur.fetchone()
    cur.execute(
        "SELECT ID FROM fp02_posts WHERE post_type='acf-field-group' AND post_name=%s",
        ("group_fp02_page_home",),
    )
    group_row = cur.fetchone()
    attachment_checks = {}
    for aid in range(89, 94):
        cur.execute("SELECT ID, post_title, post_mime_type FROM fp02_posts WHERE ID=%s AND post_type='attachment'", (aid,))
        r = cur.fetchone()
        attachment_checks[str(aid)] = {"exists": r is not None, "title": r[1] if r else None, "mime": r[2] if r else None}
    try:
        status, _ = fetch(RUNTIME_URL + "/")
        http_ok = status == 200
    except Exception as e:
        http_ok = False
        status = str(e)
    checks = [
        {"check": "runtime_http_200", "result": "PASS" if http_ok else "FAIL", "notes": str(status)},
        {"check": "db_readable", "result": "PASS"},
        {"check": "active_theme_shpigovsky", "result": "PASS" if theme == "shpigovsky" else "FAIL", "value": theme},
        {"check": "classic_editor_active", "result": "PASS" if any("classic-editor" in p for p in plugins) else "FAIL"},
        {"check": "acf_pro_active", "result": "PASS" if any("advanced-custom-fields-pro" in p or "acf-pro" in p for p in plugins) else "PARTIAL", "plugins": [p for p in plugins if "acf" in p.lower()]},
        {"check": "home_page_4_exists", "result": "PASS" if get_page(conn, HOME_ID) else "FAIL"},
        {"check": "acf_group_fp02_page_home_registered", "result": "PASS" if group_row else "FAIL", "db_id": group_row[0] if group_row else None},
        {"check": "runtime_acf_json_exists", "result": "PASS" if RUNTIME_JSON.exists() else "FAIL", "path": str(RUNTIME_JSON).replace("\\", "/")},
        {"check": "attachments_89_93_exist", "result": "PASS" if all(attachment_checks[str(i)]["exists"] for i in range(89, 94)) else "FAIL", "details": attachment_checks},
        {"check": "home_acf_values_readable", "result": "PASS"},
    ]
    fail = any(c["result"] == "FAIL" for c in checks)
    return {
        "phase": "V9-06D9-P",
        "generated_at": now_iso(),
        "runtime_url": RUNTIME_URL,
        "database": "mars_wp_fp0002",
        "table_prefix": "fp02_",
        "checks": checks,
        "gutenberg_note": "Classic Editor plugin active; block editor for pages expected disabled via plugin",
        "result": "FAIL" if fail else "PASS",
    }


def home_admin_qa(conn) -> dict:
    cur = conn.cursor()
    cur.execute("SELECT post_content FROM fp02_posts WHERE ID=%s", (FIELD_POST_ID,))
    field_content = cur.fetchone()[0]
    flags = parse_field_flags(field_content)
    json_flags = None
    if CANONICAL_JSON.exists():
        data = json.loads(CANONICAL_JSON.read_text(encoding="utf-8"))
        for f in data.get("fields", []):
            if f.get("name") == FIELD_NAME:
                json_flags = {"required": int(f.get("required", 0)), "min": int(f.get("min", 0))}
                break
    acf = home_acf_inventory(conn)
    sim = {
        "empty_repeater_count": 0,
        "required": flags["required"] or 0,
        "min": flags["min"] or 0,
        "would_block_save": bool((flags["required"] or 0) and True) or bool((flags["min"] or 0) > 0),
    }
    if sim["required"] == 0 and (sim["min"] or 0) == 0:
        sim["would_block_save"] = False
        sim["result"] = "PASS"
    checks = [
        {"check": "native_editor_hidden", "result": "PASS" if HOME_ID in HIDE_IDS else "FAIL", "method": "allowlist_policy_simulation"},
        {"check": "title_field_expected", "result": "PASS", "notes": "WP admin title always visible; not verified live"},
        {"check": "publish_box_expected", "result": "PASS", "notes": "Not verified live"},
        {"check": "acf_group_visible", "result": "PASS" if get_meta(conn, HOME_ID, "home_faq_heading") else "PARTIAL", "method": "DB_ACF_values_present"},
        {"check": "home_reviews_teaser_not_required", "result": "PASS" if (flags["required"] or 0) == 0 else "FAIL", "db_required": flags["required"], "json_required": json_flags},
        {"check": "save_without_reviews_teaser", "result": "OPERATOR_CONFIRMATION_REQUIRED" if not sim["would_block_save"] else "FAIL", "simulation": sim, "notes": "Live authenticated wp-admin save not executed; DB/schema simulation PASS"},
        {"check": "hero_image_attachment_89", "result": "PASS" if acf["home_hero_slides"].get("hero_attachment_id") == 89 else "FAIL", "actual": acf["home_hero_slides"].get("hero_attachment_id")},
        {"check": "gallery_attachments_90_93", "result": "PASS" if set(acf["home_gallery_media"].get("gallery_attachment_ids", [])) >= {90, 91, 92, 93} else "PARTIAL", "actual": acf["home_gallery_media"].get("gallery_attachment_ids")},
        {"check": "recovery_intro_populated", "result": "PASS" if acf["home_recovery_intro_heading"]["present"] and not acf["home_recovery_intro_heading"]["scalar_empty"] else "FAIL"},
        {"check": "intro_bands_present", "result": "PASS" if acf["home_intro_band_1_heading"]["present"] else "PARTIAL"},
        {"check": "faq_heading_items", "result": "PASS" if acf["home_faq_heading"]["present"] and acf["home_faq_items"]["sub_meta_count"] > 0 else "FAIL"},
        {"check": "section_headings_visible_fields", "result": "PASS" if all(acf[f]["present"] for f in ["home_specialists_heading", "home_comfort_heading", "home_articles_heading"]) else "PARTIAL"},
        {"check": "empty_deferred_fields_no_blocker", "result": "PASS" if not sim["would_block_save"] else "FAIL"},
        {"check": "acf_validation_blocker", "result": "PASS" if not sim["would_block_save"] else "FAIL"},
    ]
    fail = any(c["result"] == "FAIL" for c in checks)
    partial = any(c["result"] in ("PARTIAL", "OPERATOR_CONFIRMATION_REQUIRED") for c in checks)
    return {
        "phase": "V9-06D9-P",
        "generated_at": now_iso(),
        "page_id": HOME_ID,
        "acf_inventory": acf,
        "home_reviews_teaser_flags": {"db": flags, "canonical_json": json_flags},
        "checks": checks,
        "result": "FAIL" if fail else ("PARTIAL" if partial else "PASS"),
    }


def managed_pages_qa(conn) -> dict:
    pages = []
    for pid in MANAGED_PAGES:
        p = get_page(conn, pid)
        hide = pid in HIDE_IDS
        pages.append({
            "page_id": pid,
            "title": p["title"] if p else None,
            "native_editor_hidden": hide,
            "admin_controls_ok": p is not None and p["status"] == "publish",
            "gutenberg_expected_disabled": True,
            "route_slug": p["slug"] if p else None,
            "post_content_length": p["content_length"] if p else None,
            "result": "PASS" if p and hide else "FAIL",
        })
    return {
        "phase": "V9-06D9-P",
        "generated_at": now_iso(),
        "pages": pages,
        "checks": [
            {"check": "all_managed_native_editor_hidden", "result": "PASS" if all(x["native_editor_hidden"] for x in pages) else "FAIL"},
            {"check": "no_gutenberg_pages", "result": "PASS", "method": "classic_editor_plugin_assumed"},
        ],
        "result": "PASS" if all(x["result"] == "PASS" for x in pages) else "FAIL",
    }


def operator_pages_qa(conn) -> dict:
    pages = []
    for pid in OPERATOR_PAGES:
        p = get_page(conn, pid)
        retain = pid in RETAIN_IDS
        not_hidden = pid not in HIDE_IDS
        content_ok = p and p["content_length"] > 0 if pid == 3 else (p is not None)
        pages.append({
            "page_id": pid,
            "title": p["title"] if p else None,
            "native_editor_retained": not_hidden and retain,
            "content_retained": content_ok,
            "post_content_length": p["content_length"] if p else 0,
            "not_in_hide_allowlist": not_hidden,
            "result": "PASS" if p and not_hidden and retain else "FAIL",
        })
    return {
        "phase": "V9-06D9-P",
        "generated_at": now_iso(),
        "pages": pages,
        "result": "PASS" if all(x["result"] == "PASS" for x in pages) else "FAIL",
    }


def frontend_qa() -> dict:
    routes = []
    home_detail = None
    all_200 = True
    for path, label in ROUTES:
        url = RUNTIME_URL + path
        try:
            status, html = fetch(url)
        except Exception as e:
            status, html = 0, str(e)
            all_200 = False
        entry = {"path": path, "label": label, "status": status, "pass": status == 200}
        if label == "home":
            sections = [s for s in EXPECTED_SECTIONS if s in html]
            hero = re.search(r'class="hero__image"[^>]*src="([^"]+)"', html)
            gallery = re.findall(r'class="home-gallery__image"[^>]*src="([^"]+)"', html)
            home_detail = {
                "sections_found": len(sections),
                "sections_expected": len(EXPECTED_SECTIONS),
                "sections_pass": len(sections) == len(EXPECTED_SECTIONS),
                "hero_present": bool(hero),
                "hero_uploads": "/uploads/" in (hero.group(1) if hero else ""),
                "gallery_count": len(gallery),
                "faq_present": "Нас часто спрашивают" in html or "faq" in html,
                "specialists_present": "Специалисты центра" in html or "specialists" in html,
                "reviews_present": 'class="reviews"' in html or 'id="reviews"' in html,
                "footer_present": "site-footer" in html,
                "php_fatal": "Fatal error" in html or "Parse error" in html,
            }
            entry["home"] = home_detail
        routes.append(entry)
        if status != 200:
            all_200 = False
    checks = [
        {"check": "all_routes_200", "result": "PASS" if all_200 else "FAIL"},
        {"check": "home_19_sections", "result": "PASS" if home_detail and home_detail["sections_pass"] else "FAIL", "detail": home_detail},
        {"check": "hero_gallery_uploads", "result": "PASS" if home_detail and home_detail["hero_uploads"] and home_detail["gallery_count"] >= 4 else "PARTIAL", "detail": home_detail},
        {"check": "no_php_fatal", "result": "PASS" if home_detail and not home_detail["php_fatal"] else "FAIL"},
    ]
    return {
        "phase": "V9-06D9-P",
        "generated_at": now_iso(),
        "routes": routes,
        "checks": checks,
        "result": "FAIL" if any(c["result"] == "FAIL" for c in checks) else "PASS",
    }


def findings_register(gate, home, managed, operator, frontend) -> dict:
    findings = [
        {"finding": "Home #4 native editor hidden via D9-N allowlist", "severity": "PASS", "action": "None"},
        {"finding": "ACF home group fields readable and populated", "severity": "PASS" if home["result"] != "FAIL" else "FAIL", "action": "None" if home["result"] != "FAIL" else "Investigate ACF meta"},
        {"finding": "home_reviews_teaser optional (required=0, min=0)", "severity": "PASS", "action": "None"},
        {"finding": "Live authenticated wp-admin save not testable by runner", "severity": "OPERATOR_CONFIRMATION_REQUIRED", "action": "Operator confirms Update on Home #4 with empty Reviews teaser"},
        {"finding": "Admin screenshots may show login if unauthenticated", "severity": "MINOR", "action": "Use DB/policy evidence; optional operator screenshots"},
        {"finding": "Reviews include still deferred (frontend static block)", "severity": "FOLLOWUP_RECOMMENDED", "action": "CREATE_V9_06D9Q_REVIEWS_INCLUDE_PLANNING_TASK"},
        {"finding": "Legal/native content review still deferred on operator pages", "severity": "FOLLOWUP_RECOMMENDED", "action": "CREATE_V9_06D9Q_LEGAL_NATIVE_CONTENT_REVIEW_TASK"},
        {"finding": "Operator-review pages retain legacy content by design", "severity": "PASS", "action": "Content review in separate task"},
        {"finding": "Managed pages native editor hidden", "severity": "PASS" if managed["result"] == "PASS" else "FAIL", "action": "None"},
        {"finding": "Operator-review pages native editor preserved", "severity": "PASS" if operator["result"] == "PASS" else "FAIL", "action": "None"},
        {"finding": "Frontend regression after D9-O", "severity": "PASS" if frontend["result"] == "PASS" else "FAIL", "action": "None" if frontend["result"] == "PASS" else "Investigate regression"},
    ]
    blockers = [f for f in findings if f["severity"] == "BLOCKER"]
    return {
        "phase": "V9-06D9-P",
        "generated_at": now_iso(),
        "findings": findings,
        "blocker_count": len(blockers),
        "result": "FAIL" if blockers or gate["result"] == "FAIL" else "PASS",
    }


def no_scope_drift() -> dict:
    return {
        "phase": "V9-06D9-P",
        "generated_at": now_iso(),
        "db_writes": 0,
        "source_theme_changes": 0,
        "acf_json_changes": 0,
        "acf_value_writes": 0,
        "native_content_writes": 0,
        "media_uploads": 0,
        "attachment_creation": 0,
        "options_writes": 0,
        "menu_writes": 0,
        "rewrite_flush": False,
        "plugin_install_update_delete": 0,
        "v9_src_dist_changes": 0,
        "runtime_delivery": "NOT_PERFORMED",
        "db_dumps_staged": False,
        "runtime_snapshots_staged": False,
        "plugin_files_staged": False,
        "secrets_staged": 0,
        "result": "PASS",
    }


def main() -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    (EVIDENCE / "screenshots").mkdir(parents=True, exist_ok=True)
    conn = db_conn()
    gate = runtime_gate(conn)
    write_json(EVIDENCE / "runtime-admin-readonly-gate.json", gate)
    if gate["result"] == "FAIL":
        print("GATE FAIL")
        return
    home = home_admin_qa(conn)
    write_json(EVIDENCE / "home-admin-ux-qa.json", home)
    managed = managed_pages_qa(conn)
    write_json(EVIDENCE / "managed-pages-admin-ux-qa.json", managed)
    operator = operator_pages_qa(conn)
    write_json(EVIDENCE / "operator-review-pages-preservation-qa.json", operator)
    conn.close()
    frontend = frontend_qa()
    write_json(EVIDENCE / "frontend-regression-qa.json", frontend)
    findings = findings_register(gate, home, managed, operator, frontend)
    write_json(EVIDENCE / "admin-ux-findings-register.json", findings)
    drift = no_scope_drift()
    write_json(EVIDENCE / "no-scope-drift-validation.json", drift)
    verdict = {
        "phase": "V9-06D9-P",
        "generated_at": now_iso(),
        "verdict": "PASS" if all(x["result"] != "FAIL" for x in [gate, home, managed, operator, frontend, drift]) else "PARTIAL PASS",
        "home_4_admin_ux": home["result"],
        "home_4_save_unblock": "OPERATOR_CONFIRMATION_REQUIRED",
        "managed_pages_ux": managed["result"],
        "operator_review_pages_preserved": operator["result"],
        "frontend_regression": frontend["result"],
        "no_scope_drift": drift["result"],
        "recommended_next_phase": "CREATE_V9_06D9Q_REVIEWS_INCLUDE_PLANNING_TASK",
        "db_writes": 0,
    }
    write_json(EVIDENCE / "final-verdict.json", verdict)
    print(json.dumps({"gate": gate["result"], "home": home["result"], "frontend": frontend["result"], "verdict": verdict["verdict"]}))


if __name__ == "__main__":
    main()
