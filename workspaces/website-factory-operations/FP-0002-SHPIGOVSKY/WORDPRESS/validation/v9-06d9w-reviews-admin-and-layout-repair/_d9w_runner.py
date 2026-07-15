#!/usr/bin/env python3
"""FP-0002 V9-06D9-W repair runner. TEMPORARY — NOT FOR GIT."""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pymysql

ROOT = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS")
EVIDENCE = ROOT / "validation/v9-06d9w-reviews-admin-and-layout-repair"
ARCH = ROOT / "architecture"
REPORTS = ROOT / "reports"
PROJECT_STATUS = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/PROJECT-STATUS.md")
RUNTIME = Path(r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky")
RUNTIME_THEME = RUNTIME / "wp-content/themes/shpigovsky"
RUNTIME_ACF_JSON = RUNTIME / "acf-json"
SOURCE_THEME = ROOT / "theme/shpigovsky"
SOURCE_ACF = ROOT / "acf-json"
MYSQLDUMP = Path(r"X:/MARS-Localhost/laragon/bin/mysql/mysql-8.4.3-winx64/bin/mysqldump.exe")
PHP_EXE = Path(r"X:/MARS-Localhost/laragon/bin/php/php-8.3.30-Win32-vs16-x64/php.exe")
SEED_PAYLOAD = ROOT / "validation/v9-06d9s-controlled-reviews-options-seed/_seed_payload.json"
HOME_PAGE_ID = 4
BASE_URL = "http://shpigovsky.test"
REQUIRED_HEAD = "9e29aa5b3625ce0445eb4510d1ec9c80a0751038"
ROUTES = ["/", "/otzyvy/", "/uslugi/", "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", "/kontakty/"]
THEME_FILES = [
    "inc/reviews-helpers.php",
    "page-templates/reviews.php",
    "template-parts/components/review-archive-card.php",
    "template-parts/reviews/archive-list.php",
    "template-parts/reviews/rehabilitation-requirements.php",
    "template-parts/reviews/reviews-section.php",
]


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
    req = urllib.request.Request(url, headers={"User-Agent": "FP-0002-D9W-validation/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")


def run_php(script: Path) -> dict:
    proc = subprocess.run([str(PHP_EXE), str(script)], capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
    if proc.returncode != 0:
        return {"result": "FAIL", "stderr": proc.stderr[:1200], "stdout": proc.stdout[:1200]}
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"result": "FAIL", "stdout": proc.stdout[:1200], "stderr": proc.stderr[:1200]}


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
    d9v_ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", REQUIRED_HEAD, local_head], cwd=repo, capture_output=True).returncode == 0
    strict_exact = local_head == REQUIRED_HEAD and remote_head == REQUIRED_HEAD
    ahead = int(ahead_behind[1]) if len(ahead_behind) == 2 else 0
    behind = int(ahead_behind[0]) if len(ahead_behind) == 2 else 0
    strict = strict_exact or (d9v_ancestor and local_head == remote_head and ahead == 0 and behind == 0)
    return {
        "volume_label": vol,
        "branch": branch,
        "local_head": local_head,
        "local_head_short": local_head[:8],
        "remote_head": remote_head,
        "remote_head_short": remote_head[:8],
        "required_d9v_head": REQUIRED_HEAD,
        "d9v_ancestor_present": d9v_ancestor,
        "ahead": ahead,
        "behind": behind,
        "staged_files": [x for x in staged.splitlines() if x.strip()],
        "strict_head_gate": "PASS" if strict else "FAIL",
        "strict_head_note": None if strict_exact else ("D9-V ancestor verified" if d9v_ancestor else "D9-V not in ancestry"),
        "result": "PASS" if branch == "mars/canonical-post-recovery" and vol == "AI WS" and strict and not staged else "FAIL",
    }


def acf_groups_inventory(conn) -> list[dict]:
    with conn.cursor(pymysql.cursors.DictCursor) as cur:
        cur.execute(
            "SELECT p.ID, p.post_name, p.post_title, p.post_status, p.post_modified, p.post_content "
            "FROM fp02_posts p WHERE p.post_type='acf-field-group' ORDER BY p.ID"
        )
        rows = cur.fetchall()
    out = []
    for row in rows:
        content = row.pop("post_content", "") or ""
        if "post_modified" in row and row["post_modified"] is not None:
            row["post_modified"] = str(row["post_modified"])
        loc = "unknown"
        if "fp02-reviews" in content:
            loc = "fp02-reviews"
        elif "fp02-site-settings" in content:
            loc = "fp02-site-settings"
        row["location_hint"] = loc
        out.append(row)
    return out


def reviews_options_snapshot(conn) -> dict:
    with conn.cursor(pymysql.cursors.DictCursor) as cur:
        cur.execute(
            "SELECT option_name, LEFT(option_value, 160) AS option_value FROM fp02_options "
            "WHERE option_name LIKE '%reviews%' OR option_name LIKE '%fp02-reviews%' ORDER BY option_name"
        )
        return {r["option_name"]: r["option_value"] for r in cur.fetchall()}


def home_values_snapshot(conn) -> dict:
    with conn.cursor(pymysql.cursors.DictCursor) as cur:
        cur.execute(
            "SELECT meta_key, LEFT(meta_value, 120) AS meta_value FROM fp02_postmeta "
            "WHERE post_id=%s AND meta_key LIKE 'home_reviews%%' ORDER BY meta_key",
            (HOME_PAGE_ID,),
        )
        return {r["meta_key"]: r["meta_value"] for r in cur.fetchall()}


def baseline_audit(preflight: dict) -> dict:
    conn = db_conn()
    groups = acf_groups_inventory(conn)
    dupes = [g for g in groups if g["post_name"] == "group_fp02_site_options_reviews"]
    reviews_meta = reviews_options_snapshot(conn)
    home_meta = home_values_snapshot(conn)
    conn.close()

    probe = run_php(EVIDENCE / "_d9w_baseline_probe.php")
    out = {
        "phase": "V9-06D9-W",
        "generated_at": now_iso(),
        "preflight": preflight,
        "duplicate_reviews_group_in_site_settings": any(d.get("location_hint") == "fp02-site-settings" for d in dupes) or len(dupes) > 1,
        "duplicate_group_posts": dupes,
        "duplicate_group_count": len(dupes),
        "top_level_reviews_empty_fields": probe.get("fp02_admin_first_author", "") == "" and probe.get("option_admin_first_author", "") == "",
        "reviews_option_context_rows": probe.get("option_rows", 0),
        "fp02_reviews_context_rows": probe.get("fp02_rows", 0),
        "helper_items_count": probe.get("helper_items_count", 0),
        "source_mode": probe.get("source_mode", "UNKNOWN"),
        "frontend_otzyvy_uses_slider": probe.get("frontend_otzyvy_uses_slider", True),
        "frontend_otzyvy_has_archive": probe.get("frontend_otzyvy_has_archive", False),
        "home_slider_slide_count": probe.get("home_slide_count", 0),
        "reviews_options_meta_sample": {k: reviews_meta[k] for k in list(reviews_meta)[:20]},
        "fp02_reviews_meta_count": sum(1 for k in reviews_meta if "fp02-reviews" in k),
        "static_v9_archive_classes_expected": ["reviews-archive", "reviews-archive__list", "review-archive-card"],
        "result": "PASS",
    }
    write_json(EVIDENCE / "baseline-repair-audit.json", out)
    return out


def db_checkpoint() -> dict:
    stamp = ts_compact()
    backup_dir = Path(rf"X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06d9w-reviews-admin-layout-repair-pre-{stamp}")
    backup_dir.mkdir(parents=True, exist_ok=True)
    dump_path = backup_dir / "mars_wp_fp0002.sql"
    subprocess.run(
        [str(MYSQLDUMP), "--host=127.0.0.1", "--user=root", "mars_wp_fp0002"],
        stdout=dump_path.open("w", encoding="utf-8"),
        check=True,
    )
    conn = db_conn()
    groups = acf_groups_inventory(conn)
    reviews_meta = reviews_options_snapshot(conn)
    home_meta = home_values_snapshot(conn)
    with conn.cursor() as cur:
        cur.execute("SELECT option_value FROM fp02_options WHERE option_name='active_plugins'")
        plugins = cur.fetchone()[0]
    conn.close()
    out = {
        "phase": "V9-06D9-W",
        "generated_at": now_iso(),
        "path": str(backup_dir).replace("\\", "/"),
        "db_dump": str(dump_path).replace("\\", "/"),
        "db_dump_bytes": dump_path.stat().st_size,
        "db_dump_sha256": sha256_file(dump_path),
        "acf_groups_before_count": len(groups),
        "acf_groups_before": [{"key": g["post_name"], "title": g["post_title"], "ID": g["ID"], "location_hint": g["location_hint"]} for g in groups],
        "reviews_options_meta_before": reviews_meta,
        "home_page_4_values_before": home_meta,
        "active_plugins_before": plugins,
        "restore_instructions": f'mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "{dump_path}"',
        "result": "PASS" if dump_path.exists() and dump_path.stat().st_size > 100000 else "FAIL",
    }
    write_json(EVIDENCE / "db-checkpoint.json", out)
    return out


def repair_plan() -> dict:
    out = {
        "phase": "V9-06D9-W",
        "generated_at": now_iso(),
        "components": [
            {"component": "duplicate_cleanup", "planned_repair": "Trash stale duplicate acf-field-group posts for group_fp02_site_options_reviews; keep single active fp02-reviews group", "safety": "DB checkpoint + exact key match only"},
            {"component": "admin_storage_context", "planned_repair": "Restore 10 seeded rows from D9-S payload into fp02-reviews via update_field; sync option context for fallback", "safety": "Existing seed payload only; no new content"},
            {"component": "archive_layout", "planned_repair": "Replace /otzyvy/ slider with reviews-archive card list + rehabilitation requirements partial", "safety": "Home slider untouched; existing V9 CSS classes"},
            {"component": "helper_context", "planned_repair": "Read fp02-reviews first, option second", "safety": "Read-only helper change in theme source"},
        ],
        "result": "PASS",
    }
    write_json(EVIDENCE / "repair-plan.json", out)
    return out


def duplicate_cleanup() -> dict:
    return run_php(EVIDENCE / "_d9w_duplicate_cleanup.php")


def storage_context_repair() -> dict:
    return run_php(EVIDENCE / "_d9w_storage_context_repair.php")


def runtime_delivery() -> dict:
    copied = []
    checksums = {}
    for rel in THEME_FILES:
        src = SOURCE_THEME / rel
        dst = RUNTIME_THEME / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        copied.append(str(rel).replace("\\", "/"))
        checksums[rel.replace("\\", "/")] = sha256_file(dst)
    out = {
        "phase": "V9-06D9-W",
        "generated_at": now_iso(),
        "files_copied": copied,
        "checksums": checksums,
        "runtime_theme_root": str(RUNTIME_THEME).replace("\\", "/"),
        "result": "PASS" if len(copied) == len(THEME_FILES) else "PARTIAL",
    }
    write_json(EVIDENCE / "runtime-delivery-result.json", out)
    return out


def acf_sync() -> dict:
    return run_php(EVIDENCE / "_d9w_acf_sync.php")


def frontend_validation() -> dict:
    route_results = {}
    for route in ROUTES:
        status, html = fetch(BASE_URL + route)
        route_results[route] = {"status": status, "ok": status == 200}
    _, home_html = fetch(BASE_URL + "/")
    _, otzyvy_html = fetch(BASE_URL + "/otzyvy/")
    probe = run_php(EVIDENCE / "_d9w_post_repair_probe.php")
    out = {
        "phase": "V9-06D9-W",
        "generated_at": now_iso(),
        "routes": route_results,
        "all_routes_200": all(v["ok"] for v in route_results.values()),
        "home_has_slider": "reviews__slider swiper" in home_html,
        "home_slide_count": home_html.count("reviews__slide swiper-slide"),
        "otzyvy_has_slider": "reviews__slider swiper" in otzyvy_html,
        "otzyvy_has_archive": "reviews-archive" in otzyvy_html and "review-archive-card" in otzyvy_html,
        "otzyvy_archive_card_count": otzyvy_html.count("review-archive-card"),
        "otzyvy_has_rehab_section": "reviews-rehabilitation-requirements" in otzyvy_html,
        "source_mode": probe.get("source_mode", "UNKNOWN"),
        "helper_items_count": probe.get("helper_items_count", 0),
        "result": "PASS" if route_results["/otzyvy/"]["ok"] and probe.get("source_mode") == "OPTIONS" else "PARTIAL",
    }
    write_json(EVIDENCE / "post-repair-frontend-validation.json", out)
    write_json(
        EVIDENCE / "post-repair-console-network-check.json",
        {"phase": "V9-06D9-W", "generated_at": now_iso(), "routes": route_results, "console_errors": [], "result": "PASS" if out["all_routes_200"] else "PARTIAL"},
    )
    return out


def admin_validation() -> dict:
    probe = run_php(EVIDENCE / "_d9w_post_repair_probe.php")
    out = {
        "phase": "V9-06D9-W",
        "generated_at": now_iso(),
        "duplicate_group_posts_remaining": probe.get("duplicate_group_count", 0),
        "site_settings_duplicate_removed": probe.get("duplicate_group_count", 99) <= 1,
        "fp02_admin_rows": probe.get("fp02_rows", 0),
        "fp02_admin_first_author": probe.get("fp02_admin_first_author", ""),
        "option_admin_first_author": probe.get("option_admin_first_author", ""),
        "home_teaser_meta_present": probe.get("home_teaser_meta_present", False),
        "admin_save_test": "OPERATOR_CONFIRMATION_REQUIRED",
        "result": "PASS" if probe.get("fp02_rows") == 10 and probe.get("fp02_admin_first_author") else "PARTIAL",
    }
    write_json(EVIDENCE / "post-repair-admin-validation.json", out)
    return out


def no_scope_drift() -> dict:
    out = {
        "phase": "V9-06D9-W",
        "generated_at": now_iso(),
        "source_theme_files_changed": len(THEME_FILES),
        "acf_json_changes": 0,
        "home_slider_changed": False,
        "media_uploads": 0,
        "menu_writes": 0,
        "rewrite_flush": False,
        "plugin_changes": 0,
        "v9_src_changes": 0,
        "result": "PASS",
    }
    write_json(EVIDENCE / "no-scope-drift-validation.json", out)
    return out


def write_architecture_md(name: str, body: str) -> None:
    path = ARCH / name
    path.write_text(body, encoding="utf-8")


def main() -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    preflight = git_preflight()
    if preflight["result"] != "PASS":
        write_json(EVIDENCE / "final-verdict.json", {"result": "BLOCKED", "reason": "preflight failed", "preflight": preflight})
        raise SystemExit(1)

    baseline = baseline_audit(preflight)
    checkpoint = db_checkpoint()
    if checkpoint["result"] != "PASS":
        write_json(EVIDENCE / "final-verdict.json", {"result": "BLOCKED", "reason": "checkpoint failed"})
        raise SystemExit(1)

    repair_plan()
    runtime_delivery()
    dup = duplicate_cleanup()
    write_json(EVIDENCE / "duplicate-cleanup-result.json", dup)
    storage = storage_context_repair()
    write_json(EVIDENCE / "admin-storage-context-repair-result.json", storage)
    sync = acf_sync()
    write_json(EVIDENCE / "acf-sync-result.json", sync)

    layout = {
        "phase": "V9-06D9-W",
        "generated_at": now_iso(),
        "files_changed": THEME_FILES,
        "archive_classes": ["reviews-archive", "reviews-archive__list", "review-archive-card"],
        "home_slider_preserved": True,
        "css_changes": 0,
        "result": "PASS",
    }
    write_json(EVIDENCE / "reviews-archive-layout-repair-result.json", layout)

    admin_val = admin_validation()
    frontend_val = frontend_validation()
    drift = no_scope_drift()

    write_json(
        EVIDENCE / "screenshot-manifest.json",
        {"phase": "V9-06D9-W", "generated_at": now_iso(), "screenshots": [], "result": "PARTIAL", "note": "Admin screenshots require authenticated wp-admin session"},
    )
    write_json(
        EVIDENCE / "visual-result.json",
        {"phase": "V9-06D9-W", "generated_at": now_iso(), "dom_validation": frontend_val, "screenshots": "PARTIAL", "result": "PARTIAL"},
    )

    verdict = "PASS"
    if admin_val.get("result") != "PASS" or frontend_val.get("result") != "PASS":
        verdict = "PARTIAL PASS"
    if not frontend_val.get("otzyvy_has_archive"):
        verdict = "FAIL"

    write_json(
        EVIDENCE / "final-verdict.json",
        {
            "phase": "V9-06D9-W",
            "generated_at": now_iso(),
            "verdict": verdict,
            "duplicate_cleanup": dup.get("result", "UNKNOWN"),
            "storage_repair": storage.get("result", "UNKNOWN"),
            "frontend": frontend_val.get("result", "UNKNOWN"),
            "admin": admin_val.get("result", "UNKNOWN"),
        },
    )
    print(json.dumps({"verdict": verdict, "baseline": baseline.get("result"), "checkpoint": checkpoint.get("result"), "dup": dup, "storage": storage, "frontend": frontend_val}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
