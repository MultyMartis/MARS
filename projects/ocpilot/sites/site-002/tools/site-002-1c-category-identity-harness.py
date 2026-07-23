#!/usr/bin/env python3
"""SITE-002 1C Category Identity Harness — read-only XML ↔ DB mapping analysis.

Operation: SITE-002-PROD-1C-CATEGORY-IDENTITY-HARNESS-01 (OCPilot Run 4.293)

Modes:
  --xml + --db-snapshot-dir  (default): analyze local snapshots only
  --fetch-live              : FTP-download import XML + SSH SELECT snapshot, then analyze

Never writes to production DB/FTP. Never triggers import/admin/cache.
Credentials are read from secrets.md and never printed or written to outputs.
"""

from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import json
import re
import shlex
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-1C-CATEGORY-IDENTITY-HARNESS-01"
OCPILOT_RUN = "4.293"
SITE_ID = "SITE-002"
PRODUCTION_URL = "https://bzpm.ru/"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEFAULT_STORAGE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
REMOTE_IMPORT_XML = "public_html/1c_incoming/webdata/import0_1.xml"
CML_NS = {"cml": "urn:1C.ru:commerceml_2"}

# Legacy collision leaves under Электромеханическое оборудование (153)
LEGACY_LEAF_IDS = {154, 159, 165}
LEGACY_ROOT_ID = 153
TECH_ROOT_ID = 362

# Known interim hubs when canonical leaf missing
KNOWN_GUID_HINTS: dict[str, dict[str, Any]] = {
    "e0fd5c42-a3b8-11ea-8152-a85e4515c4f4": {"name": "ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ", "hint_id": 362},
    "2adc2489-7c1a-11f1-aecc-581122cf362c": {"name": "Мясоперерабатывающее", "hint_id": 373},
    "7e43262d-7c1a-11f1-aecc-581122cf362c": {"name": "Мясорубки", "hint_id": None, "hub_id": 373},
    "95003163-7c1a-11f1-aecc-581122cf362c": {"name": "Пилы для мяса", "hint_id": None, "hub_id": 373},
    "e0b6bb6d-7c1a-11f1-aecc-581122cf362c": {"name": "Слайсеры для мяса", "hint_id": 376},
    "bac3dc26-7c19-11f1-aecc-581122cf362c": {"name": "Электромеханическое", "hint_id": 375},
    "41a86281-7c1b-11f1-aecc-581122cf362c": {"name": "Хлеборезки", "hint_id": None, "hub_id": 375},
}

FOCUS_DEFAULT = "4707,4708,4709,4710,4712"


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
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fields})


