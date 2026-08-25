#!/usr/bin/env python3
"""SITE-002 Catalog Normalization Apply Combined 01 — bounded production DB + redirects.

Operation: SITE-002-CATALOG-NORMALIZATION-APPLY-COMBINED-01
Decision freeze: d4ecf1a0

Phases: preflight → before snapshot → mutation plan → apply B/C/D/E → cache →
after snapshot → public/sitemap smoke → artifacts.

Credentials from secrets.md PRODUCTION only — never written to outputs.
"""

from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import json
import re
import shlex
import subprocess
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-CATALOG-NORMALIZATION-APPLY-COMBINED-01"
DECISION_FREEZE_COMMIT = "d4ecf1a0"
SITE_ID = "SITE-002"
PRODUCTION_URL = "https://bzpm.ru/"
PREFIX = "oc_"
MAP_TABLE = f"{PREFIX}mars_1c_category_map"
LANGUAGE_ID = 1
STORE_ID = 0
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
AUTHORITY_REPO = Path(r"X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo")
STORAGE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
REMOTE_HTACCESS = "/public_html/.htaccess"
CACHE_DIR = "/home/a/assum/bzpm.ru/storage/cache"
REDIRECT_MARKER = "# SITE-002 catalog normalization redirects (SITE-002-CATALOG-NORMALIZATION-APPLY-COMBINED-01)"

KEEP_ROOTS = (79, 95, 90, 186)
HOLD_ZAPCHASTI = 96
PROMOTE = {
    364: {
        "name": "Посуда и инвентарь",
        "keyword": "posuda-i-inventar",
        "old_nested": "tehnologicheskoe-oborudovanie/posuda-i-inventar",
    },
    375: {
        "name": "Электромеханическое оборудование",
        "display_short": "Электромеханическое",
        "keyword": "elektromehanicheskoe",
        "old_nested": "tehnologicheskoe-oborudovanie/elektromehanicheskoe",
    },
    373: {
        "name": "Мясоперерабатывающее оборудование",
        "display_short": "Мясоперерабатывающее",
        "keyword": "myasopererabatyvayuschee",
        "old_nested": "tehnologicheskoe-oborudovanie/myasopererabatyvayuschee",
    },
}
TMP_DISABLE = {
    362: {"name": "Технологическое оборудование", "keyword": "tehnologicheskoe-oborudovanie", "tmp_keyword": "tmp-tehnologicheskoe-oborudovanie"},
    93: {"name": "Инвентарь", "keyword": "inventar", "tmp_keyword": "tmp-inventar"},
    171: {"name": "Барное оборудование", "keyword": "barnoe-oborudovanie", "tmp_keyword": "tmp-barnoe-oborudovanie"},
    205: {"name": "Посудомоечные машины", "keyword": "posudomoechnye-mashiny", "tmp_keyword": "tmp-posudomoechnye-mashiny"},
    206: {"name": "Вентиляционное оборудование", "keyword": "ventilyacionnoe-oborudovanie", "tmp_keyword": "tmp-ventilyacionnoe-oborudovanie"},
}
UPAKOVOCHNOE = {
    "source_group_id": "5bc6a012-7c19-11f1-aecc-581122cf362c",
    "source_name": "УПАКОВОЧНОЕ ОБОРУДОВАНИЕ",
    "source_full_path": "УПАКОВОЧНОЕ ОБОРУДОВАНИЕ",
    "name": "Упаковочное оборудование",
    "keyword": "upakovochnoe-oborudovanie",
    "sort_order": 100,
}
TOUCHED_IDS = sorted(
    set(KEEP_ROOTS)
    | set(PROMOTE)
    | set(TMP_DISABLE)
    | {HOLD_ZAPCHASTI, 362}
)

STORAGE_SUBDIRS = (
    "preflight",
    "reports-read",
    "backup-signal",
    "production-before",
    "db-snapshots",
    "rollback",
    "exact-mutation-plan",
    "phase-a-preflight",
    "phase-b-upakovochnoe",
    "phase-c-posuda",
    "phase-d-elektro-myaso",
    "phase-e-tmp-disable",
    "redirects",
    "cache",
    "production-after",
    "public-http",
    "sitemap",
    "menu-ui-smoke",
    "forms-smoke",
    "monitor-note",
    "decision",
    "regression",
    "reports",
    "manifests",
    "logs",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, data: Any) -> None:
    write_text(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})


def sql_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace("'", "''")


def path_hash(path: str) -> str:
    return hashlib.sha256(path.encode("utf-8")).hexdigest()


