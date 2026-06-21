#!/usr/bin/env python3
"""SITE-002 — Stable backup/checkpoint before M9 (read-only)."""
import ftplib
import hashlib
import io
import json
import re
import ssl
import urllib.parse
import urllib.request
import http.cookiejar
from datetime import datetime, timezone
from pathlib import Path

BASE_URL = "https://zpm.new-site.space"
HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DB_USER = "polygonws_zpm"
DB_PASS = "VBCDry2bJ5P"

SITE_ROOT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
STAMP = datetime.now().strftime("%Y%m%d-%H%M")
BACKUP_NAME = f"SITE-002-STABLE-M8.3-BEFORE-M9-{STAMP}"
BACKUP_DIR = SITE_ROOT / "backups" / "stable-baselines" / BACKUP_NAME
FILES_DIR = BACKUP_DIR / "files"
DB_DIR = BACKUP_DIR / "database"
QA_OUT = BACKUP_DIR / "qa-before-backup.json"

REMOTE_FILES = [
    "system/library/zpm/category_visibility.php",
    "catalog/controller/product/katalog.php",
    "catalog/controller/product/category.php",
    "catalog/controller/common/header.php",
    "catalog/controller/common/footer.php",
    "catalog/controller/common/home.php",
    "catalog/view/theme/default/template/common/megamenu.twig",
    "catalog/view/theme/default/template/common/footer.twig",
    "catalog/view/theme/default/template/sections/catalogsections.twig",
    "catalog/view/theme/default/template/sections/offcanvasmenu.twig",
    "system/library/zpm/attribute_filter_visibility.php",
    "catalog/model/catalog/product.php",
]

SCOPED_TABLES = [
    "oc_product",
    "oc_product_attribute",
    "oc_attribute",
    "oc_attribute_description",
    "oc_category",
    "oc_category_description",
]

QA_URLS = [
    ("home", "/"),
    ("katalog", "/katalog"),
    ("neutral_hub", "/katalog/nejtralnoe-oborudovanie"),
    ("stoly", "/katalog/nejtralnoe-oborudovanie/stoly/"),
    ("vanny", "/katalog/nejtralnoe-oborudovanie/vanny-moechnye/"),
    (
        "reference_pdp",
        "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850",
    ),
]

PHP_ERROR_MARKERS = [
    "Fatal error",
    "Parse error",
    "Warning:",
    "Notice:",
    "Uncaught",
]

TEST_MARKERS = [
    "ТЕСТ",
    "шир ТЕСТ",
    "выс ТЕСТ",
    "дл ТЕСТ",
    "марка стали ТЕСТ",
    "толщина столешницы ТЕСТ",
    "толщина материала ног ТЕСТ",
]

PACKAGING_MARKERS = [
    "Длина в упаковке",
    "Ширина в упаковке",
    "Высота в упаковке",
    "Упаковка (Длина",
    "Упаковка (Ширина",
    "Упаковка (Высота",
    "Упаковка (Объем",
    "Вес (нетто, кг)",
]

SERVICE_MARKERS = [
    "Дополнительные сведения",
    "Комплект поставки",
    "Комплект отгрузки",
]

HIDDEN_ROOT_SLUGS = [
    "teplovoe-oborudovanie",
    "holodilnoe-oborudovanie",
    "inventar",
    "elektromehanicheskoe-oborudovanie",
    "barnoe-oborudovanie",
    "hlebopekarnoe-oborudovanie",
    "posudomoechnye-mashiny",
    "ventilyacionnoe-oborudovanie",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def fetch(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "SITE-002-Stable-M83-Backup/1.0", "Accept": "text/html"},
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=90) as resp:
            body = resp.read().decode("utf-8", "replace")
            return {
                "url": url,
                "status": resp.status,
                "final_url": resp.geturl(),
                "body": body,
                "error": None,
            }
    except Exception as e:
        return {"url": url, "status": None, "final_url": url, "body": "", "error": str(e)}


def megamenu_roots(html: str) -> list:
    return re.findall(r'data-cat-btn[^>]*data-cat="([^"]+)"', html)


def footer_catalog_links(html: str) -> list:
    m = re.search(r"zpm-footer__col--catalog.*?</div>\s*</div>", html, re.S)
    block = m.group(0) if m else html
    return re.findall(r'class="zpm-footer__link"[^>]*href="([^"]+)"', block)