def local_tag(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[-1]
    return tag


def parse_production_section(path: Path, subsection: str | None = None) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
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


def ftp_download(remote_path: str, dest: Path) -> dict[str, Any]:
    fields = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(fields["host"], int(fields.get("port") or 21), timeout=300)
    ftp.login(fields["username"], fields["password"])
    ftp.voidcmd("TYPE I")
    buf: list[bytes] = []
    try:
        ftp.retrbinary("RETR " + remote_path, buf.append)
    except ftplib.error_perm as exc:
        # try leading slash variants
        alt = remote_path if remote_path.startswith("/") else "/" + remote_path
        try:
            buf.clear()
            ftp.retrbinary("RETR " + alt, buf.append)
            remote_path = alt
        except ftplib.error_perm:
            ftp.quit()
            return {"ok": False, "error": str(exc), "remote": remote_path}
    finally:
        try:
            ftp.quit()
        except Exception:
            pass
    data = b"".join(buf)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    return {
        "ok": True,
        "remote": remote_path,
        "local": str(dest),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "mtime_utc": utc_now(),
    }


def ssh_mysql(sql: str, timeout: int = 180) -> str:
    import paramiko  # type: ignore

    ssh_fields = parse_production_section(SECRETS_PATH, "SSH")
    db = parse_production_section(SECRETS_PATH, "Database")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        ssh_fields["host"],
        port=int(ssh_fields.get("port") or 22),
        username=ssh_fields["username"],
        password=ssh_fields["password"],
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    esc = sql.replace("\\", "\\\\").replace('"', '\\"')
    cmd = (
        f'MYSQL_PWD={shlex.quote(db["password"])} mysql -N -B '
        f'-u {shlex.quote(db["username"])} {shlex.quote(db["database"])} '
        f'-e "{esc}" 2>&1'
    )
    _i, out, err = client.exec_command(cmd, timeout=timeout)
    text = out.read().decode("utf-8", errors="replace") + err.read().decode(
        "utf-8", errors="replace"
    )
    client.close()
    if "ERROR" in text or "Access denied" in text:
        raise RuntimeError(f"MySQL SELECT failed (credentials redacted): {text[:400]}")
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


def norm_name(name: str) -> str:
    return re.sub(r"\s+", " ", (name or "").strip().casefold())


def path_key(parts: list[str]) -> str:
    return " > ".join(parts)


# --- XML parse -----------------------------------------------------------------


def parse_groups(root: ET.Element) -> list[dict[str, Any]]:
    groups: list[dict[str, Any]] = []

    def walk(el: ET.Element, parent_id: str | None, name_path: list[str], id_path: list[str]) -> None:
        if local_tag(el.tag) != "Группа":
            for child in el:
                walk(child, parent_id, name_path, id_path)
            return
        gid = ""
        gname = ""
        children_el: ET.Element | None = None
        for child in el:
            t = local_tag(child.tag)
            if t == "Ид":
                gid = (child.text or "").strip()
            elif t == "Наименование":
                gname = (child.text or "").strip()
            elif t == "Группы":
                children_el = child
        if not gid:
            return
        npath = name_path + [gname]
        ipath = id_path + [gid]
        groups.append(
            {
                "source_group_id": gid,
                "source_name": gname,
                "parent_group_id": parent_id or "",
                "full_path_names": path_key(npath),
                "full_path_ids": path_key(ipath),
                "leaf_name": gname,
                "depth": len(npath),
            }
        )
        if children_el is not None:
            for sub in children_el:
                walk(sub, gid, npath, ipath)

    # Prefer classifier groups
    for el in root.iter():
        if local_tag(el.tag) == "Классификатор":
            for child in el:
                if local_tag(child.tag) == "Группы":
                    for g in child:
                        walk(g, None, [], [])
            break
    if not groups:
        # fallback: any top-level nested groups
        for el in root.iter():
            if local_tag(el.tag) == "Группы":
                for g in list(el):
                    if local_tag(g.tag) == "Группа":
                        walk(g, None, [], [])
                break
    return groups


def parse_products(root: ET.Element, group_index: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    products: list[dict[str, Any]] = []
    for el in root.iter():
        if local_tag(el.tag) != "Товар":
            continue
        pid = ""
        name = ""
        article = ""
        group_ids: list[str] = []
        for child in el:
            t = local_tag(child.tag)
            if t == "Ид" and not pid:
                pid = (child.text or "").strip()
            elif t == "Наименование":
                name = (child.text or "").strip()
            elif t == "Артикул":
                article = (child.text or "").strip()
            elif t == "Группы":
                for g in child:
                    if local_tag(g.tag) == "Ид":
                        gid = (g.text or "").strip()
                        if gid:
                            group_ids.append(gid)
        if not pid:
            continue
        paths = []
        leaves = []
        for gid in group_ids:
            g = group_index.get(gid)
            if g:
                paths.append(g["full_path_names"])
                leaves.append(g["leaf_name"])
            else:
                paths.append("")
                leaves.append("")
        products.append(
            {
                "product_xml_id": pid,
                "product_name": name,
                "article": article,
                "source_group_ids": group_ids,
                "source_full_paths": paths,
                "source_leaf_names": leaves,
            }
        )
    return products


def load_xml(path: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    meta: dict[str, Any] = {
        "xml_path": str(path),
        "bytes": path.stat().st_size if path.exists() else 0,
        "sha256": "",
        "parse_ok": False,
        "error": "",
    }
    if not path.exists():
        meta["error"] = "xml path missing"
        return [], [], meta
    data = path.read_bytes()
    meta["sha256"] = hashlib.sha256(data).hexdigest()
    try:
        root = ET.fromstring(data)
    except ET.ParseError as exc:
        meta["error"] = f"XML ParseError: {exc}"
        return [], [], meta
    groups = parse_groups(root)
    gindex = {g["source_group_id"]: g for g in groups}
    products = parse_products(root, gindex)
    meta["parse_ok"] = True
    meta["group_count"] = len(groups)
    meta["product_count"] = len(products)
    return groups, products, meta


# --- DB snapshot ---------------------------------------------------------------


def fetch_db_snapshot(out_dir: Path) -> dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    summary: dict[str, Any] = {"fetched_at": utc_now(), "ok": False, "selects": 0}

    cat_sql = (
        "SELECT c.category_id, IFNULL(cd.name,''), c.parent_id, c.status, c.sort_order, "
        "IFNULL(c.image,''), IFNULL(su.keyword,'') "
        "FROM oc_category c "
        "LEFT JOIN oc_category_description cd ON c.category_id=cd.category_id AND cd.language_id=1 "
        "LEFT JOIN oc_seo_url su ON su.store_id=0 AND su.language_id=1 "
        "AND su.query=CONCAT('category_id=', c.category_id) "
        "ORDER BY c.category_id"
    )
    path_sql = "SELECT category_id, path_id, level FROM oc_category_path ORDER BY category_id, level"
    pcount_sql = (
        "SELECT category_id, COUNT(*) FROM oc_product_to_category GROUP BY category_id"
    )
    crit_sql = (
        "SELECT p.product_id, IFNULL(p.xml_id,''), IFNULL(pd.name,''), IFNULL(p.model,''), "
        "IFNULL(p.sku,''), p.status, IFNULL(su.keyword,'') "
        "FROM oc_product p "
        "LEFT JOIN oc_product_description pd ON p.product_id=pd.product_id AND pd.language_id=1 "
        "LEFT JOIN oc_seo_url su ON su.store_id=0 AND su.language_id=1 "
        "AND su.query=CONCAT('product_id=', p.product_id) "
        "WHERE p.product_id IN (4707,4708,4709,4710,4712) "
        "OR p.xml_id IN ("
        "'56ccee94-e203-11ea-a988-a85e4515c4f4',"
        "SELECT xml_id FROM (SELECT xml_id FROM oc_product WHERE product_id IN (4707,4708,4709,4710,4712)) t"
        ") "
        "ORDER BY p.product_id"
    )
    # Simpler critical products query
    crit_sql = (
        "SELECT p.product_id, IFNULL(p.xml_id,''), IFNULL(pd.name,''), IFNULL(p.model,''), "
        "IFNULL(p.sku,''), p.status, IFNULL(su.keyword,'') "
        "FROM oc_product p "
        "LEFT JOIN oc_product_description pd ON p.product_id=pd.product_id AND pd.language_id=1 "
        "LEFT JOIN oc_seo_url su ON su.store_id=0 AND su.language_id=1 "
        "AND su.query=CONCAT('product_id=', p.product_id) "
        "WHERE p.product_id IN (4707,4708,4709,4710,4712) "
        "ORDER BY p.product_id"
    )
    rel_sql = (
        "SELECT ptc.product_id, ptc.category_id, ptc.main_category, IFNULL(p.xml_id,''), IFNULL(pd.name,'') "
        "FROM oc_product_to_category ptc "
        "JOIN oc_product p ON p.product_id=ptc.product_id "
        "LEFT JOIN oc_product_description pd ON p.product_id=pd.product_id AND pd.language_id=1 "
        "WHERE ptc.product_id IN (4707,4708,4709,4710,4712) "
        "OR ptc.category_id IN (153,154,159,165,362,373,375,376) "
        "ORDER BY ptc.product_id, ptc.category_id"
    )
    # Also pull all products assigned to collision leaves + tech hubs for context
    leaf_collision_sql = (
        "SELECT LOWER(cd.name) AS leaf, GROUP_CONCAT(c.category_id ORDER BY c.category_id) AS ids, "
        "COUNT(*) AS cnt "
        "FROM oc_category c "
        "JOIN oc_category_description cd ON c.category_id=cd.category_id AND cd.language_id=1 "
        "GROUP BY LOWER(cd.name) HAVING COUNT(*)>1 ORDER BY cnt DESC, leaf"
    )

    cat_rows = parse_tsv(ssh_mysql(cat_sql))
    summary["selects"] += 1
    path_rows = parse_tsv(ssh_mysql(path_sql))
    summary["selects"] += 1
    pcount_rows = parse_tsv(ssh_mysql(pcount_sql))
    summary["selects"] += 1
    crit_rows = parse_tsv(ssh_mysql(crit_sql))
    summary["selects"] += 1
    rel_rows = parse_tsv(ssh_mysql(rel_sql))
    summary["selects"] += 1
    leaf_rows = parse_tsv(ssh_mysql(leaf_collision_sql))
    summary["selects"] += 1

    # Build category index
    cats: dict[int, dict[str, Any]] = {}
    for r in cat_rows:
        if len(r) < 7:
            continue
        cid = int(r[0])
        cats[cid] = {
            "category_id": cid,
            "name": r[1],
            "parent_id": int(r[2] or 0),
            "status": int(r[3] or 0),
            "sort_order": int(r[4] or 0),
            "image": r[5],
            "seo_keyword": r[6],
            "path_ids": [],
            "full_path_names": "",
            "product_direct_count": 0,
            "product_subtree_count": 0,
        }

    for r in path_rows:
        if len(r) < 3:
            continue
        cid = int(r[0])
        path_id = int(r[1])
        level = int(r[2])
        if cid in cats:
            # ensure list sized
            while len(cats[cid]["path_ids"]) <= level:
                cats[cid]["path_ids"].append(0)
            cats[cid]["path_ids"][level] = path_id

    for cid, c in cats.items():
        names = []
        for pid in c["path_ids"]:
            if pid in cats:
                names.append(cats[pid]["name"])
        c["full_path_names"] = path_key(names) if names else c["name"]
        c["full_path_ids"] = " > ".join(str(x) for x in c["path_ids"])

    for r in pcount_rows:
        if len(r) < 2:
            continue
        cid = int(r[0])
        cnt = int(r[1])
        if cid in cats:
            cats[cid]["product_direct_count"] = cnt

    # subtree counts: sum direct counts for all categories whose path includes cid
    for cid, c in cats.items():
        total = 0
        for other in cats.values():
            if cid in other["path_ids"]:
                total += other["product_direct_count"]
        c["product_subtree_count"] = total

    cat_csv_rows = list(cats.values())
    write_csv(
        out_dir / "categories-snapshot.csv",
        cat_csv_rows,
        [
            "category_id",
            "name",
            "parent_id",
            "status",
            "sort_order",
            "image",
            "seo_keyword",
            "full_path_names",
            "full_path_ids",
            "product_direct_count",
            "product_subtree_count",
        ],
    )
    write_json(out_dir / "categories-snapshot.json", cat_csv_rows)

    products = []
    for r in crit_rows:
        if len(r) < 7:
            continue
        products.append(
            {
                "product_id": int(r[0]),
                "xml_id": r[1],
                "name": r[2],
                "model": r[3],
                "sku": r[4],
                "status": int(r[5] or 0),
                "seo_keyword": r[6],
            }
        )
    write_csv(
        out_dir / "products-critical-snapshot.csv",
        products,
        ["product_id", "xml_id", "name", "model", "sku", "status", "seo_keyword"],
    )
    write_json(out_dir / "products-critical-snapshot.json", products)

    rels = []
    for r in rel_rows:
        if len(r) < 5:
            continue
        rels.append(
            {
                "product_id": int(r[0]),
                "category_id": int(r[1]),
                "main_category": int(r[2] or 0),
                "xml_id": r[3],
                "product_name": r[4],
                "category_path": cats.get(int(r[1]), {}).get("full_path_names", ""),
            }
        )
    write_csv(
        out_dir / "product-category-relations-snapshot.csv",
        rels,
        [
            "product_id",
            "category_id",
            "main_category",
            "xml_id",
            "product_name",
            "category_path",
        ],
    )
    write_json(out_dir / "product-category-relations-snapshot.json", rels)

    leaf_collisions = []
    for r in leaf_rows:
        if len(r) < 3:
            continue
        leaf_collisions.append({"leaf_name_lower": r[0], "category_ids": r[1], "count": r[2]})
    write_csv(
        out_dir / "leaf-name-collisions-db.csv",
        leaf_collisions,
        ["leaf_name_lower", "category_ids", "count"],
    )
    write_json(out_dir / "leaf-name-collisions-db.json", leaf_collisions)

    summary["ok"] = True
    summary["category_count"] = len(cats)
    summary["critical_product_count"] = len(products)
    summary["relation_rows"] = len(rels)
    summary["leaf_collision_names"] = len(leaf_collisions)
    summary["db_writes"] = 0
    write_json(out_dir / "db-readonly-summary.json", summary)
    md = [
        "# DB readonly snapshot\n\n",
        f"- fetched_at: {summary['fetched_at']}\n",
        f"- categories: {summary['category_count']}\n",
        f"- critical products: {summary['critical_product_count']}\n",
        f"- relation rows: {summary['relation_rows']}\n",
        f"- leaf collision names: {summary['leaf_collision_names']}\n",
        f"- SELECT count: {summary['selects']}\n",
        "- DB writes: 0\n",
        "- Credentials: not included\n",
    ]
    write_text(out_dir / "db-readonly-summary.md", "".join(md))
    return summary


def load_db_snapshot(snap_dir: Path) -> dict[str, Any]:
    cats_path = snap_dir / "categories-snapshot.json"
    prod_path = snap_dir / "products-critical-snapshot.json"
    rel_path = snap_dir / "product-category-relations-snapshot.json"
    if not cats_path.exists():
        # try CSV fallback
        cats = []
        with (snap_dir / "categories-snapshot.csv").open(encoding="utf-8") as fh:
            cats = list(csv.DictReader(fh))
        for c in cats:
            c["category_id"] = int(c["category_id"])
            c["parent_id"] = int(c.get("parent_id") or 0)
            c["status"] = int(c.get("status") or 0)
            c["product_direct_count"] = int(c.get("product_direct_count") or 0)
            c["product_subtree_count"] = int(c.get("product_subtree_count") or 0)
    else:
        cats = json.loads(cats_path.read_text(encoding="utf-8"))
    if prod_path.exists():
        products = json.loads(prod_path.read_text(encoding="utf-8"))
    else:
        with (snap_dir / "products-critical-snapshot.csv").open(encoding="utf-8") as fh:
            products = list(csv.DictReader(fh))
            for p in products:
                p["product_id"] = int(p["product_id"])
    if rel_path.exists():
        rels = json.loads(rel_path.read_text(encoding="utf-8"))
    else:
        with (snap_dir / "product-category-relations-snapshot.csv").open(encoding="utf-8") as fh:
            rels = list(csv.DictReader(fh))
            for r in rels:
                r["product_id"] = int(r["product_id"])
                r["category_id"] = int(r["category_id"])
    return {"categories": cats, "products": products, "relations": rels}


# --- Mapping analysis ----------------------------------------------------------


def build_db_indexes(cats: list[dict[str, Any]]) -> dict[str, Any]:
    by_id: dict[int, dict[str, Any]] = {}
    by_path: dict[str, list[int]] = defaultdict(list)
    by_path_norm: dict[str, list[int]] = defaultdict(list)
    by_leaf: dict[str, list[int]] = defaultdict(list)
    for c in cats:
        cid = int(c["category_id"])
        by_id[cid] = c
        fp = c.get("full_path_names") or c.get("name") or ""
        by_path[fp].append(cid)
        by_path_norm[norm_name(fp)].append(cid)
        by_leaf[norm_name(c.get("name") or "")].append(cid)
    return {
        "by_id": by_id,
        "by_path": dict(by_path),
        "by_path_norm": dict(by_path_norm),
        "by_leaf": dict(by_leaf),
    }


def under_legacy_tree(cat: dict[str, Any] | None) -> bool:
    if not cat:
        return False
    path_ids = cat.get("path_ids") or []
    if path_ids:
        return LEGACY_ROOT_ID in path_ids or int(cat.get("category_id") or 0) == LEGACY_ROOT_ID
    # fallback parse full_path_ids string
    fps = str(cat.get("full_path_ids") or "")
    parts = [p.strip() for p in fps.split(">") if p.strip()]
    return str(LEGACY_ROOT_ID) in parts


def under_tech_tree(cat: dict[str, Any] | None) -> bool:
    if not cat:
        return False
    path_ids = cat.get("path_ids") or []
    if path_ids:
        return TECH_ROOT_ID in path_ids or int(cat.get("category_id") or 0) == TECH_ROOT_ID
    fps = str(cat.get("full_path_ids") or "")
    return str(TECH_ROOT_ID) in [p.strip() for p in fps.split(">") if p.strip()]


def propose_category_map(
    groups: list[dict[str, Any]], dbx: dict[str, Any]
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    by_id = dbx["by_id"]
    by_path = dbx["by_path"]
    by_path_norm = dbx["by_path_norm"]
    by_leaf = dbx["by_leaf"]

    for g in groups:
        gid = g["source_group_id"]
        leaf = g["leaf_name"]
        full = g["full_path_names"]
        leaf_ids = by_leaf.get(norm_name(leaf), [])
        collision = len(leaf_ids) > 1
        exact = by_path.get(full, [])
        # also try tech-normalized: source uses ALL CAPS root names sometimes
        # Build alternate path with Title-case-ish DB names by leaf matching climb — skip; use norm
        exact_norm = by_path_norm.get(norm_name(full), [])
        # Partial: match suffix path of last 2-3 segments against DB paths
        parts = [p for p in full.split(" > ") if p]
        partial_ids: list[int] = []
        if len(parts) >= 2:
            suffix = path_key(parts[-2:])
            for fp, ids in by_path.items():
                if fp.endswith(suffix) or norm_name(fp).endswith(norm_name(suffix)):
                    partial_ids.extend(ids)
        partial_ids = sorted(set(partial_ids))

        hint = KNOWN_GUID_HINTS.get(gid, {})
        proposed: int | None = None
        confidence = "SAFE_UNKNOWN"
        action = "REVIEW_REQUIRED"
        collision_status = "COLLISION" if collision else "NO_COLLISION"
        notes = []

        # Prefer exact path (non-legacy if collision)
        candidates = exact or exact_norm
        if candidates:
            tech_cands = [c for c in candidates if under_tech_tree(by_id.get(c))]
            chosen = tech_cands[0] if tech_cands else candidates[0]
            if under_legacy_tree(by_id.get(chosen)) and any(
                under_tech_tree(by_id.get(c)) for c in leaf_ids
            ):
                tech_leaf = [c for c in leaf_ids if under_tech_tree(by_id.get(c))]
                if tech_leaf:
                    chosen = tech_leaf[0]
                    notes.append("prefer_tech_over_legacy_leaf")
            proposed = chosen
            confidence = "HIGH_FULL_PATH"
            action = "BACKFILL_MAPPING"
        elif hint.get("hint_id"):
            proposed = int(hint["hint_id"])
            confidence = "HIGH_FULL_PATH" if not collision else "MEDIUM_PARENT_PATH"
            # verify path roughly
            cat = by_id.get(proposed)
            if cat and norm_name(cat.get("name") or "") == norm_name(leaf):
                confidence = "HIGH_FULL_PATH"
            action = "BACKFILL_MAPPING"
            notes.append("known_guid_hint")
        elif collision:
            # Prefer tech-tree candidate; never propose legacy 154/159/165 for tech source paths
            tech_cands = [c for c in leaf_ids if under_tech_tree(by_id.get(c))]
            legacy_cands = [c for c in leaf_ids if under_legacy_tree(by_id.get(c))]
            if tech_cands:
                proposed = tech_cands[0]
                confidence = "BLOCKED_COLLISION"
                action = "REVIEW_REQUIRED"
                notes.append(f"leaf_collision tech={tech_cands} legacy={legacy_cands}")
            elif hint.get("hub_id"):
                proposed = int(hint["hub_id"])
                confidence = "CREATE_REQUIRED"
                action = "CREATE_CATEGORY_THEN_MAP"
                notes.append(
                    f"no_tech_leaf; interim_hub={proposed}; legacy_collision={legacy_cands}"
                )
            else:
                confidence = "BLOCKED_COLLISION"
                action = "REVIEW_REQUIRED"
                notes.append(f"leaf_collision ids={leaf_ids}")
        elif leaf_ids and len(leaf_ids) == 1:
            proposed = leaf_ids[0]
            if under_legacy_tree(by_id.get(proposed)) and "ТЕХНОЛОГИЧЕСКОЕ" in full.upper():
                if hint.get("hub_id"):
                    proposed = int(hint["hub_id"])
                    confidence = "CREATE_REQUIRED"
                    action = "CREATE_CATEGORY_THEN_MAP"
                    notes.append("leaf_only_hit_legacy_under_tech_source")
                else:
                    confidence = "LOW_LEAF_ONLY"
                    action = "REVIEW_REQUIRED"
            else:
                confidence = "LOW_LEAF_ONLY"
                action = "BACKFILL_MAPPING"
                notes.append("unique_leaf_only")
        elif hint.get("hub_id"):
            proposed = int(hint["hub_id"])
            confidence = "CREATE_REQUIRED"
            action = "CREATE_CATEGORY_THEN_MAP"
            notes.append("missing_canonical_leaf; interim_hub")
        elif partial_ids:
            tech_partial = [c for c in partial_ids if under_tech_tree(by_id.get(c))]
            proposed = (tech_partial or partial_ids)[0]
            confidence = "MEDIUM_PARENT_PATH"
            action = "REVIEW_REQUIRED"
            notes.append(f"partial_path={partial_ids}")
        else:
            confidence = "CREATE_REQUIRED"
            action = "CREATE_CATEGORY_THEN_MAP"
            notes.append("no_db_match")

        # GUID mapping status — DB has no external id
        guid_map_status = "NO_DB_MAPPING_EXISTS_YET"

        proposed_path = ""
        if proposed and proposed in by_id:
            proposed_path = by_id[proposed].get("full_path_names") or by_id[proposed].get("name")

        # Old importer leaf target (first match in global leaf index — PHP typically last-wins or first; unknown order)
        old_importer_target = ""
        if leaf_ids:
            # Prefer documenting risk: if legacy in set, old importer may pick legacy
            legacy = [c for c in leaf_ids if c in LEGACY_LEAF_IDS or under_legacy_tree(by_id.get(c))]
            old_importer_target = str((legacy or leaf_ids)[0])

        rows.append(
            {
                "source_group_id": gid,
                "source_name": leaf,
                "parent_group_id": g.get("parent_group_id", ""),
                "source_full_path": full,
                "source_full_path_ids": g.get("full_path_ids", ""),
                "guid_map_status": guid_map_status,
                "db_exact_path_ids": ";".join(str(x) for x in (exact or exact_norm)),
                "db_leaf_ids": ";".join(str(x) for x in leaf_ids),
                "collision_status": collision_status,
                "proposed_category_id": proposed if proposed is not None else "",
                "proposed_category_path": proposed_path,
                "confidence": confidence,
                "action": action,
                "old_importer_likely_category_id": old_importer_target,
                "notes": "; ".join(notes),
            }
        )
    return rows


def propose_product_map(
    products: list[dict[str, Any]],
    cat_map: list[dict[str, Any]],
    db_products: list[dict[str, Any]],
    db_rels: list[dict[str, Any]],
    dbx: dict[str, Any],
    focus_ids: set[int],
) -> list[dict[str, Any]]:
    by_guid = {r["source_group_id"]: r for r in cat_map}
    db_by_xml = {p.get("xml_id"): p for p in db_products if p.get("xml_id")}
    db_by_id = {int(p["product_id"]): p for p in db_products}
    rels_by_pid: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for r in db_rels:
        rels_by_pid[int(r["product_id"])].append(r)

    # Build xml->db product for focus: also match by xml from relations
    for r in db_rels:
        xml = r.get("xml_id") or ""
        if xml and xml not in db_by_xml:
            db_by_xml[xml] = {
                "product_id": int(r["product_id"]),
                "xml_id": xml,
                "name": r.get("product_name") or "",
            }

    rows: list[dict[str, Any]] = []
    # Focus products: ensure we emit rows even if we look up by DB first
    focus_xmls = {p.get("xml_id") for p in db_products if int(p["product_id"]) in focus_ids}

    # Index source products by xml id
    src_by_xml = {p["product_xml_id"]: p for p in products}

    # Emit for all focus DB products + any source products in focus xml set
    emit_xmls = set(focus_xmls)
    for p in products:
        # include if matches focus product names/articles loosely via DB xml
        if p["product_xml_id"] in focus_xmls:
            emit_xmls.add(p["product_xml_id"])

    # Also map DB focus products always
    for pid in sorted(focus_ids):
        dbp = db_by_id.get(pid)
        if not dbp:
            rows.append(
                {
                    "product_id": pid,
                    "product_xml_id": "",
                    "product_name": "",
                    "source_group_ids": "",
                    "source_full_paths": "",
                    "current_db_category_ids": "",
                    "current_db_category_paths": "",
                    "proposed_category_ids": "",
                    "proposed_category_paths": "",
                    "current_matches_proposed": "SAFE_UNKNOWN",
                    "old_importer_likely_category_ids": "",
                    "collision_risk": "YES",
                    "action": "SAFE_UNKNOWN",
                    "notes": "product missing from DB snapshot",
                }
            )
            continue
        xml = dbp.get("xml_id") or ""
        src = src_by_xml.get(xml)
        rels = rels_by_pid.get(pid, [])
        cur_ids = [int(r["category_id"]) for r in rels]
        cur_paths = [r.get("category_path") or dbx["by_id"].get(int(r["category_id"]), {}).get("full_path_names", "") for r in rels]

        proposed_ids: list[int] = []
        proposed_paths: list[str] = []
        old_ids: list[str] = []
        src_paths: list[str] = []
        src_gids: list[str] = []
        confidences: list[str] = []

        if src:
            src_gids = list(src.get("source_group_ids") or [])
            src_paths = list(src.get("source_full_paths") or [])
            for gid in src_gids:
                m = by_guid.get(gid)
                if not m:
                    continue
                pc = m.get("proposed_category_id")
                if pc != "" and pc is not None:
                    proposed_ids.append(int(pc))
                    proposed_paths.append(m.get("proposed_category_path") or "")
                if m.get("old_importer_likely_category_id"):
                    old_ids.append(str(m["old_importer_likely_category_id"]))
                confidences.append(m.get("confidence") or "")
        else:
            src_paths = ["SAFE_UNKNOWN_SOURCE_PRODUCT_NOT_IN_XML"]

        proposed_ids = sorted(set(proposed_ids))
        match = "NO"
        if proposed_ids and set(cur_ids) == set(proposed_ids):
            match = "YES"
        elif proposed_ids and set(cur_ids) & set(proposed_ids):
            match = "PARTIAL"
        elif not src:
            match = "SAFE_UNKNOWN"

        action = "KEEP"
        notes = []
        if any(c in ("CREATE_REQUIRED",) for c in confidences):
            action = "CREATE_CATEGORY_REQUIRED"
            notes.append("canonical_leaf_missing")
        if proposed_ids and set(cur_ids) != set(proposed_ids):
            if action == "KEEP":
                action = "WOULD_MOVE_TO_CANONICAL"
        # Old importer risk
        old_int = []
        for x in old_ids:
            try:
                old_int.append(int(x))
            except ValueError:
                pass
        if any(x in LEGACY_LEAF_IDS for x in old_int) or (
            old_int and set(old_int) != set(cur_ids) and any(x in LEGACY_LEAF_IDS for x in old_int)
        ):
            notes.append("old_importer_may_revert_to_legacy")
            if set(cur_ids) != set(old_int):
                action = "WOULD_REVERT_TO_LEGACY_UNDER_OLD_IMPORTER"
        if not src:
            action = "SAFE_UNKNOWN"
            notes.append("xml_product_not_found")

        collision_risk = "YES" if any("COLLISION" in (by_guid.get(g, {}).get("collision_status") or "") or by_guid.get(g, {}).get("confidence") == "BLOCKED_COLLISION" for g in src_gids) else "NO"
        if any(c == "CREATE_REQUIRED" for c in confidences):
            collision_risk = "YES"

        rows.append(
            {
                "product_id": pid,
                "product_xml_id": xml,
                "product_name": dbp.get("name") or (src or {}).get("product_name") or "",
                "source_group_ids": ";".join(src_gids),
                "source_full_paths": " || ".join(src_paths),
                "current_db_category_ids": ";".join(str(x) for x in cur_ids),
                "current_db_category_paths": " || ".join(cur_paths),
                "proposed_category_ids": ";".join(str(x) for x in proposed_ids),
                "proposed_category_paths": " || ".join(proposed_paths),
                "current_matches_proposed": match,
                "old_importer_likely_category_ids": ";".join(old_ids),
                "collision_risk": collision_risk,
                "action": action,
                "notes": "; ".join(notes),
            }
        )
    return rows


def analyze(
    xml_path: Path,
    snap_dir: Path,
    out_dir: Path,
    focus_products: list[int],
) -> dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    groups, products, xml_meta = load_xml(xml_path)
    write_json(out_dir / "source-groups.json", groups)
    write_json(out_dir / "source-products.json", products)
    write_json(out_dir / "xml-meta.json", xml_meta)

    if not xml_meta.get("parse_ok"):
        summary = {
            "operation_id": OPERATION_ID,
            "ocpilot_run": OCPILOT_RUN,
            "status": "HARNESS_PARTIAL_XML_PARSE_LIMITATION",
            "xml_meta": xml_meta,
            "generated_at": utc_now(),
        }
        write_json(out_dir / "summary.json", summary)
        write_text(
            out_dir / "summary.md",
            "# Harness summary\n\nXML parse failed or incomplete.\n\n"
            + json.dumps(xml_meta, ensure_ascii=False, indent=2),
        )
        return summary

    db = load_db_snapshot(snap_dir)
    dbx = build_db_indexes(db["categories"])
    write_json(
        out_dir / "db-category-index.json",
        {
            "category_count": len(dbx["by_id"]),
            "leaf_collision_count": sum(1 for ids in dbx["by_leaf"].values() if len(ids) > 1),
            "categories": list(dbx["by_id"].values()),
        },
    )

    cat_map = propose_category_map(groups, dbx)
    write_csv(
        out_dir / "proposed-category-map.csv",
        cat_map,
        [
            "source_group_id",
            "source_name",
            "parent_group_id",
            "source_full_path",
            "source_full_path_ids",
            "guid_map_status",
            "db_exact_path_ids",
            "db_leaf_ids",
            "collision_status",
            "proposed_category_id",
            "proposed_category_path",
            "confidence",
            "action",
            "old_importer_likely_category_id",
            "notes",
        ],
    )

    # leaf collisions focused
    leaf_rows = []
    for leaf, ids in sorted(dbx["by_leaf"].items(), key=lambda x: (-len(x[1]), x[0])):
        if len(ids) < 2:
            continue
        leaf_rows.append(
            {
                "leaf_name": dbx["by_id"][ids[0]].get("name") if ids else leaf,
                "leaf_name_norm": leaf,
                "category_ids": ";".join(str(i) for i in ids),
                "paths": " || ".join(dbx["by_id"][i].get("full_path_names", "") for i in ids),
                "legacy_ids": ";".join(str(i) for i in ids if under_legacy_tree(dbx["by_id"].get(i))),
                "tech_ids": ";".join(str(i) for i in ids if under_tech_tree(dbx["by_id"].get(i))),
            }
        )
    write_csv(
        out_dir / "leaf-collisions.csv",
        leaf_rows,
        ["leaf_name", "leaf_name_norm", "category_ids", "paths", "legacy_ids", "tech_ids"],
    )

    prod_map = propose_product_map(
        products, cat_map, db["products"], db["relations"], dbx, set(focus_products)
    )
    write_csv(
        out_dir / "proposed-product-map.csv",
        prod_map,
        [
            "product_id",
            "product_xml_id",
            "product_name",
            "source_group_ids",
            "source_full_paths",
            "current_db_category_ids",
            "current_db_category_paths",
            "proposed_category_ids",
            "proposed_category_paths",
            "current_matches_proposed",
            "old_importer_likely_category_ids",
            "collision_risk",
            "action",
            "notes",
        ],
    )
    # critical products = focus subset
    crit = [r for r in prod_map if int(r["product_id"]) in set(focus_products)]
    write_csv(
        out_dir / "critical-products.csv",
        crit,
        list(prod_map[0].keys()) if prod_map else [
            "product_id",
            "product_xml_id",
            "product_name",
            "action",
        ],
    )

    create_needed = sum(1 for r in cat_map if r.get("confidence") == "CREATE_REQUIRED")
    focus_create = any(r.get("action") == "CREATE_CATEGORY_REQUIRED" for r in crit)
    focus_revert = any(
        r.get("action") == "WOULD_REVERT_TO_LEGACY_UNDER_OLD_IMPORTER" for r in crit
    )

    if create_needed or focus_create:
        harness_class = "HARNESS_COMPLETE_LEAF_CREATION_NEEDED"
        next_phase = "READY_FOR_LEAF_CREATION_CHARTER"
        verdict = (
            "SITE-002 1C CATEGORY IDENTITY HARNESS COMPLETE — LEAF CREATION NEEDED BEFORE BACKFILL"
        )
    else:
        harness_class = "HARNESS_COMPLETE_MAPPING_READY"
        next_phase = "READY_FOR_MAPPING_TABLE_BACKFILL"
        verdict = "SITE-002 1C CATEGORY IDENTITY HARNESS COMPLETE — MAPPING READY FOR BACKFILL"

    # If critical products mostly map to hubs with create flags — leaf creation
    summary = {
        "operation_id": OPERATION_ID,
        "ocpilot_run": OCPILOT_RUN,
        "site_id": SITE_ID,
        "production_url": PRODUCTION_URL,
        "generated_at": utc_now(),
        "xml_meta": xml_meta,
        "group_count": len(groups),
        "product_count_in_xml": len(products),
        "category_map_rows": len(cat_map),
        "leaf_collision_names": len(leaf_rows),
        "create_required_groups": create_needed,
        "critical_products": crit,
        "harness_classification": harness_class,
        "next_phase_classification": next_phase,
        "verdict": verdict,
        "focus_old_importer_revert_risk": focus_revert,
        "production_mutation": {
            "ftp_writes": 0,
            "db_writes": 0,
            "admin_saves": 0,
            "import_runs": 0,
        },
    }
    write_json(out_dir / "summary.json", summary)

    md_lines = [
        f"# Harness summary — {OPERATION_ID}\n\n",
        f"**Verdict:** `{verdict}`\n\n",
        f"- Classification: `{harness_class}`\n",
        f"- Next phase: `{next_phase}`\n",
        f"- XML groups: {len(groups)}\n",
        f"- XML products: {len(products)}\n",
        f"- Leaf collision names: {len(leaf_rows)}\n",
        f"- CREATE_REQUIRED groups: {create_needed}\n",
        f"- Old importer revert risk on focus: {focus_revert}\n\n",
        "## Critical products\n\n",
    ]
    for r in crit:
        md_lines.append(
            f"- **{r['product_id']}** {r['product_name']}: "
            f"src=`{r['source_full_paths']}` current=`{r['current_db_category_ids']}` "
            f"proposed=`{r['proposed_category_ids']}` action=`{r['action']}`\n"
        )
    write_text(out_dir / "summary.md", "".join(md_lines))
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="SITE-002 1C category identity harness (read-only)")
    parser.add_argument("--xml", type=Path, help="Path to import0_1.xml (or CommerceML catalog)")
    parser.add_argument("--db-snapshot-dir", type=Path, help="Directory with DB snapshot CSV/JSON")
    parser.add_argument("--out", type=Path, required=True, help="Output directory")
    parser.add_argument("--site-id", default=SITE_ID)
    parser.add_argument("--focus-products", default=FOCUS_DEFAULT)
    parser.add_argument(
        "--fetch-live",
        action="store_true",
        help="FTP-download latest import XML + SSH SELECT DB snapshot into storage, then analyze",
    )
    parser.add_argument(
        "--storage-root",
        type=Path,
        default=DEFAULT_STORAGE,
        help="Operation storage root for fetch-live artifacts",
    )
    args = parser.parse_args()

    focus = [int(x.strip()) for x in args.focus_products.split(",") if x.strip()]
    storage = args.storage_root
    xml_path = args.xml
    snap_dir = args.db_snapshot_dir

    if args.fetch_live:
        xml_dir = storage / "xml-input"
        snap_dir = storage / "db-readonly"
        xml_path = xml_dir / "import0_1.xml"
        print("[fetch] FTP download import0_1.xml (read-only RETR)...", flush=True)
        meta = ftp_download(REMOTE_IMPORT_XML, xml_path)
        write_json(xml_dir / "ftp-download-meta.json", meta)
        if not meta.get("ok"):
            print(f"[fetch] FTP failed: {meta}", flush=True)
            write_json(
                args.out / "summary.json",
                {
                    "status": "HARNESS_BLOCKED_SOURCE_UNAVAILABLE",
                    "ftp": meta,
                    "generated_at": utc_now(),
                },
            )
            return 2
        print(f"[fetch] XML bytes={meta['bytes']} sha256={meta['sha256'][:16]}...", flush=True)
        print("[fetch] DB readonly snapshot via SSH SELECT...", flush=True)
        try:
            db_sum = fetch_db_snapshot(snap_dir)
        except Exception as exc:
            write_json(
                args.out / "summary.json",
                {
                    "status": "HARNESS_BLOCKED_DB_SNAPSHOT_UNAVAILABLE",
                    "error": str(exc)[:500],
                    "generated_at": utc_now(),
                },
            )
            print(f"[fetch] DB snapshot failed: {exc}", flush=True)
            return 3
        print(f"[fetch] DB ok categories={db_sum.get('category_count')}", flush=True)

    if not xml_path or not snap_dir:
        print("ERROR: --xml and --db-snapshot-dir required unless --fetch-live", file=sys.stderr)
        return 1
    if not xml_path.exists():
        print(f"ERROR: XML missing: {xml_path}", file=sys.stderr)
        return 2
    if not (snap_dir / "categories-snapshot.csv").exists() and not (
        snap_dir / "categories-snapshot.json"
    ).exists():
        print(f"ERROR: DB snapshot missing in {snap_dir}", file=sys.stderr)
        return 3

    summary = analyze(xml_path, snap_dir, args.out, focus)
    print(summary.get("verdict") or summary.get("status") or "DONE", flush=True)
    print(f"Wrote outputs to {args.out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
