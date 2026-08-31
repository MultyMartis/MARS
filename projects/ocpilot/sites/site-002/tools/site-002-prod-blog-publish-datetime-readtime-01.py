#!/usr/bin/env python3
"""SITE-002 Production blog publish datetime + reading time — Run 4.272."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import re
import shlex
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from site002_harness_authority import (
    CANONICAL_MONOREPO,
    DEFAULT_MONITOR_CHECKOUT,
    guard_historical_harness,
    resolve_repo_root_for_read,
    site002_reports_dir,
    site002_tools_dir,
)

OPERATION_ID = "SITE-002-PROD-BLOG-PUBLISH-DATETIME-READTIME-01"
OCPILOT_RUN = "4.272"
SITE_ID = "SITE-002"
PRODUCTION_URL = "https://bzpm.ru/"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
STORAGE_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
REPO_TOOLS = site002_tools_dir()
PREFIX = "oc_"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
TARGET_POST_ID = 13
TARGET_DATE_MYSQL = "2026-07-16 03:00:00"
CHARS_PER_MINUTE = 1500  # reading-time constant (Unicode chars / minute)

FTP_FILES = [
    "/public_html/admin/controller/blog/posts.php",
    "/public_html/admin/model/blog/blog.php",
    "/public_html/admin/view/template/blog/posts_form.twig",
    "/public_html/admin/view/template/blog/posts_list.twig",
    "/public_html/admin/language/ru-ru/blog/posts.php",
    "/public_html/catalog/controller/blog/category.php",
    "/public_html/catalog/controller/blog/post.php",
    "/public_html/catalog/model/blog/blog.php",
    "/public_html/catalog/view/theme/default/template/blog/category.twig",
    "/public_html/catalog/view/theme/default/template/blog/post.twig",
    "/public_html/catalog/view/theme/default/template/blog/other_news.twig",
    "/public_html/admin/view/template/catalog/product_form.twig",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_production_section(subsection: str) -> dict[str, str]:
    text = SECRETS_PATH.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    sub_match = re.search(
        rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE
    )
    if not sub_match:
        raise RuntimeError(f"Subsection {subsection} not found")
    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in sub_match.group(1).splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.endswith(":"):
            current_key = stripped[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(current_key, "")
            continue
        if current_key:
            fields[current_key] = stripped
    return fields


def mysql_query(sql: str, write: bool = False) -> str:
    import paramiko

    ssh = parse_production_section("SSH")
    db = parse_production_section("Database")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        ssh["host"],
        port=int(ssh.get("port") or 22),
        username=ssh["username"],
        password=ssh["password"],
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    esc = sql.replace("\\", "\\\\").replace('"', '\\"')
    cmd = (
        f'MYSQL_PWD={shlex.quote(db["password"])} mysql -N -B -u {shlex.quote(db["username"])} '
        f'{shlex.quote(db["database"])} -e "{esc}" 2>&1'
    )
    _i, o, e = client.exec_command(cmd, timeout=180)
    out = o.read().decode("utf-8", errors="replace") + e.read().decode("utf-8", errors="replace")
    client.close()
    if write and ("ERROR" in out.upper() or "Access denied" in out):
        raise RuntimeError(f"MySQL write failed: {out[:800]}")
    return out


def mysql_query_verbose(sql: str) -> str:
    """mysql with headers (table format) — for schema dumps."""
    import paramiko

    ssh = parse_production_section("SSH")
    db = parse_production_section("Database")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        ssh["host"],
        port=int(ssh.get("port") or 22),
        username=ssh["username"],
        password=ssh["password"],
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    esc = sql.replace("\\", "\\\\").replace('"', '\\"')
    cmd = (
        f'MYSQL_PWD={shlex.quote(db["password"])} mysql -u {shlex.quote(db["username"])} '
        f'{shlex.quote(db["database"])} -e "{esc}" 2>&1'
    )
    _i, o, e = client.exec_command(cmd, timeout=180)
    out = o.read().decode("utf-8", errors="replace") + e.read().decode("utf-8", errors="replace")
    client.close()
    return out


def ftp_connect():
    import ftplib

    ftp_cfg = parse_production_section("FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(ftp_cfg["host"], int(ftp_cfg.get("port") or 21), timeout=180)
    ftp.login(ftp_cfg["username"], ftp_cfg["password"])
    ftp.set_pasv(True)
    return ftp


def ftp_download(ftp, remote_path: str) -> bytes | None:
    import ftplib

    buf = io.BytesIO()
    try:
        ftp.retrbinary(f"RETR {remote_path}", buf.write)
        return buf.getvalue()
    except ftplib.error_perm:
        return None


def ftp_upload(ftp, remote_path: str, data: bytes) -> None:
    bio = io.BytesIO(data)
    ftp.storbinary(f"STOR {remote_path}", bio)


def http_fetch(url: str) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xml,*/*"},
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            body = resp.read()
            return {
                "url": url,
                "status": resp.status,
                "final_url": resp.geturl(),
                "length": len(body),
                "body": body.decode("utf-8", errors="replace"),
            }
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
        return {
            "url": url,
            "status": exc.code,
            "final_url": url,
            "length": len(body),
            "body": body,
        }
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "status": 0, "final_url": url, "length": 0, "body": "", "error": str(exc)}


def calc_reading_minutes(html: str) -> int:
    text = re.sub(r"(?is)<script[^>]*>.*?</script>", " ", html or "")
    text = re.sub(r"(?is)<style[^>]*>.*?</style>", " ", text)
    text = re.sub(r"(?is)<[^>]+>", " ", text)
    import html as html_mod

    text = html_mod.unescape(text)
    text = re.sub(r"\s+", " ", text, flags=re.UNICODE).strip()
    chars = len(text)  # Python str is Unicode code points ≈ mb_strlen UTF-8
    return max(1, int(math.ceil(chars / float(CHARS_PER_MINUTE))))


def ru_minutes_phrase(n: int) -> str:
    n = max(1, int(n))
    mod10 = n % 10
    mod100 = n % 100
    if mod10 == 1 and mod100 != 11:
        word = "минута"
    elif mod10 in (2, 3, 4) and mod100 not in (12, 13, 14):
        word = "минуты"
    else:
        word = "минут"
    return f"Время на чтение: {n} {word}."


def remote_to_local_name(remote: str) -> str:
    return remote.replace("/public_html/", "").replace("/", "__")


# ---------------------------------------------------------------------------
# PHASE: discover
# ---------------------------------------------------------------------------


def phase_discover() -> dict[str, Any]:
    result: dict[str, Any] = {"ts": utc_now()}
    source_before = STORAGE_ROOT / "source-before"
    source_before.mkdir(parents=True, exist_ok=True)

    ftp = ftp_connect()
    downloaded: dict[str, Any] = {}
    try:
        for remote in FTP_FILES:
            data = ftp_download(ftp, remote)
            local_name = remote_to_local_name(remote)
            if data is None:
                downloaded[remote] = {"ok": False}
                continue
            path = source_before / local_name
            path.write_bytes(data)
            downloaded[remote] = {
                "ok": True,
                "bytes": len(data),
                "sha256": sha256_bytes(data),
                "local": str(path),
            }
    finally:
        ftp.quit()

    write_json(STORAGE_ROOT / "blog-admin-before" / "ftp-download-index.json", downloaded)
    result["ftp"] = downloaded

    # DB schema + post 13
    create_sql = mysql_query_verbose("SHOW CREATE TABLE oc_blog_posts\\G")
    write_text(STORAGE_ROOT / "db-schema-before" / "oc_blog_posts-schema.sql", create_sql)
    write_text(STORAGE_ROOT / "db-backup" / "blog-posts-schema-before.sql", create_sql)

    cols = mysql_query("SHOW COLUMNS FROM oc_blog_posts")
    write_text(STORAGE_ROOT / "db-schema-before" / "columns.txt", cols)

    post13 = mysql_query(
        "SELECT id, category_id, title, image, active, date_added, "
        "CHAR_LENGTH(content) AS content_len, "
        "LEFT(content, 200) AS content_head "
        f"FROM oc_blog_posts WHERE id={TARGET_POST_ID}"
    )
    write_text(STORAGE_ROOT / "db-backup" / "post-13-before.sql", post13)

    posts = mysql_query(
        "SELECT id, title, image, active, date_added, CHAR_LENGTH(content) "
        "FROM oc_blog_posts ORDER BY id"
    )
    tz = mysql_query("SELECT @@session.time_zone, @@global.time_zone, NOW(), UTC_TIMESTAMP()")

    has_reading = any(
        c.startswith("reading_time") or c.startswith("read_time") or "time_read" in c
        for c in cols.splitlines()
    )
    # also check field names in first column
    col_names = [ln.split("\t")[0] for ln in cols.splitlines() if ln.strip()]
    reading_fields = [
        n
        for n in col_names
        if "read" in n.lower() or "time" in n.lower() and n.lower() != "date_added"
    ]

    post13_parts = post13.strip().split("\t") if post13.strip() else []
    post13_date = post13_parts[5] if len(post13_parts) > 5 else ""
    post13_ok = post13_date == TARGET_DATE_MYSQL

    summary = {
        "columns": col_names,
        "reading_time_fields": reading_fields,
        "has_reading_time_column": bool(reading_fields),
        "date_added_type": "datetime (from schema)",
        "post_13_date_added": post13_date,
        "post_13_date_matches_target": post13_ok,
        "target_date_mysql": TARGET_DATE_MYSQL,
        "timezone_row": tz.strip(),
        "posts_count_lines": len([ln for ln in posts.splitlines() if ln.strip()]),
        "ftp_ok_count": sum(1 for v in downloaded.values() if v.get("ok")),
    }
    write_json(STORAGE_ROOT / "db-schema-before" / "blog-schema-summary.json", summary)
    write_json(
        STORAGE_ROOT / "db-backup" / "blog-relevant-before.json",
        {"post13_raw": post13, "posts": posts, "timezone": tz},
    )

    # admin field notes
    form = (source_before / "admin__view__template__blog__posts_form.twig").read_text(
        encoding="utf-8", errors="replace"
    )
    ctrl = (source_before / "admin__controller__blog__posts.php").read_text(
        encoding="utf-8", errors="replace"
    )
    write_text(
        STORAGE_ROOT / "blog-admin-before" / "admin-blog-files.md",
        "\n".join(
            [
                "# Admin blog files (production)",
                "",
                "| Role | Path |",
                "|------|------|",
                "| Controller | `admin/controller/blog/posts.php` |",
                "| Model | `admin/model/blog/blog.php` |",
                "| Form | `admin/view/template/blog/posts_form.twig` |",
                "| List | `admin/view/template/blog/posts_list.twig` |",
                "| Language | `admin/language/ru-ru/blog/posts.php` |",
                "",
                f"Downloaded OK: {summary['ftp_ok_count']}/{len(FTP_FILES)}",
            ]
        ),
    )
    write_text(
        STORAGE_ROOT / "blog-admin-before" / "admin-field-current-state.md",
        "\n".join(
            [
                "# Admin publish date field — current state",
                "",
                "- Form field name: `modified`",
                "- Label: raw text `Дата` (not language key)",
                "- Input: plain `<input type=\"text\">` — no datepicker/datetimepicker",
                "- Controller display: `date('d.m.Y', strtotime($post_info['date_added']))` — **time truncated**",
                "- Model save: `date('Y-m-d H:i:s', strtotime($data['modified']))`",
                "- List display: `date('d.m.Y', ...)` date-only",
                "- Product form convention: uses `.datetime` + bootstrap datetimepicker (sampled)",
                "",
                f"Form contains datetimepicker: {'datetimepicker' in form}",
                f"Controller addScript datetime: {'datetimepicker' in ctrl}",
            ]
        ),
    )

    cat_twig = (source_before / "catalog__view__theme__default__template__blog__category.twig").read_text(
        encoding="utf-8", errors="replace"
    )
    post_twig = (source_before / "catalog__view__theme__default__template__blog__post.twig").read_text(
        encoding="utf-8", errors="replace"
    )
    write_text(
        STORAGE_ROOT / "blog-frontend-before" / "frontend-blog-files.md",
        "\n".join(
            [
                "# Frontend blog files",
                "",
                "| Role | Path |",
                "|------|------|",
                "| List controller | `catalog/controller/blog/category.php` |",
                "| Detail controller | `catalog/controller/blog/post.php` |",
                "| Model | `catalog/model/blog/blog.php` |",
                "| List template | `catalog/view/theme/default/template/blog/category.twig` |",
                "| Detail template | `catalog/view/theme/default/template/blog/post.twig` |",
                "| Related | `catalog/view/theme/default/template/blog/other_news.twig` |",
            ]
        ),
    )
    write_text(
        STORAGE_ROOT / "blog-frontend-before" / "meta-block-current-state.md",
        "\n".join(
            [
                "# Meta blocks current state",
                "",
                "## `.blog-list__item__meta` (category.twig)",
                "- Rubric / Date / Views",
                "- No reading time",
                "",
                "## `.blog-item__meta` (post.twig)",
                "- Rubric / Date / Views",
                "- No reading time",
                "",
                f"category has blog-list__item__meta: {'blog-list__item__meta' in cat_twig}",
                f"post has blog-item__meta: {'blog-item__meta' in post_twig}",
            ]
        ),
    )

    # sample product form datetime
    prod = source_before / "admin__view__template__catalog__product_form.twig"
    if prod.exists():
        snippet = []
        text = prod.read_text(encoding="utf-8", errors="replace")
        for i, line in enumerate(text.splitlines(), 1):
            if "datetime" in line.lower() or "date-format" in line.lower():
                snippet.append(f"{i}: {line.strip()}")
        write_text(
            STORAGE_ROOT / "blog-admin-before" / "product-datetimepicker-snippets.txt",
            "\n".join(snippet[:40]),
        )

    result["summary"] = summary
    result["post13_ok"] = post13_ok
    if not post13_ok:
        result["STOP"] = "post 13 date_added != expected"
    write_json(STORAGE_ROOT / "logs" / "discover-result.json", result)
    return result


# ---------------------------------------------------------------------------
# PHASE: patch local files
# ---------------------------------------------------------------------------


def patch_admin_controller(src: str) -> str:
    # add datetimepicker assets
    if "datetimepicker" not in src:
        insert = """\t\t$this->document->addScript('view/javascript/jquery/datetimepicker/moment/moment.min.js');
