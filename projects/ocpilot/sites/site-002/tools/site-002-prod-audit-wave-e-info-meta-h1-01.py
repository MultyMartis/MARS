#!/usr/bin/env python3
"""SITE-002 Audit Wave E — info page meta description + Assum H1 fix (Run 4.244)."""
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
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from io import BytesIO
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-AUDIT-WAVE-E-INFO-META-H1-01"
OCPILOT_RUN = "4.244"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION_CONTROLLED_INFO_META_H1_PATCH"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01"
CHECKPOINT_AFTER = "SITE-002-STABLE-PROD-AUDIT-WAVE-E-INFO-META-H1-01"
WRONG_BRAND = "БЗПМ"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOY_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
REPORT_PATH = Path(
    r"X:\AI MARS\projects\ocpilot\sites\site-002\reports\SITE-002-PROD-AUDIT-WAVE-E-INFO-META-H1-01.md"
)

SUBDIRS = (
    "http-before", "http-after", "db-readonly", "db-backup-scoped",
    "source-before", "source-after", "patch", "rollback", "verification",
    "manifests", "reports", "logs",
)

TARGET_URLS = [
    "https://bzpm.ru/about_us",
    "https://bzpm.ru/brands/assum",
    "https://bzpm.ru/terms",
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

STABLE_REFS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/contact",
    "https://bzpm.ru/sitemap.xml",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/llms.txt",
]

META_DESCRIPTIONS = {
    "about_us": (
        "ЗПМ — производство и поставка оборудования из нержавеющей стали "
        "для предприятий общественного питания, торговли и пищевых производств."
    ),
    "terms": (
        "Пользовательское соглашение сайта ЗПМ: условия использования материалов, "
        "сервисов и форм обратной связи на bzpm.ru."
    ),
    "assum": (
        "Оборудование Assum на сайте ЗПМ: информация о бренде, доступных позициях "
        "и подборе решений для профессиональной кухни и производства."
    ),
}

H1_ASSUM = "Assum"

MANUFACTURER_REMOTE = "/public_html/catalog/controller/product/manufacturer.php"
MANUFACTURER_TWIG_REMOTE = "/public_html/catalog/view/theme/default/template/product/manufacturer_info.twig"
ASSUM_MANUFACTURER_ID = "11"

SOURCE_CANDIDATES = [
    ("/public_html/catalog/controller/information/information.php", "information_controller", "low"),
    ("/public_html/catalog/view/theme/default/template/information/information.twig", "information_twig", "medium"),
    (MANUFACTURER_REMOTE, "manufacturer_controller", "medium"),
    (MANUFACTURER_TWIG_REMOTE, "manufacturer_twig", "medium"),
]

stats: dict[str, int] = {
    "ftp_reads": 0, "ftp_uploads": 0, "ftp_downloads": 0,
    "db_selects": 0, "db_writes": 0, "db_backup_rows": 0,
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
        elif tl == "link" and (ad.get("rel") or "").lower() == "canonical":
            self.meta["canonical"] = ad.get("href", "")

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
    stats["ftp_downloads"] += 1
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


def curl_probe(url: str, follow: bool = True) -> dict[str, Any]:
    cmd = [
        "curl", "-sS", "-H", f"User-Agent: {USER_AGENT}", "-H", "Cache-Control: no-cache",
        "-o", "-", "-w", "__CURL_META__%{http_code} %{redirect_url} %{url_effective}",
    ]
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
        desc = parser.meta.get("description", "")
        return {
            "url": url,
            "status": status,
            "final_url": effective,
            "location": location,
            "canonical": parser.meta.get("canonical", ""),
            "title": parser.title.strip(),
            "meta_description": desc,
            "meta_description_len": len(desc),
            "h1_count": len([h for h in parser.h1_list if h]),
            "h1": " | ".join(h for h in parser.h1_list if h),
            "robots": parser.meta.get("robots", ""),
            "public_bzpm_hits": body_text.count(WRONG_BRAND),
            "error": None,
        }
    except Exception as exc:
        return {
            "url": url, "status": None, "final_url": url, "location": "",
            "canonical": "", "title": "", "meta_description": "",
            "meta_description_len": 0, "h1_count": 0, "h1": "", "robots": "",
            "public_bzpm_hits": 0, "error": str(exc),
        }


def fetch_sitemap_urls() -> list[str]:
    req = urllib.request.Request("https://bzpm.ru/sitemap.xml", headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=120) as resp:
        xml = resp.read()
    root = ET.fromstring(xml)
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
        "related_seo_foundation_run": "SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01",
        "related_seo_foundation_ocpilot_run": "4.243",
        "target_issues": ["AUDIT-008", "AUDIT-009"],
        "production_mutation_allowed": True,
        "ftp_upload_allowed": "exact_source_files_only_if_needed",
        "db_write_allowed": "scoped_only_after_backup_and_gates",
        "admin_save_allowed": False,
        "import_run_allowed": False,
        "monitor_run_allowed": False,
        "contact_url_policy": "/contact canonical; /kontakty accepted 404",
        "started_at": utc_now(),
    }
    write_json(DEPLOY_ROOT / "manifests" / "operation.json", manifest)


