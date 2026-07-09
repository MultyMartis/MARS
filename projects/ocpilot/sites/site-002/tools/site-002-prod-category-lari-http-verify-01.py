#!/usr/bin/env python3
"""Full HTTP verification for lari reparent implementation."""
from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

DEPLOY = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01"
)

URLS = {
    "lari_new": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari",
    "lari_old": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari",
    "sklad_new": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/skladskie-lari",
    "sklad_old": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari/skladskie-lari",
    "proizv_new": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/proizvodstvennye-lari",
    "proizv_old": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari/proizvodstvennye-lari",
    "shkafy_hub": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari",
    "neutral_hub": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
    "home": "https://bzpm.ru/",
    "katalog": "https://bzpm.ru/katalog",
    "stoly": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "sitemap": "https://bzpm.ru/sitemap.xml",
    "robots": "https://bzpm.ru/robots.txt",
    "llms": "https://bzpm.ru/llms.txt",
}


def curl_head(url: str) -> dict:
    r = subprocess.run(
        ["curl", "-sI", "-H", "Cache-Control: no-cache", url],
        capture_output=True,
        text=True,
        timeout=60,
    )
    out = {"url": url, "status": "", "location": ""}
    for ln in r.stdout.splitlines():
        if ln.startswith("HTTP/"):
            out["status"] = ln.strip()
        if ln.lower().startswith("location:"):
            out["location"] = ln.split(":", 1)[1].strip()
    return out


def curl_body(url: str) -> str:
    r = subprocess.run(
        ["curl", "-sL", "-H", "Cache-Control: no-cache", url],
        capture_output=True,
        timeout=90,
    )
    return r.stdout.decode("utf-8", "replace")


def extract(html: str) -> dict:
    canonical = ""
    h1 = ""
    bc = []
    m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)', html, re.I)
    if m:
        canonical = m.group(1)
    m = re.search(r"<h1[^>]*>([^<]+)</h1>", html, re.I)
    if m:
        h1 = re.sub(r"\s+", " ", m.group(1)).strip()
    for m in re.finditer(r'class="[^"]*breadcrumb[^"]*"[^>]*>([^<]+)<', html, re.I):
        bc.append(m.group(1).strip())
    if not bc:
        for m in re.finditer(r'itemprop="name"[^>]*>([^<]+)<', html):
            bc.append(m.group(1).strip())
    bzpm = bool(re.search(r"БЗПМ", html))
    return {"canonical": canonical, "h1": h1, "breadcrumbs": bc, "bzpm": bzpm}


def main() -> None:
    heads = {k: curl_head(v) for k, v in URLS.items()}
    lari_html = curl_body(URLS["lari_new"])
    lari_meta = extract(lari_html)
    home_html = curl_body(URLS["home"])
    sitemap = curl_body(URLS["sitemap"])

    lari_hrefs = re.findall(r'href="([^"]*lari[^"]*)"', home_html, re.I)
    sitemap_has_new = "/shkafy-i-lari/lari" in sitemap
    sitemap_has_old_flat = "nejtralnoe-oborudovanie/lari</loc>" in sitemap and "shkafy-i-lari/lari" not in sitemap.split("nejtralnoe-oborudovanie/lari")[0][-50:]

    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "heads": heads,
        "lari_page": lari_meta,
        "home_lari_hrefs": lari_hrefs[:10],
        "sitemap_has_nested_lari": sitemap_has_new,
        "sitemap_sample_lari": [ln for ln in sitemap.splitlines() if "lari" in ln.lower()][:8],
        "regression_stoly_load_more": "load-more" in curl_body(URLS["stoly"]).lower() or "loadmore" in curl_body(URLS["stoly"]).lower(),
    }
    (DEPLOY / "http-after" / "http-verification.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
