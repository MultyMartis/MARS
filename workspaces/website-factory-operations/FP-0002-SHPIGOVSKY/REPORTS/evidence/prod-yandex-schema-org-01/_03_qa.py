# -*- coding: utf-8 -*-
"""Post-deploy JSON-LD QA matrix for schema.org wave."""
from __future__ import annotations

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
matrix = []
for label, url in URLS:
    req = urllib.request.Request(url, headers={"User-Agent": "FP02-schema-qa/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = resp.status
            html = resp.read().decode("utf-8", "replace")
            final = resp.geturl()
    except Exception as exc:
        matrix.append({"label": label, "url": url, "error": str(exc)})
        continue
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
    entry = {
        "label": label,
        "url": url,
        "status": status,
        "final_url": final,
        "jsonld_count": len(re.findall(r"application/ld\+json", html)),
        "og_count": len(re.findall(r'property="og:', html)),
        "specyalisty_in_jsonld": False,
        "parse_ok": False,
        "types": [],
        "webpage_type": None,
        "breadcrumb": False,
        "graph_size": 0,
    }
    if m:
        raw = m.group(1)
        try:
            data = json.loads(raw)
            entry["parse_ok"] = True
            graph = data.get("@graph", [])
            entry["graph_size"] = len(graph)
            types = []
            for node in graph:
                t = node.get("@type")
                if isinstance(t, list):
                    types.extend(t)
                elif t:
                    types.append(t)
                if node.get("@type") == "BreadcrumbList":
                    entry["breadcrumb"] = True
                if isinstance(t, str) and t.endswith("Page"):
                    entry["webpage_type"] = t
            entry["types"] = sorted(set(types))
            if "specyalisty" in raw:
                entry["specyalisty_in_jsonld"] = True
            (OUT / f"05-jsonld-{label}.json").write_text(
                json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
            )
        except Exception as exc:
            entry["parse_error"] = str(exc)
    matrix.append(entry)

(OUT / "05-qa-matrix.json").write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
for e in matrix:
    print(
        f"{e.get('label')}: status={e.get('status')} parse={e.get('parse_ok')} "
        f"webpage={e.get('webpage_type')} types={','.join(e.get('types', []))} "
        f"breadcrumb={e.get('breadcrumb')} specyalisty={e.get('specyalisty_in_jsonld')}"
    )
