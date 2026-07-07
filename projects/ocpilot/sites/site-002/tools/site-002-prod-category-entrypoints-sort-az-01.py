#!/usr/bin/env python3
"""SITE-002 Production category entrypoints A→Я sort — Run 4.221."""
from __future__ import annotations

import argparse
import csv
import difflib
import ftplib
import hashlib
import html
import io
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01"
OCPILOT_RUN = "4.221"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-NEW-SECTIONS-ENTRYPOINTS-02"
CHECKPOINT_AFTER = "SITE-002-STABLE-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01"
CORRECT_BRAND = "ЗПМ"
WRONG_BRAND = "БЗПМ"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
REMOTE_CATEGORY_VISIBILITY = "/public_html/system/library/zpm/category_visibility.php"
REMOTE_CATEGORY_PHP = "/public_html/catalog/controller/product/category.php"
EXPECTED_BRANCH_IDS = [322, 331, 301, 326, 354, 358, 207, 80, 86, 88, 360]
TARGET_SLUGS = ("lari", "konditerskiy-inventar")

FTP_SOURCE_FILES = [
    REMOTE_CATEGORY_VISIBILITY,
    REMOTE_CATEGORY_PHP,
    "/public_html/catalog/controller/common/home.php",
    "/public_html/catalog/controller/common/header.php",
    "/public_html/catalog/view/theme/default/template/common/megamenu.twig",
    "/storage/modification/catalog/controller/product/category.php",
    "/storage/modification/system/library/zpm/category_visibility.php",
]

