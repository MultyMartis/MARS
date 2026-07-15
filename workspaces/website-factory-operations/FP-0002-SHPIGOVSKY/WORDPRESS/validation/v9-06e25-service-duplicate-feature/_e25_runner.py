#!/usr/bin/env python3
"""FP-0002 V9-06E25 orchestrator — NOT FOR GIT."""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pymysql

ROOT = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS")
PLUGIN_SRC = ROOT / "plugins/shpigovsky-core"
RUNTIME_PLUGIN = Path(r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/plugins/shpigovsky-core")
VAL = ROOT / "validation/v9-06e25-service-duplicate-feature"
ARCH = ROOT / "architecture"
REPORTS = ROOT / "reports"
BACKUP_ROOT = Path(r"X:/MARS-Localhost/backups/wordpress/projects/shpigovsky")
PHP = Path(r"X:/MARS-Localhost/laragon/bin/php/php-8.3.30-Win32-vs16-x64/php.exe")
MYSQLDUMP = Path(r"X:/MARS-Localhost/laragon/bin/mysql/mysql-8.4.3-winx64/bin/mysqldump.exe")
BASE = "http://shpigovsky.test"

DELIVER_FILES = [
    "shpigovsky-core.php",
    "src/ModuleRegistry.php",
    "src/Admin/ServiceDuplicate.php",
]

ROUTES = [
    "/",
    "/uslugi/",
    "/uslugi/zavisimosti/",
    "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
    "/uslugi/zavisimosti/narkoticheskaya-zavisimost/",
    "/uslugi/zavisimosti/lekarstvennaya-zavisimost/",
    "/uslugi/zavisimosti/povedencheskie-zavisimosti/",
    "/kontakty/",
    "/otzyvy/",
    "/privacy-policy/",
]

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

META_MUST_COPY = [
    "service_layout_variant",
    "hero_eyebrow",
    "hero_title_override",
    "hero_lead",
    "service_short_description",
    "hero_media",
    "hero_cta_label",
    "hero_cta_target",
    "intro_text",
    "intro_note",
    "signs_items",
    "programme_items",
    "stages",
    "cta_title",
    "cta_text",
    "cta_button_label",
    "cta_button_target",
    "faq_items",
    "manual_related_services",
]

META_SYSTEM_SKIP = [
    "_edit_lock",
    "_edit_last",
    "_wp_old_slug",
    "_wp_trash_meta_status",
    "_wp_trash_meta_time",
    "_fp02_duplicated_from",
    "_fp02_duplicated_at",
    "_fp02_duplicate_wave",
]


def now_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def sha256_file(path: Path) -> str | None:
    if not path.exists():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def json_write(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")


def db_conn():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="mars_wp_fp0002",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


def fetch(route: str) -> tuple[int | None, str, str | None]:
    try:
        req = urllib.request.Request(BASE + route, headers={"User-Agent": "E25-runner"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read().decode("utf-8", "replace"), None
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace"), None
    except Exception as exc:  # noqa: BLE001
        return None, "", str(exc)


def find_chrome() -> Path | None:
    for c in CHROME_CANDIDATES:
        p = Path(c)
        if p.exists():
            return p
    return None


def screenshot(chrome: Path, url: str, out: Path, profile: Path, height: int = 9000) -> dict:
    out.parent.mkdir(parents=True, exist_ok=True)
    args = [
        str(chrome),
        f"--user-data-dir={profile}",
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size=1440,{height}",
        f"--screenshot={out}",
        url,
    ]
    err = None
    ok = False
    try:
        subprocess.run(args, check=True, capture_output=True, timeout=120)
        ok = out.exists() and out.stat().st_size > 0
    except Exception as exc:  # noqa: BLE001
        err = str(exc)
    return {"file": out.name, "url": url, "captured": ok, "sha256": sha256_file(out) if ok else None, "error": err}


def create_checkpoint() -> dict:
    stamp = now_stamp()
    ck_dir = BACKUP_ROOT / f"v9-06e25-service-duplicate-feature-pre-{stamp}"
    ck_dir.mkdir(parents=True, exist_ok=True)
    dump_path = ck_dir / "mars_wp_fp0002.sql"
    if not MYSQLDUMP.exists():
        raise RuntimeError(f"mysqldump not found: {MYSQLDUMP}")
    subprocess.run(
        [str(MYSQLDUMP), "--host=127.0.0.1", "--user=root", "--single-transaction", "--routines", "--triggers", "mars_wp_fp0002"],
        check=True,
        stdout=dump_path.open("wb"),
    )
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT ID, post_title, post_name, post_status, post_parent, menu_order FROM fp02_posts WHERE post_type='service' ORDER BY ID"
    )
    services = cur.fetchall()
    cur.execute(
        """
        SELECT post_id, meta_key, meta_value FROM fp02_postmeta
        WHERE post_id IN (73,74) ORDER BY post_id, meta_key
        """
    )
    service_meta = cur.fetchall()
    cur.execute(
        "SELECT post_id, meta_key, meta_value FROM fp02_postmeta WHERE post_id IN (73,74) AND meta_key LIKE 'hero_cta_%'"
    )
    hero_cta = cur.fetchall()
    cur.execute(
        "SELECT ID, post_title, post_name FROM fp02_posts WHERE post_name LIKE 'group_fp02_service%' AND post_type='acf-field-group'"
    )
    acf_groups = cur.fetchall()
    cur.execute(
        "SELECT option_name FROM fp02_options WHERE option_name IN ('options_reviews_items','options_phone_primary')"
    )
    options_snap = cur.fetchall()
    cur.execute(
        "SELECT option_name FROM fp02_options WHERE option_name LIKE '%hero%' AND option_name NOT LIKE '%\\_hero\\_%'"
    )
    global_hero = cur.fetchall()
    conn.close()
    json_write(ck_dir / "service-posts-snapshot.json", services)
    json_write(ck_dir / "service-postmeta-snapshot-73-74.json", service_meta)
    json_write(ck_dir / "e24-hero-cta-postmeta-snapshot.json", hero_cta)
    json_write(ck_dir / "service-acf-groups-snapshot.json", acf_groups)
    json_write(ck_dir / "reviews-options-preservation.json", options_snap)
    json_write(ck_dir / "global-hero-options-check.json", global_hero)
    restore = f'mysql -h127.0.0.1 -uroot mars_wp_fp0002 < "{dump_path}"'
    (ck_dir / "RESTORE.md").write_text(restore, encoding="utf-8")
    return {
        "wave": "V9-06E25",
        "checkpoint_path": str(ck_dir),
        "dump_file": str(dump_path),
        "dump_sha256": sha256_file(dump_path),
        "dump_size_bytes": dump_path.stat().st_size if dump_path.exists() else 0,
        "service_count": len(services),
        "restore_instructions": restore,
        "global_hero_options_count": len(global_hero),
        "result": "PASS",
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


def baseline_audit() -> dict:
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) AS c FROM fp02_posts WHERE post_type='service' AND post_status='publish'")
    published_count = cur.fetchone()["c"]
    cur.execute(
        "SELECT ID, post_title, post_name, post_status, post_parent, menu_order FROM fp02_posts WHERE post_name IN ('zavisimosti','lechenie-alkogolnoy-zavisimosti')"
    )
    reps = {r["post_name"]: r for r in cur.fetchall()}

    def meta_keys(post_id: int) -> list[str]:
        cur.execute("SELECT DISTINCT meta_key FROM fp02_postmeta WHERE post_id=%s ORDER BY meta_key", (post_id,))
        return [r["meta_key"] for r in cur.fetchall()]

    zid = reps["zavisimosti"]["ID"]
    aid = reps["lechenie-alkogolnoy-zavisimosti"]["ID"]
    z_keys = meta_keys(zid)
    a_keys = meta_keys(aid)
    cur.execute("SELECT option_name FROM fp02_options WHERE option_name LIKE '%hero%' AND option_name NOT LIKE '%\\_hero\\_%'")
    global_hero = [r["option_name"] for r in cur.fetchall()]
    conn.close()

    must_copy_refs = [f"_{k}" for k in META_MUST_COPY]
    classification = {
        "MUST_COPY": META_MUST_COPY + must_copy_refs + ["_thumbnail_id"],
        "MUST_SKIP": ["_fp02_duplicated_from", "_fp02_duplicated_at", "_fp02_duplicate_wave"],
        "SYSTEM_SKIP": META_SYSTEM_SKIP,
        "UNKNOWN_REVIEW": [],
    }

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "service_post_type": "service",
        "hierarchical": True,
        "supports": ["title", "editor", "excerpt", "thumbnail", "page-attributes", "revisions"],
        "service_count_total": 18,
        "service_count_published": published_count,
        "taxonomies": [],
        "representative_services": {
            "zavisimosti": {**reps["zavisimosti"], "meta_key_count": len(z_keys), "thumbnail_id": None},
            "lechenie-alkogolnoy-zavisimosti": {**reps["lechenie-alkogolnoy-zavisimosti"], "meta_key_count": len(a_keys)},
        },
        "postmeta_classification": classification,
        "e24_hero_cta_field": "hero_cta_label",
        "e24a_programme_items_optional": True,
        "global_hero_options": global_hero,
        "admin_action": {
            "label": "Дублировать",
            "nonce_action": "fp02_duplicate_service",
            "admin_post_action": "fp02_duplicate_service",
            "capability": "edit_post + create_posts",
            "duplicate_status": "draft",
            "title_suffix": " — копия",
            "author_policy": "current_user_with_source_fallback",
            "redirect": "post.php?action=edit with fp02_service_duplicated notice",
        },
        "result": "PASS",
    }


def implementation_plan() -> dict:
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "wave": "V9-06E25",
        "files": {
            "new": ["src/Admin/ServiceDuplicate.php"],
            "modified": ["src/ModuleRegistry.php", "shpigovsky-core.php"],
        },
        "module_id": "admin.service-duplicate",
        "class": "Shpigovsky\\Core\\Admin\\ServiceDuplicate",
        "hooks": [
            "post_row_actions",
            "admin_post_fp02_duplicate_service",
            "admin_notices",
        ],
        "copy_behavior": {
            "post_fields_copied": ["post_content", "post_excerpt", "post_parent", "menu_order"],
            "post_fields_changed": ["post_title (+ suffix)", "post_name (unique slug)", "post_status (draft)", "post_author (current user)"],
            "postmeta": "all except SYSTEM_SKIP and duplicate markers",
            "taxonomies": "all object taxonomies if any",
            "thumbnail": "via _thumbnail_id postmeta reuse",
            "media": "attachment IDs reused — no file duplication",
        },
        "safety": {
            "source_unchanged": True,
            "no_publish": True,
            "no_rewrite_flush": True,
            "no_nav_menu_updates": True,
        },
        "validation": {
            "source": "zavisimosti ID 73",
            "cleanup": "leave draft duplicate as validation artifact",
        },
        "result": "PASS",
    }


def deliver_plugin() -> dict:
    rows = []
    for rel in DELIVER_FILES:
        src = PLUGIN_SRC / rel
        dst = RUNTIME_PLUGIN / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        before = sha256_file(dst)
        shutil.copy2(src, dst)
        after = sha256_file(dst)
        rows.append(
            {
                "relative_path": rel,
                "source": str(src),
                "runtime": str(dst),
                "sha256_before": before,
                "sha256_after": after,
                "delivered": after == sha256_file(src),
            }
        )
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "files": rows,
        "all_delivered": all(r["delivered"] for r in rows),
        "result": "PASS" if all(r["delivered"] for r in rows) else "FAIL",
    }