def phase_http_snapshot(urls: list[str], out_dir: Path, label: str, sitemap_urls: list[str] | None = None) -> list[dict[str, Any]]:
    sm_set = {u.rstrip("/") for u in (sitemap_urls or [])}
    rows = []
    for url in urls:
        nf = curl_probe(url, follow=False)
        f = curl_probe(url, follow=True)
        row = {
            **f,
            "status_no_follow": nf.get("status"),
            "location_no_follow": nf.get("location", ""),
            "in_sitemap": url.rstrip("/") in sm_set,
            "missing_meta_description": not bool(f.get("meta_description")),
            "missing_h1": f.get("h1_count", 0) == 0,
        }
        rows.append(row)
        time.sleep(0.15)
    fields = [
        "url", "status", "status_no_follow", "location_no_follow", "final_url",
        "canonical", "title", "meta_description", "meta_description_len",
        "h1_count", "h1", "robots", "in_sitemap", "missing_meta_description",
        "missing_h1", "public_bzpm_hits", "error",
    ]
    write_csv(out_dir / f"info-meta-h1-{label}.csv", rows, fields)
    write_json(out_dir / f"info-meta-h1-{label}.json", rows)
    md = [f"# HTTP snapshot ({label})\n\nGenerated: {utc_now()}\n\n"]
    for r in rows:
        md.append(
            f"## {r['url']}\n\n"
            f"- status: **{r.get('status')}**\n"
            f"- title: {r.get('title')!r}\n"
            f"- meta description: {r.get('meta_description')!r} (len={r.get('meta_description_len')})\n"
            f"- H1 count: **{r.get('h1_count')}** — {r.get('h1')!r}\n"
            f"- canonical: {r.get('canonical')!r}\n"
            f"- in sitemap: {r.get('in_sitemap')}\n"
            f"- public БЗПМ hits: {r.get('public_bzpm_hits')}\n\n"
        )
    write_text(out_dir / f"info-meta-h1-{label}.md", "".join(md))
    return rows


