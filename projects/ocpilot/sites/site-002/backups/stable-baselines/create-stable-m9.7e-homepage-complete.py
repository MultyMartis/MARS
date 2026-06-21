#!/usr/bin/env python3
"""SITE-002 — Stable checkpoint M9.7E homepage complete (read-only)."""
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
from html import unescape
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
BACKUP_NAME = "SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE"
BACKUP_DIR = SITE_ROOT / "backups" / "stable-baselines" / BACKUP_NAME
FILES_DIR = BACKUP_DIR / "files"
IMAGES_DIR = BACKUP_DIR / "images" / "category-image"
DB_DIR = BACKUP_DIR / "database"
QA_OUT = BACKUP_DIR / "qa-snapshot.json"
DATA_SNAPSHOT_OUT = BACKUP_DIR / "data-snapshot.json"

REMOTE_FILES = [
    ("system/library/zpm/category_visibility.php", ["M7.1", "M9.5", "M9.7C", "M9.7E"]),
    ("catalog/controller/product/katalog.php", ["M7.1", "M9.7C"]),
    ("catalog/controller/product/category.php", ["M7.1", "M9", "M9.5"]),
    ("catalog/controller/common/header.php", ["M7.1", "M9.7C"]),
    ("catalog/controller/common/footer.php", ["M7.1"]),
    ("catalog/controller/common/home.php", ["M7.1", "M9.7E"]),
    ("catalog/view/theme/default/template/common/megamenu.twig", ["M7.1", "M9.7D-manual"]),
    ("catalog/view/theme/default/template/common/footer.twig", ["M7.1"]),
    ("catalog/view/theme/default/template/sections/catalogsections.twig", ["M7.1"]),
    ("catalog/view/theme/default/template/sections/offcanvasmenu.twig", ["M7.1", "M9.7D-manual"]),
    ("catalog/view/theme/default/template/product/category.twig", ["M9.5", "M9.7D-manual"]),
    ("catalog/view/theme/default/template/sections/filterssidebar.twig", ["M9"]),
    ("system/library/zpm/attribute_filter_visibility.php", ["M8.3-W2"]),
    ("catalog/model/catalog/product.php", ["M8.3-W2", "M9"]),
    ("system/library/zpm/filter_profile_resolver.php", ["M9"]),
    ("system/library/zpm/filter_profiles/global_hidden.php", ["M9"]),
    ("system/library/zpm/filter_profiles/301_stoly.php", ["M9-Phase1"]),
    ("system/library/zpm/filter_profiles/80_moechnye_vanny.php", ["M9-Phase2"]),
    ("system/library/zpm/filter_profiles/322_podtovarniki.php", ["M9-Phase3"]),
    ("system/library/zpm/filter_profiles/207_zonty.php", ["M9-Phase3"]),
    ("system/library/zpm/filter_profiles/326_telezhki.php", ["M9-Phase3"]),
    ("catalog/view/theme/default/stylesheet/stylesheet.css", ["M9.7D-manual"]),
    ("catalog/view/theme/default/stylesheet/zpm.css", ["M9.7D-manual"]),
    ("catalog/view/theme/default/stylesheet/zpm-catalog.css", ["M9.7D-manual"]),
    ("assets/css/style.css", ["M9.7D-manual"]),
    ("assets/css/style.min.css", ["M9.7D-manual"]),
    ("assets/css/sd.css", ["M9.7D-manual"]),
]

REMOTE_CATEGORY_IMAGES = [
    "image/catalog/Category-image/stoly.webp",
    "image/catalog/Category-image/moechnye-vanny.webp",
    "image/catalog/Category-image/podtovarniki-i-podstavki.webp",
    "image/catalog/Category-image/zonty-vytyazhnye.webp",
    "image/catalog/Category-image/telezhki-servirovochnye.webp",
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
    ("home", "/", "Home"),
    ("katalog", "/katalog", "Catalog hub"),
    ("neutral_hub", "/katalog/nejtralnoe-oborudovanie", "Neutral root hub"),
    ("stoly", "/katalog/nejtralnoe-oborudovanie/stoly/", "Столы branch PLP"),
    ("vanny", "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/", "Моечные ванны branch PLP"),
    ("podtovarniki", "/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/", "Подтоварники branch PLP"),
    ("zonty", "/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/", "Зонты branch PLP"),
    ("telezhki", "/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/", "Тележки branch PLP"),
    (
        "reference_table_pdp",
        "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850",
        "Reference table PDP",
    ),
    (
        "reference_sink_pdp",
        "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-celnotyanutye-premium-3/vanna-moechnaya-vmc-p3-2-500-1150h700h850",
        "Reference sink PDP",
    ),
]

