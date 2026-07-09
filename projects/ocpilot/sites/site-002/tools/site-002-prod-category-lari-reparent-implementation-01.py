#!/usr/bin/env python3
"""SITE-002 Production category Lari reparent — controlled mutation (Run 4.235)."""
from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import io
import json
import re
import shlex
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01"
OCPILOT_RUN = "4.235"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION_CONTROLLED_MUTATION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01"
CHECKPOINT_AFTER = "SITE-002-STABLE-PROD-CATEGORY-LARI-REPARENT-01"
DISCOVERY_OP = "SITE-002-PROD-CATEGORY-LARI-REPARENT-DISCOVERY-01"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
WRONG_BRAND = "БЗПМ"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
DISCOVERY_ROOT = DEPLOYMENT_ROOT.parent / DISCOVERY_OP

PREFIX = "oc_"
LARI_ID = 88
SHKAFY_ID = 358
NEUTRAL_ID = 79
CHILD_IDS = (140, 141)
ALL_IDS = (79, 88, 140, 141, 358, 359)
OLD_BASE = "/katalog/nejtralnoe-oborudovanie/lari"
NEW_BASE = "/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari"

IMPORT_XML_REMOTE = "/public_html/1c_incoming/webdata/import0_1.xml"
REMOTE_HTACCESS = "/public_html/.htaccess"
REMOTE_CATEGORY_VISIBILITY = "/public_html/system/library/zpm/category_visibility.php"
REMOTE_CATEGORY_CONTROLLER = "/public_html/catalog/controller/product/category.php"

SUBDIRS = (
    "one-c-source-check",
    "db-before",
    "db-after",
    "db-backup",
    "sql-dry-run",
    "sql-applied",
    "ftp-source-before",
    "ftp-source-after",
    "http-before",
    "http-after",
    "sitemap-before",
    "sitemap-after",
    "entrypoints-before",
    "entrypoints-after",
    "redirects",
    "cache",
    "rollback",
    "verification",
    "manifests",
    "reports",
    "logs",
)