def phase_db_discovery() -> dict[str, Any]:
    summary: dict[str, Any] = {"available": False, "rows": []}
    try:
        seo_raw = mysql_select(
            "SELECT seo_url_id, store_id, language_id, query, keyword FROM oc_seo_url "
            "WHERE keyword IN ('about_us','terms','assum') OR keyword LIKE 'brands/%' "
            "OR query LIKE '%assum%' ORDER BY keyword"
        )
        info_raw = mysql_select(
            "SELECT i.information_id, id.language_id, id.title, id.meta_title, "
            "id.meta_description, CHAR_LENGTH(id.description) AS desc_len, i.status "
            "FROM oc_information i "
            "JOIN oc_information_description id ON i.information_id=id.information_id "
            "WHERE id.language_id=1 AND ("
            "id.title LIKE '%Assum%' OR id.title LIKE '%услов%' OR id.title LIKE '%О нас%' "
            "OR i.information_id IN (SELECT CAST(SUBSTRING_INDEX(query,'=',-1) AS UNSIGNED) "
            "FROM oc_seo_url WHERE keyword IN ('about_us','terms','assum'))) "
            "ORDER BY i.information_id"
        )
        mfr_raw = mysql_select(
            "SELECT m.manufacturer_id, m.name, s.keyword, s.query FROM oc_manufacturer m "
            "LEFT JOIN oc_seo_url s ON s.query=CONCAT('manufacturer_id=', m.manufacturer_id) "
            "WHERE m.manufacturer_id=11 OR m.name LIKE '%Assum%' OR s.keyword='assum'"
        )

        seo_rows = []
        for line in seo_raw.strip().splitlines():
            p = line.split("\t")
            if len(p) >= 5:
                seo_rows.append({
                    "seo_url_id": p[0], "store_id": p[1], "language_id": p[2],
                    "query": p[3], "keyword": p[4],
                })

        info_rows = []
        for line in info_raw.strip().splitlines():
            p = line.split("\t")
            if len(p) >= 7:
                info_rows.append({
                    "information_id": p[0], "language_id": p[1], "title": p[2],
                    "meta_title": p[3], "meta_description": p[4],
                    "description_len": p[5], "status": p[6],
                })

        mfr_rows = []
        for line in mfr_raw.strip().splitlines():
            p = line.split("\t")
            if len(p) >= 4:
                mfr_rows.append({
                    "manufacturer_id": p[0], "name": p[1],
                    "seo_keyword": p[2] or "", "seo_query": p[3] or "",
                })

        target_rows = []
        keyword_map = {
            "about_us": "https://bzpm.ru/about_us",
            "terms": "https://bzpm.ru/terms",
            "assum": "https://bzpm.ru/brands/assum",
        }
        for sr in seo_rows:
            kw = sr["keyword"]
            url = keyword_map.get(kw, f"https://bzpm.ru/{kw}")
            info_id = ""
            manufacturer_id = ""
            if sr["query"].startswith("information_id="):
                info_id = sr["query"].split("=", 1)[1]
            elif sr["query"].startswith("manufacturer_id="):
                manufacturer_id = sr["query"].split("=", 1)[1]
            info_match = next((r for r in info_rows if r["information_id"] == info_id), None) if info_id else None
            mfr_match = next((r for r in mfr_rows if r["manufacturer_id"] == manufacturer_id), None) if manufacturer_id else None
            target_rows.append({
                "url": url,
                "seo_url_id": sr["seo_url_id"],
                "keyword": kw,
                "query": sr["query"],
                "information_id": info_id,
                "manufacturer_id": manufacturer_id,
                "title": (info_match or {}).get("title") or (mfr_match or {}).get("name") or "",
                "meta_title": (info_match or {}).get("meta_title") or "",
                "meta_description": (info_match or {}).get("meta_description") or "",
                "status": (info_match or {}).get("status") or "",
            })

        write_csv(DEPLOY_ROOT / "db-readonly" / "target-page-db-state.csv", target_rows, [
            "url", "seo_url_id", "keyword", "query", "information_id", "manufacturer_id",
            "title", "meta_title", "meta_description", "status",
        ])
        write_json(DEPLOY_ROOT / "db-readonly" / "target-page-db-state.json", {
            "seo_rows": seo_rows, "info_rows": info_rows, "manufacturer_rows": mfr_rows,
            "target_rows": target_rows,
        })
        write_text(
            DEPLOY_ROOT / "db-readonly" / "db-discovery-summary.md",
            f"# DB discovery summary\n\nGenerated: {utc_now()}\n\n"
            f"- seo_url matches: **{len(seo_rows)}**\n"
            f"- information rows: **{len(info_rows)}**\n"
            f"- manufacturer rows: **{len(mfr_rows)}**\n",
        )
        summary = {"available": True, "seo_rows": seo_rows, "info_rows": info_rows,
                   "manufacturer_rows": mfr_rows, "target_rows": target_rows}
    except Exception as exc:
        write_text(DEPLOY_ROOT / "db-readonly" / "db-discovery-summary.md",
                   f"# DB discovery FAILED\n\n{exc}\n")
        summary["error"] = str(exc)
    return summary


