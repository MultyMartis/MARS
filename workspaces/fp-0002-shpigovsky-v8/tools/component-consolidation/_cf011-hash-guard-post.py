#!/usr/bin/env python3
"""FP-0002 V8 CF-011 post-implementation protected-source hash guard."""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT.parents[1]
AUDIT = ROOT / "audits" / "cf-011-dark-cta" / "data"
PRE = AUDIT / "cf-011-source-hash-guard-pre.json"

PROTECTED = [
    "src/partials/components/internal-page-nav.html",
    "src/partials/sections/founder-quote.html",
    "src/partials/sections/specialists.html",
    "src/partials/sections/comfort.html",
    "src/partials/sections/reviews.html",
    "src/partials/sections/faq.html",
    "src/partials/sections/final-form.html",
    "src/partials/layout/header.html",
    "src/partials/layout/footer.html",
    "src/partials/components/modal-consultation.html",
    "src/partials/sections/hero.html",
    "src/partials/sections/home-clinic-landscape.html",
    "src/js/main.js",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def git_unchanged(rel: str) -> bool:
    r = subprocess.run(
        ["git", "-C", str(REPO), "diff", "--quiet", "HEAD", "--", f"workspaces/fp-0002-shpigovsky-v8/{rel}"],
        capture_output=True,
    )
    return r.returncode == 0


def main() -> None:
    AUDIT.mkdir(parents=True, exist_ok=True)
    changed = [rel for rel in PROTECTED if not git_unchanged(rel)]
    payload = {
        "validation_id": "cf-011-source-hash-guard-post",
        "protected_changed": changed,
        "protected_changed_count": len(changed),
        "result": "PASS" if not changed else "FAIL",
    }
    (AUDIT / "cf-011-source-hash-guard-post.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
