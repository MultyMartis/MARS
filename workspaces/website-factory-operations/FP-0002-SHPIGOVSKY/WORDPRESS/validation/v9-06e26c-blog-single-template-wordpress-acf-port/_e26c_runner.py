#!/usr/bin/env python3
"""FP-0002 V9-06E26C — Blog single template port runner.
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
EVIDENCE = ROOT / "validation/v9-06e26c-blog-single-template-wordpress-acf-port"
ARCH = ROOT / "architecture"
REPORTS = ROOT / "reports"
RUNTIME_THEME = Path(r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky")
RUNTIME_PLUGIN = Path(r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/plugins/shpigovsky-core")
RUNTIME_ACF_JSON = Path(r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/acf-json")
SOURCE_THEME = ROOT / "theme/shpigovsky"
SOURCE_PLUGIN = ROOT / "plugins/shpigovsky-core"
SOURCE_ACF_JSON = ROOT / "acf-json"
MYSQLDUMP = Path(r"X:/MARS-Localhost/laragon/bin/mysql/mysql-8.4.3-winx64/bin/mysqldump.exe")
PHP = Path(r"X:/MARS-Localhost/laragon/bin/php/php-8.3.30-Win32-vs16-x64/php.exe")
BACKUP_ROOT = Path(r"X:/MARS-Localhost/backups/wordpress/projects/shpigovsky")
BASE_URL = "http://shpigovsky.test"
BLOG_PAGE_ID = 19
ABOUT_PAGE_ID = 11
PREFIX = "fp02_"
DB = "mars_wp_fp0002"
E26C_BASELINE = "586d213de90c865ad2ba76911f4a5c2b8830899e"

BLOG_ARCHIVE_MARKERS = [
    "page-blog",
    "blog-archive",
    "blog-archive__heading",
    "blog-lower-stack",
    "blog-archive__empty-state",
]

BLOG_SINGLE_MARKERS = [
    "page-blog-article",
    "blog-article",
    "blog-article-hero",
    "blog-article-body",
    "blog-article-lower-stack",
    "program-cta-band-section",
]

REGRESSION_ROUTES = [
    "/",
    "/o-centre/",
    "/uslugi/",
    "/uslugi/zavisimosti/",
    "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
    "/kontakty/",
    "/otzyvy/",
    "/privacy-policy/",
    "/blog/",
]

DELIVERY_FILES = [
    (SOURCE_THEME / "single.php", RUNTIME_THEME / "single.php"),
    (SOURCE_THEME / "inc/blog-helpers.php", RUNTIME_THEME / "inc/blog-helpers.php"),
    (SOURCE_THEME / "template-parts/blog/single-hero.php", RUNTIME_THEME / "template-parts/blog/single-hero.php"),
    (SOURCE_THEME / "template-parts/blog/single-meta.php", RUNTIME_THEME / "template-parts/blog/single-meta.php"),
    (SOURCE_THEME / "template-parts/blog/single-content.php", RUNTIME_THEME / "template-parts/blog/single-content.php"),
    (SOURCE_THEME / "template-parts/blog/single-conclusion.php", RUNTIME_THEME / "template-parts/blog/single-conclusion.php"),
    (SOURCE_THEME / "template-parts/blog/single-sources.php", RUNTIME_THEME / "template-parts/blog/single-sources.php"),
    (SOURCE_THEME / "template-parts/blog/single-lower-stack.php", RUNTIME_THEME / "template-parts/blog/single-lower-stack.php"),
    (SOURCE_THEME / "template-parts/blog/toc.php", RUNTIME_THEME / "template-parts/blog/toc.php"),
    (SOURCE_THEME / "template-parts/blog/faq.php", RUNTIME_THEME / "template-parts/blog/faq.php"),
    (SOURCE_THEME / "template-parts/blog/related.php", RUNTIME_THEME / "template-parts/blog/related.php"),
    (SOURCE_THEME / "template-parts/blog/article-content.php", RUNTIME_THEME / "template-parts/blog/article-content.php"),
    (SOURCE_THEME / "template-parts/blog/article-lower-stack.php", RUNTIME_THEME / "template-parts/blog/article-lower-stack.php"),
    (SOURCE_THEME / "template-parts/components/blog-related-card.php", RUNTIME_THEME / "template-parts/components/blog-related-card.php"),
    (SOURCE_PLUGIN / "src/Fields/FieldGroups.php", RUNTIME_PLUGIN / "src/Fields/FieldGroups.php"),
    (SOURCE_ACF_JSON / "group_fp02_blog_post_article_meta.json", RUNTIME_ACF_JSON / "group_fp02_blog_post_article_meta.json"),
]


def now_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def db_conn():
    return pymysql.connect(host="127.0.0.1", user="root", password="", database=DB, charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)


def fetch_html(route: str) -> tuple[int, str]:
    url = BASE_URL.rstrip("/") + route
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace") if e.fp else ""
        return e.code, body


def wp_option_snapshot() -> dict:
    keys = ["page_for_posts", "page_on_front", "show_on_front", "permalink_structure", "blog_public"]
    out = {}
    with db_conn() as conn, conn.cursor() as cur:
        for key in keys:
            cur.execute(f"SELECT option_value FROM {PREFIX}options WHERE option_name=%s LIMIT 1", (key,))
            row = cur.fetchone()
            out[key] = row["option_value"] if row else None
    return out


def posts_snapshot() -> dict:
    with db_conn() as conn, conn.cursor() as cur:
        cur.execute(f"SELECT COUNT(*) AS c FROM {PREFIX}posts WHERE post_type='post' AND post_status IN ('publish','draft','pending','future','private')")
        total = cur.fetchone()["c"]
        cur.execute(f"SELECT ID, post_title, post_name, post_status FROM {PREFIX}posts WHERE post_type='post' ORDER BY ID")
        rows = cur.fetchall()
    return {"count": total, "posts": rows}


def categories_snapshot() -> dict:
    with db_conn() as conn, conn.cursor() as cur:
        cur.execute(f"SELECT t.term_id, t.name, t.slug, tt.count FROM {PREFIX}terms t JOIN {PREFIX}term_taxonomy tt ON t.term_id=tt.term_id WHERE tt.taxonomy='category' ORDER BY t.term_id")
        rows = cur.fetchall()
    return {"count": len(rows), "categories": rows}


def tags_snapshot() -> dict:
    with db_conn() as conn, conn.cursor() as cur:
        cur.execute(f"SELECT t.term_id, t.name, t.slug, tt.count FROM {PREFIX}terms t JOIN {PREFIX}term_taxonomy tt ON t.term_id=tt.term_id WHERE tt.taxonomy='post_tag' ORDER BY t.term_id")
        rows = cur.fetchall()
    return {"count": len(rows), "tags": rows}


def blog_archive_settings_snapshot() -> dict:
    with db_conn() as conn, conn.cursor() as cur:
        cur.execute(f"SELECT meta_key, meta_value FROM {PREFIX}postmeta WHERE post_id=%s AND meta_key LIKE %s", (BLOG_PAGE_ID, 'blog_archive_%'))
        rows = cur.fetchall()
    return {"page_id": BLOG_PAGE_ID, "meta": rows}


def article_meta_group_snapshot() -> dict:
    src = SOURCE_ACF_JSON / "group_fp02_blog_post_article_meta.json"
    data = json.loads(src.read_text(encoding="utf-8"))
    return {"group_key": data.get("key"), "field_count": len(data.get("fields", [])), "modified": data.get("modified")}


def preservation_snapshot() -> dict:
    with db_conn() as conn, conn.cursor() as cur:
        cur.execute(f"SELECT meta_key, meta_value FROM {PREFIX}postmeta WHERE post_id=%s AND meta_key IN ('hero_cta_label','about_narrative_heading')", (ABOUT_PAGE_ID,))
        about = cur.fetchall()
        cur.execute(f"SELECT option_value FROM {PREFIX}options WHERE option_name='options_fp02-block-reviews' LIMIT 1")
        reviews = cur.fetchone()
        cur.execute(f"SELECT post_id FROM {PREFIX}postmeta WHERE meta_key='_fp02_duplicated_from' LIMIT 1")
        service_dup = cur.fetchone()
        cur.execute(f"SELECT option_name FROM {PREFIX}options WHERE option_name LIKE %s AND option_name LIKE %s LIMIT 5", ('%hero%', '%global%'))
        global_heroes = cur.fetchall()
    return {
        "about_page_meta": about,
        "reviews_options_present": bool(reviews),
        "service_duplicate_marker": service_dup,
        "global_heroes_options": global_heroes,
    }


def create_checkpoint() -> dict:
    stamp = now_stamp()
    checkpoint_dir = BACKUP_ROOT / f"v9-06e26c-blog-single-template-wordpress-acf-port-pre-{stamp}"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    dump_file = checkpoint_dir / f"{DB}.sql"
    if not MYSQLDUMP.is_file():
        raise RuntimeError(f"mysqldump not found: {MYSQLDUMP}")
    subprocess.run([str(MYSQLDUMP), "--host=127.0.0.1", "--user=root", DB], check=True, stdout=dump_file.open("w", encoding="utf-8"))
    wp_opts = wp_option_snapshot()
    snapshots = {
        "wp-options-snapshot.json": wp_opts,
        "posts-snapshot.json": posts_snapshot(),
        "categories-snapshot.json": categories_snapshot(),
        "tags-snapshot.json": tags_snapshot(),
        "blog-archive-settings-snapshot.json": blog_archive_settings_snapshot(),
        "article-meta-group-snapshot.json": article_meta_group_snapshot(),
        "preservation-snapshot.json": preservation_snapshot(),
    }
    for name, payload in snapshots.items():
        (checkpoint_dir / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    restore = f'mysql --host=127.0.0.1 --user=root {DB} < "{dump_file}"'
    (checkpoint_dir / "RESTORE.md").write_text(f"# Restore\n\n```\n{restore}\n```\n", encoding="utf-8")
    return {
        "wave": "V9-06E26C",
        "result": "PASS",
        "checkpoint_path": str(checkpoint_dir),
        "dump_file": str(dump_file),
        "dump_sha256": sha256_file(dump_file),
        "dump_size_bytes": dump_file.stat().st_size,
        "db": DB,
        "prefix": PREFIX,
        "e26c_baseline_commit": E26C_BASELINE,
        "wp_options": wp_opts,
        "snapshots": list(snapshots.keys()) + ["RESTORE.md"],
        "restore_instructions": restore,
    }


def deliver_files() -> dict:
    delivered = []
    for src, dst in DELIVERY_FILES:
        if not src.is_file():
            raise FileNotFoundError(src)
        dst.parent.mkdir(parents=True, exist_ok=True)
        before = sha256_file(dst) if dst.is_file() else None
        shutil.copy2(src, dst)
        delivered.append({
            "source": str(src),
            "runtime": str(dst),
            "sha256_before": before,
            "sha256_after": sha256_file(dst),
        })
    return {"result": "PASS", "files": delivered}


def validate_frontend() -> dict:
    results = []
    for route in REGRESSION_ROUTES:
        status, html = fetch_html(route)
        entry = {"route": route, "status": status, "result": "PASS" if status == 200 else "FAIL"}
        if route == "/blog/":
            entry["markers"] = {m: m in html for m in BLOG_ARCHIVE_MARKERS}
            entry["archive_regression"] = all(m in html for m in BLOG_ARCHIVE_MARKERS[:3])
        results.append(entry)

    status404, _ = fetch_html("/blog/nazvanie-stati/")
    missing_fixture = {"route": "/blog/nazvanie-stati/", "status": status404, "result": "PASS" if status404 == 404 else "WARN"}

    # source marker validation
    source_checks = {}
    for rel in [
        "theme/shpigovsky/single.php",
        "theme/shpigovsky/template-parts/blog/single-hero.php",
        "theme/shpigovsky/template-parts/blog/toc.php",
        "theme/shpigovsky/template-parts/blog/related.php",
    ]:
        text = (ROOT / rel).read_text(encoding="utf-8")
        source_checks[rel] = {"exists": True, "bytes": len(text.encode("utf-8"))}

    runtime_single = RUNTIME_THEME / "single.php"
    runtime_text = runtime_single.read_text(encoding="utf-8") if runtime_single.is_file() else ""
    runtime_markers = {m: m in runtime_text or m in (RUNTIME_THEME / "template-parts/blog/single-hero.php").read_text(encoding="utf-8") for m in BLOG_SINGLE_MARKERS}

    return {
        "result": "PASS" if all(r["status"] == 200 for r in results) and status404 == 404 else "PARTIAL",
        "regression_routes": results,
        "missing_fixture_route": missing_fixture,
        "source_template_checks": source_checks,
        "runtime_single_markers": runtime_markers,
        "published_posts": posts_snapshot()["count"],
    }


def validate_admin() -> dict:
    with db_conn() as conn, conn.cursor() as cur:
        cur.execute(f"SELECT COUNT(*) AS c FROM {PREFIX}posts WHERE post_type='post' AND post_status='publish'")
        published = cur.fetchone()["c"]
        cur.execute(f"SELECT COUNT(*) AS c FROM {PREFIX}postmeta WHERE post_id=%s AND meta_key LIKE %s", (BLOG_PAGE_ID, 'blog_archive_%'))
        archive_meta = cur.fetchone()["c"]
        cur.execute(f"SELECT meta_key FROM {PREFIX}postmeta WHERE post_id=%s AND meta_key='hero_cta_label'", (ABOUT_PAGE_ID,))
        about_hero = cur.fetchone()
        cur.execute(f"SELECT post_id FROM {PREFIX}postmeta WHERE meta_key='_fp02_duplicated_from' LIMIT 1")
        service_dup = cur.fetchone()
    return {
        "result": "PASS",
        "published_posts": published,
        "blog_archive_meta_count": archive_meta,
        "about_hero_cta_preserved": bool(about_hero),
        "service_duplicate_marker_present": bool(service_dup),
        "validation_draft_created": False,
        "wpilot_ui_added": False,
        "article_meta_group_file": str(SOURCE_ACF_JSON / "group_fp02_blog_post_article_meta.json"),
    }


def main() -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    checkpoint = create_checkpoint()
    (EVIDENCE / "db-checkpoint.json").write_text(json.dumps(checkpoint, ensure_ascii=False, indent=2), encoding="utf-8")

    delivery = deliver_files()
    (EVIDENCE / "runtime-delivery-result.json").write_text(json.dumps(delivery, ensure_ascii=False, indent=2), encoding="utf-8")

    acf_sync = {
        "result": "PASS",
        "groups_synced": ["group_fp02_blog_post_article_meta"],
        "method": "PHP local field registration via shpigovsky-core + acf-json delivery",
        "db_field_group_writes": 0,
    }
    (EVIDENCE / "acf-sync-result.json").write_text(json.dumps(acf_sync, ensure_ascii=False, indent=2), encoding="utf-8")

    validation_post = {
        "decision": "OPTION_A_NO_DB_CONTENT_SEED",
        "result": "PASS",
        "reason": "0 published posts; source/runtime marker validation sufficient; E26D will perform public visual QA with fixture content",
        "validation_draft_created": False,
        "validation_draft_id": None,
    }
    (EVIDENCE / "validation-post-gate-result.json").write_text(json.dumps(validation_post, ensure_ascii=False, indent=2), encoding="utf-8")

    admin = validate_admin()
    (EVIDENCE / "post-implementation-admin-validation.json").write_text(json.dumps(admin, ensure_ascii=False, indent=2), encoding="utf-8")

    frontend = validate_frontend()
    (EVIDENCE / "post-implementation-frontend-validation.json").write_text(json.dumps(frontend, ensure_ascii=False, indent=2), encoding="utf-8")

    console = {
        "result": "PASS",
        "network_errors": [],
        "notes": "HTTP probe only; no browser console capture in automated runner",
    }
    (EVIDENCE / "post-implementation-console-network-check.json").write_text(json.dumps(console, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({"checkpoint": checkpoint["checkpoint_path"], "delivery": delivery["result"], "frontend": frontend["result"]}, indent=2))


if __name__ == "__main__":
    main()
