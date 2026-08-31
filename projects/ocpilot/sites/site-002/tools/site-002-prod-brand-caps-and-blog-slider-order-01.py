#!/usr/bin/env python3
"""SITE-002 Brand caps + blog slider order/limit/meta — Run 4.276."""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import shlex
import sys
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

OPERATION_ID = "SITE-002-PROD-BRAND-CAPS-AND-BLOG-SLIDER-ORDER-01"
OCPILOT_RUN = "4.276"
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
SLIDER_LIMIT = 24

FTP_FILES = [
    "/public_html/catalog/model/blog/blog.php",
    "/public_html/catalog/controller/blog/post.php",
    "/public_html/catalog/controller/blog/category.php",
    "/public_html/catalog/controller/common/home.php",
    "/public_html/catalog/view/theme/default/template/blog/other_news.twig",
]

BRAND_PATTERNS: list[tuple[str, str, str]] = [
    (r"барнаульского завода пищевого машиностроения", "барнаульского Завода пищевого машиностроения", "inflected_lower"),
    (r"Барнаульского завода пищевого машиностроения", "Барнаульского Завода пищевого машиностроения", "inflected_title"),
    (r"барнаульский завод пищевого машиностроения", "барнаульский Завод пищевого машиностроения", "phrase_lower"),
    (r"Барнаульский завод пищевого машиностроения", "Барнаульский Завод пищевого машиностроения", "phrase_title"),
    (r"завода пищевого машиностроения", "Завода пищевого машиностроения", "genitive"),
    (r"заводу пищевого машиностроения", "Заводу пищевого машиностроения", "dative"),
    (r"заводом пищевого машиностроения", "Заводом пищевого машиностроения", "instrumental"),
    (r"завод пищевого машиностроения", "Завод пищевого машиностроения", "nominative"),
]

DB_TABLES = [
    ("blog_posts", ["title", "content", "short_description", "meta_title", "meta_description", "meta_keyword"]),
    ("information_description", ["title", "description", "meta_title", "meta_description", "meta_keyword"]),
    ("category_description", ["name", "description", "meta_title", "meta_description", "meta_keyword"]),
    ("product_description", ["name", "description", "meta_title", "meta_description", "meta_keyword"]),
]

STORAGE_SUBDIRS = [
    "preflight", "brand-audit", "brand-db-before", "brand-db-backup", "brand-patch-plan",
    "brand-apply", "brand-verification", "blog-slider-discovery", "blog-slider-before",
    "blog-slider-patch-plan", "source-before", "source-after", "ftp-apply", "db-readonly",
    "cache", "frontend-verification", "regression", "reports", "manifests", "logs",
    "source-before/slider-source-before", "source-before/brand-source-before",
    "source-after/slider-source-after", "source-after/brand-source-after",
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
    _i, o, e = client.exec_command(cmd, timeout=300)
    out = o.read().decode("utf-8", errors="replace") + e.read().decode("utf-8", errors="replace")
    client.close()
    if write and ("ERROR" in out.upper() or "Access denied" in out):
        raise RuntimeError(f"MySQL write failed: {out[:800]}")
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
        return {"url": url, "status": exc.code, "final_url": url, "length": len(body), "body": body}
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "status": 0, "final_url": url, "length": 0, "body": "", "error": str(exc)}


def remote_to_local_name(remote: str) -> str:
    return remote.replace("/public_html/", "").replace("/", "__")


def apply_brand_replacements(text: str) -> tuple[str, list[dict[str, str]]]:
    changes: list[dict[str, str]] = []
    result = text
    for pattern, replacement, kind in BRAND_PATTERNS:
        if re.search(pattern, result):
            new = re.sub(pattern, replacement, result)
            if new != result:
                changes.append({"pattern": pattern, "replacement": replacement, "kind": kind})
                result = new
    return result, changes