EXPECTED_MEGAMENU = {
    "Столы",
    "Моечные ванны",
    "Подтоварники и подставки",
    "Зонты вытяжные",
    "Тележки сервировочные",
}
EXPECTED_HOME = EXPECTED_MEGAMENU
EXPECTED_HOME_ORDER = [
    "Столы",
    "Моечные ванны",
    "Подтоварники и подставки",
    "Зонты вытяжные",
    "Тележки сервировочные",
]
FORBIDDEN_HOME = {"Нейтральное оборудование"} | {
    "Стеллажи", "Полки", "Подтоварники", "Тележки", "Шкафы", "Лари", "Столы производственные",
}
FORBIDDEN_MEGAMENU = FORBIDDEN_HOME - {"Нейтральное оборудование"}

TABLE_PRIMARY = [
    "Цена (₽)", "Только в наличии", "Длина (мм)", "Ширина (мм)", "Высота (мм)",
    "Материал столешницы", "Конструкция полки", "Тип опоры", "Макс. нагрузка", "Наличие борта",
]
SINK_PRIMARY = [
    "Цена (₽)", "Только в наличии", "Длина (мм)", "Ширина (мм)", "Высота (мм)",
    "Размер раковины", "Мойка", "Наличие борта",
]
GLOBAL_HIDDEN = [
    "Длина в упаковке", "Дополнительные сведения", "Комплект поставки",
    "Габариты нетто", "Стандарт",
]
CROSS_FAMILY = ["Мойка", "Отверстие под смеситель", "Размер раковины"]
TEST_MARKERS = ["шир ТЕСТ", "выс ТЕСТ", "дл ТЕСТ", "марка стали ТЕСТ"]
PACKAGING_MARKERS = ["Длина в упаковке", "Ширина в упаковке", "Упаковка (Длина"]
SERVICE_MARKERS = ["Дополнительные сведения", "Комплект поставки"]
HIDDEN_ROOT_SLUGS = [
    "teplovoe-oborudovanie", "holodilnoe-oborudovanie", "inventar",
    "elektromehanicheskoe-oborudovanie", "barnoe-oborudovanie",
]
PHP_ERROR_MARKERS = ["Fatal error", "Parse error", "Warning:", "Notice:", "Uncaught"]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "SITE-002-Stable-M9.7E/1.0", "Accept": "text/html"},
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=90) as resp:
            body = resp.read().decode("utf-8", "replace")
            return {"url": url, "status": resp.status, "final_url": resp.geturl(), "body": body, "error": None}
    except Exception as e:
        return {"url": url, "status": None, "final_url": url, "body": "", "error": str(e)}


def extract_filter_sidebar(body: str) -> str:
    m = re.search(r'<div class="flt"[^>]*data-filters[^>]*>(.*?)</form>\s*</div>', body, re.S)
    return m.group(1) if m else ""


def hits_in_sidebar(body: str, markers: list) -> list:
    scope = extract_filter_sidebar(body)
    return [m for m in markers if m in scope]


def megamenu_roots(html: str) -> list:
    return re.findall(r'data-cat-btn[^>]*data-cat="([^"]+)"', html)


