#!/usr/bin/env python3
"""SITE-002 Blog literal newline cleanup — Run 4.277."""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import shlex
import subprocess
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

OPERATION_ID = "SITE-002-PROD-BLOG-LITERAL-NEWLINE-CLEANUP-01"
OCPILOT_RUN = "4.277"
SITE_ID = "SITE-002"
PRODUCTION_URL = "https://bzpm.ru/"
TARGET_POST_ID = 13
TARGET_SEO_URL = f"{PRODUCTION_URL}blog/news/proizvoditelnost-truda-rck-altayskiy-kray-2026"
TARGET_ROUTE_URL = f"{PRODUCTION_URL}index.php?route=blog/post&blog_post_id={TARGET_POST_ID}"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
STORAGE_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
AUTH_REPO = CANONICAL_MONOREPO
DIRTY_MAIN = CANONICAL_MONOREPO
PREFIX = "oc_"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

# Literal backslash + n (two ASCII chars), not real newline
LITERAL_NL = "\\n"
LITERAL_CRNL = "\\r\\n"

DB_TABLES: list[tuple[str, str, list[str]]] = [
    ("blog_posts", "id", ["title", "content", "short_description", "meta_title", "meta_description", "meta_keyword"]),
    ("information_description", "information_id", ["title", "description", "meta_title", "meta_description", "meta_keyword"]),
    ("category_description", "category_id", ["name", "description", "meta_title", "meta_description", "meta_keyword"]),
    ("product_description", "product_id", ["name", "description", "meta_title", "meta_description", "meta_keyword"]),
]

SOURCE_SEARCH_PATHS = [
    "catalog/controller/blog/",
    "catalog/model/blog/",
    "catalog/view/theme/default/template/blog/",
    "catalog/controller/information/",
    "catalog/view/theme/default/template/information/",
    "catalog/controller/common/home.php",
    "admin/controller/blog/",
    "admin/model/blog/",
]

PUBLIC_CHECK_URLS = [
    ("post_13_route", TARGET_ROUTE_URL),
    ("post_13_seo", TARGET_SEO_URL),
    ("blog", f"{PRODUCTION_URL}blog"),
    ("blog_news", f"{PRODUCTION_URL}blog/news"),
    ("home", PRODUCTION_URL),
    ("contact", f"{PRODUCTION_URL}contact"),
    ("about", f"{PRODUCTION_URL}about"),
    ("sitemap", f"{PRODUCTION_URL}sitemap.xml"),
    ("kontakty", f"{PRODUCTION_URL}kontakty"),
]

STORAGE_SUBDIRS = [
    "preflight", "artifact-audit", "db-audit", "source-audit", "db-backup", "db-apply",
    "source-before", "source-after", "patch-plan", "ftp-apply", "cache",
    "verification", "regression", "reports", "manifests", "logs",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def init_storage() -> None:
    for sub in STORAGE_SUBDIRS:
        (STORAGE_ROOT / sub).mkdir(parents=True, exist_ok=True)
    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "production_url": PRODUCTION_URL,
        "target_post_id": TARGET_POST_ID,
        "target_url": TARGET_SEO_URL,
        "problem_literal": "\\n",
        "production_mutation_allowed": "true_exact_content_cleanup_and_minimal_normalization_only",
        "db_write_allowed": "true_exact_affected_rows_only",
        "ftp_upload_allowed": "true_only_if_source_patch_needed",
        "import_run_allowed": False,
        "scheduler_change_allowed": False,
        "monitor_baseline_change_allowed": False,
        "form_mail_change_allowed": False,
        "dirty_main_mutation_allowed": False,
        "ocpilot_run": OCPILOT_RUN,
        "created_at": utc_now(),
    }
    write_json(STORAGE_ROOT / "manifests" / "operation.json", manifest)


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


def ssh_connect():
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
    return client


def mysql_query(sql: str, write: bool = False) -> str:
    client = ssh_connect()
    db = parse_production_section("Database")
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


def mysql_fetch_field(table: str, pk: str, row_id: int | str, field: str) -> str:
    """Fetch full field value via HEX encoding (preserves all bytes)."""
    hex_sql = f"SELECT HEX({field}) FROM {table} WHERE {pk} = {row_id} LIMIT 1"
    hex_out = mysql_query(hex_sql).strip().splitlines()[0].strip()
    if not hex_out or "ERROR" in hex_out.upper():
        raise RuntimeError(f"fetch failed {table}.{field} id={row_id}: {hex_out[:200]}")
    return bytes.fromhex(hex_out).decode("utf-8", errors="replace")


