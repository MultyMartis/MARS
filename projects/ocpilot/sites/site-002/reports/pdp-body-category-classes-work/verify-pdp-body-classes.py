#!/usr/bin/env python3
"""Verify PDP body category classes on TEST."""
from __future__ import annotations

import json
import re
import ssl
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://zpm.new-site.space"
WORK = Path(__file__).resolve().parent

PRODUCT_URLS = [
    {
        "label": "moechnye-vanny (neutral)",
        "url": f"{BASE}/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-celnotyanutye-premium-3/vanna-moechnaya-vmc-p3-2-500-1150h700h850",
    },
    {
        "label": "stoly-premium (neutral)",
        "url": f"{BASE}/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850",
    },
]

PLP_FOR_PRODUCT = [
    {
        "label": "teplovoe root",
        "plp": f"{BASE}/katalog/teplovoe-oborudovanie",
        "prefix": f"{BASE}/katalog/teplovoe-oborudovanie/",
    },
]


def fetch(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "SITE-002-verify/1.0"})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
        return resp.status, resp.read().decode("utf-8", errors="replace")


def scan(html: str) -> dict:
    body = re.search(r'<body[^>]*class="([^"]*)"', html, re.I)
    cls = body.group(1) if body else ""
    return {
        "body_class": cls,
        "has_page_product": "page--product" in cls,
        "category_root": re.search(r"\bcategory-root-(\d+)\b", cls).group(1) if re.search(r"\bcategory-root-(\d+)\b", cls) else None,
        "category_parent": re.search(r"\bcategory-parent-(\d+)\b", cls).group(1) if re.search(r"\bcategory-parent-(\d+)\b", cls) else None,
        "php_error": bool(re.search(r"(?i)(PHP Warning|PHP Notice|Fatal error|Parse error)", html)),
    }


def main() -> None:
    results = {"timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "samples": []}
    for item in PRODUCT_URLS:
        status, html = fetch(item["url"])
        results["samples"].append({"label": item["label"], "url": item["url"], "status": status, **scan(html)})

    for plp in PLP_FOR_PRODUCT:
        _, html = fetch(plp["plp"])
        for m in re.finditer(r'href="(' + re.escape(plp["prefix"]) + r'[^"]+)"', html):
            candidate = m.group(1)
            if candidate.count("/") >= plp["prefix"].count("/") + 2:
                status, phtml = fetch(candidate)
                if "page--product" in (re.search(r'<body[^>]*class="([^"]*)"', phtml, re.I).group(1) if re.search(r'<body[^>]*class="([^"]*)"', phtml, re.I) else ""):
                    results["samples"].append({"label": plp["label"], "url": candidate, "status": status, **scan(phtml)})
                    break

    out = WORK / "verify-result.json"
    out.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
