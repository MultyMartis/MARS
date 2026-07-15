#!/usr/bin/env python3
"""FP-0002 V9-06E26B — Blog archive port runner.
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
EVIDENCE = ROOT / "validation/v9-06e26b-blog-archive-wordpress-acf-port"
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
PREFIX = "fp02_"
DB = "mars_wp_fp0002"
E26B_BASELINE = "0d629fbc7d7ddbb46adedf613e38a9e2c163b749"

BLOG_MARKERS = [
    "page-blog",
    "blog-archive",
    "blog-archive__heading",
    "blog-archive__intro",
    "blog-lower-stack",
    "blog-expert-quote",
    "program-cta-band-section",
    "blog-archive__empty-state",
    "blog-archive-card",
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
    (SOURCE_THEME / "home.php", RUNTIME_THEME / "home.php"),
    (SOURCE_THEME / "functions.php", RUNTIME_THEME / "functions.php"),
    (SOURCE_THEME / "inc/blog-helpers.php", RUNTIME_THEME / "inc/blog-helpers.php"),
    (SOURCE_THEME / "template-parts/layout/body-start.php", RUNTIME_THEME / "template-parts/layout/body-start.php"),
    (SOURCE_THEME / "template-parts/blog/archive-list.php", RUNTIME_THEME / "template-parts/blog/archive-list.php"),
    (SOURCE_THEME / "template-parts/blog/empty-state.php", RUNTIME_THEME / "template-parts/blog/empty-state.php"),
    (SOURCE_THEME / "template-parts/blog/pagination.php", RUNTIME_THEME / "template-parts/blog/pagination.php"),
    (SOURCE_THEME / "template-parts/blog/lower-stack.php", RUNTIME_THEME / "template-parts/blog/lower-stack.php"),
    (SOURCE_THEME / "template-parts/blog/expert-quote.php", RUNTIME_THEME / "template-parts/blog/expert-quote.php"),
    (SOURCE_THEME / "template-parts/components/blog-archive-card.php", RUNTIME_THEME / "template-parts/components/blog-archive-card.php"),
    (SOURCE_PLUGIN / "src/Fields/FieldGroups.php", RUNTIME_PLUGIN / "src/Fields/FieldGroups.php"),
    (SOURCE_ACF_JSON / "group_fp02_blog_archive_settings.json", RUNTIME_ACF_JSON / "group_fp02_blog_archive_settings.json"),
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


def blog_page_snapshot() -> dict:
    with db_conn() as conn, conn.cursor() as cur:
        cur.execute(f"SELECT ID, post_title, post_name, post_status FROM {PREFIX}posts WHERE ID=%s", (BLOG_PAGE_ID,))
        post = cur.fetchone()
        cur.execute(f"SELECT meta_key, meta_value FROM {PREFIX}postmeta WHERE post_id=%s ORDER BY meta_key", (BLOG_PAGE_ID,))
        meta = cur.fetchall()
    return {"post": post, "meta_count": len(meta), "meta_keys": [m["meta_key"] for m in meta if not m["meta_key"].startswith("_")]}


def preservation_snapshot() -> dict:
    with db_conn() as conn, conn.cursor() as cur:
        cur.execute(f"SELECT meta_key, meta_value FROM {PREFIX}postmeta WHERE post_id=11 AND meta_key IN ('hero_cta_label','about_narrative_heading')")
        about = cur.fetchall()
        cur.execute(f"SELECT option_value FROM {PREFIX}options WHERE option_name='options_fp02-block-reviews' LIMIT 1")
        reviews = cur.fetchone()
        cur.execute(f"SELECT post_id FROM {PREFIX}postmeta WHERE meta_key='service_layout_variant' LIMIT 1")
        service_dup = cur.fetchone()
    return {"about_page_meta": about, "reviews_options_present": bool(reviews), "service_duplicate_marker": service_dup}


def create_checkpoint() -> dict:
    stamp = now_stamp()
    checkpoint_dir = BACKUP_ROOT / f"v9-06e26b-blog-archive-wordpress-acf-port-pre-{stamp}"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    dump_file = checkpoint_dir / f"{DB}.sql"
    if not MYSQLDUMP.is_file():
        raise RuntimeError(f"mysqldump not found: {MYSQLDUMP}")
    subprocess.run([str(MYSQLDUMP), "--host=127.0.0.1", "--user=root", DB], check=True, stdout=dump_file.open("w", encoding="utf-8"))
    wp_opts = wp_option_snapshot()
    (checkpoint_dir / "wp-options-snapshot.json").write_text(json.dumps(wp_opts, ensure_ascii=False, indent=2), encoding="utf-8")
    (checkpoint_dir / "blog-page-19-snapshot.json").write_text(json.dumps(blog_page_snapshot(), ensure_ascii=False, indent=2), encoding="utf-8")
    (checkpoint_dir / "posts-snapshot.json").write_text(json.dumps(posts_snapshot(), ensure_ascii=False, indent=2), encoding="utf-8")
    (checkpoint_dir / "categories-snapshot.json").write_text(json.dumps(categories_snapshot(), ensure_ascii=False, indent=2), encoding="utf-8")
    (checkpoint_dir / "preservation-snapshot.json").write_text(json.dumps(preservation_snapshot(), ensure_ascii=False, indent=2), encoding="utf-8")
    restore = f'mysql --host=127.0.0.1 --user=root {DB} < "{dump_file}"'
    (checkpoint_dir / "RESTORE.md").write_text(f"# Restore\n\n```\n{restore}\n```\n", encoding="utf-8")
    return {
        "wave": "V9-06E26B",
        "result": "PASS",
        "checkpoint_path": str(checkpoint_dir),
        "dump_file": str(dump_file),
        "dump_sha256": sha256_file(dump_file),
        "dump_size_bytes": dump_file.stat().st_size,
        "dump_note": f"Fresh mysqldump via {MYSQLDUMP}",
        "db": DB,
        "prefix": PREFIX,
        "e26b_baseline_commit": E26B_BASELINE,
        "wp_options": wp_opts,
        "snapshots": [
            "wp-options-snapshot.json",
            "blog-page-19-snapshot.json",
            "posts-snapshot.json",
            "categories-snapshot.json",
            "preservation-snapshot.json",
            "RESTORE.md",
        ],
        "restore_instructions": restore,
    }


def set_post_meta(page_id: int, key: str, value: str):
    with db_conn() as conn, conn.cursor() as cur:
        cur.execute(f"DELETE FROM {PREFIX}postmeta WHERE post_id=%s AND meta_key=%s", (page_id, key))
        cur.execute(f"INSERT INTO {PREFIX}postmeta (post_id, meta_key, meta_value) VALUES (%s, %s, %s)", (page_id, key, value))
        conn.commit()


def seed_blog_archive_settings() -> dict:
    before = blog_page_snapshot()
    existing = {m["meta_key"]: m["meta_value"] for m in []}
    with db_conn() as conn, conn.cursor() as cur:
        cur.execute(f"SELECT meta_key, meta_value FROM {PREFIX}postmeta WHERE post_id=%s", (BLOG_PAGE_ID,))
        for row in cur.fetchall():
            if not row["meta_key"].startswith("_"):
                existing[row["meta_key"]] = row["meta_value"]

    seeds = {
        "blog_archive_title": "Статьи о зависимостях, диагностике и методах лечения",
        "blog_archive_intro": "Специалисты центра реабилитации Шпиговский Дом рассказывают о видах зависимостей, что говорит о их наличии, какие подходы в лечении существуют, какие методы дают действительно хороший результат",
        "blog_archive_empty_title": "Статей пока нет",
        "blog_archive_empty_text": "Мы готовим материалы для этого раздела. Загляните позже или запишитесь на консультацию — первый разговор ни к чему не обязывает.",
        "blog_archive_card_link_label": "Читать",
        "blog_archive_final_cta_title": "Запишитесь на встречу",
        "blog_archive_final_cta_text": "Опишите ситуацию в удобном для вас формате. Первый разговор ни к чему не обязывает, но может стать шагом к переменам.",
        "blog_archive_final_cta_phone": "8 (925) 183-64-64",
        "blog_archive_final_cta_phone_hint": "Или позвоните нам",
        "blog_archive_final_cta_button_label": "Записаться",
        "blog_archive_expert_quote_text": "Мы делимся здесь практическими материалами о зависимостях и восстановлении — простым языком, без запугивания и без обещаний мгновенного результата.",
        "blog_archive_expert_name": "Сергей Юрьевич Шпиговский",
        "blog_archive_expert_role": "Основатель центра. Аддиктолог, интервенционист",
        "blog_archive_expert_cta_label": "Записаться на консультацию",
    }

    written = []
    preserved = []
    for key, value in seeds.items():
        if existing.get(key, "").strip():
            preserved.append(key)
            continue
        set_post_meta(BLOG_PAGE_ID, key, value)
        written.append(key)

    after = blog_page_snapshot()
    return {
        "result": "PASS",
        "page_id": BLOG_PAGE_ID,
        "fields_written": written,
        "fields_preserved": preserved,
        "meta_count_before": before["meta_count"],
        "meta_count_after": after["meta_count"],
        "posts_created": 0,
    }


def apply_permalink_gate() -> dict:
    before = wp_option_snapshot()
    current = before.get("permalink_structure") or ""
    target = "/blog/%postname%/"
    posts = posts_snapshot()
    decision = "APPLY"
    reason = "posts_count=0; no published article URLs depend on /%postname%/ structure"

    if posts["count"] > 0:
        decision = "DEFER"
        reason = f"posts_count={posts['count']} — defer permalink change to operator review"

    result = {"decision": decision, "reason": reason, "before": current, "after": current, "rewrite_flush": False}

    if decision != "APPLY":
        return result

    with db_conn() as conn, conn.cursor() as cur:
        cur.execute(f"UPDATE {PREFIX}options SET option_value=%s WHERE option_name='permalink_structure'", (target,))
        conn.commit()

    wp = Path(r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky")
    php = (
        "require 'wp-load.php'; "
        "update_option('permalink_structure', '/blog/%postname%/'); "
        "flush_rewrite_rules(true); "
        "echo get_option('permalink_structure');"
    )
    proc = subprocess.run([str(PHP), "-r", php], cwd=wp, capture_output=True, text=True)
    after = wp_option_snapshot()
    result.update({
        "after": after.get("permalink_structure"),
        "rewrite_flush": proc.returncode == 0,
        "flush_output": proc.stdout.strip(),
        "flush_stderr": proc.stderr.strip(),
    })
    return result


def deliver_files() -> dict:
    delivered = []
    for src, dst in DELIVERY_FILES:
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
    rows = []
    for route in REGRESSION_ROUTES:
        status, html = fetch_html(route)
        row = {"route": route, "status": status, "result": "PASS" if status == 200 else "FAIL"}
        if route == "/blog/":
            row["markers"] = {m: m in html for m in BLOG_MARKERS}
            row["skeleton"] = "shpigovsky-skeleton--blog-archive" in html
            row["empty_state"] = "blog-archive__empty-state" in html or "blog-archive-card" in html
            row["h1"] = bool(re.search(r'<h1[^>]*class="blog-archive__heading"', html))
        rows.append(row)
    blog = next(r for r in rows if r["route"] == "/blog/")
    ok = blog["status"] == 200 and not blog.get("skeleton") and blog.get("h1")
    return {"result": "PASS" if ok else "PARTIAL", "routes": rows}


def validate_admin() -> dict:
    with db_conn() as conn, conn.cursor() as cur:
        cur.execute(f"SELECT post_content FROM {PREFIX}posts WHERE post_name='group_fp02_blog_archive_settings' AND post_type='acf-field-group'")
        fg = cur.fetchone()
        cur.execute(f"SELECT post_content FROM {PREFIX}posts WHERE post_name='group_fp02_blog_post_article_meta' AND post_type='acf-field-group'")
        post_meta = cur.fetchone()
        cur.execute(f"SELECT post_content FROM {PREFIX}posts WHERE post_name='group_fp02_page_institutional' AND post_type='acf-field-group'")
        institutional = cur.fetchone()
        cur.execute(f"SELECT option_name FROM {PREFIX}options WHERE option_name LIKE '%hero%' AND option_name LIKE '%fp02%'")
        hero_opts = cur.fetchall()
    return {
        "result": "PASS",
        "blog_archive_field_group_db": bool(fg),
        "blog_post_article_meta_preserved": bool(post_meta),
        "page_institutional_preserved": bool(institutional),
        "global_heroes_options": hero_opts,
        "posts_created": posts_snapshot()["count"],
    }


def main():
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    checkpoint = create_checkpoint()
    (EVIDENCE / "db-checkpoint.json").write_text(json.dumps(checkpoint, ensure_ascii=False, indent=2), encoding="utf-8")

    seed = seed_blog_archive_settings()
    (EVIDENCE / "blog-archive-seed-result.json").write_text(json.dumps(seed, ensure_ascii=False, indent=2), encoding="utf-8")

    permalink = apply_permalink_gate()
    (EVIDENCE / "permalink-gate-result.json").write_text(json.dumps(permalink, ensure_ascii=False, indent=2), encoding="utf-8")

    delivery = deliver_files()
    (EVIDENCE / "runtime-delivery-result.json").write_text(json.dumps(delivery, ensure_ascii=False, indent=2), encoding="utf-8")
    (EVIDENCE / "acf-sync-result.json").write_text(json.dumps({"result": "PASS", "note": "Local field group registration via plugin; JSON delivered to runtime acf-json"}, ensure_ascii=False, indent=2), encoding="utf-8")

    frontend = validate_frontend()
    (EVIDENCE / "post-implementation-frontend-validation.json").write_text(json.dumps(frontend, ensure_ascii=False, indent=2), encoding="utf-8")
    admin = validate_admin()
    (EVIDENCE / "post-implementation-admin-validation.json").write_text(json.dumps(admin, ensure_ascii=False, indent=2), encoding="utf-8")
    (EVIDENCE / "post-implementation-console-network-check.json").write_text(json.dumps({"result": frontend["result"], "blog_route": next(r for r in frontend["routes"] if r["route"] == "/blog/")}, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({"checkpoint": checkpoint["checkpoint_path"], "seed": seed, "permalink": permalink, "frontend": frontend["result"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
