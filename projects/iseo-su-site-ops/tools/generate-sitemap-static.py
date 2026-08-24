#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate sitemap-static.xml from the project allowlist.

Usage (from repo root or any cwd):
  python projects/iseo-su-site-ops/tools/generate-sitemap-static.py

Reads:
  projects/iseo-su-site-ops/data/sitemaps/sitemap-static-urls-v1.txt
  projects/iseo-su-site-ops/data/sitemaps/public-canonical-static-routes-v1.txt

Writes:
  projects/iseo-su-site-ops/production-source/sitemaps/sitemap-static.xml

Rules:
  - only HTTPS https://i-seo.su/... URLs from the allowlist
  - deterministic sorted order
  - no invented lastmod / changefreq / priority
  - excludes handlers / admin / non-public surfaces by allowlist discipline
  - completeness: allowlist MUST equal public-canonical-static-routes inventory
    (PUBLIC_CANONICAL_STATIC_ROUTES - SITEMAP_STATIC_URLS = 0)

Deny-safe note:
  Do not replace this allowlist with uncontrolled filesystem crawling.
  Disk HTML may include handlers twins, tests, backups, legacy parallels.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST = ROOT / "data" / "sitemaps" / "sitemap-static-urls-v1.txt"
INVENTORY = ROOT / "data" / "sitemaps" / "public-canonical-static-routes-v1.txt"
OUT = ROOT / "production-source" / "sitemaps" / "sitemap-static.xml"
CANON_PREFIX = "https://i-seo.su/"

EXCLUDE_SUBSTRINGS = (
    "__form",
    "form.php",
    "wp-admin",
    "wp-login",
    ".bak",
    "test.html",
    "report-hub",
    "/blog/",
    "blog.html",
    "metrika",
    "wp-sitemap",
    "sitemap.xml",
    "sitemap-static",
)


def load_url_file(path: Path) -> list[str]:
    urls: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if not line.startswith(CANON_PREFIX):
            raise SystemExit(f"non-canonical URL rejected in {path.name}: {line}")
        low = line.lower()
        if any(bad in low for bad in EXCLUDE_SUBSTRINGS):
            raise SystemExit(f"excluded pattern rejected in {path.name}: {line}")
        urls.append(line.rstrip("/"))
    return sorted(set(urls))


def assert_completeness(allowlist: list[str], inventory: list[str]) -> None:
    a = set(allowlist)
    i = set(inventory)
    missing_from_sitemap = sorted(i - a)
    extra_in_sitemap = sorted(a - i)
    if missing_from_sitemap or extra_in_sitemap:
        msg = [
            "COMPLETENESS FAILURE: PUBLIC_CANONICAL_STATIC_ROUTES - SITEMAP_STATIC_URLS != 0",
            f"  inventory={len(i)} allowlist={len(a)}",
            f"  missing_from_allowlist={len(missing_from_sitemap)}",
            f"  extra_in_allowlist={len(extra_in_sitemap)}",
        ]
        for u in missing_from_sitemap[:20]:
            msg.append(f"  - missing: {u}")
        for u in extra_in_sitemap[:20]:
            msg.append(f"  - extra: {u}")
        raise SystemExit("\n".join(msg))


def render(urls: list[str]) -> str:
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url in urls:
        parts.append("  <url>")
        parts.append(f"    <loc>{url}</loc>")
        parts.append("  </url>")
    parts.append("</urlset>")
    parts.append("")
    return "\n".join(parts)


def main() -> None:
    urls = load_url_file(ALLOWLIST)
    inventory = load_url_file(INVENTORY)
    assert_completeness(urls, inventory)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(urls), encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({len(urls)} urls)")
    print("completeness: PUBLIC_CANONICAL_STATIC_ROUTES - SITEMAP_STATIC_URLS = 0")


if __name__ == "__main__":
    main()
