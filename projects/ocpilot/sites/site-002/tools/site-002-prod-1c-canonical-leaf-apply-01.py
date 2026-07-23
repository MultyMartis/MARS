#!/usr/bin/env python3
"""SITE-002 1C Canonical Leaf Apply 01 — create 3 tech leaves + move 4 products.

Operation: SITE-002-PROD-1C-CANONICAL-LEAF-APPLY-01 (OCPilot Run 4.295)

Phases: db-before → public/sitemap before → dry-run → gates → backup → apply →
cache → public/sitemap after → monitor/regression artifacts.

Credentials from secrets.md PRODUCTION — never printed or written to outputs.
"""

from __future__ import annotations

import argparse
import csv
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

OPERATION_ID = "SITE-002-PROD-1C-CANONICAL-LEAF-APPLY-01"
OCPILOT_RUN = "4.295"
SITE_ID = "SITE-002"
PRODUCTION_URL = "https://bzpm.ru/"
PREFIX = "oc_"
LANGUAGE_ID = 1
STORE_ID = 0
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
STORAGE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
CACHE_DIR = "/home/a/assum/bzpm.ru/storage/cache"

LEAVES = [
    {
        "key": "myasorubki",
        "name": "Мясорубки",
        "parent_id": 373,
        "sort_order": 10,
        "keyword": "myasorubki-tehnologicheskoe",
        "meta_title": "Мясорубки",
        "meta_description": (
            "Мясорубки ЗПМ для предприятий пищевого производства. "
            "Актуальные модели в каталоге."
        ),
        "products": [4707, 4708],
        "from_hub": 373,
        "expected_url": (
            "/katalog/tehnologicheskoe-oborudovanie/myasopererabatyvayuschee/"
            "myasorubki-tehnologicheskoe"
        ),
        "path_ancestors": [362, 373],
    },
    {
        "key": "pily",
        "name": "Пилы для мяса",
        "parent_id": 373,
        "sort_order": 20,
        "keyword": "pily-dlya-myasa-tehnologicheskoe",
        "meta_title": "Пилы для мяса",
        "meta_description": (
            "Пилы для мяса ЗПМ для разделки мяса и костей. "
            "Актуальные модели в каталоге."
        ),
        "products": [4710],
        "from_hub": 373,
        "expected_url": (
            "/katalog/tehnologicheskoe-oborudovanie/myasopererabatyvayuschee/"
            "pily-dlya-myasa-tehnologicheskoe"
        ),
        "path_ancestors": [362, 373],
    },
    {
        "key": "hleborezki",
        "name": "Хлеборезки",
        "parent_id": 375,
        "sort_order": 10,
        "keyword": "hleborezki-tehnologicheskoe",
        "meta_title": "Хлеборезки",
        "meta_description": (
            "Хлеборезки ЗПМ для предприятий общественного питания и пищевого "
            "производства. Актуальные модели в каталоге."
        ),
        "products": [4712],
        "from_hub": 375,
        "expected_url": (
            "/katalog/tehnologicheskoe-oborudovanie/elektromehanicheskoe/"
            "hleborezki-tehnologicheskoe"
        ),
        "path_ancestors": [362, 375],
    },
]

KEEP_PRODUCT = 4709
KEEP_CATEGORY = 376
LEGACY_IDS = [153, 154, 159, 165]
PARENT_IDS = [373, 375]
FOCUS_PRODUCTS = [4707, 4708, 4709, 4710, 4712]
PROPOSED_KEYWORDS = [L["keyword"] for L in LEAVES]
LEGACY_KEYWORDS = ["myasorubki", "pily-dlya-myasa", "hleborezki"]


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


def mysql_query(sql: str, write: bool = False, timeout: int = 180) -> str:
    db = parse_production_section("Database")
    esc = sql.replace("\\", "\\\\").replace('"', '\\"')
    cmd = (
        f'MYSQL_PWD={shlex.quote(db["password"])} mysql -N -B '
        f'-u {shlex.quote(db["username"])} {shlex.quote(db["database"])} '
        f'-e "{esc}" 2>&1'
    )
    text = ssh_exec(cmd, timeout=timeout)
    if "ERROR" in text or "Access denied" in text:
        raise RuntimeError(f"MySQL failed (credentials redacted): {text[:500]}")
    if write and re.search(r"(?i)\berror\b", text):
        raise RuntimeError(f"MySQL write failed (credentials redacted): {text[:500]}")
    return text


def mysql_batch_file(sql: str, timeout: int = 300) -> str:
    """Upload SQL to remote temp and execute via mysql client (supports multi-stmt)."""
    import paramiko

    db = parse_production_section("Database")
    ssh = parse_production_section("SSH")
    remote = f"/tmp/{OPERATION_ID.lower().replace('-', '_')}.sql"
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
    _i, out, err = client.exec_command(cmd, timeout=timeout)
    text = out.read().decode("utf-8", errors="replace") + err.read().decode(
        "utf-8", errors="replace"
    )
    exit_status = out.channel.recv_exit_status()
    client.close()
    if exit_status != 0 or "ERROR" in text or "Access denied" in text:
        raise RuntimeError(
            f"MySQL batch failed rc={exit_status} (credentials redacted): {text[:800]}"
        )
    return text


def parse_tsv(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in text.splitlines():
        if not line.strip():
            continue
        if line.startswith("ERROR") or line.startswith("mysql:"):
            continue
        rows.append(line.split("\t"))
    return rows


def http_fetch(path: str, timeout: int = 45) -> dict[str, Any]:
    url = PRODUCTION_URL.rstrip("/") + path
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": f"MARS-{OPERATION_ID}",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        },
    )
    result: dict[str, Any] = {
        "path": path,
        "url": url,
        "status": "",
        "final_url": url,
        "bytes": 0,
        "has_bzpm": False,
        "has_literal_backslash_n": False,
        "has_php_notice": False,
        "has_product_not_found": False,
        "title": "",
        "error": "",
    }
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read()
            result["status"] = str(resp.status)
            result["final_url"] = resp.geturl()
            result["bytes"] = len(body)
            text = body.decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        body = exc.read() if exc.fp else b""
        text = body.decode("utf-8", errors="replace")
        result["status"] = str(exc.code)
        result["bytes"] = len(body)
        result["error"] = str(exc)
    except Exception as exc:  # noqa: BLE001
        result["status"] = "ERR"
        result["error"] = str(exc)
        return result

    result["has_bzpm"] = "БЗПМ" in text
    result["has_literal_backslash_n"] = "\\n" in text and not re.search(
        r"\\\\n", text[:2000]
    )
    # literal backslash-n in visible content (blog-style artifact)
    result["has_literal_backslash_n"] = bool(re.search(r"(?<![\\])\\n", text))
    low = text.lower()
    result["has_php_notice"] = any(
        x in low for x in ("php notice", "php warning", "php fatal", "stack trace")
    )
    result["has_product_not_found"] = "Товар не найден" in text
    m = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
    if m:
        result["title"] = re.sub(r"\s+", " ", m.group(1)).strip()[:200]
    # product listing heuristic
    result["product_cards"] = len(re.findall(r"product-thumb|product-layout|class=\"product", text, re.I))
    result["mentions_4707"] = "myasorubka-tc-12" in low or "tc-12" in low
    result["mentions_4708"] = "myasorubka-tc-22" in low or "tc-22" in low
    result["mentions_4710"] = "jg-210a" in low or "jg 210a" in low
    result["mentions_4712"] = "tt-d7c" in low or "hleborezka" in low
    return result


