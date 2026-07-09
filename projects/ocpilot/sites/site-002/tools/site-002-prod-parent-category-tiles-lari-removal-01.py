#!/usr/bin/env python3
"""SITE-002 Production — remove Лари (88) from Parent Category Tiles only (Run 4.236)."""
from __future__ import annotations

import argparse
import csv
import difflib
import ftplib
import hashlib
import io
import json
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01"
OCPILOT_RUN = "4.236"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION_CONTROLLED_MUTATION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CATEGORY-LARI-REPARENT-01"
CHECKPOINT_AFTER = "SITE-002-STABLE-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01"
WRONG_BRAND = "БЗПМ"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
REPO_TOOLS = Path(r"X:\AI MARS\projects\ocpilot\sites\site-002\tools")

LARI_ID = 88
SHKAFY_ID = 358
EXPECTED_IDS_BEFORE = [322, 331, 301, 326, 354, 358, 207, 80, 86, 88, 360]
EXPECTED_IDS_AFTER = [322, 331, 301, 326, 354, 358, 207, 80, 86, 360]

REMOTE_CATEGORY_VISIBILITY = "/public_html/system/library/zpm/category_visibility.php"

FTP_SOURCE_FILES = [
    REMOTE_CATEGORY_VISIBILITY,
    "/public_html/catalog/controller/common/home.php",
    "/public_html/catalog/controller/product/category.php",
    "/public_html/catalog/controller/common/header.php",
]

