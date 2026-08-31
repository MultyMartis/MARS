#!/usr/bin/env python3
"""SITE-002 — verify product presence and temporarily hide empty roots if needed.

Operation: SITE-002-PROD-POSUDA-UPAKOVOCHNOE-EMPTY-CATEGORY-CHECK-01
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
import xml.etree.ElementTree as ET
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

OPERATION_ID = "SITE-002-PROD-POSUDA-UPAKOVOCHNOE-EMPTY-CATEGORY-CHECK-01"
PRODUCTION_URL = "https://bzpm.ru/"
PREFIX = "oc_"
MAP_TABLE = f"{PREFIX}mars_1c_category_map"
LANGUAGE_ID = 1
STORE_ID = 0
TARGET_IDS = (364, 381)
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
AUTHORITY_REPO = CANONICAL_MONOREPO  # resolved in main()
STORAGE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
CACHE_DIR = "/home/a/assum/bzpm.ru/storage/cache"
XML_LOCAL = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-CATALOG-TREE-1C-COMPARISON-AUDIT-01\import-files\import0_1.xml"
)
IMPORT_LOG = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-POST-IMPORT-AND-MONITOR-HEALTHCHECK-01\import-logs\mars_1c_import_2026-08-24_080010.txt"
)

STORAGE_SUBDIRS = (
    "preflight",
    "db-before",
    "one-c-check",
    "public-before",
    "decision",
    "rollback",
    "production-apply",
    "cache",
    "public-after",
    "regression",
    "reports",
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


def fetch_url(url: str) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "MARS-SITE-002-empty-category-check/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return {
                "url": url,
                "status": resp.status,
                "final_url": resp.geturl(),
                "bytes": len(body),
                "body": body,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return {
            "url": url,
            "status": exc.code,
            "final_url": exc.geturl(),
            "bytes": len(body),
            "body": body,
        }


def count_product_cards(html: str) -> int:
    patterns = (
        r'class="[^"]*product-layout[^"]*"',
        r'class="[^"]*product-thumb[^"]*"',
        r'data-product-id=',
        r'product/product&product_id=',
    )
    counts = [len(re.findall(p, html, re.I)) for p in patterns]
    return max(counts) if counts else 0


def count_category_cards(html: str) -> int:
    return len(re.findall(r'class="[^"]*zpm-cat-card[^"]*"', html, re.I))


def count_root_tiles(html: str) -> int:
    return len(re.findall(r'class="[^"]*zpm-catalog-section[^"]*"', html, re.I))


def slug_visible_on_page(html: str, slug: str) -> bool:
    return slug in html


def has_php_warning(html: str) -> bool:
    return bool(re.search(r"(Fatal error|Warning:|Notice:|Parse error)", html, re.I))


def has_bzpm(html: str) -> bool:
    return "БЗПМ" in html or "BZPM" in html.upper()


def ensure_storage() -> None:
    for sub in STORAGE_SUBDIRS:
        (STORAGE / sub).mkdir(parents=True, exist_ok=True)


def git_preflight() -> dict[str, str]:
    def run(args: list[str]) -> str:
        return subprocess.check_output(args, cwd=AUTHORITY_REPO, text=True, stderr=subprocess.STDOUT).strip()

    return {
        "branch": run(["git", "branch", "--show-current"]),
        "head": run(["git", "rev-parse", "--short", "HEAD"]),
        "status_short": run(["git", "status", "--short"]) or "(clean except listed)",
        "origin_head": run(["git", "rev-parse", "--short", "origin/mars/canonical-post-recovery"]),
    }


def db_category_snapshot(cat_id: int) -> dict[str, Any]:
    sql = f"""