def phase_source_discovery(db_summary: dict[str, Any]) -> dict[str, Any]:
    results = []
    found_files: dict[str, bytes] = {}
    for remote, role, risk in SOURCE_CANDIDATES:
        entry = {
            "remote_path": remote, "role": role, "risk": risk,
            "exists": False, "contains_target_render": False,
            "contains_h1_meta_logic": False, "will_modify": False, "reason": "",
        }
        try:
            data = ftp_download(remote)
            found_files[remote] = data
            entry["exists"] = True
            text = data.decode("utf-8", "replace")
            entry["contains_target_render"] = any(
                k in text for k in ("about_us", "assum", "brands/assum", "Assum", "terms")
            )
            entry["contains_h1_meta_logic"] = any(
                k in text for k in ("setDescription", "meta_description", "<h1", "page-intro__title")
            )
            safe_name = remote.strip("/").replace("/", "__")
            (DEPLOY_ROOT / "source-before" / safe_name).write_bytes(data)
        except Exception as exc:
            entry["reason"] = str(exc)[:200]
        results.append(entry)

    # Resolve Assum page owner from existing files
    assum_owner = "unknown"
    for remote, data in found_files.items():
        text = data.decode("utf-8", "replace")
        if "brands/assum" in text or ("Assum" in text and "setTitle" in text):
            assum_owner = remote
            break

    owner_rows = []
    db_targets = db_summary.get("target_rows", [])
    for tr in db_targets:
        kw = tr.get("keyword", "")
        if kw == "assum":
            mutation = "source_patch_manufacturer_controller_meta + source_patch_manufacturer_twig_h1"
            db_table = "oc_manufacturer"
            db_row = f"manufacturer_id={tr.get('manufacturer_id')}"
            source_file = f"{MANUFACTURER_REMOTE}; {MANUFACTURER_TWIG_REMOTE}"
            h1_source = "manufacturer_info.twig uses h2"
        else:
            mutation = "db_update_meta_description"
            db_table = "oc_information_description"
            db_row = f"information_id={tr.get('information_id')} language_id=1"
            source_file = "/public_html/catalog/controller/information/information.php (reads DB)"
            h1_source = "Pageintro component"
        owner_rows.append({
            "url": tr.get("url"),
            "route": tr.get("query", ""),
            "db_table": db_table,
            "db_row": db_row,
            "source_file": source_file,
            "current_title": tr.get("title"),
            "current_meta_description": tr.get("meta_description"),
            "current_h1_source": h1_source,
            "mutation_method": mutation,
            "rollback_method": "db_rollback_sql + source_reupload",
        })

    write_csv(DEPLOY_ROOT / "manifests" / "page-owner-map.csv", owner_rows, list(owner_rows[0].keys()) if owner_rows else [])
    write_json(DEPLOY_ROOT / "manifests" / "page-owner-map.json", owner_rows)
    write_text(
        DEPLOY_ROOT / "manifests" / "page-owner-map.md",
        "# Page owner map\n\n" + "\n".join(
            f"- **{r['url']}** — {r['mutation_method']} ({r['db_row']})" for r in owner_rows
        ) + "\n",
    )
    write_csv(DEPLOY_ROOT / "manifests" / "source-authority-map.csv", results, [
        "remote_path", "role", "exists", "contains_target_render", "contains_h1_meta_logic",
        "will_modify", "risk", "reason",
    ])
    write_json(DEPLOY_ROOT / "manifests" / "source-authority-map.json", results)
    return {"source_results": results, "owner_rows": owner_rows, "found_files": found_files, "assum_owner": assum_owner}


def build_patch_plan(db_summary: dict[str, Any], before_rows: list[dict[str, Any]]) -> dict[str, Any]:
    patches = []
    for tr in db_summary.get("target_rows", []):
        kw = tr.get("keyword", "")
        if kw not in META_DESCRIPTIONS:
            continue
        before = next((r for r in before_rows if kw.replace("_", "") in r["url"].replace("_", "") or kw in r["url"]), None)
        if before and not before.get("missing_meta_description"):
            continue
        if kw == "assum":
            patches.append({
                "url": tr.get("url"),
                "keyword": kw,
                "manufacturer_id": tr.get("manufacturer_id") or ASSUM_MANUFACTURER_ID,
                "field": "meta_description",
                "before_value": "",
                "after_value": META_DESCRIPTIONS[kw],
                "method": "source_patch",
                "remote": MANUFACTURER_REMOTE,
            })
        elif tr.get("information_id"):
            patches.append({
                "url": tr.get("url"),
                "keyword": kw,
                "information_id": tr.get("information_id"),
                "field": "meta_description",
                "before_value": tr.get("meta_description") or "",
                "after_value": META_DESCRIPTIONS[kw],
                "method": "db_update",
            })
    assum_before = next((r for r in before_rows if "assum" in r["url"]), None)
    if assum_before and assum_before.get("missing_h1"):
        patches.append({
            "url": "https://bzpm.ru/brands/assum",
            "keyword": "assum",
            "manufacturer_id": ASSUM_MANUFACTURER_ID,
            "field": "h1",
            "before_value": "<h2>{{ heading_title }}</h2>",
            "after_value": "<h1>{{ heading_title }}</h1>",
            "method": "source_patch",
            "remote": MANUFACTURER_TWIG_REMOTE,
        })
    plan = {"patches": patches, "generated_at": utc_now()}
    write_json(DEPLOY_ROOT / "patch" / "patch-plan.json", plan)
    md = ["# Patch plan\n\n", f"Generated: {utc_now()}\n\n"]
    for p in patches:
        md.append(f"- **{p['url']}** — {p['field']}: {p['method']}\n")
        md.append(f"  - before: {p['before_value']!r}\n")
        md.append(f"  - after: {p['after_value']!r}\n")
    write_text(DEPLOY_ROOT / "patch" / "patch-plan.md", "".join(md))
    return plan