def neutral_megamenu(html: str) -> list:
    m = re.search(
        r'data-cat-pane="Нейтральное оборудование".*?zpm-catalog__grid(.*?)zpm-catalog__last-block',
        html,
        re.S,
    )
    if not m:
        return []
    block = m.group(1)
    items = []
    for tile in re.findall(r'<a class="zpm-catalog__tile".*?</a>', block, re.S):
        title_m = re.search(r'zpm-catalog__tile-title">([^<]+)</span>', tile)
        count_m = re.search(r'<span>(\d+) шт\.</span>', tile)
        img_m = re.search(r'<img[^>]+src="([^"]+)"', tile)
        if title_m:
            items.append(
                {
                    "name": title_m.group(1).strip(),
                    "count": int(count_m.group(1)) if count_m else None,
                    "img": img_m.group(1) if img_m else None,
                }
            )
    return items


def homepage_cat_cards(html: str) -> list:
    m = re.search(r'<section class="zpm-cat-sections"[^>]*>.*?</section>', html, re.S)
    block = m.group(0) if m else ""
    cards = []
    for card in re.findall(r'<a class="zpm-cat-card".*?</a>', block, re.S):
        title_m = re.search(r'zpm-cat-card__title">([^<]+)</div>', card)
        img_m = re.search(r'<img[^>]+src="([^"]+)"', card)
        href_m = re.search(r'href="([^"]+)"', card)
        if title_m:
            cards.append(
                {
                    "name": title_m.group(1).strip(),
                    "img": img_m.group(1) if img_m else None,
                    "href": href_m.group(1) if href_m else None,
                }
            )
    return cards


def hub_cards(html: str) -> list:
    cards = []
    for card in re.findall(r'<a class="zpm-cat-card".*?</a>', html, re.S):
        title_m = re.search(r'zpm-cat-card__title">([^<]+)</div>', card)
        img_m = re.search(r'<img[^>]+src="([^"]+)"', card)
        href_m = re.search(r'href="([^"]+)"', card)
        if title_m:
            cards.append(
                {
                    "name": title_m.group(1).strip(),
                    "img": img_m.group(1) if img_m else None,
                    "href": href_m.group(1) if href_m else None,
                }
            )
    return cards


def footer_catalog_links(html: str) -> list:
    m = re.search(r"zpm-footer__col--catalog.*?</div>\s*</div>", html, re.S)
    block = m.group(0) if m else html
    return re.findall(r'class="zpm-footer__link"[^>]*href="([^"]+)"', block)