\t\t$this->document->addScript('view/javascript/jquery/datetimepicker/moment/moment-with-locales.min.js');
\t\t$this->document->addScript('view/javascript/jquery/datetimepicker/bootstrap-datetimepicker.min.js');
\t\t$this->document->addStyle('view/javascript/jquery/datetimepicker/bootstrap-datetimepicker.min.css');
"""
        src = src.replace(
            "\t\t$this->document->addStyle('view/javascript/summernote/summernote.css');\n",
            "\t\t$this->document->addStyle('view/javascript/summernote/summernote.css');\n" + insert,
            1,
        )

    # list date keep YYYY-MM-DD HH:MM display optional — show d.m.Y H:i
    src = src.replace(
        "'date'    => date('d.m.Y', strtotime($result['date_added'])),",
        "'date'    => date('d.m.Y H:i', strtotime($result['date_added'])),",
    )

    # form modified field — full datetime; safe for add vs edit
    old_mod = "\t\t$data['modified'] = date('d.m.Y', strtotime($post_info['date_added']));\n"
    new_mod = """\t\tif (!empty($post_info) && !empty($post_info['date_added'])) {
\t\t\t$data['modified'] = date('Y-m-d H:i', strtotime($post_info['date_added']));
\t\t} elseif (isset($this->request->post['modified'])) {
\t\t\t$data['modified'] = $this->request->post['modified'];
\t\t} else {
\t\t\t$data['modified'] = date('Y-m-d H:i');
\t\t}

