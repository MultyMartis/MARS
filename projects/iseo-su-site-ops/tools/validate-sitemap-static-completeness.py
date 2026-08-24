#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate static sitemap completeness against canonical public route inventory.

Acceptance criterion (after approved exclusions):
  PUBLIC_CANONICAL_STATIC_ROUTES - SITEMAP_STATIC_URLS = 0

Also cross-checks the generated XML and optionally the live tech-SEO inventory
for unexpected public marketing HTML still absent from the allowlist.

Usage:
  python projects/iseo-su-site-ops/tools/validate-sitemap-static-completeness.py
"""
from __future__ import annotations

import csv
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST = ROOT / "data" / "sitemaps" / "sitemap-static-urls-v1.txt"
INVENTORY = ROOT / "data" / "sitemaps" / "public-canonical-static-routes-v1.txt"
SITEMAP = ROOT / "production-source" / "sitemaps" / "sitemap-static.xml"
TECH_INV = ROOT / "audits" / "tech-seo" / "ISEO-SU-TECH-SEO-URL-INVENTORY-v1.csv"
CANON_PREFIX = "https://i-seo.su/"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

# Routes that may appear as public HTML but are intentionally NOT in static sitemap.
APPROVED_EXCLUSIONS_PREFIXES = (
    "https://i-seo.su/blog",
    "https://i-seo.su/report-hub/",
)
APPROVED_EXCLUSION_EXACT = {
    "https://i-seo.su/home.html",
    "https://i-seo.su/blog.html",
}


def load_url_file(path: Path) -> set[str]:
    urls: set[str] = set()
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        urls.add(line.rstrip("/"))
    return urls


def load_sitemap_locs(path: Path) -> list[str]:
    tree = ET.parse(path)
    root = tree.getroot()
    locs = [el.text.strip().rstrip("/") for el in root.findall("sm:url/sm:loc", NS) if el.text]
    return locs


def is_approved_exclusion(url: str) -> bool:
    if url in APPROVED_EXCLUSION_EXACT:
        return True
    return any(url == p or url.startswith(p) for p in APPROVED_EXCLUSIONS_PREFIXES)


def main() -> int:
    allow = load_url_file(ALLOWLIST)
    inventory = load_url_file(INVENTORY)
    locs = load_sitemap_locs(SITEMAP)
    loc_set = set(locs)

    errors: list[str] = []

    if len(locs) != len(loc_set):
        errors.append(f"duplicate sitemap locs: {len(locs) - len(loc_set)}")
    if loc_set != allow:
        errors.append("sitemap XML locs != allowlist")
    if allow != inventory:
        missing = sorted(inventory - allow)
        extra = sorted(allow - inventory)
        errors.append(
            f"allowlist != inventory (missing={len(missing)} extra={len(extra)})"
        )
        for u in missing[:10]:
            errors.append(f"  missing: {u}")
        for u in extra[:10]:
            errors.append(f"  extra: {u}")

    for u in locs:
        if not u.startswith(CANON_PREFIX):
            errors.append(f"non-canonical: {u}")
        if not u.startswith("https://"):
            errors.append(f"non-https: {u}")

    # Broader reconciliation vs tech SEO inventory (HTML only).
    unexpected_gaps: list[str] = []
    if TECH_INV.is_file():
        with TECH_INV.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                url = (row.get("url") or "").split("?", 1)[0].rstrip("/")
                if not url.startswith(CANON_PREFIX):
                    continue
                if not re.search(r"\.html$", url):
                    continue
                status = (row.get("http_status") or "").strip()
                indexable = (row.get("indexable") or "").strip().lower()
                robots = (row.get("robots") or "").lower()
                if status != "200":
                    continue
                if indexable in ("false", "0", "no"):
                    continue
                if "noindex" in robots:
                    continue
                if url in allow or is_approved_exclusion(url):
                    continue
                # WP soft paths without .html already filtered; keep marketing HTML gaps
                unexpected_gaps.append(url)

    print(f"ALLOWLIST_COUNT={len(allow)}")
    print(f"INVENTORY_COUNT={len(inventory)}")
    print(f"SITEMAP_LOC_COUNT={len(locs)}")
    print(f"PUBLIC_CANONICAL_STATIC_ROUTES - SITEMAP_STATIC_URLS = {len(inventory - loc_set)}")
    print(f"TECH_SEO_UNEXPECTED_STATIC_GAPS={len(unexpected_gaps)}")
    for u in unexpected_gaps[:30]:
        print(f"  gap: {u}")

    if unexpected_gaps:
        errors.append(
            f"tech-seo inventory still has {len(unexpected_gaps)} "
            "indexable static HTML URLs outside allowlist/exclusions"
        )

    if errors:
        print("FAIL")
        for e in errors:
            print(e)
        return 1

    print("PASS — completeness reconciled")
    return 0


if __name__ == "__main__":
    sys.exit(main())