def filter_sidebar_block(html: str) -> str:
    m = re.search(r'class="[^"]*filter[^"]*".*?(?=</aside>|</section>|</main>)', html, re.S | re.I)
    if m:
        return m.group(0)
    m = re.search(r'id="[^"]*filter[^"]*".*?(?=</aside>|</section>|</main>)', html, re.S | re.I)
    return m.group(0) if m else html


def run_qa() -> dict:
    pages = {}
    for name, path in QA_URLS:
        pages[name] = fetch(BASE_URL + path)

    checks = []
    summary = {"pass": 0, "fail": 0, "warn": 0}

    def add(cid, status, detail, evidence=None):
        checks.append({"id": cid, "status": status, "detail": detail, "evidence": evidence or {}})
        summary[status] = summary.get(status, 0) + 1

    home = pages["home"]
    php_hits = [m for m in PHP_ERROR_MARKERS if m in home["body"]]
    if home["error"]:
        add("QA-PHP", "fail", f"Home fetch error: {home['error']}")
    elif php_hits:
        add("QA-PHP", "fail", f"PHP markers on home: {php_hits}")
    else:
        add("QA-PHP", "pass", "No PHP error markers on home")

    for name, page in pages.items():
        hits = [m for m in PHP_ERROR_MARKERS if m in page["body"]]
        if page["error"]:
            add(f"QA-HTTP-{name}", "fail", f"{name}: {page['error']}")
        elif hits:
            add(f"QA-HTTP-{name}", "fail", f"{name}: PHP markers {hits}")
        elif page["status"] == 200:
            add(f"QA-HTTP-{name}", "pass", f"{name}: HTTP 200")
        else:
            add(f"QA-HTTP-{name}", "fail", f"{name}: status={page['status']}")

    roots = megamenu_roots(home["body"])
    if len(roots) == 1 and "Нейтраль" in roots[0]:
        add("QA-MEGAMENU", "pass", "Megamenu single neutral root", {"roots": roots})
    else:
        add("QA-MEGAMENU", "fail", f"Megamenu roots={roots}", {"roots": roots})

    footer = footer_catalog_links(home["body"])
    bad_footer = [h for h in footer if any(s in h for s in HIDDEN_ROOT_SLUGS)]
    if footer and not bad_footer:
        add("QA-FOOTER", "pass", "Footer catalog links show only neutral paths", {"links": footer})
    else:
        add(
            "QA-FOOTER",
            "fail" if bad_footer else "warn",
            f"Footer links issue bad={bad_footer}",
            {"links": footer},
        )

    plp = pages["stoly"]
    sidebar = filter_sidebar_block(plp["body"])
    test_hits = [m for m in TEST_MARKERS if m in sidebar]
    pack_hits = [m for m in PACKAGING_MARKERS if m in sidebar]
    svc_hits = [m for m in SERVICE_MARKERS if m in sidebar]
    if not test_hits and not pack_hits and not svc_hits:
        add("QA-FILTER-STOLY", "pass", "Stoly PLP filter clean (no TEST/packaging/service attrs)")
    else:
        add(
            "QA-FILTER-STOLY",
            "fail",
            f"Stoly filter hits test={test_hits} pack={pack_hits} svc={svc_hits}",
        )

    plp2 = pages["vanny"]
    sidebar2 = filter_sidebar_block(plp2["body"])
    test_hits2 = [m for m in TEST_MARKERS if m in sidebar2]
    pack_hits2 = [m for m in PACKAGING_MARKERS if m in sidebar2]
    svc_hits2 = [m for m in SERVICE_MARKERS if m in sidebar2]
    if not test_hits2 and not pack_hits2 and not svc_hits2:
        add("QA-FILTER-VANNY", "pass", "Vanny PLP filter clean")
    else:
        add(
            "QA-FILTER-VANNY",
            "fail",
            f"Vanny filter hits test={test_hits2} pack={pack_hits2} svc={svc_hits2}",
        )

    pdp = pages["reference_pdp"]
    if pdp["status"] == 200 and not pdp["error"]:
        add("QA-PDP", "pass", "Reference PDP opens (HTTP 200)")
    else:
        add("QA-PDP", "fail", f"Reference PDP status={pdp['status']} err={pdp['error']}")

    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "test_url": BASE_URL,
        "checks": checks,
        "summary": summary,
        "pages": {
            k: {
                "url": v["url"],
                "status": v["status"],
                "final_url": v["final_url"],
                "error": v["error"],
                "megamenu_roots": megamenu_roots(v["body"]) if k == "home" else None,
                "footer_catalog_links": footer_catalog_links(v["body"]) if k == "home" else None,
            }
            for k, v in pages.items()
        },
    }