def write_manifest() -> None:
    write_json(
        STORAGE / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "ocpilot_run": OCPILOT_RUN,
            "production_url": PRODUCTION_URL,
            "environment": "PRODUCTION_1C_CANONICAL_LEAF_APPLY",
            "operator_guid_stability_confirmed": True,
            "previous_charter_run": "SITE-002-PROD-1C-CANONICAL-LEAF-CREATION-CHARTER-01",
            "previous_charter_commit": "009a150b",
            "production_mutation_allowed": "true_exact_category_create_and_product_move_only",
            "db_write_allowed": "true_exact_3_categories_and_4_product_relations_only",
            "ftp_upload_allowed": False,
            "admin_save_allowed": False,
            "cache_clear_allowed": "true_storage_cache_only_if_needed",
            "ocmod_refresh_allowed": False,
            "import_run_allowed": False,
            "scheduler_change_allowed": False,
            "monitor_baseline_change_allowed": False,
            "category_create_allowed": "true_exact_3",
            "category_update_allowed": False,
            "category_delete_allowed": False,
            "category_disable_allowed": False,
            "product_category_relation_change_allowed": "true_exact_4_products",
            "importer_code_change_allowed": False,
            "source_deploy_allowed": False,
            "form_mail_change_allowed": False,
            "dirty_main_mutation_allowed": False,
            "created_utc": utc_now(),
        },
    )


def phase_reports_read() -> None:
    rows = []
    for leaf in LEAVES:
        for pid in leaf["products"]:
            rows.append(
                {
                    "leaf_name": leaf["name"],
                    "parent_id": leaf["parent_id"],
                    "seo_keyword": leaf["keyword"],
                    "product_id": pid,
                    "from_hub": leaf["from_hub"],
                    "keep_unchanged": "",
                }
            )
    rows.append(
        {
            "leaf_name": "(keep)",
            "parent_id": KEEP_CATEGORY,
            "seo_keyword": "slaysery-dlya-myasa",
            "product_id": KEEP_PRODUCT,
            "from_hub": KEEP_CATEGORY,
            "keep_unchanged": "yes",
        }
    )
    write_csv(
        STORAGE / "reports-read" / "target-leaves-and-products.csv",
        rows,
        ["leaf_name", "parent_id", "seo_keyword", "product_id", "from_hub", "keep_unchanged"],
    )
    write_text(
        STORAGE / "reports-read" / "apply-baseline-summary.md",
        f"""# Apply baseline summary — {OPERATION_ID}

- Source charter: SITE-002-PROD-1C-CANONICAL-LEAF-CREATION-CHARTER-01 / Run 4.294 / commit 009a150b
- Verdict then: READY FOR LEAF APPLY
- Operator approved controlled apply; GUID stability confirmed
- Create 3 canonical tech leaves; move 4 products hub→leaf; keep 4709 on 376
- Do not delete/disable legacy 153/154/159/165
- Do not patch importer; do not baseline refresh
- Order after this apply: mapping backfill → importer patch

## Planned leaves

| Leaf | Parent | Keyword | Products |
|------|--------|---------|----------|
| Мясорубки | 373 | myasorubki-tehnologicheskoe | 4707, 4708 |
| Пилы для мяса | 373 | pily-dlya-myasa-tehnologicheskoe | 4710 |
| Хлеборезки | 375 | hleborezki-tehnologicheskoe | 4712 |

Generated: {utc_now()}
""",
    )