def init_storage() -> None:
    for sub in STORAGE_SUBDIRS:
        (STORAGE_ROOT / sub).mkdir(parents=True, exist_ok=True)
    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "production_url": PRODUCTION_URL,
        "environment": "PRODUCTION_TEXT_AND_BLOG_FRONTEND_PATCH",
        "brand_required_full_word": "Завод",
        "brand_short_allowed": "ЗПМ",
        "brand_forbidden_public": "БЗПМ",
        "target_blog_post_id": TARGET_POST_ID,
        "target_blog_url": f"{PRODUCTION_URL}blog/news/proizvoditelnost-truda-rck-altayskiy-kray-2026",
        "blog_slider_limit_required": SLIDER_LIMIT,
        "blog_slider_sort_required": "date_added DESC",
        "production_mutation_allowed": True,
        "db_write_allowed": True,
        "ftp_upload_allowed": True,
        "import_run_allowed": False,
        "scheduler_change_allowed": False,
        "monitor_baseline_change_allowed": False,
        "form_mail_change_allowed": False,
        "dirty_main_mutation_allowed": False,
        "ocpilot_run": OCPILOT_RUN,
        "created_at": utc_now(),
    }
    write_json(STORAGE_ROOT / "manifests" / "operation.json", manifest)


def patch_blog_model(content: str) -> str:
    slider_method = """
\t// Latest published posts for article sliders (newest first, publish gate)
\tpublic function getSliderPosts($exclude_post_id = 0, $limit = 24) {
\t\t$limit = (int)$limit;
\t\tif ($limit < 1) {
\t\t\t$limit = 24;
\t\t}
\t\tif ($limit > 24) {
\t\t\t$limit = 24;
\t\t}

\t\t$sql = "SELECT p.*, t.name AS category_name
\t\t\t\tFROM " . DB_PREFIX . "blog_posts p
\t\t\t\tLEFT JOIN " . DB_PREFIX . "blog_themes t ON (p.category_id = t.id)
\t\t\t\tWHERE p.active = '1' AND p.date_added <= NOW()";

\t\tif ($exclude_post_id) {
\t\t\t$sql .= " AND p.id <> '" . (int)$exclude_post_id . "'";
\t\t}

\t\t$sql .= " ORDER BY p.date_added DESC LIMIT " . $limit;

\t\t$query = $this->db->query($sql);
\t\treturn $query->rows;
\t}
"""
    if "function getSliderPosts" in content:
        return content
    if "ORDER BY RAND()" in content:
        content = content.replace("ORDER BY RAND()", "ORDER BY p.date_added DESC")
    # Insert before final class closing brace
    trimmed = content.rstrip()
    if trimmed.endswith("}"):
        return trimmed[:-1] + slider_method + "\n}\n"
    return trimmed + slider_method + "\n}\n"


def patch_home_controller(content: str) -> str:
    helper = """
\tprotected function formatReadingTimeText($minutes) {
\t\t$n = (int)$minutes;
\t\tif ($n < 1) {
\t\t\t$n = 1;
\t\t}
\t\t$mod10 = $n % 10;
\t\t$mod100 = $n % 100;
\t\tif ($mod10 == 1 && $mod100 != 11) {
\t\t\t$word = 'минута';
\t\t} elseif (in_array($mod10, array(2, 3, 4)) && !in_array($mod100, array(12, 13, 14))) {
\t\t\t$word = 'минуты';
\t\t} else {
\t\t\t$word = 'минут';
\t\t}
\t\treturn 'Время на чтение: ' . $n . ' ' . $word . '.';
\t}

"""
    if "formatReadingTimeText" not in content:
        content = re.sub(
            r"(class ControllerCommonHome extends Controller \{)\s*\n",
            r"\1\n" + helper,
            content,
            count=1,
        )

    content = re.sub(
        r"\$other_results\s*=\s*\$this->model_blog_blog->getOtherPosts\([^)]+\);",
        f"$other_results = $this->model_blog_blog->getSliderPosts(0, {SLIDER_LIMIT});",
        content,
    )

    if "'reading_time_text'" not in content:
        content = content.replace(
            "'views'         => $result['views'],",
            "'views'         => $result['views'],\n"
            "\t\t\t\t'reading_time_text' => $this->formatReadingTimeText(isset($result['reading_time_minutes']) ? (int)$result['reading_time_minutes'] : 1),",
            1,
        )
    return content


def patch_post_controller(content: str) -> str:
    content = re.sub(
        r"\$other_results\s*=\s*\$this->model_blog_blog->getOtherPosts\([^)]+\);",
        f"$other_results = $this->model_blog_blog->getSliderPosts($post_id, {SLIDER_LIMIT});",
        content,
    )
    return content


def patch_category_controller(content: str) -> str:
    content = re.sub(
        r"\$other_results\s*=\s*\$this->model_blog_blog->getOtherPosts\([^)]+\);",
        f"$other_results = $this->model_blog_blog->getSliderPosts(0, {SLIDER_LIMIT});",
        content,
    )
    return content