def ftp_connect():
    ftp = ftplib.FTP(HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_download(remote_path: str) -> bytes:
    ftp = ftp_connect()
    bio = io.BytesIO()
    ftp.retrbinary("RETR " + remote_path, bio.write)
    ftp.quit()
    return bio.getvalue()


def capture_files() -> list:
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    entries = []
    for remote in REMOTE_FILES:
        data = ftp_download(remote)
        local = FILES_DIR / remote.replace("/", "\\")
        local.parent.mkdir(parents=True, exist_ok=True)
        local.write_bytes(data)
        entries.append(
            {
                "remote_path": remote,
                "local_path": str(local.relative_to(BACKUP_DIR)).replace("\\", "/"),
                "size_bytes": len(data),
                "sha256": sha256_bytes(data),
                "source": "live-ftp-test",
                "milestones": (
                    ["M7.1"]
                    if remote
                    in REMOTE_FILES[:10]
                    else ["M8.3-Wave2"]
                    if remote in REMOTE_FILES[10:]
                    else []
                ),
            }
        )
        print(f"  captured {remote} ({len(data)} bytes)")
    return entries


def pma_session():
    ctx = ssl.create_default_context()
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cj),
        urllib.request.HTTPSHandler(context=ctx),
    )
    lp = op.open(PMA + "/", timeout=60).read().decode("utf-8", "replace")
    token = re.search(r'name="token"\s+value="([^"]+)"', lp).group(1)
    op.open(
        urllib.request.Request(
            PMA + "/index.php",
            data=urllib.parse.urlencode(
                {
                    "pma_username": DB_USER,
                    "pma_password": DB_PASS,
                    "server": "1",
                    "target": "index.php",
                    "token": token,
                }
            ).encode(),
            method="POST",
        ),
        timeout=60,
    )
    db_html = op.open(PMA + "/db_structure.php?db=" + urllib.parse.quote(DB), timeout=60).read().decode(
        "utf-8", "replace"
    )
    csrf = re.search(r'name="token"\s+value="([^"]+)"', db_html).group(1)
    return op, csrf