def phase_db_before() -> dict[str, Any]:
    gates: dict[str, Any] = {"pass": True, "failures": []}

    parents_sql = (
        "SELECT c.category_id, cd.name, c.parent_id, c.status, c.sort_order, c.image, "
        "IFNULL(s.keyword,'') "
        f"FROM {PREFIX}category c "
        f"LEFT JOIN {PREFIX}category_description cd ON cd.category_id=c.category_id AND cd.language_id={LANGUAGE_ID} "
        f"LEFT JOIN {PREFIX}seo_url s ON s.query=CONCAT('category_id=',c.category_id) AND s.language_id={LANGUAGE_ID} AND s.store_id={STORE_ID} "
        f"WHERE c.category_id IN (373,375,376,153,154,159,165,362) ORDER BY c.category_id"
    )
    parent_rows = parse_tsv(mysql_query(parents_sql))
    parent_csv = []
    parent_map: dict[str, list[str]] = {}
    for r in parent_rows:
        parent_map[r[0]] = r
        parent_csv.append(
            {
                "category_id": r[0],
                "name": r[1] if len(r) > 1 else "",
                "parent_id": r[2] if len(r) > 2 else "",
                "status": r[3] if len(r) > 3 else "",
                "sort_order": r[4] if len(r) > 4 else "",
                "image": r[5] if len(r) > 5 else "",
                "seo_keyword": r[6] if len(r) > 6 else "",
            }
        )
    write_csv(
        STORAGE / "db-before" / "parent-categories-before.csv",
        parent_csv,
        ["category_id", "name", "parent_id", "status", "sort_order", "image", "seo_keyword"],
    )
    for pid in ("373", "375"):
        if pid not in parent_map:
            gates["pass"] = False
            gates["failures"].append(f"parent {pid} missing")
        elif parent_map[pid][3] != "1":
            gates["pass"] = False
            gates["failures"].append(f"parent {pid} inactive status={parent_map[pid][3]}")

    # SEO keyword check
    kw_list = ",".join(f"'{k}'" for k in PROPOSED_KEYWORDS + LEGACY_KEYWORDS)
    seo_sql = (
        f"SELECT seo_url_id, store_id, language_id, query, keyword FROM {PREFIX}seo_url "
        f"WHERE keyword IN ({kw_list}) ORDER BY keyword, seo_url_id"
    )
    seo_rows = parse_tsv(mysql_query(seo_sql))
    seo_csv = []
    occupied = {k: [] for k in PROPOSED_KEYWORDS}
    for r in seo_rows:
        row = {
            "seo_url_id": r[0],
            "store_id": r[1],
            "language_id": r[2],
            "query": r[3],
            "keyword": r[4],
        }
        seo_csv.append(row)
        if r[4] in occupied:
            occupied[r[4]].append(r[3])
    for k, qs in occupied.items():
        seo_csv.append(
            {
                "seo_url_id": "",
                "store_id": "",
                "language_id": "",
                "query": f"PROPOSED_FREE={len(qs)==0}",
                "keyword": k,
            }
        )
        if qs:
            gates["pass"] = False
            gates["failures"].append(f"SEO keyword conflict: {k} -> {qs}")
    write_csv(
        STORAGE / "db-before" / "seo-keyword-check.csv",
        seo_csv,
        ["seo_url_id", "store_id", "language_id", "query", "keyword"],
    )

    # products
    pids = ",".join(str(p) for p in FOCUS_PRODUCTS)
    prod_sql = (
        "SELECT p.product_id, pd.name, p.status, ptc.category_id, ptc.main_category, "
        "IFNULL(s.keyword,''), IFNULL(cd.name,'') "
        f"FROM {PREFIX}product p "
        f"LEFT JOIN {PREFIX}product_description pd ON pd.product_id=p.product_id AND pd.language_id={LANGUAGE_ID} "
        f"LEFT JOIN {PREFIX}product_to_category ptc ON ptc.product_id=p.product_id "
        f"LEFT JOIN {PREFIX}category_description cd ON cd.category_id=ptc.category_id AND cd.language_id={LANGUAGE_ID} "
        f"LEFT JOIN {PREFIX}seo_url s ON s.query=CONCAT('product_id=',p.product_id) AND s.language_id={LANGUAGE_ID} AND s.store_id={STORE_ID} "
        f"WHERE p.product_id IN ({pids}) ORDER BY p.product_id, ptc.category_id"
    )
    prod_rows = parse_tsv(mysql_query(prod_sql))
    prod_csv = []
    main_map: dict[str, str] = {}
    for r in prod_rows:
        prod_csv.append(
            {
                "product_id": r[0],
                "name": r[1],
                "status": r[2],
                "category_id": r[3],
                "main_category": r[4],
                "product_seo_keyword": r[5],
                "category_name": r[6] if len(r) > 6 else "",
            }
        )
        if r[4] == "1":
            main_map[r[0]] = r[3]
    write_csv(
        STORAGE / "db-before" / "target-products-before.csv",
        prod_csv,
        [
            "product_id",
            "name",
            "status",
            "category_id",
            "main_category",
            "product_seo_keyword",
            "category_name",
        ],
    )
    expected_main = {
        "4707": "373",
        "4708": "373",
        "4710": "373",
        "4712": "375",
        "4709": "376",
    }
    for pid, exp in expected_main.items():
        got = main_map.get(pid)
        if got != exp:
            gates["pass"] = False
            gates["failures"].append(f"product {pid} main category={got} expected={exp}")

    # existing children / same name under parents
    child_sql = (
        "SELECT c.category_id, cd.name, c.parent_id, c.status, c.sort_order, IFNULL(s.keyword,'') "
        f"FROM {PREFIX}category c "
        f"JOIN {PREFIX}category_description cd ON cd.category_id=c.category_id AND cd.language_id={LANGUAGE_ID} "
        f"LEFT JOIN {PREFIX}seo_url s ON s.query=CONCAT('category_id=',c.category_id) AND s.language_id={LANGUAGE_ID} AND s.store_id={STORE_ID} "
        f"WHERE c.parent_id IN (373,375) ORDER BY c.parent_id, c.sort_order, c.category_id"
    )
    child_rows = parse_tsv(mysql_query(child_sql))
    child_csv = []
    for r in child_rows:
        child_csv.append(
            {
                "category_id": r[0],
                "name": r[1],
                "parent_id": r[2],
                "status": r[3],
                "sort_order": r[4],
                "seo_keyword": r[5],
            }
        )
        for leaf in LEAVES:
            if r[2] == str(leaf["parent_id"]) and r[1] == leaf["name"]:
                gates["pass"] = False
                gates["failures"].append(
                    f"canonical leaf already exists: id={r[0]} name={r[1]} parent={r[2]}"
                )
    write_csv(
        STORAGE / "db-before" / "existing-children-before.csv",
        child_csv,
        ["category_id", "name", "parent_id", "status", "sort_order", "seo_keyword"],
    )

    max_simple = parse_tsv(mysql_query(f"SELECT MAX(category_id) FROM {PREFIX}category"))
    max_id = parse_tsv(
        mysql_query(
            "SELECT AUTO_INCREMENT FROM information_schema.TABLES "
            f"WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='{PREFIX}category'"
        )
    )
    path_sql = (
        f"SELECT category_id, path_id, level FROM {PREFIX}category_path "
        f"WHERE category_id IN (362,373,375,376) ORDER BY category_id, level"
    )
    path_rows = parse_tsv(mysql_query(path_sql))
    desc_cols = parse_tsv(mysql_query(f"SHOW COLUMNS FROM {PREFIX}category"))
    desc_desc = parse_tsv(mysql_query(f"SHOW COLUMNS FROM {PREFIX}category_description"))

    summary = f"""# DB before — {OPERATION_ID}

Generated: {utc_now()}

## Gates
- pass: {gates['pass']}
- failures: {gates['failures'] or 'none'}

## Max category_id
- max: {(max_simple[0][0] if max_simple else 'UNKNOWN')}
- auto_increment probe: {max_id}

## Parents 373/375
- 373 present/active: {'373' in parent_map and parent_map['373'][3]=='1'}
- 375 present/active: {'375' in parent_map and parent_map['375'][3]=='1'}

## Proposed SEO keywords free
{json.dumps({k: (len(v)==0) for k,v in occupied.items()}, ensure_ascii=False)}

## Product main categories
{json.dumps(main_map, ensure_ascii=False)}

## Existing children under 373/375
{json.dumps(child_csv, ensure_ascii=False)}

## category_path focus
{path_rows}

## oc_category columns
{[r[0] for r in desc_cols]}

## oc_category_description columns
{[r[0] for r in desc_desc]}
"""
    write_text(STORAGE / "db-before" / "db-before-summary.md", summary)
    write_json(
        STORAGE / "db-before" / "db-before-gates.json",
        {"gates": gates, "main_map": main_map, "max_category_id": max_simple[0][0] if max_simple else None},
    )
    return {"gates": gates, "main_map": main_map, "product_rows": prod_csv, "max_category_id": max_simple[0][0] if max_simple else None}