def run_qa() -> dict:
    pages = {}
    for name, path, _ in QA_URLS:
        pages[name] = fetch(BASE_URL + path)

    checks = []
    summary = {"pass": 0, "fail": 0, "warn": 0}

    def add(cid, status, detail, evidence=None):
        checks.append({"id": cid, "status": status, "detail": detail, "evidence": evidence or {}})
        summary[status] = summary.get(status, 0) + 1

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

    home = pages["home"]
    roots = megamenu_roots(home["body"])
    if len(roots) == 1 and "Нейтраль" in roots[0]:
        add("QA-MEGAMENU-ROOT", "pass", "Megamenu single neutral root", {"roots": roots})
    else:
        add("QA-MEGAMENU-ROOT", "fail", f"Megamenu roots={roots}", {"roots": roots})

    mm = neutral_megamenu(home["body"])
    mm_names = {x["name"] for x in mm}
    zero_counts = [x["name"] for x in mm if x.get("count") == 0]
    placeholders = [x["name"] for x in mm if x.get("img") and "placeholder" in x["img"]]
    forbidden_present = sorted(mm_names & FORBIDDEN_MEGAMENU)
    missing_expected = sorted(EXPECTED_MEGAMENU - mm_names)

    add(
        "QA-MM-COUNT",
        "pass" if len(mm) == 5 else "fail",
        f"megamenu neutral tiles={len(mm)} names={[x['name'] for x in mm]}",
        {"megamenu": mm},
    )
    add("QA-MM-NO-ZERO", "pass" if not zero_counts else "fail", f"zero-count tiles: {zero_counts}")
    add("QA-MM-NO-FORBIDDEN", "pass" if not forbidden_present else "fail", f"forbidden: {forbidden_present}")
    add(
        "QA-MM-EXPECTED",
        "pass" if not missing_expected and mm_names == EXPECTED_MEGAMENU else "fail",
        f"missing={missing_expected}",
    )
    add("QA-MM-NO-PLACEHOLDER", "pass" if not placeholders else "fail", f"placeholder imgs: {placeholders}")

    home_cards = homepage_cat_cards(home["body"])
    home_names = [c["name"] for c in home_cards]
    home_set = set(home_names)
    home_placeholders = [c["name"] for c in home_cards if c.get("img") and "placeholder" in c["img"]]
    home_forbidden = sorted(home_set & FORBIDDEN_HOME)
    home_missing = sorted(EXPECTED_HOME - home_set)

    add(
        "QA-HOME-CARD-COUNT",
        "pass" if len(home_cards) == 5 else "fail",
        f"homepage cards={len(home_cards)} names={home_names}",
        {"homepage_cards": home_cards},
    )
    add(
        "QA-HOME-EXPECTED",
        "pass" if not home_missing and home_set == EXPECTED_HOME else "fail",
        f"missing={home_missing}",
    )
    add(
        "QA-HOME-ORDER",
        "pass" if home_names == EXPECTED_HOME_ORDER else "fail",
        f"order={home_names}",
    )
    add("QA-HOME-NO-ROOT", "pass" if "Нейтральное оборудование" not in home_set else "fail", "no root card")
    add("QA-HOME-NO-FORBIDDEN", "pass" if not home_forbidden else "fail", f"forbidden={home_forbidden}")
    add("QA-HOME-NO-PLACEHOLDER", "pass" if not home_placeholders else "fail", f"placeholder={home_placeholders}")

    footer = footer_catalog_links(home["body"])
    bad_footer = [h for h in footer if any(s in h for s in HIDDEN_ROOT_SLUGS)]
    if footer and not bad_footer:
        add("QA-FOOTER", "pass", "Footer catalog links show only neutral paths", {"links": footer})
    else:
        add("QA-FOOTER", "fail" if bad_footer else "warn", f"Footer issue bad={bad_footer}", {"links": footer})

    hub = pages["neutral_hub"]
    hub_body = hub["body"]
    cards = hub_cards(hub_body)
    hub_placeholders = [c["name"] for c in cards if c.get("img") and "placeholder" in c["img"]]
    hub_ok = (
        hub["status"] == 200
        and "category--hub" in hub_body
        and not re.search(r"category--hub[\s\S]*?data-filter-sidebar", hub_body)
        and not re.search(r"category--hub[\s\S]*?data-filter-open", hub_body)
    )
    add(
        "QA-HUB-MODE",
        "pass" if hub_ok and len(cards) == 5 else "fail",
        f"hub_mode={hub_ok} hub_cards={len(cards)} (expected 5)",
        {"hub_cards": cards},
    )
    add("QA-HUB-NO-PLACEHOLDER", "pass" if not hub_placeholders else "fail", f"hub placeholder imgs: {hub_placeholders}")

    home_hub_match = (
        len(home_cards) == len(cards)
        and [c["name"] for c in home_cards] == [c["name"] for c in cards]
    )
    add(
        "QA-HOME-HUB-PARITY",
        "pass" if home_hub_match else "fail",
        f"homepage vs hub parity={home_hub_match}",
    )

    stoly = pages["stoly"]
    stoly_sidebar = extract_filter_sidebar(stoly["body"])
    stoly_primary = hits_in_sidebar(stoly["body"], TABLE_PRIMARY)
    stoly_bad = hits_in_sidebar(stoly["body"], TEST_MARKERS + PACKAGING_MARKERS + SERVICE_MARKERS + CROSS_FAMILY)
    add(
        "QA-FILTER-STOLY",
        "pass" if len(stoly_primary) >= 8 and "Мойка" not in stoly_sidebar and not stoly_bad else "fail",
        f"primary={len(stoly_primary)}/10 bad={stoly_bad}",
    )

    vanny = pages["vanny"]
    vanny_primary = hits_in_sidebar(vanny["body"], SINK_PRIMARY)
    vanny_bad = hits_in_sidebar(vanny["body"], ["Конструкция полки", "Макс. нагрузка"] + GLOBAL_HIDDEN)
    add(
        "QA-FILTER-VANNY",
        "pass" if len(vanny_primary) >= 7 and not vanny_bad else "fail",
        f"primary={len(vanny_primary)}/8 bad={vanny_bad}",
    )

    for branch_name in ("podtovarniki", "zonty", "telezhki"):
        branch = pages[branch_name]
        has_grid = "category__grid" in branch["body"] or "p-card" in branch["body"]
        has_filter = "data-filter-sidebar" in branch["body"]
        hidden_global = hits_in_sidebar(branch["body"], GLOBAL_HIDDEN)
        add(
            f"QA-BRANCH-{branch_name}",
            "pass" if branch["status"] == 200 and has_grid and has_filter and not hidden_global else "fail",
            f"grid={has_grid} filter={has_filter} hidden_global={hidden_global}",
        )

    for pdp_name in ("reference_table_pdp", "reference_sink_pdp"):
        pdp = pages[pdp_name]
        add(
            f"QA-PDP-{pdp_name}",
            "pass" if pdp["status"] == 200 and not pdp["error"] else "fail",
            f"status={pdp['status']} err={pdp['error']}",
        )

    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "test_url": BASE_URL,
        "checkpoint": BACKUP_NAME,
        "baseline_note": "LIVE TEST STATE M9.7E — homepage 5 neutral branches + M9.7D manual UI",
        "checks": checks,
        "summary": summary,
        "homepage_cards": home_cards,
        "megamenu_after": mm,
        "hub_cards": cards,
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


