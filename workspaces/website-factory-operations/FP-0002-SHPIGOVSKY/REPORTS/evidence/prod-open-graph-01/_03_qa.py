# -*- coding: utf-8 -*-
"""Post-deploy Open Graph QA matrix."""
from __future__ import annotations

import html as html_lib
import json
import re
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent
URLS = [
    ("homepage", "https://shpigovsky.ru/"),
    ("contacts", "https://shpigovsky.ru/kontakty/"),
    ("services_hub", "https://shpigovsky.ru/uslugi/"),
    ("service_single", "https://shpigovsky.ru/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/"),
    ("specialists_hub", "https://shpigovsky.ru/specialisty/"),
    ("specialist_single", "https://shpigovsky.ru/specialisty/shpigovsky/"),
    ("article", "https://shpigovsky.ru/blog/nazvanie-stati/"),
    ("about", "https://shpigovsky.ru/o-centre/o-nas/"),
    ("reviews", "https://shpigovsky.ru/otzyvy/"),
    ("legal", "https://shpigovsky.ru/privacy-policy/"),
    ("generic_institutional", "https://shpigovsky.ru/o-centre/programma-lecheniya/"),
    ("deprecated_redirect", "https://shpigovsky.ru/specyalisty/"),
]


def meta_content(html: str, prop: str) -> list[str]:
    pattern = rf'<meta property="{re.escape(prop)}" content="([^"]*)"'
    return re.findall(pattern, html, flags=re.I)


def decode_vals(values: list[str]) -> list[str]:
    return [html_lib.unescape(v) for v in values]


matrix = []
for label, url in URLS:
    req = urllib.request.Request(url, headers={"User-Agent": "FP02-og-qa/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = resp.status
            html = resp.read().decode("utf-8", "replace")
            final = resp.geturl()
    except Exception as exc:
        matrix.append({"label": label, "url": url, "error": str(exc), "result": "FAIL"})
        continue

    og_title = decode_vals(meta_content(html, "og:title"))
    og_desc = decode_vals(meta_content(html, "og:description"))
    og_url = decode_vals(meta_content(html, "og:url"))
    og_type = decode_vals(meta_content(html, "og:type"))
    og_image = decode_vals(meta_content(html, "og:image"))
    og_site = decode_vals(meta_content(html, "og:site_name"))

    dup_ok = all(
        len(v) <= 1
        for v in (og_title, og_desc, og_url, og_type, og_image, og_site)
    )
    jsonld_count = len(re.findall(r"application/ld\+json", html))
    specyalisty_in_og = any("specyalisty" in u for u in og_url)

    result = "PASS"
    if label == "deprecated_redirect":
        result = "PASS" if specyalisty_in_og is False else "FAIL"
    elif status != 200 or not dup_ok or not og_title or not og_url or not og_type:
        result = "FAIL"
    elif label == "article" and (not og_type or og_type[0] != "article"):
        result = "FAIL"
    elif label != "article" and label != "deprecated_redirect" and og_type and og_type[0] != "website":
        result = "FAIL"

    entry = {
        "label": label,
        "url": url,
        "status": status,
        "final_url": final,
        "og:title": og_title[0] if og_title else "",
        "og:description": og_desc[0] if og_desc else "",
        "og:url": og_url[0] if og_url else "",
        "og:type": og_type[0] if og_type else "",
        "og:image": og_image[0] if og_image else "",
        "og:site_name": og_site[0] if og_site else "",
        "duplicate_counts": {
            "og:title": len(og_title),
            "og:description": len(og_desc),
            "og:url": len(og_url),
            "og:type": len(og_type),
            "og:image": len(og_image),
        },
        "jsonld_count": jsonld_count,
        "specyalisty_in_og_url": specyalisty_in_og,
        "result": result,
    }
    matrix.append(entry)

(OUT / "05-qa-matrix.json").write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
for e in matrix:
    print(
        f"{e.get('label')}: {e.get('result')} type={e.get('og:type')} "
        f"title={str(e.get('og:title',''))[:60]} image={'yes' if e.get('og:image') else 'no'} "
        f"jsonld={e.get('jsonld_count')} dups={e.get('duplicate_counts')}"
    )
