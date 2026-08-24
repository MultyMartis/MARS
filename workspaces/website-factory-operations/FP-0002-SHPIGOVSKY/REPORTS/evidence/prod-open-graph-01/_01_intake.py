# -*- coding: utf-8 -*-
"""Fresh production intake before Open Graph deploy."""
from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent
URLS = [
    "https://shpigovsky.ru/",
    "https://shpigovsky.ru/robots.txt",
]


def fetch(url: str) -> tuple[int, str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "FP02-og-intake/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.status, resp.geturl(), resp.read().decode("utf-8", "replace")


def og_meta(html: str) -> dict[str, int]:
    props = re.findall(r'property="(og:[^"]+)"', html)
    counts: dict[str, int] = {}
    for p in props:
        counts[p] = counts.get(p, 0) + 1
    return counts


def main() -> None:
    intake: dict = {"urls": []}
    for url in URLS:
        status, final, body = fetch(url)
        entry = {
            "url": url,
            "status": status,
            "final_url": final,
            "bytes": len(body),
        }
        if url.endswith("robots.txt"):
            entry["robots_sha256_hint"] = __import__("hashlib").sha256(body.encode("utf-8")).hexdigest()
            entry["robots_preview"] = body[:500]
        else:
            entry["title"] = (re.search(r"<title>([^<]*)</title>", body, re.I) or [None, ""])[1]
            entry["meta_description"] = (
                re.search(r'<meta name="description" content="([^"]*)"', body, re.I) or [None, ""]
            )[1]
            entry["jsonld_count"] = len(re.findall(r"application/ld\+json", body))
            entry["og_property_counts"] = og_meta(body)
            entry["og_total"] = sum(entry["og_property_counts"].values())
        intake["urls"].append(entry)

    OUT.joinpath("01-intake.json").write_text(json.dumps(intake, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(intake, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