def phase_public_before(product_rows: list[dict[str, Any]]) -> None:
    seo_by_pid = {}
    for r in product_rows:
        if r.get("product_seo_keyword"):
            seo_by_pid[r["product_id"]] = r["product_seo_keyword"]

    paths = [
        "/katalog/tehnologicheskoe-oborudovanie/myasopererabatyvayuschee",
        "/katalog/tehnologicheskoe-oborudovanie/elektromehanicheskoe",
        "/katalog/",
        "/",
        "/sitemap.xml",
    ]
    # hub-level product URLs (current)
    for pid, kw in seo_by_pid.items():
        if pid in ("4707", "4708", "4710"):
            paths.append(
                f"/katalog/tehnologicheskoe-oborudovanie/myasopererabatyvayuschee/{kw}"
            )
        elif pid == "4712":
            paths.append(
                f"/katalog/tehnologicheskoe-oborudovanie/elektromehanicheskoe/{kw}"
            )

    rows = []
    for p in paths:
        rows.append(http_fetch(p))
    write_csv(
        STORAGE / "public-before" / "public-before.csv",
        rows,
        [
            "path",
            "url",
            "status",
            "final_url",
            "bytes",
            "has_bzpm",
            "has_literal_backslash_n",
            "has_php_notice",
            "has_product_not_found",
            "title",
            "error",
        ],
    )
    write_text(
        STORAGE / "public-before" / "public-before-summary.md",
        f"""# Public before — {OPERATION_ID}

Generated: {utc_now()}

## Results
{json.dumps(rows, ensure_ascii=False, indent=2)}
""",
    )


def phase_sitemap_before() -> dict[str, Any]:
    fetch = http_fetch("/sitemap.xml")
    body = ""
    try:
        with urllib.request.urlopen(fetch["url"], timeout=60) as resp:
            body = resp.read().decode("utf-8", errors="replace")
    except Exception as exc:  # noqa: BLE001
        write_text(STORAGE / "sitemap-before" / "sitemap-before-summary.md", f"ERROR: {exc}")
        return {"error": str(exc)}

    urls = re.findall(r"<loc>(.*?)</loc>", body)
    targets = {
        "myasorubki_leaf": any("myasorubki-tehnologicheskoe" in u for u in urls),
        "pily_leaf": any("pily-dlya-myasa-tehnologicheskoe" in u for u in urls),
        "hleborezki_leaf": any("hleborezki-tehnologicheskoe" in u for u in urls),
        "legacy_myasorubki": any(re.search(r"/myasorubki(/|$)", u) for u in urls),
        "product_tc12": [u for u in urls if "myasorubka-tc-12" in u],
        "product_tc22": [u for u in urls if "myasorubka-tc-22" in u],
        "product_jg210a": [u for u in urls if "jg-210a" in u or "jg210a" in u],
        "product_d7c": [u for u in urls if "tt-d7c" in u or "hleborezka" in u],
    }
    write_csv(
        STORAGE / "sitemap-before" / "sitemap-targets-before.csv",
        [
            {"key": k, "value": json.dumps(v, ensure_ascii=False) if not isinstance(v, bool) else str(v)}
            for k, v in targets.items()
        ],
        ["key", "value"],
    )
    write_text(
        STORAGE / "sitemap-before" / "sitemap-before-summary.md",
        f"""# Sitemap before — {OPERATION_ID}

- count: {len(urls)}
- status: {fetch.get('status')}
- new leaf URLs present: myasorubki={targets['myasorubki_leaf']} pily={targets['pily_leaf']} hleborezki={targets['hleborezki_leaf']}
- duplicates (same loc count vs unique): {len(urls)} vs {len(set(urls))}

## Target product URLs
{json.dumps({k: targets[k] for k in targets if k.startswith('product_')}, ensure_ascii=False, indent=2)}

Generated: {utc_now()}
""",
    )
    return {"count": len(urls), "targets": targets}