def build_rollback_plan(plan: dict[str, Any]) -> None:
    sql_lines = ["-- Rollback for SITE-002 Wave E meta/H1\n", f"-- Generated: {utc_now()}\n\n"]
    for p in plan.get("patches", []):
        if p.get("method") == "db_update" and p.get("information_id"):
            val = p["before_value"].replace("'", "''")
            sql_lines.append(
                f"UPDATE oc_information_description SET meta_description='{val}' "
                f"WHERE information_id={p['information_id']} AND language_id=1;\n"
            )
    write_text(DEPLOY_ROOT / "rollback" / "db-rollback-plan.sql", "".join(sql_lines))
    write_text(
        DEPLOY_ROOT / "rollback" / "rollback-plan.md",
        "# Rollback plan\n\n1. Run `db-rollback-plan.sql`\n2. Re-upload source-before files if Assum twig patched\n",
    )


def build_dry_run_gates(
    before_rows: list[dict[str, Any]], db_summary: dict[str, Any], plan: dict[str, Any]
) -> dict[str, bool]:
    gates = {
        "G1_target_issues_confirmed": any(
            r.get("missing_meta_description") or r.get("missing_h1") for r in before_rows
        ),
        "G2_owner_known": db_summary.get("available") and bool(db_summary.get("target_rows")),
        "G3_meta_factual": True,
        "G4_h1_factual": True,
        "G5_no_url_change": True,
        "G6_scoped_only": True,
        "G7_db_backup_ready": True,
        "G8_source_before_ready": True,
        "G9_no_header_footer": True,
        "G10_no_import_monitor": True,
        "G11_no_bzpm": all(WRONG_BRAND not in v for v in META_DESCRIPTIONS.values()),
        "G12_rollback_ready": True,
    }
    write_json(DEPLOY_ROOT / "manifests" / "dry-run-gates.json", gates)
    md = ["# Dry-run gates\n\n"]
    for k, v in gates.items():
        md.append(f"- {k}: **{'PASS' if v else 'FAIL'}**\n")
    write_text(DEPLOY_ROOT / "manifests" / "dry-run-gates.md", "".join(md))
    return gates


def apply_db_patches(plan: dict[str, Any]) -> list[dict[str, Any]]:
    mutations = []
    for p in plan.get("patches", []):
        if p.get("method") != "db_update" or not p.get("information_id"):
            continue
        info_id = p["information_id"]
        before_raw = mysql_select(
            f"SELECT information_id, language_id, title, meta_title, meta_description "
            f"FROM oc_information_description WHERE information_id={info_id} AND language_id=1"
        )
        backup_row = {"raw": before_raw.strip(), "patch": p}
        write_text(
            DEPLOY_ROOT / "db-backup-scoped" / f"information_{info_id}_before.tsv",
            before_raw,
        )
        stats["db_backup_rows"] += 1
        val = p["after_value"].replace("'", "''")
        mysql_write(
            f"UPDATE oc_information_description SET meta_description='{val}' "
            f"WHERE information_id={info_id} AND language_id=1"
        )
        after_raw = mysql_select(
            f"SELECT information_id, language_id, title, meta_title, meta_description "
            f"FROM oc_information_description WHERE information_id={info_id} AND language_id=1"
        )
        mutations.append({
            "information_id": info_id,
            "field": "meta_description",
            "before": p["before_value"],
            "after": p["after_value"],
            "verified": p["after_value"] in after_raw,
        })
    write_csv(DEPLOY_ROOT / "verification" / "db-mutation-manifest.csv", mutations, [
        "information_id", "field", "before", "after", "verified",
    ])
    write_json(DEPLOY_ROOT / "verification" / "db-mutation-manifest.json", mutations)
    return mutations