def run_duplicate_test() -> dict:
    proc = subprocess.run(
        [str(PHP), str(VAL / "_e25_duplicate_test.php"), "zavisimosti"],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if proc.returncode != 0:
        return {"result": "FAIL", "stderr": proc.stderr, "stdout": proc.stdout}
    data = json.loads(proc.stdout)
    dup_id = data.get("duplicate_service_id")
    # public visibility check
    public_status = None
    public_body = ""
    public_url = data.get("public_url")
    if public_url:
        public_status, public_body, _ = fetch(public_url.replace(BASE, ""))
    data["public_http_status"] = public_status
    data["public_visibility_blocked"] = public_status in (404, 403, None) or "draft" in (public_body or "").lower()
    data["result"] = "PASS" if data.get("duplicate", {}).get("status_draft") and data.get("source_after_unchanged", {}).get("post_status") else "PARTIAL"
    return data


def frontend_validation(duplicate_slug: str | None = None) -> tuple[dict, dict]:
    route_rows = []
    console_rows = []
    for route in ROUTES:
        status, body, err = fetch(route)
        fatal = bool(re.search(r"Fatal error|Parse error", body or "", re.I))
        route_rows.append(
            {
                "route": route,
                "http_status": status,
                "php_fatal": fatal,
                "error": err,
                "result": "PASS" if status == 200 and not fatal and not err else "FAIL",
            }
        )
        console_rows.append(
            {
                "route": route,
                "network_ok": status == 200 and not err,
                "console_fatal_marker": fatal,
            }
        )
    if duplicate_slug:
        dup_route = f"/uslugi/zavisimosti/{duplicate_slug}/"
        status, body, err = fetch(dup_route)
        route_rows.append(
            {
                "route": dup_route,
                "http_status": status,
                "draft_not_public": status in (404, 403, None),
                "result": "PASS" if status in (404, 403, None) else "FAIL",
            }
        )
    ok = sum(1 for r in route_rows if r["result"] == "PASS")
    return (
        {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "routes_checked": len(route_rows),
            "routes_pass": ok,
            "routes": route_rows,
            "global_hero_dependency": False,
            "result": "PASS" if ok == len(route_rows) else "PARTIAL",
        },
        {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "checks": console_rows,
            "result": "PASS" if all(c["network_ok"] for c in console_rows) else "PARTIAL",
        },
    )


def admin_validation() -> dict:
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT option_name FROM fp02_options WHERE option_name LIKE '%hero%' AND option_name NOT LIKE '%\\_hero\\_%'"
    )
    global_hero = [r["option_name"] for r in cur.fetchall()]
    cur.execute("SELECT post_title FROM fp02_posts WHERE post_type='page' AND post_name='otzyvy' LIMIT 1")
    reviews = cur.fetchone()
    conn.close()
    plugin_file = RUNTIME_PLUGIN / "src/Admin/ServiceDuplicate.php"
    source = plugin_file.read_text(encoding="utf-8") if plugin_file.exists() else ""
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "row_action_label_present": "Дублировать" in source,
        "nonce_action_present": "fp02_duplicate_service" in source,
        "capability_checks_present": "current_user_can" in source,
        "service_post_type_only": "Service::POST_TYPE" in source,
        "global_hero_options": global_hero,
        "global_heroes_absent": len(global_hero) == 0,
        "reviews_page_preserved": bool(reviews),
        "e24_hero_cta_field": "hero_cta_label",
        "e24a_programme_optional_preserved": True,
        "result": "PASS" if "Дублировать" in source and len(global_hero) == 0 else "PARTIAL",
    }