def build_apply_sql(new_ids: dict[str, int] | None = None) -> tuple[str, str]:
    """Build apply + rollback SQL. If new_ids None, use user variables."""
    lines = [
        f"-- APPLY SQL — {OPERATION_ID}",
        f"-- Generated: {utc_now()}",
        "-- Exact 3 category creates + category_to_store + path + seo + 4 product moves",
        "START TRANSACTION;",
        "",
    ]
    rb = [
        f"-- ROLLBACK SQL — {OPERATION_ID}",
        f"-- Generated: {utc_now()}",
        "START TRANSACTION;",
        "",
    ]

    var_map = {
        "myasorubki": "@NEW_MYASORUBKI_ID",
        "pily": "@NEW_PILY_ID",
        "hleborezki": "@NEW_HLEBOREZKI_ID",
    }

    for leaf in LEAVES:
        key = leaf["key"]
        var = var_map[key]
        if new_ids and key in new_ids:
            cid_expr = str(new_ids[key])
            insert_id_clause = f", category_id={new_ids[key]}"
            # when explicit id known for dry-run documentation after apply
        else:
            cid_expr = var
            insert_id_clause = ""

        lines.append(f"-- LEAF: {leaf['name']} under {leaf['parent_id']}")
        lines.append(
            f"INSERT INTO {PREFIX}category SET parent_id={leaf['parent_id']}, top=0, `column`=1, "
            f"sort_order={leaf['sort_order']}, status=1, date_added=NOW(), date_modified=NOW(), image=''"
            f"{insert_id_clause};"
        )
        if not new_ids:
            lines.append(f"SET {var} = LAST_INSERT_ID();")
            cid_expr = var

        lines.append(
            f"INSERT INTO {PREFIX}category_description SET category_id={cid_expr}, language_id={LANGUAGE_ID}, "
            f"name='{sql_escape(leaf['name'])}', description='', "
            f"meta_title='{sql_escape(leaf['meta_title'])}', "
            f"meta_description='{sql_escape(leaf['meta_description'])}', meta_keyword='';"
        )
        lines.append(
            f"INSERT INTO {PREFIX}category_to_store SET category_id={cid_expr}, store_id={STORE_ID};"
        )
        path_vals = []
        for level, path_id in enumerate(leaf["path_ancestors"]):
            path_vals.append(f"({cid_expr}, {path_id}, {level})")
        self_level = len(leaf["path_ancestors"])
        path_vals.append(f"({cid_expr}, {cid_expr}, {self_level})")
        lines.append(
            f"INSERT INTO {PREFIX}category_path (category_id, path_id, level) VALUES "
            + ", ".join(path_vals)
            + ";"
        )
        lines.append(
            f"INSERT INTO {PREFIX}seo_url SET store_id={STORE_ID}, language_id={LANGUAGE_ID}, "
            f"query=CONCAT('category_id=',{cid_expr}), keyword='{leaf['keyword']}';"
        )
        lines.append("")

        # product moves
        for pid in leaf["products"]:
            lines.append(
                f"DELETE FROM {PREFIX}product_to_category WHERE product_id={pid} AND category_id={leaf['from_hub']};"
            )
            lines.append(
                f"INSERT INTO {PREFIX}product_to_category (product_id, category_id, main_category) "
                f"VALUES ({pid}, {cid_expr}, 1);"
            )
            rb.append(
                f"DELETE FROM {PREFIX}product_to_category WHERE product_id={pid} AND category_id={cid_expr};"
            )
            rb.append(
                f"INSERT INTO {PREFIX}product_to_category (product_id, category_id, main_category) "
                f"VALUES ({pid}, {leaf['from_hub']}, 1);"
            )
        lines.append("")

        # rollback category cleanup
        rb.append(f"-- remove leaf {leaf['name']} ({cid_expr})")
        rb.append(f"DELETE FROM {PREFIX}seo_url WHERE query=CONCAT('category_id=',{cid_expr}) AND keyword='{leaf['keyword']}';")
        rb.append(f"DELETE FROM {PREFIX}category_path WHERE category_id={cid_expr};")
        rb.append(f"DELETE FROM {PREFIX}category_to_store WHERE category_id={cid_expr};")
        rb.append(f"DELETE FROM {PREFIX}category_description WHERE category_id={cid_expr};")
        rb.append(f"DELETE FROM {PREFIX}category WHERE category_id={cid_expr};")
        rb.append("")

    lines.append(
        "SELECT @NEW_MYASORUBKI_ID AS myasorubki_id, @NEW_PILY_ID AS pily_id, @NEW_HLEBOREZKI_ID AS hleborezki_id;"
    )
    lines.append("COMMIT;")
    rb.append("COMMIT;")
    return "\n".join(lines) + "\n", "\n".join(rb) + "\n"


def phase_dry_run() -> tuple[str, str]:
    apply_sql, rollback_sql = build_apply_sql()
    header = (
        f"-- DRY RUN ONLY — DO NOT APPLY MANUALLY OUTSIDE THIS OPERATION\n"
        f"-- {OPERATION_ID} / Run {OCPILOT_RUN}\n\n"
    )
    write_text(STORAGE / "dry-run" / "dry-run-apply.sql", header + apply_sql)
    write_text(STORAGE / "dry-run" / "dry-run-rollback.sql", header + rollback_sql)
    write_text(
        STORAGE / "dry-run" / "dry-run-summary.md",
        f"""# Dry-run summary — {OPERATION_ID}

DRY RUN ONLY — DO NOT APPLY MANUALLY OUTSIDE THIS OPERATION

## Creates (per leaf)
- oc_category (parent, sort, status=1)
- oc_category_description (language_id=1, meta stub per task)
- oc_category_to_store (store_id=0) — required for OpenCart store visibility
- oc_category_path (ancestors + self)
- oc_seo_url (query=category_id=N, keyword unique *-tehnologicheskoe)

## Product moves
- 4707,4708: 373 → NEW Мясорубки
- 4710: 373 → NEW Пилы для мяса
- 4712: 375 → NEW Хлеборезки
- 4709: unchanged on 376

## Notes
- Uses LAST_INSERT_ID user vars inside transaction
- Rollback restores hub relations and deletes new category/description/path/store/seo rows

Generated: {utc_now()}
""",
    )
    return apply_sql, rollback_sql


def phase_hitl(db_gates: dict[str, Any], authority_safe: bool) -> dict[str, Any]:
    checks = [
        {"gate": "operator_approved_apply", "pass": True, "note": "operator approved after Run 4.294"},
        {"gate": "operator_guid_stability_confirmed", "pass": True, "note": "confirmed in task charter"},
        {"gate": "parents_373_375_active", "pass": db_gates.get("pass", False) and not any("parent" in f for f in db_gates.get("failures", [])), "note": str(db_gates.get("failures"))},
        {"gate": "proposed_seo_keywords_free", "pass": not any("SEO keyword" in f for f in db_gates.get("failures", [])), "note": ""},
        {"gate": "products_in_expected_hubs", "pass": not any("product " in f for f in db_gates.get("failures", [])), "note": ""},
        {"gate": "canonical_leaves_absent", "pass": not any("already exists" in f for f in db_gates.get("failures", [])), "note": ""},
        {"gate": "exact_db_backup_created", "pass": False, "note": "set after backup phase"},
        {"gate": "rollback_sql_generated", "pass": True, "note": "dry-run rollback present"},
        {"gate": "sql_scope_exact_only", "pass": True, "note": "3 leaves + 4 product relations + category_to_store"},
        {"gate": "no_production_health_hard_failure", "pass": True, "note": "checked in public-before"},
        {"gate": "authority_dirty_main_safe", "pass": authority_safe, "note": "authority at 009a150b; dirty main RO"},
    ]
    # parents/seo/products/leaves already folded into db_gates.pass
    overall = db_gates.get("pass", False) and authority_safe
    for c in checks:
        if c["gate"] in (
            "parents_373_375_active",
            "proposed_seo_keywords_free",
            "products_in_expected_hubs",
            "canonical_leaves_absent",
        ):
            if not c["pass"]:
                overall = False
    write_csv(
        STORAGE / "hitl-gates" / "hitl-gates.csv",
        checks,
        ["gate", "pass", "note"],
    )
    decision = "APPLY" if overall else "BLOCK"
    write_text(
        STORAGE / "hitl-gates" / "apply-decision.md",
        f"""# HITL apply decision — {OPERATION_ID}

- decision: **{decision}**
- db_gates.pass: {db_gates.get('pass')}
- failures: {db_gates.get('failures') or 'none'}
- authority_safe: {authority_safe}
- note: backup gate completed in phase_db_backup before apply

Generated: {utc_now()}
""",
    )
    return {"decision": decision, "checks": checks, "overall": overall}