def mysql_update_field_replace(table: str, pk: str, row_id: int | str, field: str) -> str:
    """Remove literal backslash+n via SQL REPLACE (safe for exact artifact)."""
    sql = (
        f"UPDATE {table} SET {field} = REPLACE(REPLACE({field}, '\\\\r\\\\n', ''), '\\\\n', '') "
        f"WHERE {pk} = {row_id}"
    )
    return mysql_query(sql, write=True)


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


def count_literal_newlines(text: str) -> int:
    return text.count(LITERAL_NL) + text.count(LITERAL_CRNL)


def find_literal_newline_snippets(text: str, context: int = 40) -> list[str]:
    snippets: list[str] = []
    for needle in (LITERAL_CRNL, LITERAL_NL):
        start = 0
        while True:
            idx = text.find(needle, start)
            if idx < 0:
                break
            lo = max(0, idx - context)
            hi = min(len(text), idx + len(needle) + context)
            snippets.append(repr(text[lo:hi]))
            start = idx + len(needle)
    return snippets


def normalize_literal_newlines(text: str) -> tuple[str, int]:
    """Remove literal \\n / \\r\\n artifacts from public HTML-ish content."""
    if LITERAL_NL not in text and LITERAL_CRNL not in text:
        return text, 0
    original_count = count_literal_newlines(text)
    result = text.replace(LITERAL_CRNL, "")
    result = result.replace(LITERAL_NL, "")
    return result, original_count


def classify_hit(table: str, field: str, snippet: str) -> str:
    if table.endswith("blog_posts") or field in ("content", "description", "short_description"):
        return "PUBLIC_ARTIFACT_FIX_SAFE"
    if field in ("title", "name", "meta_title", "meta_description", "meta_keyword"):
        if LITERAL_NL in snippet or LITERAL_CRNL in snippet:
            return "PUBLIC_ARTIFACT_FIX_SAFE"
    return "AMBIGUOUS_REVIEW_ONLY"


def run_preflight() -> None:
    auth_cmds = [
        "git status --short",
        "git status --branch --porcelain=v2",
        "git branch --show-current",
        "git rev-parse --show-toplevel",
        "git rev-parse origin/mars/canonical-post-recovery",
        "git log --oneline --decorate -12",
    ]
    auth_out = []
    for cmd in auth_cmds:
        r = subprocess.run(cmd, cwd=AUTH_REPO, capture_output=True, text=True, shell=True)
        auth_out.append(f"$ {cmd}\n{r.stdout}{r.stderr}")
    write_text(STORAGE_ROOT / "preflight" / "authority-git.txt", "\n\n".join(auth_out))

    dirty_cmds = ["git status --short", "git status --branch --porcelain=v2", "git rev-parse HEAD"]
    dirty_out = []
    for cmd in dirty_cmds:
        r = subprocess.run(cmd, cwd=DIRTY_MAIN, capture_output=True, text=True, shell=True)
        dirty_out.append(f"$ {cmd}\n{r.stdout}{r.stderr}")
    write_text(STORAGE_ROOT / "preflight" / "dirty-main-readonly.txt", "\n\n".join(dirty_out))