def capture_files() -> tuple:
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    entries = []
    missing = []
    for remote, milestones in REMOTE_FILES:
        try:
            data = ftp_download(remote)
        except Exception as e:
            missing.append({"remote_path": remote, "error": str(e)})
            print(f"  MISSING {remote}: {e}")
            continue
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
                "milestones": milestones,
            }
        )
        print(f"  captured {remote} ({len(data)} bytes)")
    return entries, missing


def capture_category_images() -> list:
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    entries = []
    for remote in REMOTE_CATEGORY_IMAGES:
        data = ftp_download(remote)
        name = Path(remote).name
        local = IMAGES_DIR / name
        local.write_bytes(data)
        entries.append(
            {
                "remote_path": remote,
                "local_path": str(local.relative_to(BACKUP_DIR)).replace("\\", "/"),
                "size_bytes": len(data),
                "sha256": sha256_bytes(data),
            }
        )
        print(f"  captured image {remote} ({len(data)} bytes)")
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


def pma_sql(op, csrf, sql: str) -> list:
    html = op.open(
        urllib.request.Request(
            PMA + "/sql.php",
            data=urllib.parse.urlencode(
                {"db": DB, "sql_query": sql, "token": csrf, "sql_delimiter": ";"}
            ).encode(),
            method="POST",
        ),
        timeout=240,
    ).read().decode("utf-8", "replace")
    rows = []
    for tbl in re.findall(r'<table[^>]*class="[^"]*table[^"]*"[^>]*>(.*?)</table>', html, re.S):
        if "Browse" in tbl and "Drop" in tbl:
            continue
        parsed = []
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", tbl, re.S):
            cells = [
                unescape(re.sub(r"<[^>]+>", " ", c).strip())
                for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)
            ]
            cells = [re.sub(r"\s+", " ", c) for c in cells if c.strip()]
            if cells:
                parsed.append(cells)
        if len(parsed) >= 2 and not parsed[0][0].startswith("Table navigation"):
            rows = parsed
            break
    if len(rows) < 2:
        if "MySQL returned an empty result set" in html:
            return []
        m = re.search(r"<td[^>]*>\s*(\d+(?:\.\d+)?)\s*</td>", html)
        if m:
            return [{"cnt": m.group(1)}]
        return []
    h = [x.lower() for x in rows[0]]
    return [dict(zip(h, r)) for r in rows[1:] if len(r) == len(h)]


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
        payload = []
        for k, v in data.items():
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


