#!/usr/bin/env python3
"""FP-0002 V8 retired architecture names audit."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
AUDIT = ROOT / "audits" / "consolidation-checkpoint" / "data"

RETIRED = [
    "page-uslugi-v2__upper-nav",
    "page-service-subdivision-v1__upper-nav",
    "page-service-leaf-v1__upper-nav",
    "home-founder-quote",
    "home-specialists",
    "home-comfort",
    "home-reviews",
    "home-faq",
    "home-final-form",
]

ALLOWED_ASSET_SUBSTRINGS = {
    "home-specialists": ["img/content/home-specialists/"],
    "home-comfort": ["img/content/home-comfort/"],
    "home-final-form": ["img/content/home-final-form/"],
}


def is_allowed_line(line: str, retired: str) -> bool:
    for sub in ALLOWED_ASSET_SUBSTRINGS.get(retired, []):
        if sub in line and retired in line:
            return True
    return False


def scan(retired: str) -> dict:
    hits: list[str] = []
    for path in SRC.rglob("*"):
        if path.suffix not in {".html", ".scss", ".js"}:
            continue
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if retired not in line:
                continue
            if is_allowed_line(line, retired):
                continue
            if retired == "home-final-form" and re.search(r"img/content/home-final-form", line):
                continue
            hits.append(f"{path.relative_to(ROOT).as_posix()}:{i}")
    return {
        "retired_family": retired,
        "active_references": len(hits),
        "historical_docs": 0,
        "asset_path_exceptions": len(ALLOWED_ASSET_SUBSTRINGS.get(retired, [])),
        "files": hits[:20],
        "result": "PASS" if len(hits) == 0 else "FAIL",
    }


def main() -> None:
    rows = [scan(name) for name in RETIRED]
    payload = {
        "audit_id": "FP-0002-V8-RETIRED-NAMES-AUDIT",
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "src/**/*.html,scss,js",
        "rows": rows,
        "overall": "PASS" if all(r["result"] == "PASS" for r in rows) else "FAIL",
    }
    AUDIT.mkdir(parents=True, exist_ok=True)
    (AUDIT / "FP-0002-V8-RETIRED-NAMES-AUDIT.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"overall": payload["overall"]}, indent=2))


if __name__ == "__main__":
    main()