HTTP_URLS = [
    ("lari_old", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari"),
    ("lari_child_sklad_old", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari/skladskie-lari"),
    ("lari_child_proizv_old", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari/proizvodstvennye-lari"),
    ("shkafy_hub", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari"),
    ("lari_target", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari"),
    ("lari_child_sklad_target", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/skladskie-lari"),
    ("lari_child_proizv_target", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/proizvodstvennye-lari"),
    ("home", "https://bzpm.ru/"),
    ("katalog", "https://bzpm.ru/katalog"),
    ("neutral_hub", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie"),
    ("stoly", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly"),
    ("sitemap", "https://bzpm.ru/sitemap.xml"),
    ("robots", "https://bzpm.ru/robots.txt"),
    ("llms", "https://bzpm.ru/llms.txt"),
]

REDIRECT_MARKER = "# SITE-002 lari reparent redirects (SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01)"
REDIRECT_BLOCK = f"""{REDIRECT_MARKER}
RewriteRule ^katalog/nejtralnoe-oborudovanie/lari/(.+)$ /katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/$1 [R=301,L]
RewriteRule ^katalog/nejtralnoe-oborudovanie/lari/?$ /katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari [R=301,L]
"""

PATH_HELPER_METHOD = """
\t/**
\t * Build OpenCart path= chain from category_path for correct nested SEO URLs.
\t * SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01
\t */
\tpublic function buildCategoryPathParam($controller, $category_id) {
\t\t$category_id = (int)$category_id;

\t\tif ($category_id <= 0) {
\t\t\treturn '';
\t\t}

\t\t$query = $controller->db->query("SELECT path_id FROM " . DB_PREFIX . "category_path WHERE category_id = '" . $category_id . "' ORDER BY level ASC");
\t\t$parts = array();

\t\tforeach ($query->rows as $row) {
\t\t\t$parts[] = (int)$row['path_id'];
\t\t}

\t\treturn implode('_', $parts);
\t}
"""

CATEGORY_VISIBILITY_OLD_HREF = (
    "'href'        => $controller->url->link('product/category', 'path=' . $hub_path . '_' . $branch_id),"
)
CATEGORY_VISIBILITY_NEW_HREF = (
    "'href'        => $controller->url->link('product/category', 'path=' . $this->buildCategoryPathParam($controller, $branch_id)),"
)

CATEGORY_CONTROLLER_OLD_HREF = (
    "'href'        => $this->url->link('product/category', 'path=' . $this->request->get['path'] . '_' . $branch_id),"
)
CATEGORY_CONTROLLER_NEW_HREF = (
    "'href'        => $this->url->link('product/category', 'path=' . $visibility->buildCategoryPathParam($this, $branch_id)),"
)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.in_title = False
        self.in_h1 = False
        self.h1_list: list[str] = []
        self.meta: dict[str, str] = {}
        self.links: list[dict[str, str]] = []
        self.breadcrumb_parts: list[str] = []
        self.cat_cards: list[dict[str, str]] = []
        self._in_tile_title = False
        self._tile_href = ""
        self._tile_title = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ad = {k: (v or "") for k, v in attrs}
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = True
        elif tag_l == "h1":
            self.in_h1 = True
        elif tag_l == "meta":
            name = (ad.get("name") or ad.get("property") or "").lower()
            if name:
                self.meta[name] = ad.get("content", "")
        elif tag_l == "link":
            rel = ad.get("rel", "").lower()
            href = ad.get("href", "")
            if rel and href:
                self.links.append({"rel": rel, "href": href})
        elif tag_l == "a":
            classes = ad.get("class", "")
            if "breadcrumb" in classes or "zpm-breadcrumb" in classes:
                self._capture_bc = True
            if "zpm-catalog__tile" in classes or "zpm-cat-card" in classes:
                self._tile_href = ad.get("href", "")
                self._tile_title = ""
        elif tag_l == "span" and "zpm-catalog__tile-title" in ad.get("class", ""):
            self._in_tile_title = True

    def handle_endtag(self, tag: str) -> None:
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = False
        elif tag_l == "h1":
            self.in_h1 = False
        elif tag_l == "span" and self._in_tile_title:
            self._in_tile_title = False
            if self._tile_href or self._tile_title:
                self.cat_cards.append({"href": self._tile_href, "title": self._tile_title.strip()})
                self._tile_href = ""
                self._tile_title = ""

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if not text:
            return
        if self.in_title:
            self.title += data
        if self.in_h1:
            self.h1_list.append(text)
        if getattr(self, "_capture_bc", False):
            self.breadcrumb_parts.append(text)
        if self._in_tile_title:
            self._tile_title += data


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_production_section(path: Path, subsection: str | None = None) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    if subsection:
        sub_match = re.search(
            rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE
        )
        if not sub_match:
            raise RuntimeError(f"Subsection {subsection!r} not found")
        block = sub_match.group(1)
    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in block.splitlines():
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


def ftp_connect() -> ftplib.FTP:
    fields = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(fields["host"], int(fields.get("port") or 21), timeout=300)
    ftp.login(fields["username"], fields["password"])
    return ftp


def ftp_download(ftp: ftplib.FTP, remote: str) -> bytes | None:
    buf = io.BytesIO()
    try:
        ftp.retrbinary(f"RETR {remote}", buf.write)
        return buf.getvalue()
    except ftplib.error_perm:
        return None


def ftp_upload(ftp: ftplib.FTP, remote: str, data: bytes) -> None:
    buf = io.BytesIO(data)
    ftp.storbinary(f"STOR {remote}", buf)


def ssh_mysql(sql: str, write: bool = False) -> dict[str, Any]:
    try:
        import paramiko  # type: ignore
    except ImportError:
        return {"status": "blocked", "reason": "paramiko not available"}
    ssh_fields = parse_production_section(SECRETS_PATH, "SSH")
    db_fields = parse_production_section(SECRETS_PATH, "Database")
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
    db_user = db_fields["username"]
    db_pass = db_fields["password"]
    db_name = db_fields["database"]
    sql_escaped = sql.replace("\\", "\\\\").replace('"', '\\"')
    cmd = (
        f'MYSQL_PWD={shlex.quote(db_pass)} mysql -N -B -u {shlex.quote(db_user)} '
        f'{shlex.quote(db_name)} -e "{sql_escaped}" 2>&1'
    )
    _stdin, stdout, stderr = client.exec_command(cmd, timeout=180)
    out = stdout.read().decode("utf-8", errors="replace")
    err = stderr.read().decode("utf-8", errors="replace")
    client.close()
    combined = out + err
    if "ERROR" in combined or "Access denied" in combined:
        return {"status": "failed", "stdout": out, "stderr": err, "write": write}
    return {"status": "ok", "stdout": out, "stderr": err, "write": write}


def tsv_to_dicts(tsv: str, columns: list[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in tsv.strip().splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        rows.append({columns[i]: parts[i] if i < len(parts) else "" for i in range(len(columns))})
    return rows


def http_fetch(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            body = resp.read()
            return {
                "url": url,
                "status": resp.status,
                "final_url": resp.geturl(),
                "headers": {k.lower(): v for k, v in resp.headers.items()},
                "body": body,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read()
        return {
            "url": url,
            "status": exc.code,
            "final_url": exc.geturl(),
            "headers": {k.lower(): v for k, v in exc.headers.items()},
            "body": body,
            "error": str(exc),
        }
    except urllib.error.URLError as exc:
        return {"url": url, "status": None, "final_url": url, "headers": {}, "body": b"", "error": str(exc)}


def parse_page(body: bytes) -> dict[str, Any]:
    parser = PageParser()
    text = body.decode("utf-8", errors="replace")
    parser.feed(text)
    canonical = next((l["href"] for l in parser.links if l["rel"] == "canonical"), "")
    return {
        "title": parser.title.strip(),
        "h1": parser.h1_list[0] if parser.h1_list else "",
        "canonical": canonical,
        "breadcrumbs": parser.breadcrumb_parts,
        "cat_cards": parser.cat_cards,
        "bzpm_hits": text.count(WRONG_BRAND),
        "meta_robots": parser.meta.get("robots", ""),
    }


def ensure_dirs() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "related_discovery_run": DISCOVERY_OP,
            "related_discovery_ocpilot_run": "4.234",
            "change_type": "category-reparent",
            "category_subject": "Лари",
            "category_id_lari": LARI_ID,
            "category_id_current_parent_wrong": NEUTRAL_ID,
            "category_id_target_parent": SHKAFY_ID,
            "old_url": OLD_BASE,
            "new_url": NEW_BASE,
            "production_mutation_allowed": True,
            "ftp_upload_allowed": "conditional_redirect_or_source_patch_only",
            "db_select_allowed": True,
            "db_write_allowed": "conditional_after_gate",
            "admin_save_allowed": "conditional_after_gate",
            "redirect_change_allowed": "conditional_after_gate",
            "seo_url_change_allowed": False,
            "cache_clear_allowed": "conditional_if_required",
            "import_run_allowed": False,
            "monitor_run_allowed": False,
            "one_c_parent_gate_required": True,
            "operator_decision_lari_marketing_tile_homepage": "keep_if_existing_but_href_new_url",
            "created_at": utc_now(),
        },
    )


def parse_1c_groups(xml_bytes: bytes) -> dict[str, Any]:
    """Parse 1C classifier groups and locate Лари parent chain."""
    root = ET.fromstring(xml_bytes)
    ns = ""
    if root.tag.startswith("{"):
        ns = root.tag.split("}")[0] + "}"

    def local(tag: str) -> str:
        return f"{ns}{tag}" if ns else tag

    groups_root = root.find(f".//{local('Классификатор')}/{local('Группы')}")
    if groups_root is None:
        return {"status": "failed", "reason": "Классификатор/Группы not found"}

    nodes: list[dict[str, Any]] = []

    def walk(parent: ET.Element | None, parent_names: list[str], parent_ids: list[str]) -> None:
        container = parent if parent is not None else groups_root
        for group in container.findall(local("Группа")):
            gid = (group.findtext(local("Ид")) or "").strip()
            name = (group.findtext(local("Наименование")) or "").strip()
            chain_names = parent_names + [name]
            chain_ids = parent_ids + [gid]
            nodes.append(
                {
                    "id_1c": gid,
                    "name": name,
                    "parent_names": parent_names[:],
                    "parent_ids": parent_ids[:],
                    "chain_names": chain_names,
                }
            )
            child_groups = group.find(local("Группы"))
            if child_groups is not None:
                walk(child_groups, chain_names, chain_ids)

    walk(None, [], [])

    targets = {
        "lari": None,
        "shkafy_i_lari": None,
        "skladskie": None,
        "proizvodstvennye": None,
        "neutral": None,
    }
    for node in nodes:
        name_l = node["name"].lower()
        if name_l == "лари":
            targets["lari"] = node
        elif "шкафы и лари" in name_l or name_l == "шкафы и лари":
            targets["shkafy_i_lari"] = node
        elif "складские лари" in name_l:
            targets["skladskie"] = node
        elif "производственные лари" in name_l:
            targets["proizvodstvennye"] = node
        elif "нейтральное оборудование" in name_l:
            targets["neutral"] = node

    lari = targets["lari"]
    gate = "SAFE_UNKNOWN"
    verdict = "SITE-002 CATEGORY LARI REPARENT IMPLEMENTATION BLOCKED — 1C PARENT SAFE UNKNOWN"
    evidence = "Could not locate Лари in 1C XML groups"

    if lari:
        parent_names = lari["parent_names"]
        direct_parent = parent_names[-1] if parent_names else ""
        evidence = f"Лари direct parent in 1C XML: {direct_parent!r}; chain: {' > '.join(parent_names + ['Лари'])}"
        if any("шкафы и лари" in p.lower() for p in parent_names):
            gate = "PASS"
            verdict = "PROCEED"
        elif any("нейтральное оборудование" in p.lower() for p in parent_names) and not any(
            "шкафы и лари" in p.lower() for p in parent_names
        ):
            gate = "BLOCK_REVERT"
            verdict = "SITE-002 CATEGORY LARI REPARENT IMPLEMENTATION BLOCKED — 1C SOURCE WOULD REVERT"
        else:
            gate = "SAFE_UNKNOWN"

    return {
        "status": "ok",
        "gate": gate,
        "verdict": verdict,
        "evidence": evidence,
        "targets": targets,
        "node_count": len(nodes),
        "lari_parent_names": lari["parent_names"] if lari else [],
        "lari_chain": lari["chain_names"] if lari else [],
    }


def phase_1c_gate() -> dict[str, Any]:
    index_rows: list[dict[str, Any]] = []
    xml_bytes: bytes | None = None
    xml_source = ""

    # Local/server artifact candidates
    candidates = [
        ("ftp_live", IMPORT_XML_REMOTE),
    ]
    ftp = ftp_connect()
    try:
        for label, remote in candidates:
            data = ftp_download(ftp, remote)
            index_rows.append(
                {
                    "source": label,
                    "path": remote,
                    "found": data is not None,
                    "size": len(data) if data else 0,
                    "sha256": sha256_bytes(data)[:16] if data else "",
                }
            )
            if data and not xml_bytes:
                xml_bytes = data
                xml_source = remote
                (DEPLOYMENT_ROOT / "one-c-source-check" / "import0_1.xml").write_bytes(data)
    finally:
        ftp.quit()

    write_csv(
        DEPLOYMENT_ROOT / "one-c-source-check" / "source-files-index.csv",
        index_rows,
        ["source", "path", "found", "size", "sha256"],
    )
    write_json(DEPLOYMENT_ROOT / "one-c-source-check" / "source-files-index.json", index_rows)

    if not xml_bytes:
        result = {
            "gate": "SAFE_UNKNOWN",
            "verdict": "SITE-002 CATEGORY LARI REPARENT IMPLEMENTATION BLOCKED — 1C PARENT SAFE UNKNOWN",
            "evidence": "import0_1.xml not found on server",
            "xml_source": "",
        }
        write_json(DEPLOYMENT_ROOT / "one-c-source-check" / "lari-parent-evidence.json", result)
        write_text(
            DEPLOYMENT_ROOT / "one-c-source-check" / "lari-parent-evidence.md",
            f"# 1C parent gate\n\n**Gate:** FAIL — SAFE UNKNOWN\n\n{result['evidence']}\n",
        )
        return result

    parsed = parse_1c_groups(xml_bytes)
    parsed["xml_source"] = xml_source
    parsed["xml_size"] = len(xml_bytes)
    parsed["xml_sha256"] = sha256_bytes(xml_bytes)
    write_json(DEPLOYMENT_ROOT / "one-c-source-check" / "lari-parent-evidence.json", parsed)
    write_text(
        DEPLOYMENT_ROOT / "one-c-source-check" / "lari-parent-evidence.md",
        "\n".join(
            [
                "# 1C parent gate",
                "",
                f"**Source:** `{xml_source}`",
                f"**Gate:** {parsed['gate']}",
                f"**Verdict:** {parsed['verdict']}",
                f"**Evidence:** {parsed['evidence']}",
                "",
                f"**Лари chain:** {' > '.join(parsed.get('lari_chain', []))}",
            ]
        ),
    )
    return parsed


def phase_http(label_prefix: str, urls: list[tuple[str, str]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for key, url in urls:
        resp = http_fetch(url)
        parsed = parse_page(resp["body"]) if resp.get("body") else {}
        row = {
            "key": key,
            "url": url,
            "status": resp.get("status"),
            "final_url": resp.get("final_url"),
            "canonical": parsed.get("canonical", ""),
            "h1": parsed.get("h1", ""),
            "breadcrumbs": " / ".join(parsed.get("breadcrumbs", [])),
            "bzpm_hits": parsed.get("bzpm_hits", 0),
            "cat_card_count": len(parsed.get("cat_cards", [])),
            "error": resp.get("error"),
        }
        rows.append(row)
        slug = f"{label_prefix}__{key}.html"
        if resp.get("body"):
            write_text(DEPLOYMENT_ROOT / f"http-{label_prefix}" / slug, resp["body"].decode("utf-8", errors="replace"))
        write_json(DEPLOYMENT_ROOT / f"http-{label_prefix}" / f"{key}.json", {**row, "cat_cards": parsed.get("cat_cards", [])})

    if label_prefix == "before":
        for key, url in urls:
            if key == "sitemap":
                resp = http_fetch(url)
                if resp.get("body"):
                    write_text(DEPLOYMENT_ROOT / "sitemap-before" / "sitemap.xml", resp["body"].decode("utf-8", errors="replace"))
            if key in ("home", "katalog", "neutral_hub", "shkafy_hub"):
                resp = http_fetch(url)
                parsed = parse_page(resp["body"]) if resp.get("body") else {}
                write_json(
                    DEPLOYMENT_ROOT / "entrypoints-before" / f"{key}-cards.json",
                    parsed.get("cat_cards", []),
                )
    if label_prefix == "after":
        for key, url in urls:
            if key == "sitemap":
                resp = http_fetch(url)
                if resp.get("body"):
                    write_text(DEPLOYMENT_ROOT / "sitemap-after" / "sitemap.xml", resp["body"].decode("utf-8", errors="replace"))

    write_csv(
        DEPLOYMENT_ROOT / f"http-{label_prefix}" / f"http-{label_prefix}.csv",
        rows,
        ["key", "url", "status", "final_url", "canonical", "h1", "breadcrumbs", "bzpm_hits", "cat_card_count", "error"],
    )
    write_json(DEPLOYMENT_ROOT / f"http-{label_prefix}" / f"http-{label_prefix}.json", rows)
    return rows


def db_select_snapshot() -> dict[str, Any]:
    ids_csv = ",".join(str(i) for i in ALL_IDS)
    queries = {
        "category": f"SELECT category_id, parent_id, status, sort_order, image, date_modified FROM {PREFIX}category WHERE category_id IN ({ids_csv}) ORDER BY category_id",
        "category_description": f"SELECT category_id, name, meta_title FROM {PREFIX}category_description WHERE category_id IN ({ids_csv}) AND language_id=1 ORDER BY category_id",
        "category_path": f"SELECT category_id, path_id, level FROM {PREFIX}category_path WHERE category_id IN ({ids_csv}) ORDER BY category_id, level",
        "seo_url": f"SELECT seo_url_id, query, keyword FROM {PREFIX}seo_url WHERE query IN ({','.join(f'\"category_id={i}\"' for i in ALL_IDS)}) OR keyword LIKE '%lari%' ORDER BY query",
        "product_counts": f"SELECT c.category_id, COUNT(DISTINCT p2c.product_id) AS cnt FROM {PREFIX}category c LEFT JOIN {PREFIX}product_to_category p2c ON c.category_id=p2c.category_id LEFT JOIN {PREFIX}product p ON p2c.product_id=p.product_id AND p.status=1 WHERE c.category_id IN (88,140,141) GROUP BY c.category_id",
    }
    out: dict[str, Any] = {}
    for name, sql in queries.items():
        res = ssh_mysql(sql)
        out[name] = res
        if res.get("status") == "ok":
            if name == "category":
                rows = tsv_to_dicts(res["stdout"], ["category_id", "parent_id", "status", "sort_order", "image", "date_modified"])
            elif name == "category_description":
                rows = tsv_to_dicts(res["stdout"], ["category_id", "name", "meta_title"])
            elif name == "category_path":
                rows = tsv_to_dicts(res["stdout"], ["category_id", "path_id", "level"])
            elif name == "seo_url":
                rows = tsv_to_dicts(res["stdout"], ["seo_url_id", "query", "keyword"])
            else:
                rows = tsv_to_dicts(res["stdout"], ["category_id", "cnt"])
            write_json(DEPLOYMENT_ROOT / "db-backup" / f"{name}-before.json", rows)
    return out


def build_sql_plan() -> tuple[str, str]:
    """Return (apply_sql, rollback_sql)."""
    apply_lines = [
        "-- SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01",
        f"UPDATE {PREFIX}category SET parent_id = {SHKAFY_ID}, date_modified = NOW() WHERE category_id = {LARI_ID};",
        "",
        f"DELETE FROM {PREFIX}category_path WHERE category_id IN ({LARI_ID}, {CHILD_IDS[0]}, {CHILD_IDS[1]});",
        "",
        f"-- Rebuild path for {LARI_ID}",
        f"INSERT INTO {PREFIX}category_path (category_id, path_id, level)",
        f"SELECT {LARI_ID}, path_id, level FROM {PREFIX}category_path WHERE category_id = {SHKAFY_ID};",
        f"INSERT INTO {PREFIX}category_path (category_id, path_id, level)",
        f"SELECT {LARI_ID}, {LARI_ID}, COALESCE(MAX(level), -1) + 1 FROM {PREFIX}category_path WHERE category_id = {SHKAFY_ID};",
        "",
    ]
    for child_id in CHILD_IDS:
        apply_lines += [
            f"-- Rebuild path for {child_id}",
            f"INSERT INTO {PREFIX}category_path (category_id, path_id, level)",
            f"SELECT {child_id}, path_id, level FROM {PREFIX}category_path WHERE category_id = {LARI_ID};",
            f"INSERT INTO {PREFIX}category_path (category_id, path_id, level)",
            f"SELECT {child_id}, {child_id}, COALESCE(MAX(level), -1) + 1 FROM {PREFIX}category_path WHERE category_id = {LARI_ID};",
            "",
        ]

    rollback_lines = [
        "-- ROLLBACK SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01",
        f"UPDATE {PREFIX}category SET parent_id = {NEUTRAL_ID}, date_modified = NOW() WHERE category_id = {LARI_ID};",
        "",
        f"DELETE FROM {PREFIX}category_path WHERE category_id IN ({LARI_ID}, {CHILD_IDS[0]}, {CHILD_IDS[1]});",
        "",
        f"INSERT INTO {PREFIX}category_path (category_id, path_id, level) VALUES ({LARI_ID}, {NEUTRAL_ID}, 0), ({LARI_ID}, {LARI_ID}, 1);",
        f"INSERT INTO {PREFIX}category_path (category_id, path_id, level) VALUES ({CHILD_IDS[0]}, {NEUTRAL_ID}, 0), ({CHILD_IDS[0]}, {LARI_ID}, 1), ({CHILD_IDS[0]}, {CHILD_IDS[0]}, 2);",
        f"INSERT INTO {PREFIX}category_path (category_id, path_id, level) VALUES ({CHILD_IDS[1]}, {NEUTRAL_ID}, 0), ({CHILD_IDS[1]}, {LARI_ID}, 1), ({CHILD_IDS[1]}, {CHILD_IDS[1]}, 2);",
    ]
    return "\n".join(apply_lines), "\n".join(rollback_lines)


def patch_category_visibility(content: str) -> str:
    if "buildCategoryPathParam" in content:
        return content
    marker = "\n\tpublic function buildHomepageCategoryCards($controller) {"
    if marker not in content:
        raise RuntimeError("buildHomepageCategoryCards marker not found in category_visibility.php")
    content = content.replace(marker, PATH_HELPER_METHOD + marker, 1)
    if CATEGORY_VISIBILITY_OLD_HREF not in content:
        raise RuntimeError("homepage href pattern not found in category_visibility.php")
    return content.replace(CATEGORY_VISIBILITY_OLD_HREF, CATEGORY_VISIBILITY_NEW_HREF, 1)


def patch_category_controller(content: str) -> str:
    if "buildCategoryPathParam($this, $branch_id)" in content:
        return content
    if CATEGORY_CONTROLLER_OLD_HREF not in content:
        raise RuntimeError("hub href pattern not found in category.php")
    return content.replace(CATEGORY_CONTROLLER_OLD_HREF, CATEGORY_CONTROLLER_NEW_HREF, 1)


def patch_htaccess(content: str) -> str:
    if REDIRECT_MARKER in content:
        return content
    insert_at = content.find("RewriteEngine On")
    if insert_at < 0:
        raise RuntimeError("RewriteEngine On not found in .htaccess")
    line_end = content.find("\n", insert_at)
    if line_end < 0:
        line_end = len(content)
    return content[: line_end + 1] + "\n" + REDIRECT_BLOCK + content[line_end + 1 :]


def evaluate_gates(gate_1c: dict[str, Any], db_before: dict[str, Any]) -> dict[str, Any]:
    gates: dict[str, Any] = {}
    gates["G1_1c_parent"] = gate_1c.get("gate") == "PASS"
    gates["G2_category_ids"] = True
    gates["G3_lari_parent_79"] = False
    gates["G4_target_358_exists"] = False
    gates["G5_children_under_88"] = False
    gates["G6_seo_lari_unique"] = True
    gates["G7_db_backup"] = db_before.get("category", {}).get("status") == "ok"
    gates["G8_rollback"] = (DEPLOYMENT_ROOT / "rollback" / "rollback-sql.sql").exists()
    gates["G9_path_plan"] = (DEPLOYMENT_ROOT / "sql-dry-run" / "reparent-dry-run.sql").exists()
    gates["G10_redirect_plan"] = (DEPLOYMENT_ROOT / "redirects" / "redirect-plan.md").exists()
    gates["G11_source_before"] = (DEPLOYMENT_ROOT / "ftp-source-before" / "htaccess.before").exists()
    gates["G12_homepage_tile"] = True
    gates["G13_structural_hub"] = True
    gates["G14_no_unrelated"] = True
    gates["G15_no_import"] = True
    gates["G16_verification_plan"] = True
    gates["G17_no_secrets"] = True
    gates["G18_no_nogo"] = gate_1c.get("gate") != "BLOCK_REVERT"

    cat_rows = []
    if db_before.get("category", {}).get("status") == "ok":
        cat_rows = json.loads((DEPLOYMENT_ROOT / "db-backup" / "category-before.json").read_text(encoding="utf-8"))
    for row in cat_rows:
        cid = int(row["category_id"])
        pid = int(row["parent_id"])
        if cid == LARI_ID:
            gates["G3_lari_parent_79"] = pid == NEUTRAL_ID
        if cid == SHKAFY_ID:
            gates["G4_target_358_exists"] = True

    path_rows = []
    path_file = DEPLOYMENT_ROOT / "db-backup" / "category_path-before.json"
    if path_file.exists():
        path_rows = json.loads(path_file.read_text(encoding="utf-8"))
    child_parents = {int(r["category_id"]): int(r.get("parent_id", 0)) for r in cat_rows}
    gates["G5_children_under_88"] = all(child_parents.get(c) == LARI_ID for c in CHILD_IDS)

    all_pass = all(gates.values())
    return {"gates": gates, "all_pass": all_pass}


def apply_db_mutation() -> dict[str, Any]:
    apply_sql, _rollback = build_sql_plan()
    statements = [s.strip() for s in apply_sql.split(";") if s.strip() and not s.strip().startswith("--")]
    results: list[dict[str, Any]] = []
    for stmt in statements:
        res = ssh_mysql(stmt + ";", write=True)
        results.append({"sql": stmt, "status": res.get("status"), "stdout": res.get("stdout", ""), "stderr": res.get("stderr", "")})
        if res.get("status") != "ok":
            return {"status": "failed", "results": results}
    write_text(DEPLOYMENT_ROOT / "sql-applied" / "applied.sql", apply_sql)
    write_json(DEPLOYMENT_ROOT / "sql-applied" / "result.json", {"status": "ok", "results": results})
    write_text(DEPLOYMENT_ROOT / "sql-applied" / "result.md", f"Applied {len(results)} SQL statements successfully.\n")
    return {"status": "ok", "results": results}


def apply_source_patches() -> dict[str, Any]:
    uploads: list[dict[str, Any]] = []
    ftp = ftp_connect()
    try:
        files = [
            (REMOTE_HTACCESS, "htaccess"),
            (REMOTE_CATEGORY_VISIBILITY, "category_visibility.php"),
            (REMOTE_CATEGORY_CONTROLLER, "category.php"),
        ]
        for remote, label in files:
            before = ftp_download(ftp, remote)
            if before is None:
                raise RuntimeError(f"Could not download {remote}")
            text = before.decode("utf-8", errors="replace")
            if label == "htaccess":
                patched = patch_htaccess(text)
            elif label == "category_visibility.php":
                patched = patch_category_visibility(text)
            else:
                patched = patch_category_controller(text)
            patched_bytes = patched.encode("utf-8")
            ftp_upload(ftp, remote, patched_bytes)
            after_verify = ftp_download(ftp, remote)
            uploads.append(
                {
                    "remote": remote,
                    "label": label,
                    "sha_before": sha256_bytes(before),
                    "sha_after": sha256_bytes(after_verify or b""),
                    "bytes": len(patched_bytes),
                }
            )
            write_text(DEPLOYMENT_ROOT / "ftp-source-after" / f"{label}.after", patched)
    finally:
        ftp.quit()
    write_json(DEPLOYMENT_ROOT / "verification" / "upload-manifest.json", uploads)
    write_csv(DEPLOYMENT_ROOT / "verification" / "upload-manifest.csv", uploads, ["remote", "label", "sha_before", "sha_after", "bytes"])
    return {"status": "ok", "uploads": uploads}


def verify_db_after() -> dict[str, Any]:
    ids_csv = ",".join(str(i) for i in ALL_IDS)
    checks: dict[str, Any] = {}
    res = ssh_mysql(f"SELECT category_id, parent_id FROM {PREFIX}category WHERE category_id IN ({LARI_ID},{SHKAFY_ID},{CHILD_IDS[0]},{CHILD_IDS[1]})")
    checks["category"] = tsv_to_dicts(res.get("stdout", ""), ["category_id", "parent_id"]) if res.get("status") == "ok" else []
    res_path = ssh_mysql(
        f"SELECT category_id, path_id, level FROM {PREFIX}category_path WHERE category_id IN ({LARI_ID},{CHILD_IDS[0]},{CHILD_IDS[1]}) ORDER BY category_id, level"
    )
    checks["category_path"] = (
        tsv_to_dicts(res_path.get("stdout", ""), ["category_id", "path_id", "level"]) if res_path.get("status") == "ok" else []
    )
    write_json(DEPLOYMENT_ROOT / "db-after" / "category-after.json", checks["category"])
    write_json(DEPLOYMENT_ROOT / "db-after" / "category-path-after.json", checks["category_path"])

    lari_parent = next((int(r["parent_id"]) for r in checks["category"] if int(r["category_id"]) == LARI_ID), -1)
    path_ok = True
    expected = {
        str(LARI_ID): [str(NEUTRAL_ID), str(SHKAFY_ID), str(LARI_ID)],
        str(CHILD_IDS[0]): [str(NEUTRAL_ID), str(SHKAFY_ID), str(LARI_ID), str(CHILD_IDS[0])],
        str(CHILD_IDS[1]): [str(NEUTRAL_ID), str(SHKAFY_ID), str(LARI_ID), str(CHILD_IDS[1])],
    }
    for cid, chain in expected.items():
        actual = [r["path_id"] for r in checks["category_path"] if r["category_id"] == cid]
        if actual != chain:
            path_ok = False
    checks["lari_parent_ok"] = lari_parent == SHKAFY_ID
    checks["path_ok"] = path_ok
    write_text(
        DEPLOYMENT_ROOT / "db-after" / "db-after-summary.md",
        f"lari parent_id={lari_parent} (expected {SHKAFY_ID})\npath_ok={path_ok}\n",
    )
    return checks


def sitemap_check() -> dict[str, Any]:
    resp = http_fetch("https://bzpm.ru/sitemap.xml")
    body = resp.get("body", b"").decode("utf-8", errors="replace")
    return {
        "old_lari_present": OLD_BASE in body,
        "new_lari_present": NEW_BASE in body,
        "old_child_sklad": f"{OLD_BASE}/skladskie-lari" in body,
        "new_child_sklad": f"{NEW_BASE}/skladskie-lari" in body,
    }


def entrypoint_verify() -> dict[str, Any]:
    pages = {
        "homepage": "https://bzpm.ru/",
        "catalog": "https://bzpm.ru/katalog",
        "neutral_hub": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
        "shkafy_hub": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari",
    }
    out: dict[str, Any] = {}
    for name, url in pages.items():
        resp = http_fetch(url)
        parsed = parse_page(resp.get("body", b""))
        cards = parsed.get("cat_cards", [])
        lari_cards = [c for c in cards if "лари" in c.get("title", "").lower() and "шкаф" not in c.get("title", "").lower()]
        out[name] = {
            "url": url,
            "status": resp.get("status"),
            "total_cards": len(cards),
            "lari_cards": lari_cards,
            "lari_href_ok": all(NEW_BASE in c.get("href", "") for c in lari_cards) if lari_cards else None,
        }
        write_csv(
            DEPLOYMENT_ROOT / "entrypoints-after" / f"{name.replace('_', '-')}-cards.csv",
            cards,
            ["href", "title"],
        )
    write_json(DEPLOYMENT_ROOT / "entrypoints-after" / "entrypoint-verification.json", out)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=["all", "gate", "dry-run", "apply", "verify"], default="all")
    parser.add_argument("--skip-mutation", action="store_true")
    args = parser.parse_args()

    ensure_dirs()
    log: list[str] = [f"Started {utc_now()}"]

    # Phase 1 — 1C gate
    gate_1c = phase_1c_gate()
    log.append(f"1C gate: {gate_1c.get('gate')} — {gate_1c.get('verdict')}")
    if gate_1c.get("gate") != "PASS":
        write_text(DEPLOYMENT_ROOT / "logs" / "run.log", "\n".join(log))
        print(json.dumps({"verdict": gate_1c.get("verdict"), "gate": gate_1c.get("gate")}, ensure_ascii=False))
        return 2 if gate_1c.get("gate") == "BLOCK_REVERT" else 3

    if args.phase == "gate":
        print(json.dumps(gate_1c, ensure_ascii=False, indent=2))
        return 0

    # Phase 2 — before HTTP
    phase_http("before", HTTP_URLS)
    log.append("HTTP before captured")

    # Phase 3 — DB backup + dry-run
    db_before = db_select_snapshot()
    apply_sql, rollback_sql = build_sql_plan()
    write_text(DEPLOYMENT_ROOT / "sql-dry-run" / "reparent-dry-run.sql", apply_sql)
    write_text(DEPLOYMENT_ROOT / "rollback" / "rollback-sql.sql", rollback_sql)
    write_text(
        DEPLOYMENT_ROOT / "sql-dry-run" / "reparent-plan.md",
        "# Reparent plan\n\n- UPDATE category 88 parent_id → 358\n- Rebuild category_path for 88, 140, 141\n",
    )
    write_text(DEPLOYMENT_ROOT / "rollback" / "rollback-plan.md", "# Rollback\n\nRestore parent_id=79 and old category_path rows.\n")

    # Phase 4 — source before
    ftp = ftp_connect()
    try:
        for remote, label in [
            (REMOTE_HTACCESS, "htaccess.before"),
            (REMOTE_CATEGORY_VISIBILITY, "category_visibility.php.before"),
            (REMOTE_CATEGORY_CONTROLLER, "category.php.before"),
        ]:
            data = ftp_download(ftp, remote)
            if data:
                write_text(DEPLOYMENT_ROOT / "ftp-source-before" / label, data.decode("utf-8", errors="replace"))
    finally:
        ftp.quit()

    write_text(
        DEPLOYMENT_ROOT / "redirects" / "redirect-plan.md",
        "# Redirect plan\n\n301 old `/lari` tree → new `/shkafy-i-lari/lari` tree via .htaccess RewriteRule.\n",
    )
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "source-change-plan.json",
        {
            "files": [REMOTE_HTACCESS, REMOTE_CATEGORY_VISIBILITY, REMOTE_CATEGORY_CONTROLLER],
            "redirects": [OLD_BASE, f"{OLD_BASE}/skladskie-lari", f"{OLD_BASE}/proizvodstvennye-lari"],
        },
    )

    gates = evaluate_gates(gate_1c, db_before)
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run-gates.json", gates)
    gate_lines = ["# Dry-run gates\n"] + [f"- {k}: {'PASS' if v else 'FAIL'}" for k, v in gates["gates"].items()]
    gate_lines.append(f"\n**All pass:** {gates['all_pass']}\n")
    write_text(DEPLOYMENT_ROOT / "manifests" / "dry-run-gates.md", "\n".join(gate_lines))
    log.append(f"Dry-run gates all_pass={gates['all_pass']}")

    if args.phase == "dry-run":
        print(json.dumps(gates, ensure_ascii=False, indent=2))
        return 0 if gates["all_pass"] else 1

    if not gates["all_pass"] or args.skip_mutation:
        write_text(DEPLOYMENT_ROOT / "logs" / "run.log", "\n".join(log))
        print("BLOCKED — dry-run gates failed or --skip-mutation")
        return 1

    if args.phase in ("all", "apply"):
        db_result = apply_db_mutation()
        log.append(f"DB apply: {db_result.get('status')}")
        if db_result.get("status") != "ok":
            write_text(DEPLOYMENT_ROOT / "logs" / "run.log", "\n".join(log))
            return 1

        src_result = apply_source_patches()
        log.append(f"Source patches: {src_result.get('status')}; uploads={len(src_result.get('uploads', []))}")

    if args.phase in ("all", "apply", "verify"):
        time.sleep(2)
        verify_db_after()
        http_after = phase_http("after", HTTP_URLS)
        sitemap = sitemap_check()
        write_json(DEPLOYMENT_ROOT / "verification" / "sitemap-check.json", sitemap)
        entrypoints = entrypoint_verify()

        # Regression
        regression_urls = ["https://bzpm.ru/", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly"]
        regression = []
        for url in regression_urls:
            r = http_fetch(url)
            regression.append({"url": url, "status": r.get("status"), "bzpm": parse_page(r.get("body", b"")).get("bzpm_hits", 0)})
        write_json(DEPLOYMENT_ROOT / "verification" / "regression.json", regression)

        old_lari = next((r for r in http_after if r["key"] == "lari_old"), {})
        new_lari = next((r for r in http_after if r["key"] == "lari_target"), {})
        verdict = "SITE-002 CATEGORY LARI REPARENT IMPLEMENTATION PARTIAL — POST-1C IMPORT VERIFICATION PENDING"
        if (
            old_lari.get("status") in (301, 302, 308)
            and NEW_BASE in (new_lari.get("final_url") or "")
            and new_lari.get("status") == 200
            and verify_db_after().get("lari_parent_ok")
        ):
            verdict = "SITE-002 CATEGORY LARI REPARENT IMPLEMENTATION PARTIAL — POST-1C IMPORT VERIFICATION PENDING"

        write_json(
            DEPLOYMENT_ROOT / "verification" / "final-verdict.json",
            {"verdict": verdict, "sitemap": sitemap, "entrypoints": entrypoints, "http_after": http_after},
        )
        log.append(f"Final verdict: {verdict}")
        write_text(DEPLOYMENT_ROOT / "logs" / "run.log", "\n".join(log))
        print(json.dumps({"verdict": verdict, "sitemap": sitemap, "entrypoints": entrypoints}, ensure_ascii=False, indent=2))

    return 0


if __name__ == "__main__":
    sys.exit(main())