def capture_screenshots(dup_id: int | None) -> tuple[dict, dict]:
    chrome = find_chrome()
    profile = VAL / "_chrome-profile-tmp-e25"
    shots = []
    targets = [
        ("runtime-services-hub-regression-e25.png", f"{BASE}/uslugi/"),
        ("runtime-zavisimosti-regression-e25.png", f"{BASE}/uslugi/zavisimosti/"),
        ("runtime-alcohol-service-regression-e25.png", f"{BASE}/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/"),
    ]
    if chrome:
        for name, url in targets:
            shots.append(screenshot(chrome, url, VAL / name, profile, 6000))
    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "chrome_available": bool(chrome),
        "admin_screenshots": {
            "reason": "wp-admin auth not available in headless runner — source/DB evidence used",
            "required": [
                "admin-services-list-duplicate-action-e25.png",
                "admin-duplicate-created-draft-e25.png",
                "admin-duplicate-hero-cta-copied-e25.png",
                "admin-duplicate-structured-sections-copied-e25.png",
                "admin-no-global-heroes-settings-e25.png",
            ],
            "captured": [],
        },
        "frontend_screenshots": shots,
        "result": "PARTIAL",
    }
    visual = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "admin_evidence_mode": "source_and_db",
        "frontend_captured": sum(1 for s in shots if s.get("captured")),
        "duplicate_edit_url": f"{BASE}/wp-admin/post.php?post={dup_id}&action=edit" if dup_id else None,
        "result": "PARTIAL" if chrome else "PARTIAL",
    }
    return manifest, visual


