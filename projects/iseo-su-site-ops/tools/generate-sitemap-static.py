#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate sitemap-static.xml from the project allowlist.

Usage (from repo root or any cwd):
  python projects/iseo-su-site-ops/tools/generate-sitemap-static.py

Reads:
  projects/iseo-su-site-ops/data/sitemaps/sitemap-static-urls-v1.txt

Writes:
  projects/iseo-su-site-ops/production-source/sitemaps/sitemap-static.xml

Rules:
  - only HTTPS https://i-seo.su/... URLs from the allowlist
  - deterministic sorted order
  - no invented lastmod / changefreq / priority
  - excludes handlers / admin / non-public surfaces by allowlist discipline
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST = ROOT / "data" / "sitemaps" / "sitemap-static-urls-v1.txt"
OUT = ROOT / "production-source" / "sitemaps" / "sitemap-static.xml"
CANON_PREFIX = "https://i-seo.su/"


def load_urls() -> list[str]:
    urls: list[str] = []
    for raw in ALLOWLIST.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if not line.startswith(CANON_PREFIX):
            raise SystemExit(f"non-canonical URL rejected: {line}")
        if any(
            bad in line.lower()
            for bad in ("__form", "form.php", "wp-admin", "wp-login", ".bak", "test.html")
        ):
            raise SystemExit(f"excluded pattern rejected: {line}")
        urls.append(line.rstrip("/"))
    # normalize homepage if present as trailing-only
    urls = sorted(set(urls))
    return urls


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
    urls = load_urls()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(urls), encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({len(urls)} urls)")


if __name__ == "__main__":
    main()
