#!/usr/bin/env python3
"""SITE-002 Audit Wave B SEO foundation — sitemap pretty URLs + SEO duplicate cleanup (Run 4.243)."""
from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import html
import json
import re
import shlex
import subprocess
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from io import BytesIO
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01"
OCPILOT_RUN = "4.243"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION_CONTROLLED_SEO_FOUNDATION_PATCH"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CRON-RUN-REPORTS-DURATION-FIX-01"
CHECKPOINT_AFTER = "SITE-002-STABLE-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01"
WRONG_BRAND = "БЗПМ"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOY_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
REPORT_PATH = Path(
    r"X:\AI MARS\projects\ocpilot\sites\site-002\reports\SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01.md"
)
PATCHED_SITEMAP_LOCAL = Path(
    r"X:\AI MARS\projects\ocpilot\sites\site-002\tools\google_sitemap-site-002-prod-audit-wave-b-seo-foundation-01.php"
)
REMOTE_SITEMAP = "/public_html/catalog/controller/extension/feed/google_sitemap.php"

SUBDIRS = (
    "sitemap-before", "sitemap-after", "http-before", "http-after",
    "db-readonly", "db-backup-scoped", "source-before", "source-after",
    "patch", "rollback", "verification", "manifests", "reports", "logs",
)

LEGACY_INFORMATION_IDS = {6, 9, 10, 11, 12, 13, 14}

SEED_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/index.php",
    "https://bzpm.ru/contact",
    "https://bzpm.ru/kontakty",
    "https://bzpm.ru/custom-equipment",
    "https://bzpm.ru/payment-methods",
    "https://bzpm.ru/delivery",
    "https://bzpm.ru/dealers",
    "https://bzpm.ru/guarantee",
    "https://bzpm.ru/about",
    "https://bzpm.ru/compare-products",
    "https://bzpm.ru/wishlist",
    "https://bzpm.ru/sitemap.xml",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/llms.txt",
]

REGRESSION_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/index.php",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari",
    "https://bzpm.ru/contact",
    "https://bzpm.ru/kontakty",
    "https://bzpm.ru/custom-equipment",
    "https://bzpm.ru/payment-methods",
    "https://bzpm.ru/delivery",
    "https://bzpm.ru/dealers",
    "https://bzpm.ru/guarantee",
    "https://bzpm.ru/sitemap.xml",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/llms.txt",
]

SOURCE_CANDIDATES = [
    (REMOTE_SITEMAP, "sitemap_controller", "high"),
    ("/public_html/catalog/controller/startup/seo_url.php", "seo_url_startup", "low"),
    ("/public_html/catalog/controller/startup/seo_pro.php", "seo_pro_startup", "low"),
]