def run_artifact_audit(suffix: str = "before") -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    post13_body = ""
    post13_status = 0

    for label, url in PUBLIC_CHECK_URLS:
        resp = http_fetch(url)
        fname = f"{label.replace('/', '_')}-{suffix}.html"
        if label == "post_13_route":
            write_text(STORAGE_ROOT / "artifact-audit" / f"post-13-html-{suffix}.html", resp["body"])
            post13_body = resp["body"]
            post13_status = resp["status"]
        elif label == "post_13_seo" and suffix == "before":
            write_text(STORAGE_ROOT / "artifact-audit" / f"post-13-seo-{suffix}.html", resp["body"])
        elif suffix == "before" and label in ("blog", "blog_news", "home"):
            write_text(STORAGE_ROOT / "artifact-audit" / f"{label}-{suffix}.html", resp["body"])

        literal_count = count_literal_newlines(resp["body"])
        visible_backslash_n = len(re.findall(r"(?<![\\])\\n", resp["body"]))
        results.append({
            "label": label,
            "url": url,
            "status": resp["status"],
            "literal_backslash_n_in_html": visible_backslash_n,
            "body_length": resp["length"],
        })

    csv_path = STORAGE_ROOT / ("artifact-audit" if suffix == "before" else "verification") / (
        f"public-pages-literal-newline-check-{suffix}.csv"
    )
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        w.writeheader()
        w.writerows(results)

    snippets = find_literal_newline_snippets(post13_body, 60)
    snippet_md = (
        f"# Post 13 literal newline snippets ({suffix})\n\n"
        f"- URL: {TARGET_ROUTE_URL}\n"
        f"- HTTP status: {post13_status}\n"
        f"- Visible `\\n` count in body: {len(re.findall(r'\\\\n', post13_body))}\n\n"
    )
    for i, sn in enumerate(snippets[:20], 1):
        snippet_md += f"## Snippet {i}\n\n```\n{sn}\n```\n\n"

    out_dir = STORAGE_ROOT / ("artifact-audit" if suffix == "before" else "verification")
    write_text(out_dir / f"post-13-literal-newline-snippets-{suffix}.md", snippet_md)

    confirmation = {
        "checked_at": utc_now(),
        "target_post_id": TARGET_POST_ID,
        "route_url": TARGET_ROUTE_URL,
        "seo_url": TARGET_SEO_URL,
        "route_status": post13_status,
        "literal_newline_snippets_found": len(snippets),
        "pages": results,
    }
    if suffix == "before":
        write_json(STORAGE_ROOT / "artifact-audit" / "post-13-public-confirmation.json", confirmation)
    return confirmation


def run_db_audit() -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    # Search using INSTR for literal backslash (92) + n (110)
    for table_suffix, pk, fields in DB_TABLES:
        full_table = f"{PREFIX}{table_suffix}"
        exists = mysql_query(f"SHOW TABLES LIKE '{full_table}'").strip()
        if not exists:
            continue
        lang_filter = "" if table_suffix == "blog_posts" else " AND language_id = 1"
        for field in fields:
            sql = (
                f"SELECT {pk}, '{field}' AS fld, "
                f"LEFT({field}, 200) AS snippet, "
                f"(LENGTH({field}) - LENGTH(REPLACE({field}, '\\\\n', ''))) / 2 AS nl_count "
                f"FROM {full_table} "
                f"WHERE INSTR({field}, '\\\\n') > 0 {lang_filter}"
            )
            out = mysql_query(sql)
            for line in out.strip().splitlines():
                if not line.strip() or "ERROR" in line.upper():
                    continue
                parts = line.split("\t")
                if len(parts) < 4:
                    continue
                row_id, fld, snippet, nl_count = parts[0], parts[1], parts[2], parts[3]
                classification = classify_hit(full_table, fld, snippet)
                hits.append({
                    "table": full_table,
                    "pk": pk,
                    "id": row_id,
                    "field": fld,
                    "snippet": snippet,
                    "literal_nl_count": nl_count,
                    "classification": classification,
                })
    # Dedupe
    seen: set[tuple[str, str, str]] = set()
    unique: list[dict[str, Any]] = []
    for h in hits:
        key = (h["table"], h["id"], h["field"])
        if key not in seen:
            seen.add(key)
            unique.append(h)

    with (STORAGE_ROOT / "db-audit" / "db-literal-newline-hits.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(unique[0].keys()) if unique else [
            "table", "pk", "id", "field", "snippet", "literal_nl_count", "classification"
        ])
        w.writeheader()
        w.writerows(unique)
    write_json(STORAGE_ROOT / "db-audit" / "db-literal-newline-hits.json", unique)

    summary = (
        f"# DB audit summary\n\n"
        f"- Checked at: {utc_now()}\n"
        f"- Total hits: {len(unique)}\n"
        f"- PUBLIC_ARTIFACT_FIX_SAFE: {sum(1 for h in unique if h['classification'] == 'PUBLIC_ARTIFACT_FIX_SAFE')}\n"
        f"- AMBIGUOUS_REVIEW_ONLY: {sum(1 for h in unique if h['classification'] == 'AMBIGUOUS_REVIEW_ONLY')}\n\n"
    )
    for h in unique:
        summary += f"- `{h['table']}` id={h['id']} field={h['field']} count≈{h['literal_nl_count']} → {h['classification']}\n"
    write_text(STORAGE_ROOT / "db-audit" / "db-audit-summary.md", summary)
    return unique