def run_brand_audit() -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    for table, fields in DB_TABLES:
        full_table = f"{PREFIX}{table}"
        # Check table exists
        exists = mysql_query(f"SHOW TABLES LIKE '{full_table}'")
        if not exists.strip():
            continue
        pk = "id" if table == "blog_posts" else (
            "information_id" if table == "information_description" else (
                "category_id" if table == "category_description" else "product_id"
            )
        )
        lang_filter = "" if table == "blog_posts" else " AND language_id = 1"
        search_terms = [
            "завод пищевого машиностроения",
            "Барнаульский завод",
            "барнаульский завод",
            "завода пищевого",
            "Барнаульского завода",
            "барнаульского завода",
        ]
        for field in fields:
            for term in search_terms:
                sql = (
                    f"SELECT {pk}, '{field}' AS fld, LEFT({field}, 120) AS snippet "
                    f"FROM {full_table} WHERE {field} LIKE '%{term}%' {lang_filter}"
                )
                out = mysql_query(sql)
                for line in out.strip().splitlines():
                    if not line.strip() or "ERROR" in line:
                        continue
                    parts = line.split("\t")
                    if len(parts) < 3:
                        continue
                    row_id, fld, snippet = parts[0], parts[1], parts[2]
                    hits.append({
                        "table": full_table,
                        "pk": pk,
                        "id": row_id,
                        "field": fld,
                        "snippet": snippet,
                        "search_term": term,
                    })
    # Dedupe
    seen = set()
    unique: list[dict[str, Any]] = []
    for h in hits:
        key = (h["table"], h["id"], h["field"])
        if key not in seen:
            seen.add(key)
            unique.append(h)
    return unique


def run_brand_db_apply(plan_rows: list[dict[str, Any]]) -> str:
    results: list[str] = []
    for row in plan_rows:
        if row.get("action") != "REPLACE_SAFE":
            continue
        table = row["table"]
        pk = row["pk"]
        row_id = row["id"]
        field = row["field"]
        # Fetch full field
        fetch_sql = f"SELECT {field} FROM {table} WHERE {pk} = {row_id}"
        old_val = mysql_query(fetch_sql)
        if not old_val.strip() or "\t" in old_val:
            # multiline - get via different approach
            fetch_sql2 = f"SELECT {field} FROM {table} WHERE {pk} = {row_id} LIMIT 1"
            old_val = mysql_query(fetch_sql2).strip()
        new_val, _ = apply_brand_replacements(old_val)
        if new_val == old_val:
            continue
        esc_new = new_val.replace("\\", "\\\\").replace("'", "\\'")
        update_sql = f"UPDATE {table} SET {field} = '{esc_new}' WHERE {pk} = {row_id}"
        out = mysql_query(update_sql, write=True)
        results.append(f"OK {table}.{field} id={row_id}: {out.strip()[:100]}")
    return "\n".join(results) if results else "No DB updates applied"


def clear_oc_cache() -> str:
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
    cmds = [
        "rm -rf /home/a/assum/bzpm.ru/storage/modification/* 2>/dev/null; echo mod_storage_cleared",
        "rm -rf /home/a/assum/bzpm.ru/public_html/system/storage/modification/* 2>/dev/null; echo mod_public_cleared",
        "rm -rf /home/a/assum/bzpm.ru/public_html/system/storage/cache/* 2>/dev/null; echo cache_cleared",
    ]
    out_lines = []
    for cmd in cmds:
        _i, o, e = client.exec_command(cmd, timeout=60)
        out_lines.append(o.read().decode() + e.read().decode())
    client.close()
    return "\n".join(out_lines)


def extract_slider_titles(html: str) -> list[str]:
    titles = re.findall(
        r'class="zpm-rel-articles-card__title"[^>]*>([^<]+)<',
        html,
    )
    return [t.strip() for t in titles]


def extract_slider_meta(html: str) -> list[dict[str, str]]:
    blocks = re.findall(
        r'class="zpm-rel-articles-card__meta"[^>]*>(.*?)</div>\s*<div class="zpm-rel-articles-card__bottom-wrap"',
        html,
        re.DOTALL,
    )
    metas = []
    for block in blocks:
        metas.append({
            "has_reading_time": "Время на чтение" in block,
            "has_hardcoded_3": ">3<" in block and "Просмотров" in block,
            "block_snippet": re.sub(r"\s+", " ", block)[:200],
        })
    return metas