SELECT c.category_id, cd.name, c.parent_id, c.status, c.image, c.sort_order,
       su.keyword,
       m.source_group_id, m.source_name, m.status AS map_status,
       (SELECT COUNT(*) FROM {PREFIX}product_to_category ptc WHERE ptc.category_id=c.category_id) AS direct_total,
       (SELECT COUNT(*) FROM {PREFIX}product_to_category ptc
          JOIN {PREFIX}product p ON p.product_id=ptc.product_id
         WHERE ptc.category_id=c.category_id AND p.status=1) AS direct_enabled,
       (SELECT COUNT(DISTINCT ptc.product_id) FROM {PREFIX}category_path cp
          JOIN {PREFIX}product_to_category ptc ON ptc.category_id=cp.category_id
          JOIN {PREFIX}product p ON p.product_id=ptc.product_id
         WHERE cp.path_id=c.category_id AND p.status=1) AS subtree_enabled,
       (SELECT GROUP_CONCAT(CONCAT(cp.level, ':', cp.path_id) ORDER BY cp.level SEPARATOR ' > ')
          FROM {PREFIX}category_path cp WHERE cp.category_id=c.category_id) AS path_chain,
       (SELECT COUNT(*) FROM {PREFIX}category_to_store cs WHERE cs.category_id=c.category_id AND cs.store_id={STORE_ID}) AS store_bound
FROM {PREFIX}category c
JOIN {PREFIX}category_description cd ON cd.category_id=c.category_id AND cd.language_id={LANGUAGE_ID}
LEFT JOIN {PREFIX}seo_url su ON su.query=CONCAT('category_id=', c.category_id) AND su.store_id={STORE_ID} AND su.language_id={LANGUAGE_ID}
LEFT JOIN {MAP_TABLE} m ON m.category_id=c.category_id
WHERE c.category_id={cat_id};
"""
    rows = parse_tsv(mysql_query(sql))
    if not rows:
        return {"category_id": cat_id, "missing": True}
    r = rows[0]
    keys = [
        "category_id",
        "name",
        "parent_id",
        "status",
        "image",
        "sort_order",
        "keyword",
        "source_group_id",
        "source_name",
        "map_status",
        "direct_total",
        "direct_enabled",
        "subtree_enabled",
        "path_chain",
        "store_bound",
    ]
    return dict(zip(keys, r))


def db_products_for_category(cat_id: int) -> list[dict[str, Any]]:
    sql = f"""
SELECT p.product_id, p.model, pd.name, p.status, p.quantity, p.price,
       (SELECT GROUP_CONCAT(ptc2.category_id ORDER BY ptc2.category_id)
          FROM {PREFIX}product_to_category ptc2 WHERE ptc2.product_id=p.product_id) AS all_categories
FROM {PREFIX}product_to_category ptc
JOIN {PREFIX}product p ON p.product_id=ptc.product_id
JOIN {PREFIX}product_description pd ON pd.product_id=p.product_id AND pd.language_id={LANGUAGE_ID}
WHERE ptc.category_id={cat_id}
ORDER BY p.product_id;
"""
    rows = parse_tsv(mysql_query(sql))
    out: list[dict[str, Any]] = []
    for r in rows:
        out.append(
            {
                "category_id": cat_id,
                "product_id": r[0],
                "sku": r[1],
                "name": r[2],
                "status": r[3],
                "quantity": r[4],
                "price": r[5],
                "all_categories": r[6] if len(r) > 6 else "",
            }
        )
    return out


def db_child_categories(cat_id: int) -> list[dict[str, Any]]:
    sql = f"""
SELECT c.category_id, cd.name, c.status,
       (SELECT COUNT(*) FROM {PREFIX}product_to_category ptc
          JOIN {PREFIX}product p ON p.product_id=ptc.product_id
         WHERE ptc.category_id=c.category_id AND p.status=1) AS direct_enabled