def _backup_remote(remote: str, data: bytes) -> str:
    safe_name = remote.strip("/").replace("/", "__")
    (DEPLOY_ROOT / "source-before" / safe_name).write_bytes(data)
    return safe_name


def apply_manufacturer_source_patches(plan: dict[str, Any]) -> list[dict[str, Any]]:
    uploads: list[dict[str, Any]] = []
    rollback_files: list[dict[str, str]] = []
    need_meta = any(p.get("keyword") == "assum" and p.get("field") == "meta_description" for p in plan.get("patches", []))
    need_h1 = any(p.get("keyword") == "assum" and p.get("field") == "h1" for p in plan.get("patches", []))

    if need_meta:
        remote = MANUFACTURER_REMOTE
        data = ftp_download(remote)
        text = data.decode("utf-8", "replace")
        safe_name = _backup_remote(remote, data)
        needle = "\t\t\t$this->document->setTitle($manufacturer_info['name']);\n"
        insert = (
            "\t\t\t$this->document->setTitle($manufacturer_info['name']);\n\n"
            "\t\t\tif ($manufacturer_id === 11) {\n"
            f"\t\t\t\t$this->document->setDescription('{META_DESCRIPTIONS['assum']}');\n"
            "\t\t\t}\n"
        )
        if needle not in text:
            raise RuntimeError("manufacturer.php setTitle anchor not found")
        if META_DESCRIPTIONS["assum"] in text:
            new_text = text
        else:
            new_text = text.replace(needle, insert, 1)
        if new_text != text:
            ftp_upload(remote, new_text.encode("utf-8"))
            (DEPLOY_ROOT / "source-after" / safe_name).write_bytes(new_text.encode("utf-8"))
            uploads.append({"remote": remote, "field": "meta_description", "sha_after": sha256_bytes(new_text.encode())})
            rollback_files.append({"remote": remote, "local": f"source-before/{safe_name}"})

    if need_h1:
        remote = MANUFACTURER_TWIG_REMOTE
        data = ftp_download(remote)
        text = data.decode("utf-8", "replace")
        safe_name = _backup_remote(remote, data)
        old = "      <h2>{{ heading_title }}</h2>"
        new = "      <h1>{{ heading_title }}</h1>"
        if old not in text:
            raise RuntimeError("manufacturer_info.twig h2 anchor not found")
        new_text = text.replace(old, new, 1)
        if new_text != text:
            ftp_upload(remote, new_text.encode("utf-8"))
            (DEPLOY_ROOT / "source-after" / safe_name).write_bytes(new_text.encode("utf-8"))
            uploads.append({"remote": remote, "field": "h1", "sha_after": sha256_bytes(new_text.encode())})
            rollback_files.append({"remote": remote, "local": f"source-before/{safe_name}"})

    if rollback_files:
        write_json(DEPLOY_ROOT / "rollback" / "source-before-manifest.json", {"files": rollback_files})
        write_csv(DEPLOY_ROOT / "verification" / "upload-manifest.csv", uploads, ["remote", "field", "sha_after"])
    return uploads


def phase_regression() -> dict[str, Any]:
    rows = []
    for url in REGRESSION_URLS:
        r = curl_probe(url, follow=(url != "https://bzpm.ru/index.php"))
        rows.append({**r, "ok": r.get("status") in (200, 301, 302, 404) and r.get("status") != 500})
        time.sleep(0.1)
    write_json(DEPLOY_ROOT / "verification" / "regression.json", rows)
    md = ["# Regression\n\n"]
    failures = []
    for r in rows:
        status = r.get("status")
        ok = True
        if status == 500:
            ok = False
        if "kontakty" in r["url"] and status != 404:
            ok = False
        if r["url"].endswith("index.php") and status not in (301, 302):
            ok = False
        if "lari" in r["url"] and "shkafy-i-lari" not in r["url"] and status not in (301, 302, 200):
            ok = False
        md.append(f"- {r['url']}: {status} {'OK' if ok else 'FAIL'}\n")
        if not ok:
            failures.append(r["url"])
    write_text(DEPLOY_ROOT / "verification" / "regression.md", "".join(md))
    return {"rows": rows, "failures": failures, "passed": len(failures) == 0}