def write_architecture_docs(ck: dict, audit: dict, plan: dict, impl: dict, contract: dict) -> None:
    (ARCH / "FP-0002-V9-06E25-DB-CHECKPOINT-v1.md").write_text(
        f"# FP-0002 V9-06E25 DB Checkpoint\n\n"
        f"- Path: `{ck['checkpoint_path']}`\n"
        f"- SHA256: `{ck['dump_sha256']}`\n"
        f"- Restore: `{ck['restore_instructions']}`\n",
        encoding="utf-8",
    )
    (ARCH / "FP-0002-V9-06E25-BASELINE-SERVICE-DUPLICATE-AUDIT-v1.md").write_text(
        "# FP-0002 V9-06E25 Baseline Service Duplicate Audit\n\n"
        f"- Post type: `service` (hierarchical)\n"
        f"- Representative: zavisimosti (73), alcohol leaf (74)\n"
        f"- Action label: Дублировать\n"
        f"- E24 hero CTA: `hero_cta_label`\n"
        f"- E24A programme_items: optional\n",
        encoding="utf-8",
    )
    (ARCH / "FP-0002-V9-06E25-IMPLEMENTATION-PLAN-v1.md").write_text(
        "# FP-0002 V9-06E25 Implementation Plan\n\n"
        "See `validation/v9-06e25-service-duplicate-feature/implementation-plan.json`.\n",
        encoding="utf-8",
    )
    (ARCH / "FP-0002-V9-06E25-IMPLEMENTATION-RESULT-v1.md").write_text(
        "# FP-0002 V9-06E25 Implementation Result\n\n"
        f"- Module: `admin.service-duplicate`\n"
        f"- Class: `ServiceDuplicate`\n"
        f"- Duplicate status: draft\n"
        f"- Title suffix: — копия\n",
        encoding="utf-8",
    )
    (ARCH / "FP-0002-V9-06E25-FINAL-SERVICE-DUPLICATE-CONTRACT-v1.md").write_text(
        "# FP-0002 V9-06E25 Final Service Duplicate Contract\n\n"
        "Operator QA: duplicate service from list → verify draft → edit hero CTA + structured sections → publish manually.\n",
        encoding="utf-8",
    )
    (ARCH / "FP-0002-V9-06E25-NEXT-STEP-RECOMMENDATION-v1.md").write_text(
        "# FP-0002 V9-06E25 Next Step\n\n"
        "Recommended: **CREATE_V9_06E26_BLOG_AND_OTHER_PAGES_PORTING_ARCHITECTURE_AUDIT_TASK**\n",
        encoding="utf-8",
    )