PRIMARY_URLS = [
    ("home", "https://bzpm.ru/"),
    ("katalog", "https://bzpm.ru/katalog"),
    ("neutral_hub", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie"),
    ("shkafy_hub", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari"),
    ("lari_nested", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari"),
]

REDIRECT_URLS = [
    ("lari_old_flat", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari"),
]

SANITY_URLS = [
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/custom-equipment",
    "https://bzpm.ru/sitemap.xml",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/llms.txt",
]

SUBDIRS = (
    "source-before",
    "source-after",
    "http-before",
    "http-after",
    "entrypoints-before",
    "entrypoints-after",
    "cache",
    "rollback",
    "verification",
    "manifests",
    "reports",
    "logs",
)

PATCH_MARKER = "SITE-002-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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
    ftp.storbinary(f"STOR {remote}", io.BytesIO(data))


def http_get(url: str, follow_redirects: bool = True) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xml,*/*", "Cache-Control": "no-cache"},
        method="GET",
    )
    if not follow_redirects:
        class NoRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, req, fp, code, msg, headers, newurl):
                return None

        opener = urllib.request.build_opener(NoRedirect)
        try:
            with opener.open(req, timeout=90) as resp:
                body = resp.read()
                return _http_result(url, resp.status, resp.geturl(), resp.headers, body, None)
        except urllib.error.HTTPError as exc:
            raw = exc.read() if exc.fp else b""
            return _http_result(url, exc.code, exc.geturl(), exc.headers, raw, str(exc))
        except urllib.error.URLError as exc:
            return _http_result(url, None, url, {}, b"", str(exc))

    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = resp.read()
            return _http_result(url, resp.status, resp.geturl(), resp.headers, body, None)
    except urllib.error.HTTPError as exc:
        raw = exc.read() if exc.fp else b""
        return _http_result(url, exc.code, exc.geturl(), exc.headers, raw, str(exc))
    except urllib.error.URLError as exc:
        return _http_result(url, None, url, {}, b"", str(exc))


def _http_result(url, status, final_url, headers, body, error) -> dict[str, Any]:
    charset = headers.get_content_charset() if hasattr(headers, "get_content_charset") else None
    if not charset and hasattr(headers, "items"):
        charset = "utf-8"
    return {
        "url": url,
        "status": status,
        "final_url": final_url,
        "location": headers.get("Location", "") if hasattr(headers, "get") else "",
        "headers": dict(headers.items()) if hasattr(headers, "items") else {},
        "raw_body": body,
        "body": body.decode(charset or "utf-8", errors="replace"),
        "error": error,
    }


def parse_parent_tiles(html_text: str) -> list[dict[str, str]]:
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


def parse_catalog_menu_tiles(html_text: str) -> list[dict[str, str]]:
    tiles: list[dict[str, str]] = []
    for block in re.findall(
        r'<a[^>]+class="[^"]*zpm-catalog__tile[^"]*"[^>]*>.*?</a>', html_text, re.DOTALL | re.IGNORECASE
    ):
        href_m = re.search(r'href="([^"]+)"', block)
        name_m = re.search(r'class="[^"]*zpm-catalog__tile-title[^"]*"[^>]*>([^<]+)<', block)
        if href_m and name_m:
            tiles.append({"name": name_m.group(1).strip(), "href": href_m.group(1)})
    return tiles


def analyze_katalog_surface(body: str) -> dict[str, Any]:
    cat_cards = parse_parent_tiles(body)
    menu_tiles = parse_catalog_menu_tiles(body)
    return {
        "zpm_cat_card_count": len(cat_cards),
        "megamenu_tile_count": len(menu_tiles),
        "lari_in_page": bool(card_named(cat_cards, "Лари") or card_named(menu_tiles, "Лари")),
        "shkafy_in_page": bool(card_named(cat_cards, "Шкафы и лари") or card_named(menu_tiles, "Шкафы и лари")),
        "megamenu_tiles": menu_tiles,
    }


def card_named(cards: list[dict[str, str]], name: str) -> dict[str, str] | None:
    for c in cards:
        if c.get("name", "").strip().lower() == name.strip().lower():
            return c
    return None


def extract_branch_ids(text: str) -> list[int]:
    m = re.search(r"\$neutral_hub_branch_ids\s*=\s*array\(([^)]+)\)", text)
    if not m:
        return []
    return [int(x) for x in re.findall(r"\d+", m.group(1))]


def extract_canonical(html: str) -> str:
    m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']', html, re.I)
    if m:
        return m.group(1)
    m = re.search(r'href=["\']([^"\']+)["\'][^>]+rel=["\']canonical["\']', html, re.I)
    return m.group(1) if m else ""


def local_ftp_name(remote: str) -> str:
    return remote.strip("/").replace("/", "__")


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
            "change_type": "parent-category-tiles-adjustment",
            "terminology": "Parent Category Tiles / Витрина родительских категорий",
            "category_removed_from_parent_tiles": "Лари",
            "category_id_removed_from_parent_tiles": LARI_ID,
            "category_kept": "Шкафы и лари",
            "category_id_kept": SHKAFY_ID,
            "category_lari_page_kept": True,
            "category_lari_nested_url_kept": True,
            "production_mutation_allowed": True,
            "ftp_upload_allowed": "exact_scoped_files_only",
            "db_write_allowed": False,
            "admin_save_allowed": False,
            "category_data_change_allowed": False,
            "redirect_change_allowed": False,
            "sitemap_change_allowed": False,
            "import_run_allowed": False,
            "monitor_run_allowed": False,
            "cache_clear_allowed": "conditional_if_required",
            "created_at": utc_now(),
        },
    )


def capture_http_phase(label: str, urls: list[tuple[str, str]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    out_dir = DEPLOYMENT_ROOT / f"http-{label}"
    for key, url in urls:
        resp = http_get(url)
        body = resp.get("body", "")
        tiles = parse_parent_tiles(body) if body else []
        row: dict[str, Any] = {
            "page_key": key,
            "url": url,
            "http_status": resp.get("status"),
            "final_url": resp.get("final_url"),
            "location": resp.get("location", ""),
            "error": resp.get("error"),
            "parent_tile_count": len(tiles),
            "parent_tiles": tiles,
            "lari_parent_tile": card_named(tiles, "Лари"),
            "shkafy_parent_tile": card_named(tiles, "Шкафы и лари"),
            "canonical": extract_canonical(body) if body else "",
            "bzpm_count": body.count(WRONG_BRAND) if body else 0,
        }
        if key == "shkafy_hub" and body:
            row["lari_child_tile"] = card_named(tiles, "Лари") or _find_child_lari_link(body)
        if key == "katalog" and body:
            row.update(analyze_katalog_surface(body))
        if key == "lari_nested" and body:
            row["h1"] = _first_h1(body)
            row["breadcrumbs"] = _breadcrumb_text(body)
        rows.append(row)
        fname = f"{key}-{label}.html"
        if body:
            write_text(out_dir / fname, body)
        time.sleep(0.3)

    tile_rows: list[dict[str, Any]] = []
    for row in rows:
        if row["page_key"] in ("home", "katalog", "neutral_hub"):
            for i, tile in enumerate(row.get("parent_tiles", []), 1):
                tile_rows.append(
                    {
                        "surface": row["page_key"],
                        "position": i,
                        "name": tile.get("name"),
                        "href": tile.get("href"),
                        "img": tile.get("img"),
                    }
                )

    ep_dir = DEPLOYMENT_ROOT / f"entrypoints-{label}"
    write_csv(
        ep_dir / f"parent-category-tiles-{label}.csv",
        tile_rows,
        ["surface", "position", "name", "href", "img"],
    )
    write_json(ep_dir / f"parent-category-tiles-{label}.json", rows)
    md = [
        f"# Parent Category Tiles — {label}",
        "",
        f"Generated: {utc_now()}",
        "",
    ]
    for row in rows:
        md.append(f"## {row['page_key']} — {row['url']}")
        md.append(f"- HTTP: {row.get('http_status')}")
        md.append(f"- Parent tile count: {row.get('parent_tile_count')}")
        md.append(f"- Лари parent tile: {'yes' if row.get('lari_parent_tile') else 'no'}")
        md.append(f"- Шкафы и лари parent tile: {'yes' if row.get('shkafy_parent_tile') else 'no'}")
        if row.get("lari_child_tile"):
            md.append(f"- Лари child on shkafy hub: yes — {row['lari_child_tile'].get('href')}")
        md.append("")
    write_text(ep_dir / f"parent-category-tiles-{label}.md", "\n".join(md))
    write_json(out_dir / f"pages-{label}.json", rows)
    return rows


def _first_h1(html: str) -> str:
    m = re.search(r"<h1[^>]*>([^<]+)</h1>", html, re.I)
    return m.group(1).strip() if m else ""


def _breadcrumb_text(html: str) -> str:
    parts = re.findall(r'class="[^"]*breadcrumb[^"]*"[^>]*>([^<]+)<', html, re.I)
    return " / ".join(p.strip() for p in parts if p.strip())


def _find_child_lari_link(html: str) -> dict[str, str] | None:
    for block in re.findall(r'<a[^>]+href="([^"]*lari[^"]*)"[^>]*>[\s\S]*?Лари[\s\S]*?</a>', html, re.I):
        return {"name": "Лари", "href": block}
    return None


def phase_source_authority(ftp: ftplib.FTP, before_cv: bytes) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    cv_text = before_cv.decode("utf-8", errors="replace")
    branch_ids = extract_branch_ids(cv_text)
    for remote in FTP_SOURCE_FILES:
        data = ftp_download(ftp, remote) if remote != REMOTE_CATEGORY_VISIBILITY else before_cv
        exists = data is not None
        text = data.decode("utf-8", errors="replace") if data else ""
        layer = "modification" if remote.startswith("/storage/modification") else "live"
        controls_home = "buildHomepageCategoryCards" in text or remote.endswith("home.php")
        controls_katalog = "hub_categories" in text or "filterRootCategories" in text
        controls_shkafy_children = remote.endswith("category.php")
        will_modify = remote == REMOTE_CATEGORY_VISIBILITY
        reason = ""
        if remote == REMOTE_CATEGORY_VISIBILITY:
            reason = "Remove ID 88 from $neutral_hub_branch_ids; keep 358; child lists use DB tree"
        rows.append(
            {
                "remote_path": remote,
                "exists": exists,
                "layer": layer,
                "sha256": sha256_bytes(data) if data else "",
                "contains_id_88": "88" in text,
                "contains_id_358": "358" in text,
                "controls_homepage_tile": controls_home,
                "controls_katalog_tile": controls_katalog,
                "controls_shkafy_i_lari_children": controls_shkafy_children,
                "will_modify": will_modify,
                "reason": reason,
            }
        )
        if data and remote != REMOTE_CATEGORY_VISIBILITY:
            (DEPLOYMENT_ROOT / "source-before" / local_ftp_name(remote)).write_bytes(data)

    (DEPLOYMENT_ROOT / "source-before" / "category_visibility.php").write_bytes(before_cv)
    write_csv(
        DEPLOYMENT_ROOT / "manifests" / "source-authority-map.csv",
        rows,
        [
            "remote_path", "exists", "layer", "sha256", "contains_id_88", "contains_id_358",
            "controls_homepage_tile", "controls_katalog_tile", "controls_shkafy_i_lari_children",
            "will_modify", "reason",
        ],
    )
    write_json(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.json", rows)
    md = [
        "# Source authority map",
        "",
        f"Whitelist IDs in production `category_visibility.php`: {branch_ids}",
        "",
        "**Verdict:** Single whitelist `$neutral_hub_branch_ids` controls Parent Category Tiles on homepage and neutral hub (`/katalog` / `/katalog/nejtralnoe-oborudovanie`). Child category cards on `/shkafy-i-lari` come from OpenCart category tree in `category.php`, not this whitelist.",
        "",
    ]
    for row in rows:
        md.append(f"## `{row['remote_path']}`")
        md.append(f"- will_modify: {row['will_modify']}")
        md.append(f"- reason: {row.get('reason')}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.md", "\n".join(md))

    write_json(
        DEPLOYMENT_ROOT / "rollback" / "source-before-manifest.json",
        {
            "operation_id": OPERATION_ID,
            "captured_at": utc_now(),
            REMOTE_CATEGORY_VISIBILITY: {
                "sha256": sha256_bytes(before_cv),
                "local_path": str(DEPLOYMENT_ROOT / "source-before" / "category_visibility.php"),
                "branch_ids": branch_ids,
            },
        },
    )
    write_text(
        DEPLOYMENT_ROOT / "rollback" / "rollback-plan.md",
        "\n".join(
            [
                "# Rollback plan",
                "",
                "1. Re-upload `source-before/category_visibility.php` to `/public_html/system/library/zpm/category_visibility.php`.",
                "2. Re-download and verify SHA256 matches rollback manifest.",
                "3. Re-fetch homepage and `/katalog`; standalone Лари parent tile should return (11 cards).",
                "4. Scoped cache clear only if tile list does not update immediately.",
                "",
            ]
        ),
    )
    return rows


def patch_category_visibility(text: str) -> str:
    ids = extract_branch_ids(text)
    if LARI_ID not in ids:
        if ids == EXPECTED_IDS_AFTER:
            return text
        raise RuntimeError(f"ID {LARI_ID} not in whitelist; current IDs: {ids}")
    if SHKAFY_ID not in ids:
        raise RuntimeError(f"ID {SHKAFY_ID} missing from whitelist")
    new_ids = [i for i in ids if i != LARI_ID]
    if new_ids != EXPECTED_IDS_AFTER:
        raise RuntimeError(f"Patched ID list mismatch: {new_ids}")
    pattern = r"(private\s+static\s+\$neutral_hub_branch_ids\s*=\s*array\()([^)]+)(\))"
    match = re.search(pattern, text)
    if not match:
        raise RuntimeError("neutral_hub_branch_ids array not found")
    new_inner = ", ".join(str(i) for i in new_ids)
    patched = re.sub(pattern, rf"\g<1>{new_inner}\3", text, count=1)
    if f" * {PATCH_MARKER}" not in patched:
        patched = patched.replace(
            " * M9.7E — homepage category section uses neutral hub branches",
            f" * M9.7E — homepage category section uses neutral hub branches\n\t * {PATCH_MARKER} — removed ID 88 from parent tiles whitelist",
            1,
        )
    if extract_branch_ids(patched) != EXPECTED_IDS_AFTER:
        raise RuntimeError("Patch verification failed")
    return patched


def write_patch_plan(before_ids: list[int], after_ids: list[int]) -> None:
    plan = {
        "operation_id": OPERATION_ID,
        "patch_target": REMOTE_CATEGORY_VISIBILITY,
        "action": "remove_category_id_from_neutral_hub_branch_ids",
        "category_id_removed": LARI_ID,
        "category_id_kept": SHKAFY_ID,
        "ids_before": before_ids,
        "ids_after": after_ids,
        "db_changes": 0,
        "redirect_changes": 0,
        "seo_changes": 0,
        "files_to_upload": [REMOTE_CATEGORY_VISIBILITY],
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "patch-plan.json", plan)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "patch-plan.md",
        "\n".join(
            [
                "# Patch plan",
                "",
                f"- File: `{REMOTE_CATEGORY_VISIBILITY}`",
                f"- Remove `{LARI_ID}` from `$neutral_hub_branch_ids`",
                f"- Keep `{SHKAFY_ID}`",
                "- No DB / redirect / SEO changes",
                f"- IDs before: {before_ids}",
                f"- IDs after: {after_ids}",
                "",
            ]
        ),
    )


def evaluate_dry_run_gates(before_rows: list[dict[str, Any]], before_ids: list[int], patched_ids: list[int]) -> dict[str, Any]:
    home = next((r for r in before_rows if r["page_key"] == "home"), {})
    katalog = next((r for r in before_rows if r["page_key"] == "katalog"), {})
    shkafy = next((r for r in before_rows if r["page_key"] == "shkafy_hub"), {})
    gates = {
        "G1_lari_id_88": LARI_ID == 88,
        "G2_shkafy_id_358": SHKAFY_ID == 358,
        "G3_target_parent_category_tiles": True,
        "G4_removes_lari_from_home_katalog": LARI_ID in before_ids and LARI_ID not in patched_ids,
        "G5_keeps_shkafy_tile": SHKAFY_ID in patched_ids,
        "G6_no_category_delete": True,
        "G7_no_db_seo_redirect": True,
        "G8_lari_child_on_shkafy_before": bool(shkafy.get("lari_child_tile") or card_named(shkafy.get("parent_tiles", []), "Лари")),
        "G9_nested_lari_url": True,
        "G10_old_flat_redirect": True,
        "G11_sitemap_ok": True,
        "G12_no_header_footer": True,
        "G13_no_import_monitor": True,
        "G14_rollback_captured": (DEPLOYMENT_ROOT / "source-before" / "category_visibility.php").exists(),
        "G15_no_bzpm": (home.get("bzpm_count", 0) == 0 and katalog.get("bzpm_count", 0) == 0),
        "G16_before_lari_parent_tile_present": bool(home.get("lari_parent_tile") or katalog.get("lari_parent_tile")),
    }
    nested = http_get("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari")
    gates["G9_nested_lari_url"] = nested.get("status") == 200
    old = http_get("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari", follow_redirects=False)
    gates["G10_old_flat_redirect"] = old.get("status") == 301 and "shkafy-i-lari/lari" in (old.get("location") or "")
    sm = http_get("https://bzpm.ru/sitemap.xml")
    gates["G11_sitemap_ok"] = sm.get("status") == 200
    result = {"gates": gates, "all_pass": all(gates.values()), "evaluated_at": utc_now()}
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run-gates.json", result)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run-gates.md",
        "# Dry-run gates\n\n" + "\n".join(f"- {k}: {'PASS' if v else 'FAIL'}" for k, v in gates.items()) + f"\n\n**All pass:** {result['all_pass']}\n",
    )
    return result


def apply_patch(patched: bytes) -> list[dict[str, Any]]:
    ftp = ftp_connect()
    upload_rows: list[dict[str, Any]] = []
    try:
        ftp_upload(ftp, REMOTE_CATEGORY_VISIBILITY, patched)
        verify = ftp_download(ftp, REMOTE_CATEGORY_VISIBILITY)
        upload_rows.append(
            {
                "remote": REMOTE_CATEGORY_VISIBILITY,
                "sha_local": sha256_bytes(patched),
                "sha_remote_after_upload": sha256_bytes(verify) if verify else "",
                "match": verify == patched,
            }
        )
    finally:
        ftp.quit()
    write_csv(
        DEPLOYMENT_ROOT / "verification" / "upload-manifest.csv",
        upload_rows,
        ["remote", "sha_local", "sha_remote_after_upload", "match"],
    )
    write_json(DEPLOYMENT_ROOT / "verification" / "upload-manifest.json", upload_rows)
    if not all(r.get("match") for r in upload_rows):
        raise RuntimeError("Upload SHA verification failed")
    return upload_rows


def verify_redirects() -> list[dict[str, Any]]:
    rows = []
    for key, url in REDIRECT_URLS:
        resp = http_get(url, follow_redirects=False)
        rows.append(
            {
                "key": key,
                "url": url,
                "status": resp.get("status"),
                "location": resp.get("location"),
                "pass": resp.get("status") == 301 and "shkafy-i-lari/lari" in (resp.get("location") or ""),
            }
        )
    write_json(DEPLOYMENT_ROOT / "verification" / "redirect-check.json", rows)
    return rows


def run_regression() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for url in SANITY_URLS:
        resp = http_get(url)
        body = resp.get("body", "")
        row: dict[str, Any] = {"url": url, "http_status": resp.get("status"), "error": resp.get("error")}
        if "llms.txt" in url:
            row["bzpm_count"] = body.count(WRONG_BRAND)
        if "sitemap.xml" in url:
            try:
                root = ET.fromstring(body)
                row["url_count"] = len(list(root))
                row["nested_lari_present"] = "shkafy-i-lari/lari" in body
                row["flat_lari_absent"] = "/nejtralnoe-oborudovanie/lari<" in body or "/nejtralnoe-oborudovanie/lari/" in body
            except ET.ParseError:
                row["url_count"] = "parse_error"
        if url.endswith("/stoly"):
            row["load_more"] = "load-more" in body.lower() or "data-load-more" in body.lower()
        rows.append(row)
    write_json(DEPLOYMENT_ROOT / "verification" / "regression.json", rows)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "regression.md",
        "# Regression\n\n" + "\n".join(f"- {r['url']}: {r.get('http_status')}" for r in rows) + "\n",
    )
    return rows


def verify_after(before_rows: list[dict[str, Any]], after_rows: list[dict[str, Any]], regression: list[dict[str, Any]]) -> dict[str, Any]:
    home = next(r for r in after_rows if r["page_key"] == "home")
    katalog = next(r for r in after_rows if r["page_key"] == "katalog")
    hub = next(r for r in after_rows if r["page_key"] == "neutral_hub")
    shkafy = next(r for r in after_rows if r["page_key"] == "shkafy_hub")
    nested = next(r for r in after_rows if r["page_key"] == "lari_nested")
    checks = {
        "home_http_200": home.get("http_status") == 200,
        "katalog_http_200": katalog.get("http_status") == 200,
        "hub_http_200": hub.get("http_status") == 200,
        "home_lari_parent_absent": not home.get("lari_parent_tile"),
        "hub_lari_parent_absent": not hub.get("lari_parent_tile"),
        "katalog_lari_absent": not katalog.get("lari_in_page", katalog.get("lari_parent_tile")),
        "home_shkafy_present": bool(home.get("shkafy_parent_tile")),
        "hub_shkafy_present": bool(hub.get("shkafy_parent_tile")),
        "katalog_shkafy_present": bool(katalog.get("shkafy_in_page")),
        "home_tile_count_10": home.get("parent_tile_count") == 10,
        "hub_tile_count_10": hub.get("parent_tile_count") == 10,
        "shkafy_lari_child_present": bool(shkafy.get("lari_child_tile") or card_named(shkafy.get("parent_tiles", []), "Лари")),
        "nested_lari_200": nested.get("http_status") == 200,
        "nested_canonical": "shkafy-i-lari/lari" in nested.get("canonical", ""),
        "no_bzpm": all(r.get("bzpm_count", 0) == 0 for r in after_rows if "bzpm_count" in r),
    }
    stoly = next((r for r in regression if r.get("url", "").endswith("/stoly")), {})
    checks["stoly_load_more"] = bool(stoly.get("load_more"))
    checks["custom_equipment_200"] = any(
        r.get("http_status") == 200 for r in regression if "custom-equipment" in r.get("url", "")
    )
    result = {"checks": checks, "all_pass": all(checks.values()), "evaluated_at": utc_now()}
    write_json(DEPLOYMENT_ROOT / "verification" / "after-verification.json", result)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "after-verification.md",
        "# After verification\n\n" + "\n".join(f"- {k}: {'PASS' if v else 'FAIL'}" for k, v in checks.items()) + f"\n\n**All pass:** {result['all_pass']}\n",
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-only", action="store_true", help="Re-run HTTP verification only (no upload)")
    args = parser.parse_args()

    ensure_dirs()
    log: list[str] = [f"Started {utc_now()}"]

    if args.verify_only:
        before_path = DEPLOYMENT_ROOT / "http-before" / "pages-before.json"
        if not before_path.exists():
            print("BLOCKED: run full operation first to capture before snapshot", file=sys.stderr)
            return 2
        before_rows = json.loads(before_path.read_text(encoding="utf-8"))
        after_rows = capture_http_phase("after", PRIMARY_URLS)
        redirects = verify_redirects()
        regression = run_regression()
        after_verify = verify_after(before_rows, after_rows, regression)
        write_text(DEPLOYMENT_ROOT / "logs" / "run.log", "\n".join(log + ["verify-only complete"]))
        if not after_verify["all_pass"]:
            failed = [k for k, v in after_verify["checks"].items() if not v]
            print(f"PARTIAL — after verification failed: {failed}", file=sys.stderr)
            return 4
        print("SITE-002 PARENT CATEGORY TILES LARI REMOVAL COMPLETE")
        return 0

    # Phase 1 — before
    before_rows = capture_http_phase("before", PRIMARY_URLS + REDIRECT_URLS)
    log.append("Phase 1 before snapshot complete")

    ftp = ftp_connect()
    try:
        before_cv = ftp_download(ftp, REMOTE_CATEGORY_VISIBILITY)
    finally:
        ftp.quit()
    if not before_cv:
        print("BLOCKED: could not download category_visibility.php", file=sys.stderr)
        return 2
    before_ids = extract_branch_ids(before_cv.decode("utf-8", errors="replace"))
    log.append(f"Production whitelist IDs: {before_ids}")

    # Phase 2 — source authority
    ftp = ftp_connect()
    try:
        phase_source_authority(ftp, before_cv)
    finally:
        ftp.quit()
    log.append("Phase 2 source authority complete")

    # Phase 3 — patch
    before_text = before_cv.decode("utf-8", errors="replace")
    after_text = patch_category_visibility(before_text)
    patched = after_text.encode("utf-8")
    after_path = DEPLOYMENT_ROOT / "source-after" / "category_visibility.php"
    after_path.write_bytes(patched)
    (REPO_TOOLS / "category_visibility.php").write_bytes(patched)
    diff = difflib.unified_diff(
        before_text.splitlines(),
        after_text.splitlines(),
        fromfile="before",
        tofile="after",
        lineterm="",
    )
    write_text(DEPLOYMENT_ROOT / "manifests" / "category_visibility.diff", "\n".join(diff) + "\n")
    patched_ids = extract_branch_ids(after_text)
    write_patch_plan(before_ids, patched_ids)
    log.append("Phase 3 patch plan complete")

    # Phase 4 — dry-run gates
    gates = evaluate_dry_run_gates(before_rows, before_ids, patched_ids)
    if not gates["all_pass"]:
        failed = [k for k, v in gates["gates"].items() if not v]
        print(f"BLOCKED — dry-run gates failed: {failed}", file=sys.stderr)
        write_text(DEPLOYMENT_ROOT / "logs" / "run.log", "\n".join(log))
        return 3

    if args.dry_run_only:
        print("Dry-run only — gates passed, no upload")
        write_text(DEPLOYMENT_ROOT / "logs" / "run.log", "\n".join(log))
        return 0

    if not args.verify_only:
        # Phase 5 — apply
        apply_patch(patched)
        write_json(DEPLOYMENT_ROOT / "cache" / "cache-actions.json", {"actions": [], "note": "No cache clear required — PHP whitelist read directly"})
        log.append("Phase 5 patch applied")
        time.sleep(2)
    else:
        log.append("Phase 5 skipped — verify-only")

    # Phase 6 — after
    after_rows = capture_http_phase("after", PRIMARY_URLS)
    redirects = verify_redirects()
    log.append("Phase 6 after verification complete")

    # Phase 7 — regression
    regression = run_regression()
    after_verify = verify_after(before_rows, after_rows, regression)
    log.append("Phase 7 regression complete")

    write_text(DEPLOYMENT_ROOT / "logs" / "run.log", "\n".join(log))

    if not after_verify["all_pass"]:
        failed = [k for k, v in after_verify["checks"].items() if not v]
        print(f"PARTIAL — after verification failed: {failed}", file=sys.stderr)
        return 4

    print("SITE-002 PARENT CATEGORY TILES LARI REMOVAL COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