def pma_export(op, csrf, export_type, tables=None, filename="dump.sql"):
    data = {
        "db": DB,
        "token": csrf,
        "export_type": export_type,
        "export_method": "custom" if tables else "quick",
        "quick_or_custom": "custom" if tables else "quick",
        "output_format": "sendit",
        "filename_template": "@DATABASE@",
        "remember_template": "on",
        "charset": "utf-8",
        "compression": "none",
        "maxsize": "",
        "codegen_structure_or_data": "data",
        "codegen_format": "0",
        "csv_separator": ";",
        "csv_enclosed": '"',
        "csv_escaped": '"',
        "csv_terminated": "AUTO",
        "csv_null": "NULL",
        "csv_columns": "something",
        "sql_include_comments": "something",
        "sql_dates": "something",
        "sql_relation": "something",
        "sql_mime": "something",
        "sql_header_comment": "",
        "sql_use_transaction": "something",
        "sql_disable_fk": "something",
        "sql_views_as_tables": "something",
        "sql_metadata": "something",
        "sql_create_database": "something",
        "sql_drop_table": "something",
        "sql_if_not_exists": "something",
        "sql_auto_increment": "something",
        "sql_create_view": "something",
        "sql_procedure_function": "something",
        "sql_truncate": "something",
        "sql_delayed": "something",
        "sql_ignore": "something",
        "sql_type": "INSERT",
        "sql_insert_syntax": "both",
        "sql_max_query_size": "0",
        "sql_hex_for_binary": "something",
        "sql_utc_time": "something",
        "sql_structure_or_data": "structure_and_data",
        "sql_compatibility": "NONE",
    }
    if tables:
        data["export_type"] = "table"
        for t in tables:
            data.setdefault("table_select[]", [])
            if isinstance(data.get("table_select[]"), list):
                pass
        # phpMyAdmin expects repeated keys
        payload = []
        for k, v in data.items():
            if k == "table_select[]":
                continue
            payload.append((k, v))
        for t in tables:
            payload.append(("table_select[]", t))
            payload.append(("table_structure[]", t))
            payload.append(("table_data[]", t))
    else:
        payload = list(data.items())

    req = urllib.request.Request(
        PMA + "/export.php",
        data=urllib.parse.urlencode(payload).encode(),
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    resp = op.open(req, timeout=600)
    content = resp.read()
    ct = resp.headers.get("Content-Type", "")
    if b"error" in content[:500].lower() and b"CREATE TABLE" not in content[:2000]:
        text = content.decode("utf-8", "replace")
        if "CREATE TABLE" not in text and "INSERT INTO" not in text:
            raise RuntimeError(f"Export failed ({export_type}): {text[:500]}")
    out = DB_DIR / filename
    out.write_bytes(content)
    return {
        "filename": filename,
        "path": str(out.relative_to(BACKUP_DIR)).replace("\\", "/"),
        "size_bytes": len(content),
        "sha256": sha256_bytes(content),
        "content_type": ct,
        "export_type": export_type,
        "tables": tables or "full",
    }


def capture_db() -> tuple:
    DB_DIR.mkdir(parents=True, exist_ok=True)
    op, csrf = pma_session()
    dumps = []
    errors = []

    try:
        full = pma_export(op, csrf, "database", tables=None, filename="full-test-database.sql")
        dumps.append(full)
        print(f"  full DB dump: {full['size_bytes']} bytes")
    except Exception as e:
        errors.append(f"full dump: {e}")
        print(f"  full DB dump failed: {e}")

    try:
        scoped = pma_export(
            op,
            csrf,
            "table",
            tables=SCOPED_TABLES,
            filename="scoped-m7-m8-tables.sql",
        )
        dumps.append(scoped)
        print(f"  scoped dump: {scoped['size_bytes']} bytes")
    except Exception as e:
        errors.append(f"scoped dump: {e}")
        print(f"  scoped dump failed: {e}")

    return dumps, errors


def build_manifest(qa: dict, files: list, db_dumps: list, db_errors: list) -> dict:
    manifest = {
        "checkpoint_name": BACKUP_NAME,
        "site_id": "SITE-002",
        "environment": "TEST",
        "test_url": BASE_URL,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "timestamp_local_folder": STAMP,
        "stable_state": "M7.1 + M8.3 Wave 1 + M8.3 Wave 2 deployed on TEST",
        "next_planned_stage": "M9 Filter Profile System implementation",
        "mode": "read-only-backup",
        "qa_summary": qa["summary"],
        "files": files,
        "database_dumps": db_dumps,
        "database_errors": db_errors,
        "rollback_instruction": {
            "files": "Upload each file from files/ to matching remote path on FTP (polygonws.beget.tech, public_html root). Clear system/storage/cache/template/ and attribute cache files cache.category.attributes.*",
            "database_scoped": "Import scoped-m7-m8-tables.sql via phpMyAdmin on TEST only if rolling back M7/M8 data changes",
            "database_full": "Import full-test-database.sql only for full TEST DB rollback — TEST environment only, never production",
            "verify": "Re-run QA URLs and confirm megamenu/footer/filter/PDP checks pass",
        },
        "backup_dir": str(BACKUP_DIR),
    }
    manifest_path = BACKUP_DIR / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def main():
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    print("=== TASK 1: QA ===")
    qa = run_qa()
    QA_OUT.write_text(json.dumps(qa, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"QA summary: {qa['summary']}")

    print("=== TASK 2: FTP file capture ===")
    files = capture_files()

    print("=== TASK 3: DB export ===")
    db_dumps, db_errors = capture_db()

    print("=== TASK 4: Manifest ===")
    manifest = build_manifest(qa, files, db_dumps, db_errors)
    print(f"Manifest: {BACKUP_DIR / 'manifest.json'}")
    print(f"Backup folder: {BACKUP_DIR}")
    return {
        "backup_dir": str(BACKUP_DIR),
        "backup_name": BACKUP_NAME,
        "qa": qa,
        "manifest": manifest,
        "db_errors": db_errors,
    }


if __name__ == "__main__":
    main()
