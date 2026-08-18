# -*- coding: utf-8 -*-
"""Compare robots on public A vs Beget WP IP with Host header."""
from __future__ import annotations
import json
from pathlib import Path
import requests

EV = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p18b-dashboard-indexing")
UA = "FP-0002-P18B-robots-ip/1.0"

targets = [
    ("https://shpigovsky.ru/robots.txt", None),
    ("https://shpigovsky.ru/robots.txt?nocache=1", None),
    ("http://45.130.41.70/robots.txt", {"Host": "shpigovsky.ru"}),
    ("https://45.130.41.70/robots.txt", {"Host": "shpigovsky.ru"}),
    ("http://91.106.207.76/robots.txt", {"Host": "shpigovsky.ru"}),
    ("http://91.106.207.76/robots.txt", {"Host": "shpigovsky.beget.tech"}),
    ("https://shpigovsky.ru/", None),
]

rows = []
for url, extra in targets:
    headers = {"User-Agent": UA}
    if extra:
        headers.update(extra)
    try:
        r = requests.get(url, timeout=20, allow_redirects=False, headers=headers, verify=False)
        body = r.content or b""
        rows.append({
            "url": url,
            "extra_host": None if not extra else extra.get("Host"),
            "status": r.status_code,
            "server": r.headers.get("Server"),
            "ctype": r.headers.get("Content-Type"),
            "location": r.headers.get("Location"),
            "bytes": len(body),
            "hex_head": body[:24].hex(),
            "text_head": body[:180].decode("utf-8", "replace"),
            "has_wp": b"wp-content" in body or b"WordPress" in body,
            "robots_meta": None,
        })
    except Exception as e:
        rows.append({"url": url, "extra_host": extra, "error": str(e)})

(EV / "ROBOTS-BY-IP.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(rows, indent=2, ensure_ascii=False))