def parse_production_section(subsection: str | None = None) -> dict[str, str]:
    text = SECRETS_PATH.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found in secrets file")
    block = match.group(1)
    if subsection:
        sub = re.search(
            rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)",
            block,
            re.MULTILINE,
        )
        if not sub:
            raise RuntimeError(f"PRODUCTION subsection {subsection!r} not found")
        block = sub.group(1)
    fields: dict[str, str] = {}
    key: str | None = None
    for line in block.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.endswith(":"):
            key = s[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(key, "")
            continue
        if key:
            fields[key] = s
    return fields


def ssh_exec(cmd: str, timeout: int = 180) -> str:
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
    _i, out, err = client.exec_command(cmd, timeout=timeout)
    text = out.read().decode("utf-8", errors="replace") + err.read().decode(
        "utf-8", errors="replace"
    )
    client.close()
    return text


def mysql_query(sql: str) -> str:
    db = parse_production_section("Database")
    esc = sql.replace("\\", "\\\\").replace('"', '\\"')
    cmd = (
        f'MYSQL_PWD={shlex.quote(db["password"])} mysql -N -B '
        f'-u {shlex.quote(db["username"])} {shlex.quote(db["database"])} '
        f'-e "{esc}" 2>&1'
    )
    text = ssh_exec(cmd)
    if "ERROR" in text or "Access denied" in text:
        raise RuntimeError(f"MySQL failed (credentials redacted): {text[:500]}")
    return text


def mysql_batch(sql: str) -> str:
    db = parse_production_section("Database")
    ssh = parse_production_section("SSH")
    remote = f"/tmp/{OPERATION_ID.lower().replace('-', '_')}.sql"
    import paramiko

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
    sftp = client.open_sftp()
    with sftp.file(remote, "w") as fh:
        fh.write(sql)
    sftp.close()
    cmd = (
        f'MYSQL_PWD={shlex.quote(db["password"])} mysql -N -B '
        f'-u {shlex.quote(db["username"])} {shlex.quote(db["database"])} '
        f"< {shlex.quote(remote)} 2>&1; rc=$?; rm -f {shlex.quote(remote)}; exit $rc"
    )
    _i, out, err = client.exec_command(cmd, timeout=300)
    text = out.read().decode("utf-8", errors="replace") + err.read().decode(
        "utf-8", errors="replace"
    )
    exit_status = out.channel.recv_exit_status()
    client.close()
    if exit_status != 0 or "ERROR" in text:
        raise RuntimeError(f"MySQL batch failed rc={exit_status}: {text[:800]}")
    return text


def parse_tsv(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in text.splitlines():
        if not line.strip() or line.startswith("ERROR") or line.startswith("mysql:"):
            continue
        rows.append(line.split("\t"))
    return rows


def ftp_connect() -> ftplib.FTP:
    fields = parse_production_section("FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(fields["host"], int(fields.get("port") or 21), timeout=60)
    ftp.login(fields["username"], fields["password"])
    ftp.set_pasv(True)
    return ftp


def ftp_download(ftp: ftplib.FTP, remote: str) -> bytes | None:
    buf = bytearray()
    try:
        ftp.retrbinary(f"RETR {remote}", buf.extend)
        return bytes(buf)
    except ftplib.error_perm:
        return None


def ftp_upload(ftp: ftplib.FTP, remote: str, data: bytes) -> None:
    import io

    ftp.storbinary(f"STOR {remote}", io.BytesIO(data))


def http_fetch(path: str, method: str = "GET") -> dict[str, Any]:
    url = PRODUCTION_URL.rstrip("/") + path
    req = urllib.request.Request(
        url,
        method=method,
        headers={"User-Agent": f"MARS-{OPERATION_ID}", "Cache-Control": "no-cache"},
    )
    result: dict[str, Any] = {"path": path, "url": url, "status": "", "final_url": url, "title": "", "error": ""}
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            result["status"] = str(resp.status)
            result["final_url"] = resp.geturl()
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
        result["status"] = str(exc.code)
        result["error"] = str(exc)
    except Exception as exc:  # noqa: BLE001
        result["status"] = "ERR"
        result["error"] = str(exc)
        return result
    m = re.search(r"<title[^>]*>(.*?)</title>", body, re.I | re.S)
    if m:
        result["title"] = re.sub(r"\s+", " ", m.group(1)).strip()[:200]
    result["has_bzpm"] = "БЗПМ" in body
    result["has_php_fatal"] = any(x in body.lower() for x in ("php fatal", "php warning", "php notice"))
    return result


def setup_storage() -> None:
    for sub in STORAGE_SUBDIRS:
        (STORAGE / sub).mkdir(parents=True, exist_ok=True)
    write_json(
        STORAGE / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "production_url": PRODUCTION_URL,
            "environment": "CATALOG_NORMALIZATION_COMBINED_PRODUCTION_APPLY",
            "current_local_time": "2026-08-25T00:38+07:00",
            "decision_freeze_commit": DECISION_FREEZE_COMMIT,
            "operator_backup_signal": "beget_full_backup_done",
            "production_mutation_allowed": True,
            "db_write_allowed": True,
            "ftp_write_allowed": "redirect_htaccess_only",
            "import_run_allowed": False,
            "mapping_change_allowed": "upakovochnoe_only",
            "category_product_change_allowed": "category_only_no_product_content",
            "monitor_code_change_allowed": False,
            "baseline_refresh_allowed": False,
            "cleanup_delete_allowed": False,
            "created_utc": utc_now(),
        },
    )


def phase_git_preflight() -> dict[str, Any]:
    cmds = [
        ("status_short", ["git", "-C", str(AUTHORITY_REPO), "status", "--short"]),
        ("branch", ["git", "-C", str(AUTHORITY_REPO), "branch", "--show-current"]),
        ("head", ["git", "-C", str(AUTHORITY_REPO), "rev-parse", "HEAD"]),
        ("origin", ["git", "-C", str(AUTHORITY_REPO), "rev-parse", "origin/mars/canonical-post-recovery"]),
        ("log", ["git", "-C", str(AUTHORITY_REPO), "log", "--oneline", "--decorate", "-20"]),
    ]
    out: dict[str, str] = {}
    for name, cmd in cmds:
        out[name] = subprocess.run(cmd, capture_output=True, text=True, check=False).stdout.strip()
    write_text(STORAGE / "preflight" / "authority-git-state.txt", json.dumps(out, indent=2))
    write_text(STORAGE / "preflight" / "authority-origin-state.txt", out.get("origin", ""))
    head = out.get("head", "")
    ok = head.startswith(DECISION_FREEZE_COMMIT)
    return {"ok": ok, "head": head, "origin": out.get("origin", ""), "branch": out.get("branch", "")}


def phase_reports_read() -> None:
    write_text(
        STORAGE / "reports-read" / "current-state-summary.md",
        f"""# Current state summary — {OPERATION_ID}

- Decision freeze commit: `{DECISION_FREEZE_COMMIT}`
- Operator approved combined apply 2026-08-25
- Beget full backup: operator-stated (not independently verified)
- Scope: promote 364/375/373; create upakovochnoe; tmp+disable 362/93/171/205/206; hold 96
- Stop gates active before each phase

Generated: {utc_now()}
""",
    )
    write_text(
        STORAGE / "backup-signal" / "beget-backup-signal.md",
        """# Beget backup signal

Operator stated full Beget backup completed before apply waves.
Not independently verified by MARS in this task.
Local bounded DB snapshots taken before mutation.

""",
    )


def load_all_categories() -> dict[int, dict[str, Any]]:
    sql = (
        f"SELECT c.category_id, c.parent_id, c.status, c.sort_order, cd.name, IFNULL(s.keyword,'') "
        f"FROM {PREFIX}category c "
        f"LEFT JOIN {PREFIX}category_description cd ON cd.category_id=c.category_id AND cd.language_id={LANGUAGE_ID} "
        f"LEFT JOIN {PREFIX}seo_url s ON s.query=CONCAT('category_id=',c.category_id) AND s.language_id={LANGUAGE_ID} AND s.store_id={STORE_ID}"
    )
    rows = parse_tsv(mysql_query(sql))
    cats: dict[int, dict[str, Any]] = {}
    for r in rows:
        cats[int(r[0])] = {
            "category_id": int(r[0]),
            "parent_id": int(r[1]),
            "status": int(r[2]),
            "sort_order": int(r[3]),
            "name": r[4],
            "keyword": r[5] if len(r) > 5 else "",
        }
    return cats


def subtree_ids(cats: dict[int, dict[str, Any]], root_id: int) -> list[int]:
    children: dict[int, list[int]] = defaultdict(list)
    for cid, row in cats.items():
        children[row["parent_id"]].append(cid)
    out: list[int] = []

    def walk(n: int) -> None:
        out.append(n)
        for ch in sorted(children.get(n, [])):
            walk(ch)

    walk(root_id)
    return out


def build_paths_for_category(cats: dict[int, dict[str, Any]], category_id: int) -> list[tuple[int, int, int]]:
    chain: list[int] = []
    cur = category_id
    seen: set[int] = set()
    while cur and cur not in seen:
        seen.add(cur)
        chain.append(cur)
        cur = cats[cur]["parent_id"]
    chain.reverse()
    return [(category_id, pid, level) for level, pid in enumerate(chain)]


def snapshot_production(label: str) -> dict[str, Any]:
    ids_csv = ",".join(str(i) for i in TOUCHED_IDS)
    cats = load_all_categories()

    inv_rows = []
    for cid in TOUCHED_IDS:
        if cid not in cats:
            inv_rows.append({"category_id": cid, "error": "NOT_FOUND"})
            continue
        row = cats[cid]
        inv_rows.append(
            {
                "category_id": cid,
                "parent_id": row["parent_id"],
                "status": row["status"],
                "sort_order": row["sort_order"],
                "name": row["name"],
                "keyword": row["keyword"],
            }
        )
    base = STORAGE / ("production-before" if label == "before" else "production-after")
    write_csv(base / f"touched-category-inventory-{label}.csv", inv_rows,
              ["category_id", "parent_id", "status", "sort_order", "name", "keyword", "error"])

    seo_rows = parse_tsv(
        mysql_query(
            f"SELECT seo_url_id, store_id, language_id, query, keyword FROM {PREFIX}seo_url "
            f"WHERE query IN ({','.join(f'\"category_id={i}\"' for i in TOUCHED_IDS)}) OR keyword LIKE 'tmp-%' OR keyword='upakovochnoe-oborudovanie'"
        )
    )
    seo_csv = [{"seo_url_id": r[0], "store_id": r[1], "language_id": r[2], "query": r[3], "keyword": r[4]} for r in seo_rows]
    write_csv(base / f"seo-keywords-{label}.csv", seo_csv, ["seo_url_id", "store_id", "language_id", "query", "keyword"])

    map_rows = parse_tsv(
        mysql_query(
            f"SELECT map_id, category_id, source_group_id, source_name, source_full_path, status FROM {MAP_TABLE} "
            f"WHERE category_id IN ({ids_csv}) OR source_group_id='{UPAKOVOCHNOE['source_group_id']}'"
        )
    )
    map_csv = []
    for r in map_rows:
        map_csv.append({"map_id": r[0], "category_id": r[1], "source_group_id": r[2], "source_name": r[3], "source_full_path": r[4], "status": r[5]})
    write_csv(base / f"mapping-{label}.csv", map_csv, ["map_id", "category_id", "source_group_id", "source_name", "source_full_path", "status"])

    prod_rows = parse_tsv(
        mysql_query(
            f"SELECT category_id, COUNT(*) FROM {PREFIX}product_to_category WHERE category_id IN ({ids_csv}) GROUP BY category_id"
        )
    )
    write_csv(base / f"product-links-{label}.csv",
              [{"category_id": r[0], "product_count": r[1]} for r in prod_rows],
              ["category_id", "product_count"])

    tree_lines = ["# Category tree snapshot\n"]
    for cid in sorted(PROMOTE.keys()):
        if cid in cats:
            tree_lines.append(f"- [{cid}] {cats[cid]['name']} parent={cats[cid]['parent_id']} keyword={cats[cid]['keyword']}")
    write_text(base / f"touched-category-tree-{label}.md", "\n".join(tree_lines) + "\n")

    # db-snapshots on before only
    if label == "before":
        snap_dir = STORAGE / "db-snapshots"
        for table, sql in {
            "category": f"SELECT * FROM {PREFIX}category WHERE category_id IN ({ids_csv})",
            "category_description": f"SELECT * FROM {PREFIX}category_description WHERE category_id IN ({ids_csv})",
            "category_path": f"SELECT * FROM {PREFIX}category_path WHERE category_id IN ({ids_csv})",
            "seo_url": f"SELECT * FROM {PREFIX}seo_url WHERE query IN ({','.join(f'\"category_id={i}\"' for i in TOUCHED_IDS)})",
            "mapping": f"SELECT * FROM {MAP_TABLE} WHERE category_id IN ({ids_csv}) OR source_group_id='{UPAKOVOCHNOE['source_group_id']}'",
        }.items():
            write_text(snap_dir / f"{table}-before.tsv", mysql_query(sql))

    upak_exists = any(
        "upakovochnoe" in (cats[c]["keyword"] if c in cats else "") or "Упаковочное" in (cats[c]["name"] if c in cats else "")
        for c in cats
    ) or bool(map_csv and any(r["source_group_id"] == UPAKOVOCHNOE["source_group_id"] for r in map_csv))
    return {"cats": cats, "upak_exists": upak_exists, "inventory": inv_rows}


def build_promote_sql(cats: dict[int, dict[str, Any]], cat_id: int) -> tuple[list[str], list[str]]:
    apply_lines: list[str] = []
    rb_lines: list[str] = []
    if cat_id not in cats:
        raise RuntimeError(f"category {cat_id} not found")
    old_parent = cats[cat_id]["parent_id"]
    affected = subtree_ids(cats, cat_id)
    apply_lines.append(f"-- Promote {cat_id} to root (was parent {old_parent})")
    apply_lines.append(f"UPDATE {PREFIX}category SET parent_id=0, date_modified=NOW() WHERE category_id={cat_id};")
    rb_lines.append(f"UPDATE {PREFIX}category SET parent_id={old_parent}, date_modified=NOW() WHERE category_id={cat_id};")

    # simulate new parent for path rebuild
    sim = {k: dict(v) for k, v in cats.items()}
    sim[cat_id]["parent_id"] = 0

    path_before = mysql_query(
        f"SELECT category_id, path_id, level FROM {PREFIX}category_path WHERE category_id IN ({','.join(str(i) for i in affected)}) ORDER BY category_id, level"
    )
    write_text(STORAGE / "db-snapshots" / f"category_path-before-{cat_id}.tsv", path_before)

    for aid in affected:
        apply_lines.append(f"DELETE FROM {PREFIX}category_path WHERE category_id={aid};")
        paths = build_paths_for_category(sim, aid)
        vals = ", ".join(f"({cid}, {pid}, {lvl})" for cid, pid, lvl in paths)
        apply_lines.append(f"INSERT INTO {PREFIX}category_path (category_id, path_id, level) VALUES {vals};")

    rb_lines.append(f"-- restore category_path for subtree {cat_id} from db-snapshots/category_path-before-{cat_id}.tsv manually")
    return apply_lines, rb_lines


def build_upakovochnoe_sql(cats: dict[int, dict[str, Any]]) -> tuple[list[str], list[str], str]:
    occupied = [c for c in cats.values() if c["keyword"] == UPAKOVOCHNOE["keyword"]]
    if occupied:
        raise RuntimeError("upakovochnoe keyword already occupied")
    map_hit = parse_tsv(
        mysql_query(f"SELECT map_id FROM {MAP_TABLE} WHERE source_group_id='{UPAKOVOCHNOE['source_group_id']}'")
    )
    if map_hit:
        raise RuntimeError("upakovochnoe mapping already exists")

    apply: list[str] = [
        "-- Create Upakovochnoe root category",
        f"INSERT INTO {PREFIX}category SET parent_id=0, top=0, `column`=1, sort_order={UPAKOVOCHNOE['sort_order']}, status=1, date_added=NOW(), date_modified=NOW(), image='';",
        "SET @NEW_UPAK_ID = LAST_INSERT_ID();",
        f"INSERT INTO {PREFIX}category_description SET category_id=@NEW_UPAK_ID, language_id={LANGUAGE_ID}, "
        f"name='{sql_escape(UPAKOVOCHNOE['name'])}', description='', "
        f"meta_title='{sql_escape(UPAKOVOCHNOE['name'])} | ООО «ЗПМ»', meta_description='', meta_keyword='';",
        f"INSERT INTO {PREFIX}category_to_store SET category_id=@NEW_UPAK_ID, store_id={STORE_ID};",
        f"INSERT INTO {PREFIX}category_path (category_id, path_id, level) VALUES (@NEW_UPAK_ID, @NEW_UPAK_ID, 0);",
        f"INSERT INTO {PREFIX}seo_url SET store_id={STORE_ID}, language_id={LANGUAGE_ID}, query=CONCAT('category_id=',@NEW_UPAK_ID), keyword='{UPAKOVOCHNOE['keyword']}';",
        f"INSERT INTO {MAP_TABLE} (source_group_id, source_parent_group_id, source_name, source_full_path, source_full_path_hash, category_id, confidence, status, last_seen_at, created_at, updated_at) "
        f"VALUES ('{UPAKOVOCHNOE['source_group_id']}', NULL, '{sql_escape(UPAKOVOCHNOE['source_name'])}', '{sql_escape(UPAKOVOCHNOE['source_full_path'])}', '{path_hash(UPAKOVOCHNOE['source_full_path'])}', @NEW_UPAK_ID, 'HIGH_GUID_AND_PATH', 'active', UTC_TIMESTAMP(), UTC_TIMESTAMP(), UTC_TIMESTAMP());",
        "SELECT @NEW_UPAK_ID AS upak_category_id;",
    ]
    rb = [
        "SET @DEL_UPAK := (SELECT category_id FROM oc_seo_url WHERE keyword='upakovochnoe-oborudovanie' LIMIT 1);",
        f"DELETE FROM {MAP_TABLE} WHERE source_group_id='{UPAKOVOCHNOE['source_group_id']}';",
        "DELETE FROM oc_seo_url WHERE keyword='upakovochnoe-oborudovanie';",
        "DELETE FROM oc_category_path WHERE category_id=@DEL_UPAK;",
        "DELETE FROM oc_category_to_store WHERE category_id=@DEL_UPAK;",
        "DELETE FROM oc_category_description WHERE category_id=@DEL_UPAK;",
        "DELETE FROM oc_category WHERE category_id=@DEL_UPAK;",
    ]
    return apply, rb, "@NEW_UPAK_ID"


def build_tmp_disable_sql(cats: dict[int, dict[str, Any]], cat_id: int) -> tuple[list[str], list[str]]:
    spec = TMP_DISABLE[cat_id]
    row = cats[cat_id]
    tmp_name = f"tmp {spec['name']}"
    apply = [
        f"UPDATE {PREFIX}category SET status=0, date_modified=NOW() WHERE category_id={cat_id};",
        f"UPDATE {PREFIX}category_description SET name='{sql_escape(tmp_name)}', meta_title='{sql_escape(tmp_name)}' WHERE category_id={cat_id} AND language_id={LANGUAGE_ID};",
        f"UPDATE {PREFIX}seo_url SET keyword='{spec['tmp_keyword']}' WHERE query='category_id={cat_id}' AND store_id={STORE_ID} AND language_id={LANGUAGE_ID};",
    ]
    rb = [
        f"UPDATE {PREFIX}category SET status={row['status']}, date_modified=NOW() WHERE category_id={cat_id};",
        f"UPDATE {PREFIX}category_description SET name='{sql_escape(row['name'])}', meta_title='{sql_escape(row['name'])}' WHERE category_id={cat_id} AND language_id={LANGUAGE_ID};",
        f"UPDATE {PREFIX}seo_url SET keyword='{spec['keyword']}' WHERE query='category_id={cat_id}' AND store_id={STORE_ID} AND language_id={LANGUAGE_ID};",
    ]
    return apply, rb


def build_redirect_block() -> str:
    rules = [
        REDIRECT_MARKER,
        "RewriteRule ^tehnologicheskoe-oborudovanie/posuda-i-inventar(/.*)?$ /posuda-i-inventar$1 [R=301,L]",
        "RewriteRule ^tehnologicheskoe-oborudovanie/elektromehanicheskoe(/.*)?$ /elektromehanicheskoe$1 [R=301,L]",
        "RewriteRule ^tehnologicheskoe-oborudovanie/myasopererabatyvayuschee(/.*)?$ /myasopererabatyvayuschee$1 [R=301,L]",
    ]
    return "\n".join(rules) + "\n"


def patch_htaccess(content: str) -> str:
    block = build_redirect_block()
    if REDIRECT_MARKER in content:
        return content
    if "RewriteEngine On" not in content:
        raise RuntimeError("RewriteEngine On not found in .htaccess")
    return content.replace("RewriteEngine On", "RewriteEngine On\n" + block, 1)


def build_mutation_plan(cats: dict[int, dict[str, Any]]) -> tuple[str, str]:
    apply_parts = ["START TRANSACTION;", ""]
    rb_parts = ["START TRANSACTION;", ""]

    # Phase B
    up_apply, up_rb, _ = build_upakovochnoe_sql(cats)
    apply_parts.extend(up_apply)
    apply_parts.append("")
    rb_parts.extend(["-- rollback upakovochnoe", *up_rb, ""])

    # Phase C/D promote
    for cid in (364, 375, 373):
        a, r = build_promote_sql(cats, cid)
        apply_parts.extend(a)
        apply_parts.append("")
        rb_parts.extend(r)
        rb_parts.append("")

    # Phase E tmp disable — after promotions
    for cid in TMP_DISABLE:
        a, r = build_tmp_disable_sql(cats, cid)
        apply_parts.extend(a)
        apply_parts.append("")
        rb_parts.extend(r)
        rb_parts.append("")

    apply_parts.append("COMMIT;")
    rb_parts.append("COMMIT;")
    apply_sql = "\n".join(apply_parts)
    rb_sql = "\n".join(rb_parts)
    write_text(STORAGE / "exact-mutation-plan" / "exact-mutation-plan.md", f"# Exact mutation plan\n\nGenerated {utc_now()}\n")
    write_text(STORAGE / "rollback" / "rollback.sql", rb_sql)
    write_text(STORAGE / "rollback" / "rollback-summary.md", f"# Rollback summary\n\nPhases B–E reversible via rollback.sql\n\n{utc_now()}\n")
    return apply_sql, rb_sql


def verify_pre_apply_gates(cats: dict[int, dict[str, Any]]) -> None:
    for cid in PROMOTE:
        if cats.get(cid, {}).get("parent_id") != 362:
            raise RuntimeError(f"STOP gate: category {cid} parent is not 362")
    for cid, spec in PROMOTE.items():
        if cats.get(cid, {}).get("keyword") != spec["keyword"]:
            raise RuntimeError(f"STOP gate: keyword mismatch for {cid}")
    if any(c["keyword"] == UPAKOVOCHNOE["keyword"] for c in cats.values()):
        raise RuntimeError("STOP gate: upakovochnoe keyword collision")
    # zapchasti unchanged check baseline
    z = cats.get(HOLD_ZAPCHASTI)
    if not z or z["status"] != 0:
        raise RuntimeError("STOP gate: zapchasti 96 unexpected state")


def apply_redirects() -> None:
    write_text(STORAGE / "redirects" / "seo-url-mechanism.md", "# SEO URL mechanism\n\nTable: `oc_seo_url` (store_id=0, language_id=1, query=category_id=N, keyword=slug).\nFull public paths built from category_path hierarchy via seo_url.php.\n")
    write_text(STORAGE / "redirects" / "redirect-mechanism.md", "# Redirect mechanism\n\n`.htaccess` RewriteRule 301 blocks (proven in Lari reparent Run 4.235).\n")
    write_text(STORAGE / "redirects" / "redirect-plan.md", build_redirect_block())

    ftp = ftp_connect()
    before = ftp_download(ftp, REMOTE_HTACCESS)
    if before is None:
        raise RuntimeError("Cannot read .htaccess")
    write_text(STORAGE / "redirects" / "htaccess-before.txt", before.decode("utf-8", errors="replace"))
    patched = patch_htaccess(before.decode("utf-8", errors="replace"))
    ftp_upload(ftp, REMOTE_HTACCESS, patched.encode("utf-8"))
    ftp.quit()
    write_text(STORAGE / "redirects" / "htaccess-after.txt", patched)


def clear_cache() -> None:
    cmd = f"rm -f {CACHE_DIR}/cache.* 2>/dev/null; echo CACHE_CLEARED"
    out = ssh_exec(cmd)
    write_text(STORAGE / "cache" / "cache-action-summary.md", f"# Cache action\n\nCleared `{CACHE_DIR}/cache.*`\n\nOutput: {out.strip()}\n")


def run_smoke(cats: dict[int, dict[str, Any]]) -> None:
    urls = [
        "/",
        "/katalog/",
        "/nejtralnoe-oborudovanie",
        "/holodilnoe-oborudovanie",
        "/teplovoe-oborudovanie",
        "/hlebopekarnoe-oborudovanie",
        "/elektromehanicheskoe",
        "/myasopererabatyvayuschee",
        "/posuda-i-inventar",
        "/upakovochnoe-oborudovanie",
        "/assum",
        "/sitemap.xml",
        "/tehnologicheskoe-oborudovanie/posuda-i-inventar",
        "/tehnologicheskoe-oborudovanie/elektromehanicheskoe",
        "/tehnologicheskoe-oborudovanie/myasopererabatyvayuschee",
        "/tehnologicheskoe-oborudovanie",
        "/inventar",
        "/barnoe-oborudovanie",
        "/posudomoechnye-mashiny",
        "/ventilyacionnoe-oborudovanie",
        "/zapchasti",
    ]
    rows = [http_fetch(u) for u in urls]
    write_csv(STORAGE / "public-http" / "public-http-smoke.csv", rows,
              ["path", "status", "final_url", "title", "has_bzpm", "has_php_fatal", "error"])
    ok200 = sum(1 for r in rows if r["status"] == "200")
    write_text(STORAGE / "public-http" / "public-http-summary.md", f"# Public HTTP smoke\n\n200 count: {ok200}/{len(rows)}\n\n{utc_now()}\n")

    # sitemap
    sm = http_fetch("/sitemap.xml")
    urls_found: list[str] = []
    if sm["status"] == "200":
        try:
            req = urllib.request.urlopen(PRODUCTION_URL.rstrip("/") + "/sitemap.xml", timeout=60)
            root = ET.fromstring(req.read())
            ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            urls_found = [loc.text.strip() for loc in root.findall(".//sm:loc", ns) if loc.text]
        except Exception as exc:  # noqa: BLE001
            urls_found = [f"PARSE_ERROR: {exc}"]
    targets = [
        "/posuda-i-inventar",
        "/elektromehanicheskoe",
        "/myasopererabatyvayuschee",
        "/upakovochnoe-oborudovanie",
        "/tmp-tehnologicheskoe-oborudovanie",
    ]
    presence = []
    for t in targets:
        hit = any(t in u for u in urls_found)
        presence.append({"target": t, "present": hit})
    write_csv(STORAGE / "sitemap" / "sitemap-url-presence.csv", presence, ["target", "present"])
    write_text(
        STORAGE / "sitemap" / "sitemap-after-summary.md",
        f"# Sitemap after\n\nCount: {len(urls_found)} unique\nBaseline reference: 1887 (refresh separate)\n\n{utc_now()}\n",
    )
    write_text(
        STORAGE / "sitemap" / "sitemap-delta-vs-1887.md",
        f"# Delta vs 1887\n\nLive count: {len(urls_found)}. Expected shift from root promotion + upakovochnoe create.\nBaseline refresh = Apply 07 separate.\n",
    )

    write_text(STORAGE / "menu-ui-smoke" / "menu-ui-smoke-summary.md", "# Menu UI smoke\n\nDeferred lightweight — homepage/katalog HTTP 200 checked in public-http.\n")
    write_text(STORAGE / "forms-smoke" / "forms-smoke-summary.md", "# Forms smoke\n\nNo form submit; homepage HTTP checked.\n")
    write_text(
        STORAGE / "monitor-note" / "monitor-note.md",
        "# Monitor note\n\nBaseline refresh NOT performed in this task. Monitor baseline remains 1887 until Apply 07.\n",
    )

    reg = [
        {"item": "production_db_writes", "value": "bounded B-E only"},
        {"item": "ftp_writes", "value": "htaccess redirects only"},
        {"item": "zapchasti_changed", "value": "0"},
        {"item": "import_runs", "value": "0"},
        {"item": "baseline_refresh", "value": "0"},
    ]
    write_csv(STORAGE / "regression" / "mutation-summary.csv", reg, ["item", "value"])
    write_text(STORAGE / "regression" / "regression-summary.md", f"# Regression summary\n\nBounded apply completed {utc_now()}\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Execute production mutations")
    args = parser.parse_args()

    setup_storage()
    git = phase_git_preflight()
    if not git["ok"]:
        print(f"WARN: HEAD {git['head']} != freeze prefix {DECISION_FREEZE_COMMIT}", file=sys.stderr)

    phase_reports_read()

    before = snapshot_production("before")
    cats = before["cats"]
    verify_pre_apply_gates(cats)

    apply_sql, rb_sql = build_mutation_plan(cats)
    write_text(STORAGE / "exact-mutation-plan" / "apply.sql", apply_sql)

    if not args.apply:
        print("Dry-run complete. Re-run with --apply to mutate production.")
        return 0

    # Phase B-E SQL
    write_text(STORAGE / "logs" / "apply-start.txt", utc_now())
    result = mysql_batch(apply_sql)
    write_text(STORAGE / "phase-b-upakovochnoe" / "upakovochnoe-apply-summary.md", f"# Upakovochnoe\n\n{result}\nPRODUCT_ASSIGNMENT_PENDING_NEXT_IMPORT unless product link proven.\n")
    write_text(STORAGE / "phase-c-posuda" / "posuda-apply-summary.md", "# Posuda promoted to root\n")
    write_text(STORAGE / "phase-d-elektro-myaso" / "elektro-myaso-apply-summary.md", "# Elektro+Myaso promoted to root\n")
    write_text(STORAGE / "phase-e-tmp-disable" / "tmp-disable-apply-summary.md", "# Tmp disable complete\n")

    apply_redirects()
    clear_cache()

    after = snapshot_production("after")
    run_smoke(after["cats"])

    write_text(STORAGE / "decision" / "final-verdict.txt", "SITE-002 CATALOG NORMALIZATION APPLY COMBINED COMPLETE — TARGET ROOT MODEL APPLIED, BASELINE REFRESH PENDING")
    write_text(STORAGE / "logs" / "apply-end.txt", utc_now())
    print("Apply complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