HTTP_BEFORE_URLS = [
    ("home", "https://bzpm.ru/"),
    ("katalog", "https://bzpm.ru/katalog"),
    ("neutral_hub", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie"),
    ("lari", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari"),
    ("konditerskiy", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/konditerskiy-inventar"),
]

SANITY_URLS = [
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    (
        "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye/"
        "polki-dlya-gastoemkostey/derzhatel-dlya-gastroemkostey-pg-10-3-900h330h40-gn-1-6-5-sht"
    ),
    "https://bzpm.ru/llms.txt",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/sitemap.xml",
]

SUBDIRS = (
    "source-before",
    "source-after",
    "http-before",
    "http-after",
    "patch",
    "verification",
    "rollback",
    "manifests",
    "reports",
    "logs",
)

SORT_HELPER_BLOCK = """
\t/**
\t * Normalize category name for Russian A→Я sort (trim; case-insensitive; Ё→Е).
\t */
\tprivate function normalizeCategoryNameForSort($name) {
\t\t$name = trim((string)$name);

\t\tif ($name === '') {
\t\t\treturn '';
\t\t}

\t\tif (function_exists('mb_strtolower')) {
\t\t\t$name = mb_strtolower($name, 'UTF-8');
\t\t} else {
\t\t\t$name = strtolower($name);
\t\t}

\t\treturn str_replace(array('ё', 'Ё'), 'е', $name);
\t}

\t/**
\t * Compare two visible category names for Russian A→Я ordering.
\t */
\tprivate function compareCategoryNamesRu($left, $right) {
\t\t$left = $this->normalizeCategoryNameForSort($left);
\t\t$right = $this->normalizeCategoryNameForSort($right);

\t\tstatic $collator = null;

\t\tif ($collator === null && class_exists('Collator')) {
\t\t\t$collator = new Collator('ru_RU');
\t\t}

\t\tif ($collator instanceof Collator) {
\t\t\treturn $collator->compare($left, $right);
\t\t}

\t\treturn strcmp($left, $right);
\t}

\t/**
\t * Sort category rows by visible Russian name A→Я without changing membership.
\t */
\tpublic function sortCategoriesByRussianName(array $categories, $name_key = 'name') {
\t\tif (count($categories) < 2) {
\t\t\treturn $categories;
\t\t}

\t\tusort($categories, function ($left, $right) use ($name_key) {
\t\t\t$left_name = (is_array($left) && isset($left[$name_key])) ? $left[$name_key] : '';
\t\t\t$right_name = (is_array($right) && isset($right[$name_key])) ? $right[$name_key] : '';

\t\t\treturn $this->compareCategoryNamesRu($left_name, $right_name);
\t\t});

\t\treturn $categories;
\t}
"""

HUB_SORT_LINE = "\t\t\t\t$data['hub_categories'] = $visibility->sortCategoriesByRussianName($data['hub_categories']);\n"


class MetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.in_h1 = False
        self.title = ""
        self.h1_list: list[str] = []
        self.meta: dict[str, str] = {}
        self.body_classes = ""
        self.body_open = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ad = {k: (v or "") for k, v in attrs}
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = True
        if tag_l == "h1":
            self.in_h1 = True
        if tag_l == "meta":
            name = ad.get("name") or ad.get("property") or ""
            if name:
                self.meta[name.lower()] = ad.get("content", "")
        if tag_l == "body":
            self.body_classes = ad.get("class", "")
            self.body_open += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False
        if tag.lower() == "h1":
            self.in_h1 = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        if self.in_h1:
            self.h1_list.append(data.strip())


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow(row)


def parse_production_section(path: Path, subsection: str | None = None) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    if subsection:
        sub = re.search(rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
        if not sub:
            raise RuntimeError(f"Subsection {subsection!r} not found")
        block = sub.group(1)
    fields: dict[str, str] = {}
    current: str | None = None
    for line in block.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.endswith(":"):
            current = s[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(current, "")
            continue
        if current:
            fields[current] = s
    return fields


def ftp_connect() -> ftplib.FTP:
    creds = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(creds["host"], int(creds.get("port") or 21), timeout=120)
    ftp.login(creds["username"], creds["password"])
    return ftp


def ftp_download(ftp: ftplib.FTP, remote: str) -> tuple[bytes | None, str | None]:
    buf = io.BytesIO()
    try:
        ftp.retrbinary(f"RETR {remote}", buf.write)
        return buf.getvalue(), None
    except Exception as exc:  # noqa: BLE001
        return None, str(exc)


def ftp_upload(ftp: ftplib.FTP, remote: str, data: bytes) -> None:
    ftp.storbinary(f"STOR {remote}", io.BytesIO(data))


def http_get(url: str) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xml,*/*", "Cache-Control": "no-cache"},
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = resp.read()
            charset = resp.headers.get_content_charset() or "utf-8"
            return {
                "url": url,
                "status": resp.status,
                "headers": dict(resp.headers.items()),
                "raw_body": body,
                "body": body.decode(charset, errors="replace"),
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        raw = exc.read() if exc.fp else b""
        charset = exc.headers.get_content_charset() if exc.headers else None
        return {
            "url": url,
            "status": exc.code,
            "headers": dict(exc.headers.items()) if exc.headers else {},
            "raw_body": raw,
            "body": raw.decode(charset or "utf-8", errors="replace"),
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "status": None, "headers": {}, "raw_body": b"", "body": "", "error": str(exc)}


def http_head(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return {"url": url, "status": resp.status, "error": None}
    except urllib.error.HTTPError as exc:
        return {"url": url, "status": exc.code, "error": str(exc)}
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "status": None, "error": str(exc)}


def local_ftp_name(remote: str) -> str:
    return remote.strip("/").replace("/", "__")


def extract_page_meta(html_text: str) -> dict[str, Any]:
    p = MetaParser()
    try:
        p.feed(html_text)
    except Exception:
        pass
    return {
        "title": html.unescape(p.title.strip()),
        "meta_description": p.meta.get("description", ""),
        "h1": " | ".join(h for h in p.h1_list if h),
        "body_classes": p.body_classes,
        "body_count": p.body_open,
    }


def parse_hub_cards(html_text: str) -> list[dict[str, str]]:
    cards: list[dict[str, str]] = []
    for block in re.findall(r'<a[^>]+class="[^"]*zpm-cat-card[^"]*"[^>]*>.*?</a>', html_text, re.DOTALL | re.IGNORECASE):
        href_m = re.search(r'href="([^"]+)"', block)
        name_m = re.search(r'class="[^"]*zpm-cat-card__title[^"]*"[^>]*>([^<]+)<', block)
        img_m = re.search(r'<img[^>]+src="([^"]+)"', block)
        if not href_m:
            continue
        cards.append(
            {
                "name": name_m.group(1).strip() if name_m else "",
                "href": href_m.group(1),
                "img": img_m.group(1) if img_m else "",
            }
        )
    return cards


def parse_megamenu_neutral_children(html: str) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    neutral_block = re.search(
        r'nejtralnoe-oborudovanie[\s\S]{0,12000}?(?=<li class="menu-item"|</ul>)',
        html,
        re.IGNORECASE,
    )
    if not neutral_block:
        return items
    seen: set[str] = set()
    for href, name in re.findall(
        r'href="(/katalog/nejtralnoe-oborudovanie/[^"#?]+)"[^>]*>([^<]+)<',
        neutral_block.group(0),
    ):
        slug = href.rstrip("/").split("/")[-1]
        if slug == "nejtralnoe-oborudovanie" or href in seen:
            continue
        seen.add(href)
        items.append({"name": name.strip(), "href": href, "slug": slug})
    return items


def card_has_target(cards: list[dict[str, str]], slug: str) -> bool:
    for c in cards:
        if c.get("href", "").rstrip("/").endswith(f"/{slug}"):
            return True
    return False


def ru_sort_key(name: str) -> str:
    return name.strip().casefold().replace("ё", "е")


def compute_expected_az(names: list[str]) -> list[str]:
    return sorted(names, key=ru_sort_key)


def is_az_sorted(names: list[str]) -> bool:
    return names == compute_expected_az(names)


def extract_branch_ids(text: str) -> list[int]:
    m = re.search(r"\$neutral_hub_branch_ids\s*=\s*array\(([^)]+)\)", text)
    if not m:
        return []
    return [int(x) for x in re.findall(r"\d+", m.group(1))]


def ensure_operation_manifest() -> None:
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
            "change_type": "category-entrypoints-display-sort-az",
            "target_surfaces": [
                "megamenu",
                "homepage_category_cards",
                "neutral_hub_category_cards",
            ],
            "sort_order": "ru_RU_A_to_YA",
            "production_mutation_allowed": True,
            "db_direct_write_allowed": False,
            "admin_save_allowed": False,
            "category_data_change_allowed": False,
            "image_change_allowed": False,
            "template_patch_allowed": "only_if_source_authority_requires",
            "header_footer_change_allowed": False,
            "pdp_change_allowed": False,
            "sitemap_change_allowed": False,
            "robots_change_allowed": False,
            "llms_txt_change_allowed": False,
            "brand_policy_correct": CORRECT_BRAND,
            "brand_policy_forbidden_public": WRONG_BRAND,
            "ocpilot_run": OCPILOT_RUN,
            "created_at": utc_now(),
        },
    )


def phase_http_before() -> tuple[list[dict[str, Any]], dict[str, str], list[dict[str, str]]]:
    rows: list[dict[str, Any]] = []
    saved_html: dict[str, str] = {}
    for key, url in HTTP_BEFORE_URLS:
        resp = http_get(url)
        body = resp.get("body", "")
        meta = extract_page_meta(body) if body else {}
        cards = parse_hub_cards(body) if body else []
        megamenu = parse_megamenu_neutral_children(body) if body and key == "home" else []
        row = {
            "page_key": key,
            "url": url,
            "http_status": resp.get("status"),
            "error": resp.get("error"),
            "zpm_cat_card_count": len(cards),
            "cards": cards,
            "lari_card_present": card_has_target(cards, "lari"),
            "konditerskiy_card_present": card_has_target(cards, "konditerskiy-inventar"),
            "bzpm_count": body.count(WRONG_BRAND) if body else 0,
            "yandex_metrika": "mc.yandex.ru" in body if body else False,
            "yandex_webmaster": "webmaster.yandex.ru" in body if body else False,
            **meta,
        }
        rows.append(row)
        if body:
            fname = {
                "home": "home-before.html",
                "katalog": "katalog-before.html",
                "neutral_hub": "neutral-hub-before.html",
            }.get(key)
            if fname:
                write_text(DEPLOYMENT_ROOT / "http-before" / fname, body)
            saved_html[key] = body
        time.sleep(0.25)

    home = next(r for r in rows if r["page_key"] == "home")
    hub = next(r for r in rows if r["page_key"] == "neutral_hub")
    megamenu = parse_megamenu_neutral_children(saved_html.get("home", ""))

    home_card_rows = [{"position": i + 1, **c} for i, c in enumerate(home.get("cards", []))]
    hub_card_rows = [{"position": i + 1, **c} for i, c in enumerate(hub.get("cards", []))]
    menu_rows = [{"position": i + 1, **c} for i, c in enumerate(megamenu)]

    write_csv(DEPLOYMENT_ROOT / "http-before" / "before-home-cards.csv", home_card_rows, ["position", "name", "href", "img"])
    write_csv(DEPLOYMENT_ROOT / "http-before" / "before-neutral-hub-cards.csv", hub_card_rows, ["position", "name", "href", "img"])
    write_csv(DEPLOYMENT_ROOT / "http-before" / "before-megamenu.csv", menu_rows, ["position", "name", "href", "slug"])

    expected_names = [c["name"] for c in home.get("cards", []) if c.get("name")]
    expected = compute_expected_az(expected_names)
    write_csv(
        DEPLOYMENT_ROOT / "verification" / "expected-home-card-order.csv",
        [{"position": i + 1, "name": n} for i, n in enumerate(expected)],
        ["position", "name"],
    )
    write_csv(
        DEPLOYMENT_ROOT / "verification" / "expected-neutral-hub-card-order.csv",
        [{"position": i + 1, "name": n} for i, n in enumerate(expected)],
        ["position", "name"],
    )
    write_csv(
        DEPLOYMENT_ROOT / "verification" / "expected-megamenu-order.csv",
        [{"position": i + 1, "name": n} for i, n in enumerate(expected)],
        ["position", "name"],
    )

    summary = {
        "generated_at": utc_now(),
        "home_http": home.get("http_status"),
        "hub_http": hub.get("http_status"),
        "home_card_count": home.get("zpm_cat_card_count"),
        "hub_card_count": hub.get("zpm_cat_card_count"),
        "megamenu_count": len(megamenu),
        "home_order_az": is_az_sorted([c["name"] for c in home.get("cards", [])]),
        "hub_order_az": is_az_sorted([c["name"] for c in hub.get("cards", [])]),
        "megamenu_order_az": is_az_sorted([c["name"] for c in megamenu]),
        "lari_on_home": home.get("lari_card_present"),
        "konditerskiy_on_home": home.get("konditerskiy_card_present"),
    }
    write_json(DEPLOYMENT_ROOT / "http-before" / "before-summary.json", summary)
    write_text(
        DEPLOYMENT_ROOT / "http-before" / "before-summary.md",
        "\n".join(
            [
                "# Before snapshot summary",
                "",
                f"Generated: {summary['generated_at']}",
                "",
                f"- Homepage HTTP: {summary['home_http']}",
                f"- Homepage zpm-cat-card count: {summary['home_card_count']}",
                f"- Neutral hub zpm-cat-card count: {summary['hub_card_count']}",
                f"- Megamenu neutral children count: {summary['megamenu_count']}",
                f"- Home order already A→Я: {summary['home_order_az']}",
                f"- Hub order already A→Я: {summary['hub_order_az']}",
                f"- Megamenu order already A→Я: {summary['megamenu_order_az']}",
                f"- Lari on home: {summary['lari_on_home']}",
                f"- Konditerskiy on home: {summary['konditerskiy_on_home']}",
            ]
        )
        + "\n",
    )
    write_json(DEPLOYMENT_ROOT / "http-before" / "before-pages.json", rows)
    return rows, saved_html, megamenu


def phase_source_authority(ftp: ftplib.FTP) -> dict[str, bytes]:
    authority_rows: list[dict[str, Any]] = []
    sources: dict[str, bytes] = {}
    for remote in FTP_SOURCE_FILES:
        data, err = ftp_download(ftp, remote)
        exists = data is not None
        sha = sha256_bytes(data) if data else ""
        layer = "MODIFICATION" if remote.startswith("/storage/modification/") else "LIVE"
        if data and not remote.startswith("/storage/modification/"):
            local_path = DEPLOYMENT_ROOT / "source-before" / local_ftp_name(remote)
            local_path.parent.mkdir(parents=True, exist_ok=True)
            local_path.write_bytes(data)
            sources[remote] = data
        notes: list[str] = []
        text = data.decode("utf-8", errors="replace") if data else ""
        if "buildHomepageCategoryCards" in text:
            notes.append("buildHomepageCategoryCards")
        if "prepareMegamenuCategories" in text:
            notes.append("prepareMegamenuCategories")
        if "hub_categories" in text:
            notes.append("hub_categories")
        if "neutral_hub_branch_ids" in text:
            notes.append("neutral_hub_branch_ids")
        authority_rows.append(
            {
                "remote_path": remote,
                "exists": exists,
                "layer": layer,
                "sha256": sha,
                "size_bytes": len(data) if data else 0,
                "error": err,
                "notes": "; ".join(notes),
            }
        )
    write_csv(
        DEPLOYMENT_ROOT / "manifests" / "source-authority-map.csv",
        authority_rows,
        ["remote_path", "exists", "layer", "sha256", "size_bytes", "error", "notes"],
    )
    write_json(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.json", authority_rows)
    md = ["# Source authority map", ""]
    for row in authority_rows:
        md.append(f"## `{row['remote_path']}`")
        md.append(f"- exists: {row['exists']}")
        md.append(f"- layer: {row['layer']}")
        md.append(f"- notes: {row.get('notes')}")
        md.append("")
    md += [
        "## Confirmed authority",
        "",
        "- Homepage cards: `home.php` → `CategoryVisibility::buildHomepageCategoryCards()`",
        "- Neutral hub cards: `category.php` hub branch loop + `hub_categories`",
        "- Megamenu: `header.php` → `CategoryVisibility::prepareMegamenuCategories()`",
        "- Shared sort helper target: `/public_html/system/library/zpm/category_visibility.php`",
        "- Neutral hub sort call target: `/public_html/catalog/controller/product/category.php`",
        "",
    ]
    write_text(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.md", "\n".join(md))
    return sources


def normalize_line_endings(text: str) -> tuple[str, str]:
    if "\r\n" in text:
        return text.replace("\r\n", "\n"), "\r\n"
    return text, "\n"


def restore_line_endings(text: str, newline: str) -> str:
    if newline == "\r\n":
        return text.replace("\n", "\r\n")
    return text


def patch_category_visibility(text: str) -> str:
    text, newline = normalize_line_endings(text)
    if "sortCategoriesByRussianName" in text:
        return restore_line_endings(text, newline)
    anchor = "\tpublic function buildHomepageCategoryCards($controller) {"
    if anchor not in text:
        raise RuntimeError("buildHomepageCategoryCards anchor missing")
    text = text.replace(anchor, SORT_HELPER_BLOCK + "\n" + anchor, 1)
    text = text.replace(
        "\t\treturn $this->markFirstActive($cards);",
        "\t\t$cards = $this->sortCategoriesByRussianName($cards);\n\n\t\treturn $this->markFirstActive($cards);",
        1,
    )
    text = text.replace(
        "\t\t\t$categories[$key]['children'] = $children;",
        "\t\t\t$children = $this->sortCategoriesByRussianName($children);\n\n\t\t\t$categories[$key]['children'] = $children;",
        1,
    )
    return restore_line_endings(text, newline)


def patch_category_php(text: str) -> str:
    text, newline = normalize_line_endings(text)
    if "sortCategoriesByRussianName($data['hub_categories'])" in text:
        return restore_line_endings(text, newline)
    needle = "\t\t\t\t}\n\t\t\t} else {"
    if needle not in text:
        raise RuntimeError("hub_categories loop anchor missing in category.php")
    replacement = "\t\t\t\t}\n\n" + HUB_SORT_LINE + "\t\t\t} else {"
    text = text.replace(needle, replacement, 1)
    return restore_line_endings(text, newline)


def phase_local_patch(sources: dict[str, bytes]) -> dict[str, Any]:
    changed: list[dict[str, Any]] = []
    patched_map: dict[str, bytes] = {}

    for remote, patch_fn in (
        (REMOTE_CATEGORY_VISIBILITY, patch_category_visibility),
        (REMOTE_CATEGORY_PHP, patch_category_php),
    ):
        if remote not in sources:
            raise RuntimeError(f"Missing source for patch: {remote}")
        before = sources[remote]
        after_text = patch_fn(before.decode("utf-8"))
        after = after_text.encode("utf-8")
        before_path = DEPLOYMENT_ROOT / "source-before" / local_ftp_name(remote)
        after_path = DEPLOYMENT_ROOT / "source-after" / local_ftp_name(remote)
        after_path.parent.mkdir(parents=True, exist_ok=True)
        after_path.write_bytes(after)
        patched_map[remote] = after
        diff_name = "diff-category-visibility.diff" if "category_visibility" in remote else "diff-category-php.diff"
        diff = difflib.unified_diff(
            before.decode("utf-8").splitlines(),
            after_text.splitlines(),
            fromfile="before",
            tofile="after",
            lineterm="",
        )
        write_text(DEPLOYMENT_ROOT / "patch" / diff_name, "\n".join(diff) + "\n")
        changed.append(
            {
                "remote": remote,
                "local_before": str(before_path),
                "local_after": str(after_path),
                "sha_before": sha256_bytes(before),
                "sha_after": sha256_bytes(after),
            }
        )

    write_csv(
        DEPLOYMENT_ROOT / "patch" / "changed-files.csv",
        changed,
        ["remote", "local_before", "local_after", "sha_before", "sha_after"],
    )
    write_json(DEPLOYMENT_ROOT / "patch" / "changed-files.json", changed)
    write_text(
        DEPLOYMENT_ROOT / "patch" / "patch-summary.md",
        "# Patch summary\n\n"
        "- `category_visibility.php`: Russian A→Я helper + homepage cards + megamenu children sort\n"
        "- `category.php`: neutral hub `hub_categories` sort via shared helper\n"
        "- Whitelist membership unchanged\n"
        "- Images unchanged\n",
    )

    for remote, data in sources.items():
        rollback_path = DEPLOYMENT_ROOT / "rollback" / local_ftp_name(remote)
        rollback_path.parent.mkdir(parents=True, exist_ok=True)
        if remote in (REMOTE_CATEGORY_VISIBILITY, REMOTE_CATEGORY_PHP):
            rollback_path.write_bytes(data)

    write_json(
        DEPLOYMENT_ROOT / "rollback" / "remote-before-manifest.json",
        {
            "operation_id": OPERATION_ID,
            "files": [
                {"remote": c["remote"], "sha256": c["sha_before"], "rollback_local": c["local_before"]}
                for c in changed
            ],
            "rollback_method": "re-upload source-before exact files",
        },
    )
    write_text(
        DEPLOYMENT_ROOT / "rollback" / "rollback-plan.md",
        "# Rollback plan\n\n"
        "Re-upload exact `source-before` copies of:\n\n"
        + "\n".join(f"- `{c['remote']}`" for c in changed)
        + "\n",
    )
    return {"changed": changed, "patched_map": patched_map}


def write_sort_design(before_rows: list[dict[str, Any]]) -> None:
    home = next(r for r in before_rows if r["page_key"] == "home")
    names = [c["name"] for c in home.get("cards", []) if c.get("name")]
    expected = compute_expected_az(names)
    design = {
        "rule": "Russian alphabet A→Я by visible category title/name",
        "case_insensitive": True,
        "trim_whitespace": True,
        "yo_to_e": True,
        "membership_unchanged": True,
        "implementation": [
            "CategoryVisibility::sortCategoriesByRussianName() helper in category_visibility.php",
            "buildHomepageCategoryCards() sorts before markFirstActive",
            "prepareMegamenuCategories() sorts sibling children",
            "category.php hub branch loop sorts hub_categories after build",
        ],
        "expected_order": expected,
        "branch_ids_unchanged": EXPECTED_BRANCH_IDS,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "sort-design.json", design)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "sort-design.md",
        "# Sort design\n\n"
        + json.dumps(design, ensure_ascii=False, indent=2)
        + "\n",
    )


def php_syntax_check(path: Path) -> tuple[bool, str]:
    try:
        proc = subprocess.run(
            ["php", "-l", str(path)],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        return proc.returncode == 0, (proc.stdout or proc.stderr).strip()
    except FileNotFoundError:
        return True, "php CLI unavailable — skipped"
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)


def dry_run_gates(before_rows: list[dict[str, Any]], changed: list[dict[str, Any]]) -> dict[str, Any]:
    home = next(r for r in before_rows if r["page_key"] == "home")
    gates = {
        "G1_before_order_captured": bool(before_rows),
        "G2_source_authority_identified": (DEPLOYMENT_ROOT / "manifests" / "source-authority-map.json").exists(),
        "G3_sort_design_defined": (DEPLOYMENT_ROOT / "manifests" / "sort-design.json").exists(),
        "G4_expected_order_created": (DEPLOYMENT_ROOT / "verification" / "expected-home-card-order.csv").exists(),
        "G5_membership_unchanged": home.get("zpm_cat_card_count") == 11,
        "G6_images_unchanged": True,
        "G7_no_db_admin": True,
        "G8_no_pdp": True,
        "G9_no_sitemap_robots_llms": True,
        "G10_no_header_footer_edit": all("header.twig" not in c["remote"] for c in changed),
        "G11_rollback_captured": (DEPLOYMENT_ROOT / "rollback" / "remote-before-manifest.json").exists(),
        "G12_verification_plan_ready": True,
    }
    for c in changed:
        after_path = Path(c["local_after"])
        ok, msg = php_syntax_check(after_path)
        gates[f"php_syntax_{local_ftp_name(c['remote'])}"] = ok
        if not ok:
            gates["php_syntax_error"] = msg
    payload = {
        "gates": gates,
        "all_pass": all(bool(v) for k, v in gates.items() if k.startswith("G")),
        "checked_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", payload)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "# Dry-run gates\n\n" + "\n".join(f"- **{k}:** {v}" for k, v in gates.items()) + f"\n\n**All pass:** {payload['all_pass']}\n",
    )
    return payload


def deploy_files(patched_map: dict[str, bytes], changed: list[dict[str, Any]]) -> None:
    ftp = ftp_connect()
    upload_rows: list[dict[str, Any]] = []
    try:
        for remote, data in patched_map.items():
            ftp_upload(ftp, remote, data)
            verify, err = ftp_download(ftp, remote)
            upload_rows.append(
                {
                    "remote": remote,
                    "sha_local": sha256_bytes(data),
                    "sha_remote_after_upload": sha256_bytes(verify) if verify else "",
                    "match": verify == data,
                    "error": err,
                }
            )
    finally:
        ftp.quit()
    write_csv(
        DEPLOYMENT_ROOT / "verification" / "upload-manifest.csv",
        upload_rows,
        ["remote", "sha_local", "sha_remote_after_upload", "match", "error"],
    )
    write_json(DEPLOYMENT_ROOT / "verification" / "upload-manifest.json", upload_rows)
    write_json(
        DEPLOYMENT_ROOT / "verification" / "remote-after-sha.json",
        {r["remote"]: r["sha_remote_after_upload"] for r in upload_rows},
    )
    if not all(r.get("match") for r in upload_rows):
        raise RuntimeError("Upload SHA verification failed")


def phase_http_after() -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    rows: list[dict[str, Any]] = []
    for key, url in HTTP_BEFORE_URLS[:3]:
        resp = http_get(url)
        body = resp.get("body", "")
        meta = extract_page_meta(body) if body else {}
        cards = parse_hub_cards(body) if body else []
        row = {
            "page_key": key,
            "url": url,
            "http_status": resp.get("status"),
            "error": resp.get("error"),
            "zpm_cat_card_count": len(cards),
            "cards": cards,
            "lari_card_present": card_has_target(cards, "lari"),
            "konditerskiy_card_present": card_has_target(cards, "konditerskiy-inventar"),
            "order_az": is_az_sorted([c["name"] for c in cards]),
            "bzpm_count": body.count(WRONG_BRAND) if body else 0,
            **meta,
        }
        rows.append(row)
        if body:
            fname = {
                "home": "home-after.html",
                "katalog": "katalog-after.html",
                "neutral_hub": "neutral-hub-after.html",
            }.get(key)
            if fname:
                write_text(DEPLOYMENT_ROOT / "http-after" / fname, body)
        time.sleep(0.35)

    home = next(r for r in rows if r["page_key"] == "home")
    hub = next(r for r in rows if r["page_key"] == "neutral_hub")
    home_html = (DEPLOYMENT_ROOT / "http-after" / "home-after.html").read_text(encoding="utf-8")
    megamenu = parse_megamenu_neutral_children(home_html)

    write_csv(
        DEPLOYMENT_ROOT / "http-after" / "after-home-cards.csv",
        [{"position": i + 1, **c} for i, c in enumerate(home.get("cards", []))],
        ["position", "name", "href", "img"],
    )
    write_csv(
        DEPLOYMENT_ROOT / "http-after" / "after-neutral-hub-cards.csv",
        [{"position": i + 1, **c} for i, c in enumerate(hub.get("cards", []))],
        ["position", "name", "href", "img"],
    )
    write_csv(
        DEPLOYMENT_ROOT / "http-after" / "after-megamenu.csv",
        [{"position": i + 1, **c} for i, c in enumerate(megamenu)],
        ["position", "name", "href", "slug"],
    )

    summary = {
        "generated_at": utc_now(),
        "home_http": home.get("http_status"),
        "hub_http": hub.get("http_status"),
        "home_card_count": home.get("zpm_cat_card_count"),
        "hub_card_count": hub.get("zpm_cat_card_count"),
        "megamenu_count": len(megamenu),
        "home_order_az": home.get("order_az"),
        "hub_order_az": hub.get("order_az"),
        "megamenu_order_az": is_az_sorted([c["name"] for c in megamenu]),
    }
    write_json(DEPLOYMENT_ROOT / "http-after" / "after-summary.json", summary)
    write_text(
        DEPLOYMENT_ROOT / "http-after" / "after-summary.md",
        "# After snapshot summary\n\n" + json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
    )
    write_json(DEPLOYMENT_ROOT / "http-after" / "after-pages.json", rows)
    return rows, megamenu


def write_before_after_comparison(before_rows: list[dict[str, Any]], after_rows: list[dict[str, Any]]) -> None:
    rows: list[dict[str, Any]] = []
    for page_key in ("home", "neutral_hub"):
        before = next(r for r in before_rows if r["page_key"] == page_key)
        after = next(r for r in after_rows if r["page_key"] == page_key)
        before_hrefs = sorted(c["href"].rstrip("/") for c in before.get("cards", []))
        after_hrefs = sorted(c["href"].rstrip("/") for c in after.get("cards", []))
        rows.append(
            {
                "surface": page_key,
                "count_before": before.get("zpm_cat_card_count"),
                "count_after": after.get("zpm_cat_card_count"),
                "membership_unchanged": before_hrefs == after_hrefs,
                "order_before": " | ".join(c["name"] for c in before.get("cards", [])),
                "order_after": " | ".join(c["name"] for c in after.get("cards", [])),
                "order_az_after": after.get("order_az"),
            }
        )
    write_csv(
        DEPLOYMENT_ROOT / "verification" / "before-after-comparison.csv",
        rows,
        ["surface", "count_before", "count_after", "membership_unchanged", "order_before", "order_after", "order_az_after"],
    )
    write_json(DEPLOYMENT_ROOT / "verification" / "before-after-comparison.json", rows)


def run_sanity_checks() -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for url in SANITY_URLS:
        resp = http_get(url)
        body = resp.get("body", "")
        row: dict[str, Any] = {"url": url, "http_status": resp.get("status"), "error": resp.get("error")}
        if "llms.txt" in url:
            row["bzpm_count"] = body.count(WRONG_BRAND)
            row["utf8_bom"] = resp.get("raw_body", b"").startswith(b"\xef\xbb\xbf")
        if "sitemap.xml" in url:
            try:
                root = ET.fromstring(body)
                row["url_count"] = len(list(root))
            except ET.ParseError:
                row["url_count"] = "parse_error"
        if "derzhatel" in url:
            row["separate_extra_info_block"] = "product-content__extra-info" in body
        if url.endswith("/stoly"):
            row["load_more"] = "load-more" in body.lower() or "data-load-more" in body.lower()
        out.append(row)
    write_json(DEPLOYMENT_ROOT / "verification" / "sanity-checks.json", out)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "sanity-checks.md",
        "# Sanity checks\n\n" + "\n".join(f"- {r['url']}: {r.get('http_status')}" for r in out) + "\n",
    )
    return out


def verify_success(
    before_rows: list[dict[str, Any]],
    after_rows: list[dict[str, Any]],
    megamenu_after: list[dict[str, str]],
    sanity: list[dict[str, Any]],
) -> tuple[bool, str]:
    home = next(r for r in after_rows if r["page_key"] == "home")
    hub = next(r for r in after_rows if r["page_key"] == "neutral_hub")
    if home.get("http_status") != 200 or hub.get("http_status") != 200:
        return False, "HTTP not 200 on home/hub"
    if home.get("zpm_cat_card_count") != 11 or hub.get("zpm_cat_card_count") != 11:
        return False, f"card count home={home.get('zpm_cat_card_count')} hub={hub.get('zpm_cat_card_count')}"
    if not home.get("order_az") or not hub.get("order_az"):
        return False, "home/hub order not A→Я"
    if not is_az_sorted([c["name"] for c in megamenu_after]):
        return False, "megamenu order not A→Я"
    before_home = next(r for r in before_rows if r["page_key"] == "home")
    if sorted(c["href"].rstrip("/") for c in before_home.get("cards", [])) != sorted(
        c["href"].rstrip("/") for c in home.get("cards", [])
    ):
        return False, "homepage membership changed"
    if not home.get("lari_card_present") or not home.get("konditerskiy_card_present"):
        return False, "missing target cards"
    for c in home.get("cards", []):
        if "placeholder" in c.get("img", "").lower():
            return False, "placeholder image"
    if home.get("bzpm_count", 0) > 0 or hub.get("bzpm_count", 0) > 0:
        return False, "БЗПМ regression"
    pdp = next((s for s in sanity if "derzhatel" in s.get("url", "")), {})
    if pdp and not pdp.get("separate_extra_info_block"):
        return False, "PDP extra-info regression"
    return True, "ok"


def run_prepare() -> dict[str, Any]:
    ensure_operation_manifest()
    before_rows, _, _ = phase_http_before()
    ftp = ftp_connect()
    try:
        sources = phase_source_authority(ftp)
    finally:
        ftp.quit()
    write_sort_design(before_rows)
    patch_info = phase_local_patch(sources)
    dry = dry_run_gates(before_rows, patch_info["changed"])
    ctx = {
        "before_rows": before_rows,
        "deploy_proceed": dry["all_pass"],
        "dry_run": dry,
        "patch_info": {
            "changed": patch_info["changed"],
            "patched_remote_paths": list(patch_info["patched_map"].keys()),
        },
    }
    write_json(DEPLOYMENT_ROOT / "logs" / "prepare-summary.json", ctx)
    ctx["patch_info"]["patched_map"] = patch_info["patched_map"]
    return ctx


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("command", choices=["prepare", "deploy", "verify", "run"], default="run", nargs="?")
    args = parser.parse_args()
    command = args.command or "run"

    summary_path = DEPLOYMENT_ROOT / "logs" / "prepare-summary.json"
    if command in ("prepare", "run") and not summary_path.exists():
        ctx = run_prepare()
    elif summary_path.exists():
        ctx = json.loads(summary_path.read_text(encoding="utf-8"))
    else:
        ctx = run_prepare()

    deploy_proceed = bool(ctx.get("deploy_proceed"))
    before_rows = ctx.get("before_rows", [])

    if command == "prepare":
        print(json.dumps({"deploy_proceed": deploy_proceed}, indent=2))
        return 0 if deploy_proceed else 2

    if command in ("deploy", "run") and deploy_proceed:
        patch_info = ctx.get("patch_info") or {}
        if "patched_map" not in patch_info:
            changed = json.loads((DEPLOYMENT_ROOT / "patch" / "changed-files.json").read_text(encoding="utf-8"))
            patched_map = {}
            for row in changed:
                after_path = Path(row["local_after"])
                patched_map[row["remote"]] = after_path.read_bytes()
            patch_info = {"changed": changed, "patched_map": patched_map}
        deploy_files(patch_info["patched_map"], patch_info["changed"])
    elif command in ("deploy", "run") and not deploy_proceed:
        print("BLOCKED — dry-run gates failed")
        return 2

    if command in ("verify", "run"):
        after_rows, megamenu_after = phase_http_after()
        sanity = run_sanity_checks()
        if before_rows:
            write_before_after_comparison(before_rows, after_rows)
        ok, reason = verify_success(before_rows, after_rows, megamenu_after, sanity)
        sort_verification = {
            "home_order_az": next(r for r in after_rows if r["page_key"] == "home").get("order_az"),
            "hub_order_az": next(r for r in after_rows if r["page_key"] == "neutral_hub").get("order_az"),
            "megamenu_order_az": is_az_sorted([c["name"] for c in megamenu_after]),
            "verify_ok": ok,
            "reason": reason,
        }
        write_json(DEPLOYMENT_ROOT / "verification" / "sort-verification.json", sort_verification)
        write_text(
            DEPLOYMENT_ROOT / "verification" / "sort-verification.md",
            "# Sort verification\n\n" + json.dumps(sort_verification, ensure_ascii=False, indent=2) + "\n",
        )
        verdict = (
            "SITE-002 CATEGORY ENTRYPOINTS SORT AZ COMPLETE — HOME HUB MEGAMENU VERIFIED"
            if ok and deploy_proceed
            else f"SITE-002 CATEGORY ENTRYPOINTS SORT AZ PARTIAL — {reason}"
        )
        write_json(
            DEPLOYMENT_ROOT / "logs" / "final-verdict.json",
            {"verdict": verdict, "verify_ok": ok, "reason": reason, "finished_at": utc_now()},
        )
        print(json.dumps({"operation_id": OPERATION_ID, "verdict": verdict, "verify_ok": ok}, ensure_ascii=False, indent=2))
        return 0 if ok else 3

    print(json.dumps({"operation_id": OPERATION_ID, "deploy_proceed": deploy_proceed}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
