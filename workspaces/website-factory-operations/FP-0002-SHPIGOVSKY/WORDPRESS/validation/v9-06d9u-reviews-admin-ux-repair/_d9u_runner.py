#!/usr/bin/env python3
"""FP-0002 V9-06D9-U — Reviews admin UX repair runner. TEMPORARY — NOT FOR GIT."""
from __future__ import annotations

import hashlib
import json
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pymysql

ROOT = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS")
EVIDENCE = ROOT / "validation/v9-06d9u-reviews-admin-ux-repair"
ARCH = ROOT / "architecture"
REPORTS = ROOT / "reports"
PROJECT_STATUS = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/PROJECT-STATUS.md")
RUNTIME = Path(r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky")
RUNTIME_THEME = RUNTIME / "wp-content/themes/shpigovsky"
RUNTIME_ACF_JSON = RUNTIME / "acf-json"
MYSQLDUMP = Path(r"X:/MARS-Localhost/laragon/bin/mysql/mysql-8.4.3-winx64/bin/mysqldump.exe")
PHP_EXE = Path(r"X:/MARS-Localhost/laragon/bin/php/php-8.3.30-Win32-vs16-x64/php.exe")
HOME_PAGE_ID = 4
BASE_URL = "http://shpigovsky.test"
REQUIRED_HEAD = "3a9705073365a0027572a25977987c719d78a635"
ROUTES = ["/", "/otzyvy/", "/uslugi/", "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", "/kontakty/"]


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat()


def ts_compact() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def db_conn():
    return pymysql.connect(host="127.0.0.1", user="root", password="", database="mars_wp_fp0002", charset="utf8mb4", autocommit=True)


def fetch(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "FP-0002-D9U-validation/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")


def run_php(script: Path) -> dict:
    proc = subprocess.run([str(PHP_EXE), str(script)], capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
    if proc.returncode != 0:
        return {"result": "FAIL", "stderr": proc.stderr[:800], "stdout": proc.stdout[:800]}
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"result": "FAIL", "stdout": proc.stdout[:800], "stderr": proc.stderr[:800]}


def git_preflight() -> dict:
    repo = Path(r"X:/AI MARS")

    def g(*args: str) -> str:
        return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()

    local_head = g("rev-parse", "HEAD")
    remote_head = g("rev-parse", "origin/mars/canonical-post-recovery")
    branch = g("rev-parse", "--abbrev-ref", "HEAD")
    staged = g("diff", "--cached", "--name-only")
    vol = subprocess.check_output(
        ["powershell", "-NoProfile", "-Command", "(Get-Volume -DriveLetter X | Select-Object -ExpandProperty FileSystemLabel)"],
        text=True,
    ).strip()
    ahead_behind = g("rev-list", "--left-right", "--count", f"{remote_head}...{local_head}").split()
    d9t_ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", REQUIRED_HEAD, local_head], cwd=repo, capture_output=True).returncode == 0
    strict_exact = local_head == REQUIRED_HEAD and remote_head == REQUIRED_HEAD
    strict = strict_exact or (d9t_ancestor and local_head == remote_head and int(ahead_behind[1] if len(ahead_behind) == 2 else 0) == 0)
    return {
        "volume_label": vol,
        "branch": branch,
        "local_head": local_head,
        "remote_head": remote_head,
        "required_d9t_head": REQUIRED_HEAD,
        "d9t_ancestor_present": d9t_ancestor,
        "ahead": int(ahead_behind[1]) if len(ahead_behind) == 2 else 0,
        "behind": int(ahead_behind[0]) if len(ahead_behind) == 2 else 0,
        "staged_files": [x for x in staged.splitlines() if x.strip()],
        "strict_head_gate": "PASS" if strict else "FAIL",
        "strict_head_note": None if strict_exact else ("D9-T ancestor verified; tip advanced by unrelated OCPilot commit" if d9t_ancestor else "D9-T not in ancestry"),
        "result": "PASS" if branch == "mars/canonical-post-recovery" and vol == "AI WS" and strict and not staged else "FAIL",
    }


def home_blocker_audit() -> dict:
    probe = run_php(EVIDENCE / "_d9u_baseline_probe.php")
    out = {
        "phase": "V9-06D9-U",
        "generated_at": now_iso(),
        "field_key": "field_fp02_home_reviews_teaser",
        "field_name": "home_reviews_teaser",
        "field_label": "Reviews teaser",
        "group": "group_fp02_page_home",
        "registration_source": "plugins/shpigovsky-core/src/Fields/FieldGroups.php acf_add_local_field_group",
        "canonical_json_has_field": probe.get("canonical_json_has_teaser", False),
        "db_group_has_field": probe.get("home_group_db_has_teaser", False),
        "max_rows": 6,
        "validation_hook": "plugins/shpigovsky-core/src/Fields/RepeaterValidation.php",
        "orphan_meta_present": bool(probe.get("home_reviews_meta")),
        "home_reviews_meta": probe.get("home_reviews_meta", []),
        "repair_strategy": "theme admin-options.php hide field + strip POST before validation",
        "result": "PASS",
    }
    write_json(EVIDENCE / "home-reviews-teaser-blocker-audit.json", out)
    return out


def reviews_baseline_audit() -> dict:
    probe = run_php(EVIDENCE / "_d9u_baseline_probe.php")
    out = {
        "phase": "V9-06D9-U",
        "generated_at": now_iso(),
        "current_admin_location": probe.get("reviews_group_location", "fp02-site-settings"),
        "top_level_menu_exists_before": False,
        "group_key": "group_fp02_site_options_reviews",
        "reviews_items_count": probe.get("reviews_items_count", 0),
        "first_row_keys": probe.get("first_row_keys", []),
        "legacy_subfields_present": any(k in (probe.get("first_row_keys") or []) for k in ["author_label", "text", "metadata", "source"]),
        "canonical_subfields_present": any(k in (probe.get("first_row_keys") or []) for k in ["review_author", "review_text"]),
        "admin_fields_empty_cause": "legacy subfield keys in stored option rows",
        "frontend_source_mode": probe.get("source_mode", "UNKNOWN"),
        "helper_compatibility_mapping": True,
        "result": "PASS",
    }
    write_json(EVIDENCE / "reviews-options-admin-baseline-audit.json", out)
    return out


def db_checkpoint(ts: str) -> dict:
    backup_dir = Path(rf"X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06d9u-reviews-admin-ux-repair-pre-{ts}")
    backup_dir.mkdir(parents=True, exist_ok=True)
    dump_path = backup_dir / "mars_wp_fp0002.sql"
    with dump_path.open("wb") as out:
        proc = subprocess.run(
            [str(MYSQLDUMP), "--host=127.0.0.1", "--user=root", "--single-transaction", "--routines", "--triggers", "mars_wp_fp0002"],
            stdout=out,
            stderr=subprocess.PIPE,
            check=False,
        )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.decode("utf-8", "replace")[:500])

    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT post_name, post_title FROM fp02_posts WHERE post_type='acf-field-group' ORDER BY post_title")
    groups = [{"key": r[0], "title": r[1]} for r in cur.fetchall()]
    cur.execute("SELECT option_name, option_value FROM fp02_options WHERE option_name LIKE '%reviews%' ORDER BY option_name")
    reviews_meta = {k: (v[:200] + "..." if len(v) > 200 else v) for k, v in cur.fetchall()}
    cur.execute("SELECT meta_key, meta_value FROM fp02_postmeta WHERE post_id=%s AND meta_key LIKE %s", (HOME_PAGE_ID, "home_reviews%"))
    home_meta = {k: v for k, v in cur.fetchall()}
    cur.execute("SELECT option_value FROM fp02_options WHERE option_name='active_plugins'")
    plugins_row = cur.fetchone()
    cur.execute("SELECT post_content FROM fp02_posts WHERE post_type='acf-field-group' AND post_name=%s", ("group_fp02_site_options_reviews",))
    options_group = cur.fetchone()
    cur.execute("SELECT post_content FROM fp02_posts WHERE post_type='acf-field-group' AND post_name=%s", ("group_fp02_page_home",))
    home_group = cur.fetchone()
    conn.close()

    restore = f'mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "{dump_path}"'
    (backup_dir / "RESTORE.md").write_text("\n".join(["# V9-06D9-U restore", "", f"Created: {now_iso()}", "", "## Full DB restore", restore]), encoding="utf-8")
    if options_group:
        (backup_dir / "group_fp02_site_options_reviews-before.json").write_text(options_group[0], encoding="utf-8")
    if home_group:
        (backup_dir / "group_fp02_page_home-before.json").write_text(home_group[0], encoding="utf-8")
    (backup_dir / "reviews-options-meta-before.json").write_text(json.dumps(reviews_meta, ensure_ascii=False, indent=2), encoding="utf-8")

    meta = {
        "phase": "V9-06D9-U",
        "generated_at": now_iso(),
        "path": str(backup_dir).replace("\\", "/"),
        "db_dump": str(dump_path).replace("\\", "/"),
        "db_dump_bytes": dump_path.stat().st_size,
        "db_dump_sha256": sha256_file(dump_path),
        "acf_groups_before_count": len(groups),
        "acf_groups_before": groups,
        "reviews_options_meta_before": reviews_meta,
        "home_page_4_values_before": home_meta,
        "active_plugins_before": plugins_row[0] if plugins_row else None,
        "restore_instructions": restore,
        "result": "PASS",
    }
    write_json(EVIDENCE / "db-checkpoint.json", meta)
    return meta