FROM {PREFIX}category c
JOIN {PREFIX}category_description cd ON cd.category_id=c.category_id AND cd.language_id={LANGUAGE_ID}
WHERE c.parent_id={cat_id}
ORDER BY c.category_id;
"""
    rows = parse_tsv(mysql_query(sql))
    return [
        {
            "parent_id": cat_id,
            "child_category_id": r[0],
            "child_name": r[1],
            "child_status": r[2],
            "child_direct_enabled": r[3],
        }
        for r in rows
    ]


def sitemap_has_keyword(keyword: str) -> bool:
    try:
        resp = fetch_url(PRODUCTION_URL + "sitemap.xml")
        if resp["status"] != 200:
            return False
        return keyword in resp["body"]
    except Exception:
        return False


def parse_1c_groups() -> dict[str, Any]:
    result: dict[str, Any] = {"xml_path": str(XML_LOCAL), "groups": {}, "import_log": str(IMPORT_LOG)}
    if not XML_LOCAL.exists():
        result["error"] = "local import0_1.xml missing"
        return result
    ns = {"c": "urn:1C.ru:commerceml_2"}
    tree = ET.parse(XML_LOCAL)
    root = tree.getroot()
    groups: dict[str, dict[str, Any]] = {}
    for grp in root.findall(".//c:Группа", ns):
        gid = grp.find("c:Ид", ns)
        name = grp.find("c:Наименование", ns)
        if gid is None or name is None:
            continue
        guid = gid.text.strip()
        groups[guid] = {"guid": guid, "name": name.text.strip(), "products": []}
    for item in root.findall(".//c:Товар", ns):
        pid = item.find("c:Ид", ns)
        pname = item.find("c:Наименование", ns)
        grp = item.find(".//c:Группы/c:Ид", ns)
        if pid is None or grp is None:
            continue
        gguid = grp.text.strip()
        groups.setdefault(gguid, {"guid": gguid, "name": "", "products": []})
        groups[gguid]["products"].append(
            {
                "product_guid": pid.text.strip(),
                "name": pname.text.strip() if pname is not None else "",
            }
        )
    result["groups"] = groups
    if IMPORT_LOG.exists():
        result["import_log_tail"] = IMPORT_LOG.read_text(encoding="utf-8", errors="replace")[-1200:]
    return result


def map_guid_to_site_product(xml_guid: str) -> str | None:
    sql = (
        f"SELECT product_id FROM {PREFIX}product WHERE model='{xml_guid}' "
        f"OR sku='{xml_guid}' LIMIT 1;"
    )
    rows = parse_tsv(mysql_query(sql))
    return rows[0][0] if rows else None


def public_smoke(label: str) -> list[dict[str, Any]]:
    urls = [
        ("home", PRODUCTION_URL),
        ("katalog", PRODUCTION_URL + "katalog/"),
        ("posuda", PRODUCTION_URL + "posuda-i-inventar"),
        ("upak", PRODUCTION_URL + "upakovochnoe-oborudovanie"),
    ]
    rows: list[dict[str, Any]] = []
    for key, url in urls:
        resp = fetch_url(url)
        body = resp["body"]
        rows.append(
            {
                "phase": label,
                "key": key,
                "url": url,
                "http_status": resp["status"],
                "final_url": resp["final_url"],
                "product_cards": count_product_cards(body),
                "category_cards": count_category_cards(body),
                "root_sections": count_root_tiles(body),
                "posuda_slug_visible": slug_visible_on_page(body, "posuda-i-inventar"),
                "upak_slug_visible": slug_visible_on_page(body, "upakovochnoe-oborudovanie"),
                "php_warning": has_php_warning(body),
                "bzpm_marker": has_bzpm(body),
                "h1": extract_h1(body),
            }
        )
    return rows


def extract_h1(html: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S)
    if not m:
        return ""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1))).strip()


def decide(cat: dict[str, Any], public_row: dict[str, Any], one_c: dict[str, Any] | None) -> str:
    enabled = int(cat.get("subtree_enabled") or cat.get("direct_enabled") or 0)
    direct = int(cat.get("direct_enabled") or 0)
    public_products = int(public_row.get("product_cards") or 0)
    cat_id = int(cat["category_id"])

    if enabled > 0 and public_products > 0:
        return "KEEP_VISIBLE_PRODUCTS_PRESENT"
    if enabled > 0 and public_products == 0:
        return "ATTENTION_REQUIRED_DO_NOT_HIDE"
    if enabled == 0 and cat_id == 381:
        pending = one_c and one_c.get("xml_product_count", 0) > 0
        if pending:
            return "PENDING_NEXT_IMPORT_TEMP_HIDE"
        return "TEMP_HIDE_EMPTY_CATEGORY"
    if enabled == 0:
        return "TEMP_HIDE_EMPTY_CATEGORY"
    return "ATTENTION_REQUIRED_DO_NOT_HIDE"


def build_rollback_sql(to_hide: list[int], snapshots: dict[int, dict[str, Any]]) -> str:
    lines = [
        f"-- Rollback for {OPERATION_ID}",
        f"-- Generated {utc_now()}",
        "START TRANSACTION;",
    ]
    for cat_id in to_hide:
        snap = snapshots[cat_id]
        lines.append(
            f"UPDATE {PREFIX}category SET status={snap['status']}, date_modified=NOW() "
            f"WHERE category_id={cat_id};"
        )
    lines.append("COMMIT;")
    return "\n".join(lines) + "\n"


def build_hide_sql(to_hide: list[int]) -> str:
    lines = [
        f"-- Apply temporary hide for {OPERATION_ID}",
        f"-- Generated {utc_now()}",
        "START TRANSACTION;",
    ]
    for cat_id in to_hide:
        lines.append(
            f"UPDATE {PREFIX}category SET status=0, date_modified=NOW() WHERE category_id={cat_id};"
        )
    lines.append("COMMIT;")
    return "\n".join(lines) + "\n"


def clear_cache() -> str:
    return ssh_exec(f"rm -f {CACHE_DIR}/cache.* 2>&1; echo CACHE_CLEARED")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=None, help="Git authority root (default: X:\\AI MARS)")
    parser.add_argument("--apply-hide", action="store_true")
    args = parser.parse_args()
    global AUTHORITY_REPO
    AUTHORITY_REPO = resolve_repo_root_for_read(args.repo_root)

    ensure_storage()
    git = git_preflight()
    write_json(STORAGE / "preflight" / "git-state.json", git)
    write_text(
        STORAGE / "preflight" / "preflight-summary.md",
        "\n".join(
            [
                f"# Preflight — {OPERATION_ID}",
                "",
                f"- Timestamp: {utc_now()}",
                f"- Authority repo: `{AUTHORITY_REPO}`",
                f"- Branch: `{git['branch']}`",
                f"- HEAD: `{git['head']}`",
                f"- Origin canonical: `{git['origin_head']}`",
                f"- Target categories: `{list(TARGET_IDS)}`",
                f"- Production URL: `{PRODUCTION_URL}`",
                "",
                "## Git status (short)",
                "```",
                git["status_short"],
                "```",
                "",
                "## Recent related reports",
                "- SITE-002-CATALOG-NORMALIZATION-APPLY-COMBINED-01",
                "- SITE-002-CATALOG-NORMALIZATION-UI-REPAIR-01",
                "- SITE-002-PROD-CHILD-CATEGORY-IMAGES-WAVE-01",
            ]
        )
        + "\n",
    )

    snapshots: dict[int, dict[str, Any]] = {}
    category_rows: list[dict[str, Any]] = []
    product_rows: list[dict[str, Any]] = []
    for cat_id in TARGET_IDS:
        snap = db_category_snapshot(cat_id)
        snapshots[cat_id] = snap
        category_rows.append(snap)
        product_rows.extend(db_products_for_category(cat_id))
        product_rows.extend(
            {
                **child,
                "record_type": "child_category",
            }
            for child in db_child_categories(cat_id)
        )

    write_csv(
        STORAGE / "db-before" / "category-product-status.csv",
        category_rows,
        [
            "category_id",
            "name",
            "parent_id",
            "status",
            "image",
            "sort_order",
            "keyword",
            "source_group_id",
            "source_name",
            "map_status",
            "direct_total",
            "direct_enabled",
            "subtree_enabled",
            "path_chain",
            "store_bound",
        ],
    )
    write_csv(
        STORAGE / "db-before" / "products-under-target-categories.csv",
        product_rows,
        [
            "category_id",
            "product_id",
            "sku",
            "name",
            "status",
            "quantity",
            "price",
            "all_categories",
            "record_type",
            "parent_id",
            "child_category_id",
            "child_name",
            "child_status",
            "child_direct_enabled",
        ],
    )

    one_c = parse_1c_groups()
    guid_map = {
        364: "9b37b1f1-7c19-11f1-aecc-581122cf362c",
        381: "5bc6a012-7c19-11f1-aecc-581122cf362c",
    }
    one_c_summary: list[str] = [
        f"# 1C target groups — {OPERATION_ID}",
        "",
        f"- Local XML: `{XML_LOCAL}`",
        f"- Latest import log: `{IMPORT_LOG}`",
        "",
    ]
    for cat_id, guid in guid_map.items():
        grp = one_c.get("groups", {}).get(guid, {})
        products = grp.get("products", [])
        one_c_summary.append(f"## Category {cat_id} — GUID `{guid}`")
        one_c_summary.append(f"- 1C group name: {grp.get('name', 'SAFE UNKNOWN')}")
        one_c_summary.append(f"- 1C products in XML: {len(products)}")
        for p in products[:10]:
            site_id = None
            try:
                site_id = map_guid_to_site_product(p["product_guid"])
            except Exception:
                site_id = None
            one_c_summary.append(
                f"  - `{p['product_guid']}` — {p.get('name', '')} — site_product_id={site_id or 'absent'}"
            )
        snap = snapshots[cat_id]
        snap["xml_product_count"] = len(products)
        one_c_summary.append(
            f"- Site direct enabled products: {snap.get('direct_enabled')} / subtree: {snap.get('subtree_enabled')}"
        )
        one_c_summary.append("")
    write_text(STORAGE / "one-c-check" / "one-c-target-groups-summary.md", "\n".join(one_c_summary) + "\n")

    public_before = public_smoke("before")
    write_csv(
        STORAGE / "public-before" / "public-before-smoke.csv",
        public_before,
        [
            "phase",
            "key",
            "url",
            "http_status",
            "final_url",
            "product_cards",
            "category_cards",
            "root_sections",
            "posuda_slug_visible",
            "upak_slug_visible",
            "php_warning",
            "bzpm_marker",
            "h1",
        ],
    )
    write_text(
        STORAGE / "public-before" / "public-before-summary.md",
        "\n".join(
            [
                f"# Public before — {OPERATION_ID}",
                "",
                *[f"- {r['key']}: HTTP {r['http_status']} products={r['product_cards']} h1={r['h1']!r}" for r in public_before],
            ]
        )
        + "\n",
    )

    decisions: dict[int, str] = {}
    for cat_id in TARGET_IDS:
        pub = next(r for r in public_before if r["key"] == ("posuda" if cat_id == 364 else "upak"))
        guid = guid_map[cat_id]
        grp = one_c.get("groups", {}).get(guid, {})
        one_c_ctx = {"xml_product_count": len(grp.get("products", []))}
        decisions[cat_id] = decide(snapshots[cat_id], pub, one_c_ctx)

    for cat_id in TARGET_IDS:
        slug = "posuda" if cat_id == 364 else "upak"
        write_text(
            STORAGE / "decision" / f"{slug}-decision.md",
            "\n".join(
                [
                    f"# Decision — category {cat_id}",
                    "",
                    f"- Decision: **{decisions[cat_id]}**",
                    f"- DB direct enabled: {snapshots[cat_id].get('direct_enabled')}",
                    f"- DB subtree enabled: {snapshots[cat_id].get('subtree_enabled')}",
                    f"- Public product cards: {next(r for r in public_before if r['key']==('posuda' if cat_id==364 else 'upak'))['product_cards']}",
                    f"- Category status: {snapshots[cat_id].get('status')}",
                    f"- Sitemap contains keyword: {sitemap_has_keyword(str(snapshots[cat_id].get('keyword') or ''))}",
                ]
            )
            + "\n",
        )

    to_hide = [cid for cid, d in decisions.items() if d in ("TEMP_HIDE_EMPTY_CATEGORY", "PENDING_NEXT_IMPORT_TEMP_HIDE")]
    keep = [cid for cid, d in decisions.items() if d.startswith("KEEP") or d.startswith("REPAIR")]
    attention = [cid for cid, d in decisions.items() if d.startswith("ATTENTION")]

    write_text(
        STORAGE / "decision" / "final-decision-summary.md",
        "\n".join(
            [
                f"# Final decision — {OPERATION_ID}",
                "",
                f"- 364 Посuda: **{decisions[364]}**",
                f"- 381 Upakovochnoe: **{decisions[381]}**",
                f"- Hide candidates: {to_hide or 'none'}",
                f"- Keep/repair: {keep or 'none'}",
                f"- Attention: {attention or 'none'}",
            ]
        )
        + "\n",
    )

    applied = False
    hide_now = [cid for cid in to_hide if cid not in attention]
    if hide_now and args.apply_hide:
        rollback = build_rollback_sql(hide_now, snapshots)
        apply_sql = build_hide_sql(hide_now)
        write_text(STORAGE / "rollback" / "rollback.sql", rollback)
        write_text(STORAGE / "production-apply" / "apply.sql", apply_sql)
        mysql_batch(apply_sql)
        cache_out = clear_cache()
        write_text(STORAGE / "cache" / "cache-clear.txt", cache_out)
        applied = True
        write_text(
            STORAGE / "production-apply" / "apply-summary.md",
            "\n".join(
                [
                    f"# Production apply — {OPERATION_ID}",
                    "",
                    f"- Applied temporary hide status=0 for category IDs: {hide_now}",
                    f"- Skipped hide (attention): {[cid for cid in to_hide if cid in attention] or 'none'}",
                    f"- Mechanism: oc_category.status=0 (matches prior tmp-disable pattern)",
                    f"- Product rows changed: 0",
                    f"- Cache cleared: yes",
                ]
            )
            + "\n",
        )
    elif to_hide:
        write_text(
            STORAGE / "production-apply" / "apply-summary.md",
            f"# Production apply — {OPERATION_ID}\n\nNo mutation — dry-run only. Hide recommended for {to_hide}.\n",
        )
        write_text(STORAGE / "rollback" / "rollback.sql", build_rollback_sql(to_hide, snapshots))
    else:
        write_text(
            STORAGE / "production-apply" / "apply-summary.md",
            f"# Production apply — {OPERATION_ID}\n\nNo production mutation required.\n",
        )
        write_text(STORAGE / "rollback" / "rollback.sql", f"-- No mutation for {OPERATION_ID}\n")

    public_after = public_smoke("after" if applied else "after-noop")
    write_csv(
        STORAGE / "public-after" / "public-after-smoke.csv",
        public_after,
        [
            "phase",
            "key",
            "url",
            "http_status",
            "final_url",
            "product_cards",
            "category_cards",
            "root_sections",
            "posuda_slug_visible",
            "upak_slug_visible",
            "php_warning",
            "bzpm_marker",
            "h1",
        ],
    )
    write_text(
        STORAGE / "public-after" / "public-after-summary.md",
        "\n".join(
            [
                f"# Public after — {OPERATION_ID}",
                "",
                f"- Applied hide: {applied}",
                *[f"- {r['key']}: HTTP {r['http_status']} products={r['product_cards']} h1={r['h1']!r}" for r in public_after],
            ]
        )
        + "\n",
    )

    write_text(
        STORAGE / "regression" / "regression-summary.md",
        "\n".join(
            [
                f"# Regression — {OPERATION_ID}",
                "",
                f"- Categories touched: {hide_now if applied else 'none'}",
                f"- Attention (no hide): {attention or 'none'}",
                f"- Product rows changed: 0",
                f"- Import run: 0",
                f"- Baseline refresh: 0",
                f"- Root visual layout/CSS/images: untouched",
                f"- [96] Zapchasti: untouched",
            ]
        )
        + "\n",
    )
    write_csv(
        STORAGE / "regression" / "mutation-summary.csv",
        [
            {
                "entity": "oc_category",
                "category_id": cid,
                "action": "status=0 temporary hide" if applied else "none",
            }
            for cid in (hide_now if applied else [])
        ]
        or [{"entity": "none", "category_id": "", "action": "no mutation"}],
        ["entity", "category_id", "action"],
    )

    summary = {
        "operation": OPERATION_ID,
        "decisions": decisions,
        "to_hide": to_hide,
        "applied": applied,
        "attention": attention,
        "snapshots": snapshots,
        "public_before": public_before,
        "public_after": public_after,
    }
    write_json(STORAGE / "reports" / "run-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