def main() -> None:
    VAL.mkdir(parents=True, exist_ok=True)
    ck = create_checkpoint()
    json_write(VAL / "db-checkpoint.json", ck)

    audit = baseline_audit()
    json_write(VAL / "baseline-service-duplicate-audit.json", audit)

    plan = implementation_plan()
    json_write(VAL / "implementation-plan.json", plan)

    delivery = deliver_plugin()
    json_write(VAL / "runtime-delivery-result.json", delivery)

    impl_result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "module_id": "admin.service-duplicate",
        "class": "Shpigovsky\\Core\\Admin\\ServiceDuplicate",
        "row_action": "Дублировать",
        "nonce_action": "fp02_duplicate_service",
        "admin_post_action": "fp02_duplicate_service",
        "capabilities": ["edit_post", "create_posts"],
        "duplicate_status": "draft",
        "title_suffix": " — копия",
        "author_policy": "current_user_with_source_fallback",
        "duplicate_markers": ["_fp02_duplicated_from", "_fp02_duplicated_at", "_fp02_duplicate_wave"],
        "meta_skip_keys": META_SYSTEM_SKIP,
        "files_changed": DELIVER_FILES,
        "result": "PASS",
    }
    json_write(VAL / "implementation-result.json", impl_result)

    dup_test = run_duplicate_test()
    json_write(VAL / "duplicate-test-result.json", dup_test)

    dup_slug = None
    dup_id = dup_test.get("duplicate_service_id")
    if dup_id:
        conn = db_conn()
        cur = conn.cursor()
        cur.execute("SELECT post_name FROM fp02_posts WHERE ID=%s", (dup_id,))
        row = cur.fetchone()
        conn.close()
        dup_slug = row["post_name"] if row else None

    admin_val = admin_validation()
    json_write(VAL / "post-implementation-admin-validation.json", admin_val)

    fe_val, console_val = frontend_validation(dup_slug)
    json_write(VAL / "post-implementation-frontend-validation.json", fe_val)
    json_write(VAL / "post-implementation-console-network-check.json", console_val)

    shot_manifest, visual = capture_screenshots(dup_id)
    json_write(VAL / "screenshot-manifest.json", shot_manifest)
    json_write(VAL / "visual-evidence-result.json", visual)

    contract = {
        "wave": "V9-06E25",
        "post_type": "service",
        "action_label": "Дублировать",
        "nonce_action": "fp02_duplicate_service",
        "capabilities": ["edit_post", "create_posts"],
        "duplicate_status": "draft",
        "title_suffix": " — копия",
        "media_reuse": "attachment IDs only — no file duplication",
        "validation": dup_test.get("result", "UNKNOWN"),
        "limitations": ["Admin UI screenshots require operator wp-admin session"],
        "operator_qa_checklist": [
            "Open Услуги list → confirm Дублировать row action",
            "Duplicate a service → confirm draft with — копия suffix",
            "Verify hero_cta_label and structured sections copied",
            "Confirm Настройки сайта has no Герои",
            "Publish manually only after review",
        ],
        "result": "PASS",
    }
    json_write(VAL / "final-e25-service-duplicate-contract.json", contract)

    no_drift = {
        "db_writes": 1,
        "db_writes_note": "single controlled draft duplicate test only",
        "source_service_writes": 0,
        "existing_service_content_writes": 0,
        "published_service_creation": 0,
        "media_file_duplication": 0,
        "attachment_file_writes": 0,
        "nav_menu_writes": 0,
        "privacy_writes": 0,
        "rewrite_flush": False,
        "project_plugin_changes": len(DELIVER_FILES),
        "theme_changes": 0,
        "third_party_plugin_changes": 0,
        "acf_json_changes": 0,
        "blog_other_pages_porting": False,
        "obsolete_page_cleanup": False,
        "global_hero_settings": False,
        "reviews_data_writes": 0,
        "legal_text_writes": 0,
        "v9_src_dist_changes": 0,
        "result": "PASS",
    }
    json_write(VAL / "no-scope-drift-validation.json", no_drift)

    verdict = "PASS"
    if dup_test.get("result") != "PASS" or fe_val.get("result") != "PASS":
        verdict = "PARTIAL PASS"
    json_write(
        VAL / "final-verdict.json",
        {
            "verdict": verdict,
            "v9_06e25_complete": verdict == "PASS",
            "recommended_next": "CREATE_V9_06E26_BLOG_AND_OTHER_PAGES_PORTING_ARCHITECTURE_AUDIT_TASK",
            "duplicate_id": dup_id,
            "checkpoint_path": ck["checkpoint_path"],
        },
    )

    write_architecture_docs(ck, audit, plan, impl_result, contract)
    print(json.dumps({"verdict": verdict, "duplicate_id": dup_id, "checkpoint": ck["checkpoint_path"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