def export_table_json(op, csrf, table: str) -> dict:
    count_rows = pma_sql(op, csrf, f"SELECT COUNT(*) AS cnt FROM `{table}`")
    total = int(count_rows[0]["cnt"]) if count_rows else 0
    all_rows = []
    batch = 500
    for offset in range(0, total, batch):
        chunk = pma_sql(op, csrf, f"SELECT * FROM `{table}` LIMIT {batch} OFFSET {offset}")
        all_rows.extend(chunk)
    payload = {
        "table": table,
        "exported_at_utc": datetime.now(timezone.utc).isoformat(),
        "row_count": len(all_rows),
        "expected_count": total,
        "rows": all_rows,
    }
    out = DB_DIR / f"{table}.json"
    out.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    return {
        "filename": f"{table}.json",
        "path": str(out.relative_to(BACKUP_DIR)).replace("\\", "/"),
        "size_bytes": out.stat().st_size,
        "sha256": sha256_bytes(out.read_bytes()),
        "row_count": len(all_rows),
        "expected_count": total,
    }


def capture_data_snapshot(op, csrf) -> dict:
    active_skus = pma_sql(op, csrf, "SELECT COUNT(*) AS cnt FROM oc_product WHERE status = 1")
    inactive_skus = pma_sql(op, csrf, "SELECT COUNT(*) AS cnt FROM oc_product WHERE status = 0")
    branch_images = pma_sql(
        op,
        csrf,
        """
        SELECT c.category_id, cd.name, c.image, c.status
        FROM oc_category c
        JOIN oc_category_description cd ON cd.category_id = c.category_id AND cd.language_id = 1
        WHERE c.category_id IN (79,301,80,322,207,326)
        ORDER BY c.category_id
        """,
    )
    profile_categories = [
        {"category_id": 79, "name": "Нейтральное оборудование", "mode": "hub", "profile": None},
        {"category_id": 301, "name": "Столы", "mode": "branch", "profile": "301_stoly"},
        {"category_id": 80, "name": "Моечные ванны", "mode": "branch", "profile": "80_moechnye_vanny"},
        {"category_id": 322, "name": "Подтоварники и подставки", "mode": "branch", "profile": "322_podtovarniki"},
        {"category_id": 207, "name": "Зонты вытяжные", "mode": "branch", "profile": "207_zonty"},
        {"category_id": 326, "name": "Тележки сервировочные", "mode": "branch", "profile": "326_telezhki"},
    ]
    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "environment": "TEST",
        "active_sku_count": int(active_skus[0]["cnt"]) if active_skus else None,
        "inactive_sku_count": int(inactive_skus[0]["cnt"]) if inactive_skus else None,
        "total_sku_count": (
            int(active_skus[0]["cnt"]) + int(inactive_skus[0]["cnt"])
            if active_skus and inactive_skus
            else None
        ),
        "branch_category_images": branch_images,
        "profile_categories": profile_categories,
        "milestones": [
            "M7.1 Launch Mode",
            "M8.3 Wave 1+2",
            "M9 Phase 1-3",
            "M9.5 Root Hub",
            "M9.7B Category Images",
            "M9.7C Megamenu empty-category fix",
            "M9.7D Operator manual UI refinement",
            "M9.7E Homepage neutral branch cards",
        ],
    }


def capture_db(op, csrf) -> tuple:
    DB_DIR.mkdir(parents=True, exist_ok=True)
    dumps = []
    json_exports = []
    errors = []
    try:
        scoped = pma_export(
            op,
            csrf,
            "table",
            tables=SCOPED_TABLES,
            filename="scoped-m7-m9-tables.sql",
        )
        dumps.append(scoped)
        print(f"  scoped SQL dump: {scoped['size_bytes']} bytes")
    except Exception as e:
        errors.append(f"scoped sql dump: {e}")
        print(f"  scoped SQL dump failed: {e}")

    for table in SCOPED_TABLES:
        try:
            j = export_table_json(op, csrf, table)
            json_exports.append(j)
            print(f"  JSON {table}: {j['row_count']} rows ({j['size_bytes']} bytes)")
        except Exception as e:
            errors.append(f"json {table}: {e}")
            print(f"  JSON {table} failed: {e}")

    return dumps, json_exports, errors


