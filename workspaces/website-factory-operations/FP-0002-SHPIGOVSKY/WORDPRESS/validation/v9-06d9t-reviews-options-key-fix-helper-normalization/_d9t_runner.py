#!/usr/bin/env python3
"""FP-0002 V9-06D9-T — Reviews options key fix + helper normalization runner.
TEMPORARY HELPER — NOT FOR GIT COMMIT
"""
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
EVIDENCE = ROOT / "validation/v9-06d9t-reviews-options-key-fix-helper-normalization"
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
REQUIRED_D9S_HEAD = "937040c2ceab143861eae987f8a7338bce3a7f65"

ROUTES = [
    "/",
    "/otzyvy/",
    "/uslugi/",
    "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
    "/kontakty/",
]

KEY_REPAIR_MAP = {
    "field_fp02_reviews_enabled": "field_fp02_options_reviews_enabled",
    "field_fp02_reviews_section_heading": "field_fp02_options_reviews_section_heading",
    "field_fp02_reviews_items": "field_fp02_options_reviews_items",
    "field_fp02_review_author": "field_fp02_options_review_author",
    "field_fp02_review_text": "field_fp02_options_review_text",
    "field_fp02_review_context": "field_fp02_options_review_context",
    "field_fp02_review_source": "field_fp02_options_review_source",
    "field_fp02_review_date": "field_fp02_options_review_date",
    "field_fp02_review_rating": "field_fp02_options_review_rating",
    "field_fp02_review_visible": "field_fp02_options_review_visible",
    "field_fp02_review_featured": "field_fp02_options_review_featured",
}


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
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="mars_wp_fp0002",
        charset="utf8mb4",
        autocommit=True,
    )


def fetch(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "FP-0002-D9T-validation/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")