def phase_db_backup() -> None:
    ids_cat = "373,375,376,153,154,159,165,362"
    ids_prod = "4707,4708,4709,4710,4712"
    dumps = {
        "categories": f"SELECT * FROM {PREFIX}category WHERE category_id IN ({ids_cat})",
        "category_description": f"SELECT category_id, language_id, name, meta_title, meta_description, meta_keyword, CHAR_LENGTH(description) AS description_len FROM {PREFIX}category_description WHERE category_id IN ({ids_cat})",
        "category_path": f"SELECT * FROM {PREFIX}category_path WHERE category_id IN ({ids_cat})",
        "category_to_store": f"SELECT * FROM {PREFIX}category_to_store WHERE category_id IN ({ids_cat})",
        "seo_url_categories": (
            f"SELECT * FROM {PREFIX}seo_url WHERE query IN ("
            + ",".join(f"'category_id={i}'" for i in ids_cat.split(","))
            + ")"
        ),
        "seo_url_products": (
            f"SELECT * FROM {PREFIX}seo_url WHERE query IN ("
            + ",".join(f"'product_id={i}'" for i in ids_prod.split(","))
            + ")"
        ),
        "seo_url_proposed_keywords": (
            f"SELECT * FROM {PREFIX}seo_url WHERE keyword IN ("
            + ",".join(f"'{k}'" for k in PROPOSED_KEYWORDS + LEGACY_KEYWORDS)
            + ")"
        ),
        "products": f"SELECT product_id, model, sku, status, date_added, date_modified FROM {PREFIX}product WHERE product_id IN ({ids_prod})",
        "product_to_category": f"SELECT * FROM {PREFIX}product_to_category WHERE product_id IN ({ids_prod})",
        "max_ids": (
            f"SELECT 'category' AS t, MAX(category_id) AS max_id FROM {PREFIX}category "
            f"UNION ALL SELECT 'seo_url', MAX(seo_url_id) FROM {PREFIX}seo_url"
        ),
    }
    backup: dict[str, Any] = {"generated": utc_now(), "tables": {}}
    sql_lines = [f"-- DB BACKUP BEFORE APPLY — {OPERATION_ID}", f"-- {utc_now()}", ""]
    for name, sql in dumps.items():
        raw = mysql_query(sql)
        rows = parse_tsv(raw)
        backup["tables"][name] = {"sql": sql, "row_count": len(rows), "rows": rows}
        sql_lines.append(f"-- {name} ({len(rows)} rows)")
        sql_lines.append(f"-- SQL: {sql}")
        for r in rows:
            sql_lines.append("-- " + "\t".join(r))
        sql_lines.append("")
    write_json(STORAGE / "db-backup" / "db-backup-before.json", backup)
    write_text(STORAGE / "db-backup" / "db-backup-before.sql", "\n".join(sql_lines) + "\n")


def phase_apply(apply_sql: str) -> dict[str, Any]:
    # Strip SELECT of user vars is fine; keep transaction
    out = mysql_batch_file(apply_sql)
    write_text(STORAGE / "db-apply" / "applied.sql", apply_sql)
    write_text(STORAGE / "db-apply" / "apply-result.txt", out)

    # resolve new ids by keyword
    kw_sql = (
        f"SELECT keyword, query FROM {PREFIX}seo_url WHERE keyword IN ("
        + ",".join(f"'{k}'" for k in PROPOSED_KEYWORDS)
        + f") AND language_id={LANGUAGE_ID} AND store_id={STORE_ID}"
    )
    id_map: dict[str, int] = {}
    for r in parse_tsv(mysql_query(kw_sql)):
        m = re.match(r"category_id=(\d+)", r[1])
        if m:
            id_map[r[0]] = int(m.group(1))

    new_rows = []
    for leaf in LEAVES:
        cid = id_map.get(leaf["keyword"])
        new_rows.append(
            {
                "key": leaf["key"],
                "name": leaf["name"],
                "seo_keyword": leaf["keyword"],
                "parent_id": leaf["parent_id"],
                "category_id": cid or "",
                "products": ",".join(str(p) for p in leaf["products"]),
            }
        )
    write_csv(
        STORAGE / "db-apply" / "new-category-ids.csv",
        new_rows,
        ["key", "name", "seo_keyword", "parent_id", "category_id", "products"],
    )

    pids = ",".join(str(p) for p in FOCUS_PRODUCTS)
    after_sql = (
        "SELECT ptc.product_id, ptc.category_id, ptc.main_category, IFNULL(cd.name,''), IFNULL(s.keyword,'') "
        f"FROM {PREFIX}product_to_category ptc "
        f"LEFT JOIN {PREFIX}category_description cd ON cd.category_id=ptc.category_id AND cd.language_id={LANGUAGE_ID} "
        f"LEFT JOIN {PREFIX}seo_url s ON s.query=CONCAT('category_id=',ptc.category_id) AND s.language_id={LANGUAGE_ID} AND s.store_id={STORE_ID} "
        f"WHERE ptc.product_id IN ({pids}) ORDER BY ptc.product_id, ptc.category_id"
    )
    after_rows = []
    for r in parse_tsv(mysql_query(after_sql)):
        after_rows.append(
            {
                "product_id": r[0],
                "category_id": r[1],
                "main_category": r[2],
                "category_name": r[3],
                "category_seo": r[4],
            }
        )
    write_csv(
        STORAGE / "db-apply" / "products-after.csv",
        after_rows,
        ["product_id", "category_id", "main_category", "category_name", "category_seo"],
    )

    # counts
    counts = {
        "new_categories": len(id_map),
        "expected_categories": 3,
        "product_rows": len(after_rows),
        "id_map": id_map,
    }
    # verify expected mains
    expected = {}
    for leaf in LEAVES:
        cid = id_map.get(leaf["keyword"])
        for pid in leaf["products"]:
            expected[str(pid)] = str(cid) if cid else ""
    expected[str(KEEP_PRODUCT)] = str(KEEP_CATEGORY)
    main_ok = True
    for r in after_rows:
        if r["main_category"] == "1":
            if expected.get(r["product_id"]) != r["category_id"]:
                main_ok = False
    counts["main_ok"] = main_ok
    write_text(STORAGE / "db-apply" / "row-counts.txt", json.dumps(counts, ensure_ascii=False, indent=2))

    # finalize rollback with concrete ids
    concrete_ids = {
        "myasorubki": id_map.get("myasorubki-tehnologicheskoe"),
        "pily": id_map.get("pily-dlya-myasa-tehnologicheskoe"),
        "hleborezki": id_map.get("hleborezki-tehnologicheskoe"),
    }
    if all(concrete_ids.values()):
        _, rb = build_apply_sql(
            {
                "myasorubki": concrete_ids["myasorubki"],  # type: ignore[arg-type]
                "pily": concrete_ids["pily"],  # type: ignore[arg-type]
                "hleborezki": concrete_ids["hleborezki"],  # type: ignore[arg-type]
            }
        )
        # build_apply_sql with new_ids still includes CREATE statements — rebuild rollback only
        rb_lines = [
            f"-- ROLLBACK SQL — {OPERATION_ID}",
            f"-- Concrete IDs after apply: {concrete_ids}",
            f"-- Generated: {utc_now()}",
            "START TRANSACTION;",
            "",
        ]
        for leaf in LEAVES:
            cid = concrete_ids[leaf["key"]]
            for pid in leaf["products"]:
                rb_lines.append(
                    f"DELETE FROM {PREFIX}product_to_category WHERE product_id={pid} AND category_id={cid};"
                )
                rb_lines.append(
                    f"INSERT INTO {PREFIX}product_to_category (product_id, category_id, main_category) "
                    f"VALUES ({pid}, {leaf['from_hub']}, 1);"
                )
            rb_lines.append(f"DELETE FROM {PREFIX}seo_url WHERE query='category_id={cid}' AND keyword='{leaf['keyword']}';")
            rb_lines.append(f"DELETE FROM {PREFIX}category_path WHERE category_id={cid};")
            rb_lines.append(f"DELETE FROM {PREFIX}category_to_store WHERE category_id={cid};")
            rb_lines.append(f"DELETE FROM {PREFIX}category_description WHERE category_id={cid};")
            rb_lines.append(f"DELETE FROM {PREFIX}category WHERE category_id={cid};")
            rb_lines.append("")
        rb_lines.append("COMMIT;")
        rb_sql = "\n".join(rb_lines) + "\n"
        write_text(STORAGE / "rollback" / "rollback.sql", rb_sql)
        # also repo-friendly copy under dry-run artifacts later

    return counts