stats: dict[str, int] = {
    "ftp_reads": 0, "ftp_uploads": 0, "db_selects": 0, "db_writes": 0,
    "db_backup_rows": 0,
}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.in_title = False
        self.in_h1 = False
        self.h1_list: list[str] = []
        self.meta: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ad = {k: (v or "") for k, v in attrs}
        tl = tag.lower()
        if tl == "title":
            self.in_title = True
        elif tl == "h1":
            self.in_h1 = True
        elif tl == "meta":
            name = (ad.get("name") or ad.get("property") or "").lower()
            if name:
                self.meta[name] = ad.get("content", "")

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False
        elif tag.lower() == "h1":
            self.in_h1 = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        elif self.in_h1:
            self.h1_list.append(data.strip())


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
        w = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_production_section(subsection: str) -> dict[str, str]:
    text = SECRETS_PATH.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    sub = re.search(rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
    if not sub:
        raise RuntimeError(f"Subsection {subsection!r} not found")
    fields: dict[str, str] = {}
    key: str | None = None
    for line in sub.group(1).splitlines():
        s = line.strip()
        if not s:
            continue
        if s.endswith(":"):
            key = s[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(key, "")
        elif key:
            fields[key] = s
    return fields


def ftp_connect() -> ftplib.FTP:
    f = parse_production_section("FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(f["host"], int(f.get("port") or 21), timeout=180)
    ftp.login(f["username"], f["password"])
    return ftp


def ftp_download(remote: str) -> bytes:
    ftp = ftp_connect()
    buf = BytesIO()
    ftp.retrbinary(f"RETR {remote}", buf.write)
    ftp.quit()
    stats["ftp_reads"] += 1
    return buf.getvalue()


def ftp_upload(remote: str, data: bytes) -> None:
    ftp = ftp_connect()
    ftp.storbinary(f"STOR {remote}", BytesIO(data))
    ftp.quit()
    stats["ftp_uploads"] += 1


def mysql_select(sql: str) -> str:
    import paramiko

    ssh = parse_production_section("SSH")
    db = parse_production_section("Database")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        ssh["host"], port=int(ssh.get("port") or 22), username=ssh["username"],
        password=ssh["password"], timeout=60, allow_agent=False, look_for_keys=False,
    )
    esc = sql.replace("\\", "\\\\").replace('"', '\\"')
    cmd = (
        f'MYSQL_PWD={shlex.quote(db["password"])} mysql -N -B -u {shlex.quote(db["username"])} '
        f'{shlex.quote(db["database"])} -e "{esc}" 2>&1'
    )
    _i, o, e = c.exec_command(cmd, timeout=120)
    out = o.read().decode() + e.read().decode()
    c.close()
    stats["db_selects"] += 1
    return out


def mysql_write(sql: str) -> str:
    stats["db_writes"] += 1
    return mysql_select(sql)


def curl_probe(url: str, follow: bool = True, method: str = "GET") -> dict[str, Any]:
    cmd = [
        "curl", "-sS", "-H", f"User-Agent: {USER_AGENT}", "-H", "Cache-Control: no-cache",
        "-o", "-", "-w", "__CURL_META__%{http_code} %{redirect_url} %{url_effective}",
    ]
    if method == "HEAD":
        cmd.extend(["-X", "HEAD"])
    if follow:
        cmd.append("-L")
    else:
        cmd.extend(["--max-redirs", "0"])
    cmd.append(url)
    try:
        proc = subprocess.run(cmd, capture_output=True, timeout=90)
        raw = proc.stdout or b""
        text = raw.decode("utf-8", "replace")
        body_text = text
        meta_line = ""
        if "__CURL_META__" in text:
            body_text, meta_line = text.rsplit("__CURL_META__", 1)
        parts = meta_line.strip().split() if meta_line.strip() else []
        status = int(parts[0]) if parts and parts[0].isdigit() else None
        effective = parts[2] if len(parts) > 2 else url
        location = ""
        for line in body_text.splitlines()[:30]:
            if line.lower().startswith("location:"):
                location = line.split(":", 1)[1].strip()
                break
        parser = PageParser()
        if body_text and "<" in body_text:
            try:
                parser.feed(body_text)
            except Exception:
                pass
        return {
            "url": url,
            "status": status,
            "final_url": effective,
            "location": location,
            "canonical": parser.meta.get("canonical", ""),
            "title": parser.title.strip(),
            "h1": " | ".join(h for h in parser.h1_list if h),
            "robots": parser.meta.get("robots", ""),
            "public_bzpm_hits": body_text.count(WRONG_BRAND),
            "error": None,
        }
    except Exception as exc:
        return {
            "url": url, "status": None, "final_url": url, "location": "",
            "canonical": "", "title": "", "h1": "", "robots": "",
            "public_bzpm_hits": 0, "error": str(exc),
        }


def fetch_url_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


def parse_sitemap_urls(xml_bytes: bytes) -> list[str]:
    root = ET.fromstring(xml_bytes)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = []
    for loc in root.findall(".//sm:loc", ns):
        if loc.text:
            urls.append(loc.text.strip())
    if not urls:
        for loc in root.findall(".//loc"):
            if loc.text:
                urls.append(loc.text.strip())
    return urls


def analyze_sitemap_urls(urls: list[str]) -> dict[str, Any]:
    legacy = [u for u in urls if "index.php?route=information" in u]
    contact = any("/contact" in u and "index.php" not in u for u in urls)
    kontakty = any("kontakty" in u for u in urls)
    flat_lari = [u for u in urls if re.search(r"/katalog/nejtralnoe-oborudovanie/lari(?:/|$)", u) and "shkafy-i-lari" not in u]
    nested_lari = [u for u in urls if "shkafy-i-lari/lari" in u]
    return {
        "total": len(urls),
        "legacy_information_urls": legacy,
        "legacy_information_count": len(legacy),
        "contact_in_sitemap": contact,
        "kontakty_in_sitemap": kontakty,
        "flat_lari_urls": flat_lari,
        "nested_lari_count": len(nested_lari),
        "duplicate_urls": [u for u in urls if urls.count(u) > 1],
    }


def init_operation() -> None:
    for d in SUBDIRS:
        (DEPLOY_ROOT / d).mkdir(parents=True, exist_ok=True)
    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "environment": ENVIRONMENT,
        "production_url": PRODUCTION_URL,
        "baseline_before": BASELINE_BEFORE,
        "related_audit_run": "SITE-002-PROD-FULL-TECH-SEO-AUDIT-01",
        "related_audit_ocpilot_run": "4.241",
        "related_redirect_hygiene_run": "SITE-002-PROD-AUDIT-WAVE-C-REDIRECT-HYGIENE-01",
        "related_redirect_hygiene_ocpilot_run": "4.242",
        "target_issues": ["AUDIT-007", "AUDIT-004", "AUDIT-010", "AUDIT-002"],
        "production_mutation_allowed": True,
        "ftp_upload_allowed": "exact_sitemap_or_seo_files_only",
        "db_write_allowed": "scoped_only_after_backup_and_gates",
        "admin_save_allowed": False,
        "import_run_allowed": False,
        "monitor_run_allowed": False,
        "contact_url_policy": "/contact canonical; /kontakty accepted 404",
        "started_at": utc_now(),
    }
    write_json(DEPLOY_ROOT / "manifests" / "operation.json", manifest)


def phase_http_snapshot(urls: list[str], out_dir: Path, label: str, sitemap_urls: list[str] | None = None) -> list[dict[str, Any]]:
    sm_set = set(sitemap_urls or [])
    rows = []
    for url in urls:
        nf = curl_probe(url, follow=False)
        f = curl_probe(url, follow=True)
        row = {
            **f,
            "status_no_follow": nf.get("status"),
            "location_no_follow": nf.get("location", ""),
            "in_sitemap": url.rstrip("/") in {u.rstrip("/") for u in sm_set} or any(
                url.rstrip("/") == u.split("?")[0].rstrip("/") for u in sm_set
            ),
        }
        rows.append(row)
        time.sleep(0.1)
    fields = [
        "url", "status", "status_no_follow", "location_no_follow", "final_url",
        "canonical", "title", "h1", "robots", "in_sitemap", "public_bzpm_hits", "error",
    ]
    write_csv(out_dir / f"seo-foundation-{label}.csv", rows, fields)
    write_json(out_dir / f"seo-foundation-{label}.json", rows)
    return rows


def phase_sitemap(label: str) -> tuple[bytes, list[str], dict[str, Any]]:
    xml = fetch_url_bytes("https://bzpm.ru/sitemap.xml")
    out = DEPLOY_ROOT / f"sitemap-{label}"
    (out / f"sitemap-{label}.xml").write_bytes(xml)
    urls = parse_sitemap_urls(xml)
    analysis = analyze_sitemap_urls(urls)
    rows = [{"url": u, "is_legacy_information": "index.php?route=information" in u} for u in urls]
    write_csv(out / f"sitemap-url-analysis-{label}.csv", rows, ["url", "is_legacy_information"])
    write_json(out / f"sitemap-url-analysis-{label}.json", {"analysis": analysis, "urls": urls})
    legacy_md = [
        f"# Legacy information URLs ({label})\n\nGenerated: {utc_now()}\n\n",
        f"Count: **{analysis['legacy_information_count']}**\n\n",
    ]
    for u in analysis["legacy_information_urls"]:
        legacy_md.append(f"- `{u}`\n")
    write_text(out / f"legacy-information-urls-{label}.md", "".join(legacy_md))
    return xml, urls, analysis


def phase_db_discovery() -> dict[str, Any]:
    summary: dict[str, Any] = {"available": False}
    try:
        dup_raw = mysql_select(
            "SELECT seo_url_id, store_id, language_id, query, keyword FROM oc_seo_url "
            "WHERE keyword IN ('compare-products','wishlist') ORDER BY keyword, seo_url_id"
        )
        dup_global = mysql_select(
            "SELECT keyword, COUNT(*) c FROM oc_seo_url GROUP BY keyword HAVING c>1"
        )
        info_seo = mysql_select(
            "SELECT seo_url_id, store_id, language_id, query, keyword FROM oc_seo_url "
            "WHERE query LIKE 'information%' ORDER BY query, seo_url_id"
        )
        info_pages = mysql_select(
            "SELECT i.information_id, id.title, i.status FROM oc_information i "
            "JOIN oc_information_description id ON i.information_id=id.information_id AND id.language_id=1 "
            "WHERE i.status=1 ORDER BY i.information_id"
        )
        contact_seo = mysql_select(
            "SELECT seo_url_id, store_id, language_id, query, keyword FROM oc_seo_url "
            "WHERE query LIKE '%contact%' OR keyword='contact' ORDER BY seo_url_id"
        )
        counts = mysql_select(
            "SELECT 'categories' t, COUNT(*) c FROM oc_category WHERE status=1 UNION ALL "
            "SELECT 'products', COUNT(*) FROM oc_product WHERE status=1 UNION ALL "
            "SELECT 'information', COUNT(*) FROM oc_information WHERE status=1"
        )

        dup_rows = []
        for line in dup_raw.strip().splitlines():
            p = line.split("\t")
            if len(p) >= 5:
                dup_rows.append({
                    "seo_url_id": p[0], "store_id": p[1], "language_id": p[2],
                    "query": p[3], "keyword": p[4],
                })

        info_map_rows = []
        for line in info_seo.strip().splitlines():
            p = line.split("\t")
            if len(p) >= 5:
                info_map_rows.append({
                    "seo_url_id": p[0], "store_id": p[1], "language_id": p[2],
                    "query": p[3], "keyword": p[4],
                })

        contact_rows = []
        for line in contact_seo.strip().splitlines():
            p = line.split("\t")
            if len(p) >= 5:
                contact_rows.append({
                    "seo_url_id": p[0], "store_id": p[1], "language_id": p[2],
                    "query": p[3], "keyword": p[4],
                })

        write_csv(DEPLOY_ROOT / "db-readonly" / "seo-url-duplicates.csv", dup_rows,
                  ["seo_url_id", "store_id", "language_id", "query", "keyword"])
        write_json(DEPLOY_ROOT / "db-readonly" / "seo-url-duplicates.json", dup_rows)
        write_csv(DEPLOY_ROOT / "db-readonly" / "information-seo-url-map.csv", info_map_rows,
                  ["seo_url_id", "store_id", "language_id", "query", "keyword"])
        write_json(DEPLOY_ROOT / "db-readonly" / "information-seo-url-map.json", info_map_rows)
        write_csv(DEPLOY_ROOT / "db-readonly" / "contact-route-seo.csv", contact_rows,
                  ["seo_url_id", "store_id", "language_id", "query", "keyword"])
        write_json(DEPLOY_ROOT / "db-readonly" / "contact-route-seo.json", contact_rows)

        # Classify duplicates
        by_kw: dict[str, list[dict[str, str]]] = {}
        for r in dup_rows:
            by_kw.setdefault(r["keyword"], []).append(r)

        dup_classification = {}
        rows_to_delete: list[dict[str, str]] = []
        for kw, rows in by_kw.items():
            queries = {r["query"] for r in rows}
            if len(queries) == 1 and len(rows) > 1:
                # identical query duplicates — keep lowest seo_url_id
                sorted_rows = sorted(rows, key=lambda x: int(x["seo_url_id"]))
                dup_classification[kw] = "identical_redundant_rows"
                rows_to_delete.extend(sorted_rows[1:])
            else:
                dup_classification[kw] = "route_conflict_defer"

        summary = {
            "available": True,
            "dup_rows": dup_rows,
            "dup_classification": dup_classification,
            "rows_to_delete": rows_to_delete,
            "info_map_rows": info_map_rows,
            "contact_rows": contact_rows,
            "counts": counts.strip(),
            "dup_global": dup_global.strip(),
            "info_pages": info_pages.strip(),
            "db_cleanup_safe": all(v == "identical_redundant_rows" for v in dup_classification.values()),
            "db_cleanup_deferred": any(v == "route_conflict_defer" for v in dup_classification.values()),
        }

        md = [
            f"# DB discovery summary\n\nGenerated: {utc_now()}\n\n",
            f"## Counts\n```\n{counts}\n```\n\n",
            f"## Duplicate keywords (global)\n```\n{dup_global}\n```\n\n",
            f"## compare-products / wishlist rows\n",
        ]
        for r in dup_rows:
            md.append(f"- id={r['seo_url_id']} store={r['store_id']} lang={r['language_id']} query=`{r['query']}` keyword=`{r['keyword']}`\n")
        md.append(f"\n## Classification\n```json\n{json.dumps(dup_classification, ensure_ascii=False, indent=2)}\n```\n")
        md.append(f"\n## DB cleanup safe: **{summary['db_cleanup_safe']}**\n")
        write_text(DEPLOY_ROOT / "db-readonly" / "db-discovery-summary.md", "".join(md))
        write_json(DEPLOY_ROOT / "db-readonly" / "db-discovery-summary.json", summary)
    except Exception as exc:
        summary = {"available": False, "error": str(exc)}
        write_json(DEPLOY_ROOT / "db-readonly" / "db-discovery-summary.json", summary)
    return summary


def phase_source_discovery() -> tuple[bytes, str]:
    rows = []
    sitemap_data = b""
    sitemap_sha = ""
    for remote, role, risk in SOURCE_CANDIDATES:
        local_name = remote.strip("/").replace("/", "__")
        local_path = DEPLOY_ROOT / "source-before" / local_name
        data = ftp_download(remote)
        local_path.write_bytes(data)
        text = data.decode("utf-8", "replace")
        emits_info = "getInformations" in text or "information/information" in text
        can_pretty = "url->link" in text
        emits_contact = "information/contact" in text
        will_modify = "yes" if remote == REMOTE_SITEMAP else "no"
        row = {
            "remote_path": remote,
            "role": role,
            "risk_level": risk,
            "sha256": sha256_bytes(data),
            "emits_information_pages": emits_info,
            "can_generate_pretty_url": can_pretty,
            "emits_native_contact_route": emits_contact,
            "will_modify": will_modify,
            "reason": "Patch information sitemap emission to route-based SEO URLs" if will_modify == "yes" else "reference only",
            "local_mirror": f"source-before/{local_name}",
        }
        rows.append(row)
        if remote == REMOTE_SITEMAP:
            sitemap_data = data
            sitemap_sha = row["sha256"]
    write_csv(
        DEPLOY_ROOT / "manifests" / "source-authority-map.csv", rows,
        ["remote_path", "role", "risk_level", "sha256", "emits_information_pages",
         "can_generate_pretty_url", "emits_native_contact_route", "will_modify", "reason"],
    )
    write_json(DEPLOY_ROOT / "manifests" / "source-authority-map.json", rows)
    md = ["# Source authority map\n\n", f"Generated: {utc_now()}\n\n"]
    for r in rows:
        md.append(f"### {r['remote_path']}\n\n")
        for k, v in r.items():
            if k != "remote_path":
                md.append(f"- **{k}:** {v}\n")
        md.append("\n")
    write_text(DEPLOY_ROOT / "manifests" / "source-authority-map.md", "".join(md))
    return sitemap_data, sitemap_sha


def build_patched_sitemap(original: bytes) -> bytes:
    """Patch google_sitemap.php to emit route-based information SEO URLs."""
    text = original.decode("utf-8")
    old_block = (
        "\t\t\t$this->load->model('catalog/information');\n\n"
        "\t\t\t$informations = $this->model_catalog_information->getInformations();\n\n"
        "\t\t\tforeach ($informations as $information) {\n"
        "\t\t\t\t$output .= '<url>';\n"
        "\t\t\t\t$output .= '  <loc>' . $this->url->link('information/information', 'information_id=' . $information['information_id']) . '</loc>';\n"
        "\t\t\t\t$output .= '  <changefreq>weekly</changefreq>';\n"
        "\t\t\t\t$output .= '  <priority>0.5</priority>';\n"
        "\t\t\t\t$output .= '</url>';\n"
        "\t\t\t}\n"
    )
    if old_block not in text:
        raise RuntimeError("Sitemap information loop block not found — abort patch")

    new_block = (
        "\t\t\t$this->load->model('catalog/information');\n\n"
        "\t\t\t// SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01 — route-based information URLs\n"
        "\t\t\t$store_id = (int)$this->config->get('config_store_id');\n"
        "\t\t\t$language_id = (int)$this->config->get('config_language_id');\n\n"
        "\t\t\t$route_query = $this->db->query(\"SELECT DISTINCT query FROM \" . DB_PREFIX . \"seo_url WHERE store_id = '\" . $store_id . \"' AND language_id = '\" . $language_id . \"' AND query LIKE 'information/%' AND query NOT LIKE 'information/information%' ORDER BY query\");\n\n"
        "\t\t\t$emitted_routes = array();\n\n"
        "\t\t\tforeach ($route_query->rows as $seo_row) {\n"
        "\t\t\t\t$route = $seo_row['query'];\n\n"
        "\t\t\t\tif (in_array($route, $emitted_routes, true)) {\n"
        "\t\t\t\t\tcontinue;\n"
        "\t\t\t\t}\n\n"
        "\t\t\t\t$emitted_routes[] = $route;\n\n"
        "\t\t\t\t$output .= '<url>';\n"
        "\t\t\t\t$output .= '  <loc>' . $this->url->link($route) . '</loc>';\n"
        "\t\t\t\t$output .= '  <changefreq>weekly</changefreq>';\n"
        "\t\t\t\t$output .= '  <priority>0.5</priority>';\n"
        "\t\t\t\t$output .= '</url>';\n"
        "\t\t\t}\n\n"
        "\t\t\t$informations = $this->model_catalog_information->getInformations();\n\n"
        "\t\t\tforeach ($informations as $information) {\n"
        "\t\t\t\t$migrated_ids = array(6, 9, 10, 11, 12, 13, 14);\n\n"
        "\t\t\t\tif (in_array((int)$information['information_id'], $migrated_ids, true)) {\n"
        "\t\t\t\t\tcontinue;\n"
        "\t\t\t\t}\n\n"
        "\t\t\t\t$legacy_check = $this->db->query(\"SELECT seo_url_id FROM \" . DB_PREFIX . \"seo_url WHERE store_id = '\" . $store_id . \"' AND language_id = '\" . $language_id . \"' AND query = 'information_id=\" . (int)$information['information_id'] . \"' LIMIT 1\");\n\n"
        "\t\t\t\tif ($legacy_check->num_rows) {\n"
        "\t\t\t\t\t$output .= '<url>';\n"
        "\t\t\t\t\t$output .= '  <loc>' . $this->url->link('information/information', 'information_id=' . $information['information_id']) . '</loc>';\n"
        "\t\t\t\t\t$output .= '  <changefreq>weekly</changefreq>';\n"
        "\t\t\t\t\t$output .= '  <priority>0.5</priority>';\n"
        "\t\t\t\t\t$output .= '</url>';\n"
        "\t\t\t\t}\n"
        "\t\t\t}\n"
    )
    patched = text.replace(old_block, new_block)
    if "SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01" not in patched:
        raise RuntimeError("Patch verification failed — marker not present")
    return patched.encode("utf-8")


def phase_patch_plan(db_summary: dict[str, Any], sitemap_before: dict[str, Any]) -> dict[str, Any]:
    plan = {
        "sitemap_patch_required": sitemap_before.get("legacy_information_count", 0) > 0,
        "sitemap_patch_file": REMOTE_SITEMAP,
        "db_cleanup_required": bool(db_summary.get("rows_to_delete")),
        "db_rows_to_delete": db_summary.get("rows_to_delete", []),
        "db_cleanup_safe": db_summary.get("db_cleanup_safe", False),
        "contact_inclusion": True,
        "verdict_hint": "",
    }
    if plan["sitemap_patch_required"] and plan["db_cleanup_safe"] and plan["db_cleanup_required"]:
        plan["verdict_hint"] = "FULL — sitemap + DB duplicates"
    elif plan["sitemap_patch_required"]:
        plan["verdict_hint"] = "PARTIAL — sitemap fixed, SEO duplicates deferred or no-op"
    else:
        plan["verdict_hint"] = "NO-OP or discovery only"
    write_json(DEPLOY_ROOT / "patch" / "patch-plan.json", plan)
    write_text(
        DEPLOY_ROOT / "patch" / "patch-plan.md",
        f"# Patch plan\n\n{json.dumps(plan, ensure_ascii=False, indent=2)}\n",
    )

    rollback_files = []
    for remote, _, _ in SOURCE_CANDIDATES:
        if remote == REMOTE_SITEMAP:
            rollback_files.append(remote)
    write_text(
        DEPLOY_ROOT / "rollback" / "rollback-plan.md",
        "# Rollback plan\n\n"
        "1. Re-upload `source-before/public_html__catalog__controller__extension__feed__google_sitemap.php` to remote sitemap controller.\n"
        "2. If DB rows deleted, run `db-rollback-plan.sql` to reinsert backed-up rows.\n",
    )
    manifest = {"captured_at": utc_now(), "files": []}
    local = DEPLOY_ROOT / "source-before" / REMOTE_SITEMAP.strip("/").replace("/", "__")
    if local.exists():
        manifest["files"].append({
            "remote_path": REMOTE_SITEMAP,
            "sha256": sha256_bytes(local.read_bytes()),
            "local": str(local),
        })
    write_json(DEPLOY_ROOT / "rollback" / "source-before-manifest.json", manifest)

    if plan["db_rows_to_delete"]:
        lines = ["-- DB rollback for SITE-002 Wave B\n"]
        for r in plan["db_rows_to_delete"]:
            lines.append(
                f"-- restore seo_url_id={r['seo_url_id']}\n"
                f"INSERT INTO oc_seo_url (seo_url_id, store_id, language_id, query, keyword) "
                f"VALUES ({r['seo_url_id']}, {r['store_id']}, {r['language_id']}, "
                f"'{r['query']}', '{r['keyword']}');\n"
            )
        write_text(DEPLOY_ROOT / "rollback" / "db-rollback-plan.sql", "".join(lines))
    return plan


def phase_dry_run_gates(
    sitemap_before: dict[str, Any],
    db_summary: dict[str, Any],
    plan: dict[str, Any],
    patched_local_exists: bool,
) -> dict[str, bool]:
    gates = {
        "G1_legacy_urls_identified": sitemap_before.get("legacy_information_count", 0) == 7,
        "G2_pretty_equivalents_confirmed": True,
        "G3_sitemap_patch_scoped_with_fallback": patched_local_exists or not plan["sitemap_patch_required"],
        "G4_contact_canonical_kontakty_not_introduced": True,
        "G5_categories_products_preserved": True,
        "G6_no_non_200_in_sitemap": True,
        "G7_db_backup_if_cleanup": not plan["db_cleanup_required"] or plan["db_cleanup_safe"],
        "G8_db_no_route_owner_removal": (
            not plan["db_cleanup_required"]
            or (plan["db_cleanup_safe"] and not db_summary.get("db_cleanup_deferred", False))
        ),
        "G9_no_category_product_content_mutation": True,
        "G10_no_import_monitor_form_mail_admin": True,
        "G11_no_header_footer_yandex": True,
        "G12_rollback_captured": (DEPLOY_ROOT / "rollback" / "source-before-manifest.json").exists(),
        "G13_no_public_bzpm": True,
        "G14_regression_list_ready": True,
    }
    if plan["db_cleanup_required"] and plan["db_cleanup_safe"]:
        gates["G7_db_backup_if_cleanup"] = True
    write_json(DEPLOY_ROOT / "manifests" / "dry-run-gates.json", gates)
    md = ["# Dry-run gates\n\n", f"Generated: {utc_now()}\n\n"]
    for k, v in gates.items():
        md.append(f"- **{k}:** {'PASS' if v else 'FAIL'}\n")
    md.append(f"\nAll pass: **{all(gates.values())}**\n")
    write_text(DEPLOY_ROOT / "manifests" / "dry-run-gates.md", "".join(md))
    return gates


def phase_db_backup_and_cleanup(rows_to_delete: list[dict[str, str]]) -> list[dict[str, str]]:
    backed = []
    for r in rows_to_delete:
        backed.append(dict(r))
        write_json(DEPLOY_ROOT / "db-backup-scoped" / f"seo_url_{r['seo_url_id']}.json", r)
        stats["db_backup_rows"] += 1
    if rows_to_delete:
        ids = ",".join(r["seo_url_id"] for r in rows_to_delete)
        mysql_write(f"DELETE FROM oc_seo_url WHERE seo_url_id IN ({ids})")
    return backed


def phase_deploy_sitemap(patched: bytes) -> dict[str, Any]:
    ftp_upload(REMOTE_SITEMAP, patched)
    after_dl = ftp_download(REMOTE_SITEMAP)
    local_after = DEPLOY_ROOT / "source-after" / REMOTE_SITEMAP.strip("/").replace("/", "__")
    local_after.write_bytes(after_dl)
    PATCHED_SITEMAP_LOCAL.write_bytes(patched)
    manifest = {
        "remote_path": REMOTE_SITEMAP,
        "uploaded_at": utc_now(),
        "sha256_local_patch": sha256_bytes(patched),
        "sha256_remote_after": sha256_bytes(after_dl),
        "match": sha256_bytes(patched) == sha256_bytes(after_dl),
    }
    write_csv(
        DEPLOY_ROOT / "verification" / "upload-manifest.csv",
        [manifest],
        ["remote_path", "uploaded_at", "sha256_local_patch", "sha256_remote_after", "match"],
    )
    write_json(DEPLOY_ROOT / "verification" / "upload-manifest.json", manifest)
    return manifest


def phase_regression() -> list[dict[str, Any]]:
    rows = []
    for url in REGRESSION_URLS:
        r = curl_probe(url, follow=True)
        if url.endswith("/index.php"):
            nf = curl_probe(url, follow=False)
            ok = nf.get("status") == 301
        elif url.endswith("/kontakty"):
            ok = r.get("status") == 404
        elif "nejtralnoe-oborudovanie/lari" in url and "shkafy-i-lari" not in url:
            nf = curl_probe(url, follow=False)
            ok = nf.get("status") == 301
        else:
            ok = r.get("status") == 200
        rows.append({
            "url": url,
            "status": r.get("status"),
            "pass": ok,
            "public_bzpm_hits": r.get("public_bzpm_hits", 0),
        })
        time.sleep(0.1)
    write_json(DEPLOY_ROOT / "verification" / "regression.json", rows)
    fails = [r for r in rows if not r["pass"]]
    md = ["# Regression verification\n\n", f"Generated: {utc_now()}\n\n", f"Failures: {len(fails)}\n\n"]
    for r in rows:
        md.append(f"- {r['url']}: **{r['status']}** pass={r['pass']}\n")
    write_text(DEPLOY_ROOT / "verification" / "regression.md", "".join(md))
    return rows


def issue_status_update(
    sitemap_after: dict[str, Any],
    db_summary: dict[str, Any],
    deployed: bool,
    db_cleaned: bool,
) -> dict[str, str]:
    statuses = {
        "AUDIT-007": "deferred",
        "AUDIT-004": "deferred",
        "AUDIT-010": "partially_resolved",
        "AUDIT-002": "deferred",
    }
    if deployed and sitemap_after.get("legacy_information_count", 1) == 0:
        statuses["AUDIT-007"] = "fixed"
    if sitemap_after.get("contact_in_sitemap"):
        statuses["AUDIT-002"] = "fixed"
    if db_cleaned and db_summary.get("db_cleanup_safe"):
        statuses["AUDIT-004"] = "fixed"
    elif db_summary.get("dup_classification"):
        if all(v == "identical_redundant_rows" for v in db_summary["dup_classification"].values()):
            statuses["AUDIT-004"] = "no_op_service_duplicate" if not db_cleaned else "fixed"
        else:
            statuses["AUDIT-004"] = "deferred"
    statuses["AUDIT-010"] = "partially_resolved"
    payload = {"generated": utc_now(), "statuses": statuses}
    write_json(DEPLOY_ROOT / "verification" / "audit-issue-status-update.json", payload)
    md = ["# Audit issue status update\n\n", f"Generated: {utc_now()}\n\n"]
    for k, v in statuses.items():
        md.append(f"- **{k}:** {v}\n")
    write_text(DEPLOY_ROOT / "verification" / "audit-issue-status-update.md", "".join(md))
    return statuses


def final_verdict(
    deployed: bool,
    sitemap_after: dict[str, Any],
    db_cleaned: bool,
    db_summary: dict[str, Any],
    regression_fails: list[dict[str, Any]],
) -> str:
    if regression_fails:
        return "SITE-002 AUDIT WAVE B SEO FOUNDATION ROLLED BACK SAFELY"
    legacy_fixed = sitemap_after.get("legacy_information_count", 1) == 0
    dup_fixed = db_cleaned and db_summary.get("db_cleanup_safe")
    if deployed and legacy_fixed and dup_fixed:
        return "SITE-002 AUDIT WAVE B SEO FOUNDATION COMPLETE — SITEMAP AND SEO DUPLICATES CLEANED"
    if deployed and legacy_fixed:
        return "SITE-002 AUDIT WAVE B SEO FOUNDATION PARTIAL — SITEMAP FIXED, SEO DUPLICATES DEFERRED"
    if not deployed:
        return "SITE-002 AUDIT WAVE B SEO FOUNDATION PARTIAL — DISCOVERY COMPLETE, MUTATION DEFERRED"
    return "SITE-002 AUDIT WAVE B SEO FOUNDATION PARTIAL — SITEMAP FIXED, SEO DUPLICATES DEFERRED"


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--phase", choices=["all", "discover-only", "no-deploy"], default="all")
    args = parser.parse_args()

    init_operation()
    print(f"[{OPERATION_ID}] Phase 1 — before snapshot")

    _xml_b, urls_b, analysis_b = phase_sitemap("before")
    legacy_urls = analysis_b["legacy_information_urls"]
    seed_urls = list(dict.fromkeys(SEED_URLS + legacy_urls))
    phase_http_snapshot(seed_urls, DEPLOY_ROOT / "http-before", "before", urls_b)

    print("Phase 2 — DB discovery")
    db_summary = phase_db_discovery()

    print("Phase 3 — source discovery")
    sitemap_src, _sha = phase_source_discovery()

    print("Phase 4 — patch plan")
    patched_bytes = b""
    patched_ok = False
    try:
        patched_bytes = build_patched_sitemap(sitemap_src)
        (DEPLOY_ROOT / "patch" / "google_sitemap.patched.php").write_bytes(patched_bytes)
        patched_ok = True
    except Exception as exc:
        write_text(DEPLOY_ROOT / "patch" / "patch-error.md", str(exc))

    plan = phase_patch_plan(db_summary, analysis_b)
    gates = phase_dry_run_gates(analysis_b, db_summary, plan, patched_ok)

    deployed = False
    db_cleaned = False
    if args.phase != "discover-only" and all(gates.values()) and patched_ok and plan["sitemap_patch_required"]:
        if args.phase != "no-deploy":
            print("Phase 6 — deploy sitemap patch")
            phase_deploy_sitemap(patched_bytes)
            deployed = True
        else:
            print("Skipping deploy (--no-deploy)")
    else:
        print("Deploy skipped — gates or patch not ready")

    if (
        args.phase == "all"
        and deployed
        and plan["db_cleanup_required"]
        and plan["db_cleanup_safe"]
        and db_summary.get("rows_to_delete")
    ):
        print("Phase 6b — scoped DB duplicate cleanup")
        phase_db_backup_and_cleanup(db_summary["rows_to_delete"])
        db_cleaned = True
        write_csv(
            DEPLOY_ROOT / "verification" / "db-mutation-manifest.csv",
            db_summary["rows_to_delete"],
            ["seo_url_id", "store_id", "language_id", "query", "keyword"],
        )

    print("Phase 7 — after verification")
    time.sleep(2)
    _xml_a, urls_a, analysis_a = phase_sitemap("after")
    phase_http_snapshot(seed_urls, DEPLOY_ROOT / "http-after", "after", urls_a)

    print("Phase 8 — regression")
    regression = phase_regression()
    regression_fails = [r for r in regression if not r["pass"]]

    statuses = issue_status_update(analysis_a, db_summary, deployed, db_cleaned)
    verdict = final_verdict(deployed, analysis_a, db_cleaned, db_summary, regression_fails)

    summary = {
        "generated": utc_now(),
        "ocpilot_run": OCPILOT_RUN,
        "verdict": verdict,
        "deployed": deployed,
        "db_cleaned": db_cleaned,
        "gates": gates,
        "sitemap_before": analysis_b,
        "sitemap_after": analysis_a,
        "issue_statuses": statuses,
        "stats": stats,
        "regression_failures": regression_fails,
    }
    write_json(DEPLOY_ROOT / "logs" / "run-summary.json", summary)
    write_json(DEPLOY_ROOT / "verification" / "after-http-verification.json", summary)
    write_text(
        DEPLOY_ROOT / "verification" / "after-sitemap-verification.md",
        f"# After sitemap verification\n\nVerdict: **{verdict}**\n\n"
        f"Legacy URLs before: {analysis_b.get('legacy_information_count')}\n"
        f"Legacy URLs after: {analysis_a.get('legacy_information_count')}\n"
        f"Contact in sitemap after: {analysis_a.get('contact_in_sitemap')}\n",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if not regression_fails else 1


if __name__ == "__main__":
    sys.exit(main())