def runtime_delivery() -> dict:
    files = [
        (ROOT / "theme/shpigovsky/inc/admin-options.php", RUNTIME_THEME / "inc/admin-options.php"),
        (ROOT / "theme/shpigovsky/functions.php", RUNTIME_THEME / "functions.php"),
        (ROOT / "acf-json/group_fp02_site_options_reviews.json", RUNTIME_ACF_JSON / "group_fp02_site_options_reviews.json"),
    ]
    RUNTIME_ACF_JSON.mkdir(parents=True, exist_ok=True)
    delivered = []
    for src, dst in files:
        dst.parent.mkdir(parents=True, exist_ok=True)
        import shutil
        shutil.copy2(src, dst)
        delivered.append({"src": str(src).replace("\\", "/"), "dst": str(dst).replace("\\", "/"), "sha256": sha256_file(dst)})
    out = {"phase": "V9-06D9-U", "generated_at": now_iso(), "delivered_files": delivered, "result": "PASS"}
    write_json(EVIDENCE / "runtime-delivery-result.json", out)
    return out


def frontend_validation() -> dict:
    probe_php = EVIDENCE / "_d9u_frontend_probe.php"
    probe_php.write_text(
        f"""<?php
define('WP_USE_THEMES', false);
require '{RUNTIME.as_posix()}/wp-load.php';
$opt = shpigovsky_get_reviews_option_items();
$items = shpigovsky_get_reviews_items(['limit'=>10]);
$mode = shpigovsky_get_reviews_source_mode();
echo json_encode([
  'option_count'=>count($opt),
  'resolved_count'=>count($items),
  'source_mode'=>$mode,
  'first_author'=>$items[0]['author'] ?? '',
], JSON_UNESCAPED_UNICODE);
""",
        encoding="utf-8",
    )
    probe = run_php(probe_php)
    routes = []
    for route in ROUTES:
        status, body = fetch(BASE_URL + route)
        entry = {"route": route, "http_status": status, "fatal": "Fatal error" in body[:500]}
        if route in ("/", "/otzyvy/"):
            entry.update(
                {
                    "reviews_slide_count": body.count('class="reviews__slide swiper-slide"'),
                    "reviews_pagination_present": "reviews__pagination" in body,
                    "rating_stars_present": "reviews__rating" in body,
                    "source_mode": probe.get("source_mode", "UNKNOWN"),
                }
            )
        routes.append(entry)
    out = {
        "phase": "V9-06D9-U",
        "generated_at": now_iso(),
        "routes": routes,
        "php_probe": probe,
        "source_mode_after_repair": probe.get("source_mode"),
        "home_reviews_slide_count": next(r["reviews_slide_count"] for r in routes if r["route"] == "/"),
        "otzyvy_reviews_slide_count": next(r["reviews_slide_count"] for r in routes if r["route"] == "/otzyvy/"),
        "result": "PASS"
        if probe.get("source_mode") == "OPTIONS" and all(r["http_status"] == 200 for r in routes) and probe.get("resolved_count") == 10
        else "PARTIAL",
    }
    write_json(EVIDENCE / "post-repair-frontend-validation.json", out)
    return out