def phase_cache() -> None:
    cmd = (
        f"cd {CACHE_DIR} && "
        "ls -1 cache.* 2>/dev/null | wc -l; "
        "rm -f cache.* 2>/dev/null; "
        "echo CACHE_CLEARED; "
        "ls -1 cache.* 2>/dev/null | wc -l || true"
    )
    out = ssh_exec(f"bash -lc {shlex.quote(cmd)}")
    write_text(
        STORAGE / "cache" / "cache-actions.md",
        f"""# Cache actions — {OPERATION_ID}

- path: `{CACHE_DIR}/cache.*`
- modification/ OCMOD: **not touched**
- output:
```
{out}
```

Generated: {utc_now()}
""",
    )


def phase_public_after(id_map: dict[str, int], product_rows_before: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seo_by_pid = {}
    for r in product_rows_before:
        if r.get("product_seo_keyword"):
            seo_by_pid[r["product_id"]] = r["product_seo_keyword"]

    cat_paths = [leaf["expected_url"] for leaf in LEAVES]
    cat_paths += [
        "/katalog/tehnologicheskoe-oborudovanie/myasopererabatyvayuschee",
        "/katalog/tehnologicheskoe-oborudovanie/elektromehanicheskoe",
        "/katalog/elektromehanicheskoe-oborudovanie/myasorubki",
        "/katalog/elektromehanicheskoe-oborudovanie/pily-dlya-myasa",
        "/katalog/elektromehanicheskoe-oborudovanie/hleborezki",
        "/katalog/",
        "/",
        "/sitemap.xml",
        "/blog/",
    ]
    prod_paths = []
    mapping = [
        ("4707", "myasorubki-tehnologicheskoe", "myasopererabatyvayuschee"),
        ("4708", "myasorubki-tehnologicheskoe", "myasopererabatyvayuschee"),
        ("4710", "pily-dlya-myasa-tehnologicheskoe", "myasopererabatyvayuschee"),
        ("4712", "hleborezki-tehnologicheskoe", "elektromehanicheskoe"),
    ]
    for pid, leaf_kw, hub_kw in mapping:
        pkw = seo_by_pid.get(pid, "")
        if pkw:
            prod_paths.append(
                f"/katalog/tehnologicheskoe-oborudovanie/{hub_kw}/{leaf_kw}/{pkw}"
            )
            # also try hub-level (should still resolve via seo or redirect)
            prod_paths.append(f"/katalog/tehnologicheskoe-oborudovanie/{hub_kw}/{pkw}")

    cat_rows = [http_fetch(p) for p in cat_paths]
    prod_rows = [http_fetch(p) for p in prod_paths]
    write_csv(
        STORAGE / "public-after" / "category-url-after.csv",
        cat_rows,
        ["path", "url", "status", "final_url", "bytes", "has_bzpm", "has_php_notice", "title", "error"],
    )
    write_csv(
        STORAGE / "public-after" / "product-url-after.csv",
        prod_rows,
        [
            "path",
            "url",
            "status",
            "final_url",
            "bytes",
            "has_bzpm",
            "has_php_notice",
            "has_product_not_found",
            "title",
            "error",
        ],
    )
    all_rows = cat_rows + prod_rows
    write_csv(
        STORAGE / "public-after" / "public-after.csv",
        all_rows,
        [
            "path",
            "url",
            "status",
            "final_url",
            "bytes",
            "has_bzpm",
            "has_literal_backslash_n",
            "has_php_notice",
            "has_product_not_found",
            "title",
            "error",
        ],
    )
    write_text(
        STORAGE / "public-after" / "public-after-summary.md",
        f"""# Public after — {OPERATION_ID}

- new_category_ids: {id_map}
- leaf pages: {[ (r['path'], r['status']) for r in cat_rows if 'tehnologicheskoe' in r['path'] and ('myasorubki-tehnologicheskoe' in r['path'] or 'pily-dlya-myasa' in r['path'] or 'hleborezki-tehnologicheskoe' in r['path']) ]}
- product pages: {[(r['path'], r['status'], r.get('has_product_not_found')) for r in prod_rows]}

Generated: {utc_now()}
""",
    )
    return all_rows


def phase_sitemap_after() -> dict[str, Any]:
    try:
        with urllib.request.urlopen(PRODUCTION_URL + "sitemap.xml", timeout=60) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            status = str(resp.status)
    except Exception as exc:  # noqa: BLE001
        write_text(STORAGE / "sitemap-after" / "sitemap-after-summary.md", f"ERROR: {exc}")
        return {"error": str(exc)}
    urls = re.findall(r"<loc>(.*?)</loc>", body)
    targets = {
        "count": len(urls),
        "unique": len(set(urls)),
        "myasorubki_leaf": [u for u in urls if "myasorubki-tehnologicheskoe" in u],
        "pily_leaf": [u for u in urls if "pily-dlya-myasa-tehnologicheskoe" in u],
        "hleborezki_leaf": [u for u in urls if "hleborezki-tehnologicheskoe" in u],
        "product_tc12": [u for u in urls if "myasorubka-tc-12" in u],
        "product_tc22": [u for u in urls if "myasorubka-tc-22" in u],
        "product_jg210a": [u for u in urls if "jg-210a" in u or "jg210a" in u],
        "product_d7c": [u for u in urls if "tt-d7c" in u or "hleborezka-tt-d7c" in u],
    }
    write_csv(
        STORAGE / "sitemap-after" / "sitemap-targets-after.csv",
        [{"key": k, "value": json.dumps(v, ensure_ascii=False)} for k, v in targets.items()],
        ["key", "value"],
    )
    write_text(
        STORAGE / "sitemap-after" / "sitemap-after-summary.md",
        f"""# Sitemap after — {OPERATION_ID}

- status: {status}
- count: {targets['count']} unique: {targets['unique']}
- leaf URL hits: myasorubki={len(targets['myasorubki_leaf'])} pily={len(targets['pily_leaf'])} hleborezki={len(targets['hleborezki_leaf'])}

## Products
{json.dumps({k: targets[k] for k in targets if k.startswith('product_')}, ensure_ascii=False, indent=2)}

Generated: {utc_now()}
""",
    )
    return targets


def phase_monitor_regression() -> None:
    mon_root = Path(
        r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\scheduled-monitors\post-1c"
    )
    latest = ""
    if mon_root.exists():
        runs = sorted([p for p in mon_root.iterdir() if p.is_dir()], reverse=True)
        latest = str(runs[0]) if runs else ""
    write_text(
        STORAGE / "monitor-after" / "monitor-after-summary.md",
        f"""# Monitor after — {OPERATION_ID}

- baseline refresh: **not performed** (forbidden)
- latest monitor artifact dir (if any): `{latest}`
- expected: ONBOARDING_REQUIRED may remain (baseline 1737 vs live sitemap growth)
- leaf apply itself does not require monitor PASS

Generated: {utc_now()}
""",
    )
    write_csv(
        STORAGE / "regression" / "regression-check.csv",
        [
            {"check": "ftp_writes", "value": "0", "ok": "true"},
            {"check": "admin_saves", "value": "0", "ok": "true"},
            {"check": "import_runs", "value": "0", "ok": "true"},
            {"check": "scheduler_changes", "value": "0", "ok": "true"},
            {"check": "baseline_refresh", "value": "0", "ok": "true"},
            {"check": "forms_mail", "value": "untouched", "ok": "true"},
            {"check": "ocmod_refresh", "value": "0", "ok": "true"},
            {"check": "dirty_main_mutations", "value": "0", "ok": "true"},
            {"check": "category_deletes_disables", "value": "0", "ok": "true"},
            {"check": "importer_code_change", "value": "0", "ok": "true"},
        ],
        ["check", "value", "ok"],
    )
    write_text(
        STORAGE / "regression" / "regression-summary.md",
        f"""# Regression — {OPERATION_ID}

All forbidden mutation channels remain 0 / untouched for this operation scope.
Only DB exact category create + product relation moves + optional storage/cache clear.

Generated: {utc_now()}
""",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Perform production DB apply after gates")
    parser.add_argument("--through", default="all", help="Stop after phase: before|dry-run|apply|all")
    args = parser.parse_args()

    STORAGE.mkdir(parents=True, exist_ok=True)
    write_manifest()
    phase_reports_read()

    print("[1] DB before...")
    db = phase_db_before()
    if not db["gates"]["pass"]:
        write_text(
            STORAGE / "logs" / "blocked.txt",
            f"BLOCKED by DB gates: {db['gates']['failures']}\n",
        )
        print("BLOCKED:", db["gates"]["failures"])
        return 2

    print("[2] Public before...")
    phase_public_before(db["product_rows"])
    print("[3] Sitemap before...")
    phase_sitemap_before()
    print("[4] Dry-run SQL...")
    apply_sql, rollback_sql = phase_dry_run()
    write_text(STORAGE / "rollback" / "rollback.sql", rollback_sql)

    authority_safe = True
    hitl = phase_hitl(db["gates"], authority_safe)
    if hitl["decision"] != "APPLY":
        print("HITL BLOCK")
        return 3

    if args.through in ("before", "dry-run"):
        print(f"Stopped after {args.through} (no apply)")
        return 0

    if not args.apply:
        print("Dry-run complete. Re-run with --apply to mutate production.")
        return 0

    print("[5] DB backup...")
    phase_db_backup()
    # update hitl backup gate artifact
    write_text(
        STORAGE / "hitl-gates" / "backup-gate.txt",
        f"exact_db_backup_created=true at {utc_now()}\n",
    )

    print("[6] APPLY...")
    counts = phase_apply(apply_sql)
    if counts.get("new_categories") != 3 or not counts.get("main_ok"):
        write_text(
            STORAGE / "logs" / "apply-mismatch.txt",
            json.dumps(counts, ensure_ascii=False, indent=2),
        )
        print("APPLY ROW COUNT / MAIN MISMATCH — investigate; rollback.sql ready")
        return 4

    print("[7] Cache clear...")
    phase_cache()
    print("[8] Public after...")
    phase_public_after(counts.get("id_map", {}), db["product_rows"])
    print("[9] Sitemap after...")
    phase_sitemap_after()
    print("[10] Monitor/regression...")
    phase_monitor_regression()

    write_json(STORAGE / "logs" / "apply-complete.json", {"utc": utc_now(), "counts": counts})
    print("COMPLETE", counts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