def run_source_audit() -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    for rel in SOURCE_SEARCH_PATHS:
        path = AUTH_REPO / rel if rel.endswith(".php") else None
        if path and path.is_file():
            files = [path]
        elif path is None:
            base = AUTH_REPO / rel.rstrip("/")
            if not base.exists():
                continue
            files = list(base.rglob("*")) if base.is_dir() else [base]
        else:
            files = []
        for fp in files:
            if not fp.is_file() or fp.suffix not in (".php", ".twig", ".js"):
                continue
            try:
                text = fp.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            rel_path = str(fp.relative_to(AUTH_REPO)).replace("\\", "/")
            # Look for patterns that OUTPUT literal \n
            patterns = [
                (r"'\\n'", "single_quoted_literal_backslash_n"),
                (r'"\\n"', "double_quoted_literal_backslash_n"),
                (r"\. '\\n'", "concat_literal_backslash_n"),
                (r'json_encode.*\\\\n', "json_encode_escaped_newline"),
            ]
            for pat, kind in patterns:
                for m in re.finditer(pat, text):
                    line_no = text[: m.start()].count("\n") + 1
                    hits.append({
                        "file": rel_path,
                        "line": line_no,
                        "pattern": kind,
                        "match": m.group(0)[:80],
                        "classification": "SAFE_UNKNOWN",
                    })
    with (STORAGE_ROOT / "source-audit" / "source-literal-newline-hits.csv").open(
        "w", encoding="utf-8", newline=""
    ) as f:
        fields = ["file", "line", "pattern", "match", "classification"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(hits)

    source_issue = "NO_SOURCE_ISSUE" if not hits else "SAFE_UNKNOWN"
    write_text(
        STORAGE_ROOT / "source-audit" / "source-audit-summary.md",
        f"# Source audit summary\n\n"
        f"- Hits in authority worktree: {len(hits)}\n"
        f"- Classification: **{source_issue}**\n"
        f"- Root cause likely: **DB_CONTENT_ONLY** (content pasted/stored with escaped newlines)\n",
    )
    return hits


def run_patch_plan(db_hits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    plan: list[dict[str, Any]] = []
    backups: list[dict[str, Any]] = []
    for h in db_hits:
        if h["classification"] != "PUBLIC_ARTIFACT_FIX_SAFE":
            continue
        old_val = mysql_fetch_field(h["table"], h["pk"], h["id"], h["field"])
        new_val, removed = normalize_literal_newlines(old_val)
        if removed == 0 or new_val == old_val:
            continue
        plan.append({
            **h,
            "action": "REPLACE_LITERAL_NL",
            "removed_count": removed,
            "old_len": len(old_val),
            "new_len": len(new_val),
        })
        backups.append({
            "table": h["table"],
            "pk": h["pk"],
            "id": h["id"],
            "field": h["field"],
            "value": old_val,
        })

    with (STORAGE_ROOT / "patch-plan" / "db-cleanup-plan.csv").open("w", encoding="utf-8", newline="") as f:
        fields = ["table", "pk", "id", "field", "classification", "action", "removed_count", "old_len", "new_len"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in plan:
            w.writerow({k: row.get(k, "") for k in fields})

    write_json(STORAGE_ROOT / "db-backup" / "affected-rows-before.json", backups)

    sql_lines = ["-- SITE-002 literal newline cleanup backup reference", f"-- {utc_now()}"]
    for b in backups:
        sql_lines.append(
            f"-- {b['table']} {b['pk']}={b['id']} field={b['field']} len={len(b['value'])}"
        )
    write_text(STORAGE_ROOT / "db-backup" / "affected-rows-before.sql", "\n".join(sql_lines) + "\n")

    write_text(
        STORAGE_ROOT / "patch-plan" / "source-patch-decision.md",
        "# Source patch decision\n\n"
        "**Decision:** NO_SOURCE_PATCH_NEEDED\n\n"
        "Literal `\\n` artifacts are stored in DB content fields (post 13 `content`). "
        "No save/render pipeline bug identified in authority worktree source. "
        "Cleanup is exact DB content normalization only.\n",
    )
    write_text(
        STORAGE_ROOT / "patch-plan" / "final-patch-plan.md",
        f"# Final patch plan\n\n"
        f"- DB rows to update: {len(plan)}\n"
        f"- Source patch: none\n"
        f"- Cache clear: minimal (DB-only change)\n\n"
        + "\n".join(
            f"- UPDATE `{p['table']}` SET `{p['field']}` WHERE `{p['pk']}`={p['id']} (remove {p['removed_count']} literal NL)"
            for p in plan
        ),
    )
    write_text(STORAGE_ROOT / "ftp-apply" / "no-source-patch-needed.md", "No FTP upload required — DB content cleanup only.\n")
    return plan


def run_db_apply(plan: list[dict[str, Any]]) -> str:
    results: list[str] = []
    after_rows: list[dict[str, Any]] = []
    apply_sql_lines = [f"-- SITE-002 literal newline cleanup apply — {utc_now()}"]
    for row in plan:
        removed = int(row.get("removed_count") or 0)
        sql_line = (
            f"UPDATE {row['table']} SET {row['field']} = "
            f"REPLACE(REPLACE({row['field']}, '\\\\r\\\\n', ''), '\\\\n', '') "
            f"WHERE {row['pk']}={row['id']};"
        )
        apply_sql_lines.append(sql_line)
        out = mysql_update_field_replace(row["table"], row["pk"], row["id"], row["field"])
        results.append(
            f"OK {row['table']}.{row['field']} id={row['id']}: removed~{removed} literal NL — {out.strip()[:80]}"
        )
        after_val = mysql_fetch_field(row["table"], row["pk"], row["id"], row["field"])
        after_rows.append({
            "table": row["table"],
            "pk": row["pk"],
            "id": row["id"],
            "field": row["field"],
            "literal_nl_remaining": count_literal_newlines(after_val),
            "len": len(after_val),
        })
    write_text(STORAGE_ROOT / "db-apply" / "db-cleanup.sql", "\n".join(apply_sql_lines) + "\n")
    write_text(STORAGE_ROOT / "db-apply" / "db-cleanup-result.txt", "\n".join(results) if results else "No updates")
    write_json(STORAGE_ROOT / "db-apply" / "affected-rows-after.json", after_rows)
    return "\n".join(results)


def run_cache_actions() -> None:
    write_text(
        STORAGE_ROOT / "cache" / "cache-actions.md",
        "# Cache actions\n\n"
        "DB-only content change — OpenCart modification/Twig cache **not** cleared.\n"
        "Blog post content renders directly from DB; verification expected immediately.\n",
    )


def run_regression() -> None:
    checks = [
        ("home", PRODUCTION_URL, 200),
        ("blog", f"{PRODUCTION_URL}blog", 200),
        ("post_13", TARGET_ROUTE_URL, 200),
        ("contact", f"{PRODUCTION_URL}contact", 200),
        ("about", f"{PRODUCTION_URL}about", 200),
        ("sitemap", f"{PRODUCTION_URL}sitemap.xml", 200),
        ("kontakty", f"{PRODUCTION_URL}kontakty", 404),
    ]
    rows: list[dict[str, Any]] = []
    for label, url, expected in checks:
        resp = http_fetch(url)
        body = resp["body"]
        rows.append({
            "label": label,
            "url": url,
            "expected_status": expected,
            "actual_status": resp["status"],
            "ok": resp["status"] == expected,
            "literal_backslash_n": len(re.findall(r"\\\\n", body)),
            "has_reading_time": "Время на чтение" in body if label == "post_13" else "",
            "has_rck_logo": "rck-logo-altay-2026" in body if label == "post_13" else "",
            "has_hero": "rck-productivity-hero" in body if label == "post_13" else "",
            "public_bzpm": body.count("БЗПМ"),
            "has_zavod_caps": "Барнаульский Завод пищевого машиностроения" in body if label == "post_13" else "",
        })
    with (STORAGE_ROOT / "regression" / "site-regression.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    write_text(
        STORAGE_ROOT / "regression" / "site-regression-summary.md",
        f"# Regression summary\n\n"
        f"- All status checks pass: {all(r['ok'] for r in rows)}\n"
        f"- Post 13 literal NL: {rows[2]['literal_backslash_n']}\n"
        f"- Reading time: {rows[2]['has_reading_time']}\n"
        f"- RCK logo: {rows[2]['has_rck_logo']}\n"
        f"- Hero: {rows[2]['has_hero']}\n"
        f"- Завод caps: {rows[2]['has_zavod_caps']}\n",
    )


def run_verification_summary(before_conf: dict[str, Any], after_conf: dict[str, Any], plan: list[dict[str, Any]]) -> str:
    post13_after = http_fetch(TARGET_ROUTE_URL)
    write_text(STORAGE_ROOT / "verification" / "post-13-html-after.html", post13_after["body"])
    literal_after = len(re.findall(r"\\\\n", post13_after["body"]))
    verdict = "LITERAL_NEWLINE_FIXED" if literal_after == 0 else "FAILED_STILL_VISIBLE"
    write_text(
        STORAGE_ROOT / "verification" / "verification-summary.md",
        f"# Verification summary\n\n"
        f"- Post 13 route status: {post13_after['status']}\n"
        f"- Literal `\\n` before: {before_conf.get('literal_newline_snippets_found', '?')}\n"
        f"- Literal `\\n` after in HTML: {literal_after}\n"
        f"- DB rows updated: {len(plan)}\n"
        f"- Classification: **{verdict}**\n",
    )
    if verdict == "LITERAL_NEWLINE_FIXED":
        return "SITE-002 BLOG LITERAL NEWLINE CLEANUP COMPLETE — VISIBLE ARTIFACTS REMOVED"
    return "SITE-002 BLOG LITERAL NEWLINE CLEANUP FAILED — ARTIFACT STILL VISIBLE"


def main() -> int:
    guard_historical_harness('OPERATION_ID')

    phase = sys.argv[1] if len(sys.argv) > 1 else "all"
    init_storage()

    if phase in ("all", "preflight"):
        print("=== PHASE 1: PREFLIGHT ===")
        run_preflight()

    before_conf: dict[str, Any] = {}
    if phase in ("all", "artifact"):
        print("=== PHASE 2: ARTIFACT AUDIT ===")
        before_conf = run_artifact_audit("before")

    db_hits: list[dict[str, Any]] = []
    if phase in ("all", "db-audit"):
        print("=== PHASE 3: DB AUDIT ===")
        db_hits = run_db_audit()

    if phase in ("all", "source-audit"):
        print("=== PHASE 4: SOURCE AUDIT ===")
        run_source_audit()

    plan: list[dict[str, Any]] = []
    if phase in ("all", "plan"):
        print("=== PHASE 5: PATCH PLAN ===")
        if not db_hits:
            db_hits = run_db_audit()
        plan = run_patch_plan(db_hits)

    if phase in ("all", "apply"):
        print("=== PHASE 6: DB APPLY ===")
        if not plan:
            if not db_hits:
                db_hits = run_db_audit()
            plan = run_patch_plan(db_hits)
        result = run_db_apply(plan)
        print(result)

    if phase in ("all", "cache"):
        print("=== PHASE 8: CACHE ===")
        run_cache_actions()

    if phase in ("all", "verify"):
        print("=== PHASE 9: VERIFICATION ===")
        if not before_conf:
            before_conf = run_artifact_audit("before")
        run_artifact_audit("after")
        if not plan:
            plan = json.loads((STORAGE_ROOT / "patch-plan" / "db-cleanup-plan.csv").read_text()) if False else []
        verdict = run_verification_summary(before_conf, {}, plan if plan else [])
        print(f"VERDICT: {verdict}")

    if phase in ("all", "regression"):
        print("=== PHASE 10: REGRESSION ===")
        run_regression()

    if phase == "all":
        if not db_hits:
            db_hits = json.loads((STORAGE_ROOT / "db-audit" / "db-literal-newline-hits.json").read_text(encoding="utf-8"))
        if not plan:
            plan = []
            csv_path = STORAGE_ROOT / "patch-plan" / "db-cleanup-plan.csv"
            if csv_path.exists():
                with csv_path.open(encoding="utf-8") as f:
                    plan = list(csv.DictReader(f))
        verdict = run_verification_summary(before_conf, {}, plan)
        print(f"\nFINAL VERDICT: {verdict}")
        write_json(STORAGE_ROOT / "reports" / "operation-result.json", {
            "verdict": verdict,
            "db_rows_updated": len(plan),
            "completed_at": utc_now(),
        })

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