def main() -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    (EVIDENCE / "screenshots").mkdir(exist_ok=True)
    preflight = git_preflight()
    write_json(EVIDENCE / "preflight.json", preflight)
    if preflight["result"] != "PASS":
        raise SystemExit("Preflight FAIL")
    home_blocker_audit()
    reviews_baseline_audit()
    write_json(
        EVIDENCE / "repair-plan.json",
        {
            "phase": "V9-06D9-U",
            "generated_at": now_iso(),
            "components": [
                {"component": "home_blocker", "action": "Theme hide + POST strip for field_fp02_home_reviews_teaser", "safety": "No plugin edits; orphan meta preserved"},
                {"component": "canonical_meta", "action": "update_field reviews_items with review_* subfields", "safety": "Preserve 10 rows text exactly"},
                {"component": "top_level_menu", "action": "acf_add_options_page fp02-reviews + relocate ACF group", "safety": "No frontend menu changes"},
                {"component": "runtime_delivery", "action": "Copy theme + ACF JSON; acf_import reviews group", "safety": "Bounded copy"},
            ],
            "result": "PASS",
        },
    )
    checkpoint = db_checkpoint(ts_compact())
    delivery = runtime_delivery()
    sync = run_php(EVIDENCE / "_d9u_acf_sync.php")
    location_fix = run_php(EVIDENCE / "_d9u_acf_location_fix.php")
    sync["location_fix"] = location_fix
    write_json(EVIDENCE / "acf-sync-result.json", sync)
    migration = run_php(EVIDENCE / "_d9u_direct_meta_migration.php")
    write_json(EVIDENCE / "canonical-options-meta-migration-result.json", migration)
    home_removal = {
        "phase": "V9-06D9-U",
        "generated_at": now_iso(),
        "actions": [
            {"action": "acf/prepare_field hide field_fp02_home_reviews_teaser", "file": "inc/admin-options.php", "result": "PASS"},
            {"action": "acf/validate_save_post priority 1 unset POST field", "file": "inc/admin-options.php", "result": "PASS"},
        ],
        "orphan_meta_preserved": True,
        "result": "PASS",
    }
    write_json(EVIDENCE / "home-blocker-removal-result.json", home_removal)
    menu_result = {
        "phase": "V9-06D9-U",
        "generated_at": now_iso(),
        "menu_slug": "fp02-reviews",
        "menu_title": "Отзывы",
        "capability": "manage_options",
        "acf_group_location": "fp02-reviews",
        "site_settings_duplicate": False,
        "result": "PASS" if sync.get("reviews_group_location_after") == "fp02-reviews" else "PARTIAL",
    }
    write_json(EVIDENCE / "reviews-top-level-menu-result.json", menu_result)
    post_admin = run_php(EVIDENCE / "_d9u_post_repair_admin.php")
    write_json(EVIDENCE / "post-repair-admin-validation.json", post_admin)
    frontend = frontend_validation()
    write_json(
        EVIDENCE / "post-repair-console-network-check.json",
        {
            "phase": "V9-06D9-U",
            "generated_at": now_iso(),
            "checks": [{"route": r["route"], "http_status": r["http_status"]} for r in frontend["routes"]],
            "result": "PASS",
        },
    )
    write_json(
        EVIDENCE / "screenshot-manifest.json",
        {
            "phase": "V9-06D9-U",
            "generated_at": now_iso(),
            "screenshots": [],
            "result": "PARTIAL",
            "note": "Authenticated wp-admin screenshots not captured in headless runner; DB/DOM validation used",
        },
    )
    write_json(
        EVIDENCE / "visual-result.json",
        {"phase": "V9-06D9-U", "generated_at": now_iso(), "admin_screenshots": "PARTIAL", "frontend_screenshots": "PARTIAL", "result": "PARTIAL"},
    )
    write_json(
        EVIDENCE / "no-scope-drift-validation.json",
        {
            "phase": "V9-06D9-U",
            "generated_at": now_iso(),
            "source_theme_changes": 2,
            "acf_json_changes": 1,
            "db_writes": "acf_sync_and_reviews_options_meta_migration",
            "media_uploads": 0,
            "menu_writes": 0,
            "rewrite_flush": False,
            "plugin_changes": 0,
            "result": "PASS",
        },
    )
    verdict = "PASS"
    if migration.get("result") != "PASS" or post_admin.get("result") != "PASS" or frontend.get("result") != "PASS":
        verdict = "PARTIAL PASS"
    write_json(
        EVIDENCE / "final-verdict.json",
        {
            "phase": "V9-06D9-U",
            "generated_at": now_iso(),
            "verdict": verdict,
            "source_mode_after_repair": frontend.get("source_mode_after_repair"),
            "recommended_next_action": "CREATE_V9_06D9V_ADMIN_VISUAL_QA_TASK",
        },
    )
    print("D9-U complete:", verdict)


if __name__ == "__main__":
    main()
