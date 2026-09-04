#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add WAVE 04 niche URLs to both sitemap inventories (preserve header comments)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(r"X:\AI MARS\projects\iseo-su-site-ops\data\sitemaps")
NEW = [
    "https://i-seo.su/services/seo/prodvizhenie-sajta-pitomnika.html",
    "https://i-seo.su/services/seo/prodvizhenie-sajta-smi.html",
    "https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html",
    "https://i-seo.su/services/seo/prodvizhenie-internet-magazina-zapchastej.html",
    "https://i-seo.su/services/seo/prodvizhenie-sajta-internet-provajdera.html",
    "https://i-seo.su/services/seo/prodvizhenie-internet-magazina-kosmetiki.html",
    "https://i-seo.su/services/seo/prodvizhenie-internet-magazina-czvetov.html",
]


def update(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    header: list[str] = []
    urls: list[str] = []
    for line in lines:
        s = line.strip()
        if not s:
            if not urls:
                header.append(line)
            continue
        if s.startswith("#"):
            if not urls:
                header.append(line)
            continue
        urls.append(s.rstrip("/"))
    before = len(set(urls))
    for u in NEW:
        if u not in urls:
            urls.append(u)
    urls = sorted(set(urls))
    out = header[:]
    if out and out[-1].strip() != "":
        out.append("")
    out.extend(urls)
    out.append("")
    path.write_text("\n".join(out), encoding="utf-8", newline="\n")
    return {"path": str(path), "before": before, "after": len(urls)}


def main() -> None:
    for name in ("sitemap-static-urls-v1.txt", "public-canonical-static-routes-v1.txt"):
        r = update(ROOT / name)
        print(r["path"], "before", r["before"], "after", r["after"])


if __name__ == "__main__":
    main()