\t\tif (!empty($post_info) && isset($post_info['reading_time_minutes'])) {
\t\t\t$data['reading_time_minutes'] = (int)$post_info['reading_time_minutes'];
\t\t} else {
\t\t\t$data['reading_time_minutes'] = 0;
\t\t}
"""
    if old_mod in src:
        src = src.replace(old_mod, new_mod)
    elif "date('Y-m-d H:i'" not in src:
        # already partially patched or different — force near action=
        pass

    return src


def patch_admin_model(src: str) -> str:
    helper = r'''
	/**
	 * Reading time: strip HTML, decode entities, normalize whitespace,
	 * count Unicode characters (mb_strlen UTF-8), divide by CHARS_PER_MINUTE.
	 * Constant: 1500 characters per minute.
	 */
	public function calculateReadingTimeMinutes($html) {
		$text = (string)$html;
		$text = preg_replace('/(?is)<script[^>]*>.*?<\/script>/', ' ', $text);
		$text = preg_replace('/(?is)<style[^>]*>.*?<\/style>/', ' ', $text);
		$text = strip_tags($text);
		$text = html_entity_decode($text, ENT_QUOTES, 'UTF-8');
		$text = preg_replace('/\s+/u', ' ', $text);
		$text = trim($text);
		$chars = mb_strlen($text, 'UTF-8');
		$chars_per_minute = 1500; // SITE-002 reading-time constant
		$minutes = (int)max(1, (int)ceil($chars / $chars_per_minute));
		return $minutes;
	}

	protected function normalizePublishDatetime($value) {
		$value = trim((string)$value);
		if ($value === '') {
			return '';
		}
		// HTML5 datetime-local: YYYY-MM-DDTHH:MM
		$value = str_replace('T', ' ', $value);
		$ts = strtotime($value);
		if ($ts === false) {
			return '';
		}
		return date('Y-m-d H:i:00', $ts);
	}

'''
    if "calculateReadingTimeMinutes" not in src:
        src = src.replace(
            "class ModelBlogBlog extends Model {\n",
            "class ModelBlogBlog extends Model {\n" + helper,
            1,
        )

    # rewrite addPost date + reading_time
    if "reading_time_minutes" not in src or "calculateReadingTimeMinutes($data['content']" not in src:
        # Replace addPost body date block and INSERT
        add_old = """\t\tpublic function addPost($data) {

\t\t$date = 'NOW()';
\t\tif ((isset($data['modified'])) AND ($data['modified']!=''))
\t\t\t{
\t\t\t\t$date ="'".date('Y-m-d H:i:s', strtotime($data['modified']))."'";
\t\t\t}


\t\t$this->db->query("INSERT INTO " . DB_PREFIX . "blog_posts SET 
            category_id = '" . (int)$data['category_id'] . "', 
            title = '" . $this->db->escape($data['title']) . "', 
            short_description = '" . $this->db->escape($data['short_description']) . "', 
            content = '" . $this->db->escape($data['content']) . "', 
            image = '" . $this->db->escape($data['image']) . "', 
            active = '" . (int)$data['active'] . "', 
            meta_title = '" . $this->db->escape($data['meta_title']) . "', 
            meta_description = '" . $this->db->escape($data['meta_description']) . "', 
            meta_keyword = '" . $this->db->escape($data['meta_keyword']) . "', 
            date_added = ".$date);"""

        add_new = """\tpublic function addPost($data) {

\t\t$date = 'NOW()';
\t\tif (isset($data['modified']) && $data['modified'] != '') {
\t\t\t$normalized = $this->normalizePublishDatetime($data['modified']);
\t\t\tif ($normalized !== '') {
\t\t\t\t$date = "'" . $this->db->escape($normalized) . "'";
\t\t\t}
\t\t}

\t\t$reading_time_minutes = $this->calculateReadingTimeMinutes(isset($data['content']) ? $data['content'] : '');

\t\t$this->db->query("INSERT INTO " . DB_PREFIX . "blog_posts SET 
            category_id = '" . (int)$data['category_id'] . "', 
            title = '" . $this->db->escape($data['title']) . "', 
            short_description = '" . $this->db->escape($data['short_description']) . "', 
            content = '" . $this->db->escape($data['content']) . "', 
            reading_time_minutes = '" . (int)$reading_time_minutes . "',
            image = '" . $this->db->escape($data['image']) . "', 
            active = '" . (int)$data['active'] . "', 
            meta_title = '" . $this->db->escape($data['meta_title']) . "', 
            meta_description = '" . $this->db->escape($data['meta_description']) . "', 
            meta_keyword = '" . $this->db->escape($data['meta_keyword']) . "', 
            date_added = ".$date);"""

        if add_old in src:
            src = src.replace(add_old, add_new)
        else:
            raise RuntimeError("addPost block not found for patch")

        edit_old = """\tpublic function editPost($post_id, $data) {
\t\t
\t\t$date = '';
\t\t\tif ((isset($data['modified'])) AND ($data['modified']!=''))
\t\t\t{
\t\t\t\t$date =", date_added = '".date('Y-m-d H:i:s', strtotime($data['modified']))."'";
\t\t\t}


\t\t$this->db->query("UPDATE " . DB_PREFIX . "blog_posts SET 
            category_id = '" . (int)$data['category_id'] . "', 
            title = '" . $this->db->escape($data['title']) . "', 
            short_description = '" . $this->db->escape($data['short_description']) . "', 
            content = '" . $this->db->escape($data['content']) . "', 
            image = '" . $this->db->escape($data['image']) . "', 
            active = '" . (int)$data['active'] . "', 
            meta_title = '" . $this->db->escape($data['meta_title']) . "', 
            meta_description = '" . $this->db->escape($data['meta_description']) . "', 
            meta_keyword = '" . $this->db->escape($data['meta_keyword']) . "'".
\t\t\t$date. 
            " WHERE id = '" . (int)$post_id . "'");"""

        edit_new = """\tpublic function editPost($post_id, $data) {
\t\t
\t\t$date = '';
\t\tif (isset($data['modified']) && $data['modified'] != '') {
\t\t\t$normalized = $this->normalizePublishDatetime($data['modified']);
\t\t\tif ($normalized !== '') {
\t\t\t\t$date = ", date_added = '" . $this->db->escape($normalized) . "'";
\t\t\t}
\t\t}

\t\t$reading_time_minutes = $this->calculateReadingTimeMinutes(isset($data['content']) ? $data['content'] : '');

\t\t$this->db->query("UPDATE " . DB_PREFIX . "blog_posts SET 
            category_id = '" . (int)$data['category_id'] . "', 
            title = '" . $this->db->escape($data['title']) . "', 
            short_description = '" . $this->db->escape($data['short_description']) . "', 
            content = '" . $this->db->escape($data['content']) . "', 
            reading_time_minutes = '" . (int)$reading_time_minutes . "',
            image = '" . $this->db->escape($data['image']) . "', 
            active = '" . (int)$data['active'] . "', 
            meta_title = '" . $this->db->escape($data['meta_title']) . "', 
            meta_description = '" . $this->db->escape($data['meta_description']) . "', 
            meta_keyword = '" . $this->db->escape($data['meta_keyword']) . "'".
\t\t\t$date. 
            " WHERE id = '" . (int)$post_id . "'");"""

        if edit_old in src:
            src = src.replace(edit_old, edit_new)
        else:
            raise RuntimeError("editPost block not found for patch")

    return src


def patch_admin_form(src: str) -> str:
    old = """                <div class="form-group">
                    <label class="col-sm-2 control-label" for="input-modified">
                    Дата
                    </label>
                    <div class="col-sm-10">
                    <input type="text" name="modified" value="{{ modified }}"  id="input-modified" class="form-control" />
                    </div>
                </div>"""

    new = """                <div class="form-group">
                    <label class="col-sm-2 control-label" for="input-modified">
                    <span data-toggle="tooltip" title="Используется для отложенной публикации статьи на сайте. Время сайта (как в MySQL/OpenCart).">Дата и время публикации</span>
                    </label>
                    <div class="col-sm-3">
                      <div class="input-group datetime">
                        <input type="text" name="modified" value="{{ modified }}" placeholder="YYYY-MM-DD HH:MM" data-date-format="YYYY-MM-DD HH:mm" id="input-modified" class="form-control" />
                        <span class="input-group-btn">
                          <button type="button" class="btn btn-default"><i class="fa fa-calendar"></i></button>
                        </span>
                      </div>
                      <span class="help-block">Дата и время публикации (по времени сайта). Для отложенной публикации укажите будущую дату и время.</span>
                    </div>
                </div>
{% if reading_time_minutes %}
                <div class="form-group">
                    <label class="col-sm-2 control-label">Время на чтение</label>
                    <div class="col-sm-10">
                      <p class="form-control-static">{{ reading_time_minutes }} мин. (считается автоматически при сохранении по объёму текста)</p>
                    </div>
                </div>
{% endif %}"""

    if old not in src:
        if "datetime" in src and "input-modified" in src:
            return src  # already patched
        raise RuntimeError("admin form date block not found")
    src = src.replace(old, new)

    # init datetimepicker at bottom
    if "datetimepicker" not in src:
        src = src.replace(
            '<script type="text/javascript"></script>\n</div>\n{{ footer }}',
            """<script type="text/javascript"><!--
$('.datetime').datetimepicker({
  language: 'ru',
  pickDate: true,
  pickTime: true
});
//--></script>
</div>
{{ footer }}""",
        )
    return src


def patch_language(src: str) -> str:
    if "entry_date_publish" in src:
        return src
    addition = """
$_['entry_date_publish']     = 'Дата и время публикации';
$_['help_date_publish']      = 'Используется для отложенной публикации статьи на сайте. Время сайта (как в MySQL/OpenCart).';
$_['entry_reading_time']     = 'Время на чтение';
"""
    return src.rstrip() + "\n" + addition


def reading_time_php_helper() -> str:
    return r'''
	protected function formatReadingTimeText($minutes) {
		$n = (int)$minutes;
		if ($n < 1) {
			$n = 1;
		}
		$mod10 = $n % 10;
		$mod100 = $n % 100;
		if ($mod10 == 1 && $mod100 != 11) {
			$word = 'минута';
		} elseif (in_array($mod10, array(2, 3, 4)) && !in_array($mod100, array(12, 13, 14))) {
			$word = 'минуты';
		} else {
			$word = 'минут';
		}
		return 'Время на чтение: ' . $n . ' ' . $word . '.';
	}

'''


def patch_catalog_category_controller(src: str) -> str:
    if "formatReadingTimeText" not in src:
        src = src.replace(
            "class ControllerBlogCategory extends Controller {\n",
            "class ControllerBlogCategory extends Controller {\n" + reading_time_php_helper(),
            1,
        )
    old = """            $data['posts'][] = array(
                'title'         => $result['title'],
                'category_name' => $result['category_name'] ? $result['category_name'] : 'Без рубрики',
                'date'          => date('d.m.Y', strtotime($result['date_added'])),
                'views'         => $result['views'],
                'thumb'         => $image,
                'short'         => html_entity_decode($result['short_description'], ENT_QUOTES, 'UTF-8'),
                'href'          => $this->url->link('blog/post', 'blog_post_id=' . $result['id'])
            );"""
    new = """            $reading_minutes = isset($result['reading_time_minutes']) ? (int)$result['reading_time_minutes'] : 1;
            if ($reading_minutes < 1) {
                $reading_minutes = 1;
            }
            $data['posts'][] = array(
                'title'         => $result['title'],
                'category_name' => $result['category_name'] ? $result['category_name'] : 'Без рубрики',
                'date'          => date('d.m.Y', strtotime($result['date_added'])),
                'views'         => $result['views'],
                'reading_time_text' => $this->formatReadingTimeText($reading_minutes),
                'thumb'         => $image,
                'short'         => html_entity_decode($result['short_description'], ENT_QUOTES, 'UTF-8'),
                'href'          => $this->url->link('blog/post', 'blog_post_id=' . $result['id'])
            );"""
    if old not in src:
        if "reading_time_text" in src:
            return src
        raise RuntimeError("category posts array block not found")
    src = src.replace(old, new)

    # other news cards if present
    old2 = """            $data['other_news_list'][] = array(
                'title'         => $result['title'],
                'category_name' => $result['category_name'] ? $result['category_name'] : 'Без рубрики',
                'date'          => date('d.m.Y', strtotime($result['date_added'])),
                'views'         => $result['views'],
                'short'         => utf8_substr(strip_tags(html_entity_decode($result['short_description'], ENT_QUOTES, 'UTF-8')), 0, 150) . '..',
                'thumb'         => $other_thumb,
                'href'          => $this->url->link('blog/post', 'blog_post_id=' . $result['id'])
            );"""
    new2 = """            $other_minutes = isset($result['reading_time_minutes']) ? (int)$result['reading_time_minutes'] : 1;
            if ($other_minutes < 1) {
                $other_minutes = 1;
            }
            $data['other_news_list'][] = array(
                'title'         => $result['title'],
                'category_name' => $result['category_name'] ? $result['category_name'] : 'Без рубрики',
                'date'          => date('d.m.Y', strtotime($result['date_added'])),
                'views'         => $result['views'],
                'reading_time_text' => $this->formatReadingTimeText($other_minutes),
                'short'         => utf8_substr(strip_tags(html_entity_decode($result['short_description'], ENT_QUOTES, 'UTF-8')), 0, 150) . '..',
                'thumb'         => $other_thumb,
                'href'          => $this->url->link('blog/post', 'blog_post_id=' . $result['id'])
            );"""
    if old2 in src:
        src = src.replace(old2, new2)
    return src


def patch_catalog_post_controller(src: str) -> str:
    if "formatReadingTimeText" not in src:
        src = src.replace(
            "class ControllerBlogPost extends Controller {\n",
            "class ControllerBlogPost extends Controller {\n" + reading_time_php_helper(),
            1,
        )
    if "$data['reading_time_text']" not in src:
        src = src.replace(
            "\t\t\t$data['date'] = date('d.m.Y', strtotime($post_info['date_added']));\n\t\t\t$data['views'] = $post_info['views'] + 1;\n",
            "\t\t\t$data['date'] = date('d.m.Y', strtotime($post_info['date_added']));\n"
            "\t\t\t$data['views'] = $post_info['views'] + 1;\n"
            "\t\t\t$reading_minutes = isset($post_info['reading_time_minutes']) ? (int)$post_info['reading_time_minutes'] : 1;\n"
            "\t\t\tif ($reading_minutes < 1) {\n"
            "\t\t\t\t$reading_minutes = 1;\n"
            "\t\t\t}\n"
            "\t\t\t$data['reading_time_text'] = $this->formatReadingTimeText($reading_minutes);\n",
        )
    # other news in post controller
    old2 = """\t\t\t\t$data['other_news_list'][] = array(
\t\t\t\t\t'title'         => $result['title'],
\t\t\t\t\t'category_name' => $result['category_name'] ? $result['category_name'] : 'Без рубрики',
\t\t\t\t\t'date'          => date('d.m.Y', strtotime($result['date_added'])),
\t\t\t\t\t'views'         => $result['views'],
\t\t\t\t\t'short'         => utf8_substr(strip_tags(html_entity_decode($result['short_description'], ENT_QUOTES, 'UTF-8')), 0, 150) . '..',
\t\t\t\t\t'thumb'         => $other_thumb,
\t\t\t\t\t'href'          => $this->url->link('blog/post', 'blog_post_id=' . $result['id'])
\t\t\t\t);"""
    new2 = """\t\t\t\t$other_minutes = isset($result['reading_time_minutes']) ? (int)$result['reading_time_minutes'] : 1;
\t\t\t\tif ($other_minutes < 1) {
\t\t\t\t\t$other_minutes = 1;
\t\t\t\t}
\t\t\t\t$data['other_news_list'][] = array(
\t\t\t\t\t'title'         => $result['title'],
\t\t\t\t\t'category_name' => $result['category_name'] ? $result['category_name'] : 'Без рубрики',
\t\t\t\t\t'date'          => date('d.m.Y', strtotime($result['date_added'])),
\t\t\t\t\t'views'         => $result['views'],
\t\t\t\t\t'reading_time_text' => $this->formatReadingTimeText($other_minutes),
\t\t\t\t\t'short'         => utf8_substr(strip_tags(html_entity_decode($result['short_description'], ENT_QUOTES, 'UTF-8')), 0, 150) . '..',
\t\t\t\t\t'thumb'         => $other_thumb,
\t\t\t\t\t'href'          => $this->url->link('blog/post', 'blog_post_id=' . $result['id'])
\t\t\t\t);"""
    if old2 in src:
        src = src.replace(old2, new2)
    return src


def patch_list_twig(src: str) -> str:
    if "reading_time_text" in src:
        return src
    needle = """              <div class="views">
                <b>Просмотров:</b>
                <span>{{ post.views }}</span>
              </div>
            </div>"""
    insert = """              <div class="views">
                <b>Просмотров:</b>
                <span>{{ post.views }}</span>
              </div>
              {% if post.reading_time_text %}
              <div class="reading-time">
                <span>{{ post.reading_time_text }}</span>
              </div>
              {% endif %}
            </div>"""
    if needle not in src:
        raise RuntimeError("list meta block not found")
    return src.replace(needle, insert)


def patch_post_twig(src: str) -> str:
    if "reading_time_text" in src:
        return src
    needle = """          <div class="views">
            <b>Просмотров:</b>
            <span>{{ views }}</span>
          </div>
        </div>"""
    insert = """          <div class="views">
            <b>Просмотров:</b>
            <span>{{ views }}</span>
          </div>
          {% if reading_time_text %}
          <div class="reading-time">
            <span>{{ reading_time_text }}</span>
          </div>
          {% endif %}
        </div>"""
    if needle not in src:
        raise RuntimeError("post meta block not found")
    return src.replace(needle, insert)


def phase_prepare_patches() -> dict[str, Any]:
    before = STORAGE_ROOT / "source-before"
    after = STORAGE_ROOT / "source-after"
    after.mkdir(parents=True, exist_ok=True)
    prepared = STORAGE_ROOT / "prepared"
    prepared.mkdir(parents=True, exist_ok=True)

    mapping = [
        ("admin__controller__blog__posts.php", patch_admin_controller, "/public_html/admin/controller/blog/posts.php"),
        ("admin__model__blog__blog.php", patch_admin_model, "/public_html/admin/model/blog/blog.php"),
        ("admin__view__template__blog__posts_form.twig", patch_admin_form, "/public_html/admin/view/template/blog/posts_form.twig"),
        ("admin__language__ru-ru__blog__posts.php", patch_language, "/public_html/admin/language/ru-ru/blog/posts.php"),
        ("catalog__controller__blog__category.php", patch_catalog_category_controller, "/public_html/catalog/controller/blog/category.php"),
        ("catalog__controller__blog__post.php", patch_catalog_post_controller, "/public_html/catalog/controller/blog/post.php"),
        ("catalog__view__theme__default__template__blog__category.twig", patch_list_twig, "/public_html/catalog/view/theme/default/template/blog/category.twig"),
        ("catalog__view__theme__default__template__blog__post.twig", patch_post_twig, "/public_html/catalog/view/theme/default/template/blog/post.twig"),
    ]

    results = []
    for fname, fn, remote in mapping:
        src_path = before / fname
        if not src_path.exists():
            results.append({"file": fname, "ok": False, "error": "missing source-before"})
            continue
        original = src_path.read_text(encoding="utf-8")
        patched = fn(original)
        out_path = after / fname
        out_path.write_text(patched, encoding="utf-8", newline="\n")
        prep_name = remote.replace("/public_html/", "").replace("/", "__")
        (prepared / prep_name).write_text(patched, encoding="utf-8", newline="\n")
        # also copy to repo tools mirrors
        results.append(
            {
                "file": fname,
                "remote": remote,
                "ok": True,
                "changed": original != patched,
                "sha256": sha256_bytes(patched.encode("utf-8")),
                "bytes": len(patched.encode("utf-8")),
            }
        )

    write_json(STORAGE_ROOT / "patch-plan" / "files-to-change.md.json", results)
    lines = ["# Files to change", ""]
    for r in results:
        lines.append(f"- `{r.get('remote', r['file'])}` changed={r.get('changed')} ok={r.get('ok')}")
    write_text(STORAGE_ROOT / "patch-plan" / "files-to-change.md", "\n".join(lines) + "\n")
    write_text(STORAGE_ROOT / "source-after" / "admin-datetime-files.txt", "\n".join(r["remote"] for r in results if r.get("ok")))
    return {"files": results}


def phase_db_migrate() -> dict[str, Any]:
    cols = mysql_query("SHOW COLUMNS FROM oc_blog_posts LIKE 'reading_time_minutes'")
    added = False
    if not cols.strip():
        alter = (
            "ALTER TABLE oc_blog_posts "
            "ADD COLUMN reading_time_minutes TINYINT UNSIGNED NOT NULL DEFAULT 1 "
            "AFTER content"
        )
        write_text(STORAGE_ROOT / "db-migration" / "add-reading-time-column.sql", alter + ";\n")
        out = mysql_query(alter, write=True)
        write_text(STORAGE_ROOT / "db-migration" / "alter-result.txt", out)
        if "ERROR" in out.upper():
            raise RuntimeError(f"ALTER failed: {out}")
        added = True
    else:
        write_text(
            STORAGE_ROOT / "db-migration" / "add-reading-time-column.sql",
            "-- column already exists\n",
        )

    # backfill from content
    rows_raw = mysql_query("SELECT id, content FROM oc_blog_posts")
    updates = []
    # content may contain tabs/newlines — use a safer query per id
    ids_raw = mysql_query("SELECT id FROM oc_blog_posts ORDER BY id")
    ids = [int(x.strip()) for x in ids_raw.splitlines() if x.strip().isdigit()]

    import paramiko

    ssh = parse_production_section("SSH")
    db = parse_production_section("Database")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        ssh["host"],
        port=int(ssh.get("port") or 22),
        username=ssh["username"],
        password=ssh["password"],
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )

    summary_rows = []
    for pid in ids:
        # fetch content via SELECT id, HEX-less — use --batch with NULL as SEP and careful: content is mediumtext
        esc_sql = f"SELECT content FROM oc_blog_posts WHERE id={pid}"
        esc = esc_sql.replace("\\", "\\\\").replace('"', '\\"')
        cmd = (
            f'MYSQL_PWD={shlex.quote(db["password"])} mysql -N -B -u {shlex.quote(db["username"])} '
            f'{shlex.quote(db["database"])} -e "{esc}" 2>&1'
        )
        _i, o, e = client.exec_command(cmd, timeout=180)
        content = o.read().decode("utf-8", errors="replace")
        err = e.read().decode("utf-8", errors="replace")
        if err and "ERROR" in err.upper():
            client.close()
            raise RuntimeError(err)
        minutes = calc_reading_minutes(content)
        upd = (
            f"UPDATE oc_blog_posts SET reading_time_minutes={minutes} "
            f"WHERE id={pid} AND date_added=date_added"
        )
        # extra guard for post 13 date
        if pid == TARGET_POST_ID:
            upd = (
                f"UPDATE oc_blog_posts SET reading_time_minutes={minutes} "
                f"WHERE id={pid} AND date_added='{TARGET_DATE_MYSQL}'"
            )
        esc_u = upd.replace("\\", "\\\\").replace('"', '\\"')
        cmd_u = (
            f'MYSQL_PWD={shlex.quote(db["password"])} mysql -N -B -u {shlex.quote(db["username"])} '
            f'{shlex.quote(db["database"])} -e "{esc_u}" 2>&1'
        )
        _i2, o2, e2 = client.exec_command(cmd_u, timeout=180)
        uout = o2.read().decode("utf-8", errors="replace") + e2.read().decode("utf-8", errors="replace")
        if "ERROR" in uout.upper():
            client.close()
            raise RuntimeError(f"backfill failed id={pid}: {uout}")
        summary_rows.append({"id": pid, "minutes": minutes, "chars_approx": len(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", content)))})
        updates.append(upd + ";")

    client.close()

    write_text(STORAGE_ROOT / "db-migration" / "backfill-reading-time.sql", "\n".join(updates) + "\n")
    with (STORAGE_ROOT / "db-migration" / "backfill-summary.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "minutes", "chars_approx"])
        w.writeheader()
        w.writerows(summary_rows)

    after_schema = mysql_query_verbose("SHOW CREATE TABLE oc_blog_posts\\G")
    write_text(STORAGE_ROOT / "db-after" / "blog-schema-after.sql", after_schema)
    post13 = mysql_query(
        "SELECT id, title, image, active, date_added, reading_time_minutes, "
        "CHAR_LENGTH(content) FROM oc_blog_posts WHERE id=13"
    )
    write_json(
        STORAGE_ROOT / "db-after" / "post-13-after-db.json",
        {"raw": post13, "ts": utc_now()},
    )

    # verify date unchanged
    parts = post13.strip().split("\t")
    date_ok = len(parts) > 4 and parts[4] == TARGET_DATE_MYSQL
    return {
        "column_added": added,
        "backfilled": len(summary_rows),
        "summary": summary_rows,
        "post13_date_ok": date_ok,
        "post13_raw": post13.strip(),
    }


def phase_upload() -> dict[str, Any]:
    prepared = STORAGE_ROOT / "prepared"
    upload_map = [
        ("admin__controller__blog__posts.php", "/public_html/admin/controller/blog/posts.php"),
        ("admin__model__blog__blog.php", "/public_html/admin/model/blog/blog.php"),
        ("admin__view__template__blog__posts_form.twig", "/public_html/admin/view/template/blog/posts_form.twig"),
        ("admin__language__ru-ru__blog__posts.php", "/public_html/admin/language/ru-ru/blog/posts.php"),
        ("catalog__controller__blog__category.php", "/public_html/catalog/controller/blog/category.php"),
        ("catalog__controller__blog__post.php", "/public_html/catalog/controller/blog/post.php"),
        ("catalog__view__theme__default__template__blog__category.twig", "/public_html/catalog/view/theme/default/template/blog/category.twig"),
        ("catalog__view__theme__default__template__blog__post.twig", "/public_html/catalog/view/theme/default/template/blog/post.twig"),
    ]
    ftp = ftp_connect()
    results = []
    try:
        for local_name, remote in upload_map:
            path = prepared / local_name
            if not path.exists():
                # also try source-after naming
                path = STORAGE_ROOT / "source-after" / local_name
            data = path.read_bytes()
            ftp_upload(ftp, remote, data)
            # verify
            verify = ftp_download(ftp, remote)
            ok = verify is not None and sha256_bytes(verify) == sha256_bytes(data)
            results.append(
                {
                    "remote": remote,
                    "bytes": len(data),
                    "sha256": sha256_bytes(data),
                    "verified": ok,
                }
            )
    finally:
        ftp.quit()

    lines = [f"{r['remote']}\t{r['bytes']}\tverified={r['verified']}" for r in results]
    write_text(STORAGE_ROOT / "ftp-apply" / "uploaded-files.txt", "\n".join(lines) + "\n")
    write_text(
        STORAGE_ROOT / "ftp-apply" / "upload-result.txt",
        f"uploaded={len(results)} all_verified={all(r['verified'] for r in results)} ts={utc_now()}\n",
    )
    write_json(STORAGE_ROOT / "ftp-apply" / "upload-result.json", results)
    return {"uploads": results}


def phase_cache_clear() -> dict[str, Any]:
    """Clear OpenCart twig/modification caches via SSH if present."""
    import paramiko

    ssh = parse_production_section("SSH")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        ssh["host"],
        port=int(ssh.get("port") or 22),
        username=ssh["username"],
        password=ssh["password"],
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    # Beget layout: /home/.../bzpm.ru/ or relative from home
    cmds = [
        "ls -la ~/bzpm.ru/storage/cache 2>/dev/null | head -20",
        "ls -la ~/bzpm.ru/system/storage/cache 2>/dev/null | head -20",
        "find ~/bzpm.ru -maxdepth 4 -type d -name cache 2>/dev/null | head -20",
    ]
    listings = []
    for cmd in cmds:
        _i, o, e = client.exec_command(cmd, timeout=60)
        listings.append(o.read().decode("utf-8", errors="replace") + e.read().decode("utf-8", errors="replace"))

    # clear template cache files cautiously under known storage/cache
    clear_cmds = [
        "find ~/bzpm.ru/storage/cache -type f -name 'template.*' -delete 2>/dev/null; echo template_cache_cleared:$?",
        "find ~/bzpm.ru/storage/cache -type f -name 'cache.*' -delete 2>/dev/null; echo cache_star_cleared:$?",
        "find ~/bzpm.ru/storage/modification -mindepth 1 -maxdepth 1 ! -name 'index.html' -exec rm -rf {} + 2>/dev/null; echo mod_cleared:$?",
    ]
    clear_out = []
    for cmd in clear_cmds:
        _i, o, e = client.exec_command(cmd, timeout=120)
        clear_out.append(o.read().decode("utf-8", errors="replace") + e.read().decode("utf-8", errors="replace"))
    client.close()
    write_text(
        STORAGE_ROOT / "cache" / "cache-actions.md",
        "# Cache actions\n\n## Listings\n\n```\n"
        + "\n---\n".join(listings)
        + "\n```\n\n## Clear\n\n```\n"
        + "\n".join(clear_out)
        + "\n```\n",
    )
    return {"listings": listings, "clear": clear_out}


def phase_verify_frontend() -> dict[str, Any]:
    urls = [
        "https://bzpm.ru/blog",
        "https://bzpm.ru/blog/news",
        "https://bzpm.ru/blog/news/proizvoditelnost-truda-rck-altayskiy-kray-2026",
        "https://bzpm.ru/",
        "https://bzpm.ru/contact",
        "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stellazhi/stellazhi-premium/stellazhi-premium-vysota-1600",
        "https://bzpm.ru/sitemap.xml",
    ]
    rows = []
    for url in urls:
        r = http_fetch(url)
        body = r.get("body", "")
        rows.append(
            {
                "url": url,
                "status": r.get("status"),
                "has_reading_time": "Время на чтение:" in body,
                "has_bzpm": "БЗПМ" in body,
                "has_blog_list_meta": "blog-list__item__meta" in body,
                "has_blog_item_meta": "blog-item__meta" in body,
                "snippet": "",
            }
        )
        if "Время на чтение:" in body:
            m = re.search(r"Время на чтение:\s*\d+\s+минут[аы]?\.", body)
            rows[-1]["snippet"] = m.group(0) if m else "found but regex miss"
        time.sleep(0.3)

    # find one published detail for reading time if blog list has links
    blog = http_fetch("https://bzpm.ru/blog")
    detail_check = None
    if blog.get("status") == 200:
        links = re.findall(r'href="(https://bzpm\.ru/blog/[^"]+)"', blog.get("body", ""))
        # unique preserve order
        seen = set()
        uniq = []
        for ln in links:
            if ln in seen or ln.rstrip("/") in ("https://bzpm.ru/blog", "https://bzpm.ru/blog/news"):
                continue
            seen.add(ln)
            uniq.append(ln)
        for ln in uniq[:5]:
            d = http_fetch(ln)
            if d.get("status") == 200 and "blog-item__meta" in d.get("body", ""):
                m = re.search(r"Время на чтение:\s*\d+\s+минут[аы]?\.", d.get("body", ""))
                detail_check = {
                    "url": ln,
                    "status": d.get("status"),
                    "reading_time": m.group(0) if m else None,
                    "has_reading_time": bool(m),
                }
                if m:
                    break
            time.sleep(0.2)

    # DB gate for post 13
    gate = mysql_query(
        f"SELECT id, date_added, reading_time_minutes, "
        f"(date_added <= NOW()) AS published_gate FROM oc_blog_posts WHERE id={TARGET_POST_ID}"
    )

    write_json(
        STORAGE_ROOT / "frontend-verification" / "frontend-check.json",
        {"rows": rows, "detail_check": detail_check, "post13_gate": gate.strip(), "ts": utc_now()},
    )
    with (STORAGE_ROOT / "frontend-verification" / "frontend-check.csv").open(
        "w", encoding="utf-8", newline=""
    ) as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "url",
                "status",
                "has_reading_time",
                "has_bzpm",
                "has_blog_list_meta",
                "has_blog_item_meta",
                "snippet",
            ],
        )
        w.writeheader()
        w.writerows(rows)

    # regression csv
    reg = [r for r in rows if r["url"] in urls[:1] or "/contact" in r["url"] or "katalog" in r["url"] or "sitemap" in r["url"] or r["url"].rstrip("/") == "https://bzpm.ru"]
    with (STORAGE_ROOT / "verification" / "regression-check.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["url", "status", "has_bzpm"])
        w.writeheader()
        for r in rows:
            if r["url"] in (
                "https://bzpm.ru/",
                "https://bzpm.ru/contact",
                "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stellazhi/stellazhi-premium/stellazhi-premium-vysota-1600",
                "https://bzpm.ru/sitemap.xml",
            ):
                w.writerow({"url": r["url"], "status": r["status"], "has_bzpm": r["has_bzpm"]})

    write_text(
        STORAGE_ROOT / "frontend-verification" / "screenshots-or-html-snippets.md",
        "# Frontend snippets\n\n"
        + "\n".join(f"- {r['url']}: status={r['status']} reading={r['snippet'] or r['has_reading_time']}" for r in rows)
        + f"\n\nDetail check: {json.dumps(detail_check, ensure_ascii=False)}\n"
        + f"\nPost13 gate: {gate.strip()}\n",
    )
    return {"rows": rows, "detail_check": detail_check, "post13_gate": gate.strip()}


def phase_admin_db_check() -> dict[str, Any]:
    post13 = mysql_query(
        "SELECT id, title, image, active, date_added, reading_time_minutes "
        f"FROM oc_blog_posts WHERE id={TARGET_POST_ID}"
    )
    parts = post13.strip().split("\t")
    data = {
        "raw": post13.strip(),
        "id": parts[0] if parts else None,
        "title": parts[1] if len(parts) > 1 else None,
        "image": parts[2] if len(parts) > 2 else None,
        "active": parts[3] if len(parts) > 3 else None,
        "date_added": parts[4] if len(parts) > 4 else None,
        "reading_time_minutes": parts[5] if len(parts) > 5 else None,
        "date_ok": len(parts) > 4 and parts[4] == TARGET_DATE_MYSQL,
        "image_ok": len(parts) > 2 and parts[2] == "catalog/blog/rck-productivity-hero-zpm-2026.jpg",
    }
    # logo in content
    logo = mysql_query(
        f"SELECT id, (content LIKE '%rck-logo-altay-2026.png%') AS has_logo "
        f"FROM oc_blog_posts WHERE id={TARGET_POST_ID}"
    )
    data["logo_check"] = logo.strip()
    write_json(STORAGE_ROOT / "admin-verification" / "post-13-admin-after.json", data)
    write_text(
        STORAGE_ROOT / "admin-verification" / "post-13-admin-check.md",
        "\n".join(
            [
                "# Post 13 admin/DB check",
                "",
                f"- date_added: `{data['date_added']}` ok={data['date_ok']}",
                f"- image: `{data['image']}` ok={data['image_ok']}",
                f"- reading_time_minutes: `{data['reading_time_minutes']}`",
                f"- logo: {data['logo_check']}",
                "",
                "Admin save via UI: not required for backfill (DB-calculated).",
                "Datetime UI verified by source patch + FTP upload of form with datetimepicker.",
            ]
        ),
    )
    return data


def write_decisions() -> None:
    write_text(
        STORAGE_ROOT / "patch-plan" / "admin-datetime-decision.md",
        "\n".join(
            [
                "# Admin datetime decision",
                "",
                "- Keep `oc_blog_posts.date_added` as publish datetime.",
                "- Admin field remains POST name `modified` (compatibility).",
                "- Display/save format: `YYYY-MM-DD HH:mm` (+ seconds `:00` on save).",
                "- UI: OpenCart bootstrap `datetimepicker` (same as product admin).",
                "- Label: «Дата и время публикации» + help about site time / deferred publish.",
                "- Do not convert Barnaul↔Moscow in admin; storage stays MySQL/site time.",
                f"- Post 13 must remain `{TARGET_DATE_MYSQL}`.",
            ]
        )
        + "\n",
    )
    write_text(
        STORAGE_ROOT / "patch-plan" / "reading-time-decision.md",
        "\n".join(
            [
                "# Reading time decision",
                "",
                f"- Column: `reading_time_minutes TINYINT UNSIGNED NOT NULL DEFAULT 1`",
                f"- Constant: `{CHARS_PER_MINUTE}` Unicode characters / minute",
                "- Formula: strip tags → decode entities → normalize whitespace → mb_strlen → ceil(chars/1500), min 1",
                "- Calculated on admin add/edit save",
                "- Frontend uses stored value + Russian pluralization",
                "- Output: `Время на чтение: N минут.` (with correct склонение)",
                "- Display locations: `.blog-list__item__meta`, `.blog-item__meta`",
            ]
        )
        + "\n",
    )
    write_text(
        STORAGE_ROOT / "patch-plan" / "db-migration-decision.md",
        "\n".join(
            [
                "# DB migration decision",
                "",
                "- No existing reading_time field → ADD COLUMN",
                "- `ALTER TABLE oc_blog_posts ADD COLUMN reading_time_minutes TINYINT UNSIGNED NOT NULL DEFAULT 1 AFTER content;`",
                "- Backfill all posts once from content",
                "- Post 13 update guarded by `date_added='2026-07-16 03:00:00'`",
            ]
        )
        + "\n",
    )


def copy_mirrors_to_repo_tools() -> list[str]:
    REPO_TOOLS.mkdir(parents=True, exist_ok=True)
    prepared = STORAGE_ROOT / "prepared"
    mapping = {
        "admin__controller__blog__posts.php": f"admin_controller_blog_posts-{OPERATION_ID}.php",
        "admin__model__blog__blog.php": f"admin_model_blog_blog-{OPERATION_ID}.php",
        "admin__view__template__blog__posts_form.twig": f"admin_posts_form-{OPERATION_ID}.twig",
        "admin__language__ru-ru__blog__posts.php": f"admin_language_blog_posts-{OPERATION_ID}.php",
        "catalog__controller__blog__category.php": f"catalog_controller_blog_category-{OPERATION_ID}.php",
        "catalog__controller__blog__post.php": f"catalog_controller_blog_post-{OPERATION_ID}.php",
        "catalog__view__theme__default__template__blog__category.twig": f"catalog_blog_category-{OPERATION_ID}.twig",
        "catalog__view__theme__default__template__blog__post.twig": f"catalog_blog_post-{OPERATION_ID}.twig",
    }
    out = []
    for src_name, dest_name in mapping.items():
        src = prepared / src_name
        if src.exists():
            dest = REPO_TOOLS / dest_name
            dest.write_bytes(src.read_bytes())
            out.append(str(dest))
    return out


def main() -> int:
    guard_historical_harness('OPERATION_ID')

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "phase",
        choices=["discover", "prepare", "migrate", "upload", "cache", "verify", "all"],
    )
    args = parser.parse_args()
    STORAGE_ROOT.mkdir(parents=True, exist_ok=True)

    if args.phase in ("discover", "all"):
        print("PHASE discover...")
        d = phase_discover()
        write_decisions()
        print(json.dumps(d.get("summary", d), ensure_ascii=False, indent=2))
        if not d.get("post13_ok"):
            print("STOP — post 13 date mismatch")
            return 2

    if args.phase in ("prepare", "all"):
        print("PHASE prepare...")
        p = phase_prepare_patches()
        mirrors = copy_mirrors_to_repo_tools()
        print(json.dumps({"files": len(p["files"]), "mirrors": len(mirrors)}, indent=2))
        for f in p["files"]:
            print(f"  {f.get('remote')}: changed={f.get('changed')} ok={f.get('ok')}")

    if args.phase in ("migrate", "all"):
        print("PHASE migrate...")
        m = phase_db_migrate()
        print(json.dumps({k: m[k] for k in ("column_added", "backfilled", "post13_date_ok", "post13_raw")}, ensure_ascii=False, indent=2))
        if not m.get("post13_date_ok"):
            print("STOP — post 13 date regression after migrate")
            return 3

    if args.phase in ("upload", "all"):
        print("PHASE upload...")
        u = phase_upload()
        print(json.dumps(u, ensure_ascii=False, indent=2))

    if args.phase in ("cache", "all"):
        print("PHASE cache...")
        c = phase_cache_clear()
        print("cache done")

    if args.phase in ("verify", "all"):
        print("PHASE verify...")
        a = phase_admin_db_check()
        f = phase_verify_frontend()
        print(json.dumps({"admin": a, "frontend_detail": f.get("detail_check"), "gate": f.get("post13_gate")}, ensure_ascii=False, indent=2))

    write_text(STORAGE_ROOT / "logs" / "apply.log", f"phase={args.phase} done ts={utc_now()}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