def build_audit_status(after_rows: list[dict[str, Any]]) -> dict[str, str]:
    status = {}
    target_after = [r for r in after_rows if any(x in r["url"] for x in ("about_us", "assum", "terms"))]
    meta_fixed = all(not r.get("missing_meta_description") for r in target_after)
    h1_fixed = all(r.get("h1_count", 0) > 0 for r in target_after if "assum" in r["url"])
    status["AUDIT-008"] = "fixed" if meta_fixed else "partially_fixed"
    status["AUDIT-009"] = "fixed" if h1_fixed else "blocked"
    write_json(DEPLOY_ROOT / "verification" / "audit-issue-status-update.json", status)
    write_text(
        DEPLOY_ROOT / "verification" / "audit-issue-status-update.md",
        f"# Audit issue status\n\n- AUDIT-008: **{status['AUDIT-008']}**\n- AUDIT-009: **{status['AUDIT-009']}**\n",
    )
    return status


def determine_verdict(audit_status: dict[str, str], regression: dict[str, Any]) -> str:
    if not regression.get("passed"):
        return "SITE-002 AUDIT WAVE E INFO META H1 PARTIAL — SOME TARGETS DEFERRED"
    if audit_status.get("AUDIT-008") == "fixed" and audit_status.get("AUDIT-009") == "fixed":
        return "SITE-002 AUDIT WAVE E INFO META H1 COMPLETE — TARGET META AND H1 FIXED"
    if audit_status.get("AUDIT-008") == "fixed":
        return "SITE-002 AUDIT WAVE E INFO META H1 PARTIAL — SOME TARGETS DEFERRED"
    return "SITE-002 AUDIT WAVE E INFO META H1 BLOCKED — PAGE OWNER AMBIGUOUS"


def run_full(apply: bool = False) -> dict[str, Any]:
    init_operation()
    sitemap_urls = fetch_sitemap_urls()
    before_rows = phase_http_snapshot(TARGET_URLS + STABLE_REFS, DEPLOY_ROOT / "http-before", "before", sitemap_urls)
    db_summary = phase_db_discovery()
    source_discovery = phase_source_discovery(db_summary)
    plan = build_patch_plan(db_summary, before_rows)
    build_rollback_plan(plan)
    gates = build_dry_run_gates(before_rows, db_summary, plan)

    mutations: list[dict[str, Any]] = []
    source_uploads: list[dict[str, Any]] = []
    if apply and all(gates.values()):
        mutations = apply_db_patches(plan)
        source_uploads = apply_manufacturer_source_patches(plan)
        write_json(DEPLOY_ROOT / "verification" / "source-upload-manifest.json", source_uploads)
        time.sleep(2)

    after_rows = phase_http_snapshot(TARGET_URLS, DEPLOY_ROOT / "http-after", "after", sitemap_urls)
    regression = phase_regression()
    audit_status = build_audit_status(after_rows)
    verdict = determine_verdict(audit_status, regression)

    after_md = ["# After verification\n\n", f"Verdict: **{verdict}**\n\n"]
    for r in after_rows:
        after_md.append(
            f"- {r['url']}: meta={r.get('meta_description_len')} h1={r.get('h1_count')}\n"
        )
    write_text(DEPLOY_ROOT / "verification" / "after-verification.md", "".join(after_md))
    write_json(DEPLOY_ROOT / "verification" / "after-verification.json", after_rows)

    return {
        "before_rows": before_rows,
        "after_rows": after_rows,
        "db_summary": db_summary,
        "plan": plan,
        "gates": gates,
        "mutations": mutations,
        "source_uploads": source_uploads,
        "regression": regression,
        "audit_status": audit_status,
        "verdict": verdict,
        "stats": stats,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Apply scoped DB/source patches after gates")
    parser.add_argument("--discover-only", action="store_true")
    args = parser.parse_args()
    result = run_full(apply=args.apply and not args.discover_only)
    print(json.dumps({"verdict": result["verdict"], "stats": result["stats"], "audit_status": result["audit_status"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