def build_manifest(qa, files, images, missing_files, db_dumps, json_exports, db_errors, data_snapshot) -> dict:
    manifest = {
        "checkpoint_name": BACKUP_NAME,
        "site_id": "SITE-002",
        "environment": "TEST",
        "test_url": BASE_URL,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "stable_state": "M7.1 + M8.3 + M9 + M9.5 + M9.7B/C/D/E on TEST — homepage complete",
        "supersedes": "SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI",
        "visual_baseline_note": "LIVE TEST STATE M9.7E — homepage 5 neutral branches aligned with hub/megamenu",
        "next_planned_stage": "M10 (not authorized — checkpoint only)",
        "mode": "read-only-backup",
        "qa_summary": qa["summary"],
        "data_snapshot_summary": {
            "active_sku_count": data_snapshot.get("active_sku_count"),
            "branch_category_images": data_snapshot.get("branch_category_images"),
            "profile_categories": [p["category_id"] for p in data_snapshot.get("profile_categories", [])],
        },
        "files": files,
        "missing_files": missing_files,
        "category_images": images,
        "database_dumps": db_dumps,
        "database_json_exports": json_exports,
        "database_errors": db_errors,
        "deploy_manifests_reference": [
            "m7.1-launch-mode-work/backups/m7.1-launch-mode-deploy-20260614-173622.json",
            "m8.3-wave1-cleanup-work/m8.3-wave1-cleanup-result-20260614-182952.json",
            "m8.3-wave2-cleanup-work/backups/m8.3-wave2-deploy-20260614-184547.json",
            "m9-phase1-tables-work/backups/m9-phase1-deploy-20260614-193725.json",
            "m9-phase2-sinks-work/backups/m9-phase2-deploy-20260614-195231.json",
            "m9-phase3-remaining-work/backups/m9-phase3-deploy-20260614-200051.json",
            "m9.5-root-hub-work/backups/m9.5-root-hub-deploy-20260614-203141.json",
            "m9.7c-image-megamenu-work/backups/m9.7c-deploy-20260614-215218.json",
            "m9.7e-homepage-neutral-branches-work/backups/m9.7e-deploy-20260614-224916.json",
        ],
        "rollback_instruction": {
            "files": "Upload each file from files/ to matching remote path on FTP. Clear system/storage/cache/template/ and cache.category.attributes.*",
            "images": "Upload images/category-image/*.webp to image/catalog/Category-image/ on TEST",
            "database_scoped": "Import scoped-m7-m9-tables.sql — TEST only",
            "prior_checkpoint": "SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI for pre-M9.7E rollback (homepage 1 root card)",
            "verify": "Re-run qa-snapshot.json checks",
        },
        "backup_dir": str(BACKUP_DIR),
    }
    manifest_path = BACKUP_DIR / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def main():
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    print("=== PRE-FLIGHT + QA ===")
    qa = run_qa()
    QA_OUT.write_text(json.dumps(qa, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"QA summary: {qa['summary']}")

    print("=== FTP file capture ===")
    files, missing_files = capture_files()

    print("=== Category images ===")
    images = capture_category_images()

    print("=== DB export + data snapshot ===")
    op, csrf = pma_session()
    data_snapshot = capture_data_snapshot(op, csrf)
    DATA_SNAPSHOT_OUT.write_text(json.dumps(data_snapshot, ensure_ascii=False, indent=2), encoding="utf-8")
    db_dumps, json_exports, db_errors = capture_db(op, csrf)

    print("=== Manifest ===")
    manifest = build_manifest(qa, files, images, missing_files, db_dumps, json_exports, db_errors, data_snapshot)
    print(f"Manifest: {BACKUP_DIR / 'manifest.json'}")
    print(f"Backup folder: {BACKUP_DIR}")
    return manifest


if __name__ == "__main__":
    main()