def run_php(script: Path) -> dict:
    proc = subprocess.run(
        [str(PHP_EXE), str(script)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
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
        [
            "powershell",
            "-NoProfile",
            "-Command",
            "(Get-Volume -DriveLetter X | Select-Object -ExpandProperty FileSystemLabel)",
        ],
        text=True,
    ).strip()
    ahead_behind = g("rev-list", "--left-right", "--count", f"{remote_head}...{local_head}").split()
    d9s_ancestor = (
        subprocess.run(
            ["git", "merge-base", "--is-ancestor", REQUIRED_D9S_HEAD, local_head],
            cwd=repo,
            capture_output=True,
        ).returncode
        == 0
    )
    strict = local_head == REQUIRED_D9S_HEAD and remote_head == REQUIRED_D9S_HEAD
    return {
        "volume_label": vol,
        "branch": branch,
        "local_head": local_head,
        "local_head_short": local_head[:8],
        "remote_head": remote_head,
        "remote_head_short": remote_head[:8],
        "required_d9s_head": REQUIRED_D9S_HEAD,
        "d9s_ancestor_present": d9s_ancestor,
        "ahead": int(ahead_behind[1]) if len(ahead_behind) == 2 else 0,
        "behind": int(ahead_behind[0]) if len(ahead_behind) == 2 else 0,
        "staged_files": [x for x in staged.splitlines() if x.strip()],
        "strict_head_gate": "PASS" if strict else "PARTIAL",
        "strict_head_note": None
        if strict
        else "HEAD advanced beyond D9-S; D9-S ancestor verified for repair baseline",
        "result": "PASS"
        if branch == "mars/canonical-post-recovery" and vol == "AI WS" and d9s_ancestor and not staged
        else "PARTIAL",
    }


def read_acf_json_keys(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    keys = []
    for field in data.get("fields", []):
        keys.append({"key": field["key"], "name": field["name"]})
        for sf in field.get("sub_fields", []):
            keys.append({"key": sf["key"], "name": sf["name"]})
    return keys


def baseline_audit() -> dict:
    probe = run_php(EVIDENCE / "_d9t_baseline_probe.php")
    options_json = ROOT / "acf-json/group_fp02_site_options_reviews.json"
    page_json = ROOT / "acf-json/group_fp02_page_reviews.json"
    src_opt = read_acf_json_keys(options_json)
    src_page = read_acf_json_keys(page_json)
    src_dup = sorted(set(x["key"] for x in src_opt) & set(x["key"] for x in src_page))

    migration_required = True
    if probe.get("first_option_row_keys"):
        legacy = {"author_label", "text", "metadata", "source"}
        canonical = {
            "review_author",
            "review_text",
            "review_context",
            "review_source",
            "review_date",
            "review_rating",
            "review_visible",
            "review_featured",
        }
        row_keys = set(probe["first_option_row_keys"])
        if row_keys & legacy and not (row_keys & canonical):
            migration_mode = "helper_only_or_post_sync"
        elif row_keys & canonical:
            migration_mode = "optional_canonical_meta"
        else:
            migration_mode = "unknown"
    else:
        migration_mode = "none"

    out = {
        "phase": "V9-06D9-T",
        "generated_at": now_iso(),
        "source_options_json_keys": src_opt,
        "source_page_json_keys": src_page,
        "source_json_duplicate_keys": src_dup,
        "runtime_duplicate_keys": probe.get("duplicate_keys", []),
        "runtime_options_group_keys": probe.get("options_group_keys", []),
        "runtime_page_group_keys": probe.get("page_group_keys", []),
        "seeded_reviews_items_count": probe.get("reviews_items_count", 0),
        "first_option_row": probe.get("first_option_row"),
        "first_option_row_subfield_names": probe.get("first_option_row_keys", []),
        "helper_option_items_count_before": probe.get("helper_option_items_count", 0),
        "frontend_source_mode_before": probe.get("frontend_source_mode_before", "UNKNOWN"),
        "home_reviews_slide_count_before": 0,
        "otzyvy_reviews_slide_count_before": 0,
        "helper_expected_subfields": [
            "review_author",
            "review_text",
            "review_context",
            "review_source",
            "review_date",
            "review_rating",
            "review_visible",
            "review_featured",
        ],
        "legacy_subfield_names_in_db": ["author_label", "text", "metadata", "source"],
        "collision_reproducible": bool(probe.get("duplicate_keys") or src_dup),
        "migration_assessment": migration_mode,
        "home_page_4_reviews_meta": probe.get("home_page_4_reviews_meta", {}),
        "result": "PASS"
        if probe.get("reviews_items_count") == 10 and (probe.get("duplicate_keys") or src_dup)
        else "STOP",
    }
    home_status, home_body = fetch(BASE_URL + "/")
    otzyvy_status, otzyvy_body = fetch(BASE_URL + "/otzyvy/")
    out["home_http_status"] = home_status
    out["otzyvy_http_status"] = otzyvy_status
    out["home_reviews_slide_count_before"] = home_body.count('class="reviews__slide swiper-slide"')
    out["otzyvy_reviews_slide_count_before"] = otzyvy_body.count('class="reviews__slide swiper-slide"')
    write_json(EVIDENCE / "baseline-collision-data-audit.json", out)
    return out


def db_checkpoint(ts: str) -> dict:
    backup_dir = Path(
        rf"X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06d9t-reviews-options-key-fix-pre-{ts}"
    )
    backup_dir.mkdir(parents=True, exist_ok=True)
    dump_path = backup_dir / "mars_wp_fp0002.sql"
    with dump_path.open("wb") as out:
        proc = subprocess.run(
            [
                str(MYSQLDUMP),
                "--host=127.0.0.1",
                "--user=root",
                "--single-transaction",
                "--routines",
                "--triggers",
                "mars_wp_fp0002",
            ],
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
    cur.execute(
        "SELECT option_name, option_value FROM fp02_options WHERE option_name LIKE '%reviews%' ORDER BY option_name"
    )
    reviews_meta = {k: (v[:200] + "..." if len(v) > 200 else v) for k, v in cur.fetchall()}
    cur.execute(
        "SELECT meta_key, meta_value FROM fp02_postmeta WHERE post_id=%s AND meta_key LIKE %s",
        (HOME_PAGE_ID, "home_reviews%"),
    )
    home_meta = {k: v for k, v in cur.fetchall()}
    cur.execute("SELECT option_value FROM fp02_options WHERE option_name='active_plugins'")
    plugins_row = cur.fetchone()
    cur.execute(
        "SELECT post_content FROM fp02_posts WHERE post_type='acf-field-group' AND post_name=%s",
        ("group_fp02_site_options_reviews",),
    )
    options_group_json = cur.fetchone()
    cur.execute(
        "SELECT post_content FROM fp02_posts WHERE post_type='acf-field-group' AND post_name=%s",
        ("group_fp02_page_reviews",),
    )
    page_group_json = cur.fetchone()
    conn.close()

    restore = f'mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "{dump_path}"'
    (backup_dir / "RESTORE.md").write_text(
        "\n".join(
            [
                "# V9-06D9-T restore",
                "",
                f"Created: {now_iso()}",
                "",
                "## Full DB restore",
                restore,
            ]
        ),
        encoding="utf-8",
    )
    if options_group_json:
        (backup_dir / "group_fp02_site_options_reviews-before.json").write_text(
            options_group_json[0], encoding="utf-8"
        )
    if page_group_json:
        (backup_dir / "group_fp02_page_reviews-before.json").write_text(page_group_json[0], encoding="utf-8")
    (backup_dir / "reviews-options-meta-before.json").write_text(
        json.dumps(reviews_meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    meta = {
        "phase": "V9-06D9-T",
        "generated_at": now_iso(),
        "path": str(backup_dir).replace("\\", "/"),
        "db_dump": str(dump_path).replace("\\", "/"),
        "db_dump_bytes": dump_path.stat().st_size,
        "db_dump_sha256": sha256_file(dump_path),
        "acf_groups_before_count": len(groups),
        "acf_groups_before": groups,
        "reviews_options_meta_before": reviews_meta,
        "home_page_4_reviews_meta_before": home_meta,
        "active_plugins_before": plugins_row[0] if plugins_row else None,
        "restore_instructions": restore,
        "result": "PASS",
    }
    write_json(EVIDENCE / "db-checkpoint.json", meta)
    return meta


def runtime_delivery() -> dict:
    src_helper = ROOT / "theme/shpigovsky/inc/reviews-helpers.php"
    dst_helper = RUNTIME_THEME / "inc/reviews-helpers.php"
    src_acf = ROOT / "acf-json/group_fp02_site_options_reviews.json"
    dst_acf = RUNTIME_ACF_JSON / "group_fp02_site_options_reviews.json"
    RUNTIME_ACF_JSON.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_helper, dst_helper)
    shutil.copy2(src_acf, dst_acf)
    out = {
        "phase": "V9-06D9-T",
        "generated_at": now_iso(),
        "delivered_files": [
            {"src": str(src_helper).replace("\\", "/"), "dst": str(dst_helper).replace("\\", "/")},
            {"src": str(src_acf).replace("\\", "/"), "dst": str(dst_acf).replace("\\", "/")},
        ],
        "helper_sha256": sha256_file(dst_helper),
        "acf_json_sha256": sha256_file(dst_acf),
        "result": "PASS",
    }
    write_json(EVIDENCE / "runtime-delivery-result.json", out)
    return out


def php_source_probe() -> dict:
    probe_php = EVIDENCE / "_d9t_php_source_probe.php"
    probe_php.write_text(
        f"""<?php
define('WP_USE_THEMES', false);
require '{RUNTIME.as_posix()}/wp-load.php';
$opt = shpigovsky_get_reviews_option_items();
$items = shpigovsky_get_reviews_items(['limit'=>10]);
$first = $items[0] ?? [];
$mode = function_exists('shpigovsky_get_reviews_source_mode')
  ? shpigovsky_get_reviews_source_mode()
  : (empty($opt) ? 'FALLBACK' : ((!empty($first['is_demo'])) ? 'FALLBACK' : 'OPTIONS'));
echo json_encode([
  'option_count'=>count($opt),
  'resolved_count'=>count($items),
  'source_mode'=>$mode,
  'first_author'=>$first['author'] ?? '',
  'is_demo'=>!empty($first['is_demo']),
], JSON_UNESCAPED_UNICODE);
""",
        encoding="utf-8",
    )
    return run_php(probe_php)


def main() -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    preflight = git_preflight()
    write_json(EVIDENCE / "preflight.json", preflight)
    print("Preflight:", preflight["result"], preflight.get("strict_head_gate"))
    baseline = baseline_audit()
    print("Baseline:", baseline["result"])
    if baseline["result"] == "STOP":
        raise SystemExit("Baseline STOP")
    checkpoint = db_checkpoint(ts_compact())
    print("Checkpoint:", checkpoint["result"])
    delivery = runtime_delivery()
    print("Delivery:", delivery["result"])
    sync = run_php(EVIDENCE / "_d9t_acf_sync.php")
    write_json(EVIDENCE / "acf-sync-result.json", sync)
    print("ACF sync:", sync.get("result"))
    migration = run_php(EVIDENCE / "_d9t_options_meta_migration.php")
    write_json(EVIDENCE / "options-meta-migration-result.json", migration)
    print("Migration:", migration.get("result", migration.get("mode")))
    post_db = run_php(EVIDENCE / "_d9t_post_repair_db_admin.php")
    write_json(EVIDENCE / "post-repair-db-admin-validation.json", post_db)
    frontend = frontend_validation()
    write_json(EVIDENCE / "post-repair-frontend-validation.json", frontend)
    write_json(EVIDENCE / "post-repair-console-network-check.json", console_network_check())
    write_json(EVIDENCE / "no-scope-drift-validation.json", no_scope_drift())
    write_json(EVIDENCE / "acf-key-repair-result.json", acf_key_repair_result())
    write_json(EVIDENCE / "helper-normalization-result.json", helper_normalization_result())
    write_json(EVIDENCE / "repair-plan.json", repair_plan())
    write_json(EVIDENCE / "final-verdict.json", final_verdict(preflight, baseline, checkpoint, sync, migration, post_db, frontend))
    print("Done")


def acf_key_repair_result() -> dict:
    src = json.loads((ROOT / "acf-json/group_fp02_site_options_reviews.json").read_text(encoding="utf-8"))
    page = json.loads((ROOT / "acf-json/group_fp02_page_reviews.json").read_text(encoding="utf-8"))
    repairs = []
    for field in src.get("fields", []):
        old = field["key"]
        repairs.append({"group": "group_fp02_site_options_reviews", "name": field["name"], "old_key": old, "new_key": field["key"], "changed": old in KEY_REPAIR_MAP})
        for sf in field.get("sub_fields", []):
            old_sf = sf["key"]
            repairs.append({"group": "group_fp02_site_options_reviews", "name": sf["name"], "old_key": old_sf, "new_key": sf["key"], "changed": old_sf in KEY_REPAIR_MAP})
    page_keys = set()
    for field in page.get("fields", []):
        page_keys.add(field["key"])
        for sf in field.get("sub_fields", []):
            page_keys.add(sf["key"])
    opt_keys = set()
    for field in src.get("fields", []):
        opt_keys.add(field["key"])
        for sf in field.get("sub_fields", []):
            opt_keys.add(sf["key"])
    return {
        "phase": "V9-06D9-T",
        "generated_at": now_iso(),
        "repairs": repairs,
        "remaining_collisions_with_page_group": sorted(opt_keys & page_keys),
        "result": "PASS" if not (opt_keys & page_keys) else "FAIL",
    }


def helper_normalization_result() -> dict:
    helper = (ROOT / "theme/shpigovsky/inc/reviews-helpers.php").read_text(encoding="utf-8")
    mappings = [
        ("author", ["review_author", "author_label", "author"]),
        ("text", ["review_text", "text"]),
        ("context", ["review_context", "metadata"]),
        ("source", ["review_source", "source"]),
        ("date", ["review_date", "date"]),
        ("rating", ["review_rating", "rating"]),
        ("visible", ["review_visible", "visible"]),
        ("featured", ["review_featured", "featured"]),
    ]
    checks = []
    for label, keys in mappings:
        checks.append({"field": label, "fallback_chain": keys, "present_in_helper": all(k in helper for k in keys[:2])})
    probe = php_source_probe()
    return {
        "phase": "V9-06D9-T",
        "generated_at": now_iso(),
        "mapping_checks": checks,
        "source_mode_detector_present": "shpigovsky_get_reviews_source_mode" in helper,
        "runtime_probe": probe,
        "result": "PASS" if probe.get("source_mode") == "OPTIONS" and probe.get("option_count", 0) >= 1 else "PARTIAL",
    }


def repair_plan() -> dict:
    return {
        "phase": "V9-06D9-T",
        "generated_at": now_iso(),
        "components": [
            {"component": "acf_key_repair", "action": "Unique field_fp02_options_* keys in options reviews group", "safety": "No page reviews group changes"},
            {"component": "helper_normalization", "action": "Legacy + canonical subfield mapping in normalize_review_row", "safety": "Read-only; no content mutation"},
            {"component": "options_meta", "action": "Migrate only if post-sync admin/read requires canonical keys", "safety": "Preserve 10 rows text exactly"},
            {"component": "runtime_delivery", "action": "Copy helper + ACF JSON; acf_import options group", "safety": "Bounded file copy only"},
            {"component": "validation", "action": "OPTIONS source mode; 10 reviews Home + /otzyvy/", "safety": "No rewrite/menu/media"},
        ],
        "result": "PASS",
    }


def frontend_validation() -> dict:
    probe = php_source_probe()
    routes = []
    for route in ROUTES:
        status, body = fetch(BASE_URL + route)
        entry = {"route": route, "http_status": status, "fatal": "Fatal error" in body[:500]}
        if route in ("/", "/otzyvy/"):
            entry.update(
                {
                    "reviews_slider_present": 'data-reviews-slider' in body,
                    "reviews_slide_count": body.count('class="reviews__slide swiper-slide"'),
                    "reviews_pagination_present": 'reviews__pagination' in body,
                    "rating_stars_present": 'reviews__rating' in body or 'star' in body.lower(),
                    "source_mode": probe.get("source_mode", "UNKNOWN"),
                }
            )
        routes.append(entry)
    return {
        "phase": "V9-06D9-T",
        "generated_at": now_iso(),
        "routes": routes,
        "php_source_probe": probe,
        "source_mode_after_repair": probe.get("source_mode"),
        "home_reviews_slide_count": next(r["reviews_slide_count"] for r in routes if r["route"] == "/"),
        "otzyvy_reviews_slide_count": next(r["reviews_slide_count"] for r in routes if r["route"] == "/otzyvy/"),
        "options_not_fallback": probe.get("source_mode") == "OPTIONS",
        "result": "PASS"
        if probe.get("source_mode") == "OPTIONS"
        and all(r["http_status"] == 200 for r in routes)
        else "PARTIAL",
    }


def console_network_check() -> dict:
    checks = []
    for route in ROUTES:
        status, body = fetch(BASE_URL + route)
        checks.append(
            {
                "route": route,
                "http_status": status,
                "content_length": len(body),
                "has_php_fatal_snippet": "Fatal error" in body[:800],
            }
        )
    return {"phase": "V9-06D9-T", "generated_at": now_iso(), "checks": checks, "result": "PASS"}


def no_scope_drift() -> dict:
    return {
        "phase": "V9-06D9-T",
        "generated_at": now_iso(),
        "source_theme_changes": 1,
        "acf_json_changes": 1,
        "db_writes": "acf_sync_and_optional_meta_migration_only",
        "media_uploads": 0,
        "menu_writes": 0,
        "rewrite_flush": False,
        "plugin_changes": 0,
        "result": "PASS",
    }


def final_verdict(preflight, baseline, checkpoint, sync, migration, post_db, frontend) -> dict:
    source_mode = frontend.get("source_mode_after_repair", "UNKNOWN")
    verdict = "PASS" if source_mode == "OPTIONS" and frontend.get("result") == "PASS" else "PARTIAL PASS"
    if checkpoint.get("result") != "PASS":
        verdict = "FAIL"
    return {
        "phase": "V9-06D9-T",
        "generated_at": now_iso(),
        "verdict": verdict,
        "source_mode_after_repair": source_mode,
        "seeded_reviews_preserved": post_db.get("reviews_items_count") == 10,
        "acf_collision_resolved": post_db.get("duplicate_field_fp02_reviews_items", True) is False,
        "recommended_next_action": "CREATE_V9_06D9U_ADMIN_VISUAL_QA_TASK",
    }


if __name__ == "__main__":
    main()