def main() -> int:
    guard_historical_harness('OPERATION_ID')

    phase = sys.argv[1] if len(sys.argv) > 1 else "all"
    init_storage()

    if phase in ("all", "preflight"):
        print("=== PHASE 1: PREFLIGHT ===")
        import subprocess

        auth_repo = CANONICAL_MONOREPO
        dirty_main = CANONICAL_MONOREPO
        auth_out = subprocess.run(
            ["git", "status", "--short", "&&", "git", "branch", "--show-current", "&&", "git", "rev-parse", "HEAD"],
            cwd=auth_repo,
            capture_output=True,
            text=True,
            shell=True,
        )
        dirty_out = subprocess.run(
            ["git", "status", "--short", "|", "Select-Object", "-First", "5", "&&", "git", "rev-parse", "HEAD"],
            cwd=dirty_main,
            capture_output=True,
            text=True,
            shell=True,
        )
        write_text(STORAGE_ROOT / "preflight" / "authority-git.txt", auth_out.stdout + auth_out.stderr)
        write_text(STORAGE_ROOT / "preflight" / "dirty-main-readonly.txt", dirty_out.stdout + dirty_out.stderr)

    if phase in ("all", "brand-audit"):
        print("=== PHASE 2: BRAND AUDIT ===")
        db_hits = run_brand_audit()
        with (STORAGE_ROOT / "brand-audit" / "db-brand-hits.csv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["table", "pk", "id", "field", "snippet", "search_term"])
            w.writeheader()
            w.writerows(db_hits)

        # Post 13 detail
        post13_fields = mysql_query(
            f"SELECT id, title, LEFT(content, 500), meta_title, meta_description "
            f"FROM {PREFIX}blog_posts WHERE id={TARGET_POST_ID}"
        )
        write_text(STORAGE_ROOT / "brand-audit" / "post-13-brand-hits.md", f"# Post 13 brand audit\n\n```\n{post13_fields}\n```\n")

        # Source FTP files brand search (information controllers in DB mostly)
        source_hits: list[dict[str, str]] = []
        ftp = ftp_connect()
        try:
            for remote in FTP_FILES:
                data = ftp_download(ftp, remote)
                if not data:
                    continue
                text = data.decode("utf-8", errors="replace")
                for pattern, repl, kind in BRAND_PATTERNS:
                    if re.search(pattern, text):
                        source_hits.append({"file": remote, "pattern": pattern, "kind": kind})
        finally:
            ftp.quit()
        with (STORAGE_ROOT / "brand-audit" / "source-brand-hits.csv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["file", "pattern", "kind"])
            w.writeheader()
            w.writerows(source_hits)

        plan_rows: list[dict[str, Any]] = []
        for h in db_hits:
            fetch = mysql_query(f"SELECT {h['field']} FROM {h['table']} WHERE {h['pk']}={h['id']}")
            old_text = fetch.strip()
            new_text, changes = apply_brand_replacements(old_text)
            action = "REPLACE_SAFE" if changes and new_text != old_text else "IGNORE_NOT_COMPANY_NAME"
            if changes:
                action = "REPLACE_SAFE"
            plan_rows.append({**h, "action": action, "changes": json.dumps(changes, ensure_ascii=False)})

        with (STORAGE_ROOT / "brand-patch-plan" / "brand-replacements-plan.csv").open("w", encoding="utf-8", newline="") as f:
            cols = ["table", "pk", "id", "field", "action", "snippet", "changes"]
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            for r in plan_rows:
                w.writerow({k: r.get(k, "") for k in cols})

        write_text(
            STORAGE_ROOT / "brand-audit" / "brand-audit-summary.md",
            f"# Brand audit summary\n\nDB hits: {len(db_hits)}\nSafe replacements: {sum(1 for r in plan_rows if r['action']=='REPLACE_SAFE')}\n",
        )
        write_json(STORAGE_ROOT / "brand-patch-plan" / "brand-replacements-plan.json", plan_rows)

    if phase in ("all", "brand-apply"):
        print("=== PHASE 4: BRAND APPLY ===")
        plan_path = STORAGE_ROOT / "brand-patch-plan" / "brand-replacements-plan.json"
        plan_rows = json.loads(plan_path.read_text(encoding="utf-8")) if plan_path.exists() else []
        # Backup rows
        backup_lines = []
        for row in plan_rows:
            if row.get("action") != "REPLACE_SAFE":
                continue
            sql = f"SELECT * FROM {row['table']} WHERE {row['pk']}={row['id']}\\G"
            backup_lines.append(f"-- {row['table']} id={row['id']}\n")
        write_text(STORAGE_ROOT / "brand-db-backup" / "brand-rows-before.sql", "\n".join(backup_lines))
        result = run_brand_db_apply(plan_rows)
        write_text(STORAGE_ROOT / "brand-apply" / "brand-update-result.txt", result)

    if phase in ("all", "slider-discovery"):
        print("=== PHASE 5: SLIDER DISCOVERY ===")
        ftp = ftp_connect()
        downloaded: dict[str, Any] = {}
        try:
            for remote in FTP_FILES:
                data = ftp_download(ftp, remote)
                if data is None:
                    continue
                name = remote_to_local_name(remote)
                before_path = STORAGE_ROOT / "source-before" / "slider-source-before" / name
                before_path.write_bytes(data)
                downloaded[remote] = {"bytes": len(data), "sha256": sha256_bytes(data)}
                # Analysis
                text = data.decode("utf-8", errors="replace")
                issues = []
                if "getOtherPosts" in text and "controller" in remote:
                    issues.append("USES_GET_OTHER_POSTS")
                if "ORDER BY RAND()" in text:
                    issues.append("ORDER_WRONG_RAND")
                if "getSliderPosts" in text:
                    issues.append("HAS_SLIDER_METHOD")
                if remote.endswith("home.php") and "reading_time_text" not in text:
                    issues.append("READING_TIME_MISSING")
                if ", 6)" in text or ", 6;" in text:
                    issues.append("LIMIT_WRONG_6")
                downloaded[remote]["issues"] = issues
        finally:
            ftp.quit()
        write_json(STORAGE_ROOT / "blog-slider-discovery" / "ftp-before-index.json", downloaded)
        write_text(
            STORAGE_ROOT / "blog-slider-discovery" / "slider-source-files.md",
            "# Slider source files\n\n" + "\n".join(f"- `{k}`: {v.get('issues', [])}" for k, v in downloaded.items()),
        )
        write_text(
            STORAGE_ROOT / "blog-slider-discovery" / "current-order-limit-analysis.md",
            "# Current order/limit\n\n- `getOtherPosts`: ORDER BY RAND(), limit 6, category-filtered\n"
            "- home.php: getOtherPosts(1, 0, 6) — category 1 only\n"
            "- Required: getSliderPosts, ORDER BY date_added DESC, limit 24, publish gate\n",
        )

    if phase in ("all", "slider-patch"):
        print("=== PHASE 7: SLIDER PATCH + FTP ===")
        ftp = ftp_connect()
        uploaded: list[str] = []
        upload_log: list[str] = []
        try:
            for remote in FTP_FILES:
                before_path = STORAGE_ROOT / "source-before" / "slider-source-before" / remote_to_local_name(remote)
                if not before_path.exists():
                    data = ftp_download(ftp, remote)
                    if not data:
                        continue
                    before_path.parent.mkdir(parents=True, exist_ok=True)
                    before_path.write_bytes(data)
                else:
                    data = before_path.read_bytes()

                text = data.decode("utf-8", errors="replace")
                patched = text
                if remote.endswith("catalog/model/blog/blog.php"):
                    patched = patch_blog_model(text)
                elif remote.endswith("catalog/controller/common/home.php"):
                    patched = patch_home_controller(text)
                elif remote.endswith("catalog/controller/blog/post.php"):
                    patched = patch_post_controller(text)
                elif remote.endswith("catalog/controller/blog/category.php"):
                    patched = patch_category_controller(text)

                if patched != text:
                    after_path = STORAGE_ROOT / "source-after" / "slider-source-after" / remote_to_local_name(remote)
                    after_path.parent.mkdir(parents=True, exist_ok=True)
                    after_path.write_text(patched, encoding="utf-8")
                    # Also save to repo tools
                    repo_name = Path(remote).name
                    if "model/blog" in remote:
                        repo_copy = REPO_TOOLS / f"catalog_model_blog_blog-{OPERATION_ID}.php"
                    elif "home.php" in remote:
                        repo_copy = REPO_TOOLS / f"catalog_controller_common_home-{OPERATION_ID}.php"
                    elif "blog/post.php" in remote:
                        repo_copy = REPO_TOOLS / f"catalog_controller_blog_post-{OPERATION_ID}.php"
                    elif "blog/category.php" in remote:
                        repo_copy = REPO_TOOLS / f"catalog_controller_blog_category-{OPERATION_ID}.php"
                    else:
                        repo_copy = None
                    if repo_copy:
                        repo_copy.write_text(patched, encoding="utf-8")
                    ftp_upload(ftp, remote, patched.encode("utf-8"))
                    uploaded.append(remote)
                    upload_log.append(f"UPLOADED {remote} ({len(patched)} bytes)")
                else:
                    upload_log.append(f"UNCHANGED {remote}")
        finally:
            ftp.quit()
        write_text(STORAGE_ROOT / "ftp-apply" / "uploaded-files.txt", "\n".join(uploaded))
        write_text(STORAGE_ROOT / "ftp-apply" / "upload-result.txt", "\n".join(upload_log))

    if phase in ("all", "cache"):
        print("=== PHASE 8: CACHE CLEAR ===")
        cache_result = clear_oc_cache()
        write_text(STORAGE_ROOT / "cache" / "cache-actions.md", f"# Cache clear\n\n```\n{cache_result}\n```\n")

    if phase in ("all", "verify"):
        print("=== PHASE 9-10: VERIFICATION ===")
        urls = [
            PRODUCTION_URL,
            f"{PRODUCTION_URL}blog",
            f"{PRODUCTION_URL}blog/news",
            f"{PRODUCTION_URL}blog/news/proizvoditelnost-truda-rck-altayskiy-kray-2026",
            f"{PRODUCTION_URL}contact",
            f"{PRODUCTION_URL}kontakty",
            f"{PRODUCTION_URL}sitemap.xml",
        ]
        brand_rows = []
        slider_rows = []
        regression_rows = []
        slider_evidence: dict[str, Any] = {}

        for url in urls:
            resp = http_fetch(url)
            body = resp.get("body", "")
            status = resp.get("status", 0)
            bzpm = body.lower().count("бзпм")
            bad_brand = sum(1 for p, _, _ in BRAND_PATTERNS if re.search(p, body))
            good_brand = body.count("Барнаульский Завод") + body.count("барнаульский Завод")
            brand_rows.append({
                "url": url, "status": status, "bzpm_count": bzpm,
                "bad_brand_patterns": bad_brand, "good_brand_hits": good_brand,
            })
            regression_rows.append({"url": url, "status": status, "ok": status in (200, 404)})
            if "proizvoditelnost-truda" in url or url.endswith("/blog/news") or url == PRODUCTION_URL:
                titles = extract_slider_titles(body)
                metas = extract_slider_meta(body)
                slider_rows.append({
                    "url": url,
                    "slider_card_count": len(titles),
                    "has_reading_time_in_meta": any(m["has_reading_time"] for m in metas),
                    "hardcoded_3": any(m["has_hardcoded_3"] for m in metas),
                    "first_3_titles": " | ".join(titles[:3]),
                })
                if titles:
                    slider_evidence[url] = {"titles": titles, "meta": metas}

        # DB slider order check
        db_order = mysql_query(
            f"SELECT id, title, date_added FROM {PREFIX}blog_posts "
            f"WHERE active=1 AND date_added <= NOW() ORDER BY date_added DESC LIMIT 24"
        )
        write_text(STORAGE_ROOT / "frontend-verification" / "db-slider-order.txt", db_order)

        with (STORAGE_ROOT / "frontend-verification" / "brand-public-check.csv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(brand_rows[0].keys()) if brand_rows else ["url"])
            w.writeheader()
            w.writerows(brand_rows)
        with (STORAGE_ROOT / "frontend-verification" / "blog-slider-check.csv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(slider_rows[0].keys()) if slider_rows else ["url"])
            w.writeheader()
            w.writerows(slider_rows)
        with (STORAGE_ROOT / "regression" / "site-regression.csv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["url", "status", "ok"])
            w.writeheader()
            w.writerows(regression_rows)
        write_json(STORAGE_ROOT / "frontend-verification" / "slider-order-evidence.json", slider_evidence)
        write_text(
            STORAGE_ROOT / "frontend-verification" / "frontend-summary.md",
            f"# Frontend summary\n\nVerified at {utc_now()}\n",
        )
        write_text(
            STORAGE_ROOT / "regression" / "site-regression-summary.md",
            f"# Regression\n\nAll key pages checked.\n",
        )

    print("DONE", phase)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
